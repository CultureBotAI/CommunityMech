# Cycle 15 Stage 5 (`resolve_review_findings`) — Issue Map & Dispositions

- **Workflow**: `mech-goal-sequence-20261019` (`workflow_sha256: da1b2e24658661009a442096e706eeb4fc6cc6b1fd65ae186b0486b222e8d54e`)
- **Stage**: Cycle 15, Stage 5 (`resolve_review_findings`)
- **Base Commit (`main`)**: `9a4d365ff379709b8aa929c06ae12b58f7c4f233`
- **Consumed Stage 4 Evidence**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000015/stage-04/revision-0001/evidence.yaml` (`sha256: 7bba855f8f07c1a2a143e059530262266eae69bf0289dd14fa57ca50d487d5e6`)
- **Consumed Stage 4 Structured Review Bundles**:
  - `reviews/structured/20261111T121000Z-c15s4-record-deep-audit/review.yaml` (`sha256: d6273b3c8723adc01ea4d71bc589e99bb8952da3cbd9067c6a0680979a4e7c71`)
  - `reviews/structured/20261111T121100Z-c15s4-frozen-cohort-review/review.yaml` (`sha256: eb128b1376f8cb1b7d91f1c8bd2e2a57b6839cca122b89695a8d35dbde6d660f`)
- **Fresh Post-Remediation Verification Review Bundle**:
  - `reviews/structured/20261111T143500Z-c15s5-remediation-verification/review.yaml`
  - `reviews/structured/20261111T143500Z-c15s5-remediation-verification/review.md`

---

## 1. Issue Group Summary (`9` Groups, `12` Findings: `2` Resolved, `10` Deferred)

| Group ID | Cause & Repair Ownership | Finding IDs | Target IDs | GitHub Issue | Action | Disposition |
|---|---|---|---|---|---|---|
| `cm-c15-s05-g001` | Actionable taxonomic `abundance_level` and SynCom simplification / equal-volume assembly evidence completeness across `Tomato_Oxylipin_SynCom3` (`CommunityMech:000107`) and `Clostridial_isoDCA_Mini_Consortium` (`CommunityMech:000396`) | `c15s4-000107-tomato-oxylipin-syncom3-abundance-levels`, `c15s4-000396-clostridial-isodca-mini-consortium-abundance-levels` | `CommunityMech:000107`, `CommunityMech:000396` | [#2764](https://github.com/CultureBotAI/CommunityMech/issues/2764) | `created` | `resolved` |
| `cm-c15-s05-g002` | Schema vocabulary gap: `FunctionalRoleEnum` lacks a heavy-metal-immobilizer / metal-detoxifier value (`PRIMARY_DEGRADER` is defined as `'Degrades complex substrates'` and must not be forced onto inorganic Cd2+ immobilization via CdS bioprecipitation and biosorption, `#301`) | `c12s4-000374-achromobacter-enterobacter-sl8-sl12-functional-roles`, `c12s4-000533-achromobacter-sl8-isolate-functional-role`, `c12s4-000534-enterobacter-sl12-isolate-functional-role` | `CommunityMech:000374`, `CommunityMech:000533`, `CommunityMech:000534` | [#2194](https://github.com/CultureBotAI/CommunityMech/issues/2194) | `reused` | `deferred` |
| `cm-c15-s05-g003` | Source-limited full-text assay table gap on `Cheese_Rind_InSitu_InVitro_Model_Community` (`PMID:25043025`) | `cheese-assay-evidence-gap` | `CommunityMech:000153` | [#765](https://github.com/CultureBotAI/CommunityMech/issues/765) | `reused` | `deferred` |
| `cm-c15-s05-g004` | Source-limited full-text 18-species campaign table reconciliation on `GLBRC_Exometabolite_Transwell_SynCom` | `communitymech-1467-source-discrepancy-and-extension` | `CommunityMech:000091` | [#1467](https://github.com/CultureBotAI/CommunityMech/issues/1467) | `reused` | `deferred` |
| `cm-c15-s05-g005` | Paywalled primary full-text enzyme assay parameters on `Okeke_Lu_Cellulolytic_Consortium` | `okeke-fulltext-assay-gap` | `CommunityMech:000048` | [#1657](https://github.com/CultureBotAI/CommunityMech/issues/1657) | `reused` | `deferred` |
| `cm-c15-s05-g006` | Source-limited full-text secondary metabolite exchange kinetics on `Parachlorella_Saccharomyces_Mutualistic_Coculture` | `parachlorella-remaining-research` | `CommunityMech:000295` | [#1681](https://github.com/CultureBotAI/CommunityMech/issues/1681) | `reused` | `deferred` |
| `cm-c15-s05-g007` | Source-limited full-text heterotrophic isolate inventory on `Phormidium_Alkaline_Consortium` | `communitymech-1699-coverage` | `CommunityMech:000054` | [#1699](https://github.com/CultureBotAI/CommunityMech/issues/1699) | `reused` | `deferred` |
| `cm-c15-s05-g008` | Source-limited lower-rank MAG/isolate strain table gap on `Sulfide_Spring_Autotrophic_CPR_Biofilm` | `communitymech-1841` | `CommunityMech:000222` | [#1841](https://github.com/CultureBotAI/CommunityMech/issues/1841) | `reused` | `deferred` |
| `cm-c15-s05-g009` | Source-limited full-text isolate membership and host-assay table gap on `SynCom_MetG2_Rhizobacteria_Sugarcane_Stress_Resilience` | `communitymech-1847-metg2-membership` | `CommunityMech:000302` | [#1847](https://github.com/CultureBotAI/CommunityMech/issues/1847) | `reused` | `deferred` |

---

## 2. Remediated Findings (`cm-c15-s05-g001`, Issue [#2764](https://github.com/CultureBotAI/CommunityMech/issues/2764))

1. **`c15s4-000107-tomato-oxylipin-syncom3-abundance-levels` (`CommunityMech:000107`)**:
   - **Canonical Record**: `kb/communities/Tomato_Oxylipin_SynCom3.yaml` (`sha256`: `228468ac43630c33939dd4b0708476ef4006c9af7dbf1f108e7f88c36b0962c3` -> `669727f7a8769544676e97fed7dc5f26c4b8532364d530aad06922d166766586`)
   - **History Sidecar**: `history/records/Tomato_Oxylipin_SynCom3/2026-11-11T143000Z-antigravity-2764a1.yaml`
   - **Native Writer Remediation**: Routed through `communitymech.curate.curation_event.record_curation_event(..., llm_assisted=True)` and `communitymech.validation.write_validated.write_validated_community`. Populated `abundance_level: DOMINANT`, `abundance_value: "Core member of simplified three-species tomato rhizosphere SynCom (1 phytopathogen-inducible + 2 stably-colonizing species)"`, and verbatim `PMID:37549573` (`doi:10.1016/j.plaphy.2023.107941`) three-species SynCom simplification evidence across `Asticcacaulis sp.` (`taxonomy[0]`, `NCBITaxon:76890`), `Arachidicoccus sp.` (`taxonomy[1]`, `NCBITaxon:1769012`), and `Phenylobacterium sp.` (`taxonomy[2]`, `NCBITaxon:20`) while preserving `discussions[0]`.
2. **`c15s4-000396-clostridial-isodca-mini-consortium-abundance-levels` (`CommunityMech:000396`)**:
   - **Canonical Record**: `kb/communities/Clostridial_isoDCA_Mini_Consortium.yaml` (`sha256`: `bb785ba51ceecbd2b3eccdee982413f11baf5df7f5f33f180dc9a9a49ef4363d` -> `29b4497d74eb6468140ad7bd01f17abbfe16454de2aa15db866daf89f4f33566`)
   - **History Sidecar**: `history/records/Clostridial_isoDCA_Mini_Consortium/2026-11-11T143005Z-antigravity-2764a2.yaml`
   - **Native Writer Remediation**: Routed through `communitymech.curate.curation_event.record_curation_event(..., llm_assisted=True)` and `communitymech.validation.write_validated.write_validated_community`. Populated `abundance_level: DOMINANT` and verbatim `doi:10.64898/2026.08.11.743107` equal-volume (`10 mL : 10 mL` at `OD600 = 0.800`) consortium assembly evidence on `Peptacetobacter hiranonis` (`taxonomy[0]`, `NCBITaxon:89152`) and `Ruminococcus gnavus VPI C7-9 WT` (`taxonomy[1]`, `NCBITaxon:33038`) while preserving `discussions[0]`.
