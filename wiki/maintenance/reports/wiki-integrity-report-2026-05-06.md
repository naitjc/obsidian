---
created: 2026-05-06
updated: 2026-05-06
tags: [maintenance, lint, index]
sources: []
---

# Wiki Integrity Report 2026-05-06

## Scope

This pass checked global wiki link integrity after all 150 numbered PDF source pages were aligned to `deep-ingest-v2` source-page format.

## Current Inventory

| Area | Count |
|---|---:|
| Raw source PDFs | 150 |
| Wiki pages | 274 |
| Source pages | 158 |
| Concept pages | 96 |
| Entity pages | 18 |
| Numbered PDF source pages tagged `deep-ingest-v2` | 150 |
| Numbered PDF source pages tagged `auto-ingest` | 0 |

## Link and Catalog Integrity

| Check | Result |
|---|---|
| Broken wiki links | 0 found |
| Wiki pages missing required frontmatter | 0 found |
| Source direction-tag drift against [[sources-index]] | 0 mismatches |
| PDF text control-character artifacts | 0 offenders |
| Pending metrics rows for rendered-page verification | 0 rows |
| Publication-checked priority metrics rows | Hate speech and LLM reasoning selected by user; priority rows updated in their metrics matrices |
| High-impact source-summary cleanup | Completed for selected noisy hate speech and LLM reasoning priority source pages |
| Query-answer promotion rule | Durable synthesis answers auto-promoted by default; transient operational answers skipped |

## Direction Hub Coverage

| Direction | Source pages | Deep-ingested | Hub links | Missing from hub |
|---|---:|---:|---:|---:|
| Hate speech detection | 37 | 37 | 37 | 0 |
| Stance detection | 24 | 24 | 24 | 0 |
| Dialogue / intent / slot filling | 24 | 24 | 24 | 0 |
| LLM reasoning and evaluation | 34 | 34 | 34 | 0 |
| Sarcasm / humor detection | 17 | 17 | 17 | 0 |
| Role-playing agents and persona modeling | 13 | 13 | 13 | 0 |
| Emotion recognition | 9 | 9 | 9 | 0 |
| Multimodal learning | 34 | 34 | 34 | 0 |

## Remaining Boundary

The automated structural backlog is closed for the current corpus. User-selected publication-grade priority checks are complete for hate speech and LLM reasoning metrics matrices, the noisiest high-impact source summaries in those directions have been cleaned, and the query-answer promotion rule is set to automatic promotion for durable synthesis. Remaining work is human judgment: whether to do deeper source-summary review beyond the selected priority pages, and whether additional directions or non-priority rows need publication-grade exact-number checks.
