# Cycle 4, Stage 1 (`add_records`) — Bounded-Frontier Discovery & Intake Report (2026-10-31)

## 1. Executive Summary

- **Workflow Stage**: Run `mech-goal-sequence-20261019`, Cycle 4, Stage 1 (`add_records`)
- **Instruction ID**: `562655c74facc6331f493e8d`
- **Action ID**: `0b987a9cefdcc76e21992c1f`
- **Starting Corpus State**: 489 `MicrobialCommunity` records (`CommunityMech:000001`–`CommunityMech:000495`, with 6 historical ID gaps; 480 in `kb/communities/` and 9 in `data/isolates/`) plus 2 `CommonTaxon` records in `kb/taxa/`
- **Ending Corpus State**: 490 `MicrobialCommunity` records (`CommunityMech:000001`–`CommunityMech:000496`, with 6 historical ID gaps; 481 in `kb/communities/` and 9 in `data/isolates/`) plus 2 `CommonTaxon` records in `kb/taxa/`
- **New Records Added**: **1** (`CommunityMech:000496` — `kb/communities/Methylomicrobium_Arthrospira_Biogas_Conversion_Coculture.yaml`)
- **Exhaustion Verification**: Two full passes over the local offline reference cache (`references_cache/`, 866 top-level `.md`/`.txt` files), `research/scouting/` (4 scouting batches), `notes/new-communities-to-create.md`, and `notes/new-datasets-to-curate.md` confirmed that after curating `CommunityMech:000496` (linking `PMID_35295538.txt`, `doi_10.1016_j.mex.2022.101652.md`, and `doi_10.20517_mrr.2023.70.md`), **0** additional uncited references with verbatim abstract/full-text support describe an uncurated microbial community or supported isolate baseline.

---

## 2. Bounded-Frontier Search Methodology & Repeated Passes

### Pass 1: Structured Citation Index & Full Cache Sweep

1. **Structured Corpus Citation Index**:
   - Parsed all 489 existing `MicrobialCommunity` YAML records (`480` in `kb/communities/` and `9` in `data/isolates/`) and `2` `CommonTaxon` records (`kb/taxa/`), extracting every structured `evidence[].reference` value (rather than prose mentions in `curation_history` or `notes`).
   - Confirmed highest existing identifier: `CommunityMech:000495` (`data/isolates/Ferroplasma_Acidiphilum_ZJ_AMD_Genomic_Island_Adaptation.yaml`) and next available identifier: `CommunityMech:000496`.
2. **Local Reference Cache Audit (`references_cache/`)**:
   - Audited all `866` top-level `.md` and `.txt` files in `references_cache/` against the structured `evidence[].reference` index across all prefix conventions (`PMID_`, `pmc_full_pmid_`, `doi_`, `europepmc_`, `openalex_`, `semanticscholar_`, `epmc_chem_`, `pmc_`, `GITHUB_`).
   - Identified **54** top-level cache files not cited in any structured `evidence[].reference` slot.
   - Inspected all 54 uncited cache files line-by-line and discovered **1 admissible uncurated defined binary coculture** backed by **3** uncited open-access full-text cache files:
     - `PMID_35295538.txt` and `doi_10.1016_j.mex.2022.101652.md`: Kiumars Badr, Q. Peter He, Jin Wang (2022), *Matlab implementation of a novel semi-structured kinetic model for methanotroph-photoautotroph cocultures*, MethodsX 9:101652 (`PMID:35295538`, `PMCID:PMC8918855`).
     - `doi_10.20517_mrr.2023.70.md`: Kiumars Badr, Q. Peter He, Jin Wang (2024), *Probing interspecies metabolic interactions within a synthetic binary microbiome using genome-scale modeling*, Microbiome Research Reports 3:31 (`PMID:39421256`, `PMCID:PMC11480724`).
   - **Provenance of Discovery**: In issue `#1608` (PR `#2076`), `CommunityMech:000192` (`kb/communities/Methylomicrobium_Synechococcus_Biogas_Conversion_Coculture.yaml`) had mixed two distinct methanotroph-photoautotroph cocultures from the same research group: (a) `Methylomicrobium alcaliphilum 20Z` + `Synechococcus` sp. PCC 7002 (`PMID:34039511`) and (b) `Methylomicrobium buryatense 5GB1` + `Arthrospira platensis` (`PMID:35295538` / `doi:10.1016/j.mex.2022.101652` and `doi:10.20517/mrr.2023.70`). Remediation of `#1608` scoped `CommunityMech:000192` strictly to `M. alcaliphilum 20Z` + `Synechococcus` PCC 7002 (`PMID:34039511`), leaving the `M. buryatense 5GB1` + `A. platensis` biogas conversion coculture uncurated in the KB despite having complete cached open-access full text in `references_cache/`.

