# Cycle 6 Stage 1 (`add_records`) Bounded-Frontier Discovery & Curation Report (2026-11-04)

## 1. Executive Summary

During **Run `mech-goal-sequence-20261019`, Cycle 6, Stage 1 (`add_records`)**, we executed a repeated, recorded search of the local bounded frontier (`references_cache/`, `reports/scout/`, `research/`, `kb/communities/`, `data/isolates/`, and `kb/taxa/`) following the repository-local [`add-community-record`](../.claude/skills/add-community-record/SKILL.md) and [`scout-communities`](../.claude/skills/scout-communities/SKILL.md) skills:

- **Pre-Stage Corpus Inventory**:
  - `kb/communities/*.yaml`: **485** records (`489` post-stage)
  - `data/isolates/*.yaml`: **9** records
  - `kb/taxa/*.yaml`: **2** records
  - Highest existing `CommunityMech:` identifier: `CommunityMech:000500` (`data/isolates/Variovorax_boronicumulans_G4.yaml`)
- **Pass 1 Discovery & Curation**:
  - Identified **4 admissible, experimentally characterized defined synthetic microbial communities** in committed multi-consortium full-text/figure reference caches (`PMID:42144568` and `PMID:42587276`) whose sibling consortia were previously curated (`CommunityMech:000347` and `CommunityMech:000358`), where every member taxon is grounded in the offline `cache/ncbitaxon/terms.csv` ontology cache and every claim is backed by verbatim snippets in `references_cache/`:
    1. **`CommunityMech:000501`** — [Burkholderia_Bacillus_C2_Masson_Pine_SynCom.yaml](../kb/communities/Burkholderia_Bacillus_C2_Masson_Pine_SynCom.yaml) (*Burkholderia-Bacillus C2 Masson Pine SynCom*, 5-member PGPR SynCom `RW5 + RW1 + RW6 + RW7 + RW8` from `PMID:42144568` / `doi:10.1002/ps.70924`).
    2. **`CommunityMech:000502`** — [Bacillus_B81_A1_PAH_Biofilm_Consortium_1.yaml](../kb/communities/Bacillus_B81_A1_PAH_Biofilm_Consortium_1.yaml) (*Bacillus B8-1 and A1 PAH Biofilm Consortium 1*, 2-member PAH-degrading biofilm consortium `B8-1 + A1` from `PMID:42587276` / `doi:10.1186/s12866-026-05144-y`).
    3. **`CommunityMech:000503`** — [Bacillus_B81_A3_Naphthalene_Biofilm_Consortium_2.yaml](../kb/communities/Bacillus_B81_A3_Naphthalene_Biofilm_Consortium_2.yaml) (*Bacillus B8-1 and A3 Naphthalene Biofilm Consortium 2*, 2-member naphthalene-degrading biofilm consortium `B8-1 + A3` from `PMID:42587276` / `doi:10.1186/s12866-026-05144-y`).
    4. **`CommunityMech:000504`** — [Bacillus_B81_A1_A3_PAH_Biofilm_Consortium_4.yaml](../kb/communities/Bacillus_B81_A1_A3_PAH_Biofilm_Consortium_4.yaml) (*Bacillus B8-1, A1, and A3 Three-Strain PAH Biofilm Consortium 4*, 3-member PAH-degrading biofilm consortium `B8-1 + A1 + A3` from `PMID:42587276` / `doi:10.1186/s12866-026-05144-y`).
- **Pass 2 Repeated Bounded-Frontier Search**:
  - Re-ran the bounded-frontier audit across all **907** committed `references_cache/*.txt` files, all **3** scouting queues (`reports/scout/*.yaml`), all **3** research folders (`research/CommunityMech_*`), and all **498** curated community/isolate records (`489` in `kb/communities/` + `9` in `data/isolates/`).
  - Confirmed **0 further admissible new community or isolate records** exist within the offline-verifiable bounded frontier.

---

## 2. Newly Curated Community Records (`CommunityMech:000501`–`CommunityMech:000504`)

