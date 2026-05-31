import argparse
import json
import os
import random
from typing import Dict, List, Set, Tuple

import numpy as np
import torch
from datasets import load_dataset
from peft import LoraConfig, TaskType, get_peft_model, prepare_model_for_kbit_training
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
    DataCollatorForSeq2Seq,
    Trainer,
    TrainingArguments,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="QLoRA SFT for structured toxicity generation.")
    parser.add_argument("--model-name-or-path", required=True)
    parser.add_argument("--train-file", required=True)
    parser.add_argument("--validation-file", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--max-length", type=int, default=512)
    parser.add_argument("--learning-rate", type=float, default=2e-4)
    parser.add_argument("--num-train-epochs", type=float, default=3.0)
    parser.add_argument("--per-device-train-batch-size", type=int, default=2)
    parser.add_argument("--per-device-eval-batch-size", type=int, default=2)
    parser.add_argument("--gradient-accumulation-steps", type=int, default=8)
    parser.add_argument("--warmup-ratio", type=float, default=0.05)
    parser.add_argument("--weight-decay", type=float, default=0.01)
    parser.add_argument("--logging-steps", type=int, default=20)
    parser.add_argument("--eval-steps", type=int, default=100)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--lora-r", type=int, default=16)
    parser.add_argument("--lora-alpha", type=int, default=32)
    parser.add_argument("--lora-dropout", type=float, default=0.05)
    parser.add_argument("--bf16", action="store_true")
    parser.add_argument("--fp16", action="store_true")
    parser.add_argument("--use-4bit", action="store_true")
    parser.add_argument("--gradient-checkpointing", action="store_true")
    parser.add_argument("--schema-mode", choices=["class_only", "class_target", "full"], default="full")
    return parser.parse_args()


def set_seed(seed: int) -> None:
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)


def _normalize_text(value: str) -> str:
    return " ".join((value or "").strip().split())


def _normalize_hate_class_list(values) -> List[str]:
    if not isinstance(values, list):
        return []

    cleaned = []
    seen: Set[str] = set()
    for value in values:
        if not isinstance(value, str):
            continue
        text = _normalize_text(value)
        if not text:
            continue
        key = text.lower()
        if key in seen:
            continue
        seen.add(key)
        cleaned.append(text)
    return cleaned


def _filter_hate_class_list(values: List[str], allowed_hate_class: List[str]) -> List[str]:
    if not allowed_hate_class:
        return values

    allowed_keys = {item.lower() for item in allowed_hate_class}
    filtered = []
    seen: Set[str] = set()
    for value in values:
        key = value.lower()
        if key in seen:
            continue
        if key not in allowed_keys:
            continue
        seen.add(key)
        filtered.append(value)
    return filtered


def build_allowed_hate_class(dataset) -> List[str]:
    ordered = []
    seen: Set[str] = set()
    for split_name in ["train", "validation"]:
        for row in dataset[split_name]:
            for item in _normalize_hate_class_list(row.get("hate_class", [])):
                key = item.lower()
                if key in seen:
                    continue
                seen.add(key)
                ordered.append(item)
    return ordered


def build_prompt(text: str, schema_mode: str, allowed_hate_class: List[str]) -> str:
    if schema_mode == "class_only":
        return (
            "You are a hate-speech analysis assistant. "
            "Given the text, output ONLY valid JSON with key class.\n"
            "- class must be exactly one of: toxic, non_toxic\n"
            "Do not output any explanation.\n"
            f"Text: {text}\n"
            "JSON:"
        )

    if schema_mode == "class_target":
        return (
            "You are a hate-speech analysis assistant. "
            "Given the text, output ONLY valid JSON with keys class, target.\n"
            "- class must be exactly one of: toxic, non_toxic\n"
            "- target must be a JSON array of strings\n"
            "- If class is non_toxic, use an empty array for target\n"
            "Do not output any explanation.\n"
            f"Text: {text}\n"
            "JSON:"
        )

    allowed_line = ""
    if allowed_hate_class:
        allowed_line = "- hate_class entries must be one of: " + ", ".join(allowed_hate_class) + "\n"

    return (
        "You are a hate-speech analysis assistant. "
        "Given the text, output ONLY valid JSON with keys class, hate_class, target.\n"
        "- class must be exactly one of: toxic, non_toxic\n"
        "- hate_class must be a JSON array of strings\n"
        f"{allowed_line}"
        "- target must be a JSON array of strings\n"
        "- If class is non_toxic, use empty arrays for hate_class and target\n"
        "Do not output any explanation.\n"
        f"Text: {text}\n"
        "JSON:"
    )


