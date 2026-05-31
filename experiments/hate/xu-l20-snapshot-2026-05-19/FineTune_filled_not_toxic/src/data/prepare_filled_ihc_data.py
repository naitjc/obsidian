import argparse
import json
import os
from collections import Counter
from typing import Dict, List


LABEL_TO_ID: Dict[str, int] = {
    "toxic": 1,
    "non_toxic": 0,
}

LABEL_MAP: Dict[str, str] = {
    "toxic": "toxic",
    "not_toxic": "non_toxic",
    "non_toxic": "non_toxic",
}


def clean_text(text: str) -> str:
    return " ".join((text or "").replace("\u00a0", " ").strip().split())


def clean_string_list(values) -> List[str]:
    if not isinstance(values, list):
        return []
    cleaned = []
    seen = set()
    for value in values:
        if not isinstance(value, str):
            continue
        item = clean_text(value)
        key = item.lower()
        if not item or key in seen:
            continue
        seen.add(key)
        cleaned.append(item)
    return cleaned


def normalize_label(raw_label: str) -> str:
    return LABEL_MAP.get((raw_label or "").strip(), "")


def convert_file(input_path: str, output_path: str, split: str) -> Dict[str, int]:
    with open(input_path, "r", encoding="utf-8") as f:
        rows = json.load(f)
    if not isinstance(rows, list):
        raise ValueError(f"Expected list in {input_path}")

    stats = Counter()
    with open(output_path, "w", encoding="utf-8") as f:
        for idx, row in enumerate(rows):
            if not isinstance(row, dict):
                continue
            text = clean_text(row.get("post", ""))
            label = normalize_label(row.get("class", ""))
            if not text or label not in LABEL_TO_ID:
                continue
            target = clean_string_list(row.get("target", []))
            hate_class = clean_string_list(row.get("hate_class", []))
            out = {
                "id": str(row.get("id") or f"IHC_{split}_{idx}"),
                "text": text,
                "label": label,
                "label_id": LABEL_TO_ID[label],
                "hate_class": hate_class,
                "target": target,
                "source": "IHC_filled_not_toxic",
                "split": split,
            }
            f.write(json.dumps(out, ensure_ascii=False) + "\n")
            stats["total"] += 1
            stats[label] += 1
            if target:
                stats[f"{label}_with_target"] += 1
    return dict(stats)


def main() -> None:
    parser = argparse.ArgumentParser(description="Prepare llm_target_filled IHC JSON files for target-input class-only SFT.")
    parser.add_argument("--input-dir", default="/data/chenjt/hate/DATA/llm_target_filled/IHC/processed")
    parser.add_argument("--output-dir", default="data/processed/ihc_filled")
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)
    mapping = {
        "train": "train.json",
        "validation": "valid.json",
        "test": "test.json",
    }
    stats = {}
    for split, filename in mapping.items():
        input_path = os.path.join(args.input_dir, filename)
        output_path = os.path.join(args.output_dir, f"{split}.jsonl")
        stats[split] = convert_file(input_path, output_path, split)

    with open(os.path.join(args.output_dir, "stats.json"), "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)
    with open(os.path.join(args.output_dir, "label_map.json"), "w", encoding="utf-8") as f:
        json.dump(LABEL_TO_ID, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
