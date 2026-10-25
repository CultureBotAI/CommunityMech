# Cycle 2 Stage 3 (`protein_examples`) Corpus Review & Curation Report (2026-10-25)

## 1. Scope & Workflow Context
- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle / Stage**: Cycle 2, Stage 3 (`protein_examples` — UniProt Protein Examples & `CommonTaxon` Gene Grounding)
- **Repository**: `CultureBotAI/CommunityMech`
- **Base Commit**: `4c9894083622d50bc213d54dc5cfcec17b07af71` (`main` after Cycle 2 Stage 2 PR `#2066`)
- **Active Skill**: `.claude/skills/add-uniprot-protein-examples/SKILL.md`
- **Eligible Corpus**:
  - `2` reusable taxon records in `kb/taxa/*.yaml` (`CommonTaxon` target class)
  - `477` community records in `kb/communities/*.yaml` (`MicrobialCommunity` target class)
  - `7` isolate records in `data/isolates/*.yaml` (`MicrobialCommunity` target class)
  - **Total Corpus Audited**: `486` YAML records

## 2. Corpus-Wide Census & Disposition Summary

| Cohort | Record Count | Stage 3 Status | Summary |
| --- | ---: | --- | --- |
| `kb/taxa/Geobacter_sulfurreducens.yaml` (`CommunityMech:taxon:000002`) | 1 | `changed` | Upgraded all 4 `CommonTaxon.genes[]` entries (`omcS` `UniProtKB:Q749X9`, `omcZ` `UniProtKB:Q74A90`, `pilA` `UniProtKB:Q74BW5`, `omcB` `UniProtKB:Q74A86`) with verbatim `IN_VITRO` experimental DIET coculture RNA-Seq (`PMID:37650614`) and deletion-mutant coculture (`PMID:28992596`) evidence and `SYNTROPHIC_PARTNER` functional role annotations. |
| `kb/taxa/Shewanella_oneidensis_MR1.yaml` (`CommunityMech:taxon:000001`) | 1 | `checked` | Verified all 5 `CommonTaxon.genes[]` entries (`mtrA` `UniProtKB:Q8EG35`, `mtrB` `UniProtKB:Q8EG34`, `mtrC` `UniProtKB:Q8EG33`, `omcA` `UniProtKB:Q8EG32`, `cymA` `UniProtKB:Q8E945`) against `NCBITaxon:211586` (`GCF_000146165.2`), GO terms, and verbatim `references_cache/` snippets. |
| `kb/communities/Geobacter_Pseudomonas_Formate_Fumarate_Electroactive_Coculture.yaml` (`CommunityMech:000201`) | 1 | `changed` | Added `common_taxon: CommunityMech:taxon:000002` on `taxonomy[0]` (`Geobacter sulfurreducens`, `NCBITaxon:35554`), backed by `PMID:32265334` (`G. sulfurreducens DL-1 (PCA strain, ATCC 51573)`, `GCF_000007985.2`) and `PMID:28992596` (`ΔomcZ` and `ΔomcS` mutant cocultures). |
| Previously linked `CommonTaxon` community records (`7` MR-1 records, including `000177` which also links to `taxon:000002`) | 7 | `checked` | Verified `common_taxon` linkage (`CommunityMech:000177`, `000203`, `000211`, `000279`, `000298`, `000385`, `000402` $\to$ `CommunityMech:taxon:000001`; `000177` $\to$ `CommunityMech:taxon:000002`) and strain/proteome consistency. |
| Unlinked *Shewanella* / *Geobacter* community records | 17 | `evidence-limited` / `not_applicable` | Audited every remaining *Shewanella* (`5`) and *Geobacter* (`12`) record; left unlinked to preserve strict strain/species/proteome scope (different species, genus-only OTUs, or unverified strain in cached sources). |
| Cycle 2 Stage 1 records (`CommunityMech:000484`–`000490`: `4` communities + `3` isolates) | 7 | `not_applicable` | Audited cached full text/abstracts for gene/protein mentions (`cbbL`, `cbbM`, `coxL`, `nifH`, `tpx`, `bcp`, `cydA`, `hdr`, `sdo`, `sqr`, `sor`, `iro`, `omp40`); documented schema boundary (`MicrobialCommunity` and `EcologicalInteraction` have no inline `genes` slot; taxa are not in `kb/taxa/`). |
| Remaining community (`448`) and isolate (`4`) records | 452 | `not_applicable` | Audited for `CommonTaxon` membership and schema protein-slot applicability; none contain `Shewanella` or `Geobacter`. |
| **Total Corpus** | **486** | **2 `changed` / 8 `checked` / 476 `evidence-limited` or `not_applicable`** | **9 verified `UniProtKB` protein entries across 2 `CommonTaxon` records; 8 unique linked community records (`9` total `common_taxon` links).** |

