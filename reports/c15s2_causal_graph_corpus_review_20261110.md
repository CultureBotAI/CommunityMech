# Cycle 15 Stage 2 (`causal_graphs`) Corpus Review and Curation Report (2026-11-10)

## 1. Corpus-Wide Inventory & Eligibility Audit

All **551** eligible YAML records across the three repository roots were audited for native ecological interaction and causal-graph representation during Cycle 15 Stage 2 (`mech-goal-sequence-20261019`):

| Corpus Root | Root Class | Record Count | Ecological Interaction Nodes | Directed `downstream` Edges | Review Disposition |
|---|---|---:|---:|---:|---|
| `kb/communities/*.yaml` | `MicrobialCommunity` | 512 | 1,522 | 594 | `458 reviewed`, `54 needs_research`, `0 pending`, `0 stale` |
| `data/isolates/*.yaml` | `MicrobialCommunity` | 37 | 37 | 0 | `37 reviewed`, `0 needs_research`, `0 pending`, `0 stale` |
| `kb/taxa/*.yaml` | `CommonTaxon` | 2 | 0 (no `ecological_interactions` slot on `CommonTaxon`) | 0 | `2 reviewed` (`role_genes` + UniProt protein evidence verified) |
| **Total** | — | **551** | **1,559** | **594** | **`495 reviewed` (`MicrobialCommunity`) + `2 CommonTaxon`, `54 needs_research`, `0 pending`, `0 stale`, `0 structural_defects`** |

- **`reports/causal_graph_review/summary.json` invariants**:
  - `records`: `549` (`512` in `kb/communities/` + `37` in `data/isolates/`)
  - `nodes`: `1559`
  - `edges`: `594`
  - `records_without_nodes`: `10` (`9` in `needs_research` + `1` in `reviewed` (`CommunityMech:000390`))
  - `records_without_edges`: `240`
  - `review_status_counts`: `{"needs_research": 54, "reviewed": 495}` (`pending: 0`, `stale: 0`)
  - `structural_defects`: `[]`

## 2. Batch 147 Source-Based Curation (`CommunityMech:000549`–`CommunityMech:000555`)

The 7 isolate baseline records added in Cycle 15 Stage 1 (`PR #2758`, commit `ed7f2fc5932885879416d178711744243835c536`) entered Stage 2 in `pending` status and were reviewed against their committed full-text primary sources (`references_cache/PMID_42587276.txt` / `PMC13548369`, `references_cache/PMID_42666409.txt` / `PMC13554761`, and `references_cache/PMID_42364169.txt` / `PMC13506996`), enriched via `write_validated_community` + `record_curation_event(action="CURATE_CAUSAL_GRAPH")`, recorded in `reports/causal_graph_review/decisions/20261110-stage2-seven-records-batch147.yaml`, and logged in append-only `history/records/` sidecars:

