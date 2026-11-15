# Purpose: render declared native JSON review inputs for independent SHA256 checking.
# Input: native review JSON; output: stdout check lines, PR2896, 2026-11-15.
.source.inputs[] | "\(.sha256)  \(.path)"
