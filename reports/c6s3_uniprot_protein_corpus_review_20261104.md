# Cycle 6 Stage 3 (`protein_examples`): Corpus-Wide UniProt Protein & Mechanism-Gene Audit Report

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle / Stage**: Cycle `6`, Stage `3` (`protein_examples`)
- **Date**: `2026-11-04`
- **Repository**: `CultureBotAI/CommunityMech`

---

## 1. Executive Summary & Corpus Accounting

During Cycle 6 Stage 3 (`protein_examples`), we audited all **`500`** canonical YAML records in the repository across all three record roots:
- **`2`** reusable taxon/gene records in [`kb/taxa/`](../../kb/taxa/) (`Root class: CommonTaxon`)
- **`489`** community records in [`kb/communities/`](../../kb/communities/) (`Root class: MicrobialCommunity`, including the `4` new communities `CommunityMech:000501`–`000504` added in Cycle 6 Stage 1 and the causal-graph updates from Cycle 6 Stage 2)
- **`9`** isolate/defined-baseline records in [`data/isolates/`](../../data/isolates/) (`Root class: MicrobialCommunity`)

### Summary of Verified Curation Changes in Cycle 6 Stage 3

1. **[`kb/taxa/Shewanella_oneidensis_MR1.yaml`](../../kb/taxa/Shewanella_oneidensis_MR1.yaml) (`CommunityMech:taxon:000001`, `NCBITaxon:211586`, `GCF_000146165.2`)**:
   - **Pre-edit SHA-256**: `df038771231777f9846f246f0c578484c697845043103008586e813badd113f8` (`5` genes, `21` `EvidenceItem`s)
   - **Post-edit SHA-256**: `2fcc32b1e409beb3b69c850a7ca22ac562a47bc9cf3a028e31eb1d7e85c92671` (`5` genes, `22` `EvidenceItem`s)
   - **Curation applied**:
     - Added `1` verified full-text `EvidenceItem` (`PMID:34986141`, `supports: SUPPORT`, `evidence_source: COMPUTATIONAL`) from [`references_cache/PMID_34986141.md`](../../references_cache/PMID_34986141.md) (Chadwick et al. 2022, primary reference for [`kb/communities/ANME_SRB_Marine_Methane_Seep_Consortium.yaml`](../../kb/communities/ANME_SRB_Marine_Methane_Seep_Consortium.yaml), `CommunityMech:000134`) to **`cymA`** (`UniProtKB:Q8E945`, `SO_4591`), explicitly characterizing `CymA in S. oneidensis MR-1` as a 4-heme-binding cytochrome *c* protein with a single-transmembrane helix initiating extracellular electron transfer (`3 -> 4` `EvidenceItem`s on `cymA`).
     - Recorded append-only `CurationEvent` (`2026-11-04T15:30:00Z`, `action: ADD_UNIPROT_PROTEIN_EXAMPLES`, `llm_assisted: true`) and history sidecar [`history/records/Shewanella_oneidensis_MR1/2026-11-04T153000Z-antigravity-c6s301.yaml`](../../history/records/Shewanella_oneidensis_MR1/2026-11-04T153000Z-antigravity-c6s301.yaml).

