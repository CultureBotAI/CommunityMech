# Cycle 3 Stage 2 (`causal_graphs`) Corpus Review & Curation Report (2026-10-25)

## 1. Scope & Workflow Context
- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle / Stage**: Cycle 3, Stage 2 (`causal_graphs` — Curation of Causal Graphs)
- **Repository**: `CultureBotAI/CommunityMech`
- **Base Commit**: `bce50b6f793bf1a600dcf60b444e14e5b478f9c0` (`main` after Cycle 3 Stage 1 PR `#2077`)
- **Eligible Corpus**:
  - `381` community records in `kb/communities/*.yaml`
  - `108` isolate records in `data/isolates/*.yaml`
  - `2` shared taxon records in `kb/taxa/*.yaml` (`kb/taxa/Shewanella_oneidensis_MR1.yaml` `NCBITaxon:211586`, `kb/taxa/Geobacter_sulfurreducens.yaml` `NCBITaxon:35554`)
  - **Total `MicrobialCommunity` records**: `489`

## 2. Corpus-Wide SHA-256 Census & Review Status
Every record in `kb/communities/*.yaml` and `data/isolates/*.yaml` was audited against `reports/causal_graph_review/inventory.tsv` and `reports/causal_graph_review/summary.json`:

| Cohort | Record Count | Pre-Stage-2 Status | Post-Stage-2 Status | Notes |
| --- | ---: | --- | --- | --- |
| Previously reviewed records (`000001`–`000490`, 484 files) | 430 | `reviewed` | `reviewed` | Zero SHA-256 drift since Cycle 2 Stage 2 / Stage 5 remediation (`bce50b6`). |
| Source-limited / awaiting paid full-text DRC (`000001`–`000490`) | 54 | `needs_research` | `needs_research` | Zero SHA-256 drift; zero new files for these 54 records in `references_cache/` or `reports/drc/`; paid Edison/PaperQA3 credits not spent per authorization policy. |
| Cycle 3 Stage 1 additions (`000491`–`000495`, Batch 135) | 5 | `pending` | `reviewed` | Curated in Batch 135 (`reports/causal_graph_review/decisions/20261025-stage2-five-records-batch135.yaml`) via guarded `record_curation_event` + `write_validated_community`. |
| **Total (`MicrobialCommunity`)** | **489** | **430 reviewed / 54 needs_research / 5 pending** | **435 reviewed / 54 needs_research / 0 pending** | **`1,459` nodes, `582` directed `downstream` causal edges, `0` structural defects.** |

## 3. Batch 135 Causal-Graph Curation (`CommunityMech:000491`–`000495`)

All five records added in Cycle 3 Stage 1 were reviewed end-to-end against their cached primary sources in `references_cache/` and updated via `record_curation_event` + `write_validated_community`:

1. **`CommunityMech:000491` — `kb/communities/TwoStep_PCB_Copper_Gold_Bioleaching_Consortium.yaml`** (`PMID:26704063`)
   - **Graph**: 3 nodes, 2 converging directed `downstream` causal edges (`First-Step Acidophilic Copper Bioleaching from Waste PCBs` $\to$ `Second-Step Alkaline Cyanogenic Gold Mobilization from Cu-Leached PCBs` and `Heterotrophic Glycine-Dependent Cyanide Lixiviant Biosynthesis` $\to$ `Second-Step Alkaline Cyanogenic Gold Mobilization from Cu-Leached PCBs`).
   - **Curation Updates**: Separated heterotrophic cyanide lixiviant biosynthesis (`Pseudomonas putida` strain WCS361 producing `21.5 +/- 1.5 mg/L` cyanide from `10 g/L` glycine with `Pseudomonas fluorescens`) from the alkaline gold mobilization step on Cu-leached PCB material (`44.0%` Au mobilized at `pH 7.3-8.6`, `30 degrees C`, `2 days`), removed redundant pairwise `target_taxon` slots on `COMMUNITY_LEVEL` nodes that already declare `participating_taxa`, and added verbatim `PMID:26704063` snippets on each upstream node backing its outgoing `downstream` causal edge. Readiness score increased from `85.0` to `100.0`.

2. **`CommunityMech:000492` — `data/isolates/Intrasporangium_Chromatireducens_Q5_1_Chromate_Reduction.yaml`** (`PMID:21441371`, `doi:10.1007/s11274-009-0047-x`)
   - **Graph**: 3 nodes, 2 directed `downstream` causal edges (`High-Tolerance Aerobic Chromate Reduction by Free Cells` $\to$ `Acetate-Stimulated Resting-Cell Chromate Reduction` $\to$ `Immobilized Compounding-Bead Chromate Bioremediation in Continuous Systems`).
   - **Curation Updates**: Expanded the 2-node single-species physiological causal graph (`scope: COMMUNITY_LEVEL`) into a 3-node, 2-edge chain distinguishing (1) high-tolerance aerobic growth-coupled `Cr(VI)` reduction (`>30 mmol/L` tolerance; complete reduction of `0.4 mmol/L Cr(VI)` in `72 h`), (2) `1 mmol/L` acetate-stimulated resting-cell `Cr(VI)` reduction (`doi:10.1007/s11274-009-0047-x`), and (3) immobilization of Q5-1 cells in compounding beads (`4% PVA, 3% sodium alginate, 1.5% active carbon, 3% diatomite`) for continuous-system wastewater treatment, with verbatim cached snippets on each upstream node directly supporting its outgoing `downstream` causal edge. Readiness score increased from `85.0` to `100.0`.

