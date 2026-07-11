# IHC Workflow Valid-200 FineTune Baselines Manifest

- Source framework: `xu-l20:/data/chenjt/hate/FineTune`
- Target: `xu-l20:/data/chenjt/hate/ihc-workflow-valid200-finetune-baselines`
- Adapters: `statement_full_v1/text_label_target_1x/{Qwen3-4B,Qwen3-8B}`
- Evaluation sample: fixed workflow v3 validation-200, selected from the FineTune validation split in workflow order
- Input boundary: model receives only `text`
- Output schema: `class_hate_class_target_statement_all_rows`
- Primary metric: class Macro-F1
- Execution: serial Qwen3-4B then Qwen3-8B, greedy decoding, BF16, max length 512, max new tokens 192

## Local bundle

- `code/build_valid200.py`: deterministic normalized-text selection with uniqueness and 100/100 label checks
- `configs/run_valid200_finetune_baselines.sh`: serial launcher using the existing evaluator
- `README.md`: protocol, paths, and run entry point

No model weights, adapters, full datasets, predictions, credentials, or test-1869 labels are included in the local bundle.

## Completed results

- Qwen3-4B: Macro-F1 `0.8397435897`, accuracy `0.84`, TN/FP/FN/TP `88/12/20/80`
- Qwen3-8B: Macro-F1 `0.8195488722`, accuracy `0.82`, TN/FP/FN/TP `87/13/23/77`
- Output validity: both models produced 200/200 valid JSON outputs with parsed classes; zero fallback classifications
- Cross-model disagreement: 22 rows; Qwen3-4B wins 13 and Qwen3-8B wins 9
- Local retained diagnostics: only the two compact `test_metrics.json` files
- Remote-only diagnostics: bulk `test_predictions.jsonl` and run logs
