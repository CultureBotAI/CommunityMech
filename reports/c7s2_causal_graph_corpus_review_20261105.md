# Cycle 7 Stage 2 Causal-Graph & Mechanism Corpus Review (2026-11-05)

- **Run**: `mech-goal-sequence-20261019`
- **Cycle / Stage**: Cycle 7, Stage 2 (`causal_graphs`)
- **Base Commit**: `0694c268437c0eba37f93b08ca45fc203ad30255`
- **Decision Ledger Added**: `reports/causal_graph_review/decisions/20261105-stage2-five-records-batch139.yaml`
- **Inventory & Summary Updated**: `reports/causal_graph_review/inventory.tsv`, `reports/causal_graph_review/summary.json`

## 1. Corpus Scope & Summary Metrics

| Cohort | Count | Status After Cycle 7 Stage 2 | Notes |
|---|---:|---|---|
| `kb/communities/*.yaml` (`MicrobialCommunity`) | 494 | 440 `reviewed`, 54 `needs_research`, 0 `pending` | Includes Batch 139 (`CommunityMech:000505`–`000509`) curated & reviewed in this stage |
| `data/isolates/*.yaml` (`MicrobialCommunity`) | 9 | 9 `reviewed`, 0 `needs_research`, 0 `pending` | All 9 isolate baseline records verified unchanged via SHA-256 census |
| **Total `MicrobialCommunity` Records** | **503** | **449 `reviewed`, 54 `needs_research`, 0 `pending`** | **0 structural defects (`structural_defects == []`), 1,485 nodes, 586 downstream edges** |
| `kb/taxa/*.yaml` (`CommonTaxon`) | 2 | Verified schema- & term-valid | `Geobacter_sulfurreducens.yaml` (`e18219ed...`), `Shewanella_oneidensis_MR1.yaml` (`2fcc32b1...`) |
| **Total Eligible Corpus** | **505** | **100% accounted for** | 0 unreviewed (`pending`) records |

## 2. Batch 139 Causal-Graph Curation & Review (`CommunityMech:000505`–`000509`)

All five community records added in Cycle 7 Stage 1 were audited line-by-line against their committed primary-source evidence cache (`references_cache/PMID_41743136.txt`) and sibling record (`CommunityMech:000405`, `Hexamine_Formaldehyde_Degrading_Consortium_C6`), updated via `record_curation_event(..., action="CURATE_CAUSAL_GRAPH", llm_assisted=True)` and `write_validated_community(...)`, and recorded in append-only history sidecars under `history/records/`:

1. **`CommunityMech:000505` (`kb/communities/Hexamine_Formaldehyde_Consortium_C1.yaml`)**
   - **SHA-256**: `60d92b655af5f221456b8a8691dffffdc8c2e060c35481856ce125d487a0a263` → `1183b1f4762087ed7d8adf1b9960dc38beda73f5d23a8c378fdf8fd0a23e0a2a`
   - **Primary Source**: `PMID:41743136` (`PMC12929517`, `doi:10.3389/fmicb.2026.1753858`, `references_cache/PMID_41743136.txt`)
   - **Mechanism Representation (1 `COMMUNITY_LEVEL` node, 0 downstream edges)**:
     - `C1 suspended-culture hexamine, formaldehyde, and COD removal`: Enriched description and evidence with 2 additional verbatim snippets (5 total on the node) from `PMID:41743136` anchoring (i) monoculture log-phase durations and doubling times for C1 constituents *Brucella pseudintermedia* `SRCHD05` (`13.5 h` log phase, `73 min 2 s` doubling time) and *Ochrobactrum* sp. `SRCHD06` (`14 h` log phase, `128 min 12 s` doubling time) (`"The growth curve data of the selected isolates revealed that the isolate SRCHD07 was the fastest growing strain among the selected five isolates, with a log phase of 12 h and doubling time of 49 min and 6 s. Isolates SRCHD06 (14 h log phase, 128 min and 12 s doubling time), SRCHD05 (13.5 h log phase, 73 min and 2 s doubling time), SRCHD03 (20 h log phase, 121 min and 4 s doubling time), and SRCHD04 (25 h log phase, 80 min, and 6 s doubling time) took longer time to reach growth saturation ( Figure 3 )."`, `IN_VITRO`, `SUPPORT`), and (ii) reversible acidic chemical equilibrium between hexamine, formaldehyde, and ammonia (`"In acidic conditions, hexamine breaks down into ammonia and formaldehyde, both of which play an important role in water pollution. This being a reversible reaction, leads to the production of hexamine in the presence of formaldehyde and ammonia in wastewater, hence emphasizing the rapid removal of both formaldehyde and ammonia from wastewater."`, `OTHER`, `PARTIAL`).
   - **Taxon Grounding**: Verified `Brucella pseudintermedia SRCHD05` (`NCBITaxon:370111`) and `Ochrobactrum sp. SRCHD06` (`NCBITaxon:528`) synchronization across `taxonomy` and `participating_taxa`.
   - **Source-Limited Gaps**: Specific cross-fed C1 metabolites, formaldehyde dehydrogenase / hexamine-cleaving enzyme assignments, and pairwise strain growth couplings between `SRCHD05` and `SRCHD06` are not experimentally dissected (`discussions[0]: c1-molecular-division-of-labor`, `kind: KNOWLEDGE_GAP`).
   - **History Sidecar**: `history/records/Hexamine_Formaldehyde_Consortium_C1/2026-11-05T095000Z-antigravity-c7s201.yaml`.