3. **`CommunityMech:000493` — `kb/communities/Magnetite_Thiobacillus_Sulfur_Cycle_Phenol_Chromate_Reactor.yaml`** (`doi:10.1016/j.cej.2020.124801`)
   - **Graph**: 3 nodes, 2 directed `downstream` causal edges (`Magnetite-Driven Thiobacillus Oxidation of Elemental Sulfur to Sulfate` $\to$ `Sulfur-Cycle-Coupled Anaerobic Phenol Degradation and Cr(VI) Reduction` $\to$ `Dissimilatory Fe(II)-Mediated Dissolved Oxygen Scavenging and Cr(III) Stabilization`).
   - **Curation Updates**: Corrected the biological process on Node 1 from `GO:0019418` (`sulfide oxidation`) to `GO:0019417` (`sulfur oxidation`) with `CHEBI:33403` (`elemental sulfur`) to match the source's verbatim mechanism (`"promoted Thiobacillus to oxidize S0 to SO42-"`), separated dissimilatory `Fe(II)` generation/dissolved-oxygen scavenging (`< 0.5 mg/L`) and `Cr(III)` stabilization into Node 3 so the full 3-step magnetite/sulfur/iron coupling is represented as a 3-node, 2-edge causal chain, and attached verbatim snippets from `references_cache/doi_10.1016_j.cej.2020.124801.md` on each upstream node. Readiness score increased from `85.0` to `100.0`.

4. **`CommunityMech:000494` — `kb/communities/Tunisian_Sahara_Saline_Spore_Forming_Halophile_Community.yaml`** (`PMID:23949950`)
   - **Graph**: 2 nodes, 1 directed `downstream` causal edge (`Poly-Extremophilic Endospore Persistence and Osmotic-Oxidative Stress Adaptation` $\to$ `Geographic Niche Partitioning and Marine-Origin Halobacillus-Bacillus Dominance`).
   - **Curation Updates**: Removed the redundant pairwise `target_taxon: Bacillus` slot on `COMMUNITY_LEVEL` Node 1 (where all seven spore-forming halophilic genera — `Halobacillus`, `Bacillus`, `Oceanobacillus`, `Virgibacillus`, `Thalassobacillus`, `Pontibacillus`, `Ornithinibacillus` — are already listed in `participating_taxa`), added the verbatim `PMID:23949950` geographic/BOX-PCR microdiversity snippet to Node 1 so the upstream node directly supports its outgoing `downstream` causal edge to Node 2, and added the marine-origin `Halobacillus`/`Bacillus` dominance snippet (`>60%` of isolates) to Node 2 (`readiness score: 85.0`).

5. **`CommunityMech:000495` — `data/isolates/Ferroplasma_Acidiphilum_ZJ_AMD_Genomic_Island_Adaptation.yaml`** (`PMID:40722006` / `PMC12302457`)
   - **Graph**: 3 nodes, 2 directed `downstream` causal edges (`Horizontal Gene Transfer and Integration of Five Genomic Islands in Ferroplasma acidiphilum ZJ` $\to$ `Third-Genomic-Island CRISPR/Cas Immune Defense and Toxin-Antitoxin Maintenance` $\to$ `Acidophilic Iron Oxidation and Heavy-Metal Stress Adaptation in pH 1.6 AMD`).
   - **Curation Updates**: Expanded the 2-node single-species physiological causal graph (`scope: COMMUNITY_LEVEL`) into a 3-node, 2-edge chain using verbatim open-access full-text evidence from `PMC12302457` (`references_cache/PMID_40722006.txt`), separating (1) horizontal gene transfer and genomic integration of five genomic islands (`GI1`–`GI5`) with metabolic, stress-resistance, and mobile genetic elements, (2) concentration of the complete type I-F `CRISPR/Cas` defense system (`cas3f`, `csy1`–`csy3`, `cas6f`, and CRISPR array) alongside four toxin-antitoxin (`TA`) stability pairs on the third genomic island (`GI3`), and (3) downstream cell-membrane biogenesis (`crtB`, `ispH`), energy metabolism, ferrous iron oxidation, and heavy-metal (`Cu`, `Zn`) stress adaptation in `pH 1.6` acid mine drainage. Readiness score increased from `85.0` to `100.0`.

## 4. Source-Limited Gaps & Representation/Writer Audit
- **Source-Limited Cohort (`54` `needs_research` records)**:
  - All 54 `needs_research` records (`44` with `1+` nodes and `0` directed edges where cached abstracts/metadata do not establish an explicit multi-step causal arrow between interaction nodes; `10` with `0` nodes where primary sources are paywalled or lack extractable interaction mechanisms in `references_cache/`) were verified to have no new cached full text in `references_cache/` and no new DRC bundles in `reports/drc/`. No unsupported edges or fabricated fields were added.
- **Reusable Taxon Records (`kb/taxa/*.yaml`)**:
  - Verified both shared `CommonTaxon` records (`kb/taxa/Shewanella_oneidensis_MR1.yaml` and `kb/taxa/Geobacter_sulfurreducens.yaml`) pass `scripts/validate_shared_taxon_ids.py` with zero drift.
- **Writer & Representation Audit**:
  - `scripts/audit_writers.py` passes with zero unguarded writers (`every writer imports communitymech.ControlledCuration`).
  - Single-species records in `data/isolates/*.yaml` represent multi-step physiological causal chains using `EcologicalInteraction` with `scope: COMMUNITY_LEVEL`, `source_taxon` (and no `target_taxon` or `participating_taxa`), and `downstream` edges (`target` + `description`), satisfying both `scripts/validate_strict.py` and `scripts/audit_causal_graphs.py` (`structural_defects == 0`).
