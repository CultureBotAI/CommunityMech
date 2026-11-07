# Cycle 10 Stage 5 Grouped Issue Map and Finding Dispositions

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `10` (`cycle-000010`)
- **Stage**: `5` (`resolve_review_findings`, `revision-0001`)
- **Repository**: `CultureBotAI/CommunityMech`
- **Consumed Stage 4 Evidence**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000010/stage-04/revision-0001/evidence.yaml` (`ab829e0e09a5703f823bb8629e8073d53e0d3cddc90ef92134668a70148289c3`)
- **Successor Structured Review**: `reviews/structured/20261107T202000Z-c10s5-remediation-verification-r2/review.yaml` (`f388e7743bbde0e5954ea32d4a0a9956d3f030d79371ab985e374fe7d8e936f2`)

## 1. Issue Grouping and Deduplication Summary

All 10 carried-forward finding IDs from Cycle 10 Stage 4 (`carry_forward_ids`: 3 actionable `open` findings across 3 community records, plus 7 source-limited `deferred` findings across 7 community records) were grouped by shared root cause and repair ownership and deduplicated against real GitHub issues in `CultureBotAI/CommunityMech`:

| Group ID | Shared Root Cause & Repair Ownership | GitHub Issue | Action | Finding IDs | Target Records | Disposition |
|---|---|---|---|---|---|---|
| `cm-c10-s05-g001` | Omitted source-backed taxonomic `abundance_level` enums across 6 taxonomic entries on `CommunityMech:000052`, `CommunityMech:000092`, and `CommunityMech:000162`. Repair owner: `kb/communities/` + `history/records/` + `reports/causal_graph_review/` + `tests/` + `docs/communities/`. | [#2723](https://github.com/CultureBotAI/CommunityMech/issues/2723) | `created` | `c10s4-000052-pelotomaculum-methanothermobacter-abundance-levels`, `c10s4-000092-rhodopseudomonas-ecoli-abundance-levels`, `c10s4-000162-thalassiosira-ruegeria-abundance-levels` | `CommunityMech:000052`, `CommunityMech:000092`, `CommunityMech:000162` | `resolved` |
| `cm-c10-s05-g002` | Source-limited full-text co-culture assay tables for cheese rind model community (`PMID:25043025`). | [#765](https://github.com/CultureBotAI/CommunityMech/issues/765) | `reused` | `cheese-assay-evidence-gap` | `CommunityMech:000153` | `deferred` |
| `cm-c10-s05-g003` | Source-limited full-text strain-pair exometabolite tables for GLBRC transwell SynCom (`PMID:38329909`). | [#1467](https://github.com/CultureBotAI/CommunityMech/issues/1467) | `reused` | `communitymech-1467-source-discrepancy-and-extension` | `CommunityMech:000091` | `deferred` |
| `cm-c10-s05-g004` | Source-limited paywalled full-text enzyme assay parameters for Okeke-Lu cellulolytic consortium (`PMID:21319991`). | [#1657](https://github.com/CultureBotAI/CommunityMech/issues/1657) | `reused` | `okeke-fulltext-assay-gap` | `CommunityMech:000048` | `deferred` |
| `cm-c10-s05-g005` | Source-limited full-text secondary bacterial satellite interaction data for *Parachlorella*–*Saccharomyces* co-culture (`PMID:35101850`). | [#1681](https://github.com/CultureBotAI/CommunityMech/issues/1681) | `reused` | `parachlorella-remaining-research` | `CommunityMech:000295` | `deferred` |
| `cm-c10-s05-g006` | Source-limited full-text heterotrophic co-isolate tables for *Phormidium* alkaline consortium (`PMID:29138632`). | [#1699](https://github.com/CultureBotAI/CommunityMech/issues/1699) | `reused` | `communitymech-1699-coverage` | `CommunityMech:000054` | `deferred` |
| `cm-c10-s05-g007` | Source-limited full-text supplementary strain tables for sulfide spring CPR biofilm (`PMID:41606024`). | [#1841](https://github.com/CultureBotAI/CommunityMech/issues/1841) | `reused` | `communitymech-1841` | `CommunityMech:000222` | `deferred` |
| `cm-c10-s05-g008` | Source-limited full-text 18-isolate membership and media tables for sugarcane stress-resilience SynCom MetG2 (`PMID:41908926`). | [#1847](https://github.com/CultureBotAI/CommunityMech/issues/1847) | `reused` | `communitymech-1847-metg2-membership` | `CommunityMech:000302` | `deferred` |

## 2. Remediated Records and Provenance Sidecars

1. `kb/communities/Pelotomaculum_Methanothermobacter_Syntrophy.yaml` (`CommunityMech:000052`) — Added `abundance_level: DOMINANT` and verbatim two-member syntrophic co-culture evidence from `PMID:12361280` (`doi:10.1099/00207713-52-5-1729`) on `Pelotomaculum thermopropionicum` (`NCBITaxon:110500`, `taxonomy[0]`) and `Methanothermobacter thermautotrophicus` (`NCBITaxon:145262`, `taxonomy[1]`) while preserving `discussions[0]` (`si-deltah-fulltext-and-feedback`); provenance sidecar `history/records/Pelotomaculum_Methanothermobacter_Syntrophy/2026-11-07T193300Z-antigravity-2723a1.yaml`.
2. `kb/communities/Rhodopseudomonas_Ecoli_CrossFeeding_Coculture.yaml` (`CommunityMech:000092`) — Added `abundance_level: DOMINANT` and verbatim two-member reciprocal cross-feeding coculture evidence from `PMID:32788711` (`PMC7784955`, `doi:10.1038/s41396-020-00737-5`) on `Rhodopseudomonas palustris` (`NCBITaxon:1076`, `taxonomy[0]`) and `Escherichia coli` (`NCBITaxon:562`, `taxonomy[1]`) while preserving `discussions[0]` (`reciprocal_exchange_strain_context`); provenance sidecar `history/records/Rhodopseudomonas_Ecoli_CrossFeeding_Coculture/2026-11-07T193310Z-antigravity-2723a2.yaml`.
3. `kb/communities/Thalassiosira_Ruegeria_Phycosphere_Coculture.yaml` (`CommunityMech:000162`) — Added `abundance_level: DOMINANT` and verbatim two-member marine phytoplankton-bacterium model coculture evidence from `PMID:28631440` (`doi:10.1111/1462-2920.13834`) on `Thalassiosira pseudonana CCMP1335` (`NCBITaxon:296543`, `taxonomy[0]`) and `Ruegeria pomeroyi DSS-3` (`NCBITaxon:246200`, `taxonomy[1]`) while preserving `discussions[0]` (`ruegeria-recognition-mediation-and-b12-extension`); provenance sidecar `history/records/Thalassiosira_Ruegeria_Phycosphere_Coculture/2026-11-07T193320Z-antigravity-2723a3.yaml`.