---

## 3. Detailed Record Changes & SHA-256 Provenance

### 3.1 `kb/taxa/Geobacter_sulfurreducens.yaml` (`CommunityMech:taxon:000002`)
- **Input SHA-256**: `f9f26fa06765ab4c6864ab9197fb8636b0578a5d8e5c063195488b434125eb36`
- **Output SHA-256**: `b3e02ec32304b400312e5320a64bbd963b9667c175c019a3cc5bd7bbdb1979a9`
- **Organism & Reference Proteome Scope**: *Geobacter sulfurreducens* PCA (`NCBITaxon:243231` / species `NCBITaxon:35554`, `GCF_000007985.2`, `ATCC:51573`, `DSM:12127`).
- **Curated `CommonTaxon.genes[]` Updates**:
  1. **`omcS` (`UniProtKB:Q749X9`, `GSU2504`, `SO:0000704`)**:
     - Added `SYNTROPHIC_PARTNER` alongside `ELECTRON_DONOR` in `supports_roles`.
     - Added `IN_VITRO` DIET coculture RNA-Seq evidence from `PMID:37650614` (`references_cache/PMID_37650614.txt`): `"Significant differences occurred in the expression of a variety of key multiheme Geobacter c-type cytochromes during DIET versus FUMARATE, notably, GSU2504 (OmcS) and GSU2887 were significantly upregulated under DIET relative to FUMARATE (LFC > 2.5 and 5.5, respectively), whereas other key multiheme cytochromes, including GSU0618 (OmcE), GSU2737 (OmcB), and GSU2731 (OmcC), had lower expression levels during DIET (Fig. 3)."`
     - Added `IN_VITRO` deletion-mutant coculture evidence from `PMID:28992596` (`references_cache/PMID_28992596.md`): `"The growth reduction of G. sulfurreducens ΔomcZ and ΔomcS mutant cocultures could indicate that both cytochromes participate in the IET in the coculture via this alternative pathway."`
  2. **`omcZ` (`UniProtKB:Q74A90`, `GSU2076`, `SO:0000704`)**:
     - Added `SYNTROPHIC_PARTNER` alongside `ELECTRON_DONOR` in `supports_roles`.
     - Updated `supports_interaction` to document both anode current production and cytochrome-associated interspecies electron transfer.
     - Added `IN_VITRO` deletion-mutant coculture evidence from `PMID:28992596` (`references_cache/PMID_28992596.md`) explicitly naming `ΔomcZ` and `ΔomcS` mutant cocultures.
  3. **`pilA` (`UniProtKB:Q74BW5`, `GSU1496`, `SO:0000704`)**:
     - Added `SYNTROPHIC_PARTNER` alongside `ELECTRON_DONOR` in `supports_roles`.
     - Added `IN_VITRO` DIET coculture RNA-Seq evidence from `PMID:37650614` (`references_cache/PMID_37650614.txt`): `"Additionally, conductive pili genes (PilA) had high baseline expression across conditions and had slightly higher expression under DIET relative to FUMARATE (GSU1496: LFC = 0.64, padj = 5.42E-5) (Fig. 3)."`
  4. **`omcB` (`UniProtKB:Q74A86`, `GSU2737`, `SO:0000704`)**:
     - Added `SYNTROPHIC_PARTNER` alongside `ELECTRON_DONOR` in `supports_roles`.
     - Upgraded from `COMPUTATIONAL`-only (`PMID:41876513`) to include `IN_VITRO` DIET coculture RNA-Seq evidence from `PMID:37650614` (`references_cache/PMID_37650614.txt`) explicitly reporting `GSU2737 (OmcB)` expression during DIET vs fumarate coculture growth.