def build_target_json(
    label: str,
    hate_class: List[str],
    target: List[str],
    schema_mode: str,
    allowed_hate_class: List[str],
) -> str:
    if schema_mode == "class_only":
        payload = {"class": label}
        return json.dumps(payload, ensure_ascii=False)

    safe_target = target if label == "toxic" else []
    if schema_mode == "class_target":
        payload = {"class": label, "target": safe_target}
        return json.dumps(payload, ensure_ascii=False)

    safe_hate_class = _normalize_hate_class_list(hate_class) if label == "toxic" else []
    safe_hate_class = _filter_hate_class_list(safe_hate_class, allowed_hate_class)
    payload = {
        "class": label,
        "hate_class": safe_hate_class,
        "target": safe_target,
    }
    return json.dumps(payload, ensure_ascii=False)


def load_tokenizer(model_name_or_path: str):
    tokenizer = AutoTokenizer.from_pretrained(model_name_or_path, use_fast=True, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    tokenizer.padding_side = "right"
    return tokenizer


def _encode_example(
    tokenizer,
    text: str,
    label: str,
    hate_class: List[str],
    target: List[str],
    max_length: int,
    schema_mode: str,
    allowed_hate_class: List[str],
) -> Dict[str, List[int]]:
    prompt = build_prompt(text, schema_mode, allowed_hate_class)
    answer = build_target_json(label.strip(), hate_class, target, schema_mode, allowed_hate_class)

    prompt_ids = tokenizer(prompt, add_special_tokens=False)["input_ids"]
    answer_ids = tokenizer(" " + answer, add_special_tokens=False)["input_ids"]
    eos_ids: List[int] = []
    if tokenizer.eos_token_id is not None:
        eos_ids = [tokenizer.eos_token_id]

    input_ids = prompt_ids + answer_ids + eos_ids
    labels = ([-100] * len(prompt_ids)) + answer_ids + eos_ids

    if len(input_ids) > max_length:
        # Keep the tail to preserve the answer supervision when the prompt is too long.
        input_ids = input_ids[-max_length:]
        labels = labels[-max_length:]

    attention_mask = [1] * len(input_ids)
    return {
        "input_ids": input_ids,
        "attention_mask": attention_mask,
        "labels": labels,
    }


def tokenize_datasets(train_file: str, validation_file: str, tokenizer, max_length: int, schema_mode: str):
    dataset = load_dataset("json", data_files={"train": train_file, "validation": validation_file})
    allowed_hate_class = build_allowed_hate_class(dataset)

    def tokenize_fn(example: Dict):
        return _encode_example(
            tokenizer,
            example["text"],
            example["label"],
            example.get("hate_class", []),
            example.get("target", []),
            max_length,
            schema_mode,
            allowed_hate_class,
        )

    columns_to_remove = [
        col
        for col in ["id", "text", "label", "label_id", "hate_class", "target", "source", "split"]
        if col in dataset["train"].column_names
    ]
    dataset = dataset.map(tokenize_fn, remove_columns=columns_to_remove)
    dataset = dataset.filter(lambda x: any(label != -100 for label in x["labels"]))
    dataset.set_format(type="torch")
    return dataset, allowed_hate_class


def build_model(args: argparse.Namespace) -> Tuple[torch.nn.Module, Dict[str, str]]:
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
    set_seed(args.seed)

    tokenizer = load_tokenizer(args.model_name_or_path)
    tokenized, allowed_hate_class = tokenize_datasets(
        args.train_file,
        args.validation_file,
        tokenizer,
        args.max_length,
        args.schema_mode,
    )
    model, trainable = build_model(args)

    trainable_path = os.path.join(args.output_dir, "trainable_params.json")
    with open(trainable_path, "w", encoding="utf-8") as f:
        json.dump(trainable, f, indent=2)

    hate_class_vocab_path = os.path.join(args.output_dir, "hate_class_vocab.json")
    with open(hate_class_vocab_path, "w", encoding="utf-8") as f:
        json.dump({"hate_class": allowed_hate_class}, f, ensure_ascii=False, indent=2)

    data_collator = DataCollatorForSeq2Seq(
        tokenizer=tokenizer,
        model=model,
        padding=True,
        label_pad_token_id=-100,
        return_tensors="pt",
    )

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
        eval_strategy="no",
        save_strategy="no",
        load_best_model_at_end=False,
        bf16=args.bf16,
        fp16=args.fp16,
        gradient_checkpointing=args.gradient_checkpointing,
        report_to="none",
        seed=args.seed,
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized["train"],
        eval_dataset=tokenized["validation"],
        data_collator=data_collator,
    )

    trainer.train()

    trainer.save_model(args.output_dir)
    tokenizer.save_pretrained(args.output_dir)

    print("Training completed. Output dir:", args.output_dir)


if __name__ == "__main__":
    main()
