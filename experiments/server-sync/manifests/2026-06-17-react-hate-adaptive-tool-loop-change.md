# ReAct Hate Adaptive Tool Loop Change

Generated: 2026-06-17

## Task

Update the DeepSeek ReAct IHC experiment from a fixed single retrieval call to
an adaptive Search tool loop.

## Remote Project

`huashan:/data/chenjt/Hate/Try/ReAct_hate_deepseek_v4_flash`

## Code Boundary

Updated local staging bundle:

`experiments/server-sync/staging/react-hate-deepseek-v4-flash/`

Changed behavior:

- The model can now decide whether to call `Search` or stop with `Finish[...]`.
- `Search` accepts JSON tool arguments:
  - `query`
  - `k`
  - `evidence_type`: `similar`, `contrastive`, `toxic`, `non_toxic`
  - `label_filter`: `any`, `toxic`, `non_toxic`
  - `pool`: `train`, `validation`, `train+validation`
- Search is capped by `MAX_SEARCHES`, default `2`.
- `TOP_K` is the default requested k, and `MAX_K` clamps model-requested k.
- The default retrieval pool is `train,validation`.
- When evaluating a validation sample, the current sample is excluded from the
  retrieval results by id/text to avoid direct label leakage.

## Verification

Remote dry-run:

- command: `MODE=dry-run SAMPLE_SIZE=8 SPLIT=validation RUN_ID=remote_adaptive_tool_dryrun_8 MAX_SEARCHES=2 SEARCH_POOLS=train,validation bash run_smoke.sh`
- result: completed with 8 valid predictions and 0 parse failures
- self-leak check: no observation id matched the current eval id
- observation pools included both `train` and `validation`

The dry-run was moved to:

`runs/archive/dryrun/remote_adaptive_tool_dryrun_8`

## Next API Check

Run a fresh API validation smoke before full test because prompts and tool
behavior changed:

`MODE=api SAMPLE_SIZE=50 SPLIT=validation RUN_ID=api_validation_adaptive_50 MAX_SEARCHES=2 SEARCH_POOLS=train,validation bash run_smoke.sh`
