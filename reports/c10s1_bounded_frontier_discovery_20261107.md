# Cycle 10 Stage 1 (`add_records`) Bounded-Frontier Discovery & Curation Report (2026-11-07)

## 1. Executive Summary

During **Run `mech-goal-sequence-20261019`, Cycle 10, Stage 1 (`add_records`)**, we executed a repeated, recorded search of the local bounded frontier (`references_cache/`, `research/scouting/`, `research/communities/`, `notes/new-communities-to-create.md`, `notes/new-datasets-to-curate.md`, `kb/communities/`, `data/isolates/`, and `kb/taxa/`) following the repository-local [`add-community-record`](../.claude/skills/add-community-record/SKILL.md), [`scout-communities`](../.claude/skills/scout-communities/SKILL.md), [`ground-causal-graph-taxa`](../.claude/skills/ground-causal-graph-taxa/SKILL.md), and [`ground-taxa-gtdb`](../.claude/skills/ground-taxa-gtdb/SKILL.md) skills:

- **Pre-Stage Corpus Inventory**:
  - `kb/communities/*.yaml`: **505** records (`507` post-stage)
  - `data/isolates/*.yaml`: **10** records (`12` post-stage)
  - `kb/taxa/*.yaml`: **2** records (`2` post-stage)
  - Total `MicrobialCommunity` records: **515** pre-stage (`CommunityMech:000001`–`CommunityMech:000521`, with 6 historical ID gaps: `000212, 000228, 000229, 000230, 000231, 000232`; **517** total corpus records including `2` `CommonTaxon` records in `kb/taxa/`), **519** post-stage (`CommunityMech:000001`–`CommunityMech:000525`, with the same 6 historical ID gaps; **521** total corpus records including `2` `CommonTaxon` records in `kb/taxa/`)
  - Highest existing `CommunityMech:` identifier pre-stage: `CommunityMech:000521` ([data/isolates/Pseudomonas_Protegens_E1BL2_Jala_Maize_Isolate_Baseline.yaml](../data/isolates/Pseudomonas_Protegens_E1BL2_Jala_Maize_Isolate_Baseline.yaml))
