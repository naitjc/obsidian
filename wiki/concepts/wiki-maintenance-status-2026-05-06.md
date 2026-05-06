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
- `raw/assets/` was created as the local attachment target.
- A query answer template was added under `wiki/templates/`.
- [[global-research-map]] now acts as the top-level research map.
- [[cross-direction-synthesis-2026-05-06]] records synthesis across all completed directions.
- [[wiki-maintenance-playbook]] records repeatable maintenance and query workflows.
- The vault root was initialized as a git repository for local version history.

## Current Structural Status

| Check | Status |
|---|---|
| Direction-level wiki construction | Complete |
| Source hubs for completed directions | Complete |
| Structural lint script | Added |
| Inventory script | Added |
| PDF table locator | Added |
| PDF table verification index | Generated |
| Poppler / `pdftoppm` | Installed |
| Rendered table checks | Complete for all priority metrics rows in direction metrics matrices |
| Query answer template | Added |
| Attachment directory | Added |
| Git repository | Initialized |
| Publication-grade numeric verification | Priority metrics rows have rendered-page visual verification; avoid global SOTA rankings across mismatched tasks |

## Remaining Work That Can Still Be Automated Later

- Generate dataset/method entity pages for non-hate directions.
- Add a small script to regenerate source hubs from tags.
- Add a script to detect source pages whose tag set has drifted from [[sources-index]].
- Keep PDF-derived markdown text free of NUL/control-character artifacts after extraction.

## Remaining Work That Requires Human Judgment

- Review source summaries for emphasis and correctness.
- Decide which future query answers should be promoted into permanent wiki pages.
- Decide whether any future publication needs additional exact-number extraction beyond the already verified priority metrics rows.
