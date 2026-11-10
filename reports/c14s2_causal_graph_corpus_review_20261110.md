# Cycle 14 Stage 2 (`causal_graphs`) Corpus Review and Curation Report (2026-11-10)

## 1. Corpus-Wide Inventory & Eligibility Audit

All **544** eligible YAML records across the three repository roots were audited for native ecological interaction and causal-graph representation during Cycle 14 Stage 2 (`mech-goal-sequence-20261019`):

| Corpus Root | Root Class | Record Count | Ecological Interaction Nodes | Directed `downstream` Edges | Review Disposition |
|---|---|---:|---:|---:|---|
| `kb/communities/*.yaml` | `MicrobialCommunity` | 512 | 1,522 | 594 | `458 reviewed`, `54 needs_research`, `0 pending`, `0 stale` |
| `data/isolates/*.yaml` | `MicrobialCommunity` | 30 | 30 | 0 | `30 reviewed`, `0 needs_research`, `0 pending`, `0 stale` |
| `kb/taxa/*.yaml` | `CommonTaxon` | 2 | 0 (no `ecological_interactions` slot on `CommonTaxon`) | 0 | `2 reviewed` (`role_genes` + UniProt protein evidence verified) |
| **Total** | — | **544** | **1,552** | **594** | **`488 reviewed` (`MicrobialCommunity`) + `2 CommonTaxon`, `54 needs_research`, `0 pending`, `0 stale`, `0 structural_defects`** |

- **`reports/causal_graph_review/summary.json` invariants**:
  - `records`: `542` (`512` in `kb/communities/` + `30` in `data/isolates/`)
  - `nodes`: `1552`
  - `edges`: `594`
  - `records_without_nodes`: `10` (`9` in `needs_research` + `1` in `reviewed` (`CommunityMech:000390`))
  - `records_without_edges`: `233`
  - `review_status_counts`: `{"needs_research": 54, "reviewed": 488}` (`pending: 0`, `stale: 0`)
  - `structural_defects`: `[]`

## 2. Batch 146 Source-Based Curation (`CommunityMech:000542`–`CommunityMech:000548`)

The 7 isolate baseline records added in Cycle 14 Stage 1 (`PR #2751`, commit `9a936b784960156acd8963b71323ad338287a563`) entered Stage 2 in `pending` status and were reviewed against their committed full-text primary sources (`references_cache/PMID_42038008.txt` / `PMC13109302`, `references_cache/PMID_42655156.txt` / `PMC13515949`, and `references_cache/PMID_42478817.txt` / `PMC13488302`), enriched via `write_validated_community` + `record_curation_event(action="CURATE_CAUSAL_GRAPH")`, recorded in `reports/causal_graph_review/decisions/20261110-stage2-seven-records-batch146.yaml`, and logged in append-only `history/records/` sidecars:

