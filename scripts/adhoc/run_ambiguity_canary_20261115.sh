#!/usr/bin/env bash
# Purpose: same-shell isolated M5 canary launcher for #2848, 2026-11-15.
# Inputs: exact revision, exclusive attempt, optional explicitly reviewed hashes.
# Outputs: immutable private command/log/exit metadata; only apply mode delegates
# the one authorized canonical change to the separately guarded native applier.
set -euo pipefail

mode=${1:?plan|stage|validate|apply}
revision=${2:?full reviewed code revision}
attempt=${3:?numeric exclusive attempt}
candidate_sha=${4:-}
receipt_sha=${5:-}
source_attempt=${6:-001}
[[ $revision =~ ^[0-9a-f]{40}$ && $attempt =~ ^[0-9]+$ && $source_attempt =~ ^[0-9]+$ ]]
root=$(git rev-parse --show-toplevel)
cd "$root"
[[ $(git rev-parse HEAD) == "$revision" ]]
state=.temp/gtdb-ambiguity-20261115
output="$state/launch-$mode-$attempt"
[[ ! -e $output && ! -L $output ]]
export UV_OFFLINE=1 UV_NO_SYNC=1
stage_script=scripts/adhoc/stage_ambiguity_status_canary_20261115.py
apply_script=scripts/adhoc/apply_ambiguity_status_canary_20261115.py
case "$mode" in
  plan|stage)
    [[ -z $candidate_sha && -z $receipt_sha ]]
    command=(.venv/bin/python "$stage_script" --attempt "$attempt" --expected-revision "$revision")
    if [[ $mode == plan ]]; then command+=(--plan); fi
    ;;
  validate|apply)
    [[ $candidate_sha =~ ^[0-9a-f]{64}$ && $receipt_sha =~ ^[0-9a-f]{64}$ ]]
    candidate="$state/ambiguity-candidate-$source_attempt/Faecalibacterium_Prausnitzii_A2_165_2FL_FOS_Monoculture_Baseline.yaml"
    command=(.venv/bin/python "$apply_script" --candidate "$candidate" --candidate-sha256 "$candidate_sha" --receipt-sha256 "$receipt_sha" --expected-revision "$revision" --output "$state/ambiguity-$mode-$attempt")
    if [[ $mode == apply ]]; then command+=(--apply); fi
    ;;
  *) exit 2 ;;
esac
mkdir "$output"
git rev-parse HEAD > "$output/revision.txt"
.venv/bin/python --version > "$output/python.txt" 2>&1
shasum -a 256 "$0" "$stage_script" "$apply_script" uv.lock > "$output/implementation.sha256"
printf '%s\n' "${command[@]}" > "$output/argv.txt"
date -u +%FT%TZ > "$output/started.txt"
set +e
"${command[@]}" > "$output/command.log" 2>&1
code=$?
set -e
printf '%s\n' "$code" > "$output/command.exit"
date -u +%FT%TZ > "$output/completed.txt"
[[ $(git rev-parse HEAD) == "$revision" ]]
shasum -a 256 -c "$output/implementation.sha256" > "$output/implementation-verified.log"
[[ -s $output/command.log && -s $output/command.exit ]]
exit "$code"
