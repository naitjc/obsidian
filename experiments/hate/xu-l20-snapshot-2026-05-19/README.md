# xu-l20 Hate Experiment Snapshot 2026-05-19

This archive preserves selected evidence from `xu-l20:/data/chenjt/hate` inside the Obsidian Vault. It keeps experiment results, predictions, error cases, configs, scripts, and derived data needed to inspect or reproduce the findings without copying large model weights.

## Scope

Copied from:

- `/data/chenjt/hate/DATA`
- `/data/chenjt/hate/FineTune`
- `/data/chenjt/hate/FineTune_filled_not_toxic`
- `/data/chenjt/hate/Try`

Local archive size at creation: 435 files, about 172 MB.

## What Was Preserved

- `FineTune/experiments/eval_results.md`: main IHC/SBIC fine-tuning score table.
- `FineTune/experiments/*/eval/`: `test_metrics.json`, `test_predictions.jsonl`, `false_positive.jsonl`, `false_negative.jsonl`, and `error_summary.json` for all copied runs.
- `FineTune_filled_not_toxic/experiments*/`: normal, target-shuffle, and target-other evaluation evidence for target-input leakage diagnostics.
- `DATA/llm_target_filled_new/` and `DATA/llm_target_filled_old/`: LLM-filled target data used by filled-not-toxic experiments.
- `DATA/fill_not_toxic_targets_with_llm.py`: generation script for filled targets.
- `FineTune*/configs/`, `FineTune*/scripts/`, `FineTune*/src/`, and processed data folders needed to understand the local pipeline.
- `Try/Hidden CoT_old/`: old Hidden CoT code, run configs, metrics, predictions, and logs.
- `Try/Dual-model_old/`: old dual-model code/config/scripts, preserved as a low-priority method attempt.

## Deliberately Not Preserved

Large or easily regenerated model artifacts were not copied:

- `adapter_model.safetensors`
- `tokenizer.json`
- `training_args.bin`
- Python bytecode and `__pycache__/`
- large original HARE dumps under `DATA/HARE/`

If exact checkpoint continuation is needed later, recover those files from `xu-l20`; this archive is intended as evidence and analysis material, not a full model checkpoint backup.

## Key FineTune Results

The full table is in `FineTune/experiments/eval_results.md`.

Best IHC runs:

| Schema | Best run | Macro F1 | Target Jaccard |
|---|---|---:|---:|
| class_only | `ihc_Mistral-7B-Instruct-v0.3_class_only_sft` | 0.8254 | n/a |
| class_target | `ihc_Mistral-7B-Instruct-v0.3_class_target_sft` | 0.8363 | 0.3633 |
| full | `ihc_Mistral-7B-Instruct-v0.3_full_sft` | 0.8330 | 0.3769 |

Best SBIC runs:

| Schema | Best run | Macro F1 | Target Jaccard |
|---|---|---:|---:|
| class_only | `sbic_Mistral-7B-Instruct-v0.3_class_only_sft` | 0.8750 | n/a |
| class_target | `sbic_Qwen3-8B_class_target_sft` | 0.8797 | 0.6682 |
| full | `sbic_Mistral-7B-Instruct-v0.3_full_sft` | 0.8784 | 0.6634 |

## Key Filled-Not-Toxic Target-Input Diagnostic

Normal filled-target input produces near-perfect classification, but target ablations collapse performance. This is evidence that row-level target input is a shortcut/leakage channel.

Normal target-input runs:

| Run | Macro F1 | Accuracy |
|---|---:|---:|
| `ihc_filled_Mistral-7B-Instruct-v0.3_target_input_class_only_sft` | 0.9866 | 0.9888 |
| `ihc_filled_Qwen2.5-7B_target_input_class_only_sft` | 0.9879 | 0.9898 |
| `ihc_filled_Qwen3-4B_target_input_class_only_sft` | 0.9847 | 0.9871 |
| `ihc_filled_Qwen3-8B_target_input_class_only_sft` | 0.9853 | 0.9877 |
| `ihc_filled_Qwen3-4B_target_input_class_only_retargeted_no_other_sft` | 0.9828 | 0.9855 |

Ablation runs:

| Ablation | Macro F1 range | Notes |
|---|---:|---|
| target replaced with `other` | 0.4107 | all four old models collapse to the same result |
| target shuffled with seed 42 | 0.4032-0.4811 | all four old models fall far below normal target-input results |

## Hidden CoT Old Trial Results

| Run | Class Macro F1 | Hate-Class Macro F1 | Target Set Jaccard |
|---|---:|---:|---:|
| `ihc_minimal_20260419_125238` | 0.7918 | 0.4184 | 0.7427 |
| `ihc_hybrid_20260419_174617` | 0.8018 | 0.4027 | 0.7504 |
| `sbic_minimal_20260419_222239` | 0.8633 | 0.6365 | 0.7771 |
| `sbic_hybrid_20260420_125507` | 0.8666 | 0.6179 | 0.7900 |

## Use In The Wiki

Treat this folder as experiment evidence. Durable conclusions already relevant to the wiki include:

- target-input evaluation can be inflated by target leakage;
- filled not-toxic target diagnostics should be framed as local evidence, not as a final paper contribution by itself;
- future relation-grounding experiments should use leakage-controlled candidate generation and report target ablations separately from main task metrics.
