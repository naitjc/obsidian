---
created: 2026-05-19
updated: 2026-05-19
tags: [maintenance, schema]
sources: []
---

# Frontmatter Conventions

## Required Fields

Every markdown page under `wiki/` must start with YAML frontmatter containing:

```yaml
---
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: []
sources: []
---
```

## Tag Vocabulary

- `index`: routing page.
- `source`: source-grounded note.
- `concept`: stable topic or method synthesis.
- `entity`: reusable named entity such as a dataset or benchmark.
- `maintenance`: schema, lint, status, or workflow page.
- `status`: current state, completion boundary, or backlog page.
- `metrics`: quantitative workspace.
- `query-answer`: durable answer promoted from a research question.
- `auto-ingest`: metadata or first-pass extraction only.
- `deep-ingest-v2`: completed source-page extraction with required sections.
- direction tags: `hate-speech`, `stance-detection`, `dialogue`, `llm-reasoning`, `sarcasm`, `role-playing`, `emotion-recognition`, `multimodal`.

## Status Vocabulary

- `internal-navigation`: suitable for browsing, routing, and internal Q&A.
- `visually-verified`: checked against rendered or layout-preserved PDF evidence.
- `publication-checked`: exact value or claim checked against original table or source-statement evidence.
- `pending-manual-verification`: candidate claim or metric still needs table-level or source-level checking.
- `out-of-scope`: intentionally not pursued for the current direction.

## Numeric Claim Rule

Do not convert automatically extracted numeric candidates into final claims unless the original table or source statement has been checked. If a value is useful but not checked, keep it in the relevant metrics matrix and mark the verification state explicitly.
