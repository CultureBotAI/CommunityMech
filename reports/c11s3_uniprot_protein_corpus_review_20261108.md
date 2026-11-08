# Cycle 11 Stage 3 (`protein_examples`) Corpus Review & UniProt Protein Curation Report

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle / Stage**: Cycle 11, Stage 3 (`protein_examples`)
- **Date**: 2026-11-08
- **Base Commit (`main`)**: `81009d54bf25de2100264e03733f9620110c0b60`
- **Skills Followed**:
  - `.claude/skills/add-uniprot-protein-examples/SKILL.md`
  - `.claude/skills/curate-yaml-record/SKILL.md`
  - `.claude/skills/communitymech-evolve-workflow/SKILL.md`

---

## 1. Corpus Scope & Applicability Accounting (`526` Total Records)

All **526** canonical YAML records across the three repository record roots were audited at commit `81009d54bf25de2100264e03733f9620110c0b60`:

| Record Root | Root Class | Record Count | UniProtKB / `CommonTaxon` Status |
|---|---|---:|---|
| `kb/taxa/*.yaml` | `CommonTaxon` | **2** | **9** verified `UniProtKB:` `GeneAnnotation` entries (**61** total cached `EvidenceItem`s after Cycle 11 Stage 3; up from **55** after Cycle 10 Stage 3) |
| `kb/communities/*.yaml` | `MicrobialCommunity` | **510** | **20** records linked via `taxonomy[].common_taxon` to `kb/taxa/*.yaml` (`15` to `CommunityMech:taxon:000001` including newly added `CommunityMech:000526`, `CommunityMech:000527`, `CommunityMech:000528`; `6` to `CommunityMech:taxon:000002`; `1` overlap on `CommunityMech:000177`) |
| `data/isolates/*.yaml` | `MicrobialCommunity` | **14** | **1** isolate baseline (`CommunityMech:000524`) linked via `taxonomy[].common_taxon: CommunityMech:taxon:000001` to `kb/taxa/Shewanella_oneidensis_MR1.yaml`; **13** single-strain isolate baselines (including newly added `CommunityMech:000529` and `CommunityMech:000530`) without endogenous sequenced-strain `UniProtKB:` protein accessions in cached sources |
| **Total** | — | **526** | **2** `CommonTaxon` records + **524** `MicrobialCommunity` records |

### Partition of the `524` `MicrobialCommunity` Records (`kb/communities/` + `data/isolates/`)

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
     - `CommunityMech:000526` (`kb/communities/SO3_DeltaMtrC_BS3_Lithium_Battery_Bioleaching_Consortium.yaml`) — **added in Cycle 11 Stage 1**
     - `CommunityMech:000527` (`kb/communities/SO3_DeltaOmcA_BS3_Lithium_Battery_Bioleaching_Consortium.yaml`) — **added in Cycle 11 Stage 1**
     - `CommunityMech:000528` (`kb/communities/SO3_DeltaMtrC_DeltaOmcA_BS3_Lithium_Battery_Bioleaching_Consortium.yaml`) — **added in Cycle 11 Stage 1**
   - **`CommunityMech:taxon:000002` (`kb/taxa/Geobacter_sulfurreducens.yaml`, `NCBITaxon:35554`, `GCF_000007985.2`) — `6` records**:
     - `CommunityMech:000031` (`kb/communities/Geobacter_Clostridium_Interspecies_Electron_Transfer_Coculture.yaml`)
     - `CommunityMech:000175` (`kb/communities/Clostridium_Cellulolyticum_Geobacter_Cellulose_MFC_Coculture.yaml`)
     - `CommunityMech:000176` (`kb/communities/ORNL_Clostridium_Desulfovibrio_Geobacter_Trophic_Model.yaml`)
     - `CommunityMech:000177` (`kb/communities/Shewanella_Geobacter_Exoelectrogenic_Biofilm_Community.yaml`)
     - `CommunityMech:000201` (`kb/communities/Geobacter_Pseudomonas_Formate_Fumarate_Electroactive_Coculture.yaml`)
     - `CommunityMech:000268` (`kb/communities/Rhodopseudomonas_Geobacter_Magnetite_Redox_Coculture.yaml`)
   - *Overlap*: `CommunityMech:000177` references both `CommunityMech:taxon:000001` and `CommunityMech:taxon:000002` (`16 + 6 - 1 = 21` distinct `MicrobialCommunity` records).

