# M5 CommunityMech stopped-work scope reconstruction

Generated 2026-11-14T21:13:47.865822+00:00; current revision `76aa644cd6803ea2c9545d4c704276ede219d354`.

The unfinished scientific scope is the four maintained records changed by PR #2102. The retained session explicitly superseded its original all-unreviewed-record goal, skipped batches 17–46, and completed the 15-PR publication phase. The last ten-record publication batch does not define the remaining scientific work.

PR #2102 had already merged as `b0a9df35188b40081a3ba8f354ee3b024f8276ad`. Its partial audit stopped after the separate corpus reference check reproduced issue #622 on unchanged record 000219; the handoff retained #2700–#2710 and #1548. These are historical findings, reconciled against the current GitHub states below.

## Frozen scientific target set

| Record | Maintained path | Changed since stopped checkout |
| --- | --- | --- |
| CommunityMech:000516 | `kb/communities/Brachypodium_Natural_Variation_Dopamine_SynCom16.yaml` | False |
| CommunityMech:000025 | `kb/communities/EcoFAB_Ring_Trial_SynCom17.yaml` | False |
| CommunityMech:000087 | `kb/communities/LBNL_Switchgrass_Soil_SynCom16.yaml` | False |
| CommunityMech:000515 | `kb/communities/Yolo_Silt_Loam_Soil_Dopamine_Amendment_Microcosm.yaml` | False |

## Surviving EcoFAB review

`reviews/structured/20261106T211930Z-ecofab-ring-trial-current-main/review.yaml` remains the authoritative retained review. It records four old open curation findings plus a fifth cache-header finding despite eight focused checks passing. Its original Git base is `31c456d35d214662bf435750b783a762d59a22df`.

