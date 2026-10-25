# Cycle 3, Stage 1 (`add_records`) — Bounded-Frontier Discovery & Intake Report (2026-10-25)

## 1. Executive Summary

- **Workflow Stage**: Run `mech-goal-sequence-20261019`, Cycle 3, Stage 1 (`add_records`)
- **Action ID**: `0b987a9cefdcc76e21992c1f`
- **Starting Corpus State**: 484 records (`CommunityMech:000001`–`CommunityMech:000490`; 378 in `kb/communities/` and 106 in `data/isolates/`)
- **Ending Corpus State**: 489 records (`CommunityMech:000001`–`CommunityMech:000495`; 381 in `kb/communities/` and 108 in `data/isolates/`)
- **New Records Added**: **5** (`CommunityMech:000491`–`CommunityMech:000495`: 3 multi-species/reactor communities in `kb/communities/` and 2 single-species isolate baselines in `data/isolates/`)
- **Exhaustion Verification**: Two full passes over the local offline reference cache (`references_cache/`), `research/`, `notes/new-communities-to-create.md`, and `notes/new-datasets-to-curate.md` confirmed that **0** additional uncited references with verbatim abstract/full-text support describe an uncurated microbial community or supported isolate baseline.

---

## 2. Bounded-Frontier Search Methodology & Repeated Passes

### Pass 1: Corpus Deduplication & Full Cache Sweep

1. **Corpus Citation Index**:
   - Parsed all 484 existing YAML records across `kb/communities/*.yaml` (378 files) and `data/isolates/*.yaml` (106 files), extracting every cited `PMID:` and `doi:` reference, community name, and taxon set.
   - Confirmed highest existing identifier: `CommunityMech:000490` (`data/isolates/Ferrimicrobium_acidiphilum_Iron_Respiration.yaml`).
2. **Local Reference Cache Audit (`references_cache/`)**:
   - Audited all cached reference files (`PMID_*.md`, `PMID_*.txt`, and `doi_*.md`) against the corpus citation index.
   - Filtered out empty/metadata-only stubs (`Abstract\nNone` or `<200` bytes of normalized prose) and references already cited in `kb/communities/` or `data/isolates/`.
   - Screened all remaining uncited references with substantive text for defined microbial consortia, co-cultures, enriched bioreactor communities, natural extreme-environment assemblages, and single-species isolate baselines.
3. **Admissibility & Boundary Classification**:
   - Applied the repository boundary contract (`kb/communities/` for multi-taxa communities and enriched reactor assemblages; `data/isolates/` for single-strain / single-species experimental baselines) and strict evidence policy (100% verbatim snippets from cached source text verified by `scripts/evidence_snippet_audit.py`, OAK-verified `NCBITaxon` / `ENVO` / `CHEBI` / `GO` terms, GTDB grounding status on every `taxonomy[].taxon_term`, and connected `ecological_interactions` causal graphs).

### Pass 2: Post-Intake Re-Sweep & Exhaustion Verification

- Re-ran the corpus-vs-cache deduplication scan after allocating `CommunityMech:000491`–`000495`.
- Verified that all 6 newly linked reference files (`PMID_26704063.md`, `PMID_21441371.md`, `doi_10.1007_s11274-009-0047-x.md`, `doi_10.1016_j.cej.2020.124801.md`, `PMID_23949950.txt`, and `PMID_40722006.txt`) are now cited in the corpus with 44/44 `MATCH` snippets in `scripts/evidence_snippet_audit.py`, and that **0** further admissible uncited community or isolate records remain in the local frontier.

---

## 3. Newly Added Records (`CommunityMech:000491`–`CommunityMech:000495`)

