# Cycle 8 Stage 3 — UniProtKB Protein Examples Corpus Review (`2026-11-05`)

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle / Stage**: Cycle `8`, Stage `3` (`protein_examples`, `required_outputs: []`)
- **Base Commit (`main`)**: `e894bf87d3c77d08595d1810d4bd5b474ff1797f`
- **Primary Skill**: [`.claude/skills/add-uniprot-protein-examples/SKILL.md`](../.claude/skills/add-uniprot-protein-examples/SKILL.md)
- **Companion Skill**: [`.claude/skills/curate-yaml-record/SKILL.md`](../.claude/skills/curate-yaml-record/SKILL.md)

---

## 1. Corpus Inventory & Summary Accounting

Across the current `main` baseline (`e894bf87d3c77d08595d1810d4bd5b474ff1797f`), the repository contains **510** curated YAML records across three roots:

| Corpus Root | Root Class | Record Count | Linked to `kb/taxa/*.yaml` (`common_taxon`) | Curated `UniProtKB:` `GeneAnnotation` Entries | Total Gene-Level `EvidenceItem`s (Before -> After C8S3) |
|---|---|---:|---:|---:|---:|
| `kb/communities/*.yaml` | `MicrobialCommunity` | `499` | `14` (`9` -> `taxon:000001`, `6` -> `taxon:000002`, `1` overlap) | Linked via `common_taxon` | — |
| `data/isolates/*.yaml` | `MicrobialCommunity` | `9` | `0` | `0` | — |
| `kb/taxa/*.yaml` | `CommonTaxon` | `2` | `2` (`CommunityMech:taxon:000001`, `CommunityMech:taxon:000002`) | `9` (`5` on `taxon:000001`, `4` on `taxon:000002`) | `43` -> `47` (`24 -> 26` on `taxon:000001`; `19 -> 21` on `taxon:000002`) |
| **Total** | — | **510** | **14 communities + 2 taxon records** | **9** | **43 -> 47** |

### Reusable Taxon Records Updated in Cycle 8 Stage 3

1. **[`kb/taxa/Shewanella_oneidensis_MR1.yaml`](../kb/taxa/Shewanella_oneidensis_MR1.yaml)** (`CommunityMech:taxon:000001`, `NCBITaxon:211586`, reference assembly `GCF_000146165.2`):
   - **Base SHA-256**: `264d4a709ae864575d9d0f66463508ee9dedf39c659997e6bbdd31f52b05a6aa`
   - **Updated SHA-256**: `3ef039817198dc7acb2d61a79b3910288753cccdcf8b7cf327b524ecf8be4144`
   - **History Sidecar**: [`history/records/Shewanella_oneidensis_MR1/2026-11-06T071700Z-antigravity-c8s301.yaml`](../history/records/Shewanella_oneidensis_MR1/2026-11-06T071700Z-antigravity-c8s301.yaml) (`sha256: 6ac2233cc55e1f7c3a477c32a86c7975cdb3aa915fae4d4ba74e8e92302b3d8d`)
   - **Curated Genes (`5`) & Evidence Counts (`24 -> 26`)**:
     - `mtrC` (`UniProtKB:Q8EG33`, `SO_1778`, `GO:0009055`, `GO:0020037`): `5 -> 6` `EvidenceItem`s (`PMID:42733304` x3, `PMID:41236292`, `PMID:39504696`, `PMID:31537786`). Added verbatim `IN_VITRO` `SUPPORT` snippet from [`references_cache/PMID_42733304.txt`](../references_cache/PMID_42733304.txt) (`CommunityMech:000010`) documenting targeted homologous-recombination deletion of `mtrC` (`SO_1778`) in wild-type *S. oneidensis* MR-1 (`GCF_000146165.2`) to construct strains `SO3∆mtrC` and `SO3∆mtrC∆omcA`.
     - `mtrB` (`UniProtKB:Q8EG34`, `SO_1776`, `GO:0015288`): `4` `EvidenceItem`s (`PMID:42733304`, `PMID:41210787`, `PMID:31537786`, `PMID:32849356`).
     - `mtrA` (`UniProtKB:Q8EG35`, `SO_1777`, `GO:0009055`, `GO:0020037`): `5` `EvidenceItem`s (`PMID:42733304`, `PMID:41210787`, `PMID:31537786`, `PMID:32849356` x2).
     - `omcA` (`UniProtKB:Q8EG32`, `SO_1779`, `GO:0009055`, `GO:0020037`): `5 -> 6` `EvidenceItem`s (`PMID:42733304` x3, `PMID:41236292`, `PMID:39504696`, `PMID:31537786`). Added verbatim `IN_VITRO` `SUPPORT` snippet from [`references_cache/PMID_42733304.txt`](../references_cache/PMID_42733304.txt) (`CommunityMech:000010`) documenting targeted homologous-recombination deletion of `omcA` (`SO_1779`) in wild-type *S. oneidensis* MR-1 (`GCF_000146165.2`) to construct strains `SO3∆omcA` and `SO3∆mtrC∆omcA`.
     - `cymA` (`UniProtKB:Q8E945`, `SO_4591`, `GO:0009055`, `GO:0020037`): `5` `EvidenceItem`s (`PMID:42733304`, `PMID:39504696`, `PMID:31537786`, `PMID:34986141` x2).

