#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT_DIR}"

DATASET="${1:-sbic}"
MODEL_NAME="${2:-/data/public_model/qwen3.5-4b}"
SCHEMA_MODE="${3:-full}"
if [[ "${DATASET}" != "ihc" && "${DATASET}" != "sbic" ]]; then
  echo "Usage: bash scripts/run_train_gen.sh [ihc|sbic] [model_path] [class_only|class_target|full]"
  exit 1
fi

if [[ "${SCHEMA_MODE}" != "class_only" && "${SCHEMA_MODE}" != "class_target" && "${SCHEMA_MODE}" != "full" ]]; then
  echo "Usage: bash scripts/run_train_gen.sh [ihc|sbic] [model_path] [class_only|class_target|full]"
  exit 1
fi

MODEL_TAG="$(basename "${MODEL_NAME}")"
MODEL_TAG="$(echo "${MODEL_TAG}" | sed 's/[^[:alnum:]_.-]/_/g')"
TRAIN_FILE="${ROOT_DIR}/data/processed/${DATASET}/train.jsonl"
VALID_FILE="${ROOT_DIR}/data/processed/${DATASET}/validation.jsonl"
OUTPUT_DIR="${ROOT_DIR}/experiments/${DATASET}_${MODEL_TAG}_${SCHEMA_MODE}_sft"

python -m src.train.train_qlora_sft_binary \
  --model-name-or-path "${MODEL_NAME}" \
  --train-file "${TRAIN_FILE}" \
  --validation-file "${VALID_FILE}" \
  --output-dir "${OUTPUT_DIR}" \
  --schema-mode "${SCHEMA_MODE}" \
  --max-length 512 \
  --learning-rate 2e-4 \
  --num-train-epochs 3 \
  --per-device-train-batch-size 8 \
  --per-device-eval-batch-size 8 \
  --gradient-accumulation-steps 4 \
  --warmup-ratio 0.05 \
  --weight-decay 0.01 \
  --logging-steps 20 \
  --eval-steps 100 \
  --lora-r 8 \
  --lora-alpha 16 \
  --lora-dropout 0.05 \
  --seed 42 \
  --bf16 \
  --gradient-checkpointing

echo "Generative training outputs in ${OUTPUT_DIR}"
echo "Training completed. Run scripts/run_eval_gen.sh separately for evaluation."
