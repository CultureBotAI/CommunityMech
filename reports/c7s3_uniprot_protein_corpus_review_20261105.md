# Cycle 7 Stage 3: UniProt Protein Examples Corpus Review (`2026-11-05`)

## 1. Executive Summary

This report documents the Cycle 7 Stage 3 (`protein_examples`) corpus-wide review of all `505` records in the CommunityMech knowledge base (`494` community records in `kb/communities/`, `9` isolate/co-culture baseline records in `data/isolates/`, and `2` reusable taxon records in `kb/taxa/`), prioritizing gene and protein elements of mechanism graphs (`ecological_interactions` and `downstream` causal chains) while preserving exact organism (`NCBITaxon`), assembly (`genomes`), sequence (`UniProtKB:` + `locus_tag`), and claim scope.

In Cycle 7 Stage 3:
- **Audited all `505` records**, including the `5` newly added Cycle 7 Stage 1 community records (`CommunityMech:000505`–`CommunityMech:000509` in `kb/communities/Hexamine_Formaldehyde_Consortium_C1.yaml` through `C5.yaml`, `PMID:41743136`) and all `2` reusable `CommonTaxon` records in `kb/taxa/`.
- **Curated `4` new verbatim cached `EvidenceItem` entries** across the `2` reusable `CommonTaxon` records (`kb/taxa/Shewanella_oneidensis_MR1.yaml` and `kb/taxa/Geobacter_sulfurreducens.yaml`), increasing total curated `GeneAnnotation` evidence items from `39` to `43` (`22 -> 24` in `Shewanella_oneidensis_MR1.yaml`; `17 -> 19` in `Geobacter_sulfurreducens.yaml`):
  1. `kb/taxa/Shewanella_oneidensis_MR1.yaml` (`CommunityMech:taxon:000001`, `NCBITaxon:211586`, `GCF_000146165.2`):
     - Added `PMID:32849356` (`SUPPORT`, `COMPUTATIONAL`, linked from `CommunityMech:000241` `Shewanella_Geobacter_Exoelectrogenic_Biofilm_Community.yaml`) to `mtrA` (`UniProtKB:Q8EG35`, `SO_1777`, `4 -> 5` `EvidenceItem`s).
     - Added `PMID:34986141` (`SUPPORT`, `COMPUTATIONAL`, linked from `CommunityMech:000134` `Electrosynthetic_Consortia_Shewanella_Clostridium_Acetobacterium_Acetate.yaml`) to `cymA` (`UniProtKB:Q8E945`, `SO_4591`, `4 -> 5` `EvidenceItem`s).
  2. `kb/taxa/Geobacter_sulfurreducens.yaml` (`CommunityMech:taxon:000002`, `NCBITaxon:35554`, `GCF_000007985.2`):
     - Added `PMID:32265334` (`PARTIAL`, `IN_VITRO`, linked from `CommunityMech:000032` `Geobacter_Pseudomonas_Formate_Fumarate_Electroactive_Coculture.yaml`) to `pilA` (`UniProtKB:Q74BW5`, `GSU1496`, `5 -> 6` `EvidenceItem`s).
     - Added `PMID:34986141` (`SUPPORT`, `COMPUTATIONAL`, linked from `CommunityMech:000134` `Electrosynthetic_Consortia_Shewanella_Clostridium_Acetobacterium_Acetate.yaml`) to `omcS` (`UniProtKB:Q749X9`, `GSU2504`, `6 -> 7` `EvidenceItem`s).
- **Verified `100%` `common_taxon` linkage completeness** (`15` links across `14` community records; `0` unlinked occurrences of `NCBITaxon:211586`, `NCBITaxon:60480`, `NCBITaxon:35554`, or `NCBITaxon:243231` across all `503` community/isolate records).
- **Documented exact organism/sequence inapplicability** for the `5` newly added Cycle 7 Stage 1 community records (`CommunityMech:000505`–`CommunityMech:000509`) and the corpus-wide structural/source boundaries.

---

## 2. Corpus Accounting & File Checksums

