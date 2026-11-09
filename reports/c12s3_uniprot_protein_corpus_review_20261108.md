# Cycle 12 Stage 3 (`protein_examples`) Corpus Review & UniProt Protein Curation Report

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle / Stage**: Cycle 12, Stage 3 (`protein_examples`)
- **Date**: 2026-11-08
- **Base Commit (`main`)**: `2f37c20ed1f01e78741d590aacff3c75d31fed8a`
- **Skills Followed**:
  - `.claude/skills/add-uniprot-protein-examples/SKILL.md`
  - `.claude/skills/curate-yaml-record/SKILL.md`
  - `.claude/skills/communitymech-evolve-workflow/SKILL.md`

---

## 1. Corpus Scope & Applicability Accounting (`531` Total Records)

All **531** canonical YAML records across the three repository record roots were audited at commit `2f37c20ed1f01e78741d590aacff3c75d31fed8a`:

| Record Root | Root Class | Record Count | UniProtKB / `CommonTaxon` Status |
|---|---|---:|---|
| `kb/taxa/*.yaml` | `CommonTaxon` | **2** | **9** verified `UniProtKB:` `GeneAnnotation` entries (**66** total cached `EvidenceItem`s after Cycle 12 Stage 3; up from **61** after Cycle 11 Stage 3, with `>= 5` verified `EvidenceItem`s on every gene) |
| `kb/communities/*.yaml` | `MicrobialCommunity` | **511** | **20** records linked via `taxonomy[].common_taxon` to `kb/taxa/*.yaml` (`15` to `CommunityMech:taxon:000001`; `6` to `CommunityMech:taxon:000002`; `1` overlap on `CommunityMech:000177`) |
| `data/isolates/*.yaml` | `MicrobialCommunity` | **18** | **1** isolate baseline (`CommunityMech:000524`) linked via `taxonomy[].common_taxon: CommunityMech:taxon:000001` to `kb/taxa/Shewanella_oneidensis_MR1.yaml`; **17** single-strain isolate baselines (including newly added `CommunityMech:000531`–`000534`) without endogenous sequenced-strain `UniProtKB:` protein accessions in cached sources |
| **Total** | — | **531** | **2** `CommonTaxon` records + **529** `MicrobialCommunity` records |

### Partition of the `529` `MicrobialCommunity` Records (`kb/communities/` + `data/isolates/`)

