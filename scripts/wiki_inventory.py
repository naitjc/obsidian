#!/usr/bin/env python3
"""Print a compact inventory of the wiki."""

from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"


def page_tags(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    match = re.search(r"^tags:\s*\[([^\]]*)\]", text, re.M)
    if not match:
        return []
    return [tag.strip() for tag in match.group(1).split(",") if tag.strip()]


def main() -> None:
    source_pages = sorted((WIKI / "sources").glob("*.md"))
    tag_counts = Counter(tag for path in source_pages for tag in page_tags(path))
    result = {
        "raw_pdfs": len(list((ROOT / "raw" / "sources").glob("*.pdf"))),
        "wiki_pages": len(list(WIKI.rglob("*.md"))),
        "source_pages": len(source_pages),
        "concept_pages": len(list((WIKI / "concepts").glob("*.md"))),
        "entity_pages": len(list((WIKI / "entities").glob("*.md"))),
        "source_tag_counts": dict(tag_counts.most_common()),
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
