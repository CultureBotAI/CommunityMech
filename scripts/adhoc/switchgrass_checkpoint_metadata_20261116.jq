# Select exactly five missing metadata files from the verified native checkpoint plan.
# Input: full87 plan002; output: bounded transfer manifest. #1996, 2026-11-16.
# No source-body selection, copy, path discovery or network action.
[
  ".temp/phase2-schema-20261115/switchgrass-full-network-001.exit",
  ".temp/phase2-schema-20261115/switchgrass-full-network-001.json",
  ".temp/phase2-schema-20261115/switchgrass-full-network-001.log",
  ".temp/supplement-adoption-1996-20261115/switchgrass-canonical-coverage-local-001/receipt.json",
  ".temp/supplement-adoption-1996-20261115/switchgrass-canonical-coverage-local-001/started.json"
] as $names
| if .status != "ready" or (.reviews|length) != 1
  or .reviews[0].review_id != "20261116T011931Z-switchgrass-full-source-successor"
  then error("unexpected checkpoint plan") else . end
| [.reviews[0].files[] | select(.original_path as $p | $names | index($p))] as $selected
| if ([$selected[].original_path]|sort) != ($names|sort)
  or any($selected[]; .status != "matched" or .expected_sha256 != .actual_sha256)
  then error("missing, duplicate or changed metadata row") else . end
| {schema_version:1,
   scope:"Five existing native metadata files only; no article or figure content.",
   destination:"/Users/marcin/agent-work/CommunityMech/supplement-adoption-1996-20261115",
   canary:".temp/phase2-schema-20261115/switchgrass-full-network-001.json",
   files:[$selected[] | {path:.original_path,sha256:.expected_sha256,bytes:.bytes}],
   total_bytes:([$selected[].bytes]|add)}
