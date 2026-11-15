# Phase 2 completion checkpoint

Phase 2 is in progress in [PR #2804](https://github.com/CultureBotAI/CommunityMech/pull/2804).
The requested order is to finish Phase 2, then resume the all-record scientific
review campaign. This checkpoint does not declare either task complete or
authorize a merge. The original stalled M5 checkout and session remain preserved.

The explicitly approved recovery [PR #2775](https://github.com/CultureBotAI/CommunityMech/pull/2775)
merged through the required queue at `2026-11-15T03:22:07Z` as
`6097f1ad3d47424b3cc092fc24cdb869aee5b539`. Its published branch and the local
branch in the shared recovery repository were removed; the recovery checkout
and evidence remain at detached commit `68699871415fda3c9eebf20382a315f9f3c7b17a`.
The separate dirty M5 recovery clone and original November 6 checkout were not
changed. Drafts #2797 and #2798 now target main and retain only their intended
inventory and reference-coverage changes. No Phase 2 merge has been approved.

The newer [integrated checkpoint](integrated-checkpoint-012d755b.md) records the
five current full scientific assessments, preserved Yolo assessment and correction,
verified product export, actual correction-history chain and pending private
checkpoint transfer. The execution table below preserves earlier attempts.

## Scope and acceptance

The recovered Phase 2 scope covers the host/soil/related-community work in
PR #2102, findings #2700–#2707, optional named treatment arms and abundance
observations (#2796), EnvironmentalFactor ontology grounding (#2429), contextual
KGX export (#2430), and all three LBNL records in #1548. The four original
scientific targets are EcoFAB 000025, switchgrass 000087, Yolo 000515 and dopamine
SynCom 000516; #1548 also names Brachypodium drought 000088 and human gut 000122.

Completion requires the full native `just qc` stages on a recorded combined
revision, separate reference-validation results with actual comparison counts,
evidence-backed scoped scientific assessments, and explicit disposition of every
unresolved finding. A valid review file, matching quotation or green validator
does not independently establish scientific correctness.

## Implementation checkpoint

Published revision `2052c0a13b2636459a8a5129348595e116b4ae30` combines the
reference-coverage instrumentation and the initial reviewed schema and product
changes. It precedes the subsequent scientific corrections and the strict
reference-type repair found during review.

| Work | Checkpoint | Remaining acceptance |
|---|---|---|
| Stock, host, quantity and related-record validation (#2700–#2704) | Implemented; independently reviewed | Combined M5 QC and corrected record relations |
| Treatment arms and abundance observations (#2796) | Optional model/rendering implemented; malformed-reference finding #2807 repaired and independently checked | Combined acceptance |
| EnvironmentalFactor ontology terms (#2429) | Dynamic union and narrow root-exclusion guards implemented | Combined acceptance; upstream root behavior remains #2802 |
| Host/soil/related rendering and KGX (#2705–#2707, #2430) | Implemented and independently reviewed; real CLI product canary persisted | Combined revision products/docs |
| Scientific curation (#1548 and retained findings) | 000087 source-backed correction and immutable assessment verified and integrated at `6db62bda`; independent records and linked metadata in progress | Remaining scoped assessments and integrated gates |
| Discussion reference traversal (#476) | Canonical Claw repair reviewed and published; native governed adoption applied; unchanged SL8 control compared all four previously skipped assertions | Full final-corpus measurement; Claw CI transport blocker and merge decision |

The [governed adoption checkpoint](governed-reference-adoption.md) records exact
canonical bytes and the real downstream comparison control. The schema change
does not turn a lexical match into scientific approval or waive source-specific
reference mismatches.

Whole-record generated dump/reload remains limited by #1703. Native model
materialization and new treatment-arm/observation roundtrips are distinct checks;
this limitation has not been waived or turned into a passing assertion.

## M5 execution evidence

The fresh dedicated checkout installed the frozen Python 3.13 development
environment offline. The installation completed with exit 0; its retained
5,457-byte log has SHA-256
`434f0ff24ffa9d85a36eb084d06f727adf100cc9ee4c5c96876e3f1d0d6e0dd4`.

| Run | Actual scope | Result | Evidence |
|---|---|---|---|
| `phase2-code001-plan` | Native QC dry run at `2052c0a1` | Plan completed; no checks executed | [Receipt](technical-evidence/phase2-code001-plan.receipt.json) |
| `phase2-code001-canary` | One real strict validation through the M5 driver at `2052c0a1` | Exit 0; persisted log/exit/hash verified; checkout remained clean | [Receipt](technical-evidence/phase2-code001-canary.receipt.json) · [log](technical-evidence/phase2-code001-canary.log.txt) |
| `phase2-code002-plan` | Native QC dry run at `3b063f07` | Plan completed; no checks executed | [Receipt](technical-evidence/phase2-code002-plan.receipt.json) |
| `phase2-code002-canary` | One real strict validation through the same M5 driver at `3b063f07` | Exit 0; persisted proof verified | [Receipt](technical-evidence/phase2-code002-canary.receipt.json) |
| `phase2-code002-qc` | Full native `just qc` at `3b063f07` | Exit 1: lint passed; tests had 6 failures, 5,628 passes, 103 skips and 8 deselections; every subsequent QC recipe NOT RUN | [Receipt](technical-evidence/phase2-code002-qc.receipt.json) · [log](technical-evidence/phase2-code002-qc.log.txt) |
| `phase2-code003-history` | Exact native CI historical-base acquisition at `5ea6e658` | Exit 0; five commit/tree identities verified, four newly acquired; HEAD preserved | [Receipt](technical-evidence/phase2-code003-history.receipt.json) |
| `phase2-code003-regressions` | Six native modules covering every prior full-run failure at `5ea6e658` | Exit 0; 53 tests passed | [Receipt](technical-evidence/phase2-code003-regressions.receipt.json) · [log](technical-evidence/phase2-code003-regressions.log.txt) |

This canary proves the driver, environment, native strict path and persistence
for that revision. It does not prove later revisions, full QC, scientific review
or reference coverage. Later native QC stages remain unrun until recorded.

The completed failed run preserved a clean checkout. Four failures arose because
the fresh Git object store lacked pre-squash historical review bases; their
immutable ledger checks correctly refused to substitute current cache bytes
(#2813). One failure requires classification of four new enums in the existing
vocabulary registry (#2812). One fixture was outside the established test-data
directory (#2811); its unchanged bytes have since been moved and the native ID
guard passes. These diagnostics do not retrospectively change the failed run.
The raw full-run log is 773,200 bytes, SHA-256
`7b026b7a3e32da0f9e68431c516a0769a5d00f35111bb0e7fcdd7804cd7b59b3`.

The subsequent focused rerun passes all affected modules. It is not another
aggregate QC run. Integration of the scientifically corrected records separately
exposed historical-snapshot checks that must retain their old audited bytes while
binding the new current assessments and actual curation receipt chains (#2816).
Those checks remain required; no old review or expected scientific claim is
rewritten to appear current.

Raw receipts/logs are retained in repository `.temp` on M5 and mirrored locally.
[The exporter](../../scripts/adhoc/export_phase2_qc_evidence_20261115.py) verifies
receipt identity, completion, revision, log bytes/hash and exit agreement before
writing immutable sanitized public derivatives. Failed attempts remain evidence;
separate diagnostics never replace failed aggregate stages.

## Separate measured reference baseline

At `9ba3eefc1be7a9f8bb9f0b9399f69429c16e44fc`, the M5 run completed 549 records
and enumerated 10,695 snippet surfaces: 10,172 actual comparisons, comprising
10,070 matches and 102 mismatches; one assertion had no content and 522
SupportingReference assertions were unannotated. Native validation exited 1.
These are source-comparison outcomes, not scientific verdicts. The detailed
[measurement report](../reference-assertion-coverage-20261115/README.md) retains
the failed parser attempt, corrected canaries, per-record counters and limits.
The final Phase 2 canonical revision requires its own measurement.

## Campaign restart

The separate [inventory PR #2797](https://github.com/CultureBotAI/CommunityMech/pull/2797)
preserves the original path-ordered campaign and its stronger scientific-coverage
subsets. Refresh that inventory after Phase 2; verify one saved full-record
scientific review before distributing independent records. Each record gets a
native immutable YAML/Markdown bundle, and batches of ten get fresh branches,
reviewed PRs and durable checkpoints. Previous bundles are not rewritten and
their declarations are not treated as current scientific approval.