2. **`CommunityMech:000506` (`kb/communities/Hexamine_Formaldehyde_Consortium_C2.yaml`)**
   - **SHA-256**: `69e753afea36f64daaa75ae9793d7f2f212dd9dd740694cad1b2f230a72fcdcd` → `5a2c59369389c982d1a1f2a54d2a278eee49908493a78e5c54d85af2d575979d`
   - **Primary Source**: `PMID:41743136` (`PMC12929517`, `doi:10.3389/fmicb.2026.1753858`, `references_cache/PMID_41743136.txt`)
   - **Mechanism Representation (1 `COMMUNITY_LEVEL` node, 0 downstream edges)**:
     - `C2 suspended-culture hexamine, formaldehyde, and COD removal`: Enriched description and evidence with 2 additional verbatim snippets (4 total on the node) anchoring (i) monoculture 72 h COD reduction baselines for `SRCHD05` (`42%`) and `SRCHD06` (`36%`) from an initial load of `11,900 mg/L` (`"COD analysis revealed that isolates SRCHD05 and SRCHD06 were more efficient among the selected isolates. They could reduce COD by 42 and 36% after 72 h of incubation at 37 °C from an initial load of 11,900 mg/L, respectively"`, `IN_VITRO`, `SUPPORT`), and (ii) monoculture log-phase durations and doubling times across C2 constituents *Brevundimonas diminuta* `SRCHD03` (`20 h`, `121 min 4 s`), *Brucella pseudintermedia* `SRCHD05` (`13.5 h`, `73 min 2 s`), and *Ochrobactrum* sp. `SRCHD06` (`14 h`, `128 min 12 s`).
   - **Taxon Grounding**: Verified `Brevundimonas diminuta SRCHD03` (`NCBITaxon:293` / `GTDB:s__Brevundimonas_diminuta`), `Brucella pseudintermedia SRCHD05` (`NCBITaxon:370111`), and `Ochrobactrum sp. SRCHD06` (`NCBITaxon:528`) synchronization across `taxonomy` and `participating_taxa`.
   - **Source-Limited Gaps**: Strain-level division of labor among `SRCHD03`, `SRCHD05`, and `SRCHD06` is not resolved (`discussions[0]: c2-molecular-division-of-labor`, `kind: KNOWLEDGE_GAP`).
   - **History Sidecar**: `history/records/Hexamine_Formaldehyde_Consortium_C2/2026-11-05T095000Z-antigravity-c7s202.yaml`.