### 3.2 `kb/communities/Geobacter_Pseudomonas_Formate_Fumarate_Electroactive_Coculture.yaml` (`CommunityMech:000201`)
- **Input SHA-256**: `23bc65dd7bc600d926ad4f080c7f5af377da12558d2602e08f8c77324bab6fe1`
- **Output SHA-256**: `36c0ea58af1a8cd8d96ccf3bf7d3909176613b4be114cf4f8c7e24d6cea246bd`
- **Curation Change**:
  - Linked `taxonomy[0]` (`Geobacter sulfurreducens`, `NCBITaxon:35554`) to `common_taxon: CommunityMech:taxon:000002`.
  - **Strain & Mechanism Scope Verification**:
    - `taxonomy[0].evidence[0]` (`PMID:32265334`) explicitly states: `"An electroactive bacterium, G. sulfurreducens DL-1 (PCA strain, ATCC 51573) was anaerobically grown on regions of a glass slide..."`, matching the `GCF_000007985.2` / `ATCC:51573` PCA reference proteome in `kb/taxa/Geobacter_sulfurreducens.yaml`.
    - `ecological_interactions[1]` (`Conductive Pili and Cytochrome-Mediated Interspecies Electron Transfer`) directly cites `PMID:28992596` (`G. sulfurreducens ΔomcZ and ΔomcS mutant cocultures`), matching `omcS` (`UniProtKB:Q749X9`) and `omcZ` (`UniProtKB:Q74A90`) in `kb/taxa/Geobacter_sulfurreducens.yaml`.
  - **Provenance & History Artifacts**:
    - Emitted history sidecar `history/records/Geobacter_Pseudomonas_Formate_Fumarate_Electroactive_Coculture/2026-10-25T092000Z-claude-stage3.yaml`.
    - Updated `reports/causal_graph_review/decisions/20261021-stage3-common-taxon-links.yaml` and `reports/causal_graph_review/inventory.tsv` with the post-Stage-3 SHA-256.

---

## 4. Verification of Existing Linked `CommonTaxon` Records (7 Checked Community Records)

| Community ID | File | Linked `CommonTaxon` | Input = Output SHA-256 | Verification Note |
| --- | --- | --- | --- | --- |
| `CommunityMech:000177` | `kb/communities/Shewanella_Geobacter_Exoelectrogenic_Biofilm_Community.yaml` | `CommunityMech:taxon:000001`, `CommunityMech:taxon:000002` | `dc6f365d6db2c42544bf4a99266535d87da7c68216deb081fe0d8c8eaa86b68e` | *S. oneidensis* MR-1 (`NCBITaxon:211586`) and *G. sulfurreducens* PCA (`NCBITaxon:35554`) verified against `PMID:28505929`. |
| `CommunityMech:000203` | `kb/communities/Shewanella_Streptococcus_Starch_Microbial_Fuel_Cell.yaml` | `CommunityMech:taxon:000001` | `f13a67f791f7da3e05d9c44634eb88f39b4656ccf0240d6a0c2cf37f55ef4a0a` | *S. oneidensis* MR-1 (`NCBITaxon:211586`) verified against `PMID:28466423`. |
| `CommunityMech:000211` | `kb/communities/Synechococcus_Shewanella_Dlactate_Biophotovoltaic_Consortium.yaml` | `CommunityMech:taxon:000001` | `5900d0ac6541c1dd5c1a676acc0021ac07dd1dab41971377019a024c03d1f281` | *S. oneidensis* MR-1 (`NCBITaxon:211586`, `ATCC 700550`) verified against `PMID:31583088`. |
| `CommunityMech:000279` | `kb/communities/Shewanella_oneidensis_Rhodopseudomonas_palustris_Electrosyntrophic_Coculture.yaml` | `CommunityMech:taxon:000001` | `ce91d403ce97a292953dca9c2259b0e7e9cc8d0effbf104c03a0a26d5151087b` | *S. oneidensis* MR-1 (`NCBITaxon:211586`, `ΔmtrC ΔomcA`) verified against `PMID:35147800`. |
| `CommunityMech:000298` | `kb/communities/Electrosynthetic_Consortia_Shewanella_Clostridium_Acetobacterium_Acetate.yaml` | `CommunityMech:taxon:000001` | `52be42c07f33ad2b481d2ccadefd827d842568e463b5d1cb7d8c3ef905517dff` | *S. oneidensis* MR-1 (`NCBITaxon:211586`) verified against `PMID:34636895`. |
| `CommunityMech:000385` | `kb/communities/SO3_BS3_Lithium_Battery_Bioleaching_Consortium.yaml` | `CommunityMech:taxon:000001` | `b70b100dcdc43b4caf560b3794f0165db3b7c99410a7ba8d5b811825ebdceef4` | *S. oneidensis* MR-1 (`NCBITaxon:211586`) verified against `PMID:37805110`. |
| `CommunityMech:000402` | `kb/communities/Shewanella_Anammox_Delta_nrfA_Nitrite_Coupled_Consortium.yaml` | `CommunityMech:taxon:000001` | `f300a08a92756ce174019800b7a50cec74b8d9a6be17a56accd8e2daa8aa6cf3` | *S. oneidensis* MR-1 (`NCBITaxon:211586`, `ΔnrfA`) verified against `PMID:39471819`. |