2. **[`kb/taxa/Geobacter_sulfurreducens.yaml`](../../kb/taxa/Geobacter_sulfurreducens.yaml) (`CommunityMech:taxon:000002`, `NCBITaxon:35554`, `GCF_000007985.2`)**:
   - **Pre-edit SHA-256**: `5d2b49dc2fd42756bdc303302e135ad208c10f76de161e618545a99dd1f6e142` (`4` genes, `15` `EvidenceItem`s)
   - **Post-edit SHA-256**: `e18219ed636fb72eba06642469cdcca904a0c2f21697a1893447f80dab179556` (`4` genes, `17` `EvidenceItem`s)
   - **Curation applied**:
     - Added `1` verified full-text `EvidenceItem` (`PMID:34986141`, `supports: SUPPORT`, `evidence_source: COMPUTATIONAL`) from [`references_cache/PMID_34986141.md`](../../references_cache/PMID_34986141.md) (`CommunityMech:000134`) to **`omcZ`** (`UniProtKB:Q74A90`, `GSU2076`), characterizing the *Geobacter sulfurreducens* 8-heme multiheme cytochrome *c* (`OmcZ`) as required for optimal anodic current in electrode-grown biofilms (`2 -> 3` `EvidenceItem`s on `omcZ`).
     - Added `1` verified full-text `EvidenceItem` (`PMID:37747940`, `supports: SUPPORT`, `evidence_source: COMPUTATIONAL`) from [`references_cache/PMID_37747940.md`](../../references_cache/PMID_37747940.md) (Murali et al. 2023, cited by [`kb/communities/ANME_SRB_Marine_Methane_Seep_Consortium.yaml`](../../kb/communities/ANME_SRB_Marine_Methane_Seep_Consortium.yaml), `CommunityMech:000134`, and [`kb/communities/ANME_SRB_Anaerobic_Methanotrophic_Syntrophic_Consortia.yaml`](../../kb/communities/ANME_SRB_Anaerobic_Methanotrophic_Syntrophic_Consortia.yaml), `CommunityMech:000276`) to **`omcB`** (`UniProtKB:Q74A86`, `GSU2737`), documenting that the alternative `OetI`-type outer-membrane conduit in *G. sulfurreducens* is expressed when a *Geobacter* mutant of `omcB` is grown on Fe(III) oxide (`2 -> 3` `EvidenceItem`s on `omcB`).
     - Recorded append-only `CurationEvent` (`2026-11-04T15:30:00Z`, `action: ADD_UNIPROT_PROTEIN_EXAMPLES`, `llm_assisted: true`) and history sidecar [`history/records/Geobacter_sulfurreducens/2026-11-04T153000Z-antigravity-c6s302.yaml`](../../history/records/Geobacter_sulfurreducens/2026-11-04T153000Z-antigravity-c6s302.yaml).

3. **Regression Test Suite Strengthening**:
   - Updated [`tests/test_taxon_records.py`](../../tests/test_taxon_records.py) (`test_taxa_record_structure`) to assert the newly added `PMID:34986141` and `PMID:37747940` `EvidenceItem` references on `cymA` (`UniProtKB:Q8E945`), `omcZ` (`UniProtKB:Q74A90`), and `omcB` (`UniProtKB:Q74A86`).

---

## 2. Complete Inventory of Reusable `CommonTaxon` Protein Annotations (`kb/taxa/`)

All `9` `GeneAnnotation` entries across both `CommonTaxon` records carry verified `UniProtKB:` accessions (`100%`), canonical locus tags, RefSeq assembly IDs (`GCF_`), GO molecular function/cellular component terms, functional role mappings (`supports_roles`), ecological mechanism descriptions (`supports_interaction`), and `39` total `EvidenceItem` entries (`22` on `Shewanella_oneidensis_MR1.yaml` + `17` on `Geobacter_sulfurreducens.yaml`), each verified verbatim against `references_cache/`.

