#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT_DIR}"

DATASET="${1:-sbic}"
BASE_MODEL="${2:-/data/public_model/qwen3.5-4b}"
SCHEMA_MODE="${3:-full}"
if [[ "${DATASET}" != "ihc" && "${DATASET}" != "sbic" ]]; then
  echo "Usage: bash scripts/run_eval_gen.sh [ihc|sbic] [base_model_path] [class_only|class_target|full]"
  exit 1
fi

if [[ "${SCHEMA_MODE}" != "class_only" && "${SCHEMA_MODE}" != "class_target" && "${SCHEMA_MODE}" != "full" ]]; then
  echo "Usage: bash scripts/run_eval_gen.sh [ihc|sbic] [base_model_path] [class_only|class_target|full]"
  exit 1
fi

MODEL_TAG="$(basename "${BASE_MODEL}")"
MODEL_TAG="$(echo "${MODEL_TAG}" | sed 's/[^[:alnum:]_.-]/_/g')"
ADAPTER_PATH="${ROOT_DIR}/experiments/${DATASET}_${MODEL_TAG}_${SCHEMA_MODE}_sft"
TEST_FILE="${ROOT_DIR}/data/processed/${DATASET}/test.jsonl"
EVAL_OUT="${ADAPTER_PATH}/eval"

if [[ ! -d "${ADAPTER_PATH}" ]]; then
  echo "Missing adapter directory: ${ADAPTER_PATH}"
  exit 1
fi

if [[ ! -f "${TEST_FILE}" ]]; then
  echo "Missing test file: ${TEST_FILE}"
  exit 1
fi

python -m src.eval.evaluate_generative_binary \
  --base-model "${BASE_MODEL}" \
  --adapter-path "${ADAPTER_PATH}" \
  --test-file "${TEST_FILE}" \
  --output-dir "${EVAL_OUT}" \
  --schema-mode "${SCHEMA_MODE}" \
  --max-length 512 \
  --max-new-tokens 96 \
  --bf16

python -m src.eval.error_analysis \
  --predictions-file "${EVAL_OUT}/test_predictions.jsonl" \
  --output-dir "${EVAL_OUT}"

echo "Generative evaluation outputs in ${EVAL_OUT}"
