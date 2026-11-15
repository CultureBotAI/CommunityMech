#!/usr/bin/env bash
# Purpose: retained native one-record genus-canary gates/history for #2848.
# Inputs: reviewed applied000434 and exact executionHEAD; outputs: exclusive
# private command/log/exit metadata, plus native history sidecar when requested.
# 2026-11-15. No references acquisition, provider calls or other record writes.
set -euo pipefail
set -C
cd "$(dirname "$0")/../.."
expected="${1:?exact execution revision required}"
mode="${2:?plan or run required}"
gate="${3:?gate required}"
attempt="${4:?numeric attempt required}"
[[ "$expected" =~ ^[0-9a-f]{40}$ && "$attempt" =~ ^[0-9]+$ ]]
[[ "$(git rev-parse HEAD)" == "$expected" ]]
state=.temp/gtdb-code006-20261115
target=kb/communities/Acidic_Nitrification_Minimal_Consortium.yaml
expected_record=c2cf66bb2d62e59ac75c16db1aa9598a33719c6461822ae237d44558c6c91ea9
[[ "$(shasum -a 256 "$target" | cut -d ' ' -f 1)" == "$expected_record" ]]
[[ "$(shasum -a 256 "$state/genus-applied-001/receipt.json" | cut -d ' ' -f 1)" == 14a946e2082e7203b18b39d3c5862403c56eb47ee2844fb917b35b1b4d00123c ]]
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
  strict) command+=(validate-strict "$target" --out "$state/genus-strict-$attempt.tsv")
          test ! -e "$state/genus-strict-$attempt.tsv" ;;
  gtdb) command+=(validate-gtdb "$target") ;;
  domain) command+=(validate-gtdb-domain "$target") ;;
  scalars) command+=(validate-scalars "$target") ;;
  history) command+=(validate-history history/records/Acidic_Nitrification_Minimal_Consortium) ;;
  new-history)
    command+=(new-history --kind record --slug Acidic_Nitrification_Minimal_Consortium
      --target-root kb/communities --event EDIT --outcome changed --sections taxonomy,curation_history
      --actor-name codex --model gpt-6 --agent-tool codex
      --issue https://github.com/CultureBotAI/CommunityMech/issues/2848
      --pr https://github.com/CultureBotAI/CommunityMech/pull/2853
      --summary "Add the source-backed Mycobacterium genus correspondence"
      --details "Applied exactly reviewed genus candidate001 c2cf66bb: native GTDB:g__Mycobacterium for unchanged NCBITaxon1763,18589/18589 named genomes, no reclassification, exact crosswalk SHA256761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd. One database correspondence and GROUNDED status with two native inline events; no source species/genome identity, biological claim, quotation or prior scientific review changed. Actual application receipt .temp/gtdb-code006-20261115/genus-applied-001/receipt.json SHA25614a946e2082e7203b18b39d3c5862403c56eb47ee2844fb917b35b1b4d00123c connects the prior diagnostic status application to this mapping. The November5 scientific uncertainty and saved status-only needs_curation diagnostic remain immutable historical evidence. Scoped gates and two native completion tests follow; no full scientific re-review or corpus repair is asserted.") ;;
  *) exit 2 ;;
esac
prefix="$state/genus-canary-$mode-$gate-$attempt"
printf '%q ' "${command[@]}" > "$prefix.command.txt"
printf '\n' >> "$prefix.command.txt"
{
  git rev-parse HEAD
  .venv/bin/python --version
  shasum -a 256 "$0" "$target" uv.lock
  date -u '+%Y-%m-%dT%H:%M:%SZ'
} > "$prefix.start.txt"
set +e
"${command[@]}" > "$prefix.log" 2>&1
result=$?
set -e
printf '%s\n' "$result" > "$prefix.exit"
test -s "$prefix.log"
[[ "$(shasum -a 256 "$target" | cut -d ' ' -f 1)" == "$expected_record" ]]
shasum -a 256 "$prefix.log" > "$prefix.log.sha256"
date -u '+%Y-%m-%dT%H:%M:%SZ' > "$prefix.finished.txt"
exit "$result"
