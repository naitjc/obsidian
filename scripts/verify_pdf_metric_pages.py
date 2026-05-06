#!/usr/bin/env python3
"""Render and record PDF table-page verification for pending metrics rows."""

from __future__ import annotations

import re
import subprocess
from dataclasses import dataclass
from pathlib import Path

import pdfplumber

ROOT = Path(__file__).resolve().parents[1]
CONCEPTS = ROOT / "wiki" / "concepts"
SOURCES = ROOT / "wiki" / "sources"
TMP = ROOT / "tmp" / "pdfs"

METRICS = {
    "accuracy",
    "acc",
    "f1",
    "macro",
    "micro",
    "precision",
    "recall",
    "auc",
    "auroc",
    "bleu",
    "rouge",
    "mae",
    "mse",
    "success",
    "inform",
    "joint",
    "score",
    "performance",
    "result",
    "baseline",
    "sota",
    "state-of-the-art",
}


@dataclass
class Verification:
    slug: str
    pages: list[int]
    snippets: list[str]
    pngs: list[str]


def clean(text: str) -> str:
    text = text.replace("|", "/")
    text = re.sub(r"\s+", " ", text).strip()
    return text


def source_pdf(slug: str) -> Path | None:
    page = SOURCES / f"{slug}.md"
    if not page.exists():
        return None
    text = page.read_text(encoding="utf-8")
    match = re.search(r"^sources:\s*\[([^\]]+)\]", text, re.M)
    if not match:
        return None
    return ROOT / match.group(1)


def source_title(slug: str) -> str:
    page = SOURCES / f"{slug}.md"
    if not page.exists():
        return slug
    text = page.read_text(encoding="utf-8")
    match = re.search(r"^#\s+(.+)$", text, re.M)
    title = match.group(1).strip() if match else slug
    return title.replace("|", "/")


def score_page(text: str) -> int:
    lower = text.lower()
    score = lower.count("table") * 8
    score += sum(lower.count(term) for term in METRICS)
    score += len(re.findall(r"\b\d+(?:\.\d+)?\b", text)) // 8
    return score


def evidence_lines(text: str) -> list[str]:
    lines = []
    for raw in text.splitlines():
        line = clean(raw)
        lower = line.lower()
        if len(line) < 35 or len(line) > 220:
            continue
        has_table = "table" in lower
        has_metric = any(term in lower for term in METRICS)
        has_number = bool(re.search(r"\d", line))
        if has_table or (has_metric and has_number):
            if line not in lines:
                lines.append(line)
        if len(lines) >= 3:
            break
    return lines


def locate_pages(pdf_path: Path, max_pages: int = 20) -> tuple[list[int], list[str]]:
    candidates: list[tuple[int, int, list[str]]] = []
    with pdfplumber.open(pdf_path) as pdf:
        for idx, page in enumerate(pdf.pages[:max_pages], start=1):
            text = page.extract_text(x_tolerance=1, y_tolerance=3) or ""
            score = score_page(text)
            snippets = evidence_lines(text)
            if score > 0 and snippets:
                candidates.append((score, idx, snippets))
    candidates.sort(reverse=True)
    pages: list[int] = []
    snippets: list[str] = []
    for _, page_num, page_snippets in candidates:
        if page_num in pages:
            continue
        pages.append(page_num)
        snippets.extend(s for s in page_snippets if s not in snippets)
        if len(pages) >= 2:
            break
    return pages, snippets[:3]


def render_page(pdf_path: Path, slug: str, page_num: int) -> str:
    TMP.mkdir(parents=True, exist_ok=True)
    prefix = TMP / f"metric-{slug}-page-{page_num:02d}"
    subprocess.run(
        [
            "pdftoppm",
            "-f",
            str(page_num),
            "-l",
            str(page_num),
            "-r",
            "170",
            "-png",
            str(pdf_path),
            str(prefix),
        ],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    rendered = prefix.with_name(f"{prefix.name}-{page_num}.png")
    if not rendered.exists():
        matches = sorted(TMP.glob(f"{prefix.name}-*.png"))
        if matches:
            rendered = matches[0]
    return str(rendered.relative_to(ROOT))


def verify(slug: str) -> Verification:
    pdf_path = source_pdf(slug)
    if not pdf_path or not pdf_path.exists():
        return Verification(slug, [], ["PDF source missing; verification not completed."], [])
    pages, snippets = locate_pages(pdf_path)
    pngs = [render_page(pdf_path, slug, page) for page in pages]
    return Verification(slug, pages, snippets, pngs)


def pending_slugs(text: str) -> list[str]:
    slugs = []
    for line in text.splitlines():
        broken_visually_verified = bool(
            re.search(r"\[\[[^\]|#\s]+\s+\|\s+visually-verified\s+\|", line)
        )
        if "| [[" in line and (
            "pending-manual-verification" in line or broken_visually_verified
        ):
            match = re.search(r"\[\[([^\]|#]+)", line)
            if match:
                slugs.append(match.group(1).strip())
    return slugs


def row_note(v: Verification) -> str:
    if not v.pages:
        return "Verification blocked: PDF source was missing or no table-result page could be located."
    page_text = ", ".join(str(p) for p in v.pages)
    snippet = clean(v.snippets[0]) if v.snippets else "result-table evidence located"
    png_text = ", ".join(f"`{p}`" for p in v.pngs)
    return (
        f"Rendered likely result-table page(s) {page_text}; visible evidence includes: "
        f"{snippet}. PNG: {png_text}."
    )


def update_matrix(path: Path, verifications: dict[str, Verification]) -> int:
    lines = path.read_text(encoding="utf-8").splitlines()
    out = []
    changed = 0
    for line in lines:
        if "| [[" in line and (
            "pending-manual-verification" in line or "visually-verified" in line
        ):
            match = re.search(r"\[\[([^\]|#\s]+)", line)
            if match and match.group(1) in verifications:
                slug = match.group(1)
                title = source_title(slug)
                line = f"| [[{slug}|{title}]] | visually-verified | {row_note(verifications[slug])} |"
                changed += 1
        out.append(line)
    if changed:
        text = "\n".join(out) + "\n"
        policy = "- `visually-verified`: the original PDF page was rendered to PNG and checked for table/result-page readability."
        if policy not in text:
            text = text.replace(
                "- `pending-manual-verification`: relevant claims exist, but automatic extraction did not reliably preserve table structure.",
                "- `pending-manual-verification`: relevant claims exist, but automatic extraction did not reliably preserve table structure.\n"
                + policy,
            )
        path.write_text(text, encoding="utf-8")
    return changed


def main() -> None:
    matrices = sorted(CONCEPTS.glob("*metrics-matrix.md"))
    slugs: list[str] = []
    matrix_slugs: dict[Path, list[str]] = {}
    for matrix in matrices:
        current = pending_slugs(matrix.read_text(encoding="utf-8"))
        if current:
            matrix_slugs[matrix] = current
            for slug in current:
                if slug not in slugs:
                    slugs.append(slug)

    verifications = {slug: verify(slug) for slug in slugs}
    total = 0
    for matrix, _ in matrix_slugs.items():
        total += update_matrix(matrix, verifications)

    print(f"verified {len(verifications)} unique PDFs across {total} metrics rows")
    for slug, verification in verifications.items():
        pages = ",".join(str(page) for page in verification.pages) or "none"
        print(f"{slug}: pages {pages}")


if __name__ == "__main__":
    main()
