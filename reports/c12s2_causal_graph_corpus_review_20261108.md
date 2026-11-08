# Cycle 12 Stage 2 — Full-Corpus Causal Graph & Native Mechanism Review (2026-11-08)

## 1. Executive Summary & Corpus Accounting

- **Run / Cycle / Stage**: `mech-goal-sequence-20261019`, Cycle 12, Stage 2 (`causal_graphs`)
- **Base Commit on `main`**: `201f5b09872e231fe13b76e215f521310f94891d` (merged PR `#2735` from Cycle 12 Stage 1)
- **Total Eligible Records Reviewed**: **531 YAML records** across all three repository roots:
  - `kb/communities/*.yaml`: **511** `MicrobialCommunity` records
  - `data/isolates/*.yaml`: **18** `MicrobialCommunity` isolate-baseline records
  - `kb/taxa/*.yaml`: **2** `CommonTaxon` reusable taxon records (`NCBITaxon_1280.yaml`, `NCBITaxon_1423.yaml`)
- **Post-Stage-2 `MicrobialCommunity` Causal-Graph Review Coverage (`529` records in `reports/causal_graph_review/summary.json`)**:
  - **`reviewed` (hash-bound semantic review tip matches current file SHA-256)**: **475** (`+5` from Batch 144: `CommunityMech:000531` through `CommunityMech:000535`)
  - **`needs_research` (source-limited records preserved unchanged with documented blockers)**: **54**
  - **`pending` / `stale`**: **0**
  - **`structural_defects`**: **0** (`[]`)
  - **Total `EcologicalInteraction` nodes**: **1,538**
  - **Total directed `downstream` causal edges**: **593**
  - **Records with 0 interaction nodes**: **10** (all 10 are source-limited `needs_research` records)
  - **Records with 0 `downstream` edges**: **221** (`216` prior + `5` single-node `COMMUNITY_LEVEL` records curated in Batch 144)

---

## 2. Batch 144 Curation & Evidence Enrichment (`CommunityMech:000531`–`000535`)

All 5 records added in Cycle 12 Stage 1 (`CommunityMech:000531`–`000535`) entered Stage 2 with `review_status = pending`. Each record was audited against its committed full-text source cache (`references_cache/PMID_42598292.txt`, `references_cache/PMID_42307251.txt`, `references_cache/PMID_42318495.txt`) following `.claude/skills/curate-causal-graphs/SKILL.md`, `.claude/skills/curate-yaml-record/SKILL.md`, and `.claude/skills/ground-causal-graph-taxa/SKILL.md`:

