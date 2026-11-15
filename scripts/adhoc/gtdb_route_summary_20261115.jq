# Purpose: summarize complete per-occurrence native outcomes without truncation.
# Input: retained route report; output: diagnostic JSON, #2848, 2026-11-15.
{
  execution_revision, python_version, selected_record_count, inputs_unchanged,
  records: [.records[] | {
    record, record_id, before_sha256,
    occurrences: [.occurrences[] | {
      taxonomy_index, term, strain_name,
      stored_status: .existing_descriptor.gtdb_grounding_status,
      stored_gtdb: .existing_descriptor.gtdb_classification,
      native_result, classify_status, manual_curated_reason, manual_withheld_reason
    }]
  }]
}