2. **16S amplicon / metagenomic / phylum-, family-, or genus-rank guild or unsequenced environmental isolate communities (`352` records)**:
   - Taxa are resolved at genus, family, order, phylum, or unsequenced environmental isolate rank without an exact sequenced strain proteome (`GCF_`/`GCA_`). Under `.claude/skills/add-uniprot-protein-examples/SKILL.md` ("Only attach a UniProt accession when the organism and gene context match the record"), assigning a reference-strain UniProtKB accession would violate organism- and sequence-scope rules.

3. **Defined / species-grounded communities and isolate baselines whose cached sources assay metabolites, fermentation kinetics, or growth yields without naming specific endogenous protein accessions or sequenced isolate proteomes (`131` records: `118` in `kb/communities/` + `13` in `data/isolates/`)**:
   - Increased from `129` in Cycle 10 Stage 3 to `131` in Cycle 11 Stage 3 due to the addition of the two single-strain *Bacillus subtilis* 168 isolate baselines `CommunityMech:000529` (`data/isolates/Bacillus_Subtilis_BS3_Brewing_Wastewater_Isolate_Baseline.yaml`) and `CommunityMech:000530` (`data/isolates/Bacillus_Subtilis_BS0_Brewing_Wastewater_Isolate_Baseline.yaml`) in Cycle 11 Stage 1.

4. **Species- / strain-grounded communities whose cached sources name gene symbols or locus tags (`narG`, `nirK`, `nosZ`, `mcrA`, `acsB`, `fhs`, `nifH`, `amoA`, `hao`, `nxrB`, `dsrAB`, `hydA`, `fldA`/`fmnA`/`dmkA`, `nqrF`, `tauD`, `iscS`, `tenA`) without a local offline `UniProtKB:` mapping table or without `CommonTaxon` promotion (`20` records)**:
   - Documented in Section 4 below as offline-proteome/reference-cache scope boundaries.

---

## 2. Detailed Audit of Cycle 11 Stage 1 Additions (`CommunityMech:000526` – `CommunityMech:000530`)

