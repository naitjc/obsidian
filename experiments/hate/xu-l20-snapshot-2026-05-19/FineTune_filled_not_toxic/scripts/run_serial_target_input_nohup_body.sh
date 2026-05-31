#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT_DIR}"

bash scripts/run_prepare_filled.sh /data/chenjt/hate/DATA/llm_target_filled/IHC/processed

MODELS=(
  "/data/public_model/Mistral-7B-Instruct-v0.3"
  "/data/public_model/Qwen3-4B"
  "/data/public_model/Qwen3-8B"
  "/data/public_model/Qwen2.5-7B"
)

for model in "${MODELS[@]}"; do
  echo "===== $(date '+%F %T') train ${model} ====="
  bash scripts/run_train_target_input.sh "${model}"
  echo "===== $(date '+%F %T') eval ${model} ====="
  bash scripts/run_eval_target_input.sh "${model}"
  echo "===== $(date '+%F %T') done ${model} ====="
done

echo "===== $(date '+%F %T') all done ====="