| Record Root | Root Class | File Count | Total `GeneAnnotation` Entries | Total `GeneAnnotation` `EvidenceItem`s |
|---|---|---|---|---|
| `kb/taxa/*.yaml` | `CommonTaxon` | `2` | `9` (`5` in `CommunityMech:taxon:000001` + `4` in `CommunityMech:taxon:000002`) | `43` (`24` + `19`) |
| `kb/communities/*.yaml` | `MicrobialCommunity` | `494` | N/A (linked via `taxonomy[].common_taxon`) | `15` `common_taxon` links across `14` community files |
| `data/isolates/*.yaml` | `MicrobialCommunity` | `9` | N/A (linked via `taxonomy[].common_taxon`) | `0` (`0` occurrences of `CommonTaxon` NCBITaxon IDs) |
| **Total Corpus** | — | **`505`** | **`9`** | **`43`** |

### Modified `CommonTaxon` Record Checksums (`kb/taxa/`)

| File | Record ID | Pre-Edit SHA-256 | Post-Edit SHA-256 | Genes | `EvidenceItem`s (Pre -> Post) | History Sidecar |
|---|---|---|---|---|---|---|
| `kb/taxa/Shewanella_oneidensis_MR1.yaml` | `CommunityMech:taxon:000001` | `2fcc32b1e409beb3b69c850a7ca22ac562a47bc9cf3a028e31eb1d7e85c92671` | `6687d4c9e1e325504bf725ab763aa4c75251c6d9af2c30a07de13f49a387d35f` | `5` (`mtrC`, `mtrB`, `mtrA`, `omcA`, `cymA`) | `22 -> 24` | `history/records/Shewanella_oneidensis_MR1/2026-11-05T122500Z-antigravity-c7s301.yaml` |
| `kb/taxa/Geobacter_sulfurreducens.yaml` | `CommunityMech:taxon:000002` | `e18219ed636fb72eba06642469cdcca904a0c2f21697a1893447f80dab179556` | `5c732b29b72f3e8e00ed37a7436e755b6db320a356f095a1d90c0db330b3acbf` | `4` (`pilA`, `omcS`, `omcZ`, `omcB`) | `17 -> 19` | `history/records/Geobacter_sulfurreducens/2026-11-05T122500Z-antigravity-c7s302.yaml` |

---

## 3. Complete `CommonTaxon` Gene & Protein Annotation Inventory (`kb/taxa/`)

### 3.1 `kb/taxa/Shewanella_oneidensis_MR1.yaml` (`CommunityMech:taxon:000001`)
- **Taxon**: `NCBITaxon:211586` (*Shewanella oneidensis* MR-1), `GTDB:s__Shewanella_oneidensis` (*Shewanella oneidensis*)
- **Reference Genome**: `GCF_000146165.2` (strain `MR-1`, chromosome `NC_004347.2` + megaplasmid `NC_004349.1`)
- **Linked Communities (`9`)**:
  - `CommunityMech:000090` (`Corynebacterium_glutamicum_Shewanella_oneidensis_Succinic_Acid_Coculture.yaml`)
  - `CommunityMech:000134` (`Electrosynthetic_Consortia_Shewanella_Clostridium_Acetobacterium_Acetate.yaml`)
  - `CommunityMech:000237` (`SO3_BS3_Lithium_Battery_Bioleaching_Consortium.yaml`)
  - `CommunityMech:000239` (`Shewanella_Anammox_Delta_nrfA_Nitrite_Coupled_Consortium.yaml`)
  - `CommunityMech:000241` (`Shewanella_Geobacter_Exoelectrogenic_Biofilm_Community.yaml`)
  - `CommunityMech:000242` (`Shewanella_Pseudomonas_Fe0_Electrosyntrophic_Denitrifying_Consortium.yaml`)
  - `CommunityMech:000243` (`Shewanella_Streptococcus_Starch_Microbial_Fuel_Cell.yaml`)
  - `CommunityMech:000244` (`Shewanella_oneidensis_Rhodopseudomonas_palustris_Electrosyntrophic_Coculture.yaml`)
  - `CommunityMech:000282` (`Synechococcus_Shewanella_Dlactate_Biophotovoltaic_Consortium.yaml`)

