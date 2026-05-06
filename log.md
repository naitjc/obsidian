# Log

## [2026-04-23] init | Wiki initialized
- Created AGENTS.md schema
- Created wiki directory structure
- Created index.md

## [2026-04-23] ingest | NLP Research Papers Collection
- 140 papers identified in raw/sources/
- Created [[nlp-research-collection]] overview
- Created 6 concept pages: Implicit Hate Speech, Stance Detection, Sarcasm Detection, Role-Playing Agents, Multimodal Hate Detection, LLM Reasoning
- Created 6 source summary pages
- Updated index.md

## [2026-04-23] ingest | Batch ingest of PDF sources
- Confirmed PDF parsers available (`pypdf`, `pdfplumber`)
- Parsed and indexed 149 PDF sources from `raw/sources/`
- Generated 149 source pages in `wiki/sources/`
- Built `wiki/sources/sources-index.md` catalog
- Updated `wiki/sources/nlp-research-collection.md`
- Updated `wiki/index.md`

## [2026-04-23] ingest | Hate speech direction deep-ingest v1
- Identified 39 hate-speech pages and upgraded 36 auto-ingest source pages with extracted abstracts and structured sections
- Added concept map: `wiki/concepts/hate-speech-research-map.md`
- Added supporting concept pages for datasets, generalization, and explainability
- Cross-linked hate-related concept pages and index entries

## [2026-04-23] lint | Hate speech direction v2 pass
- Upgraded 38 hate-speech source pages to deep-ingest-v2 template
- Added synthesis page: `wiki/concepts/hate-speech-sota-landscape.md`
- Added lint report: `wiki/concepts/hate-speech-lint-report-2026-04-23.md`
- Updated `wiki/index.md` with hate-direction analysis entry points

## [2026-04-23] maintain | Hate speech structure cleanup
- Added `wiki/concepts/hate-speech-source-hub.md` with grouped links to all hate-speech source pages
- Fixed broken concept links and added missing concept stubs (`explicit-hate-speech-detection`, `multimodal-learning`)
- Refreshed lint report: `wiki/concepts/hate-speech-lint-report-2026-04-23.md`
- Updated `wiki/index.md` and `wiki/concepts/hate-speech-research-map.md` navigation links

## [2026-04-23] research | Hate speech continuation pass
- Added `wiki/concepts/hate-speech-priority-papers.md` (top 10 queue)
- Rebuilt `wiki/concepts/hate-speech-source-hub.md` with improved thematic grouping
- Added benchmark-evidence line extraction to top hate papers
- Extended `wiki/concepts/hate-speech-sota-landscape.md` with contradiction tracker
- Refreshed lint report and updated index navigation

## [2026-04-23] research | Hate speech completion framework
- Added `wiki/concepts/hate-speech-metrics-matrix.md` for top-10 comparative tracking
- Added dataset normalization assets under `wiki/entities/` (alias map + dataset entity pages)
- Linked metrics matrix into `wiki/concepts/hate-speech-research-map.md` and `wiki/index.md`
- Prepared hate direction for table-verified quantitative pass

## [2026-04-23] research | Hate speech hardening pass
- Rewrote `wiki/concepts/hate-speech-metrics-matrix.md` to verification-oriented v2 format
- Added `wiki/concepts/hate-speech-direction-status.md` with completion criteria and current progress
- Linked status page from map and index for explicit direction-level tracking

## [2026-04-23] research | Hate speech direction completion pass
- Added `wiki/concepts/hate-speech-final-synthesis.md` with scenario-specific method conclusions
- Updated contradiction tracker with resolved direction-level findings
- Updated `wiki/concepts/hate-speech-direction-status.md` to complete (workflow level)
- Linked final synthesis in map and index

## [2026-04-23] maintain | Hate speech tail closure
- Finalized `wiki/concepts/hate-speech-metrics-matrix.md` status labels to `pending-manual-verification`
- Added verification blockers and close-out note in `wiki/concepts/hate-speech-direction-status.md`
- Marked direction as fully closed at workflow level with optional manual numeric verification

## [2026-04-23] maintain | Global wiki integrity fixes
- Normalized cross-page wiki links to slug targets and fixed source reference typos
- Added missing concept stubs for unresolved links (CoT, RAG, zero-shot, evaluation, etc.)
- Converted 6 duplicate legacy source pages into alias stubs to remove duplicate PDF mappings
- Added frontmatter to `wiki/index.md` and cleaned AGENTS link example syntax

## [2026-04-27] ingest | New hate-related resources
- Detected and ingested newly added PDF sources into `wiki/sources/`
- Rebuilt `wiki/sources/sources-index.md` and updated corpus totals
- Updated hate direction hub and status counts (`wiki/concepts/hate-speech-source-hub.md`, `wiki/concepts/hate-speech-direction-status.md`)
- Refreshed `wiki/index.md` and `wiki/sources/nlp-research-collection.md`