| ID | File Slug | Name | Source | Members & NCBITaxon Grounding | Key Curated Outcomes |
|---|---|---|---|---|---|
| `CommunityMech:000501` | `Burkholderia_Bacillus_C2_Masson_Pine_SynCom` | Burkholderia-Bacillus C2 Masson Pine SynCom | `PMID:42144568` (`doi:10.1002/ps.70924`) | *Burkholderia cepacia* RW1 (`NCBITaxon:292`), *Bacillus siamensis* RW5 (`NCBITaxon:659243`, `GTDB:s__Bacillus_siamensis`), *Bacillus amyloliquefaciens* RW6 (`NCBITaxon:1390`), *Bacillus velezensis* RW7 (`NCBITaxon:492670`, `GTDB:s__Bacillus_velezensis`), *Bacillus vallismortis* RW8 (`NCBITaxon:72361`) | Five-strain C2 PGPR SynCom reduced *Fusarium oxysporum* damping-off incidence by 50% and increased *Pinus massoniana* seedling height by 10.18% (vs. 36.67% and 9.44% for 2-strain HT `CommunityMech:000347`), enhanced protective enzymes, alleviated membrane damage, and activated *PR1*, *FLS2*, and *CAT1*. |
| `CommunityMech:000502` | `Bacillus_B81_A1_PAH_Biofilm_Consortium_1` | Bacillus B8-1 and A1 PAH Biofilm Consortium 1 | `PMID:42587276` (`doi:10.1186/s12866-026-05144-y`) | *Bacillus cereus* B8-1 (`NCBITaxon:1396`, `PP499640`), *Bacillus subtilis* A1 (`NCBITaxon:1423`, `GTDB:s__Bacillus_subtilis`, `PP499639`) | Consortium 1 (`B8-1 + A1`) exhibited mutualistic growth promotion across 24–72 h (`OD600 = 1.97` at 48 h, vs. `1.44` for B8-1 and `1.47` for A1), high mixed-species biofilm formation (`OD570 > 3.1`), 93.41% naphthalene degradation at 6 d, and 38.24% anthracene degradation at 15 d (`3.11x` B8-1 monoculture). |
| `CommunityMech:000503` | `Bacillus_B81_A3_Naphthalene_Biofilm_Consortium_2` | Bacillus B8-1 and A3 Naphthalene Biofilm Consortium 2 | `PMID:42587276` (`doi:10.1186/s12866-026-05144-y`) | *Bacillus cereus* B8-1 (`NCBITaxon:1396`, `PP499640`), *Bacillus licheniformis* A3 (`NCBITaxon:1402`, `GTDB:s__Bacillus_licheniformis`, `PP499641`) | Consortium 2 (`B8-1 + A3`) showed early growth promotion (`OD600 = 1.24` at 24 h; `1.70` at 48 h) followed by 72 h nutrient competition (`OD600 = 1.44`), highest mixed-species biofilm among two-strain consortia (`OD570 = 3.24`), and 93.49% naphthalene degradation at 6 d, while anthracene degradation remained near monoculture levels (`~15%`). |
| `CommunityMech:000504` | `Bacillus_B81_A1_A3_PAH_Biofilm_Consortium_4` | Bacillus B8-1, A1, and A3 Three-Strain PAH Biofilm Consortium 4 | `PMID:42587276` (`doi:10.1186/s12866-026-05144-y`) | *Bacillus cereus* B8-1 (`NCBITaxon:1396`, `PP499640`), *Bacillus subtilis* A1 (`NCBITaxon:1423`, `GTDB:s__Bacillus_subtilis`, `PP499639`), *Bacillus licheniformis* A3 (`NCBITaxon:1402`, `GTDB:s__Bacillus_licheniformis`, `PP499641`) | Three-strain Consortium 4 (`B8-1 + A1 + A3`) achieved the highest mixed-species biofilm biomass in the study (`OD570 = 3.45`, **p < 0.01**), early 24 h growth promotion (`OD600 = 1.37`) followed by 48–72 h nutrient competition, 90.89% naphthalene degradation at 6 d, and 28.08% anthracene degradation at 15 d (`2.29x` B8-1 monoculture, `1.97x` A1 monoculture, `1.88x` A3 monoculture). |

---

## 3. Preserved Unresolved Candidates & Search Limits

### 3.1 Multi-Consortium Candidates Evaluated and Deferred / Rejected

