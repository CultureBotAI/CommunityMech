#!/usr/bin/env bash
# Purpose: same-path one-record canary and nine native successor gates, #2831.
# Inputs: exact de4c checkout, current accepted 000122, local frozen environment.
# Outputs: exclusive retained receipts/logs/exit files in .temp; 2026-11-15.
set -euo pipefail
cd "$(dirname "$0")/../.."
export UV_NO_SYNC=true JUST_NO_DOTENV=true PYTHONUNBUFFERED=1
mode="${1:?canary or remaining required}"
runner=scripts/adhoc/check_gut_successor_20261115.py
state=.temp/phase2-gut-20261115
if [[ "$mode" == canary ]]; then
  gates=(schema)
elif [[ "$mode" == remaining ]]; then
  test "$(cat "$state/canary-schema-historical-001.exit")" = 0
  test -s "$state/canary-schema-historical-001.log"
  test -s "$state/canary-schema-historical-001.json"
  gates=(strict terms references gtdb domain scalars history network)
else
  exit 2
fi
for gate in "${gates[@]}"; do
  .venv/bin/python "$runner" "$gate" --name "canary-$gate-historical-001" --plan
  .venv/bin/python "$runner" "$gate" --name "canary-$gate-historical-001"
done
