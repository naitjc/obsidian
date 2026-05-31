import argparse
import json
import math
import os
from collections import defaultdict
from typing import Dict, List, Set, Tuple

import numpy as np
import torch
from datasets import load_dataset
from peft import PeftModel
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score, precision_recall_fscore_support
from transformers import AutoModelForCausalLM, AutoTokenizer


LABEL_TO_ID = {"non_toxic": 0, "toxic": 1}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Evaluate generative LoRA model on binary toxicity test set.")
    parser.add_argument("--base-model", required=True)
    parser.add_argument("--adapter-path", required=True)
    parser.add_argument("--test-file", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--max-length", type=int, default=512)
    parser.add_argument("--max-new-tokens", type=int, default=4)
    parser.add_argument("--bf16", action="store_true")
    parser.add_argument("--fp16", action="store_true")
    parser.add_argument("--schema-mode", choices=["class_only", "class_target", "full"], default="full")
    return parser.parse_args()


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


def load_allowed_hate_class(adapter_path: str) -> List[str]:
    vocab_path = os.path.join(adapter_path, "hate_class_vocab.json")
    if not os.path.isfile(vocab_path):
        return []

    with open(vocab_path, "r", encoding="utf-8") as f:
        payload = json.load(f)

    if not isinstance(payload, dict):
        return []
    return _normalize_hate_class_list(payload.get("hate_class", []))


def filter_hate_class_list(values: List[str], allowed_hate_class: List[str]) -> List[str]:
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


def build_model(args: argparse.Namespace):
    base = AutoModelForCausalLM.from_pretrained(
        args.base_model,
        trust_remote_code=True,
        torch_dtype=torch.bfloat16 if args.bf16 else (torch.float16 if args.fp16 else None),
        device_map="auto",
    )
    model = PeftModel.from_pretrained(base, args.adapter_path)
    model.eval()
    return model


def normalize_label_text(text: str) -> str:
    norm = (text or "").strip().lower()
    norm = norm.replace("-", "_").replace(" ", "")
    if norm.startswith("non_toxic") or norm.startswith("nontoxic"):
        return "non_toxic"
    if norm.startswith("toxic"):
        return "toxic"
    return ""


def _normalize_string_list(values) -> List[str]:
    return _normalize_hate_class_list(values)


def parse_generated_json(text: str, allowed_hate_class: List[str]) -> Dict:
    output = {
        "class": "",
        "hate_class": [],
        "target": [],
    }

    raw = (text or "").strip()
    if not raw:
        return output

    start = raw.find("{")
    end = raw.rfind("}")
    if start == -1 or end == -1 or start > end:
        output["class"] = normalize_label_text(raw)
        return output

    json_chunk = raw[start : end + 1]
    try:
        payload = json.loads(json_chunk)
    except json.JSONDecodeError:
        output["class"] = normalize_label_text(raw)
        return output

    if not isinstance(payload, dict):
        return output

    output["class"] = normalize_label_text(str(payload.get("class", "")))
    output["hate_class"] = _normalize_string_list(payload.get("hate_class", []))
    output["hate_class"] = filter_hate_class_list(output["hate_class"], allowed_hate_class)
    output["target"] = _normalize_string_list(payload.get("target", []))
    if output["class"] == "non_toxic":
        output["hate_class"] = []
        output["target"] = []
    return output


def _candidate_logprob(
    model,
    tokenizer,
    prompt: str,
    candidate_label: str,
    max_length: int,
) -> float:
    prompt_ids = tokenizer(prompt, add_special_tokens=False)["input_ids"]
    candidate_ids = tokenizer(" " + candidate_label, add_special_tokens=False)["input_ids"]

    eos_ids: List[int] = []
    if tokenizer.eos_token_id is not None:
        eos_ids = [tokenizer.eos_token_id]

    input_ids = prompt_ids + candidate_ids + eos_ids
    if len(input_ids) > max_length:
        overflow = len(input_ids) - max_length
        if overflow < len(prompt_ids):
            prompt_ids = prompt_ids[overflow:]
        else:
            prompt_ids = []
        input_ids = prompt_ids + candidate_ids + eos_ids

    if len(prompt_ids) == 0:
        return -1e9

    input_tensor = torch.tensor([input_ids], device=model.device)
    with torch.no_grad():
        logits = model(input_ids=input_tensor).logits[0]

    log_probs = torch.log_softmax(logits, dim=-1)
    score = 0.0

    target_tokens = candidate_ids + eos_ids
    for idx, token_id in enumerate(target_tokens):
        token_pos = len(prompt_ids) + idx
        pred_pos = token_pos - 1
        if pred_pos < 0 or pred_pos >= log_probs.shape[0]:
            return -1e9
        score += float(log_probs[pred_pos, token_id].item())
    return score


def score_labels(model, tokenizer, prompt: str, max_length: int) -> Tuple[float, float]:
    toxic_logp = _candidate_logprob(model, tokenizer, prompt, "toxic", max_length)
    non_toxic_logp = _candidate_logprob(model, tokenizer, prompt, "non_toxic", max_length)

    max_logp = max(toxic_logp, non_toxic_logp)
    toxic_p = math.exp(toxic_logp - max_logp)
    non_toxic_p = math.exp(non_toxic_logp - max_logp)
    denom = toxic_p + non_toxic_p + 1e-12
    return toxic_p / denom, non_toxic_p / denom


def generate_label(model, tokenizer, prompt: str, max_length: int, max_new_tokens: int) -> str:
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=max_length)
    inputs = {k: v.to(model.device) for k, v in inputs.items()}

    with torch.no_grad():
        out = model.generate(
            **inputs,
            do_sample=False,
            max_new_tokens=max_new_tokens,
            pad_token_id=tokenizer.pad_token_id,
            eos_token_id=tokenizer.eos_token_id,
        )

    new_tokens = out[0][inputs["input_ids"].shape[1] :]
    return tokenizer.decode(new_tokens, skip_special_tokens=True).strip()


