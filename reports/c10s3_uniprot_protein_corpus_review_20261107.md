# Cycle 10 Stage 3 (`protein_examples`) Corpus Review & UniProt Protein Curation Report

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle / Stage**: Cycle 10, Stage 3 (`protein_examples`)
- **Date**: 2026-11-07
- **Base Commit (`main`)**: `915eecf8c8fea3fd20559c7861e821dc279fcc21`
- **Skills Followed**:
  - `.claude/skills/add-uniprot-protein-examples/SKILL.md`
  - `.claude/skills/curate-yaml-record/SKILL.md`
  - `.claude/skills/communitymech-evolve-workflow/SKILL.md`

---

## 1. Corpus Scope & Applicability Accounting (`521` Total Records)

All **521** canonical YAML records across the three repository record roots were audited at commit `915eecf8c8fea3fd20559c7861e821dc279fcc21`:

| Record Root | Root Class | Record Count | UniProtKB / `CommonTaxon` Status |
|---|---|---:|---|
| `kb/taxa/*.yaml` | `CommonTaxon` | **2** | **9** verified `UniProtKB:` `GeneAnnotation` entries (**55** total cached `EvidenceItem`s after Cycle 10 Stage 3; up from **51** after Cycle 9 Stage 3) |
| `kb/communities/*.yaml` | `MicrobialCommunity` | **507** | **17** records linked via `taxonomy[].common_taxon` to `kb/taxa/*.yaml` (`12` to `CommunityMech:taxon:000001` including newly added `CommunityMech:000523`, `6` to `CommunityMech:taxon:000002`, `1` overlap on `CommunityMech:000177`) |
| `data/isolates/*.yaml` | `MicrobialCommunity` | **12** | **1** isolate baseline (`CommunityMech:000524`) linked via `taxonomy[].common_taxon: CommunityMech:taxon:000001` to `kb/taxa/Shewanella_oneidensis_MR1.yaml`; **11** single-strain isolate baselines without sequenced isolate proteomes or `UniProtKB:` accessions in cached sources |
| **Total** | — | **521** | **2** `CommonTaxon` records + **519** `MicrobialCommunity` records |

### Partition of the `519` `MicrobialCommunity` Records (`kb/communities/` + `data/isolates/`)

1. **Linked to reusable `CommonTaxon` records (`kb/taxa/*.yaml`) with verified `UniProtKB:` protein annotations (`18` records: `17` in `kb/communities/` + `1` in `data/isolates/`)**:
   - **`CommunityMech:taxon:000001` (`kb/taxa/Shewanella_oneidensis_MR1.yaml`, `NCBITaxon:211586`, `GCF_000146165.2`) — `13` records (`12` communities + `1` isolate baseline)**:
     - `CommunityMech:000140` (`Corynebacterium_glutamicum_Shewanella_oneidensis_Succinic_Acid_Coculture.yaml`)
     - `CommunityMech:000177` (`Shewanella_Geobacter_Exoelectrogenic_Biofilm_Community.yaml`)
     - `CommunityMech:000178` (`Shewanella_Streptococcus_Starch_Microbial_Fuel_Cell.yaml`)
     - `CommunityMech:000211` (`Synechococcus_Shewanella_Dlactate_Biophotovoltaic_Consortium.yaml`)
     - `CommunityMech:000279` (`Shewanella_oneidensis_Rhodopseudomonas_palustris_Electrosyntrophic_Coculture.yaml`)
     - `CommunityMech:000376` (`Electrosynthetic_Consortia_Shewanella_Clostridium_Acetobacterium_Acetate.yaml`)
     - `CommunityMech:000385` (`SO3_BS3_Lithium_Battery_Bioleaching_Consortium.yaml`)
     - `CommunityMech:000419` (`Shewanella_Anammox_Delta_nrfA_Nitrite_Coupled_Consortium.yaml`)
     - `CommunityMech:000420` (`Shewanella_Pseudomonas_Fe0_Electrosyntrophic_Denitrifying_Consortium.yaml`)
     - `CommunityMech:000519` (`SO1_BS1_Lithium_Battery_Bioleaching_Consortium.yaml`)
     - `CommunityMech:000520` (`SO2_BS2_Lithium_Battery_Bioleaching_Consortium.yaml`)
     - `CommunityMech:000523` (`SO2_BS1_Lithium_Battery_Bioleaching_Consortium.yaml`) — **added in Cycle 10 Stage 1**
     - `CommunityMech:000524` (`data/isolates/Shewanella_Oneidensis_SO1_NCM_Bioleaching_Isolate_Baseline.yaml`) — **added in Cycle 10 Stage 1**
   - **`CommunityMech:taxon:000002` (`kb/taxa/Geobacter_sulfurreducens.yaml`, `NCBITaxon:35554`, `GCF_000007985.2`) — `6` records**:
     - `CommunityMech:000031` (`Geobacter_Methanosarcina_Propionate_Bone_Char_Coculture.yaml`)
     - `CommunityMech:000134` (`Geobacter_Pili_Deficient_Direct_Contact_Iet_Coculture.yaml`)
     - `CommunityMech:000177` (`Shewanella_Geobacter_Exoelectrogenic_Biofilm_Community.yaml`)
     - `CommunityMech:000201` (`Geobacter_Pseudomonas_Formate_Fumarate_Electroactive_Coculture.yaml`)
     - `CommunityMech:000241` (`Rifle_Groundwater_Acetate_Electrode_Bioanode_Community.yaml`)
     - `CommunityMech:000276` (`Syntrophic_Sludge_Direct_Interspecies_Electron_Transfer_Consortium.yaml`)
   - *Overlap*: `CommunityMech:000177` references both `CommunityMech:taxon:000001` and `CommunityMech:taxon:000002` (`13 + 6 - 1 = 18` distinct `MicrobialCommunity` records).

