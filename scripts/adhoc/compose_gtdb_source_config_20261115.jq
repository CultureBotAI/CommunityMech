# Purpose: expand an authored source plan with exact retained native outcomes.
# Inputs: slurped authored JSON, route JSON; bound source/helper paths+hashes as args.
# Output: binder configuration on stdout; no scientific judgment or writes (#2848, 2026-11-15).
if length != 2 then error("authored plan and native route report required") else . end
| .[0] as $authored | .[1] as $routes
| if ($authored.records | length) < 1 or ($authored.records | length) > 10
  then error("one to ten authored whole records required") else $authored end
| .records |= map(
    . as $unit
    | [$routes.records[] | select(.record_id == $unit.record_id)] as $found
    | if ($found | length) != 1
         or $found[0].record != .record
         or $found[0].before_sha256 != .before_sha256
      then error("authored record identity or before hash differs") else . end
    | .additional_inputs += {
        ($authored_path): $authored_sha,
        "scripts/adhoc/compose_gtdb_source_config_20261115.jq": $helper_sha
      }
    | .occurrences |= map(
        . as $claim
        | [$found[0].occurrences[] | select(.taxonomy_index == $claim.taxonomy_index)] as $observed
        | if ($observed | length) != 1
             or $observed[0].term != .term
             or $observed[0].strain_name != .strain_name
          then error("authored occurrence identity differs") else . end
        | if any(.expected_native | to_entries[];
                   $observed[0].native_result[.key] != .value)
          then error("authored native expectation differs") else . end
        | del(.expected_native)
        | . + {
            native_result: $observed[0].native_result,
            classify_status: $observed[0].classify_status
          }
      )
  )
