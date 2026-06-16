# Research Vault Operating Guide

This vault is a persistent LLM-maintained research wiki. It stores immutable source material, compiled research knowledge, local experiment records, baseline reproductions, manuscript work, and reusable maintenance rules.

## Request Handling

- Start from the user's original need. Do not assume the goal, constraints, or implementation path are already fully specified.
- Ask for clarification only when there is a key ambiguity and different interpretations would lead to clearly different plans or high error cost.
- Otherwise continue under the most reasonable interpretation and state the assumption when it matters.
- For modification, cleanup, or refactor tasks, stay within the user's stated goal. Do not broaden the business or research objective.
- Prefer the smallest complete solution that satisfies the goal. If the shortest path would create structural debt, choose the smallest structurally correct solution instead.
- Do not add unrelated fallback branches, alternative task paths, or speculative future features. Necessary input constraints, state checks, and boundary protection are allowed.
- Before proposing or applying a structural change, check the full path: inputs, processing flow, state changes, outputs, and upstream/downstream impact. Mark assumptions and unverified premises explicitly.

## Mission

- Treat `raw/` as source-of-truth inputs.
- Treat `wiki/` as the compiled long-term knowledge layer.
- Treat `experiments/` as local experiment process, artifacts, and results.
- Treat `experiments/server-sync/` as the local staging and mirror area for portable server-side experiment work.
- Treat `baselines/` as external paper code, upstream checkouts, and baseline-specific reproduction work.
- Treat `papers/` as manuscript-specific argument work when present.
- Treat `/Users/chen/Documents/Codex` as a separate non-vault workspace for coursework, side tasks, and non-research experiments. Do not mix those files into this vault unless the user explicitly promotes something into the research workflow.
- Prefer updating existing wiki pages over creating duplicate pages.
- Preserve links, backlinks, and concise synthesis across pages.
- Do not rely on chat history when the rule, result, or decision should live in the vault.

## Read First

Start from the file that routes the task:

- research question or source interpretation -> `wiki/index.md`
- source ingestion -> `wiki/index.md`, then the relevant direction hub under `wiki/concepts/`
- active experiment work -> `EXPERIMENTS.md`
- server-side experiment setup, sync, or remote-run work -> `EXPERIMENTS.md`, then `experiments/server-sync/README.md`
- wiki health, schema, or lint work -> `wiki/maintenance/index.md`
- manuscript work -> `papers/{paper-slug}/README.md` when it exists

## Namespace Map

- `raw/` -> immutable source documents, datasets, and captured assets
- `wiki/` -> durable research knowledge
- `experiments/` -> prompts, configs, runs, metrics, notes, and cross-run results
- `experiments/server-sync/` -> local-first staging, remote mirrors, manifests, and portable server bundles
- `baselines/` -> external paper code, upstream repositories, and baseline-specific runs
- `papers/` -> manuscript-specific drafts, claims, outlines, and argument work
- `scripts/` and `src/` -> reusable local tooling and code
- `tmp/` -> disposable derived files and render caches

Within `wiki/`:

- `index.md` -> master router
- `sources/` -> source-grounded notes
- `concepts/` -> topic, method, synthesis, direction, metrics, and status pages
- `entities/` -> datasets, benchmarks, people, organizations, and reusable named entities
- `templates/` -> reusable page templates
- `maintenance/` -> schema, routing, lint, direction registry, and maintenance decisions
- `maintenance/reports/` -> dated lint reports, verification indexes, and historical maintenance snapshots

Optional future namespaces under `wiki/` may include `domains/`, `topics/`, `methods/`, `datasets/`, `comparisons/`, `claims/`, or `questions/` when a task needs a cleaner split than the current `concepts/` and `entities/` layout.

## Current Research Directions

Use the vault's existing direction registry, not directions from imported example rule files. Current canonical directions are:

- hate speech detection
- stance detection
- dialogue, intent, and slot filling
- LLM reasoning and evaluation
- sarcasm and humor detection
- role-playing agents and persona modeling
- emotion recognition and empathetic response
- multimodal learning

The direction registry and canonical entry points live in `wiki/maintenance/research-direction-registry.md`. The top-level map is `wiki/concepts/global-research-map.md`.

## Task Workflows

### New Raw Source

1. Do not edit existing files under `raw/`.
2. Create or update the relevant page under `wiki/sources/`.
3. Integrate the source into affected concept, entity, synthesis, metrics, or direction pages.
4. Update `wiki/index.md` and the relevant source hub when routing changes.
5. Append `log.md`.
6. Run the relevant maintenance checks.

### Research Question