3. **`CommunityMech:000507` (`kb/communities/Hexamine_Formaldehyde_Consortium_C3.yaml`)**
   - **SHA-256**: `d780f6bd211cd7144fc0db26b4dedf54b3c734d12349ade1511d51f243ddb5c7` → `042454b4b13904fcd05ee42b019346e9940ef68ae6504be8f745266e1d9f2c5f`
   - **Primary Source**: `PMID:41743136` (`PMC12929517`, `doi:10.3389/fmicb.2026.1753858`, `references_cache/PMID_41743136.txt`)
   - **Mechanism Representation (1 `COMMUNITY_LEVEL` node, 0 downstream edges)**:
     - `C3 suspended-culture hexamine, formaldehyde, and COD removal`: Enriched description and evidence with 2 additional verbatim snippets (4 total on the node) anchoring (i) non-`SRCHD03` monoculture ammonia accumulation during hexamine degradation (`"The remaining isolates showed an increase in ammonia concentration as an indication of hexamine degradation, but demonstrated an inability to remove ammonia"`, `IN_VITRO`, `SUPPORT`), and (ii) monoculture log-phase durations and doubling times across C3 constituents *Brevundimonas diminuta* `SRCHD04` (`25 h`, `80 min 6 s`), *Brucella pseudintermedia* `SRCHD05` (`13.5 h`, `73 min 2 s`), and *Ochrobactrum* sp. `SRCHD06` (`14 h`, `128 min 12 s`).
   - **Taxon Grounding**: Verified `Brevundimonas diminuta SRCHD04` (`NCBITaxon:293` / `GTDB:s__Brevundimonas_diminuta`), `Brucella pseudintermedia SRCHD05` (`NCBITaxon:370111`), and `Ochrobactrum sp. SRCHD06` (`NCBITaxon:528`) synchronization across `taxonomy` and `participating_taxa`.
   - **Source-Limited Gaps**: Pairwise metabolite transfer among `SRCHD04`, `SRCHD05`, and `SRCHD06` is not resolved (`discussions[0]: c3-molecular-division-of-labor`, `kind: KNOWLEDGE_GAP`).
   - **History Sidecar**: `history/records/Hexamine_Formaldehyde_Consortium_C3/2026-11-05T095000Z-antigravity-c7s203.yaml`.

4. **`CommunityMech:000508` (`kb/communities/Hexamine_Formaldehyde_Consortium_C4.yaml`)**
   - **SHA-256**: `5906a4b9c77a88595b3fab441042bd01bf6809d8573a333600e1293367992f54` → `63a03e2e8960e287c4637edf7562b97d8c90e9ee25d07a3f77fb8843170488bd`
   - **Primary Source**: `PMID:41743136` (`PMC12929517`, `doi:10.3389/fmicb.2026.1753858`, `references_cache/PMID_41743136.txt`)
   - **Mechanism Representation (1 `COMMUNITY_LEVEL` node, 0 downstream edges)**:
     - `C4 suspended-culture hexamine, formaldehyde, and COD removal`: Enriched description and evidence with 1 additional verbatim snippet (4 total on the node) anchoring *Brucella pseudintermedia* `SRCHD07` rapid monoculture growth kinetics (`12 h` log phase, `49 min 6 s` doubling time) alongside `SRCHD05` (`13.5 h`, `73 min 2 s`) and `SRCHD06` (`14 h`, `128 min 12 s`), accounting for accelerated 24–72 h hexamine (`71.13/83.62/91.11%`) and formaldehyde (`42.11/43.76/45.64%`) removal in Consortium C4.
   - **Taxon Grounding**: Verified `Brucella pseudintermedia SRCHD05` (`NCBITaxon:370111`), `Ochrobactrum sp. SRCHD06` (`NCBITaxon:528`), and `Brucella pseudintermedia SRCHD07` (`NCBITaxon:370111`) synchronization across `taxonomy` and `participating_taxa`.
   - **Source-Limited Gaps**: Specific metabolic interactions explaining why adding `SRCHD07` to `SRCHD05 + SRCHD06` increases hexamine and formaldehyde removal while leaving 72 h COD removal at `19.61%` are not dissected (`discussions[0]: c4-molecular-division-of-labor`, `kind: KNOWLEDGE_GAP`).
   - **History Sidecar**: `history/records/Hexamine_Formaldehyde_Consortium_C4/2026-11-05T095000Z-antigravity-c7s204.yaml`.