1. **Linked to reusable `CommonTaxon` records (`kb/taxa/*.yaml`) with verified `UniProtKB:` protein annotations (`21` records: `20` in `kb/communities/` + `1` in `data/isolates/`)**:
   - **`CommunityMech:taxon:000001` (`kb/taxa/Shewanella_oneidensis_MR1.yaml`, `NCBITaxon:211586`, `GCF_000146165.2`) — `16` records (`15` communities + `1` isolate baseline)**:
     - `CommunityMech:000177` (`kb/communities/Shewanella_Geobacter_Exoelectrogenic_Biofilm_Community.yaml`)
     - `CommunityMech:000203` (`kb/communities/Shewanella_Streptococcus_Starch_Microbial_Fuel_Cell.yaml`)
     - `CommunityMech:000211` (`kb/communities/Synechococcus_Shewanella_Dlactate_Biophotovoltaic_Consortium.yaml`)
     - `CommunityMech:000279` (`kb/communities/Shewanella_oneidensis_Rhodopseudomonas_palustris_Electrosyntrophic_Coculture.yaml`)
     - `CommunityMech:000288` (`kb/communities/Shewanella_Pseudomonas_Fe0_Electrosyntrophic_Denitrifying_Consortium.yaml`)
     - `CommunityMech:000294` (`kb/communities/Corynebacterium_glutamicum_Shewanella_oneidensis_Succinic_Acid_Coculture.yaml`)
     - `CommunityMech:000298` (`kb/communities/Electrosynthetic_Consortia_Shewanella_Clostridium_Acetobacterium_Acetate.yaml`)
     - `CommunityMech:000385` (`kb/communities/SO3_BS3_Lithium_Battery_Bioleaching_Consortium.yaml`)
     - `CommunityMech:000402` (`kb/communities/Shewanella_Anammox_Delta_nrfA_Nitrite_Coupled_Consortium.yaml`)
     - `CommunityMech:000519` (`kb/communities/SO1_BS1_Lithium_Battery_Bioleaching_Consortium.yaml`)
     - `CommunityMech:000520` (`kb/communities/SO2_BS2_Lithium_Battery_Bioleaching_Consortium.yaml`)
     - `CommunityMech:000523` (`kb/communities/SO2_BS1_Lithium_Battery_Bioleaching_Consortium.yaml`)
     - `CommunityMech:000524` (`data/isolates/Shewanella_Oneidensis_SO1_NCM_Bioleaching_Isolate_Baseline.yaml`)
     - `CommunityMech:000526` (`kb/communities/SO3_DeltaMtrC_BS3_Lithium_Battery_Bioleaching_Consortium.yaml`)
     - `CommunityMech:000527` (`kb/communities/SO3_DeltaOmcA_BS3_Lithium_Battery_Bioleaching_Consortium.yaml`)
     - `CommunityMech:000528` (`kb/communities/SO3_DeltaMtrC_DeltaOmcA_BS3_Lithium_Battery_Bioleaching_Consortium.yaml`)
   - **`CommunityMech:taxon:000002` (`kb/taxa/Geobacter_sulfurreducens.yaml`, `NCBITaxon:35554`, `GCF_000007985.2`) — `6` records**:
     - `CommunityMech:000031` (`kb/communities/Geobacter_Clostridium_Interspecies_Electron_Transfer_Coculture.yaml`)
     - `CommunityMech:000175` (`kb/communities/Clostridium_Cellulolyticum_Geobacter_Cellulose_MFC_Coculture.yaml`)
     - `CommunityMech:000176` (`kb/communities/ORNL_Clostridium_Desulfovibrio_Geobacter_Trophic_Model.yaml`)
     - `CommunityMech:000177` (`kb/communities/Shewanella_Geobacter_Exoelectrogenic_Biofilm_Community.yaml`)
     - `CommunityMech:000201` (`kb/communities/Geobacter_Pseudomonas_Formate_Fumarate_Electroactive_Coculture.yaml`)
     - `CommunityMech:000268` (`kb/communities/Rhodopseudomonas_Geobacter_Magnetite_Redox_Coculture.yaml`)
   - *Overlap*: `CommunityMech:000177` references both `CommunityMech:taxon:000001` and `CommunityMech:taxon:000002` (`16 + 6 - 1 = 21` distinct `MicrobialCommunity` records).

2. **16S amplicon / metagenomic / phylum-, family-, or genus-rank guild or unsequenced environmental isolate communities (`352` records)**:
   - Taxa are resolved at genus, family, order, phylum, or unsequenced environmental isolate rank without an exact sequenced strain proteome (`GCF_`/`GCA_`). Under `.claude/skills/add-uniprot-protein-examples/SKILL.md` ("Prefer an exact assayed protein over a convenient ortholog. A named gene alone is not a unique protein match"), assigning a reference-strain `UniProtKB:` accession would violate organism- and sequence-scope rules.

3. **Defined / species-grounded communities and isolate baselines whose cached sources assay metabolites, fermentation kinetics, or growth yields without naming specific endogenous protein accessions or sequenced isolate proteomes (`135` records: `118` in `kb/communities/` + `17` in `data/isolates/`)**:
   - Increased from `131` in Cycle 11 Stage 3 to `135` in Cycle 12 Stage 3 due to the addition of four single-strain isolate baselines in Cycle 12 Stage 1:
     - `CommunityMech:000531` (`data/isolates/Microbacterium_BR1_Sulfadiazine_Cleaving_Isolate_Baseline.yaml`)
     - `CommunityMech:000532` (`data/isolates/Terrabacter_2APm3_Sulfadiazine_Isolate_Baseline.yaml`)
     - `CommunityMech:000533` (`data/isolates/Achromobacter_SL8_Cadmium_Immobilization_Isolate_Baseline.yaml`)
     - `CommunityMech:000534` (`data/isolates/Enterobacter_SL12_Cadmium_Immobilization_Isolate_Baseline.yaml`)