| Record ID | File Path | Pre-Stage-3 / Post-Stage-3 SHA-256 | Primary Reference | Taxa & Grounding | Stage 3 Protein / `CommonTaxon` Audit |
|---|---|---|---|---|---|
| `CommunityMech:000526` | `kb/communities/SO3_DeltaMtrC_BS3_Lithium_Battery_Bioleaching_Consortium.yaml` | `8ce45b8ea2b6e7f966aecf7b30e8508aa427316ac92c53ab788e858a708ea968` (unchanged) | `PMID:42733304` (`references_cache/PMID_42733304.txt`, abstract + full text cached) | *Shewanella oneidensis* (`NCBITaxon:70863`, preferred term *Shewanella oneidensis* MR-1 `SO3ΔmtrC`, linked via `common_taxon: CommunityMech:taxon:000001` to `NCBITaxon:211586`, `GCF_000146165.2`), *Bacillus subtilis* (`NCBITaxon:1423`, strain `BS3`) | **Linked to `CommunityMech:taxon:000001` (`kb/taxa/Shewanella_oneidensis_MR1.yaml`)**: `SO3ΔmtrC` carries a targeted deletion of `mtrC` (`SO_1778`, `UniProtKB:Q8EG33`) in wild-type *S. oneidensis* MR-1 (`GCF_000146165.2`) transformed with `pHG13-Ptac-ribADEHC-irrE`, causing a 9.50-fold drop in MFC power density (`47.67 mW m^-2`) and a 6.13-fold drop in 14-day NCM metal leaching (`16.7 mg L^-1`). Added verified Figure 5d NCM leaching perturbation `EvidenceItem`s on `mtrC` (`UniProtKB:Q8EG33`) and `omcA` (`UniProtKB:Q8EG32`) in `kb/taxa/Shewanella_oneidensis_MR1.yaml` and registered in `tests/test_taxon_records.py::test_community_links_common_taxon`. |
| `CommunityMech:000527` | `kb/communities/SO3_DeltaOmcA_BS3_Lithium_Battery_Bioleaching_Consortium.yaml` | `568d6b743edb421494036d68981dfb3c6a812d24992119d49f802fee5400aba7` (unchanged) | `PMID:42733304` (`references_cache/PMID_42733304.txt`, abstract + full text cached) | *Shewanella oneidensis* (`NCBITaxon:70863`, preferred term *Shewanella oneidensis* MR-1 `SO3ΔomcA`, linked via `common_taxon: CommunityMech:taxon:000001` to `NCBITaxon:211586`, `GCF_000146165.2`), *Bacillus subtilis* (`NCBITaxon:1423`, strain `BS3`) | **Linked to `CommunityMech:taxon:000001` (`kb/taxa/Shewanella_oneidensis_MR1.yaml`)**: `SO3ΔomcA` carries a targeted deletion of `omcA` (`SO_1779`, `UniProtKB:Q8EG32`) in wild-type *S. oneidensis* MR-1 (`GCF_000146165.2`) transformed with `pHG13-Ptac-ribADEHC-irrE`, causing a 9.05-fold drop in MFC power density (`50.01 mW m^-2`) and a 5.48-fold drop in 14-day NCM metal leaching (`18.7 mg L^-1`). Added verified Figure 5d NCM leaching perturbation `EvidenceItem`s on `omcA` (`UniProtKB:Q8EG32`) and `mtrC` (`UniProtKB:Q8EG33`) in `kb/taxa/Shewanella_oneidensis_MR1.yaml` and registered in `tests/test_taxon_records.py::test_community_links_common_taxon`. |
| `CommunityMech:000528` | `kb/communities/SO3_DeltaMtrC_DeltaOmcA_BS3_Lithium_Battery_Bioleaching_Consortium.yaml` | `c83966d6d3c59f5aa614dfe035ae3dc483531e2da8e08d4f886b11fa77984f43` (unchanged) | `PMID:42733304` (`references_cache/PMID_42733304.txt`, abstract + full text cached) | *Shewanella oneidensis* (`NCBITaxon:70863`, preferred term *Shewanella oneidensis* MR-1 `SO3ΔmtrCΔomcA`, linked via `common_taxon: CommunityMech:taxon:000001` to `NCBITaxon:211586`, `GCF_000146165.2`), *Bacillus subtilis* (`NCBITaxon:1423`, strain `BS3`) | **Linked to `CommunityMech:taxon:000001` (`kb/taxa/Shewanella_oneidensis_MR1.yaml`)**: `SO3ΔmtrCΔomcA` carries simultaneous deletions of `mtrC` (`SO_1778`, `UniProtKB:Q8EG33`) and `omcA` (`SO_1779`, `UniProtKB:Q8EG32`) in *S. oneidensis* MR-1 (`GCF_000146165.2`), reducing 14-day NCM metal leaching 7.64-fold to `13.4 mg L^-1` (indistinguishable from sole strain `BS3` at `13.4 mg L^-1`). Added verified Figure 5d `EvidenceItem`s on `mtrC` (`UniProtKB:Q8EG33`) and `omcA` (`UniProtKB:Q8EG32`) in `kb/taxa/Shewanella_oneidensis_MR1.yaml` and registered in `tests/test_taxon_records.py::test_community_links_common_taxon`. |
| `CommunityMech:000529` | `data/isolates/Bacillus_Subtilis_BS3_Brewing_Wastewater_Isolate_Baseline.yaml` | `42834ab5f80c67edd88527a323dfa94514b440d63891e4fd88790b50a230cf28` (unchanged) | `PMID:42733304` (`references_cache/PMID_42733304.txt`, abstract + full text cached) | *Bacillus subtilis* (`NCBITaxon:1423`, engineered strain `BS3` = `BS2` carrying heterologous `P43::irrE` from *Deinococcus radiodurans* R1 on plasmid `pCE2` in mutation-bred `BSG3` background with `P43::adh` from *S. cerevisiae* BY4341 and `aldH` from *Issatchenkia terricola* XJ-2) | **Inapplicable (heterologous *D. radiodurans* / yeast plasmid genes and uncharacterized mutation-bred `BSG3` background without locus tags or UniProtKB identifiers)**: `PMID:42733304` characterizes `BS3` via heterologous expression of *D. radiodurans* R1 `irrE` (with no `DR_` locus tag or sequence accession reported in `PMID:42733304` and *D. radiodurans* not a community member) and yeast `adh`/`aldH` in mutation-bred `BSG3` (`the genotype of which is still unknown` in Table 1), without endogenous *B. subtilis* 168 (`BSU_`) protein accessions. However, sole strain `BS3`'s 14-day NCM leaching benchmark (`13.4 mg L^-1`) is cited in the newly added `mtrC`/`omcA` `EvidenceItem`s on `kb/taxa/Shewanella_oneidensis_MR1.yaml`. |
| `CommunityMech:000530` | `data/isolates/Bacillus_Subtilis_BS0_Brewing_Wastewater_Isolate_Baseline.yaml` | `452de842b34bb5c9073f31331ddef8f120323f5a934257e9a9db1e5e8f043f43` (unchanged) | `PMID:42733304` (`references_cache/PMID_42733304.txt`, abstract + full text cached) | *Bacillus subtilis* (`NCBITaxon:1423`, wild-type strain `BS0` = *B. subtilis* 168 carrying empty vector `pCE2`, `Cmr`) | **Inapplicable (wild-type empty-vector growth and ethanol-removal control without gene or protein assertions)**: `PMID:42733304` assays `BS0` solely for 48 h cell growth (`OD600,max = 0.641`, Figure 2a) and basal residual ethanol removal (`35.6%`, lowering ethanol from `1.8%` to `1.16% v/v`, Figure 2b) in Moutai brewing wastewater without naming any endogenous *B. subtilis* 168 gene symbols, locus tags, or `UniProtKB:` protein accessions. |