5. **`CommunityMech:000509` (`kb/communities/Hexamine_Formaldehyde_Consortium_C5.yaml`)**
   - **SHA-256**: `26627da7d477347c611e8339ff3da1239b97579faab867be6316259af710659d` → `c80260476fe0975446f9e2415313873060271d7a38240c64bae507ed7055b99e`
   - **Primary Source**: `PMID:41743136` (`PMC12929517`, `doi:10.3389/fmicb.2026.1753858`, `references_cache/PMID_41743136.txt`)
   - **Mechanism Representation (1 `COMMUNITY_LEVEL` node, 0 downstream edges)**:
     - `C5 suspended-culture hexamine, formaldehyde, and COD removal`: Enriched description and evidence with 1 additional verbatim snippet (4 total on the node) anchoring monoculture log-phase durations and doubling times across all five C5 constituent isolates (`SRCHD07`: `12 h`, `49 min 6 s`; `SRCHD06`: `14 h`, `128 min 12 s`; `SRCHD05`: `13.5 h`, `73 min 2 s`; `SRCHD03`: `20 h`, `121 min 4 s`; `SRCHD04`: `25 h`, `80 min 6 s`).
   - **Taxon Grounding**: Verified `Brevundimonas diminuta SRCHD03` (`NCBITaxon:293` / `GTDB:s__Brevundimonas_diminuta`), `Brevundimonas diminuta SRCHD04` (`NCBITaxon:293` / `GTDB:s__Brevundimonas_diminuta`), `Brucella pseudintermedia SRCHD05` (`NCBITaxon:370111`), `Ochrobactrum sp. SRCHD06` (`NCBITaxon:528`), and `Brucella pseudintermedia SRCHD07` (`NCBITaxon:370111`) synchronization across `taxonomy` and `participating_taxa`.
   - **Source-Limited Gaps**: Pairwise metabolite transfer and the functional consequence of omitting *Micrococcus luteus* `SRCHD02` from C5 relative to C6 (`CommunityMech:000405`) are not dissected at the molecular level (`discussions[0]: c5-molecular-division-of-labor`, `kind: KNOWLEDGE_GAP`).
   - **History Sidecar**: `history/records/Hexamine_Formaldehyde_Consortium_C5/2026-11-05T095000Z-antigravity-c7s205.yaml`.

## 3. Verification of Previously Reviewed (444) & `needs_research` (54) Records

- **444 Previously `reviewed` `MicrobialCommunity` Records**:
  - SHA-256 hash comparison against `reports/causal_graph_review/inventory.tsv` confirmed **0 hash drift** (`drift == []`).
- **54 `needs_research` `MicrobialCommunity` Records**:
  - Audited against `references_cache/`, `reports/drc/`, and `research/`: **0** of the 54 abstract-limited or paywalled records gained new cached open-access full text or deep-research reports since Cycle 6 Stage 2. Per repository policy, paid provider credits were not spent and no unsupported causal edges were fabricated; all 54 records remain explicitly tracked as `needs_research` in `reports/causal_graph_review/inventory.tsv`.
- **2 `CommonTaxon` Records (`kb/taxa/`)**:
  - Verified `kb/taxa/Geobacter_sulfurreducens.yaml` (`sha256: e18219ed636fb72eba06642469cdcca904a0c2f21697a1893447f80dab179556`) and `kb/taxa/Shewanella_oneidensis_MR1.yaml` (`sha256: 2fcc32b1e409beb3b69c850a7ca22ac562a47bc9cf3a028e31eb1d7e85c92671`) pass `just validate-taxa` and `just validate-terms-taxa`.
- **Representation & Writer Blockers**:
  - **0** representation or writer blockers encountered (`write_validated_community` and `record_curation_event` handled all Batch 139 edits cleanly, and `scripts/audit_causal_graphs.py` + `reports/causal_graph_review/build_inventory.py` confirm `structural_defects == []` across all 503 `MicrobialCommunity` records).
