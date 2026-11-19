# Sorghum and Shrimp integration checkpoint

Reviewed Sorghum leaf `f3ecf5dba91f50c7b3c30daa4953c9cc7425f762` and
Shrimp leaf `cb10773aa462f501fd07d41b766b80215b5b3858` are integrated at
`38c48a84187f86395d6e6b6fa8d8829d8e6c1ef4`, together with their published
source-preparation commits. The initial Sorghum leaf-only cherry-pick exposed
a missing preparatory README. That attempt was aborted, and its two reviewed
preparation commits were included before the leaf, preserving the linked source
records. No record conflict or scientific-content rewrite was needed.

The [Sorghum outcome](../gtdb-final-four-20261115/348-canary-outcome-001.md)
records five reference correspondences among fifteen stocks, eight native M5
checks, an immutable partial diagnostic, 80 verified source inputs, complete
82-file checkpoints on both hosts and 27 public evidence artifacts. Its
scientific assay limits and unresolved flavonoid mechanism remain explicit.

The [Shrimp outcome](../gtdb-shrimp-thermophilic-sahara-20261115/436-canary-outcome-001.md)
records eight genus correspondences, eight native M5 checks, an immutable partial
diagnostic, 82 verified source inputs, complete 84-file checkpoints on both hosts
and 27 public evidence artifacts. The abstract-only source, unnamed experimental
stocks, four SynCom variants and enrichment-versus-SynCom distinction remain
explicit. A reference correspondence does not identify a study stock's genome.

Both saved diagnostics retain `scientific_review: false`. Their historical
admissions require the actual application, native checks, saved review and
append-only history before accepting only the bounded taxonomy differences.
The existing tests still evaluate current biological content.

These checks ran on clean combined revision `38c48a84`:

| Recorder under `.temp/phase2-schema-20261115/` | Result | Raw log SHA256 |
| --- | --- | --- |
| `integration-sorghum-shrimp-proofs-001` | 49 passed, 12 warnings, 24.08 s; both actual-proof registries and historical callers 101/103 | `b4a21a901fc048c6703d9320492dc0d03df2fffedac9b787b704ffe9351bdbcb` |
| `integration-sorghum-shrimp-lint-001` | Black 798 files, Ruff, mypy 52 source files passed | `86a3bd3c2b85cdfcb8676ac0a9a021cf75af2e9370603ca6da0853d8568c63cf` |

The new byte inventory is
`.temp/phase2-schema-20261115/assignment-progress-38c48a84-001.json`, SHA256
`1ccc66940fd45773a4184c52bc7b2376335ddfe273f6b90f525ca5f551f9621d`.
Of the 126 historical assignments, 113 record files differ and 13 remain
unchanged. This inventory does not infer review completion and excludes pending
worktrees. Remaining record IDs are 091, 363, 376, 381, 389, 395, 398, 416, 419,
441, 482, 494 and 501. Exact private inputs for the genus and ambiguity lanes,
and the three-file Thermophilic416 transfer, still await separate approval.

Supplement routing remains on its separate adoption branch. Claw PR1283's
reviewed head `8d09d230` now has all eight hosted checks passing, including
11,624 tests, 574 skips and 87.72% coverage. Its merge has been requested and
is not yet authorized. The immutable hosted test log is retained in that Claw
checkout as `.temp/supplement-schema-20261115/pr1283-ci-success-001.log`, SHA256
`a875a45397569afdd9545c45dfa0fb8fd2e9ea1d5f33bf4e42f82e23ce852f48`.

Current generated products, full combined M5 QC, reference comparison coverage
and scientific-finding dispositions remain required. The independent full
Switchgrass reassessment is in progress and preserves the substantive panel
correspondence finding; two factual errors in its earlier immutable review are
recorded separately in issue2938. The all-record scientific campaign has not
resumed. No merge to main is claimed by this checkpoint.
