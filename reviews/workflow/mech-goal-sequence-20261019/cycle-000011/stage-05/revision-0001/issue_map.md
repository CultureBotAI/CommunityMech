# Cycle 11 Stage 5 Grouped Issue Map and Finding Dispositions

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `11` (`cycle-000011`)
- **Stage**: `5` (`resolve_review_findings`, `revision-0001`)
- **Repository**: `CultureBotAI/CommunityMech`
- **Consumed Stage 4 Evidence**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000011/stage-04/revision-0001/evidence.yaml` (`c20a3c813204740a40bed4e1b698bb611529ae68c6b952289509c0865e750cbd`)
- **Successor Structured Review**: `reviews/structured/20261108T150500Z-c11s5-remediation-verification/review.yaml` (`0f602a2832255f1fd7366a4f63792dbbf7cbb59044c77e3c95568e82cba315f4`)

## 1. Issue Grouping and Deduplication Summary

All 10 carried-forward finding IDs from Cycle 11 Stage 4 (`carry_forward_ids`: 3 actionable `open` findings across 3 community records, plus 7 source-limited `deferred` findings across 7 community records) were grouped by shared root cause and repair ownership and deduplicated against real GitHub issues in `CultureBotAI/CommunityMech`:

| Group ID | Shared Root Cause & Repair Ownership | GitHub Issue | Action | Finding IDs | Target Records | Disposition |
|---|---|---|---|---|---|---|
| `cm-c11-s05-g001` | Omitted source-backed taxonomic `abundance_level` enums across 6 taxonomic entries on `CommunityMech:000069`, `CommunityMech:000181`, and `CommunityMech:000213`. Repair owner: `kb/communities/` + `history/records/` + `reports/causal_graph_review/` + `tests/` + `docs/communities/`. | [#2732](https://github.com/CultureBotAI/CommunityMech/issues/2732) | `created` | `c11s4-000069-syntrophobacter-methanospirillum-abundance-levels`, `c11s4-000181-pseudomonas-rhodococcus-abundance-levels`, `c11s4-000213-variovorax-cryptococcus-abundance-levels` | `CommunityMech:000069`, `CommunityMech:000181`, `CommunityMech:000213` | `resolved` |
| `cm-c11-s05-g002` | Source-limited full-text co-culture assay tables for cheese rind model community (`PMID:25043025`). | [#765](https://github.com/CultureBotAI/CommunityMech/issues/765) | `reused` | `cheese-assay-evidence-gap` | `CommunityMech:000153` | `deferred` |
| `cm-c11-s05-g003` | Source-limited full-text strain-pair exometabolite tables for GLBRC transwell SynCom (`PMID:38329909`). | [#1467](https://github.com/CultureBotAI/CommunityMech/issues/1467) | `reused` | `communitymech-1467-source-discrepancy-and-extension` | `CommunityMech:000091` | `deferred` |
| `cm-c11-s05-g004` | Source-limited paywalled full-text enzyme assay parameters for Okeke-Lu cellulolytic consortium (`PMID:21319991`). | [#1657](https://github.com/CultureBotAI/CommunityMech/issues/1657) | `reused` | `okeke-fulltext-assay-gap` | `CommunityMech:000048` | `deferred` |
| `cm-c11-s05-g005` | Source-limited full-text secondary bacterial satellite interaction data for *Parachlorella*–*Saccharomyces* co-culture (`PMID:35101850`). | [#1681](https://github.com/CultureBotAI/CommunityMech/issues/1681) | `reused` | `parachlorella-remaining-research` | `CommunityMech:000295` | `deferred` |
| `cm-c11-s05-g006` | Source-limited full-text heterotrophic co-isolate tables for *Phormidium* alkaline consortium (`PMID:29138632`). | [#1699](https://github.com/CultureBotAI/CommunityMech/issues/1699) | `reused` | `communitymech-1699-coverage` | `CommunityMech:000054` | `deferred` |
| `cm-c11-s05-g007` | Source-limited full-text supplementary strain tables for sulfide spring CPR biofilm (`PMID:41606024`). | [#1841](https://github.com/CultureBotAI/CommunityMech/issues/1841) | `reused` | `communitymech-1841` | `CommunityMech:000222` | `deferred` |
| `cm-c11-s05-g008` | Source-limited full-text 18-isolate membership and media tables for sugarcane stress-resilience SynCom MetG2 (`PMID:41908926`). | [#1847](https://github.com/CultureBotAI/CommunityMech/issues/1847) | `reused` | `communitymech-1847-metg2-membership` | `CommunityMech:000302` | `deferred` |

## 2. Remediated Records and Provenance Sidecars

1. `kb/communities/Syntrophobacter_Methanospirillum_Syntrophy.yaml` (`CommunityMech:000069`) — Added `abundance_level: DOMINANT` and verbatim two-member syntrophic co-culture evidence from `PMID:9828440` (`doi:10.1099/00207713-48-4-1383`) on `Syntrophobacter fumaroxidans` (`NCBITaxon:119484`, `taxonomy[0]`) and `Methanospirillum hungatei` (`NCBITaxon:2203`, `taxonomy[1]`) while preserving `discussions[0]` (`propionate-carrier-partition-and-enzyme-roles`); provenance sidecar `history/records/Syntrophobacter_Methanospirillum_Syntrophy/2026-11-08T150000Z-antigravity-2732a1.yaml`.
2. `kb/communities/Pseudomonas_Rhodococcus_Chloronitrobenzene_Coculture.yaml` (`CommunityMech:000181`) — Added `abundance_level: DOMINANT` and verbatim two-strain chloronitrobenzene-degrading coculture evidence from `PMID:10049867` (`doi:10.1128/AEM.65.3.1083-1091.1999`) on `Pseudomonas putida` (`NCBITaxon:303`, `taxonomy[0]`) and `Rhodococcus` (`NCBITaxon:1827`, `taxonomy[1]`) while preserving `discussions[0]` (`chloronitro-direction-and-mineralization`); provenance sidecar `history/records/Pseudomonas_Rhodococcus_Chloronitrobenzene_Coculture/2026-11-08T150000Z-antigravity-2732a2.yaml`.
3. `kb/communities/Variovorax_Cryptococcus_Vitamin_Mutualism_Microcosm.yaml` (`CommunityMech:000213`) — Added `abundance_level: DOMINANT` and verbatim two-member vitamin cross-feeding mutualism evidence from `PMID:37553333` (`doi:10.1038/s41467-023-40360-4`) on `Variovorax` (`NCBITaxon:34072`, `taxonomy[0]`) and `Cryptococcus` (`NCBITaxon:5206`, `taxonomy[1]`) while preserving `discussions[0]` (`variovorax-evidence-boundaries-batch117`); provenance sidecar `history/records/Variovorax_Cryptococcus_Vitamin_Mutualism_Microcosm/2026-11-08T150000Z-antigravity-2732a3.yaml`.
