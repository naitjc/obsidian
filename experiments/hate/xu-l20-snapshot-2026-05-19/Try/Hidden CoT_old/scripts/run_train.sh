#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="/home/chenjt/Hate/Try/Hidden CoT"
SRC_DIR="$ROOT_DIR/src"
RUN_ID="${RUN_ID:-$(date +%Y%m%d_%H%M%S)}"

SEED="${SEED:-42}"
DATA_DIR="${DATA_DIR:-/home/chenjt/Hate/DATA/IHC/processed}"
TRAIN_FILE="${TRAIN_FILE:-$DATA_DIR/train.json}"
TEST_FILE="${TEST_FILE:-$DATA_DIR/test.json}"
VALIDATION_FILE="${VALIDATION_FILE:-}"
if [[ -z "$VALIDATION_FILE" ]]; then
  if [[ -f "$DATA_DIR/valid.json" ]]; then
    VALIDATION_FILE="$DATA_DIR/valid.json"
  elif [[ -f "$DATA_DIR/vaild.json" ]]; then
    VALIDATION_FILE="$DATA_DIR/vaild.json"
  else
    VALIDATION_FILE="$DATA_DIR/valid.json"
  fi
fi

MODEL_NAME="${MODEL_NAME:-/data/public_model/qwen3-4b}"
OUTPUT_DIR="${OUTPUT_DIR:-$ROOT_DIR/outputs/$RUN_ID}"

COT_DROPOUT="${COT_DROPOUT:-0.3}"
LAMBDA_CLASS="${LAMBDA_CLASS:-1.0}"
LAMBDA_HATE="${LAMBDA_HATE:-1.0}"
LAMBDA_TARGET="${LAMBDA_TARGET:-0.5}"
ALIGN_GAMMA="${ALIGN_GAMMA:-0.5}"
NORM_MODE="${NORM_MODE:-hybrid}"

mkdir -p "$OUTPUT_DIR"

python "$SRC_DIR/train_hidden_cot.py" \
  --model-name-or-path "$MODEL_NAME" \
  --train-file "$TRAIN_FILE" \
  --validation-file "$VALIDATION_FILE" \
  --output-dir "$OUTPUT_DIR" \
  --max-length 768 \
  --learning-rate 2e-4 \
  --num-train-epochs 2 \
  --per-device-train-batch-size 2 \
  --per-device-eval-batch-size 2 \
  --gradient-accumulation-steps 8 \
  --warmup-ratio 0.05 \
  --weight-decay 0.01 \
  --logging-steps 20 \
  --eval-steps 100 \
  --save-steps 100 \
  --seed "$SEED" \
  --lora-r 8 \
  --lora-alpha 16 \
  --lora-dropout 0.05 \
  --bf16 \
  --gradient-checkpointing \
  --cot-dropout "$COT_DROPOUT" \
  --lambda-class "$LAMBDA_CLASS" \
  --lambda-hate "$LAMBDA_HATE" \
  --lambda-target "$LAMBDA_TARGET" \
  --align-gamma "$ALIGN_GAMMA" \
  --norm-mode "$NORM_MODE"

python "$SRC_DIR/eval_hidden_cot.py" \
  --base-model "$MODEL_NAME" \
  --adapter-path "$OUTPUT_DIR" \
  --test-file "$TEST_FILE" \
  --output-dir "$OUTPUT_DIR" \
  --eval-output-dir "$OUTPUT_DIR/eval" \
  --max-length 768 \
  --max-new-tokens 128 \
  --eval-batch-size 8 \
  --norm-mode "$NORM_MODE" \
  --bf16

echo "Run complete: $OUTPUT_DIR"
