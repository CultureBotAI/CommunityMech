# Cycle 11 Stage 2 Causal-Graph Corpus Review Report (2026-11-08)

## 1. Corpus Accounting

- **Base revision**: `c3f3870d3b94266858c89e18c229e41893c5495e` (`main` after Cycle 11 Stage 1 PR `#2728`).
- **Total YAML records in repository**: **526**
  - `kb/communities/`: **510** `MicrobialCommunity` records
  - `data/isolates/`: **14** `MicrobialCommunity` records
  - `kb/taxa/`: **2** `CommonTaxon` records (`CommunityMech:taxon:000001` `Shewanella oneidensis MR-1`, `CommunityMech:taxon:000002` `Priestia megaterium`)
- **Causal-graph inventory (`reports/causal_graph_review/inventory.tsv` & `summary.json`)**:
  - Total `MicrobialCommunity` records indexed: **524**
  - `reviewed`: **470** (465 carried forward with verified SHA-256 hashes + 5 newly reviewed and enriched in Batch 143)
  - `needs_research`: **54** (source-limited records preserved unchanged without fabricated mechanisms or unsupported edges)
  - `pending`: **0**
  - `structural_defects`: **0** (`[]`)
  - Total interaction nodes across 524 `MicrobialCommunity` records: **1533**
  - Total directed `downstream` causal edges across 524 `MicrobialCommunity` records: **593**
  - Records without interaction nodes: **10** (source-limited observational/descriptive records)
  - Records without directed downstream edges: **216**

## 2. Batch 143 Curation Summary (`reports/causal_graph_review/decisions/20261108-stage2-five-records-batch143.yaml`)

| ID | Path | Pre-Stage-2 SHA-256 | Post-Stage-2 SHA-256 | Nodes | Directed Edges | Interaction Quotations (Before -> After) | Discussion Quotations | Primary Source |
|---|---|---|---|---:|---:|---:|---:|---|
| `CommunityMech:000526` | `kb/communities/SO3_DeltaMtrC_BS3_Lithium_Battery_Bioleaching_Consortium.yaml` | `2f6bb5bb8629deb73c33dd19e057e61ba5893f97e562788c0e8609330ba5a4ee` | `8ce45b8ea2b6e7f966aecf7b30e8508aa427316ac92c53ab788e858a708ea968` | 2 | 1 | 5 -> 7 | 1 | `PMID:42733304` (`PMC13572860`, `doi:10.1002/advs.77699`) |
| `CommunityMech:000527` | `kb/communities/SO3_DeltaOmcA_BS3_Lithium_Battery_Bioleaching_Consortium.yaml` | `26a8290f4cf7bfd217c45b3ca599a5b5d0dfcf89c4a8204b17e8a53cad9008a3` | `568d6b743edb421494036d68981dfb3c6a812d24992119d49f802fee5400aba7` | 2 | 1 | 5 -> 7 | 1 | `PMID:42733304` (`PMC13572860`, `doi:10.1002/advs.77699`) |
| `CommunityMech:000528` | `kb/communities/SO3_DeltaMtrC_DeltaOmcA_BS3_Lithium_Battery_Bioleaching_Consortium.yaml` | `e1207bef98d13ee304a806d784ad308333a36a39ff3c9d8098f4c21ded905b26` | `c83966d6d3c59f5aa614dfe035ae3dc483531e2da8e08d4f886b11fa77984f43` | 2 | 1 | 5 -> 7 | 1 | `PMID:42733304` (`PMC13572860`, `doi:10.1002/advs.77699`) |
| `CommunityMech:000529` | `data/isolates/Bacillus_Subtilis_BS3_Brewing_Wastewater_Isolate_Baseline.yaml` | `0f30458127b3b8c83fae13e6a27028aa84589af27e5941d4eb3338e128085880` | `42834ab5f80c67edd88527a323dfa94514b440d63891e4fd88790b50a230cf28` | 2 | 0 | 4 -> 7 | 1 | `PMID:42733304` (`PMC13572860`, `doi:10.1002/advs.77699`) |
| `CommunityMech:000530` | `data/isolates/Bacillus_Subtilis_BS0_Brewing_Wastewater_Isolate_Baseline.yaml` | `b060b7eabef4b87d2625e38eb9473b3924402bf09da997b2c16076b1e32b7d09` | `452de842b34bb5c9073f31331ddef8f120323f5a934257e9a9db1e5e8f043f43` | 1 | 0 | 2 -> 4 | 1 | `PMID:42733304` (`PMC13572860`, `doi:10.1002/advs.77699`) |

## 3. Taxonomic Grounding & Source-Bounded Mechanism Representation