def compute_metrics(labels: List[int], preds: List[int]) -> Dict[str, float]:
    precision, recall, f1, _ = precision_recall_fscore_support(labels, preds, average="binary", zero_division=0)
    macro_f1 = f1_score(labels, preds, average="macro")
    acc = accuracy_score(labels, preds)
    return {
        "accuracy": float(acc),
        "precision": float(precision),
        "recall": float(recall),
        "f1": float(f1),
        "macro_f1": float(macro_f1),
    }


def jaccard_for_targets(gold_targets: List[str], pred_targets: List[str]) -> float:
    gold_set = {item for item in gold_targets}
    pred_set = {item for item in pred_targets}
    union = gold_set | pred_set
    if not union:
        return 1.0
    intersection = gold_set & pred_set
    return float(len(intersection) / len(union))


def main() -> None:
    args = parse_args()
    os.makedirs(args.output_dir, exist_ok=True)

    tokenizer = AutoTokenizer.from_pretrained(args.adapter_path, use_fast=True, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    dataset = load_dataset("json", data_files={"test": args.test_file})["test"]
    allowed_hate_class = load_allowed_hate_class(args.adapter_path)
    model = build_model(args)

    all_labels: List[int] = []
    all_preds: List[int] = []
    prediction_rows: List[Dict] = []
    target_jaccard_values: List[float] = []
    target_jaccard_by_source = defaultdict(list)

    for row in dataset:
        prompt = build_prompt(row["text"], args.schema_mode, allowed_hate_class)
        generated = generate_label(model, tokenizer, prompt, args.max_length, args.max_new_tokens)
        parsed = parse_generated_json(generated, allowed_hate_class)
        normalized = parsed["class"]
        prob_toxic, prob_non_toxic = score_labels(model, tokenizer, prompt, args.max_length)

        if normalized in LABEL_TO_ID:
            pred_id = LABEL_TO_ID[normalized]
        else:
            pred_id = 1 if prob_toxic >= prob_non_toxic else 0

        all_labels.append(int(row["label_id"]))
        all_preds.append(int(pred_id))

        row_target_jaccard = None
        if int(row["label_id"]) == 1:
            row_target_jaccard = jaccard_for_targets(row.get("target", []), parsed["target"])
            target_jaccard_values.append(row_target_jaccard)
            target_jaccard_by_source[row["source"]].append(row_target_jaccard)

        prediction_rows.append(
            {
                "id": row["id"],
                "text": row["text"],
                "source": row["source"],
                "label": row["label"],
                "label_id": int(row["label_id"]),
                "gold_hate_class": row.get("hate_class", []),
                "gold_target": row.get("target", []),
                "pred_id": int(pred_id),
                "pred_label": "toxic" if pred_id == 1 else "non_toxic",
                "generated_text": generated,
                "generated_class": parsed["class"],
                "generated_hate_class": parsed["hate_class"],
                "generated_target": parsed["target"],
                "prob_non_toxic": float(prob_non_toxic),
                "prob_toxic": float(prob_toxic),
                "target_jaccard": row_target_jaccard,
            }
        )

    metrics_all = compute_metrics(all_labels, all_preds)
    cm = confusion_matrix(all_labels, all_preds, labels=[0, 1]).tolist()

    by_source_indices = defaultdict(list)
    for idx, row in enumerate(dataset):
        by_source_indices[row["source"]].append(idx)

    by_source_metrics = {}
    for source, indices in by_source_indices.items():
        src_labels = [all_labels[i] for i in indices]
        src_preds = [all_preds[i] for i in indices]
        by_source_metrics[source] = compute_metrics(src_labels, src_preds)

    target_jaccard_mean = float(sum(target_jaccard_values) / len(target_jaccard_values)) if target_jaccard_values else 0.0
    target_jaccard_by_source_mean = {
        source: float(sum(values) / len(values)) if values else 0.0
        for source, values in target_jaccard_by_source.items()
    }

    predictions_file = os.path.join(args.output_dir, "test_predictions.jsonl")
    with open(predictions_file, "w", encoding="utf-8") as f:
        for out in prediction_rows:
            f.write(json.dumps(out, ensure_ascii=False) + "\n")

    metrics_file = os.path.join(args.output_dir, "test_metrics.json")
    with open(metrics_file, "w", encoding="utf-8") as f:
        json.dump(
            {
                "overall": metrics_all,
                "target_jaccard_toxic_only": target_jaccard_mean,
                "confusion_matrix_label_order": ["non_toxic", "toxic"],
                "confusion_matrix": cm,
                "by_source": by_source_metrics,
                "target_jaccard_toxic_only_by_source": target_jaccard_by_source_mean,
            },
            f,
            indent=2,
            ensure_ascii=False,
        )

    print("Saved metrics:", metrics_file)
    print("Saved predictions:", predictions_file)


if __name__ == "__main__":
    main()