2. **16S amplicon / metagenomic / phylum-, family-, or genus-rank guild or unsequenced environmental isolate communities (`352` records)**:
   - Taxa are resolved at genus, family, order, phylum, or unsequenced environmental isolate rank without an exact sequenced strain proteome (`GCF_`/`GCA_`). Under `.claude/skills/add-uniprot-protein-examples/SKILL.md` ("Only attach a UniProt accession when the organism and gene context match the record"), assigning a reference-strain UniProtKB accession would violate organism- and sequence-scope rules.

3. **Defined / species-grounded communities and isolate baselines whose cached sources assay metabolites, fermentation kinetics, or growth yields without naming specific protein accessions or sequenced isolate proteomes (`129` records: `118` in `kb/communities/` + `11` in `data/isolates/`)**:
   - Increased from `127` in Cycle 9 Stage 3 to `129` in Cycle 10 Stage 3 due to the addition of `CommunityMech:000522` (`kb/communities/Parmigiano_NWS_Set3_LAB_Triculture.yaml`) and `CommunityMech:000525` (`data/isolates/Bacillus_Subtilis_BS1_Brewing_Wastewater_Isolate_Baseline.yaml`) in Cycle 10 Stage 1.

4. **Species- / strain-grounded communities whose cached sources name gene symbols or locus tags (`narG`, `nirK`, `nosZ`, `mcrA`, `acsB`, `fhs`, `nifH`, `amoA`, `hao`, `nxrB`, `dsrAB`, `hydA`, `fldA`/`fmnA`/`dmkA`, `nqrF`, `tauD`, `iscS`, `tenA`) without a local offline `UniProtKB:` mapping table or without `CommonTaxon` promotion (`20` records)**:
   - Documented in Section 4 below as offline-proteome/reference-cache scope boundaries.

---

## 2. Detailed Audit of Cycle 10 Stage 1 Additions (`CommunityMech:000522` – `CommunityMech:000525`)

