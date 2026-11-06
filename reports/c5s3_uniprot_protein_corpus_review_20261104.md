# Cycle 5 Stage 3 — Corpus-Wide UniProt Protein Examples Review & Audit

**Date:** 2026-11-04
**Run / Cycle / Stage:** `mech-goal-sequence-20261019`, Cycle 5, Stage 3 (`protein_examples`)
**Repository:** `CultureBotAI/CommunityMech`
**Skill Source of Truth:** `.claude/skills/add-uniprot-protein-examples/SKILL.md`, `.claude/skills/curate-yaml-record/SKILL.md`, `.claude/skills/communitymech-evolve-workflow/SKILL.md`

---

## 1. Executive Summary & Corpus Scope

All **496** records in `CultureBotAI/CommunityMech` were audited for verified `UniProtKB:` protein example annotations (`CommonTaxon.genes[]` `GeneAnnotation` entries and `TaxonomicComposition.common_taxon` community linkages):

| Record Root | Schema Target Class | Record Count | UniProtKB Coverage / Linkage Status |
|---|---|---:|---|
| `kb/taxa/*.yaml` | `CommonTaxon` | **2** | **100%** (2 / 2 records; **9** `GeneAnnotation` entries, all using `UniProtKB:[A-Z0-9]+` with locus tags, NCBI RefSeq `GCF_` genome assemblies, GO terms, `supports_roles`, `supports_interaction`, and **36** verbatim cached `EvidenceItem`s, up from 32 in Cycle 4 Stage 3) |
| `kb/communities/*.yaml` | `MicrobialCommunity` | **485** | **14** records carry **15** `TaxonomicComposition.common_taxon` links (`9` to `CommunityMech:taxon:000001`, `6` to `CommunityMech:taxon:000002`); **0** unlinked *Shewanella oneidensis* or *Geobacter sulfurreducens* entries; **471** records documented as inapplicable / schema-bounded (including the 4 new Cycle 5 Stage 1 records `CommunityMech:000497`–`000500`) |
| `data/isolates/*.yaml` | `MicrobialCommunity` | **9** | **0** `common_taxon` links; **9** records documented as inapplicable (single-isolate cohorts without *S. oneidensis* or *G. sulfurreducens* members or gene-resolved `CommonTaxon` records) |
| **Total Corpus** | `CommonTaxon` + `MicrobialCommunity` | **496** | **2** `CommonTaxon` records (**9** `UniProtKB:` protein examples, **36** `EvidenceItem`s) + **14** linked `MicrobialCommunity` records (**15** `common_taxon` references) |

---

## 2. Native Representation Architecture & Schema Boundaries

In `src/communitymech/schema/communitymech.yaml`, protein and gene examples are represented exclusively on reusable `CommonTaxon` records in `kb/taxa/*.yaml` via `GeneAnnotation` (`CommonTaxon.genes[]`):

- `gene_id` (`string`, `required: true`): Canonical protein/gene CURIE (`UniProtKB:<accession>` preferred per `.claude/skills/add-uniprot-protein-examples/SKILL.md`).
- `gene_symbol` (`string`): Short gene symbol (`mtrC`, `mtrB`, `mtrA`, `omcA`, `cymA`, `pilA`, `omcS`, `omcZ`, `omcB`).
- `locus_tag` (`string`): Reference-genome locus tag (`SO_1778`, `SO_1776`, `SO_1777`, `SO_1779`, `SO_4591`, `GSU1496`, `GSU2504`, `GSU2076`, `GSU2737`).
- `product` (`string`): Verified UniProtKB protein product description.
- `genome` (`string`): Reference `GCF_` assembly id declared in `CommonTaxon.genomes[]` (`GCF_000146165.2` or `GCF_000007985.2`).
- `kegg_ortholog` (`string`, pattern `^K\d{5}$`): Optional KO identifier where verified.
- `go_terms` (`OntologyTerm[]`): Molecular function / biological process / cellular component GO terms (`GO:0009055`, `GO:0020037`, `GO:0015288`, `GO:0009289`).
- `supports_roles` (`FunctionalRoleEnum[]`): Community functional roles supported by the protein (`ELECTRON_DONOR`, `ELECTROGEN`, `SYNTROPHIC_PARTNER`).
- `supports_interaction` (`string`): Narrative mechanism connecting the protein to community-level ecological interactions.
- `evidence` (`EvidenceItem[]`): Verbatim literature snippets (`PMID:` cached in `references_cache/`) supporting the gene/protein's mechanistic role.

