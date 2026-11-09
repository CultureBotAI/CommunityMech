# Cycle 13 Stage 3 UniProt Protein Examples Corpus Audit and Curation Report (2026-11-09)

- **Run / Cycle / Stage**: `mech-goal-sequence-20261019` / Cycle 13 / Stage 3 (`protein_examples`)
- **Source Revision**: `524b135504eb1b58c1f530fd198a73ad3d8ca99e` (PR #2744 merge commit)
- **Skill Followed**: `.claude/skills/add-uniprot-protein-examples/SKILL.md`
- **Records Audited**: **537** total YAML records (**512** `kb/communities/*.yaml`, **23** `data/isolates/*.yaml`, **2** `kb/taxa/*.yaml`)

---

## 1. Corpus-Wide Audit Summary (537 Records)

Every record across all three repository roots (`kb/communities/`, `data/isolates/`, `kb/taxa/`) was audited at commit `524b135504eb1b58c1f530fd198a73ad3d8ca99e` for:
1. Reusable `CommonTaxon` linkage (`taxonomy[*].common_taxon`) and `GeneAnnotation` entries (`kb/taxa/*.yaml` `genes[*].gene_id` `UniProtKB:` accessions, `locus_tag`, `genome`, `go_terms`, `supports_roles`, `supports_interaction`, and `evidence`).
2. Newly added Cycle 13 Stage 1 (`PR #2743`) and Stage 2 (`PR #2744`) records (`CommunityMech:000536` through `CommunityMech:000541`).
3. New verbatim, non-overlapping `EvidenceItem` support in `references_cache/` for the 9 curated `UniProtKB:` protein entries across `kb/taxa/Shewanella_oneidensis_MR1.yaml` and `kb/taxa/Geobacter_sulfurreducens.yaml`.
4. Representation, writer, and offline-proteome boundaries.

| Cohort | Description | `kb/communities/` | `data/isolates/` | `kb/taxa/` | Total |
|---|---|---:|---:|---:|---:|
| **Reusable `CommonTaxon` Records** | Canonical `CommonTaxon` records carrying `GeneAnnotation` entries with verified `UniProtKB:` accessions (`Shewanella_oneidensis_MR1.yaml`, `Geobacter_sulfurreducens.yaml`) | 0 | 0 | 2 | **2** |
| **Cohort 1 — `CommonTaxon`-Linked Records** | `MicrobialCommunity` records linking `taxonomy[*].common_taxon` to `CommunityMech:taxon:000001` (16 records: 15 communities + 1 isolate) and/or `CommunityMech:taxon:000002` (6 communities; 1 shared with `000001`) | 20 | 1 | 0 | **21** |
| **Cohort 2 — Inapplicable (16S / Metagenomic / Higher-Rank / Unsequenced Guilds)** | Amplicon/16S, MAG/metagenomic, enrichment, or genus/family/phylum-level guilds where assigning a single strain-specific `UniProtKB:` accession would violate organism and sequence specificity | 352 | 0 | 0 | **352** |
| **Cohort 3 — Inapplicable (Defined/Isolate Kinetic & Metabolite Assays Without Gene/Protein Identifiers)** | Defined co-cultures, SynComs, and isolate baselines assaying growth kinetics, biomass, or metabolite fluxes without gene symbols, locus tags, or protein identifiers in their cached sources | 118 | 20 | 0 | **138** |
| **Cohort 4 — Offline-Proteome-Mapping-Limited (Gene Symbols / Locus Tags Without Offline `UniProtKB:` Mapping Table)** | Species- or strain-grounded records whose sources name gene symbols or locus tags (`purH`, `nifA*`, `hupV`, `hoxJ`, `hoxA`, `RPA2390`, `entF`, `rpoC`, `rpoS`, `rph`, `pyrE`, `nrfA`, `napA`, `nosZ`, `narG`, `nirK`, `ldh`, `cscB`, `sacC`, `katG`, `tnaA`, `metE`, `btuB`, `ackA`, `pta`, `acs`, `fdh`, `hdr`, `mvh`, `mcrA`) without reporting `UniProtKB:` accessions in cached text and without a local offline UniProt proteome table in `data/raw/` | 22 | 2 | 0 | **24** |
| **Total** | All YAML records across repository roots | **512** | **23** | **2** | **537** |

---

## 2. Audit of Cycle 13 Stage 1 & Stage 2 Additions (`CommunityMech:000536`–`000541`)

| ID | Path | SHA-256 at `524b135504eb1b58c1f530fd198a73ad3d8ca99e` | Taxa & Grounding | Primary Source | Stage 3 Classification & Audit Rationale |
|---|---|---|---|---|---|
| `CommunityMech:000536` | `data/isolates/Pseudomonas_ZM1_Prometryn_Degrading_Isolate_Baseline.yaml` | `61b09aef22790ae6960d309edc1a1a51fffca8c659ed04be36fa08fecdd2ccf9` | `Pseudomonas sp. ZM-1` (`NCBITaxon:286`, `GTDB:g__Pseudomonas`, 16S rDNA GenBank `PV643981`) | `PMID:42795638` (`references_cache/PMID_42795638.txt`) | **Cohort 3 (Inapplicable — 16S genus-rank isolate kinetic baseline without genome assembly or gene/protein identifiers)**. `PMID:42795638` characterizes strain ZM-1 by 16S rDNA phylogeny (`PV643981`, 99.6% similarity to *Pseudomonas monteilii*), liquid BSM prometryn degradation kinetics (`97.3 ± 1.2%` within 48 h, `k = 0.075 h^-1`, `t1/2 = 9.2 h`, Table 2), and soil microcosm attenuation (`t1/2 = 12.3 d`, `11.4 ± 1.8%` residual at 30 d, Table 6), explicitly noting that targeted intermediate detection and genomic functional gene analysis were deferred to follow-up work. |
| `CommunityMech:000537` | `data/isolates/Achromobacter_ZM2_Prometryn_Degrading_Isolate_Baseline.yaml` | `54d10773f390acfaf392996a1ce4bb25978fb6f0d3cc1d10657c4626fef56819` | `Achromobacter sp. ZM-2` (`NCBITaxon:222`, `GTDB:g__Achromobacter`, 16S rDNA GenBank `PV643982`) | `PMID:42795638` (`references_cache/PMID_42795638.txt`) | **Cohort 3 (Inapplicable — 16S genus-rank isolate kinetic baseline without genome assembly or gene/protein identifiers)**. `PMID:42795638` characterizes strain ZM-2 by 16S rDNA phylogeny (`PV643982`, 99.8% similarity to *Achromobacter xylosoxidans*), liquid BSM prometryn degradation kinetics (`85.1 ± 1.5%` within 48 h, `k = 0.040 h^-1`, `t1/2 = 17.3 h`, max `OD600 = 0.91` at 28 h, Table 2), and soil microcosm attenuation (`t1/2 = 14.1 d`, `17.6 ± 2.3%` residual at 30 d, Table 6) without sequenced isolate genome assembly or protein accessions. |
| `CommunityMech:000538` | `data/isolates/Stenotrophomonas_ZM3_Prometryn_Degrading_Isolate_Baseline.yaml` | `c41cdba4bbbd54b987db9e8f901658ae1e76c79524a8cf9b2ac8ae271044bc4f` | `Stenotrophomonas sp. ZM-3` (`NCBITaxon:40323`, `GTDB:g__Stenotrophomonas`, 16S rDNA GenBank `PZ433558`) | `PMID:42795638` (`references_cache/PMID_42795638.txt`) | **Cohort 3 (Inapplicable — 16S genus-rank isolate kinetic baseline without genome assembly or gene/protein identifiers)**. `PMID:42795638` characterizes strain ZM-3 by 16S rDNA phylogeny (`PZ433558`, 99.5% similarity to *Stenotrophomonas maltophilia*), liquid BSM prometryn degradation kinetics (`92.8 ± 1.1%` within 48 h, `k = 0.055 h^-1`, `t1/2 = 12.6 h`, max `OD600 = 0.79` at 44 h, Table 2), and soil microcosm attenuation (`t1/2 = 9.5 d`, `92.1 ± 1.5%` removal / `7.9 ± 1.5%` residual at 30 d, Table 6) without sequenced isolate genome assembly or protein accessions. |
| `CommunityMech:000539` | `data/isolates/Rhodopseudomonas_Palustris_CGA676_Anaerobic_Monoculture_Baseline.yaml` | `ad02b70b47aa8cd86d7949e08c3ce23366c1caec6c5463c74cd45a9396aac666` | `Rhodopseudomonas palustris CGA676` (`NCBITaxon:1076`, `AMBIGUOUS` across 5 `gtdb_candidates`: `GTDB:s__Rhodopseudomonas_palustris_C`, `_F`, `_G`, `_J`, `GTDB:s__Rhodopseudomonas_pseudopalustris`) | `PMID:42117636` (`references_cache/PMID_42117636.txt`) | **Cohort 4 (Offline-Proteome-Mapping-Limited — strain-grounded isolate baseline with gene symbols/locus tags in source but no cached `UniProtKB:` accession or offline proteome table)**. `PMID:42117636` names CGA0092/CGA676 loci (`nifA*`, `hupV`, `hoxJ`, `hoxA`, `RPA2390`, `RPA2382-90`) without reporting `UniProtKB:` accessions in cached full text (`references_cache/PMID_42117636.txt`), and no offline UniProt proteome TSV for `Rhodopseudomonas palustris` (`NCBITaxon:1076` / CGA009 `NCBITaxon:258594`) is present in `data/raw/`. |
| `CommunityMech:000540` | `data/isolates/Escherichia_Coli_PFM2_Anaerobic_Monoculture_Baseline.yaml` | `991e85326303854835a6a7481d1599e068f4d67411856fbb8092620953919b18` | `Escherichia coli PFM2` (`NCBITaxon:562`, `GTDB:s__Escherichia_coli`, `GROUNDED`) | `PMID:42117636` (`references_cache/PMID_42117636.txt`) | **Cohort 4 (Offline-Proteome-Mapping-Limited — strain-grounded isolate baseline with gene symbols in source but no cached `UniProtKB:` accession or offline proteome table)**. `PMID:42117636` names MG1655/PFM2 genes (`purH`, `entF`, `rpoC`, `rpoS`, `rph`, `pyrE`) without reporting `UniProtKB:` accessions in cached full text (`references_cache/PMID_42117636.txt`), and no offline UniProt proteome TSV for `Escherichia coli` (`NCBITaxon:562` / K-12 MG1655 `NCBITaxon:83333`) is present in `data/raw/`. |
| `CommunityMech:000541` | `kb/communities/Rhodopseudomonas_CGA676_Ecoli_PFM2_DeltaPurH_Adenine_Competition_Coculture.yaml` | `19eb2a05854e12882277cdc6646edf9f9c5fc91f4392cc080fc2b09bcb9b0382` | `Rhodopseudomonas palustris CGA676` (`NCBITaxon:1076`, `AMBIGUOUS`) + `Escherichia coli PFM2` (`NCBITaxon:562`, `GTDB:s__Escherichia_coli`, `GROUNDED`) + `Escherichia coli PFM2 ΔpurH` (`NCBITaxon:562`, `GTDB:s__Escherichia_coli`, `GROUNDED`) | `PMID:42117636` (`references_cache/PMID_42117636.txt`) | **Cohort 4 (Offline-Proteome-Mapping-Limited — three-strain coculture naming `purH` and `nifA*`/`hupV`/`RPA2390` without cached `UniProtKB:` accessions or offline proteome table)**. Furthermore, `EcologicalInteraction` and `InteractionDownstream` lack schema slots (`associated_genes`) for direct interaction-level gene/protein CURIE binding. |

---

## 3. Curated `CommonTaxon` Protein Evidence Additions (`kb/taxa/*.yaml`)

Four new verbatim, bracket-free `EvidenceItem` entries were verified against committed files in `references_cache/` and added through `write_validated_community(..., target_class="CommonTaxon")` and `record_curation_event(..., action="ADD_UNIPROT_PROTEIN_EXAMPLES")`, increasing total curated `CommonTaxon` protein `EvidenceItem` entries from **66 to 70** across the **9** verified `UniProtKB:` proteins (**39** on `kb/taxa/Shewanella_oneidensis_MR1.yaml` and **31** on `kb/taxa/Geobacter_sulfurreducens.yaml`):

| CommonTaxon Record | Gene Symbol (`locus_tag`) | `UniProtKB:` ID | Genome Assembly | Added Reference (`supports`, `evidence_source`) | Verbatim Snippet & Linked Communities | `EvidenceItem` Count (Before $\rightarrow$ After) |
|---|---|---|---|---|---|---:|
| `kb/taxa/Shewanella_oneidensis_MR1.yaml` (`CommunityMech:taxon:000001`, `NCBITaxon:211586`) | `mtrC` (`SO_1778`) | `UniProtKB:Q8EG33` | `GCF_000146165.2` | `PMID:40845095` (`SUPPORT`, `IN_VITRO`) | `"In model electroactive bacteria such as Geobacter and Shewanella, cytochromes such as PpcA, OmcS, OmcZ, MtrA, and MtrC exhibit redox-active windows spanning several hundred millivolts ( Fig. 4, A and B ), enabling them to transfer electrons to acceptors with more negative midpoint potentials, such as anthraquinone-2,6-disulfonate (AQDS; −186 mV) and flavins (−210 mV) ( 52 – 57 )."` (`CommunityMech:000134`, `CommunityMech:000276`) | 10 $\rightarrow$ **11** |
| `kb/taxa/Shewanella_oneidensis_MR1.yaml` (`CommunityMech:taxon:000001`, `NCBITaxon:211586`) | `omcA` (`SO_1779`) | `UniProtKB:Q8EG32` | `GCF_000146165.2` | `PMID:42733304` (`SUPPORT`, `IN_VITRO`) | `"The results showed that the SO3∆mtrC‐BS3 consortium (47.67 mW m−2), the SO3∆omcA‐BS3 consortium (50.01 mW m−2), and the SO3∆mtrC∆omcA‐BS3 consortium (28.39 mW m−2) showed 9.50‐, 9.05‐, and 15.95‐fold decreases in the EET rate compared to the SO3‐BS3 consortium (452.90 mW m−2), respectively (Figure 5c ), confirming that the disruption of MtrC and OmcA significantly inhibited the EET process in strain SO3."` (`CommunityMech:000527`, `CommunityMech:000528`, `CommunityMech:000385`) | 10 $\rightarrow$ **11** |
| `kb/taxa/Geobacter_sulfurreducens.yaml` (`CommunityMech:taxon:000002`, `NCBITaxon:35554`) | `omcS` (`GSU2504`) | `UniProtKB:Q749X9` | `GCF_000007985.2` | `PMID:40845095` (`SUPPORT`, `IN_VITRO`) | `"In model electroactive bacteria such as Geobacter and Shewanella, cytochromes such as PpcA, OmcS, OmcZ, MtrA, and MtrC exhibit redox-active windows spanning several hundred millivolts ( Fig. 4, A and B ), enabling them to transfer electrons to acceptors with more negative midpoint potentials, such as anthraquinone-2,6-disulfonate (AQDS; −186 mV) and flavins (−210 mV) ( 52 – 57 )."` (`CommunityMech:000134`, `CommunityMech:000276`) | 9 $\rightarrow$ **10** |
| `kb/taxa/Geobacter_sulfurreducens.yaml` (`CommunityMech:taxon:000002`, `NCBITaxon:35554`) | `omcB` (`GSU2737`) | `UniProtKB:Q74A86` | `GCF_000007985.2` | `PMID:41876513` (`SUPPORT`, `COMPUTATIONAL`) | `"c Maximum likelihood phylogeny of OmcB amino acid sequences from representative Geobacterales. The tree was inferred using RAxML-HPC2 on the CIPRES Science Gateway, based on protein alignments (1323 aligned amino acids) using the PROTCAT + DAYHOFF model with 100 bootstrap replicates."` (`CommunityMech:000349`) | 6 $\rightarrow$ **7** |

### Complete `CommonTaxon` Gene & Protein Inventory After Cycle 13 Stage 3

| CommonTaxon Record | `gene_symbol` | `gene_id` | `locus_tag` | `genome` | `EvidenceItem` Count | Cited References |
|---|---|---|---|---|---:|---|
| `kb/taxa/Shewanella_oneidensis_MR1.yaml` | `mtrC` | `UniProtKB:Q8EG33` | `SO_1778` | `GCF_000146165.2` | **11** | `PMID:42733304` (7), `PMID:41236292` (1), `PMID:39504696` (1), `PMID:31537786` (1), `PMID:40845095` (1) |
| `kb/taxa/Shewanella_oneidensis_MR1.yaml` | `mtrB` | `UniProtKB:Q8EG34` | `SO_1776` | `GCF_000146165.2` | **5** | `PMID:42733304` (1), `PMID:41210787` (1), `PMID:31537786` (1), `PMID:32849356` (1), `PMID:34986141` (1) |
| `kb/taxa/Shewanella_oneidensis_MR1.yaml` | `mtrA` | `UniProtKB:Q8EG35` | `SO_1777` | `GCF_000146165.2` | **6** | `PMID:42733304` (1), `PMID:41210787` (1), `PMID:31537786` (1), `PMID:32849356` (2), `PMID:40845095` (1) |
| `kb/taxa/Shewanella_oneidensis_MR1.yaml` | `omcA` | `UniProtKB:Q8EG32` | `SO_1779` | `GCF_000146165.2` | **11** | `PMID:42733304` (8), `PMID:41236292` (1), `PMID:39504696` (1), `PMID:31537786` (1) |
| `kb/taxa/Shewanella_oneidensis_MR1.yaml` | `cymA` | `UniProtKB:Q8E945` | `SO_4591` | `GCF_000146165.2` | **6** | `PMID:42733304` (1), `PMID:39504696` (1), `PMID:31537786` (1), `PMID:34986141` (2), `PMID:37747940` (1) |
| `kb/taxa/Geobacter_sulfurreducens.yaml` | `pilA` | `UniProtKB:Q74BW5` | `GSU1496` | `GCF_000007985.2` | **8** | `PMID:41210787` (2), `PMID:37650614` (1), `PMID:41236292` (1), `PMID:28287150` (1), `PMID:32265334` (1), `PMID:41876513` (2) |
| `kb/taxa/Geobacter_sulfurreducens.yaml` | `omcS` | `UniProtKB:Q749X9` | `GSU2504` | `GCF_000007985.2` | **10** | `PMID:41210787` (1), `PMID:37650614` (1), `PMID:28992596` (1), `PMID:41236292` (1), `PMID:31537786` (1), `PMID:32849356` (2), `PMID:34986141` (1), `PMID:37747940` (1), `PMID:40845095` (1) |
| `kb/taxa/Geobacter_sulfurreducens.yaml` | `omcZ` | `UniProtKB:Q74A90` | `GSU2076` | `GCF_000007985.2` | **6** | `PMID:41210787` (1), `PMID:28992596` (1), `PMID:34986141` (3), `PMID:40845095` (1) |
| `kb/taxa/Geobacter_sulfurreducens.yaml` | `omcB` | `UniProtKB:Q74A86` | `GSU2737` | `GCF_000007985.2` | **7** | `PMID:41876513` (5), `PMID:37650614` (1), `PMID:37747940` (1) |

### `CommonTaxon` SHA-256 Provenance Chain Across Cycles 11–13

| CommonTaxon Record | Cycle 11 Stage 3 SHA-256 | Cycle 12 Stage 3 SHA-256 | Cycle 13 Stage 3 SHA-256 |
|---|---|---|---|
| `kb/taxa/Shewanella_oneidensis_MR1.yaml` (`CommunityMech:taxon:000001`) | `3bb69ddaa4d9064fe6340d04dff7bd9bac375fb08495580e369ba239b71bdd75` | `5666e10e654de62d43df48c97be2215b1b24e7c94b471b3ece95bb248b7f41f5` | `5994b4b237f3d87d16dcbb47edfd6a9fa88fc3898100457ce39036e712cccdf6` |
| `kb/taxa/Geobacter_sulfurreducens.yaml` (`CommunityMech:taxon:000002`) | `ab3bcd9639241391f25a20b5bbdb3a40ee6e907d441f696355ce16745e3c4b92` | `aeddfc60dfc34c721e1b2355aeddcd1b809da8196e449d360ce509f0af0c76dc` | `413329d881e1bcfcf692ffcd76a3839d183e9abd64952703233f6e786b918d7e` |

---

## 4. Documented Representation, Writer, and Offline-Proteome Boundaries

1. **Schema Representation Boundary on `EcologicalInteraction` and `InteractionDownstream`**:
   - In `src/communitymech/schema/communitymech.yaml`, `GeneAnnotation` (with `gene_id` `UniProtKB:...`) lives exclusively on `CommonTaxon.genes` (`kb/taxa/*.yaml`), linked from `MicrobialCommunity` via `TaxonomicComposition.common_taxon`.
   - `EcologicalInteraction` and `InteractionDownstream` do not define an `associated_genes` or `proteins` slot, so interaction-level protein participation is represented via `GeneAnnotation.supports_interaction` and `GeneAnnotation.supports_roles` on the linked `CommonTaxon` record.
2. **Offline Proteome Mapping Boundary (`Cohort 4`, 24 records)**:
   - `scripts/build_sequence_map.py` requires live network queries (`--email` for NCBI Entrez and UniProt REST APIs), which are prohibited during offline curation runs (`AGENTS.md`).
   - No local offline UniProt reference-proteome mapping table (`data/raw/`) is committed for the 24 Cohort 4 records (including Cycle 13 additions `CommunityMech:000539`, `000540`, and `000541`). Per `.claude/skills/add-uniprot-protein-examples/SKILL.md`, `UniProtKB:` accessions are never guessed from memory.
3. **Append-Only Provenance**:
   - Curation events and `HistoryRecord` sidecars were recorded at `history/records/Shewanella_oneidensis_MR1/2026-11-09T214500Z-antigravity-c13s301.yaml` and `history/records/Geobacter_sulfurreducens/2026-11-09T214500Z-antigravity-c13s302.yaml`.
