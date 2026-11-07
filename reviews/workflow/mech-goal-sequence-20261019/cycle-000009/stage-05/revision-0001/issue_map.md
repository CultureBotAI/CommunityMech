# Cycle 9 Stage 5 Grouped Issue Map and Finding Dispositions

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `9` (`cycle-000009`)
- **Stage**: `5` (`resolve_review_findings`, `revision-0001`)
- **Repository**: `CultureBotAI/CommunityMech`
- **Consumed Stage 4 Evidence**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000009/stage-04/revision-0001/evidence.yaml` (`1da63dcbd733c73c2a821d46dfa0a19d6c9edd5440443c53edcca3d0b62c73b7`)
- **Successor Structured Review**: `reviews/structured/20261107T062000Z-c9s5-remediation-verification-r2/review.yaml` (`c13deb20f1ff3dcfb993e90d9856d772519f512ea0aee14733246d4c5e40bb7e`)

## 1. Issue Grouping and Deduplication Summary

All 10 carried-forward finding IDs from Cycle 9 Stage 4 (`carry_forward_ids`: 3 actionable `open` findings across 3 community records, plus 7 source-limited `deferred` findings across 7 community records) were grouped by shared root cause and repair ownership and deduplicated against real GitHub issues in `CultureBotAI/CommunityMech`:

| Group ID | Shared Root Cause & Repair Ownership | GitHub Issue | Action | Finding IDs | Target Records | Disposition |
|---|---|---|---|---|---|---|
| `cm-c09-s05-g001` | Omitted source-backed taxonomic `abundance_level` enums across 6 taxonomic entries on `CommunityMech:000331`, `CommunityMech:000455`, and `CommunityMech:000461`. Repair owner: `kb/communities/` + `history/records/` + `reports/causal_graph_review/` + `tests/` + `docs/communities/`. | [#2713](https://github.com/CultureBotAI/CommunityMech/issues/2713) | `created` | `c9s4-000331-pseudomonas-paracoccus-abundance-levels`, `c9s4-000455-ecoli-arg-met-abundance-levels`, `c9s4-000461-pseudomonas-acidovorax-abundance-levels` | `CommunityMech:000331`, `CommunityMech:000455`, `CommunityMech:000461` | `resolved` |
| `cm-c09-s05-g002` | Source-limited full-text co-culture assay tables for cheese rind model community (`PMID:25043025`). | [#765](https://github.com/CultureBotAI/CommunityMech/issues/765) | `reused` | `cheese-assay-evidence-gap` | `CommunityMech:000153` | `deferred` |
| `cm-c09-s05-g003` | Source-limited full-text strain-pair exometabolite tables for GLBRC transwell SynCom (`PMID:38329909`). | [#1467](https://github.com/CultureBotAI/CommunityMech/issues/1467) | `reused` | `communitymech-1467-source-discrepancy-and-extension` | `CommunityMech:000091` | `deferred` |
| `cm-c09-s05-g004` | Source-limited paywalled full-text enzyme assay parameters for Okeke-Lu cellulolytic consortium (`PMID:21319991`). | [#1657](https://github.com/CultureBotAI/CommunityMech/issues/1657) | `reused` | `okeke-fulltext-assay-gap` | `CommunityMech:000048` | `deferred` |
| `cm-c09-s05-g005` | Source-limited full-text secondary bacterial satellite interaction data for *Parachlorella*–*Saccharomyces* co-culture (`PMID:35101850`). | [#1681](https://github.com/CultureBotAI/CommunityMech/issues/1681) | `reused` | `parachlorella-remaining-research` | `CommunityMech:000295` | `deferred` |
| `cm-c09-s05-g006` | Source-limited full-text heterotrophic co-isolate tables for *Phormidium* alkaline consortium (`PMID:29138632`). | [#1699](https://github.com/CultureBotAI/CommunityMech/issues/1699) | `reused` | `communitymech-1699-coverage` | `CommunityMech:000054` | `deferred` |
| `cm-c09-s05-g007` | Source-limited full-text supplementary strain tables for sulfide spring CPR biofilm (`PMID:41606024`). | [#1841](https://github.com/CultureBotAI/CommunityMech/issues/1841) | `reused` | `communitymech-1841` | `CommunityMech:000222` | `deferred` |
| `cm-c09-s05-g008` | Source-limited full-text 18-isolate membership and media tables for sugarcane stress-resilience SynCom MetG2 (`PMID:41908926`). | [#1847](https://github.com/CultureBotAI/CommunityMech/issues/1847) | `reused` | `communitymech-1847-metg2-membership` | `CommunityMech:000302` | `deferred` |

## 2. Remediated Records and Provenance Sidecars

1. `kb/communities/Pseudomonas_Paracoccus_Bifenthrin_Degradation_Consortium.yaml` (`CommunityMech:000331`) — Added `abundance_level: DOMINANT` and verbatim two-strain synthetic consortium evidence from `PMID:42269294` (`doi:10.1016/j.jhazmat.2026.142626`) on `Pseudomonas aeruginosa PA` (`NCBITaxon:287`, `taxonomy[0]`) and `Paracoccus pantotrophus PP` (`NCBITaxon:82367`, `taxonomy[1]`); provenance sidecar `history/records/Pseudomonas_Paracoccus_Bifenthrin_Degradation_Consortium/2026-11-07T051500Z-antigravity-2713a1.yaml`.
2. `kb/communities/Ecoli_K12_MG1655_Arg_Met_CrossFeeding_Coculture.yaml` (`CommunityMech:000455`) — Added `abundance_level: DOMINANT` and bracket-free verbatim two-strain obligate mutualistic coculture evidence from `PMID:42592155` (`PMC13463769`, `doi:10.1093/nsr/nwag357`) on `Escherichia coli K-12 MG1655 ΔargA-ΔmetJ` (`NCBITaxon:511145`, `taxonomy[0]`) and `Escherichia coli K-12 MG1655 ΔmetA-ΔargR` (`NCBITaxon:511145`, `taxonomy[1]`); provenance sidecars `history/records/Ecoli_K12_MG1655_Arg_Met_CrossFeeding_Coculture/2026-11-07T051500Z-antigravity-2713a2.yaml` and `history/records/Ecoli_K12_MG1655_Arg_Met_CrossFeeding_Coculture/2026-11-07T061900Z-antigravity-2713a4.yaml`.
3. `kb/communities/Pseudomonas_Acidovorax_Aniline_Degradation_SynCom.yaml` (`CommunityMech:000461`) — Added `abundance_level: DOMINANT` on `Pseudomonas sp. RF` (`NCBITaxon:286`, `taxonomy[0]`) and `abundance_level: ABUNDANT` on `Acidovorax sp. PH` (`NCBITaxon:12916`, `taxonomy[1]`) with verbatim 3:1 inoculation-ratio evidence from `PMID:41900437` (`PMC13029111`, `doi:10.3390/microorganisms14030678`); provenance sidecar `history/records/Pseudomonas_Acidovorax_Aniline_Degradation_SynCom/2026-11-07T051500Z-antigravity-2713a3.yaml`.