Community records (`MicrobialCommunity` in `kb/communities/*.yaml` and `data/isolates/*.yaml`) do **not** have a `genes` or `proteins` slot on `TaxonomicComposition` or `EcologicalInteraction`; instead, `TaxonomicComposition.common_taxon` (`CommunityMech:taxon:NNNNNN`) links community members to their reusable `CommonTaxon` record and its `genes[]` annotations.

---

## 3. Cycle 5 Stage 3 Curated Evidence Additions (`kb/taxa/Geobacter_sulfurreducens.yaml` & `kb/taxa/Shewanella_oneidensis_MR1.yaml`)

During the Cycle 5 Stage 3 audit of cached full-text references across the corpus, **4** new source-verified `EvidenceItem` entries were curated across `kb/taxa/Geobacter_sulfurreducens.yaml` (`CommunityMech:taxon:000002`, `NCBITaxon:35554`, reference assembly `GCF_000007985.2`) and `kb/taxa/Shewanella_oneidensis_MR1.yaml` (`CommunityMech:taxon:000001`, `NCBITaxon:211586`, reference assembly `GCF_000146165.2`) using `record_curation_event` and `write_validated_community(..., target_class="CommonTaxon")`:

### 3.1 `kb/taxa/Geobacter_sulfurreducens.yaml` (`CommunityMech:taxon:000002`)
- **Pre-edit SHA-256:** `b081a3672463ea1a9b240583e63d3273bfdf27d600be6e2df99c85b4394f0a27` (4 genes, 13 `EvidenceItem`s)
- **Post-edit SHA-256:** `5d2b49dc2fd42756bdc303302e135ad208c10f76de161e618545a99dd1f6e142` (4 genes, 15 `EvidenceItem`s)
- **History sidecar:** `history/records/Geobacter_sulfurreducens/2026-11-04T014000Z-antigravity-c5s302.yaml`

1. **`PMID:28287150` (`references_cache/PMID_28287150.txt`, Moscoviz et al. 2017, *Sci. Rep.* 7:44334 — primary reference for `CommunityMech:000031`, `kb/communities/Geobacter_Clostridium_Interspecies_Electron_Transfer_Coculture.yaml`) on `pilA` (`UniProtKB:Q74BW5`, `GSU1496`)**:
   - **Organism / Strain / Sequence Scope:** `PMID:28287150` experimentally cultivates *Geobacter sulfurreducens* DSM 12127 (= type strain PCA = ATCC 51573, the exact strain of reference assembly `GCF_000007985.2`) with *Clostridium pasteurianum* DSM 525 (`CommunityMech:000031`, which links `taxonomy[0]` to `CommunityMech:taxon:000002`). In the Discussion of `PMID:28287150`, the authors cite prior proteomic characterization of *G. sulfurreducens* DSM 12127 showing increased synthesis of the `pilA` protein (`UniProtKB:Q74BW5`, `GSU1496`) involved in nanowire conductivity under long-term electron-acceptor limitation as background for aggregate pre-culture preparation, while contact-dependent nanowire transfer in the *G. sulfurreducens*–*C. pasteurianum* coculture itself was not established (and was contested by `PMID:34939136`).
   - **Curated `EvidenceItem` (`pilA`, `supports: PARTIAL`, `evidence_source: IN_VITRO`):**
     - `snippet`: `"In particular, this increased the synthesis of the pilA protein involved in nanowires conductivity 7 ."`
     - `explanation`: `"PARTIAL - cites prior proteomic characterization of Geobacter sulfurreducens DSM 12127 (= PCA = ATCC 51573, GCF_000007985.2) showing increased synthesis of PilA (GSU1496, UniProtKB:Q74BW5) involved in nanowire conductivity under long-term electron-acceptor limitation; used as pre-culture background in CommunityMech:000031 where contact-dependent nanowire transfer in the Clostridium pasteurianum coculture itself was not established."`

