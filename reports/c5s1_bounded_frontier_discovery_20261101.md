# Cycle 5, Stage 1 (`add_records`) — Bounded-Frontier Discovery & Intake Report (2026-11-01)

## 1. Executive Summary

- **Workflow Stage**: Run `mech-goal-sequence-20261019`, Cycle 5, Stage 1 (`add_records`)
- **Instruction ID**: `35e3094ffef2a48c6a7f86ce`
- **Action ID**: `0b987a9cefdcc76e21992c1f`
- **Starting Corpus State**: 490 `MicrobialCommunity` records (`CommunityMech:000001`–`CommunityMech:000496`, with 6 historical ID gaps: `000212, 000228, 000229, 000230, 000231, 000232`; 481 in `kb/communities/` and 9 in `data/isolates/`) plus 2 `CommonTaxon` records in `kb/taxa/`
- **Ending Corpus State**: 494 `MicrobialCommunity` records (`CommunityMech:000001`–`CommunityMech:000500`, with 6 historical ID gaps; 485 in `kb/communities/` and 9 in `data/isolates/`) plus 2 `CommonTaxon` records in `kb/taxa/`
- **New Records Added**: **4** (`CommunityMech:000497`–`CommunityMech:000500`):
  1. `CommunityMech:000497` — `kb/communities/Synechocystis_Ecoli_Acetate_Butanol_Coculture.yaml` (`PMID:42726284`)
  2. `CommunityMech:000498` — `kb/communities/Cyantraniliprole_Consortium_T1.yaml` (`PMID:42354927`)
  3. `CommunityMech:000499` — `kb/communities/Cyantraniliprole_Consortium_T2.yaml` (`PMID:42354927`)
  4. `CommunityMech:000500` — `kb/communities/Cyantraniliprole_Consortium_T3.yaml` (`PMID:42354927`)
- **Exhaustion Verification**: Two full passes over the local offline reference cache (`references_cache/`, 866 top-level `.md`/`.txt` files), multi-consortium full-text papers already cached in `references_cache/`, `research/scouting/` (4 scouting batches), `notes/new-communities-to-create.md`, and `notes/new-datasets-to-curate.md` confirmed that after curating `CommunityMech:000497`–`CommunityMech:000500`, **0** additional admissible uncurated microbial community or supported isolate baseline records with verbatim cached abstract/full-text support remain in the bounded local frontier.

---

## 2. Bounded-Frontier Search Methodology & Repeated Passes

### Pass 1: Structured Citation Index, Uncited Cache Sweep & Multi-Consortium Full-Text Audit

1. **Structured Corpus Citation Index**:
   - Parsed all 490 existing `MicrobialCommunity` YAML records (`481` in `kb/communities/` and `9` in `data/isolates/`) and `2` `CommonTaxon` records (`kb/taxa/`), extracting every structured `evidence[].reference` value.
   - Confirmed highest existing identifier prior to intake: `CommunityMech:000496` (`kb/communities/Methylomicrobium_Arthrospira_Biogas_Conversion_Coculture.yaml`) and next available sequential identifiers: `CommunityMech:000497`–`CommunityMech:000500`.
2. **Uncited Reference Cache Audit (`references_cache/`)**:
   - Re-audited all `866` top-level `.md` and `.txt` files in `references_cache/` against the structured `evidence[].reference` index across all prefix conventions (`PMID_`, `pmc_full_pmid_`, `doi_`, `europepmc_`, `openalex_`, `semanticscholar_`, `epmc_chem_`, `pmc_`, `GITHUB_`).
   - Confirmed that the `51` top-level cache files not cited in any structured `evidence[].reference` slot contain `0` admissible uncurated communities (8 duplicate/superseded cache copies of already-curated records, 6 `Abstract\nNone` metadata stubs, 9 broad review/perspective articles, and 28 abiotic/plant-only/host-pathology/single-enzyme/unresolved-isolate-code studies).
