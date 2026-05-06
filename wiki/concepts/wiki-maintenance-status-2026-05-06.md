---
created: 2026-05-06
updated: 2026-05-06
tags: [maintenance, status]
sources: []
---

# Wiki Maintenance Status 2026-05-06

## Completed Without Human Review

- Reusable maintenance scripts were added under `scripts/`.
- [[pdf-table-verification-index-2026-05-06]] was generated from direction metrics matrices to narrow PDF table checks.
- `scripts/verify_pdf_metric_pages.py` was added to render likely result-table pages for remaining metrics rows.
- Non-hate dataset and benchmark entity map pages were added under `wiki/entities/`.
- Source hub regeneration, source tag drift, and PDF text artifact check scripts were added under `scripts/`.
- `raw/assets/` was created as the local attachment target.
- A query answer template was added under `wiki/templates/`.
- [[global-research-map]] now acts as the top-level research map.
- [[cross-direction-synthesis-2026-05-06]] records synthesis across all completed directions.
- [[wiki-maintenance-playbook]] records repeatable maintenance and query workflows.
- The vault root was initialized as a git repository for local version history.
- The remaining 21 numbered PDF source pages were upgraded from `auto-ingest`/`peripheral-source` navigation nodes to `deep-ingest-v2` source pages.
- [[index]] was refreshed with current inventory counts and source status boundaries.
- [[wiki-integrity-report-2026-05-06]] records the current post-alignment integrity state.
- User selected [[hate-speech-metrics-matrix]] and [[llm-reasoning-metrics-matrix]] for publication-grade priority metrics checking. Their priority rows are now marked `publication-checked` where exact table values or source-statement ranges were checked against rendered/layout-preserved PDF evidence.
- User selected high-impact source-summary review for hate speech and LLM reasoning. The highest-noise priority source pages were rewritten from PDF-extraction fragments into clean evidence-oriented summaries, and two misleading `cross-lingual` tags were removed from cross-modality/cross-dataset hate pages.
- User selected automatic query-answer promotion: durable query answers should be filed as wiki pages by default and recorded in [[log]], while transient operational answers should not be promoted.

## Current Structural Status

| Check | Status |
|---|---|
| Direction-level wiki construction | Complete |
| Source hubs for completed directions | Complete |
| Structural lint script | Added |
| Inventory script | Added |
| PDF table locator | Added |
| PDF table verification index | Generated |
| Source hub regeneration script | Added |
| Source tag drift checker | Added; current result has 0 mismatches |
| PDF text artifact checker | Added; current result has 0 offenders |
| Poppler / `pdftoppm` | Installed |
| Rendered table checks | Complete for all priority metrics rows in direction metrics matrices |
| Auto-ingest PDF source pages | 0 remaining among the 150 numbered PDF source pages |
| Non-hate entity maps | Added |
| Query answer template | Added |
| Attachment directory | Added |
| Git repository | Initialized |
| Numeric verification boundary | Hate speech and LLM reasoning priority metrics rows have `publication-checked` evidence where exact table values or source-statement ranges are listed. Other directions remain internal-navigation grade unless separately selected. Avoid global SOTA rankings across mismatched tasks |
| High-impact source-summary review | Completed for the noisiest hate speech and LLM reasoning priority source pages selected in this pass |
| Query-answer promotion rule | Automatically promote durable synthesis answers; record promotions in [[log]] |

## Current Automated Maintenance Backlog

- No current structural automation backlog remains for the completed directions or numbered PDF source pages.
- Future source additions should rerun `scripts/lint_wiki.py`, `scripts/wiki_inventory.py`, `scripts/check_source_tag_drift.py`, and `scripts/check_pdf_text_artifacts.py`.

## Remaining Work That Requires Human Judgment

- Optional deeper human review of source summaries beyond the high-impact hate speech and LLM reasoning priority pages already cleaned.
- For future query answers, apply the automatic promotion rule and only skip pages for transient or purely operational answers.
- Decide whether any future publication needs additional exact-number extraction beyond the selected hate speech and LLM reasoning priority rows.
