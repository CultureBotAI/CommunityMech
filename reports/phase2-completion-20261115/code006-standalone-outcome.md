# M5 code006: eight standalone native gates

All eight standalone native recipes below passed on unchanged revision
`c9e151eb9f22afb5c531dd5a8b3346ce1d58b12a`, using the frozen M5 Python 3.13.2
environment. They ran serially from `2026-11-15T04:36:40Z` through
`05:04:20Z`, after the [aggregate failed in pytest](code006-outcome.md).
Each used the retained native launcher with dependencies enabled, exited **0**,
reported no `SKIPPED, NOT PASSED` markers, and left the tracked checkout clean.

| Native recipe and receipt | Observed native result |
|---|---|
| [validate-all](technical-evidence/phase2-code006-standalone-validate-all.receipt.json) | 549 community/isolate paths validated |
| [validate-taxa](technical-evidence/phase2-code006-standalone-validate-taxa.receipt.json) | Both CommonTaxon records: no issues |
| [validate-strict](technical-evidence/phase2-code006-standalone-validate-strict.receipt.json) | 549 files scanned; 0 errors |
| [validate-gtdb-all](technical-evidence/phase2-code006-standalone-validate-gtdb-all.receipt.json) | 551 files; 0 incoherent blocks, malformed lineages or lineage conflicts |
| [validate-scalars](technical-evidence/phase2-code006-standalone-validate-scalars.receipt.json) | 551 files; 0 truncated scalars |
| [validate-scalars-idiomatic](technical-evidence/phase2-code006-standalone-validate-scalars-idiomatic.receipt.json) | 1,140 files in the native scan; 0 truncated scalars |
| [validate-terms-all](technical-evidence/phase2-code006-standalone-validate-terms-all.receipt.json) | 549 logged community/isolate term validations; all passed |
| [validate-terms-taxa](technical-evidence/phase2-code006-standalone-validate-terms-taxa.receipt.json) | Both CommonTaxon term validations passed |

Before each newly exercised large path, a single-record run through the same
launcher was persisted and verified: [schema](technical-evidence/phase2-code006-schema-canary.receipt.json),
[GTDB coherence](technical-evidence/phase2-code006-gtdb-record-canary.receipt.json),
[scalar](technical-evidence/phase2-code006-scalars-canary.receipt.json),
[idiomatic scalar](technical-evidence/phase2-code006-scalars-idiomatic-canary.receipt.json),
and [ontology terms](technical-evidence/phase2-code006-terms-canary.receipt.json).
The earlier [strict canary](technical-evidence/phase2-code006-canary.receipt.json)
already exercised the same frozen source and environment. These technical
controls do not establish scientific correctness or comprehensive ontology coverage
beyond the native recipe's configured, in-use prefixes.

The GTDB coherence recipe checks internal blocks and lineages. Its pass does
not resolve the separate classifier and stored-grounding reproducibility failures
[#2848](https://github.com/CultureBotAI/CommunityMech/issues/2848) and
[#2849](https://github.com/CultureBotAI/CommunityMech/issues/2849). The original
aggregate remains **FAILED**; its later stages remain **NOT RUN** within that
aggregate. These standalone receipts do not retroactively change it.
Reference comparisons are a separate measured run, not credited by this report.

Raw receipt/log/exit triplets are retained on M5 and hash-verified in the local
mirror. The linked public receipts bind all three raw hashes and their sanitized
log derivatives. The exact raw log hashes are:

| Recipe | Raw log bytes | Raw log SHA-256 |
|---|---:|---|
| validate-all | 53,181 | `2420624bc6abd27f7e930fbcfe2ce451b0cdc7ab881f4b785cfa690eb8ac9e83` |
| validate-taxa | 176 | `e28cf5979bddc55d60310f8427d75a785749836dd1d680c1646542adbf70b1c4` |
| validate-strict | 943 | `1bdde61874f0f32e7aa0f03a0f6cab7eff36a481b16945b2610872c4c167acae` |
| validate-gtdb-all | 249 | `780124e364b199cde94b293bc90513652232ab7ad68bb09cc36c2cc7a3aac00c` |
| validate-scalars | 146 | `cb13b4b6ff7bf7809c08a4cff741624aa3aefd32a820a0f03a4aadf0bab8704c` |
| validate-scalars-idiomatic | 168 | `f3dfafb0a019356ac15d2486fe0da0cc98c18aecc3634ccec57838e3bf32bd60` |
| validate-terms-all | 61,462 | `3d2fff570308fc16786b8aaa97e2414f6d40e81de6040c2bf5e45d0201c65ad7` |
| validate-terms-taxa | 252 | `2353c631f3f8ed4cfdd5de3d3e946467fa826e8fbe4395273c033c36807abc09` |