- `cm-000025-causal-role-evidence` (major; #1427): Treatment outcomes exceed member-specific causal/role evidence.
- `cm-000025-study-stage-scope` (major; #1427): Ring trial, related nitrogen/light studies and preparation assays conflated.
- `cm-000025-grounding-provenance` (minor; #2674): OAP107 rank refinement and unsupported mapping build/latest wording.
- `cm-000025-genome-identifiers` (minor; #2675): Genome pseudo-range omits OAE908 Gp0440934 and is not all17 projects.
- `cm-000025-cache-content-type` (minor; #2676): Two abstract_only headers contradict appended full-main content.

The exact target and two cited cache files were compared byte-for-byte with the stopped revision; the JSON records hashes and change flags. Technical checks and provenance-only review bundles do not resolve scientific findings.

## Current issue and linked PR state

Read from GitHub at 2026-11-14T21:11:36.438474+00:00. Closed states require separate acceptance verification before being treated as resolved.

| Issue | State | Subject | Linked closing PRs |
| --- | --- | --- | --- |
| [#622](https://github.com/CultureBotAI/CommunityMech/issues/622) | OPEN | validate-references silently strips [bracketed] text from snippets before matching | None returned by GitHub closure linkage |
| [#1427](https://github.com/CultureBotAI/CommunityMech/issues/1427) | OPEN | EcoFAB SynCom17 metadata: disentangle ring-trial, isolate and nitrogen-study protocols | None returned by GitHub closure linkage |
| [#1548](https://github.com/CultureBotAI/CommunityMech/issues/1548) | OPEN | Resolve LBNL strain rosters and non-graph mechanism and protocol metadata | None returned by GitHub closure linkage |
| [#2429](https://github.com/CultureBotAI/CommunityMech/issues/2429) | OPEN | Add ontology term slot on EnvironmentalFactor | None returned by GitHub closure linkage |
| [#2430](https://github.com/CultureBotAI/CommunityMech/issues/2430) | OPEN | KGX export of host, soils, and related_communities sections | None returned by GitHub closure linkage |
| [#2674](https://github.com/CultureBotAI/CommunityMech/issues/2674) | OPEN | CommunityMech:000025: Refine OAP107 rank and mapping provenance | None returned by GitHub closure linkage |
| [#2675](https://github.com/CultureBotAI/CommunityMech/issues/2675) | OPEN | CommunityMech:000025: Replace the genome pseudo-range with exact identifiers | None returned by GitHub closure linkage |
| [#2676](https://github.com/CultureBotAI/CommunityMech/issues/2676) | OPEN | CommunityMech:000025: Align two cache content declarations with their actual article payloads | None returned by GitHub closure linkage |
| [#2700](https://github.com/CultureBotAI/CommunityMech/issues/2700) | OPEN | PR #2102: Computed community membership collapses distinct stocks with the same local strain name | None returned by GitHub closure linkage |
| [#2701](https://github.com/CultureBotAI/CommunityMech/issues/2701) | OPEN | PR #2102: Strict validation does not enforce the new host interaction boundary | None returned by GitHub closure linkage |
| [#2702](https://github.com/CultureBotAI/CommunityMech/issues/2702) | OPEN | PR #2102: Soil pH accepts a kilogram unit despite its explicit pH-unit contract | None returned by GitHub closure linkage |
| [#2703](https://github.com/CultureBotAI/CommunityMech/issues/2703) | OPEN | PR #2102: New Quantity values accept non-finite measurements | None returned by GitHub closure linkage |
| [#2704](https://github.com/CultureBotAI/CommunityMech/issues/2704) | OPEN | PR #2102: Focused related-community validation resolves a duplicated target ID arbitrarily | None returned by GitHub closure linkage |
| [#2705](https://github.com/CultureBotAI/CommunityMech/issues/2705) | OPEN | PR #2102: Optional soil location coordinates render as empty coordinate pairs | None returned by GitHub closure linkage |
| [#2706](https://github.com/CultureBotAI/CommunityMech/issues/2706) | OPEN | PR #2102: Host developmental-stage qualifiers are dropped from rendered pages | None returned by GitHub closure linkage |
| [#2707](https://github.com/CultureBotAI/CommunityMech/issues/2707) | OPEN | PR #2102: Related-community renderer invents HTML destinations for isolate records | None returned by GitHub closure linkage |
| [#2708](https://github.com/CultureBotAI/CommunityMech/issues/2708) | OPEN | PR #2102: reconcile Ding article cache content-type provenance | None returned by GitHub closure linkage |
| [#2709](https://github.com/CultureBotAI/CommunityMech/issues/2709) | OPEN | PR #2102: remove copied amoA mechanism rationale from 000515 mapping provenance | None returned by GitHub closure linkage |
| [#2710](https://github.com/CultureBotAI/CommunityMech/issues/2710) | OPEN | PR #2102: preserve unresolved host versus microbial mechanism in 000516 | None returned by GitHub closure linkage |

## Reconciliation against current code

All five maintained owner files for the eleven PR #2102 findings are unchanged from the stopped revision: related-community validation, schema, host/soil template, renderer, and Ding article cache. All four maintained target records are also unchanged. No remediation is present in these identified owner files across the compared revision range. This verifies unchanged inputs; the historical synthetic counterexamples and any dependency-mediated behavior have not been rerun here.

## Broader Phase2 work retained separately

- Named treatment arms referenced by abundances/interactions.
- EnvironmentalFactor ontology term slot (existing issue #2429).
- KGX support for host/soils/related_communities (existing issue #2430).
- Issue #1548 strain roster for CommunityMech:000087.

These original implementation requirements remain outside a claim that four scientific assessments and technical QC are complete. Current issue state above must determine which remain open; neither this report nor a green gate implements them.

## Completion evidence required

- Run full required technical QC on current revision and preserve exact commands/results.
- Canary one current record, then independently assess remaining three with primary sources.
- Save immutable native scientific reviews with claim/participant/direction/context evidence.
- Carry exact prior issue keys/occurrences and test each acceptance criterion.
- Reconcile later changes and existing issues; no duplicate issue creation.
- Report broader Phase2 schema/export implementation separately; do not claim it complete.

## Recovery provenance and limits

Source: preserved M5 session. Raw private instructions and the stopped-work handoff are retained separately in ignored working evidence. Public `scope.json` contains excerpt digests, reconstructed scope, target hashes, Git selection and public GitHub facts.
Instruction excerpt SHA256: `b670d34c6cdcec544ec409ad79e4e70d273541f5a14fb2342bbff548429f6934`.
Final handoff excerpt SHA256: `ac8d16aea620dfcb01b688500eded839fe29b86889d1dd6f8d6f51f8f0b92974`.

The original `.temp` directory was inspected with `ls -la`, including hidden and ignored entries; it was empty. Both referenced handoffs are unavailable. No old scratch was recreated or treated as current evidence.

- This scope reconstruction is not a scientific assessment or QC result.
- Closed GitHub state alone does not prove remediation; inspect linked code and evidence.
- Historical scratch evidence is unavailable; retained hashes do not reconstruct missing bytes.
