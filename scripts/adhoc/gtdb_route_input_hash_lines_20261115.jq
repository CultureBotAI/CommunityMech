# Purpose: render a native route report's captured inputs for SHA256 verification.
# Input: retained route JSON; output: stdout check lines, #2848, 2026-11-15.
.inputs | to_entries[] | "\(.value)  \(.key)"