---

## 5. Audit of Unlinked *Shewanella* and *Geobacter* Community Records (17 Records)

To preserve strict organism, strain, and reference-proteome scope, the remaining 17 *Shewanella* and *Geobacter* community records were audited and intentionally kept unlinked from `CommunityMech:taxon:000001` (*S. oneidensis* MR-1) and `CommunityMech:taxon:000002` (*G. sulfurreducens* PCA/KN400):

1. **`CommunityMech:000017` (`Chromium_Sulfur_Reduction_Enrichment.yaml`)** — Genus-level `Geobacter` (`NCBITaxon:28231`) 16S enrichment without strain-level PCA/KN400 proteomic identity (`not_applicable`).
2. **`CommunityMech:000031` (`Geobacter_Clostridium_Interspecies_Electron_Transfer_Coculture.yaml`)** — `Geobacter sulfurreducens` (`NCBITaxon:35554`), but the cached source does not verify strain PCA/KN400 or assay specific outer-membrane cytochromes/e-pili (`evidence-limited`).
3. **`CommunityMech:000032` (`Geobacter_Methanosaeta_DIET.yaml`)** — Uses *Geobacter metallireducens* (`NCBITaxon:28232`), a distinct species from *G. sulfurreducens* (`not_applicable`).
4. **`CommunityMech:000033` (`Geobacter_Methanosarcina_DIET.yaml`)** — Uses *Geobacter metallireducens* (`NCBITaxon:28232`), a distinct species from *G. sulfurreducens* (`not_applicable`).
5. **`CommunityMech:000055` (`Polaromonas_Vanadium_Reduction_Community.yaml`)** — Uses *Geobacter metallireducens* (`NCBITaxon:28232`), a distinct species from *G. sulfurreducens* (`not_applicable`).
6. **`CommunityMech:000060` (`Rifle_Uranium_Reducing_Community.yaml`)** — Uses *Geobacter metallireducens* (`NCBITaxon:28232`), a distinct species from *G. sulfurreducens* (`not_applicable`).
7. **`CommunityMech:000113` (`Phylogenetically_Diverse_Denitrifying_SynCom.yaml`)** — Genus-level `Shewanella` (`NCBITaxon:22`) SynCom member (`not_applicable`).
8. **`CommunityMech:000114` (`Shewanella_Denitrifying_Richness_SynComs.yaml`)** — Multi-species genus-level `Shewanella` (`NCBITaxon:22`) denitrifying SynCom (`not_applicable`).
9. **`CommunityMech:000136` (`Oak_Ridge_FRC_Uranium_Nitrate_Groundwater_Community.yaml`)** — Genus-level `Shewanella` (`NCBITaxon:22`) groundwater guild (`not_applicable`).
10. **`CommunityMech:000175` (`Clostridium_Cellulolyticum_Geobacter_Cellulose_MFC_Coculture.yaml`)** — `Geobacter sulfurreducens` (`NCBITaxon:35554`), but the cached source (`PMID:22706069`) does not verify strain PCA/KN400 or assay specific outer-membrane cytochrome/pilin loci (`evidence-limited`).
11. **`CommunityMech:000176` (`ORNL_Clostridium_Desulfovibrio_Geobacter_Trophic_Model.yaml`)** — Synthetic trophic model where *G. sulfurreducens* (`NCBITaxon:35554`) is modeled for metabolic stoichiometry (`PMID:22923819`) without strain-level PCA/KN400 gene/protein attribution (`evidence-limited`).
12. **`CommunityMech:000241` (`Rifle_Aquifer_Bioanode_EET_Community.yaml`)** — Field bioanode enrichment containing genus-level `Geobacter` (`NCBITaxon:28231`) (`not_applicable`).
13. **`CommunityMech:000268` (`Rhodopseudomonas_Geobacter_Magnetite_Redox_Coculture.yaml`)** — `Geobacter sulfurreducens` (`NCBITaxon:35554`), where the cached source (`PMID:26243195`) examines Fe(II)/Fe(III) magnetite redox cycling without strain PCA/KN400 verification or cytochrome/pilin mutant attribution (`evidence-limited`).
14. **`CommunityMech:000288` (`Shewanella_Pseudomonas_Fe0_Electrosyntrophic_Denitrifying_Consortium.yaml`)** — `Shewanella oneidensis` (`NCBITaxon:70863`), where the cached source (`PMID:35114575`) does not explicitly identify strain MR-1 or `SO_` locus tags (`evidence-limited`).
15. **`CommunityMech:000294` (`Corynebacterium_glutamicum_Shewanella_oneidensis_Succinic_Acid_Coculture.yaml`)** — `Shewanella oneidensis` (`NCBITaxon:70863`), where the cached source (`PMID:38340774`) does not explicitly identify strain MR-1 or `SO_` locus tags (`evidence-limited`).
16. **`CommunityMech:000327` (`Methane_MFC_Electrogenesis_Nitrogen_Fixation_Consortium.yaml`)** — Genus-level `Geobacter` (`NCBITaxon:28231`) MFC guild (`not_applicable`).
17. **`CommunityMech:000328` (`Waste_Sludge_Electrofermentation_Biofilm_Suspension_Community.yaml`)** — Genus-level `Geobacter` (`NCBITaxon:28231`) electrofermentation guild (`not_applicable`).