2. **`PMID:32849356` (`references_cache/PMID_32849356.md`, Arbour et al. 2020, *Front. Microbiol.* 11:1694 — primary reference for `CommunityMech:000241`, `kb/communities/Rifle_Aquifer_Bioanode_EET_Community.yaml`) on `omcS` (`UniProtKB:Q749X9`, `GSU2504`)**:
   - **Organism / Strain / Sequence Scope:** `PMID:32849356` explicitly cites the canonical *Geobacter sulfurreducens* PCA OmcS RefSeq protein accession `WP_119334099.1` (corresponding to locus `GSU2504` / `UniProtKB:Q749X9` in `GCF_000007985.2`) used as the BLASTP query to identify extracellular electron-transfer cytochrome filament homologs across the Rifle bioanode metagenome-assembled genomes (`CommunityMech:000241`).
   - **Curated `EvidenceItem` (`omcS`, `supports: SUPPORT`, `evidence_source: COMPUTATIONAL`):**
     - `snippet`: `"A search for cytochrome OmcS homologs was performed as above for e-pili against the same internal BLASTP database, using the G. sulfurreducens OmcS sequence ( WP_119334099.1 ) as query, giving 47 sequences with default search parameters."`
     - `explanation`: `"Uses the canonical Geobacter sulfurreducens PCA OmcS protein sequence (RefSeq WP_119334099.1, corresponding to locus GSU2504 / UniProtKB:Q749X9 in reference assembly GCF_000007985.2) as the reference BLASTP query to identify extracellular electron-transfer cytochrome filament homologs in the Rifle bioanode community (CommunityMech:000241)."`

### 3.2 `kb/taxa/Shewanella_oneidensis_MR1.yaml` (`CommunityMech:taxon:000001`)
- **Pre-edit SHA-256:** `8d3910162407ca61bcb5bc1ebbec2c7f1f57e32bea34149d4f873a86bc257061` (5 genes, 19 `EvidenceItem`s)
- **Post-edit SHA-256:** `df038771231777f9846f246f0c578484c697845043103008586e813badd113f8` (5 genes, 21 `EvidenceItem`s)
- **History sidecar:** `history/records/Shewanella_oneidensis_MR1/2026-11-04T014000Z-antigravity-c5s301.yaml`

1. **`PMID:32849356` (`references_cache/PMID_32849356.md`, Arbour et al. 2020 — primary reference for `CommunityMech:000241`) on `mtrB` (`UniProtKB:Q8EG34`, `SO_1776`)**:
   - **Organism / Strain / Sequence Scope:** Explicitly names `Shewanella oneidensis MR-1` (`NCBITaxon:211586`, `GCF_000146165.2`) and `MtrB (SO_1776)` (`UniProtKB:Q8EG34`), anchoring the verbatim locus tag `SO_1776` in a cached snippet as the reference outer-membrane porin protein used to build profile HMMs for porin-cytochrome complex (PCC) extracellular electron-transfer conduits.
   - **Curated `EvidenceItem` (`mtrB`, `supports: SUPPORT`, `evidence_source: COMPUTATIONAL`):**
     - `snippet`: `"Four separate models were constructed based on the following porin proteins from Shewanella oneidensis MR-1 and Geobacter sulfurreducens PCA: MtrB (SO_1776) ( Hartshorne et al., 2009 ), OmbB (GSU2733), ExtB (GSU2644)/ExtE (GSU2726), and ExtI (GSU2939) ( Liu et al., 2014 ; Chan et al., 2016 )."`
     - `explanation`: `"Explicitly identifies Shewanella oneidensis MR-1 MtrB by its canonical locus tag SO_1776 (UniProtKB:Q8EG34, GCF_000146165.2) as the reference outer-membrane porin protein used to build profile HMMs for porin-cytochrome complex (PCC) extracellular electron-transfer conduits in CommunityMech:000241."`

2. **`PMID:32849356` (`references_cache/PMID_32849356.md`, Arbour et al. 2020 — primary reference for `CommunityMech:000241`) on `mtrA` (`UniProtKB:Q8EG35`, `SO_1777`)**:
   - **Organism / Strain / Sequence Scope:** Explicitly names `"the decaheme periplasmic cytochrome MtrA from Shewanella oneidensis MR-1"` (`SO_1777`, `UniProtKB:Q8EG35`, `GCF_000146165.2`) and reports its heme-packing density (`25.1 residues per heme` across 10 heme-binding motifs) as the reference standard for extracellular electron-transfer multiheme cytochromes.
   - **Curated `EvidenceItem` (`mtrA`, `supports: SUPPORT`, `evidence_source: COMPUTATIONAL`):**
     - `snippet`: `"These MHCs display a remarkably high density of heme-binding motifs: the 24- and 49-heme cytochromes use only 22.4 and 23.4 residues per heme, respectively (for reference, the decaheme periplasmic cytochrome MtrA from Shewanella oneidensis MR-1 has 25.1 residues per heme; see Figure 4 )."`
     - `explanation`: `"Characterizes the reference decaheme periplasmic cytochrome MtrA from Shewanella oneidensis MR-1 (SO_1777, UniProtKB:Q8EG35, GCF_000146165.2) as having 10 heme-binding motifs at 25.1 amino-acid residues per heme during comparative sequence analysis of extracellular electron-transfer multiheme cytochromes in CommunityMech:000241."`