| Gene Symbol | `gene_id` (`UniProtKB`) | `locus_tag` | `product` | `go_terms` | `supports_roles` | `EvidenceItem` References (`24` total) | Cycle 7 Stage 3 Additions |
|---|---|---|---|---|---|---|---|
| `mtrC` | `UniProtKB:Q8EG33` | `SO_1778` | Outer-membrane decaheme c-type cytochrome (terminal extracellular electron-transfer reductase) | `GO:0009055`, `GO:0020037` | `ELECTRON_DONOR`, `ELECTROGEN`, `SYNTROPHIC_PARTNER` | `PMID:42733304` (×2), `PMID:41236292`, `PMID:39504696`, `PMID:31537786` (`5`) | — |
| `mtrB` | `UniProtKB:Q8EG34` | `SO_1776` | Outer-membrane beta-barrel that embeds the MtrA/MtrC cytochrome module | `GO:0015288` | `ELECTRON_DONOR`, `ELECTROGEN`, `SYNTROPHIC_PARTNER` | `PMID:42733304`, `PMID:41210787`, `PMID:31537786`, `PMID:32849356` (`4`) | — |
| `mtrA` | `UniProtKB:Q8EG35` | `SO_1777` | Periplasmic decaheme c-type cytochrome of the Mtr pathway | `GO:0009055`, `GO:0020037` | `ELECTRON_DONOR`, `ELECTROGEN`, `SYNTROPHIC_PARTNER` | `PMID:42733304`, `PMID:41210787`, `PMID:31537786`, `PMID:32849356` (×2) (`5`) | **`+1` (`PMID:32849356`, `SUPPORT`, `COMPUTATIONAL`)** |
| `omcA` | `UniProtKB:Q8EG32` | `SO_1779` | Outer-membrane decaheme c-type cytochrome (extracellular electron-transfer lipoprotein) | `GO:0009055`, `GO:0020037` | `ELECTRON_DONOR`, `ELECTROGEN`, `SYNTROPHIC_PARTNER` | `PMID:42733304` (×2), `PMID:41236292`, `PMID:39504696`, `PMID:31537786` (`5`) | — |
| `cymA` | `UniProtKB:Q8E945` | `SO_4591` | Inner-membrane tetraheme c-type cytochrome (menaquinol oxidase) feeding the Mtr pathway | `GO:0009055`, `GO:0020037` | `ELECTRON_DONOR`, `ELECTROGEN`, `SYNTROPHIC_PARTNER` | `PMID:42733304`, `PMID:39504696`, `PMID:31537786`, `PMID:34986141` (×2) (`5`) | **`+1` (`PMID:34986141`, `SUPPORT`, `COMPUTATIONAL`)** |

### 3.2 `kb/taxa/Geobacter_sulfurreducens.yaml` (`CommunityMech:taxon:000002`)
- **Taxon**: `NCBITaxon:35554` (*Geobacter sulfurreducens*), `GTDB:s__Geobacter_sulfurreducens` (*Geobacter sulfurreducens*)
- **Reference Genome**: `GCF_000007985.2` (strain `PCA` = `ATCC 51573` = `DSM 12127`, `NCBITaxon:243231`, chromosome `NC_002939.5`)
- **Linked Communities (`6`)**:
  - `CommunityMech:000018` (`Clostridium_Cellulolyticum_Geobacter_Cellulose_MFC_Coculture.yaml`)
  - `CommunityMech:000031` (`Geobacter_Clostridium_Interspecies_Electron_Transfer_Coculture.yaml`)
  - `CommunityMech:000032` (`Geobacter_Pseudomonas_Formate_Fumarate_Electroactive_Coculture.yaml`)
  - `CommunityMech:000190` (`ORNL_Clostridium_Desulfovibrio_Geobacter_Trophic_Model.yaml`)
  - `CommunityMech:000215` (`Rhodopseudomonas_Geobacter_Magnetite_Redox_Coculture.yaml`)
  - `CommunityMech:000241` (`Shewanella_Geobacter_Exoelectrogenic_Biofilm_Community.yaml`)

