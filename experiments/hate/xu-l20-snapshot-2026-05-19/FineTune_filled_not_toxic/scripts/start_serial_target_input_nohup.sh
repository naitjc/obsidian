#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT_DIR}"

mkdir -p logs
LOG_FILE="${ROOT_DIR}/logs/target_input_serial_$(date '+%Y%m%d_%H%M%S').log"

nohup bash scripts/run_serial_target_input_nohup_body.sh > "${LOG_FILE}" 2>&1 &
PID="$!"

echo "${PID}" > "${ROOT_DIR}/logs/target_input_serial.pid"
echo "Started serial target-input fine-tuning PID=${PID}"
echo "Log: ${LOG_FILE}"
