# ReAct Hate DeepSeek V4 Flash Local Change Manifest

Generated: 2026-06-17

## Task

Prepare a direct ReAct-style smoke-test bundle for IHC hate speech detection
using DeepSeek V4 Flash through the OpenAI-compatible API.

## Local Bundle

`experiments/server-sync/staging/react-hate-deepseek-v4-flash/`

Included:

- `README.md`
- `MANIFEST.md`
- `run_smoke.sh`
- `scripts/react_ihc_smoke.py`

## Remote Target

`huashan:/data/chenjt/Hate/Try/ReAct_hate_deepseek_v4_flash`

## Data Dependencies

Expected on huashan:

- `/data/chenjt/Hate/FineTune_only/data/processed/ihc/train.jsonl`
- `/data/chenjt/Hate/FineTune_only/data/processed/ihc/validation.jsonl`
- `/data/chenjt/Hate/FineTune_only/data/processed/ihc/test.jsonl`

## Environment Dependencies

Expected on huashan:

- `/data/chenjt/miniconda3/envs/cjt`
- `openai` Python package for `MODE=api`

Verified earlier in the active task:

- huashan SSH works
- IHC processed files exist
- `cjt` has `torch`, `transformers`, `peft`, `sklearn`, `openai`, `numpy`,
  and `pandas`

## Dry-Run Verification

Local dry-run:

- command: `MODE=dry-run SAMPLE_SIZE=50 SPLIT=validation RUN_ID=local_validation_dryrun_50 bash run_smoke.sh`
- result: completed with 50 valid predictions and 0 parse failures

Remote dry-run:

- command: `MODE=dry-run SAMPLE_SIZE=50 SPLIT=validation RUN_ID=remote_validation_dryrun_50 bash run_smoke.sh`
- output: `/data/chenjt/Hate/Try/ReAct_hate_deepseek_v4_flash/runs/remote_validation_dryrun_50`
- result: completed with 50 valid predictions and 0 parse failures

Dry-run metrics are parser/pipeline checks only and should not be interpreted as
DeepSeek model quality.

## Excluded

- API key or credentials
- Dataset copies
- Local generated run outputs from the staging bundle
- Full model checkpoints, caches, and generated bulk outputs
