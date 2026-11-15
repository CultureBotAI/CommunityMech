# Render accepted BR1 export-plan hashes for shasum -c; #2860, 2026-11-15.
# Input: frozen plan JSON. Output: checksum lines; no writes or source changes.
.artifacts[] | .sha256 + "  " + .path