---

## 6. Audit of Cycle 2 Stage 1 Additions (`CommunityMech:000484`–`000490`)

All seven records added in Cycle 2 Stage 1 were inspected against their cached primary sources in `references_cache/` for gene/protein mentions and `CommonTaxon` applicability:

1. **`CommunityMech:000484` (`kb/communities/Aquifer_Sediment_Cable_Bacteria_Sulfur_Community.yaml`)** —SHA-256 `a668d7cf503ca7fc3a521f8fc507b9eb2953096fc3ba0fb1614661a243343b98` (`not_applicable`): Field sediment 16S/dPCR study (`PMID:27058505`, `dsrA` qPCR marker only); family/genus-level taxa (*Desulfobulbaceae*, *Thiobacillus*, *Ignavibacteria*); no strain-level reference proteome or `CommonTaxon` record.
2. **`CommunityMech:000485` (`kb/communities/Dexing_Copper_Bioleaching_Heap_Community.yaml`)** — SHA-256 `ca5ba37ce5b659344c44e4a1c3ba229c0c806947c2685729d04a1b54f74ab804` (`not_applicable`): Metagenomic GeoChip study (`PMID:26781463`) mentioning functional gene families (`cbbL`, `cbbM`, `coxL`, `nifH`, `tpx`, `bcp`, `cydA`) across environmental heap guilds without strain-resolved UniProtKB accessions; `MicrobialCommunity` / `EcologicalInteraction` has no inline `genes` slot.
3. **`CommunityMech:000486` (`kb/communities/Stare_Ransko_Mine_Tailings_Bioleaching_Consortium.yaml`)** — SHA-256 `4b457ef110d737be5b8d0795ef2faad70142dfda6abcf17b2de5d9f482441e82` (`not_applicable`): Tailings bioleaching study (`doi:10.3390/min14030255`) with no gene or protein sequences reported.
4. **`CommunityMech:000487` (`kb/communities/Moderate_Thermophile_Chalcopyrite_pH_Bioleaching_Consortium.yaml`)** — SHA-256 `78d8bf68a91982e8e82865dcdd1c7906097a265f299474deae2b9fb02216f498` (`not_applicable`): RT-qPCR study (`doi:10.1007/s13213-019-01453-y`) measuring `hdr`, `sdo`, `sqr`, `sor`, `iro`, and `omp40` transcripts in *Sulfobacillus thermosulfidooxidans*, *Acidithiobacillus caldus*, and *Ferroplasma thermophilum*; neither `MicrobialCommunity` nor `EcologicalInteraction` has an inline `genes` slot, and none of these three species is a `CommonTaxon` record in `kb/taxa/`.
5. **`CommunityMech:000488` (`data/isolates/Bacillus_licheniformis_Chromate_Biosorption.yaml`)** — SHA-256 `89b445ab25b21497cb97c0ec2332a1ec3c8011ca49e334ab409866ef8069f730` (`not_applicable`): FTIR/zeta-potential biosorption study (`doi:10.3389/fmicb.2024.1423741`) in *Bacillus licheniformis* Put3; no specific genes or UniProt proteins identified.
6. **`CommunityMech:000489` (`data/isolates/Acidithiobacillus_LED_Metal_Bioleaching.yaml`)** — SHA-256 `bb745e9058d354db2ec72a2395cf18c44eb1bd59a977fd121b606704e9e6d869` (`not_applicable`): Waste-LED bioleaching study (`PMID:30343816`, `PMID:31203122`) in *Acidithiobacillus ferrooxidans*; no specific genes or UniProt proteins assayed.
7. **`CommunityMech:000490` (`data/isolates/Ferrimicrobium_acidiphilum_Iron_Respiration.yaml`)** — SHA-256 `1ec2b4ab521cb95da40eb3791845ba8d255e025a37364023879308ceeb4d1ac8` (`not_applicable`): In situ whole-cell spectrophotometric study (`doi:10.1128/aem.01906-20`) of *Ferrimicrobium acidiphilum* DSM 19497 measuring whole-cell 532/562 nm cytochrome absorbance changes without identifying a specific gene locus or UniProtKB accession.

