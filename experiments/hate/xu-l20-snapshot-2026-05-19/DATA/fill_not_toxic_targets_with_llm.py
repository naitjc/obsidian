#!/usr/bin/env python3
"""Fill not_toxic target fields by asking an LLM for mentioned referents.

The script reads processed IHC/SBIC JSON files, finds not_toxic examples whose
target is empty or ["none"], and writes augmented copies plus a JSONL cache.
It does not modify the input files in place unless --in-place is provided.
"""

from __future__ import annotations

import argparse
import json
import os
import random
import sys
import time
from pathlib import Path
from typing import Any


DEFAULT_FILES = (
    "IHC/processed/train.json",
    "IHC/processed/valid.json",
    "IHC/processed/test.json",
    "SBIC/processed/train.json",
    "SBIC/processed/valid.json",
    "SBIC/processed/test.json",
)

NOT_TOXIC_LABELS = {"not_toxic", "non_toxic", "not_hate", "not_offensive"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Use an OpenAI-compatible LLM API to fill target lists for "
            "not_toxic samples in processed hate-speech datasets."
        )
    )
    parser.add_argument("--data-root", default="/data/chenjt/hate/DATA")
    parser.add_argument("--files", nargs="*", default=list(DEFAULT_FILES))
    parser.add_argument("--output-root", default="/data/chenjt/hate/DATA/llm_target_filled")
    parser.add_argument("--cache-file", default="/data/chenjt/hate/DATA/llm_not_toxic_target_cache.jsonl")
    parser.add_argument("--model", default=os.environ.get("LLM_TARGET_MODEL", "gpt-4.1-mini"))
    parser.add_argument("--base-url", default=os.environ.get("OPENAI_BASE_URL"))
    parser.add_argument("--api-key-env", default="OPENAI_API_KEY")
    parser.add_argument("--temperature", type=float, default=0.0)
    parser.add_argument("--max-output-tokens", type=int, default=300)
    parser.add_argument("--request-timeout", type=float, default=60.0)
    parser.add_argument("--sleep", type=float, default=0.0, help="Seconds to sleep between successful calls.")
    parser.add_argument("--max-retries", type=int, default=5)
    parser.add_argument("--retry-base-sleep", type=float, default=2.0)
    parser.add_argument("--limit", type=int, default=0, help="Process at most this many pending rows; 0 means all.")
    parser.add_argument("--sample", type=int, default=0, help="Randomly sample this many pending rows before processing.")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--in-place", action="store_true", help="Overwrite input files after updating.")
    parser.add_argument("--dry-run", action="store_true", help="Print pending counts without calling the API.")
    return parser.parse_args()


def load_json(path: Path) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, list):
        raise ValueError(f"{path} must contain a JSON list")
    for idx, row in enumerate(data):
        if not isinstance(row, dict):
            raise ValueError(f"{path}[{idx}] is not an object")
    return data


