# Huashan V9 Current-Validation Runner

- Timestamp: 2026-07-07
- Remote workspace: `huashan:/data/chenjt/Hate/Try/ihc-target-relation-workflow`
- Added remote script: `scripts/run_v9_current_validation.py`

## Purpose

Run the prior `raw-target-relation-memory-v9` method on the current huashan 200-sample validation subset instead of the earlier balanced 100-toxic/100-not-toxic validation set.

## Inputs

- Corpus: `data/corpora/target_only.jsonl`
- Validation texts: `private/validation_texts.json`
- Validation labels: `private/validation_labels.json`
- Embeddings:
  - `private/embeddings/bge-small-en-v1.5/training/text.npy`
  - `private/embeddings/bge-small-en-v1.5/queries/validation/text.npy`

## Dry Run

The dry run completed without API calls:

- samples: 200
- label counts: `not_toxic=142`, `toxic=58`
- training rows: 14,930
- training embedding shape: `[14930, 384]`
- query embedding shape: `[200, 384]`
- relation block counts:
  - attacked blocks: 1,008
  - mentioned blocks: 597

## Run Command

Run from a shell where `MODEL_API_KEY`/`MODEL_BASE_URL` or `DEEPSEEK_API_KEY`/`DEEPSEEK_BASE_URL` are set:

```bash
cd /data/chenjt/Hate/Try/ihc-target-relation-workflow
nohup /data/chenjt/miniconda3/envs/cjt/bin/python scripts/run_v9_current_validation.py \
  --workers 4 \
  --run-name v9-current-200 \
  > logs/v9-current-validation.log 2>&1 &
```

Outputs:

- `runs/v9-current-validation/v9-current-200/metrics.json`
- `runs/v9-current-validation/v9-current-200/predictions.jsonl`
- `runs/v9-current-validation/v9-current-200/traces/`
- checkpoint: `checkpoints/v9-current-validation.json`

## Completed Result

Run path: `huashan:/data/chenjt/Hate/Try/ihc-target-relation-workflow/runs/v9-current-validation/v9-current-200`

Metrics:

- samples: 200
- label counts: `not_toxic=142`, `toxic=58`
- accuracy: 0.79
- macro-F1: 0.75
- toxic: precision 0.6290, recall 0.6724, F1 0.65, support 58
- not_toxic: precision 0.8623, recall 0.8380, F1 0.85, support 142
- confusion matrix:
  - toxic -> toxic: 39
  - toxic -> not_toxic: 19
  - not_toxic -> toxic: 23
  - not_toxic -> not_toxic: 119
- prediction counts: `not_toxic=138`, `toxic=62`

Comparison on the same current 200-sample subset:

| Method | Macro-F1 | FP not_toxic->toxic | FN toxic->not_toxic |
|---|---:|---:|---:|
| `raw-target-relation-memory-v9` temporary runner | 0.7500 | 23 | 19 |
| current `target_only` v9-like summary-json run | 0.4720 | 102 | 3 |
| previous `target_only` summary-json run | 0.5044 | 95 | 4 |

Interpretation: the current 142/58 validation subset does not by itself explain the poor summary-json results. The main gap is structural: v9 keeps a richer analysis text and applies explicit classification rules, while the summary-json workflow compresses relation evidence into short pattern arrays and then classifies from query plus summary only.
