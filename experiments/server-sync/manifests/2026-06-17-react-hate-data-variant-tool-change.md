# ReAct Hate Data Variant Tool Change

Generated: 2026-06-17

## Task

Add a dataset-variant switch for the DeepSeek ReAct IHC experiment so completed
and uncompleted datasets use different prompt and observation schemas.

## Remote Project

`huashan:/data/chenjt/Hate/Try/ReAct_hate_deepseek_v4_flash`

## New Parameter

`DATA_VARIANT`

Values:

- `uncompleted` (default): Search observations expose only `split`, `score`,
  binary `label`, and `text`. `hate_class` and `target` fields are not shown to
  the model or included in observation records.
- `completed`: Search observations also expose completed `hate_class` and
  `target` as auxiliary evidence. The final task remains binary
  `toxic`/`non_toxic` classification.

`DATA_DIR` still selects the actual JSONL split directory. `DATA_VARIANT` only
controls how the selected dataset is described and shown to the model.

## Search Tool Semantics

`evidence_type` is a model-chosen Search tool argument, not a dataset field.

- `similar`: nearest labeled examples without forcing one label side
- `contrastive`: retrieve both toxic and non-toxic neighbors
- `toxic`: retrieve only toxic neighbors
- `non_toxic`: retrieve only non-toxic neighbors

## Verification

Local dry-runs:

- `DATA_VARIANT=uncompleted SAMPLE_SIZE=4`: completed with 4 valid predictions
- `DATA_VARIANT=completed SAMPLE_SIZE=4`: completed with 4 valid predictions

Trace inspection:

- uncompleted observation keys: `id`, `label`, `rank`, `score`, `split`, `text`
- completed observation keys additionally include `hate_class` and `target`

Remote dry-run:

- command: `MODE=dry-run DATA_VARIANT=uncompleted SAMPLE_SIZE=4 SPLIT=validation RUN_ID=remote_variant_uncompleted_dryrun_4 MAX_SEARCHES=2 SEARCH_POOLS=train,validation bash run_smoke.sh`
- result: completed with 4 valid predictions and 0 parse failures
- archived under `runs/archive/dryrun/remote_variant_uncompleted_dryrun_4`
