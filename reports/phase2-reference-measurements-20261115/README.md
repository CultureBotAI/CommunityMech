# Phase2 native assertion measurements

These metadata-only exports verify the retained native measurements against
their receipt, start record, case, log, exact Git inventory, selected record
bytes, and current schema/configuration/cache hashes. The exporter recomputes
counts from individual occurrences and resolves their classes through the
measured schema. It performs no matching, acquisition, cache writes, or record
changes.

| Attempt | Records | Compared surfaces | SupportingReference compared | Matches | Mismatches | Native / wrapper exit |
|---|---:|---:|---:|---:|---:|---|
| [LBNL canary](lbnl-annotation-measurement-001.json) | 1 | 37/37 | 11 | 35 | 2 | 1 / 1 |
| [Gut and Brachypodium](gut-brach-annotation-measurement-001.json) | 2 | 107/107 | 3 | 107 | 0 | 0 / 0 |

The [complete M5 corpus export](m5-final-reference-corpus-001.json) and its
[549-record table](m5-final-reference-corpus-001.md) bind native measurement
revision `20185647ad327b686b37dcf3a0036cf298028779`. All 549 declared records were
processed. Of 10,837 snippet occurrences, 10,836 were actually compared:
10,728 matched and 108 mismatched. The remaining occurrence has no source
content: Bayan Obo, `ecological_interactions[0].evidence[0].snippet`, class
`EvidenceItem`. Its excerpt validator ran once but its matcher ran zero times;
it is not counted as examined. There are 109 native issues in 17 records.
Assertion coverage and validation therefore remain false, with native and
wrapper exit 1. Per-record native-class counts, including SupportingReference,
are retained in the JSON.

This complete export verifies the original M5 measurement; it does not rerun
matching or claim the separate full-QC run passed. The first full export was
refused because a requested uppercase DOI cache name is a filesystem alias of
the lowercase inventory name. Repair #2829 requires a unique inventory spelling,
the same physical file, and matching current/retained/native hashes. The failed
attempt and raw measurement remain intact. A second export carried an explicitly
unbound Python declaration and remains private; published attempt 003 records
Python as unknown. The contemporaneous M5 runtime observation is not retroactively
bound to this measurement.

The LBNL one-record export was verified before the two-record export used the
same launcher/environment/output mechanism. Exporter exit zero means the
retained measurement was verified and published; the two LBNL mismatches remain
failures. Complete lexical coverage does not establish scientific support.
The original scientific reviews and earlier annotation-omission measurements
remain unchanged.

The first two native runs were local; the complete corpus run was on M5, as
declared by their operator. Their receipts
record dependency/source hashes but do not record the Python runtime or host;
these exports report Python as unrecorded. None includes a separately
retained process-exit file, so the native and wrapper exit values are verified
from the native log/receipt rather than represented as independent shell-exit
evidence. Raw artifacts stay in the source checkout's ignored
`.temp/phase2-integration-20261115/<attempt>/`; their exact hashes are public in
each JSON. No raw quotes, reference identifiers, or absolute paths are published.

The maintained invocation is:

```sh
python scripts/adhoc/export_phase2_reference_measurement_20261115.py \
  --source-root "$SOURCE_ROOT" \
  --run "$SOURCE_ROOT/.temp/phase2-integration-20261115/$ATTEMPT" \
  --execution-host local --format json > "$NEW_EXCLUSIVE_OUTPUT"
```

Use `--format markdown` for the table and `--exit-file` only when a real
separately captured process exit exists. For an M5 measurement, use the retained
M5 source/input snapshot and declare `--execution-host M5`; do not relabel a
local run. The exporter is a pure reader and sends output to stdout; the caller
must refuse overwriting a saved artifact.