| Taxon Record | Taxon ID & NCBITaxon | Genome Assembly | Gene Symbol | Locus Tag | Verified `gene_id` | GO Terms | `EvidenceItem` Count & References |
|---|---|---|---|---|---|---|---|
| `kb/taxa/Shewanella_oneidensis_MR1.yaml` | `CommunityMech:taxon:000001` (`NCBITaxon:211586`) | `GCF_000146165.2` (`ASM14616v2`) | `mtrC` | `SO_1778` | `UniProtKB:Q8EG33` | `GO:0009055`, `GO:0020037` | **5** (`PMID:42733304` ×2, `PMID:41236292`, `PMID:39504696`, `PMID:31537786`) |
| `kb/taxa/Shewanella_oneidensis_MR1.yaml` | `CommunityMech:taxon:000001` (`NCBITaxon:211586`) | `GCF_000146165.2` (`ASM14616v2`) | `mtrB` | `SO_1776` | `UniProtKB:Q8EG34` | `GO:0015288` | **4** (`PMID:42733304`, `PMID:41210787`, `PMID:31537786`, `PMID:32849356`) |
| `kb/taxa/Shewanella_oneidensis_MR1.yaml` | `CommunityMech:taxon:000001` (`NCBITaxon:211586`) | `GCF_000146165.2` (`ASM14616v2`) | `mtrA` | `SO_1777` | `UniProtKB:Q8EG35` | `GO:0009055`, `GO:0020037` | **4** (`PMID:42733304`, `PMID:41210787`, `PMID:31537786`, `PMID:32849356`) |
| `kb/taxa/Shewanella_oneidensis_MR1.yaml` | `CommunityMech:taxon:000001` (`NCBITaxon:211586`) | `GCF_000146165.2` (`ASM14616v2`) | `omcA` | `SO_1779` | `UniProtKB:Q8EG32` | `GO:0009055`, `GO:0020037` | **5** (`PMID:42733304` ×2, `PMID:41236292`, `PMID:39504696`, `PMID:31537786`) |
| `kb/taxa/Shewanella_oneidensis_MR1.yaml` | `CommunityMech:taxon:000001` (`NCBITaxon:211586`) | `GCF_000146165.2` (`ASM14616v2`) | `cymA` | `SO_4591` | `UniProtKB:Q8E945` | `GO:0009055`, `GO:0020037` | **4** (`PMID:42733304`, `PMID:39504696`, `PMID:31537786`, **`PMID:34986141` [new]**) |
| `kb/taxa/Geobacter_sulfurreducens.yaml` | `CommunityMech:taxon:000002` (`NCBITaxon:35554`) | `GCF_000007985.2` (`ASM798v2`) | `pilA` | `GSU1496` | `UniProtKB:Q74BW5` | `GO:0009055`, `GO:0009289` | **5** (`PMID:41210787` ×2, `PMID:37650614`, `PMID:41236292`, `PMID:28287150` [PARTIAL]) |
| `kb/taxa/Geobacter_sulfurreducens.yaml` | `CommunityMech:taxon:000002` (`NCBITaxon:35554`) | `GCF_000007985.2` (`ASM798v2`) | `omcS` | `GSU2504` | `UniProtKB:Q749X9` | `GO:0009055`, `GO:0020037` | **6** (`PMID:41210787`, `PMID:37650614`, `PMID:28992596`, `PMID:41236292`, `PMID:31537786` [PARTIAL], `PMID:32849356`) |
| `kb/taxa/Geobacter_sulfurreducens.yaml` | `CommunityMech:taxon:000002` (`NCBITaxon:35554`) | `GCF_000007985.2` (`ASM798v2`) | `omcZ` | `GSU2076` | `UniProtKB:Q74A90` | `GO:0009055`, `GO:0020037` | **3** (`PMID:41210787`, `PMID:28992596`, **`PMID:34986141` [new]**) |
| `kb/taxa/Geobacter_sulfurreducens.yaml` | `CommunityMech:taxon:000002` (`NCBITaxon:35554`) | `GCF_000007985.2` (`ASM798v2`) | `omcB` | `GSU2737` | `UniProtKB:Q74A86` | `GO:0009055`, `GO:0020037` | **3** (`PMID:41876513`, `PMID:37650614`, **`PMID:37747940` [new]**) |

---

## 3. Corpus-Wide `common_taxon` Linkage Verification (`498` Community & Isolate Records)

All **`15`** occurrences of *Shewanella oneidensis* (`NCBITaxon:211586` / `NCBITaxon:60480` where MR-1 or an MR-1 derivative is used) and *Geobacter sulfurreducens* (`NCBITaxon:35554` / `NCBITaxon:243231`) across **`14`** distinct community records are linked via `common_taxon` (`0` unlinked occurrences across all `489` `kb/communities/*.yaml` and `9` `data/isolates/*.yaml` records):

1. `kb/communities/Shewanella_Geobacter_Exoelectrogenic_Biofilm_Community.yaml` (`CommunityMech:000060`) → `CommunityMech:taxon:000001` & `CommunityMech:taxon:000002`
2. `kb/communities/Shewanella_Streptococcus_Starch_Microbial_Fuel_Cell.yaml` (`CommunityMech:000061`) → `CommunityMech:taxon:000001`
3. `kb/communities/Synechococcus_Shewanella_Dlactate_Biophotovoltaic_Consortium.yaml` (`CommunityMech:000211`) → `CommunityMech:taxon:000001`
4. `kb/communities/Shewanella_oneidensis_Rhodopseudomonas_palustris_Electrosyntrophic_Coculture.yaml` (`CommunityMech:000263`) → `CommunityMech:taxon:000001`
5. `kb/communities/Electrosynthetic_Consortia_Shewanella_Clostridium_Acetobacterium_Acetate.yaml` (`CommunityMech:000370`) → `CommunityMech:taxon:000001`
6. `kb/communities/SO3_BS3_Lithium_Battery_Bioleaching_Consortium.yaml` (`CommunityMech:000438`) → `CommunityMech:taxon:000001`
7. `kb/communities/Shewanella_Anammox_Delta_nrfA_Nitrite_Coupled_Consortium.yaml` (`CommunityMech:000488`) → `CommunityMech:taxon:000001`
8. `kb/communities/Shewanella_Pseudomonas_Fe0_Electrosyntrophic_Denitrifying_Consortium.yaml` (`CommunityMech:000493`) → `CommunityMech:taxon:000001`
9. `kb/communities/Corynebacterium_glutamicum_Shewanella_oneidensis_Succinic_Acid_Coculture.yaml` (`CommunityMech:000496`) → `CommunityMech:taxon:000001`
10. `kb/communities/Clostridium_Cellulolyticum_Geobacter_Cellulose_MFC_Coculture.yaml` (`CommunityMech:000014`) → `CommunityMech:taxon:000002`
11. `kb/communities/Geobacter_Clostridium_Interspecies_Electron_Transfer_Coculture.yaml` (`CommunityMech:000031`) → `CommunityMech:taxon:000002`
12. `kb/communities/Geobacter_Pseudomonas_Formate_Fumarate_Electroactive_Coculture.yaml` (`CommunityMech:000032`) → `CommunityMech:taxon:000002`
13. `kb/communities/ORNL_Clostridium_Desulfovibrio_Geobacter_Trophic_Model.yaml` (`CommunityMech:000049`) → `CommunityMech:taxon:000002`
14. `kb/communities/Rhodopseudomonas_Geobacter_Magnetite_Redox_Coculture.yaml` (`CommunityMech:000270`) → `CommunityMech:taxon:000002`