1. Read `wiki/index.md` and the routed direction, concept, source, and entity pages before answering.
2. Keep direct source claims separate from synthesis and inference.
3. If the answer has durable research value, file it in the nearest existing wiki page or a page based on `wiki/templates/query-answer-template.md`.
4. Update routing pages and `log.md` only when durable knowledge is created or materially changed.

### Experiment Result

1. Keep raw outputs, configs, predictions, logs, and run artifacts under `experiments/`.
2. Record run-level observations in the run folder and cross-run conclusions under `experiments/{dataset}/notes/`.
3. Promote only durable, checked, or cross-run conclusions into `wiki/`.
4. Update `EXPERIMENTS.md` or the relevant experiment notes when the workflow or result convention changes.

### Server-Side Experiment Work

1. Work local-first under `experiments/server-sync/staging/{task-slug}/`.
2. Use `baselines/` as the durable home for external method repositories.
3. Use `experiments/server-sync/merged/` only as a local snapshot selection layer when choosing server-derived inputs for a runnable task bundle.
4. Treat `experiments/server-sync/remotes/{server}/` as snapshots. Do not edit remote mirrors directly for task work.
5. Update the staging README and a matching manifest whenever code, configs, prompts, or small deterministic task data change.
6. Sync the prepared bundle to the chosen server only after the local runnable bundle is coherent.
7. Pull back only diagnostics needed for local analysis: run configs, logs, metrics, summaries, and selected predictions or error samples.

### External Baseline Code

Keep third-party paper repositories and reproduction-specific upstream code under `baselines/`. Copy only code, docs, configs, compact metadata, and small examples by default; exclude datasets, checkpoints, caches, and generated outputs. Promote only durable findings, adaptations, or comparison conclusions into `wiki/`.

### Wiki Maintenance

Use `wiki/maintenance/` for reusable maintenance guidance and `log.md` for major schema, routing, or lint changes. Do not put ordinary maintenance reports directly under `wiki/concepts/`.

## Required Updates

When a task changes durable knowledge, update the routing layer as needed:

- new or renamed durable page -> update `wiki/index.md`
- new source ingest -> update `wiki/sources/sources-index.md`, the relevant source hub, and `log.md`
- meaningful maintenance change -> update `wiki/maintenance/` and append `log.md`
- reusable benchmark fact -> update the relevant benchmark or dataset page
- reused conclusion across sources -> create or update the relevant synthesis, claim, or comparison page
- repeated cross-paper distinction -> create or update a durable comparison or topic page
- schema, taxonomy, or lint convention change -> record it under `wiki/maintenance/`
- experiment workflow or result convention change -> update `EXPERIMENTS.md` or the relevant `experiments/{dataset}/notes/` file

## Local And Public Boundaries

- Track README files, configs, source code, aggregate metrics, compact summaries, manifests, and non-sample analysis when they are useful evidence.
- Keep derived datasets, sample-level JSONL, raw LLM responses, bulk predictions, logs, checkpoints, model weights, optimizer states, caches, virtual environments, package caches, and remote mirrors local unless the user explicitly reviews and approves publication.
- Do not store credentials, tokens, private keys, or server secrets in this vault.
- Use `.gitignore` and local manifests to document intentionally omitted high-value artifacts.

## Hard Constraints

- Do not edit files under `raw/`.
- Do not write converted datasets, model outputs, or temporary files under `raw/`.
- Do not leave a new durable wiki page unlinked from `wiki/index.md` or a relevant hub page.
- Do not mix third-party paper repositories into active `experiments/` folders when `baselines/` is the cleaner fit.
- Do not present working interpretation as if it were a direct source claim.
- Do not convert automatically extracted numeric candidates into final claims unless the original table has been checked.
- Do not report global SOTA rankings across mismatched datasets, task settings, or evaluation protocols.
- Do not introduce unrelated fallback branches, business goals, or alternative task paths when the user asked for a narrower change.

## Routine Checks

Run these after source ingestion, schema changes, broad wiki maintenance, or before considering the vault structurally clean:

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

## Pointers

- schema and namespace detail -> `wiki/maintenance/wiki-schema.md`
- frontmatter and status vocabulary -> `wiki/maintenance/frontmatter-conventions.md`
- task routing and promotion detail -> `wiki/maintenance/task-routing-and-promotion.md`
- maintenance checks -> `wiki/maintenance/wiki-maintenance-checklist.md`
- completed direction registry -> `wiki/maintenance/research-direction-registry.md`
- active experiment workflow -> `EXPERIMENTS.md`
- server sync workflow -> `experiments/server-sync/README.md`
