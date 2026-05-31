#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LOG_DIR="${ROOT_DIR}/logs"
mkdir -p "${LOG_DIR}"

LOG_FILE="${LOG_DIR}/serial_16runs_$(date '+%Y%m%d_%H%M%S').log"
nohup bash "${ROOT_DIR}/scripts/run_serial_experiments.sh" > "${LOG_FILE}" 2>&1 &
PID="$!"

echo "Started serial experiments"
echo "PID: ${PID}"
echo "Log: ${LOG_FILE}"