| Record ID | File Path | Pre-Stage-3 / Post-Stage-3 SHA-256 | Primary Reference | Taxa & Grounding | Stage 3 Protein / `CommonTaxon` Audit |
|---|---|---|---|---|---|
| `CommunityMech:000522` | `kb/communities/Parmigiano_NWS_Set3_LAB_Triculture.yaml` | `178f803afb7a8bef72f1f34a3eabefc751cc4095c11b6b28d1bf736ee7af6749` (unchanged) | `PMID:41859451` (full text cached) | *Lactobacillus helveticus* (`NCBITaxon:1587`, strains `Lh29`, `Lh28`), *Lactobacillus delbrueckii* (`NCBITaxon:1584`, strain `Ld25`), *Lacticaseibacillus rhamnosus* (`NCBITaxon:47715`, strain `Lr2136`) | **Inapplicable (no sequenced strain proteome or UniProtKB accession in source)**: `PMID:41859451` characterizes Set 3 via species-specific qPCR (`pheS`, `clpX`, `mutL` amplification targets), milk acidification kinetics (`ΔpH`), lactose consumption, galactose accumulation, and D-/L-lactic acid enantiomer production without genome assemblies (`GCF_`/`GCA_`) or UniProtKB protein accessions for dairy isolates `Lh29`, `Lh28`, `Ld25`, or `Lr2136`. |
| `CommunityMech:000523` | `kb/communities/SO2_BS1_Lithium_Battery_Bioleaching_Consortium.yaml` | `6e09328a97a58487fe879282ebc174db8c5990a6db79a35e2f96dafffc5990a6db79a35e2f96dafffc5d1c93` (`6e09328a97a58487fe879282ebc174db8c5990a6db79a35e2f96dafffc5d1c93`, unchanged) | `PMID:42733304` (abstract + full text cached) | *Shewanella oneidensis* MR-1 (`NCBITaxon:211586`, strain `SO2` carrying `pYYDT-C5-ribADEHC`, linked to `common_taxon: CommunityMech:taxon:000001`), *Bacillus subtilis* (`NCBITaxon:1423`, strain `BS1` carrying `pCE2-P43-adh-aldH` in *B. subtilis* 168) | **Linked to `CommunityMech:taxon:000001` (`kb/taxa/Shewanella_oneidensis_MR1.yaml`)**: `SO2` is engineered in the *S. oneidensis* MR-1 background (`GCF_000146165.2`) and uses the curated MtrCAB/OmcA/CymA pathway (`UniProtKB:Q8EG33`, `UniProtKB:Q8EG34`, `UniProtKB:Q8EG35`, `UniProtKB:Q8EG32`, `UniProtKB:Q8E945`) and riboflavin shuttles to reduce spent NCM cathode particles. Added verified `PMID:42733304` cellular-electrophysiology `EvidenceItem`s on `mtrC` (`UniProtKB:Q8EG33`) and `omcA` (`UniProtKB:Q8EG32`) in `kb/taxa/Shewanella_oneidensis_MR1.yaml` and registered `SO2_BS1_Lithium_Battery_Bioleaching_Consortium.yaml` in `tests/test_taxon_records.py::test_community_links_common_taxon`. |
| `CommunityMech:000524` | `data/isolates/Shewanella_Oneidensis_SO1_NCM_Bioleaching_Isolate_Baseline.yaml` | `671bdcdf702788c7280e49be29c0e95455be1ca1ded72119ede0b0da864154f1` (unchanged) | `PMID:42733304` (abstract + full text cached) | *Shewanella oneidensis* MR-1 (`NCBITaxon:211586`, wild-type strain `SO1`, linked to `common_taxon: CommunityMech:taxon:000001`) | **Linked to `CommunityMech:taxon:000001` (`kb/taxa/Shewanella_oneidensis_MR1.yaml`)**: First `data/isolates/` baseline record linking directly to `CommunityMech:taxon:000001`. Wild-type *S. oneidensis* MR-1 (`SO1`, `GCF_000146165.2`) utilizes `mtrC` (`UniProtKB:Q8EG33`) and `omcA` (`UniProtKB:Q8EG32`) with endogenous riboflavin to transfer electrons to spent NCM particles (`19.6%` Li, `14.1%` Co, `18.3%` Ni, `24.1%` Mn leaching efficiency). Registered in `tests/test_taxon_records.py::test_community_links_common_taxon`. |
| `CommunityMech:000525` | `data/isolates/Bacillus_Subtilis_BS1_Brewing_Wastewater_Isolate_Baseline.yaml` | `165451ae89b467384dae87f9e5ef00d4b68fc7823037b3b96226e632bf186947` (unchanged) | `PMID:42733304` (abstract + full text cached) | *Bacillus subtilis* (`NCBITaxon:1423`, engineered strain `BS1` = *B. subtilis* 168 carrying plasmid `pCE2` with heterologous `P43::adh` from *Saccharomyces cerevisiae* BY4341 and `aldH` from *Issatchenkia terricola* XJ-2) | **Inapplicable (heterologous yeast genes without locus tags, sequence accessions, or UniProtKB identifiers)**: `PMID:42733304` describes `BS1` as *B. subtilis* 168 expressing heterologous yeast alcohol dehydrogenase (`adh` from *S. cerevisiae* BY4341, a multi-paralog `ADH1`–`ADH5` gene family) and acetaldehyde dehydrogenase (`aldH` from non-model yeast *Issatchenkia terricola* XJ-2) without locus tags, nucleotide/protein accessions, or endogenous *B. subtilis* 168 protein identifiers in the article text. |

---

## 3. Verified `CommonTaxon` Updates in Cycle 10 Stage 3 (`51 -> 55` Gene-Level `EvidenceItem`s)

### 3.1 `kb/taxa/Shewanella_oneidensis_MR1.yaml` (`CommunityMech:taxon:000001`)

