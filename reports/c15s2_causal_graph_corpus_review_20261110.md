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

The 7 isolate baseline records added in Cycle 15 Stage 1 (`PR #2758`, commit `ed7f2fc5932885879416d178711744243835c536`) entered Stage 2 in `pending` status and were reviewed against their committed full-text primary sources (`references_cache/PMID_42587276.txt` / `PMC13471667`, `references_cache/PMID_42666409.txt` / `PMC13522185`, and `references_cache/PMID_42364169.txt` / `PMC13440307`), enriched via `write_validated_community` + `record_curation_event(action="CURATE_CAUSAL_GRAPH")`, recorded in `reports/causal_graph_review/decisions/20261110-stage2-seven-records-batch147.yaml`, and logged in append-only `history/records/` sidecars:

| ID | Path | Primary Source | Nodes | `downstream` Edges | Interaction `EvidenceItem` Snippets (Before -> After) | Pre-Stage-2 `original_sha256` -> Post-Stage-2 `record_sha256` |
|---|---|---|---:|---:|---|---|
| `CommunityMech:000549` | `data/isolates/Bacillus_Paramycoides_B81_PAH_Biodegradation_Isolate_Baseline.yaml` | `PMID:42587276` (`PMC13471667`) | 1 (`COMMUNITY_LEVEL`) | 0 | `3 -> 5` (`+2` verbatim snippets on the 37 °C phenanthrene optimum `77.94%` and B8-1's highest phenanthrene degrading capacity relative to all four multi-strain consortia) | `a1862a927c0c...` -> `cb226c9c70b14d042991de11ef4a7b3677790ffd8a93549332e213dc4946b04e` |
| `CommunityMech:000550` | `data/isolates/Bacillus_Paranthracis_A1_PAH_Biofilm_Isolate_Baseline.yaml` | `PMID:42587276` (`PMC13471667`) | 1 (`COMMUNITY_LEVEL`) | 0 | `3 -> 5` (`+2` verbatim snippets on >2-fold biofilm naphthalene degradation enhancement and 48-h flask-wall biofilm formation for soil microcosm experiments) | `00fd3bda9890...` -> `3b4fa9c9579fe2f3c0b94f2c1c55ec6b8f36bb5e22d4c5f9718aeb798cc15988` |
| `CommunityMech:000551` | `data/isolates/Bacillus_Licheniformis_A3_PAH_Biofilm_Isolate_Baseline.yaml` | `PMID:42587276` (`PMC13471667`) | 1 (`COMMUNITY_LEVEL`) | 0 | `2 -> 5` (`+3` verbatim snippets on 7-day planktonic phenanthrene `28.40%` and naphthalene `38.92%` screening rates, biofilm degradation increases, and glass-surface biofilm formation) | `41dbfbc369e4...` -> `de118e18969d2bfaddac33e51e49d5481ec224427441cf90d1faa5c18438d73b` |
| `CommunityMech:000552` | `data/isolates/Pelagerythrobacter_N7_Halophilic_Pyrene_Oxidation_Isolate_Baseline.yaml` | `PMID:42666409` (`PMC13522185`) | 1 (`COMMUNITY_LEVEL`) | 0 | `3 -> 5` (`+2` verbatim snippets from Section 3.3 on GC–MS intermediates at `40.25 min` and `38.10 min` and Section 3.7 on `pahA`/`pahB`/`pahC` conversion of pyrene to 4,5-dicarboxyphenanthrene) | `114c68f88dd9...` -> `16d14ed3792a286afedaa4f17ba1c1773ebb04c6a7e8fc622cb7d946ce4c9610` |
| `CommunityMech:000553` | `data/isolates/Salinicola_A11_Halophilic_Bioemulsifier_Decarboxylase_Isolate_Baseline.yaml` | `PMID:42666409` (`PMC13522185`) | 1 (`COMMUNITY_LEVEL`) | 0 | `3 -> 5` (`+2` verbatim snippets from Section 3.5 on Emulsan-like glycoprotein FTIR absorption bands at `3419.9`, `1128.4`, `2924.3`, `2854.7`, and `1631.1 cm−1` and Section 3.4 on the `His109`–`His111`–`His172` catalytic triad) | `a23fb3d2c224...` -> `82b65eee0a1216e8a26c875a17206c3060b2304223a3eac2fcb1171de79aee4b` |
| `CommunityMech:000554` | `data/isolates/Rhizorhabdus_Wittichii_YL_JM2C_BDE47_Dioxygenase_Isolate_Baseline.yaml` | `PMID:42364169` (`PMC13440307`) | 1 (`COMMUNITY_LEVEL`) | 0 | `3 -> 5` (`+2` verbatim snippets on stoichiometric `2,4-DBP` formation via diphenyl ether cleavage in `Fig. 1c` and recombinant `E. coli BL21(DE3)/pET-tcsAaAb` conversion of BDE-47 to `2,4-DBP` and `3,5-DBC` in `Fig. S3`) | `f1dc3f787b96...` -> `e70a8434bd8db3852302899814f08a19d97c0e9d73a6636cb7715295642fdf59` |
| `CommunityMech:000555` | `data/isolates/Cupriavidus_Necator_JMP134_24DBP_Hydroxylase_Isolate_Baseline.yaml` | `PMID:42364169` (`PMC13440307`) | 1 (`COMMUNITY_LEVEL`) | 0 | `2 -> 5` (`+3` verbatim snippets on `BL21-TfdBI`/`BL21-TfdBII` whole-cell biotransformation of `2,4-DBP` to `3,5-DBC` in `Fig. S8`, downstream `tcsCDEF`/`tfdCDEF` clusters, and `TfdB` funneling of `2,4-DBP` into the `3,5-DBC` pathway) | `c97c0c57afa5...` -> `429964cbf945c41b2e89b57a072718158cf674e03786ef34b1ef96fe9247995e` |

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
   - **PAH-degrading `Bacillus` isolate baselines (`CommunityMech:000549`, `000550`, `000551`, `PMID:42587276` / `PMC13471667`)**: Each axenic isolate baseline contains a single `COMMUNITY_LEVEL` node with `0` `downstream` edges because `PMID:42587276` characterizes single-strain planktonic and biofilm phenanthrene and naphthalene removal without multi-step intraspecific ecological causal chains. Unresolved evidence boundaries—the omitted inline numeric percentage for B8-1 biofilm naphthalene degradation in Figure 8b (`b81_biofilm_naphthalene_numeric_value`) and unmapped individual 16S rRNA GenBank accessions `PV848451`, `PV848453`, and `PV848454` across isolates (`a1_genbank_accession_assignment`, `a3_genbank_accession_assignment`)—are preserved in `KNOWLEDGE_GAP` discussions. Multi-strain PAH interactions belong on Consortia 1–4 (`CommunityMech:000502`, `CommunityMech:000503`, `CommunityMech:000358`, `CommunityMech:000504`).
   - **Halophilic pyrene-degrading isolate baselines (`CommunityMech:000552`, `000553`, `PMID:42666409` / `PMC13522185`)**: Each axenic halophilic isolate baseline contains a single `COMMUNITY_LEVEL` node with `0` `downstream` edges. Unresolved metabolic boundaries—why downstream phenanthrene/salicylate ring-cleavage genes (`pahA`/`pahB`, `G12O`, `C12O`) in `Pelagerythrobacter sp. N7` remain unexpressed or arrested at `4,5-dicarboxyphenanthrene` in axenic culture (`n7_downstream_pathway_expression_without_a11`) and whether axenic `Salinicola sp. A11` can decarboxylate and grow on purified exogenous `4,5-dicarboxyphenanthrene` via candidate `HphtC-5` (`a11_axenic_45dcp_growth_and_decarboxylation`)—are preserved in `KNOWLEDGE_GAP` discussions. Interspecies Emulsan-like bioemulsifier facilitation and `4,5-dicarboxyphenanthrene` cross-feeding belong on the two-member PES consortium record (`CommunityMech:000340`).
   - **BDE-47 and `2,4-DBP` cooperative degradation isolate baselines (`CommunityMech:000554`, `000555`, `PMID:42364169` / `PMC13440307`)**: Each axenic isolate baseline contains a single `COMMUNITY_LEVEL` node with `0` `downstream` edges. Unresolved biochemical boundaries—the active-site structural determinants explaining why `Rhizorhabdus wittichii YL-JM2C` flavin monooxygenase `RwTfdB` is active on `2-bromophenol` and `2-hydroxybiphenyl` but excludes `2,4-dibromophenol` (`yl_jm2c_rwtfdb_structural_determinants`) and the relative in vivo flux contributions of plasmid pJP4 paralogs `tfdBI` vs `tfdBII` during `2,4-DBP` growth by `Cupriavidus necator JMP134` (`jmp134_tfdbi_vs_tfdbii_in_vivo_contribution`)—are preserved in `KNOWLEDGE_GAP` discussions. Diffusible `2,4-DBP` cross-feeding and `TfdBI`/`TfdBII`-mediated metabolic relay belong on the `YL-JM2C + JMP134` synthetic consortium record (`CommunityMech:000388`).
2. **Corpus-Wide `needs_research` Cohort (`54` Records)**:
   - `54` community records in `kb/communities/` remain in `needs_research` status (`9` without interaction nodes and `45` where committed `references_cache/` sources are abstract-only or lack multi-step experimental perturbation evidence; `1` reviewed record `CommunityMech:000390` also has `0` nodes). In compliance with Stage 2 instructions, no unsupported nodes or `downstream` edges were invented.
3. **Representation & Writer Blockers (`0` Active Blockers)**:
   - `InteractionDownstream` in `src/communitymech/schema/communitymech.yaml` has `target` and `description` attributes (`communitymech-infra-0001` formalized the two-tier edge-provenance contract where parent `EcologicalInteraction.evidence` holds verbatim `EvidenceItem` citations and `reports/causal_graph_review/decisions/*.yaml` records `edges_after` and `retained_edge_decisions`).
   - `CommonTaxon` (`kb/taxa/Geobacter_sulfurreducens.yaml` and `kb/taxa/Shewanella_oneidensis_MR1.yaml`) represents reusable taxon/gene reference records (`role_genes` + UniProt protein evidence) rather than community-specific causal graphs.
