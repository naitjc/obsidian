#!/usr/bin/env python3
"""Locate likely result-table pages for metrics-matrix source links."""

from __future__ import annotations

import re
from pathlib import Path

import pdfplumber

ROOT = Path(__file__).resolve().parents[1]
CONCEPTS = ROOT / "wiki" / "concepts"
SOURCES = ROOT / "wiki" / "sources"
OUT = CONCEPTS / "pdf-table-verification-index-2026-05-06.md"
METRIC_PAT = re.compile(
    r"\b(table|accuracy|acc\.?|macro[- ]?f1|f1|precision|recall|auc|auroc|mae|bleu|rouge|"
    r"state-of-the-art|sota|outperform|baseline)\b",
    re.I,
)


def wiki_links(text: str) -> list[str]:
    return [
        match.group(1)
        for match in re.finditer(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]*)?\]\]", text)
    ]


def source_pdf(slug: str) -> tuple[str, str] | None:
    path = SOURCES / f"{slug}.md"
    if not path.exists():
        return None
    text = path.read_text(encoding="utf-8")
    title = re.search(r"^#\s+(.+)$", text, re.M)
    src = re.search(r"^sources:\s*\[([^\]]+)\]", text, re.M)
    if not src:
        return None
    return (title.group(1) if title else slug, src.group(1))


def clean(line: str) -> str:
    return re.sub(r"\s+", " ", line).strip()


def locate(pdf_path: Path, max_pages: int = 20) -> list[tuple[int, list[str]]]:
    hits: list[tuple[int, list[str]]] = []
    if not pdf_path.exists():
        return hits
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for idx, page in enumerate(pdf.pages[:max_pages], start=1):
                try:
                    text = page.extract_text(x_tolerance=1, y_tolerance=3) or ""
                except Exception:
                    text = ""
                lines = []
                for raw in text.splitlines():
                    line = clean(raw)
                    if 40 <= len(line) <= 240 and METRIC_PAT.search(line):
                        if line not in lines:
                            lines.append(line)
                    if len(lines) >= 5:
                        break
                if lines:
                    hits.append((idx, lines))
    except Exception as exc:
        hits.append((0, [f"PDF extraction error: {exc}"]))
    return hits[:6]


def main() -> None:
    metric_pages = sorted(CONCEPTS.glob("*metrics-matrix.md"))
    slugs: list[str] = []
    for page in metric_pages:
        for target in wiki_links(page.read_text(encoding="utf-8")):
            if (SOURCES / f"{target}.md").exists() and target not in slugs:
                slugs.append(target)

    sections = []
    for slug in slugs:
        info = source_pdf(slug)
        if not info:
            continue
        title, src = info
        hits = locate(ROOT / src)
        section = [f"## [[{slug}|{title}]]", "", f"- Source PDF: `{src}`"]
        if hits:
            section.append("- Likely table/result pages:")
            for page_num, lines in hits:
                if page_num == 0:
                    section.append(f"  - Extraction error: {lines[0]}")
                    continue
                section.append(f"  - Page {page_num}:")
                for line in lines[:4]:
                    section.append(f"    - {line}")
        else:
            section.append("- Likely table/result pages: none found in first 20 pages")
        sections.append("\n".join(section))

    output = """---
created: 2026-05-06
updated: 2026-05-06
tags: [maintenance, pdf, metrics, verification]
sources: []
---

# PDF Table Verification Index 2026-05-06

This page was generated from source links in direction metrics matrices. It narrows manual metric verification to likely PDF pages and evidence lines. It is not a substitute for visual table inspection.

## Scope

- Input pages: direction `*metrics-matrix.md` files
- Extraction method: `pdfplumber`, first 20 pages per PDF
- Verification boundary: exact benchmark values still require visual checking against the rendered PDF table

"""
    output += "\n\n".join(sections)
    output += "\n"
    OUT.write_text(output, encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)} with {len(sections)} source sections")


if __name__ == "__main__":
    main()
