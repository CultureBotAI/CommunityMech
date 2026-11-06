# Cycle 8 Stage 2 (`causal_graphs`) Corpus Review — 2026-11-05

## 1. Corpus Scope and Complete Record Accounting

In Cycle 8 Stage 2 (`causal_graphs`, `run_id: mech-goal-sequence-20261019`, `cycle: 8`, `stage: 2`), every canonical record across all three repository record roots (`kb/communities/`, `data/isolates/`, and `kb/taxa/`) was accounted for and verified against its SHA-256 content hash, LinkML schema, and causal-graph review ledger:

| Record Root | Root Class | Record Count | Status Breakdown |
|---|---|---:|---|
| `kb/communities/*.yaml` | `MicrobialCommunity` | 499 | 445 `reviewed` (440 prior + 5 newly curated in Batch 140), 54 `needs_research` |
| `data/isolates/*.yaml` | `MicrobialCommunity` | 9 | 9 `reviewed` |
| `kb/taxa/*.yaml` | `CommonTaxon` | 2 | 2 verified (`Geobacter_sulfurreducens.yaml`, `Shewanella_oneidensis_MR1.yaml`; no `ecological_interactions` slot on `CommonTaxon`) |
| **Total (`MicrobialCommunity`)** | `MicrobialCommunity` | **508** | **454 `reviewed`, 54 `needs_research`, 0 `pending`, 0 `stale`, 0 `structural_defects`** |
| **Total (all YAML records)** | `MicrobialCommunity` + `CommonTaxon` | **510** | **100% corpus coverage** |

Summary metrics from `reports/causal_graph_review/summary.json`:

