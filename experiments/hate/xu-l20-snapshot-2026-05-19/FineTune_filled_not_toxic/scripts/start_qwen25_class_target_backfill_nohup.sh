#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LOG_DIR="${ROOT_DIR}/logs"
mkdir -p "${LOG_DIR}"

WAIT_PID="${1:-1289140}"
LOG_FILE="${LOG_DIR}/backfill_qwen25_class_target_$(date '+%Y%m%d_%H%M%S').log"
nohup bash "${ROOT_DIR}/scripts/run_qwen25_class_target_after_current.sh" "${WAIT_PID}" > "${LOG_FILE}" 2>&1 &
PID="$!"

echo "Started Qwen2.5-7B class_target backfill"
echo "PID: ${PID}"
echo "Wait PID: ${WAIT_PID}"
echo "Log: ${LOG_FILE}"
