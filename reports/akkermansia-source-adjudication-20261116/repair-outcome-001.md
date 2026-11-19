# Source-bound Akkermansia consistency checks

The lineage CLI and current-corpus denominator check now keep the two verified
R232 Akkermansia assertions in their own comparison group. The native Amsterdam
assertion remains in the existing group. No canonical record, numerical
tolerance, grounding algorithm or historical successor proof changed.

The separate [source checkpoint](README.md), published as
`9ef1f41bf3523a662b7f5a21a681147c5408f58e`, documents the official workbook and
taxonomy observations underlying this change. This implementation addresses
[#2833](https://github.com/CultureBotAI/CommunityMech/issues/2833) and
[#2948](https://github.com/CultureBotAI/CommunityMech/issues/2948).

## What the guard admits

The runtime contract authenticates three complete public metadata files before
using their contents: the independently inspected R232 workbook, the official
R232 taxonomy extraction, and the already published Amsterdam native proof.
It then checks the exact relative record path, record ID, taxonomy index and
complete selected descriptor, including its stock and notes.

| Selected assertion | Comparison group | Retained population |
| --- | --- | --- |
| Amsterdam 382, taxonomy[0] | Existing shared comparison | 4,983, fraction 1.0, native name route |
| MUC2 351, taxonomy[13] | Verified R232 Akkermansia population | 1,806, fraction .731 |
| MDSC 392, taxonomy[0] | Verified R232 Akkermansia population | 1,806, fraction .731 |

Only the last two blocks move between comparison groups. Every other block
remains in the existing group; no block is dropped. The unchanged pure hierarchy
checker runs separately within each group, including the two R232 blocks against
each other. Current shape and count checks still inspect the actual documents.
The CLI supplies full relative paths rather than basenames. Changed source bytes,
selected assertions, record identity, stock, duplicate occurrence, copied path or
unreviewed manual-source label refuse admission.

The denominator consumer shares this contract. The established exact MDSC/Blautia
guard runs first and keeps its original source hash, semantic-block assertion and
refusal behavior. Independent review found that the initial unexecuted ordering
would intercept its changed-block control with a different exception; this is
recorded in [#2953](https://github.com/CultureBotAI/CommunityMech/issues/2953).
Those original files remain under
`.temp/akkermansia-source-20261116/pre-ordering-review-001/`.
The finding was established by reading the control contract, not by a claimed
fail-before test. The correction adds an actual Blautia positive, changed-count
refusal and restoration, plus refusal when a changed Akkermansia block adopts
the Blautia ID. Existing Blautia controls are included in the composed matrix.

## Actual validation

The first real canary exercised the actual CLI on copies of all three records
and the exact source metadata. Its assertions also verify that the unchanged
unpartitioned checker still reports the original four parent-lineage conflicts,
while the source-bound comparison succeeds and retains every block. Only after
that one-unit canary passed did the composed matrix and corpus command run.

All recorder triplets are retained in `.temp/phase2-schema-20261115/`:

| Run | Observed result | Raw log SHA-256 |
| --- | --- | --- |
| `akkermansia-source-positive-canary-001` | 1 passed, 1.51 s; actual CLI exit 0 | `96a8cb52be1ed2c3302d2e9f6528eca38c1cf7c2462ec7201e826ec440278f9d` |
| `akkermansia-source-matrix-001` | 90 passed, 9 skipped, 85.20 s | `f205ab4f498b25832499bd5647e71a72857fb1f71e570cda7af00c43c42688ed` |
| `akkermansia-source-native-corpus-001` | Exit 0; 551 files, 0 incoherent blocks, 0 malformed lineages, 0 within-group lineage conflicts | `218c6c1e91dcf308610638a08f3fe2ff2a926100a91202611387be8d73d0d0c5` |
| `akkermansia-source-lint-002` | Exit 0; Black 816 files, Ruff passed, mypy 53 source files | `1819bd1b3bf52b1a1a137fd096a22056377c0f0c589770d4f467d3aa63b9bb3b` |

The matrix runs the new actual-source/CLI controls together with the unchanged
Blautia controls and the complete lineage and support-count modules. Controls
mutate each source proof, selected counts/fractions/lineage/IDs, stock, source
labels and paths, then restore the original positive state. They also preserve
contradiction detection within both comparison groups and in an unselected block.

The nine skipped tests depend on the module's shared live-crosswalk fixture.
A separate one-test observation with skip reporting retained the fixture's exact
refusal in `akkermansia-mapping-fixture-observation-001` (raw log
`4542d2795452be3f449197e660bc79063241a49e4cf17922dfcd9f060a4d18b6`).
That observation was one skip, not an additional passing control or fresh native
grounding result. The source contract uses the already captured native proof.

The first lint attempt refused before executing checks because the recorder's
`JUST_NO_DOTENV=1` is not a valid boolean for the installed `just`. Its exit 2 and
raw log `3e6bdd695c4f518ccb8857917f42178c0601fc4cfad25b5023237d9101c6ff3e`
are retained as `akkermansia-source-lint-001`. The successful second attempt
explicitly passed `env JUST_NO_DOTENV=true just lint`; no helper was changed.
Ruff also reported the existing invalid `noqa` directive warning in
`scripts/gtdb_ground.py:74`, while returning success.

Execution used Python 3.13.12 at source checkpoint `9ef1f41b` with the five
reviewed implementation/test changes recorded in the receipts. This is not a
clean aggregate-check result. No canonical or history file changed, and the pure
`gtdb_lineage_tree.py` implementation remains byte-identical to that checkpoint.

## Limits retained

The 1,806 NCBI-name workbook population and 1,372 exact GTDB-species taxonomy rows
are different selections. Neither supplies an independently observed integer
numerator for the stored .731 fraction. The native crosswalk's release remains
unknown, so this change establishes no older/newer relationship to R232.

The comparison deliberately does not assert global hierarchy coherence across
those unverified releases. It verifies the two admitted R232 assertions together
and preserves the existing comparison for everything else. Source strings or a
`curated` flag never grant an exemption. The original R232 metadata and exact
experimental-stock genome matches remain unverified; ATCC BAA-83 is not changed
to BAA-835, and the DSM stock assertions remain as sourced. No new scientific
review, full ecological/causal approval, whole-corpus QC or issue closure is
claimed by these focused checks.