3. **Multi-Consortium Full-Text Audit (`references_cache/`)**:
   - Audited committed full-text caches for multi-consortium experimental studies where earlier intake had curated only a subset of the experimentally tested synthetic consortia:
     - **`PMID:42726284` (`references_cache/PMID_42726284.txt`, Roussou & Lindblad 2026, *Applied Microbiology and Biotechnology* 110:215, `doi:10.1007/s00253-026-14029-z`)**: Constructed and maintained two distinct 42-day photosynthetic acetate-to-1-butanol consortia pairing engineered `Synechocystis` sp. PCC 6803 (`WT_PKPa_RBS_BsPta_Δacs`) with either `Pseudomonas taiwanensis` VLB120 (`P. taiwanensis_Pem7_ButOH`, already curated as `CommunityMech:000363`) or `Escherichia coli` BL21(DE3) (`E. coli_Pem7_ButOH`). The `Synechocystis`–`E. coli` consortium had not yet been curated as its own record despite complete full-text evidence (5:1 starting OD ratio `OD750 = 2.5` : `OD600 = 0.5`, closed Biolite 25 cm2 plug-sealed flasks in CoBG11 with 50 mM NaHCO3, sharper extracellular acetate decrease after day 22, and 1-butanol peaks on days 10 and 14). Curated as **`CommunityMech:000497`** (`kb/communities/Synechocystis_Ecoli_Acetate_Butanol_Coculture.yaml`).
     - **`PMID:42354927` (`references_cache/PMID_42354927.txt`, Fahmy et al. 2026, *Scientific Reports*, `doi:10.1038/s41598-026-42362-y`)**: Constructed and benchmarked four distinct defined bacterial consortia (`T1`, `T2`, `T3`, and `T4`) from six MALDI-TOF-MS-identified pesticide-degrading isolates (`Bacillus cereus` Ch1, `Priestia megaterium` Ch2, `Micrococcus luteus` Ch3, `Pseudomonas aeruginosa` Ht4, `Pseudomonas aeruginosa` Ht5, and `Pseudomonas aeruginosa` Ht6) for biodegradation of the diamide insecticide cyantraniliprole (`100 mg/L` in MSM over 15 days at 30 °C, pH 7, 150 rpm). Previously, only the 6-strain mixture `T4` had been curated (`CommunityMech:000369`, `kb/communities/Cyantraniliprole_Fahmy_Consortium_T4.yaml`), whereas the three 3-strain consortia with complete strain-identity, GC-MS metabolite, and HPLC removal time-course data (`T1`: Ch1 + Ch2 + Ch3, `83.9%` removal; `T2`: Ht4 + Ht5 + Ht6, `81.3%` removal; `T3`: Ch1 + Ch2 + Ht4, `89.3%` removal) were uncurated. Curated as **`CommunityMech:000498`** (`kb/communities/Cyantraniliprole_Consortium_T1.yaml`), **`CommunityMech:000499`** (`kb/communities/Cyantraniliprole_Consortium_T2.yaml`), and **`CommunityMech:000500`** (`kb/communities/Cyantraniliprole_Consortium_T3.yaml`).
     - Verified that other multi-consortium papers with cached full text are already completely represented across their admissible defined consortia (`PMID:42274939` has both `Consortium_T1` and `Consortium_T2`; `PMID:42562958` has both `Wheat_Consortium_C1` and `Wheat_Consortium_C6`; `PMID:42080511` has all three `Synechococcus` SPCs; `PMID:42514046` has both `Wine_Yeast_ThreeSpecies_Contact_Consortium` and `Wine_Yeast_FiveSpecies_Strain_Substitution_Consortium`).

### Pass 2: Post-Intake Re-Sweep & Exhaustion Verification

- After writing and validating `CommunityMech:000497`–`CommunityMech:000500` via `communitymech.validation.write_validated.write_validated_community`, re-ran the corpus inventory and reference audit across all `494` `MicrobialCommunity` records (`485` in `kb/communities/` and `9` in `data/isolates/`) and `2` `CommonTaxon` records.
- Verified `104/104` `MATCH` snippets (`0` `MISMATCH`, `0` `RENDERING`, `0` `ASSEMBLED`, `0` `WEAK`, `0` `NOCONTENT`) across the 4 new records in `scripts/evidence_snippet_audit.py` and `0` issues in `linkml-reference-validator` and `linkml-term-validator`.
- Confirmed that **0** remaining admissible uncurated microbial community or supported isolate baseline records exist in the bounded local frontier.

---

## 3. Newly Added Records (`CommunityMech:000497`–`CommunityMech:000500`)

