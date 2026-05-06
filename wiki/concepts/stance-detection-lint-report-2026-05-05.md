---
created: 2026-05-05
updated: 2026-05-05
tags: [lint, stance-detection]
sources: []
---

# Stance Detection Lint Report 2026-05-05

## Scope

- Checked stance detection direction pages and 24 stance-tagged source pages.
- This report focuses on wiki structure and direction completeness, not publication-grade table verification.

## Results

| Check | Result |
|---|---|
| Stance-tagged source pages | 24 |
| Deep-ingested stance pages | 24 |
| Stance source hub coverage | 24/24 |
| Broken wiki links after completion pass | 0 |
| Numeric claims requiring table checks | Preserved in [[stance-detection-metrics-matrix]] |

## Remaining Risks

- Automatic PDF extraction can merge columns or split lines, so metric tables are not publication-ready.
- Method keyword tags are useful for navigation but should not be treated as exact taxonomy counts.
- Some stance papers overlap with LLM reasoning, multimodal learning, and dialogue; downstream directions may reuse these sources with different emphasis.
