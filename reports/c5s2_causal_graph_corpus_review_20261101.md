# Cycle 5 Stage 2 (`causal_graphs`) Corpus Review & Curation Report (2026-11-01)

## 1. Scope & Workflow Context
- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle / Stage**: Cycle 5, Stage 2 (`causal_graphs` — Curation of Causal Graphs)
- **Repository**: `CultureBotAI/CommunityMech`
- **Base Commit**: `5ee21bb39a6e11f8f7cd9f0361899dce26598c8c` (`main` after Cycle 5 Stage 1 PR `#2098`)
- **Eligible Corpus**:
  - `485` community records in `kb/communities/*.yaml`
  - `9` isolate records in `data/isolates/*.yaml`
  - `2` shared taxon records in `kb/taxa/*.yaml` (`kb/taxa/Shewanella_oneidensis_MR1.yaml` `NCBITaxon:211586`, `kb/taxa/Geobacter_sulfurreducens.yaml` `NCBITaxon:35554`)
  - **Total `MicrobialCommunity` records**: `494`

## 2. Corpus-Wide SHA-256 Census & Review Status
Every record in `kb/communities/*.yaml` and `data/isolates/*.yaml` was audited against `reports/causal_graph_review/inventory.tsv` and `reports/causal_graph_review/summary.json`:

| Cohort | Record Count | Pre-Stage-2 Status | Post-Stage-2 Status | Notes |
| --- | ---: | --- | --- | --- |
| Previously reviewed records (`000001`–`000496`, 490 files) | 436 | `reviewed` | `reviewed` | Zero SHA-256 drift since Cycle 4 Stage 2 (`4f34e0a0`). |
| Source-limited / awaiting paid full-text DRC (`000001`–`000490`) | 54 | `needs_research` | `needs_research` | Zero SHA-256 drift; zero new files for these 54 records in `references_cache/`, `reports/drc/`, or `research/`; paid Edison/PaperQA3 credits not spent per authorization policy. |
| Cycle 5 Stage 1 additions (`000497`–`000500`, Batch 137) | 4 | `pending` | `reviewed` | Curated in Batch 137 (`reports/causal_graph_review/decisions/20261101-stage2-four-records-batch137.yaml`) via guarded `record_curation_event` + `write_validated_community`. |
| **Total (`MicrobialCommunity`)** | **494** | **436 reviewed / 54 needs_research / 4 pending** | **440 reviewed / 54 needs_research / 0 pending** | **`1,471` nodes, `586` directed `downstream` causal edges, `0` structural defects.** |

## 3. Batch 137 Causal-Graph & Taxon-Grounding Curation (`CommunityMech:000497`–`000500`)

All four records added in Cycle 5 Stage 1 (`CommunityMech:000497`–`000500`) were reviewed end-to-end against their cached open-access full text (`references_cache/PMID_42726284.md` and `references_cache/PMID_42354927.md`) and updated via `record_curation_event` + `write_validated_community`:

1. **`CommunityMech:000497` — `kb/communities/Synechocystis_Ecoli_Acetate_Butanol_Coculture.yaml`** (`PMID:42726284`, `doi:10.1007/s00253-026-14029-z`)
   - **Graph**: 2 nodes, 1 directed `downstream` causal edge:
     1. `Photosynthetic Acetate Supply To Escherichia coli` (`PAIRWISE` `CROSS_FEEDING`: `Synechocystis sp. PCC 6803 WT_PKPa_RBS_BsPta_Δacs` $\to$ `Escherichia coli BL21(DE3) Pem7_ButOH`) $\to$
     2. `Acetate-Coupled 1-Butanol Production` (`COMMUNITY_LEVEL`: `participating_taxa` covering both coculture partners).
   - **Curation Updates**:
     - Enriched `Photosynthetic Acetate Supply To Escherichia coli` with verbatim evidence from `PMID:42726284` documenting post-day-10 `E. coli_Pem7_ButOH` population recovery and sustained viable cell counts through day 30 alongside the sharper post-day-22 decline in extracellular acetate relative to the parallel `P. taiwanensis_Pem7_ButOH` coculture.
     - Enriched `Acetate-Coupled 1-Butanol Production` with verbatim `PMID:42726284` evidence for the oxygen-tolerant fatty-acid-synthesis-derived TPC4 pathway (`Pásztor et al. 2015`) and the energetic/redox constraint explaining why acetate adaptation did not increase 1-butanol titers (acetate assimilation consumes ATP without increasing NAD(P)H reducing power).
     - Preserved the `HYPOTHESIZED/PARTIAL` downstream causal edge and open `KNOWLEDGE_GAP` discussion (`ecoli_butanol_coculture_carbon_specificity`) because carbon flux from acetate vs. secreted cyanobacterial carbohydrates/EPS was not isotope-resolved.

2. **`CommunityMech:000498` — `kb/communities/Cyantraniliprole_Consortium_T1.yaml`** (`PMID:42354927`, `doi:10.3390/microorganisms14020438`)
   - **Graph**: 2 `COMMUNITY_LEVEL` nodes (`T1 distributed cyantraniliprole enzyme potential` and `HPLC-confirmed cyantraniliprole removal`), `0` directed `downstream` causal edges (matching sister record `CommunityMech:000369` in Batch 28).
   - **Curation Updates**:
     - Expanded YAML anchor/alias reuse (`&id001` / `*id001`) on `participating_taxa` into explicit compact `{preferred_term, term}` lists across both interaction nodes.
     - Enriched `T1 distributed cyantraniliprole enzyme potential` (`COMPUTATIONAL`) with the strain-by-strain Table 8 EAWAG-BBD enzyme-class distribution (`TPI`, `AP`, and `C1,2O` across `Re1`–`Re6`; `COMT` in `Re1` and `Re3`; `OEX` in `Re2`; 19 total enzyme hits).
     - Enriched `HPLC-confirmed cyantraniliprole removal` (`IN_VITRO`, 70.11% removal, 57.58 $\to$ 17.21 mg/L) with day-11 microcosm bacterial proliferation evidence (`5.86 x 10^6 CFU/mL`).
     - Preserved `edges_after: []` and the open `KNOWLEDGE_GAP` discussion (`cyantraniliprole_t1_expressed_enzymes`) because Table 8 is post-assay bioinformatic pathway prediction rather than experimentally demonstrated causal enzyme mediation.

