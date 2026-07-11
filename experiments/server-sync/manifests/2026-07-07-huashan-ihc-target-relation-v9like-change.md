# Huashan IHC Target-Relation V9-Like Change

- Timestamp: 2026-07-07 20:02:10 +0800
- Remote workspace: `huashan:/data/chenjt/Hate/Try/ihc-target-relation-workflow`
- Scope: update the 200-sample big-big workflow to use target-relation evidence closer to the prior v9 protocol.

## Changed Remote Files

- `src/core.py`
- `src/run_architecture.py`
- `src/build_summary_dataset.py`
- `tests/test_core.py`
- `configs/original.json`
- `configs/target_only.json`
- `configs/target_statement.json`
- `data/corpora/target_only.jsonl`
- `data/corpora/target_statement.jsonl`

## Protocol Changes

- Added `target_status` to `target_only` and `target_statement` corpus rows by merging from the huashan dataset copies by `id`.
- Preserved original corpus text order and text bytes from the previous corpus files so existing BGE embeddings remain aligned.
- Runtime evidence memory now maps:
  - `label=toxic` and `target_status=attacked_target` -> `relation=attacked`
  - `label=not_toxic` and `target_status=mentioned_not_attacked` -> `relation=mentioned_not_attacked`
- `no_target`, `implicit_target`, and `uncertain` rows are excluded from relation evidence memory.
- Evidence selection now uses v9-like target-conditioned relation evidence:
  - `top_k=10`
  - `max_targets=3`
  - `attacked_examples_per_target=2`
  - `mentioned_examples_per_target=1`
  - attacked examples are selected with `hate_class` diversity before filling by nearest score.
- Summary JSON schema now contains only:
  - `toxic_patterns`
  - `not_toxic_patterns`
- Removed `key_difference` from current prompt and parser contracts.

## Validation

- `target_only` corpus text hash matches config: `4d19e6f9581329156a4530df47efd9cf2cb92e45794bd8fa5f9af69472b37636`.
- `target_statement` corpus text hash matches config: `4d19e6f9581329156a4530df47efd9cf2cb92e45794bd8fa5f9af69472b37636`.
- Current corpus relation-eligible counts:
  - `attacked`: 4,365
  - `mentioned_not_attacked`: 7,553
- Remote checks passed:
  - `python -m py_compile src/core.py src/run_architecture.py src/build_summary_dataset.py tests/test_core.py`
  - `PYTHONPATH=src python -m unittest discover -s tests -v`
  - manual evidence smoke for `target_only` and `target_statement`

## Run Note

The old incompatible checkpoint files were renamed under `checkpoints/*.bak_pre_relation_v9like_20260707_200159` so the next run starts fresh under the new code/config/corpus identity.