- **Pass 1 Discovery & Curation**:
  - Identified **2 admissible, experimentally characterized defined synthetic/engineered microbial communities (`CommunityMech:000522`–`CommunityMech:000523`) in `kb/communities/` and 2 admissible single-strain isolate baselines (`CommunityMech:000524`–`CommunityMech:000525`) in `data/isolates/`** across two committed full-text reference caches (`PMID:41859451` and `PMID:42733304`), where 100% of member taxa are grounded at their exact source-supported rank in the offline `cache/ncbitaxon/terms.csv` ontology cache, all `related_communities` links satisfy `src/communitymech/validators/related_communities.py` without requiring mutations to pre-existing corpus records, and every claim is backed by verbatim snippets in `references_cache/`:
    1. **`CommunityMech:000522`** — [Parmigiano_NWS_Set3_LAB_Triculture.yaml](../kb/communities/Parmigiano_NWS_Set3_LAB_Triculture.yaml) (*Parmigiano NWS Set 3 LAB Triculture*, defined 1:1:1 milk triculture of *Lactobacillus helveticus* `C001.15` [`NCBITaxon:1587`, `UNRESOLVED`], *Streptococcus thermophilus* `RBC06` [`NCBITaxon:1308`, `GROUNDED`: `GTDB:s__Streptococcus_thermophilus`], and *Lactobacillus delbrueckii* subsp. *lactis* `C5I3` [`NCBITaxon:29397`, `UNRESOLVED`] fermented at `2 × 10^7 CFU/mL` total final cell concentration in `40 mL` partially skimmed UHT milk at `42 °C` for `160 h` in inoculation set 3 from `PMID:41859451` / `doi:10.3389/fmicb.2026.1755652`).
    2. **`CommunityMech:000523`** — [SO2_BS1_Lithium_Battery_Bioleaching_Consortium.yaml](../kb/communities/SO2_BS1_Lithium_Battery_Bioleaching_Consortium.yaml) (*SO2-BS1 Lithium-ion Battery Bioleaching Consortium*, intermediate 2-member engineered consortium of *Shewanella oneidensis* MR-1 `SO2` [`SO1` carrying `Ptac::ribADEHC` on `pHG13`, `NCBITaxon:70863`, `GROUNDED`: `GTDB:s__Shewanella_oneidensis`, `common_taxon: CommunityMech:taxon:000001`] and *Bacillus subtilis* 168 `BS1` [`BS0` carrying `P43::adh-aldH` on `pCE2`, `NCBITaxon:1423`, `GROUNDED`: `GTDB:s__Bacillus_subtilis`] derived from `SO1-BS1` [`CommunityMech:000519`, `DERIVED_FROM`], synthesizing `3.65 µM` riboflavin (`13.22-fold` over `SO1-BS1`), reaching `243.71 mW m^-2` maximum power density (`2.10-fold` over `SO1-BS1`), and leaching `64.1 mg L^-1` total Li, Ni, Co, and Mn (`53.1, 4.7, 1.9, and 4.4 mg L^-1`; `16.4 mg L^-1 day^-1` maximal rate) from `PMID:42733304` / `doi:10.1002/advs.77699`).
    3. **`CommunityMech:000524`** — [Shewanella_Oneidensis_SO1_NCM_Bioleaching_Isolate_Baseline.yaml](../data/isolates/Shewanella_Oneidensis_SO1_NCM_Bioleaching_Isolate_Baseline.yaml) (*Shewanella oneidensis MR-1 SO1 Brewing-Wastewater NCM Bioleaching Isolate Baseline*, single-strain electrogenic monoculture baseline [`NCBITaxon:70863`, `GROUNDED`: `GTDB:s__Shewanella_oneidensis`, `common_taxon: CommunityMech:taxon:000001`] demonstrating `61.62-fold` inhibition of extracellular electron transfer power density by `1.8% (v/v)` ethanol (`2.08` vs `128.20 mW m^-2`), `3.10 mW m^-2` power density in Moutai brewing wastewater, and `15.4 mg L^-1` total dissolved Li, Ni, Co, and Mn leaching over 14 days from `PMID:42733304` / `doi:10.1002/advs.77699`, linked bidirectionally via `SAME_STUDY_AS` to `CommunityMech:000523` and `CommunityMech:000525`).
    4. **`CommunityMech:000525`** — [Bacillus_Subtilis_BS1_Brewing_Wastewater_Isolate_Baseline.yaml](../data/isolates/Bacillus_Subtilis_BS1_Brewing_Wastewater_Isolate_Baseline.yaml) (*Bacillus subtilis 168 BS1 Brewing-Wastewater Ethanol-Detoxifying Isolate Baseline*, single-strain engineered `P43::adh-aldH` ethanol-detoxifying partner monoculture baseline [`NCBITaxon:1423`, `GROUNDED`: `GTDB:s__Bacillus_subtilis`] generating `1.25 mW m^-2` maximum power density and `3.8 mg L^-1` total dissolved Li, Ni, Co, and Mn leaching over 14 days in Moutai brewing wastewater from `PMID:42733304` / `doi:10.1002/advs.77699`, linked bidirectionally via `MEMBER_SUBSET_OF` / `MEMBER_SUPERSET_OF` and `SAME_STUDY_AS` to `CommunityMech:000523` and via `SAME_STUDY_AS` to `CommunityMech:000524`).
