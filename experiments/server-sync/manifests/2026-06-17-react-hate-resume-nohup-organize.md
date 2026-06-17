# ReAct Hate Resume, Nohup, And Run Directory Cleanup

Generated: 2026-06-17

## Scope

Project:

`huashan:/data/chenjt/Hate/Try/ReAct_hate_deepseek_v4_flash`

Local staging bundle:

`experiments/server-sync/staging/react-hate-deepseek-v4-flash`

## Changes

- Added `--resume` support to `scripts/react_ihc_smoke.py`.
- Added `RESUME=1` handling in `run_smoke.sh`.
- Added `launch_nohup.sh` as the default launcher for long runs.
- API runs now default to `runs/api/{split}/{RUN_ID}`.
- Dry-run checks launched through `launch_nohup.sh` default to
  `runs/archive/dryrun/{RUN_ID}`.
- Moved the interrupted strict adaptive API run from:

  `runs/api_validation_uncompleted_adaptive_50_strict`

  to:

  `runs/api/validation/api_validation_uncompleted_adaptive_50_strict`
- Moved local staging dry-run outputs under `runs/archive/dryrun/` and the
  local missing-data preflight output under `runs/archive/failed/`.

## Resume Semantics

When `RESUME=1` is set:

- existing `config.json` must match the requested run settings
- existing `smoke_predictions.jsonl` is loaded
- predictions are de-duplicated by sample id, with index fallback
- completed samples are skipped
- new predictions and traces are appended
- partial and final metrics are recomputed over all completed predictions

If the run settings do not match, the script exits instead of mixing artifacts.

## Verification

Local:

- `python3 -m py_compile scripts/react_ihc_smoke.py`
- dry-run resume test with 4 samples
- second resume pass skipped all 4 completed samples

Remote on huashan:

- `python3 -m py_compile scripts/react_ihc_smoke.py`
- `bash -n run_smoke.sh`
- `bash -n launch_nohup.sh`
- nohup dry-run resume test with 3 samples
- second resume pass skipped the completed samples without duplicates
- nohup log append behavior verified with a 2-sample dry-run

The interrupted API run currently has:

- completed predictions: `33/50`
- completed traces: `33/50`
- partial accuracy: `0.6666666666666666`
- partial macro-F1: `0.6552706552706553`
- missing predictions: `0`

## Resume Command

Use this command after setting the DeepSeek key in the same shell:

```bash
cd /data/chenjt/Hate/Try/ReAct_hate_deepseek_v4_flash

MODE=api DATA_VARIANT=uncompleted \
DATA_DIR=/data/chenjt/Hate/FineTune_only/data/processed/ihc \
SAMPLE_SIZE=50 SPLIT=validation RUN_ID=api_validation_uncompleted_adaptive_50_strict \
MAX_SEARCHES=2 SEARCH_POOLS=train,validation RESUME=1 \
bash launch_nohup.sh
```

Monitor with:

```bash
tail -f runs/api/validation/api_validation_uncompleted_adaptive_50_strict.run.log
```
