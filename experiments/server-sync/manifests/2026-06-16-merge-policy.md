# Server Mirror Merge Policy

Generated: 2026-06-16

## Decision

Create `experiments/server-sync/merged/` as a symlink-based consolidated view. Keep `experiments/server-sync/remotes/{server}/` unchanged as the provenance layer.

## Canonical Choices

| Consolidated path | Canonical source | Reason |
|---|---|---|
| `merged/hate-data` | `xu-l20:/data/chenjt/hate/DATA` | Fuller mirror than `nlp06:/data/cjt/hate/AnyCode-xu-l20/DATA`; includes HARE, IHC raw/processed files, SBIC raw/processed files, PLEAD train split, and newer `llm_restructed` data. |
| `merged/hate-finetune` | `xu-l20:/data/chenjt/hate/FineTune` | Superset of `nlp06:/data/cjt/hate/AnyCode-xu-l20/FineTune` after weight/cache exclusion. |
| `merged/rahmd-text` | `nlp06:/data/cjt/hate/Try/RA-HMD_text` | Unique RA-HMD_text migration and ablation project; no equivalent mirror on the other two downloaded servers. |
| `merged/study/nlpcourse` | `nlp06:/data/cjt/nlpcourse` | Unique course project mirror. |
| `merged/study/base-multi-study` | `huashan:/data/chenjt/Study/base_multi_study` | Unique study project mirror. |
| `merged/study/practise` | `huashan:/data/chenjt/Study/practise` | Unique practice/course corpus mirror. |

## Kept Separate

| Path | Reason |
|---|---|
| `merged/legacy/nlp06-llm-filled-target-old` | Three old `llm_filled_target` files exist only in the `nlp06` DATA mirror; they are retained as legacy evidence, not canonical data. |
| `merged/legacy/huashan-finetune-only` | Shares only a small base with `xu-l20/FineTune`; it represents an older binary fine-tuning project and should not be mixed into the canonical FineTune tree. |
| `merged/legacy/huashan-try` | Contains older Hidden-CoT and dual-model experiments with different layout and assumptions. |

## Comparison Evidence

- `nlp06/AnyCode-xu-l20/FineTune`: 478 files; all 478 matching relative paths are present in `xu-l20/FineTune`; no `nlp06`-only FineTune files after the selected mirror filters.
- `nlp06/AnyCode-xu-l20/DATA`: 79 files; 76 matching relative paths are present in `xu-l20/DATA`; the three `nlp06`-only files are under `llm_filled_target`.
- `huashan/FineTune_only`: 202 files; only 24 matching relative paths overlap with `xu-l20/FineTune`, so direct merge would blur distinct experiment generations.

## Use Rule

Use `merged/` for path discovery and read-only reuse. For new work, copy the needed subset into `staging/{task-slug}/` and edit there before syncing to a server.