---

## 3. Verified `CommonTaxon` Updates in Cycle 11 Stage 3 (`55 -> 61` Gene-Level `EvidenceItem`s)

### 3.1 `kb/taxa/Shewanella_oneidensis_MR1.yaml` (`CommunityMech:taxon:000001`)

- **Pre-Stage-3 SHA-256**: `c841f96e490b0406dbccd7bca516dd0aacb42c34cf5f6042e99740ebfe86d49e`
- **Post-Stage-3 SHA-256**: `3bb69ddaa4d9064fe6340d04dff7bd9bac375fb08495580e369ba239b71bdd75`
- **History Sidecar**: `history/records/Shewanella_oneidensis_MR1/2026-11-08T083200Z-antigravity-c11s301.yaml`
- **Total Gene-Level `EvidenceItem`s**: `30 -> 34` (`5` curated `UniProtKB:` genes: `mtrC` `10`, `mtrB` `4`, `mtrA` `5`, `omcA` `10`, `cymA` `5`)
- **Added `EvidenceItem`s (`+4`)**:
  1. **`mtrC` (`UniProtKB:Q8EG33`, locus tag `SO_1778`, `GCF_000146165.2`) — `EvidenceItem` #9**:
     - `reference`: `PMID:42733304` (`references_cache/PMID_42733304.txt`, abstract + full text cached)
     - `supports`: `SUPPORT`
     - `evidence_source`: `IN_VITRO`
     - `snippet`: `"Correspondingly, compared with the total leached metal ions catalyzed by the SO3‐BS3 microbial consortium (102.4 mg L−1), the contents of leached metal ions catalyzed by the SO3∆mtrC‐BS3 consortium (16.7 mg L−1), the SO3∆omcA‐BS3 microbial consortium (18.7 mg L−1), and the SO3∆mtrC∆omcA‐BS3 consortium (13.4 mg L−1) were dramatically decreased by 6.13‐, 5.48‐, and 7.64‐fold, respectively (Figure 5d )."`
  2. **`mtrC` (`UniProtKB:Q8EG33`, locus tag `SO_1778`, `GCF_000146165.2`) — `EvidenceItem` #10**:
     - `reference`: `PMID:42733304` (`references_cache/PMID_42733304.txt`, abstract + full text cached)
     - `supports`: `SUPPORT`
     - `evidence_source`: `IN_VITRO`
     - `snippet`: `"Notably, the leached metal ions catalyzed by the SO3∆mtrC∆omcA‐BS3 consortium (13.4 mg L−1) exhibited negligible difference from that catalyzed by the sole strain BS3 (13.4 mg L−1), suggesting that MtrC and OmcA in S. oneidensis were essential for NCM reduction in metal oxide leaching."`
  3. **`omcA` (`UniProtKB:Q8EG32`, locus tag `SO_1779`, `GCF_000146165.2`) — `EvidenceItem` #9**:
     - `reference`: `PMID:42733304` (`references_cache/PMID_42733304.txt`, abstract + full text cached)
     - `supports`: `SUPPORT`
     - `evidence_source`: `IN_VITRO`
     - `snippet`: `"Correspondingly, compared with the total leached metal ions catalyzed by the SO3‐BS3 microbial consortium (102.4 mg L−1), the contents of leached metal ions catalyzed by the SO3∆mtrC‐BS3 consortium (16.7 mg L−1), the SO3∆omcA‐BS3 microbial consortium (18.7 mg L−1), and the SO3∆mtrC∆omcA‐BS3 consortium (13.4 mg L−1) were dramatically decreased by 6.13‐, 5.48‐, and 7.64‐fold, respectively (Figure 5d )."`
  4. **`omcA` (`UniProtKB:Q8EG32`, locus tag `SO_1779`, `GCF_000146165.2`) — `EvidenceItem` #10**:
     - `reference`: `PMID:42733304` (`references_cache/PMID_42733304.txt`, abstract + full text cached)
     - `supports`: `SUPPORT`
     - `evidence_source`: `IN_VITRO`
     - `snippet`: `"Notably, the leached metal ions catalyzed by the SO3∆mtrC∆omcA‐BS3 consortium (13.4 mg L−1) exhibited negligible difference from that catalyzed by the sole strain BS3 (13.4 mg L−1), suggesting that MtrC and OmcA in S. oneidensis were essential for NCM reduction in metal oxide leaching."`

