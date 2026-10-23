# Cycle 2 Stage 1 Bounded-Frontier Discovery & Curation Report (2026-10-23)

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle / Stage**: Cycle 2, Stage 1 (`add_records`)
- **Goal ID**: `goal-7897` (`start_step_index: 7897`, `started_at: 2026-10-22T03:40:43.293477+00:00`)
- **Base Commit (`origin/main`)**: `cb7a782c8ba80299dca8761ad0a2c90bccd8a117`
- **Skills Applied**:
  - `.claude/skills/communitymech-evolve-workflow/SKILL.md`
  - `.claude/skills/add-community-record/SKILL.md`
  - `.claude/skills/scout-communities/SKILL.md`
  - `.claude/skills/manage-identifiers/SKILL.md`
  - `.claude/skills/curate-yaml-record/SKILL.md`
  - `.claude/skills/review-communities/SKILL.md`
  - `.claude/skills/ground-taxa-gtdb/SKILL.md`

---

## 1. Bounded Frontier Definition & Search Protocol

Under the local-first bounded-frontier discovery protocol (`add-community-record` and `scout-communities`), we audited all local cached literature in `references_cache/` against the existing CommunityMech corpus (`kb/communities/*.yaml`, `data/isolates/*.yaml`, and `kb/taxa/*.yaml`):

1. **`references_cache/` Inventory**:
   - `947` top-level files (`866` `.md`/`.txt` text, abstract, and full-text files + `81` `.json` metadata files; `982` total files including `35` supplementary files under `references_cache/files/`).
2. **Deduplication Baseline (Pre-C2S1)**:
   - `kb/communities/*.yaml`: `473` curated community records.
   - `data/isolates/*.yaml`: `4` curated single-species isolate baseline records (`CommunityMech:000273` `Chromobacterium_Gold_Biocyanidation.yaml`, `CommunityMech:000320` `Aspergillus_Indium_LED_Recovery.yaml`, `CommunityMech:000321` `BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml`, and `CommunityMech:000322` `Methylobacterium_REE_Ewaste_Platform.yaml`).
   - `kb/taxa/*.yaml`: `2` reusable taxon records (`CommonTaxon`).
   - Pre-C2S1 corpus total: `477` `MicrobialCommunity` records (`473` communities + `4` isolates) and `2` `CommonTaxon` records (`479` YAML files total).
   - Every `PMID:` and `doi:` identifier referenced across `evidence[].reference` in the corpus was indexed and cross-matched against both the filenames and full text of `references_cache/`.

---

## 2. Candidate Evaluation Across Uncurated Cached References

Programmatic cross-matching of `references_cache/` (`866` top-level `.md`/`.txt` files) against the pre-C2S1 corpus identified **8 uncurated primary-source files covering 7 admissible community/isolate systems** with sufficient verbatim composition, mechanism, and environmental detail for full schema-compliant curation, alongside source-limited (`content_type: unavailable` or taxon-unresolved abstract-only) candidates and out-of-scope/duplicate cached items:

### 2.1 Admissible Candidates Curated in C2S1 (`CommunityMech:000484`–`000490`)

