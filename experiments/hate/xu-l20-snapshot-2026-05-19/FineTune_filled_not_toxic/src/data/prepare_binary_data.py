import argparse
import json
import os
import random
from dataclasses import dataclass
from typing import Dict, Iterable, List, Sequence, Tuple


LABEL_TO_ID: Dict[str, int] = {
    "toxic": 1,
    "non_toxic": 0,
}

LABEL_MAP: Dict[str, str] = {
    "implicit_hate": "toxic",
    "not_hate": "non_toxic",
    "offensive": "toxic",
    "not_offensive": "non_toxic",
    "toxic": "toxic",
    "non_toxic": "non_toxic",
    "not_toxic": "non_toxic",
}


@dataclass
class Example:
    id: str
    text: str
    label: str
    label_id: int
    hate_class: List[str]
    target: List[str]
    source: str
    split: str


def clean_text(text: str) -> str:
    cleaned = (text or "").replace("\u00a0", " ").strip()
    cleaned = " ".join(cleaned.split())
    return cleaned


def clean_string_list(values) -> List[str]:
    if not isinstance(values, list):
        return []

    items = []
    seen = set()
    for value in values:
        if not isinstance(value, str):
            continue
        text = clean_text(value)
        if not text:
            continue
        key = text.lower()
        if key in seen:
            continue
        seen.add(key)
        items.append(text)
    return items


def normalize_label(raw_label: str) -> str:
    return LABEL_MAP.get((raw_label or "").strip(), "")


def read_pure_json(file_path: str, split: str, source: str) -> List[Example]:
    rows: List[Example] = []
    with open(file_path, "r", encoding="utf-8") as f:
        raw_rows = json.load(f)

    if not isinstance(raw_rows, list):
        return rows

    for idx, row in enumerate(raw_rows):
        if not isinstance(row, dict):
            continue
        post = clean_text(row.get("post", ""))
        label = normalize_label(row.get("class", ""))
        if not post or label not in LABEL_TO_ID:
            continue

        row_id = str(row.get("id") or f"{source}_{split}_{idx}")
        rows.append(
            Example(
                id=row_id,
                text=post,
                label=label,
                label_id=LABEL_TO_ID[label],
                hate_class=clean_string_list(row.get("hate_class", [])),
                target=clean_string_list(row.get("target", [])),
                source=source,
                split=split,
            )
        )
    return rows


def stratified_split(
    rows: Sequence[Example],
    train_ratio: float,
    validation_ratio: float,
    seed: int,
) -> Tuple[List[Example], List[Example], List[Example]]:
    toxic = [row for row in rows if row.label == "toxic"]
    non_toxic = [row for row in rows if row.label == "non_toxic"]

    rng = random.Random(seed)
    rng.shuffle(toxic)
    rng.shuffle(non_toxic)

    def split_bucket(bucket: List[Example]) -> Tuple[List[Example], List[Example], List[Example]]:
        total = len(bucket)
        n_train = int(total * train_ratio)
        n_validation = int(total * validation_ratio)
        n_test = total - n_train - n_validation

        if total >= 3:
            n_train = max(1, n_train)
            n_validation = max(1, n_validation)
            n_test = total - n_train - n_validation
            if n_test <= 0:
                n_test = 1
                if n_train >= n_validation and n_train > 1:
                    n_train -= 1
                elif n_validation > 1:
                    n_validation -= 1
                else:
                    n_train = max(1, n_train - 1)

        train_rows = bucket[:n_train]
        validation_rows = bucket[n_train : n_train + n_validation]
        test_rows = bucket[n_train + n_validation : n_train + n_validation + n_test]
        return train_rows, validation_rows, test_rows

    train_t, val_t, test_t = split_bucket(toxic)
    train_n, val_n, test_n = split_bucket(non_toxic)

    train_rows = train_t + train_n
    validation_rows = val_t + val_n
    test_rows = test_t + test_n

    rng.shuffle(train_rows)
    rng.shuffle(validation_rows)
    rng.shuffle(test_rows)
    return train_rows, validation_rows, test_rows


def deduplicate(examples: Iterable[Example]) -> List[Example]:
    dedup: List[Example] = []
    seen = set()
    for ex in examples:
        key = (
            ex.text.lower(),
            ex.label_id,
            tuple(item.lower() for item in ex.hate_class),
            tuple(item.lower() for item in ex.target),
            ex.source,
            ex.split,
        )
        if key in seen:
            continue
        seen.add(key)
        dedup.append(ex)
    return dedup


