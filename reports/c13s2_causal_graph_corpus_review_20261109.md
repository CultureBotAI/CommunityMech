# Cycle 13 Stage 2 (`causal_graphs`) Corpus Review and Curation Report (2026-11-09)

## 1. Corpus-Wide Inventory & Eligibility Audit

All **537** eligible YAML records across the three repository roots were audited for native ecological interaction and causal-graph representation during Cycle 13 Stage 2 (`mech-goal-sequence-20261019`):

| Corpus Root | Root Class | Record Count | Ecological Interaction Nodes | Directed `downstream` Edges | Review Disposition |
|---|---|---:|---:|---:|---|
| `kb/communities/*.yaml` | `MicrobialCommunity` | 512 | 1,522 | 594 | `458 reviewed`, `54 needs_research`, `0 pending`, `0 stale` |
| `data/isolates/*.yaml` | `MicrobialCommunity` | 23 | 23 | 0 | `23 reviewed`, `0 needs_research`, `0 pending`, `0 stale` |
| `kb/taxa/*.yaml` | `CommonTaxon` | 2 | 0 (no `ecological_interactions` slot on `CommonTaxon`) | 0 | `2 reviewed` (`role_genes` + UniProt protein evidence verified) |
| **Total** | — | **537** | **1,545** | **594** | **`481 reviewed` (`MicrobialCommunity`) + `2 CommonTaxon`, `54 needs_research`, `0 pending`, `0 stale`, `0 structural_defects`** |

- **`reports/causal_graph_review/summary.json` invariants**:
  - `records`: `535` (`512` in `kb/communities/` + `23` in `data/isolates/`)
  - `nodes`: `1545`
  - `edges`: `594`
  - `records_without_nodes`: `10` (all in `needs_research`)
  - `records_without_edges`: `226`
  - `review_status_counts`: `{"needs_research": 54, "reviewed": 481}` (`pending: 0`, `stale: 0`)
  - `structural_defects`: `[]`

## 2. Batch 145 Source-Based Curation (`CommunityMech:000536`–`CommunityMech:000541`)

The 6 records added in Cycle 13 Stage 1 (`PR #2743`, commit `487f82dcae308bb50cf1088f50734f5263b8e8a2`) entered Stage 2 in `pending` status and were reviewed against their committed full-text primary sources (`references_cache/PMID_42795638.txt` / `PMC13609637` and `references_cache/PMID_42117636.txt` / `PMC13274399`), enriched via `write_validated_community` + `record_curation_event(action="CURATE_CAUSAL_GRAPH")`, recorded in `reports/causal_graph_review/decisions/20261109-stage2-six-records-batch145.yaml`, and logged in append-only `history/records/` sidecars:

