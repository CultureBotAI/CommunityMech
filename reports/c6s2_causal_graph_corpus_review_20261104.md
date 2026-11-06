# Cycle 6 Stage 2 Causal-Graph & Mechanism Corpus Review (2026-11-04)

- **Run**: `mech-goal-sequence-20261019`
- **Cycle / Stage**: Cycle 6, Stage 2 (`causal_graphs`)
- **Base Commit**: `3a22fac5692988cd3443375ff8bb2e52ce45d009`
- **Decision Ledger Added**: `reports/causal_graph_review/decisions/20261104-stage2-four-records-batch138.yaml`
- **Inventory & Summary Updated**: `reports/causal_graph_review/inventory.tsv`, `reports/causal_graph_review/summary.json`

## 1. Corpus Scope & Summary Metrics

| Cohort | Count | Status After Cycle 6 Stage 2 | Notes |
|---|---:|---|---|
| `kb/communities/*.yaml` (`MicrobialCommunity`) | 489 | 435 `reviewed`, 54 `needs_research`, 0 `pending` | Includes Batch 138 (`CommunityMech:000501`–`000504`) curated & reviewed in this stage |
| `data/isolates/*.yaml` (`MicrobialCommunity`) | 9 | 9 `reviewed`, 0 `needs_research`, 0 `pending` | All 9 isolate baseline records verified unchanged via SHA-256 census |
| **Total `MicrobialCommunity` Records** | **498** | **444 `reviewed`, 54 `needs_research`, 0 `pending`** | **0 structural defects (`structural_defects == []`), 1,480 nodes, 586 downstream edges** |
| `kb/taxa/*.yaml` (`CommonTaxon`) | 2 | Verified schema- & term-valid | `Geobacter_sulfurreducens.yaml` (`5d2b49dc...`), `Shewanella_oneidensis_MR1.yaml` (`df038771...`) |
| **Total Eligible Corpus** | **500** | **100% accounted for** | 0 unreviewed (`pending`) records |

## 2. Batch 138 Causal-Graph Curation & Review (`CommunityMech:000501`–`000504`)

All four community records added in Cycle 6 Stage 1 were audited line-by-line against their committed primary-source evidence caches (`references_cache/PMID_42144568.txt` and `references_cache/PMID_42587276.txt`) and sibling records (`CommunityMech:000347` and `CommunityMech:000358`), updated via `record_curation_event(..., action="CURATE_CAUSAL_GRAPH", llm_assisted=True)` and `write_validated_community(...)`, and recorded in append-only history sidecars under `history/records/`:

1. **`CommunityMech:000501` (`kb/communities/Burkholderia_Bacillus_C2_Masson_Pine_SynCom.yaml`)**
   - **SHA-256**: `55ce7c926f40884b845f1341e8479f2de19a96490d9745dc7093dd92b9c9616c` → `4c540d55438895202d84cb0b25957c0637780be4e031b5029211b747ad07a18d`
   - **Primary Source**: `PMID:42144568` (`doi:10.1002/ps.70924`, `references_cache/PMID_42144568.txt`)
   - **Mechanism Representation (3 `COMMUNITY_LEVEL` nodes, 0 downstream edges)**:
     - `C2 SynCom Suppression of Fusarium oxysporum`: Added verbatim snippet (`"Of these, eight strains demonstrated significant inhibitory effects against F. oxysporum, ranging from 33.81% to 59.52%."`, `IN_VITRO`, `SUPPORT`) anchoring the single-strain antagonism range cited in the node description, and bounded in vitro plate confrontation, pot-assay damping-off control, and host defense-gene activation as parallel experimental endpoints without intermediate pathway ablation.
     - `C2 SynCom Masson Pine Damping-Off Protection and Seedling Growth Promotion`: Added verbatim snippet (`"The synthetic PGPR community assembled under the influence of T. koningiopsis effectively enhances damping-off resistance and promotes the growth of Masson pine seedlings."`, `IN_VIVO`, `SUPPORT`) reinforcing the combined damping-off resistance and seedling growth promotion outcome alongside the `10.18%` height increase and `50%` disease-incidence reduction snippet.
     - `C2 Protective Enzyme Enhancement and Resistance-Gene Activation`: Verified existing `SUPPORT` (`"These treatments also enhanced protective enzyme activity and alleviated membrane damage."`) and `PARTIAL` (`"At the molecular level, the C2 and HT SynComs boost plant resistance by modulating the plant hormone and mitogen-activated protein kinase (MAPK) signaling pathways, thereby activating the expression of crucial resistance genes such as PR1, FLS2, and CAT1."`) snippets against `references_cache/PMID_42144568.txt`.
   - **Taxon Grounding**: Verified all five inoculant strains (`Burkholderia cepacia RW1` `NCBITaxon:292`, `Bacillus siamensis RW5` `NCBITaxon:659243` / `GTDB:s__Bacillus_siamensis`, `Bacillus amyloliquefaciens RW6` `NCBITaxon:1390`, `Bacillus velezensis RW7` `NCBITaxon:492670` / `GTDB:s__Bacillus_velezensis`, `Bacillus vallismortis RW8` `NCBITaxon:72361`) across `taxonomy` and `participating_taxa`.
   - **Source-Limited Gaps**: Specific secreted antifungal metabolites and causal necessity between direct pathogen inhibition and induced systemic resistance in *Pinus massoniana* are not experimentally ablated in `PMID:42144568`.
   - **History Sidecar**: `history/records/Burkholderia_Bacillus_C2_Masson_Pine_SynCom/2026-11-04T133500Z-antigravity-c6s201.yaml`.