| Record ID | Path | Primary Source | Interaction Nodes | Downstream Edges | Node Evidence (`before -> after`) | Pre-Stage-2 SHA-256 (`original_sha256`) | Post-Stage-2 SHA-256 (`record_sha256`) |
|---|---|---|---|---:|---:|---|---|
| `CommunityMech:000531` | `data/isolates/Microbacterium_BR1_Sulfadiazine_Cleaving_Isolate_Baseline.yaml` | `PMID:42598292` (`PMC13472149`) | 1 (`COMMUNITY_LEVEL`: `Ipso-Substitution Sulfadiazine Cleavage and Dead-End 2-Aminopyrimidine Accumulation by Axenic Microbacterium BR1`) | 0 | `3 -> 5` | `149a6ab7149a19719ff9e73f58a650b744327ec2306350af2f495cbd85e81531` | `5965fcdc4339472b062db3e80b73f336c75328591666049a1ce05e6df94be7c7` |
| `CommunityMech:000532` | `data/isolates/Terrabacter_2APm3_Sulfadiazine_Isolate_Baseline.yaml` | `PMID:42598292` (`PMC13472149`) | 1 (`COMMUNITY_LEVEL`: `Inability of Axenic Terrabacter sp. 2APm3 to Cleave Intact Sulfadiazine Without Upstream Ipso-Substitution`) | 0 | `3 -> 5` | `677193069c629cbbecdaad6e13fb53881e3ead1c644725acab370fe1cfdd2b5c` | `1f8686e5878cea0ab2f49f34bf3964dc23bafab6814ee9048a0301d5a735713a` |
| `CommunityMech:000533` | `data/isolates/Achromobacter_SL8_Cadmium_Immobilization_Isolate_Baseline.yaml` | `PMID:42307251` (`PMC13340288`) | 1 (`COMMUNITY_LEVEL`: `Cadmium Immobilization, Alkalinization, and N-H Surface Coordination by Achromobacter sp. SL8 Monoculture`) | 0 | `4 -> 6` | `9570a1bcd8115e59d8dedd2a31760f6acccdbb030f0d98f5670cd0af203c556f` | `106192c3aff58a26aca56f6d42ca90054dc0e6ae03bbc0a6dea29eaebd2d58e8` |
| `CommunityMech:000534` | `data/isolates/Enterobacter_SL12_Cadmium_Immobilization_Isolate_Baseline.yaml` | `PMID:42307251` (`PMC13340288`) | 1 (`COMMUNITY_LEVEL`: `High-Cadmium Induced Immobilization and Amide C=O Surface Binding by Enterobacter sp. SL12 Monoculture`) | 0 | `4 -> 6` | `e35dcd4e7772a4525d707fe454bdd188c2500e8bfc8024fb1ec0d989b290cb0f` | `fdc54a3c28bbda72e51690583fabd2fd1441f32b7d2d4bb8ead59558c9a54904` |
| `CommunityMech:000535` | `kb/communities/Ogataea_Str3_Leu2_Auxotrophic_CrossFeeding_Coculture.yaml` | `PMID:42318495` (`PMC13273856`) | 1 (`COMMUNITY_LEVEL`: `STR3-LEU2 Cross-Pathway Auxotrophic Complementation and Biomass Restoration on Glucose`) | 0 | `4 -> 6` | `cf4a1289c42b61654ff9fa1407a55cad4bf9b22f0c829235b26c8705c2ffe282` | `ee3d60ffa29820d717dcb8a7f60e855d04cefb85fd71e580c57cf14a466a2637` |

### Why 0 `downstream` Edges Are Curated on `CommunityMech:000531`–`000535`

1. **Axenic Isolate Baselines (`CommunityMech:000531`, `CommunityMech:000532`, `CommunityMech:000533`, `CommunityMech:000534`)**:
   - In `PMID:42598292`, axenic *Microbacterium* sp. BR1 (`000531`) cleaves `1.0 +- 0.1 mM` sulfadiazine within 2 days via ipso-substitution and accumulates stoichiometric `1.0 +- 0.1 mM` 2-aminopyrimidine (`2-AP`) as a dead-end metabolite through Day 4, while axenic *Terrabacter* sp. 2APm3 (`000532`) catalyzes zero sulfadiazine removal (`1.0 +- 0.1 mM` remaining at Day 4, `0.0 mM` `2-AP`) and declines from `775 +- 10` to `474 +- 44 cells/uL`. Inter-taxon cross-feeding and downstream `2-AP` ring cleavage occur only in the two-species consortium (`CommunityMech:000371`).
   - In `PMID:42307251`, axenic *Achromobacter* sp. SL8 (`000533`) and axenic *Enterobacter* sp. SL12 (`000534`) were assayed as 7-day monoculture baselines (`82.6% -> 69.55%` and `63.4% -> 70.8%` `Cd2+` removal at `50` vs `100 mg/L`, broth alkalinization to `pH 8.0-8.5`, strain-specific FTIR `N-H` vs amide `C=O` binding, and TEM morphology), and the authors explicitly note (lines 169–170) that proteomic/metabolomic profiles (Groups A and B) are correlative without gene-knockout causal validation.
