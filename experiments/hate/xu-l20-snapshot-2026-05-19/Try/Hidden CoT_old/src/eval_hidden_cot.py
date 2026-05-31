import argparse
import json
import os
import time
from typing import Dict, List

import torch
from datasets import load_dataset
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

from common import (
    build_prompt,
    normalize_class_label,
    normalize_hate_classes,
    normalize_targets,
    parse_output_text,
)
from metrics import (
    compute_class_metrics,
    compute_multilabel_metrics,
    embedding_cosine_for_sets,
    f1_for_sets,
    jaccard_for_sets,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Evaluate Hidden CoT model on IHC test set.")
    parser.add_argument("--base-model", required=True)
    parser.add_argument("--adapter-path", required=True)
    parser.add_argument("--test-file", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--eval-output-dir", default="")
    parser.add_argument("--max-length", type=int, default=768)
    parser.add_argument("--max-new-tokens", type=int, default=128)
    parser.add_argument("--eval-batch-size", type=int, default=8)
    parser.add_argument("--norm-mode", type=str, default="minimal", choices=["minimal", "hybrid"])
    parser.add_argument("--bf16", action="store_true")
    parser.add_argument("--fp16", action="store_true")
    parser.add_argument("--use-4bit", action="store_true")
    return parser.parse_args()


def build_model(args: argparse.Namespace):
    quantization_config = None
    if args.use_4bit:
        quantization_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=torch.bfloat16 if args.bf16 else torch.float16,
            bnb_4bit_use_double_quant=True,
        )

    base = AutoModelForCausalLM.from_pretrained(
        args.base_model,
        trust_remote_code=True,
        quantization_config=quantization_config,
        torch_dtype=torch.bfloat16 if args.bf16 else (torch.float16 if args.fp16 else None),
        device_map="auto",
    )
    model = PeftModel.from_pretrained(base, args.adapter_path)
    model.eval()
    return model


def generate_outputs_batch(
    model,
    tokenizer,
    prompts: List[str],
    max_length: int,
    max_new_tokens: int,
    batch_size: int,
) -> List[str]:
    if batch_size <= 0:
        raise ValueError("eval_batch_size must be > 0")

    all_generated: List[str] = []
    for i in range(0, len(prompts), batch_size):
        batch_prompts = prompts[i : i + batch_size]
        inputs = tokenizer(
            batch_prompts,
            return_tensors="pt",
            truncation=True,
            max_length=max_length,
            padding=True,
        )
        inputs = {k: v.to(model.device) for k, v in inputs.items()}

        with torch.no_grad():
            out = model.generate(
                **inputs,
                do_sample=False,
                max_new_tokens=max_new_tokens,
                pad_token_id=tokenizer.pad_token_id,
                eos_token_id=tokenizer.eos_token_id,
            )

        prompt_len = inputs["input_ids"].shape[1]
        for row in out:
            new_tokens = row[prompt_len:]
            all_generated.append(tokenizer.decode(new_tokens, skip_special_tokens=True).strip())

    return all_generated


def compute_multilabel_per_label_metrics(
    y_true: List[List[str]],
    y_pred: List[List[str]],
) -> Dict[str, Dict[str, float]]:
    labels = sorted({x for row in y_true for x in row} | {x for row in y_pred for x in row})
    out: Dict[str, Dict[str, float]] = {}
    for label in labels:
        tp = 0
        fp = 0
        fn = 0
        support = 0
        pred_count = 0
        for g_row, p_row in zip(y_true, y_pred):
            g = set(g_row)
            p = set(p_row)
            has_g = label in g
            has_p = label in p
            if has_g:
                support += 1
            if has_p:
                pred_count += 1
            if has_g and has_p:
                tp += 1
            elif has_p and not has_g:
                fp += 1
            elif has_g and not has_p:
                fn += 1

        precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
        recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
        f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0.0

        out[label] = {
            "precision": float(precision),
            "recall": float(recall),
            "f1": float(f1),
            "support": float(support),
            "pred_count": float(pred_count),
            "tp": float(tp),
            "fp": float(fp),
            "fn": float(fn),
        }
    return out


def main() -> None:
    args = parse_args()
    os.makedirs(args.output_dir, exist_ok=True)
    eval_output_dir = args.eval_output_dir or os.path.join(args.output_dir, "eval")
    os.makedirs(eval_output_dir, exist_ok=True)

    tokenizer = AutoTokenizer.from_pretrained(args.adapter_path, use_fast=True, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    tokenizer.padding_side = "left"

    dataset = load_dataset("json", data_files={"test": args.test_file})["test"]
    model = build_model(args)
    eval_start = time.time()

    y_class_true: List[str] = []
    y_class_pred: List[str] = []
    y_hate_true: List[List[str]] = []
    y_hate_pred: List[List[str]] = []
    y_target_true: List[List[str]] = []
    y_target_pred: List[List[str]] = []

    prediction_rows: List[Dict] = []

    rows = [row for row in dataset]
    texts = [str(row.get("post", row.get("text", ""))).strip() for row in rows]
    if any(not t for t in texts):
        raise ValueError("Each test sample must contain non-empty 'post' (or 'text').")
    prompts = [build_prompt(t) for t in texts]
    generated_list = generate_outputs_batch(
        model=model,
        tokenizer=tokenizer,
        prompts=prompts,
        max_length=args.max_length,
        max_new_tokens=args.max_new_tokens,
        batch_size=args.eval_batch_size,
    )

    for row, text, generated in zip(rows, texts, generated_list):
        parsed = parse_output_text(generated, norm_mode=args.norm_mode)

        gt_class = normalize_class_label(str(row.get("class", "not_toxic")))
        gt_hate = normalize_hate_classes(row.get("hate_class", []), norm_mode=args.norm_mode)
        gt_target = normalize_targets(row.get("target", []), norm_mode=args.norm_mode)

        pred_class = parsed["class"]
        pred_hate = parsed["hate_class"]
        pred_target = parsed["target"]

        y_class_true.append(gt_class)
        y_class_pred.append(pred_class)
        y_hate_true.append(gt_hate)
        y_hate_pred.append(pred_hate)
        y_target_true.append(gt_target)
        y_target_pred.append(pred_target)

        prediction_rows.append(
            {
                "id": row["id"],
                "text": text,
                "gold": {
                    "class": gt_class,
                    "hate_class": gt_hate,
                    "target": gt_target,
                },
                "pred": {
                    "class": pred_class,
                    "hate_class": pred_hate,
                    "target": pred_target,
                },
                "generated_text": generated,
            }
        )

    class_metrics = compute_class_metrics(y_class_true, y_class_pred)
    hate_metrics = compute_multilabel_metrics(y_hate_true, y_hate_pred)
    hate_per_label = compute_multilabel_per_label_metrics(y_hate_true, y_hate_pred)
    target_metrics = {
        "set_jaccard": jaccard_for_sets(y_target_true, y_target_pred),
        "set_f1": f1_for_sets(y_target_true, y_target_pred),
        "embedding_cosine": embedding_cosine_for_sets(y_target_true, y_target_pred),
    }

    predictions_file = os.path.join(eval_output_dir, "test_predictions.jsonl")
    with open(predictions_file, "w", encoding="utf-8") as f:
        for out in prediction_rows:
            f.write(json.dumps(out, ensure_ascii=False) + "\n")

    metrics_file = os.path.join(eval_output_dir, "test_metrics.json")
    eval_runtime = time.time() - eval_start
    with open(metrics_file, "w", encoding="utf-8") as f:
        json.dump(
            {
                "class": class_metrics,
                "hate_class": {
                    **hate_metrics,
                    "per_label": hate_per_label,
                },
                "target": target_metrics,
                "eval": {
                    "num_samples": len(rows),
                    "eval_runtime_sec": eval_runtime,
                    "eval_samples_per_sec": (len(rows) / eval_runtime) if eval_runtime > 0 else 0.0,
                },
            },
            f,
            indent=2,
            ensure_ascii=False,
        )

    print("Saved metrics:", metrics_file)
    print("Saved predictions:", predictions_file)


if __name__ == "__main__":
    main()
