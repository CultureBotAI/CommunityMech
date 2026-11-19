# Purpose: list exact captured input paths for one to ten explicitly selected whole records.
# Inputs: source proof JSON and $record_ids array. Output: unique relative paths on stdout.
# No writes/acquisition; native source/apply guards remain authoritative. Serves #2873, 2026-11-15.
# Additive successor: preserve the previously executed selector and its immutable evidence.
.records as $records
| if ($record_ids | type) != "array"
     or ($record_ids | length) < 1 or ($record_ids | length) > 10
     or any($record_ids[]; type != "string" or length == 0)
     or ($record_ids | unique | length) != ($record_ids | length)
  then error("one to ten unique nonempty record IDs required") else . end
| if ($records | type) != "array" then error("source records array required") else . end
| [$records[] | select(.record_id as $id | $record_ids | index($id))] as $selected
| if ($selected | map(.record_id) | sort) != ($record_ids | sort)
  then error("each requested unit must exist exactly once") else . end
| [$selected[].input_paths[]] | unique[]