3. **`CommunityMech:000499` — `kb/communities/Cyantraniliprole_Consortium_T2.yaml`** (`PMID:42354927`, `doi:10.3390/microorganisms14020438`)
   - **Graph**: 2 `COMMUNITY_LEVEL` nodes (`T2 distributed cyantraniliprole enzyme potential` and `HPLC-confirmed cyantraniliprole removal`), `0` directed `downstream` causal edges (matching sister record `CommunityMech:000369` in Batch 28).
   - **Curation Updates**:
     - Expanded YAML anchor/alias reuse (`&id001` / `*id001`, `&id002` / `*id002`) into explicit lists.
     - Enriched `T2 distributed cyantraniliprole enzyme potential` (`COMPUTATIONAL`) with the strain-by-strain Table 8 EAWAG-BBD enzyme-class distribution (`TPI`, `AP`, and `C1,2O` across `Bo1`–`Bo6`; `OEX` in `Bo3`–`Bo6`; `COMT` absent across all six strains; 22 total enzyme hits).
     - Enriched `HPLC-confirmed cyantraniliprole removal` (`IN_VITRO`, 75.04% removal, 57.33 $\to$ 14.31 mg/L) with day-11 microcosm bacterial proliferation evidence (`5.92 x 10^6 CFU/mL`).
     - Preserved `edges_after: []` and the open `KNOWLEDGE_GAP` discussion (`cyantraniliprole_t2_expressed_enzymes`).

4. **`CommunityMech:000500` — `kb/communities/Cyantraniliprole_Consortium_T3.yaml`** (`PMID:42354927`, `doi:10.3390/microorganisms14020438`)
   - **Graph**: 2 `COMMUNITY_LEVEL` nodes (`T3 distributed cyantraniliprole enzyme potential` and `HPLC-confirmed cyantraniliprole removal`), `0` directed `downstream` causal edges (matching sister record `CommunityMech:000369` in Batch 28).
   - **Curation Updates**:
     - **GTDB Grounding (`ground-causal-graph-taxa`)**: Upgraded `Bacillus subtilis Ht1` and `Bacillus subtilis Ht2` (`NCBITaxon:1423`) in `taxonomy[].taxon_term` from `gtdb_grounding_status: UNRESOLVED` to `GROUNDED` with canonical `gtdb_classification` (`GTDB:s__Bacillus_subtilis`, `d__Bacteria;p__Bacillota;c__Bacilli;o__Bacillales;f__Bacillaceae;g__Bacillus;s__Bacillus subtilis`, `majority_fraction: 0.91`, `total_genomes: 1256`, `is_reclassified: false`), bringing `CommunityMech:000500` to `5/6` GTDB-grounded members (`Ht1`, `Ht2`, `Ht4`, `Ht5`, `Ht6`).
     - Expanded YAML anchor/alias reuse (`&id001` / `*id001`, `&id002` / `*id002`) into explicit lists.
     - Enriched `T3 distributed cyantraniliprole enzyme potential` (`COMPUTATIONAL`) with the strain-by-strain Table 8 EAWAG-BBD complementary enzyme-class distribution (`TPI`, `AP`, and `C1,2O` in `Ht1`–`Ht6`; `COMT` in `Bacillus` strains `Ht1`–`Ht3`; `OEX` in `Pseudomonas aeruginosa` strains `Ht4`–`Ht6`; 24 total enzyme hits).
     - Enriched `HPLC-confirmed cyantraniliprole removal` (`IN_VITRO`, 96.72% removal, 57.89 $\to$ 1.90 mg/L) with day-11 microcosm bacterial proliferation evidence (`6.11 x 10^6 CFU/mL`).
     - Preserved `edges_after: []` and the open `KNOWLEDGE_GAP` discussion (`cyantraniliprole_t3_expressed_enzymes`).

## 4. Source-Limited Gaps & Representation/Writer Audit
- **Source-Limited Cohort (`54` `needs_research` records)**:
  - All 54 `needs_research` records (`44` with `1+` nodes and `0` directed edges where cached abstracts/metadata do not establish an explicit multi-step causal arrow between interaction nodes; `10` with `0` nodes where primary sources are paywalled or lack extractable interaction mechanisms in `references_cache/`) were verified to have no new cached full text in `references_cache/` and no new DRC bundles in `reports/drc/` or `research/`. No unsupported edges or fabricated fields were added.
- **Reusable Taxon Records (`kb/taxa/*.yaml`)**:
  - Verified both shared `CommonTaxon` records (`kb/taxa/Shewanella_oneidensis_MR1.yaml` and `kb/taxa/Geobacter_sulfurreducens.yaml`) pass `scripts/validate_shared_taxon_ids.py`, `scripts/validate_gtdb_coherence.py`, and `scripts/validate_prokaryotic_lineage.py` with zero drift.
- **Writer & Representation Audit**:
  - `scripts/audit_writers.py` passes with zero unguarded writers.
  - `scripts/audit_causal_graphs.py` and `reports/causal_graph_review/build_inventory.py` confirm `structural_defects == []` across all 494 records.