def write_jsonl(file_path: str, examples: List[Example]) -> None:
    with open(file_path, "w", encoding="utf-8") as f:
        for ex in examples:
            f.write(
                json.dumps(
                    {
                        "id": ex.id,
                        "text": ex.text,
                        "label": ex.label,
                        "label_id": ex.label_id,
                        "hate_class": ex.hate_class,
                        "target": ex.target,
                        "source": ex.source,
                        "split": ex.split,
                    },
                    ensure_ascii=False,
                )
                + "\n"
            )


def summarize(file_path: str) -> Dict[str, int]:
    stats = {"total": 0, "toxic": 0, "non_toxic": 0}
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            row = json.loads(line)
            stats["total"] += 1
            stats[row["label"]] += 1
    return stats


def save_stats(output_dir: str, split_to_file: Dict[str, str]) -> None:
    stats = {}
    for split, file_path in split_to_file.items():
        stats[split] = summarize(file_path)

    stats_path = os.path.join(output_dir, "stats.json")
    with open(stats_path, "w", encoding="utf-8") as f:
        json.dump(stats, f, indent=2, ensure_ascii=False)


def main() -> None:
    parser = argparse.ArgumentParser(description="Prepare binary generative dataset for LLM fine-tuning.")
    parser.add_argument("--ihc-file", required=True, help="Path to IHC_pure.json")
    parser.add_argument("--sbic-train-file", required=True, help="Path to sbic_train_pure.json")
    parser.add_argument("--sbic-validation-file", required=True, help="Path to sbic_dev_pure.json")
    parser.add_argument("--sbic-test-file", required=True, help="Path to sbic_test_pure.json")
    parser.add_argument("--output-dir", required=True, help="Output directory for processed JSONL files")
    parser.add_argument(
        "--dataset",
        choices=["merged", "ihc", "sbic"],
        default="ihc",
        help="Which dataset to prepare: merged, ihc, or sbic",
    )
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--ihc-train-ratio", type=float, default=0.8)
    parser.add_argument("--ihc-validation-ratio", type=float, default=0.1)
    args = parser.parse_args()

    if args.ihc_train_ratio + args.ihc_validation_ratio >= 1.0:
        raise ValueError("ihc split ratios must satisfy train_ratio + validation_ratio < 1.0")

    os.makedirs(args.output_dir, exist_ok=True)

    split_rows = {
        "train": [],
        "validation": [],
        "test": [],
    }

    if args.dataset in {"merged", "ihc"}:
        ihc_rows = read_pure_json(args.ihc_file, "all", "IHC")
        train_rows, validation_rows, test_rows = stratified_split(
            ihc_rows,
            train_ratio=args.ihc_train_ratio,
            validation_ratio=args.ihc_validation_ratio,
            seed=args.seed,
        )
        for row in train_rows:
            row.split = "train"
        for row in validation_rows:
            row.split = "validation"
        for row in test_rows:
            row.split = "test"

        split_rows["train"].extend(train_rows)
        split_rows["validation"].extend(validation_rows)
        split_rows["test"].extend(test_rows)

    if args.dataset in {"merged", "sbic"}:
        split_rows["train"].extend(read_pure_json(args.sbic_train_file, "train", "SBIC"))
        split_rows["validation"].extend(read_pure_json(args.sbic_validation_file, "validation", "SBIC"))
        split_rows["test"].extend(read_pure_json(args.sbic_test_file, "test", "SBIC"))

    split_to_file = {}
    for split, rows in split_rows.items():
        dedup_rows = deduplicate(rows)
        out_file = os.path.join(args.output_dir, f"{split}.jsonl")
        write_jsonl(out_file, dedup_rows)
        split_to_file[split] = out_file

    save_stats(args.output_dir, split_to_file)

    label_map_file = os.path.join(args.output_dir, "label_map.json")
    with open(label_map_file, "w", encoding="utf-8") as f:
        json.dump({"id_to_label": {"0": "non_toxic", "1": "toxic"}, "label_to_id": LABEL_TO_ID}, f, indent=2)

    print("Prepared dataset saved to:", args.output_dir)
    for split, fp in split_to_file.items():
        print(split, fp)


if __name__ == "__main__":
    main()