4. **Species- / strain-grounded communities whose cached sources name gene symbols or locus tags (`narG`, `nirK`, `nosZ`, `mcrA`, `acsB`, `fhs`, `nifH`, `amoA`, `hao`, `nxrB`, `dsrAB`, `hydA`, `fldA`/`fmnA`/`dmkA`, `nqrF`, `tauD`, `iscS`, `tenA`, `STR3`/`LEU2`) without a local offline `UniProtKB:` mapping table or without `CommonTaxon` promotion (`21` records)**:
   - Increased from `20` in Cycle 11 Stage 3 to `21` in Cycle 12 Stage 3 due to the addition of `CommunityMech:000535` (`kb/communities/Ogataea_Str3_Leu2_Auxotrophic_CrossFeeding_Coculture.yaml`), whose primary source (`PMID:42318495`) names the *Ogataea polymorpha* (`NCBITaxon:460523`, strain `JQcr03L`) gene symbols `STR3` (cystathionine beta-lyase) and `LEU2` (3-isopropylmalate dehydrogenase) without reporting locus tags, RefSeq genome assemblies (`GCF_`), or `UniProtKB:` accessions in cached text.

---

## 2. Detailed Audit of Cycle 12 Stage 1 Additions (`CommunityMech:000531` – `CommunityMech:000535`)

| Record ID | File Path | Pre-Stage-3 / Post-Stage-3 SHA-256 | Primary Reference | Taxa & Grounding | Stage 3 Protein / `CommonTaxon` Audit |
|---|---|---|---|---|---|
| `CommunityMech:000531` | `data/isolates/Microbacterium_BR1_Sulfadiazine_Cleaving_Isolate_Baseline.yaml` | `c0326c5cdaf678c922659c33dbe4fe1b5717be2bf79dab54d672f160574c0fe5` (unchanged) | `PMID:42598292` (`references_cache/PMID_42598292.txt`, abstract + full text cached) | *Microbacterium* sp. BR1 (`NCBITaxon:1070896`, `GTDB:s__Microbacterium_lacus`) | **Inapplicable (defined strain baseline assaying HPLC metabolite kinetics, flow cytometry, and Raman-SIP without gene/protein identifiers in source)**: `PMID:42598292` characterizes *Microbacterium* sp. BR1 via HPLC sulfadiazine (`CHEBI:10223`) and 2-aminopyrimidine (`2-AP`, `CHEBI:38331`) quantification, flow-cytometric cell counts, and 13C/15N single-cell Raman microspectroscopy without naming any specific catabolic genes, locus tags, or `UniProtKB:` protein accessions in the cached text. |
| `CommunityMech:000532` | `data/isolates/Terrabacter_2APm3_Sulfadiazine_Isolate_Baseline.yaml` | `81c8fd983bc57050595d7a4d51b64acdf2617ce9fea0f03f7ec9db4fa617c05e` (unchanged) | `PMID:42598292` (`references_cache/PMID_42598292.txt`, abstract + full text cached) | *Terrabacter* sp. 2APm3 (`DSMZ 28514`, `NCBITaxon:1472881`, `GTDB:g__Terrabacter`) | **Inapplicable (defined strain baseline assaying HPLC metabolite kinetics, flow cytometry, and Raman-SIP without gene/protein identifiers in source)**: `PMID:42598292` characterizes *Terrabacter* sp. 2APm3 via HPLC sulfadiazine/2-AP quantification, flow-cytometric cell counts, and 13C/15N single-cell Raman-SIP without naming catabolic enzymes, locus tags, genome assemblies (`GCF_`), or `UniProtKB:` protein accessions (explicitly documented in `discussions[0].discussion_id: terrabacter_2apm3_enzymatic_pathway_for_2ap_ring_cleavage`). |
| `CommunityMech:000533` | `data/isolates/Achromobacter_SL8_Cadmium_Immobilization_Isolate_Baseline.yaml` | `0680fbc0c1ee94f3a79ce13d9c6b3d8b91317022addca4c095195a37974b6d0e` (unchanged) | `PMID:42307251` (`references_cache/PMID_42307251.txt`, abstract + full text cached) | *Achromobacter* sp. SL8 (`NCBITaxon:222`, `GTDB:g__Achromobacter`, 16S rRNA GenBank `PZ429300`) | **Inapplicable (16S-identified genus-rank environmental isolate without sequenced isolate genome assembly or UniProtKB accessions in cached text)**: *Achromobacter* sp. SL8 is identified by partial 16S rRNA sequence (`PZ429300`, 99.79% homology); while Group A label-free proteomics is deposited in iProX (`IPX0017179000`), `PMID:42307251` reports KEGG pathway enrichments, FTIR N-H coordination, TEM morphology, and Cd removal kinetics without isolate genome assemblies (`GCF_`) or `UniProtKB:` protein accessions in the cached article text. |
| `CommunityMech:000534` | `data/isolates/Enterobacter_SL12_Cadmium_Immobilization_Isolate_Baseline.yaml` | `68a2f6ea9b523e7db0eacf6ef1a87af5227cd3f6c7e93be14facffc265232796` (unchanged) | `PMID:42307251` (`references_cache/PMID_42307251.txt`, abstract + full text cached) | *Enterobacter* sp. SL12 (`NCBITaxon:547`, `GTDB:g__Enterobacter`, 16S rRNA GenBank `PZ429301`) | **Inapplicable (16S-identified genus-rank environmental isolate without sequenced isolate genome assembly or UniProtKB accessions in cached text)**: *Enterobacter* sp. SL12 is identified by partial 16S rRNA sequence (`PZ429301`, 99.31% homology); Group B label-free proteomics is deposited in iProX (`IPX0017179000`), but `PMID:42307251` reports no isolate genome assembly (`GCF_`) or `UniProtKB:` protein accessions in the cached article text. |
| `CommunityMech:000535` | `kb/communities/Ogataea_Str3_Leu2_Auxotrophic_CrossFeeding_Coculture.yaml` | `be16aa69ef1611a0d1d452da9e20ccea58a5497d912ce167819f706fdb57a401` (unchanged) | `PMID:42318495` (`references_cache/PMID_42318495.txt`, abstract + full text cached) | *Ogataea polymorpha* (`NCBITaxon:460523`, strains `JQcr03L(Δstr3,LEU2)` and `JQcr03L(STR3,Δleu2)`) | **Offline-Proteome-Mapping-Limited (Cohort 4)**: `PMID:42318495` names the *Ogataea polymorpha* (`NCBITaxon:460523`, background `JQcr03L` derived from NCYC 495) gene symbols `STR3` (cystathionine beta-lyase in the sulfur assimilation pathway), `LEU2` (leucine biosynthesis), `URA3`, `MET10`, `MET14`, and `MET3`, but does not report locus tags, RefSeq genome assembly accessions (`GCF_`), or `UniProtKB:` protein accessions in the cached text, and no offline *Ogataea polymorpha* UniProtKB proteome table is committed in the repository. |

