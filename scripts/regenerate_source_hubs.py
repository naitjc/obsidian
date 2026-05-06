#!/usr/bin/env python3
"""Regenerate flat direction source hubs from source page frontmatter tags."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONCEPTS = ROOT / "wiki" / "concepts"
SOURCES = ROOT / "wiki" / "sources"

DIRECTIONS = {
    "hate-speech": {
        "hub": "hate-speech-source-hub.md",
        "title": "Hate Speech Source Hub",
        "concepts": ["hate-speech-research-map", "hate-speech-final-synthesis", "hate-speech-metrics-matrix"],
    },
    "stance-detection": {
        "hub": "stance-detection-source-hub.md",
        "title": "Stance Detection Source Hub",
        "concepts": ["stance-detection", "zero-shot-learning", "synthetic-data-generation", "llm-reasoning", "multimodal-learning"],
    },
    "dialogue": {
        "hub": "dialogue-systems-source-hub.md",
        "title": "Dialogue, Intent, and Slot Filling Source Hub",
        "concepts": ["dialogue-systems", "llm-reasoning", "multimodal-learning", "synthetic-data-generation", "llm-evaluation"],
    },
    "llm-reasoning": {
        "hub": "llm-reasoning-source-hub.md",
        "title": "LLM Reasoning and Evaluation Source Hub",
        "concepts": ["llm-reasoning", "llm-evaluation", "synthetic-data-generation", "retrieval-augmented-generation"],
    },
    "sarcasm": {
        "hub": "sarcasm-detection-source-hub.md",
        "title": "Sarcasm and Humor Detection Source Hub",
        "concepts": ["sarcasm-detection", "multimodal-learning", "llm-reasoning", "emotion-recognition"],
    },
    "role-playing": {
        "hub": "role-playing-agents-source-hub.md",
        "title": "Role-Playing Agents and Persona Modeling Source Hub",
        "concepts": ["role-playing-agents", "llm-reasoning", "llm-evaluation", "synthetic-data-generation"],
    },
    "emotion-recognition": {
        "hub": "emotion-recognition-source-hub.md",
        "title": "Emotion Recognition and Empathetic Response Source Hub",
        "concepts": ["emotion-recognition", "dialogue-systems", "multimodal-learning", "llm-reasoning"],
    },
    "multimodal": {
        "hub": "multimodal-learning-source-hub.md",
        "title": "Multimodal Learning Source Hub",
        "concepts": ["multimodal-learning", "hate-speech-research-map", "stance-detection", "sarcasm-detection", "emotion-recognition"],
    },
}


def source_records() -> list[tuple[str, str, set[str]]]:
    records = []
    for path in sorted(SOURCES.glob("*.md")):
        if path.name in {"sources-index.md", "nlp-research-collection.md", "pdf-manifest.json"}:
            continue
        text = path.read_text(encoding="utf-8")
        title_match = re.search(r"^#\s+(.+)$", text, re.M)
        tags_match = re.search(r"^tags:\s*\[([^\]]*)\]", text, re.M)
        if not title_match or not tags_match:
            continue
        title = title_match.group(1).strip().replace("|", "/")
        tags = {tag.strip() for tag in tags_match.group(1).split(",") if tag.strip()}
        records.append((path.stem, title, tags))
    return records


def render_hub(tag: str, config: dict[str, object], records: list[tuple[str, str, set[str]]]) -> str:
    linked = [(slug, title) for slug, title, tags in records if tag in tags]
    concept_links = "\n".join(f"- [[{concept}]]" for concept in config["concepts"])
    source_links = "\n".join(f"- [[{slug}|{title}]]" for slug, title in linked)
    return f"""---
created: 2026-05-06
updated: 2026-05-06
tags: [index, {tag}, sources]
sources: []
---

# {config["title"]}

Total linked papers: **{len(linked)}**

Use this page as the canonical entry point generated from source page frontmatter tags.

## Sources
{source_links}

## Cross-Cutting Concept Links
{concept_links}
"""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true", help="rewrite source hub files")
    args = parser.parse_args()

    records = source_records()
    changed = []
    for tag, config in DIRECTIONS.items():
        path = CONCEPTS / str(config["hub"])
        new_text = render_hub(tag, config, records)
        old_text = path.read_text(encoding="utf-8") if path.exists() else ""
        if old_text != new_text:
            changed.append(str(path.relative_to(ROOT)))
            if args.write:
                path.write_text(new_text, encoding="utf-8")
    print({"changed_hubs": changed, "write": args.write})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