### 3.2 `kb/taxa/Geobacter_sulfurreducens.yaml` (`CommunityMech:taxon:000002`)

- **Pre-Stage-3 SHA-256**: `5acba5205a69a57fb7270a7e92e156ca3f26affd7035aaa8216bb29307b57aaf`
- **Post-Stage-3 SHA-256**: `ab3bcd9639241391f25a20b5bbdb3a40ee6e907d441f696355ce16745e3c4b92`
- **History Sidecar**: `history/records/Geobacter_sulfurreducens/2026-11-08T083200Z-antigravity-c11s302.yaml`
- **Total Gene-Level `EvidenceItem`s**: `25 -> 27` (`4` curated `UniProtKB:` genes: `pilA` `8`, `omcS` `9`, `omcZ` `5`, `omcB` `5`)
- **Added `EvidenceItem`s (`+2`)**:
  1. **`pilA` (`UniProtKB:Q74BW5`, locus tag `GSU1496`, `GCF_000007985.2`) — `EvidenceItem` #8**:
     - `reference`: `PMID:41876513` (`references_cache/PMID_41876513.txt`, primary reference for `CommunityMech:000462`)
     - `supports`: `PARTIAL`
     - `evidence_source`: `COMPUTATIONAL`
     - `snippet`: `"Also, deletion of the pilA gene abolished DIET between Geobacter and a type II Methanosarcina (M. acetivorans) and GAC could compensate for this loss suggesting that the role of pili in the interaction with GAC and the methanogenic partner is not crucial"`
  2. **`omcB` (`UniProtKB:Q74A86`, locus tag `GSU2737`, `GCF_000007985.2`) — `EvidenceItem` #5**:
     - `reference`: `PMID:41876513` (`references_cache/PMID_41876513.txt`, primary reference for `CommunityMech:000462`)
     - `supports`: `SUPPORT`
     - `evidence_source`: `COMPUTATIONAL`
     - `snippet`: `"Top OmcB hits were collected and used to assemble a dedicated Geobacteraceae OmcB reference database."`

---

## 4. Representation & Offline Verification Boundaries

1. **No schema or writer blockers for `CommonTaxon` (`kb/taxa/*.yaml`)**:
   - `write_validated_community(doc, path, target_class="CommonTaxon")` in `src/communitymech/validation/write_validated.py` validates `CommonTaxon` records in-memory against `src/communitymech/schema/communitymech.yaml` before writing and passes `scripts/audit_writers.py`.
2. **Offline UniProtKB verification boundary for the `20` gene-symbol-bearing community records**:
   - Under `AGENTS.md` ("Do not make network calls, spend provider credits, or apply generated curation unless the task authorizes it") and `.claude/skills/add-uniprot-protein-examples/SKILL.md` ("Prefer verified `UniProtKB:` identifiers when you can confirm the exact accession for that organism and gene; otherwise leave existing locus tags in place rather than guessing"), no unverified `UniProtKB:` accessions were guessed for taxa lacking a local offline UniProt proteome table in the repository.