### Pass 2: Post-Intake Re-Sweep & Exhaustion Verification

- After curating `CommunityMech:000496` (`kb/communities/Methylomicrobium_Arthrospira_Biogas_Conversion_Coculture.yaml`), re-ran the structured `evidence[].reference` deduplication scan across all `490` `MicrobialCommunity` records (`481` in `kb/communities/`, `9` in `data/isolates/`) and `2` `CommonTaxon` records.
- Verified that `PMID_35295538.txt`, `doi_10.1016_j.mex.2022.101652.md`, and `doi_10.20517_mrr.2023.70.md` are now cited in `CommunityMech:000496` with `24/24` `MATCH` snippets in `scripts/evidence_snippet_audit.py` and `0` issues in `linkml-reference-validator`.
- Confirmed that the remaining **51** uncited top-level cache files contain **0** admissible uncurated microbial community or supported isolate baseline records (full disposition table in Section 4).

---

## 3. Newly Added Record (`CommunityMech:000496`)

| ID | Path | Category / State / Origin | Primary Reference(s) | Taxa (`NCBITaxon` & GTDB Status) | Summary of Curated Mechanism |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `CommunityMech:000496` | `kb/communities/Methylomicrobium_Arthrospira_Biogas_Conversion_Coculture.yaml` | `BIOTECHNOLOGY` / `ENGINEERED` / `SYNTHETIC` | `PMID:35295538`, `doi:10.1016/j.mex.2022.101652`, `doi:10.20517/mrr.2023.70` | `Methylotuvimicrobium buryatense 5G` (`preferred_term`: `Methylomicrobium buryatense 5GB1`, `NCBITaxon:675511`, `UNRESOLVED`), `Limnospira platensis` (`preferred_term`: `Arthrospira platensis`, `NCBITaxon:118562`, `AMBIGUOUS`: `GTDB:s__Limnospira_fusiformis`, `GTDB:s__Limnospira_platensis`) | Defined binary methanotroph-photoautotroph coculture in 90% Zarrouk + 10% NMS2 medium (pH 8.7–9, 100 mL photobioreactor, 60% CH4 / 30% CO2 / 10% N2 refed every 24 h, 180 umol m-2 s-1, 12.5:1 P:M inoculum ratio). In situ photosynthetic O2 from `A. platensis` is completely consumed by `M. buryatense 5GB1` for CH4 oxidation, while methanotrophic CO2 feeds cyanobacterial carbon fixation; SteadyCom/DynamiCom (iMb5G(B1) + NIES-39) predicts emergent cross-feeding of succinate, ammonium, pyruvate, formate, citrate, sucrose, glutamine, and glutamate with a ~45 h shift to exclusive cyanobacterial ammonium consumption. |

---

## 4. Preserved Unresolved Candidates & Search Limits

### 4.1 Complete Disposition of the 51 Remaining Uncited Top-Level Cache Files

1. **Duplicate / Superseded Cache Copies of Already-Curated Records (8 files)**:
   - `PMID_42195847.txt`, `PMID_42243405.txt`, `PMID_42385706.txt`: Cached with erroneous synthetic PMIDs; their actual DOIs (`doi:10.1038/s41467-026-68616-x`, `doi:10.1186/s40168-026-02358-4`, `doi:10.1093/jambio/lxaf298`) are already curated and cited in `kb/communities/Synthetic_Lichen_Synechococcus_Rhodotorula_Coculture.yaml`, `kb/communities/Sorghum_19Strain_CrossKingdom_Drought_SynCom.yaml`, and `kb/communities/Caldicellulosiruptor_Thermoanaerobacter_Cellulose_H2_Coculture.yaml`.
   - `doi_10.1038_s41559-022-01923-8.md`: Already curated via `PMID:36443462` in `kb/communities/Variovorax_Cryptococcus_Vitamin_Mutualism_Microcosm.yaml`.
   - `doi_10.1016_j.cell.2014.05.041.txt`: Duplicate text file of `europepmc_10.1016_j.cell.2014.05.041.txt` (human infant gut cohort study, `PMID:24995982`).
   - `GITHUB_Xinming9606_lignin_SynCom_proteomics_blob_ed208e4d5df80c96100f2113db39698832d7b685_downstream_analysis.py.md`: Supporting GitHub script for `kb/communities/Comamonas_Lindane_Degrading_Soil_SynCom.yaml` / lignin SynCom proteomics.
   - `GITHUB_deanpettinga_src2_paper_tree_693011e69d83bf23f02f144d506df5b8ee17a8dd.md`: Supporting GitHub repository listing for `kb/communities/Synechococcus_Elongatus_Rhodotorula_Glutinosa_Coculture.yaml`.
   - `doi_10.25345_C58W38C48.md`: Dryad/MassIVE dataset landing page metadata stub.
