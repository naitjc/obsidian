#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT_DIR}"

INPUT_DIR="${1:-/data/chenjt/hate/DATA/llm_target_filled/IHC/processed}"
OUT_DIR="${ROOT_DIR}/data/processed/ihc_filled"

PYTHON_BIN="${PYTHON_BIN:-/data/chenjt/miniconda3/envs/cjt/bin/python}"

"${PYTHON_BIN}" -m src.data.prepare_filled_ihc_data \
  --input-dir "${INPUT_DIR}" \
  --output-dir "${OUT_DIR}"

echo "Prepared filled IHC data in ${OUT_DIR}"
