#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT_DIR}"

MODEL_NAME="${1:?Usage: bash scripts/run_train_target_input.sh MODEL_PATH}"
MODEL_TAG="$(basename "${MODEL_NAME}")"
MODEL_TAG="$(echo "${MODEL_TAG}" | sed 's/[^[:alnum:]_.-]/_/g')"

TRAIN_FILE="${ROOT_DIR}/data/processed/ihc_filled/train.jsonl"
VALID_FILE="${ROOT_DIR}/data/processed/ihc_filled/validation.jsonl"
OUTPUT_DIR="${ROOT_DIR}/experiments/ihc_filled_${MODEL_TAG}_target_input_class_only_sft"
PYTHON_BIN="${PYTHON_BIN:-/data/chenjt/miniconda3/envs/cjt/bin/python}"

"${PYTHON_BIN}" -m src.train.train_qlora_sft_binary \
  --model-name-or-path "${MODEL_NAME}" \
  --train-file "${TRAIN_FILE}" \
  --validation-file "${VALID_FILE}" \
  --output-dir "${OUTPUT_DIR}" \
  --schema-mode target_input_class_only \
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

echo "Training outputs in ${OUTPUT_DIR}"
