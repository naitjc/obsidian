#!/bin/bash

# 数据预处理
# Usage: bash scripts/preprocess.sh [IHC|SBIC]

DATASET=${1:-IHC}
DATA_DIR="/data/chenjt/hate/DATA"

for SPLIT in train valid test; do
    echo "Processing ${DATASET} ${SPLIT}..."
    python3 data/preprocess.py \
        --data_dir "${DATA_DIR}/${DATASET}/processed" \
        --output_dir "data/${DATASET}" \
        --split ${SPLIT} \
        --is_training
done

echo "Done!"