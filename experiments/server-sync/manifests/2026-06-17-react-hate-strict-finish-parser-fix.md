# ReAct Hate Strict Finish Parser Fix

Generated: 2026-06-17

## Issue

The adaptive tool-loop run `api_validation_uncompleted_adaptive_50` used a
lenient substring fallback in `parse_finish`. Several model responses contained
`Action: Search[...]` but also mentioned words such as `toxic` or `non_toxic`
in the reasoning. The parser incorrectly treated those responses as final
labels, so Search was not executed for many examples.

That run is invalid as an adaptive ReAct result.

## Fix

`parse_finish` now defaults to strict parsing. A response is considered a final
classification only when it uses an explicit final-label pattern such as
`Finish[...]`, `Answer: ...`, `Label: ...`, or `Prediction: ...`.

Free-text substring fallback is disabled for normal ReAct loop outputs. If a
final response is not parseable, the existing repair call asks the model to emit
one strict `Finish[...]` line.

## Remote Actions

Updated project:

`huashan:/data/chenjt/Hate/Try/ReAct_hate_deepseek_v4_flash`

Archived invalid run:

`runs/archive/invalid/api_validation_uncompleted_adaptive_50_lenient_parser`

Remote dry-run verification:

- command: `MODE=dry-run DATA_VARIANT=uncompleted SAMPLE_SIZE=6 SPLIT=validation RUN_ID=remote_strict_finish_dryrun_6 MAX_SEARCHES=2 SEARCH_POOLS=train,validation bash run_smoke.sh`
- result: completed with 6 valid predictions and 0 missing predictions
- search counts: all 6 examples executed 1 Search call
- archived under `runs/archive/dryrun/remote_strict_finish_dryrun_6`

## Next Valid Run

Run a fresh adaptive API smoke after this fix:

`MODE=api DATA_VARIANT=uncompleted DATA_DIR=/data/chenjt/Hate/FineTune_only/data/processed/ihc SAMPLE_SIZE=50 SPLIT=validation RUN_ID=api_validation_uncompleted_adaptive_50_strict MAX_SEARCHES=2 SEARCH_POOLS=train,validation bash run_smoke.sh`