2. **`CommunityMech:000502` (`kb/communities/Bacillus_B81_A1_PAH_Biofilm_Consortium_1.yaml`)**
   - **SHA-256**: `170e3f3299cf2fdb216173ff6121366549146165a89be8d34c93e6680885367b` → `715ea160d2968d36d0d7d0fab42cfec1c66cd5cbbce39b3381861a036e9d6ff4`
   - **Primary Source**: `PMID:42587276` (`PMC13471667`, `doi:10.1186/s12866-026-05144-y`, `references_cache/PMID_42587276.txt`)
   - **Mechanism Representation (2 `COMMUNITY_LEVEL` nodes, 0 downstream edges)**:
     - `Consortium 1 Planktonic and Biofilm Naphthalene Biodegradation`: Added verbatim snippets for single-strain *Bacillus paramycoides* B8-1 naphthalene removal (`98.43%`, `"Among them, isolate B8-1 showed the highest degradation efficiency, with 77.94% phenanthrene degradation and 98.43% naphthalene degradation."`) and the authors' proposed biotransformation-product cross-feeding hypothesis (`"One possible reason that makes the bacterial consortia have a superior naphthalene biodegradation efficiency is that, during the process of biotransformation, the product of one bacterium can be employed as the foundation for the catabolism and growth of another."`), while bounding 7-day HPLC parent-substrate disappearance (`75.54%` planktonic, `77.45%` glass-attached biofilm) without unmeasured metabolite intermediates.
     - `Consortium 1 Biofilm-Mitigated Phenanthrene Antagonism`: Added verbatim snippet (`"On the contrary, the isolate B8-1 exhibited a biodegradation rate, in the planktonic mode, of 77.94% that relatively higher than that obtained in its biofilm mode, 60.72% (see Fig. 8 a)."`) anchoring B8-1 single-strain phenanthrene removal baselines (`77.94%` planktonic / `60.72%` biofilm) cited in the node description.
   - **Taxon Grounding**: Verified `Bacillus paramycoides B8-1` (`NCBITaxon:2026194`) and `Bacillus paranthracis A1` (`NCBITaxon:2026186`) synchronization across `taxonomy` and `participating_taxa`.
   - **Source-Limited Gaps**: Secreted naphthalene biotransformation intermediates, EPS matrix composition, and strain-resolved cell abundances in B8-1 + A1 planktonic and biofilm co-cultures are not chemically or molecularly quantified in `PMID:42587276`.
   - **History Sidecar**: `history/records/Bacillus_B81_A1_PAH_Biofilm_Consortium_1/2026-11-04T133500Z-antigravity-c6s202.yaml`.