| Gene Symbol | `gene_id` (`UniProtKB`) | `locus_tag` | `product` | `go_terms` | `supports_roles` | `EvidenceItem` References (`19` total) | Cycle 7 Stage 3 Additions |
|---|---|---|---|---|---|---|---|
| `pilA` | `UniProtKB:Q74BW5` | `GSU1496` | Type IV pilin; structural subunit of conductive (electrically conductive) pili / e-pili | `GO:0009055`, `GO:0009289` | `ELECTRON_DONOR`, `SYNTROPHIC_PARTNER` | `PMID:41210787` (×2), `PMID:37650614`, `PMID:41236292`, `PMID:28287150`, `PMID:32265334` (`6`) | **`+1` (`PMID:32265334`, `PARTIAL`, `IN_VITRO`)** |
| `omcS` | `UniProtKB:Q749X9` | `GSU2504` | Outer-surface hexaheme c-type cytochrome associated with conductive pili | `GO:0009055`, `GO:0020037` | `ELECTRON_DONOR`, `SYNTROPHIC_PARTNER` | `PMID:41210787`, `PMID:37650614`, `PMID:28992596`, `PMID:41236292`, `PMID:31537786`, `PMID:32849356`, `PMID:34986141` (`7`) | **`+1` (`PMID:34986141`, `SUPPORT`, `COMPUTATIONAL`)** |
| `omcZ` | `UniProtKB:Q74A90` | `GSU2076` | Outer-surface octaheme c-type cytochrome | `GO:0009055`, `GO:0020037` | `ELECTRON_DONOR`, `SYNTROPHIC_PARTNER` | `PMID:41210787`, `PMID:28992596`, `PMID:34986141` (`3`) | — |
| `omcB` | `UniProtKB:Q74A86` | `GSU2737` | Outer-membrane dodecaheme c-type cytochrome of the OmbB-OmaB-OmcB porin-cytochrome conduit | `GO:0009055`, `GO:0020037` | `ELECTRON_DONOR`, `SYNTROPHIC_PARTNER` | `PMID:41876513`, `PMID:37650614`, `PMID:37747940` (`3`) | — |

---

## 4. Audit of Newly Added Cycle 7 Stage 1 Records (`CommunityMech:000505`–`CommunityMech:000509`)

In Cycle 7 Stage 1 (`PR #2116`), `5` community records were added from `PMID:41743136` (`doi:10.1038/s41598-026-41167-9`, `references_cache/PMID_41743136.txt`, *Biodegradation of hexamine and formaldehyde by bacterial consortia with mathematical Kinetic modeling*):

