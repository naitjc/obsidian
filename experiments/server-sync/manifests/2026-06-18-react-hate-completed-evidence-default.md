# ReAct Hate Completed Evidence Default

Generated: 2026-06-18

## Scope

Project:

`huashan:/data/chenjt/Hate/Try/ReAct_hate_deepseek_v4_flash`

Local staging bundle:

`experiments/server-sync/staging/react-hate-deepseek-v4-flash`

## Change

The default evidence variant is now `completed`.

Affected defaults:

- `run_smoke.sh`: `DATA_VARIANT=completed`
- `launch_nohup.sh`: `DATA_VARIANT=completed`
- `scripts/react_ihc_smoke.py`: `--data-variant completed`

## Experiment Meaning

Retrieved examples shown to the model now include:

- `split`
- retrieval `score`
- `id`
- `source`
- binary `label`
- `label_id`
- `text`
- `hate_class`, when present in the retrieved row
- `target`, when present in the retrieved row

The final task remains binary `toxic` / `non_toxic` classification.

`DATA_VARIANT=uncompleted` remains available for class-only ablations, but it is
no longer the default setting for the full test run.

## Intended Full Test Setting

- eval split: `test`
- retrieval memory: `train,validation`
- sample size: full split via `SAMPLE_SIZE=0`
- evidence variant: `completed`
- model: `deepseek-v4-flash`
- thinking: `disabled`
- parser: strict `Finish[...]`

The run should still exclude `test` from `SEARCH_POOLS`.