2. **Screening-Stage Cross-Pathway Yeast Co-Culture (`CommunityMech:000535`)**:
   - In `PMID:42318495` Section 3.2 (Figure 2a–d), the *Ogataea polymorpha* `str3Δ-leu2Δ` pair was validated in 96-well plates (`RI >= 0.8`) and 100 mL shake flasks (`20 g/L` glucose, initial total `OD600 = 0.2`, 1:1 ratio, `n = 4`), reaching a maximum `OD600` of `27.3–28.5` (comparable to prototrophic `FY00` at `26.8`, `p > 0.1`) after an extended lag phase (`p < 10^-4`). Unlike `met10Δ-str3Δ` (`CommunityMech:000527`), `PMID:42318495` did not perform single-intermediate supplementation or fluorescent ratio tracking on `str3Δ-leu2Δ`, so directional secretion vs uptake of specific sulfur and branched-chain amino acid intermediates is not experimentally dissected in the source. Curating a single `COMMUNITY_LEVEL` mutualism node with 0 `downstream` edges and 6 non-overlapping verbatim snippets preserves the exact experimental boundary without inventing unverified intermediate steps.

---

## 3. Taxonomic Grounding & Reusable Taxon Audit (`kb/taxa/*.yaml`)

- All `TaxonDescriptor` entries across `CommunityMech:000531`–`000535` (`taxonomy[].taxon_term` and `ecological_interactions[].participating_taxa`) were verified with `scripts/validate_gtdb_grounding.py`, `scripts/validate_gtdb_ncbi_domain.py`, and `tests/test_gtdb_lineage_tree.py`:
  - `Microbacterium sp. BR1` (`NCBITaxon:53399` -> genus `GTDB:g__Microbacterium`, `GROUNDED`)
  - `Terrabacter sp. 2APm3` (`NCBITaxon:1892307` -> genus `GTDB:g__Terrabacter`, `GROUNDED`)
  - `Achromobacter sp. SL8` (`NCBITaxon:222` -> genus `GTDB:g__Achromobacter`, `GROUNDED`)
  - `Enterobacter sp. SL12` (`NCBITaxon:547` -> genus `GTDB:g__Enterobacter`, `GROUNDED`)
  - `Ogataea polymorpha` (`NCBITaxon:460523`, eukaryotic yeast -> `NO_GTDB_EQUIVALENT`)
- Both reusable taxon records in `kb/taxa/` (`kb/taxa/NCBITaxon_1280.yaml`, `kb/taxa/NCBITaxon_1423.yaml`) remain schema-valid, term-valid, and reference-valid (`just validate-taxa`, `just validate-terms-taxa`).

---

## 4. Source-Limited Records (`needs_research`: 54) & Representation/Writer Blockers

- **54 `needs_research` records**: Re-verified unchanged via `reports/causal_graph_review/summary.json`. These records lack cached open-access full text or multi-step experimental perturbation data in their cited sources (e.g., paywalled articles, abstract-only metadata, or descriptive survey/amplicon studies). In accordance with the Stage 2 prompt ("do not invent fields or unsupported edges"), no synthetic nodes or speculative `downstream` edges were added.
- **Representation / Writer Blockers**:
  1. **Supplement-only evidence routing (`#1996`)**: `linkml-reference-validator` matches against committed article caches under `references_cache/` (`PMID_*.md` / `PMID_*.txt` / `DOI_*.md`) and does not route to external supplementary tables (such as Zenodo `https://zenodo.org/records/20263325` Tables S1–S2 in `PMID:42307251` or Supplementary Table 1 in `PMID:42318495`). Supplement-only boundaries are recorded in each record's `discussions` (`category: EVIDENCE_GAP`) and in `source_backed_gaps` in `reports/causal_graph_review/decisions/20261108-stage2-five-records-batch144.yaml`.
  2. **Bracketed citation token rejection in `linkml-reference-validator`**: Verbatim sentences containing inline bracketed reference numbers (`[1]`, `[34]`) are split by `linkml-reference-validator` into separate sub-queries. All 10 newly added `EvidenceItem` snippets across `CommunityMech:000531`–`000535` were selected from contiguous unbracketed spans in `references_cache/` and verified with `linkml-reference-validator`.