- `records`: `508`
- `nodes`: `1493` (`+8` from Cycle 7 Stage 2's `1485`)
- `edges`: `587` (`+1` from Cycle 7 Stage 2's `586`)
- `records_without_nodes`: `10` (all in `needs_research`)
- `records_without_edges`: `206` (`302` records have `>= 1` directed causal edge)
- `review_status_counts`: `{"needs_research": 54, "reviewed": 454}`
- `structural_defects`: `[]`

---

## 2. Batch 140 Curation and Review (`CommunityMech:000510`–`CommunityMech:000514`)

All five records added in Cycle 8 Stage 1 (`PR #2328`) were audited line-by-line against their committed primary-source full-text caches (`references_cache/PMID_29611893.md`, `references_cache/PMID_35699440.md`, `references_cache/PMID_40920748.md`, and `references_cache/PMID_36118206.md`) and sibling records (`CommunityMech:000068`, `CommunityMech:000069`, `CommunityMech:000188`, `CommunityMech:000025`, `CommunityMech:000076`, and `CommunityMech:000077`). Decision ledger: `reports/causal_graph_review/decisions/20261105-stage2-five-records-batch140.yaml`.

| ID | Record Path | Primary Reference | Scope & Nodes | Edges (Before -> After) | Original SHA-256 -> Curated SHA-256 | Curation & Source-Bounded Summary |
|---|---|---|---|---:|---|---|
| `CommunityMech:000510` | `kb/communities/Syntrophobacter_Desulfovibrio_Propionate_Syntrophy.yaml` | `PMID:29611893` (`PMC5947623`) | 2 `PAIRWISE` (`Syntrophic Propionate Oxidation with Interspecies Formate and Hydrogen Transfer`; `Hydrogen- and Formate-Coupled Dissimilatory Sulfate Reduction`) | `1 -> 1` | `dda800f1...` -> `2e95cd16...` | Added verbatim proteomic evidence for *S. fumaroxidans* MPOB simultaneous sulfidogenic (`Sat`, `HppA`, `AprAB`, `DsrAB`, `DsrC`, `HdrABC/HdrL` `Sfum_0819-0824`) and RET/IET (`Fdh1`, `Fdh2`, `Hox`, `Hyn` `Sfum_2952-53`, `FrdABEF` `Sfum_4092-4095`) expression and *D. desulfuricans* G11 coculture PCA separation (`PC1 ~70%` variance, `317` core proteins with `AprA` `G11_01440`, `FDH3` `G11_11530-11545`, `Hyd-3` `G11_06350-06355`); bounded the retained downstream edge to note that formate vs H2 flux and partner sulfate-reduction partitioning were not separately resolved. |
| `CommunityMech:000511` | `kb/communities/Syntrophomonas_Methanobacterium_Butyrate_Syntrophy.yaml` | `PMID:35699440` (`PMC9275234`) | 1 `PAIRWISE` (`Syntrophic Butyrate Beta-Oxidation Coupled to Methanogenesis`) | `0 -> 0` | `cb90444c...` -> `b52fec15...` | Added verbatim evidence confirming zero detectable extracellular formate accumulation in *S. wolfei* G311 + *M. formicicum* MF bicultures without *T. flocculiformis* ES5 alongside Table 1 modified Gompertz kinetics (`5.38 ± 0.43 d` lag phase, `0.15 ± 0.006 mmol/L/day` methane rate, `3.92 ± 0.23 mmol/L` max methane); preserved 0 downstream edges because H2 vs formate flux partitioning and biculture proteomics were not measured for the *M. formicicum* pair. |
| `CommunityMech:000512` | `kb/communities/Trichococcus_Syntrophomonas_Methanobacterium_Butyrate_Coculture.yaml` | `PMID:35699440` (`PMC9275234`) | 1 `COMMUNITY_LEVEL` (`Trichococcus-Stimulated Syntrophic Butyrate Conversion to Methane`) | `0 -> 0` | `1b14a29a...` -> `c51b53ad...` | Added verbatim Table 1 biculture baseline (`5.38 ± 0.43 d` lag, `0.15 ± 0.006 mmol/L/day` Vm, `3.92 ± 0.23 mmol/L` max CH4) and transient triculture formate detection (`smallest amounts of formate` among the three tricultures vs none in bicultures); preserved 0 downstream edges because SEM aggregation and differential proteomics were performed exclusively on the *M. hungatei* JF1 triculture (`CommunityMech:000188`). |
| `CommunityMech:000513` | `kb/communities/EcoFAB_Ring_Trial_SynCom16.yaml` | `PMID:40920748` (`PMC12416739`) | 2 `COMMUNITY_LEVEL` (`Rhodococcus-, Methylobacterium-, and Mycobacterium-Dominated SynCom16 Root Assembly`; `SynCom16 Shoot Biomass Reduction and Exometabolite Remodeling`) | `0 -> 0` | `3df3baa2...` -> `05be6ff3...` | Added verbatim evidence for *Rhodococcus* sp. OAS809 fast liquid growth and high swimming motility traits (`68 ± 33%` root abundance alongside *Methylobacterium* sp. OAE515 at `15 ± 20%` and *Mycobacterium* sp. OAE908 at `14 ± 27%`) and higher within-lab microbiome (`S6c Fig`) and exometabolome (`S7d Fig`) coefficient of variation relative to SynCom17 across all 5 ring-trial laboratories; preserved 0 downstream edges because individual strain contributions to metabolite remodeling and shoot biomass decrease were not dissected in SynCom16. |
| `CommunityMech:000514` | `kb/communities/Wheat_Consortium_C7.yaml` | `PMID:36118206` (`PMC9473337`) | 2 `COMMUNITY_LEVEL` (`C7 Dual-Culture and Volatile Inhibition of R. solani AG8`; `C7 Greenhouse Wheat Protection and Salkowski Auxin Output`) | `0 -> 0` | `c773cdfa...` -> `fa1c93e4...` | Added verbatim Table 4 evidence for individual C7 constituent-strain cell-free supernatant radial growth inhibition of *R. solani* AG8 (`B5` `40.62 ± 9.10%`, `B6` `57.53 ± 15.53%`, `B7` `76.56 ± 3.60%`, `B11` `48.45 ± 18.90%`, contrasting with inactive pooled C7 CFS) and Table 3 individual Salkowski IAA concentrations (`4.40` to `18.04 μg/mL` vs `10.87 ± 2.54 μg/mL` in C7); preserved 0 downstream edges because in vitro antagonism, volatile emission, auxin output, and greenhouse suppression were assayed as parallel screens. |

---

## 3. Taxonomic Grounding Verification Across Batch 140 (`ground-causal-graph-taxa`)

Every taxon across `taxonomy[]`, `source_taxon`, `target_taxon`, and `participating_taxa` in `CommunityMech:000510`–`CommunityMech:000514` (27 total taxonomic entries) was verified against `NCBITaxon` and `GTDB` R220:

- `CommunityMech:000510`: 1 `GROUNDED` (`Syntrophobacter fumaroxidans` `NCBITaxon:119484` -> `GTDB:s__Syntrophobacter_fumaroxidans`) and 1 `AMBIGUOUS` (`Desulfovibrio desulfuricans` `NCBITaxon:876`, `gtdb_candidates: [GTDB:s__Desulfovibrio_desulfuricans, GTDB:s__Desulfovibrio_sp900243745]`).
- `CommunityMech:000511`: 1 `GROUNDED` (`Methanobacterium formicicum` `NCBITaxon:2162` -> `GTDB:s__Methanobacterium_formicicum`) and 1 `AMBIGUOUS` (`Syntrophomonas wolfei` `NCBITaxon:863`, `gtdb_candidates: [GTDB:s__Syntrophomonas_methylbutyratica, GTDB:s__Syntrophomonas_wolfei]`).
- `CommunityMech:000512`: 2 `GROUNDED` (`Trichococcus flocculiformis` `NCBITaxon:82803` -> `GTDB:s__Trichococcus_flocculiformis`; `Methanobacterium formicicum` `NCBITaxon:2162` -> `GTDB:s__Methanobacterium_formicicum`) and 1 `AMBIGUOUS` (`Syntrophomonas wolfei` `NCBITaxon:863`, `gtdb_candidates: [GTDB:s__Syntrophomonas_methylbutyratica, GTDB:s__Syntrophomonas_wolfei]`).
- `CommunityMech:000513`: 14 `GROUNDED` at genus rank (`Rhodococcus sp. OAS809` `NCBITaxon:1827` -> `GTDB:g__Rhodococcus`; `Methylobacterium sp. OAE515` `NCBITaxon:407` -> `GTDB:g__Methylobacterium`; `Mycobacterium sp. OAE908` `NCBITaxon:1763` -> `GTDB:g__Mycobacterium`; `Bradyrhizobium sp. OAE829` `NCBITaxon:374` -> `GTDB:g__Bradyrhizobium`; `Rhizobium sp. OAE497` `NCBITaxon:379` -> `GTDB:g__Rhizobium`; `Bosea sp. OAE506` `NCBITaxon:85413` -> `GTDB:g__Bosea`; `Variovorax sp. OAS795` `NCBITaxon:34072` -> `GTDB:g__Variovorax`; `Lysobacter sp. OAE881` `NCBITaxon:68` -> `GTDB:g__Lysobacter`; `Chitinophaga sp. OAE865` `NCBITaxon:79328` -> `GTDB:g__Chitinophaga`; `Niastella sp. OAS944` `NCBITaxon:354354` -> `GTDB:g__Niastella`; `Mucilaginibacter sp. OAE612` `NCBITaxon:423349` -> `GTDB:g__Mucilaginibacter`; `Brevibacillus sp. OAP136` `NCBITaxon:55080` -> `GTDB:g__Brevibacillus`; `Gottfriedia sp. OAE603` `NCBITaxon:2837503` -> `GTDB:g__Gottfriedia`; `Marmoricola sp. OAE513` `NCBITaxon:86795` -> `GTDB:g__Marmoricola`), 1 `AMBIGUOUS` (`Paenibacillus sp. OAE614` `NCBITaxon:44249`, 33 GTDB genus candidates), and 1 `UNRESOLVED` (`Arthrobacter sp. OAP107` `NCBITaxon:1667`).
- `CommunityMech:000514`: 4/4 `GROUNDED` (`Pseudomonas sp. B5` and `Pseudomonas sp. B11` `NCBITaxon:286` -> `GTDB:g__Pseudomonas`; `Streptomyces sp. B6` `NCBITaxon:1883` -> `GTDB:g__Streptomyces`; `Chryseobacterium sp. B7` `NCBITaxon:59732` -> `GTDB:g__Chryseobacterium`).

---

## 4. Prior Reviewed (`449`) and `needs_research` (`54`) Records plus `CommonTaxon` (`2`)

- **449 previously reviewed `MicrobialCommunity` records** (`440` in `kb/communities/` + `9` in `data/isolates/`): All `449` records match their exact `record_sha256` in `reports/causal_graph_review/decisions/*.yaml` (`0` stale hashes, `0` structural defects).
- **54 `needs_research` `MicrobialCommunity` records**: All `54` records are source-limited (`10` without interaction nodes and `44` with single-node/zero-edge or source-bounded representations where cached literature lacks multi-step causal mechanism evidence) and are preserved unchanged in `reports/causal_graph_review/decisions/20260417-remediated-records-status.yaml` and subsequent batch ledgers.
- **2 `CommonTaxon` records in `kb/taxa/`**:
  - `kb/taxa/Geobacter_sulfurreducens.yaml` (`SHA-256: 970ca3a904da541269aa8e7091295f8970cbd77da6957f4d34e4380266844fc`)
  - `kb/taxa/Shewanella_oneidensis_MR1.yaml` (`SHA-256: 264d4a709ae864575d9d0f66463508ee9dedf39c659997e6bbdd31f52b05a6aa`)
  Both validate cleanly under `CommonTaxon` schema and term checks (`CommonTaxon` records store reusable taxon/gene/UniProt annotations and do not carry an `ecological_interactions` slot).
