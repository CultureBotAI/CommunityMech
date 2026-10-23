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

Under the local-first bounded-frontier discovery protocol (`add-community-record` and `scout-communities`), we audited all local literature caches and citation stores against the existing CommunityMech corpus (`kb/communities/*.yaml` and `data/isolates/*.yaml`):

1. **`references_cache/`**: `1,417` cached reference files (`PMID_*.md` and `doi_*.md`).
2. **`literature_20260405/`**: `133` full-text markdown files and `133` metadata JSON sidecars (`*_meta.json`).
3. **Deduplication Baseline (Pre-C2S1)**:
   - `kb/communities/*.yaml`: `473` curated community records (`CommunityMech:000001`–`000483`, shared ID space with isolates).
   - `data/isolates/*.yaml`: `9` curated single-species isolate baseline records (`CommunityMech:000171`, `000249`, `000250`, `000273`, `000321`, `000480`–`000483`).
   - All `PMID:` and `doi:` identifiers referenced across `evidence[].reference` in all `482` existing records were indexed and cross-matched against `references_cache/` and `literature_20260405/`.

---

## 2. Candidate Evaluation Across Uncurated Cached References

Across all `1,417` files in `references_cache/` and `133` files in `literature_20260405/`, exactly **13 cached references** were not yet cited by any record in `kb/communities/` or `data/isolates/`. Every uncurated reference was inspected in full:

| Reference | Cache Source | Content Length | System / Study Scope | Admissibility Disposition |
|---|---|---:|---|---|
| `PMID:27058505` (`doi:10.1038/ismej.2016.29`) | `references_cache/PMID_27058505.md` + `literature_20260405/PMID_27058505.md` | Full text + abstract | Freshwater tar-oil-contaminated aquifer sediment microcosm with *Desulfobulbaceae* cable bacteria, *Sulfuricella*, *Sideroxydans*, *Thiobacillus*, and *Rhodocyclaceae* guild | **Added (`CommunityMech:000484`)** in `kb/communities/Aquifer_Sediment_Cable_Bacteria_Sulfur_Community.yaml` |
| `PMID:26781463` (`doi:10.1186/s12863-016-0330-4`) | `references_cache/PMID_26781463.md` + `references_cache/doi_10_1186_s12863-016-0330-4.md` + `literature_20260405/PMID_26781463.md` | Full text (`27,452` chars) + abstract | Dexing Copper Mine industrial bioleaching heap community (*Acidithiobacillus ferrooxidans*, *Acidithiobacillus caldus*, *Acidithiobacillus thiooxidans*, *Leptospirillum ferrooxidans*, *Sulfobacillus*) | **Added (`CommunityMech:000485`)** in `kb/communities/Dexing_Copper_Bioleaching_Heap_Community.yaml` |
| `doi:10.3390/min14030255` | `references_cache/doi_10_3390_min14030255.md` | Abstract (`2,140` chars) | Staré Ransko Zn-Cu mine tailings indigenous and laboratory-enriched *Acidithiobacillus ferrooxidans* + *Acidithiobacillus ferrivorans* bioleaching consortium | **Added (`CommunityMech:000486`)** in `kb/communities/Stare_Ransko_Mine_Tailings_Bioleaching_Consortium.yaml` |
| `doi:10.1007/s13213-019-01453-y` | `references_cache/doi_10_1007_s13213-019-01453-y.md` | Abstract (`1,812` chars) | Moderately thermophilic chalcopyrite bioleaching consortium (*Leptospirillum ferriphilum*, *Acidithiobacillus caldus*, *Sulfobacillus* sp., *Ferroplasma* sp.) at 40 °C under controlled pH 1.30–1.90 | **Added (`CommunityMech:000487`)** in `kb/communities/Moderate_Thermophile_Chalcopyrite_pH_Bioleaching_Consortium.yaml` |
| `doi:10.3389/fmicb.2024.1423741` | `references_cache/doi_10_3389_fmicb_2024_1423741.md` | Abstract (`2,095` chars) | *Bacillus licheniformis* strain 24 single-species hexavalent chromium Cr(VI) biosorption and bio-reduction isolate baseline | **Added (`CommunityMech:000488`)** in `data/isolates/Bacillus_licheniformis_Chromate_Biosorption.yaml` |
| `PMID:30343816` (`doi:10.1016/j.WASMAN.2018.09.044`) + `PMID:31203122` (`doi:10.1016/j.biortech.2019.121626`) | `references_cache/PMID_30343816.md` + `references_cache/PMID_31203122.md` | Abstracts (`1,546` + `1,590` chars) | *Acidithiobacillus* sp. single-species LED-enhanced heavy-metal bioleaching and *Acidithiobacillus ferrooxidans* Fe2+ oxidation acceleration under blue LED illumination | **Added (`CommunityMech:000489`)** in `data/isolates/Acidithiobacillus_LED_Metal_Bioleaching.yaml` |
| `doi:10.1128/aem.01906-20` | `references_cache/doi_10_1128_aem_01906-20.md` | Abstract (`1,878` chars) | *Ferrimicrobium acidiphilum* DSM 19497 single-species aerobic and anaerobic Fe(II)/Fe(III) electron-transfer isolate baseline with *a*, *b*, and *c*-type cytochromes | **Added (`CommunityMech:000490`)** in `data/isolates/Ferrimicrobium_acidiphilum_Iron_Respiration.yaml` |
| `PMID:28658891` (`doi:10.1007/s11356-017-9582-6`) | `references_cache/PMID_28658891.md` | Abstract (`1,320` chars) | Gold cyanidation tailings bioaugmentation with abbreviated taxa (`B.licheniformis`, `B. amyloliquefaciens`, `P.stutzeri`, `R.erythropolis`, `C.tropicalis`) | **Preserved unresolved candidate (source-limited)**: abstract uses genus-initial abbreviations without strain designations, inoculum ratios, or pairwise/guild mechanism resolution; full text required before promotion. |
| `PMID:27585725` (`doi:10.1038/srep32527`) | `references_cache/PMID_27585725.md` | Abstract + full text (`literature_20260405/PMID_27585725.md`) | Agricultural soil lime (CaCO3) amendment suppressing *Ralstonia solanacearum* bacterial wilt via pH shift and bulk soil metagenomic correlation | **Excluded (out of scope)**: bulk soil chemical amendment study with family-level amplicon correlation and no defined consortium, co-culture, or isolate functional baseline. |
| `PMID:32279217` (`doi:10.3389/fmicb.2020.00521`) | `references_cache/PMID_32279217.md` | Abstract (`1,185` chars) | Mini-review on microbial siderophores in metal mobilization | **Excluded (review article)**: secondary review without primary experimental community or isolate data. |
| `PMID:28600656` (`doi:10.1038/s41598-017-03335-8`) | `literature_20260405/PMID_28600656.md` | Full text | Single-strain *Methylosinus trichosporium* OB3b copper vs. lanthanum MMO gene-expression switch | **Excluded (out of scope)**: pure-culture transcriptional regulation study without community interaction or metal/bioprocess baseline mechanism. |
| `PMID:20878950` (`doi:10.1186/1471-2105-11-489`) | `literature_20260405/PMID_20878950.md` | Full text | Bioinformatics methodology paper on DNA microarray spot quality control | **Excluded (out of scope)**: non-ecological computational methods paper. |

---

## 3. Newly Curated Records (`CommunityMech:000484`–`000490`)

All 7 records were minted sequentially via `manage-identifiers` (`000484`–`000490`), written through the repository's validated writer (`communitymech.curation.write_validated_community`) with accompanying history sidecars (`communitymech.history.record_curation_event`), grounded in NCBITaxon, GTDB r220 (`data/gtdb/ncbi_gtdb_map.tsv`), ENVO, GO, and CHEBI, and verified with `linkml-term-validator` and `evidence_snippet_audit.py`:

| ID | Record Path | Category / Origin / State | Taxa Count | Interactions | Metals / Environment | Evidence Snippets |
|---|---|---|---:|---:|---|---:|
| `CommunityMech:000484` | `kb/communities/Aquifer_Sediment_Cable_Bacteria_Sulfur_Community.yaml` | `BIOREMEDIATION` / `NATURAL` / `PERTURBED` | 5 | 3 (`SYNTROPHY`, `CROSS_FEEDING`, `COMMENSALISM`) | `IRON`, `ENVO:00002007` (sediment) | 9 / 9 MATCH |
| `CommunityMech:000485` | `kb/communities/Dexing_Copper_Bioleaching_Heap_Community.yaml` | `BIOMINING` / `NATURAL` / `STABLE` | 5 | 2 (`MUTUALISM`, `CROSS_FEEDING`) | `COPPER`, `IRON`, `ZINC`, `ENVO:00001997` (acid mine drainage) | 11 / 11 MATCH |
| `CommunityMech:000486` | `kb/communities/Stare_Ransko_Mine_Tailings_Bioleaching_Consortium.yaml` | `BIOMINING` / `ENGINEERED` / `STABLE` | 2 | 1 (`MUTUALISM`) | `ZINC`, `COPPER`, `IRON`, `NICKEL`, `COBALT`, `ENVO:01001269` (mine tailings) | 8 / 8 MATCH |
| `CommunityMech:000487` | `kb/communities/Moderate_Thermophile_Chalcopyrite_pH_Bioleaching_Consortium.yaml` | `BIOMINING` / `ENGINEERED` / `STABLE` | 4 | 2 (`MUTUALISM`, `COMMENSALISM`) | `COPPER`, `IRON`, `ENVO:00001998` (soil) | 9 / 9 MATCH |
| `CommunityMech:000488` | `data/isolates/Bacillus_licheniformis_Chromate_Biosorption.yaml` | `BIOREMEDIATION` / `NATURAL` / `PERTURBED` | 1 | 0 (isolate baseline) | `CHROMIUM`, `ENVO:00002001` (wastewater) | 4 / 4 MATCH |
| `CommunityMech:000489` | `data/isolates/Acidithiobacillus_LED_Metal_Bioleaching.yaml` | `BIOMINING` / `ENGINEERED` / `STABLE` | 1 | 0 (isolate baseline) | `COPPER`, `ZINC`, `IRON`, `CADMIUM`, `LEAD`, `ENVO:00002034` (biofilm) | 5 / 5 MATCH |
| `CommunityMech:000490` | `data/isolates/Ferrimicrobium_acidiphilum_Iron_Respiration.yaml` | `BIOMINING` / `NATURAL` / `STABLE` | 1 | 0 (isolate baseline) | `IRON`, `ENVO:00001997` (acid mine drainage) | 5 / 5 MATCH |

---

## 4. Repeated Bounded-Frontier Search Verification

After curating `CommunityMech:000484`–`000490`, a repeated programmatic pass over `references_cache/` (`1,417` files) and `literature_20260405/` (`133` files) was executed against the updated corpus (`477` communities in `kb/communities/*.yaml` + `12` isolates in `data/isolates/*.yaml` = `489` records total):

- **Remaining admissible uncurated community or isolate papers in bounded frontier**: `0`
- **Preserved unresolved source-limited candidates**: `1` (`PMID:28658891` / `doi:10.1007/s11356-017-9582-6`, abstract-only gold cyanidation tailings bioaugmentation study requiring full text for species/strain and mechanism disambiguation)
- **Out-of-scope / review / non-community cached items**: `4` (`PMID:27585725`, `PMID:32279217`, `PMID:28600656`, `PMID:20878950`)

---

## 5. Validation & Quality Gate Summary

All repository validation gates passed on the updated `489`-record corpus (`477` communities + `12` isolates + `2` taxa):

1. `scripts/validate_strict.py`: `484` community/history files scanned, `0` `ERROR` rows (`EXIT=0`).
2. `scripts/validate_gtdb_coherence.py`: `486` files checked (`kb/communities`, `kb/taxa`, `data/isolates`), `0` incoherent blocks, `0` malformed lineages, `0` lineage conflicts (`EXIT=0`).
3. `scripts/validate_yaml_scalars.py`: `486` files checked, `0` truncated scalars (`EXIT=0`).
4. `scripts/audit_writers.py`: `30` writer scripts audited, `0` violations (`EXIT=0`).
5. `linkml-term-validator`: all 7 new records validated against `src/communitymech/schema/communitymech.yaml` with `--cache-dir cache --labels` (`EXIT=0`).
6. `scripts/evidence_snippet_audit.py`: `51` snippets audited across the 7 new records (`51 MATCH`, `0 MISMATCH`).
7. `pytest`: `tests/test_causal_review_batch109.py`, `tests/test_gtdb_coherence_validator.py`, `tests/test_is_reclassified_semantics.py`, `tests/test_transwell_participants.py`, and `tests/test_stage6_infrastructure.py` passed (`EXIT=0`).
8. `docs/` synchronization (`communitymech.render`, `communitymech.export`, `communitymech.datamodel`): `0` diff against freshly rendered output.
