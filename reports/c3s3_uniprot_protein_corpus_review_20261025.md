# Cycle 3 Stage 3 — UniProt Protein Examples Corpus Review (`2026-10-25`)

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle / Stage**: Cycle 3, Stage 3 (`protein_examples`, `goal-10343`)
- **Skill**: `.claude/skills/add-uniprot-protein-examples/SKILL.md`
- **Schema**: `src/communitymech/schema/communitymech.yaml` (`CommonTaxon`, `GeneAnnotation`, `TaxonomicComposition.common_taxon`, `FunctionalRoleEnum`)
- **Corpus Freeze**:
  - `2` reusable `CommonTaxon` records in `kb/taxa/*.yaml` (`CommunityMech:taxon:000001`, `CommunityMech:taxon:000002`)
  - `480` community records in `kb/communities/*.yaml`
  - `9` isolate records in `data/isolates/*.yaml`
  - **Total records inspected**: `491` (`2` `CommonTaxon` + `489` `MicrobialCommunity`)

---

## 1. Corpus-Wide Accounting Summary

| Target Cohort | Record Count | Status Classification | Summary |
|---|---:|---|---|
| `kb/taxa/Shewanella_oneidensis_MR1.yaml` (`CommunityMech:taxon:000001`) | 1 | **Changed** | Enriched `mtrC` (`UniProtKB:Q8EG33`, `SO_1778`) and `omcA` (`UniProtKB:Q8EG32`, `SO_1779`) with verbatim `IN_VITRO` cyclic voltammetry coculture evidence from `PMID:41236292` (`CommunityMech:000298`); enriched `mtrC` (`UniProtKB:Q8EG33`), `omcA` (`UniProtKB:Q8EG32`), and `cymA` (`UniProtKB:Q8E945`, `SO_4591`) with verbatim `IN_VITRO` electro-syntrophic Fe0 denitrification coculture evidence from `PMID:39504696` (`CommunityMech:000288`); enriched `mtrC`, `mtrB` (`UniProtKB:Q8EG34`, `SO_1776`), `mtrA` (`UniProtKB:Q8EG35`, `SO_1777`), `omcA`, and `cymA` with verbatim `IN_VITRO` biophotovoltaic consortium EET pathway evidence from `PMID:31537786` (`CommunityMech:000211`); added `ELECTROGEN` and `SYNTROPHIC_PARTNER` to `supports_roles` across all 5 genes. |
| `kb/taxa/Geobacter_sulfurreducens.yaml` (`CommunityMech:taxon:000002`) | 1 | **Checked (Clean)** | All 4 `genes[]` entries (`pilA` `UniProtKB:Q74BW5` `GSU1496`, `omcS` `UniProtKB:Q749X9` `GSU2504`, `omcZ` `UniProtKB:Q74A90` `GSU2076`, `omcB` `UniProtKB:Q74A86` `GSU2737`) on reference assembly `GCF_000007985.2` carry verified UniProt accessions, GO terms, `ELECTRON_DONOR`/`SYNTROPHIC_PARTNER` roles, and verbatim `IN_VITRO` + `COMPUTATIONAL` evidence (`PMID:41210787`, `PMID:37650614`, `PMID:28992596`, `PMID:41876513`). |
| Linked `kb/communities/*.yaml` (`000031`, `000175`, `000176`, `000177`, `000201`, `000203`, `000211`, `000268`, `000279`, `000288`, `000294`, `000298`, `000385`, `000402`) | 14 | **Checked (Clean)** | Verified all 15 `common_taxon` links across these 14 records (`9` links to `CommunityMech:taxon:000001` across `000177`, `000203`, `000211`, `000279`, `000288`, `000294`, `000298`, `000385`, `000402`; `6` links to `CommunityMech:taxon:000002` across `000031`, `000175`, `000176`, `000177`, `000201`, `000268`). |
| Unlinked *Shewanella* / *Geobacter* `kb/communities/*.yaml` (`000017`, `000032`, `000033`, `000055`, `000060`, `000113`, `000114`, `000136`, `000241`, `000327`, `000328`; plus third member `taxonomy[2]` on `000177`) | 11 | **Excluded (Genus / Species Scope)** | Inspected all 12 unlinked *Shewanella*/*Geobacter* `taxonomy[]` entries across 12 community records (`11` wholly unlinked records + `000177` `taxonomy[2]`); all 12 are genus-level (`NCBITaxon:22` / `NCBITaxon:28231`) or a different species (*Geobacter metallireducens* `NCBITaxon:28232`) and are excluded to preserve exact organism and sequence scope. |
| Remaining `kb/communities/*.yaml` (`455` records, including Cycle 3 Stage 1 records `000491`, `000493`, `000494`) and `data/isolates/*.yaml` (`9` records, including Cycle 3 Stage 1 records `000492`, `000495`) | 464 | **Not Applicable / Representation-Blocked** | Do not contain *Shewanella oneidensis* MR-1 (`CommunityMech:taxon:000001`) or *Geobacter sulfurreducens* PCA (`CommunityMech:taxon:000002`), and `EcologicalInteraction` carries no interaction-level `protein_examples` slot in `src/communitymech/schema/communitymech.yaml`. |

---

## 2. Reusable Taxon Records (`kb/taxa/*.yaml`)

| Taxon ID | File Path | Input SHA-256 | Output SHA-256 | Genome Assembly | Verified UniProtKB Entries | Status |
|---|---|---|---|---|---|---|
| `CommunityMech:taxon:000001` | `kb/taxa/Shewanella_oneidensis_MR1.yaml` | `abc63353af993a7e23f1e676dca15c7012add80ac20cb8827284a32ddbcc95bf` | `8d3910162407ca61bcb5bc1ebbec2c7f1f57e32bea34149d4f873a86bc257061` | `GCF_000146165.2` (`ASM14616v2`, `NCBITaxon:211586`) | `UniProtKB:Q8EG33` (`mtrC`, `SO_1778`), `UniProtKB:Q8EG34` (`mtrB`, `SO_1776`), `UniProtKB:Q8EG35` (`mtrA`, `SO_1777`), `UniProtKB:Q8EG32` (`omcA`, `SO_1779`), `UniProtKB:Q8E945` (`cymA`, `SO_4591`) | **Changed** |
| `CommunityMech:taxon:000002` | `kb/taxa/Geobacter_sulfurreducens.yaml` | `b3e02ec32304b400312e5320a64bbd963b9667c175c019a3cc5bd7bbdb1979a9` | `b3e02ec32304b400312e5320a64bbd963b9667c175c019a3cc5bd7bbdb1979a9` | `GCF_000007985.2` (`ASM798v2`, PCA = `ATCC 51573` = `DSM 12127`) | `UniProtKB:Q74BW5` (`pilA`, `GSU1496`), `UniProtKB:Q749X9` (`omcS`, `GSU2504`), `UniProtKB:Q74A90` (`omcZ`, `GSU2076`), `UniProtKB:Q74A86` (`omcB`, `GSU2737`) | Checked (Unchanged) |

---

## 3. Detailed Record Edits in Cycle 3 Stage 3

### 3.1 `kb/taxa/Shewanella_oneidensis_MR1.yaml` (`CommunityMech:taxon:000001`)
- **Input SHA-256**: `abc63353af993a7e23f1e676dca15c7012add80ac20cb8827284a32ddbcc95bf`
- **Output SHA-256**: `8d3910162407ca61bcb5bc1ebbec2c7f1f57e32bea34149d4f873a86bc257061`
- **Enrichments Applied**:
  1. **`mtrC` (`UniProtKB:Q8EG33`, `locus_tag: SO_1778`, `genome: GCF_000146165.2`)**:
     - Added `ELECTROGEN` and `SYNTROPHIC_PARTNER` alongside `ELECTRON_DONOR` in `supports_roles`.
     - Appended `IN_VITRO` cyclic voltammetry coculture evidence from `PMID:41236292` (`references_cache/PMID_41236292.md`, line 192, linked from `CommunityMech:000298`):
       - Verbatim snippet: `"Cyclic voltammetry (CV) analysis of the co‐culture AS and CS consortia (Figure  2d ) revealed a reversible redox peak at ≈−0.32 and −0.37 V, attributed to the electron conversion of flavin‐bound MtrC/OmcA."`
     - Appended `IN_VITRO` electro-syntrophic Fe0 denitrification coculture evidence from `PMID:39504696` (`references_cache/PMID_39504696.md`, lines 58–61, linked from `CommunityMech:000288`):
       - Verbatim snippet: `"In the electro-syntrophic consortium, the membrane-bound CymA-OmcA-MtrC protein complexes of S. oneidensis drive the generation, transfer and consumption of electrons, thus enabling modulation of microbial metabolic activity."`
     - Appended `IN_VITRO` biophotovoltaic consortium EET pathway evidence from `PMID:31537786` (`references_cache/PMID_31537786.md`, line 89, *S. oneidensis* MR-1 `ATCC 700550`, linked from `CommunityMech:000211`):
       - Verbatim snippet: `"CymA: an inner membrane tetraheme cytochrome c; MtrA: a periplasmic decaheme cytochrome c; MtrB: a non-heme outer membrane porin protein; MtrC/OmcA: two outer membrane decaheme c-type cytochromes; NapA: periplasmic nitrate reductase"`
  2. **`mtrB` (`UniProtKB:Q8EG34`, `locus_tag: SO_1776`, `genome: GCF_000146165.2`)**:
     - Added `ELECTROGEN` and `SYNTROPHIC_PARTNER` alongside `ELECTRON_DONOR` in `supports_roles`.
     - Appended `IN_VITRO` biophotovoltaic consortium EET pathway evidence from `PMID:31537786` (`references_cache/PMID_31537786.md`, line 89):
       - Verbatim snippet: `"CymA: an inner membrane tetraheme cytochrome c; MtrA: a periplasmic decaheme cytochrome c; MtrB: a non-heme outer membrane porin protein; MtrC/OmcA: two outer membrane decaheme c-type cytochromes; NapA: periplasmic nitrate reductase"`
  3. **`mtrA` (`UniProtKB:Q8EG35`, `locus_tag: SO_1777`, `genome: GCF_000146165.2`)**:
     - Added `ELECTROGEN` and `SYNTROPHIC_PARTNER` alongside `ELECTRON_DONOR` in `supports_roles`.
     - Appended `IN_VITRO` biophotovoltaic consortium EET pathway evidence from `PMID:31537786` (`references_cache/PMID_31537786.md`, line 89):
       - Verbatim snippet: `"CymA: an inner membrane tetraheme cytochrome c; MtrA: a periplasmic decaheme cytochrome c; MtrB: a non-heme outer membrane porin protein; MtrC/OmcA: two outer membrane decaheme c-type cytochromes; NapA: periplasmic nitrate reductase"`
  4. **`omcA` (`UniProtKB:Q8EG32`, `locus_tag: SO_1779`, `genome: GCF_000146165.2`)**:
     - Added `ELECTROGEN` and `SYNTROPHIC_PARTNER` alongside `ELECTRON_DONOR` in `supports_roles`.
     - Appended `IN_VITRO` cyclic voltammetry coculture evidence from `PMID:41236292` (`references_cache/PMID_41236292.md`, line 192), `IN_VITRO` electro-syntrophic Fe0 denitrification coculture evidence from `PMID:39504696` (`references_cache/PMID_39504696.md`, lines 58–61), and `IN_VITRO` biophotovoltaic consortium EET pathway evidence from `PMID:31537786` (`references_cache/PMID_31537786.md`, line 89).
  5. **`cymA` (`UniProtKB:Q8E945`, `locus_tag: SO_4591`, `genome: GCF_000146165.2`)**:
     - Added `ELECTROGEN` and `SYNTROPHIC_PARTNER` alongside `ELECTRON_DONOR` in `supports_roles`.
     - Upgraded `cymA` from single-paper evidence (`PMID:42733304`) by appending `IN_VITRO` electro-syntrophic Fe0 denitrification coculture evidence from `PMID:39504696` (`references_cache/PMID_39504696.md`, lines 58–61) and `IN_VITRO` biophotovoltaic consortium EET pathway evidence from `PMID:31537786` (`references_cache/PMID_31537786.md`, line 89).

---

## 4. Complete Inventory of `common_taxon` Links Across the Corpus (`15` Links in `14` Community Records)

| Community ID | File Path | Output SHA-256 | Slot | Taxon Preferred Term (`NCBITaxon`) | Linked `common_taxon` | Supporting References in Slot | Stage 3 Status |
|---|---|---|---|---|---|---|---|
| `CommunityMech:000031` | `kb/communities/Geobacter_Clostridium_Interspecies_Electron_Transfer_Coculture.yaml` | `c4d14762f14174fa4f51e7921d8c2c2105f141e12ca78451f39ade949ceabcd7` | `taxonomy[0]` | `Geobacter sulfurreducens` (`NCBITaxon:35554`) | `CommunityMech:taxon:000002` | `PMID:28287150` | Checked (Pre-existing) |
| `CommunityMech:000175` | `kb/communities/Clostridium_Cellulolyticum_Geobacter_Cellulose_MFC_Coculture.yaml` | `20a878c274695f48d5ad4fd8fe4475e576d4210926f3a9cb901ff85001bf3eff` | `taxonomy[1]` | `Geobacter sulfurreducens` (`NCBITaxon:35554`) | `CommunityMech:taxon:000002` | `PMID:17695929`, `PMID:18725730` | Checked (Pre-existing) |
| `CommunityMech:000176` | `kb/communities/ORNL_Clostridium_Desulfovibrio_Geobacter_Trophic_Model.yaml` | `fdd3d6c6e4fccd5b1416af814ec60609f0353ddc01d5d3e6ec88b4b83da94edc` | `taxonomy[2]` | `Geobacter sulfurreducens` (`NCBITaxon:35554`) | `CommunityMech:taxon:000002` | `doi:10.1186/1471-2180-10-149` | Checked (Pre-existing) |
| `CommunityMech:000177` | `kb/communities/Shewanella_Geobacter_Exoelectrogenic_Biofilm_Community.yaml` | `dc6f365d6db2c42544bf4a99266535d87da7c68216deb081fe0d8c8eaa86b68e` | `taxonomy[0]` | `Shewanella oneidensis` (`NCBITaxon:70863`) | `CommunityMech:taxon:000001` | `PMID:28087529` | Checked (Pre-existing) |
| `CommunityMech:000177` | `kb/communities/Shewanella_Geobacter_Exoelectrogenic_Biofilm_Community.yaml` | `dc6f365d6db2c42544bf4a99266535d87da7c68216deb081fe0d8c8eaa86b68e` | `taxonomy[1]` | `Geobacter sulfurreducens` (`NCBITaxon:35554`) | `CommunityMech:taxon:000002` | `PMID:28087529` | Checked (Pre-existing) |
| `CommunityMech:000201` | `kb/communities/Geobacter_Pseudomonas_Formate_Fumarate_Electroactive_Coculture.yaml` | `36c0ea58af1a8cd8d96ccf3bf7d3909176613b4be114cf4f8c7e24d6cea246bd` | `taxonomy[0]` | `Geobacter sulfurreducens` (`NCBITaxon:35554`) | `CommunityMech:taxon:000002` | `PMID:28992596`, `PMID:32265334` | Checked (Pre-existing) |
| `CommunityMech:000203` | `kb/communities/Shewanella_Streptococcus_Starch_Microbial_Fuel_Cell.yaml` | `f13a67f791f7da3e05d9c44634eb88f39b4656ccf0240d6a0c2cf37f55ef4a0a` | `taxonomy[0]` | `Shewanella oneidensis MR-1` (`NCBITaxon:211586`) | `CommunityMech:taxon:000001` | `PMID:28434977` | Checked (Pre-existing) |
| `CommunityMech:000211` | `kb/communities/Synechococcus_Shewanella_Dlactate_Biophotovoltaic_Consortium.yaml` | `5900d0ac6541c1dd5c1a676acc0021ac07dd1dab41971377019a024c03d1f281` | `taxonomy[1]` | `Shewanella oneidensis MR-1` (`NCBITaxon:211586`) | `CommunityMech:taxon:000001` | `PMID:31537786` | Checked (Pre-existing; `PMID:31537786` evidence added to `taxon:000001`) |
| `CommunityMech:000268` | `kb/communities/Rhodopseudomonas_Geobacter_Magnetite_Redox_Coculture.yaml` | `143da9f7c6ce3d97701a9de829b13b48eead9113266dbf191c51f1e6f11d0912` | `taxonomy[1]` | `Geobacter sulfurreducens` (`NCBITaxon:35554`) | `CommunityMech:taxon:000002` | `PMID:25814583` | Checked (Pre-existing) |
| `CommunityMech:000279` | `kb/communities/Shewanella_oneidensis_Rhodopseudomonas_palustris_Electrosyntrophic_Coculture.yaml` | `ce91d403ce97a292953dca9c2259b0e7e9cc8d0effbf104c03a0a26d5151087b` | `taxonomy[0]` | `Shewanella oneidensis MR-1` (`NCBITaxon:70863`) | `CommunityMech:taxon:000001` | `PMID:42285537` | Checked (Pre-existing) |
| `CommunityMech:000288` | `kb/communities/Shewanella_Pseudomonas_Fe0_Electrosyntrophic_Denitrifying_Consortium.yaml` | `9bdfc9d2f4aa351bf677c6d1b8838738592fe1b7358798860cd13d6bc10472ce` | `taxonomy[0]` | `Shewanella oneidensis` (`NCBITaxon:70863`) | `CommunityMech:taxon:000001` | `PMID:39504696` | Checked (Pre-existing; `PMID:39504696` evidence added to `taxon:000001`) |
| `CommunityMech:000294` | `kb/communities/Corynebacterium_glutamicum_Shewanella_oneidensis_Succinic_Acid_Coculture.yaml` | `12ec7d94161d772e79598564ae50e6f322c9cfd82e889a2fd5e0fbcde687f8f6` | `taxonomy[1]` | `Shewanella oneidensis` (`NCBITaxon:70863`) | `CommunityMech:taxon:000001` | `PMID:42203120` | Checked (Pre-existing) |
| `CommunityMech:000298` | `kb/communities/Electrosynthetic_Consortia_Shewanella_Clostridium_Acetobacterium_Acetate.yaml` | `52be42c07f33ad2b481d2ccadefd827d842568e463b5d1cb7d8c3ef905517dff` | `taxonomy[0]` | `Shewanella oneidensis MR-1` (`NCBITaxon:70863`) | `CommunityMech:taxon:000001` | `PMID:41236292` | Checked (Pre-existing; `PMID:41236292` evidence added to `taxon:000001`) |
| `CommunityMech:000385` | `kb/communities/SO3_BS3_Lithium_Battery_Bioleaching_Consortium.yaml` | `b70b100dcdc43b4caf560b3794f0165db3b7c99410a7ba8d5b811825ebdceef4` | `taxonomy[0]` | `Shewanella oneidensis MR-1 SO3` (`NCBITaxon:70863`) | `CommunityMech:taxon:000001` | `PMID:42733304` | Checked (Pre-existing) |
| `CommunityMech:000402` | `kb/communities/Shewanella_Anammox_Delta_nrfA_Nitrite_Coupled_Consortium.yaml` | `f300a08a92756ce174019800b7a50cec74b8d9a6be17a56accd8e2daa8aa6cf3` | `taxonomy[0]` | `Delta nrfA Shewanella oneidensis MR-1` (`NCBITaxon:211586`) | `CommunityMech:taxon:000001` | `PMID:42655905` | Checked (Pre-existing) |

---

## 5. Complete Inventory of Unlinked *Shewanella* and *Geobacter* `taxonomy[]` Entries (`12` Entries Across `12` Community Records)

Every unlinked `taxonomy[]` entry mentioning *Shewanella* or *Geobacter* across all 489 community/isolate files was inspected against its cached literature to determine whether linking to `CommunityMech:taxon:000001` (*S. oneidensis* MR-1) or `CommunityMech:taxon:000002` (*G. sulfurreducens* PCA) is warranted:

| Community ID | File Path | SHA-256 | Slot & Taxon (`NCBITaxon`) | Cited References | Classification & Exact Rationale for Not Linking |
|---|---|---|---|---|---|
| `CommunityMech:000017` | `kb/communities/Chromium_Sulfur_Reduction_Enrichment.yaml` | `5be48eb0c799123a45f64ec1a3dc2e07d3fcd614110fa95c383edbdcd4ed4a87` | `taxonomy[1]`: `Geobacter` (`NCBITaxon:28231`) | `doi:10.1021/acs.est.8b05053` | **Excluded (Genus-level 16S guild)**: Environmental enrichment resolved only to genus *Geobacter* (`NCBITaxon:28231`); not *G. sulfurreducens* PCA. |
| `CommunityMech:000032` | `kb/communities/Geobacter_Methanosaeta_DIET.yaml` | `8e194a9177b013c6db3e2dd9b4ed9744f06ca0379116f41a0f4ed62cf1d4fde1` | `taxonomy[0]`: `Geobacter metallireducens` (`NCBITaxon:28232`) | `doi:10.1039/C3EE42189A` | **Excluded (Different species)**: Uses *Geobacter metallireducens* (`NCBITaxon:28232`), not *G. sulfurreducens* (`NCBITaxon:35554`). |
| `CommunityMech:000033` | `kb/communities/Geobacter_Methanosarcina_DIET.yaml` | `b6b5f1714e6692936ca408e74dba44df4cbb9518a258c7c7203425998c2979e0` | `taxonomy[0]`: `Geobacter metallireducens` (`NCBITaxon:28232`) | `PMID:24837373` | **Excluded (Different species)**: Uses *Geobacter metallireducens* (`NCBITaxon:28232`), not *G. sulfurreducens* (`NCBITaxon:35554`). |
| `CommunityMech:000055` | `kb/communities/Polaromonas_Vanadium_Reduction_Community.yaml` | `bdb14ed3d33c4a9adc05479849201bf3530bd23d9867a2bc5ddb635b9507a3a5` | `taxonomy[2]`: `Geobacter species` (`NCBITaxon:28232`) | `PMID:33125214`, `PMID:19077236` | **Excluded (Genus/different species)**: Environmental *Geobacter* guild mapped to `NCBITaxon:28232`; not *G. sulfurreducens* PCA. |
| `CommunityMech:000060` | `kb/communities/Rifle_Uranium_Reducing_Community.yaml` | `5232c86c135db06616a847e0d21d7ab88bf15028fc91986af38447c9e7ec5307` | `taxonomy[0]`: `Geobacter species` (`NCBITaxon:28232`) | `PMID:14532040` | **Excluded (Genus/different species)**: Field aquifer *Geobacter* population mapped to `NCBITaxon:28232`; not *G. sulfurreducens* PCA. |
| `CommunityMech:000113` | `kb/communities/Phylogenetically_Diverse_Denitrifying_SynCom.yaml` | `6c83e98d24d68c5be779516c7d8a827629f79a37d7b91597db85ca7e727a8bd6` | `taxonomy[0]`: `Shewanella sp.` (`NCBITaxon:22`) | `PMID:37207729` | **Excluded (Genus-level isolate)**: Denitrifying soil isolate `Shewanella sp.` (`NCBITaxon:22`), not *S. oneidensis* MR-1. |
| `CommunityMech:000114` | `kb/communities/Shewanella_Denitrifying_Richness_SynComs.yaml` | `05411e4ca408a2b94816dd54d7fddacd79d31a3b8a979cf896781440f350054a` | `taxonomy[0]`: `Shewanella denitrifiers` (`NCBITaxon:22`) | `PMID:37154752` | **Excluded (Multi-species guild)**: Genus-level `Shewanella denitrifiers` (`NCBITaxon:22`) richness assemblage; not *S. oneidensis* MR-1 alone. |
| `CommunityMech:000136` | `kb/communities/Oak_Ridge_FRC_Uranium_Nitrate_Groundwater_Community.yaml` | `fd8891c4ada299a06c57062e47f8598fc7f5a1755fc2e1241255c44cff6211d4` | `taxonomy[2]`: `Shewanella spp.` (`NCBITaxon:22`) | `PMID:22988623` | **Excluded (Genus-level guild)**: Groundwater `Shewanella spp.` (`NCBITaxon:22`); not *S. oneidensis* MR-1. |
| `CommunityMech:000177` | `kb/communities/Shewanella_Geobacter_Exoelectrogenic_Biofilm_Community.yaml` | `dc6f365d6db2c42544bf4a99266535d87da7c68216deb081fe0d8c8eaa86b68e` | `taxonomy[2]`: `Geobacter metallireducens` (`NCBITaxon:28232`) | `PMID:28087529` | **Excluded (Different species)**: Third member of `000177` (`taxonomy[0]` and `taxonomy[1]` are already linked to `000001` and `000002`); `taxonomy[2]` is *G. metallireducens* (`NCBITaxon:28232`). |
| `CommunityMech:000241` | `kb/communities/Rifle_Aquifer_Bioanode_EET_Community.yaml` | `9ebd0ac8d6b48fef67e67549627557ceb23347f0de930357ed73b185c666def3` | `taxonomy[0]`: `novel multiheme-cytochrome Geobacter sp.` (`NCBITaxon:28231`) | `PMID:32849356` | **Excluded (Uncultivated MAG)**: Metagenome-assembled *Geobacter* sp. (`NCBITaxon:28231`) from Rifle aquifer; not *G. sulfurreducens* PCA. |
| `CommunityMech:000327` | `kb/communities/Methane_MFC_Electrogenesis_Nitrogen_Fixation_Consortium.yaml` | `11138074c4f29dbcc2edc83f109d31930d2011cab626c35dbab9d04a865252b4` | `taxonomy[1]`: `Geobacter` (`NCBITaxon:28231`) | `PMID:42551599` | **Excluded (Genus-level 16S guild)**: Genus-level *Geobacter* (`NCBITaxon:28231`) in an anaerobic methane MFC; not *G. sulfurreducens* PCA. |
| `CommunityMech:000328` | `kb/communities/Waste_Sludge_Electrofermentation_Biofilm_Suspension_Community.yaml` | `96790620c4f70dd5ca498af0636db53fc9fb7d6779a96851bb31385b71c6f329` | `taxonomy[1]`: `Geobacter` (`NCBITaxon:28231`) | `PMID:41793807` | **Excluded (Genus-level 16S guild)**: Genus-level *Geobacter* (`NCBITaxon:28231`) in a waste-sludge electrofermentation community; not *G. sulfurreducens* PCA. |

---

## 6. Cycle 3 Stage 1 Newly Added Records (`CommunityMech:000491`–`000495`) Checked

All 5 records added in Cycle 3 Stage 1 (`3` communities in `kb/communities/` + `2` isolates in `data/isolates/`) were inspected for reusable `CommonTaxon` linkage and gene/protein elements:

| Record ID | File Path | SHA-256 | Taxa (`NCBITaxon`) | Stage 3 Assessment |
|---|---|---|---|---|
| `CommunityMech:000491` | `kb/communities/TwoStep_PCB_Copper_Gold_Bioleaching_Consortium.yaml` | `1d08be9793a28d66c9dabd74e48ea132d3b8dc44a16e394d7c259fbfca0aa486` | `Acidithiobacillus ferrivorans` (`NCBITaxon:160808`), `Acidithiobacillus thiooxidans` (`NCBITaxon:930`), `Pseudomonas putida` (`NCBITaxon:303`), `Pseudomonas fluorescens` (`NCBITaxon:294`) | **Evidence-Limited / Not Applicable**: Two-step bioleaching consortium (`PMID:26704063`, `references_cache/PMID_26704063.md`); cached source reports Cu/Au bioleaching efficiency and cyanogenesis without strain genome accessions or specific UniProtKB protein assays. |
| `CommunityMech:000492` | `data/isolates/Intrasporangium_Chromatireducens_Q5_1_Chromate_Reduction.yaml` | `3be922d81b044ad742cd52ae866f3007d2f17141fc7355c4a34ad9f96ca304c4` | `Intrasporangium chromatireducens Q5-1` (`NCBITaxon:1386088`) | **Evidence-Limited / Not Applicable**: Species description and NADH-dependent aerobic Cr(VI) reduction kinetic study of strain Q5-1 (`PMID:21441371`, `doi:10.1007/s11274-009-0047-x`, `references_cache/PMID_21441371.md`, `references_cache/doi_10.1007_s11274-009-0047-x.md`); cached sources characterize soluble intracellular chromate reductase activity physiologically without a sequenced genome assembly, locus tags, or UniProtKB identifiers. |
| `CommunityMech:000493` | `kb/communities/Magnetite_Thiobacillus_Sulfur_Cycle_Phenol_Chromate_Reactor.yaml` | `4c9c616655f567840e3c70b680825405cc5871bd144b4c0348c1648a22be6ff6` | `Thiobacillus` (`NCBITaxon:919`) | **Not Applicable (Genus-level reactor guild)**: Magnetite-supplemented bioreactor enrichment resolved to genus *Thiobacillus* (`NCBITaxon:919`, `doi:10.1016/j.cej.2020.124801`, `references_cache/doi_10.1016_j.cej.2020.124801.md`); no strain-resolved genome or UniProtKB protein target. |
| `CommunityMech:000494` | `kb/communities/Tunisian_Sahara_Saline_Spore_Forming_Halophile_Community.yaml` | `c6f381d8af6c86618d0d64bedf8d7e16f2c19aa7286be81579d6d8d9600d210b` | `Halobacillus trueperi` (`NCBITaxon:156205`), `Bacillus` (`NCBITaxon:1386`), `Virgibacillus` (`NCBITaxon:84406`), `Oceanobacillus` (`NCBITaxon:182709`), `Gracilibacillus` (`NCBITaxon:74385`), `Paenibacillus` (`NCBITaxon:44249`), `Pontibacillus` (`NCBITaxon:289201`) | **Not Applicable (Multi-genus culture-collection survey)**: Spore-forming halophile survey across 336 aerobic endospore-forming isolates from five Tunisian Sahara salt-saturated brines and soils typed by 16S–23S ITS-PCR and 16S rRNA sequencing into 14 BOX-PCR genotypes (`PMID:23949950`, `references_cache/PMID_23949950.md`); no sequenced reference genomes or UniProtKB protein identifiers. |
| `CommunityMech:000495` | `data/isolates/Ferroplasma_Acidiphilum_ZJ_AMD_Genomic_Island_Adaptation.yaml` | `cc05785add2613ee69f29971820f913e038de75e44d584a3d8ec22015377c0f1` | `Ferroplasma acidiphilum ZJ` (`NCBITaxon:74969`) | **Evidence-Limited / Not Applicable**: Comparative genomic island study predicting 131 genes across 5 genomic islands in *F. acidiphilum* ZJ, including Cas2 and Cas4 on the 3rd GI (`PMID:40722006`, `PMC12302457`, `references_cache/PMID_40722006.md`); cached source reports gene-family symbols without locus tags or UniProtKB accessions. |

---

## 7. Representation & Writer Blockers Documented

1. **No Interaction-Level `protein_examples` Slot on `EcologicalInteraction`**:
   - In `src/communitymech/schema/communitymech.yaml`, `EcologicalInteraction` has `biological_processes` (`GO` terms) and `metabolites` (`CHEBI` terms), while `GeneAnnotation` (`UniProtKB:...`) lives exclusively on `CommonTaxon.genes[]` in `kb/taxa/*.yaml` and is linked from `TaxonomicComposition.common_taxon`.
   - Community-specific enzymes/transporters mentioned in community descriptions or interaction notes for non-reusable taxa cannot be attached directly to an `EcologicalInteraction` node without minting a dedicated `CommonTaxon` file in `kb/taxa/`. Per `.claude/skills/add-uniprot-protein-examples/SKILL.md` ("The native protein route is `CommonTaxon.genes[]` (`GeneAnnotation`), not a new `protein_examples` field on community interactions... If a community-specific protein example lacks a suitable native owner or relationship, record the representation gap instead of inserting unsupported fields"), no unsupported fields were added.
2. **All 15 `common_taxon` Links Enforced by `scripts/validate_shared_taxon_ids.py`**:
   - All 9 *Shewanella oneidensis* MR-1 links (`CommunityMech:taxon:000001`) and 6 *Geobacter sulfurreducens* PCA links (`CommunityMech:taxon:000002`) across 14 community records pass `scripts/validate_shared_taxon_ids.py` with zero missing or dangling references.