---

## 4. Complete Inventory of Verified `UniProtKB` Protein Examples (`kb/taxa/*.yaml`)

### 4.1 `kb/taxa/Shewanella_oneidensis_MR1.yaml` (`CommunityMech:taxon:000001`)
- **Taxon:** *Shewanella oneidensis* MR-1 (`NCBITaxon:211586`, `GTDB:s__Shewanella_oneidensis`)
- **Reference Genome:** `GCF_000146165.2` (`ASM14616v2`)
- **SHA-256 (post-edit):** `df038771231777f9846f246f0c578484c697845043103008586e813badd113f8`

| `gene_symbol` | `gene_id` | `locus_tag` | `kegg_ortholog` | `go_terms` | `supports_roles` | Cached `EvidenceItem` References |
|---|---|---|---|---|---|---|
| `mtrC` | `UniProtKB:Q8EG33` | `SO_1778` | `K07234` | `GO:0009055` (electron transfer activity), `GO:0020037` (heme binding) | `ELECTRON_DONOR`, `ELECTROGEN`, `SYNTROPHIC_PARTNER` | `PMID:42733304` (×2), `PMID:41236292`, `PMID:39504696`, `PMID:31537786` (5 items) |
| `mtrB` | `UniProtKB:Q8EG34` | `SO_1776` | — | `GO:0015288` (porin activity) | `ELECTRON_DONOR`, `ELECTROGEN`, `SYNTROPHIC_PARTNER` | `PMID:42733304`, `PMID:41210787`, `PMID:31537786`, `PMID:32849356` (4 items) |
| `mtrA` | `UniProtKB:Q8EG35` | `SO_1777` | — | `GO:0009055` (electron transfer activity), `GO:0020037` (heme binding) | `ELECTRON_DONOR`, `ELECTROGEN`, `SYNTROPHIC_PARTNER` | `PMID:42733304`, `PMID:41210787`, `PMID:31537786`, `PMID:32849356` (4 items) |
| `omcA` | `UniProtKB:Q8EG32` | `SO_1779` | — | `GO:0009055` (electron transfer activity), `GO:0020037` (heme binding) | `ELECTRON_DONOR`, `ELECTROGEN`, `SYNTROPHIC_PARTNER` | `PMID:42733304` (×2), `PMID:41236292`, `PMID:39504696`, `PMID:31537786` (5 items) |
| `cymA` | `UniProtKB:Q8E945` | `SO_4591` | — | `GO:0009055` (electron transfer activity), `GO:0020037` (heme binding) | `ELECTRON_DONOR`, `ELECTROGEN`, `SYNTROPHIC_PARTNER` | `PMID:42733304`, `PMID:39504696`, `PMID:31537786` (3 items) |

### 4.2 `kb/taxa/Geobacter_sulfurreducens.yaml` (`CommunityMech:taxon:000002`)
- **Taxon:** *Geobacter sulfurreducens* (`NCBITaxon:35554`, `GTDB:s__Geobacter_sulfurreducens`)
- **Reference Genome:** `GCF_000007985.2` (`ASM798v2`)
- **SHA-256 (post-edit):** `5d2b49dc2fd42756bdc303302e135ad208c10f76de161e618545a99dd1f6e142`

