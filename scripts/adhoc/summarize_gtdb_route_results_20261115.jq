# Purpose: inspect exact native outcomes without the large crosswalk row table.
# Input: retained route report JSON; output: full per-occurrence native/status values.
# Provenance: #2848 source preparation, 2026-11-15; no inferred counts or approvals.
{execution_revision, python_version, selected_record_count, inputs_unchanged,
 ncbi_database, records: [.records[] | {record_id, record, before_sha256,
 occurrences: [.occurrences[] | {taxonomy_index, term, strain_name,
 native_result, classify_status}]}]}
