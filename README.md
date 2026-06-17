# Obsidian Research Vault

This repository is a local research vault for source-grounded NLP research notes, experiment evidence, and maintenance rules.

## Main Entry Points

- `AGENTS.md`: project operating guide for LLM/Codex work in this vault.
- `wiki/index.md`: durable knowledge router and research map.
- `EXPERIMENTS.md`: experiment workspace rules.
- `experiments/server-sync/README.md`: local-first server experiment staging, mirror, and transfer workflow.
- `wiki/maintenance/index.md`: schema, lint, and maintenance router.
- `log.md`: append-only activity log for meaningful ingest, maintenance, and promoted experiment changes.

## Task Router

| Need | Start Here | Then Check |
|---|---|---|
| Answer a research question from the built wiki | `wiki/index.md` | Relevant direction map, source hub, source pages, and entity pages |
| Scout external papers for transferable ideas | `wiki/concepts/ai-assisted-research-ideation-workflow.md` | `wiki/templates/transfer-idea-screening-template.md` |
| Ingest a new source | `wiki/index.md` | `wiki/sources/sources-index.md`, relevant direction hub, `log.md` |
| Inspect or record experiment work | `EXPERIMENTS.md` | `experiments/{dataset}/notes/` and linked concept pages |
| Prepare server-runnable experiment code/data | `experiments/server-sync/README.md` | `experiments/server-sync/staging/{task-slug}/` and manifests |
| Inspect or preserve third-party method code | `baselines/README.md` | `baselines/{method}/README.md` |
| Check wiki health or publish readiness | `wiki/maintenance/index.md` | `wiki/maintenance/wiki-maintenance-checklist.md` and `git diff --check` |
| Coordinate subagents for context, remote runs, diagnostics, dedup, or cleanup | `wiki/maintenance/subagent-collaboration-workflow.md` | Main thread merges evidence before state-changing work |

## Directory Boundaries

- `raw/`: immutable source files. Do not edit or write generated files here.
- `wiki/`: compiled long-term knowledge and maintenance pages.
- `experiments/`: local experiment artifacts, configs, metrics, and notes.
- `experiments/server-sync/`: local staging, server mirrors, manifests, and run diagnostics for portable server-side work.
- `baselines/`: external paper code and baseline reproduction work. Use this instead of `experiments/server-sync/` for durable method-repo mirrors.
- `scripts/`: reusable maintenance and analysis scripts.
- `tmp/`: disposable local scratch space ignored by Git.

## Routine Checks

```bash
python3 scripts/lint_wiki.py
python3 scripts/wiki_inventory.py
python3 scripts/check_source_tag_drift.py
python3 scripts/check_pdf_text_artifacts.py
```

Run these after broad wiki changes, source ingestion, or project-structure maintenance.
