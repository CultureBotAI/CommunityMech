# Cycle 8 Stage 5 Grouped Issue Map and Finding Dispositions

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `8` (`cycle-000008`)
- **Stage**: `5` (`resolve_review_findings`, `revision-0001`)
- **Repository**: `CultureBotAI/CommunityMech`
- **Consumed Stage 4 Evidence**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000008/stage-04/revision-0001/evidence.yaml` (`e4b2e534667c17f56f4eb5d98e2405183262beaa9fabe77aa9eaf7cfc90a2c46`)
- **Successor Structured Review**: `reviews/structured/20261106T114000Z-c8s5-remediation-verification/review.yaml` (`ed51b8045cb6412accc548a2fe6caf122477e3e0dbc1bebf49cd875c9feb5266`)

## 1. Issue Grouping and Deduplication Summary

All 10 carried-forward finding IDs from Cycle 8 Stage 4 (`carry_forward_ids`: 3 actionable `open` findings across 3 community records, plus 7 source-limited `deferred` findings across 7 community records) were grouped by shared root cause and repair ownership and deduplicated against real GitHub issues in `CultureBotAI/CommunityMech`:

| Group ID | Shared Root Cause & Repair Ownership | GitHub Issue | Action | Finding IDs | Target Records | Disposition |
|---|---|---|---|---|---|---|
| `cm-c08-s05-g001` | Omitted source-backed taxonomic `abundance_level` enums across 4 taxonomic entries on `CommunityMech:000210`, `CommunityMech:000359`, and `CommunityMech:000454`. Repair owner: `kb/communities/` + `history/records/` + `reports/causal_graph_review/` + `docs/communities/`. | [#2514](https://github.com/CultureBotAI/CommunityMech/issues/2514) | `created` | `c8s4-000210-zymomonas-ecoli-abundance-levels`, `c8s4-000359-pphet-heterotroph-abundance-level`, `c8s4-000454-thermoleptolyngbya-chelatococcus-abundance-level` | `CommunityMech:000210`, `CommunityMech:000359`, `CommunityMech:000454` | `resolved` |
| `cm-c08-s05-g002` | Source-limited full-text co-culture assay tables for cheese rind model community (`PMID:25043025`). | [#765](https://github.com/CultureBotAI/CommunityMech/issues/765) | `reused` | `cheese-assay-evidence-gap` | `CommunityMech:000153` | `deferred` |
| `cm-c08-s05-g003` | Source-limited full-text strain-pair exometabolite tables for GLBRC transwell SynCom (`PMID:38329909`). | [#1467](https://github.com/CultureBotAI/CommunityMech/issues/1467) | `reused` | `communitymech-1467-source-discrepancy-and-extension` | `CommunityMech:000091` | `deferred` |
| `cm-c08-s05-g004` | Source-limited paywalled full-text enzyme assay parameters for Okeke-Lu cellulolytic consortium (`PMID:21319991`). | [#1657](https://github.com/CultureBotAI/CommunityMech/issues/1657) | `reused` | `okeke-fulltext-assay-gap` | `CommunityMech:000048` | `deferred` |
| `cm-c08-s05-g005` | Source-limited full-text secondary bacterial satellite interaction data for *Parachlorella*–*Saccharomyces* co-culture (`PMID:35101850`). | [#1681](https://github.com/CultureBotAI/CommunityMech/issues/1681) | `reused` | `parachlorella-remaining-research` | `CommunityMech:000295` | `deferred` |
| `cm-c08-s05-g006` | Source-limited full-text heterotrophic co-isolate tables for *Phormidium* alkaline consortium (`PMID:29138632`). | [#1699](https://github.com/CultureBotAI/CommunityMech/issues/1699) | `reused` | `communitymech-1699-coverage` | `CommunityMech:000054` | `deferred` |
| `cm-c08-s05-g007` | Source-limited full-text supplementary strain tables for sulfide spring CPR biofilm (`PMID:41606024`). | [#1841](https://github.com/CultureBotAI/CommunityMech/issues/1841) | `reused` | `communitymech-1841` | `CommunityMech:000222` | `deferred` |
| `cm-c08-s05-g008` | Source-limited full-text 18-isolate membership and media tables for sugarcane stress-resilience SynCom MetG2 (`PMID:41908926`). | [#1847](https://github.com/CultureBotAI/CommunityMech/issues/1847) | `reused` | `communitymech-1847-metg2-membership` | `CommunityMech:000302` | `deferred` |

## 2. Remediated Records and Provenance Sidecars

1. `kb/communities/Zymomonas_Ecoli_Exometabolomics_Obligate_Mutualism.yaml` (`CommunityMech:000210`) — Added `abundance_level: DOMINANT` and verbatim flow-cytometry coculture evidence from `PMID:26885935` (`doi:10.1021/acssynbio.5b00236`) on `Zymomonas mobilis` (`NCBITaxon:542`, `taxonomy[0]`) and `Escherichia coli` (`NCBITaxon:562`, `taxonomy[1]`); provenance sidecar `history/records/Zymomonas_Ecoli_Exometabolomics_Obligate_Mutualism/2026-11-06T113500Z-antigravity-2514a1.yaml`.
2. `kb/communities/PPHET_Hybrid_Photosynthetic_PHB_Microbiome.yaml` (`CommunityMech:000359`) — Added `abundance_level: ABUNDANT` and verbatim 16S community-composition evidence from `PMID:41559821` (`PMC12819161`, `doi:10.1111/1751-7915.70302`) on `non-cyanobacterial WCRM heterotrophs` (`NCBITaxon:2`, `taxonomy[1]`); provenance sidecar `history/records/PPHET_Hybrid_Photosynthetic_PHB_Microbiome/2026-11-06T113500Z-antigravity-2514a2.yaml`.
3. `kb/communities/Thermoleptolyngbya_Chelatococcus_Arsenic_Detoxification_Coculture.yaml` (`CommunityMech:000454`) — Added `abundance_level: DOMINANT` and verbatim mutualistic co-culture evidence from `PMID:42468699` (`doi:10.1016/j.biortech.2026.135440`) on `Chelatococcus sp. XZ-Ab1` (`NCBITaxon:3034027`, `taxonomy[1]`); provenance sidecar `history/records/Thermoleptolyngbya_Chelatococcus_Arsenic_Detoxification_Coculture/2026-11-06T113500Z-antigravity-2514a3.yaml`.
