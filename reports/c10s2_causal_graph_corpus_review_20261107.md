# Cycle 10 Stage 2 Causal-Graph Corpus Review Report (2026-11-07)

## 1. Corpus Accounting

- **Base revision**: `7be226bc89c074c3697efa78344f2180067f53d8` (`main` after Cycle 10 Stage 1 PR `#2718`).
- **Total YAML records in repository**: **521**
  - `kb/communities/`: **507** `MicrobialCommunity` records
  - `data/isolates/`: **12** `MicrobialCommunity` records
  - `kb/taxa/`: **2** `CommonTaxon` records (`CommunityMech:taxon:000001` `Shewanella oneidensis MR-1`, `CommunityMech:taxon:000002` `Priestia megaterium`)
- **Causal-graph inventory (`reports/causal_graph_review/inventory.tsv` & `summary.json`)**:
  - Total `MicrobialCommunity` records indexed: **519**
  - `reviewed`: **465** (461 carried forward with verified SHA-256 hashes + 4 newly reviewed and enriched in Batch 142)
  - `needs_research`: **54** (source-limited records preserved unchanged without fabricated mechanisms or unsupported edges)
  - `pending`: **0**
  - `structural_defects`: **0** (`[]`)
  - Total interaction nodes across 519 `MicrobialCommunity` records: **1524**
  - Total directed `downstream` causal edges across 519 `MicrobialCommunity` records: **590**
  - Records without interaction nodes: **10** (source-limited observational/descriptive records)
  - Records without directed downstream edges: **214**

## 2. Batch 142 Curation Summary (`reports/causal_graph_review/decisions/20261107-stage2-four-records-batch142.yaml`)

| ID | Path | Pre-Stage-2 SHA-256 | Post-Stage-2 SHA-256 | Nodes | Directed Edges | Interaction Quotations (Before -> After) | Discussion Quotations | Primary Source |
|---|---|---|---|---:|---:|---:|---:|---|
| `CommunityMech:000522` | `kb/communities/Parmigiano_NWS_Set3_LAB_Triculture.yaml` | `dcf0f2e6fa847d81087feaa1fc8a9a41afcc025aba724cc917f92700713419aa` | `178f803afb7a8bef72f1f34a3eabefc751cc4095c11b6b28d1bf736ee7af6749` | 4 | 0 | 9 -> 13 | 1 | `PMID:41859451` (`PMC12996222`, `doi:10.3389/fmicb.2026.1755652`) |
| `CommunityMech:000523` | `kb/communities/SO2_BS1_Lithium_Battery_Bioleaching_Consortium.yaml` | `1f735d624a000f65d1d5b63d8259522e4570e927f1fcafc5943163402aecf370` | `e38b8362a648604964f05d027f8c39b0e44061013075a51d015cc67b87dc0dc7` | 2 | 1 | 5 -> 7 | 1 | `PMID:42733304` (`PMC13572860`, `doi:10.1002/advs.77699`) |
| `CommunityMech:000524` | `data/isolates/Shewanella_Oneidensis_SO1_NCM_Bioleaching_Isolate_Baseline.yaml` | `ec17e90c148403022202771f3d7ed933ef82714145b76b2c909f39e4ace4aa7e` | `20377604ffca85327b78dc52ddcd6e2caadfd329b223ab10287594f568627297` | 2 | 0 | 3 -> 6 | 1 | `PMID:42733304` (`PMC13572860`, `doi:10.1002/advs.77699`) |
| `CommunityMech:000525` | `data/isolates/Bacillus_Subtilis_BS1_Brewing_Wastewater_Isolate_Baseline.yaml` | `6fc667594cd8748bc8b6cdc554dc00bbba4bc117e6015e65429ec7fb1b5b9e35` | `bc97ca29591df15e69f5c06b5d83b5c9f11a9ba8f4a216dd6c3a4da79aaac07e` | 2 | 0 | 4 -> 7 | 1 | `PMID:42733304` (`PMC13572860`, `doi:10.1002/advs.77699`) |

## 3. Taxonomic Grounding & Source-Bounded Mechanism Representation

