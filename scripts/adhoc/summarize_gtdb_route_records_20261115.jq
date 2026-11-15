# Purpose: display selected descriptor routes from a retained native route report.
# Input: report JSON; output: read-only route summary for #2848, 2026-11-15.
.records[] | {record_id, record, before_sha256, occurrences: [.occurrences[] | {taxonomy_index, selector, descriptor: .existing_descriptor.term, strain_name, native_result, classify_status, manual_curated_reason, manual_withheld_reason}]}
