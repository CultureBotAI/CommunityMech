# Measured reference assertion coverage

The native reference CLI's `Total checks` label counts retained issues. A zero
there does not say how many snippets were examined. The historical real-CLI
controls in `reports/reference_cli_coverage/probe.py` and
`tests/test_reference_cli_coverage.py` demonstrate positive, mutated and restored
records. They remain unchanged.

`just reference-assertion-coverage` measures actual native traversal and matcher
calls, using the pinned `linkml-reference-validator==0.2.1`. It invokes the real
Typer `validate data` command and calls the original traversal, validation and
substring functions. It inventories every `snippet` and `supporting_text` field
independently, then reconciles those occurrences against the instrumented calls.
Each occurrence binds the raw reference (string or native-supported ID mapping)
to the plugin and actual validator arguments using native identifier normalization.
A wrong-reference comparison invalidates the measurement even when the other
source contains identical text (#2795). Parsed cache reference IDs are retained
as metadata; they are not independent proof that a source is correct.
This is a lexical coverage diagnostic, not a scientific review or a count of all
possible scientific claims in prose.

The default denominator is the exact current Git tree's top-level
`kb/communities/*.yaml` and `data/isolates/*.yaml`, matching the native reference
recipe. Modified, missing or extra record files are refused. `kb/taxa` is outside
that recipe. `--record PATH` selects a record without hiding the full declared
inventory in the receipt.

## Run and retain evidence

Install the frozen development environment first (`uv sync --frozen --extra dev`).
The command uses `uv run --no-sync`; it will not alter dependencies during a run.
Inspect the selection before validating:

```bash
just --no-dotenv reference-assertion-coverage --plan
```

Run the complete Asgard positive/mutated/restored canary through the same
launcher, shell, environment, output location and background mode intended for
the corpus. For example, from the checkout root:

```bash
mkdir -p .temp/reference-coverage-launches
nohup env JUST_NO_DOTENV=true UV_NO_SYNC=1 PYTHONDONTWRITEBYTECODE=1 \
  just --no-dotenv reference-assertion-coverage \
  --record kb/communities/Asgard_Wetland_Soil_Methanogenesis_Substrate_Community.yaml \
  --canary --output .temp/reference-coverage-canary-001 \
  > .temp/reference-coverage-launches/canary-001.log 2>&1 < /dev/null &
```

Verify the nonempty `receipt.json`, all three case logs/receipts, the scratch
inputs, `inputs_unchanged: true`, and `canary_passed: true`. The original `[NiFe]`
snippet must match, its scratch-only `[FeFe]` mutation must produce exactly one
native issue, and restoration must pass immediately. This verifies the complete
record's native CLI path; it does not establish corpus coverage or long-tail
cache behavior. Only after acceptance, use the same launch path for the batch:

```bash
nohup env JUST_NO_DOTENV=true UV_NO_SYNC=1 PYTHONDONTWRITEBYTECODE=1 \
  just --no-dotenv reference-assertion-coverage \
  --output .temp/reference-coverage-corpus-001 \
  > .temp/reference-coverage-launches/corpus-001.log 2>&1 < /dev/null &
```

Every output directory must be new and beneath this checkout's `.temp`.
Existing directories are refused. Retained artifacts include the exact Git
inventory, dependency versions, implementation hashes, all record/schema/config/
cache input hashes, per-occurrence outcomes and native stdout. The canary writes
JSON copies, which the native YAML reader accepts; canonical inputs are never
edited. Raw logs may contain source excerpts and local paths: review/sanitize
them before publishing.

## Interpret the counters separately

| Field | Meaning |
| --- | --- |
| `record_processing_complete` | Every selected record completed native traversal. |
| `snippet_surfaces` | Independently enumerated snippet/supporting-text fields, including unsupported/empty surfaces. |
| `excerpt_validator_invocations` | Actual native excerpt validator calls; includes prefix skips and missing caches. |
| `snippet_occurrences_compared` | Unique occurrences reaching a real substring comparison. |
| `matcher_calls` | Native `find_text_in_reference` calls; an empty normalized query may not compare text. |
| `substring_calls` | Actual native substring matcher invocations. |
| `substring_parts_compared` | Native loop iterations, including ellipsis-separated parts; early mismatch stops the loop. |
| `title_only_invocations` | Separate native title validation; never counted as snippet comparison. |
| `native_issues` | Retained native validation issues, matching the native `Total checks` label. |
| `assertion_coverage_complete` | Every inventoried snippet surface was actually compared. |
| `native_validation_passed` | The native CLI returned zero under the stated cache-only policy. |
| `validation_passed` | Measurement integrity, full snippet coverage and native validation all passed. |

Per-occurrence outcomes distinguish matched/mismatched text, skipped prefixes
(including BIOPROJECT), missing/unparseable caches, no content, empty query,
unannotated excerpts, fields outside native traversal and missing references.
An individual record with no snippet fields is explicitly typed
`no_snippet_surfaces`; it does not inflate comparison counts. A whole run with
zero actual comparisons, inconsistent dispatch/accounting or changed inputs is
invalid (exit 2). Valid measurements with uncovered surfaces or native issues
exit 1. Exit 0 requires coverage and validation, or a fully verified canary.

## Cache and coverage boundaries

The native identifier normalization, filename selection and Markdown/legacy
cache parsers are retained. No files are renamed or normalized on disk. Native
DOI filename casing therefore retains the platform's filesystem behavior.
`--no-full-text` is explicit, and a cache-only adapter replaces acquisition.
Source lookup, enrichment, saving, filesystem mutation, network connections and
child processes are refused during native dispatch. All input hashes must be
unchanged afterward. Missing content remains a visible failure; there is no
network retry or fallback to `pmc_full_*`, supplement files or other sources.

The maintained shared-schema gap in SupportingReference is tracked in #476;
unannotated fields remain uncovered in this measurement. Source-specific
supplement routing is tracked in #1996; faithful supplement excerpts may remain
article-cache mismatches. This command neither repairs those gaps nor treats
their findings as evidence that the scientific claim is false. Online
`just qc-references` retains its separate acquisition policy and scope.
