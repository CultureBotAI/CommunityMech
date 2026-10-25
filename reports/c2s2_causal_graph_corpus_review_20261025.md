# Cycle 2 Stage 2 (`causal_graphs`) Corpus Review & Curation Report (2026-10-25)

## 1. Scope & Workflow Context
- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle / Stage**: Cycle 2, Stage 2 (`causal_graphs` — Curation of Causal Graphs)
- **Repository**: `CultureBotAI/CommunityMech`
- **Base Commit**: `edd740d502690303a691935d1ee8deef911362f8` (`main` after Cycle 2 Stage 1 PR `#2064`)
- **Eligible Corpus**:
  - `477` community records in `kb/communities/*.yaml`
  - `7` isolate records in `data/isolates/*.yaml`
  - `2` shared taxon records in `kb/taxa/*.yaml` (`CommunityMechTaxon:000001` `Escherichia coli`, `CommunityMechTaxon:000002` `Saccharomyces cerevisiae`)
  - **Total `MicrobialCommunity` records**: `484`

## 2. Corpus-Wide SHA-256 Census & Review Status
Every record in `kb/communities/*.yaml` and `data/isolates/*.yaml` was audited against `reports/causal_graph_review/inventory.tsv` and `reports/causal_graph_review/summary.json`:

| Cohort | Record Count | Pre-Stage-2 Status | Post-Stage-2 Status | Notes |
| --- | ---: | --- | --- | --- |
| Previously reviewed records (`000001`–`000483`, 477 files) | 423 | `reviewed` | `reviewed` | Zero SHA-256 drift since Cycle 1 Stage 2 / Stage 5 remediation (`6683de7`). |
| Source-limited / awaiting paid full-text DRC (`000001`–`000483`) | 54 | `needs_research` | `needs_research` | Zero SHA-256 drift; zero new files in `references_cache/` or `reports/drc/` since Cycle 1 Stage 2; paid Edison/PaperQA3 credits not spent per authorization policy. |
| Cycle 2 Stage 1 additions (`000484`–`000490`, Batch 134) | 7 | `unreviewed` | `reviewed` | Curated in Batch 134 (`reports/causal_graph_review/decisions/20261025-stage2-seven-records-batch134.yaml`) via guarded `record_curation_event` + `write_validated_community`. |
| **Total (`MicrobialCommunity`)** | **484** | **423 reviewed / 54 needs_research / 7 unreviewed** | **430 reviewed / 54 needs_research / 0 unreviewed** | **`1,445` nodes, `573` directed `downstream` causal edges, `0` structural defects.** |

## 3. Batch 134 Causal-Graph Curation (`CommunityMech:000484`–`000490`)

All seven records added in Cycle 2 Stage 1 were reviewed end-to-end against their cached primary sources in `references_cache/` and updated via `communitymech.ControlledCuration` (`record_curation_event` + `write_validated_community`):

1. **`CommunityMech:000484` — `kb/communities/Aquifer_Sediment_Cable_Bacteria_Sulfur_Community.yaml`** (`PMID:27058505`)
   - **Graph**: 3 nodes, 2 directed `downstream` causal edges (`Long-Distance Electron Transfer Sulfide Oxidation and Sulfate Recycling` $\to$ `Sulfate-Reducing Hydrocarbon Plume Fringe Biodegradation` and `Long-Distance Electron Transfer Sulfide Oxidation and Sulfate Recycling` $\to$ `Redox-Gradient Niche Competition with Unicellular Sulfide Oxidizers`).
   - **Curation Updates**: Added explicit `participating_taxa` (`Desulfobulbaceae` `NCBITaxon:213121`, `Thiobacillus` `NCBITaxon:919`, `Ignavibacteria` `NCBITaxon:1134404`) and co-occurrence evidence on `COMMUNITY_LEVEL` Node 2 (`Sulfate-Reducing Hydrocarbon Plume Fringe Biodegradation`) with exact `{preferred_term, term}` coherence against `taxonomy`; aligned Node 1 and Node 2 descriptions with all participating guilds; updated field plume-fringe `evidence_source` to `FIELD_STUDY`; and added two verbatim `PMID:27058505` snippets on Node 1 so the upstream node directly backs both outgoing `downstream` edges. Preserved `PAIRWISE` competition on Node 3 (`Desulfobulbaceae` vs `Thiobacillus`).

