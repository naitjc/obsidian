#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT_DIR}"

BASE_MODEL="${1:?Usage: bash scripts/run_eval_target_input.sh MODEL_PATH}"
MODEL_TAG="$(basename "${BASE_MODEL}")"
MODEL_TAG="$(echo "${MODEL_TAG}" | sed 's/[^[:alnum:]_.-]/_/g')"

ADAPTER_PATH="${ROOT_DIR}/experiments/ihc_filled_${MODEL_TAG}_target_input_class_only_sft"
TEST_FILE="${ROOT_DIR}/data/processed/ihc_filled/test.jsonl"
EVAL_OUT="${ADAPTER_PATH}/eval"
PYTHON_BIN="${PYTHON_BIN:-/data/chenjt/miniconda3/envs/cjt/bin/python}"

"${PYTHON_BIN}" -m src.eval.evaluate_generative_binary \
  --base-model "${BASE_MODEL}" \
  --adapter-path "${ADAPTER_PATH}" \
  --test-file "${TEST_FILE}" \
  --output-dir "${EVAL_OUT}" \
  --schema-mode target_input_class_only \
  --max-length 512 \
  --max-new-tokens 32 \
  --bf16

"${PYTHON_BIN}" -m src.eval.error_analysis \
  --predictions-file "${EVAL_OUT}/test_predictions.jsonl" \
  --output-dir "${EVAL_OUT}"

echo "Evaluation outputs in ${EVAL_OUT}"