- **Pre-Stage-3 SHA-256**: `de999e7aecb248114e22e9fad626a92004249d396f301d2851eec4bf54de469d`
- **Post-Stage-3 SHA-256**: `c841f96e490b0406dbccd7bca516dd0aacb42c34cf5f6042e99740ebfe86d49e`
- **History Sidecar**: `history/records/Shewanella_oneidensis_MR1/2026-11-07T154500Z-antigravity-c10s301.yaml`
- **Total Gene-Level `EvidenceItem`s**: `28 -> 30` (`5` curated `UniProtKB:` genes: `mtrC` `8`, `mtrB` `4`, `mtrA` `5`, `omcA` `8`, `cymA` `5`)
- **Added `EvidenceItem`s (`+2`)**:
  1. **`mtrC` (`UniProtKB:Q8EG33`, locus tag `SO_1778`, `GCF_000146165.2`)**:
     - `reference`: `PMID:42733304` (`references_cache/PMID_42733304.txt` and `references_cache/PMID_42733304.md`)
     - `supports`: `SUPPORT`
     - `evidence_source`: `IN_VITRO`
     - `snippet`: `"Cellular electrophysiology analyses reveal that S. oneidensis utilizes c‐type cytochromes MtrC and OmcA, and riboflavin to transfer electrons to NCM."`
  2. **`omcA` (`UniProtKB:Q8EG32`, locus tag `SO_1779`, `GCF_000146165.2`)**:
     - `reference`: `PMID:42733304` (`references_cache/PMID_42733304.txt` and `references_cache/PMID_42733304.md`)
     - `supports`: `SUPPORT`
     - `evidence_source`: `IN_VITRO`
     - `snippet`: `"Cellular electrophysiology analyses reveal that S. oneidensis utilizes c‐type cytochromes MtrC and OmcA, and riboflavin to transfer electrons to NCM."`

### 3.2 `kb/taxa/Geobacter_sulfurreducens.yaml` (`CommunityMech:taxon:000002`)

- **Pre-Stage-3 SHA-256**: `0375aa7a83cdd80a150c797769261014d4dcf7c7f94de1f6b3d6edf058f0a37b`
- **Post-Stage-3 SHA-256**: `5acba5205a69a57fb7270a7e92e156ca3f26affd7035aaa8216bb29307b57aaf`
- **History Sidecar**: `history/records/Geobacter_sulfurreducens/2026-11-07T154500Z-antigravity-c10s302.yaml`
- **Total Gene-Level `EvidenceItem`s**: `23 -> 25` (`4` curated `UniProtKB:` genes: `pilA` `7`, `omcS` `9`, `omcZ` `5`, `omcB` `4`)
- **Added `EvidenceItem`s (`+2`)**:
  1. **`pilA` (`UniProtKB:Q74BW5`, locus tag `GSU1496`, `GCF_000007985.2`)**:
     - `reference`: `PMID:41876513` (`references_cache/PMID_41876513.md`, primary reference for `CommunityMech:000462`)
     - `supports`: `SUPPORT`
     - `evidence_source`: `COMPUTATIONAL`
     - `snippet`: `"To identify putative electrically conductive e-pili, we used the e-pilin protein sequence from Geobacter sulfurreducens PCA (GenBank accession: AAR34870.1 ) as a reference"`
  2. **`omcB` (`UniProtKB:Q74A86`, locus tag `GSU2737`, `GCF_000007985.2`)**:
     - `reference`: `PMID:41876513` (`references_cache/PMID_41876513.md`, primary reference for `CommunityMech:000462`)
     - `supports`: `SUPPORT`
     - `evidence_source`: `COMPUTATIONAL`
     - `snippet`: `"In Ca. Geosyntrophus, both PCCs mirrored the gene organization of G. sulfurreducens PCCs 35 , a porin followed by a periplasmic facing MHC (penta- or octaheme) and an outer-membrane duodecaheme MHC (Fig.  4 )."`

---

## 4. Representation & Offline Verification Boundaries

1. **No schema or writer blockers for `CommonTaxon` (`kb/taxa/*.yaml`)**:
   - `write_validated_community(doc, path, target_class="CommonTaxon")` in `src/communitymech/validation/write_validated.py` validates `CommonTaxon` records in-memory against `src/communitymech/schema/communitymech.yaml` before writing and passes `scripts/audit_writers.py`.
2. **Offline UniProtKB verification boundary for the `20` gene-symbol-bearing community records**:
   - Under `AGENTS.md` ("Do not make network calls, spend provider credits, or apply generated curation unless the task authorizes it") and `.claude/skills/add-uniprot-protein-examples/SKILL.md` ("Prefer verified `UniProtKB:` identifiers when you can confirm the exact accession for that organism and gene; otherwise leave existing locus tags in place rather than guessing"), no unverified `UniProtKB:` accessions were guessed for taxa lacking a local offline UniProt proteome table in the repository.
