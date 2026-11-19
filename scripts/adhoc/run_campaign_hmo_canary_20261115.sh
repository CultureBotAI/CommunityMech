#!/usr/bin/env bash
# Plan or run the single 000296 campaign canary's focused checks, 2026-11-15.
# Inputs: exact source revision/new generation. Outputs: exclusive native receipts.
# No batch, curation or provider acquisition. --run awaits Phase2 handoff.
set -uo pipefail
TASK_ROOT=$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)
cd "$TASK_ROOT" || exit 2
if [ "$#" -ne 3 ] || [[ ! "$1" =~ ^--(plan|run)$ ]] || [[ ! "$2" =~ ^[0-9a-f]{40}$ ]] || [[ ! "$3" =~ ^[0-9]+$ ]]; then
  echo 'Usage: run_campaign_hmo_canary_20261115.sh --plan|--run EXPECTED_SHA GENERATION' >&2
  exit 2
fi
export PATH="$TASK_ROOT/.venv/bin:/Users/marcin/.local/bin:/opt/homebrew/bin:/usr/bin:/bin:/usr/sbin:/sbin"
if [ "$1" = --plan ]; then
  exec .venv/bin/python scripts/adhoc/check_campaign_hmo_canary_20261115.py --expected-revision "$2" --generation "$3" --plan
fi
TASK_FAILED=0
for TASK_GATE in schema strict terms references gtdb domain history scalars network; do
  .venv/bin/python scripts/adhoc/check_campaign_hmo_canary_20261115.py --expected-revision "$2" --generation "$3" --gate "$TASK_GATE" || TASK_FAILED=1
done
.venv/bin/python scripts/reference_assertion_coverage.py \
  --record kb/communities/Ecoli_Bifidobacterium_bifidum_Infant_gut_HMO_Mutualism_Coculture.yaml \
  --output ".temp/campaign-resume-20261115/hmo-coverage-$3" || TASK_FAILED=1
exit "$TASK_FAILED"
