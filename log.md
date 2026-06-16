# Log

## [2026-06-08] query-answer | Remote RA-HMD IHC implementation snapshot
- Inspected `nlp06:/data/cjt/hate/Try/RA-HMD` and updated [[rahmd-inspired-ihc-relation-adaptation-2026-06-05]] with the active project layout, stage-1/stage-2 scripts, dataset counts, saved Qwen3-4B seed-42 artifacts, feature paths, and latest Stage2 run status.
- Recorded that the one-epoch Stage1 run saved usable adapter and classifier artifacts before being marked failed by a post-save `evaluate(... do_sample=...)` API mismatch.
- Recorded that feature extraction succeeded and the latest CPU Stage2 one-epoch run completed, while earlier retries were mainly permission or FAISS/GPU related.
- Clarified that the current remote implementation is binary text-only IHC classification, not yet the candidate-level three-way relation-state design needed for the final relation-grounding method.

## [2026-06-06] ingest | Multimodal retrieval and retrieval-augmented defense PDFs
- Detected five new PDF files under `raw/sources/`; treated `raw/sources/2024.acl-long.291.pdf` as a duplicate of existing [[080-mei-2024-improving-hateful-meme-detection-through-retrieval-guided-contrastive-learning]] rather than creating a duplicate source page.
- Added four new deep-ingested source pages: [[188-lin-2023-fine-grained-late-interaction-multi-modal-retrieval-for-retrieval-augmented-visual-question-answering]], [[189-lin-2024-preflmr-scaling-up-fine-grained-late-interaction-multi-modal-retrievers]], [[190-yang-2025-retrieval-augmented-defense-adaptive-and-controllable-jailbreak-prevention-for-large-language-models]], and [[191-chen-2026-berag-bayesian-ensemble-retrieval-augmented-generation-for-knowledge-based-visual-question-answering]].
- Updated [[sources-index]], [[nlp-research-collection]], [[retrieval-augmented-generation]], [[multimodal-learning]], [[llm-reasoning]], [[llm-evaluation]], and regenerated the multimodal and LLM-reasoning source hubs.
- Refreshed [[index]] inventory counts for 192 raw PDF files, 191 unique indexed source PDFs, 199 source pages, 348 wiki pages, 38 multimodal source pages, and 48 LLM-reasoning source pages.
- Re-ran `scripts/lint_wiki.py`, `scripts/wiki_inventory.py`, `scripts/check_source_tag_drift.py`, and `scripts/check_pdf_text_artifacts.py`; no structural, routing, tag-drift, or PDF text-artifact failures were reported.

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

## [2026-05-08] query-answer | Using not_toxic targets for hate speech detection
- Added [[using-not-toxic-targets-for-hate-speech-detection]] to preserve a method-design answer on using LLM-extracted `not_toxic` targets as target-aware hard negatives.
- Connected the proposal to existing hate-speech wiki evidence on ToxiGen identity-term bias, STATE ToxiCN target-aware toxicity, implicit hate, contrastive learning, failure-guided robustness, and counterfactual hard-case generation.
- Updated [[index]] with the promoted query answer.

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

## [2026-05-06] maintain | Final automated maintenance closure
- Added non-hate benchmark and dataset entity map pages for stance, dialogue, LLM reasoning, sarcasm/humor, role-playing agents, emotion recognition, and multimodal learning.
- Added `scripts/regenerate_source_hubs.py`, `scripts/check_source_tag_drift.py`, and `scripts/check_pdf_text_artifacts.py`.
- Removed remaining control-character artifacts from `wiki/sources/008-2510-07707v2.md`.
- Verified source direction tags against `wiki/sources/sources-index.md` with 0 mismatches and verified source markdown pages with 0 control-character offenders.

## [2026-05-06] maintain | Automated backlog closure
- Refreshed [[index]] with current inventory counts and explicit deep-ingest/peripheral-source boundaries.
- Marked 21 source pages outside completed directions as `auto-ingest` / `peripheral-source` navigation nodes rather than implied deep-ingest evidence pages.
- Refreshed [[sources-index]] tag entries for peripheral sources and corrected the remaining blank catalog tag rows.
- Updated [[wiki-maintenance-status-2026-05-06]] and `AGENTS.md` to record the current automated maintenance boundary and retained PDF verification cache.

## [2026-05-06] maintain | Peripheral source deep-ingest alignment
- Upgraded the remaining 21 numbered PDF source pages from navigation nodes to `deep-ingest-v2` pages with the standard source-page sections.
- Normalized source frontmatter and rebuilt [[sources-index]] from the source pages.
- Regenerated all direction source hubs from source page frontmatter tags.
- Updated [[index]] and [[wiki-maintenance-status-2026-05-06]] to record 0 remaining auto-ingest numbered PDF source pages.

## [2026-05-12] query-answer | CADET and HARE target/category usage
- Added [[cadet-hare-target-category-usage]] explaining how CADET uses target/category labels as causal latent-factor supervision while HARE uses target/implied-statement annotations mainly for rationale prompting.
- Expanded the answer with how non-native fields are obtained: CADET uses native annotations where available, DynaHate heuristics, and GPT-4 style transformations with manual inspection; HARE uses GPT-3.5-generated rationales and falls back to Fr-HARE prompts when annotations are absent.
- Corrected the page after the user clarified that `category` means hate-speech type rather than explicit/implicit style.
- Clarified that CADET's optional target means target supervision is available-if-present, while HARE uses dataset free-text target group and implied-statement annotations rather than a new fixed target ontology.
- Updated [[index]] to include the new query answer.

