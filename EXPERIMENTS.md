# Experiment Workspace

This file holds experiment-specific operating rules for the research vault. Keep `AGENTS.md` focused on durable wiki-wide routing rules, and put active experiment details here.

## Repository Layout

Keep experiment work separate from the research wiki:

- Keep `raw/` immutable. Do not write converted datasets, model outputs, or temporary files under `raw/`.
- Keep external baseline repositories under `baselines/{method}/`, not under `experiments/`.
- Put deterministic derived data under `experiments/{dataset}/processed/`.
- Put prompt templates under `experiments/{dataset}/prompts/`.
- Put run configs under `experiments/{dataset}/configs/`.
- Put each model, prompt, or baseline run under `experiments/{dataset}/runs/{date}_{subset}_{method}/`.
- Each run folder should preserve `config.json` or `config.yaml`, `inputs.jsonl`, `outputs.jsonl`, `raw_llm_responses.jsonl`, `metrics.json`, `errors.jsonl`, `notes.md`, and `findings.md` when applicable.
- Put cross-run research notes under `experiments/{dataset}/notes/`.
- Use `scripts/` for small entry points such as dataset conversion, prompt running, evaluation, and error sampling.
- Move shared experiment logic into `src/` instead of duplicating it across scripts.
- Use `wiki/` for durable synthesis and interpretation, not large raw outputs.
- Link important experiment artifacts from the relevant wiki source, concept, method, or direction page.

Use `experiments/` for active local experiment pipelines. Use `baselines/` when the main artifact is an external paper implementation that you are inspecting, reproducing, or adapting.

## Experiment Tracking Workflow

Keep experiment tracking in three layers:

- Run artifacts are machine-written files under `experiments/{dataset}/runs/{run_id}/`. Do not hand-edit `inputs.jsonl`, `outputs.jsonl`, `raw_llm_responses.jsonl`, `metrics.json`, or generated summaries.
- Per-run notes are human-written observations for one run. Put them in `experiments/{dataset}/runs/{run_id}/findings.md`.
- Cross-run notes are durable research memory. Put them under `experiments/{dataset}/notes/`.

Use these note files when they become relevant:

- `experiments/{dataset}/notes/experiment-log.md`: chronological lab notebook. Add one short entry for each meaningful run.
- `experiments/{dataset}/notes/results-summary.md`: compact table of important runs, metrics, and links.
- `experiments/{dataset}/notes/error-taxonomy.md`: reusable categories for label confusion, boundary mismatch, formatting artifacts, parse failures, API failures, shortcut behavior, and evidence mismatch.
- `experiments/{dataset}/notes/decisions.md`: decisions and rationale, especially scoring rules, prompt changes, dataset split choices, baseline choices, annotation schema changes, and stopping criteria.

After each meaningful run:

1. Check `metrics.json`, `outputs.jsonl`, `raw_llm_responses.jsonl`, and `errors.jsonl` if present.
2. Generate or update an error summary when the run is used for analysis.
3. Write `findings.md` in the run folder with summary, notable errors, and next actions.
4. Append a short entry to `notes/experiment-log.md`.
5. Add or update one row in `notes/results-summary.md`.
6. If the run changes the experiment plan, record the decision in `notes/decisions.md`.
7. Promote only durable, source-grounded, or cross-run conclusions into `wiki/`.

## Scoring and Reporting

- Keep strict exact-match scores for diagnostics when the task has structured outputs.
- Add normalized scores only when the mismatch is a documented data-format artifact.
- Document any normalization rule before using it as the main reported number.
- Keep shortcut, leakage, and ablation diagnostics separate from main task metrics.
- Mark synthetic, weak, LLM-filled, or manually audited labels explicitly.
- Do not report global SOTA rankings across mismatched datasets, task settings, or evaluation protocols.

## Archive Hygiene

- Preserve the smallest complete local evidence set needed to inspect a result: README files, configs, source code, metrics, sampled or required predictions, error summaries, and derived data when regeneration is not trivial.
- Treat sample-level experiment evidence as local by default. In the public repository, publish README files, configs, source code, aggregate metrics, and non-sample summaries; keep derived datasets, per-example JSONL files, and logs local unless their release has been reviewed explicitly.
- Exclude interpreter caches and process state such as `__pycache__/`, `*.pyc`, and `*.pid`.
- Keep large checkpoint artifacts out of the vault unless a task explicitly requires them and the storage decision has been reviewed.
- Document deliberately omitted artifacts in the archive README so recovery assumptions remain explicit.

## Server-Portable Code and Data

Use `experiments/server-sync/` as the local staging and mirror area for code/data that should be runnable on different servers. It is not the durable archive for external paper repositories; those belong under `baselines/` once their code/data boundary is clear. For server-side experiment tasks, first prepare the code, configs, and needed dataset files locally under `experiments/server-sync/staging/{task-slug}/`, then sync that bundle to the selected server and run it there. Keep remote snapshots under `experiments/server-sync/remotes/{server}/` as local-only evidence, and record inventories and omitted high-value artifacts under `experiments/server-sync/manifests/`.

For model-framework modifications or new framework creation, always make task edits in the local staging folder first. Automatically update that staging folder's README and a matching manifest whenever code, configs, prompts, or small deterministic task data are changed. Use `baselines/` for reusable external method code, use `experiments/server-sync/merged/` only as a read-only server-snapshot selection layer, and keep `remotes/{server}/` as server snapshots unless a task explicitly asks to resync or promote a new local canonical baseline.

Do not store credentials in this folder. Do not commit remote mirrors, large datasets, checkpoints, package caches, model caches, virtual environments, or bulk generated outputs. Promote only durable conclusions or reusable workflow changes into `wiki/`.

## Current Active Experiment

No active experiment is assumed by the global rules. When a new experiment becomes active, create or update the relevant `experiments/{dataset}/notes/` files and link durable conclusions back into the appropriate wiki pages.