- **Pass 2 Repeated Bounded-Frontier Search**:
  - Re-ran the bounded-frontier audit across all **988** files in `references_cache/` (`953` top-level files: `429` `.txt`, `439` `.md`, `85` `.json`, plus `35` files in `references_cache/edison/`), all **34** scouting files in `research/scouting/` (`4485` candidate rows, `855` unique references), `research/communities/`, `notes/new-communities-to-create.md`, `notes/new-datasets-to-curate.md`, and all **519** curated `MicrobialCommunity` records (`507` in `kb/communities/` + `12` in `data/isolates/`) plus `2` `CommonTaxon` records in `kb/taxa/` (`521` corpus records total).
  - Verified all **67/67** snippets across `CommunityMech:000522`–`CommunityMech:000525` (`24` in `000522`, `21` in `000523`, `11` in `000524`, `11` in `000525`) against `references_cache/` (`67/67` `MATCH` in `scripts/evidence_snippet_audit.py` with `0` `MISMATCH`, `0` `RENDERING`, `0` `ASSEMBLED`, `0` `WEAK`, `0` `NOCONTENT`, and `0` issues across all 4 records in `validate_strict.py`, `linkml-reference-validator`, `linkml-term-validator`, and `communitymech audit-network`).
  - Confirmed **0 further admissible new community or isolate records** exist within the offline-verifiable bounded frontier.

---

## 2. Newly Curated Community and Isolate Records (`CommunityMech:000522`–`CommunityMech:000525`)

| ID | File Path | Name | Source | Members & NCBITaxon / GTDB Grounding | Key Curated Outcomes |
|---|---|---|---|---|---|
| `CommunityMech:000522` | `kb/communities/Parmigiano_NWS_Set3_LAB_Triculture.yaml` | Parmigiano NWS Set 3 LAB Triculture | `PMID:41859451` (`doi:10.3389/fmicb.2026.1755652`) | *Lactobacillus helveticus* C001.15 (`NCBITaxon:1587`, `UNRESOLVED`), *Streptococcus thermophilus* RBC06 (`NCBITaxon:1308`, `GROUNDED`: `GTDB:s__Streptococcus_thermophilus`), *Lactobacillus delbrueckii* subsp. *lactis* C5I3 (`NCBITaxon:29397`, `UNRESOLVED`) | Defined 1:1:1 species-level LAB triculture (`set 3`) inoculated at `2 × 10^7 CFU/mL` total final cell density in `40 mL` partially skimmed UHT milk at `42 °C` for `160 h`; displayed the highest maximum acidification rate (`μmax`), highest maximum fermentative efficiency (`ΔpHmax`), and highest total lactic acid production relative to monocultures and 1:1 co-cultures (`p < 0.05`), resolved mutualistic `RBC06 + C5I3` and `RBC06 + C001.15` (`86.73%` L-lactate) pairs versus antagonistic `C001.15 + C5I3` (`56.63%` D-lactate), and produced balanced D-/L-lactate in the triculture without significantly exceeding the `C5I3` monoculture D-lactate baseline. |
| `CommunityMech:000523` | `kb/communities/SO2_BS1_Lithium_Battery_Bioleaching_Consortium.yaml` | SO2-BS1 Lithium-ion Battery Bioleaching Consortium | `PMID:42733304` (`doi:10.1002/advs.77699`) | *Shewanella oneidensis* MR-1 `SO2` (`NCBITaxon:70863`, `GROUNDED`: `GTDB:s__Shewanella_oneidensis`, `common_taxon: CommunityMech:taxon:000001`), *Bacillus subtilis* 168 `BS1` (`NCBITaxon:1423`, `GROUNDED`: `GTDB:s__Bacillus_subtilis`) | Intermediate 2-member engineered consortium derived from `SO1-BS1` (`CommunityMech:000519`, `DERIVED_FROM`) by overexpressing `Ptac::ribADEHC` in *S. oneidensis* `SO2` while retaining *B. subtilis* `BS1` (`P43::adh-aldH`); synthesized `3.65 µM` riboflavin (`13.22-fold` over `SO1-BS1` at `0.276 µM`), reached `243.71 mW m^-2` maximum power density (`2.10-fold` over `SO1-BS1` at `116.15 mW m^-2`), and leached `64.1 mg L^-1` total dissolved Li, Ni, Co, and Mn (`53.1, 4.7, 1.9, and 4.4 mg L^-1`; `66.5%, 18.6%, 20.2%, and 33.3%` efficiencies; `16.4 mg L^-1 day^-1` maximal rate) before late-stage Ni2+/Co2+ accumulation reduced the average leaching rate from `9.867 mg L^-1 day^-1` (days 1–6) to `0.617 mg L^-1 day^-1` (days 7–14). |
| `CommunityMech:000524` | `data/isolates/Shewanella_Oneidensis_SO1_NCM_Bioleaching_Isolate_Baseline.yaml` | Shewanella oneidensis MR-1 SO1 Brewing-Wastewater NCM Bioleaching Isolate Baseline | `PMID:42733304` (`doi:10.1002/advs.77699`) | *Shewanella oneidensis* MR-1 `SO1` (`NCBITaxon:70863`, `GROUNDED`: `GTDB:s__Shewanella_oneidensis`, `common_taxon: CommunityMech:taxon:000001`) | Single-strain electrogenic monoculture baseline (`wild-type S. oneidensis MR-1` carrying `pHG13`, `Cmr`) evaluated alongside `BS1` monoculture (`CommunityMech:000525`) and the engineered consortia in Moutai brewing wastewater; demonstrated `61.62-fold` inhibition of MFC maximum power density by `1.8% (v/v)` ethanol (`2.08` vs `128.20 mW m^-2`), `3.10 mW m^-2` power density in brewing wastewater (`34.47-fold` below `SO1-BS1`), and `15.4 mg L^-1` total dissolved NCM metal leaching over 14 days (`4.53-fold` above cell-free wastewater at `3.4 mg L^-1` and `3.29-fold` below `SO1-BS1` at `50.7 mg L^-1`). |
| `CommunityMech:000525` | `data/isolates/Bacillus_Subtilis_BS1_Brewing_Wastewater_Isolate_Baseline.yaml` | Bacillus subtilis 168 BS1 Brewing-Wastewater Ethanol-Detoxifying Isolate Baseline | `PMID:42733304` (`doi:10.1002/advs.77699`) | *Bacillus subtilis* 168 `BS1` (`NCBITaxon:1423`, `GROUNDED`: `GTDB:s__Bacillus_subtilis`) | Single-strain engineered ethanol-detoxifying partner baseline (`BS0` carrying `P43::adh` from *S. cerevisiae* BY4341 and `aldH` from *I. terricola* XJ-2 on `pCE2`, `Cmr`, linked via `MEMBER_SUBSET_OF` to `CommunityMech:000523`); oxidized residual brewing-wastewater ethanol to acetaldehyde and acetate via the heterologous Adh-AldH cascade (contrasting with `~35.6%` ethanol removal by wild-type `BS0`), while generating only `1.25 mW m^-2` standalone MFC power density (`92.92-fold` below `SO1-BS1`) and `3.8 mg L^-1` standalone NCM metal leaching over 14 days (`13.34-fold` below `SO1-BS1`). |