2. **[`kb/taxa/Geobacter_sulfurreducens.yaml`](../kb/taxa/Geobacter_sulfurreducens.yaml)** (`CommunityMech:taxon:000002`, `NCBITaxon:35554`, reference assembly `GCF_000007985.2`):
   - **Base SHA-256**: `970ca3a904da541269aa8e7091295f8970cbd77da6957f4d34e43802666844fc`
   - **Updated SHA-256**: `d66891d072989f3101fed3ec44891ba141eaf13a8930cad23c0359477f5b825c`
   - **History Sidecar**: [`history/records/Geobacter_sulfurreducens/2026-11-06T071700Z-antigravity-c8s302.yaml`](../history/records/Geobacter_sulfurreducens/2026-11-06T071700Z-antigravity-c8s302.yaml) (`sha256: add7b86e75e14cff7b337f32c54902f79f8289072337e4503cbe3321b1025cf1`)
   - **Curated Genes (`4`) & Evidence Counts (`19 -> 21`)**:
     - `pilA` (`UniProtKB:Q74BW5`, `GSU1496`, `GO:0009055`, `GO:0009289`): `6 -> 7` `EvidenceItem`s (`PMID:41210787` x2, `PMID:37650614` x2, `PMID:41236292`, `PMID:28287150`, `PMID:32265334`). Added verbatim `IN_VITRO` `SUPPORT` snippet from [`references_cache/PMID_37650614.txt`](../references_cache/PMID_37650614.txt) (`CommunityMech:000249`) identifying `PilA` (`GSU1496`) in *G. sulfurreducens* PCA as the monomer assembled into electrically conductive pili required for Fe(III) oxide reduction and DIET.
     - `omcS` (`UniProtKB:Q749X9`, `GSU2504`, `GO:0009055`, `GO:0020037`): `7` `EvidenceItem`s (`PMID:41210787`, `PMID:37650614`, `PMID:28992596`, `PMID:41236292`, `PMID:31537786`, `PMID:32849356`, `PMID:34986141`).
     - `omcZ` (`UniProtKB:Q74A90`, `GSU2076`, `GO:0009055`, `GO:0020037`): `3 -> 4` `EvidenceItem`s (`PMID:41210787`, `PMID:28992596`, `PMID:34986141` x2). Added verbatim `COMPUTATIONAL` `SUPPORT` snippet from [`references_cache/PMID_34986141.md`](../references_cache/PMID_34986141.md) (`CommunityMech:000134`) documenting polymerization of *G. sulfurreducens* `OmcZ` (`GSU2076`) into conductive extracellular nanowires as the benchmark for evaluating ANME `OmcZ` homologs.
     - `omcB` (`UniProtKB:Q74A86`, `GSU2737`, `GO:0009055`, `GO:0020037`): `3` `EvidenceItem`s (`PMID:41876513`, `PMID:37650614`, `PMID:37747940`).

---

## 2. Audit of Newly Added Cycle 8 Stage 1 Records (`CommunityMech:000510`–`CommunityMech:000514`, Batch 140)

All 5 community records added in Cycle 8 Stage 1 (and updated with causal downstream mechanism graphs in Cycle 8 Stage 2) were audited against their committed `references_cache/` files for gene/protein elements and exact organism/sequence scope:

