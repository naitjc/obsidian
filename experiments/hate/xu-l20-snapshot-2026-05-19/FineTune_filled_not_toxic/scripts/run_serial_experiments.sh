#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LOG_DIR="${ROOT_DIR}/logs"
mkdir -p "${LOG_DIR}"

DATASETS=("ihc" "sbic")
SCHEMAS=("class_only" "full")
MODELS=(
  "/data/public_model/Mistral-7B-Instruct-v0.3"
  "/data/public_model/Qwen2.5-7B"
)

echo "[$(date '+%F %T')] Starting serial in-domain experiments"
echo "[$(date '+%F %T')] Preparing datasets: ihc, sbic"

bash "${ROOT_DIR}/scripts/run_prepare.sh" ihc
bash "${ROOT_DIR}/scripts/run_prepare.sh" sbic

echo "[$(date '+%F %T')] Data preparation completed"

run_count=0
total_runs=$(( ${#DATASETS[@]} * ${#SCHEMAS[@]} * ${#MODELS[@]} ))

for dataset in "${DATASETS[@]}"; do
  for schema in "${SCHEMAS[@]}"; do
    for model in "${MODELS[@]}"; do
      run_count=$((run_count + 1))
      model_tag="$(basename "${model}")"
      model_tag="$(echo "${model_tag}" | sed 's/[^[:alnum:]_.-]/_/g')"
      step_log="${LOG_DIR}/${run_count}_${dataset}_${schema}_${model_tag}.log"
      output_dir="${ROOT_DIR}/experiments/${dataset}_${model_tag}_${schema}_sft"
      metrics_file="${output_dir}/eval/test_metrics.json"
      adapter_file="${output_dir}/adapter_model.safetensors"

      echo "[$(date '+%F %T')] [${run_count}/${total_runs}] START dataset=${dataset} schema=${schema} model=${model}"

      if [[ -f "${metrics_file}" ]]; then
        echo "[$(date '+%F %T')] [${run_count}/${total_runs}] SKIP completed metrics=${metrics_file}" > "${step_log}"
        echo "[$(date '+%F %T')] [${run_count}/${total_runs}] SKIP dataset=${dataset} schema=${schema} model=${model} reason=metrics_exists"
        continue
      fi

      if [[ -f "${adapter_file}" ]]; then
        bash "${ROOT_DIR}/scripts/run_eval_gen.sh" "${dataset}" "${model}" "${schema}" > "${step_log}" 2>&1
      else
        bash "${ROOT_DIR}/scripts/run_train_gen.sh" "${dataset}" "${model}" "${schema}" > "${step_log}" 2>&1
        bash "${ROOT_DIR}/scripts/run_eval_gen.sh" "${dataset}" "${model}" "${schema}" >> "${step_log}" 2>&1
      fi

      echo "[$(date '+%F %T')] [${run_count}/${total_runs}] DONE dataset=${dataset} schema=${schema} model=${model} log=${step_log}"
    done
  done
done

echo "[$(date '+%F %T')] All serial experiments completed"