---

## 4. Audit of Newly Added Cycle 6 Stage 1 Records (`CommunityMech:000501`–`000504`)

We inspected all `4` new community records added in Cycle 6 Stage 1 (`PR #2108`) and their cached primary sources:

| Community ID & File | Primary Reference & Cache | Taxa & Strain Accessions in Source | Protein-Example Applicability & Scope Assessment |
|---|---|---|---|
| `CommunityMech:000501` ([`kb/communities/Burkholderia_Bacillus_C2_Masson_Pine_SynCom.yaml`](../../kb/communities/Burkholderia_Bacillus_C2_Masson_Pine_SynCom.yaml)) | `PMID:42144568` ([`references_cache/PMID_42144568.txt`](../../references_cache/PMID_42144568.txt)) | *Burkholderia cepacia* RW1 (`OQ996942`), *Bacillus siamensis* RW5 (`OQ996945`), *Bacillus amyloliquefaciens* RW6 (`OQ996954`), *Bacillus velezensis* RW7 (`OQ996949`), *Bacillus vallismortis* RW8 (`OQ996934`) | **Inapplicable (Source-Limited)**: Bacterial strains are identified only by partial 16S rRNA GenBank accessions (`OQ996934`–`OQ996954`) without strain genome assemblies (`GCF_`) or bacterial protein/locus-tag identifiers. Named genes in the paper (`PR1`, `FLS2`, `CAT1`) are *Pinus massoniana* plant host defense genes, not microbial proteins. |
| `CommunityMech:000502` ([`kb/communities/Bacillus_B81_A1_PAH_Biofilm_Consortium_1.yaml`](../../kb/communities/Bacillus_B81_A1_PAH_Biofilm_Consortium_1.yaml)) | `PMID:42587276` ([`references_cache/PMID_42587276.txt`](../../references_cache/PMID_42587276.txt), OA full text `PMC13471667`) | *Bacillus paramycoides* B8-1 (`PV848451`), *Bacillus paranthracis* A1 (`PV848453`) | **Inapplicable (Source-Limited)**: Soil isolates B8-1 and A1 are characterized by 16S rRNA sequencing (`PV848451`, `PV848453`), crystal-violet biofilm assays, and HPLC PAH-degradation measurements; no strain genome assemblies (`GCF_`), locus tags, or UniProtKB protein accessions are reported. |
| `CommunityMech:000503` ([`kb/communities/Bacillus_B81_A3_Naphthalene_Biofilm_Consortium_2.yaml`](../../kb/communities/Bacillus_B81_A3_Naphthalene_Biofilm_Consortium_2.yaml)) | `PMID:42587276` ([`references_cache/PMID_42587276.txt`](../../references_cache/PMID_42587276.txt), OA full text `PMC13471667`) | *Bacillus paramycoides* B8-1 (`PV848451`), *Bacillus licheniformis* A3 (`PV848454`) | **Inapplicable (Source-Limited)**: Same primary study (`PMID:42587276`); strains B8-1 and A3 carry 16S rRNA accessions (`PV848451`, `PV848454`) without genome assemblies or protein sequence identifiers. |
| `CommunityMech:000504` ([`kb/communities/Bacillus_B81_A1_A3_PAH_Biofilm_Consortium_4.yaml`](../../kb/communities/Bacillus_B81_A1_A3_PAH_Biofilm_Consortium_4.yaml)) | `PMID:42587276` ([`references_cache/PMID_42587276.txt`](../../references_cache/PMID_42587276.txt), OA full text `PMC13471667`) | *Bacillus paramycoides* B8-1 (`PV848451`), *Bacillus paranthracis* A1 (`PV848453`), *Bacillus licheniformis* A3 (`PV848454`) | **Inapplicable (Source-Limited)**: Same primary study (`PMID:42587276`); three-strain consortium evaluated at phenotype/metabolite level without strain genome assemblies or protein sequence identifiers. |

