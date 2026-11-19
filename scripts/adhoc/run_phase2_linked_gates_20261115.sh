#!/usr/bin/env bash
# Run nine persisted native gates for one linked record (#2674/#2774/#2806).
# 2026-11-15. Inputs: record key, exact reviewed HEAD, new generation suffix.
# Output: check_phase2_linked_records receipts under repository .temp; no curation.
# Run/verify one entire record before calling this same launcher for the others.
set -uo pipefail
TASK_ROOT=$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)
cd "$TASK_ROOT" || exit 2
if [ "$#" -ne 3 ]; then
  echo 'Usage: run_phase2_linked_gates_20261115.sh ecofab|dopamine|lbnl EXPECTED_SHA GENERATION' >&2
  exit 2
fi
case "$1" in ecofab|dopamine|lbnl) ;; *) exit 2 ;; esac
if [[ ! "$2" =~ ^[0-9a-f]{40}$ ]] || [[ ! "$3" =~ ^[0-9]+$ ]]; then
  exit 2
fi
TASK_FAILED=0
for TASK_GATE in schema strict terms references gtdb domain history scalars network; do
  uv run --frozen --offline python scripts/adhoc/check_phase2_linked_records_20261115.py \
    "$TASK_GATE" --record "$1" --expected-revision "$2" \
    --name "linked-$1-$TASK_GATE-$3" || TASK_FAILED=1
done
exit "$TASK_FAILED"