## [2026-05-12] ingest | Recent pure-text hate speech papers
- Added 7 deep-ingested source pages for recent pure-text hate speech detection papers: [[151-salles-2025-hatebrxplain-a-benchmark-dataset-with-human-annotated-rationales-for-explainable-hate-speech-detection-in-brazilian-portuguese]], [[152-calabrese-2025-compositional-generalisation-for-explainable-hate-speech-detection]], [[153-mnassri-2025-rag-and-recall-multilingual-hate-speech-detection-with-semantic-memory]], [[154-boudraa-2025-implicit-hate-target-span-identification-in-zero-and-few-shot-settings-with-selective-sub-billion-parameter-models]], [[155-carvallo-2025-hate-explained-evaluating-ner-enriched-text-in-human-and-machine-moderation-of-hate-speech]], [[156-melis-2025-a-modular-taxonomy-for-hate-speech-definitions-and-its-impact-on-zero-shot-llm-classification-performance]], and [[157-ghorbanpour-2025-can-prompting-llms-unlock-hate-speech-detection-across-languages]].
- Regenerated [[hate-speech-source-hub]] and updated [[sources-index]], [[implicit-hate-speech-detection]], [[explainable-hate-speech-detection]], [[hate-speech-generalization-and-transfer]], [[hate-speech-datasets-and-benchmarks]], and [[index]].
- Marked these papers as pure-text additions covering rationales, compositional generalization, target span identification, NER intent/group enrichment, definition-sensitive prompting, multilingual prompting, and RAG/semantic memory.

## [2026-05-12] query-answer | Intent-slot style hate speech modeling
- Added [[intent-slot-style-hate-speech-modeling]] to preserve a method-design answer connecting local target leakage with intent-slot, NER enrichment, target-span tagging, and compositional generalization papers.
- Recommended reframing `target` from a sample-level feature into a structured relation among entity/group mentions, harmful intent, target link, and evidence spans.
- Updated [[index]] with the new query answer.

## [2026-05-17] ingest | New intent-slot and explainability papers
- Added 6 deep-ingest source pages: AGIF, DGM, HateXplain, MUDES, PLEAD, and OneIE.
- Regenerated [[hate-speech-source-hub]] and [[dialogue-systems-source-hub]], then updated [[sources-index]], [[nlp-research-collection]], [[explainable-hate-speech-detection]], [[hate-speech-datasets-and-benchmarks]], [[dialogue-systems]], [[intent-slot-style-hate-speech-modeling]], and [[index]].
- Treated OneIE as a peripheral structured extraction/global-constraint method node rather than a completed-direction source.

## [2026-05-17] query-answer | Hate speech intent-slot refactor plan
- Added [[hate-speech-intent-slot-refactor-plan]] to turn the prior intent-slot discussion into a concrete structured task schema and minimal experiment plan.
- Recommended deriving the final moderation verdict from mentions, intent labels, target links, and evidence spans rather than feeding target as a row-level shortcut.
- Updated [[index]] with the new query answer.

## [2026-05-18] query-answer | PLEAD follow-up trace
- Added [[plead-u-plead-target-follow-up-trace]] to record how PLEAD was extended through structured moderator explanations and U-PLEAD/TARGET compositional generalization.
- Noted that U-PLEAD/TARGET is too recent to support a broad downstream-use claim; the stronger use for IHC/SBIC is as a design template for target-expression balancing and structured evaluation.
- Updated [[index]] with the new query answer.

## [2026-05-18] query-answer | IHC/SBIC target completion layer
- Added [[ihc-sbic-target-completion-layer]] to specify the data-layer target completion step for intent-slot hate speech parsing on IHC and SBIC.
- Distinguished attacked targets, neutral mentioned targets, no relevant target, and uncertain target states to avoid target-presence leakage.
- Updated [[index]] with the new query answer.

## [2026-05-18] query-answer | LLM augmentation fields in related papers
- Added [[llm-augmentation-fields-in-related-papers]] to compare what related papers supplement with LLMs or span-level annotation.
- Recorded that related work typically adds task-aligned intermediate fields such as intent/group tags, target BIO spans, implicit targets, synthetic slot-balanced posts, or target-argument-hateful-group quadruples rather than fully relabeling natural datasets.
- Updated [[index]] with the new query answer.

