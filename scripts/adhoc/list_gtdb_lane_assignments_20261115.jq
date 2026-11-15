# Read an explicit frozen assignment ledger and list one named lane; stdout only.
# Input: assignments JSON plus --arg lane; no completion inference. #2848, 2026-11-15.
.records[] | select(.lane == $lane) | [.record_id, .record, .group] | @tsv
