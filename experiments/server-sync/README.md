# Server Sync Workspace

This folder is the local staging and mirror area for portable server-side experiments.

It is not the durable archive for external paper repositories. When a remote folder is mainly an upstream method repo, copy a code-only mirror into `baselines/` and leave this folder for staging, server snapshots, transfer manifests, and run diagnostics.

## Purpose

When a future task needs code or datasets to run on a GPU/server machine, first prepare the smallest complete runnable bundle locally in this vault, then sync that bundle to the selected server and run it there. The goal is to make experiments movable across `nlp06`, `xu-l20`, `huashan`, or another available server without repeatedly hand-uploading scattered code and data.

Do not treat any one server as canonical. The local bundle should contain the code, configs, dataset subset or dataset pointer, and README needed to reproduce the run on another server.

## Layout

- `staging/{task-slug}/code/`: local code written or modified for a task.
- `staging/{task-slug}/data/`: task-specific dataset files or deterministic processed data needed by the code.
- `staging/{task-slug}/configs/`: run configs, launch scripts, and environment notes.
- `staging/{task-slug}/README.md`: command entry points, expected inputs/outputs, and server assumptions.
- `remotes/{server}/...`: local-only mirrors of important code and datasets copied from remote server paths.
- `merged/`: local-only symlink view over selected remote mirrors, with entries for choosing server-derived inputs for future staging bundles.
- `manifests/`: inventories, transfer logs, and omission notes for remote mirrors and future upload bundles.
- `scripts/`: reusable helper scripts for inventorying, packaging, syncing, or verifying bundles.

## Selection Policy

Keep the smallest useful set:

- Include source code, launch scripts, configs, prompt templates, notebooks when they are the only available record, README files, metric summaries, label maps, dataset schema files, and dataset files needed for reproduction.
- Include dataset formats such as `.csv`, `.tsv`, `.json`, `.jsonl`, `.parquet`, `.txt`, `.pkl`, `.pickle`, `.npy`, and `.npz` when they are source or deterministic processed inputs.
- Exclude Python caches, virtual environments, package caches, downloaded model caches, wandb/TensorBoard run directories, large checkpoints, adapter weights, full model weights, optimizer states, and bulk generated predictions unless a task explicitly requires preserving them.
- Record omitted high-value artifacts in `manifests/` instead of silently dropping them.

Large or sensitive payloads under `remotes/` and `staging/` are local evidence by default and are intentionally ignored by Git. Promote external method code into `baselines/` when it should be inspected or reused as a baseline; promote only durable conclusions, compact summaries, or reusable workflow rules into `wiki/` or `EXPERIMENTS.md`.

## Future Run Workflow

1. Build or update `staging/{task-slug}` locally.
2. Verify that the bundle has runnable code, required data, configs, and a short README.
3. Sync the bundle to the chosen server with `rsync`, preserving relative paths.
4. Run on the selected server under a task-specific work directory, not inside unrelated old experiment folders.
5. Pull back metrics, configs, logs needed for diagnosis, and concise result summaries.
6. Keep large checkpoints and bulk outputs on the server unless the storage decision is explicitly reviewed.

## Local-First Modification Rule

For any future task that modifies an existing model framework or creates a new one, use local files first:

1. Choose the closest code base from `baselines/` or from a server snapshot under `merged/`, such as `merged/hate-finetune`, `merged/rahmd-text`, or a legacy/study entry.
2. Copy only the needed runnable subset into `staging/{task-slug}/`.
3. Make all code, config, prompt, and small deterministic data edits inside that staging folder.
4. Automatically update the staging folder's `README.md` with the source baseline, changed files, run command, target server path, and expected outputs.
5. Automatically write or refresh a manifest under `manifests/{date}-{task-slug}-local-change.md` describing local inputs, modified files, data dependencies, excluded files, and intended remote sync target.
6. If the task creates reusable code/data that should become the default for future tasks, update the consolidated `merged/` policy document instead of silently changing old assumptions.

Do not edit `remotes/{server}/` directly for task work. Treat `remotes/` as server snapshots. Refresh a remote mirror only when the user asks to resync a server path or when a completed run needs to pull back results.

When the task proceeds to server execution, upload the staging bundle to the target server and run from that uploaded task directory. After execution, pull back only diagnostics needed for local analysis: run configs, logs, metrics, summaries, and selected predictions or error samples.

## Current Mirrors

The initial mirror set is generated from:

- `nlp06:/data/cjt/hate/Try/RA-HMD_text`
- `nlp06:/data/cjt/hate/AnyCode-xu-l20/DATA`
- `nlp06:/data/cjt/hate/AnyCode-xu-l20/FineTune`
- `nlp06:/data/cjt/nlpcourse`
- `xu-l20:/data/chenjt/hate/DATA`
- `xu-l20:/data/chenjt/hate/FineTune`
- `huashan:/data/chenjt/Hate/FineTune_only`
- `huashan:/data/chenjt/Hate/Try`
- `huashan:/data/chenjt/Study/base_multi_study`
- `huashan:/data/chenjt/Study/practise`

Use the files in `manifests/` to check exactly what was copied and what was excluded.

The current consolidated view lives under `merged/`:

- `merged/hate-data` uses the fuller `xu-l20` DATA mirror.
- `merged/hate-finetune` uses the fuller `xu-l20` FineTune mirror.
- `merged/rahmd-text` uses the `nlp06` RA-HMD_text mirror.
- `merged/legacy/` keeps older or non-canonical server-specific projects separate.
- `merged/study/` keeps course and practice projects separate from hate-speech experiment code.

If local task edits make a staging bundle more current than the original mirror, prefer that staging bundle for the active task. Do not back-propagate it into `remotes/` unless the user explicitly asks to refresh the mirror. If the reusable result is external method code, promote a cleaned copy into `baselines/`; if it is an experiment workflow or result, document it in `experiments/` and promote only durable conclusions into `wiki/`.
