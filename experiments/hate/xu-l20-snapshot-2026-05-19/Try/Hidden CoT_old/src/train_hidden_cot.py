import argparse
import json
import os
import random
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

import numpy as np
import torch
import torch.nn.functional as F
from datasets import load_dataset
from peft import LoraConfig, TaskType, get_peft_model, prepare_model_for_kbit_training
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
    Trainer,
    TrainingArguments,
)

from common import (
    build_output_text,
    build_prompt,
    build_think_text,
    normalize_hate_classes,
    normalize_targets,
    normalize_class_label,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Train Hidden CoT model with CoT dropout.")
    parser.add_argument("--model-name-or-path", required=True)
    parser.add_argument("--train-file", required=True)
    parser.add_argument("--validation-file", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--max-length", type=int, default=768)
    parser.add_argument("--learning-rate", type=float, default=2e-4)
    parser.add_argument("--num-train-epochs", type=float, default=3.0)
    parser.add_argument("--per-device-train-batch-size", type=int, default=2)
    parser.add_argument("--per-device-eval-batch-size", type=int, default=2)
    parser.add_argument("--gradient-accumulation-steps", type=int, default=8)
    parser.add_argument("--warmup-ratio", type=float, default=0.05)
    parser.add_argument("--weight-decay", type=float, default=0.01)
    parser.add_argument("--logging-steps", type=int, default=20)
    parser.add_argument("--eval-steps", type=int, default=100)
    parser.add_argument("--save-steps", type=int, default=100)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--lora-r", type=int, default=16)
    parser.add_argument("--lora-alpha", type=int, default=32)
    parser.add_argument("--lora-dropout", type=float, default=0.05)
    parser.add_argument("--bf16", action="store_true")
    parser.add_argument("--fp16", action="store_true")
    parser.add_argument("--use-4bit", action="store_true")
    parser.add_argument("--gradient-checkpointing", action="store_true")
    parser.add_argument("--cot-dropout", type=float, default=0.3)
    parser.add_argument("--lambda-class", type=float, default=1.0)
    parser.add_argument("--lambda-hate", type=float, default=1.0)
    parser.add_argument("--lambda-target", type=float, default=0.5)
    parser.add_argument("--align-gamma", type=float, default=0.5)
    parser.add_argument("--norm-mode", type=str, default="minimal", choices=["minimal", "hybrid"])
    return parser.parse_args()


def set_seed(seed: int) -> None:
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)


def _extract_output_lines(output_text: str) -> Tuple[str, str, str, str, str]:
    lines = [x for x in output_text.splitlines() if x.strip()]
    if len(lines) < 5:
        raise ValueError(f"Malformed output block: {output_text}")
    return lines[0] + "\n", lines[1] + "\n", lines[2] + "\n", lines[3] + "\n", lines[4]


def _extract_think_lines(think_text: str) -> List[str]:
    if not think_text:
        return []
    lines = [x for x in think_text.splitlines() if x.strip()]
    if len(lines) < 2:
        return []
    return lines


def _encode_piece(tokenizer, text: str) -> List[int]:
    if not text:
        return []
    return tokenizer(text, add_special_tokens=False)["input_ids"]


def _encode_example(
    tokenizer,
    prompt: str,
    think_text: str,
    output_text: str,
    max_length: int,
    use_think: bool,
    lambda_class: float,
    lambda_hate: float,
    lambda_target: float,
) -> Dict[str, List]:
    out_prefix, class_line, hate_line, target_line, out_suffix = _extract_output_lines(output_text)
    think_lines = _extract_think_lines(think_text)

    pieces: List[Tuple[str, int, float, int]] = []
    pieces.append((prompt, 0, 0.0, 0))
    if use_think:
        if think_lines:
            pieces.append(("\n" + think_lines[0] + "\n", 0, 0.0, 0))
            for ln in think_lines[1:-1]:
                pieces.append((ln + "\n", 0, 0.0, 0))
            pieces.append((think_lines[-1] + "\n", 0, 0.0, 0))
        else:
            pieces.append(("\n" + think_text, 0, 0.0, 0))
    pieces.append(("\n" + out_prefix, 1, 1.0, 0))
    pieces.append((class_line, 1, lambda_class, 0))
    pieces.append((hate_line, 1, lambda_hate, 0))
    pieces.append((target_line, 1, lambda_target, 1))
    pieces.append((out_suffix, 1, 1.0, 0))

    input_ids: List[int] = []
    labels: List[int] = []
    loss_weights: List[float] = []
    target_mask: List[int] = []

    for text, supervised, weight, is_target in pieces:
        ids = _encode_piece(tokenizer, text)
        input_ids.extend(ids)
        if supervised:
            labels.extend(ids)
            loss_weights.extend([float(weight)] * len(ids))
            target_mask.extend([is_target] * len(ids))
        else:
            labels.extend([-100] * len(ids))
            loss_weights.extend([0.0] * len(ids))
            target_mask.extend([0] * len(ids))

    if tokenizer.eos_token_id is not None:
        input_ids.append(tokenizer.eos_token_id)
        labels.append(tokenizer.eos_token_id)
        loss_weights.append(1.0)
        target_mask.append(0)

    if len(input_ids) > max_length:
        input_ids = input_ids[-max_length:]
        labels = labels[-max_length:]
        loss_weights = loss_weights[-max_length:]
        target_mask = target_mask[-max_length:]

    attention_mask = [1] * len(input_ids)
    return {
        "input_ids": input_ids,
        "attention_mask": attention_mask,
        "labels": labels,
        "loss_weights": loss_weights,
        "target_mask": target_mask,
    }


@dataclass
class WeightedDataCollator:
    pad_token_id: int

    def __call__(self, features: List[Dict]) -> Dict[str, torch.Tensor]:
        max_len = max(len(f["input_ids"]) for f in features)
        input_ids = []
        attention_mask = []
        labels = []
        loss_weights = []
        target_mask = []
        hate_multihot = []

        for f in features:
            n = len(f["input_ids"])
            pad_n = max_len - n
            input_ids.append(f["input_ids"].tolist() + [self.pad_token_id] * pad_n)
            attention_mask.append(f["attention_mask"].tolist() + [0] * pad_n)
            labels.append(f["labels"].tolist() + [-100] * pad_n)
            loss_weights.append(f["loss_weights"].tolist() + [0.0] * pad_n)
            target_mask.append(f["target_mask"].tolist() + [0] * pad_n)
            hate_multihot.append(f["hate_multihot"].tolist())

        return {
            "input_ids": torch.tensor(input_ids, dtype=torch.long),
            "attention_mask": torch.tensor(attention_mask, dtype=torch.long),
            "labels": torch.tensor(labels, dtype=torch.long),
            "loss_weights": torch.tensor(loss_weights, dtype=torch.float),
            "target_mask": torch.tensor(target_mask, dtype=torch.long),
            "hate_multihot": torch.tensor(hate_multihot, dtype=torch.float),
        }


class WeightedLossTrainer(Trainer):
    def compute_loss(self, model, inputs, return_outputs=False, num_items_in_batch: Optional[torch.Tensor] = None):
        labels = inputs.pop("labels")
        loss_weights = inputs.pop("loss_weights")
        target_mask = inputs.pop("target_mask", None)
        hate_multihot = inputs.pop("hate_multihot", None)

        outputs = model(**inputs, output_hidden_states=True)
        logits = outputs.logits

        shift_logits = logits[..., :-1, :].contiguous()
        shift_labels = labels[..., 1:].contiguous()
        shift_weights = loss_weights[..., 1:].contiguous()

        per_token_loss = F.cross_entropy(
            shift_logits.view(-1, shift_logits.size(-1)),
            shift_labels.view(-1),
            reduction="none",
            ignore_index=-100,
        ).view(shift_labels.shape)

        mask = (shift_labels != -100).float()
        weighted_loss = per_token_loss * shift_weights * mask
        denom = (shift_weights * mask).sum().clamp(min=1e-8)
        ce_loss = weighted_loss.sum() / denom

        align_loss = torch.tensor(0.0, device=ce_loss.device)
        align_gamma = float(getattr(self, "align_gamma", 0.0))
        hate_label_embeddings = getattr(self, "hate_label_embeddings", None)
        if (
            align_gamma > 0.0
            and target_mask is not None
            and hate_multihot is not None
            and hate_label_embeddings is not None
            and hate_label_embeddings.numel() > 0
        ):
            hidden = outputs.hidden_states[-1]
            attn = inputs["attention_mask"].float()
            tmask = target_mask.float() * attn
            label_embs = hate_label_embeddings.to(device=hidden.device, dtype=hidden.dtype)
            sample_losses = []
            for i in range(hidden.size(0)):
                tm = tmask[i]
                hm = hate_multihot[i]
                if tm.sum() <= 0 or hm.sum() <= 0:
                    continue
                h_t = (hidden[i] * tm.unsqueeze(-1)).sum(dim=0) / tm.sum()
                h_c = (hm.unsqueeze(-1) * label_embs).sum(dim=0) / hm.sum()
                cos = F.cosine_similarity(h_t.unsqueeze(0), h_c.unsqueeze(0), dim=-1)
                sample_losses.append(1.0 - cos.squeeze(0))
            if sample_losses:
                align_loss = torch.stack(sample_losses).mean()

        loss = ce_loss + align_gamma * align_loss

        if return_outputs:
            return loss, outputs
        return loss


def load_tokenizer(model_name_or_path: str):
    tokenizer = AutoTokenizer.from_pretrained(model_name_or_path, use_fast=True, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    tokenizer.padding_side = "right"
    return tokenizer


def tokenize_datasets(args: argparse.Namespace, tokenizer):
    dataset = load_dataset("json", data_files={"train": args.train_file, "validation": args.validation_file})
    rng = random.Random(args.seed)

    hate_label_set = set()
    for split in ["train", "validation"]:
        for row in dataset[split]:
            for x in normalize_hate_classes(row.get("hate_class", []), norm_mode=args.norm_mode):
                hate_label_set.add(x)
    hate_labels = sorted(hate_label_set)
    hate_to_idx = {x: i for i, x in enumerate(hate_labels)}

    def tokenize_fn(example: Dict[str, str]):
        text = str(example.get("post", example.get("text", ""))).strip()
        if not text:
            raise ValueError("Each sample must contain non-empty 'post' (or 'text').")

        class_label = normalize_class_label(str(example.get("class", "not_toxic")))
        hate_classes = normalize_hate_classes(example.get("hate_class", []), norm_mode=args.norm_mode)
        targets = normalize_targets(example.get("target", []), norm_mode=args.norm_mode)

        prompt = build_prompt(text)
        think_text = build_think_text(hate_classes, targets)
        output_text = build_output_text(class_label, hate_classes, targets)

        use_think = rng.random() >= args.cot_dropout
        encoded = _encode_example(
            tokenizer=tokenizer,
            prompt=prompt,
            think_text=think_text,
            output_text=output_text,
            max_length=args.max_length,
            use_think=use_think,
            lambda_class=args.lambda_class,
            lambda_hate=args.lambda_hate,
            lambda_target=args.lambda_target,
        )
        multi_hot = [0] * len(hate_labels)
        for h in set(hate_classes):
            if h in hate_to_idx:
                multi_hot[hate_to_idx[h]] = 1
        encoded["hate_multihot"] = multi_hot
        return encoded

    remove_columns = dataset["train"].column_names
    tokenized = dataset.map(tokenize_fn, remove_columns=remove_columns)
    tokenized = tokenized.filter(lambda x: any(y != -100 for y in x["labels"]))
    tokenized.set_format(type="torch")
    return tokenized, hate_labels


def build_hate_label_embeddings(model, tokenizer, hate_labels: List[str]) -> torch.Tensor:
    if not hate_labels:
        hidden_size = int(getattr(model.config, "hidden_size", 1))
        return torch.zeros((0, hidden_size), dtype=torch.float)

    emb = model.get_input_embeddings()
    device = emb.weight.device
    out = []
    with torch.no_grad():
        for label in hate_labels:
            text = label.replace("_", " ")
            ids = tokenizer(text, add_special_tokens=False, return_tensors="pt")["input_ids"].squeeze(0)
            if ids.numel() == 0:
                vec = torch.zeros((emb.embedding_dim,), device=device, dtype=emb.weight.dtype)
            else:
                vec = emb(ids.to(device)).mean(dim=0)
            out.append(vec.detach().to(dtype=torch.float, device="cpu"))
    return torch.stack(out, dim=0)


def build_training_loss_curve(log_history: List[Dict]) -> Dict[str, List[Dict[str, float]]]:
    train_points: List[Dict[str, float]] = []
    eval_points: List[Dict[str, float]] = []
    lr_points: List[Dict[str, float]] = []

    for item in log_history:
        step = float(item.get("step", 0))
        epoch = float(item.get("epoch", 0.0))

        if "loss" in item:
            train_points.append(
                {
                    "step": step,
                    "epoch": epoch,
                    "loss": float(item["loss"]),
                }
            )

        if "eval_loss" in item:
            eval_points.append(
                {
                    "step": step,
                    "epoch": epoch,
                    "eval_loss": float(item["eval_loss"]),
                }
            )

        if "learning_rate" in item:
            lr_points.append(
                {
                    "step": step,
                    "epoch": epoch,
                    "learning_rate": float(item["learning_rate"]),
                }
            )

    return {
        "train_loss": train_points,
        "eval_loss": eval_points,
        "learning_rate": lr_points,
    }


def save_training_loss_plot(loss_curve: Dict[str, List[Dict[str, float]]], output_path: str) -> None:
    train_points = loss_curve.get("train_loss", [])
    eval_points = loss_curve.get("eval_loss", [])
    if not train_points and not eval_points:
        return

    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(8, 5))

    if train_points:
        ax.plot(
            [p["step"] for p in train_points],
            [p["loss"] for p in train_points],
            label="train_loss",
            linewidth=1.8,
        )

    if eval_points:
        ax.plot(
            [p["step"] for p in eval_points],
            [p["eval_loss"] for p in eval_points],
            label="eval_loss",
            linewidth=1.8,
        )

    ax.set_xlabel("Step")
    ax.set_ylabel("Loss")
    ax.set_title("Training Loss Curve")
    ax.grid(True, alpha=0.3)
    ax.legend()
    fig.tight_layout()
    fig.savefig(output_path, dpi=200)
    plt.close(fig)


def build_model(args: argparse.Namespace):
    quantization_config = None
    if args.use_4bit:
        quantization_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=torch.bfloat16 if args.bf16 else torch.float16,
            bnb_4bit_use_double_quant=True,
        )

    model = AutoModelForCausalLM.from_pretrained(
        args.model_name_or_path,
        trust_remote_code=True,
        quantization_config=quantization_config,
        torch_dtype=torch.bfloat16 if args.bf16 else (torch.float16 if args.fp16 else None),
        device_map="auto",
    )

    if args.use_4bit:
        model = prepare_model_for_kbit_training(model)

    target_modules = ["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"]
    lora_config = LoraConfig(
        r=args.lora_r,
        lora_alpha=args.lora_alpha,
        lora_dropout=args.lora_dropout,
        bias="none",
        task_type=TaskType.CAUSAL_LM,
        target_modules=target_modules,
    )
    model = get_peft_model(model, lora_config)

    trainable = {
        "trainable_parameters": str(sum(p.numel() for p in model.parameters() if p.requires_grad)),
        "all_parameters": str(sum(p.numel() for p in model.parameters())),
    }
    return model, trainable