## [2026-05-18] query-answer | IHC/SBIC hate speech innovation ideas
- Added [[hate-speech-innovation-ideas-ihc-sbic-2026-05-18]] to preserve initial innovation ideas grounded in the hate-speech wiki, related target-aware papers, and current IHC/SBIC fine-tuning outputs on `xu-l20`.
- Recorded that the strongest local signal is class-target coupling: false positives tend to generate targets for target-empty non-toxic rows, while false negatives tend to drop gold targets for toxic rows.
- Recommended leakage-resistant target-relation completion, target-conditioned evaluation, bad-case curricula, compositional target-expression splits, and a small intent layer as first research directions.
- Updated the page with the user's filled-not-toxic target-input experiments from `FineTune_filled_not_toxic`: normal target-input evaluation gives near-perfect macro-F1, while target shuffling or replacing targets with `other` collapses performance, confirming row-level target-input leakage.
- Added [[leakage-resistant-target-relation-modeling]] to refine the user's proposal into a focused paper thesis: replace row-level target-aware classification with candidate-target relation classification.
- Noted the supporting structure: target-shortcut evaluation, same-target contrastive pairs, hard-negative mining, lightweight intent labels, and target ontology normalization should serve the relation-aware main claim rather than appear as separate innovations.
- Added [[target-relation-modeling-reject-review]] to preserve the strict rejection case against the target-relation thesis, including risks around self-inflicted leakage, artificial shortcut tests, relation-label validity, candidate generation, novelty, and overclaiming understanding.
- Updated [[target-relation-modeling-reject-review]] and [[leakage-resistant-target-relation-modeling]] with a stricter defensible revision: same candidate-generation pipeline for toxic and not-toxic rows, external transfer tests, manually audited relation labels, cleaner relation/uncertainty schema, and conservative claims about shortcut reduction rather than understanding.
- Added a concrete revised plan to [[leakage-resistant-target-relation-modeling]]: uniform candidate generation, clean relation labels, manual audit, relation-model baselines, cross-dataset evaluation, diagnostic shortcut tests, and explicit stop/reframe criteria.
- Clarified that LLM-filled `not_toxic` targets are a local diagnostic and should not be framed as the paper's core field-level problem; the broader problem is target annotation asymmetry and target shortcuts under leakage-controlled candidate generation.
- Reframed [[leakage-resistant-target-relation-modeling]] to start from existing-paper gaps: target/span/intent/rationale methods add structure but do not jointly control candidate construction, relation supervision, target-present non-hateful examples, and cross-dataset shortcut evaluation.
- Broadened [[leakage-resistant-target-relation-modeling]] beyond a few target-aware papers to 2024+ hate speech detection trends: definition shift, implicit pragmatics, target framing, transfer, explanation reliability, LLM inconsistency, weak/synthetic label risk, and multimodal/multicultural grounding.
- Added a scope-expansion note to [[leakage-resistant-target-relation-modeling]]: the direct target-aware papers are evidence anchors, while the actual literature motivation should cover the shared 2024+ problem of unstable semantic grounding under definition, context, target, language, platform, and modality shifts.
- Added [[cross-direction-innovation-ideas-2026-05-18]] to preserve preliminary innovation ideas derived from the wiki's cross-direction common problems.
- Proposed five candidate lines: definition/target-controlled semantic grounding, curation-first synthetic hard cases, verifiable reasoning schemas, evidence-role multimodal alignment, and benchmark sensitivity cards.
- Marked the ideas as proposal-level syntheses pending direction-specific literature and experiment verification.
- Recorded the user's prioritization that the near-term work should focus on the first three lines: controlled semantic grounding, curation-first synthetic hard cases, and verifiable reasoning.
- Added [[hate-speech-grounding-directions-review-2026-05-18]] to assess the novelty and feasibility of the first three hate-speech directions from a critical reviewer perspective.

## [2026-05-21] ingest | Target-relation hate speech literature additions
- Added 6 deep-ingested source pages for target-relation-relevant hate/offensive-language papers: [[164-elsherief-2018-hate-lingo-a-target-based-linguistic-analysis-of-hate-speech-in-social-media]], [[165-zampieri-2019-predicting-the-type-and-target-of-offensive-posts-in-social-media]], [[166-davidson-2019-racial-bias-in-hate-speech-and-abusive-language-detection-datasets]], [[167-chandra-2020-abuseanalyzer-abuse-detection-severity-and-target-prediction-for-gab-posts]], [[168-yu-2022-hate-speech-and-counter-speech-detection-conversational-context-does-matter]], and [[169-zampieri-2023-target-based-offensive-language-identification]].
- Added [[target-relation-grounding-literature-map]] to route target category, target-expression span, context modifier, and shortcut/bias evidence for the active relation-grounded hate detection discussion.
- Updated [[hate-speech-source-hub]], [[sources-index]], [[nlp-research-collection]], [[index]], [[hate-speech-research-map]], [[hate-speech-final-synthesis]], [[hate-speech-direction-status]], [[explainable-hate-speech-detection]], [[hate-speech-datasets-and-benchmarks]], [[intent-slot-style-hate-speech-modeling]], [[hate-speech-intent-slot-refactor-plan]], [[leakage-resistant-target-relation-modeling]], and [[candidate-target-relation-grounding-experiment-plan-2026-05-18]].
- Recorded [[wiki-integrity-report-2026-05-21]] after `scripts/wiki_inventory.py`, `scripts/lint_wiki.py`, `scripts/check_source_tag_drift.py`, and `scripts/check_pdf_text_artifacts.py` all passed.
- Recommended using definition-controllable candidate-target relation grounding as the main contribution, with governed synthetic hard cases as the data/evaluation engine and verifiable structured reasoning as the reliability layer.
- Added [[candidate-target-relation-grounding-experiment-plan-2026-05-18]] to turn the converged paper framing into an experimental sequence.
- Proposed phases for shortcut diagnostics, uniform candidate generation, relation/evidence labeling, model baselines, curated hard-case generation, robustness evaluation, faithfulness tests, and accept/reject criteria.
- Clarified the core method as a definition-conditioned candidate-target relation grounding model: `f(content, candidate_target, definition_frame) -> relation_state, evidence, uncertainty`, with the row-level verdict derived from attacked candidate relations.
- Added worked examples to [[candidate-target-relation-grounding-experiment-plan-2026-05-18]] covering explicit attack, target-present benign mention, counterspeech, definition-sensitive labeling, and evidence deletion.

## [2026-05-06] lint | Post-alignment integrity report
- Added [[wiki-integrity-report-2026-05-06]] with current inventory, direction hub coverage, source tag drift, PDF text artifact, and pending metrics verification status.
- Updated [[global-research-map]], [[index]], and [[wiki-maintenance-playbook]] to point to the current integrity state.

## [2026-05-06] maintain | Hate speech source quality pass
- Replaced file-ID display titles with real paper titles for five hate-speech source pages and synchronized aliases in source indexes and hubs.
- Removed low-confidence `multimodal` and `cross-lingual` tags from clearly text-only or non-cross-lingual hate-speech source pages.
- Cleaned noisy PDF-extraction bullets in eight high-impact hate-speech source pages while preserving source files and stable slugs.
- Cleaned residual `Benchmark Evidence Lines` noise from five already reviewed hate-speech source pages (`031`, `043`, `056`, `081`, and `095`) and replaced it with concise evidence-handling notes.

## [2026-05-06] maintain | Selected publication-grade metrics check
- User selected hate speech and LLM reasoning for publication-grade priority metrics checking.
- Upgraded [[hate-speech-metrics-matrix]] priority rows to `publication-checked` where the listed exact values had already been visually checked against rendered PDF tables.
- Added table-checked values and source-statement ranges to all [[llm-reasoning-metrics-matrix]] priority rows, marking exact table rows and approximate author-reported ranges explicitly.
- Updated [[wiki-maintenance-status-2026-05-06]], [[wiki-integrity-report-2026-05-06]], and `AGENTS.md` to record the selected publication-grade boundary.