---

## 3. Preserved Unresolved Candidates & Search Limits

### 3.1 Candidates Sharing Strain Designations with Pre-Existing Fully Strain-Designated Corpus Records (`related_communities` Inverse-Link Boundary)

Per `src/communitymech/validators/related_communities.py`, any two records in the corpus whose `taxonomy` slots are 100% strain-designated and share `>= 1` normalized strain designation must carry reciprocal `related_communities` links (`SHARED_STRAIN_DESIGNATIONS` for `MEMBER_SUBSET_OF`/`MEMBER_SUPERSET_OF`/`OVERLAPPING_MEMBERSHIP`, or `SAME_STUDY_AS` where strain sets are disjoint), unless one of the records has at least one member without `strain_designation.strain_name` (in which case `_strain_set` returns `None` and only `DERIVED_FROM` / `SAME_STUDY_AS` links apply). Because Stage 1 (`add_records`) is scoped to adding new records without mutating pre-existing community records, the following multi-consortium candidates that share strains with fully strain-designated pre-existing corpus records remain documented and preserved:

1. **`PMID:42602126` (`doi:10.1186/s40793-026-00926-z`) — `SC-1` through `SC-6` (6-strain *Medicago sativa* mercury-phytoremediation consortia)**:
   - **Status**: **Deferred (`shared_strain_requires_existing_record_edit`)**.
   - **Details**: Share strains `CAR08` and/or `Lupac 08` with fully strain-designated existing `Mercury_Resistant_Alfalfa_PGPR_Consortium_SC7` ([CommunityMech:000427](../kb/communities/Mercury_Resistant_Alfalfa_PGPR_Consortium_SC7.yaml)), requiring inverse `OVERLAPPING_MEMBERSHIP` edits on `CommunityMech:000427`.
