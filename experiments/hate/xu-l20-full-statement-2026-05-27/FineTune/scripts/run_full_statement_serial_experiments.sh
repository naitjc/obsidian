#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LOG_DIR="${ROOT_DIR}/logs"
mkdir -p "${LOG_DIR}"

CONDA_BIN="/data/chenjt/miniconda3/bin/conda"
CONDA_RUN=("${CONDA_BIN}" run --no-capture-output -n cjt)

DATASETS=("ihc" "sbic")
SCHEMA="full_statement"
MODELS=(
  "/data/public_model/Mistral-7B-Instruct-v0.3"
  "/data/public_model/Qwen2.5-7B"
  "/data/public_model/Qwen3-4B"
  "/data/public_model/Qwen3-8B"
)

echo "[$(date '+%F %T')] Starting serial full_statement in-domain experiments"
echo "[$(date '+%F %T')] Rebuilding processed datasets with statement: ihc, sbic"

for dataset in "${DATASETS[@]}"; do
  "${CONDA_RUN[@]}" bash "${ROOT_DIR}/scripts/run_prepare.sh" "${dataset}"
  for split in train validation test; do
    data_file="${ROOT_DIR}/data/processed/${dataset}/${split}.jsonl"
    if [[ ! -f "${data_file}" ]]; then
      echo "[$(date '+%F %T')] FAIL missing_processed_data=${data_file}"
      exit 1
    fi
  done
done

echo "[$(date '+%F %T')] Processed data rebuild completed"

run_count=0
total_runs=$(( ${#DATASETS[@]} * ${#MODELS[@]} ))

for dataset in "${DATASETS[@]}"; do
  for model in "${MODELS[@]}"; do
    run_count=$((run_count + 1))
    model_tag="$(basename "${model}")"
    model_tag="$(echo "${model_tag}" | sed 's/[^[:alnum:]_.-]/_/g')"
    step_log="${LOG_DIR}/${run_count}_${dataset}_${SCHEMA}_${model_tag}.log"
    output_dir="${ROOT_DIR}/experiments/${dataset}_${model_tag}_${SCHEMA}_sft"
    metrics_file="${output_dir}/eval/test_metrics.json"
    adapter_file="${output_dir}/adapter_model.safetensors"

    echo "[$(date '+%F %T')] [${run_count}/${total_runs}] START dataset=${dataset} schema=${SCHEMA} model=${model}"

    if [[ ! -d "${model}" ]]; then
      echo "[$(date '+%F %T')] [${run_count}/${total_runs}] FAIL missing_model=${model}" > "${step_log}"
      echo "[$(date '+%F %T')] [${run_count}/${total_runs}] FAIL dataset=${dataset} schema=${SCHEMA} model=${model} reason=missing_model"
      exit 1
    fi

    if [[ ! -r "${model}" || ! -x "${model}" ]]; then
      echo "[$(date '+%F %T')] [${run_count}/${total_runs}] SKIP unreadable_model=${model}" > "${step_log}"
      echo "[$(date '+%F %T')] [${run_count}/${total_runs}] SKIP dataset=${dataset} schema=${SCHEMA} model=${model} reason=unreadable_model"
      continue
    fi

    if [[ -f "${metrics_file}" ]]; then
      echo "[$(date '+%F %T')] [${run_count}/${total_runs}] SKIP completed metrics=${metrics_file}" > "${step_log}"
      echo "[$(date '+%F %T')] [${run_count}/${total_runs}] SKIP dataset=${dataset} schema=${SCHEMA} model=${model} reason=metrics_exists"
      continue
    fi

    if [[ -f "${adapter_file}" ]]; then
      "${CONDA_RUN[@]}" bash "${ROOT_DIR}/scripts/run_eval_gen.sh" "${dataset}" "${model}" "${SCHEMA}" > "${step_log}" 2>&1
    else
      "${CONDA_RUN[@]}" bash "${ROOT_DIR}/scripts/run_train_gen.sh" "${dataset}" "${model}" "${SCHEMA}" > "${step_log}" 2>&1
      "${CONDA_RUN[@]}" bash "${ROOT_DIR}/scripts/run_eval_gen.sh" "${dataset}" "${model}" "${SCHEMA}" >> "${step_log}" 2>&1
    fi

    echo "[$(date '+%F %T')] [${run_count}/${total_runs}] DONE dataset=${dataset} schema=${SCHEMA} model=${model} log=${step_log}"
  done
done

echo "[$(date '+%F %T')] All serial full_statement experiments completed"