## [2026-05-06] maintain | High-impact source-summary cleanup
- User selected high-impact source-summary review for hate speech and LLM reasoning rather than all directions.
- Cleaned PDF-extraction fragments and removed stale `Benchmark Evidence Lines` sections from selected priority source pages: Mei 2024 RGCL, Hee 2024 cross-modality ICL, Kim 2022 ImpCon, Yang 2024 UCA, Zhang 2023 TOT, Cocchieri 2025 PHUNNY, Fu 2025 LaERC-S, Han 2025 RWG, He Crab, Ji 2025 DyMCA/HCTA, Lan 2024 Avalon agents, and Li 2025 BEHAVIORCHAIN.
- Removed misleading `cross-lingual` tags from the Hee 2024 cross-modality page and Kim 2022 cross-dataset page, and synchronized [[sources-index]].
- Re-ran structural lint, inventory, source tag drift, and PDF artifact checks successfully.

## [2026-05-06] maintain | Query answer promotion rule
- User selected automatic promotion for query answers with durable wiki value.
- Updated `AGENTS.md`, [[wiki-maintenance-playbook]], [[query-answer-template]], [[wiki-maintenance-status-2026-05-06]], and [[wiki-integrity-report-2026-05-06]].
- Future durable synthesis answers should be filed as wiki pages and logged; transient operational answers should not be promoted.

## [2026-05-19] maintain | Rule and experiment workflow migration
- Replaced root `AGENTS.md` with a concise global routing rule set adapted from the provided newer structure while keeping this vault's original research directions.
- Added root `EXPERIMENTS.md` for experiment artifact, run tracking, scoring, and promotion rules.
- Added `wiki/maintenance/` pages for schema, frontmatter conventions, task routing, maintenance checks, and the completed research direction registry.
- Updated [[index]] with the maintenance entry points and current wiki page count.

## [2026-05-19] experiment | xu-l20 hate experiment evidence snapshot
- Archived selected evidence from `xu-l20:/data/chenjt/hate` into `experiments/hate/xu-l20-snapshot-2026-05-19/`.
- Preserved IHC/SBIC fine-tuning metrics, predictions, false positives/false negatives, error summaries, configs, scripts, processed data, filled-not-toxic target diagnostics, and old Hidden CoT trial evidence.
- Deliberately did not copy large checkpoint artifacts such as adapter weights, tokenizer JSON files, training args binaries, Python bytecode, or large original HARE dumps.

## [2026-05-19] maintain | Navigation audit and orphan-page cleanup
- Added [[navigation-audit-2026-05-19]] to record the structural check, backlink audit, retained alias-stub boundary, and current automated check results.
- Reconnected [[chain-of-thought-prompting]], [[incongruity-theory]], and [[persona-modeling]] from their corresponding direction entry pages.
- Routed older integrity reports and legacy source alias stubs through the navigation audit instead of deleting them.
- Updated [[index]], [[wiki-maintenance-checklist]], and `wiki/maintenance/index.md` routing for the new audit.

## [2026-05-19] maintain | Maintenance namespace cleanup
- Moved [[wiki-maintenance-playbook]] into `wiki/maintenance/` and moved dated lint, integrity, verification, and status reports into `wiki/maintenance/reports/`.
- Kept direction completion reports and research status pages under `wiki/concepts/` because they remain direction-level research outputs.
- Extended `scripts/lint_wiki.py` to flag duplicate wiki slugs and maintenance/lint pages misplaced under `wiki/concepts/`.
- Extended `scripts/wiki_inventory.py` to report maintenance page counts and refreshed [[index]] with the updated concept/maintenance split.
- Removed non-source `.DS_Store` files outside `raw/`, `.git/`, and `tmp/`.

## [2026-05-20] query-answer | Intent-slot not-toxic slot completion refinement
- Updated [[hate-speech-intent-slot-refactor-plan]] to assess the proposed not-toxic slot-completion strategy: keyword matching can bootstrap candidate targets, LLMs can fill ambiguous or unmatched rows, but missing targets should remain `no_relevant_target` rather than being force-filled.
- Updated [[ihc-sbic-target-completion-layer]] with a concrete first-pass completion rule separating candidate target generation, relation state, non-hate explanation, uncertainty, and `hate_class`/harm-subtype handling.
- Recorded that `threat` versus `non_threat` is only a coarse harmful-intent dimension; not-toxic examples should use `neutral/no_hate_intent` plus relation states such as `mentioned_not_attacked` or `no_relevant_target`.

## [2026-05-25] query-answer | IHC completion alignment with recent target-aware papers
- Updated [[ihc-sbic-target-completion-layer]] after checking the recently added Boudraa, Carvallo, Calabrese, and HARE sources against the target-completion implementation decision.
- Recorded that Boudraa uses an `80/10/10` stratified IHC split, Carvallo creates GPT tag supervision from training partitions, and U-PLEAD/TARGET balances synthetic combinations rather than constructing split-specific IHC target lexicons.
- Selected one train-toxic native-target lexicon over per-split lexicons for the current IHC completion prototype; generated not-toxic statements remain weak labels requiring audit.
- Cleaned obsolete failed-run outputs and temporary validation artifacts from the remote `llm_restructed` working directory after the revised pipeline passed structural and failure-deferral checks.
- User selected the unpruned lexicon condition for the first target-matching run: all native train-toxic target terms are retained, with placeholder and person-name matches tracked as an audit risk rather than silently removed.
- Recorded the first-stage IHC execution checkpoint: 8,563 lexical matches plus 4,145 completed target-LLM rows, leaving 499 deferred rows; noted 666 anomaly-term lexical matches and 32 unnamed `implicit_target` rows for audit before statement generation.
- Updated the target-completion checkpoint after rerun: only 13 current remaining rows persist, all with `empty_llm_response`; per-split remaining files supersede the cumulative deferred-attempt log for active work.