| ID | Path | Primary Source | Nodes | `downstream` Edges | Interaction `EvidenceItem` Snippets (Before -> After) | Pre-Stage-2 `original_sha256` -> Post-Stage-2 `record_sha256` |
|---|---|---|---:|---:|---|---|
| `CommunityMech:000542` | `data/isolates/Escherichia_Coli_GL10_Glucose_D_Lactate_Isolate_Baseline.yaml` | `PMID:42038008` (`PMC13109302`) | 1 (`COMMUNITY_LEVEL`) | 0 | `4 -> 6` (`+2` verbatim snippets from Section 3.3.1 / Fig. 5A and Fig. S7–S8) | `12e55314ccdf...` -> `a747c09cf287a252aa4e8fc66485fd6aa337d320cb7903c8a92d101a44855dc0` |
| `CommunityMech:000543` | `data/isolates/Escherichia_Coli_XL12_Xylose_D_Lactate_Isolate_Baseline.yaml` | `PMID:42038008` (`PMC13109302`) | 1 (`COMMUNITY_LEVEL`) | 0 | `4 -> 6` (`+2` verbatim snippets from Section 3.2.2 / Fig. 3A and Fig. S4–S5) | `f5573eb7c8d6...` -> `c19c097c6068fa07ecdd2e9533d2d6a2225637a5a594ff14b21ef3a86f6d2e9f` |
| `CommunityMech:000544` | `data/isolates/Escherichia_Coli_XL5_PTS_Deficient_D_Lactate_Isolate_Baseline.yaml` | `PMID:42038008` (`PMC13109302`) | 1 (`COMMUNITY_LEVEL`) | 0 | `4 -> 6` (`+2` verbatim snippets from Section 3.2.1) | `2c8b31a3d82c...` -> `4105ae978347925a7541a5bd66f6ceadc35bd4bda35683f70bffca35b36ab79f` |
| `CommunityMech:000545` | `data/isolates/Bifidobacterium_Bifidum_JCM1254_2FL_FOS_Monoculture_Baseline.yaml` | `PMID:42655156` (`PMC13515949`) | 1 (`COMMUNITY_LEVEL`) | 0 | `3 -> 5` (`+2` verbatim snippets from Section 4 Discussion and Section 2.2) | `188b2c8b4444...` -> `8190e352c3a803e85e2ab6b64a1791a6f14b2ea93dab2173c1ef653ea9e0a216` |
| `CommunityMech:000546` | `data/isolates/Faecalibacterium_Prausnitzii_A2_165_2FL_FOS_Monoculture_Baseline.yaml` | `PMID:42655156` (`PMC13515949`) | 1 (`COMMUNITY_LEVEL`) | 0 | `3 -> 5` (`+2` verbatim snippets from Section 3.1 and Section 4 Discussion) | `7a4f13515e39...` -> `b6dc768bf6f705611933fc50882d91957225ef1e32c61330e1adb717fe175790` |
| `CommunityMech:000547` | `data/isolates/Ramichloridium_Apiculatum_CMS1_Wollastonite_Bioleaching_Isolate_Baseline.yaml` | `PMID:42478817` (`PMC13488302`) | 1 (`COMMUNITY_LEVEL`) | 0 | `4 -> 6` (`+2` verbatim snippets from RESULTS AND DISCUSSION on L-glutamic acid and Si4+ R-COO− complexation) | `3335d6f85de2...` -> `d772c9002f1af1474616567beadbdd148c9724daf6e910b5a242621d04cc1f30` |
| `CommunityMech:000548` | `data/isolates/Talaromyces_Pseudofuniculosus_Hzt3_Wollastonite_Bioleaching_Isolate_Baseline.yaml` | `PMID:42478817` (`PMC13488302`) | 1 (`COMMUNITY_LEVEL`) | 0 | `3 -> 6` (`+3` verbatim snippets from RESULTS AND DISCUSSION on pH acidification, days 0–2 sucrose consumption, and 1,428 cm−1 carbonate FT-IR band removal) | `e669bcf94e26...` -> `5963957669bdfef206891e57c3b354d0ef934edb13e840651edd73f113d3d900` |

## 3. Taxonomic Grounding Verification Across Causal-Graph Elements

In accordance with `.claude/skills/ground-causal-graph-taxa/SKILL.md`, every taxon in `taxonomy` and `ecological_interactions[].participating_taxa` across Batch 146 was verified for exact string and `NCBITaxon` match plus GTDB grounding:

- `CommunityMech:000542`: `Escherichia coli GL10` (`NCBITaxon:562` `Escherichia coli`, `GTDB:s__Escherichia_coli`, `gtdb_grounding_status: GROUNDED`, `is_reclassified: false`).
- `CommunityMech:000543`: `Escherichia coli XL12` (`NCBITaxon:562` `Escherichia coli`, `GTDB:s__Escherichia_coli`, `gtdb_grounding_status: GROUNDED`, `is_reclassified: false`).
- `CommunityMech:000544`: `Escherichia coli XL5` (`NCBITaxon:562` `Escherichia coli`, `GTDB:s__Escherichia_coli`, `gtdb_grounding_status: GROUNDED`, `is_reclassified: false`).
- `CommunityMech:000545`: `Bifidobacterium bifidum JCM1254` (`NCBITaxon:1681` `Bifidobacterium bifidum`, `GTDB:s__Bifidobacterium_bifidum`, `gtdb_grounding_status: GROUNDED`, `is_reclassified: false`).
- `CommunityMech:000546`: `Faecalibacterium prausnitzii A2-165` (`NCBITaxon:853` `Faecalibacterium prausnitzii`, `gtdb_grounding_status: UNRESOLVED`).
- `CommunityMech:000547`: `Ramichloridium apiculatum CMS-1` (`NCBITaxon:470080` `Ramichloridium apiculatum`, `gtdb_grounding_status: NO_GTDB_EQUIVALENT`).
- `CommunityMech:000548`: `Talaromyces pseudofuniculosus hzt-3′` (`NCBITaxon:2015341` `Talaromyces pseudofuniculosus`, `gtdb_grounding_status: NO_GTDB_EQUIVALENT`).

## 4. Source-Limited Gaps and Representation / Writer Blockers

