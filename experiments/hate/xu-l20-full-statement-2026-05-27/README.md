# xu-l20 Full-Statement Experiment Archive 2026-05-27

This supplemental archive preserves the completed `full_statement` runs from
`xu-l20:/data/chenjt/hate/FineTune`. It extends the earlier
`xu-l20-snapshot-2026-05-19/` archive without changing the meaning of that
dated snapshot.

## Scope

The experiment supplies only `text` to the model and generates:

```text
class + hate_class + target + statement
```

All eight in-domain runs completed on 2026-05-27:

- datasets: `ihc`, `sbic`
- models: `Mistral-7B-Instruct-v0.3`, `Qwen2.5-7B`, `Qwen3-4B`, `Qwen3-8B`

## Preserved Evidence

- `FineTune/experiments/eval_results.md`: updated comparison across all four schemas.
- `FineTune/experiments/*_full_statement_sft/eval/`: metrics, predictions, false
  positives, false negatives, and error summaries for all eight new runs.
- `FineTune/experiments/*_full_statement_sft/`: lightweight model metadata only:
  README, adapter config, hate-class vocabulary, and trainable parameter counts.
- `FineTune/data/processed/`: rebuilt IHC/SBIC train, validation, and test data
  including `statement`.
- `FineTune/src/`, `FineTune/scripts/`, and `FineTune/logs/*full_statement*.log`:
  code and execution evidence needed to inspect the new condition.

Adapter weights, tokenizer artifacts, and training binaries were not copied.
They remain recoverable from the remote experiment directories.

## Results

IHC:

| Model | Macro F1 | Target Jaccard | Statement Jaccard |
|---|---:|---:|---:|
| Mistral-7B-Instruct-v0.3 | 0.8319 | 0.3807 | 0.0438 |
| Qwen2.5-7B | 0.8354 | 0.3708 | 0.0454 |
| Qwen3-4B | 0.8212 | 0.3470 | 0.0503 |
| Qwen3-8B | 0.8169 | 0.3377 | 0.0450 |

SBIC:

| Model | Macro F1 | Target Jaccard | Statement Jaccard |
|---|---:|---:|---:|
| Mistral-7B-Instruct-v0.3 | 0.8676 | 0.6450 | 0.0471 |
| Qwen2.5-7B | 0.8787 | 0.6550 | 0.0453 |
| Qwen3-4B | 0.8726 | 0.6595 | 0.0499 |
| Qwen3-8B | 0.8755 | 0.6621 | 0.0533 |

Adding `statement` did not improve the best classification result already in
the earlier schemas: the prior best remains Mistral `class_target` on IHC
(`0.8363`) and Qwen3-8B `class_target` on SBIC (`0.8797`). Generated
statement set overlap is low in this exact-match-style Jaccard evaluation.

## Comparability Note

`ihc_Mistral-7B-Instruct-v0.3_full_statement_sft` completed before the
batch-size adjustment with `per_device_train_batch_size=8`. The remaining
seven `full_statement` runs used `per_device_train_batch_size=2` with
`gradient_accumulation_steps=4`. Direct model ranking inside this new
condition therefore includes a training-hyperparameter difference.