| Record ID | File | SHA-256 | Primary Reference | Taxa (`NCBITaxon`) | Gene / Protein Context in Source | Disposition & Blocker Classification |
|---|---|---|---|---|---|---|
| `CommunityMech:000510` | [`kb/communities/Syntrophobacter_Desulfovibrio_Propionate_Syntrophy.yaml`](../kb/communities/Syntrophobacter_Desulfovibrio_Propionate_Syntrophy.yaml) | `2e95cd16f6affd030fd63c57346db02eee8b3e2d5331d72163cc908c6f118129` | `PMID:29611893` ([`PMID_29611893.md`](../references_cache/PMID_29611893.md)) | *Syntrophobacter fumaroxidans* (`NCBITaxon:119484`), *Desulfovibrio desulfuricans* (`NCBITaxon:876`, strain G11) | Names locus tags and enzyme complexes in *S. fumaroxidans* MPOB (`Sfum_2682-85` `Fdh1`, `Sfum_1273-74` `Fdh2`, `Sfum_0035-37` `Fdh3`, `Sfum_2703-06` `Hyn`, `Sfum_2952-53` `Hyd1`, `Sfum_0844-46` `Hyd2`, `Sfum_0819-24` `HdrABC/HdrL`, `Sfum_1998-2006` `Rnf`, `Sfum_4047` `Flx-Hdr`, `Sfum_0457-0458` `Mcm`, `Sfum_1218-1225` `Sdh`) and *Desulfovibrio* sp. G11 (`G11_16920-16925` `FdhAB-1`, `G11_14815-14820` `FdhAB-2`, `G11_21480-21495` `FdhAB-3`, `G11_07685-07690` `HynAB-1`, `G11_00765-00770` `HynAB-2`, `G11_06780-06795` `HydABC`, `G11_04645-04650` `Ech`), but does not cite `UniProtKB:` accessions in text. | **Offline-Proteome-Mapping-Limited (`20`-record cohort)**: Exact locus tags are known in `PMID:29611893`, but no offline UniProtKB mapping table for *S. fumaroxidans* MPOB or *Desulfovibrio* sp. G11 is committed in the repository, and offline policy prohibits network queries to resolve `Sfum_*` / `G11_*` locus tags to `UniProtKB:` accessions. |
| `CommunityMech:000511` | [`kb/communities/Syntrophomonas_Methanobacterium_Butyrate_Syntrophy.yaml`](../kb/communities/Syntrophomonas_Methanobacterium_Butyrate_Syntrophy.yaml) | `b52fec1591b3ffbe6a33a11c32ff86d885ed63e7284e8b9f095e087b48b754f2` | `PMID:35699440` ([`PMID_35699440.md`](../references_cache/PMID_35699440.md)) | *Syntrophomonas wolfei* (`NCBITaxon:863`), *Methanobacterium formicicum* (`NCBITaxon:2162`) | Characterizes syntrophic butyrate beta-oxidation, interspecies H2/formate transfer, and methanogenesis kinetics via substrate/product stoichiometry and 16S rRNA monitoring without naming specific genes, locus tags, or UniProtKB proteins. | **Inapplicable — Metabolite / Kinetic Assay Only (`125`-record cohort)**: Source paper does not assay or name specific genes or proteins. |
| `CommunityMech:000512` | [`kb/communities/Trichococcus_Syntrophomonas_Methanobacterium_Butyrate_Coculture.yaml`](../kb/communities/Trichococcus_Syntrophomonas_Methanobacterium_Butyrate_Coculture.yaml) | `c51b53adc804e4073882001d3627689d519ab8a9971c9573e3e0561874e512d3` | `PMID:35699440` ([`PMID_35699440.md`](../references_cache/PMID_35699440.md)) | *Trichococcus flocculiformis* strain ES5 (`NCBITaxon:82803`), *Syntrophomonas wolfei* (`NCBITaxon:863`), *Methanobacterium formicicum* (`NCBITaxon:2162`) | Characterizes glycerol fermentation to butyrate/acetate/formate/1,3-propanediol and syntrophic methanogenesis without naming specific genes, locus tags, or UniProtKB proteins. | **Inapplicable — Metabolite / Kinetic Assay Only (`125`-record cohort)**: Source paper does not assay or name specific genes or proteins. |
| `CommunityMech:000513` | [`kb/communities/EcoFAB_Ring_Trial_SynCom16.yaml`](../kb/communities/EcoFAB_Ring_Trial_SynCom16.yaml) | `05be6ff3f83a28c6195ef5138b60a08fb66732a4fe398738ba572ebe439d0633` | `PMID:40920748` ([`PMID_40920748.md`](../references_cache/PMID_40920748.md)) | 16 switchgrass-rhizosphere isolates grounded at genus/species-group rank (`NCBITaxon:1827`, `1763`, `407`, `34072`, `379`, `85413`, `374`, `68`, `1667`, `86795`, `79328`, `423349`, `354354`, `2837503`, `55080`, `44249`) | Multi-laboratory ring trial assaying 16S rRNA amplicon profiles, root/shoot biomass, and LC-MS exometabolomics; no individual genes, locus tags, or proteins are assayed in `PMID:40920748`. | **Inapplicable — 16S / Genus-Rank / Exometabolomic Study (`349`-record cohort)**: Isolates are grounded at genus rank (`NCBITaxon`) and no gene or protein sequences are assayed. |
| `CommunityMech:000514` | [`kb/communities/Wheat_Consortium_C7.yaml`](../kb/communities/Wheat_Consortium_C7.yaml) | `fa1c93e48c4380cf67a45ce6d6dbd63a0f13f8823057fa3e4a7b8c71ac526f73` | `PMID:36118206` ([`PMID_36118206.md`](../references_cache/PMID_36118206.md)) | *Pseudomonas* sp. B5 (`NCBITaxon:286`), *Streptomyces* sp. B6 (`NCBITaxon:1883`), *Chryseobacterium* sp. B7 (`NCBITaxon:59732`), *Pseudomonas* sp. B11 (`NCBITaxon:286`) | Mentions biosynthetic gene cluster families (`2,4-diacetylphloroglucinol`, `phenazine`) in genome-mined wheat isolates grounded at genus rank (`NCBITaxon`), without locus tags, RefSeq assembly accessions, or UniProtKB protein accessions. | **Inapplicable — Genus-Rank Isolates Without Sequence-Specific Protein Accessions (`349`-record cohort)**: Assigning reference-strain *Pseudomonas* or *Streptomyces* UniProtKB accessions onto genus-level isolates `B5`/`B6`/`B7`/`B11` would violate organism and sequence scope. |

