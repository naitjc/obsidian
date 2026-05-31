# FineTuneLLM: Generative Toxicity Fine-Tuning

QLoRA generative fine-tuning and evaluation toolkit for toxicity detection on IHC/SBIC.
Current workflow is unified generative SFT that predicts `class`, `hate_class`, and `target`.

## 1. Project Layout

- `src/data/prepare_binary_data.py`: merge/clean/split datasets, remap labels, export stats
- `src/train/train_qlora_sft_binary.py`: generative SFT training (JSON generation)
- `src/eval/evaluate_generative_binary.py`: generative SFT evaluation and prediction export
- `src/eval/error_analysis.py`: false-positive/false-negative analysis from prediction files
- `scripts/`: one-command prepare/train/eval entry points
- `configs/`: model-specific QLoRA config templates
- `data/processed/`: prepared train/validation/test JSONL files and metadata
- `experiments/`: training artifacts and evaluation outputs

## 2. Environment

```bash
pip install -r requirements.txt
```

If you use private or gated model repos:

```bash
huggingface-cli login
```

## 3. Quick Start

### 3.1 Prepare data

```bash
bash scripts/run_prepare.sh ihc
bash scripts/run_prepare.sh sbic
```

Data sources are fixed in `scripts/run_prepare.sh`:

- IHC: `DATA/IHC/processed/IHC_pure.json`
- SBIC train/validation/test: `DATA/SBIC/processed/sbic_train_pure.json`, `DATA/SBIC/processed/sbic_dev_pure.json`, `DATA/SBIC/processed/sbic_test_pure.json`

Label mapping:

- `implicit_hate` -> `toxic`
- `offensive` -> `toxic`
- `not_hate` -> `non_toxic`
- `not_offensive` -> `non_toxic`
- `not_toxic` -> `non_toxic`

Output files are written to `data/processed/<dataset>/`.

### 3.2 Train (generative, with auto inference)

```bash
bash scripts/run_train_gen.sh ihc /data/public_model/qwen3.5-4b full
bash scripts/run_train_gen.sh sbic /data/public_model/qwen3.5-4b class_only
```

This command now:

- trains generative SFT model
- runs test inference automatically after training
- runs error analysis automatically

Default output directory pattern: `experiments/<dataset>_<model_tag>_sft`.

### 3.3 Evaluate existing generative checkpoint

```bash
bash scripts/run_eval_gen.sh ihc /data/public_model/qwen3.5-4b full
bash scripts/run_eval_gen.sh sbic /data/public_model/qwen3.5-4b class_only
```

Main outputs:

- `experiments/<dataset>_<model_tag>_sft/eval/test_metrics.json`
- `experiments/<dataset>_<model_tag>_sft/eval/test_predictions.jsonl`
- `experiments/<dataset>_<model_tag>_sft/eval/false_positive.jsonl`
- `experiments/<dataset>_<model_tag>_sft/eval/false_negative.jsonl`
- `experiments/<dataset>_<model_tag>_sft/eval/error_summary.json`

## 4. Extend to Other Base Models

Change the model path in script arguments, for example:

- `Qwen/Qwen2.5-7B-Instruct`
- `mistralai/Mistral-7B-Instruct-v0.3`
- `meta-llama/Llama-3.1-8B-Instruct`

`configs/` provides baseline hyperparameter templates (reference-only unless you manually apply them in scripts/CLI).

## 5. Notes

- Target hardware: single GPU with ~48GB or more memory.
- 4-bit QLoRA is enabled in provided scripts (`--use-4bit`).
- If OOM occurs, lower `max_length` or eval/train batch size, then increase gradient accumulation.
