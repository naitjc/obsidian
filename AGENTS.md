# Research Wiki Map

This vault is a persistent LLM-maintained research wiki. It stores immutable source material, compiled research knowledge, local experiment records, and reusable maintenance rules.

## Mission

- Treat `raw/` as source-of-truth inputs.
- Treat `wiki/` as the compiled long-term knowledge layer.
- Treat `experiments/` as local experiment process, artifacts, and results.
- Treat `baselines/` as external paper code, upstream checkouts, and baseline-specific reproduction work.
- Prefer updating existing wiki pages over creating duplicate pages.
- Preserve links, backlinks, and concise synthesis across pages.
- Do not rely on chat history when the rule, result, or decision should live in the vault.

## Read First

Start from the file that routes the task:

- research question or source interpretation -> `wiki/index.md`
- active experiment work -> `EXPERIMENTS.md`
- wiki health, schema, or lint work -> `wiki/maintenance/index.md`
- manuscript work -> `papers/{paper-slug}/README.md` when it exists

## Namespace Map

- `raw/` -> immutable source documents, datasets, and captured assets
- `wiki/` -> durable research knowledge
- `experiments/` -> prompts, configs, runs, metrics, notes, and cross-run results
- `baselines/` -> external paper code, upstream repositories, and baseline-specific runs
- `papers/` -> manuscript-specific argument work
- `scripts/` and `src/` -> reusable local tooling and code

Within `wiki/`:

- `index.md` -> master router
- `sources/` -> source-grounded notes
- `concepts/` -> topic, method, synthesis, direction, and status pages
- `entities/` -> datasets, benchmarks, people, organizations, and reusable named entities
- `templates/` -> reusable page templates
- `maintenance/` -> schema, routing, lint, direction registry, and maintenance decisions

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

## Task Map

- new raw source -> create or update `wiki/sources/`, integrate it into affected synthesis pages, update `wiki/index.md`, append `log.md`
- research question -> read routed wiki pages first, then write reusable answers into an appropriate durable wiki page when the answer has long-term value
- experiment result -> keep raw outputs in `experiments/`, promote only durable conclusions into `wiki/`
- external baseline code -> keep it under `baselines/`, promote only durable findings into `wiki/`
- wiki maintenance -> use `wiki/maintenance/` for reusable maintenance guidance and `log.md` for major schema changes
- manuscript work -> keep draft-specific work in `papers/`, push reusable knowledge back into `wiki/`

## Required Updates

When a task changes durable knowledge, update the routing layer as needed:

- new or renamed durable page -> update `wiki/index.md`
- new ingest or meaningful maintenance change -> append `log.md`
- reusable benchmark fact -> update the relevant benchmark or dataset page
- reused conclusion across sources -> create or update the relevant synthesis, claim, or comparison page
- repeated cross-paper distinction -> create or update a durable comparison or topic page
- schema, taxonomy, or lint convention change -> record it under `wiki/maintenance/`
- experiment workflow or result convention change -> update `EXPERIMENTS.md` or the relevant `experiments/{dataset}/notes/` file

## Hard Constraints

- Do not edit files under `raw/`.
- Do not write converted datasets, model outputs, or temporary files under `raw/`.
- Do not leave a new durable wiki page unlinked from `wiki/index.md` or a relevant hub page.
- Do not mix third-party paper repositories into active `experiments/` folders when `baselines/` is the cleaner fit.
- Do not present working interpretation as if it were a direct source claim.
- Do not convert automatically extracted numeric candidates into final claims unless the original table has been checked.
- Do not introduce unrelated fallback branches, business goals, or alternative task paths when the user asked for a narrower change.

## Pointers

- schema and namespace detail -> `wiki/maintenance/wiki-schema.md`
- frontmatter and status vocabulary -> `wiki/maintenance/frontmatter-conventions.md`
- task routing and promotion detail -> `wiki/maintenance/task-routing-and-promotion.md`
- maintenance checks -> `wiki/maintenance/wiki-maintenance-checklist.md`
- completed direction registry -> `wiki/maintenance/research-direction-registry.md`
- active experiment workflow -> `EXPERIMENTS.md`
