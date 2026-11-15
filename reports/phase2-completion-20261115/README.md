# Phase 2 completion checkpoint

Phase 2 is in progress in [PR #2804](https://github.com/CultureBotAI/CommunityMech/pull/2804).
The requested order is to finish Phase 2, then resume the all-record scientific
review campaign. This checkpoint does not declare either task complete or
authorize a merge. The original stalled M5 checkout and session remain preserved.

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
| Treatment arms and abundance observations (#2796) | Optional model, rendering and focused checks implemented | Malformed-reference finding #2807; combined acceptance |
| EnvironmentalFactor ontology terms (#2429) | Dynamic union and narrow root-exclusion guards implemented | Combined acceptance; upstream root behavior remains #2802 |
| Host/soil/related rendering and KGX (#2705–#2707, #2430) | Implemented and independently reviewed; real CLI product canary persisted | Combined revision products/docs |
| Scientific curation (#1548 and retained findings) | First record undergoing end-to-end canary checks | Verified immutable canary, dependent and independent records |
| Discussion reference traversal (#476) | Gap measured; canonical owner is Claw | Reviewed canonical repair and governed downstream update |

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

This canary proves the driver, environment, native strict path and persistence
for that revision. It does not prove later revisions, full QC, scientific review
or reference coverage. Later native QC stages remain unrun until recorded.

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
