# Purpose: render the exporter-returned artifact plan as SHA256 check lines.
# Input: scoped GTDB export JSON; output: stdout for shasum --check (#2848, 2026-11-15).
.artifacts[] | "\(.sha256)  \(.path)"
