---
created: 2026-06-01
updated: 2026-06-01
tags: [maintenance, lint, index]
sources: []
---

# Wiki Integrity Report 2026-06-01

## Scope

This pass checked the global wiki after ingesting five user-added P0 follow-up PDFs and promoting [[p0-target-grounding-reading-synthesis-2026-06-01]].

Previous global pass: [[wiki-integrity-report-2026-05-31]].

## Current Inventory

| Area | Count |
|---|---:|
| Raw source PDFs | 182 |
| Wiki pages | 335 |
| Source pages | 190 |
| Concept pages | 101 |
| Entity pages | 18 |
| Maintenance pages | 24 |
| PDF source pages tagged `deep-ingest-v2` | 182 |
| PDF source pages tagged `auto-ingest` | 0 |

## Link and Catalog Integrity

| Check | Result |
|---|---|
| Broken wiki links | 0 found |
| Wiki pages missing required frontmatter | 0 found |
| Orphan pages | 0 found |
| Duplicate slugs | 0 found |
| Misplaced maintenance pages | 0 found |
| Source direction-tag drift against [[sources-index]] | 0 mismatches |
| PDF text control-character artifacts | 0 offenders |

## Direction Hub Coverage

| Direction | Source pages | Deep-ingested | Hub links | Missing from hub |
|---|---:|---:|---:|---:|
| Hate speech detection | 59 | 59 | 59 | 0 |
| Stance detection | 24 | 24 | 24 | 0 |
| Dialogue / intent / slot filling | 28 | 28 | 28 | 0 |
| LLM reasoning and evaluation | 39 | 39 | 39 | 0 |
| Sarcasm / humor detection | 17 | 17 | 17 | 0 |
| Role-playing agents and persona modeling | 13 | 13 | 13 | 0 |
| Emotion recognition | 9 | 9 | 9 | 0 |
| Multimodal learning | 34 | 34 | 34 | 0 |

## Verification

The following commands passed on 2026-06-01:

```bash
python3 scripts/lint_wiki.py
python3 scripts/wiki_inventory.py
python3 scripts/check_source_tag_drift.py
python3 scripts/check_pdf_text_artifacts.py
```
