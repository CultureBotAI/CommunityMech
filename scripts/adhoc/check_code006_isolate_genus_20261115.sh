#!/usr/bin/env bash
# Purpose: same-path native isolate genus canary/history/completion, #2848.
# Inputs: exact execution SHA, selected record/application hashes and gate.
# Outputs: exclusive private command/log/exit/hash receipts; native sidecar
# only for explicit new-history. 2026-11-15. No acquisition/provider calls.
set -euo pipefail
set -C
cd "$(dirname "$0")/../.."
expected="${1:?execution SHA required}"
mode="${2:?plan or run required}"
gate="${3:?gate required}"
record="${4:?000552 or000553 required}"
attempt="${5:?numeric attempt required}"
expected_record="${6:?accepted candidate SHA required}"
application="${7:?relative actual application receipt required}"
application_sha="${8:?actual application receipt SHA required}"
[[ "$expected" =~ ^[0-9a-f]{40}$ && "$expected_record" =~ ^[0-9a-f]{64}$ && "$application_sha" =~ ^[0-9a-f]{64}$ && "$attempt" =~ ^[0-9]+$ ]]
[[ "$(git rev-parse HEAD)" == "$expected" ]]
state=.temp/gtdb-code006-20261115
case "$record" in
  000552) slug=Pelagerythrobacter_N7_Halophilic_Pyrene_Oxidation_Isolate_Baseline ;;
  000553) slug=Salinicola_A11_Halophilic_Bioemulsifier_Decarboxylase_Isolate_Baseline ;;
  *) exit 2 ;;
esac
[[ "$application" == "$state/isolate-$record-applied-$attempt/receipt.json" ]]
target="data/isolates/$slug.yaml"
[[ "$(shasum -a 256 "$target" | cut -d ' ' -f 1)" == "$expected_record" ]]
[[ "$(shasum -a 256 "$application" | cut -d ' ' -f 1)" == "$application_sha" ]]
[[ "$(cat "$state/install-001.exit")" == 0 ]]
export PATH=/Users/marcin/.local/bin:/opt/homebrew/bin:/usr/bin:/bin
export UV_NO_SYNC=true UV_OFFLINE=true JUST_NO_DOTENV=true PYTHONUNBUFFERED=1
export PYSTOW_HOME=/Users/marcin/.data
export KG_MICROBE_DIR="$PWD/$state/kg-microbe"
export CLAW_SRC=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/src
command=(just --verbose --no-dotenv --color never)
case "$mode" in
  plan) command+=(--dry-run) ;;
  run) ;;
  *) exit 2 ;;
esac
case "$gate" in
  schema) command+=(validate "$target") ;;
  strict) command+=(validate-strict "$target" --out "$state/isolate-$record-strict-$attempt.tsv")
          test ! -e "$state/isolate-$record-strict-$attempt.tsv" ;;
  gtdb) command+=(validate-gtdb "$target") ;;
  domain) command+=(validate-gtdb-domain "$target") ;;
  scalars) command+=(validate-scalars "$target") ;;
  history) command+=(validate-history "history/records/$slug") ;;
  completion)
    command=(uv run pytest
      tests/test_gtdb_coherence_validator.py::test_the_status_distribution_is_what_was_measured
      tests/test_gtdb_not_attempted.py::test_no_taxon_is_silently_outstanding -q)
    [[ "$mode" != plan ]] || command+=(--collect-only) ;;
  new-history)
    command+=(new-history --kind record --slug "$slug" --target-root data/isolates
      --event EDIT --outcome changed --sections taxonomy,curation_history
      --actor-name codex --model gpt-6 --agent-tool codex
      --issue https://github.com/CultureBotAI/CommunityMech/issues/2848
      --pr https://github.com/CultureBotAI/CommunityMech/pull/2853
      --summary "Add the source-backed same-genus reference correspondence for $record"
      --details "Applied exactly reviewed native candidate SHA256 $expected_record through actual receipt $application SHA256 $application_sha. The original NCBI genus, study strain/genome identity, primary evidence, biological mechanisms and historical assessments remain unchanged. Only the corresponding GTDB genus block, GROUNDED status and two native inline events were added using crosswalk SHA256761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd. This is a scoped database correspondence; no exact study-stock species/genome mapping, scientific re-review, bulk completion or corpus-QC pass is asserted. Historical batch147 biology requires a separately verified actual successor chain.") ;;
  *) exit 2 ;;
esac
prefix="$state/isolate-$record-$mode-$gate-$attempt"
printf '%q ' "${command[@]}" > "$prefix.command.txt"
printf '\n' >> "$prefix.command.txt"
{
  git rev-parse HEAD
  .venv/bin/python --version
  shasum -a 256 "$0" "$target" uv.lock "$application"
  git -C "${CLAW_SRC%/src}" rev-parse HEAD
  shasum -a 256 "$CLAW_SRC/kg_microbe_history/__main__.py" "$CLAW_SRC/kg_microbe_history/scaffold.py"
  date -u '+%Y-%m-%dT%H:%M:%SZ'
} > "$prefix.start.txt"
set +e
"${command[@]}" > "$prefix.log" 2>&1
result=$?
set -e
printf '%s\n' "$result" > "$prefix.exit"
test -s "$prefix.log"
[[ "$(shasum -a 256 "$target" | cut -d ' ' -f 1)" == "$expected_record" ]]
[[ "$(shasum -a 256 "$application" | cut -d ' ' -f 1)" == "$application_sha" ]]
shasum -a 256 "$prefix.log" > "$prefix.log.sha256"
date -u '+%Y-%m-%dT%H:%M:%SZ' > "$prefix.finished.txt"
exit "$result"
