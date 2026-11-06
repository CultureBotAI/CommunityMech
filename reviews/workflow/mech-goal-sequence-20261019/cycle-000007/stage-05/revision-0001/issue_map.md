# Cycle 7 Stage 5 Grouped Issue Map and Finding Dispositions

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `7` (`cycle-000007`)
- **Stage**: `5` (`resolve_review_findings`, `revision-0001`)
- **Repository**: `CultureBotAI/CommunityMech`
- **Consumed Stage 4 Evidence**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000007/stage-04/revision-0001/evidence.yaml` (`67d488c71265d3f63fa0f697d95cd78e5a4d2ef83ec8a4ce734861c5d6c48de6`)
- **Successor Structured Review**: `reviews/structured/20261105T171000Z-c7s5-remediation-verification/review.yaml` (`1e05838838578c4c17bd6e24742b3d38b882600b38a3ed45fff2eadd222c19fa`)

## 1. Issue Grouping and Deduplication Summary

All 10 carried-forward finding IDs from Cycle 7 Stage 4 (`carry_forward_ids`: 3 actionable `open` findings across 3 community records, plus 7 source-limited `deferred` findings across 7 community records) were grouped by shared root cause and repair ownership and deduplicated against real GitHub issues in `CultureBotAI/CommunityMech`:

| Group ID | Shared Root Cause & Repair Ownership | GitHub Issue | Action | Finding IDs | Target Records | Disposition |
|---|---|---|---|---|---|---|
| `cm-c07-s05-g001` | Omitted source-backed taxonomic `abundance_level` enums across 6 taxonomic entries on `CommunityMech:000146`, `CommunityMech:000190`, and `CommunityMech:000451`. Repair owner: `kb/communities/` + `history/records/` + `reports/causal_graph_review/` + `docs/communities/`. | [#2120](https://github.com/CultureBotAI/CommunityMech/issues/2120) | `created` | `c7s4-000146-anammox-granule-abundance-levels`, `c7s4-000190-pelotomaculum-methanocella-abundance-levels`, `c7s4-000451-auxenochlorella-pseudomonas-sp1-abundance-level` | `CommunityMech:000146`, `CommunityMech:000190`, `CommunityMech:000451` | `resolved` |
| `cm-c07-s05-g002` | Source-limited full-text co-culture assay tables for cheese rind model community (`PMID:25043025`). | [#765](https://github.com/CultureBotAI/CommunityMech/issues/765) | `reused` | `cheese-assay-evidence-gap` | `CommunityMech:000153` | `deferred` |
| `cm-c07-s05-g003` | Source-limited full-text strain-pair exometabolite tables for GLBRC transwell SynCom (`PMID:38329909`). | [#1467](https://github.com/CultureBotAI/CommunityMech/issues/1467) | `reused` | `communitymech-1467-source-discrepancy-and-extension` | `CommunityMech:000091` | `deferred` |
| `cm-c07-s05-g004` | Source-limited paywalled full-text enzyme assay parameters for Okeke-Lu cellulolytic consortium (`PMID:21319991`). | [#1657](https://github.com/CultureBotAI/CommunityMech/issues/1657) | `reused` | `okeke-fulltext-assay-gap` | `CommunityMech:000048` | `deferred` |
| `cm-c07-s05-g005` | Source-limited full-text secondary bacterial satellite interaction data for *Parachlorella*–*Saccharomyces* co-culture (`PMID:35101850`). | [#1681](https://github.com/CultureBotAI/CommunityMech/issues/1681) | `reused` | `parachlorella-remaining-research` | `CommunityMech:000295` | `deferred` |
| `cm-c07-s05-g006` | Source-limited full-text heterotrophic co-isolate tables for *Phormidium* alkaline consortium (`PMID:29138632`). | [#1699](https://github.com/CultureBotAI/CommunityMech/issues/1699) | `reused` | `communitymech-1699-coverage` | `CommunityMech:000054` | `deferred` |
| `cm-c07-s05-g007` | Source-limited full-text supplementary strain tables for sulfide spring CPR biofilm (`PMID:41606024`). | [#1841](https://github.com/CultureBotAI/CommunityMech/issues/1841) | `reused` | `communitymech-1841` | `CommunityMech:000222` | `deferred` |
| `cm-c07-s05-g008` | Source-limited full-text 18-isolate membership and media tables for sugarcane stress-resilience SynCom MetG2 (`PMID:41908926`). | [#1847](https://github.com/CultureBotAI/CommunityMech/issues/1847) | `reused` | `communitymech-1847-metg2-membership` | `CommunityMech:000302` | `deferred` |

## 2. Remediated Records and Provenance Sidecars

1. `kb/communities/Anammox_Granule_Metabolic_Interaction_Community.yaml` (`CommunityMech:000146`) — Added `abundance_level: DOMINANT` on `Brocadia-affiliated anammox bacterium AMX1` (`NCBITaxon:795830`, `taxonomy[0]`), `abundance_level: ABUNDANT` on `Chlorobi-affiliated heterotrophic bacteria` (`NCBITaxon:1090`, `taxonomy[1]`), and `abundance_level: COMMON` on `anammox-granule heterotrophic flanking bacteria` (`NCBITaxon:2`, `taxonomy[2]`) backed by verbatim snippets from `doi:10.1038/ncomms15416` (`PMID:28561030`, `PMC5460018`); provenance sidecar `history/records/Anammox_Granule_Metabolic_Interaction_Community/2026-11-05T165000Z-antigravity-2120a1.yaml`.
2. `kb/communities/Pelotomaculum_Methanocella_Propionate_RNASeq_Coculture.yaml` (`CommunityMech:000190`) — Added `abundance_level: DOMINANT` and verbatim RNA-Seq read-mapping evidence from `PMID:30038609` (`PMC6046458`, `doi:10.3389/fmicb.2018.01551`) on `Pelotomaculum thermopropionicum` (`NCBITaxon:110500`, `taxonomy[0]`) and `Methanocella conradii` (`NCBITaxon:1175444`, `taxonomy[1]`); provenance sidecar `history/records/Pelotomaculum_Methanocella_Propionate_RNASeq_Coculture/2026-11-05T165000Z-antigravity-2120a2.yaml`.
3. `kb/communities/Auxenochlorella_Pseudomonas_Florfenicol_Phycosphere_Coculture.yaml` (`CommunityMech:000451`) — Added `abundance_level: DOMINANT` and verbatim defined-coculture selection evidence from `PMID:41724996` (`PMC13037320`, `doi:10.1186/s40168-026-02335-7`) on `Pseudomonas sp. Pseudomonas_sp1` (`NCBITaxon:306`, `taxonomy[1]`); provenance sidecar `history/records/Auxenochlorella_Pseudomonas_Florfenicol_Phycosphere_Coculture/2026-11-05T165000Z-antigravity-2120a3.yaml`.