| Reference(s) | Exact Cache File(s) | Cached Size | System / Study Scope | Admissibility Disposition |
|---|---|---:|---|---|
| `PMID:27058505` (`doi:10.1038/ismej.2016.29`) | `references_cache/PMID_27058505.txt` | `50,240` chars (full text) | Flingern tar-oil-contaminated aquifer sediment community with suboxic filamentous *Desulfobulbaceae* cable bacteria (T-RF 159) bridging anodic sulfide oxidation and cathodic oxygen reduction over 1–2 cm via long-distance electron transfer (LDET), co-occurring with *Thiobacillus* (*T. denitrificans* T-RF 477), *Ignavibacteria* (T-RF 163), and toluene-degrading sulfate-reducing *Desulfobulbaceae* | **Added (`CommunityMech:000484`)** in `kb/communities/Aquifer_Sediment_Cable_Bacteria_Sulfur_Community.yaml` |
| `PMID:26781463` (`doi:10.1186/s12863-016-0330-4`) | `references_cache/PMID_26781463.txt` + `references_cache/doi_10.1186_s12863-016-0330-4.md` | `3,546` chars (abstract) + `66,684` chars (full text) | Dexing Copper Mine industrial bioleaching heap community (*Acidithiobacillus ferrooxidans*, *Acidithiobacillus* [*A. ferrivorans*-like], *Thiobacillus* [*T. plumbophilus*-like], *Leptospirillum ferrooxidans*) profiled by 16S rRNA pyrosequencing and GeoChip 4.0 across heap 1 (pH 2.45) and heap 2 (pH 2.60) | **Added (`CommunityMech:000485`)** in `kb/communities/Dexing_Copper_Bioleaching_Heap_Community.yaml` |
| `doi:10.3390/min14030255` | `references_cache/doi_10.3390_min14030255.md` | `2,854` chars (abstract) | Staré Ransko Zn–Cu mine tailings bioleaching consortium (*Acidithiobacillus ferrooxidans*, *Acidithiobacillus thiooxidans*, *Leptospirillum ferrooxidans*) comparing native vs. synthetic acidophilic consortia over a 70-day metal extraction experiment (97% Zn, 74.6% Cu, 62% Fe, 89.2% Ni, 63% Co) | **Added (`CommunityMech:000486`)** in `kb/communities/Stare_Ransko_Mine_Tailings_Bioleaching_Consortium.yaml` |
| `doi:10.1007/s13213-019-01453-y` | `references_cache/doi_10.1007_s13213-019-01453-y.md` | `2,326` chars (abstract) | Moderately thermophilic defined chalcopyrite bioleaching consortium (*Sulfobacillus thermosulfidooxidans*, *Acidithiobacillus caldus*, *Ferroplasma thermophilum*) at 48 °C across controlled pH 1.5, 1.7, and 2.0 (77.6% Cu extraction at pH 1.5 vs. 61.9% at pH 2.0) | **Added (`CommunityMech:000487`)** in `kb/communities/Moderate_Thermophile_Chalcopyrite_pH_Bioleaching_Consortium.yaml` |
| `doi:10.3389/fmicb.2024.1423741` | `references_cache/doi_10.3389_fmicb.2024.1423741.md` | `89,715` chars (full text) | *Bacillus licheniformis* isolated from tannery effluent as a single-species hexavalent chromium Cr(VI) biosorption and detoxifying isolate baseline (95.8% Cr removal at 50 ppm, 35 °C, pH 7.0) | **Added (`CommunityMech:000488`)** in `data/isolates/Bacillus_licheniformis_Chromate_Biosorption.yaml` |
| `PMID:30343816` (`doi:10.1016/j.wasman.2018.07.010`) + `PMID:31203122` (`doi:10.1016/j.jhazmat.2019.05.041`) | `references_cache/PMID_30343816.txt` + `references_cache/PMID_31203122.txt` | `2,044` chars + `1,929` chars (abstracts) | Adapted *Acidithiobacillus ferrooxidans* single-species isolate bioleaching of Cu, Ni, and Ga from waste light-emitting diode (WLED) powder via direct vs. indirect two-step spent-medium ferric sulfate leaching (93.96% Cu, 96.59% Ni, 87.98% Ga recovery) | **Added (`CommunityMech:000489`)** in `data/isolates/Acidithiobacillus_LED_Metal_Bioleaching.yaml` |
| `doi:10.1128/aem.01906-20` | `references_cache/doi_10.1128_aem.01906-20.md` | `1,904` chars (abstract) | *Ferrimicrobium acidiphilum* single-species acidophilic actinobacterium isolate baseline performing aerobic Fe(II) respiration and anaerobic Fe(III) reduction at pH ≤ 2.0 via *a*-, *b*-, and *c*-type cytochromes | **Added (`CommunityMech:000490`)** in `data/isolates/Ferrimicrobium_acidiphilum_Iron_Respiration.yaml` |

### 2.2 Preserved Unresolved / Source-Limited Candidates & Excluded Cache Items

After curating `CommunityMech:000484`–`000490`, `54` top-level `.md`/`.txt` files in `references_cache/` do not have a direct string citation in the corpus; all `54` were audited and classified into four reproducible buckets:

