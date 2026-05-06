#!/usr/bin/env python3
"""Detect control-character artifacts in PDF-derived wiki markdown."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE_PAGES = ROOT / "wiki" / "sources"

ALLOWED = {"\n", "\r", "\t"}


def bad_chars(text: str) -> list[str]:
    found = []
    for char in text:
        if ord(char) < 32 and char not in ALLOWED and char not in found:
            found.append(char)
    return found


def main() -> int:
    offenders = []
    for path in sorted(SOURCE_PAGES.glob("*.md")):
        chars = bad_chars(path.read_text(encoding="utf-8", errors="replace"))
        if chars:
            offenders.append(
                {
                    "path": str(path.relative_to(ROOT)),
                    "codepoints": [f"U+{ord(char):04X}" for char in chars],
                }
            )
    result = {"checked_source_pages": len(list(SOURCE_PAGES.glob("*.md"))), "offenders": offenders}
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 1 if offenders else 0


if __name__ == "__main__":
    raise SystemExit(main())
