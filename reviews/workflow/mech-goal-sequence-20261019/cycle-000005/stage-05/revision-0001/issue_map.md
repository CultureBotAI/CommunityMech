# Cycle 5 Stage 5 Grouped Issue Map and Finding Dispositions

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `5` (`cycle-000005`)
- **Stage**: `5` (`resolve_review_findings`, `revision-0001`)
- **Repository**: `CultureBotAI/CommunityMech`
- **Consumed Stage 4 Evidence**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000005/stage-04/revision-0001/evidence.yaml` (`008a828eed62ef738183d063d4d626267ce55c6c84458f155fcaf7823c226552`)
- **Successor Structured Review**: `reviews/structured/20261104T060000Z-c5s5-remediation-verification/review.yaml` (`131c08557576c443a9d3c5181e8c6d265d5ebf863d0d9494cb526af0e2ae9483`)

## 1. Issue Grouping and Deduplication Summary

All 10 carried-forward finding IDs from Cycle 5 Stage 4 (`carry_forward_ids`: 3 actionable `open` findings across 3 community records, plus 7 source-limited `deferred` findings across 7 community records) were grouped by shared root cause and repair ownership and deduplicated against real GitHub issues in `CultureBotAI/CommunityMech`:

| Group ID | Shared Root Cause & Repair Ownership | GitHub Issue | Action | Finding IDs | Target Records | Disposition |
|---|---|---|---|---|---|---|
| `cm-c05-s05-g001` | Omitted source-backed taxonomic `functional_role` / `abundance_level` enums across taxa on `CommunityMech:000084`, `CommunityMech:000085`, and `CommunityMech:000385`, plus omitted `environmental_factors` (`1% (w/v) sucrose`) on `CommunityMech:000084` and `CommunityMech:000085`. Repair owner: `kb/communities/` + `history/records/` + `reports/causal_graph_review/` + `tests/test_causal_review_batch97.py` + `docs/`. | [#2105](https://github.com/CultureBotAI/CommunityMech/issues/2105) | `created` | `c5s4-000084-smutans-ssputigena-roles-abundance-and-sucrose`, `c5s4-000085-smutans-vparvula-roles-abundance-and-sucrose`, `c5s4-000385-so3-bs3-bsubtilis-functional-role` | `CommunityMech:000084`, `CommunityMech:000085`, `CommunityMech:000385` | `resolved` |
| `cm-c05-s05-g002` | Source-limited full-text co-culture assay tables for cheese rind model community (`PMID:25043025`). | [#765](https://github.com/CultureBotAI/CommunityMech/issues/765) | `reused` | `cheese-assay-evidence-gap` | `CommunityMech:000153` | `deferred` |
| `cm-c05-s05-g003` | Source-limited full-text strain-pair exometabolite tables for GLBRC transwell SynCom (`PMID:38329909`). | [#1467](https://github.com/CultureBotAI/CommunityMech/issues/1467) | `reused` | `communitymech-1467-source-discrepancy-and-extension` | `CommunityMech:000091` | `deferred` |
| `cm-c05-s05-g004` | Source-limited paywalled full-text enzyme assay parameters for Okeke-Lu cellulolytic consortium (`PMID:21319991`). | [#1657](https://github.com/CultureBotAI/CommunityMech/issues/1657) | `reused` | `okeke-fulltext-assay-gap` | `CommunityMech:000048` | `deferred` |
| `cm-c05-s05-g005` | Source-limited full-text secondary bacterial satellite interaction data for *Parachlorella*–*Saccharomyces* co-culture (`PMID:35101850`). | [#1681](https://github.com/CultureBotAI/CommunityMech/issues/1681) | `reused` | `parachlorella-remaining-research` | `CommunityMech:000295` | `deferred` |
| `cm-c05-s05-g006` | Source-limited full-text heterotrophic co-isolate tables for *Phormidium* alkaline consortium (`PMID:29138632`). | [#1699](https://github.com/CultureBotAI/CommunityMech/issues/1699) | `reused` | `communitymech-1699-coverage` | `CommunityMech:000054` | `deferred` |
| `cm-c05-s05-g007` | Source-limited full-text supplementary strain tables for sulfide spring CPR biofilm (`PMID:41606024`). | [#1841](https://github.com/CultureBotAI/CommunityMech/issues/1841) | `reused` | `communitymech-1841` | `CommunityMech:000222` | `deferred` |
| `cm-c05-s05-g008` | Source-limited full-text 18-isolate membership and media tables for sugarcane stress-resilience SynCom MetG2 (`PMID:41908926`). | [#1847](https://github.com/CultureBotAI/CommunityMech/issues/1847) | `reused` | `communitymech-1847-metg2-membership` | `CommunityMech:000302` | `deferred` |

## 2. Remediated Records and Provenance Sidecars

1. `kb/communities/SMutans_SSputigena_ECC_Pathobiont.yaml` (`CommunityMech:000084`) — Added `functional_role: [PRIMARY_DEGRADER, CROSS_FEEDER]` and `abundance_level: ABUNDANT` on `Streptococcus mutans` (`NCBITaxon:1309`), `functional_role: [SYNTROPHIC_PARTNER, CROSS_FEEDER]` on `Selenomonas sputigena` (`NCBITaxon:69823`), and `environmental_factors` for `Sucrose availability` (`1% (w/v) sucrose in brain heart infusion (BHIS) medium`) backed by verbatim snippets from `PMID:37217495`; provenance sidecar `history/records/SMutans_SSputigena_ECC_Pathobiont/2026-11-04T054500Z-antigravity-2105.yaml`.
2. `kb/communities/SMutans_VParvula_ASC_Biofilm.yaml` (`CommunityMech:000085`) — Added `functional_role: [PRIMARY_DEGRADER, CROSS_FEEDER]` and `abundance_level: ABUNDANT` on `Streptococcus mutans` (`NCBITaxon:1309`), `functional_role: [SYNTROPHIC_PARTNER, CROSS_FEEDER]` on `Veillonella parvula` (`NCBITaxon:29466`), and `environmental_factors` for `Sucrose availability` (`1% (w/v) sucrose in BHI broth`) backed by verbatim snippets from `PMID:39345197`; provenance sidecar `history/records/SMutans_VParvula_ASC_Biofilm/2026-11-04T054500Z-antigravity-2105.yaml`.
3. `kb/communities/SO3_BS3_Lithium_Battery_Bioleaching_Consortium.yaml` (`CommunityMech:000385`) — Added `functional_role: [SYNTROPHIC_PARTNER, CROSS_FEEDER]` on `Bacillus subtilis 168 (BS3)` (`NCBITaxon:224308`) backed by verbatim snippets from `PMID:42733304` (`doi:10.1002/advs.77699`); provenance sidecar `history/records/SO3_BS3_Lithium_Battery_Bioleaching_Consortium/2026-11-04T054500Z-antigravity-2105.yaml`.