1. **Preserved Unresolved / Source-Limited Community & Isolate Candidates (`12` files)**:
   - **Title-only stubs (`content_type: unavailable`, `7` files)**: `doi_10.1007_s10311-019-00911-y.md` (`800` chars, *Acidithiobacillus* circuit-board Cu bioleaching), `doi_10.1016_j.algal.2016.05.024.md` (`708` chars, algal cofactor symbiosis), `doi_10.1016_j.cej.2020.124801.md` (`2,384` chars, sulfur-cycle phenol degradation + Cr(VI) reduction), `doi_10.1016_j.cej.2021.133461.md` (`613` chars, methanotroph-photoautotroph coculture kinetic model), `doi_10.1016_j.ibiod.2025.106190.md` (`1,002` chars, *Ferroplasma acidiphilum* + *Leptospirillum ferriphilum* under organic matter stress), `doi_10.1080_10889868.2024.2407240.md` (`779` chars, alkaliphilic sulfur-oxidizing consortium), and `doi_10.1186_s12302-025-01103-y.md` (`1,860` chars, bacterial consortia bioremediation review/abstract). None contain abstract or full-text bodies for verbatim snippet extraction.
   - **Taxon-unresolved / abstract-limited consortia (`3` files)**: `PMID_12620881.md` (`2,060` chars, DGGE comparison of unnamed sulfidogenic vs. nonsulfidogenic Cr(VI)-reducing sediment enrichments without named genus/species membership), `PMID_42243405.txt` (`3,098` chars, mouse gut biofilm consortium abstract that does not name the constituent bacterial species/strains), and `PMID_42667226.txt` (`2,262` chars, contactless fungal co-culture assay protocol abstract that does not specify the fungal species pair).
   - **De-composited single-strain chromate-reduction candidate (`2` files)**: `PMID_21441371.md` (`3,164` chars, *Intrasporangium chromatireducens* sp. nov. strain Q5-1 taxonomic description) and `doi_10.1007_s11274-009-0047-x.md` (`2,137` chars, immobilized *Intrasporangium* sp. Q5-1 Cr(VI) removal; previously detached from `CommunityMech:000017` during de-compositing in commit `fa3f1a8c`), preserved as a future isolate candidate pending offline NCBITaxon/GTDB cache registration for `Intrasporangium chromatireducens`.
2. **Already Represented in Curated Corpus via Primary DOI/PMID (`14` files)**:
   - `PMID_26704063.md` (`3,006` chars, two-step PCB Cu/Au bioleaching covered by `CommunityMech:000026` `Ewaste_Bioleaching_Consortium.yaml`), `pmc_6417678.txt` (`1,752` chars, covered by `CommunityMech:000169` `Methylocaldum_Methyloceanibacter_Methane_Crossfeeding_Coculture.yaml`), `pmc_6746925.txt` (`1,581` chars, covered by `CommunityMech:000180` `Clostridium_Thermoanaerobacterium_JN4_GD17_Cellulosic_Biofuel_Coculture.yaml`), `doi_10.25345_C58W38C48.md` (`657 chars`, MassIVE dataset already linked in `CommunityMech:000371` `Synechococcus_Pseudomonas_PhotoPHA_DNT_Coculture.yaml`), `PMID_11034209.md` (`233` chars) and `PMID_19383036.md` (`280` chars, ANME-SRB consortia covered by `CommunityMech:000003` and `000004`), `GITHUB_Xinming9606_...md` and `GITHUB_deanpettinga_...md` (dataset sidecars cited in corpus `external_resources`), and `6` `epmc_chem_PMC*.txt` chemical-entity sidecars for existing PMC records.
3. **Review Articles, Computational Modeling Frameworks & Taxonomic/Method Papers (`14` files)**:
   - `PMID_42195847.txt` (`166,187` chars, review article on omics-guided fermented food consortia), `PMID_42385706.txt` (`2,770` chars, computational genotype-to-function modeling framework), `PMID_18330567.md` (`2,579` chars, chemical/physical EPS extraction protocol comparison on Río Tinto biofilms), `doi_10.1016_j.cell.2014.05.041.txt` and `europepmc_10.1016_j.cell.2014.05.041.txt` (`1,080` chars each, cheese-rind perspective/summary covered by `CommunityMech:000072`), `doi_10.1101_2024.03.28.587009.md` (`2,436` chars, host-aging metabolic modeling preprint), `doi_10.1111_j.1462-2920.2005.00861.x.md` (`2,837` chars, *Ferroplasma* minireview), `doi_10.1155_2021_7694157.md` (`2,345` chars, chromium bioremediation review), `doi_10.1007_BF02106205.md` (`859` chars, *Acidobacterium capsulatum* sp. nov. taxonomy), `PMID_23949950.txt` and `doi_10.1007_s00248-013-0274-4.md` (*Halobacillus trueperi* single-species biogeography survey), `doi_10.1007_s10230-008-0059-z.md` (`914` chars, geochemical lake stratification), and `doi_10.1016_j.mineng.2013.03.022.md` (`658` chars, dead macroalgal biomass lead biosorption).
