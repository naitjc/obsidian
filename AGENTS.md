# Wiki Schema

## Overview
This is a personal research wiki maintained by LLM. The wiki is a persistent, compounding artifact that grows with each source added and question asked.

## Directory Structure

```
./
├── raw/                    # Immutable source documents
│   └── sources/           # Articles, papers, PDFs, etc.
├── wiki/                  # LLM-generated content
│   ├── entities/         # People, places, things
│   ├── concepts/         # Topics, ideas, theories
│   ├── sources/          # Source summaries and notes
│   └── index.md          # Master catalog
├── log.md                # Chronological activity log
└── AGENTS.md            # This schema file
```

## Conventions

### Page Format
- Markdown with YAML frontmatter
- Frontmatter fields: `created`, `updated`, `tags`, `sources`
- Cross-links using ``page-name`` syntax
- Citations: `[source](source-url)`
- Wiki page names use lowercase slug targets.
- Raw source files are immutable; do not edit files under `raw/`.
- Source pages should separate extracted evidence from synthesis. Do not convert automatically extracted numeric candidates into final claims unless the original table has been checked.

### Source Page Format
- Required sections: `Metadata`, `Problem Framing`, `Method`, `Data and Evaluation Setup`, `Results and Claims`, `Limitations and Follow-ups`, `Structured Signals`, `Related Concepts`.
- If a page is only metadata/first-page extraction, tag it `auto-ingest` and treat it as a navigation node, not as a reliable synthesis source.
- If a page has multi-section extraction and direction-level links, tag it `deep-ingest-v2`.

### Concept and Synthesis Pages
- Concept pages summarize stable knowledge across sources and link to evidence-bearing source pages.
- Synthesis pages may resolve tensions between papers, but must mark unverifiable quantitative claims as assumptions or pending verification.
- Direction status pages track completion criteria, remaining gaps, and whether the direction is complete for internal wiki use or publication-grade external citation.

### Ingest Workflow
1. LLM reads the new source
2. Creates/updates relevant entity and concept pages
3. Updates `index.md`
4. Appends entry to `log.md`

### Query Workflow
1. Check `index.md` for relevant pages
2. Read relevant pages
3. Synthesize answer with citations
4. If valuable, file answer as new wiki page using `wiki/templates/query-answer-template.md`
5. Update `index.md` and append to `log.md`

### Lint Checklist
- Contradictions between pages
- Stale claims superseded by newer sources
- Orphan pages (no inbound links)
- Missing cross-references
- Data gaps
- Numeric claims without table-level evidence

### Log Format
```
## [YYYY-MM-DD] type | Title
```

## Completed Directions

The following directions are complete for internal wiki use. Other directions are intentionally left as-is unless the user asks for them.

### Hate Speech Detection

#### Scope
- Explicit and implicit hate speech detection
- Multimodal hate detection and hateful memes
- Cross-platform, cross-domain, and cross-lingual transfer
- Hate speech datasets and benchmark normalization
- Explainability, reasoning, retrieval, causal, and contrastive methods when used for hate detection

#### Canonical Entry Points
- Direction map: `wiki/concepts/hate-speech-research-map.md`
- Source hub: `wiki/concepts/hate-speech-source-hub.md`
- SOTA synthesis: `wiki/concepts/hate-speech-sota-landscape.md`
- Final synthesis: `wiki/concepts/hate-speech-final-synthesis.md`
- Metrics workspace: `wiki/concepts/hate-speech-metrics-matrix.md`
- Status: `wiki/concepts/hate-speech-direction-status.md`
- Latest completion report: `wiki/concepts/hate-speech-completion-report-2026-04-29.md`

#### Completion Rule
- The direction is complete for internal wiki use when all hate-tagged source pages are deep-ingested, linked from the source hub, represented in concept/synthesis pages, and included in lint/status reporting.
- Publication-grade quantitative claims require manual table verification in the original PDFs. If that has not been done, keep numeric rows marked as table-located, partial, or pending-manual-verification.

### Stance Detection

#### Scope
- Stance classification toward targets, topics, claims, and entities
- Zero-shot and open-domain stance detection
- Conversational, multimodal, cross-lingual, and target-adaptive stance settings
- LLM prompting, reasoning, synthetic data, retrieval/knowledge, and verification when used for stance detection
- Bias, stereotypes, target absence, and target formulation effects

