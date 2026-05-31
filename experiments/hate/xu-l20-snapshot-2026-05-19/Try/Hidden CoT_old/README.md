# Hidden CoT on IHC

This project trains and evaluates a Hidden CoT model with:

- Hidden structured hint (`[THINK]`) used only during training
- CoT dropout to randomly remove `[THINK]` on part of training samples
- Joint structured generation for `class`, `hate_class`, and `target`

## Project structure

- `src/train_hidden_cot.py`: training (weighted loss + CoT dropout)
- `src/eval_hidden_cot.py`: test evaluation
- `src/common.py`: prompt/output formatting and parsing
- `src/metrics.py`: classification and set-level metrics
- `scripts/run_train.sh`: one full run (train -> eval)
- `scripts/run_grid.sh`: grid search over `cot_dropout` and `lambda_target`

## Dataset format

The pipeline now reads pre-split files directly from `DATA_DIR`:

- `train.json`
- `valid.json` (or `vaild.json` for compatibility)
- `test.json`

## Normalization modes

The pipeline supports two normalization modes for `hate_class` and `target`:

- `minimal` (default): only basic cleanup (trim/case/none handling/dedup)
- `hybrid`: `minimal` + lightweight surface-form normalization (punctuation and simple plural normalization)

No dataset-specific hard synonym mapping is used.

## Quick start

```bash
chmod +x scripts/run_train.sh scripts/run_grid.sh
bash scripts/run_train.sh
```

## Common overrides

```bash
DATA_DIR=/path/to/dataset \
MODEL_NAME=/path/to/base_model \
OUTPUT_DIR=/path/to/output \
NORM_MODE=minimal \
bash scripts/run_train.sh
```

You can also override file paths explicitly:

```bash
TRAIN_FILE=/path/to/train.json \
VALIDATION_FILE=/path/to/valid.json \
TEST_FILE=/path/to/test.json \
bash scripts/run_train.sh
```

## Key outputs

- `outputs/<run>/metrics/train_metrics.json`
- `outputs/<run>/metrics/validation_metrics.json`
- `outputs/<run>/metrics/training_loss_curve.json`
- `outputs/<run>/plots/training_loss_curve.png`
- `outputs/<run>/eval/test_metrics.json`
- `outputs/<run>/eval/test_predictions.jsonl`

`<run>` defaults to the experiment start timestamp: `YYYYMMDD_HHMMSS`.
You can override it by setting `RUN_ID` or directly setting `OUTPUT_DIR`.

## Notes

- Eval stage no longer computes or saves eval loss.
- Inference uses only `[OUTPUT]` parsing, not `[THINK]` generation.