1. **Batch 146 Source-Limited Boundaries**:
   - **Glucose/xylose D-lactate engineered `E. coli` isolate baselines (`CommunityMech:000542`, `000543`, `000544`, `PMID:42038008` / `PMC13109302`)**: Each axenic isolate baseline contains a single `COMMUNITY_LEVEL` fermentation node with `0` `downstream` edges because `PMID:42038008` characterizes single-strain sugar utilization and D-lactate synthesis without multi-step intraspecific ecological causal chains. Unresolved intracellular flux questions—why `E. coli GL10` (`Δpps ΔpoxB ΔpflB Δpta ΔfrdABC ΔadhE Δdld ΔmgsA`) yields only `0.64 g/L` D-lactate on sole xylose despite wild-type growth and xylose consumption kinetics (`gl10_xylose_d_lactate_conversion_bottleneck`), which alternative hexose transporters (`GalP`/`Mgl`) and non-`FrdABC` pathways sustain residual glucose uptake and `0.72 g/L` succinate leak in `E. coli XL12` (`Δglk ΔptsI Δpps ΔpoxB ΔpflB Δpta ΔfrdABC ΔadhE Δdld ΔmgsA`, `xl12_residual_glucose_uptake_and_succinate_leak`), and why deleting `pta`, `frdABC`, `adhE`, `dld`, and `mgsA` in intermediate strain `E. coli XL5` (`Δglk ΔptsI Δpps ΔpoxB ΔpflB`) inverted single-sugar D-lactate yields between glucose and xylose (`xl5_to_xl12_glucose_lactate_switch_mechanism`)—are preserved in `KNOWLEDGE_GAP` discussions. Parallel glucose+xylose co-fermentation belongs on the `GL10` + `XL12` synthetic consortium record (`CommunityMech:000357`).
   - **2′-FL and FOS axenic monoculture baselines (`CommunityMech:000545`, `000546`, `PMID:42655156` / `PMC13515949`)**: Each axenic monoculture baseline contains a single `COMMUNITY_LEVEL` carbohydrate-fermentation node with `0` `downstream` edges. Unresolved metabolic boundaries—how much liberated L-fucose or 1,2-propanediol accumulates alongside lactate and acetate in `B. bifidum JCM1254` monoculture (`bbifidum_jcm1254_fucose_and_12propanediol_fate`) and how endogenous acetyl-CoA is cycled to butyrate in `F. prausnitzii A2-165` monoculture on FOS in VFA-free `YCFA−` medium without exogenous acetate (`fprausnitzii_a2165_butyrate_without_exogenous_acetate_in_ycfa_minus`)—are preserved in `KNOWLEDGE_GAP` discussions. Interspecies cross-feeding and FOS competition belong on the `B. bifidum` + `F. prausnitzii` coculture record (`CommunityMech:000401`).
   - **Wollastonite-weathering fungal isolate baselines (`CommunityMech:000547`, `000548`, `PMID:42478817` / `PMC13488302`)**: Each axenic fungal isolate baseline contains a single `COMMUNITY_LEVEL` mineral-bioleaching node with `0` `downstream` edges. Unresolved analytical boundaries—reconciling the `2.65%` (Abstract) vs `2.46%` (Results) `Ca2+` leaching efficiency reported for `100% CMS-1` (`cms1_abstract_vs_results_ca_leaching_discrepancy`) and quantifying how much leached `Ca2+` and soluble oxalate are sequestered into secondary weddellite (`PDF#17-0541`) in the `100% hzt-3′` residue (`hzt3_weddellite_precipitation_vs_soluble_oxalate_depletion`)—are preserved in `KNOWLEDGE_GAP` discussions. Synergistic co-cultivation weathering belongs on the `20% CMS-1 + 80% hzt-3′` mixed fungal consortium record (`CommunityMech:000404`).
2. **Corpus-Wide `needs_research` Cohort (`54` Records)**:
   - `54` community records in `kb/communities/` remain in `needs_research` status (`9` without interaction nodes and `45` where committed `references_cache/` sources are abstract-only or lack multi-step experimental perturbation evidence; `1` reviewed record `CommunityMech:000390` also has `0` nodes). In compliance with Stage 2 instructions, no unsupported nodes or `downstream` edges were invented.
3. **Representation & Writer Blockers (`0` Active Blockers)**:
   - `InteractionDownstream` in `src/communitymech/schema/communitymech.yaml` has `target` and `description` attributes (`communitymech-infra-0001` formalized the two-tier edge-provenance contract where parent `EcologicalInteraction.evidence` holds verbatim `EvidenceItem` citations and `reports/causal_graph_review/decisions/*.yaml` records `edges_after` and `retained_edge_decisions`).
   - `CommonTaxon` (`kb/taxa/Geobacter_sulfurreducens.yaml` and `kb/taxa/Shewanella_oneidensis_MR1.yaml`) represents reusable taxon/gene reference records (`role_genes` + UniProt protein evidence) rather than community-specific causal graphs.