1. **`PMID:42135302` (`doi:10.3390/microorganisms14040864`) — `Consortia-B18-4M11` (*Peribacillus frigoritolerans* B18 + *Enterobacter hormaechei* 4M11)**:
   - **Status**: **Deferred (Offline Ontology Cache Blocker `#708`)**.
   - **Details**: `PMID_42135302.txt` contains full experimental characterization of two two-strain consortia in strawberry: `Consortia-4M4-B18` (already curated as `CommunityMech:000496`) and `Consortia-B18-4M11` (*P. frigoritolerans* B18 + *E. hormaechei* 4M11, Accession `PX795047`). However, `NCBITaxon:400634` (*Peribacillus frigoritolerans*) and `NCBITaxon:158836` (*Enterobacter hormaechei*) are absent from the local offline `cache/ncbitaxon/terms.csv` term table (`validate_terms.py` / `linkml-term-validator`), which is tracked under open issue `#708` (affected across 8 existing Cycle 4/5 records). Creating a new record with `NCBITaxon:400634` / `NCBITaxon:158836` would add a new `linkml-term-validator` failure until `cache/ncbitaxon/terms.csv` is refreshed. Preserved as the top candidate once `#708` lands.
2. **`PMID:42144568` (`doi:10.1002/ps.70924`) — `C1` (`RW1, RW2, RW3, RW4, RW5, RW6, RW7, RW8`) and `2K` (`RW3, RW4`)**:
   - **Status**: **Inadmissible (Insufficient *In Vivo* / Community-Specific Characterization in Cache)**.
   - **Details**: While `C1` (8-strain mixture) and `2K` (2-strain mixture `RW3 + RW4`) are defined in Figure 4a of `PMID_42144568.txt` and screened for *in vitro* inhibition, only `C2` (`CommunityMech:000501`) and `HT` (`CommunityMech:000347`) were advanced to *in vivo* Masson pine seedling trials and physiological/molecular characterization in the cached text.
3. **Other Multi-Consortium Papers Checked (`PMID:38918625`, `PMID:37985686`, `PMID:41495400`, `PMID:42015524`, `PMID:42162201`, `PMID:42180758`)**:
   - **Status**: **Already Curated or Sub-Community Comparison Controls**.
   - **Details**:
     - `PMID:38918625`: Curated as `CommunityMech:000357` (SynCom4) and `CommunityMech:000499` (SynCom7); `SynCom3` (`Sm + Sp + Ml`) is the unstable dropout control lacking the stabilizer *P. koreensis* (`Pk`).
     - `PMID:37985686`: Curated as `CommunityMech:000350` (NSC / At-RSPHERE SynCom) and `CommunityMech:000498` (SC1 drought-enriched 5-member SynCom); `SC2` (`Microbacterium` + `Curtobacterium` + `Sphingomonas` + `Streptomyces` + `Arthrobacter`) is the non-enriched control SynCom whose members are only partially species-resolved in the abstract/cache.
     - `PMID:41495400`: Curated as `CommunityMech:000349` (5-strain SynCom1.2); `SynCom1.1` (7-strain parent pool) includes 2 strains whose taxonomy is not resolved in the abstract cache.
     - `PMID:42015524`: Curated as `CommunityMech:000308` (7-strain B7 consortia); `A5` and `C12` member lists are not enumerated in the abstract cache.
     - `PMID:42162201`: Curated as `CommunityMech:000336` (`SynCom2` = *P. putida* L2 + *S. maltophilia* L3); `SynCom1` (5-strain mixture) member species beyond L2 and L3 are not enumerated in the abstract cache.
     - `PMID:42180758`: Curated as `CommunityMech:000346` (`CS1` four-strain core community); `CS` (full 14-strain synthetic flora) member taxa beyond the four `CS1` core strains are not enumerated in the abstract cache.

### 3.2 Uncited Reference Cache Files (`51` files) and Scouting Queues (`3` queues)

- All **51** uncited `references_cache/PMID_*.txt` files and all **3** scouting queues (`reports/scout/2026-04-12-scout-queue.yaml`, `reports/scout/2026-04-13-scout-queue.yaml`, `reports/scout/2026-04-13-batch2-scout-queue.yaml`) were re-inspected and verified unchanged from the Cycle 5 Stage 1 bounded-frontier audit (`reports/c5s1_bounded_frontier_discovery_20261101.md`):
  - **20** uncited caches are non-community / out-of-scope papers (reviews, single-strain genetics, host clinical trials, uncharacterized amplicon surveys, or retracted articles).
  - **12** uncited caches are mechanism/method papers whose communities or isolates are already represented in `kb/communities/` or `data/isolates/` under other primary PMIDs.
  - **19** uncited caches and the remaining scouting-queue entries are abstract-only caches where full taxonomic member lists or interaction endpoints require full-text OA retrieval or paid deep research outside the offline sandbox boundary.