2. **`CommunityMech:000485` — `kb/communities/Dexing_Copper_Bioleaching_Heap_Community.yaml`** (`doi:10.1186/s12863-016-0330-4`, `PMID:26781463`)
   - **Graph**: 3 nodes, 2 directed `downstream` causal edges (`Cooperative Chemolithoautotrophic Carbon and Nitrogen Fixation` $\to$ `Coupled Ferrous Iron and Reduced Sulfur Oxidation in Copper Tailings` $\to$ `Peroxiredoxin-Mediated Hydroxyl Radical Detoxification`).
   - **Curation Updates**: Completed `participating_taxa` across all three `COMMUNITY_LEVEL` nodes so all four `taxonomy` guilds (`Acidithiobacillus ferrooxidans` `NCBITaxon:920`, `Acidithiobacillus` `NCBITaxon:119977`, `Leptospirillum ferrooxidans` `NCBITaxon:180`, `Thiobacillus` `NCBITaxon:919`) are represented on Nodes 1, 2, and 3; aligned Node 2 and Node 3 descriptions with the four participating guilds; and added verbatim `PMID:26781463` / `doi:10.1186/s12863-016-0330-4` snippets (`evidence_source: FIELD_STUDY`) across Nodes 1–3 to directly support both outgoing `downstream` edges.

3. **`CommunityMech:000486` — `kb/communities/Stare_Ransko_Mine_Tailings_Bioleaching_Consortium.yaml`** (`doi:10.3390/min14030255`)
   - **Graph**: 2 nodes, 1 directed `downstream` causal edge (`Cooperative Iron and Sulfur Oxidation for Polymetallic Tailings Solubilization` $\to$ `Silver-Catalyzed Copper and Arsenic Bioleaching and Secondary Sulfate Precipitation`).
   - **Curation Updates**: Added the verbatim `Ag+` copper (+40.33%) and arsenic (+23.79%) solubilization-enhancement snippet from `doi:10.3390/min14030255` onto Node 1 (`Cooperative Iron and Sulfur Oxidation for Polymetallic Tailings Solubilization`) so the upstream node directly supports its outgoing `downstream` causal edge to `Silver-Catalyzed Copper and Arsenic Bioleaching and Secondary Sulfate Precipitation`.

4. **`CommunityMech:000487` — `kb/communities/Moderate_Thermophile_Chalcopyrite_pH_Bioleaching_Consortium.yaml`** (`doi:10.1007/s13213-019-01453-y`)
   - **Graph**: 2 nodes, 1 directed `downstream` causal edge (`Early Planktonic-Attached Niche Partitioning in Chalcopyrite Oxidation` $\to$ `Late-Phase Ferroplasma Succession and pH-Regulated Iron-Sulfur Oxidation`).
   - **Curation Updates**: Restricted `participating_taxa` on Node 1 (`Early Planktonic-Attached Niche Partitioning in Chalcopyrite Oxidation`) to the two early-stage dominant species (`Sulfobacillus thermosulfidooxidans` `NCBITaxon:28034` and `Acidithiobacillus caldus` `NCBITaxon:33059`) while retaining all three consortium members (including `Ferroplasma thermophilum` `NCBITaxon:2591003`) on late-stage Node 2; tightened Node 1's `downstream[0].description` to remove unsupported `"organic carbon conditions"` phrasing (`"Early-stage chalcopyrite bioleaching dominated by free Sulfobacillus thermosulfidooxidans and mineral-attached Acidithiobacillus caldus transitions in the later phase to Ferroplasma thermophilum predominance alongside pH-dependent iron and sulfur oxidation gene expression."`); and added verbatim pH-regulation and succession snippets from `doi:10.1007/s13213-019-01453-y` across Nodes 1 and 2.

5. **`CommunityMech:000488` — `data/isolates/Bacillus_licheniformis_Chromate_Biosorption.yaml`** (`doi:10.3389/fmicb.2024.1423741`)
   - **Graph**: Added a 2-node, 1-edge single-species physiological causal graph (`scope: COMMUNITY_LEVEL` per `scripts/audit_causal_graphs.py` single-species convention):
     - Node 1: `Cell-Surface Functional-Group Chromate Complexation and Deprotonation` (`source_taxon: Bacillus licheniformis`, `metabolites: [chromate(2-) CHEBI:35404, hydron CHEBI:15378]`, `biological_processes: [response to metal ion GO:0010038]`) backed by the verbatim FTIR Results deprotonation snippet (`"These changes suggest that the phosphate-containing compounds are involved in the interaction with metal ions. This interaction yields the emergence of negative phosphoryl groups as a result of a deprotonation process."`) and zeta-potential shift snippet (`−10.63 ± 0.38` to `−39.53 ± 1 mV`).
     - Directed Edge ($\to$): `Deprotonation of cell-surface phosphate/phosphoryl functional groups upon Cr(VI) exposure shifts the cellular zeta potential from -10.63 mV to -39.53 mV and drives surface Cr loading up to a 100 mg/L Cr6+ adsorption limit.`
     - Node 2: `Electrostatic Surface-Charge Shift and Chromium Biosorption Saturation` (`source_taxon: Bacillus licheniformis`, `metabolites: [chromate(2-) CHEBI:35404]`, `biological_processes: [response to metal ion GO:0010038]`)

