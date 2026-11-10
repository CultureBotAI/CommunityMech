# Cycle 14 Stage 5 (`resolve_review_findings`) — Issue Map & Dispositions

- **Workflow**: `mech-goal-sequence-20261019` (`workflow_sha256: da1b2e24658661009a442096e706eeb4fc6cc6b1fd65ae186b0486b222e8d54e`)
- **Stage**: Cycle 14, Stage 5 (`resolve_review_findings`)
- **Base Commit (`main`)**: `f8be056c7cd6c2daa11658470a0d99d189aedb1f`
- **Consumed Stage 4 Evidence**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000014/stage-04/revision-0001/evidence.yaml` (`sha256: 3f5840dd145008e56bcef47b149fc11f28ea97b38a5f64f0e606ff8c93cc256f`)
- **Consumed Stage 4 Structured Review Bundles**:
  - `reviews/structured/20261110T164500Z-c14s4-record-deep-audit/review.yaml` (`sha256: f5b334e18b16a382cc4d81741d3c998706e14b6a722a1b43b68e75f9f31d21bb`)
  - `reviews/structured/20261110T164600Z-c14s4-frozen-cohort-review/review.yaml` (`sha256: ab93e696d55635208f90f4dbbd91db67c3a830240b3053632e078f85a64d1da0`)
- **Fresh Post-Remediation Verification Review Bundle**:
  - `reviews/structured/20261110T185500Z-c14s5-remediation-verification/review.yaml`
  - `reviews/structured/20261110T185500Z-c14s5-remediation-verification/review.md`

---

## 1. Issue Group Summary (`9` Groups, `12` Findings: `2` Resolved, `10` Deferred)

| Group ID | Cause & Repair Ownership | Finding IDs | Target IDs | GitHub Issue | Action | Disposition |
|---|---|---|---|---|---|---|
| `cm-c14-s05-g001` | Actionable taxonomic `abundance_level` and equal-ratio / equal-density SynCom inoculation evidence completeness across `Tobacco_Chemotactic_Biocontrol_SynCom` (`CommunityMech:000106`) and `Rice_P_Uptake_Intercropping_SynCom4` (`CommunityMech:000110`) | `c14s4-000106-tobacco-chemotactic-syncom-abundance-levels`, `c14s4-000110-rice-p-uptake-intercropping-syncom4-abundance-levels` | `CommunityMech:000106`, `CommunityMech:000110` | [#2755](https://github.com/CultureBotAI/CommunityMech/issues/2755) | `created` | `resolved` |
| `cm-c14-s05-g002` | Schema vocabulary gap: `FunctionalRoleEnum` lacks a heavy-metal-immobilizer / metal-detoxifier value (`PRIMARY_DEGRADER` is defined as `'Degrades complex substrates'` and must not be forced onto inorganic Cd2+ immobilization via CdS bioprecipitation and biosorption, `#301`) | `c12s4-000374-achromobacter-enterobacter-sl8-sl12-functional-roles`, `c12s4-000533-achromobacter-sl8-isolate-functional-role`, `c12s4-000534-enterobacter-sl12-isolate-functional-role` | `CommunityMech:000374`, `CommunityMech:000533`, `CommunityMech:000534` | [#2194](https://github.com/CultureBotAI/CommunityMech/issues/2194) | `reused` | `deferred` |
| `cm-c14-s05-g003` | Source-limited full-text assay table gap on `Cheese_Rind_InSitu_InVitro_Model_Community` (`PMID:25043025`) | `cheese-assay-evidence-gap` | `CommunityMech:000153` | [#765](https://github.com/CultureBotAI/CommunityMech/issues/765) | `reused` | `deferred` |
| `cm-c14-s05-g004` | Source-limited full-text 18-species campaign table reconciliation on `GLBRC_Exometabolite_Transwell_SynCom` | `communitymech-1467-source-discrepancy-and-extension` | `CommunityMech:000091` | [#1467](https://github.com/CultureBotAI/CommunityMech/issues/1467) | `reused` | `deferred` |
| `cm-c14-s05-g005` | Source-limited full-text heterotrophic isolate inventory on `Phormidium_Alkaline_Consortium` | `communitymech-1699-coverage` | `CommunityMech:000054` | [#1699](https://github.com/CultureBotAI/CommunityMech/issues/1699) | `reused` | `deferred` |
| `cm-c14-s05-g006` | Source-limited lower-rank MAG/isolate strain table gap on `Sulfide_Spring_Autotrophic_CPR_Biofilm` | `communitymech-1841` | `CommunityMech:000222` | [#1841](https://github.com/CultureBotAI/CommunityMech/issues/1841) | `reused` | `deferred` |
| `cm-c14-s05-g007` | Source-limited full-text isolate membership and host-assay table gap on `SynCom_MetG2_Rhizobacteria_Sugarcane_Stress_Resilience` | `communitymech-1847-metg2-membership` | `CommunityMech:000302` | [#1847](https://github.com/CultureBotAI/CommunityMech/issues/1847) | `reused` | `deferred` |
| `cm-c14-s05-g008` | Paywalled primary full-text enzyme assay parameters on `Okeke_Lu_Cellulolytic_Consortium` | `okeke-fulltext-assay-gap` | `CommunityMech:000048` | [#1657](https://github.com/CultureBotAI/CommunityMech/issues/1657) | `reused` | `deferred` |
| `cm-c14-s05-g009` | Source-limited full-text secondary metabolite exchange kinetics on `Parachlorella_Saccharomyces_Mutualistic_Coculture` | `parachlorella-remaining-research` | `CommunityMech:000295` | [#1681](https://github.com/CultureBotAI/CommunityMech/issues/1681) | `reused` | `deferred` |

---

## 2. Remediated Findings (`cm-c14-s05-g001`, Issue [#2755](https://github.com/CultureBotAI/CommunityMech/issues/2755))

1. **`c14s4-000106-tobacco-chemotactic-syncom-abundance-levels` (`CommunityMech:000106`)**:
   - **Canonical Record**: `kb/communities/Tobacco_Chemotactic_Biocontrol_SynCom.yaml` (`sha256`: `2d1851c88c385f813706b923eeb0754bf70bbac4dd94fb15369bf5e45317e371` -> `05fbd542d92c9fc17a9538e9ab69804f5a0a4771488110aaee7c70e1d8c4539f`)
   - **History Sidecar**: `history/records/Tobacco_Chemotactic_Biocontrol_SynCom/2026-11-10T185000Z-antigravity-2755a1.yaml`
   - **Native Writer Remediation**: Routed through `communitymech.curate.curation_event.record_curation_event(..., llm_assisted=True)` and `communitymech.validation.write_validated.write_validated_community`. Populated `abundance_level: DOMINANT`, `abundance_value: "5% (v/w) equal-ratio strain inoculation into composite organic fertilizer"`, and verbatim `PMID:40670700` (`doi:10.1007/s00253-025-13547-6`) equal-ratio inoculation evidence across `Pseudomonas sp.` (`taxonomy[0]`, `NCBITaxon:306`) and `Bacillus sp.` (`taxonomy[1]`, `NCBITaxon:1386`) while preserving `discussions[0]`.
2. **`c14s4-000110-rice-p-uptake-intercropping-syncom4-abundance-levels` (`CommunityMech:000110`)**:
   - **Canonical Record**: `kb/communities/Rice_P_Uptake_Intercropping_SynCom4.yaml` (`sha256`: `9a5de564abd6e776d8f8eb5717c5d11d60cdf85a27414c0b58df620fae74dd9e` -> `2f705e42f3bb09abc227b96b636a133d3c82f612203782eb31412be6bea54a0e`)
   - **History Sidecar**: `history/records/Rice_P_Uptake_Intercropping_SynCom4/2026-11-10T185005Z-antigravity-2755a2.yaml`
   - **Native Writer Remediation**: Routed through `communitymech.curate.curation_event.record_curation_event(..., llm_assisted=True)` and `communitymech.validation.write_validated.write_validated_community`. Populated `abundance_level: DOMINANT`, `abundance_value: "1 x 10^8 CFU/g equal-density four-strain SynCom suspension (15 mL injected into sterilized soil)"`, and verbatim `PMID:39684532` (`doi:10.3390/ijms252312819`) isolate selection and equal-density inoculation evidence on `Variovorax paradoxus` (`taxonomy[0]`, `NCBITaxon:34073`), `Novosphingobium subterraneum` (`taxonomy[1]`, `NCBITaxon:48936`), `Hydrogenophaga pseudoflava` (`taxonomy[2]`, `NCBITaxon:47421`), and `Acidovorax sp.` (`taxonomy[3]`, `NCBITaxon:12916`) while preserving `discussions[0]`.