1. **`CommunityMech:000526` (`SO3_DeltaMtrC_BS3_Lithium_Battery_Bioleaching_Consortium.yaml`)**:
   - Both engineered partners (`Shewanella oneidensis MR-1 SO3ΔmtrC` -> `NCBITaxon:70863`, linked to `CommunityMech:taxon:000001`; `Bacillus subtilis 168 BS3` -> `NCBITaxon:1423`) are grounded at exact species rank with GTDB classification.
   - Enriched the 2-node, 1-edge `COMMUNITY_LEVEL` causal graph (`Ethanol Removal and Riboflavin Shuttle Provision by Bacillus subtilis BS3 -> MtrC-Deficient Extracellular Electron Transfer and Attenuated Cathode Bioleaching by Shewanella oneidensis SO3ΔmtrC`) from 5 to 7 non-overlapping verbatim snippets from `PMID:42733304` (`PMC13572860`). Per-metal (Li, Ni, Co, Mn) dissolved concentrations and NCM surface colonization fractions were not separately reported for the `SO3ΔmtrC-BS3` mutant consortium and are bounded in `discussions[0]` (`000526_cytochrome_partition_and_elemental_breakdown`).
2. **`CommunityMech:000527` (`SO3_DeltaOmcA_BS3_Lithium_Battery_Bioleaching_Consortium.yaml`)**:
   - Both engineered partners (`Shewanella oneidensis MR-1 SO3ΔomcA` -> `NCBITaxon:70863`, linked to `CommunityMech:taxon:000001`; `Bacillus subtilis 168 BS3` -> `NCBITaxon:1423`) are grounded at exact species rank with GTDB classification.
   - Enriched the 2-node, 1-edge `COMMUNITY_LEVEL` causal graph (`Ethanol Removal and Riboflavin Shuttle Provision by Bacillus subtilis BS3 -> OmcA-Deficient Extracellular Electron Transfer and Attenuated Cathode Bioleaching by Shewanella oneidensis SO3ΔomcA`) from 5 to 7 non-overlapping verbatim snippets from `PMID:42733304` (`PMC13572860`). Per-metal leached concentrations and relative direct-vs-riboflavin electron flux through remaining MtrC conduits are bounded in `discussions[0]` (`000527_cytochrome_partition_and_elemental_breakdown`).
3. **`CommunityMech:000528` (`SO3_DeltaMtrC_DeltaOmcA_BS3_Lithium_Battery_Bioleaching_Consortium.yaml`)**:
   - Both engineered partners (`Shewanella oneidensis MR-1 SO3ΔmtrCΔomcA` -> `NCBITaxon:70863`, linked to `CommunityMech:taxon:000001`; `Bacillus subtilis 168 BS3` -> `NCBITaxon:1423`) are grounded at exact species rank with GTDB classification.
   - Enriched the 2-node, 1-edge `COMMUNITY_LEVEL` causal graph (`Ethanol Removal and Riboflavin Shuttle Provision by Bacillus subtilis BS3 -> MtrC/OmcA-Abrogated Extracellular Electron Transfer and Residual Background Cathode Leaching by Shewanella oneidensis SO3ΔmtrCΔomcA`) from 5 to 7 non-overlapping verbatim snippets from `PMID:42733304` (`PMC13572860`). The uncharacterized non-MtrC/OmcA pathway responsible for the residual 28.39 mW m^-2 MFC anodic power density despite zero net NCM leaching above sole BS3 (13.4 mg L^-1) is bounded in `discussions[0]` (`000528_cytochrome_partition_and_elemental_breakdown`).
4. **`CommunityMech:000529` (`Bacillus_Subtilis_BS3_Brewing_Wastewater_Isolate_Baseline.yaml`)**:
   - Single-strain engineered monoculture baseline (`Bacillus subtilis 168 BS3` -> `NCBITaxon:1423`).
   - Enriched the 2 `COMMUNITY_LEVEL` nodes (`IrrE-Mediated Reactive Oxygen Species Scavenging and DNA Repair Under Nickel and Cobalt Stress` and `Sole-Strain BS3 Monoculture NCM Metal Oxide Leaching Baseline`) from 4 to 7 non-overlapping verbatim snippets from `PMID:42733304`, preserving 0 downstream edges because the synthetic-medium Ni2+/Co2+ challenge and 14-day brewing-wastewater NCM leaching control were independent assays (`discussions[0]`: `bs3_standalone_leaching_increment_over_bs1`).
5. **`CommunityMech:000530` (`Bacillus_Subtilis_BS0_Brewing_Wastewater_Isolate_Baseline.yaml`)**:
   - Single-strain empty-vector monoculture baseline (`Bacillus subtilis 168 BS0` -> `NCBITaxon:1423`).
   - Enriched the single `COMMUNITY_LEVEL` node (`Basal Endogenous Ethanol Oxidation and Growth in Brewing Wastewater`) from 2 to 4 non-overlapping verbatim snippets from `PMID:42733304`, preserving 0 downstream edges because BS0 was not assayed for standalone MFC power density or NCM leaching (`discussions[0]`: `bs0_unengineered_consortium_leaching_omission`).