---

## 3. Verified `CommonTaxon` Updates in Cycle 12 Stage 3 (`61 -> 66` Gene-Level `EvidenceItem`s)

### 3.1 `kb/taxa/Shewanella_oneidensis_MR1.yaml` (`CommunityMech:taxon:000001`)

- **Pre-Stage-3 SHA-256**: `3bb69ddaa4d9064fe6340d04dff7bd9bac375fb08495580e369ba239b71bdd75`
- **Post-Stage-3 SHA-256**: `5666e10e654de62d43df48c97be2215b1b24e7c94b471b3ece95bb248b7f41f5`
- **History Sidecar**: `history/records/Shewanella_oneidensis_MR1/2026-11-09T021000Z-antigravity-c12s301.yaml`
- **Total Gene-Level `EvidenceItem`s**: `34 -> 37` (`5` curated `UniProtKB:` genes: `mtrC` `10`, `mtrB` `5`, `mtrA` `6`, `omcA` `10`, `cymA` `6`)
- **Added `EvidenceItem`s (`+3`)**:
  1. **`mtrB` (`UniProtKB:Q8EG34`, locus tag `SO_1776`, `GCF_000146165.2`) — `EvidenceItem` #5**:
     - `reference`: `PMID:34986141` (`references_cache/PMID_34986141.md`, primary reference for `CommunityMech:000134`)
     - `supports`: `SUPPORT`
     - `evidence_source`: `COMPUTATIONAL`
     - `snippet`: `"(A) EET systems in gram-negative bacteria involve membrane-bound quinol:cytochrome c oxidoreductases (CbcL, ImcH, CymA, NetD), small soluble cytochromes apparently involved in electron transport through the periplasmic space (PpcA, Stc, PdsA), and a beta-barrel/decaheme cytochrome c protein complex (MtrCAB) that acts as an electron conduit by which electrons can transit through the outer membrane to the extracellular space filled with additional cytochrome c such as OmcZ and filaments of OmcS."`
  2. **`mtrA` (`UniProtKB:Q8EG35`, locus tag `SO_1777`, `GCF_000146165.2`) — `EvidenceItem` #6**:
     - `reference`: `PMID:40845095` (`references_cache/PMID_40845095.md`, cited in `CommunityMech:000134` and `CommunityMech:000276`)
     - `supports`: `SUPPORT`
     - `evidence_source`: `IN_VITRO`
     - `snippet`: `"In model electroactive bacteria such as Geobacter and Shewanella, cytochromes such as PpcA, OmcS, OmcZ, MtrA, and MtrC exhibit redox-active windows spanning several hundred millivolts ( Fig. 4, A and B ), enabling them to transfer electrons to acceptors with more negative midpoint potentials, such as anthraquinone-2,6-disulfonate (AQDS; −186 mV) and flavins (−210 mV) ( 52 – 57 )."`
  3. **`cymA` (`UniProtKB:Q8E945`, locus tag `SO_4591`, `GCF_000146165.2`) — `EvidenceItem` #6**:
     - `reference`: `PMID:37747940` (`references_cache/PMID_37747940.md`, cited in `CommunityMech:000134` and `CommunityMech:000276`)
     - `supports`: `SUPPORT`
     - `evidence_source`: `COMPUTATIONAL`
     - `snippet`: `"(A) The presence of CymA, CbcL, CbcAB, and NetBCD, commonly used electron donors to the EET conduits in Shewanella and Geobacter are mapped on to the classes Thermodesulfobacteria and Desulfobulbia."`

