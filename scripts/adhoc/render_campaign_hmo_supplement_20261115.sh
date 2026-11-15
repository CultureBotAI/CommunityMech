#!/usr/bin/env bash
# Render one retained HMO supplement page for #1428 preparation, 2026-11-15.
# Inputs: fixed verified Supplementary Information PDF and one page/attempt.
# Outputs: exclusive private PNG plus hashes/command receipt; no source writes.
set -euo pipefail
TASK_ROOT=$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)
cd "$TASK_ROOT"
if [ "$#" -ne 2 ] || [[ ! "$1" =~ ^([1-9]|10)$ ]] || [[ ! "$2" =~ ^[a-z0-9-]+$ ]]; then
  echo 'Usage: render_campaign_hmo_supplement_20261115.sh PAGE ATTEMPT' >&2
  exit 2
fi
TASK_SOURCE=.temp/campaign-resume-20261115/assets-required-001/41467_2026_71764_MOESM1_ESM.pdf
TASK_EXPECTED=f8b360d36970f74cced27accdabccdcc871c96727cc6d5077ae8bebb473972dc
TASK_OUT=.temp/campaign-resume-20261115/si-page-$1-$2
test ! -e "$TASK_OUT"
TASK_BEFORE=$(shasum -a 256 "$TASK_SOURCE" | cut -d ' ' -f 1)
test "$TASK_BEFORE" = "$TASK_EXPECTED"
mkdir "$TASK_OUT"
pdftoppm -f "$1" -l "$1" -singlefile -scale-to 2000 -png "$TASK_SOURCE" "$TASK_OUT/page"
test -s "$TASK_OUT/page.png"
TASK_AFTER=$(shasum -a 256 "$TASK_SOURCE" | cut -d ' ' -f 1)
test "$TASK_AFTER" = "$TASK_BEFORE"
{
  printf 'Purpose: HMO source inspection preparation; no campaign gate or review save.\n'
  printf 'source=%s\nsource_sha256=%s\npage=%s\n' "$TASK_SOURCE" "$TASK_BEFORE" "$1"
  printf 'command=pdftoppm -f %s -l %s -singlefile -scale-to 2000 -png SOURCE OUTPUT/page\n' "$1" "$1"
  shasum -a 256 "$TASK_OUT/page.png" scripts/adhoc/render_campaign_hmo_supplement_20261115.sh
} > "$TASK_OUT/receipt.txt"
cat "$TASK_OUT/receipt.txt"
