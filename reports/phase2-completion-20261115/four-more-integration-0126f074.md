# Four further taxonomy corrections integrated

Apple377, KZ344, Barley428 and Quinoa459 are integrated through
`0126f074d97eb795e68bbe27bc15f21468c31634`. They follow the
[six-record checkpoint](six-record-integration-420a8ca9.md). Each correction
preserves scientific claims and unresolved findings while adding narrowly
reviewed database correspondences or complete ambiguity sets. These are partial
diagnostics with `scientific_review: false`, not full scientific assessments.

| Record | Published leaf → integration commit | Durable evidence |
| --- | --- | --- |
| Apple377 | `60e35fbb` → `208e3782` | [Outcome](../gtdb-species-fifth-batch-20261115/377-canary-outcome-001.md); 82 inputs and complete 84-file checkpoint verified on both hosts |
| KZ344 | `d54cbc1d` → `30cbf84d` | [Outcome](../gtdb-source-intake-four-20261115/344-canary-outcome-001.md); 80 inputs and complete 82-file checkpoint verified on both hosts |
| Barley428 and Quinoa459 | `e620c77a` → `0126f074` | [Two-record outcome](../gtdb-species-fifth-batch-20261115/remaining-two-outcome-001.md); 126 inputs and complete 128-file checkpoint verified on both hosts |

The corresponding immutable reviews are
[Apple](../../reviews/structured/20261115T122258Z-apple-anp-species-reference-diagnostic/review.yaml),
[KZ](../../reviews/structured/20261115T123209Z-kz344-complete-genus-reference-ambiguity-diagnostic/review.yaml)
and [Barley/Quinoa](../../reviews/structured/20261115T124033Z-barley-quinoa-species-reference-diagnostic/review.yaml).
Each has its native derived Markdown in the same directory. Saved-pair and
complete-input verification preceded historical caller changes. The immutable
snapshots retain the old callers while the integration uses exact proof-bound
admissions and current biological predicates.

All four actual M5 applications passed their eight scoped commands, including
native history scaffolding. The seven other commands validate the individual
record or its history. The outcome reports retain exact frozen M5 revisions,
source coverage, original and applied hashes, raw receipts, sidecars, native
logs and checkpoint manifests. They distinguish local Python3.13.12 from actual
M5 Python3.13.2 execution. Source quotations and prior findings remain unchanged.

The following checks ran on clean combined revisions, separately from the leaf
working-tree runs. Overlapping controls are not summed into a unique-test count.

| Combined revision | Check | Actual result | Raw log SHA-256 |
| --- | --- | --- | --- |
| `208e3782` | Apple proof and participant controls | 27 passed; 12 warnings; 45.40s | `2c049e113613ea3d835040c6a26ff22a3ebfae1fa444e3eec821988c560a8227` |
| `208e3782` | Native lint | Black762, Ruff and mypy52 passed | `4da37b1b9e71d51875a9fbd01809579beeb8988d16c9641db4543ddcc35d7b43` |
| `30cbf84d` | KZ actual proof controls and batch60 | 25 passed; 12 warnings; 9.43s | `bae2ce60d5574509f9e41393740e4e0ef630efa725f5c0fb9d2b7110ca495331` |
| `0126f074` | Barley/Quinoa actual proof controls and direct Barley admission | 35 passed; 18 deselected; 12 warnings; 21.48s | `966e4375bed48def9a38af6e9c5829ddddb966396f29d207f5bfde8844e54c74` |
| `0126f074` | Unchanged batch7 and composed batch92 | 18 passed; 12 warnings; 4.45s | `5f359951405d9117465cb3b235f0bf12bf02e90d6d361ccb3fc48fe8be0b6bc9` |
| `0126f074` | Native lint | Black764, Ruff and mypy52 passed | `513487dae861d36e8d2af0170724a245e07b97ceff9258a3fb72709feb335d57` |

Actual commands, start/end revisions and exits remain in
`.temp/phase2-schema-20261115/integration-apple377-*`,
`integration-kz344-proof-001`, `integration-barley-quinoa-*` and
`integration-four-more-lint-001`. The species registry auto-merged additively:
only the two new fixed proof entries were added, preserving all earlier pins.
KZ uses a separate explicit registry; batch60 retains current KMC/Komagataella
biology and literal ledger assertions. Batch92 preserves its existing424
remediation/genus chain and361 admission while projecting only the accepted
predecessors for old digest/history expectations.

A fresh captured-input inventory at0126f074 found **93 changed and33 unchanged**
records among the historical126 assignments. Its JSON is
`.temp/phase2-schema-20261115/assignment-progress-0126f074-001.json`, SHA-256
`e1d1fe499ed99e79aa78f34e45f76e10d156ddbfc0c9b4aac5e3aec7c03791fa`.
The maintained inventory helper pins the assignment ledger and rechecks captured
bytes plus HEAD before persistence. This is a byte comparison, not a scientific
completion count; other worktrees and pending candidates are excluded.

Two independent private-input transfers remain pending permission: the earlier
40-input four-record set and the new eight-input genus set (6,328,356 bytes).
Automatic approval review rejected the latter before copying its first file to
the new M5 destination. No alternate transfer was attempted. Its public source
preparation is in draft2905; local work that does not need that transfer continues.
PPCP420 is separately held under2904 until an explicit fungal-domain proof path
is reviewed; Wetland471 retains identity/mechanism findings2898/2899. These holds
are not part of the four completed bounded corrections above.

Current generated products, final combined M5 `just qc`, separate measured
reference validation and explicit disposition of scoped scientific findings
remain required. Later aggregate gates are not reported as passed from focused
checks. Phase2 is incomplete, and the all-record scientific campaign has not yet
resumed. No additional merge is authorized or proposed by this checkpoint.