#### Canonical Entry Points
- Direction map: `wiki/concepts/stance-detection-research-map.md`
- Source hub: `wiki/concepts/stance-detection-source-hub.md`
- SOTA synthesis: `wiki/concepts/stance-detection-sota-landscape.md`
- Final synthesis: `wiki/concepts/stance-detection-final-synthesis.md`
- Metrics workspace: `wiki/concepts/stance-detection-metrics-matrix.md`
- Status: `wiki/concepts/stance-detection-direction-status.md`
- Latest completion report: `wiki/concepts/stance-detection-completion-report-2026-05-05.md`

#### Completion Rule
- The direction is complete for internal wiki use when all stance-tagged source pages are deep-ingested, linked from the source hub, represented in concept/synthesis pages, and included in lint/status reporting.
- Publication-grade quantitative claims require manual table verification in the original PDFs. Avoid global SOTA rankings across mismatched stance settings.

### Other Completed Directions

The following directions are also complete for internal wiki use as of 2026-05-05:

| Direction | Source Hub | Completion Report |
|---|---|---|
| Dialogue, intent, and slot filling | `wiki/concepts/dialogue-systems-source-hub.md` | `wiki/concepts/dialogue-systems-completion-report-2026-05-05.md` |
| LLM reasoning and evaluation | `wiki/concepts/llm-reasoning-source-hub.md` | `wiki/concepts/llm-reasoning-completion-report-2026-05-05.md` |
| Sarcasm and humor detection | `wiki/concepts/sarcasm-detection-source-hub.md` | `wiki/concepts/sarcasm-detection-completion-report-2026-05-05.md` |
| Role-playing agents and persona modeling | `wiki/concepts/role-playing-agents-source-hub.md` | `wiki/concepts/role-playing-agents-completion-report-2026-05-05.md` |
| Emotion recognition and empathetic response | `wiki/concepts/emotion-recognition-source-hub.md` | `wiki/concepts/emotion-recognition-completion-report-2026-05-05.md` |
| Multimodal learning | `wiki/concepts/multimodal-learning-source-hub.md` | `wiki/concepts/multimodal-learning-completion-report-2026-05-05.md` |

Completion boundary for all directions: internal research navigation, browsing, and Q&A are complete; priority benchmark rows have rendered-PDF visual verification, but global SOTA rankings across mismatched tasks remain out of scope.

### Global Entry Points
- Top-level map: `wiki/concepts/global-research-map.md`
- Cross-direction synthesis: `wiki/concepts/cross-direction-synthesis-2026-05-06.md`
- PDF table verification index: `wiki/concepts/pdf-table-verification-index-2026-05-06.md`
- Maintenance playbook: `wiki/concepts/wiki-maintenance-playbook.md`
- Current maintenance status: `wiki/concepts/wiki-maintenance-status-2026-05-06.md`

### Local Maintenance Tools
- Structural lint: `python3 scripts/lint_wiki.py`
- Inventory summary: `python3 scripts/wiki_inventory.py`
- PDF table locator: `python3 scripts/locate_pdf_tables.py`
- PDF metric page verifier: `python3 scripts/verify_pdf_metric_pages.py`
- Query answer template: `wiki/templates/query-answer-template.md`
- Local attachment target: `raw/assets/`
- Local version history: git repository initialized at the vault root

## Status
- [x] First source ingested
- [x] Core concepts mapped
- [x] Initial entity pages created
- [x] Hate speech detection direction completed for internal wiki use
- [x] Stance detection direction completed for internal wiki use
- [x] Dialogue / intent / slot filling direction completed for internal wiki use
- [x] LLM reasoning / evaluation direction completed for internal wiki use
- [x] Sarcasm / humor direction completed for internal wiki use
- [x] Role-playing agents / persona modeling direction completed for internal wiki use
- [x] Emotion recognition direction completed for internal wiki use
- [x] Multimodal learning direction completed for internal wiki use
- [x] Cross-direction synthesis created
- [x] Maintenance scripts added
- [x] PDF table locator added
- [x] PDF priority metrics rows visually verified
- [x] Query answer template added
- [x] Attachment directory created
- [x] Git repository initialized
