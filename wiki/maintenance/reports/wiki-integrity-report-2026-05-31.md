---
created: 2026-05-31
updated: 2026-05-31
tags: [maintenance, lint, index]
sources: []
---

# Wiki Integrity Report 2026-05-31

## Scope

This pass checked the global wiki after the 2026-05-27 source additions, the
IHC/SBIC experiment archive import, and the routing updates for target-relation
grounding and missing-annotation utility validation.

Previous global pass: [[wiki-integrity-report-2026-05-21]].

## Current Inventory

| Area | Count |
|---|---:|
| Raw source PDFs | 177 |
| Wiki pages | 325 |
| Source pages | 185 |
| Concept pages | 97 |
| Entity pages | 18 |
| Maintenance pages | 23 |
| PDF source pages tagged `deep-ingest-v2` | 177 |
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
| Hate speech detection | 55 | 55 | 55 | 0 |
| Stance detection | 24 | 24 | 24 | 0 |
| Dialogue / intent / slot filling | 28 | 28 | 28 | 0 |
| LLM reasoning and evaluation | 37 | 37 | 37 | 0 |
| Sarcasm / humor detection | 17 | 17 | 17 | 0 |
| Role-playing agents and persona modeling | 13 | 13 | 13 | 0 |
| Emotion recognition | 9 | 9 | 9 | 0 |
| Multimodal learning | 34 | 34 | 34 | 0 |

## Repository Hygiene

- Added project-level ignore rules for Python interpreter caches and PID files.
- Removed copied `__pycache__/` directories and a stale PID file from the local
  experiment archive before publication.
- Kept sample-level experiment data, per-example JSONL outputs, and execution
  logs in the local archive while publishing README files, code, configs,
  aggregate metrics, and non-sample summaries.
- Preserved source PDFs as immutable inputs and kept Obsidian workspace UI state
  outside the publication scope.

## Verification

The following commands passed on 2026-05-31:

```bash
python3 scripts/lint_wiki.py
python3 scripts/wiki_inventory.py
python3 scripts/check_source_tag_drift.py
python3 scripts/check_pdf_text_artifacts.py
```