| ID | Path | Primary Source | Nodes | `downstream` Edges | Interaction `EvidenceItem` Snippets (Before -> After) | Pre-Stage-2 `original_sha256` -> Post-Stage-2 `record_sha256` |
|---|---|---|---:|---:|---|---|
| `CommunityMech:000549` | `data/isolates/Bacillus_Paramycoides_B81_PAH_Biodegradation_Isolate_Baseline.yaml` | `PMID:42587276` (`PMC13548369`) | 1 (`COMMUNITY_LEVEL`) | 0 | `3 -> 5` (`+2` verbatim snippets from Section 3.3 and Section 3.4 on single-strain phenanthrene degradation rate, pyrene non-degradation, and bioemulsifier/CSH comparison) | `a1862a927c0c...` -> `cb226c9c70b14d042991de11ef4a7b3677790ffd8a93549332e213dc4946b04e` |
| `CommunityMech:000550` | `data/isolates/Bacillus_Paranthracis_A1_PAH_Biofilm_Isolate_Baseline.yaml` | `PMID:42587276` (`PMC13548369`) | 1 (`COMMUNITY_LEVEL`) | 0 | `3 -> 5` (`+2` verbatim snippets from Section 3.2 and Section 3.3 on A1+A3+B8-1 synergy and biofilm formation/CSH enhancement) | `00fd3bda9890...` -> `3b4fa9c9579fe2f3c0b94f2c1c55ec6b8f36bb5e22d4c5f9718aeb798cc15988` |
| `CommunityMech:000551` | `data/isolates/Bacillus_Licheniformis_A3_PAH_Biofilm_Isolate_Baseline.yaml` | `PMID:42587276` (`PMC13548369`) | 1 (`COMMUNITY_LEVEL`) | 0 | `2 -> 5` (`+3` verbatim snippets from Section 3.1, Section 3.2, and Section 3.3 on pyrene isolation, A3+B8-1 vs A1+A3+B8-1 comparison, and biofilm stimulation) | `41dbfbc369e4...` -> `de118e18969d2bfaddac33e51e49d5481ec224427441cf90d1faa5c18438d73b` |
| `CommunityMech:000552` | `data/isolates/Pelagerythrobacter_N7_Halophilic_Pyrene_Oxidation_Isolate_Baseline.yaml` | `PMID:42666409` (`PMC13554761`) | 1 (`COMMUNITY_LEVEL`) | 0 | `3 -> 5` (`+2` verbatim snippets from Section 3.2 and Section 3.3 on `N7` mono/dioxygenase dominance vs low decarboxylase activity and high CSH `43.25%`) | `114c68f88dd9...` -> `16d14ed3792a286afedaa4f17ba1c1773ebb04c6a7e8fc622cb7d946ce4c9610` |
| `CommunityMech:000553` | `data/isolates/Salinicola_A11_Halophilic_Bioemulsifier_Decarboxylase_Isolate_Baseline.yaml` | `PMID:42666409` (`PMC13554761`) | 1 (`COMMUNITY_LEVEL`) | 0 | `3 -> 5` (`+2` verbatim snippets from Section 3.2 and Section 3.4 on low axenic CSH `24.85%`, decarboxylase activity, and phthalate pathway division of labor) | `a23fb3d2c224...` -> `82b65eee0a1216e8a26c875a17206c3060b2304223a3eac2fcb1171de79aee4b` |
| `CommunityMech:000554` | `data/isolates/Rhizorhabdus_Wittichii_YL_JM2C_BDE47_Dioxygenase_Isolate_Baseline.yaml` | `PMID:42364169` (`PMC13506996`) | 1 (`COMMUNITY_LEVEL`) | 0 | `3 -> 5` (`+2` verbatim snippets from Abstract and Section 3.2 on `YL-JM2C` BDE-47 cleavage to `2,4-DBP` and `2,4-DBP` cytotoxicity threshold) | `f1dc3f787b96...` -> `e70a8434bd8db3852302899814f08a19d97c0e9d73a6636cb7715295642fdf59` |
| `CommunityMech:000555` | `data/isolates/Cupriavidus_Necator_JMP134_24DBP_Hydroxylase_Isolate_Baseline.yaml` | `PMID:42364169` (`PMC13506996`) | 1 (`COMMUNITY_LEVEL`) | 0 | `2 -> 5` (`+3` verbatim snippets from Abstract, Section 3.1, and Section 3.5 on `JMP134` lack of BDE-47 degradation, `2,4-DBP` mineralization kinetics, and `TfdB` hydroxylase) | `c97c0c57afa5...` -> `429964cbf945c41b2e89b57a072718158cf674e03786ef34b1ef96fe9247995e` |

## 3. Taxonomic Grounding Verification Across Causal-Graph Elements

In accordance with `.claude/skills/ground-causal-graph-taxa/SKILL.md`, every taxon in `taxonomy` and `ecological_interactions[].participating_taxa` across Batch 147 was verified for exact string and `NCBITaxon` match plus GTDB grounding status:

- `CommunityMech:000549`: `Bacillus paramycoides B8-1` (`NCBITaxon:2026194` `Bacillus paramycoides`, `gtdb_grounding_status: UNRESOLVED`).
- `CommunityMech:000550`: `Bacillus paranthracis A1` (`NCBITaxon:2026186` `Bacillus paranthracis`, `gtdb_grounding_status: UNRESOLVED`).
- `CommunityMech:000551`: `Bacillus licheniformis A3` (`NCBITaxon:1402` `Bacillus licheniformis`, `GTDB:s__Bacillus_licheniformis`, `gtdb_grounding_status: GROUNDED`, `is_reclassified: false`).
- `CommunityMech:000552`: `Pelagerythrobacter sp. N7` (`NCBITaxon:2800685` `Pelagerythrobacter`, `gtdb_grounding_status: UNRESOLVED`).
- `CommunityMech:000553`: `Salinicola sp. A11` (`NCBITaxon:404432` `Salinicola`, `gtdb_grounding_status: UNRESOLVED`).
- `CommunityMech:000554`: `Rhizorhabdus wittichii YL-JM2C` (`NCBITaxon:160791` `Rhizorhabdus wittichii`, `gtdb_grounding_status: UNRESOLVED`).
- `CommunityMech:000555`: `Cupriavidus necator JMP134` (`NCBITaxon:264198` `Cupriavidus pinatubonensis JMP134`, `gtdb_grounding_status: UNRESOLVED`).