### 3.2 `kb/taxa/Geobacter_sulfurreducens.yaml` (`CommunityMech:taxon:000002`)

- **Pre-Stage-3 SHA-256**: `ab3bcd9639241391f25a20b5bbdb3a40ee6e907d441f696355ce16745e3c4b92`
- **Post-Stage-3 SHA-256**: `08edb6b5409c2b77ab7ddfdb32f85fdf3292674c9333263b4271985f0be2ca78`
- **History Sidecar**: `history/records/Geobacter_sulfurreducens/2026-11-09T021000Z-antigravity-c12s302.yaml`
- **Total Gene-Level `EvidenceItem`s**: `27 -> 29` (`4` curated `UniProtKB:` genes: `pilA` `8`, `omcS` `9`, `omcZ` `6`, `omcB` `6`)
- **Added `EvidenceItem`s (`+2`)**:
  1. **`omcZ` (`UniProtKB:Q74A90`, locus tag `GSU2076`, `GCF_000007985.2`) — `EvidenceItem` #6**:
     - `reference`: `PMID:40845095` (`references_cache/PMID_40845095.md`, cited in `CommunityMech:000134` and `CommunityMech:000276`)
     - `supports`: `SUPPORT`
     - `evidence_source`: `IN_VITRO`
     - `snippet`: `"In model electroactive bacteria such as Geobacter and Shewanella, cytochromes such as PpcA, OmcS, OmcZ, MtrA, and MtrC exhibit redox-active windows spanning several hundred millivolts ( Fig. 4, A and B ), enabling them to transfer electrons to acceptors with more negative midpoint potentials, such as anthraquinone-2,6-disulfonate (AQDS; −186 mV) and flavins (−210 mV) ( 52 – 57 )."`
  2. **`omcB` (`UniProtKB:Q74A86`, locus tag `GSU2737`, `GCF_000007985.2`) — `EvidenceItem` #6**:
     - `reference`: `PMID:41876513` (`references_cache/PMID_41876513.txt`, primary reference for `CommunityMech:000462`)
     - `supports`: `SUPPORT`
     - `evidence_source`: `COMPUTATIONAL`
     - `snippet`: `"To determine OmcB evolutionary relationships, the Ca. Geosyntrophus OmcB sequence was used as a BLASTP query to identify homologs from related species."`

---

## 4. Representation & Offline Verification Boundaries

1. **No schema or writer blockers for `CommonTaxon` (`kb/taxa/*.yaml`)**:
   - `write_validated_community(doc, path, target_class="CommonTaxon")` in `src/communitymech/validation/write_validated.py` validates `CommonTaxon` records in-memory against `src/communitymech/schema/communitymech.yaml` before writing and passes `scripts/audit_writers.py`.
2. **Offline UniProtKB verification boundary for the `21` gene-symbol-bearing community records**:
   - Under `AGENTS.md` ("Do not make network calls, spend provider credits, or apply generated curation unless the task authorizes it") and `.claude/skills/add-uniprot-protein-examples/SKILL.md` ("Inspect live UniProt entry metadata or a release-pinned, provenance-verifiable native snapshot... A named gene alone is not a unique protein match"), no unverified `UniProtKB:` accessions were guessed for taxa lacking a local offline UniProt proteome table in the repository.
