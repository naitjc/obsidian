#!/usr/bin/env python3
"""Check direction-tag drift between sources-index and source page frontmatter."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCES = ROOT / "wiki" / "sources"
SOURCES_INDEX = SOURCES / "sources-index.md"

DIRECTION_TAGS = {
    "hate-speech",
    "stance-detection",
    "dialogue",
    "llm-reasoning",
    "sarcasm",
    "role-playing",
    "emotion-recognition",
    "multimodal",
}


def parse_index_rows() -> dict[str, set[str]]:
    rows: dict[str, set[str]] = {}
    for line in SOURCES_INDEX.read_text(encoding="utf-8").splitlines():
        if not line.startswith("| [["):
            continue
        parts = [part.strip() for part in line.strip().strip("|").split("|")]
        if len(parts) < 4:
            continue
        link_cell = parts[0]
        tag_cell = parts[-1]
        match = re.search(r"\[\[([^\]|#]+)", link_cell)
        if not match:
            continue
        tags = {tag.strip() for tag in tag_cell.split(",") if tag.strip()}
        rows[match.group(1)] = tags & DIRECTION_TAGS
    return rows


def frontmatter_tags(slug: str) -> set[str]:
    path = SOURCES / f"{slug}.md"
    if not path.exists():
        return set()
    text = path.read_text(encoding="utf-8")
    match = re.search(r"^tags:\s*\[([^\]]*)\]", text, re.M)
    if not match:
        return set()
    return {tag.strip() for tag in match.group(1).split(",") if tag.strip()} & DIRECTION_TAGS


def main() -> int:
    index_tags = parse_index_rows()
    missing_pages = []
    mismatches = []
    for slug, expected in sorted(index_tags.items()):
        if not (SOURCES / f"{slug}.md").exists():
            missing_pages.append(slug)
            continue
        actual = frontmatter_tags(slug)
        if expected != actual:
            mismatches.append(
                {
                    "slug": slug,
                    "sources_index": sorted(expected),
                    "frontmatter": sorted(actual),
                }
            )

    result = {
        "checked_sources": len(index_tags),
        "missing_source_pages": missing_pages,
        "direction_tag_mismatches": mismatches,
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 1 if missing_pages or mismatches else 0


if __name__ == "__main__":
    raise SystemExit(main())