## [2026-05-27] query-answer | Missing annotation completion and utility literature map
- Added [[missing-annotation-completion-and-utility-literature-map]] after web verification of missing-data, synthetic-data utility, and IHC/SBIC-adjacent target/explanation literature.
- Distinguished annotation-policy and class-conditioned target absence from generic random value imputation, and recorded that a formal MAR/MNAR claim requires a stated probabilistic missingness model.
- After the user requested deduplication, excluded papers already represented in the vault, including SBIC, IHC, PLEAD, Boudraa, Hate Explained, HateCheck, DynaHate, ToxiGen, and U-PLEAD.
- Routed new-to-vault readings through incomplete-annotation NER, partially annotated and positive-unlabeled relation extraction, generation-bias evaluation, missing-data foundations, and the 2026 HARM explanation-evaluation paper.
- Recorded a minimum validation protocol: preserve native labels, use training-only construction resources, audit weak completions, test target shortcuts, and evaluate on untouched and cross-dataset/functional sets.
- Updated [[index]] with the new durable query answer.

## [2026-05-27] experiment | IHC/SBIC full-statement output condition
- Added the `full_statement` output condition on `xu-l20` for text-only IHC/SBIC fine-tuning: the model generates `class`, `hate_class`, `target`, and `statement`.
- Archived the completed eight-run evidence set in `experiments/hate/xu-l20-full-statement-2026-05-27/`, including metrics, predictions, errors, processed data with `statement`, scripts, source code, and logs while excluding large checkpoint artifacts.
- Recorded that `full_statement` reaches Macro F1 `0.8354` on IHC and `0.8787` on SBIC at best, without exceeding the existing `class_target` best runs; statement Jaccard remains low (`0.0438-0.0533`).
- Recorded the comparability limitation: IHC/Mistral completed with per-device train batch size `8`, while the remaining seven `full_statement` runs used batch size `2`.

## [2026-05-27] ingest | Partial annotation, explanation evaluation, and agenda sources
- Added source pages [[170-ning-2018-exploiting-partially-annotated-data-for-temporal-relation-extraction]], [[171-jie-2019-better-modeling-of-incomplete-annotations-for-named-entity-recognition]], [[172-mayhew-2019-named-entity-recognition-with-partially-annotated-training-data]], and [[173-xie-2021-revisiting-the-negative-data-of-distantly-supervised-relation-extraction]] as method analogues for incomplete span/relation supervision.
- Added [[174-casula-tonelli-2023-generation-based-data-augmentation-for-offensive-language-detection-is-it-worth-it]] and [[176-puppi-vecchi-2026-harm-learning-hate-aware-reward-model-for-evaluating-natural-language-explanations-of-offensive-content]] for generated-data robustness and generated-explanation fidelity evaluation.
- Added [[175-zhang-2024-graph-induced-syntactic-semantic-spaces-in-transformer-based-variational-autoencoders]] as a peripheral latent-representation source and [[177-natural-language-understanding-topic-reflections]] as a research-agenda input rather than empirical benchmark evidence.
- Routed these additions through [[missing-annotation-completion-and-utility-literature-map]], [[target-relation-grounding-literature-map]], [[explainable-hate-speech-detection]], [[synthetic-data-generation]], [[latent-space]], [[llm-evaluation]], and the affected direction hubs.
- Updated [[sources-index]], [[nlp-research-collection]], and [[index]] to represent 177 PDF documents and 177 deep-ingested source pages.
- Verified the updated wiki with `scripts/lint_wiki.py`, `scripts/wiki_inventory.py`, `scripts/check_source_tag_drift.py`, and `scripts/check_pdf_text_artifacts.py`; all checks passed on 2026-05-27.

## [2026-05-27] query-answer | Supplementary dataset decision for IHC/SBIC target relations
- Updated [[hate-speech-datasets-and-benchmarks]] to separate primary development corpora from external structured evaluation, functional diagnostics, and deferred explanation-stage resources.
- Selected IHC/SBIC as the core audited relation corpora, TBO as the closest structured external resource, and HateXplain plus HateCheck as rationale/bias and shortcut-diagnostic complements.
- Recorded that PLEAD and context-aware Reddit are conditional additions for policy-slot or conversational claims, while bulk generated augmentation and SBIC-Explain/HARM should not be introduced into the first target-relation classifier stage.

## [2026-05-27] query-answer | Completion scope narrowed to IHC and SBIC only
- Clarified that the current supplementation task applies only to IHC and SBIC; no third dataset is part of the immediate data-completion pipeline.
- Revised [[hate-speech-datasets-and-benchmarks]] so TBO, HateXplain, HateCheck, PLEAD, context-aware Reddit, and span resources remain future evaluation references rather than selected current supplements.
- Fixed the current target schema objective as comparable `attacked_target`, `mentioned_not_attacked`, `no_relevant_target`, and `uncertain_target` states with retained provenance and audit status in both corpora.

## [2026-05-31] maintenance | Full wiki publication pass
- Ran the global structural, inventory, source-tag drift, and PDF text artifact checks after the 2026-05-27 source additions and IHC/SBIC experiment archive import.
- Added [[wiki-integrity-report-2026-05-31]] and refreshed [[index]] plus the maintenance router to point to the current verified state: 177 raw PDFs, 325 wiki pages, 185 source pages, 23 maintenance pages, and no reported integrity failures.
- Added experiment archive hygiene rules to `EXPERIMENTS.md`, ignored interpreter caches and PID files, and removed copied Python bytecode plus a stale PID before publication.
- Kept derived experiment datasets, per-example JSONL outputs, and execution logs local because the GitHub repository is public; the publication scope contains README files, code, configs, aggregate metrics, and non-sample summaries.
- Kept source PDFs immutable and excluded local Obsidian workspace UI state from the publication scope.

