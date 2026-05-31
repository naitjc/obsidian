import argparse
import json
import os
from typing import Dict, List


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Export bad cases from prediction file.")
    parser.add_argument("--predictions-file", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument(
        "--top-k",
        type=int,
        default=-1,
        help="Optional: keep top-k by confidence for each error type. Use -1 to keep all.",
    )
    return parser.parse_args()


def load_rows(file_path: str) -> List[Dict]:
    rows = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            rows.append(json.loads(line))
    return rows


def main() -> None:
    args = parse_args()
    os.makedirs(args.output_dir, exist_ok=True)

    rows = load_rows(args.predictions_file)
    false_positive = []
    false_negative = []

    for row in rows:
        gold = row["label_id"]
        pred = row["pred_id"]
        if gold == pred:
            continue

        row["text_len"] = len(row["text"])
        if pred == 1 and gold == 0:
            row["error_type"] = "false_positive"
            row["confidence"] = row["prob_toxic"]
            false_positive.append(row)
        elif pred == 0 and gold == 1:
            row["error_type"] = "false_negative"
            row["confidence"] = row["prob_non_toxic"]
            false_negative.append(row)

    false_positive.sort(key=lambda x: x["confidence"], reverse=True)
    false_negative.sort(key=lambda x: x["confidence"], reverse=True)

    if args.top_k > 0:
        false_positive = false_positive[: args.top_k]
        false_negative = false_negative[: args.top_k]

    fp_path = os.path.join(args.output_dir, "false_positive.jsonl")
    fn_path = os.path.join(args.output_dir, "false_negative.jsonl")

    with open(fp_path, "w", encoding="utf-8") as f:
        for row in false_positive:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")

    with open(fn_path, "w", encoding="utf-8") as f:
        for row in false_negative:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")

    bucket = {
        "<=32": 0,
        "33-64": 0,
        "65-128": 0,
        "129-256": 0,
        ">256": 0,
    }
    for row in false_positive + false_negative:
        text_len = row["text_len"]
        if text_len <= 32:
            bucket["<=32"] += 1
        elif text_len <= 64:
            bucket["33-64"] += 1
        elif text_len <= 128:
            bucket["65-128"] += 1
        elif text_len <= 256:
            bucket["129-256"] += 1
        else:
            bucket[">256"] += 1

    summary_path = os.path.join(args.output_dir, "error_summary.json")
    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump(
            {
                "total_errors": len(false_positive) + len(false_negative),
                "false_positive": len(false_positive),
                "false_negative": len(false_negative),
                "top_k": args.top_k,
                "length_bucket": bucket,
            },
            f,
            indent=2,
            ensure_ascii=False,
        )

    print("Saved:", fp_path)
    print("Saved:", fn_path)
    print("Saved:", summary_path)


if __name__ == "__main__":
    main()
