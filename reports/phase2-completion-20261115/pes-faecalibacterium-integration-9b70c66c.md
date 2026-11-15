# PES and Faecalibacterium community integration

The actual M5 corrections for CommunityMech:000340 and 000401 are integrated at `9b70c66c75f24e1f485ec1fb1c58ae24f4635cac`. Their source judgments, guarded writes, native checks, immutable partial reviews and complete private input checkpoints were independently verified before integration. They retain `scientific_review: false`; neither is a complete scientific review.

| Record | Actual persisted change | Evidence |
|---|---|---|
| 000340 PES | Native genus correspondences for the existing N7/A11 descriptors, with 16/16 and 46/46 reference genomes; no stock species or assembly assignment | [Canary outcome](../gtdb-code006-20261115/pes-001-outcome.md), [strict proof](../gtdb-code006-20261115/pes-001-successor.json) |
| 000401 Bifidobacterium/Faecalibacterium | All three native alternatives for the existing Faecalibacterium descriptor, without selecting one for A2-165/JCM31915 | [Canary outcome](../gtdb-ambiguity-20261115/status401-canary-outcome-001.md), [strict proof](../gtdb-ambiguity-20261115/status401-001-successor.json) |

The source commits are `1d5bfe5ad58c0321fa988646d049cc810ba292b2` and `62c290b4c22f3ded1c4a669acff68e9e8d01e72d`, integrated as `c80a224f` and `233acb1d`. Source execution remains tied to each original M5 revision and runtime; those runs are not relabeled as executions of the integration revision.

## Combined verification

At the clean recorded revision above, 13 focused modules passed **208 tests**, with 12 existing Pydantic deprecation warnings, in 67.74 seconds. They cover the unchanged scientific assertions in batches 6/83/147, the existing fixed genus/species successors, shared strict admission, actual evidence mutation/restoration, evidence export, native write provenance and the R226 captured-byte regression. The actual 554/340/401 cases all run by default. The 26 missing-sibling fixture setup errors in the isolated 401 branch do not occur in this composed tree. No old failed run or missing fixture was waived.

Native `just lint` passed: Black checked 726 files, Ruff passed, and mypy passed all 52 source files. Both runs used the existing offline/no-sync environment and persisted their actual command, clean initial Git status, revision, nonempty log and exit 0.

| Run in `.temp/phase2-schema-20261115/` | Log bytes | Log SHA-256 |
|---|---:|---|
| `integrated-pes-status401-9b70c66c-001` | 993 | `447260825b57e5364e370f745e5dceb274f8e700277670ec8ce0bfeab0317995` |
| `integrated-pes-status401-lint-9b70c66c-001` | 219 | `c1641a2df95d89be0db300c030cdf4966a84d2ab8de99cad58d16c4c185ed35b` |

Each run retains `.json`, `.log` and `.exit` files. These focused checks do not replace the required final full M5 `just qc` run or separate reference comparison.

## Persistence and products

Independent saved-pair audits verified all 77 PES inputs (4,920,982 bytes) and 81 Faecalibacterium inputs (5,032,174 bytes), native schema validity and exact derived Markdown. Complete checkpoints preserve the old caller bytes before historical-admission edits: PES has 79 files/4,990,803 bytes on both machines; Faecalibacterium has 83 files/5,104,038 bytes on M5, with local audit receipts and public proof. The individual outcome reports retain the exact manifest identities and original scope limits. Current caller changes use the strict proof to expose verified predecessor bytes for historical predicates while preserving assertions about current biology.

The native page renderer first persisted the PES canary, whose nonempty HTML and record identity were checked before rendering the second record through the same CLI. Both rendered successfully into private `community-render-9b70c66c-001/`; maintained pages were not overwritten by these probes.

| Generated page | Bytes | SHA-256 |
|---|---:|---|
| `Pelagerythrobacter_Salinicola_PES_Pyrene_Degradation_SynCom.html` | 65,876 | `885149f95317c328a04d8e977882a4028712571ae56b191db7e8c954f029ae9f` |
| `Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.html` | 67,035 | `76dd23338a595c0033c4fdd45132d15aac250b925979499b21a59e64e6a84778` |

The render receipts are `community-render-000340-9b70c66c-001` and `community-render-000401-9b70c66c-001`. This verifies native rendering and persisted record identity, not complete browser interaction or visual presentation of every taxonomy field. Updating the maintained generated products remains part of the combined completion work.

The integration also retains the independently reviewed [R226 source comparison](../gtdb-ambiguity-20261115/paenibacillus-source-comparison-001.md), including the captured-byte verification for #2870. Record 393's source disagreement remains unresolved under #2869; no candidate was selected or resolver policy exempted by that report.

Eleven correction canaries are integrated in total, seven drawn from the historical 126-record repair partition. That partition remains an immutable planning snapshot, not proof of current corpus completion. Further actual M5 records and source plans are separate work. Full combined QC, the 109 previously measured reference failures and their issue owners, the scoped scientific limitations, upstream Claw #1219's pending merge decision, and the subsequent all-record scientific campaign retain their prior status.