---

## 5. Documented Inapplicability Categories & Representation/Resolution Boundaries Across the Corpus

Following `.claude/skills/add-uniprot-protein-examples/SKILL.md` ("Preserve exact organism, sequence and claim scope; document inapplicability and representation/writer blockers"), the remaining records in the corpus fall into four documented boundary categories:

1. **Offline-UniProt-Resolution Candidates on `Geobacter_sulfurreducens.yaml` (`PMID:32265334`, `CommunityMech:000032`)**:
   - In [`kb/communities/Geobacter_Pseudomonas_Formate_Fumarate_Electroactive_Coculture.yaml`](../../kb/communities/Geobacter_Pseudomonas_Formate_Fumarate_Electroactive_Coculture.yaml) (`CommunityMech:000032`), [`references_cache/PMID_32265334.md`](../../references_cache/PMID_32265334.md) explicitly aligns resequencing reads to the *Geobacter sulfurreducens* PCA reference genome (`GCF_000007985.2`) and identifies adaptive coculture mutations and upregulated proteins by canonical `GSU` locus tags:
     - `GSU0951` (`tetR`, TetR family transcriptional regulator; nonsense mutation `W163Stop`)
     - `GSU0949` (RND family efflux transporter, 30.8-fold higher protein level in adaptively evolved coculture)
     - `GSU1008` (`fabI`, enoyl-[acyl-carrier-protein] reductase, missense variant `G147S`)
     - `GSU0950` (`cyaE`, efflux pump membrane protein, missense variant `L354P`)
   - **Boundary**: The cached text of `PMID:32265334` reports `GSU` locus tags and gene symbols on `GCF_000007985.2` (`NCBITaxon:243231`), but does not print their `UniProtKB:` accessions. Because the local proteome cache (`src/communitymech/uniprot_reference_proteomes.py`) does not contain a pre-downloaded *G. sulfurreducens* PCA (`UP000000577`) locus-to-UniProt lookup table and network calls are disabled in the sandbox, we do not guess `UniProtKB:` accessions from memory.
2. **Engineered / Heterologous Strain Operons Without Reusable `CommonTaxon` Records (`CommunityMech:000211`, `CommunityMech:000488`, `CommunityMech:000496`)**:
   - *Shewanella oneidensis* $\Delta\text{nrfA}$ (`SO_3980` deletion in `CommunityMech:000488`, `PMID:41210787`), engineered *Shewanella oneidensis* `B23` carrying heterologous `ackA-pta` (`CommunityMech:000496`, `PMID:38016552`), and engineered *Synechococcus elongatus* `Syn2973-omcS-ldh` carrying *E. coli* `ldhA` + *G. sulfurreducens* `omcS` + native `glcD1` (`SYNPCC7942_0156` / `M744_04025`, `CommunityMech:000211`, `PMID:31537786`) represent strain-specific genetic modifications or non-native constructs rather than wild-type reusable `CommonTaxon` electron-transfer proteins (note that the heterologous `omcS` usage in `PMID:31537786` is already captured as a `PARTIAL` `EvidenceItem` on `kb/taxa/Geobacter_sulfurreducens.yaml`).
3. **16S / Metagenomic / Phenotype-Only Consortia (`484` Communities + `9` Isolates)**:
   - Communities characterized by 16S rRNA amplicons, unbinned or MAG-level metagenomic functional pathways (KO/EC/COG), or metabolite/growth phenotypes without strain-resolved `GCF_` reference genome assemblies and UniProtKB protein accessions are ineligible for `UniProtKB:` protein grounding under the organism/strain-scope rule.
4. **Schema Representation Note (Already Tracked in `INFRA_TASKS.md`)**:
   - `EcologicalInteraction` in `src/communitymech/schema/communitymech.yaml` links interactions to taxa via `source_taxon`, `target_taxon`, and `participating_taxa` (which link to `CommonTaxon` via `TaxonomicComposition.common_taxon`), rather than carrying a direct `gene_terms` / `mediating_proteins` slot on `EcologicalInteraction`. No new infrastructure tasks were added in Cycle 6 Stage 3 because this representation note is already tracked in `INFRA_TASKS.md`.
