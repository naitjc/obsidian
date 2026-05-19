---
created: 2026-05-19
updated: 2026-05-19
tags: [maintenance, lint, navigation]
sources: []
---

# Navigation Audit 2026-05-19

## Scope

This audit checked structural lint, current inventory, source-tag drift, PDF text artifacts, and pages with no inbound wiki links after the maintenance-rule migration.

## Automated Checks

| Check | Result |
|---|---|
| `python3 scripts/lint_wiki.py` | 0 broken links, 0 missing frontmatter, 0 orphan pages, 0 duplicate slugs, 0 misplaced maintenance pages, direction hubs complete |
| `python3 scripts/wiki_inventory.py` | 163 raw PDFs, 307 wiki pages, 171 source pages, 95 concept pages, 18 entity pages, 21 maintenance pages |
| `python3 scripts/check_source_tag_drift.py` | 0 direction-tag mismatches |
| `python3 scripts/check_pdf_text_artifacts.py` | 0 offenders |

## Navigation Issues Found

The automated lint was clean, but a backlink scan found 11 pages with no inbound wiki links:

- Stable concept pages: [[chain-of-thought-prompting]], [[incongruity-theory]], [[persona-modeling]].
- Historical integrity reports: [[wiki-integrity-report-2026-04-29]], [[wiki-integrity-report-2026-05-05]].
- Legacy source aliases: [[chen-2024-socialbench]], [[elsherief-2021-latent-hatred]], [[jang-2025-inference-computation]], [[kim-2022-generalizable-implicit-hate]], [[zhang-2025-incongruity-aware-sarcasm]], [[zhao-2024-zerostance]].

## Changes Made

- Linked [[chain-of-thought-prompting]] from [[llm-reasoning]] because it is a reusable reasoning scaffold.
- Linked [[incongruity-theory]] from [[sarcasm-detection]] because it is the conceptual basis for expectation/observation conflict.
- Linked [[persona-modeling]] from [[role-playing-agents]] because persona representation is central to role-playing behavior.
- Routed historical integrity reports and legacy alias stubs through this audit page instead of deleting them.
- Added an orphan-page expectation to [[wiki-maintenance-checklist]].

## Follow-up Structural Cleanup

- Moved reusable maintenance playbook content from `wiki/concepts/` to `wiki/maintenance/`.
- Moved dated integrity reports, direction lint reports, the PDF table verification index, and the maintenance status snapshot from `wiki/concepts/` to `wiki/maintenance/reports/`.
- Extended `scripts/lint_wiki.py` to report duplicate wiki slugs and maintenance/lint pages misplaced under `wiki/concepts/`.
- Extended `scripts/wiki_inventory.py` to report `wiki/maintenance/` page counts.
- Removed non-source `.DS_Store` files outside `raw/`, `.git/`, and `tmp/`.

## Retained Exceptions

The legacy source alias pages are intentionally retained as redirect-like stubs to preserve older links and search habits. They should not be expanded into duplicate source summaries; the canonical numbered source page remains the evidence-bearing page.

The duplicate `index` slug is intentionally retained because the vault uses both `wiki/index.md` as the master router and `wiki/maintenance/index.md` as the maintenance router. Other duplicate wiki slugs should be treated as a lint failure.

## Boundary

This audit did not review the truth of source-derived claims or numeric metric values. It only checked navigation, structural consistency, and maintenance routing.
