# Cycle 11 Stage 1 Bounded-Frontier Discovery Report (`2026-11-08`)

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle / Stage**: Cycle 11, Stage 1 (`add_records`)
- **Base Commit (`main`)**: `8eb2e616feafda46f9fc7ef4d0b231d330908493` (PR `#2725` merge commit)
- **Feature Branch**: `c11s1-add-records-20261107`

## 1. Bounded-Frontier Scope and Search Protocol

Following the repository-local discovery and curation skills ([add-community-record](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.claude/skills/add-community-record/SKILL.md), [scout-communities](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.claude/skills/scout-communities/SKILL.md), [manage-identifiers](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.claude/skills/manage-identifiers/SKILL.md), [curate-yaml-record](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.claude/skills/curate-yaml-record/SKILL.md), and [review-communities](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.claude/skills/review-communities/SKILL.md)), we conducted a two-pass bounded-frontier scan across all local evidence and candidate sources without paid provider calls or promotion of unverified scouting stubs:

1. **Committed Full-Text & Abstract Reference Cache** (`references_cache/*.md`, `references_cache/*.txt` — `1,158` files):
   - Audited all full-text and abstract cache files for experimentally characterized multi-species microbial consortia (`kb/communities/`) and single-strain isolate baselines (`data/isolates/`) that were not yet represented as standalone records in the corpus (`507` `kb/communities/*.yaml`, `12` `data/isolates/*.yaml`, `2` `kb/taxa/*.yaml` at Stage 1 start; highest existing ID `CommunityMech:000525`).
2. **Scouting Queue and Deep-Research Artifacts** (`research/scouting/`, `research/communities/`, `notes/curation-When-the-Watchdog-Bites-20260417/`):
   - Cross-checked all candidate queues, scouted papers, and draft notes against curated PMIDs, DOIs, and strain rosters across `kb/communities/` and `data/isolates/`.

---

## 2. Pass 1: Admissible Candidates Identified and Curated (`CommunityMech:000526`–`CommunityMech:000530`)

In Pass 1, inspection of the committed open-access full text of Zhang et al. 2026 (*Adv Sci* `e77699`, `PMID:42733304`, `PMC13572860`, [PMID_42733304.txt](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/references_cache/PMID_42733304.txt)) identified **five** experimentally characterized engineered consortia and single-strain isolate baselines in Table 1, Section 2.2 (Figure 2a,b), Section 2.4 (Figure 4c–g), and Section 2.5 (Figure 5c,d) that had verbatim full-text evidence and distinct strain rosters (`SO3ΔmtrC` + `BS3`, `SO3ΔomcA` + `BS3`, `SO3ΔmtrCΔomcA` + `BS3`, sole strain `BS3`, and wild-type strain `BS0`):