## 4. Source-Limited Gaps and Representation / Writer Blockers

1. **Batch 147 Source-Limited Boundaries**:
   - **PAH-degrading `Bacillus` isolate baselines (`CommunityMech:000549`, `000550`, `000551`, `PMID:42587276` / `PMC13548369`)**: Each axenic isolate baseline contains a single `COMMUNITY_LEVEL` node with `0` `downstream` edges because `PMID:42587276` characterizes single-strain phenanthrene/pyrene degradation, bioemulsifier production, and biofilm formation without multi-step intraspecific ecological causal chains. Unresolved enzymatic/signaling boundaries—identifying the specific ring-hydroxylating dioxygenase and cytochrome P450 monooxygenase gene clusters in `Bacillus paramycoides B8-1` (`b81_pah_dioxygenase_and_p450_gene_cluster_identity`), the quorum-sensing or secreted matrix signals by which `Bacillus paranthracis A1` (`a1_biofilm_induction_signal_molecule_identity`) and `Bacillus licheniformis A3` (`a3_synergistic_biofilm_and_pyrene_cooxidation_mechanism`) stimulate consortium biofilm formation and unlock pyrene co-oxidation—are preserved in `KNOWLEDGE_GAP` discussions. Multi-species cooperative PAH degradation belongs on the `A1 + A3 + B8-1` synthetic consortium record (`CommunityMech:000501`).
   - **Halophilic pyrene-degrading isolate baselines (`CommunityMech:000552`, `000553`, `PMID:42666409` / `PMC13554761`)**: Each axenic halophilic isolate baseline contains a single `COMMUNITY_LEVEL` node with `0` `downstream` edges. Unresolved molecular boundaries—determining why axenic `Pelagerythrobacter sp. N7` exhibits low decarboxylase activity and accumulates upstream ring-cleavage intermediates (`n7_axenic_decarboxylase_bottleneck_and_intermediate_accumulation`) and characterizing the chemical structure of the glycolipid/lipopeptide bioemulsifier secreted by `Salinicola sp. A11` (`a11_bioemulsifier_chemical_structure_and_phthalate_transporters`)—are preserved in `KNOWLEDGE_GAP` discussions. Interspecies bioemulsifier facilitation and phthalate-pathway cross-feeding belong on the halophilic `N7 + A11` coculture record (`CommunityMech:000502`).
   - **BDE-47 and `2,4-DBP` cooperative degradation isolate baselines (`CommunityMech:000554`, `000555`, `PMID:42364169` / `PMC13506996`)**: Each axenic isolate baseline contains a single `COMMUNITY_LEVEL` node with `0` `downstream` edges. Unresolved biochemical boundaries—establishing the molecular mechanism by which accumulating `2,4-DBP` (`>= 1 mg/L`) inhibits `Rhizorhabdus wittichii YL-JM2C` growth and Rieske dioxygenase activity (`yljm2c_24dbp_feedback_inhibition_and_export_mechanism`) and determining why `Cupriavidus necator JMP134` cannot oxidatively cleave diphenyl ether bonds in parent `BDE-47` (`jmp134_lack_of_diphenyl_ether_dioxygenase_for_bde47`)—are preserved in `KNOWLEDGE_GAP` discussions. Detoxification cross-feeding and `TfdB`-mediated `2,4-DBP` removal belong on the `YL-JM2C + JMP134` synthetic consortium record (`CommunityMech:000503`).
2. **Corpus-Wide `needs_research` Cohort (`54` Records)**:
   - `54` community records in `kb/communities/` remain in `needs_research` status (`9` without interaction nodes and `45` where committed `references_cache/` sources are abstract-only or lack multi-step experimental perturbation evidence; `1` reviewed record `CommunityMech:000390` also has `0` nodes). In compliance with Stage 2 instructions, no unsupported nodes or `downstream` edges were invented.
3. **Representation & Writer Blockers (`0` Active Blockers)**:
   - `InteractionDownstream` in `src/communitymech/schema/communitymech.yaml` has `target` and `description` attributes (`communitymech-infra-0001` formalized the two-tier edge-provenance contract where parent `EcologicalInteraction.evidence` holds verbatim `EvidenceItem` citations and `reports/causal_graph_review/decisions/*.yaml` records `edges_after` and `retained_edge_decisions`).
   - `CommonTaxon` (`kb/taxa/Geobacter_sulfurreducens.yaml` and `kb/taxa/Shewanella_oneidensis_MR1.yaml`) represents reusable taxon/gene reference records (`role_genes` + UniProt protein evidence) rather than community-specific causal graphs.