| ID | Path | Primary Source | Nodes | `downstream` Edges | Interaction `EvidenceItem` Snippets (Before -> After) | Pre-Stage-2 `original_sha256` -> Post-Stage-2 `record_sha256` |
|---|---|---|---:|---:|---|---|
| `CommunityMech:000536` | `data/isolates/Pseudomonas_ZM1_Prometryn_Degrading_Isolate_Baseline.yaml` | `PMID:42795638` (`PMC13609637`) | 1 (`COMMUNITY_LEVEL`) | 0 | `4 -> 6` (`+2` verbatim snippets from Table 1 and Discussion) | `67480cb95671...` -> `e600a10abb5375a5f013fd189c67d16b0ae8cedebc1032c5c28526f206e786f1` |
| `CommunityMech:000537` | `data/isolates/Achromobacter_ZM2_Prometryn_Degrading_Isolate_Baseline.yaml` | `PMID:42795638` (`PMC13609637`) | 1 (`COMMUNITY_LEVEL`) | 0 | `4 -> 6` (`+2` verbatim snippets from Table 1 and Discussion) | `e023b1735aa3...` -> `1473199ef62f7ecfc0cef4a07469f452050a512ce973c24ddc0d049587feeb7e` |
| `CommunityMech:000538` | `data/isolates/Stenotrophomonas_ZM3_Prometryn_Degrading_Isolate_Baseline.yaml` | `PMID:42795638` (`PMC13609637`) | 1 (`COMMUNITY_LEVEL`) | 0 | `3 -> 6` (`+3` verbatim snippets from Table 1, Figure 2A, and Table 2) | `ce4fa1d8c260...` -> `d8d5b3564c9a94a868e278f7d04b23999b02ddfeda1e72b89495ec8402a35fa3` |
| `CommunityMech:000539` | `data/isolates/Rhodopseudomonas_Palustris_CGA676_Anaerobic_Monoculture_Baseline.yaml` | `PMID:42117636` (`PMC13274399`) | 1 (`COMMUNITY_LEVEL`) | 0 | `5 -> 7` (`+2` verbatim snippets from Figure 3D and Figure 7C/2C) | `72a714951fe8...` -> `ad02b70b47aa8cd86d7949e08c3ce23366c1caec6c5463c74cd45a9396aac666` |
| `CommunityMech:000540` | `data/isolates/Escherichia_Coli_PFM2_Anaerobic_Monoculture_Baseline.yaml` | `PMID:42117636` (`PMC13274399`) | 1 (`COMMUNITY_LEVEL`) | 0 | `5 -> 7` (`+2` verbatim snippets from Figure 2C-D and Figure S1A-B) | `7a3ddab08e70...` -> `991e85326303854835a6a7481d1599e068f4d67411856fbb8092620953919b18` |
| `CommunityMech:000541` | `kb/communities/Rhodopseudomonas_CGA676_Ecoli_PFM2_DeltaPurH_Adenine_Competition_Coculture.yaml` | `PMID:42117636` (`PMC13274399`) | 2 (`COMMUNITY_LEVEL CROSS_FEEDING`, `COMMUNITY_LEVEL COMPETITION`) | 1 (`Node 1 -> Node 2`) | `5 -> 9` (`2 -> 4` on Node 1; `3 -> 5` on Node 2) | `f9225d426a29...` -> `19eb2a05854e12882277cdc6646edf9f9c5fc91f4392cc080fc2b09bcb9b0382` |

## 3. Taxonomic Grounding Verification Across Causal-Graph Elements

In accordance with `.claude/skills/ground-causal-graph-taxa/SKILL.md`, every taxon in `taxonomy` and `ecological_interactions[].participating_taxa` across Batch 145 was verified for exact string and `NCBITaxon` match plus GTDB grounding:

- `CommunityMech:000536`: `Pseudomonas sp. ZM-1` (`NCBITaxon:286` `Pseudomonas`, `GTDB:g__Pseudomonas`, `gtdb_grounding_status: GROUNDED`, `is_reclassified: false`).
- `CommunityMech:000537`: `Achromobacter sp. ZM-2` (`NCBITaxon:222` `Achromobacter`, `GTDB:g__Achromobacter`, `gtdb_grounding_status: GROUNDED`, `is_reclassified: false`).
- `CommunityMech:000538`: `Stenotrophomonas sp. ZM-3` (`NCBITaxon:40323` `Stenotrophomonas`, `GTDB:g__Stenotrophomonas`, `gtdb_grounding_status: GROUNDED`, `is_reclassified: false`).
- `CommunityMech:000539`: `Rhodopseudomonas palustris CGA676` (`NCBITaxon:1076` `Rhodopseudomonas palustris`, `gtdb_grounding_status: AMBIGUOUS` across 5 GTDB species candidates `GTDB:s__Rhodopseudomonas_palustris_C`/`F`/`G`/`J` and `GTDB:s__Rhodopseudomonas_pseudopalustris`).
- `CommunityMech:000540`: `Escherichia coli PFM2` (`NCBITaxon:562` `Escherichia coli`, `GTDB:s__Escherichia_coli`, `gtdb_grounding_status: GROUNDED`, `is_reclassified: false`).
- `CommunityMech:000541`: `Rhodopseudomonas palustris CGA676` (`NCBITaxon:1076`, `AMBIGUOUS`), `Escherichia coli PFM2` (`NCBITaxon:562`, `GTDB:s__Escherichia_coli`, `GROUNDED`), and `Escherichia coli PFM2 ΔpurH` (`NCBITaxon:562`, `GTDB:s__Escherichia_coli`, `GROUNDED`) match identically between `taxonomy` and both `ecological_interactions[].participating_taxa` lists.

