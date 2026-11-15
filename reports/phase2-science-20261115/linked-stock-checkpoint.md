# Linked-stock curation checkpoint

This checkpoint applies the independently reviewed corrections for
[2674](https://github.com/CultureBotAI/CommunityMech/issues/2674),
[2774](https://github.com/CultureBotAI/CommunityMech/issues/2774) and
[2806](https://github.com/CultureBotAI/CommunityMech/issues/2806).
The new scientific successor review and 27 integrated native gates are pending.
It does not claim full QC, Phase 2 completion or a merge.

| Record | Bounded change | Persisted SHA-256 |
| --- | --- | --- |
| 000025 EcoFAB SynCom17 | Source-supported OAP107 genus, reproducible mapping provenance, individual OAS925 deposit and reciprocal membership | `0adba2db63b8277d16d0a0e71db00a36009daf5e8ac6231b9081128421bd818c` |
| 000516 dopamine SynCom16 | Same grounding and stock corrections, without changing its five scientific nodes | `304702c684faedb244d678e628ec174851dbdcafe46128eab86d824798e0482a` |
| 000087 Coker final16 | Reciprocal membership basis and explicit Methods-defined collection scope only | `bb31b1df4a9be2241453528101fc5d55657c23eccf1d58ce1cc9639e5912b368` |

The paired records retain all 29 existing numerical GTDB mapping cores, including
the curated bacterial Bosea mapping associated with NCBI Allobosea. Current
NCBI genus labels and the explicit bacterial synonym were verified in a readonly
local ontology. The inspected crosswalk is
`sha256:761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd`.
OAP107 now retains 11 ambiguous genus candidates; no stock genome or GTDB release
date is inferred. Existing Paenibacillus ambiguity and curated notes survive.

Coker Methods reports DSM 113627 for OAS925. Ring-trial Methods supplies the
same-stock genus rename and distinguishes the DSM 200000SY consortium collection
from individual strains. The accession remains a primary-source assertion;
the current individual DSMZ catalog was not independently checked for OAS925.
All six reciprocal membership links across these three records now use the
complete source-designated rosters. The Methods/Table S1 conflict remains
explicit in 000087.

Before application, the maintained related-community policy from public
integration revision `34cce97e312752a59daf1f1ffa05c5f966304111` checked a complete
549-record native index with exactly these three staged overrides. It found no
duplicate IDs and no findings for the three candidates. This bounded diagnostic
does not replace full strict validation or source review.

The EcoFAB write canary persisted the exact reviewed candidate, created a native
actor-codex history sidecar, and passed native schema and scoped history checks.
Only then were the other two candidates applied and their native sidecars
created. Every previous review and history artifact remains immutable. The
guard rejects source/peer changes and reconstructs every candidate from pinned
originals, so editing a candidate and its manifest hash cannot expand scope.

Retained source and check evidence is in the repository-private
`.temp/phase2-science-20261115/` tree: `linked-stock-plan-003`,
`linked-staged-policy-001.json`, `linked-*-grounding-001.json`, and
`linked-ecofab-*-canary001` receipts. The plan receipt SHA-256 is
`109a87dc852011cc050f5e3c5c8aa77c2a8c7bdc0b4ed893f13891df7b013275`.
The provenance helpers are retained under `scripts/adhoc/` with the
`phase2_linked` name, and the guarded application tests are in
`tests/test_phase2_linked_stock_guard.py`.

Checkpoint validation: 12 guarded-write and writer-classification tests passed;
Black, Ruff and mypy passed; native page generation completed and changed only
the three expected community pages. All three scoped native history validations
passed after the final writes. The earlier writer-classification failure is
retained; its reviewed exemption covers only the private diagnostic runner.

[1427](https://github.com/CultureBotAI/CommunityMech/issues/1427) still owns the
EcoFAB non-graph causal roles and mixed study-stage claims.
[2675](https://github.com/CultureBotAI/CommunityMech/issues/2675) remains an
**actionable** exact-genome correction: retained Ring S2 contains all 17
stock-to-IMG/GOLD/assembly rows, including the OAE908 accession omitted by the
record's pseudo-range. These findings are not resolved by this checkpoint.