4. **Non-Microbial-Ecology / Unrelated PubMed Cache Artifacts (`14` files)**:
   - Historical wrong-PMID lookup artifacts (`PMID_2039291.txt`, `PMID_21559381.txt`, `PMID_25687895.txt` + `doi_10.1016_j.bbabio.2015.02.010.md`, `PMID_28080685.txt`, `PMID_32753581.txt`, `PMID_34742794.txt` + `doi_10.1016_j.scitotenv.2021.151468.md`, `PMID_39126844.txt` + `doi_10.1016_j.jenvman.2024.122098.md`, `PMID_4381058.txt`, `PMID_8161360.txt`, `PMID_9734072.txt`, `PMID_9734074.txt`, `PMID_9785463.txt`).

---

## 3. Newly Curated Records (`CommunityMech:000484`–`000490`)

All 7 records were minted sequentially via `manage-identifiers` (`000484`–`000490`), written through the repository's validated writer (`communitymech.curation.write_validated_community`) with accompanying history sidecars (`history/records/*/2026-10-23T073800Z-antigravity-a101.yaml` through `a107.yaml`), grounded in NCBITaxon, GTDB (`kg-microbe` `NCBI2GTDB.tsv.gz` via `scripts/gtdb_ground.py`), ENVO, GO, and CHEBI, and verified with `linkml-term-validator` and `scripts/evidence_snippet_audit.py`:

| ID | Record Path | Category / Origin / State | Taxa Count & Grounded Members | Interactions | Environment Term | Evidence Snippets (`51 / 51 MATCH`) |
|---|---|---|---:|---|---|---:|
| `CommunityMech:000484` | `kb/communities/Aquifer_Sediment_Cable_Bacteria_Sulfur_Community.yaml` | `BIOREMEDIATION` / `NATURAL` / `PERTURBED` | `3` (`Desulfobulbaceae` `NCBITaxon:213121`, `Thiobacillus` `NCBITaxon:919`, `Ignavibacteria` `NCBITaxon:1134404`) | `3` (`SYNTROPHY`, `CROSS_FEEDING`, `COMPETITION`) | `ENVO:00002007` (`sediment`) | `10 / 10 MATCH` (`4` taxonomy + `4` interactions + `2` env factors) |
| `CommunityMech:000485` | `kb/communities/Dexing_Copper_Bioleaching_Heap_Community.yaml` | `BIOMINING` / `ENGINEERED` / `ENGINEERED` | `4` (`Acidithiobacillus ferrooxidans` `NCBITaxon:920`, `Acidithiobacillus` `NCBITaxon:119977`, `Thiobacillus` `NCBITaxon:919`, `Leptospirillum ferrooxidans` `NCBITaxon:180`) | `3` (`MUTUALISM`, `SYNTROPHY`, `COMMENSALISM`) | `ENVO:00000003` (`mine tailing`) | `11 / 11 MATCH` (`4` taxonomy + `4` interactions + `3` env factors) |
| `CommunityMech:000486` | `kb/communities/Stare_Ransko_Mine_Tailings_Bioleaching_Consortium.yaml` | `BIOMINING` / `SYNTHETIC` / `ENGINEERED` | `3` (`Acidithiobacillus ferrooxidans` `NCBITaxon:920`, `Acidithiobacillus thiooxidans` `NCBITaxon:930`, `Leptospirillum ferrooxidans` `NCBITaxon:180`) | `2` (`SYNTROPHY`, `MUTUALISM`) | `ENVO:00000003` (`mine tailing`) | `9 / 9 MATCH` (`1` eng design + `3` taxonomy + `2` interactions + `3` env factors) |
| `CommunityMech:000487` | `kb/communities/Moderate_Thermophile_Chalcopyrite_pH_Bioleaching_Consortium.yaml` | `BIOMINING` / `SYNTHETIC` / `ENGINEERED` | `3` (`Sulfobacillus thermosulfidooxidans` `NCBITaxon:28034`, `Acidithiobacillus caldus` `NCBITaxon:33059`, `Ferroplasma thermophilum` `NCBITaxon:2591003`) | `2` (`SYNTROPHY`, `COMMENSALISM`) | `ENVO:00002123` (`bioreactor`) | `8 / 8 MATCH` (`1` eng design + `3` taxonomy + `2` interactions + `2` env factors) |
| `CommunityMech:000488` | `data/isolates/Bacillus_licheniformis_Chromate_Biosorption.yaml` | `BIOREMEDIATION` / `ENGINEERED` / `PERTURBED` | `1` (`Bacillus licheniformis` `NCBITaxon:1402`) | `0` (single-species isolate baseline) | `ENVO:00002001` (`waste water`) | `5 / 5 MATCH` (`1` eng design + `2` taxonomy + `2` env factors) |
| `CommunityMech:000489` | `data/isolates/Acidithiobacillus_LED_Metal_Bioleaching.yaml` | `BIOMINING` / `ENGINEERED` / `ENGINEERED` | `1` (`Acidithiobacillus ferrooxidans` `NCBITaxon:920`) | `0` (single-species isolate baseline) | `ENVO:01001405` (`laboratory environment`) | `5 / 5 MATCH` (`2` eng design + `2` taxonomy + `1` env factors) |
| `CommunityMech:000490` | `data/isolates/Ferrimicrobium_acidiphilum_Iron_Respiration.yaml` | `BIOMINING` / `NATURAL` / `STABLE` | `1` (`Ferrimicrobium acidiphilum` `NCBITaxon:52256`) | `0` (single-species isolate baseline) | `ENVO:01001405` (`laboratory environment`) | `3 / 3 MATCH` (`2` taxonomy + `1` env factors) |

