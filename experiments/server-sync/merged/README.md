# Consolidated Local View

This folder is a non-destructive local view over `../remotes/`. It uses symlinks to reduce path hunting while keeping the original per-server snapshots intact.

## Canonical Entries

- `hate-data` -> `xu-l20:/data/chenjt/hate/DATA`
- `hate-finetune` -> `xu-l20:/data/chenjt/hate/FineTune`
- `rahmd-text` -> `nlp06:/data/cjt/hate/Try/RA-HMD_text`

Use these three paths first for future hate-speech experiment staging unless a task explicitly needs an older server-specific snapshot.

## Legacy And Special Entries

- `legacy/nlp06-llm-filled-target-old` -> old `nlp06`-only `llm_filled_target` files that are not present in the newer `xu-l20` DATA mirror.
- `legacy/huashan-finetune-only` -> older Huashan binary fine-tuning project. It overlaps only lightly with `hate-finetune`, so it is kept separate.
- `legacy/huashan-try` -> older Hidden-CoT and dual-model experiments from Huashan.

## Study Entries

- `study/nlpcourse` -> `nlp06:/data/cjt/nlpcourse`
- `study/base-multi-study` -> `huashan:/data/chenjt/Study/base_multi_study`
- `study/practise` -> `huashan:/data/chenjt/Study/practise`

## Merge Policy

Do not edit files through these symlinks unless the task explicitly says to modify local mirrors. For new work, copy the needed code/data into `../staging/{task-slug}/`, edit there, then sync that staging bundle to the chosen server.

The original server mirrors remain the provenance layer. This folder is only a convenience layer.