## 4. Source-Limited Gaps and Representation / Writer Blockers

1. **Batch 145 Source-Limited Boundaries**:
   - **Prometryn-degrading isolate baselines (`CommunityMech:000536`, `000537`, `000538`, `PMID:42795638`)**: Each axenic isolate baseline contains a single `COMMUNITY_LEVEL` prometryn catabolism node with `0` `downstream` edges because `PMID:42795638` measures parent-compound removal by HPLC and defers intermediate s-triazine metabolite identification and catabolic gene sequencing (`trzN`/`atzA`/`atzB`/`atzC`) to follow-up work (recorded in 3 `KNOWLEDGE_GAP` discussions: `zm1_specific_prometryn_transformation_enzymes_unresolved`, `zm2_fast_biomass_vs_lower_prometryn_degradation_efficiency`, and `zm3_acid_alkali_tolerance_and_triazine_pathway_genes_unresolved`). Multi-strain temporal niche complementarity belongs on the 3-strain synthetic consortium record (`CommunityMech:000503`).
   - **Anaerobic experimental evolution monoculture baselines (`CommunityMech:000539`, `000540`, `PMID:42117636`)**: Each axenic monoculture baseline contains a single `COMMUNITY_LEVEL` node with `0` `downstream` edges. Unresolved mechanistic questions—why `hoxJ` 5-bp deletions swept in 7 replicate `R. palustris` monocultures but not in cocultures (`cga676_monoculture_vs_coculture_hoxj_selection_asymmetry`) and which intraspecific metabolites supported the 6 non-adenine auxotrophic `E. coli` monoculture isolates (`pfm2_monoculture_rpoc_polyauxotrophy_and_subpopulation_crossfeeding`)—are preserved in `KNOWLEDGE_GAP` discussions. Cross-species NH4+/adenine and organic-acid exchange is represented on `CommunityMech:000370` and `CommunityMech:000541`.
   - **Three-strain mutual-invasion competition coculture (`CommunityMech:000541`, `PMID:42117636`)**: Represented as a 2-node, 1-edge causal graph (`Ammonium and Adenine Cross-Feeding from R. palustris CGA676 to Prototrophic E. coli PFM2 and Auxotrophic PFM2 ΔpurH` -> `Repression of Prototrophic E. coli purH Expression Eliminating Fitness Advantage of PFM2 ΔpurH in Mutual-Invasion Competition`). The contrast with `E. coli` MG1655 `rph`-linked adenine toxicity is captured in the `EMERGING_HYPOTHESIS` discussion `rph_frameshift_adenine_toxicity_vs_bqh_cost_saving_in_ecoli`.
2. **Corpus-Wide `needs_research` Cohort (`54` Records)**:
   - `54` community records in `kb/communities/` remain in `needs_research` status (`10` without interaction nodes and `44` where committed `references_cache/` sources are abstract-only or lack multi-step experimental perturbation evidence). In compliance with Stage 2 instructions, no unsupported nodes or `downstream` edges were invented.
3. **Representation & Writer Blockers (`0` Active Blockers)**:
   - `InteractionDownstream` in `src/communitymech/schema/communitymech.yaml` has `target` and `description` attributes (`communitymech-infra-0001` formalized the two-tier edge-provenance contract where parent `EcologicalInteraction.evidence` holds verbatim `EvidenceItem` citations and `reports/causal_graph_review/decisions/*.yaml` records `edges_after` and `retained_edge_decisions`).
   - `CommonTaxon` (`kb/taxa/Geobacter_sulfurreducens.yaml` and `kb/taxa/Shewanella_oneidensis_MR1.yaml`) represents reusable taxon/gene reference records (`role_genes` + UniProt protein evidence) rather than community-specific causal graphs.