| `gene_symbol` | `gene_id` | `locus_tag` | `kegg_ortholog` | `go_terms` | `supports_roles` | Cached `EvidenceItem` References |
|---|---|---|---|---|---|---|
| `pilA` | `UniProtKB:Q74BW5` | `GSU1496` | `K02650` | `GO:0009055` (electron transfer activity), `GO:0009289` (pilus) | `ELECTRON_DONOR`, `SYNTROPHIC_PARTNER` | `PMID:41210787` (×2), `PMID:37650614`, `PMID:41236292`, `PMID:28287150` (PARTIAL) (5 items) |
| `omcS` | `UniProtKB:Q749X9` | `GSU2504` | — | `GO:0009055` (electron transfer activity), `GO:0020037` (heme binding) | `ELECTRON_DONOR`, `SYNTROPHIC_PARTNER` | `PMID:41210787`, `PMID:37650614`, `PMID:28992596`, `PMID:41236292`, `PMID:31537786` (PARTIAL), `PMID:32849356` (6 items) |
| `omcZ` | `UniProtKB:Q74A90` | `GSU2076` | — | `GO:0009055` (electron transfer activity), `GO:0020037` (heme binding) | `ELECTRON_DONOR`, `SYNTROPHIC_PARTNER` | `PMID:41210787`, `PMID:28992596` (2 items) |
| `omcB` | `UniProtKB:Q74A86` | `GSU2737` | — | `GO:0009055` (electron transfer activity), `GO:0020037` (heme binding) | `ELECTRON_DONOR`, `SYNTROPHIC_PARTNER` | `PMID:41876513`, `PMID:37650614` (2 items) |

---

## 5. Community-to-`CommonTaxon` Linkage Inventory (15 Links Across 14 Communities)

Every `MicrobialCommunity` record in `kb/communities/*.yaml` (485) and `data/isolates/*.yaml` (9) was scanned for *Shewanella oneidensis* (`NCBITaxon:211586` / `NCBITaxon:70863`) and *Geobacter sulfurreducens* (`NCBITaxon:35554` / `NCBITaxon:243231`). All **15** occurrences across **14** community records carry verified `common_taxon` links, with **0** unlinked occurrences:

