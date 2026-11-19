#!/usr/bin/env bash
# Purpose: retain the unchanged native corpus grounding check for issue2849, 2026-11-15.
# Inputs: published f39c0fe4, frozen environment, exact761 crosswalk and all record roots.
# Output: exclusive private plan/run logs, exits and native before/after checksum evidence.
# No source, cache, environment or canonical mutations; no waiver or skip override.
set -euo pipefail
mode="${1:?use plan or run}"
case "$mode" in plan|run) ;; *) exit 2 ;; esac
repo_root="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$repo_root"
expected_revision=f39c0fe400740a754f2d006d17ffa8c8e82fae63
test "$(git rev-parse HEAD)" = "$expected_revision"
state=.temp/gtdb-source-routes-2849-20261115
mapping="$state/kg-microbe/data/raw/NCBI2GTDB.tsv.gz"
test "$(shasum -a 256 "$mapping" | cut -d ' ' -f 1)" = 761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd
test "$(shasum -a 256 tests/test_gtdb_uncurated_blocks_match_the_tool.py | cut -d ' ' -f 1)" = 102ee759b9cd43c34d65d1b169affe6f0823400d40fa4571cdf59fa462306df0
output="$state/corpus-$mode-001"
test ! -e "$output" && test ! -L "$output"
mkdir "$output"
git rev-parse HEAD > "$output/revision.txt"
.venv/bin/python --version > "$output/python.txt"
find kb/communities data/isolates kb/taxa -name '*.yaml' -print0 > "$output/records.nul"
test -s "$output/records.nul"
xargs -0 shasum -a 256 < "$output/records.nul" > "$output/inputs.sha256"
shasum -a 256 "$mapping" scripts/gtdb_ground.py \
  tests/test_gtdb_uncurated_blocks_match_the_tool.py src/communitymech/paths.py \
  src/communitymech/taxon_blocks.py uv.lock \
  scripts/adhoc/check_gtdb_source_routes_corpus_20261115.sh >> "$output/inputs.sha256"
export KG_MICROBE_DIR="$repo_root/$state/kg-microbe"
export UV_NO_SYNC=true UV_OFFLINE=true PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
command=(.venv/bin/python -m pytest -q tests/test_gtdb_uncurated_blocks_match_the_tool.py -rs)
if [[ "$mode" = plan ]]; then command+=(--collect-only); fi
printf '%q ' "${command[@]}" > "$output/command.txt"
printf '\n' >> "$output/command.txt"
date -u '+%Y-%m-%dT%H:%M:%SZ' > "$output/started-at.txt"
set +e
"${command[@]}" > "$output/native.log" 2>&1
native_exit=$?
set -e
printf '%s\n' "$native_exit" > "$output/native.exit"
date -u '+%Y-%m-%dT%H:%M:%SZ' > "$output/finished-at.txt"
test -s "$output/native.log"
shasum -a 256 -c "$output/inputs.sha256" > "$output/inputs-verified.log"
test "$(git rev-parse HEAD)" = "$expected_revision"
find kb/communities data/isolates kb/taxa -name '*.yaml' -print0 > "$output/records-after.nul"
cmp "$output/records.nul" "$output/records-after.nul"
test "$native_exit" = 0
if [[ "$mode" = run ]]; then
  grep -Eq '(^| )3 passed([, ]|$)' "$output/native.log"
  if grep -Eiq '[0-9]+ skipped|SKIPPED' "$output/native.log"; then exit 2; fi
fi
shasum -a 256 "$output/native.log" "$output/native.exit" "$output/inputs.sha256"