| ID | Path | Category / State / Origin | Primary Reference(s) | Taxa (`NCBITaxon` & GTDB Status) | Summary of Curated Mechanism |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `CommunityMech:000491` | `kb/communities/TwoStep_PCB_Copper_Gold_Bioleaching_Consortium.yaml` | `BIOMINING` / `ENGINEERED` / `ENGINEERED` | `PMID:26704063` | `Acidithiobacillus ferrivorans` (`NCBITaxon:160808`, `UNRESOLVED`), `Acidithiobacillus thiooxidans` (`NCBITaxon:930`, `GROUNDED`), `Pseudomonas putida` (`NCBITaxon:303`, `AMBIGUOUS`), `Pseudomonas fluorescens` (`NCBITaxon:294`, `AMBIGUOUS`) | Two-step waste PCB bioleaching: step 1 acidophilic Cu solubilization (98.4% at 1% pulp density / 10 g/L PCB, pH 1.0–1.6, 23 ± 2 °C, 7 d) followed by step 2 alkaline glycine-assisted (10 g/L glycine; 21.5 mg/L cyanide by `P. putida` WCS361) Au mobilization (44.0% at pH 7.3–8.6, 30 °C, 2 d). |
| `CommunityMech:000492` | `data/isolates/Intrasporangium_Chromatireducens_Q5_1_Chromate_Reduction.yaml` | `BIOREMEDIATION` / `STABLE` / `NATURAL` | `PMID:21441371`, `doi:10.1007/s11274-009-0047-x` | `Intrasporangium chromatireducens Q5-1` (`NCBITaxon:1386088`, `UNRESOLVED`) | Manganese/chromium-mine soil Actinobacterium isolate Q5-1 with high Cr(VI) resistance (MIC 17 mmol/L), reducing Cr(VI) aerobically (optimal pH 8.0, 37 °C), in resting cells stimulated by 1 mmol/L acetate, and when immobilized in PVA-alginate-carbon-diatomite compounding beads. |
| `CommunityMech:000493` | `kb/communities/Magnetite_Thiobacillus_Sulfur_Cycle_Phenol_Chromate_Reactor.yaml` | `BIOREMEDIATION` / `ENGINEERED` / `ENGINEERED` | `doi:10.1016/j.cej.2020.124801` | `Thiobacillus` (`NCBITaxon:919`, `GROUNDED`) | Magnetite-supplemented anaerobic sulfur-cycle bioreactor enriching chemolithotrophic `Thiobacillus` species to oxidize elemental sulfur to sulfate (6.85% vs 4.49% aggregate S), lowering effluent Cr(VI) (18.0 vs 187.7 mg/L) and phenol (354.2 vs 1256.0 mgCOD/L) under low-sulfate conditions via Fe(III)/Fe(II) transformation. |
| `CommunityMech:000494` | `kb/communities/Tunisian_Sahara_Saline_Spore_Forming_Halophile_Community.yaml` | `EXTREME_ENVIRONMENT` / `STABLE` / `NATURAL` | `PMID:23949950` | `Halobacillus trueperi` (`NCBITaxon:156205`, `UNRESOLVED`), `Bacillus` (`NCBITaxon:1386`, `UNRESOLVED`), `Virgibacillus` (`NCBITaxon:84406`, `UNRESOLVED`), `Oceanobacillus` (`NCBITaxon:182709`, `UNRESOLVED`), `Gracilibacillus` (`NCBITaxon:74385`, `UNRESOLVED`), `Paenibacillus` (`NCBITaxon:44249`, `AMBIGUOUS`), `Pontibacillus` (`NCBITaxon:289201`, `UNRESOLVED`) | Seven-genus halophilic/halotolerant aerobic endospore-forming Firmicutes community (336 isolates across 5 salt-saturated Chott and Sebkha brines/soils dominated by `Halobacillus trueperi` across 14 BOX-PCR genotypes) partitioned across extremely halotolerant (44.3%), strict halophilic (32.7%), and moderately halotolerant (23%) guilds. |
| `CommunityMech:000495` | `data/isolates/Ferroplasma_Acidiphilum_ZJ_AMD_Genomic_Island_Adaptation.yaml` | `EXTREME_ENVIRONMENT` / `STABLE` / `NATURAL` | `PMID:40722006` | `Ferroplasma acidiphilum ZJ` (`NCBITaxon:74969`, `GROUNDED`) | Acidophilic iron-oxidizing archaeal isolate from Zijin Mine acid mine drainage (modified 9K medium, pH 1.6, 22.4 g/L FeSO4·7H2O, 40 °C, 170 rpm) carrying 131 genes across 5 genomic islands (including 3rd-GI Cas2/Cas4 CRISPR/Cas defense, iron oxidation, mercury reduction, and toxin-antitoxin systems). |

---

## 4. Preserved Unresolved Candidates & Search Limits

### 4.1 Uncited Cached References Audited and Excluded (With Reasons)

1. **Broad Review / Perspective / Meta-Analysis Articles (No Single Curatable Community or Isolate)**:
   - `PMID:32127679`, `PMID:32300263`, `PMID:33339060`, `PMID:33690148`, `PMID:34818850`, `PMID:35105963`, `PMID:36690657`, `PMID:37914746`: Broad reviews of microbiome ecology, synthetic biology design principles, or biogeochemical cycles without experimental parameters or defined taxon composition for a specific community record.
2. **Abiotic / Chemical / Mineralogical / Non-Microbial Studies**:
   - Uncited `doi_10.1016_*` and `doi_10.1021_*` cache entries describing purely chemical leaching, electrochemical catalysis, or mineral surface spectroscopy without biological inocula.
3. **Metadata-Only / Abstract-Less Cache Stubs (`Abstract\nNone`)**:
   - Cached reference stubs lacking verbatim abstract or full-text sentences cannot satisfy CommunityMech's mandatory verbatim-snippet evidence gate (`scripts/evidence_snippet_audit.py`) without external full-text retrieval.

### 4.2 Candidates Preserved in `notes/` for Future Network-Enabled Scouting Cycles

- Candidate communities listed in `notes/new-communities-to-create.md` and `notes/new-datasets-to-curate.md` whose primary DOIs/PMIDs do not yet have full-text or abstract text in `references_cache/` remain preserved in `notes/` for future network-enabled Europe PMC / Edison retrieval runs.