2. **`PMID:35444261` (`doi:10.3389/fpls.2022.866065`) — 15-strain Jizan Desert Plant Endophyte SynCom**:
   - **Status**: **Deferred (`shared_strain_requires_existing_record_edit`)**.
   - **Details**: Supersets the 5 strains (`SA087`, `SA187`, `SA403`, `SA436`, `SA444`) of fully strain-designated existing `Heat_Responsive_Desert_Plant_Endophyte_SynCom` ([CommunityMech:000096](../kb/communities/Heat_Responsive_Desert_Plant_Endophyte_SynCom.yaml)), requiring an inverse `MEMBER_SUBSET_OF` (`SHARED_STRAIN_DESIGNATIONS`) edit on `CommunityMech:000096`.
3. **`PMID:36118206` (`doi:10.3389/fmicb.2022.908981`) — Single-strain wheat rhizosphere isolates (`Pseudomonas` sp. B5, `Streptomyces` sp. B6, `Chryseobacterium` sp. B7, `Pseudomonas` sp. B11)**:
   - **Status**: **Deferred (`shared_strain_requires_existing_record_edit`)**.
   - **Details**: Share strains `B5`, `B6`, `B7`, `B11` with fully strain-designated existing `Wheat_Consortium_C1` (`000076`), `Wheat_Consortium_C6` (`000077`), and `Wheat_Consortium_C7` (`000514`), requiring inverse `MEMBER_SUPERSET_OF` edits on those existing community records.

### 3.2 Candidates Blocked by Offline NCBITaxon Term Cache Gaps (`cache/ncbitaxon/terms.csv` — Issue `#708`)

1. **`PMID:37275168` (`doi:10.3389/fmicb.2023.1167839`) — `SynCom 1` (7 strains) and `SynCom 2` (5 strains)**:
   - **Status**: **Deferred (`offline_ncbi_term_cache_gap` — Issue `#708`)**.
   - **Details**: Both `SynCom 1` and `SynCom 2` contain *Phytobacter diazotrophicus* `Z2WL1` (GenBank `MK855127`), whose genus *Phytobacter* and species *Phytobacter diazotrophicus* (`NCBITaxon:395631`) are absent from `cache/ncbitaxon/terms.csv` (and both also share strains with existing `Jala_Maize_PGPB_SynCom` `CommunityMech:000441`).
2. **`PMID:42135302` (`doi:10.1038/s41598-026-49136-4`) — `Consortia-B18-4M11` (*Lysinibacillus* sp. SK18-4 [`MK554502`] + *Bacillus* sp. KH5M11 [`MK634660`])**:
   - **Status**: **Deferred (`offline_ncbi_term_cache_gap` — Issue `#708`)**.
   - **Details**: Genus *Lysinibacillus* (`NCBITaxon:400634`) is absent from `cache/ncbitaxon/terms.csv`.
3. **`PMID:35699440`, `PMID:36118206` (`C2`–`C5`, `C8`–`C10`), `PMID:42121419` (`SC1`, `SC2`), `PMID:42032280` (`Consortium 1`)**:
   - **Status**: **Deferred (`offline_ncbi_term_cache_gap` — Issue `#708`)**.
   - **Details**: Previously documented species-level NCBITaxon gaps (*Methanobrevibacter arboriphilus* `NCBITaxon:2173`, *Chryseobacterium soldanellicola*, *Cupriavidus campinensis*, *Rhodococcus erythropolis*, *Janthinobacterium lividum*, *Wickerhamomyces anomalus*, *Prevotella ruminicola* `NCBITaxon:839`, *Megasphaera elsdenii* `NCBITaxon:907`) remain absent from `cache/ncbitaxon/terms.csv`.

### 3.3 Candidates with Strain Membership Only in External Supplementary Tables or Figures (`#1996`)