| File | Record ID | SHA-256 | Taxa (`NCBITaxon`) & Strain Designations | Stage 3 Protein / Gene Evaluation |
|---|---|---|---|---|
| `kb/communities/Hexamine_Formaldehyde_Consortium_C1.yaml` | `CommunityMech:000505` | `1183b1f4762087ed7d8adf1b9960dc38beda73f5d23a8c378fdf8fd0a23e0a2a` | `NCBITaxon:293` (*Brevundimonas diminuta* `SRCHD03` + `SRCHD04`), `NCBITaxon:94625` (*Brucella pseudintermedia* `SRCHD05` + `SRCHD07`) | **Inapplicable (16S-only wild wastewater isolates; no genome assembly or protein sequence accession)** |
| `kb/communities/Hexamine_Formaldehyde_Consortium_C2.yaml` | `CommunityMech:000506` | `5a2c59369389c982d1a1f2a54d2a278eee49908493a78e5c54d85af2d575979d` | `NCBITaxon:293` (*Brevundimonas diminuta* `SRCHD03`), `NCBITaxon:94625` (*Brucella pseudintermedia* `SRCHD05` + `SRCHD07`), `NCBITaxon:2334111` (*Ochrobactrum* sp. `SRCHD06`) | **Inapplicable (16S-only wild wastewater isolates; no genome assembly or protein sequence accession)** |
| `kb/communities/Hexamine_Formaldehyde_Consortium_C3.yaml` | `CommunityMech:000507` | `042454b4b13904fcd05ee42b019346e9940ef68ae6504be8f745266e1d9f2c5f` | `NCBITaxon:293` (*Brevundimonas diminuta* `SRCHD04`), `NCBITaxon:94625` (*Brucella pseudintermedia* `SRCHD05` + `SRCHD07`), `NCBITaxon:2334111` (*Ochrobactrum* sp. `SRCHD06`) | **Inapplicable (16S-only wild wastewater isolates; no genome assembly or protein sequence accession)** |
| `kb/communities/Hexamine_Formaldehyde_Consortium_C4.yaml` | `CommunityMech:000508` | `63a03e2e8960e287c4637edf7562b97d8c90e9ee25d07a3f77fb8843170488bd` | `NCBITaxon:293` (*Brevundimonas diminuta* `SRCHD03` + `SRCHD04`), `NCBITaxon:94625` (*Brucella pseudintermedia* `SRCHD05`), `NCBITaxon:2334111` (*Ochrobactrum* sp. `SRCHD06`) | **Inapplicable (16S-only wild wastewater isolates; no genome assembly or protein sequence accession)** |
| `kb/communities/Hexamine_Formaldehyde_Consortium_C5.yaml` | `CommunityMech:000509` | `c80260476fe0975446f9e2415313873060271d7a38240c64bae507ed7055b99e` | `NCBITaxon:293` (*Brevundimonas diminuta* `SRCHD03` + `SRCHD04`), `NCBITaxon:94625` (*Brucella pseudintermedia* `SRCHD07`), `NCBITaxon:2334111` (*Ochrobactrum* sp. `SRCHD06`) | **Inapplicable (16S-only wild wastewater isolates; no genome assembly or protein sequence accession)** |

**Detailed Scope Verification for `PMID:41743136`**:
1. **Isolate Identification Method**: Strains `SRCHD03`, `SRCHD04`, `SRCHD05`, `SRCHD06`, and `SRCHD07` were isolated from industrial wastewater activated sludge and identified solely by partial 16S rRNA/rDNA sequencing (GenBank 16S accessions `OR262371`, `OR262372`, `OR262373`, `OR262374`, `OR262375`). No whole-genome assembly (`GCF_`/`GCA_`), proteome, or locus-tag annotation exists for any of the 5 isolates.
2. **Enzyme Mentions in `PMID:41743136`**: The Discussion section of `references_cache/PMID_41743136.txt` mentions `"formaldehyde dehydrogenase"` and `"glutamate dehydrogenase"`, but strictly when summarizing prior literature on *Bacillus subtilis* (citing Ref. 52) and *Enterobacter* sp. (citing Ref. 49), not experimental assays or sequenced genes of `SRCHD03`–`SRCHD07`. Under the `add-uniprot-protein-examples` organism- and sequence-scope rules, mapping a reference-strain UniProtKB accession onto unsequenced 16S wastewater isolates or from heterologous literature comparisons is prohibited.

---

## 5. Corpus-Wide Inapplicability & Representation / Resolution Boundaries

Across the `503` `MicrobialCommunity` records (`494` in `kb/communities/` + `9` in `data/isolates/`), the native CommunityMech schema (`src/communitymech/schema/communitymech.yaml`) places `GeneAnnotation` (`gene_symbol`, `gene_id`, `product`, `locus_tag`, `genome`, `go_terms`, `supports_roles`, `supports_interactions`, `evidence`) on reusable `CommonTaxon` records in `kb/taxa/`, which are referenced from `TaxonomicComposition.common_taxon` on `MicrobialCommunity` records (`EcologicalInteraction` and `DownstreamLink` carry `biological_processes` (`GO`) and `metabolites` (`CHEBI`), not a direct `UniProtKB:` protein slot).