---

## 4. Repeated Bounded-Frontier Search Verification

After curating `CommunityMech:000484`–`000490`, a repeated programmatic pass over `references_cache/` (`947` top-level files; `866` `.md`/`.txt` files) was executed against the updated corpus (`477` communities in `kb/communities/*.yaml` + `7` isolates in `data/isolates/*.yaml` = `484` `MicrobialCommunity` records, plus `2` `CommonTaxon` records in `kb/taxa/*.yaml` = `486` YAML files total):

- **Remaining admissible uncurated community or isolate papers with sufficient text/taxonomic resolution in bounded frontier**: `0`
- **Preserved unresolved / source-limited candidates**: `12` files (`7` `content_type: unavailable` title-only stubs, `3` taxon-unresolved abstracts, and `2` files for the de-composited *Intrasporangium chromatireducens* Q5-1 candidate pending offline ontology/GTDB cache registration)
- **Already-covered / review / methods / non-ecological cached files**: `42` files (`14` already covered by existing records, `14` review/modeling/method papers, `14` unrelated historical PubMed lookup artifacts)

---

## 5. Validation & Quality Gate Summary

All repository validation gates passed on the updated `486`-file corpus (`477` communities + `7` isolates + `2` taxa):

1. `scripts/validate_strict.py`: `484` community/isolate + history sidecar files scanned, `0` `ERROR` rows (`EXIT=0`).
2. `scripts/validate_gtdb_coherence.py`: `486` files checked (`kb/communities`, `kb/taxa`, `data/isolates`), `0` incoherent blocks, `0` malformed lineages, `0` lineage conflicts (`EXIT=0`).
3. `scripts/validate_yaml_scalars.py`: `486` files checked, `0` truncated scalars (`EXIT=0`).
4. `scripts/audit_writers.py`: `30` writer scripts audited, `0` violations (`EXIT=0`).
5. `linkml-term-validator`: all 7 new records validated against `src/communitymech/schema/communitymech.yaml` with `--cache-dir cache --labels` (`EXIT=0`).
6. `scripts/evidence_snippet_audit.py`: `51` snippets audited across the 7 new records (`51 MATCH`, `0 MISMATCH`).
7. `pytest`: `tests/test_causal_review_batch109.py`, `tests/test_gtdb_coherence_validator.py`, `tests/test_is_reclassified_semantics.py`, `tests/test_transwell_participants.py`, and `tests/test_stage6_infrastructure.py` passed (`EXIT=0`).
8. `docs/` synchronization (`communitymech.render`, `communitymech.export`, `communitymech.datamodel`): `0` diff against freshly rendered output.
