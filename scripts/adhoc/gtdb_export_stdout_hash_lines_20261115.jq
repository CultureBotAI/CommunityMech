# Purpose: verify exported artifacts when native review validation adds its known warning.
# Input: complete raw exporter stdout; output: SHA256 check lines; #2848, 2026-11-15.
# Strip only this exact optional prefix. Any other non-JSON output still fails.
sub("^topClass is deprecated - use top_class\n"; "")
| fromjson
| .artifacts[]
| "\(.sha256)  \(.path)"