1. **`CommunityMech:000522` (`Parmigiano_NWS_Set3_LAB_Triculture.yaml`)**:
   - All 3 members (`Lactobacillus helveticus C001.15` -> `NCBITaxon:1587`, `Streptococcus thermophilus RBC06` -> `NCBITaxon:1308`, `Lactobacillus delbrueckii subsp. lactis C5I3` -> `NCBITaxon:29397`) are grounded at exact species/subspecies rank with GTDB classification (`GTDB:s__Lactobacillus_helveticus`, `GTDB:s__Streptococcus_thermophilus`, `GTDB:s__Lactobacillus_delbrueckii`).
   - All 4 `COMMUNITY_LEVEL` nodes (`Set 3 triculture milk acidification and total lactate enhancement`, `RBC06-containing pairwise acidification and lactate stimulation in Set 3`, `C001.15-C5I3 reduced acidification and D-lactate-majority pairwise subset`, and `Set 3 triculture balanced D-/L-lactate accumulation relative to C5I3 monoculture`) were enriched with 4 non-overlapping verbatim snippets from `PMID:41859451` (`PMC12996222`). Zero downstream edges are asserted because the study measured bulk milk pH kinetics (`umax`, `Delta pHmax`) and endpoint D-/L-lactate pools without quantifying exchanged metabolites or per-species CFU trajectories in mixed milk (`discussions[0]`: `nws_set3_d_lactate_non_significance_and_strain_combination_specificity`).
2. **`CommunityMech:000523` (`SO2_BS1_Lithium_Battery_Bioleaching_Consortium.yaml`)**:
   - Both engineered partners (`Shewanella oneidensis MR-1 SO2` -> `NCBITaxon:70863`, linked to `CommunityMech:taxon:000001`; `Bacillus subtilis 168 BS1` -> `NCBITaxon:1423`) are grounded at exact species rank with GTDB classification.
   - Enriched the 2-node, 1-edge `COMMUNITY_LEVEL` causal graph (`SO2 Ptac::ribADEHC Riboflavin Overproduction and BS1 Ethanol Detoxification -> SO2-BS1 Riboflavin-Accelerated NCM Metal Oxide Leaching and Late-Stage Rate Decline`) with 2 non-overlapping verbatim snippets from Section 2.3 of `PMID:42733304` (`PMC13572860`). Cell-surface attachment proportions and comet/ROS assays were not separately measured for the intermediate `SO2-BS1` consortium and are bounded in `discussions[0]` (`so2_bs1_surface_attachment_and_ni_co_toxicity_threshold`).
3. **`CommunityMech:000524` (`Shewanella_Oneidensis_SO1_NCM_Bioleaching_Isolate_Baseline.yaml`)**:
   - Single-strain electrogenic monoculture baseline (`Shewanella oneidensis MR-1 SO1` -> `NCBITaxon:70863`, linked to `CommunityMech:taxon:000001`).
   - Enriched the 2 `COMMUNITY_LEVEL` nodes (`Ethanol-Inhibited Extracellular Electron Transfer of S. oneidensis SO1 in Brewing Wastewater` and `Baseline Brewing-Wastewater NCM Cathode Metal Oxide Leaching by SO1 Monoculture`) from 3 to 6 non-overlapping verbatim snippets from Section 2.1 of `PMID:42733304`, preserving 0 downstream edges (`discussions[0]`: `so1_monoculture_ethanol_inhibition_mechanism`).
4. **`CommunityMech:000525` (`Bacillus_Subtilis_BS1_Brewing_Wastewater_Isolate_Baseline.yaml`)**:
   - Single-strain ethanol-detoxifying monoculture baseline (`Bacillus subtilis 168 BS1` -> `NCBITaxon:1423`).
   - Enriched the 2 `COMMUNITY_LEVEL` nodes (`Heterologous Adh-AldH Dual-Enzyme Oxidation of Brewing-Wastewater Ethanol by BS1` and `Minimal Standalone Electrogenic Power Density and NCM Metal Leaching by BS1 Monoculture`) from 4 to 7 non-overlapping verbatim snippets from Sections 2.1–2.2 of `PMID:42733304`, preserving 0 downstream edges (`discussions[0]`: `bs1_acetate_cross_feeding_versus_ethanol_detoxification`).