def main() -> None:
    args = parse_args()
    os.makedirs(args.output_dir, exist_ok=True)
    metrics_dir = os.path.join(args.output_dir, "metrics")
    plots_dir = os.path.join(args.output_dir, "plots")
    os.makedirs(metrics_dir, exist_ok=True)
    os.makedirs(plots_dir, exist_ok=True)
    set_seed(args.seed)

    tokenizer = load_tokenizer(args.model_name_or_path)
    tokenized, hate_labels = tokenize_datasets(args, tokenizer)
    model, trainable = build_model(args)
    hate_label_embeddings = build_hate_label_embeddings(model, tokenizer, hate_labels)

    with open(os.path.join(args.output_dir, "trainable_params.json"), "w", encoding="utf-8") as f:
        json.dump(trainable, f, indent=2)

    with open(os.path.join(args.output_dir, "train_config.json"), "w", encoding="utf-8") as f:
        json.dump(vars(args), f, indent=2)

    data_collator = WeightedDataCollator(pad_token_id=tokenizer.pad_token_id)

    training_args = TrainingArguments(
        output_dir=args.output_dir,
        learning_rate=args.learning_rate,
        num_train_epochs=args.num_train_epochs,
        per_device_train_batch_size=args.per_device_train_batch_size,
        per_device_eval_batch_size=args.per_device_eval_batch_size,
        gradient_accumulation_steps=args.gradient_accumulation_steps,
        warmup_ratio=args.warmup_ratio,
        weight_decay=args.weight_decay,
        logging_steps=args.logging_steps,
        eval_strategy="steps",
        eval_steps=args.eval_steps,
        save_strategy="steps",
        save_steps=args.save_steps,
        save_total_limit=1,
        load_best_model_at_end=True,
        metric_for_best_model="eval_loss",
        greater_is_better=False,
        bf16=args.bf16,
        fp16=args.fp16,
        gradient_checkpointing=args.gradient_checkpointing,
        report_to="none",
        seed=args.seed,
        remove_unused_columns=False,
    )

    trainer = WeightedLossTrainer(
        model=model,
        args=training_args,
        train_dataset=tokenized["train"],
        eval_dataset=tokenized["validation"],
        data_collator=data_collator,
    )
    trainer.align_gamma = args.align_gamma
    trainer.hate_label_embeddings = hate_label_embeddings

    train_result = trainer.train()
    metrics = trainer.evaluate()

    with open(os.path.join(metrics_dir, "train_metrics.json"), "w", encoding="utf-8") as f:
        json.dump(train_result.metrics, f, indent=2)

    loss_curve = build_training_loss_curve(trainer.state.log_history)
    with open(os.path.join(metrics_dir, "training_loss_curve.json"), "w", encoding="utf-8") as f:
        json.dump(loss_curve, f, indent=2)
    save_training_loss_plot(loss_curve, os.path.join(plots_dir, "training_loss_curve.png"))

    with open(os.path.join(metrics_dir, "validation_metrics.json"), "w", encoding="utf-8") as f:
        json.dump(metrics, f, indent=2)

    trainer.save_model(args.output_dir)
    tokenizer.save_pretrained(args.output_dir)

    print("Training completed. Output dir:", args.output_dir)


if __name__ == "__main__":
    main()