| Community ID | File | Linked Member (`preferred_term` / `term.id`) | `common_taxon` | Member `functional_role` |
|---|---|---|---|---|
| `CommunityMech:000018` | `kb/communities/Clostridium_Cellulolyticum_Geobacter_Cellulose_MFC_Coculture.yaml` | *Geobacter sulfurreducens* (`NCBITaxon:35554`) | `CommunityMech:taxon:000002` | `SYNTROPHIC_PARTNER` |
| `CommunityMech:000021` | `kb/communities/Corynebacterium_glutamicum_Shewanella_oneidensis_Succinic_Acid_Coculture.yaml` | *Shewanella oneidensis* (`NCBITaxon:70863`) | `CommunityMech:taxon:000001` | `SYNTROPHIC_PARTNER`, `CROSS_FEEDER` |
| `CommunityMech:000031` | `kb/communities/Geobacter_Clostridium_Interspecies_Electron_Transfer_Coculture.yaml` | *Geobacter sulfurreducens* (`NCBITaxon:35554`) | `CommunityMech:taxon:000002` | `SYNTROPHIC_PARTNER` |
| `CommunityMech:000032` | `kb/communities/Geobacter_Pseudomonas_Formate_Fumarate_Electroactive_Coculture.yaml` | *Geobacter sulfurreducens* (`NCBITaxon:35554`) | `CommunityMech:taxon:000002` | `SYNTROPHIC_PARTNER`, `ELECTRON_ACCEPTOR` |
| `CommunityMech:000051` | `kb/communities/ORNL_Clostridium_Desulfovibrio_Geobacter_Trophic_Model.yaml` | *Geobacter sulfurreducens* (`NCBITaxon:35554`) | `CommunityMech:taxon:000002` | `ELECTRON_ACCEPTOR`, `SYNTROPHIC_PARTNER` |
| `CommunityMech:000060` | `kb/communities/Rhodopseudomonas_Geobacter_Magnetite_Redox_Coculture.yaml` | *Geobacter sulfurreducens* PCA (`NCBITaxon:243231`) | `CommunityMech:taxon:000002` | `ELECTRON_DONOR`, `SYNTROPHIC_PARTNER` |
| `CommunityMech:000066` | `kb/communities/Shewanella_Geobacter_Exoelectrogenic_Biofilm_Community.yaml` | *Shewanella oneidensis* MR-1 (`NCBITaxon:211586`) | `CommunityMech:taxon:000001` | `SYNTROPHIC_PARTNER`, `ELECTRON_DONOR`, `BIOFILM_FORMER` |
| `CommunityMech:000066` | `kb/communities/Shewanella_Geobacter_Exoelectrogenic_Biofilm_Community.yaml` | *Geobacter sulfurreducens* (`NCBITaxon:35554`) | `CommunityMech:taxon:000002` | `SYNTROPHIC_PARTNER`, `ELECTRON_DONOR`, `BIOFILM_FORMER` |
| `CommunityMech:000067` | `kb/communities/Shewanella_Streptococcus_Starch_Microbial_Fuel_Cell.yaml` | *Shewanella oneidensis* (`NCBITaxon:70863`) | `CommunityMech:taxon:000001` | `SYNTROPHIC_PARTNER`, `CROSS_FEEDER` |
| `CommunityMech:000211` | `kb/communities/Synechococcus_Shewanella_Dlactate_Biophotovoltaic_Consortium.yaml` | *Shewanella oneidensis* MR-1 (`NCBITaxon:211586`) | `CommunityMech:taxon:000001` | `ELECTROGEN`, `CROSS_FEEDER` |
| `CommunityMech:000214` | `kb/communities/Shewanella_oneidensis_Rhodopseudomonas_palustris_Electrosyntrophic_Coculture.yaml` | *Shewanella oneidensis* MR-1 (`NCBITaxon:211586`) | `CommunityMech:taxon:000001` | `ELECTRON_DONOR`, `SYNTROPHIC_PARTNER` |
| `CommunityMech:000298` | `kb/communities/Electrosynthetic_Consortia_Shewanella_Clostridium_Acetobacterium_Acetate.yaml` | *Shewanella oneidensis* MR-1 (`NCBITaxon:211586`) | `CommunityMech:taxon:000001` | `ELECTRON_DONOR`, `SYNTROPHIC_PARTNER` |
| `CommunityMech:000438` | `kb/communities/SO3_BS3_Lithium_Battery_Bioleaching_Consortium.yaml` | *Shewanella oneidensis* SO3 (MR-1 derivative) (`NCBITaxon:211586`) | `CommunityMech:taxon:000001` | `ELECTRON_DONOR`, `SYNTROPHIC_PARTNER`, `CROSS_FEEDER` |
| `CommunityMech:000462` | `kb/communities/Shewanella_Anammox_Delta_nrfA_Nitrite_Coupled_Consortium.yaml` | *Shewanella oneidensis* MR-1 (delta-nrfA mutant) (`NCBITaxon:211586`) | `CommunityMech:taxon:000001` | `ELECTRON_DONOR`, `SYNTROPHIC_PARTNER`, `CROSS_FEEDER` |
| `CommunityMech:000478` | `kb/communities/Shewanella_Pseudomonas_Fe0_Electrosyntrophic_Denitrifying_Consortium.yaml` | *Shewanella oneidensis* (`NCBITaxon:70863`) | `CommunityMech:taxon:000001` | `ELECTRON_DONOR`, `SYNTROPHIC_PARTNER` |

---

## 6. Audit of Cycle 5 Stage 1 Frontier Records (`CommunityMech:000497`–`000500`) & Corpus Inapplicability / Representation Boundaries

### 6.1 Audit of the 4 New Cycle 5 Stage 1 Records (`CommunityMech:000497`–`000500`)

