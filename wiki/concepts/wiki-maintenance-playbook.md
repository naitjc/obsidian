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
5. If the answer adds reusable synthesis, automatically create a new page using [[query-answer-template]].
6. Do not create a page for one-off operational answers, simple status answers, or local maintenance confirmations.
7. Update [[index]] and append to [[log]] whenever a query answer page is created.

## Query Answer Promotion Rule

Default rule selected by the user: the LLM should decide whether a query answer has long-term wiki value and automatically promote it when it does. Promotion is appropriate when the answer:

- synthesizes multiple sources or directions;
- creates a reusable comparison, taxonomy, timeline, decision record, or research hypothesis;
- resolves a tension between pages or records a caveat that should not be rediscovered later;
- identifies follow-up sources, gaps, or maintenance tasks that matter beyond the current chat.

Promotion is not appropriate for transient command output, local status updates, git/worktree housekeeping, simple yes/no answers, or answers that merely repeat an existing page without adding synthesis.

## Routine Lint Workflow

Run:

```bash
python3 scripts/lint_wiki.py
python3 scripts/wiki_inventory.py
python3 scripts/locate_pdf_tables.py
python3 scripts/check_source_tag_drift.py
python3 scripts/check_pdf_text_artifacts.py
```

Expected structural state:
- 0 broken wiki links
- 0 wiki pages missing required frontmatter
- 0 auto-ingest pages among numbered PDF source pages
- 100% source hub coverage for completed directions
- 0 source direction-tag mismatches against [[sources-index]]
- 0 control-character artifacts in source markdown pages

`scripts/locate_pdf_tables.py` regenerates [[pdf-table-verification-index-2026-05-06]] from source links in direction metrics matrices.

Use `python3 scripts/regenerate_source_hubs.py` to preview flat source-hub output from source page tags. Add `--write` only when intentionally replacing curated hub grouping with generated flat hub pages.

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
