#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT_DIR}"

DATASET="${1:-ihc}"
if [[ "${DATASET}" != "ihc" && "${DATASET}" != "sbic" && "${DATASET}" != "merged" ]]; then
  echo "Usage: bash scripts/run_prepare.sh [ihc|sbic|merged]"
  exit 1
fi

IHC_FILE="${ROOT_DIR}/../DATA/IHC/processed/IHC_pure.json"
SBIC_TRAIN_FILE="${ROOT_DIR}/../DATA/SBIC/processed/train_pure.json"
SBIC_VALID_FILE="${ROOT_DIR}/../DATA/SBIC/processed/dev_pure.json"
SBIC_TEST_FILE="${ROOT_DIR}/../DATA/SBIC/processed/test_pure.json"
OUT_DIR="${ROOT_DIR}/data/processed/${DATASET}"

python -m src.data.prepare_binary_data \
  --ihc-file "${IHC_FILE}" \
  --sbic-train-file "${SBIC_TRAIN_FILE}" \
  --sbic-validation-file "${SBIC_VALID_FILE}" \
  --sbic-test-file "${SBIC_TEST_FILE}" \
  --dataset "${DATASET}" \
  --output-dir "${OUT_DIR}"

echo "Prepared data in ${OUT_DIR}"