## [2026-05-31] query-answer | Privacy Filter bridge for span-grounded hate detection
- Added [[privacy-filter-inspired-span-grounded-hate-detection]] after inspecting `xu-l20:/data/chenjt/hate/clone/privacy-filter` and the local IHC/SBIC/PLEAD data shapes.
- Recorded the recommended use of the Privacy Filter architecture as a bidirectional BIOES span extractor for `target_mention` and `attack_evidence`, followed by candidate-target relation classification.
- Kept the main research claim scoped to leakage-resistant target-relation grounding; direct architecture reuse, PII-first moderation, and unified PII/harm extraction remain baseline or follow-up directions.
- Linked the new answer from [[intent-slot-style-hate-speech-modeling]] and [[index]].
- Re-ran `scripts/lint_wiki.py` and `scripts/wiki_inventory.py`; the wiki now contains 326 pages and 98 concept pages with no reported structural failures.

## [2026-05-31] query-answer | Deduplicated NLP reading route for target grounding
- Added [[recent-nlp-reading-route-for-target-grounding-2026-05-31]] after checking `wiki/`, `experiments/`, `log.md`, and `raw/sources/` for existing coverage.
- Kept the highest-priority readings close to the active IHC/SBIC work: implicit harmful-content target spans, LLM-generated functional tests, and target-identity moderation audits.
- Expanded the route into adjacent reusable methods: open-label span extraction, zero-shot relation extraction, concept-level NER, guideline-conditioned information extraction, uncertainty-aware annotation, dialect audits, moderation-system inconsistency, and efficient specialist moderation models.
- Updated [[index]] to route the new query answer.

## [2026-06-01] query-answer | 2025-2026 reading route addendum
- Extended [[recent-nlp-reading-route-for-target-grounding-2026-05-31]] with deduplicated 2025-2026 papers after re-checking local coverage and ACL Anthology publication records.
- Prioritized 2026 explanation-evaluation work on causal span grounding, protected-group identification, argument consistency, and annotator disagreement modeling.
- Added 2025 references for pragmatic inference in implicit toxic language, cross-domain hate-speech definition variation, and multilingual multi-hop explanation evaluation.
- Corrected the ACL Anthology links and venue metadata for `Who Speaks Matters` and `Model-Dependent Moderation`.

## [2026-06-01] query-answer | arXiv-first reading route addendum
- Extended [[recent-nlp-reading-route-for-target-grounding-2026-05-31]] with a deduplicated arXiv-first section.
- Added new-to-vault 2025-2026 arXiv readings for community-driven implicit-hate agents, fine-grained multimodal moderation semantics, transferable hate prototypes, cross-cultural human-LLM moderation, and faithfulness evaluation for toxicity explanations.
- Separated new arXiv-first readings from arXiv versions of already recommended conference papers so version tracking does not create duplicate recommendations.

## [2026-06-01] query-answer | Integrated paper summaries and reading priorities
- Added an integrated priority matrix to [[recent-nlp-reading-route-for-target-grounding-2026-05-31]] covering 24 unique papers.
- Separated immediate experiment-design readings, baseline-construction references, evaluation-section readings, and deliberate later extensions.
- Kept five arXiv links for conference-paper version tracking outside the unique-paper count.

## [2026-06-01] query-answer | P0 reading synthesis and experiment alignment
- Added [[p0-target-grounding-reading-synthesis-2026-06-01]] after the user browsed the six P0 papers.
- Consolidated source-grounded constraints for candidate-span extraction, identity-sensitive functional tests, NLI-filtered hard-case generation, structured explanation metrics, optional pragmatic traces, and modular definition frames.
- Updated [[candidate-target-relation-grounding-experiment-plan-2026-05-18]] with explicit-versus-implicit candidate recall, minimal evidence-span output, and emotional-disapproval functional slices.
- Corrected reading-route metadata and links: Jafari et al. for target-span detection, Jin et al. at LREC-COLING 2024 for GPT-HateCheck, Jin et al. at NAACL 2025 for `What the #?*!`, and GLiNER at NAACL 2024 Long Papers.
- Updated [[index]] to route the new synthesis page.

## [2026-06-01] ingest | Five local P0 follow-up PDFs
- Detected five user-added immutable PDFs under `raw/sources/` and added deep-ingested source pages [[178-jafari-2024-target-span-detection-for-implicit-harmful-content]], [[179-zaratiana-2024-gliner-generalist-model-for-named-entity-recognition-using-bidirectional-transformer]], [[180-chen-wang-2025-pragmatic-inference-chain-improving-llms-reasoning-of-authentic-implicit-toxic-language]], [[181-korre-2025-untangling-hate-speech-definitions-a-semantic-componential-analysis-across-cultures-and-domains]], and [[182-hu-lee-2026-hatexscore-a-metric-suite-for-evaluating-reasoning-quality-in-hate-speech-explanations]].
- Updated [[sources-index]], [[nlp-research-collection]], [[target-relation-grounding-literature-map]], and [[index]] for 182 raw PDFs and 182 deep-ingested PDF source pages.
- Kept GPT-HateCheck and `What the #?*!` as external links because corresponding local PDFs were not present.

## [2026-06-01] lint | Post-P0-ingest integrity report
- Added [[wiki-integrity-report-2026-06-01]] after all structural, inventory, source-tag drift, and PDF text-artifact checks passed.
- Updated [[index]] and the maintenance router to point to the current verified state: 182 raw PDFs, 334 wiki pages, 190 source pages, 100 concept pages, 24 maintenance pages, and no reported integrity failures.

