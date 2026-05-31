#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LOG_DIR="${ROOT_DIR}/logs"
mkdir -p "${LOG_DIR}"

CONDA_BIN="/data/chenjt/miniconda3/bin/conda"
CONDA_RUN=("${CONDA_BIN}" run --no-capture-output -n cjt)
SCHEMA="class_target"

RUNS=(
  "ihc /data/public_model/Qwen3-8B"
  "sbic /data/public_model/Mistral-7B-Instruct-v0.3"
  "sbic /data/public_model/Qwen3-4B"
  "sbic /data/public_model/Qwen3-8B"
)

echo "[$(date '+%F %T')] Starting unfinished class_target runs"

run_count=0
total_runs="${#RUNS[@]}"
failed=0

for item in "${RUNS[@]}"; do
  run_count=$((run_count + 1))
  read -r dataset model <<< "${item}"
  model_tag="$(basename "${model}")"
  model_tag="$(echo "${model_tag}" | sed 's/[^[:alnum:]_.-]/_/g')"
  step_log="${LOG_DIR}/unfinished_${run_count}_${dataset}_${SCHEMA}_${model_tag}.log"
  output_dir="${ROOT_DIR}/experiments/${dataset}_${model_tag}_${SCHEMA}_sft"
  metrics_file="${output_dir}/eval/test_metrics.json"
  adapter_file="${output_dir}/adapter_model.safetensors"

  echo "[$(date '+%F %T')] [${run_count}/${total_runs}] START dataset=${dataset} schema=${SCHEMA} model=${model}"

  if [[ -f "${metrics_file}" ]]; then
    echo "[$(date '+%F %T')] [${run_count}/${total_runs}] SKIP completed metrics=${metrics_file}" > "${step_log}"
    echo "[$(date '+%F %T')] [${run_count}/${total_runs}] SKIP dataset=${dataset} schema=${SCHEMA} model=${model} reason=metrics_exists"
    continue
  fi

  if [[ -f "${adapter_file}" ]]; then
    if "${CONDA_RUN[@]}" bash "${ROOT_DIR}/scripts/run_eval_gen.sh" "${dataset}" "${model}" "${SCHEMA}" > "${step_log}" 2>&1; then
      echo "[$(date '+%F %T')] [${run_count}/${total_runs}] DONE eval_only dataset=${dataset} schema=${SCHEMA} model=${model} log=${step_log}"
    else
      failed=$((failed + 1))
      echo "[$(date '+%F %T')] [${run_count}/${total_runs}] FAIL eval_only dataset=${dataset} schema=${SCHEMA} model=${model} log=${step_log}"
    fi
    continue
  fi

  if "${CONDA_RUN[@]}" bash "${ROOT_DIR}/scripts/run_train_gen.sh" "${dataset}" "${model}" "${SCHEMA}" > "${step_log}" 2>&1; then
    if "${CONDA_RUN[@]}" bash "${ROOT_DIR}/scripts/run_eval_gen.sh" "${dataset}" "${model}" "${SCHEMA}" >> "${step_log}" 2>&1; then
      echo "[$(date '+%F %T')] [${run_count}/${total_runs}] DONE dataset=${dataset} schema=${SCHEMA} model=${model} log=${step_log}"
    else
      failed=$((failed + 1))
      echo "[$(date '+%F %T')] [${run_count}/${total_runs}] FAIL eval dataset=${dataset} schema=${SCHEMA} model=${model} log=${step_log}"
    fi
  else
    failed=$((failed + 1))
    echo "[$(date '+%F %T')] [${run_count}/${total_runs}] FAIL train dataset=${dataset} schema=${SCHEMA} model=${model} log=${step_log}"
  fi
done

echo "[$(date '+%F %T')] Unfinished class_target runs completed failed=${failed}"
exit "${failed}"
