# M5 code006: real-source GTDB reproducibility failures

The full native `just qc-references` run on
`c9e151eb9f22afb5c531dd5a8b3346ce1d58b12a` ran from
`2026-11-15T04:15:59Z` to `04:34:03Z`, with dependencies enabled, and exited
**1**. Lint passed. Pytest reported **2 failed, 5,861 passed, 30 skipped,
8 deselected and 18 warnings**, taking 1,080.02 seconds. The tracked checkout
remained clean. Both production-ID checks repaired under #2840 passed.

The [verified source prerequisite](code006-crosswalk-prerequisite.md) supplied
the existing GTDB crosswalk through the native resolver. The checks now expose
two reproducibility failures that a missing source previously concealed:

- [#2848](https://github.com/CultureBotAI/CommunityMech/issues/2848): the status
  classifier reports 492 stored status or candidate-list discrepancy entries.
  These are not 492 distinct organisms or scientific verdicts.
- [#2849](https://github.com/CultureBotAI/CommunityMech/issues/2849): three
  uncurated mappings do not reproduce through the tested native routes:
  Microbacterium BR1, Terrabacter 2APm3 and the Industrial Bioreactor
  Sulfobacillus entry. Their actual source routes and curation provenance must
  be assessed before any correction.

The same two tests reproduce locally on the exact revision and crosswalk.
That diagnostic used Python 3.13.12; the M5 aggregate used Python 3.13.2.
Neither a blanket status rewrite nor a blanket `curated` flag is a resolution.
The supplied source remains enabled and the failures remain recorded.

| Native stage | Aggregate result |
|---|---|
| `lint` | PASSED |
| `test` | FAILED |
| `validate-all`, `validate-taxa`, `validate-strict` | NOT RUN |
| `validate-gtdb-all`, `validate-scalars`, `validate-scalars-idiomatic` | NOT RUN |
| `validate-terms-all`, `validate-terms-taxa` | NOT RUN |
| `qc`, `validate-references-all`, `qc-references` | NOT RUN |

There were no native `SKIPPED, NOT PASSED` recipe markers. The 30 pytest skips
and eight e2e tests deselected by `-m 'not e2e'` remain distinct from these
eleven later recipe entries that never started. Subsequent standalone native
checks retain their own receipts and cannot turn this aggregate into a pass.
The separate measured-reference run likewise does not replace technical QC.

The [public receipt](technical-evidence/phase2-code006-qc-references.receipt.json)
and [sanitized log](technical-evidence/phase2-code006-qc-references.log.txt)
preserve the failed status. Raw artifacts are retained on M5 and mirrored
locally:

| Raw artifact | Bytes / SHA-256 |
|---|---|
| Receipt | `b96a0a80820842c061a5f16835742c00f74aaa3225001ea8d61f896f1c61e769` |
| Log | 770,023 bytes; `9ea6742aa081136d3133d153d49103cb5ae696d35670edc3ed59e816afdae450` |
| Exit | `4355a46b19d348dc2f57c046f8ef63d4538ebb936000f3c9ee954a27460dd865` |

Before and after cache archives were byte-identical: 47,403,520 bytes,
SHA-256 `2284f07a11f0e6482ce2cee3d6dd5cb1f7bde4e065554203c6a83c8aa273162b`.
Per-file hashes also matched. Archive bodies remain on M5; their metadata is
mirrored locally. Scientific assessments and the approved private checkpoint
are preserved separately from this technical result.