1. **`PMID:35992653` (`doi:10.3389/fmicb.2022.967885`) — `SynCom 1.0` (44 banana root-endosphere isolates)**:
   - **Status**: **Deferred (`supplement_only_strain_membership` in `Supplementary Table S2`; `SynCom 1.1` is curated as `CommunityMech:000518` and `SynCom 1.2` is curated as `CommunityMech:000097`)**.
2. **`PMID:40663585` (`doi:10.1371/journal.pbio.3003269`) — `AtSC5`, `AtSC6`, `LjSC5`, `LjSC6` (45-strain cross-host core and variable root microbiota SynComs)**:
   - **Status**: **Deferred (`supplement_only_strain_membership` in `S1 Table`)**.
3. **`PMID:41634815` (`SynCom5`)** and **`PMID:42592155` (`ΔargA-ΔtrpR / ΔtrpC-ΔargR`)**:
   - **Status**: **Deferred (`figure_or_supplement_only_strain_membership`)**.

### 3.4 Abstract-Only / Uncached Scouting Candidates (`research/scouting/`)

- All **855** unique references across the **34** scouting files in `research/scouting/` (`4485` rows) remain audited:
  - **28** unique references (`83` rows) map to curated `MicrobialCommunity` records in `kb/communities/` or `data/isolates/`.
  - **10** uncurated scouting references have cached text in `references_cache/` (`PMID:38396045`, `PMID:40404721`, `PMID:41103940`, `PMID:41620521`, `PMID:41664180`, `PMID:41774312`, `PMID:41787314`, `PMID:41900249`, `PMID:41939321`, `PMID:41957634`), all 10 of which remain **abstract-only** (`1482–2889` chars) without strain-level composition or quantitative mechanism tables.
  - **817** unique references (`4347` rows) have no local text in `references_cache/` and cannot be promoted without network fetching (`--no-fetch-missing`).

---

## 4. Validation Summary

All 4 newly created records (`CommunityMech:000522`–`CommunityMech:000525`) and their 4 append-only history sidecars passed every validation gate:

1. **Guarded Writer (`communitymech.validation.write_validated.write_validated_community`)**:
   - All 4 YAML records were written via `write_validated_community(...)` (enforcing `linkml-validate`, `validate-strict` closed-schema/cross-field/scalar/GTDB/related-communities checks, `linkml-term-validator` ontology label bindings, and `linkml-reference-validator` offline snippet verification against `references_cache/`).
2. **Closed-Schema & Cross-Field Validation (`scripts/validate_strict.py`)**:
   - `files scanned: 4 | files with ERROR: 0 | total ERROR rows: 0`.
3. **Evidence Snippet Audit (`scripts/evidence_snippet_audit.py`)**:
   - `67/67` snippets (`100%`) `MATCH` verbatim against `references_cache/` (`0` `RENDERING`, `0` `ASSEMBLED`, `0` `WEAK`, `0` `MISMATCH`, `0` `NOCONTENT`).
4. **History Schema Validation (`linkml-validate -s src/communitymech/schema/history.yaml -C RecordHistory`)**:
   - All 4 append-only history records under `history/records/` passed with `No issues found`.
5. **Generated HTML & Browser Site (`communitymech.render` + `scripts/check_docs_current.py`)**:
   - Regenerated `docs/` (`507` community pages rendered) and verified `docs/ is current with kb/communities/ and templates.`.

---

## 5. Provenance & Append-Only History Sidecars

- `history/records/Parmigiano_NWS_Set3_LAB_Triculture/2026-11-07T103500Z-antigravity-000522.yaml`
- `history/records/SO2_BS1_Lithium_Battery_Bioleaching_Consortium/2026-11-07T103500Z-antigravity-000523.yaml`
- `history/records/Shewanella_Oneidensis_SO1_NCM_Bioleaching_Isolate_Baseline/2026-11-07T103500Z-antigravity-000524.yaml`
- `history/records/Bacillus_Subtilis_BS1_Brewing_Wastewater_Isolate_Baseline/2026-11-07T103500Z-antigravity-000525.yaml`
