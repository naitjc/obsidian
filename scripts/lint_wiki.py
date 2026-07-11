#!/usr/bin/env python3
"""Structural lint for the LLM-maintained markdown wiki."""

from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"
SOURCES = WIKI / "sources"
CONCEPTS = WIKI / "concepts"
ALLOWED_DUPLICATE_SLUGS = {"index"}
REQUIRED_FRONTMATTER = ("created", "updated", "tags", "sources")
DIRECTIONS = {
    "hate-speech": "hate-speech",
    "stance-detection": "stance-detection",
    "dialogue-systems": "dialogue",
    "llm-reasoning": "llm-reasoning",
    "sarcasm-detection": "sarcasm",
    "role-playing-agents": "role-playing",
    "emotion-recognition": "emotion-recognition",
    "multimodal-learning": "multimodal",
}


def markdown_files(root: Path) -> list[Path]:
    return sorted(p for p in root.rglob("*.md") if not any(part.startswith(".") for part in p.parts))


def frontmatter(text: str) -> str:
    match = re.match(r"^---\n([\s\S]*?)\n---", text)
    return match.group(1) if match else ""


def tags(text: str) -> list[str]:
    match = re.search(r"^tags:\s*\[([^\]]*)\]", frontmatter(text), re.M)
    if not match:
        return []
    return [tag.strip() for tag in match.group(1).split(",") if tag.strip()]


def wiki_links(text: str) -> list[str]:
    return [
        match.group(1)
        for match in re.finditer(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]*)?\]\]", text)
    ]


def main() -> int:
    all_md = markdown_files(ROOT)
    wiki_md = markdown_files(WIKI)
    slug_paths = defaultdict(list)
    for path in all_md:
        slug_paths[path.stem].append(path)
    wiki_slug_paths = defaultdict(list)
    for path in wiki_md:
        wiki_slug_paths[path.stem].append(path)
    duplicate_slugs = {
        slug: [str(path.relative_to(ROOT)) for path in paths]
        for slug, paths in sorted(wiki_slug_paths.items())
        if len(paths) > 1 and slug not in ALLOWED_DUPLICATE_SLUGS
    }

    missing_frontmatter = []
    broken_links = []
    ambiguous_links = []
    misplaced_maintenance_pages = []
    inbound_links = {path.stem: set() for path in wiki_md}
    for path in wiki_md:
        text = path.read_text(encoding="utf-8")
        fm = frontmatter(text)
        missing = [key for key in REQUIRED_FRONTMATTER if not re.search(rf"^{key}:", fm, re.M)]
        if missing:
            missing_frontmatter.append({"file": str(path.relative_to(ROOT)), "missing": missing})
        page_tags = tags(text)
        if path.parent == CONCEPTS and (
            "lint" in page_tags or ("maintenance" in page_tags and "completion" not in page_tags)
        ):
            misplaced_maintenance_pages.append(str(path.relative_to(ROOT)))
        for target in wiki_links(text):
            candidates = slug_paths.get(target, [])
            if not candidates:
                broken_links.append({"from": str(path.relative_to(ROOT)), "target": target})
            elif len(candidates) > 1:
                ambiguous_links.append(
                    {
                        "from": str(path.relative_to(ROOT)),
                        "target": target,
                        "candidates": [str(candidate.relative_to(ROOT)) for candidate in candidates],
                    }
                )
            elif target != path.stem and target in inbound_links:
                inbound_links[target].add(path.stem)

    orphan_pages = [
        str(path.relative_to(ROOT))
        for path in wiki_md
        if path.stem != "index" and not inbound_links.get(path.stem)
    ]

    direction_status = {}
    for prefix, tag in DIRECTIONS.items():
        source_pages = []
        for path in sorted(SOURCES.glob("*.md")):
            page_tags = tags(path.read_text(encoding="utf-8"))
            if tag in page_tags:
                source_pages.append(
                    {
                        "slug": path.stem,
                        "deep": "deep-ingest-v2" in page_tags,
                        "auto": "auto-ingest" in page_tags,
                    }
                )
        hub_path = CONCEPTS / f"{prefix}-source-hub.md"
        hub_links = []
        if hub_path.exists():
            hub_links = [
                target
                for target in wiki_links(hub_path.read_text(encoding="utf-8"))
                if (SOURCES / f"{target}.md").exists()
            ]
        unique_hub_links = sorted(set(hub_links))
        source_slugs = [item["slug"] for item in source_pages]
        direction_status[prefix] = {
            "tag": tag,
            "source_pages": len(source_pages),
            "deep_ingested": sum(1 for item in source_pages if item["deep"]),
            "auto_ingest": sum(1 for item in source_pages if item["auto"]),
            "hub_links": len(unique_hub_links),
            "missing_from_hub": sorted(set(source_slugs) - set(unique_hub_links)),
            "extra_in_hub": sorted(set(unique_hub_links) - set(source_slugs)),
        }

    result = {
        "wiki_pages": len(wiki_md),
        "source_pages": len(list(SOURCES.glob("*.md"))),
        "concept_pages": len(list(CONCEPTS.glob("*.md"))),
        "entity_pages": len(list((WIKI / "entities").glob("*.md"))),
        "broken_links": broken_links,
        "ambiguous_links": ambiguous_links,
        "missing_frontmatter": missing_frontmatter,
        "orphan_pages": orphan_pages,
        "duplicate_slugs": duplicate_slugs,
        "misplaced_maintenance_pages": misplaced_maintenance_pages,
        "directions": direction_status,
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))

    has_direction_gap = any(
        status["auto_ingest"]
        or status["missing_from_hub"]
        or status["extra_in_hub"]
        or status["source_pages"] != status["deep_ingested"]
        for status in direction_status.values()
    )
    return 1 if (
        broken_links
        or ambiguous_links
        or missing_frontmatter
        or orphan_pages
        or duplicate_slugs
        or misplaced_maintenance_pages
        or has_direction_gap
    ) else 0


if __name__ == "__main__":
    raise SystemExit(main())