## [2026-06-01] query-answer | Dual-view target-statement relation alignment
- Added [[dual-view-target-statement-relation-alignment]] to specify how completed `not_toxic.target` and `not_toxic.statement` fields should be used downstream.
- Used [[175-zhang-2024-graph-induced-syntactic-semantic-spaces-in-transformer-based-variational-autoencoders]] as a bounded structural analogy: separate heterogeneous views and align them, without claiming direct hate-speech evidence or requiring a VAE.
- Recommended `(text, candidate_target) -> relation_state` as the inference path and `statement` as a training-only semantic teacher with provenance weighting, statement-type normalization, matched-view alignment, and same-target hard negatives.
- Updated [[ihc-sbic-target-completion-layer]], [[using-not-toxic-targets-for-hate-speech-detection]], and [[index]] to route the downstream decision.

## [2026-06-02] experiment | Strict target completion and statement pilot
- Completed the four-model IHC strict target-completion ablation on `xu-l20`, comparing `class_target_toxic_only` with `class_target_all_rows`.
- Recorded that preserving non-toxic targets improves toxic-target Jaccard for all four models, while Macro F1 improves only for Qwen3-8B (`0.8153 -> 0.8215`).
- Completed five Qwen3-4B statement-pilot conditions using train-only generated non-toxic statements and statement-free inference evaluation.
- Recorded `s2_text_only_1x` as the strongest classification pilot condition (`0.8287` Macro F1 versus the `0.8210` target-all reference), while target metrics do not improve consistently.
- Updated [[dual-view-target-statement-relation-alignment]] with the pilot tables and retained the recommendation to use statements as controlled training-only semantic supervision rather than row-level inference input.
- Reorganized `xu-l20:/data/chenjt/hate/FineTune`: documented all 45 completed adapters, archived completed logs and one-off queue scripts, removed stale PID files, and verified all adapter, metrics, prediction, and error-summary artifacts.

## [2026-06-02] query-answer | Privacy Filter architecture review and direct-conversion decision
- Re-inspected `xu-l20:/data/chenjt/hate/clone/privacy-filter` at the implementation level, covering the bidirectional local attention stack, sparse MoE routing, BIOES output head, Triton path, Viterbi decoding, checkpoint loading, training loss, and runtime output flow.
- Updated [[privacy-filter-inspired-span-grounded-hate-detection]] to distinguish useful architectural lessons from an immediate engineering recommendation.
- Recorded that direct OPF conversion is not the current implementation route: replacing PII labels only yields a span tagger, while a complete hate-speech detector still requires sentence-level heads, relation modeling, new losses, moderation outputs, long-text aggregation, evaluation changes, and a separately obtained checkpoint.
- Retained `target_mention` and `attack_evidence` span extraction plus constrained decoding as bounded design references, with task-native encoder and open-label extraction baselines prioritized before any OPF efficiency baseline.
- Updated [[intent-slot-style-hate-speech-modeling]] and [[index]] to route the narrowed decision.

## [2026-06-04] ingest | Four local structured-output and safety-alignment PDFs
- Detected four local PDFs without source notes and added deep-ingested pages [[183-li-2024-large-language-models-as-zero-shot-dialogue-state-tracker-through-function-calling]], [[184-ao-2025-safe-pruning-lora-robust-distance-guided-pruning-for-safety-alignment-in-adaptation-of-llms]], [[185-park-kim-2026-inference-time-vulnerability-beyond-shallow-safety-alignment-along-generation-trajectories]], and [[186-reddy-2026-biasgrpo-stabilizing-bias-mitigation-in-high-variance-reward-landscapes-via-group-relative-policy-optimization]].
- Treated the five other untracked PDFs as already-ingested P0 source files because they are referenced by source pages 178-182.
- Updated [[sources-index]], [[nlp-research-collection]], generated dialogue and LLM-reasoning source hubs, and refreshed [[index]] inventory counts for 186 raw PDFs and 186 deep-ingested PDF source pages.
- Re-ran `scripts/lint_wiki.py`, `scripts/wiki_inventory.py`, `scripts/check_source_tag_drift.py`, and `scripts/check_pdf_text_artifacts.py`; no structural, routing, tag-drift, or PDF text-artifact failures were reported.

## [2026-06-05] query-answer | Full IHC completion method reassessment
- Inspected `xu-l20:/data/chenjt/hate/DATA/llm_restructed` after full IHC target and statement completion: all `13,207` `not_toxic` rows now have three generated statement conditions, and `9,587` `not_toxic` rows have non-empty targets.
- Recorded that `9,411` `not_toxic` rows are `mentioned_not_attacked`, making target-present benign rows the main resource for leakage-resistant relation modeling and same-target hard negatives.
- Added the full-scale Qwen3-4B statement results from `FineTune/experiments/statement_full_v1`: `text_label_target_1x` gives the strongest Macro F1 (`0.8235`) and toxic-target Jaccard (`0.3746`), but all full-statement conditions reduce all-row target Jaccard.
- Updated [[dual-view-target-statement-relation-alignment]] to recommend a constrained relation-alignment prototype: inference uses `(text, candidate_target) -> relation_state`, while generated statements are masked, provenance-aware training-only semantic views.

## [2026-06-05] query-answer | Multimodal-inspired IHC relation methods
- Added [[multimodal-inspired-ihc-relation-methods-2026-06-05]] after inspecting `xu-l20:/data/chenjt/hate/DATA/llm_restructed` and `xu-l20:/data/chenjt/hate/FineTune`.
- Translated multimodal hate-detection ideas into the completed IHC setting: retrieval-guided hard examples, ground-statement dual-view alignment, uncertainty-gated weak supervision, cross-dataset support transfer, and optional target-alias graph features.
- Recommended a candidate-level relation model where inference uses `(text, candidate_target) -> relation_state`; generated statements and retrieved examples are support signals rather than mandatory row-level classifier inputs.
- Updated [[index]] to route the new method-design answer and refreshed the wiki inventory counts after `scripts/lint_wiki.py` and `scripts/wiki_inventory.py` passed.
- Added the user constraint that the dataset should not be manually increased, reduced, rewritten, or relabeled; the method is limited to existing artifacts, candidate-level views, retrieval indexes, loss construction, sample weighting, artifact masking, and evaluation slices.
- Added the user constraint that the core model should be a small-parameter generative LLM such as Qwen2.5 or Qwen3, implemented through constrained JSON generation and lightweight QLoRA rather than a large encoder-only or full multimodal architecture.

