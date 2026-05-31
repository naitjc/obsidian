#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="/home/chenjt/Hate/Try/Hidden CoT"
SEED="${SEED:-42}"
DATA_DIR="${DATA_DIR:-/home/chenjt/Hate/DATA/IHC/processed}"
NORM_MODE="${NORM_MODE:-minimal}"

PDROPS=(0.0 0.2 0.4 0.6)
LTARGETS=(0.3 0.5 0.7)

for p in "${PDROPS[@]}"; do
  for lt in "${LTARGETS[@]}"; do
    run_id="$(date +%Y%m%d_%H%M%S)_p${p}_lt${lt}"
    out_dir="$ROOT_DIR/outputs/$run_id"
    echo "Running p_drop=$p lambda_target=$lt"
    SEED="$SEED" \
    DATA_DIR="$DATA_DIR" \
    NORM_MODE="$NORM_MODE" \
    COT_DROPOUT="$p" \
    LAMBDA_TARGET="$lt" \
    OUTPUT_DIR="$out_dir" \
    bash "$ROOT_DIR/scripts/run_train.sh"
  done
done

echo "Grid complete."