## [2026-04-29] maintain | Global wiki navigation optimization
- Checked global wiki link integrity and found 0 broken wiki links
- Expanded `wiki/index.md` into a navigation dashboard with inventory, entity, concept, source, and output sections
- Linked dataset entity pages through `wiki/entities/hate-speech-dataset-alias-map.md`
- Expanded `wiki/concepts/synthetic-data-generation.md` from a seed stub into a usable concept page
- Added `wiki/concepts/wiki-integrity-report-2026-04-29.md`
- Updated `AGENTS.md` status to match current wiki progress

## [2026-04-29] maintain | Hate speech detection direction completion
- Scoped completion work to the hate speech detection direction only
- Updated `AGENTS.md` with source/concept/synthesis conventions and hate speech direction completion rules
- Rebuilt `wiki/concepts/hate-speech-source-hub.md` into primary groups covering all 36 hate speech papers
- Normalized stale 37/38-paper scope references to 36 in direction status and synthesis pages
- Rewrote `wiki/concepts/hate-speech-metrics-matrix.md` as a conservative table-evidence verification workspace
- Added `wiki/concepts/hate-speech-completion-report-2026-04-29.md`
- Refreshed `wiki/index.md` links for the completion report

## [2026-05-05] maintain | Stance detection direction completion
- Upgraded 24 stance-tagged source pages from `auto-ingest` to `deep-ingest-v2`
- Added `wiki/concepts/stance-detection-source-hub.md` with all 24 stance papers
- Added stance direction map, SOTA synthesis, final synthesis, metrics workspace, lint report, status page, and completion report
- Updated `wiki/concepts/stance-detection.md` as the direction concept entry point
- Updated `AGENTS.md` to list stance detection as a completed direction for internal wiki use
- Refreshed `wiki/index.md` with stance direction entry points and current page counts
- Added `wiki/concepts/wiki-integrity-report-2026-05-05.md` after global link and frontmatter checks

## [2026-05-05] maintain | Remaining major directions completion
- Upgraded remaining auto-ingest pages for dialogue, LLM reasoning, sarcasm, role-playing, emotion recognition, and multimodal learning
- Corrected over-broad automatic direction tags by restoring primary direction tags from `wiki/sources/sources-index.md`
- Added source hubs, research maps, SOTA landscapes, final syntheses, metrics workspaces, lint reports, status pages, and completion reports for all remaining major directions
- Updated `AGENTS.md` and `wiki/index.md` to mark all major source-tagged directions complete for internal wiki use
- Refreshed `wiki/concepts/wiki-integrity-report-2026-05-05.md`

## [2026-05-06] maintain | Automation and cross-direction hardening
- Added reusable maintenance scripts: `scripts/lint_wiki.py` and `scripts/wiki_inventory.py`
- Added `scripts/locate_pdf_tables.py` and generated [[pdf-table-verification-index-2026-05-06]]
- Added `wiki/templates/query-answer-template.md` to support query answer write-back
- Created `raw/assets/` as the local attachment target
- Added [[global-research-map]], [[cross-direction-synthesis-2026-05-06]], [[wiki-maintenance-playbook]], and [[wiki-maintenance-status-2026-05-06]]
- Updated `AGENTS.md` and `wiki/index.md` with global entry points and maintenance tools
- Initialized a git repository at the vault root and added a minimal `.gitignore`
- Installed Poppler and visually verified two hate speech metric rows by rendering PDF result-table pages

## [2026-05-06] maintain | PDF table verification pass
- Used PDF rendering workflow to visually verify Zhang 2023 TOT Table 2 and upgrade its hate speech metrics row to `visually-verified`.
- Removed NUL control-character artifacts from PDF-derived markdown pages.
- Continued hate speech PDF table verification and upgraded the remaining priority metrics rows for ElSherief 2021, Hartvigsen 2022, Kim 2022, Sheth 2024, Hee 2024, Jiang 2025, and Mei 2025 to `visually-verified`.
- Continued stance detection PDF table verification and upgraded all stance priority metrics rows to `visually-verified`.

## [2026-05-06] maintain | Remaining PDF metrics verification closure
- Added `scripts/verify_pdf_metric_pages.py` to locate and render likely result-table pages for metrics rows still marked `pending-manual-verification`.
- Rendered 112 PDF pages under `tmp/pdfs/` for 56 unique PDFs and upgraded 69 remaining priority metrics rows across dialogue, emotion recognition, LLM reasoning, multimodal learning, role-playing agents, and sarcasm/humor to `visually-verified`.
- Reviewed contact sheets for the rendered pages and found no blank-page, black-square, clipping, or legibility blockers.
- Updated `wiki/concepts/wiki-maintenance-status-2026-05-06.md` and `AGENTS.md` to mark priority PDF metrics verification complete while keeping global cross-task SOTA ranking out of scope.