## [2026-06-05] query-answer | Completed-IHC small-LLM innovation ideas
- Added [[ihc-completed-small-llm-innovation-ideas-2026-06-05]] after rechecking the hate-speech wiki, target-relation synthesis pages, and `xu-l20` IHC completion and FineTune summaries.
- Ranked the next research ideas under the updated constraints: candidate-target relation JSON SFT, retrieval-guided relation memory, statement-as-teacher alignment, definition-frame probing, evidence-cue faithfulness tests, relation-adapter reliability, and SBIC support/transfer tests.
- Rejected data augmentation, direct row-level target/statement concatenation, large graph-first designs, and long chain-of-thought generation as first-line directions for the current project state.
- Updated [[index]] to route the new broad method-planning answer.
- Re-ran `scripts/lint_wiki.py` and `scripts/wiki_inventory.py`; the wiki now contains 341 pages and 103 concept pages with no reported structural failures.

## [2026-06-05] query-answer | RA-HMD-inspired IHC relation adaptation
- Added [[rahmd-inspired-ihc-relation-adaptation-2026-06-05]] after checking the RA-HMD source page and PDF method sections.
- Mapped RA-HMD's projection head, auxiliary classifier, two-stage training, FAISS hard-neighbor contrastive tuning, and retrieval-augmented KNN inference into the completed-IHC candidate-target relation task.
- Specified the local version as small generative LLM JSON SFT plus a relation embedding path: stage 1 optimizes `L_json + L_rel`, stage 2 freezes the LLM and optimizes `L_rel + L_contrast`, and inference compares JSON, relation-head, and retrieval-KNN modes.
- Updated [[multimodal-inspired-ihc-relation-methods-2026-06-05]], [[ihc-completed-small-llm-innovation-ideas-2026-06-05]], and [[index]] to route the focused RA-HMD adaptation page.
- Re-ran `scripts/lint_wiki.py` and `scripts/wiki_inventory.py`; the wiki now contains 342 pages and 104 concept pages with no reported structural failures.

## [2026-06-05] query-answer | AI-assisted research ideation workflow
- Added [[ai-assisted-research-ideation-workflow]] to preserve a reusable planning rule: use LLMs for source-grounded conflict search, constraint hardening, metric design, and adversarial reviewer attack rather than broad context-free brainstorming.
- Connected the workflow to existing cross-direction innovation, target-relation rejection review, grounding-direction review, P0 reading synthesis, and completed-IHC method-design pages.
- Updated [[index]] to route the new planning page and refreshed the current inventory counts.

## [2026-06-05] ingest | ExPO-HM hateful meme explain-then-detect PDF
- Detected the remaining unindexed local PDF `raw/sources/2510.08630v3.pdf` and added deep-ingested source page [[187-mei-2026-expo-hm-learning-to-explain-then-detect-for-hateful-meme-detection]].
- Recorded ExPO-HM as an ICLR 2026 / arXiv v3 hateful meme paper on explain-then-detect policy optimization, policy-manual SFT warmup, GRPO curriculum learning, and Conditional Decision Entropy.
- Updated [[sources-index]], [[nlp-research-collection]], generated hate-speech, LLM-reasoning, and multimodal source hubs, and refreshed [[index]] inventory counts for 187 raw PDFs and 187 deep-ingested PDF source pages.
- Re-ran `scripts/lint_wiki.py`, `scripts/wiki_inventory.py`, `scripts/check_source_tag_drift.py`, and `scripts/check_pdf_text_artifacts.py`; no structural, routing, tag-drift, or PDF text-artifact failures were reported.

## [2026-06-13] query-answer | RA-HMD_text migration lineage
- Added [[rahmd-text-migration-lineage-2026-06-13]] after inspecting `nlp06:/data/cjt/hate/RGCL-main/RA-HMD`, `nlp06:/data/cjt/hate/Try/RA-HMD_text`, and the supplement run directory under `/home/cjt/RA-HMD_text_supplement_text_only_ablation_20260612_231535`.
- Recorded the migration lineage from native RA-HMD Stage2 RAC to text-only IHC Qwen feature extraction, paper-aligned RAC supplement, frozen-feature Stage2 classifier, single-stage text retrieval, predicted-target retrieval, parser/cluster/Macro-F1 threshold changes, dual-adapter runs, and uncertainty-gated ablations.
- Preserved the key score trail: native RAC stayed below about 0.70 Macro-F1, single-stage text retrieval reached 0.7604, predicted-target retrieval reached 0.7895, target clustering reached 0.7938, uncertainty-gated dual-adapter retrieval reached 0.7981, and the dual-adapter base-only ablation reached 0.7965 tuned / 0.7994 at threshold 0.5.
- Added a post-ablation direction audit after checking the full remote project tree: dedicated target extraction, target-then-classifier, always-on retrieval, cluster retrieval, uncertainty gating, parser cleanup, and Macro-F1 thresholding have already been tried. The revised next step is retrieval-trust calibration/error slicing rather than more target extraction or broad cluster sweeps.
- Updated [[rahmd-inspired-ihc-relation-adaptation-2026-06-05]] and [[index]] to route the experiment lineage.
- Re-ran `scripts/lint_wiki.py` and `scripts/wiki_inventory.py`; the wiki now contains 349 pages and 106 concept pages with no reported structural failures.
