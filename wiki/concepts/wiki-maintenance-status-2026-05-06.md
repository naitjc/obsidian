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
| Rendered table checks | Hate speech and stance priority metrics rows visually verified; other direction metrics still require table checks |
| Query answer template | Added |
| Attachment directory | Added |
| Git repository | Initialized |
| Publication-grade numeric verification | Not done; requires manual table checks |

## Remaining Work That Can Still Be Automated Later

- Generate dataset/method entity pages for non-hate directions.
- Add a small script to regenerate source hubs from tags.
- Add a script to detect source pages whose tag set has drifted from [[sources-index]].
- Continue rendered-page snapshots for the highest-priority result tables.
- Keep PDF-derived markdown text free of NUL/control-character artifacts after extraction.

## Remaining Work That Requires Human Judgment

- Decide which exact benchmark numbers matter enough to verify manually.
- Review source summaries for emphasis and correctness.
- Decide which future query answers should be promoted into permanent wiki pages.