| Minted ID | Record Path | Root Class / Placement | Strain Roster (`strain_designation.strain_name`) | Quantitative Phenotype & Evidence Summary (`PMID:42733304`) | Reciprocal `related_communities` Links |
|---|---|---|---|---|---|
| `CommunityMech:000526` | [kb/communities/SO3_DeltaMtrC_BS3_Lithium_Battery_Bioleaching_Consortium.yaml](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/kb/communities/SO3_DeltaMtrC_BS3_Lithium_Battery_Bioleaching_Consortium.yaml) | `MicrobialCommunity` (`kb/communities/`) | `SO3ΔmtrC` (*S. oneidensis* MR-1 $\Delta mtrC$ + `pHG13-Ptac-ribADEHC-irrE`), `BS3` (*B. subtilis* 168 `BS2` + `pCE2-P43::irrE`) | Outer-membrane decaheme cytochrome $mtrC$ deletion perturbation consortium: MFC maximum power density `47.67 mW m^-2` (`9.50-fold` decrease vs `SO3-BS3` at `452.90 mW m^-2`, Figure 5c) and 14-day total leached NCM metal ions `16.7 mg L^-1` (`6.13-fold` decrease vs `SO3-BS3` at `102.4 mg L^-1`, Figure 5d). | `DERIVED_FROM` `000385`; `MEMBER_SUPERSET_OF` & `SAME_STUDY_AS` `000529`; `OVERLAPPING_MEMBERSHIP` & `SAME_STUDY_AS` `000527`, `000528`; `SAME_STUDY_AS` `000530` |
| `CommunityMech:000527` | [kb/communities/SO3_DeltaOmcA_BS3_Lithium_Battery_Bioleaching_Consortium.yaml](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/kb/communities/SO3_DeltaOmcA_BS3_Lithium_Battery_Bioleaching_Consortium.yaml) | `MicrobialCommunity` (`kb/communities/`) | `SO3ΔomcA` (*S. oneidensis* MR-1 $\Delta omcA$ + `pHG13-Ptac-ribADEHC-irrE`), `BS3` (*B. subtilis* 168 `BS2` + `pCE2-P43::irrE`) | Outer-membrane decaheme cytochrome $omcA$ deletion perturbation consortium: MFC maximum power density `50.01 mW m^-2` (`9.05-fold` decrease vs `SO3-BS3` at `452.90 mW m^-2`, Figure 5c) and 14-day total leached NCM metal ions `18.7 mg L^-1` (`5.48-fold` decrease vs `SO3-BS3` at `102.4 mg L^-1`, Figure 5d). | `DERIVED_FROM` `000385`; `MEMBER_SUPERSET_OF` & `SAME_STUDY_AS` `000529`; `OVERLAPPING_MEMBERSHIP` & `SAME_STUDY_AS` `000526`, `000528`; `SAME_STUDY_AS` `000530` |
| `CommunityMech:000528` | [kb/communities/SO3_DeltaMtrC_DeltaOmcA_BS3_Lithium_Battery_Bioleaching_Consortium.yaml](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/kb/communities/SO3_DeltaMtrC_DeltaOmcA_BS3_Lithium_Battery_Bioleaching_Consortium.yaml) | `MicrobialCommunity` (`kb/communities/`) | `SO3ΔmtrCΔomcA` (*S. oneidensis* MR-1 $\Delta mtrC\Delta omcA$ + `pHG13-Ptac-ribADEHC-irrE`), `BS3` (*B. subtilis* 168 `BS2` + `pCE2-P43::irrE`) | Double outer-membrane cytochrome $\Delta mtrC\Delta omcA$ deletion consortium: MFC maximum power density `28.39 mW m^-2` (`15.95-fold` decrease vs `SO3-BS3` at `452.90 mW m^-2`, Figure 5c) and 14-day total leached NCM metal ions `13.4 mg L^-1` (`7.64-fold` decrease vs `SO3-BS3` at `102.4 mg L^-1`, indistinguishable from sole strain `BS3` monoculture at `13.4 mg L^-1`, Figure 5d). | `DERIVED_FROM` `000385`; `MEMBER_SUPERSET_OF` & `SAME_STUDY_AS` `000529`; `OVERLAPPING_MEMBERSHIP` & `SAME_STUDY_AS` `000526`, `000527`; `SAME_STUDY_AS` `000530` |
| `CommunityMech:000529` | [data/isolates/Bacillus_Subtilis_BS3_Brewing_Wastewater_Isolate_Baseline.yaml](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/data/isolates/Bacillus_Subtilis_BS3_Brewing_Wastewater_Isolate_Baseline.yaml) | `MicrobialCommunity` (`data/isolates/`) | `BS3` (*B. subtilis* 168 `BS2` carrying `P43::irrE` from *D. radiodurans* R1 on `pCE2`, `Cmr`) | Single-strain metal-resistant isolate baseline: `54.2%` reduction in comet-assay DNA tail length (`31.0` to `14.2 um`, Figure 4c), `67.4%` reduction in intracellular ROS fluorescence (Figure 4d), `OD600,max` increase from `0.830` (`BS2`) to `1.175` under `6 mg L^-1 Ni2+` and `3 mg L^-1 Co2+` (Figure 4f), and `13.4 mg L^-1` standalone 14-day NCM metal leaching (Figure 5d). | `MEMBER_SUBSET_OF` & `SAME_STUDY_AS` `000526`, `000527`, `000528`; `SAME_STUDY_AS` `000530` |
| `CommunityMech:000530` | [data/isolates/Bacillus_Subtilis_BS0_Brewing_Wastewater_Isolate_Baseline.yaml](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/data/isolates/Bacillus_Subtilis_BS0_Brewing_Wastewater_Isolate_Baseline.yaml) | `MicrobialCommunity` (`data/isolates/`) | `BS0` (wild-type *B. subtilis* 168 containing plasmid `pCE2`, `Cmr`) | Single-strain wild-type isolate baseline: reaches `OD600,max` of `0.641` in Moutai brewing wastewater (vs `0.884` for `BS1`, Figure 2a) and removes `~35.6%` of ethanol within 48 h, lowering ethanol from `1.8%` to `1.16% (v/v)` (vs `99.4%` removal to `0.01% v/v` by `BS1`, Figure 2b). | `SAME_STUDY_AS` `000526`, `000527`, `000528`, `000529` |