| Community ID | File | Primary Reference | Protein / Gene Element Audit & Inapplicability Rationale |
|---|---|---|---|
| `CommunityMech:000497` | `kb/communities/Synechocystis_Ecoli_Acetate_Butanol_Coculture.yaml` | `PMID:42726284` (`references_cache/PMID_42726284.md`, OA full text) | Pairs engineered *Synechocystis* sp. PCC 6803 (`WT_PKPa_RBS_BsPta_Δacs`, `NCBITaxon:1148`) with engineered *Escherichia coli* BL21(DE3) (`Pem7_ButOH`, `NCBITaxon:469008`). Neither organism has a reusable `CommonTaxon` record in `kb/taxa/`. Furthermore, `BsPta` is a heterologous phosphotransacetylase from *Bacillus subtilis* combined with a native `Δacs` deletion, and `Pem7_ButOH` is a synthetic multi-gene plasmid construct (`TPC4` 1-butanol pathway + `ackA-pta` overexpression); `PMID:42726284` does not report UniProtKB protein accessions for these synthetic constructs. |
| `CommunityMech:000498` | `kb/communities/Cyantraniliprole_Consortium_T1.yaml` | `PMID:42354927` (`references_cache/PMID_42354927.md`, OA full text) | Six-strain agricultural-drain consortium (*Bacillus licheniformis* B1, *Bacillus subtilis* B3, *Serratia marcescens* S2, *Pseudomonas putida* P1, *Pseudomonas fluorescens* P3, *Pseudomonas stutzeri* P5) identified by MALDI-TOF MS without strain genome assemblies (`GCF_`) or protein sequence accessions. Enzyme abbreviations mentioned in `PMID:42354927` (`TPI`, `AP`, `C1,2O`, `COMT`, `OEX`) are post-assay *in silico* EAWAG-BBD biotransformation pathway predictions rather than strain-resolved proteins. |
| `CommunityMech:000499` | `kb/communities/Cyantraniliprole_Consortium_T2.yaml` | `PMID:42354927` (`references_cache/PMID_42354927.md`, OA full text) | Six-strain agricultural-drain consortium (*B. licheniformis* B2, *B. subtilis* B4, *S. marcescens* S2, *P. putida* P2, *P. fluorescens* P4, *P. stutzeri* P5) identified by MALDI-TOF MS without strain genome assemblies (`GCF_`) or UniProtKB protein accessions; enzyme classes are *in silico* EAWAG-BBD predictions. |
| `CommunityMech:000500` | `kb/communities/Cyantraniliprole_Consortium_T3.yaml` | `PMID:42354927` (`references_cache/PMID_42354927.md`, OA full text) | Six-strain agricultural-drain consortium (*B. licheniformis* B1, *B. subtilis* B3, *S. marcescens* S1, *P. putida* P2, *P. fluorescens* P3, *P. stutzeri* P6) identified by MALDI-TOF MS without strain genome assemblies (`GCF_`) or UniProtKB protein accessions; enzyme classes are *in silico* EAWAG-BBD predictions. |

### 6.2 Corpus-Wide Inapplicability & Representation Boundaries (480 Unlinked `MicrobialCommunity` Records)

Across the remaining **480** `MicrobialCommunity` records (`471` in `kb/communities/*.yaml` and `9` in `data/isolates/*.yaml`):

1. **Representation Boundary (`MicrobialCommunity` vs `CommonTaxon`):**
   - `MicrobialCommunity` records have no schema slot for inline `GeneAnnotation` entries on `TaxonomicComposition` or `EcologicalInteraction`; protein annotations live exclusively on `CommonTaxon` records in `kb/taxa/*.yaml` and require a reference genome assembly (`GCF_`), a verified strain-specific `UniProtKB:` accession, a reference locus tag, and cached verbatim literature evidence.
2. **Taxonomic / Strain Scope Boundary:**
   - Records containing genus-level *Geobacter* sp. (e.g. `CommunityMech:000241` `Rifle_Aquifer_Bioanode_EET_Community.yaml`, where the dominant organism is an uncultured metagenomic bin `S0_RifleGW_Geobacter_53_40` at genus rank `NCBITaxon:28231`, or `CommunityMech:000180` *Geobacter metallireducens* `NCBITaxon:28232`) or genus-level *Shewanella* sp. (`CommunityMech:000465` *Shewanella putrefaciens* CN32 `NCBITaxon:24`, `CommunityMech:000468` *Shewanella* sp. strain HN-41 `NCBITaxon:22`) are intentionally not linked to `CommunityMech:taxon:000001` (*S. oneidensis* MR-1, `GCF_000146165.2`) or `CommunityMech:taxon:000002` (*G. sulfurreducens* PCA, `GCF_000007985.2`) to preserve exact organism, strain, and sequence scope. Note that where `PMID:32849356` (`CommunityMech:000241`) explicitly uses *S. oneidensis* MR-1 (`MtrB`/`SO_1776`, `MtrA`/`SO_1777`) and *G. sulfurreducens* PCA (`OmcS`/`WP_119334099.1`/`GSU2504`) as reference sequences for comparative bioinformatic analysis, those `COMPUTATIONAL` `EvidenceItem`s are recorded directly on `CommunityMech:taxon:000001` and `CommunityMech:taxon:000002`.
3. **16S / Metagenomic / Amplicon & Phenotypic Cohorts:**
   - The remaining community and isolate records describe 16S rRNA amplicon cohorts, genome-resolved metagenomic bins without strain-matched Swiss-Prot/TrEMBL reference assemblies, or metabolite/phenotypic co-cultures where cached primary sources do not provide verbatim gene/protein mechanism claims grounded to a reusable `CommonTaxon` record.
