# Cycle 2 Stage 3 — UniProt Protein Examples Corpus Review (`2026-10-25`)

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle / Stage**: Cycle 2, Stage 3 (`protein_examples`, `goal-10343`)
- **Skill**: `.claude/skills/add-uniprot-protein-examples/SKILL.md`
- **Schema**: `src/communitymech/schema/communitymech.yaml` (`CommonTaxon`, `GeneAnnotation`, `TaxonomicComposition.common_taxon`, `FunctionalRoleEnum`)
- **Corpus Freeze**:
  - `2` reusable `CommonTaxon` records in `kb/taxa/*.yaml` (`CommunityMech:taxon:000001`, `CommunityMech:taxon:000002`)
  - `477` community records in `kb/communities/*.yaml`
  - `7` isolate records in `data/isolates/*.yaml`
  - **Total records inspected**: `486` (`2` `CommonTaxon` + `484` `MicrobialCommunity`)

---

## 1. Corpus-Wide Accounting Summary

| Target Cohort | Record Count | Status Classification | Summary |
|---|---:|---|---|
| `kb/taxa/Geobacter_sulfurreducens.yaml` (`CommunityMech:taxon:000002`) | 1 | **Changed** | Enriched `pilA` (`UniProtKB:Q74BW5`, `GSU1496`), `omcS` (`UniProtKB:Q749X9`, `GSU2504`), and `omcB` (`UniProtKB:Q74A86`, `GSU2737`) with verbatim `IN_VITRO` DIET coculture RNA-Seq evidence from `PMID:37650614`; enriched `omcS` (`UniProtKB:Q749X9`) and `omcZ` (`UniProtKB:Q74A90`, `GSU2076`) with verbatim `IN_VITRO` deletion-mutant (`ΔomcZ`, `ΔomcS`) coculture evidence from `PMID:28992596`; added `SYNTROPHIC_PARTNER` to `supports_roles`. |
| `kb/taxa/Shewanella_oneidensis_MR1.yaml` (`CommunityMech:taxon:000001`) | 1 | **Checked (Clean)** | All 5 `genes[]` entries (`mtrC` `UniProtKB:Q8EG33` `SO_1778`, `mtrB` `UniProtKB:Q8EG34` `SO_1776`, `mtrA` `UniProtKB:Q8EG35` `SO_1777`, `omcA` `UniProtKB:Q8EG32` `SO_1779`, `cymA` `UniProtKB:Q8E945` `SO_4591`) on reference assembly `GCF_000146165.2` carry verified UniProt accessions, GO terms, and verbatim `IN_VITRO` evidence (`PMID:42733304`, `PMID:41210787`). |
| `kb/communities/Geobacter_Pseudomonas_Formate_Fumarate_Electroactive_Coculture.yaml` (`CommunityMech:000201`) | 1 | **Changed** | Linked `taxonomy[0]` (`Geobacter sulfurreducens`, `NCBITaxon:35554`) to `common_taxon: CommunityMech:taxon:000002`, backed by strain confirmation (`G. sulfurreducens DL-1 (PCA strain, ATCC 51573)`, `GCF_000007985.2`) in `PMID:32265334` and experimental `ΔomcZ` and `ΔomcS` mutant coculture assays in `PMID:28992596`. |
| Previously linked `kb/communities/*.yaml` (`000177`, `000203`, `000211`, `000279`, `000298`, `000385`, `000402`) | 7 | **Checked (Clean)** | Verified all 8 pre-existing `common_taxon` links across these 7 records (`7` links to `CommunityMech:taxon:000001` across all 7 records, plus `1` link to `CommunityMech:taxon:000002` on `000177` `taxonomy[1]`). With `000201` added, the corpus now has **9 total `common_taxon` links across 8 community records**. |
| Unlinked *Shewanella* / *Geobacter* `kb/communities/*.yaml` (`000017`, `000031`, `000032`, `000033`, `000055`, `000060`, `000113`, `000114`, `000136`, `000175`, `000176`, `000241`, `000268`, `000288`, `000294`, `000327`, `000328`; plus third member `taxonomy[2]` on `000177`) | 17 | **Evidence-Limited / Excluded** | Inspected all 18 unlinked *Shewanella*/*Geobacter* `taxonomy[]` entries across 18 community records (`17` wholly unlinked records + `000177` `taxonomy[2]`); deferred due to genus-level/different-species identity (*G. metallireducens* `NCBITaxon:28232`, genus `NCBITaxon:28231` / `NCBITaxon:22`), lack of strain/assembly/protein assay in cached sources, or contested non-DIET mechanism (`000031`). |
| Remaining `kb/communities/*.yaml` (`452` records) and `data/isolates/*.yaml` (`7` records) | 459 | **Not Applicable / Representation-Blocked** | Do not contain *Shewanella oneidensis* MR-1 (`CommunityMech:taxon:000001`) or *Geobacter sulfurreducens* PCA (`CommunityMech:taxon:000002`), and `EcologicalInteraction` carries no interaction-level `protein_examples` slot in `src/communitymech/schema/communitymech.yaml`. |

---

## 2. Reusable Taxon Records (`kb/taxa/*.yaml`)

| Taxon ID | File Path | Input SHA-256 | Output SHA-256 | Genome Assembly | Verified UniProtKB Entries | Status |
|---|---|---|---|---|---|---|
| `CommunityMech:taxon:000001` | `kb/taxa/Shewanella_oneidensis_MR1.yaml` | `abc63353af993a7e23f1e676dca15c7012add80ac20cb8827284a32ddbcc95bf` | `abc63353af993a7e23f1e676dca15c7012add80ac20cb8827284a32ddbcc95bf` | `GCF_000146165.2` (`ASM14616v2`, `NCBITaxon:211586`) | `UniProtKB:Q8EG33` (`mtrC`, `SO_1778`), `UniProtKB:Q8EG34` (`mtrB`, `SO_1776`), `UniProtKB:Q8EG35` (`mtrA`, `SO_1777`), `UniProtKB:Q8EG32` (`omcA`, `SO_1779`), `UniProtKB:Q8E945` (`cymA`, `SO_4591`) | Checked (Unchanged) |
| `CommunityMech:taxon:000002` | `kb/taxa/Geobacter_sulfurreducens.yaml` | `2a17e614d13876fbb4b2e3bed44c3bd8c339eb8602d53f091cabf6beb5d7e6bd` | `b3e02ec32304b400312e5320a64bbd963b9667c175c019a3cc5bd7bbdb1979a9` | `GCF_000007985.2` (`ASM798v2`, PCA = `ATCC 51573` = `DSM 12127`) | `UniProtKB:Q74BW5` (`pilA`, `GSU1496`), `UniProtKB:Q749X9` (`omcS`, `GSU2504`), `UniProtKB:Q74A90` (`omcZ`, `GSU2076`), `UniProtKB:Q74A86` (`omcB`, `GSU2737`) | **Changed** |

---

## 3. Detailed Record Edits in Cycle 2 Stage 3

### 3.1 `kb/taxa/Geobacter_sulfurreducens.yaml` (`CommunityMech:taxon:000002`)
- **Input SHA-256**: `2a17e614d13876fbb4b2e3bed44c3bd8c339eb8602d53f091cabf6beb5d7e6bd`
- **Output SHA-256**: `b3e02ec32304b400312e5320a64bbd963b9667c175c019a3cc5bd7bbdb1979a9`
- **Enrichments Applied**:
  1. **`pilA` (`UniProtKB:Q74BW5`, `locus_tag: GSU1496`, `genome: GCF_000007985.2`)**:
     - Added `SYNTROPHIC_PARTNER` alongside `ELECTRON_DONOR` in `supports_roles`.
     - Appended `IN_VITRO` experimental RNA-Seq coculture evidence from `PMID:37650614` (`references_cache/PMID_37650614.txt`, line 115, *G. sulfurreducens* PCA `ATCC 51573` aligned to `NC_002939` / `GCF_000007985.2`):
       - Verbatim snippet: `"The gene coding for the pilin monomer, PilA, which is assembled into electrically conductive pili ( 79 ), was also 63 times more highly expressed in DIET-grown cells."`
  2. **`omcS` (`UniProtKB:Q749X9`, `locus_tag: GSU2504`, `genome: GCF_000007985.2`)**:
     - Added `SYNTROPHIC_PARTNER` alongside `ELECTRON_DONOR` in `supports_roles`.
     - Appended `IN_VITRO` experimental RNA-Seq coculture evidence from `PMID:37650614` (`references_cache/PMID_37650614.txt`, line 115):
       - Verbatim snippet: `"These included genes for over 25 c-type cytochromes, including omcS, omcB, omcX, and omcI, which encode multi-heme, outer-surface c-type cytochromes."`
     - Appended `IN_VITRO` experimental deletion-mutant (`ΔomcS`) coculture evidence from `PMID:28992596` (`references_cache/PMID_28992596.md`, lines 61–64):
       - Verbatim snippet: `"The syntrophy was not reliant on phenazine, since Δphz mutant strain cocultures grew, however appeared to rely on cytochromes as evidenced from the stunted growth G. sulfurreducens ΔomcZ and ΔomcS mutant cocultures."`
  3. **`omcZ` (`UniProtKB:Q74A90`, `locus_tag: GSU2076`, `genome: GCF_000007985.2`)**:
     - Added `SYNTROPHIC_PARTNER` alongside `ELECTRON_DONOR` in `supports_roles` and updated `supports_interaction` to reflect syntrophic coculture growth during cytochrome-associated interspecies electron transfer.
     - Appended `IN_VITRO` experimental deletion-mutant (`ΔomcZ`) coculture evidence from `PMID:28992596` (`references_cache/PMID_28992596.md`, lines 61–64):
       - Verbatim snippet: `"The syntrophy was not reliant on phenazine, since Δphz mutant strain cocultures grew, however appeared to rely on cytochromes as evidenced from the stunted growth G. sulfurreducens ΔomcZ and ΔomcS mutant cocultures."`
  4. **`omcB` (`UniProtKB:Q74A86`, `locus_tag: GSU2737`, `genome: GCF_000007985.2`)**:
     - Added `SYNTROPHIC_PARTNER` alongside `ELECTRON_DONOR` in `supports_roles` and updated `supports_interaction` to include DIET coculture electron transfer.
     - Upgraded `omcB` from `COMPUTATIONAL`-only (`PMID:41876513`) by appending direct `IN_VITRO` experimental DIET coculture RNA-Seq evidence from `PMID:37650614` (`references_cache/PMID_37650614.txt`, line 115):
       - Verbatim snippet: `"These included genes for over 25 c-type cytochromes, including omcS, omcB, omcX, and omcI, which encode multi-heme, outer-surface c-type cytochromes."`

### 3.2 `kb/communities/Geobacter_Pseudomonas_Formate_Fumarate_Electroactive_Coculture.yaml` (`CommunityMech:000201`)
- **Input SHA-256**: `23bc65dd7bc600d926ad4f080c7f5af377da12558d2602e08f8c77324bab6fe1`
- **Output SHA-256**: `36c0ea58af1a8cd8d96ccf3bf7d3909176613b4be114cf4f8c7e24d6cea246bd`
- **Enrichment Applied**:
  - Linked `taxonomy[0]` (`Geobacter sulfurreducens`, `NCBITaxon:35554`) to `common_taxon: CommunityMech:taxon:000002`.
  - **Strain & Mechanism Verification**:
    - `taxonomy[0].evidence[0]` cites `PMID:28992596`, and `ecological_interactions[1]` (`Cytochrome-Associated Interspecies Electron Transfer`, lines 157–184) cites `PMID:28992596` with the verbatim snippet `"The syntrophy was not reliant on phenazine, since Δphz mutant strain cocultures grew, however appeared to rely on cytochromes as evidenced from the stunted growth G. sulfurreducens ΔomcZ and ΔomcS mutant cocultures"`, directly assaying `omcZ` (`GSU2076`, `UniProtKB:Q74A90`) and `omcS` (`GSU2504`, `UniProtKB:Q749X9`) deletion mutants in coculture.
    - `taxonomy[0].evidence[1]` cites `PMID:32265334` (`references_cache/PMID_32265334.md`), whose Materials and Methods (line 107) explicitly identifies the strain and reference genome assembly: `"G. sulfurreducens DL-1 (PCA strain, ATCC 51573) was grown under strictly anaerobic conditions in NB supplemented with acetate and fumarate (NBAF) medium..."` and aligns reads to `GCF_000007985.2` (line 141).

---

## 4. Complete Inventory of `common_taxon` Links Across the Corpus (`9` Links in `8` Community Records)

| Community ID | File Path | Output SHA-256 | Slot | Taxon Preferred Term (`NCBITaxon`) | Linked `common_taxon` | Supporting References in Slot | Stage 3 Status |
|---|---|---|---|---|---|---|---|
| `CommunityMech:000177` | `kb/communities/Shewanella_Geobacter_Exoelectrogenic_Biofilm_Community.yaml` | `dc6f365d6db2c42544bf4a99266535d87da7c68216deb081fe0d8c8eaa86b68e` | `taxonomy[0]` | `Shewanella oneidensis` (`NCBITaxon:70863`) | `CommunityMech:taxon:000001` | `PMID:28087529` | Checked (Pre-existing) |
| `CommunityMech:000177` | `kb/communities/Shewanella_Geobacter_Exoelectrogenic_Biofilm_Community.yaml` | `dc6f365d6db2c42544bf4a99266535d87da7c68216deb081fe0d8c8eaa86b68e` | `taxonomy[1]` | `Geobacter sulfurreducens` (`NCBITaxon:35554`) | `CommunityMech:taxon:000002` | `PMID:28087529` | Checked (Pre-existing) |
| `CommunityMech:000201` | `kb/communities/Geobacter_Pseudomonas_Formate_Fumarate_Electroactive_Coculture.yaml` | `36c0ea58af1a8cd8d96ccf3bf7d3909176613b4be114cf4f8c7e24d6cea246bd` | `taxonomy[0]` | `Geobacter sulfurreducens` (`NCBITaxon:35554`) | `CommunityMech:taxon:000002` | `PMID:28992596`, `PMID:32265334` | **Added in C2S3** |
| `CommunityMech:000203` | `kb/communities/Shewanella_Streptococcus_Starch_Microbial_Fuel_Cell.yaml` | `f13a67f791f7da3e05d9c44634eb88f39b4656ccf0240d6a0c2cf37f55ef4a0a` | `taxonomy[0]` | `Shewanella oneidensis MR-1` (`NCBITaxon:211586`) | `CommunityMech:taxon:000001` | `PMID:28434977` | Checked (Pre-existing) |
| `CommunityMech:000211` | `kb/communities/Synechococcus_Shewanella_Dlactate_Biophotovoltaic_Consortium.yaml` | `5900d0ac6541c1dd5c1a676acc0021ac07dd1dab41971377019a024c03d1f281` | `taxonomy[1]` | `Shewanella oneidensis MR-1` (`NCBITaxon:211586`) | `CommunityMech:taxon:000001` | `PMID:31537786` | Checked (Pre-existing) |
| `CommunityMech:000279` | `kb/communities/Shewanella_oneidensis_Rhodopseudomonas_palustris_Electrosyntrophic_Coculture.yaml` | `ce91d403ce97a292953dca9c2259b0e7e9cc8d0effbf104c03a0a26d5151087b` | `taxonomy[0]` | `Shewanella oneidensis MR-1` (`NCBITaxon:70863`) | `CommunityMech:taxon:000001` | `PMID:42285537` | Checked (Pre-existing) |
| `CommunityMech:000298` | `kb/communities/Electrosynthetic_Consortia_Shewanella_Clostridium_Acetobacterium_Acetate.yaml` | `52be42c07f33ad2b481d2ccadefd827d842568e463b5d1cb7d8c3ef905517dff` | `taxonomy[0]` | `Shewanella oneidensis MR-1` (`NCBITaxon:70863`) | `CommunityMech:taxon:000001` | `PMID:41236292` | Checked (Pre-existing) |
| `CommunityMech:000385` | `kb/communities/SO3_BS3_Lithium_Battery_Bioleaching_Consortium.yaml` | `b70b100dcdc43b4caf560b3794f0165db3b7c99410a7ba8d5b811825ebdceef4` | `taxonomy[0]` | `Shewanella oneidensis MR-1 SO3` (`NCBITaxon:70863`) | `CommunityMech:taxon:000001` | `PMID:42733304` | Checked (Pre-existing) |
| `CommunityMech:000402` | `kb/communities/Shewanella_Anammox_Delta_nrfA_Nitrite_Coupled_Consortium.yaml` | `f300a08a92756ce174019800b7a50cec74b8d9a6be17a56accd8e2daa8aa6cf3` | `taxonomy[0]` | `Delta nrfA Shewanella oneidensis MR-1` (`NCBITaxon:211586`) | `CommunityMech:taxon:000001` | `PMID:42655905` | Checked (Pre-existing) |

---

## 5. Complete Inventory of Unlinked *Shewanella* and *Geobacter* `taxonomy[]` Entries (`18` Entries Across `18` Community Records)

Every unlinked `taxonomy[]` entry mentioning *Shewanella* or *Geobacter* across all 484 community/isolate files was inspected against its cached literature to determine whether linking to `CommunityMech:taxon:000001` (*S. oneidensis* MR-1) or `CommunityMech:taxon:000002` (*G. sulfurreducens* PCA) is warranted:

| Community ID | File Path | SHA-256 | Slot & Taxon (`NCBITaxon`) | Cited References | Classification & Exact Rationale for Not Linking |
|---|---|---|---|---|---|
| `CommunityMech:000017` | `kb/communities/Chromium_Sulfur_Reduction_Enrichment.yaml` | `5be48eb0c799123a45f64ec1a3dc2e07d3fcd614110fa95c383edbdcd4ed4a87` | `taxonomy[1]`: `Geobacter` (`NCBITaxon:28231`) | `doi:10.1021/acs.est.8b05053` | **Excluded (Genus-level 16S guild)**: Environmental enrichment resolved only to genus *Geobacter* (`NCBITaxon:28231`); not *G. sulfurreducens* PCA. |
| `CommunityMech:000031` | `kb/communities/Geobacter_Clostridium_Interspecies_Electron_Transfer_Coculture.yaml` | `2bfa8ffd6b7d147f3c471eb88aa26482f93b0cc8d7b23dc39838402715463329` | `taxonomy[0]`: `Geobacter sulfurreducens` (`NCBITaxon:35554`) | `PMID:28287150` | **Excluded (Contested non-DIET mechanism)**: Although `taxonomy[0].taxon_term.notes` names `G. sulfurreducens (strain DSM 12127)` (= PCA), the record explicitly warns `MECHANISM CONTESTED - do not read this record as establishing contact-dependent DIET`: `PMID:28287150` did not demonstrate physical contact, conductive pili (`pilA`), or outer-membrane cytochromes (`omcS`, `omcZ`, `omcB`), and the follow-up (`PMID:34939136`) concluded the interaction is **mediated** via a diffusible cobamide acting on glycerol dehydratase. Per `SKILL.md` ("Confirm... that the source establishes the role/interaction claimed. A gene annotation must not assert a role merely because the family is present"), `000031` is kept unlinked to avoid attributing conductive-pili/cytochrome DIET gene annotations (`CommunityMech:taxon:000002`) to a mediated/contested coculture. |
| `CommunityMech:000032` | `kb/communities/Geobacter_Methanosaeta_DIET.yaml` | `8e194a9177b013c6db3e2dd9b4ed9744f06ca0379116f41a0f4ed62cf1d4fde1` | `taxonomy[0]`: `Geobacter metallireducens` (`NCBITaxon:28232`) | `doi:10.1039/C3EE42189A` | **Excluded (Different species)**: Uses *Geobacter metallireducens* (`NCBITaxon:28232`), not *G. sulfurreducens* (`NCBITaxon:35554`). |
| `CommunityMech:000033` | `kb/communities/Geobacter_Methanosarcina_DIET.yaml` | `b6b5f1714e6692936ca408e74dba44df4cbb9518a258c7c7203425998c2979e0` | `taxonomy[0]`: `Geobacter metallireducens` (`NCBITaxon:28232`) | `PMID:24837373` | **Excluded (Different species)**: Uses *Geobacter metallireducens* (`NCBITaxon:28232`), not *G. sulfurreducens* (`NCBITaxon:35554`). |
| `CommunityMech:000055` | `kb/communities/Polaromonas_Vanadium_Reduction_Community.yaml` | `bdb14ed3d33c4a9adc05479849201bf3530bd23d9867a2bc5ddb635b9507a3a5` | `taxonomy[2]`: `Geobacter species` (`NCBITaxon:28232`) | `PMID:19077236`, `PMID:33125214` | **Excluded (Genus/different species)**: Environmental *Geobacter* guild mapped to `NCBITaxon:28232`; not *G. sulfurreducens* PCA. |
| `CommunityMech:000060` | `kb/communities/Rifle_Uranium_Reducing_Community.yaml` | `5232c86c135db06616a847e0d21d7ab88bf15028fc91986af38447c9e7ec5307` | `taxonomy[0]`: `Geobacter species` (`NCBITaxon:28232`) | `PMID:14532040` | **Excluded (Genus/different species)**: Field aquifer *Geobacter* population mapped to `NCBITaxon:28232`; not *G. sulfurreducens* PCA. |
| `CommunityMech:000113` | `kb/communities/Phylogenetically_Diverse_Denitrifying_SynCom.yaml` | `6c83e98d24d68c5be779516c7d8a827629f79a37d7b91597db85ca7e727a8bd6` | `taxonomy[0]`: `Shewanella sp.` (`NCBITaxon:22`) | `PMID:37207729` | **Excluded (Genus-level isolate)**: Denitrifying soil isolate `Shewanella sp.` (`NCBITaxon:22`), not *S. oneidensis* MR-1. |
| `CommunityMech:000114` | `kb/communities/Shewanella_Denitrifying_Richness_SynComs.yaml` | `05411e4ca408a2b94816dd54d7fddacd79d31a3b8a979cf896781440f350054a` | `taxonomy[0]`: `Shewanella denitrifiers` (`NCBITaxon:22`) | `PMID:37154752` | **Excluded (Multi-species guild)**: Genus-level `Shewanella denitrifiers` (`NCBITaxon:22`) richness assemblage; not *S. oneidensis* MR-1 alone. |
| `CommunityMech:000136` | `kb/communities/Oak_Ridge_FRC_Uranium_Nitrate_Groundwater_Community.yaml` | `fd8891c4ada299a06c57062e47f8598fc7f5a1755fc2e1241255c44cff6211d4` | `taxonomy[2]`: `Shewanella spp.` (`NCBITaxon:22`) | `PMID:22988623` | **Excluded (Genus-level guild)**: Groundwater `Shewanella spp.` (`NCBITaxon:22`); not *S. oneidensis* MR-1. |
| `CommunityMech:000175` | `kb/communities/Clostridium_Cellulolyticum_Geobacter_Cellulose_MFC_Coculture.yaml` | `bafb8c0e58150b2e586e92c84725b0e3ad88001a64c2d1acb1d2889ede2810b3` | `taxonomy[1]`: `Geobacter sulfurreducens` (`NCBITaxon:35554`) | `PMID:17695929`, `PMID:18725730` | **Evidence-Limited**: Cached abstracts (`PMID:17695929`, `PMID:18725730`) report species-level *G. sulfurreducens* in cellulose MFC coculture without specifying strain PCA / `GCF_000007985.2` or assaying PilA/OmcS/OmcZ/OmcB proteins. |
| `CommunityMech:000176` | `kb/communities/ORNL_Clostridium_Desulfovibrio_Geobacter_Trophic_Model.yaml` | `151a414766ded2f1c8b094002819c6e620751b6344ef9753d1f3a988c1cf99dd` | `taxonomy[2]`: `Geobacter sulfurreducens` (`NCBITaxon:35554`) | `doi:10.1186/1471-2180-10-149` | **Evidence-Limited**: Stoichiometric metabolic network model (`doi:10.1186/1471-2180-10-149`); does not experimentally assay extracellular conductive-pili or multiheme-cytochrome proteins. |
| `CommunityMech:000177` | `kb/communities/Shewanella_Geobacter_Exoelectrogenic_Biofilm_Community.yaml` | `dc6f365d6db2c42544bf4a99266535d87da7c68216deb081fe0d8c8eaa86b68e` | `taxonomy[2]`: `Geobacter metallireducens` (`NCBITaxon:28232`) | `PMID:28087529` | **Excluded (Different species)**: Third member of `000177` (`taxonomy[0]` and `taxonomy[1]` are already linked to `000001` and `000002`); `taxonomy[2]` is *G. metallireducens* (`NCBITaxon:28232`). |
| `CommunityMech:000241` | `kb/communities/Rifle_Aquifer_Bioanode_EET_Community.yaml` | `9ebd0ac8d6b48fef67e67549627557ceb23347f0de930357ed73b185c666def3` | `taxonomy[0]`: `novel multiheme-cytochrome Geobacter sp.` (`NCBITaxon:28231`) | `PMID:32849356` | **Excluded (Uncultivated MAG)**: Metagenome-assembled *Geobacter* sp. (`NCBITaxon:28231`) from Rifle aquifer; not *G. sulfurreducens* PCA. |
| `CommunityMech:000268` | `kb/communities/Rhodopseudomonas_Geobacter_Magnetite_Redox_Coculture.yaml` | `21ea769fcc97b50c66ad0fd3ba76cca647ae23fde4a34ce2b7d1aea81bc69378` | `taxonomy[1]`: `Geobacter sulfurreducens` (`NCBITaxon:35554`) | `PMID:25814583` | **Evidence-Limited**: Cached abstract (`PMID:25814583`) describes Fe(II)/Fe(III) magnetite redox cycling without specifying strain PCA or assaying PilA/OmcS/OmcZ/OmcB proteins. |
| `CommunityMech:000288` | `kb/communities/Shewanella_Pseudomonas_Fe0_Electrosyntrophic_Denitrifying_Consortium.yaml` | `1c9db92e6594e7744b051cec01e1f4cc33c3ff0370d73ca6419f56fd4edcc241` | `taxonomy[0]`: `Shewanella oneidensis` (`NCBITaxon:70863`) | `PMID:39504696` | **Evidence-Limited**: Cached abstract (`PMID:39504696`) names species-level *S. oneidensis* without confirming strain MR-1 (`NCBITaxon:211586`) or assaying MtrCAB/CymA proteins. |
| `CommunityMech:000294` | `kb/communities/Corynebacterium_glutamicum_Shewanella_oneidensis_Succinic_Acid_Coculture.yaml` | `1522534e0e993cff111c4fcde85182868aeae81389cb47120d97a3882b88250d` | `taxonomy[1]`: `Shewanella oneidensis` (`NCBITaxon:70863`) | `PMID:42203120` | **Evidence-Limited**: Cached abstract (`PMID:42203120`) describes an engineered *S. oneidensis* strain in a succinic acid coculture without specifying parent strain MR-1 or assaying MtrCAB/CymA proteins. |
| `CommunityMech:000327` | `kb/communities/Methane_MFC_Electrogenesis_Nitrogen_Fixation_Consortium.yaml` | `11138074c4f29dbcc2edc83f109d31930d2011cab626c35dbab9d04a865252b4` | `taxonomy[1]`: `Geobacter` (`NCBITaxon:28231`) | `PMID:42551599` | **Excluded (Genus-level 16S guild)**: Genus-level *Geobacter* (`NCBITaxon:28231`) in an anaerobic methane MFC; not *G. sulfurreducens* PCA. |
| `CommunityMech:000328` | `kb/communities/Waste_Sludge_Electrofermentation_Biofilm_Suspension_Community.yaml` | `96790620c4f70dd5ca498af0636db53fc9fb7d6779a96851bb31385b71c6f329` | `taxonomy[1]`: `Geobacter` (`NCBITaxon:28231`) | `PMID:41793807` | **Excluded (Genus-level 16S guild)**: Genus-level *Geobacter* (`NCBITaxon:28231`) in a waste-sludge electrofermentation community; not *G. sulfurreducens* PCA. |

---

## 6. Cycle 2 Stage 1 Newly Added Records (`CommunityMech:000484`–`000490`) Checked

All 7 records added in Cycle 2 Stage 1 (`4` communities in `kb/communities/` + `3` isolates in `data/isolates/`) were inspected for reusable `CommonTaxon` linkage and gene/protein elements:

| Record ID | File Path | SHA-256 | Taxa (`NCBITaxon`) | Stage 3 Assessment |
|---|---|---|---|---|
| `CommunityMech:000484` | `kb/communities/Aquifer_Sediment_Cable_Bacteria_Sulfur_Community.yaml` | `8faad2ab07cfb8f5cd789e5090d327abc5aeab737872d1b32ec6b47e59e77df4` | `Desulfobulbaceae` (`NCBITaxon:213121`), `Thiobacillus` (`NCBITaxon:919`), `Ignavibacteria` (`NCBITaxon:1134404`) | **Not Applicable**: Family/genus/class-level sediment guilds (`PMID:32123322`); no reusable `CommonTaxon` or strain-resolved UniProt target. |
| `CommunityMech:000485` | `kb/communities/Dexing_Copper_Bioleaching_Heap_Community.yaml` | `e12ae0d4c80ec68da97fd77e007b609261f6865e9256bb27edfc58c2634965d5` | `Acidithiobacillus ferrooxidans` (`NCBITaxon:920`), `Acidithiobacillus` (`NCBITaxon:119977`), `Thiobacillus` (`NCBITaxon:919`), `Leptospirillum ferrooxidans` (`NCBITaxon:180`) | **Evidence-Limited / Not Applicable**: Species/genus-level bioleaching heap guilds without strain/genome resolution or protein-level assays in cached source (`PMID:26781463`, `doi:10.1186/s12863-016-0330-4`). |
| `CommunityMech:000486` | `kb/communities/Stare_Ransko_Mine_Tailings_Bioleaching_Consortium.yaml` | `65d9768713aa281dca229c73794ae3f825f22acb78d857b9eb189addfeeb7acf` | `Acidithiobacillus ferrooxidans` (`NCBITaxon:920`), `Acidithiobacillus thiooxidans` (`NCBITaxon:930`), `Leptospirillum ferrooxidans` (`NCBITaxon:180`) | **Evidence-Limited / Not Applicable**: Indigenous mine-tailings consortium without strain/genome resolution or protein-level assays in cached source (`doi:10.3390/min14030255`). |
| `CommunityMech:000487` | `kb/communities/Moderate_Thermophile_Chalcopyrite_pH_Bioleaching_Consortium.yaml` | `6dd87be5e5181dd81e8119e10bc5a3f645c33a98084614df9d60e2a26f085e2b` | `Sulfobacillus thermosulfidooxidans` (`NCBITaxon:28034`), `Acidithiobacillus caldus` (`NCBITaxon:33059`), `Ferroplasma thermophilum` (`NCBITaxon:2591003`) | **Evidence-Limited / Not Applicable**: Defined moderate-thermophile bioleaching consortium (`doi:10.1007/s13213-019-01453-y`); cached abstract reports physiological pH/redox kinetics without gene/protein assays. |
| `CommunityMech:000488` | `data/isolates/Bacillus_licheniformis_Chromate_Biosorption.yaml` | `7ad94b96c56469311346da8af429fb922eaa122a96464121697282771c45120e` | `Bacillus licheniformis` (`NCBITaxon:1402`) | **Evidence-Limited / Not Applicable**: Single-isolate Cr(VI) biosorption study (`doi:10.3389/fmicb.2024.1423741`); cached source does not resolve a sequenced reference genome or specific chromate-reductase UniProt accession. |
| `CommunityMech:000489` | `data/isolates/Acidithiobacillus_LED_Metal_Bioleaching.yaml` | `1183e9ac2b3567f395e7f19cceb575ac15227bc4ce1323736c042d1fbd43fb4b` | `Acidithiobacillus ferrooxidans` (`NCBITaxon:920`) | **Evidence-Limited / Not Applicable**: Single-isolate LED-illuminated bioleaching study (`PMID:30343816`, `PMID:31203122`); no sequenced genome or specific protein assay in cached sources. |
| `CommunityMech:000490` | `data/isolates/Ferrimicrobium_acidiphilum_Iron_Respiration.yaml` | `58f2d2fd0be0be26c7519de2e31f5cc80a9dbb2a43932a242dc27fc832e1a492` | `Ferrimicrobium acidiphilum` (`NCBITaxon:121039`) | **Evidence-Limited / Not Applicable**: Single-isolate acidophilic Fe(II)/Fe(III) respiration study (`doi:10.1128/aem.01906-20`); no specific UniProt protein assayed in cached source. |

---

## 7. Representation & Writer Blockers Documented

1. **No Interaction-Level `protein_examples` Slot on `EcologicalInteraction`**:
   - In `src/communitymech/schema/communitymech.yaml`, `EcologicalInteraction` has `biological_processes` (`GO` terms) and `metabolites` (`CHEBI` terms), while `GeneAnnotation` (`UniProtKB:...`) lives exclusively on `CommonTaxon.genes[]` in `kb/taxa/*.yaml` and is linked from `TaxonomicComposition.common_taxon`.
   - Community-specific enzymes/transporters mentioned in community descriptions or interaction notes for non-reusable taxa cannot be attached directly to an `EcologicalInteraction` node without minting a dedicated `CommonTaxon` file in `kb/taxa/`. Per `.claude/skills/add-uniprot-protein-examples/SKILL.md` ("The native protein route is `CommonTaxon.genes[]` (`GeneAnnotation`), not a new `protein_examples` field on community interactions... If a community-specific protein example lacks a suitable native owner or relationship, record the representation gap instead of inserting unsupported fields"), no unsupported fields were added.
2. **Corpus Ledger & Hash Synchronization**:
   - All 484 `MicrobialCommunity` file SHA-256 hashes and review statuses are tracked in `reports/causal_graph_review/inventory.tsv` and `reports/causal_graph_review/decisions/20261021-stage3-common-taxon-links.yaml` (`CommunityMech:000201` updated to `36c0ea58af1a8cd8d96ccf3bf7d3909176613b4be114cf4f8c7e24d6cea246bd`).
