# Purpose: list captured inputs for explicit whole-record units, without unrelated canonicals.
# Inputs: accepted source proof and JSON array $record_ids. Output: relative paths on stdout.
# No writes or source computation; source bytes remain verified by the native apply guard.
# Serves #2848, 2026-11-15.
.records as $records
| if ($record_ids | length) < 1 or ($record_ids | length) > 10
     or ($record_ids | unique | length) != ($record_ids | length)
  then error("one to ten unique record IDs required") else . end
| [$records[] | select(.record_id as $id | $record_ids | index($id))] as $selected
| if ($selected | length) != ($record_ids | length)
  then error("each requested unit must exist exactly once") else . end
| [$selected[].input_paths[]] | unique[]
