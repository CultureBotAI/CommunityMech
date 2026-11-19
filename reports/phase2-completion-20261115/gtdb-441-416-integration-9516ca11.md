# Akkermansia source adjudication and two M5 record checkpoints

Integration revision `9516ca1100ee47ee413b6d13f03365744f798428` includes
the independently reviewed Akkermansia source repair, Dolichospermum441 and
Thermophilic416 checkpoints. Full combined QC remains incomplete. The
all-record scientific review campaign has not resumed; Phase 2 remains first.

## Source and record scope

The Akkermansia source commits are
`9ef1f41bf3523a662b7f5a21a681147c5408f58e` and
`ec1a6788f2748fb9e6890f9c08159b9cdd96bd19`, published in
[PR2951](https://github.com/CultureBotAI/CommunityMech/pull/2951).
They were integrated without conflicts as `983ba78ba9cea429e8cd819a7525a89f5e93b608`.
The [source report](../akkermansia-source-adjudication-20261116/README.md)
and [repair outcome](../akkermansia-source-adjudication-20261116/repair-outcome-001.md)
distinguish the official R232 NCBI-name population from the separate GTDB-species
population and the name-route result from a crosswalk of unestablished release. No integer support
numerator is reconstructed from the rounded workbook percentage. Exact source
proofs and current record blocks govern the two R232 comparisons; the pure
lineage checker and current record biology remain unchanged. Unknown manual
claims, proof changes, same-source contradictions and the existing Blautia
contract still refuse invalid input.

The reviewed Dolichospermum441 leaf
`4f46bb640e0a5ceec646df90527bdfa881a20e12` was integrated as
`57dc0452c6cb58540a66e371dd63b6cb3f87d09e`. Its
[outcome](../gtdb-genus-last-four-20261115/441-canary-outcome-001.md)
records eight actual M5 gates and a saved partial diagnostic. The complete
81-file checkpoint was independently verified on both hosts. Generic genus
correspondences and the complete cyanobacterial ambiguity remain distinct from
the paper's recovered stock genomes and computational cofactor predictions.

The Thermophilic416 leaf `d7e3b4a99815d3555d9979f0b25cda3a4552b181`
was integrated as `9516ca1100ee47ee413b6d13f03365744f798428`. Its
[outcome](../gtdb-shrimp-thermophilic-sahara-20261115/416-canary-outcome-001.md)
records eight actual M5 gates, a saved partial diagnostic and the independently
verified 85-file checkpoints on both hosts. The six reference descriptors are
overlapping ranks. qPCR controls are not identified reactor members; total-DNA
counts do not establish viability, activity or taxon-specific flux. The single
reactor's sequential phases do not resolve the causal alternatives in issue1935.
Both new diagnostics retain `scientific_review: false` and partial scope.

The cherry-picks required composition of historical callers. Batch33 now keeps
both the existing Diclofenac379 and Dolichospermum441 strict proof paths. Batch120
keeps the existing 454 remediation chain, the literal 106 C14S5 chain and the new
416 proof. Current biological predicates and old ledgers were not rewritten.
The incoming genus README was retained because its preparation parent was not
previously included in this integration checkout. No canonical YAML conflict
was resolved manually. Failed cherry-pick logs remain preserved.

## Actual integrated verification

At clean `983ba78b`, the real crosswalk was supplied through `KG_MICROBE_DIR`.
Its SHA256 is `761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd`;
the directory name does not establish a release. One real population-path
canary passed before the four-module regression batch. The batch passed all
99 tests with 12 warnings and no skips. Native `just validate-gtdb-all` separately
checked 551 files with zero incoherent blocks, malformed lineages or conflicts.
This closes the nine missing-crosswalk skips in the leaf's focused execution;
neither result is a full-QC pass.

At clean `9516ca11`, the real current near-tie census failed once because
Thermophilic416 adds the reviewed Methanobacteriota majority. The observed
failure is recorded in [issue2954](https://github.com/CultureBotAI/CommunityMech/issues/2954).
The independently read correction authenticates the entire strict 416 proof,
then exact descriptor 0 (2815/5300, 0.531) or descriptor 1 (226306/451729, 0.501).
The existing Algal415 proof, historical four-Bacillota floor, advisory 0.55
threshold, maximum marked population and curation requirement at or below 0.5
remain unchanged. The tests exercise actual copied proof artifacts, altered
counts/identities, record/manifest/native-proof bytes, unknown paths and immediate
restoration. No test mutates the maintained evidence bundles.

The correction was tested as two working-file changes atop `9516ca11`:
`test_gtdb_near_tie_marker.py` SHA256
`5e6eddd9730c61c63025b297ae0e74265e91a5d385140c1476ca8e03a26bee45`
and `test_near_tie_source_admission.py` SHA256
`ee14c32625d9d6a8c80df1afbe22e3e13065ef8966b7b69e06558d0a3e35e4ed`.
The separate real 416 proof canary passed before the composed batch. Native
lint passed Black over 823 files, Ruff and mypy over 53 source files.

All raw triplets below are retained under `.temp/phase2-schema-20261115/`.

| Recorder name | Revision / outcome | Raw log SHA256 |
| --- | --- | --- |
| `integration-akkermansia-crosswalk-canary-001` | clean `983ba78b`; 1 passed | `364fae48cbe8f4ef8e995f8fb3224d43792e784eb9919ceefea2fe0106918edf` |
| `integration-akkermansia-with-crosswalk-controls-001` | clean `983ba78b`; 99 passed, 12 warnings | `cec3f5220992987b051f9cc140bf497c58977b6b0210379212024f13ede814b3` |
| `integration-akkermansia-native-corpus-001` | clean `983ba78b`; 551 files, zero errors | `218c6c1e91dcf308610638a08f3fe2ff2a926100a91202611387be8d73d0d0c5` |
| `integration-416-near-tie-baseline-001` | clean `9516ca11`; 1 failed, 12 warnings | `f9a596cce20b89a631d4d2272dc63bb70ff61b81b95277b985eec43add9f3ec9` |
| `integration-416-near-tie-canary-001` | `9516ca11` plus the two pinned test changes; 1 passed, 12 warnings | `077b6d907aff4f0d0e5619ce16680c440abcd02668f90244461511001dfbf4ba` |
| `integration-441-416-lint-001` | same two pinned changes; Black/Ruff/mypy passed | `ec2b51749e2d01045365a337a17973ac1f09699e198cf9dedb795cce68b53b20` |
| `integration-441-416-composed-controls-001` | same two pinned changes; 236 passed, 12 warnings, no skips | `506b3d5b935d6ab8504c24526d53e27282d3439bb52d4c990625d522349a7a2c` |

The composed regression batch finished with exit 0 after 299.60 seconds.
It covered the actual genus, Shrimp, environment and remaining-four proof
registries, both composed historical callers, the actual near-tie proof
controls and the current native near-tie tests. These 236 focused passes
do not replace the required full native QC run.

## Remaining work

The byte inventory at `9516ca11` has 118 changed and eight unchanged records
among the original 126 assignments. Changed bytes are not proof of review or
completion. The unchanged IDs are 363, 376, 381, 389, 419, 482, 494 and 501;
other execution branches are not counted as integrated corrections. Inventory
`.temp/phase2-integration-20261115/gtdb-progress-9516ca11-001.json` has SHA256
`5ed342072e22c0efbd0b348408af2e83f8e2e4ba547b99a45f533a472f9e685f`.
The four-record ambiguity input transfer still awaits its specific permission
after the recorded automatic approval rejection.

The six-record measurement at `d7350491` and its 270 actual matches remain
historical results, as recorded in the [preceding integration checkpoint](supplement-census-integration-ff4621c5.md).
They do not replace fresh combined M5 QC, the full reference sweep or disposition
of the scoped scientific blockers. No CommunityMech merge is authorized by this
checkpoint.
