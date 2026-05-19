---
created: 2026-05-19
updated: 2026-05-19
tags: [maintenance, checklist]
sources: []
---

# Wiki Maintenance Checklist

## Routine Checks

Run these after source ingestion, schema changes, or broad wiki maintenance:

```bash
python3 scripts/lint_wiki.py
python3 scripts/wiki_inventory.py
python3 scripts/check_source_tag_drift.py
python3 scripts/check_pdf_text_artifacts.py
```

Use these when relevant:

```bash
python3 scripts/locate_pdf_tables.py
python3 scripts/verify_pdf_metric_pages.py
python3 scripts/regenerate_source_hubs.py
```

Add `--write` to `scripts/regenerate_source_hubs.py` only when intentionally replacing curated hub grouping with generated flat hub pages.

## Expected Structural State

- 0 broken wiki links.
- 0 wiki pages missing required frontmatter.
- 0 non-exempt wiki orphan pages; intentional alias stubs or historical reports should be linked from a maintenance audit or archive page.
- 0 non-exempt duplicate wiki slugs; `index` is allowed because the vault has both the root wiki router and the maintenance router.
- 0 maintenance or lint pages directly under `wiki/concepts/`, except direction-level completion reports tagged `completion`.
- 0 source direction-tag mismatches against [[sources-index]].
- 0 control-character artifacts in source markdown pages.
- 0 `auto-ingest` pages among numbered PDF source pages when a direction is marked complete.
- Completed directions have source hubs, direction maps, status pages, and completion reports.

## Current Tool Inventory

- Structural lint: `python3 scripts/lint_wiki.py`
- Inventory summary: `python3 scripts/wiki_inventory.py`
- PDF table locator: `python3 scripts/locate_pdf_tables.py`
- PDF metric page verifier: `python3 scripts/verify_pdf_metric_pages.py`
- Source hub preview/regeneration: `python3 scripts/regenerate_source_hubs.py`
- Source tag drift check: `python3 scripts/check_source_tag_drift.py`
- PDF text artifact check: `python3 scripts/check_pdf_text_artifacts.py`
- Query answer template: `wiki/templates/query-answer-template.md`
- Local attachment target: `raw/assets/`
- Rendered PDF verification cache: `tmp/pdfs/`

## Link and Log Checklist

- New durable page is linked from [[index]] or a relevant hub page.
- New source page is linked from [[sources-index]] and the relevant source hub.
- Meaningful maintenance, ingest, or promoted query-answer changes are appended to `log.md`.
- Raw files remain untouched except for intentional source additions by the user.
