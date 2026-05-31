#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LOG_DIR="${ROOT_DIR}/logs"
mkdir -p "${LOG_DIR}"

LOG_FILE="${LOG_DIR}/unfinished_class_target_$(date '+%Y%m%d_%H%M%S').log"
nohup bash "${ROOT_DIR}/scripts/run_unfinished_class_target.sh" > "${LOG_FILE}" 2>&1 &
PID="$!"

echo "Started unfinished class_target runs"
echo "PID: ${PID}"
echo "Log: ${LOG_FILE}"
