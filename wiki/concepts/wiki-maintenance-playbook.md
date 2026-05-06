---
created: 2026-05-06
updated: 2026-05-06
tags: [maintenance, workflow]
sources: []
---

# Wiki Maintenance Playbook

## Routine Query Workflow

1. Read [[global-research-map]] and the relevant direction map.
2. Read the source hub for the direction.
3. Read the final synthesis and metrics workspace.
4. Answer with source-page links and explicit confidence boundaries.
5. If the answer adds reusable synthesis, create a new page using [[query-answer-template]].
6. Update [[index]] and append to [[log]].

## Routine Lint Workflow

Run:

```bash
python3 scripts/lint_wiki.py
python3 scripts/wiki_inventory.py
python3 scripts/locate_pdf_tables.py
```

Expected structural state:
- 0 broken wiki links
- 0 wiki pages missing required frontmatter
- 0 auto-ingest pages in completed directions
- 100% source hub coverage for completed directions

`scripts/locate_pdf_tables.py` regenerates [[pdf-table-verification-index-2026-05-06]] from source links in direction metrics matrices.

## Ingest Workflow for New Sources

1. Add source under `raw/sources/`.
2. Create or update the source page under `wiki/sources/`.
3. Add `deep-ingest-v2` only after the source page has the required sections.
4. Update the relevant direction source hub.
5. Update concept/synthesis/status pages if the source changes direction-level conclusions.
6. Update [[sources-index]], [[index]], and [[log]].

## Quantitative Claim Rule

Exact benchmark values are not publication-grade unless manually checked against original PDF result tables. Keep all unverified exact numbers in the relevant metrics matrix.

Use [[pdf-table-verification-index-2026-05-06]] to locate likely table pages before doing manual or rendered visual checks.

## Attachment Workflow

Use `raw/assets/` for local images or attachments. Raw assets are source material; do not modify them after capture.