2. **Metadata-Only / Abstract-Less Cache Stubs (`Abstract\nNone`, 6 files)**:
   - `doi_10.1007_BF02106205.md`, `doi_10.1007_s10230-008-0059-z.md`, `doi_10.1016_j.algal.2016.05.024.md`, `doi_10.1016_j.bbabio.2015.02.010.md`, `doi_10.1016_j.ijhydene.2015.05.135.md`, `doi_10.1016_j.mineng.2013.03.022.md`: Contain only bibliographic metadata (`Abstract\nNone`) and cannot provide verbatim evidence snippets without external full-text retrieval.
3. **Broad Reviews, Perspectives, and Multi-System Surveys (9 files)**:
   - `PMID_11034209.md`, `PMID_18330567.md`, `PMID_19383036.md`, `PMID_36593292.txt`, `doi_10.1007_s10311-019-00911-y.md`, `doi_10.1016_j.cej.2021.133461.md`, `doi_10.1016_j.scitotenv.2021.151468.md`, `doi_10.1186_s12302-025-01103-y.md`, `epmc_chem_PMC8072228.txt`: Review articles or broad technology surveys that do not define a single curatable microbial community or isolate baseline.
4. **Abiotic, Plant-Only, Host-Pathology, Pure Enzyme/Genetics, or Unresolved Taxon-Code Studies (28 files)**:
   - `PMID_12620881.md` (pure `Rhodobacter sphaeroides` RubisCO biochemistry), `PMID_2039291.txt` (human clinical pathology), `PMID_21559381.txt` (pure `Leptospirillum` comparative genomics), `PMID_25687895.txt` (mouse gut host antibiotic pathology), `PMID_28080685.txt` (pure `Pseudomonas` genetics), `PMID_32753581.txt` (plant physiology), `PMID_34742794.txt` (single-strain genetics), `PMID_39126844.txt` (host clinical study), `PMID_42667226.txt` (`doi:10.3389/fpls.2026.1781140`; abstract uses only internal isolate codes `N67`, `N92`, `N111`, `N238` without genus/species names in the cached abstract), `PMID_4381058.txt` (1972 enzyme purification), `PMID_8161360.txt` (1994 single-gene cloning), `PMID_9734072.txt` (1998 single-protein biochemistry), `PMID_9734074.txt` (1998 single-protein biochemistry), `PMID_9785463.txt` (1998 single-enzyme characterization), `doi_10.1016_j.cej.2023.146646.md` (abiotic/sludge reactor engineering without resolved community interactions), `doi_10.1016_j.ibiod.2025.106190.md` (ungrounded fungal isolate screening without ecological interactions), `doi_10.1016_j.jenvman.2024.122098.md` (bulk soil amendment without defined community taxa), `doi_10.1038_s41522-020-00170-8.md` (broad mouse gut 16S survey), `doi_10.1080_10889868.2024.2407240.md` (single-strain petroleum hydrocarbon screening), `doi_10.1101_2024.03.28.587009.md` (computational benchmark preprint), `doi_10.1111_j.1462-2920.2005.00861.x.md` (environmental clone library survey), `doi_10.1155_2021_7694157.md` (clinical oral microbiome survey), `doi_10.1186_s40793-021-00380-3.md` (single-genome announcement), `epmc_chem_PMC1287685.txt` (single-protein crystal structure), `epmc_chem_PMC242454.txt` (1991 `Escherichia coli` operon genetics), `epmc_chem_PMC4510191.txt` (single-strain metabolic engineering), `epmc_chem_PMC4984294.txt` (single-strain biochemistry), `epmc_chem_PMC5373366.txt` (broad soil amplicon survey).

### 4.2 Scouting Stubs & Notes Preserved for Future Network-Enabled Intake

- Audited all 4 scouting batches under `research/scouting/` (`2026-04-06` [25 candidates], `2026-04-06-b2` [22 candidates], `2026-04-12` [100 candidates], `2026-04-12-syncom` [25 candidates]). Every scouting stub that has a corresponding cached reference in `references_cache/` is already curated in `kb/communities/`; the remaining scouting candidates have no local cached abstract/full-text file in `references_cache/` and are preserved in `research/scouting/` and `notes/` for future network-authorized deep-research or Europe PMC intake cycles.
