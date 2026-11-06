# Cycle 4 Stage 2 (`causal_graphs`) Corpus Review & Curation Report (2026-10-31)

## 1. Scope & Workflow Context
- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle / Stage**: Cycle 4, Stage 2 (`causal_graphs` — Curation of Causal Graphs)
- **Repository**: `CultureBotAI/CommunityMech`
- **Base Commit**: `5704621640724d4d051283d3babc12d1c29a2707` (`main` after Cycle 4 Stage 1 PR `#2087`)
- **Eligible Corpus**:
  - `481` community records in `kb/communities/*.yaml`
  - `9` isolate records in `data/isolates/*.yaml`
  - `2` shared taxon records in `kb/taxa/*.yaml` (`kb/taxa/Shewanella_oneidensis_MR1.yaml` `NCBITaxon:211586`, `kb/taxa/Geobacter_sulfurreducens.yaml` `NCBITaxon:35554`)
  - **Total `MicrobialCommunity` records**: `490`

## 2. Corpus-Wide SHA-256 Census & Review Status
Every record in `kb/communities/*.yaml` and `data/isolates/*.yaml` was audited against `reports/causal_graph_review/inventory.tsv` and `reports/causal_graph_review/summary.json`:

| Cohort | Record Count | Pre-Stage-2 Status | Post-Stage-2 Status | Notes |
| --- | ---: | --- | --- | --- |
| Previously reviewed records (`000001`–`000495`, 489 files) | 435 | `reviewed` | `reviewed` | Zero SHA-256 drift since Cycle 3 Stage 2 (`22266813`). |
| Source-limited / awaiting paid full-text DRC (`000001`–`000490`) | 54 | `needs_research` | `needs_research` | Zero SHA-256 drift; zero new files for these 54 records in `references_cache/`, `reports/drc/`, or `research/`; paid Edison/PaperQA3 credits not spent per authorization policy. |
| Cycle 4 Stage 1 addition (`000496`, Batch 136) | 1 | `pending` | `reviewed` | Curated in Batch 136 (`reports/causal_graph_review/decisions/20261031-stage2-one-record-batch136.yaml`) via guarded `record_curation_event` + `write_validated_community`. |
| **Total (`MicrobialCommunity`)** | **490** | **435 reviewed / 54 needs_research / 1 pending** | **436 reviewed / 54 needs_research / 0 pending** | **`1,463` nodes, `585` directed `downstream` causal edges, `0` structural defects.** |

## 3. Batch 136 Causal-Graph Curation (`CommunityMech:000496`)

The record added in Cycle 4 Stage 1 (`CommunityMech:000496`) was reviewed end-to-end against its cached primary sources (`references_cache/PMID_35295538.txt`, `references_cache/doi_10.1016_j.mex.2022.101652.md`, `references_cache/doi_10.20517_mrr.2023.70.md`) and updated via `record_curation_event` + `write_validated_community`:

1. **`CommunityMech:000496` — `kb/communities/Methylomicrobium_Arthrospira_Biogas_Conversion_Coculture.yaml`** (`PMID:35295538`, `doi:10.1016/j.mex.2022.101652`, `doi:10.20517/mrr.2023.70`)
   - **Graph**: 4 nodes, 3 directed `downstream` causal edges:
     1. `In Situ Oxygen Provision for Methane Oxidation` (`Arthrospira platensis` $\to$ `Methylomicrobium buryatense 5GB1`) $\to$
     2. `Reciprocal Carbon Dioxide Provision and Synergistic Coculture Growth` (`Methylomicrobium buryatense 5GB1` $\to$ `Arthrospira platensis`) $\to$
     3. `Predicted Emergent Cyanobacterial Ammonium and Organic Acid Cross-Feeding` (`Arthrospira platensis` $\to$ `Methylomicrobium buryatense 5GB1`, marked `HYPOTHESIZED`) $\to$
     4. `Predicted Reciprocal Methanotroph Carbon and Glutamine Cross-Feeding` (`Methylomicrobium buryatense 5GB1` $\to$ `Arthrospira platensis`, marked `HYPOTHESIZED`).
   - **Curation Updates**:
     - Resolved directional conflation in the original third interaction node (`Predicted Emergent Nitrogen and Metabolite Cross-Feeding`), which had declared `source_taxon: Arthrospira platensis` and `target_taxon: Methylomicrobium buryatense 5GB1` while including `L-glutamine` (`CHEBI:18050`, produced by the methanotroph for the cyanobacterium) and omitting three of the SteadyCom/DynamiCom-predicted methanotroph-exported metabolites (`citrate` `CHEBI:16947`, `lactate` `CHEBI:24996`, and `sucrose` `CHEBI:17992`).
     - Split the predicted non-gaseous cross-feeding mechanism from `doi:10.20517/mrr.2023.70` into two directionally accurate `PAIRWISE` `CROSS_FEEDING` nodes connected by a `downstream` edge:
       - Node 3 (`Predicted Emergent Cyanobacterial Ammonium and Organic Acid Cross-Feeding`, `A. platensis` $\to$ `M. buryatense 5GB1`): exports `ammonium` (`CHEBI:28938`), `succinate` (`CHEBI:30031`), `pyruvate` (`CHEBI:15361`), `formate` (`CHEBI:15740`), and `L-glutamate` (`CHEBI:29985`), capturing both the ~38 h increase in cyanobacterial pyruvate/glutamate provision and the ~45 h switch by `M. buryatense 5GB1` to exclusive cyanobacterial ammonium consumption.
       - Node 4 (`Predicted Reciprocal Methanotroph Carbon and Glutamine Cross-Feeding`, `M. buryatense 5GB1` $\to$ `A. platensis`): reciprocally exports `citrate` (`CHEBI:16947`), `L-glutamine` (`CHEBI:18050`), `lactate` (`CHEBI:24996`), and `sucrose` (`CHEBI:17992`) after mutualistic establishment (~38 h), backed by verbatim `doi:10.20517/mrr.2023.70` Figure 3 and Figure 5 snippets.
     - Updated `discussions[0].attaches_to` so the open `KNOWLEDGE_GAP` discussion (`m_buryatense_a_platensis_metabolite_flux_validation`) attaches to both predicted cross-feeding nodes.

## 4. Source-Limited Gaps & Representation/Writer Audit
- **Source-Limited Cohort (`54` `needs_research` records)**:
  - All 54 `needs_research` records (`44` with `1+` nodes and `0` directed edges where cached abstracts/metadata do not establish an explicit multi-step causal arrow between interaction nodes; `10` with `0` nodes where primary sources are paywalled or lack extractable interaction mechanisms in `references_cache/`) were verified to have no new cached full text in `references_cache/` and no new DRC bundles in `reports/drc/` or `research/`. No unsupported edges or fabricated fields were added.
- **Reusable Taxon Records (`kb/taxa/*.yaml`)**:
  - Verified both shared `CommonTaxon` records (`kb/taxa/Shewanella_oneidensis_MR1.yaml` and `kb/taxa/Geobacter_sulfurreducens.yaml`) pass `scripts/validate_shared_taxon_ids.py` with zero drift.
- **Writer & Representation Audit**:
  - `scripts/audit_writers.py` passes with zero unguarded writers.
  - `scripts/audit_causal_graphs.py` and `reports/causal_graph_review/build_inventory.py` confirm `structural_defects == []` across all 490 records.