---

## 7. Representation & Writer Blockers Audit

1. **Schema Scope (`GeneAnnotation` vs `MicrobialCommunity` / `EcologicalInteraction`)**:
   - In `src/communitymech/schema/communitymech.yaml`, `GeneAnnotation` (`gene_id: UniProtKB:...`, `gene_symbol`, `locus_tag`, `product`, `go_terms`, `supports_roles`, `supports_interaction`, `evidence`) is attached exclusively to `CommonTaxon.genes[]` in `kb/taxa/*.yaml` and linked from `MicrobialCommunity.taxonomy[].common_taxon`.
   - Neither `TaxonomicComposition` nor `EcologicalInteraction` defines an inline `genes` or `proteins` slot; mechanism-graph nodes represent biochemical/physiological activities via `biological_processes` (`GO`) and `metabolites` (`CHEBI`), while strain-specific protein effectors live on reusable `CommonTaxon` records.
2. **Guarded Writer Contract**:
   - All community record edits were executed through `communitymech.ControlledCuration` (`record_curation_event` + `write_validated_community`), emitting the corresponding `history/records/` sidecar and passing `scripts/audit_curation_writers.py` and `scripts/validate_history.py`.
3. **Infrastructure Carry-Forward**:
   - Existing open deferred item `#2063` (`communitymech-infra-0004` in `INFRA_TASKS.md`: `scripts/validate_references.py` does not resolve `references_cache/DOI_*.txt` files when checking `doi:` references) remains tracked for Stage 6. No new Stage 3 infrastructure blockers were encountered.
