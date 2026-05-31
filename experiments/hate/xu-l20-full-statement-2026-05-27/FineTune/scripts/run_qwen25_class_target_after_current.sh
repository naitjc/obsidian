#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LOG_DIR="${ROOT_DIR}/logs"
mkdir -p "${LOG_DIR}"

WAIT_PID="${1:-1289140}"
CONDA_BIN="/data/chenjt/miniconda3/bin/conda"
CONDA_RUN=("${CONDA_BIN}" run --no-capture-output -n cjt)

DATASETS=("ihc" "sbic")
MODEL="/data/public_model/Qwen2.5-7B"
SCHEMA="class_target"

echo "[$(date '+%F %T')] Waiting for current class_target queue pid=${WAIT_PID}"
while kill -0 "${WAIT_PID}" 2>/dev/null; do
  sleep 60
done

echo "[$(date '+%F %T')] Starting Qwen2.5-7B class_target backfill"

run_count=0
total_runs="${#DATASETS[@]}"

for dataset in "${DATASETS[@]}"; do
  run_count=$((run_count + 1))
  model_tag="$(basename "${MODEL}")"
  model_tag="$(echo "${model_tag}" | sed 's/[^[:alnum:]_.-]/_/g')"
  step_log="${LOG_DIR}/backfill_${run_count}_${dataset}_${SCHEMA}_${model_tag}.log"
  output_dir="${ROOT_DIR}/experiments/${dataset}_${model_tag}_${SCHEMA}_sft"
  metrics_file="${output_dir}/eval/test_metrics.json"
  adapter_file="${output_dir}/adapter_model.safetensors"

  echo "[$(date '+%F %T')] [${run_count}/${total_runs}] START dataset=${dataset} schema=${SCHEMA} model=${MODEL}"

  if [[ -f "${metrics_file}" ]]; then
    echo "[$(date '+%F %T')] [${run_count}/${total_runs}] SKIP completed metrics=${metrics_file}" > "${step_log}"
    echo "[$(date '+%F %T')] [${run_count}/${total_runs}] SKIP dataset=${dataset} schema=${SCHEMA} model=${MODEL} reason=metrics_exists"
    continue
  fi

  if [[ -f "${adapter_file}" ]]; then
    "${CONDA_RUN[@]}" bash "${ROOT_DIR}/scripts/run_eval_gen.sh" "${dataset}" "${MODEL}" "${SCHEMA}" > "${step_log}" 2>&1
  else
    "${CONDA_RUN[@]}" bash "${ROOT_DIR}/scripts/run_train_gen.sh" "${dataset}" "${MODEL}" "${SCHEMA}" > "${step_log}" 2>&1
    "${CONDA_RUN[@]}" bash "${ROOT_DIR}/scripts/run_eval_gen.sh" "${dataset}" "${MODEL}" "${SCHEMA}" >> "${step_log}" 2>&1
  fi

  echo "[$(date '+%F %T')] [${run_count}/${total_runs}] DONE dataset=${dataset} schema=${SCHEMA} model=${MODEL} log=${step_log}"
done

echo "[$(date '+%F %T')] Qwen2.5-7B class_target backfill completed"