6. **`CommunityMech:000489` — `data/isolates/Acidithiobacillus_LED_Metal_Bioleaching.yaml`** (`PMID:30343816`, `PMID:31203122`)
   - **Graph**: Added a 3-node, 2-edge single-species physiological causal graph (`scope: COMMUNITY_LEVEL`):
     - Node 1: `Serial Heavy-Metal Acclimatization to Waste LED Powder` (`source_taxon: Acidithiobacillus ferrooxidans`, `metabolites: [iron(2+) CHEBI:29033, iron(3+) CHEBI:29034]`, `biological_processes: [response to metal ion GO:0010038]`)
     - Directed Edge 1 ($\to$): `Serial adaptation to 5-25 g/L LED powder enables higher cell density, elevated ORP, lower pH, and sustained 4-5 g/L biogenic Fe3+ production in the presence of 20 g/L LED powder.`
     - Node 2: `Biogenic Ferric Iron and Acid Generation` (`source_taxon: Acidithiobacillus ferrooxidans`, `metabolites: [iron(2+) CHEBI:29033, iron(3+) CHEBI:29034, sulfuric acid CHEBI:26836]`, `biological_processes: [electron transport chain GO:0022900, sulfur oxidation GO:0019417]`)
     - Directed Edge 2 ($\to$): `Controlled 4-5 g/L biogenic Fe3+ and acidic lixiviant drive oxidative solubilization of copper, nickel, and gallium from 20 g/L waste LED powder while halving leaching duration from 30 days to 15 days.`
     - Node 3: `Catalytic Ferric Bioleaching of Copper, Nickel, and Gallium from Waste LEDs` (`source_taxon: Acidithiobacillus ferrooxidans`, `metabolites: [copper(2+) CHEBI:29036, nickel(2+) CHEBI:49786, gallium(3+) CHEBI:84043]`, `biological_processes: [electron transport chain GO:0022900]`)

7. **`CommunityMech:000490` — `data/isolates/Ferrimicrobium_acidiphilum_Iron_Respiration.yaml`** (`doi:10.1128/aem.01906-20`)
   - **Graph**: Added a 2-node, 1-edge single-species physiological causal graph (`scope: COMMUNITY_LEVEL`):
     - Node 1: `Extracellular Ferrous Iron Oxidation and Whole-Cell Cytochrome Reduction` (`source_taxon: Ferrimicrobium acidiphilum`, `metabolites: [iron(2+) CHEBI:29033, iron(3+) CHEBI:29034]`, `biological_processes: [electron transport chain GO:0022900]`)
     - Directed Edge ($\to$): `Electrons transferred from extracellular Fe(II) into cellular redox proteins feed the acidophilic aerobic respiratory chain to reduce dioxygen in intact live suspensions.`
     - Node 2: `Acidophilic Aerobic Respiratory Electron Transport Chain Coupling` (`source_taxon: Ferrimicrobium acidiphilum`, `metabolites: [dioxygen CHEBI:15379, hydron CHEBI:15378]`, `biological_processes: [aerobic respiration GO:0009060, electron transport chain GO:0022900]`)

## 4. Source-Limited Gaps & Representation/Writer Audit
- **Source-Limited Cohort (`54` `needs_research` records)**:
  - All 54 `needs_research` records (`44` with `1+` nodes and `0` directed edges where cached abstracts/metadata do not establish an explicit multi-step causal arrow between interaction nodes; `10` with `0` nodes where primary sources are paywalled or lack extractable interaction mechanisms in `references_cache/`) were verified to have no new cached full text in `references_cache/` and no new DRC bundles in `reports/drc/`. No unsupported edges or fabricated fields were added.
- **Writer & Representation Audit**:
  - `scripts/audit_writers.py` passes with zero unguarded writers (`every writer imports communitymech.ControlledCuration`).
  - Single-species records in `data/isolates/*.yaml` represent multi-step physiological causal chains using `EcologicalInteraction` with `scope: COMMUNITY_LEVEL`, `source_taxon` (and no `target_taxon` or `participating_taxa`), and `downstream` edges (`target` + `description`), satisfying both `scripts/validate_strict.py` and `scripts/audit_causal_graphs.py` (`structural_defects == 0`).
  - Existing deferred infrastructure tracking in `INFRA_TASKS.md` (`#2063` / `communitymech-infra-0004`: `scripts/validate_references.py` does not resolve `references_cache/DOI_*.txt` files when checking `doi:` references) remains documented for Stage 6.
