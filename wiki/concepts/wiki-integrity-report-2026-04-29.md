---
created: 2026-04-29
updated: 2026-04-29
tags: [maintenance, lint, index]
sources: []
---

# Wiki Integrity Report 2026-04-29

## Scope

This pass checked the current wiki structure, navigation entry points, frontmatter coverage, wiki-link integrity, and orphan pages.

## Current Inventory

| Area | Count |
|---|---:|
| Markdown files total | 203 |
| Wiki pages | 200 |
| Concept pages | 30 |
| Source pages | 158 |
| Entity pages | 11 |
| Raw source PDFs | 150 |

## Link Integrity

| Check | Result |
|---|---|
| Broken wiki links | 0 found |
| Markdown files without frontmatter | 3 non-wiki files: `AGENTS.md`, `log.md`, `欢迎.md` |
| Wiki orphan pages before this pass | 17 |
| Wiki orphan pages after this pass | 6 legacy source alias stubs remain intentionally low-traffic |

## Changes Made

- Expanded [[index]] into a practical navigation dashboard with inventory, entity, concept, source, and output sections.
- Linked dataset entity pages through [[hate-speech-dataset-alias-map]] so dataset pages are no longer disconnected from the main graph.
- Expanded [[synthetic-data-generation]] from a seed stub into a usable concept page.
- Updated `AGENTS.md` status to reflect that initial ingestion, concept mapping, and entity creation are complete.

## Remaining Gaps

- The six legacy source alias stubs are intentionally retained as redirects to canonical source pages; they do not need stronger inbound links unless old notes depend on them.
- The hate speech metrics matrix remains marked for manual numeric verification. This report did not validate PDF table values.
- Many non-hate source pages are still auto-ingest summaries; deeper synthesis should be done by research direction rather than globally.