All five records were written through [`write_validated_community`](file:///Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/src/communitymech/validation/write_validated.py#L99-L129) and paired with validated `RecordHistory` sidecars under `history/records/`.

---

## 3. Pass 2: Repeated Bounded-Frontier Search After Curation

After adding `CommunityMech:000526`–`CommunityMech:000530` (bringing the corpus to `510` `kb/communities/*.yaml`, `14` `data/isolates/*.yaml`, and `2` `kb/taxa/*.yaml`; `526` total records), we re-ran the bounded-frontier search across all local sources:

1. **`references_cache/PMID_42733304.txt` (Zhang et al. 2026)**:
   - Every multi-species consortium tested in `PMID:42733304` is now curated as a dedicated record:
     - `SO1-BS1` (`CommunityMech:000519`)
     - `SO2-BS1` (`CommunityMech:000523`)
     - `SO2-BS2` (`CommunityMech:000520`)
     - `SO3-BS3` (`CommunityMech:000385`)
     - `SO3ΔmtrC-BS3` (`CommunityMech:000526`)
     - `SO3ΔomcA-BS3` (`CommunityMech:000527`)
     - `SO3ΔmtrCΔomcA-BS3` (`CommunityMech:000528`)
   - Single-strain isolate baselines tested with standalone NCM leaching or ethanol-removal curves in `PMID:42733304`:
     - `SO1` monoculture (`CommunityMech:000524`)
     - `BS1` monoculture (`CommunityMech:000525`)
     - `BS3` monoculture (`CommunityMech:000529`)
     - `BS0` monoculture (`CommunityMech:000530`)
   - Remaining strains in Table 1 (`SO2`, `SO3`, `BSG3`, `BS2`):
     - `BSG3` has an unknown mutation-bred genotype (`the genotype of which is still unknown`) and no standalone fermentation or bioleaching assay data in `PMID:42733304`.
     - `SO2`, `SO3`, and `BS2` are only assayed for cell viability (`OD600`, comet DNA tail length, CM-H2DCFDA ROS fluorescence, and live-dead staining under `6 mg L^-1 Ni2+` and `3 mg L^-1 Co2+` in ethanol-free test medium, Section 2.4 Figure 4c–g) without standalone brewing-wastewater ethanol fermentation, MFC power density, or NCM black-mass bioleaching assays, and their `Ni2+/Co2+` stress comparisons are already captured with verbatim evidence in `CommunityMech:000520` (`SO2-BS2`), `CommunityMech:000385` (`SO3-BS3`), and `CommunityMech:000529` (`BS3`).
2. **All other full-text cache files (`references_cache/*.txt`, `references_cache/*.md`)**:
   - `PMID:41859451` (`PMC12992708`): both defined consortia (`Met-3` [`CommunityMech:000521`] and `9-Mix` [`CommunityMech:000522`]) and the 24-strain mother community (`CommunityMech:000415`) are already curated; single-strain drop-out/screening entries lack standalone isolate-baseline mechanism graphs.
   - `PMID:41802591`, `PMID:41862205`, `PMID:42622731`, `PMID:42762737`, `PMID:42304541`, `PMID:41908926`: all admissible defined consortia and isolate baselines with full-text support are already curated in `kb/communities/` and `data/isolates/`.
3. **Scouting Queue and Notes (`research/scouting/`, `notes/curation-When-the-Watchdog-Bites-20260417/`)**:
   - The second pass confirmed **0** further admissible new community or isolate baseline records in the local bounded frontier.

---

## 4. Preserved Unresolved Candidates and Search Limits

The following candidates and search limits remain preserved for future cycles when additional open-access full text or supplementary tables are ingested:

| Candidate / Source | Status | Blocker / Search Limit |
|---|---|---|
| `PMID:25043025` (Cheese rind *in situ* / *in vitro* pairwise manipulations, tracked in `#765`) | Preserved / Deferred | Full-text pairwise assay tables are not present in `references_cache/`; only abstract-level evidence is cached. |
| `PMID:38329909` (GLBRC 18-species exometabolite Transwell campaign, tracked in `#1467`) | Preserved / Deferred | Full-text strain and exometabolite tables are required before splitting or extending sub-consortia beyond `CommunityMech:000091`. |
| `PMID:21319991` (Okeke & Lu cellulolytic sub-combinations, tracked in `#1657`) | Preserved / Deferred | Primary article is paywalled; only abstract text is cached in `references_cache/`. |
| `PMID:35101850` (*Parachlorella*–*Saccharomyces* satellite bacterial isolates, tracked in `#1681`) | Preserved / Deferred | Requires full-text isolate characterization tables not available in the abstract cache. |
| `PMID:29138632` (*Phormidium* alkaline consortium heterotrophic co-isolates, tracked in `#1699`) | Preserved / Deferred | Requires full-text isolate table verification beyond the cached abstract. |
| `PMID:41606024` (Sulfide spring autotrophic CPR biofilm sub-consortia, tracked in `#1841`) | Preserved / Deferred | Lower-rank isolate and genome resolution lives in external supplementary tables (`#1996`). |
| `PMID:41908926` (Sugarcane `SynCom_MetG2` sub-panels, tracked in `#1847`) | Preserved / Deferred | Full 18-isolate membership and media tables require supplementary table ingestion. |
| `notes/curation-When-the-Watchdog-Bites-20260417/` (`CommunityMech:000512`–`000518`, *Klebsiella* + 11-commensal decolonization consortia) |Already Curated | Already present in `kb/communities/` (`CommunityMech:000512`–`000518`); verified deduplicated. |
| `PMID:42733304` Table 1 intermediate strains `BSG3`, `BS2`, `SO2`, `SO3` (standalone monocultures) | Excluded / Documented | `BSG3` has an unknown mutation-bred genotype (`the genotype of which is still unknown`) and no standalone fermentation or leaching data; `BS2`, `SO2`, and `SO3` were only assayed in ethanol-free `Ni2+/Co2+` viability controls (`Figure 4c–g`) without standalone brewing-wastewater ethanol removal, MFC power density, or NCM leaching curves. |
