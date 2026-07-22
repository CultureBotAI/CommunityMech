#!/usr/bin/env bash
# Drift check for vendored byte-identical files (hub-and-spoke model).
#
# THE FIX for the self-referential-pin blind spot: instead of hashing a file
# against a hash generated FROM THE SAME REPO, this fetches the authoritative
# copy from the canonical hub at a pinned commit and diffs. A repo that edits
# its vendored copy now fails CI, because the reference lives elsewhere.
#
# The hub is the PUBLIC CultureBotAI/CultureMech (culturebotai-claw is private,
# so public Mech CI cannot fetch raw content from it). Dependency-free: bash +
# curl + diff only (no uv/OAK), so it runs as a fast blocking CI job before any
# heavy setup. The pinned canonical commit lives in scripts/.vendored_canon_ref;
# the file list is embedded (this script is itself vendored byte-identical across
# the spokes). Bump .vendored_canon_ref in the same PR that syncs a changed file
# from the hub — that bump is the deliberate propagation act.
set -euo pipefail

CANON_REPO="CultureBotAI/CultureMech"
REF_FILE="scripts/.vendored_canon_ref"

# Same-path vendored files: identical relative path in the hub and here.
FILES=(
  scripts/validate_id_label_correspondence.py
  scripts/chem_formula.py
  tests/test_id_label_empty_adapter.py
  tests/test_id_label_unknown_prefix.py
  tests/test_id_label_plausibility.py
)

# Package-namespaced shared files: same bytes, but the local path is namespaced
# by this repo's package while the hub's is culturemech. Format "local_glob|hub".
MAPPED=(
  "src/*/schema/mech_shared.yaml|src/culturemech/schema/mech_shared.yaml"
)

[ -f "$REF_FILE" ] || { echo "ERROR: $REF_FILE missing (pinned canonical commit)"; exit 2; }
REF="$(tr -d '[:space:]' < "$REF_FILE")"
[ -n "$REF" ] || { echo "ERROR: $REF_FILE is empty"; exit 2; }

tmp="$(mktemp)"
trap 'rm -f "$tmp"' EXIT
fail=0
checked=0
for f in "${FILES[@]}"; do
  [ -f "$f" ] || { echo "MISSING: $f not present locally"; fail=1; continue; }
  url="https://raw.githubusercontent.com/${CANON_REPO}/${REF}/${f}"
  if ! curl -fsSL "$url" -o "$tmp"; then
    echo "ERROR: could not fetch $f from ${CANON_REPO}@${REF:0:8} ($url)"; fail=1; continue
  fi
  # byte-exact comparison (temp file preserves the trailing newline that $() would strip)
  if ! cmp -s "$tmp" "$f"; then
    echo "DRIFT: $f differs from ${CANON_REPO}@${REF:0:8}"; fail=1
  fi
  checked=$((checked + 1))
done

# Path-mapped files: resolve the single local match via glob, diff the hub copy.
for entry in "${MAPPED[@]}"; do
  glob="${entry%%|*}"; hubf="${entry#*|}"
  local=""
  for cand in $glob; do [ -f "$cand" ] && local="$cand" && break; done
  if [ -z "$local" ]; then echo "MISSING: no local file matching $glob"; fail=1; continue; fi
  url="https://raw.githubusercontent.com/${CANON_REPO}/${REF}/${hubf}"
  if ! curl -fsSL "$url" -o "$tmp"; then
    echo "ERROR: could not fetch $hubf from ${CANON_REPO}@${REF:0:8} ($url)"; fail=1; continue
  fi
  if ! cmp -s "$tmp" "$local"; then
    echo "DRIFT: $local differs from ${CANON_REPO}@${REF:0:8}:$hubf"; fail=1
  fi
  checked=$((checked + 1))
done

if [ "$fail" -eq 0 ]; then
  echo "OK: all ${checked} vendored files match ${CANON_REPO}@${REF:0:8}"
else
  echo ""
  echo "To resolve: copy the canonical files from ${CANON_REPO}@${REF:0:8}, and if the"
  echo "hub intentionally changed them, bump ${REF_FILE} to the new hub commit."
  exit 1
fi
