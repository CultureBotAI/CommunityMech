# Purpose: select exactly one authored whole-record unit for a real binder canary.
# Inputs: source config on stdin; record_id and parent_path/parent_sha arguments.
# Output: same config with one explicit record, binding the complete parent config.
# No route computation or scientific judgment; #2848, 2026-11-15.
.records |= map(select(.record_id == $record_id))
| if (.records | length) != 1 then error("one exact canary record required") else . end
| .records[0].additional_inputs += {($parent_path): $parent_sha}