| ID | Path | Category / State / Origin | Primary Reference | Taxa (`NCBITaxon` & GTDB Status) | Summary of Curated Mechanism |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `CommunityMech:000497` | `kb/communities/Synechocystis_Ecoli_Acetate_Butanol_Coculture.yaml` | `BIOTECHNOLOGY` / `ENGINEERED` / `SYNTHETIC` | `PMID:42726284` (`doi:10.1007/s00253-026-14029-z`) | `Synechocystis sp. PCC 6803` (`WT_PKPa_RBS_BsPta_Δacs`, `NCBITaxon:1148`, `UNRESOLVED`), `Escherichia coli` (`BL21(DE3) Pem7_ButOH`, `NCBITaxon:562`, `GROUNDED`: `GTDB:s__Escherichia_coli`) | Two-member photosynthetic synthetic coculture in closed Biolite 25 cm2 plug-sealed flasks (25 mL CoBG11 + 50 mM NaHCO3, 30 °C, 65 umol photons m^-2 s^-1, 5:1 starting OD ratio `OD750 = 2.5` : `OD600 = 0.5`, 10% medium refresh every 2–4 days for 42 days). `Synechocystis` fixes CO2/bicarbonate and secretes acetate; `E. coli_Pem7_ButOH` lowers extracellular acetate relative to axenic `Synechocystis` (with a sharp drop after day 22) and produces 1-butanol via the O2-tolerant TPC4 pathway with peaks on days 10 and 14 (`PARTIAL` carbon-flux exclusivity due to potential cyanobacterial carbohydrate/EPS exudates). |
| `CommunityMech:000498` | `kb/communities/Cyantraniliprole_Consortium_T1.yaml` | `BIOREMEDIATION` / `PERTURBED` / `SYNTHETIC` | `PMID:42354927` (`doi:10.1038/s41598-026-42362-y`) | `Bacillus cereus` (`Ch1`, `NCBITaxon:1396`, `AMBIGUOUS`), `Priestia megaterium` (`Ch2`, `NCBITaxon:1404`, `UNRESOLVED`), `Micrococcus luteus` (`Ch3`, `NCBITaxon:1270`, `UNRESOLVED`) | Three-strain chlorantraniliprole-selected bacterial consortium (`T1`, 2% v/v equal-cell-density inoculum in 100 mL MSM with 100 mg/L cyantraniliprole, pH 7, 30 °C, 150 rpm, 15 days). Achieves `83.9%` cyantraniliprole removal via nitrile-hydratase/amidase-associated hydrolysis and ring-closure/fragmentation pathways (`PARTIAL` member-level step attribution). |
| `CommunityMech:000499` | `kb/communities/Cyantraniliprole_Consortium_T2.yaml` | `BIOREMEDIATION` / `PERTURBED` / `SYNTHETIC` | `PMID:42354927` (`doi:10.1038/s41598-026-42362-y`) | `Pseudomonas aeruginosa` (`Ht4`, `NCBITaxon:287`, `GROUNDED`: `GTDB:s__Pseudomonas_aeruginosa`), `Pseudomonas aeruginosa` (`Ht5`, `NCBITaxon:287`, `GROUNDED`), `Pseudomonas aeruginosa` (`Ht6`, `NCBITaxon:287`, `GROUNDED`) | Three-strain lambdacyhalothrin-selected `Pseudomonas aeruginosa` consortium (`T2`: isolates `Ht4`, `Ht5`, `Ht6`; 2% v/v inoculum in 100 mL MSM with 100 mg/L cyantraniliprole, pH 7, 30 °C, 150 rpm, 15 days). Achieves `81.3%` cyantraniliprole removal (`PARTIAL` strain-level step attribution). |
| `CommunityMech:000500` | `kb/communities/Cyantraniliprole_Consortium_T3.yaml` | `BIOREMEDIATION` / `PERTURBED` / `SYNTHETIC` | `PMID:42354927` (`doi:10.1038/s41598-026-42362-y`) | `Bacillus cereus` (`Ch1`, `NCBITaxon:1396`, `AMBIGUOUS`), `Priestia megaterium` (`Ch2`, `NCBITaxon:1404`, `UNRESOLVED`), `Pseudomonas aeruginosa` (`Ht4`, `NCBITaxon:287`, `GROUNDED`: `GTDB:s__Pseudomonas_aeruginosa`) | Highest-performing three-strain cross-enrichment consortium (`T3`: `Ch1 + Ch2 + Ht4`; 2% v/v inoculum in 100 mL MSM with 100 mg/L cyantraniliprole, pH 7, 30 °C, 150 rpm, 15 days). Combines the top degraders from both pesticide-history enrichments to achieve `89.3%` cyantraniliprole removal over 15 days (`PARTIAL` member-level step attribution). |

---

## 4. Preserved Unresolved Candidates & Search Limits

1. **51 Uncited Top-Level Cache Files in `references_cache/`**:
   - All 51 remaining uncited top-level cache files were re-verified and remain non-admissible without external full-text or strain-taxonomic resolution (8 duplicate/superseded cache copies of already-curated records, 6 `Abstract\nNone` metadata stubs, 9 broad review/perspective articles, and 28 abiotic/plant-only/host-pathology/single-enzyme/unresolved-isolate-code studies including `PMID_42667226.txt` which reports only internal isolate codes `N67`, `N92`, `N111`, `N238` in its cached abstract).
2. **Scouting Stubs & Intake Queues (`research/scouting/`, `notes/`)**:
   - All scouting candidates in `research/scouting/` (`2026-04-06`, `2026-04-06-b2`, `2026-04-12`, `2026-04-12-syncom`) and `notes/` that have cached full text or abstracts in `references_cache/` are curated in `kb/communities/`; candidates lacking local cached source text are preserved for future network-authorized intake cycles.