def atomic_write_json(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    with tmp.open("w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)
        f.write("\n")
    tmp.replace(path)


def is_pending_not_toxic(row: dict[str, Any]) -> bool:
    label = str(row.get("class", row.get("label", ""))).strip().lower()
    if label not in NOT_TOXIC_LABELS:
        return False
    target = row.get("target")
    if target in (None, "", []):
        return True
    if isinstance(target, list) and len(target) == 1 and str(target[0]).strip().lower() == "none":
        return True
    return False


def row_key(rel_file: str, row: dict[str, Any], idx: int) -> str:
    row_id = str(row.get("id", idx))
    return f"{rel_file}::{row_id}::{idx}"


def load_cache(path: Path) -> dict[str, list[str]]:
    cached: dict[str, list[str]] = {}
    if not path.exists():
        return cached
    with path.open("r", encoding="utf-8") as f:
        for line_no, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"Bad JSON in cache {path}:{line_no}") from exc
            key = obj.get("key")
            targets = obj.get("targets")
            if isinstance(key, str) and isinstance(targets, list):
                cached[key] = [str(item).strip() for item in targets if str(item).strip()]
    return cached


def append_cache(path: Path, record: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")


def build_prompt(text: str) -> str:
    return (
        "Extract the people, groups, communities, organizations, or entities that the statement is directed at "
        "or makes a claim about.\n"
        "Return ONLY valid JSON with this schema:\n"
        "{\"targets\": [\"target\"]}\n\n"
        "Rules:\n"
        "- Use normalized real-world names, not surface phrases.\n"
        "- Prefer the main social group, community, person, or organization over incidental context.\n"
        "- Return at most 5 targets, ordered by salience.\n"
        "- If there is no clear target, return {\"targets\": []}.\n"
        "- Do not include explanations or extra keys.\n\n"
        f"Text: {text}\n"
    )


def parse_targets(raw: str) -> list[str]:
    text = raw.strip()
    start = text.find("{")
    end = text.rfind("}")
    if start == -1 or end == -1 or start > end:
        raise ValueError(f"LLM output is not JSON: {raw[:200]}")
    payload = json.loads(text[start : end + 1])
    targets = payload.get("targets")
    if not isinstance(targets, list):
        raise ValueError(f"LLM output missing targets list: {raw[:200]}")

    cleaned: list[str] = []
    seen: set[str] = set()
    for item in targets:
        if not isinstance(item, str):
            continue
        value = " ".join(item.strip().split())
        value = value.replace("：", ":")
        if ":" in value:
            value = value.split(":", 1)[1].strip()
        if not value:
            continue
        key = value.lower()
        if key in seen:
            continue
        seen.add(key)
        cleaned.append(value)
    return cleaned[:3]


def build_client(args: argparse.Namespace):
    api_key = os.environ.get(args.api_key_env)
    if not api_key:
        raise RuntimeError(f"Missing API key env var: {args.api_key_env}")
    try:
        from openai import OpenAI
    except ImportError as exc:
        raise RuntimeError("Install the openai package in the cjt environment: pip install openai") from exc

    kwargs: dict[str, str] = {"api_key": api_key}
    if args.base_url:
        kwargs["base_url"] = args.base_url
    return OpenAI(**kwargs, timeout=args.request_timeout, max_retries=0)


def call_llm(client: Any, args: argparse.Namespace, text: str) -> tuple[list[str], str]:
    messages = [
        {
            "role": "system",
            "content": "You are a precise information extraction system. Output only valid JSON.",
        },
        {"role": "user", "content": build_prompt(text)},
    ]

    last_error: Exception | None = None
    for attempt in range(args.max_retries + 1):
        try:
            request_kwargs = {
                "model": args.model,
                "messages": messages,
                "temperature": args.temperature,
                "max_tokens": args.max_output_tokens,
                "response_format": {"type": "json_object"},
            }
            if args.base_url and "deepseek" in args.base_url.lower():
                request_kwargs["extra_body"] = {"thinking": {"type": "disabled"}}

            response = client.chat.completions.create(**request_kwargs)
            message = response.choices[0].message
            raw = message.content or ""
            if not raw:
                raw = getattr(message, "reasoning_content", "") or ""
            return parse_targets(raw), raw
        except Exception as exc:  # API and parsing failures are retryable.
            last_error = exc
            if attempt >= args.max_retries:
                break
            print(
                f"retrying_after_error attempt={attempt + 1}/{args.max_retries} "
                f"error={type(exc).__name__}: {str(exc)[:200]}",
                flush=True,
            )
            delay = args.retry_base_sleep * (2**attempt) + random.random()
            time.sleep(delay)
    raise RuntimeError(f"LLM call failed after retries: {last_error}") from last_error


def output_path_for(args: argparse.Namespace, rel_file: str) -> Path:
    if args.in_place:
        return Path(args.data_root) / rel_file
    return Path(args.output_root) / rel_file


def main() -> None:
    args = parse_args()
    random.seed(args.seed)

    data_root = Path(args.data_root)
    cache_path = Path(args.cache_file)
    cached = load_cache(cache_path)

    file_rows: dict[str, list[dict[str, Any]]] = {}
    pending: list[tuple[str, int, dict[str, Any], str]] = []
    total_pending = 0

    for rel_file in args.files:
        path = data_root / rel_file
        rows = load_json(path)
        file_rows[rel_file] = rows
        for idx, row in enumerate(rows):
            if not is_pending_not_toxic(row):
                continue
            total_pending += 1
            key = row_key(rel_file, row, idx)
            if key in cached:
                row["target"] = cached[key]
                continue
            pending.append((rel_file, idx, row, key))

    print(
        f"pending_total={total_pending} cached_applied={total_pending - len(pending)} api_pending={len(pending)}",
        flush=True,
    )
    if args.dry_run:
        return

    if args.sample:
        pending = random.sample(pending, min(args.sample, len(pending)))
    if args.limit:
        pending = pending[: args.limit]

    client = build_client(args)
    processed = 0
    for rel_file, idx, row, key in pending:
        print(f"calling_api item={processed + 1}/{len(pending)} key={key}", flush=True)
        targets, raw = call_llm(client, args, str(row.get("post", row.get("text", ""))))
        row["target"] = targets
        record = {
            "key": key,
            "file": rel_file,
            "index": idx,
            "id": row.get("id"),
            "targets": targets,
            "raw_output": raw,
        }
        append_cache(cache_path, record)
        processed += 1
        if processed % 25 == 0:
            print(f"processed={processed}/{len(pending)} latest={key}", flush=True)
        if args.sleep:
            time.sleep(args.sleep)

    for rel_file, rows in file_rows.items():
        out_path = output_path_for(args, rel_file)
        atomic_write_json(out_path, rows)
        print(f"wrote {out_path}")

    print(f"done processed_api={processed} cache={cache_path}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted", file=sys.stderr)
        raise