---

## 3. Corpus-Wide Partition & Representation / Writer Boundaries (`508` `MicrobialCommunity` Records)

| Cohort | Record Count | Description & Scope Boundary |
|---|---:|---|
| **1. Linked to Reusable `CommonTaxon` (`kb/taxa/*.yaml`)** | `14` | `9` communities link to `CommunityMech:taxon:000001` (*Shewanella oneidensis* MR-1) and `6` link to `CommunityMech:taxon:000002` (*Geobacter sulfurreducens* PCA), with `1` overlap (`Shewanella_Geobacter_Exoelectrogenic_Biofilm_Community.yaml`). All `9` curated `UniProtKB:` proteins carry `GO:` terms, `locus_tag`, `genome` (`GCF_000146165.2` / `GCF_000007985.2`), `supports_roles`, `supports_interaction`, and `47` total verbatim cached `EvidenceItem`s. |
| **2. 16S / Metagenomic / Genus- or Family-Rank Guild Communities** | `349` | Communities and enrichments defined by 16S rRNA amplicon sequencing, metagenomic OTUs/ASVs/MAGs, or genus-rank isolates (`NCBITaxon` at genus/family/order rank or unsequenced environmental isolates, including `CommunityMech:000513` and `CommunityMech:000514`). Generalizing reference-strain `UniProtKB:` accessions onto these taxa is prohibited by the organism/sequence scope rules of [`add-uniprot-protein-examples`](../.claude/skills/add-uniprot-protein-examples/SKILL.md). |
| **3. Defined / Species-Grounded Communities Assaying Metabolites or Kinetics Only** | `125` | Co-cultures, synthetic consortia, and isolate baselines (`499` communities + `9` `data/isolates/*.yaml`) whose cited sources measure substrate/product fluxes, growth yields, or electron balances without assaying or naming specific genes or proteins (including `CommunityMech:000511` and `CommunityMech:000512`). |
| **4. Species- / Strain-Grounded Communities Naming Gene Symbols or Locus Tags Without Offline UniProtKB Tables** | `20` | Records whose cached sources name gene symbols or locus tags (e.g., `CommunityMech:000510` naming `Sfum_*` and `G11_*` locus tags in `PMID:29611893`; `Synechococcus elongatus` PCC 7942 `cscB`; `Rhodopseudomonas palustris` CGA009 `nifA`), but for which no offline UniProtKB accession mapping table is committed in the repository and `references_cache/` does not contain `UniProtKB:` identifiers. Under the repository offline rule (no network calls to UniProt REST APIs), fabricating or guessing `UniProtKB:` accessions from memory is strictly forbidden. |
| **Total `MicrobialCommunity` Records (`kb/communities/` + `data/isolates/`)** | **508** | Plus `2` `CommonTaxon` records in `kb/taxa/` = **510** total YAML records. |