3. **`CommunityMech:000503` (`kb/communities/Bacillus_B81_A3_Naphthalene_Biofilm_Consortium_2.yaml`)**
   - **SHA-256**: `1cf4e9cee25ba78a2abccbab1d98eec8dc1078d124b15b55e422ad444e8507c8` → `de9b2f80f9c505f9404ccc9f107d1bdfdf5849291e944cb5be6ce8063c8507f5`
   - **Primary Source**: `PMID:42587276` (`PMC13471667`, `doi:10.1186/s12866-026-05144-y`, `references_cache/PMID_42587276.txt`)
   - **Mechanism Representation (2 `COMMUNITY_LEVEL` nodes, 0 downstream edges)**:
     - `Consortium 2 Biofilm-Accelerated and Mixture Naphthalene Synergy`: Added verbatim snippets quantifying planktonic (`44.71%`) vs glass-attached biofilm (`86.88%`) naphthalene biodegradation across all isolates and consortia (`"The result demonstrated that the naphthalene biodegradation rates of 41.01, 38.92, 75.54, 44.71, 92.43, and 64.47% for the planktonic cultures, whereas were 87.72, 64.57, 77.45, 86.88, 94.69, and 79.74% for the biofilm cultures of isolates A1, A3, consortium 1, consortium 2, consortium 3, and consortium 4, respectively."`) and contrasting weak planktonic B8-1 + A3 synergy with strong biofilm acceleration (`"This finding demonstrated the synergistic interaction between the consortia`s members, with the highest synergistic interaction between the planktonic isolates (A1 and A3) in the consortium 3 and the least synergistic interaction between the planktonic isolates (B8-1 and A3) in the consortium 2."`).
     - `Consortium 2 Lower Phenanthrene Removal`: Added verbatim snippet (`"On the contrary, the isolate B8-1 exhibited a biodegradation rate, in the planktonic mode, of 77.94% that relatively higher than that obtained in its biofilm mode, 60.72% (see Fig. 8 a)."`) anchoring B8-1 single-strain phenanthrene removal baselines (`77.94%` planktonic / `60.72%` biofilm).
   - **Taxon Grounding**: Verified `Bacillus paramycoides B8-1` (`NCBITaxon:2026194`) and `Bacillus licheniformis A3` (`NCBITaxon:1402`, `GTDB:s__Bacillus_licheniformis`) synchronization across `taxonomy` and `participating_taxa`.
   - **Source-Limited Gaps**: Specific naphthalene ring-cleavage intermediates and strain-level population ratios inside the glass-attached B8-1 + A3 biofilm are not resolved in `PMID:42587276`.
   - **History Sidecar**: `history/records/Bacillus_B81_A3_Naphthalene_Biofilm_Consortium_2/2026-11-04T133500Z-antigravity-c6s203.yaml`.

4. **`CommunityMech:000504` (`kb/communities/Bacillus_B81_A1_A3_PAH_Biofilm_Consortium_4.yaml`)**
   - **SHA-256**: `bf6e05a86bd9413d4ca63a676c2a4fa519c414549151cccba8c312ab86238747` → `49c084f295ba077f383e193820af2dd4a1620e0af6310110f2da9eb71a4d77a8`
   - **Primary Source**: `PMID:42587276` (`PMC13471667`, `doi:10.1186/s12866-026-05144-y`, `references_cache/PMID_42587276.txt`)
   - **Mechanism Representation (2 `COMMUNITY_LEVEL` nodes, 0 downstream edges)**:
     - `Consortium 4 Three-Strain Planktonic and Biofilm Naphthalene Biodegradation`: Added verbatim snippet for the proposed biotransformation-product cross-feeding hypothesis (`"One possible reason that makes the bacterial consortia have a superior naphthalene biodegradation efficiency is that, during the process of biotransformation, the product of one bacterium can be employed as the foundation for the catabolism and growth of another."`) and bounded three-strain HPLC parent-substrate removal (`64.47%` planktonic, `79.74%` glass-attached biofilm) relative to two-strain Consortium 3 (`92.43%` planktonic / `94.69%` biofilm).
     - `Consortium 4 Three-Strain Phenanthrene Antagonism`: Added verbatim snippet (`"On the contrary, the isolate B8-1 exhibited a biodegradation rate, in the planktonic mode, of 77.94% that relatively higher than that obtained in its biofilm mode, 60.72% (see Fig. 8 a)."`) anchoring B8-1 single-strain phenanthrene removal (`77.94%` planktonic / `60.72%` biofilm) within the `60.72-77.94%` single-strain range cited in the node description.
   - **Taxon Grounding**: Verified `Bacillus paramycoides B8-1` (`NCBITaxon:2026194`), `Bacillus paranthracis A1` (`NCBITaxon:2026186`), and `Bacillus licheniformis A3` (`NCBITaxon:1402`, `GTDB:s__Bacillus_licheniformis`) synchronization across `taxonomy` and `participating_taxa`.
   - **Source-Limited Gaps**: Pairwise inhibitory interactions and metabolic fluxes explaining why three-strain Consortium 4 underperforms two-strain A1+A3 Consortium 3 on naphthalene and single isolates on phenanthrene are not dissected beyond bulk HPLC removal in `PMID:42587276`.
   - **History Sidecar**: `history/records/Bacillus_B81_A1_A3_PAH_Biofilm_Consortium_4/2026-11-04T133500Z-antigravity-c6s204.yaml`.

## 3. Verification of Previously Reviewed (440) & `needs_research` (54) Records

- **440 Previously `reviewed` `MicrobialCommunity` Records**:
  - SHA-256 hash comparison against `reports/causal_graph_review/inventory.tsv` confirmed **0 hash drift** (`drift == []`).
- **54 `needs_research` `MicrobialCommunity` Records**:
  - Audited against `references_cache/`, `reports/drc/`, and `research/`: **0** of the 54 abstract-limited or paywalled records gained new cached open-access full text or deep-research reports since Cycle 5 Stage 2. Per repository policy, paid provider credits were not spent and no unsupported causal edges were fabricated; all 54 records remain explicitly tracked as `needs_research` in `reports/causal_graph_review/inventory.tsv`.
- **2 `CommonTaxon` Records (`kb/taxa/`)**:
  - Verified `kb/taxa/Geobacter_sulfurreducens.yaml` (`sha256: 5d2b49dc2fd42756bdc303302e135ad208c10f76de161e618545a99dd1f6e142`) and `kb/taxa/Shewanella_oneidensis_MR1.yaml` (`sha256: df038771231777f9846f246f0c578484c697845043103008586e813badd113f8`) pass `just validate-taxa` and `just validate-terms-taxa`.
- **Representation & Writer Blockers**:
  - **0** representation or writer blockers encountered (`write_validated_community` and `record_curation_event` handled all Batch 138 edits cleanly, and `scripts/audit_causal_graphs.py` + `reports/causal_graph_review/build_inventory.py` confirm `structural_defects == []` across all 498 `MicrobialCommunity` records).
