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

The [integrated checkpoint at 012d755b](integrated-checkpoint-012d755b.md) preserves
the five full scientific assessments at that revision, the Yolo assessment and
correction, verified product export and actual correction-history chain. The
[subsequent M5 code004 outcome](code004-outcome.md) records the failed full run:
lint passed, 5,751 tests passed and ten failed; later QC stages and global
reference validation were **NOT RUN**. Its six issue owners and exact evidence
are retained. Repairs require a new aggregate run; focused passes do not change
that result. The explicitly approved
[private five-record checkpoint](private-checkpoint-m5-final-five-001.md) is now
copied to M5: all 403 files and 64,961,689 bytes were verified, including the
manifest and verifier. Its earlier gut review was preserved as approved; the
newer gut successor was not silently substituted.

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

## Integrated implementation

PR #2804 combines the reviewed model, product and scientific corrections below.
Its original implementation checkpoint was `2052c0a13b2636459a8a5129348595e116b4ae30`;
that historical revision predates the subsequent scientific corrections.

| Work | Checkpoint | Remaining acceptance |
|---|---|---|
| Stock, host, quantity and related-record validation (#2700–#2704) | Implemented and independently reviewed; corrected stock/record relations integrated | Combined M5 QC |
| Treatment arms and abundance observations (#2796) | Optional model/rendering implemented; malformed-reference finding #2807 repaired | Combined M5 QC |
| EnvironmentalFactor ontology terms (#2429) | Dynamic union and narrow root-exclusion guards implemented | Combined QC; upstream root behavior remains #2802 |
| Host/soil/related rendering and KGX (#2705–#2707, #2430) | Verified native product canary followed by full export: 1,538 nodes, 2,535 edges, zero errors/warnings | Subsequent source changes require affected generated pages to stay current |
| Scientific curation (#1548 and retained findings) | Five full immutable assessments plus Yolo's preserved full review and bounded correction | Retained scientific/source limitations remain explicit blockers; validators do not resolve them |
| Discussion reference traversal (#476) | Canonical Claw annotations adopted through native governance; actual corpus comparison and three real-record mutation/restoration controls retained | Source mismatches, Claw hosted CI/governance blockers and explicit merge decision |

The [governed adoption checkpoint](governed-reference-adoption.md) records exact
canonical bytes and the real downstream comparison control. The schema change
does not turn a lexical match into scientific approval or waive source-specific
reference mismatches.

Whole-record generated dump/reload remains limited by #1703. Native model
materialization and new treatment-arm/observation roundtrips are distinct checks;
this limitation has not been waived or turned into a passing assertion.

The [three-record full review](../../reviews/structured/20261115T031503Z-phase2-three-record-final-science/review.md)
covers EcoFAB, switchgrass and dopamine; the
[Brachypodium review](../../reviews/structured/20261115T025413Z-phase2-brachypodium-drought/review.md)
covers the drought experiment. The
[gut successor](../../reviews/structured/20261115T033902Z-phase2-gut-historical-successor/review.md)
retains the full scientific assessment after dating the old aggregate-roster
discussion to its historical checkpoint. Its 141 retained inputs match and all
44 current snippets were actually compared and matched. Molecular mechanisms
and individual-stock genome grounding remain unresolved. The original five-record
manifest and prior reviews remain immutable. The
[numbered successor manifest](scientific-successor-provenance-002.yaml) binds
the five current records, three full review bundles, nine actual application
receipts and eleven new history sidecars at `bb6c71c3`. It records persistence
and the correction chain without granting independent scientific approval.

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
| `phase2-code004-qc` | Full native `just qc-references` at `012d755b` | Exit 1: lint passed; 10 tests failed, 5,751 passed, 103 skipped and 8 deselected; subsequent QC and reference stages NOT RUN | [Outcome](code004-outcome.md) · [receipt](technical-evidence/phase2-code004-qc.receipt.json) |

This canary proves the driver, environment, native strict path and persistence
for that revision. It does not prove later revisions, full QC, scientific review
or reference coverage. Later native QC stages remain unrun until recorded.

The earlier `phase2-code002-qc` failed run preserved a clean checkout. Four failures arose because
the fresh Git object store lacked pre-squash historical review bases; their
immutable ledger checks correctly refused to substitute current cache bytes
(#2813). One failure requires classification of four new enums in the existing
vocabulary registry (#2812). One fixture was outside the established test-data
directory (#2811); its unchanged bytes have since been moved and the native ID
guard passes. These diagnostics do not retrospectively change the failed run.
The raw full-run log is 773,200 bytes, SHA-256
`7b026b7a3e32da0f9e68431c516a0769a5d00f35111bb0e7fcdd7804cd7b59b3`.

The subsequent `phase2-code003-regressions` focused rerun passes all modules affected
by those code002 failures. It is not another
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

## Separate measured reference outcomes

At `9ba3eefc1be7a9f8bb9f0b9399f69429c16e44fc`, the M5 run completed 549 records
and enumerated 10,695 snippet surfaces: 10,172 actual comparisons, comprising
10,070 matches and 102 mismatches; one assertion had no content and 522
SupportingReference assertions were unannotated. Native validation exited 1.
These are source-comparison outcomes, not scientific verdicts. The detailed
[measurement report](../reference-assertion-coverage-20261115/README.md) retains
the failed parser attempt, corrected canaries, per-record counters and limits.
The subsequent [full M5 measurement at 20185647](../phase2-reference-measurements-20261115/m5-final-reference-corpus-001.md)
completed all 549 records with the SupportingReference annotations: 10,837
snippet surfaces, 10,836 actual comparisons, 10,728 matches, 108 mismatches and
one assertion without source content. Native validation exited 1 with 109 issues
across 17 records. No SupportingReference occurrence was omitted for missing
annotations. The single uncompared EvidenceItem and all source mismatches remain
recorded. This is a measured historical revision, not a passing final reference
gate; the later gut discussion correction requires a new final measurement.

## Campaign restart

The separate [inventory PR #2797](https://github.com/CultureBotAI/CommunityMech/pull/2797)
preserves the original path-ordered campaign and its stronger scientific-coverage
subsets. Refresh that inventory after Phase 2; verify one saved full-record
scientific review before distributing independent records. Each record gets a
native immutable YAML/Markdown bundle, and batches of ten get fresh branches,
reviewed PRs and durable checkpoints. Previous bundles are not rewritten and
their declarations are not treated as current scientific approval.