| Category | Record Count | Explanation & Scope Boundary |
|---|---|---|
| **Communities linked to `kb/taxa/` `CommonTaxon` records with curated `UniProtKB:` protein examples** | `14` communities (`15` `common_taxon` links; `2` `kb/taxa/*.yaml` records) | All `Shewanella oneidensis` (`NCBITaxon:211586` / `NCBITaxon:60480`) and `Geobacter sulfurreducens` (`NCBITaxon:35554` / `NCBITaxon:243231`) community occurrences link to `CommunityMech:taxon:000001` (`5` proteins, `24` `EvidenceItem`s) and `CommunityMech:taxon:000002` (`4` proteins, `19` `EvidenceItem`s). |
| **16S amplicon / metagenomic / guild / genus- or family-level communities (including `CommunityMech:000505`–`000509`)** | `346` (`337` in `kb/communities/` + `9` in `data/isolates/`) | Taxa are resolved at genus/family/order rank, MAG/ASV/OTU level, or 16S-only isolate level without sequenced strain reference genomes (`GCF_`/`GCA_`). Assigning a strain-specific `UniProtKB:` accession would violate exact organism and sequence scope. |
| **Defined species/strain co-cultures where cached evidence describes metabolite flux, kinetics, or pathway-level `GO`/`CHEBI` processes without naming specific genes/proteins** | `124` in `kb/communities/` | Cached abstracts/full texts (`references_cache/`) characterize growth rates, trophic cross-feeding, or bulk metabolite conversion (`CHEBI` + `GO`) without naming specific genes, locus tags, or proteins. |
| **Records whose cached evidence names a gene symbol, mutant genotype, or enzyme family (`nifH`, `mcrA`, `narG`, `adhE`, `cydAB`, `katG`, etc.) without local offline UniProtKB proteome verification** | `19` in `kb/communities/` | Minting a new `kb/taxa/*.yaml` `CommonTaxon` record with `GeneAnnotation.gene_id: UniProtKB:<accession>` and `locus_tag` requires verifying the exact strain genome (`GCF_`), locus tag, and UniProtKB entry without guessing or network calls. No offline UniProtKB lookup table is bundled in the repository outside the verified `Shewanella oneidensis` MR-1 and `Geobacter sulfurreducens` PCA proteomes. |

---

## 6. Validation Summary

All targeted and corpus-wide validation gates passed with `0` errors:
- `linkml-validate --schema src/communitymech/schema/communitymech.yaml --target-class CommonTaxon kb/taxa/Shewanella_oneidensis_MR1.yaml kb/taxa/Geobacter_sulfurreducens.yaml` (`No issues found`)
- `linkml-term-validator validate-data kb/taxa/*.yaml --schema src/communitymech/schema/communitymech.yaml -t CommonTaxon --labels -c oak_config.yaml` (`Validation passed`)
- `linkml-reference-validator validate data kb/taxa/Shewanella_oneidensis_MR1.yaml -s src/communitymech/schema/communitymech.yaml --target-class CommonTaxon --config conf/reference_validator.yaml` and `linkml-reference-validator validate data kb/taxa/Geobacter_sulfurreducens.yaml -s src/communitymech/schema/communitymech.yaml --target-class CommonTaxon --config conf/reference_validator.yaml` (`All references valid!`)
- `python scripts/evidence_snippet_audit.py kb/taxa/Shewanella_oneidensis_MR1.yaml kb/taxa/Geobacter_sulfurreducens.yaml` (`43` snippets checked, `43` valid, `0` invalid)
- `linkml-validate --schema src/communitymech/schema/history.yaml --target-class HistoryRecord history/records/Shewanella_oneidensis_MR1/2026-11-05T122500Z-antigravity-c7s301.yaml history/records/Geobacter_sulfurreducens/2026-11-05T122500Z-antigravity-c7s302.yaml` (`No issues found`)
- `pytest tests/test_taxon_records.py tests/test_stage6_infrastructure.py` (`14 passed`)
- `validate_strict.py`, `audit_writers.py`, `validate_yaml_scalars.py`, `validate_shared_taxon_ids.py`, `validate_prokaryotic_lineage.py`, `validate_gtdb_coherence.py` (`0` errors across all `505` records)
