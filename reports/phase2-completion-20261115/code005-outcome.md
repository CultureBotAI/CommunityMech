# M5 code005: private checkpoint copies entered the ID inventory

The full native `just qc-references` run at
`63b833d3f1752efbb5010f9ae1f5e6e3e1813962` completed on M5 at
`2026-11-15T04:09:12Z` with exit **1**. It started at `03:49:49Z`.
Lint passed. Pytest reported **2 failed, 5,777 passed, 103 skipped,
8 deselected and 18 warnings**, taking 1,159.39 seconds. The two failures were
the production-ID uniqueness and known-directory checks.

The approved private checkpoint contains historical and staged copies of the
five reviewed records. The repository-wide ID scanner included those copies
under `.temp`, although native review documentation assigns that directory to
durable private review inputs. The saved checkpoint remains intact.
[#2840](https://github.com/CultureBotAI/CommunityMech/issues/2840) records the
failure and the narrow repair: exclude that exact directory component while
retaining checks for production duplicates and unexpected record directories.
The repaired module passed all 28 tests; near-matching directory names and real
production duplicates remain checked. This focused result does not change the
failed aggregate result.

| Native stage | Result |
|---|---|
| `lint` | PASSED |
| `test` | FAILED |
| `validate-all`, `validate-taxa`, `validate-strict` | NOT RUN |
| `validate-gtdb-all`, `validate-scalars`, `validate-scalars-idiomatic` | NOT RUN |
| `validate-terms-all`, `validate-terms-taxa` | NOT RUN |
| `qc`, `validate-references-all`, `qc-references` | NOT RUN |

No native `SKIPPED, NOT PASSED` recipe marker occurred; the 103 pytest skips
and eight e2e tests deselected by the default `-m 'not e2e'` selection are
separate from the later recipes that never started. Neither ontology validation
nor reference validation completed in this run. The tracked checkout remained clean.
The [skip ledger](code005-pytest-skips.json) binds all 103 logged identifiers to
their recorded source guards. It distinguishes those associations from runtime
causes that the native log did not fully report.

The raw receipt has SHA-256
`c9c95cba9924ccfd0bacd68e9744fcbcb6b3c99ed2a0be756551a526e9ed9a1a`.
The 776,661-byte raw log has SHA-256
`30584303fffb594d37ccfbe4b70740961383f945b3b74ae9c63a5f7931245e4d`.
The independently retained exit file has SHA-256
`4355a46b19d348dc2f57c046f8ef63d4538ebb936000f3c9ee954a27460dd865`.
Before and after cache archives both have SHA-256
`2284f07a11f0e6482ce2cee3d6dd5cb1f7bde4e065554203c6a83c8aa273162b`;
the per-file manifests also match.

The [public receipt](technical-evidence/phase2-code005-qc-references.receipt.json)
and [sanitized log](technical-evidence/phase2-code005-qc-references.log.txt)
retain the actual run name and failed status. The reviewed exporter checks
completion, revision, raw bytes, hashes and exit agreement before publication.
The raw run receipt, log and exit file remain private on M5 and are mirrored
locally. Full cache archives remain on M5; their metadata is mirrored locally.
These distinctions were checked in the independent report review
[#2842](https://github.com/CultureBotAI/CommunityMech/issues/2842).

The next aggregate is assigned revision
`c9e151eb9f22afb5c531dd5a8b3346ce1d58b12a`. It includes the ID-inventory repair,
the additional immutable historical-base prerequisite and the
[historical reference-blocker ledger](../phase2-reference-blockers-20261115/reference-blockers-20185647.md).
An existing verified GTDB crosswalk will be supplied through the supported
process-local `KG_MICROBE_DIR` setting, after a real source canary. A fresh
aggregate must establish its own results; no later stage is credited here.
