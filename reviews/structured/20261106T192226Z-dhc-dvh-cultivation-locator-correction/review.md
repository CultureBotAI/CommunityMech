# Correct the Dhc195/DvH cultivation source locator while retaining open curation

- Review: 20261106T192226Z-dhc-dvh-cultivation-locator-correction
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-11-06T19:22:26.372745Z
- Finished UTC: 2026-11-06T19:22:26.994037Z
- Reviewer: codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Correct the 2012 unshaken-culture locator from Discussion paragraph2 to #sec26 direct paragraph5. The statement is supported, and the cultivation omissions remain open. This bounded scientific observation replaces only the cultivation finding occurrence; the four other original findings and their original actions remain active.

## Scope And Provenance

Source-based reassessment of the cultivation finding and its exact source locator only; completion applies to this bounded scope, not a new whole-record scientific certification or canonical repair.

Selection: Exactly CommunityMech:000199 and cm-000199-cultivation; other original findings and the other three records in the frozen context are not superseded.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 04d52194c1e25af2740b7441b4aace0ed8b8f680.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000199 | kb/communities/Dehalococcoides_Desulfovibrio_Lactate_TCE_Syntrophy.yaml | maintained | Dehalococcoides-Desulfovibrio Lactate-Fed TCE Dechlorination Coculture |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000199 | Actual current-target check executed during the preceding read-only pass; target and validator inputs remain unchanged and are frozen here. |
| validate-strict | passed | True | CommunityMech:000199 | Actual current-target check executed during the preceding read-only pass; target and validator inputs remain unchanged and are frozen here. |
| validate-terms | passed | True | CommunityMech:000199 | Actual current-target check executed during the preceding read-only pass; target and validator inputs remain unchanged and are frozen here. |
| validate-references-explained | passed | True | CommunityMech:000199 | Actual current-target check executed during the preceding read-only pass; target and validator inputs remain unchanged and are frozen here. |
| validate-gtdb | passed | True | CommunityMech:000199 | Actual current-target check executed during the preceding read-only pass; target and validator inputs remain unchanged and are frozen here. |
| validate-gtdb-domain | passed | True | CommunityMech:000199 | Actual current-target check executed during the preceding read-only pass; target and validator inputs remain unchanged and are frozen here. |
| validate-history | passed | True | CommunityMech:000199 | Actual current-target check executed during the preceding read-only pass; target and validator inputs remain unchanged and are frozen here. |

## Scientific And Domain Assessments

### Exact culture-source paragraph and treatment separation

evidence: supported. Targets: CommunityMech:000199.

Fresh primary text supports unshaken conditions in Discussion #sec26 direct paragraph5 and the remaining source-bounded cultivation guidance.

This explicitly corrects both the original evidence locator and enrich-cultivation acceptance check. The corrected phrase is: Discussion section #sec26, fifth direct paragraph, states unshaken conditions (the paragraph beginning 'Another possible reason for more robust growth').

### Still-open source-specific cultivation and independent finding heads

completeness: concern. Targets: CommunityMech:000199.

The current target still lacks the bounded culture details. No record change, terminal disposition or status promotion occurs.

The original dvh-roles, dataset-type, omics-evidence and gtdb-provenance heads retain their original complete actions. The shared validate-curation acceptance is repeated here for the cultivation head only.

## Findings

### cultivation: Recover source-specific culture and transfer details

minor / open / confirmed; issue key: cm-000199-cultivation.

The partial lactate/TCE entry omits available vessel, working volume, gas, cobalamin and transfer information. Add bounded study arms without merging the pair, triculture and bioassay conditions.

## Recommended Actions And Acceptance Checks

### enrich-cultivation

Add separate source-specific cultivation details and an access follow-up.

- For PMID21881617, cite Materials and methods → Bacterial cultures and growth conditions: 160 mL serum bottle, 100 mL working volume, N2:CO2 90:10, 100 µg/L cyanocobalamin, initial 195:DvH 10:1, 10% transfers every 10 days for 20 passages with 78 µmol TCE; distinguish the 40 µmol lower-TCE arm. Discussion section #sec26, fifth direct paragraph, states unshaken conditions (the paragraph beginning 'Another possible reason for more robust growth'). The PMC 5 m rendering is not a direct 5 mM quote; Results 500 µmol/100 mL gives 5 mM only by labeled calculation.
- For PMID24463969, cite the sole culture Methods paragraph: 160 mL sealed serum bottle, 100 mL basal medium / 60 mL N2:CO2 90:10, about 0.7 mmol lactate / 77 µmol TCE, 74 nM cobalamin, 34°C, dark, no shaking, and six 3% transfers. Keep the cobalamin-free/DMB/PfR7 comparisons distinct. Do not transfer pure-PfR7 pH 7.5 or Lactobacillus bioassay incubation to the pair.
- Keep PMID28159790 maintenance, acceptor-limited and donor-limited arms separate. Add a dated follow-up that the original main body is now available; preserve the factual historical 2026-10-06 access statement and open ancillary-mechanism uncertainty.

### validate-curation

Validate any separately authorized maintained-record repair.

- Recheck exact strain, assay and treatment scope, then focused schema, strict, term, explained-reference, GTDB/domain and history checks. Run just gen-html and just check-docs-current when canonical curation is authorized.
- Preserve caches, source responses, histories and previous decisions. This review does not authorize record, issue, Git or status mutations.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| current-record | kb/communities/Dehalococcoides_Desulfovibrio_Lactate_TCE_Syntrophy.yaml; growth_media[0], cultivation_setup, discussions[0]; unchanged exact target bytes | supports | The source-specific cultivation omissions remain open; no canonical field is repaired. |
| prior-review | reviews/structured/20261022T044407Z-dehalococcoides-desulfovibrio-record-review/review.yaml; evidence[cultivation].locator and actions[enrich-cultivation].acceptance_checks[0] | supports | The original paragraph-2 locator is wrong. All five scientific findings and their acceptance scopes remain unresolved; only cultivation receives a new open occurrence. |
| culture-2012 | .temp/pr2061/independent-secondary/sources/21881617-main.html; PMID:21881617 / PMC3260503: culture Methods #sec3; Discussion #sec26 fifth direct paragraph, not second; complete scientific narrative and Table1 inspected | supports | The fifth paragraph explicitly describes unshaken conditions. Methods separately supports vessel, working volume, gas, amendments and transfer stages; 5 m typography is not silently normalized into a direct concentration quote. |
| culture-2014 | .temp/pr2061/independent-secondary/sources/24463969-main.html; PMID:24463969 / PMC3993147: #sec2-1 sole direct culture Methods paragraph | supports | Pair and triculture cultivation are source-specific; pure-PfR7 pH and bioassay conditions must not migrate into the pair. |
| culture-2017 | .temp/pr2061/independent-secondary/sources/28159790-main.html; PMID:28159790 / PMC5377507: culture Methods and donor-excess/donor-limited Results | supports | Maintenance, acceptor-limited pair and donor-limited triculture remain separate; the original ancillary-mechanism and threshold limitations are preserved. |
| focused-qc | .temp/pr2061/independent-secondary/000199-focused-checks.json; Seven actual focused commands, with concrete stdout/stderr inputs also frozen | supports | All seven focused schema/strict/terms/references/GTDB/domain/history checks exited0. Their deterministic success is distinct from this source-based locator correction. |
| science-context | .temp/pr2061/independent-secondary/independent-science-four-records.json; Earlier independent read-only pass, frozen before switching to author role | supports | Records the locator defect and bounded scientific source scope. This author does not claim independent approval of the new successor. |

## Limits And Additional Notes

- Historical unpublished scratch inputs were not recovered. Current concrete sources are not reconstructed historical bytes; the original review is immutable.
- No new full-record scientific verdict, source-stage harmonization, full medium recipe reconstruction, raw-data analysis, graph revision or KB edit is claimed.
- 2012/2014/2017 declared supplementary routes returned access/error bodies. This locator and culture finding is supported by the complete primary main text; unread supplements are not claimed inspected.
- The earlier source-reviewer now authors this correction; independent approval must come from another reviewer on the final committed bytes.
- PR #2061 bundle remediation issue #2635; canonical cultivation stays open.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261106T192226Z-dhc-dvh-cultivation-locator-correction
kind: record
repository: CultureBotAI/CommunityMech
title: Correct the Dhc195/DvH cultivation source locator while retaining open curation
started_at: '2026-11-06T19:22:26.372745Z'
finished_at: '2026-11-06T19:22:26.994037Z'
reviewer:
  identity: codex
  kind: agent
  independence: self_review
  independence_basis: Author of this bounded successor after a separate read-only
    science pass. A different reviewer must approve this new document.
skill: review-yaml-record
completion: completed
verdict: needs_curation
scientific_review: true
summary: 'Correct the 2012 unshaken-culture locator from Discussion paragraph2 to
  #sec26 direct paragraph5. The statement is supported, and the cultivation omissions
  remain open. This bounded scientific observation replaces only the cultivation finding
  occurrence; the four other original findings and their original actions remain active.'
source:
  git_revision: 04d52194c1e25af2740b7441b4aace0ed8b8f680
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: d2f94c87b82f59663bc2b0c91ac04a245e56fab52d8c11e6bddb559eb9237c84
    role: context
  - path: .claude/skills/ground-taxa-gtdb/SKILL.md
    sha256: 0f7f4423eca28dd0605784d0a01b0886618d0d0f8f1739acb1aae7702e4560a1
    role: context
  - path: .claude/skills/review-communities/reference/execution-protocol.md
    sha256: 0d4448074611c020c54b6b20c478b24e2cf2a195f7fc4f7dbcfac19134f731c4
    role: context
  - path: .claude/skills/review-communities/reference/metrics-and-reports.md
    sha256: 2647416ac98a8f9569e0afbd826a0d1229bb4262639934848639ce536b0974fc
    role: context
  - path: .claude/skills/review-communities/reference/validation-rules.md
    sha256: 3860e91a64f7c1f55f80e3d7a361d0798bbd00cbaf5cb7720a7533673e5afe2e
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: 1005e1b9eb7f83306a1f88a6d22ec7954a54c2bf2e2fc15923fdaaa1111a3d2b
    role: context
  - path: .temp/pr2061/199-correction/full-lint.json
    sha256: 65a2ce3fcde665d2982e6bc7296240af319b73323a689bd45d8ac0a2d4fd9bd8
    role: context
  - path: .temp/pr2061/199-correction/full-lint.stderr
    sha256: 533312691021c6323d7d34d29c3f8aae5d883973549525221887c00718d3cd0d
    role: context
  - path: .temp/pr2061/199-correction/full-lint.stdout
    sha256: 1cffccf768da50ca84db43e973c69c47f795b57101ebfc1825d52472c790ab4d
    role: context
  - path: .temp/pr2061/199-correction/input-paths.json
    sha256: 67600ea46665dea717ae3dfbbfa408c6d56c612793373cead623e6b1a160c4de
    role: context
  - path: .temp/pr2061/199-correction/started.json
    sha256: f19f2be08b445e344823df1aa4fdff89e271a8e613c985a730ee7bece5a82b36
    role: context
  - path: .temp/pr2061/199-correction/targets.json
    sha256: 295c07c6d13cad59ab7a78da81f5f244f7cded7f0c7cebbb8f67c0dca35b65ca
    role: context
  - path: .temp/pr2061/independent-secondary/000183-focused-checks.json
    sha256: 35da97b002a634d70408d70713035538ba543f57a6cfb754a77516fbcfd96581
    role: context
  - path: .temp/pr2061/independent-secondary/000183-gtdb-ground.stderr
    sha256: ae39576491f839dddd3e4c7e27100098a7308a13b6f1c6358e18837ca96f925e
    role: context
  - path: .temp/pr2061/independent-secondary/000183-gtdb-ground.stdout
    sha256: 98feb4cb208528e1ed8d9599afce368999b8c94187317df4c03e59117ba44cf2
    role: context
  - path: .temp/pr2061/independent-secondary/000183-inspect.json
    sha256: 49d46b2b530aea92ce95e593fe293bf1f5e77c69300dacf65ccbc6fc9ab01a87
    role: context
  - path: .temp/pr2061/independent-secondary/000183-inspect.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/000183-review-sections.json
    sha256: e6a3b7d2a73d8c1cf2cf43ad69a3e75811ee1fbfdf2214e6e71ce52fdd03a6ab
    role: context
  - path: .temp/pr2061/independent-secondary/000183-targets.json
    sha256: c0e32fa3ed16fd8a58097bbfe62d287982faef51b279a9db781d342a6b2dac63
    role: context
  - path: .temp/pr2061/independent-secondary/000183-validate-gtdb-domain.stderr
    sha256: 5704cc1c9c104f5804cd8cb53d605e7295a63723d8231c06bfe64199e82fc3bf
    role: context
  - path: .temp/pr2061/independent-secondary/000183-validate-gtdb-domain.stdout
    sha256: ede937293c42cad366f434dce49a485a9a0c56fe86620b52ca243ad10e09ecae
    role: context
  - path: .temp/pr2061/independent-secondary/000183-validate-gtdb.stderr
    sha256: c92473922fd68943025baec067daceabb17a65b894697607c5934787e0e2736b
    role: context
  - path: .temp/pr2061/independent-secondary/000183-validate-gtdb.stdout
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/000183-validate-history.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/000183-validate-history.stdout
    sha256: de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
    role: context
  - path: .temp/pr2061/independent-secondary/000183-validate-references-explained.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/000183-validate-references-explained.stdout
    sha256: 98674563d11bfd07ec6695a5853009c11374f3c83e8992063c7bafec2b43bca3
    role: context
  - path: .temp/pr2061/independent-secondary/000183-validate-strict.stderr
    sha256: 30954cec5f70f8ebb71948cee733a6120e49294f76b342091ea60de0b66166cb
    role: context
  - path: .temp/pr2061/independent-secondary/000183-validate-strict.stdout
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/000183-validate-terms.stderr
    sha256: 69bd16d2c47b8a8c4e81734d8dc580d027c9c07b8110e27281bf4a5a501890a4
    role: context
  - path: .temp/pr2061/independent-secondary/000183-validate-terms.stdout
    sha256: 23acda1c1d3194d12bc947d897d07de83f4a076a9d93c135148885108530e018
    role: context
  - path: .temp/pr2061/independent-secondary/000183-validate.stderr
    sha256: da2fb1560b945d7d7bd0f530da4f4d0a99ae789ac27f3568109d76856fbb843e
    role: context
  - path: .temp/pr2061/independent-secondary/000183-validate.stdout
    sha256: de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
    role: context
  - path: .temp/pr2061/independent-secondary/000184-focused-checks.json
    sha256: 349147af3095a35529da568ef31264a2fbaaed03b65a90de4b35345edf14978d
    role: context
  - path: .temp/pr2061/independent-secondary/000184-gtdb-ground.stderr
    sha256: 567fdfd97d161fb53a8c0c4f5cb6a81e997019203ae85446df9b3537d40cf83b
    role: context
  - path: .temp/pr2061/independent-secondary/000184-gtdb-ground.stdout
    sha256: b011c614681551b13d98d385f4d2ec4bc12c62fde23b49aa8ddc1281d8701b49
    role: context
  - path: .temp/pr2061/independent-secondary/000184-inspect.json
    sha256: a5e649a640a0395ad536d7836b196301a79ac00ea4f4ff5aeb86287bee029454
    role: context
  - path: .temp/pr2061/independent-secondary/000184-inspect.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/000184-review-sections.json
    sha256: fb62420e351661b421c77468a357dbe9a09536a531750ba1ad92000e8ff82b51
    role: context
  - path: .temp/pr2061/independent-secondary/000184-targets.json
    sha256: ec113130f68b5cca6b21a49a9ae2a263d237915e9a275c717f2743dbef683d12
    role: context
  - path: .temp/pr2061/independent-secondary/000184-validate-gtdb-domain.stderr
    sha256: 7dd7210928ebc82abfc9ddbc125082bbdb52b1286981fddf2ede294c93e2235a
    role: context
  - path: .temp/pr2061/independent-secondary/000184-validate-gtdb-domain.stdout
    sha256: ede937293c42cad366f434dce49a485a9a0c56fe86620b52ca243ad10e09ecae
    role: context
  - path: .temp/pr2061/independent-secondary/000184-validate-gtdb.stderr
    sha256: 2a711c3e55da1a754f4f191043e9d8390aa877177ab0c72a51d084f1e78ff61d
    role: context
  - path: .temp/pr2061/independent-secondary/000184-validate-gtdb.stdout
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/000184-validate-history.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/000184-validate-history.stdout
    sha256: de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
    role: context
  - path: .temp/pr2061/independent-secondary/000184-validate-references-explained.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/000184-validate-references-explained.stdout
    sha256: 9925a51bb71bd49e290e65cf8b195aafed834adbd3c9f40900c0c45af96927d4
    role: context
  - path: .temp/pr2061/independent-secondary/000184-validate-strict.stderr
    sha256: 04c7092b1df528161473af575d6b8eaafb2f98c667b8a68d288bce9c7319e0e5
    role: context
  - path: .temp/pr2061/independent-secondary/000184-validate-strict.stdout
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/000184-validate-terms.stderr
    sha256: f77260ef15494eac1a2c504ceab2e1a2ae7298cd8392b6bb9862ea573a10a38c
    role: context
  - path: .temp/pr2061/independent-secondary/000184-validate-terms.stdout
    sha256: 23acda1c1d3194d12bc947d897d07de83f4a076a9d93c135148885108530e018
    role: context
  - path: .temp/pr2061/independent-secondary/000184-validate.stderr
    sha256: cf81561253734e52fac9756ca31a2bca2a70ac58fc970d68ccbfa864d7e3252b
    role: context
  - path: .temp/pr2061/independent-secondary/000184-validate.stdout
    sha256: de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
    role: context
  - path: .temp/pr2061/independent-secondary/000199-focused-checks.json
    sha256: 39de026943fec95c29128d59cb5939389aca7d7347c31ee9cea4b74a560c35be
    role: context
  - path: .temp/pr2061/independent-secondary/000199-gtdb-ground.stderr
    sha256: aef7f2be6294d74504bedc84c782e56308a288cdd2fcb17a708cfd2de2b747c5
    role: context
  - path: .temp/pr2061/independent-secondary/000199-gtdb-ground.stdout
    sha256: 822c529b06175f48363867985ee7041445864b1ac25580e24131f3321ff3a51d
    role: context
  - path: .temp/pr2061/independent-secondary/000199-inspect.json
    sha256: 99cae00b07521cc21a3fb778445303afef4e8e50d1e2cde65cce612b9b08dded
    role: context
  - path: .temp/pr2061/independent-secondary/000199-inspect.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/000199-review-sections.json
    sha256: 06e348398218f63c7c47c8bd4be71a44abba94b77f9118ef84c292804abd34b7
    role: context
  - path: .temp/pr2061/independent-secondary/000199-targets.json
    sha256: 295c07c6d13cad59ab7a78da81f5f244f7cded7f0c7cebbb8f67c0dca35b65ca
    role: context
  - path: .temp/pr2061/independent-secondary/000199-validate-gtdb-domain.stderr
    sha256: 5046217b1bce2132e0aeeb6c375cc751f5c1dcea92ca41d59f354d39ea999a40
    role: context
  - path: .temp/pr2061/independent-secondary/000199-validate-gtdb-domain.stdout
    sha256: ede937293c42cad366f434dce49a485a9a0c56fe86620b52ca243ad10e09ecae
    role: context
  - path: .temp/pr2061/independent-secondary/000199-validate-gtdb.stderr
    sha256: a01cdaa463953e98d8159c75882af981bce7bc519af99b350fbd01abf0ead2bc
    role: context
  - path: .temp/pr2061/independent-secondary/000199-validate-gtdb.stdout
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/000199-validate-history.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/000199-validate-history.stdout
    sha256: de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
    role: context
  - path: .temp/pr2061/independent-secondary/000199-validate-references-explained.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/000199-validate-references-explained.stdout
    sha256: 57204fdc452e72d676aa3e092379e945c13286ad1c3c899f227e2a611c0485ed
    role: context
  - path: .temp/pr2061/independent-secondary/000199-validate-strict.stderr
    sha256: e773d734327978da58c9b8a41d30c84f7b5cd80a10f660d74e2f98ceb7d43e08
    role: context
  - path: .temp/pr2061/independent-secondary/000199-validate-strict.stdout
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/000199-validate-terms.stderr
    sha256: 1b54d879a6864e6212094977ddcd42231f4c14a2d8402616f81a191a49dff265
    role: context
  - path: .temp/pr2061/independent-secondary/000199-validate-terms.stdout
    sha256: 23acda1c1d3194d12bc947d897d07de83f4a076a9d93c135148885108530e018
    role: context
  - path: .temp/pr2061/independent-secondary/000199-validate.stderr
    sha256: 3625b693e94b45c987183d3ba9f2f15698b86c4a2bbcb6d1946fdb1a7cd9a1de
    role: context
  - path: .temp/pr2061/independent-secondary/000199-validate.stdout
    sha256: de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
    role: context
  - path: .temp/pr2061/independent-secondary/000200-focused-checks.json
    sha256: 18293f1ea07a1884e36334c3a0962f50d871e255cf4fff33011fa860663cbd6c
    role: context
  - path: .temp/pr2061/independent-secondary/000200-gtdb-ground.stderr
    sha256: 0056585d6b9ea14c333b48ba36d9eb666977ca1fb367a74a3aa21cd64e5db63d
    role: context
  - path: .temp/pr2061/independent-secondary/000200-gtdb-ground.stdout
    sha256: 775591ae15b55104a28e1c2360decdcbd852e8367dd38ccb618b2bda161f020a
    role: context
  - path: .temp/pr2061/independent-secondary/000200-inspect.json
    sha256: 72ebbce9e4b1b4240bdf01bed63e84ebb92fc69bb68f2d20de48a892251fa89c
    role: context
  - path: .temp/pr2061/independent-secondary/000200-inspect.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/000200-review-sections.json
    sha256: 764d7ff70adfbc5da5b4242e8b874174260eaf8d51ca560f13e546beca365280
    role: context
  - path: .temp/pr2061/independent-secondary/000200-targets.json
    sha256: 3a01872641cd44905c5b370ee5d46761ee84ad006ea381607c37fd7113e4e529
    role: context
  - path: .temp/pr2061/independent-secondary/000200-validate-gtdb-domain.stderr
    sha256: 360f27ba6f4b8e2c40169e0abef2d018dbe6e93c5afeb48ef01165af56589285
    role: context
  - path: .temp/pr2061/independent-secondary/000200-validate-gtdb-domain.stdout
    sha256: ede937293c42cad366f434dce49a485a9a0c56fe86620b52ca243ad10e09ecae
    role: context
  - path: .temp/pr2061/independent-secondary/000200-validate-gtdb.stderr
    sha256: 2f1e0776b4c64c08dc7ba44541bfad40fe039337928ea45ca5bf774f8d89d8e0
    role: context
  - path: .temp/pr2061/independent-secondary/000200-validate-gtdb.stdout
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/000200-validate-history.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/000200-validate-history.stdout
    sha256: de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
    role: context
  - path: .temp/pr2061/independent-secondary/000200-validate-references-explained.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/000200-validate-references-explained.stdout
    sha256: 82771e901cfc926cff99ef6204c902f2680fd631ce168db2185f53c813ab9431
    role: context
  - path: .temp/pr2061/independent-secondary/000200-validate-strict.stderr
    sha256: 01b90b8b2b290c6d1004e8618e900ad1b324993226cf5152b5a0e39008cc50af
    role: context
  - path: .temp/pr2061/independent-secondary/000200-validate-strict.stdout
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/000200-validate-terms.stderr
    sha256: a8143309ed0bf9b51e09cf8e45e1b9c742f7d8105c15ea002fede8eaf66dcf6b
    role: context
  - path: .temp/pr2061/independent-secondary/000200-validate-terms.stdout
    sha256: 23acda1c1d3194d12bc947d897d07de83f4a076a9d93c135148885108530e018
    role: context
  - path: .temp/pr2061/independent-secondary/000200-validate.stderr
    sha256: 6f7e99c325d6fef1bfffb133192d89e54f96ba9ba62565e8597ee614ff94a6e3
    role: context
  - path: .temp/pr2061/independent-secondary/000200-validate.stdout
    sha256: de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
    role: context
  - path: .temp/pr2061/independent-secondary/cache-name-check.json
    sha256: 20ad5aa58504ff72951bba93c88f6bf11bfea28f149e53111a7c3211577b16de
    role: context
  - path: .temp/pr2061/independent-secondary/cache-name-check.stderr
    sha256: f8f8ac7b3d9cb25e181b606092e1491c8b8bcfbe15fce53e0887fcd2f838eab6
    role: context
  - path: .temp/pr2061/independent-secondary/cache-name-check.stdout
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/cache-name-preflight.json
    sha256: a1b79dcbf003b9f7d02c7212944490bef65e931d696bbb882b86d85edc71e18e
    role: context
  - path: .temp/pr2061/independent-secondary/cache-name-preflight.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/cache-name-preflight.stdout
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/context-and-counts.json
    sha256: af6b3e3b572039405676cd49ebf711deb4efe961d4b4efc8b0f0e40555f30692
    role: context
  - path: .temp/pr2061/independent-secondary/current-science-input-manifest.json
    sha256: e6049798108132dfb0857b5b8cdab6ae0dccdfe0e90026c2c384427c7cb30002
    role: context
  - path: .temp/pr2061/independent-secondary/focused-checks.json
    sha256: 436f8aa52d6c3cfb5146089dcbe0ac5c1cc7d30b4f0622cb962e6363a29cc308
    role: context
  - path: .temp/pr2061/independent-secondary/fresh-snippet-audit-complete.json
    sha256: 635c4e52398291bb149541459b25ca6ee81102112ba2badc6f353f27082c6a3d
    role: context
  - path: .temp/pr2061/independent-secondary/fresh-snippet-audit.json
    sha256: 9af77b18b9d6108035a8705fa2283e921e6e9b1bea54f11512ef62166a5355d3
    role: context
  - path: .temp/pr2061/independent-secondary/gtdb-exact-rows.json
    sha256: 5c89a0868585f8efcaae56a813774b6eb00aaf11dfb3ac58b44e0007f5c35849
    role: context
  - path: .temp/pr2061/independent-secondary/gtdb-ground-receipts.json
    sha256: 086051b4045b507b688eaa572956dbe517008b8329b4ac7b0e6d5ee86719d3af
    role: context
  - path: .temp/pr2061/independent-secondary/gtdb-snapshot.json
    sha256: ac2cb0a4ecf114c7aaceeca38fc669f293977a06f6f3e7191cfc6bee193ffbdd
    role: context
  - path: .temp/pr2061/independent-secondary/independent-science-four-records.json
    sha256: 519313736a8d0415e08badb79b84adb83c7556ac8a927218e9eb4dc8b4d9d568
    role: context
  - path: .temp/pr2061/independent-secondary/initial-inspect-receipt.json
    sha256: 6f773dc2825fa7d76571b0421c985c477b5c58ac5dbffc6b7ee60f87cfd1ae99
    role: context
  - path: .temp/pr2061/independent-secondary/maintained-context-inputs.json
    sha256: e6918cef6c147300e1d1b909ab538bea9365a02c16e1fe0d4142ed4d10f1ae6c
    role: context
  - path: .temp/pr2061/independent-secondary/metrics-recomputed.json
    sha256: 5778af321ab83aed51a50c74c4b18efea03dfd75f3a3f5a1c20f15215fd5c190
    role: context
  - path: .temp/pr2061/independent-secondary/selection.json
    sha256: 7a66a682f3f695509c306137f822e846e8e84dfa2685cf6cd7db29c308d5a996
    role: context
  - path: .temp/pr2061/independent-secondary/sources/184-SI-page2.png
    sha256: 1317d98d33d3411db714247b727943f6c9598815b4aefdf32fce7d4d93069f25
    role: context
  - path: .temp/pr2061/independent-secondary/sources/184-SI-page3.png
    sha256: 8f02cfd41a31aa1dab74e1751edb84f6a4dad221f61c8f3facfe58b515284b4b
    role: context
  - path: .temp/pr2061/independent-secondary/sources/21881617-main.html
    sha256: 1901c5d00dc3894b024df1868610c7ae63eb13b1482195dcf2e67426abd382a1
    role: context
  - path: .temp/pr2061/independent-secondary/sources/21881617-main.html.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/21881617-main.txt
    sha256: ad43e21b3ffc5550eafae94983a55b58d57ab71563feab80b8a980e02c91e9ce
    role: context
  - path: .temp/pr2061/independent-secondary/sources/21881617-main.xml
    sha256: 93d527abeb0d73b6a99c80342a8b7e89caac579791ba18b1843cc66070edbd72
    role: context
  - path: .temp/pr2061/independent-secondary/sources/21881617-main.xml.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/21881617-metadata.json
    sha256: d04abfc1be89b49035e7fb1efef79f204caeb9a54ed48f60950ba593fa7752c0
    role: context
  - path: .temp/pr2061/independent-secondary/sources/21881617-metadata.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/21881617-sections.json
    sha256: 5510db6dfdf9621b59ff1f3c57690de4d7ab743b598e1f11ade777071b5b33a6
    role: context
  - path: .temp/pr2061/independent-secondary/sources/21881617-supp.zip
    sha256: f9656458c028fcf723a426fec10492b8b0e82b40131de16c2b645a626c507fa7
    role: context
  - path: .temp/pr2061/independent-secondary/sources/21881617-supp.zip.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/24015929-metadata.json
    sha256: 213dd90e22591aec8612e69f649c85b553b802154d154d2955c078d49c059a86
    role: context
  - path: .temp/pr2061/independent-secondary/sources/24015929-metadata.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/24463969-main.html
    sha256: 4b15df78b9c312024337e876f7d24aaf97b03bfb58a9af42d9753efbc0f2313c
    role: context
  - path: .temp/pr2061/independent-secondary/sources/24463969-main.html.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/24463969-main.txt
    sha256: 0d9e8ac58501525ca35bc0ded80db42329661679a688d4eb085aae1742b5a34f
    role: context
  - path: .temp/pr2061/independent-secondary/sources/24463969-main.xml
    sha256: 16ed1e445787a30cb396b62b9736704f9bf610136be8bdbb5f8509580aed936d
    role: context
  - path: .temp/pr2061/independent-secondary/sources/24463969-main.xml.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/24463969-metadata.json
    sha256: f32bf76fd162de508232626242d94f98d32570b97e4e543cbc5c1adfdb271ba9
    role: context
  - path: .temp/pr2061/independent-secondary/sources/24463969-metadata.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/24463969-sections.json
    sha256: 15b89f8272c1d50b21d98fbefd85e7cf91bcc222e1948968b37e6be42c7394a5
    role: context
  - path: .temp/pr2061/independent-secondary/sources/24463969-supp.zip
    sha256: 9068fa2d24ea0f8c040a8a34ba0d0fd8b7d82a33387e0b974ea40cfaba8e51d5
    role: context
  - path: .temp/pr2061/independent-secondary/sources/24463969-supp.zip.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/25576615-main.html
    sha256: 01ea90852ac32dc460503d8b77afe2ffa228f219a8413630ce378961007f601b
    role: context
  - path: .temp/pr2061/independent-secondary/sources/25576615-main.html.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/25576615-main.txt
    sha256: 2257889d51c004df204865f384461bd520659b81b30ef51778d3e6cd2cd5fdcd
    role: context
  - path: .temp/pr2061/independent-secondary/sources/25576615-main.xml
    sha256: a89c83caa54b31e35aa85f773708c699c3b48f66d2f01dbef049a1299322c1ee
    role: context
  - path: .temp/pr2061/independent-secondary/sources/25576615-main.xml.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/25576615-metadata.json
    sha256: 1a8bb077a8f00585b4748f76d124e7bff80e3240ceeb56270c964e0d1de2530f
    role: context
  - path: .temp/pr2061/independent-secondary/sources/25576615-metadata.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/25576615-sections.json
    sha256: d96ea622323741f883fdd1d66b5838e78554b830e6d7219efac1fd1fe5351bd3
    role: context
  - path: .temp/pr2061/independent-secondary/sources/25576615-supp.zip
    sha256: daced4ed799b7337d03a58b761035681a8e874ed893c53ce1ba67b72565b9689
    role: context
  - path: .temp/pr2061/independent-secondary/sources/25576615-supp.zip.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/27881975-assets/Image_1.TIF
    sha256: dbcaa5c0924fb969b205ab45c34fb829e2e8c8610b8f6555d4adc5630bf8f968
    role: context
  - path: .temp/pr2061/independent-secondary/sources/27881975-assets/Image_2.PDF
    sha256: 2921979c3c6beda3fbaa13f418c6348be8f4633583c8b8950bb5791098e3c84c
    role: context
  - path: .temp/pr2061/independent-secondary/sources/27881975-assets/Image_3.PDF
    sha256: b85248cb7adf6fd9aa48ac5b0cdce4a8595c92226d0416bea3efa802321002ed
    role: context
  - path: .temp/pr2061/independent-secondary/sources/27881975-assets/Table_1.DOCX
    sha256: c160a609694c74664c01f110cdd27550a134ad72cf024b26a76d6960729ad060
    role: context
  - path: .temp/pr2061/independent-secondary/sources/27881975-assets/Table_1.txt
    sha256: 9be41351fabfeb185e056a981d7e354e5582bb0e8a44b326aeb622c602b23beb
    role: context
  - path: .temp/pr2061/independent-secondary/sources/27881975-assets/Table_2.DOCX
    sha256: 9e6b4c49b3140a01a2908289b210494bd282d372017fcd47124d80734c9e0ce5
    role: context
  - path: .temp/pr2061/independent-secondary/sources/27881975-assets/Table_2.txt
    sha256: 7907a2572546aae11e31d97471d0329b63ba0a2129546e4a766c027f7f92c97a
    role: context
  - path: .temp/pr2061/independent-secondary/sources/27881975-assets/fmicb-07-01795-g001.gif
    sha256: a54564bc71d3b8a35e8c3e4567be3047af19d76c448dd7ccc812d2991cd8fe8b
    role: context
  - path: .temp/pr2061/independent-secondary/sources/27881975-assets/fmicb-07-01795-g001.jpg
    sha256: 52131bc992a061f31e0bbb4f051f3574f7c099cb45edcb769a05f6f0e9d44a54
    role: context
  - path: .temp/pr2061/independent-secondary/sources/27881975-assets/fmicb-07-01795-g002.gif
    sha256: 7aafb83527ad5f66144383edd4f55eb56fad357cd3210b6293ec7be2193eb635
    role: context
  - path: .temp/pr2061/independent-secondary/sources/27881975-assets/fmicb-07-01795-g002.jpg
    sha256: 3469382a2ed1e47e8e8b10d94d6afb6c3a21281e619f9d4f291c6ac30bf9c86a
    role: context
  - path: .temp/pr2061/independent-secondary/sources/27881975-assets/fmicb-07-01795-g003.gif
    sha256: d07cb3f0581f4364ad359c5902a364f69dbf4db4061b62e9ac6143fafc354a4f
    role: context
  - path: .temp/pr2061/independent-secondary/sources/27881975-assets/fmicb-07-01795-g003.jpg
    sha256: 40f549c3030ae17b5227f082a8cf9f8e72342ff9f293082b5140ea978519b319
    role: context
  - path: .temp/pr2061/independent-secondary/sources/27881975-main.txt
    sha256: d560b460d9e91db33f29a037dab30d9620e474baba180f82b099e51e21b24948
    role: context
  - path: .temp/pr2061/independent-secondary/sources/27881975-main.xml
    sha256: c0a3ffbf7ccb4e4bcd9ed0fec153616355ecc933606440d7b6caeb79cd2e6198
    role: context
  - path: .temp/pr2061/independent-secondary/sources/27881975-main.xml.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/27881975-metadata.json
    sha256: e64a34757718ba3b91e9e29a587a2c35d9361df3a53cb5147e29fed08e65312b
    role: context
  - path: .temp/pr2061/independent-secondary/sources/27881975-metadata.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/27881975-sections.json
    sha256: 28a7619124031d4f62e17f4807f087c1f1e84c5f29ad1108a7c9edd952de35b8
    role: context
  - path: .temp/pr2061/independent-secondary/sources/27881975-supp.zip
    sha256: 07073f7ebe8601582b2d422c0eb79d56813ddff68c8852695eab6abbfeafc8ef
    role: context
  - path: .temp/pr2061/independent-secondary/sources/27881975-supp.zip.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/28075122-main.html
    sha256: 8af69a27614109e852947d067df564e5816c71a874610cbc9fd9b1228c9cbaa4
    role: context
  - path: .temp/pr2061/independent-secondary/sources/28075122-main.html.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/28075122-main.txt
    sha256: c4bcb5b9043e341d2b57e8f6202cdb06e9fe435fab540e33707cae0b6f50fdd2
    role: context
  - path: .temp/pr2061/independent-secondary/sources/28075122-main.xml
    sha256: d061cb42e67abdc6b1a25b66b27e6747bfb460aa4a6ac179a5800a9a6a83a760
    role: context
  - path: .temp/pr2061/independent-secondary/sources/28075122-main.xml.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/28075122-metadata.json
    sha256: 839eeb59a69aa0a7a2756607323aa9cdfb431698ebf300723cc151928a4d34e0
    role: context
  - path: .temp/pr2061/independent-secondary/sources/28075122-metadata.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/28075122-sections.json
    sha256: c57dc161fd1adc076fa991992b5befaf39894f1875848b5a7ed348e68ec9e508
    role: context
  - path: .temp/pr2061/independent-secondary/sources/28075122-supp.zip
    sha256: e7ca3455ca67c58fc3afba63c80f39ec18d004ab8ef74df28ce65b1c06dc2719
    role: context
  - path: .temp/pr2061/independent-secondary/sources/28075122-supp.zip.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/28159790-main.html
    sha256: 3ffc67bb0e5d0bf60c3e671823b9ec9752c0b353df23f9b914ceef2fad19235c
    role: context
  - path: .temp/pr2061/independent-secondary/sources/28159790-main.html.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/28159790-main.txt
    sha256: 576db02abdaae62a891b87d85f40b4832aac01bea3c6effc086df0a637fc7404
    role: context
  - path: .temp/pr2061/independent-secondary/sources/28159790-main.xml
    sha256: 35f58234da8277cd3088ffae5f8796eb6bee43362a6d9a5e0430e425274dae10
    role: context
  - path: .temp/pr2061/independent-secondary/sources/28159790-main.xml.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/28159790-metadata.json
    sha256: 96e4fa9c091d2dee4e677c79864629a10263053d81b18ffdde92942b456744ee
    role: context
  - path: .temp/pr2061/independent-secondary/sources/28159790-metadata.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/28159790-sections.json
    sha256: 4a44fd7bccd7289ea8f776d6774eec0acb5f202db0f8eaca06627202441cc0eb
    role: context
  - path: .temp/pr2061/independent-secondary/sources/28159790-supp.zip
    sha256: 81dccd607506b216dfbaa9b129961e173973222901e2396ebdd95bd66b432d0d
    role: context
  - path: .temp/pr2061/independent-secondary/sources/28159790-supp.zip.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/NCBI2GTDB.tsv.gz
    sha256: 761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd
    role: context
  - path: .temp/pr2061/independent-secondary/sources/acs184-detail.json
    sha256: 7a367695881ff13236286d2bf7a77f025c83efbd99072f52cc8d7d291433fd62
    role: context
  - path: .temp/pr2061/independent-secondary/sources/acs184-detail.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/acs184-download-receipt.json
    sha256: 3cb8fea8a07dd284249011e4670b3c160ba42d8040c40e641e8c5edb130c129b
    role: context
  - path: .temp/pr2061/independent-secondary/sources/acs184-figshare.json
    sha256: cbdc54399ac7c7f728530674f0009274b887c4df14ef10a4c466f1f8c5992825
    role: context
  - path: .temp/pr2061/independent-secondary/sources/acs184-figshare.json.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/alternate-fetches.json
    sha256: 702023d4513970de48d18902ad7422fc4b00246eb48485bb40d775f3016209a4
    role: context
  - path: .temp/pr2061/independent-secondary/sources/asset-fetches.json
    sha256: 8f07a543609d74070e22cae45d32bbb02a48bdf56881c2f85c15ed57807c1014
    role: context
  - path: .temp/pr2061/independent-secondary/sources/atcc195.html
    sha256: 05f5feda685a788faaf3ed1a780830aa97f36a1a0777ca82200c0eb05f33cc3b
    role: context
  - path: .temp/pr2061/independent-secondary/sources/atcc195.html.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/atccDvH.html
    sha256: 9a872df9e25a59dae83aad5bf1a4a4688b3bd0748f8847f090f17bb3a4c49274
    role: context
  - path: .temp/pr2061/independent-secondary/sources/atccDvH.html.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/atccDvH.txt
    sha256: 89f0fe7169d51df04c2442462a8e3e8bb8d4ed16a0295aaab08e29d11c7978c0
    role: context
  - path: .temp/pr2061/independent-secondary/sources/atccR7.html
    sha256: 4a570cac028dc2db905690bcbdc71bcd619b5388aac8ebd96ab6a692037fdf2b
    role: context
  - path: .temp/pr2061/independent-secondary/sources/atccR7.html.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/atccR7.txt
    sha256: 36ce5b7810662a6563237ca5034e6e7e6a831d51151163bb126814a6a9f44349
    role: context
  - path: .temp/pr2061/independent-secondary/sources/authority-si-fetches.json
    sha256: 8f94d22e5a145eb5f80c49eebf55b73ea5e6929637a9374e921d25401bb5089f
    role: context
  - path: .temp/pr2061/independent-secondary/sources/dsm102351.html
    sha256: 525cf8ffbd5f5b2d9c1c605a084dcecdceb98b803fb6b6d9fd5589250456531a
    role: context
  - path: .temp/pr2061/independent-secondary/sources/dsm102351.html.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/dsm102351.txt
    sha256: c44aee31d1084390a421c85aa17db3ac2f4eb1dc62fa7531ec10f9e51ba4bdbe
    role: context
  - path: .temp/pr2061/independent-secondary/sources/dsm2245.html
    sha256: 51824f665573c9d86c4cd8ee485d885322bee840ebcce5dfde2e64ec547c7003
    role: context
  - path: .temp/pr2061/independent-secondary/sources/dsm2245.html.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/dsm2245.txt
    sha256: 2452c23e1007a0b3cd4910964441dfd4ca741b5284ff9a1daa065977e77a6c43
    role: context
  - path: .temp/pr2061/independent-secondary/sources/es6b05770_si_001.pdf
    sha256: 2d76ef30256eb70a6df116aab5b1042322940e3859abdd9a044ebd7a2e3a6052
    role: context
  - path: .temp/pr2061/independent-secondary/sources/es6b05770_si_001.pdf.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/es6b05770_si_001.txt
    sha256: 05a1ea936fcecee547136c13b7f7955842b581f4ed69d32886c84afd275f9e5d
    role: context
  - path: .temp/pr2061/independent-secondary/sources/genome-main.txt
    sha256: f780546a9fd1a465ac0938713b7e8af60fb3d40bf2793fcac355f813aaf53820
    role: context
  - path: .temp/pr2061/independent-secondary/sources/genome-main.xml
    sha256: 9740fde3343add0117b94fda17a0a1d694e928dca37dd0785cde85df570b2e00
    role: context
  - path: .temp/pr2061/independent-secondary/sources/genome-main.xml.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/genome-metadata.json
    sha256: f9f6ead379f0b6d31d8a92626064b82c407215758f058e4dd324266526286a67
    role: context
  - path: .temp/pr2061/independent-secondary/sources/genome-metadata.json.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/harding-thesis-page.html
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/harding-thesis-page.html.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/harding-thesis.pdf
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/harding-thesis.pdf.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/harding-web-chapter.json
    sha256: ca4f066c411f6eb23303614c9db87adcf5acd5ae82fecc977c9f5a647369dde1
    role: context
  - path: .temp/pr2061/independent-secondary/sources/harding-web-cohort.json
    sha256: 45ba2bd6be716cd85a32a491fe0ea1f7936c6a2b60436631079fa03e71f81c72
    role: context
  - path: .temp/pr2061/independent-secondary/sources/isotope-acs.html
    sha256: 5675d2719f83230924ce49dc336a188a4e274277d3335a291bcca543a0dd8147
    role: context
  - path: .temp/pr2061/independent-secondary/sources/isotope-acs.html.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/main-figure-manifest.json
    sha256: 111e4c761b5cfcc9755d8599b2401793e56143de781efc61d31db682a6bbf4d5
    role: context
  - path: .temp/pr2061/independent-secondary/sources/main-tables-figures.json
    sha256: a544f6e9bc386684086939e52c8d3af588dd048eb2fe1a4dff326f93d3afae75
    role: context
  - path: .temp/pr2061/independent-secondary/sources/metadata-fetches.json
    sha256: 9c83c05b3347eefe9b408ad091a6e393b4a79b549f7afcd3d5b1423d8ef620e1
    role: context
  - path: .temp/pr2061/independent-secondary/sources/pride.json
    sha256: 93e9647784eec437635b7288f28ac267acbea31d255ed000348f6dd7d7a14399
    role: context
  - path: .temp/pr2061/independent-secondary/sources/pride.json.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-assets/21881617-fig1.jpg
    sha256: f92f3002681dea4094faf01345b701119dce59bef46d6865f478777a4b8464fa
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-assets/21881617-fig1.jpg.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-assets/21881617-fig2.jpg
    sha256: 1a44b769ce786ae7eda5d8b17b7bd35fe5b3fab5b7b5dad69c538d1d7f12f813
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-assets/21881617-fig2.jpg.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-assets/21881617-fig3.jpg
    sha256: a51e6e8614efa8c1811a45a89bc7c74095731f9ec10d7eb5d83fd7ad409749fa
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-assets/21881617-fig3.jpg.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-assets/21881617-fig4.jpg
    sha256: f05b4e97ddf6fdb8d9d6d9a56e8c2f4db94332e8e24f7ca7dccfe7391b0907fd
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-assets/21881617-fig4.jpg.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-assets/21881617-fig5.jpg
    sha256: b4251b9e44585f5e6373f04907a5501fe494c222d583280ba889c44f83fb79bf
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-assets/21881617-fig5.jpg.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-assets/21881617-ismej2011111x1.pdf
    sha256: a5ad102ef93d7d136e1eb6b58bf830063e1c27435c20ea8ff8cc0ad5a26ad496
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-assets/21881617-ismej2011111x1.pdf.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-assets/21881617-ismej2011111x2.doc
    sha256: df85af994964736c5a8c6545d44a75436f7ac4d63e2bcb7ff0dc08c5f71c8ecf
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-assets/21881617-ismej2011111x2.doc.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-assets/21881617-ismej2011111x3.xls
    sha256: 642cdade64aec907b7ebb5370be1f31f3b23220cea8a209cbebf390e16934d58
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-assets/21881617-ismej2011111x3.xls.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-assets/21881617-ismej2011111x4.doc
    sha256: 4814e03ea67b0c0bee7c293ece4b95534bb5e4040cc3d93b7bc2e4fd7039ed7b
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-assets/21881617-ismej2011111x4.doc.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-assets/21881617-ismej2011111x5.doc
    sha256: 9e4d6ab10631cceaba62a1cb7c4c7f2bb83034be29f050a3e5f3db91d08ac6ca
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-assets/21881617-ismej2011111x5.doc.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-assets/21881617-ismej2011111x6.doc
    sha256: 113613674789795b893318ad82e6395517f8671dc55a431351fe28e967ac04e5
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-assets/21881617-ismej2011111x6.doc.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-assets/21881617-ismej2011111x7.doc
    sha256: 013e9ed1cf9cfbdf54f5fa914ca440ed132eb2f9f83501b05927ff4625f054ca
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-assets/21881617-ismej2011111x7.doc.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-assets/21881617-ismej2011111x8.doc
    sha256: 60f221d7792a322da423fc455b744a53e3324434378a9782802d54b5c25bdcbf
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-assets/21881617-ismej2011111x8.doc.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-assets/24463969-AEM.03477-13_zam999105224sd2.xls
    sha256: 19564b4524613ab203ca7da7dc170d4247d056edfe1dc5a3518a1cfb127203d7
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-assets/24463969-AEM.03477-13_zam999105224sd2.xls.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-assets/24463969-AEM.03477-13_zam999105224so1.pdf
    sha256: 58b39419024f879d6996d15305fe48be02fc2e2170684845beb583a37ee96757
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-assets/24463969-AEM.03477-13_zam999105224so1.pdf.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-assets/24463969-F1.jpg
    sha256: fdab8f57803d992138d719ae19a3b9fafd861641feeba69a4d2857dbb67ed148
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-assets/24463969-F1.jpg.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-assets/24463969-F2.jpg
    sha256: 65c81f678f8f484a1e9c1b1224ae19f2a80885b1162ae37a789c3cd51e84f9ee
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-assets/24463969-F2.jpg.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-assets/24463969-F3.jpg
    sha256: 32297586d5f216bbb2424577d286315e504ff06af06d9c54f3042f70a3f8d11c
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-assets/24463969-F3.jpg.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-assets/24463969-F4.jpg
    sha256: 0041f438378eac8abb44bd899c777af33a6dfa740a940bd6a4aa8e378e7ecce7
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-assets/24463969-F4.jpg.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-assets/24463969-F5.jpg
    sha256: 5bb1b87d720d565da1e8fa8704a50f9fe364fe50a5db3a98d4215e9115d57686
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-assets/24463969-F5.jpg.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-assets/24463969-F6.jpg
    sha256: 3877bbb2ec627932f2200f73343f8d3abd5a0bd88222dba6cd9c94387a382993
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-assets/24463969-F6.jpg.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-assets/25576615-AEM.03464-14_zam999116094sd2.xlsx
    sha256: 979aaef3bdb704dc38c8d6702c342f32567911d9f100625969d3d9337b899f2c
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-assets/25576615-AEM.03464-14_zam999116094sd2.xlsx.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-assets/25576615-AEM.03464-14_zam999116094so1.pdf
    sha256: 0d2ee216f0463196ec899881f5c998bcd863531a1ef36dc0a1231a16137262f2
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-assets/25576615-AEM.03464-14_zam999116094so1.pdf.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-assets/25576615-F1.jpg
    sha256: c9047b2ade3b69e577de36a97edc710a13331ac3e7d5aca8301c884f8dd8fbca
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-assets/25576615-F1.jpg.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-assets/25576615-F2.jpg
    sha256: 44035ea00d8c904eba94f8fc7d386660dc0b94920775e7900be98de8423d07de
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-assets/25576615-F2.jpg.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-assets/25576615-F3.jpg
    sha256: 7bb8a2d038365322017253e0ab9a6b7e655e39e9faa7a0ee4632fbca27bd488d
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-assets/25576615-F3.jpg.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-assets/25576615-F4.jpg
    sha256: 7e8dcc6e37e5d874337733616c127c4391a47934526bd68410f536c462a257f6
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-assets/25576615-F4.jpg.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-assets/28075122-F1.jpg
    sha256: 49e9ab625e466761f4cc1cd011d0e5957223078444cfb5142f4d562f6d4bcd6b
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-assets/28075122-F1.jpg.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-assets/28075122-F2.jpg
    sha256: 2e2ff0e84fed2f3dbbd731f308dc6de8503c9e9066b4810b113e21f59dd8f24c
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-assets/28075122-F2.jpg.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-assets/28075122-F3.jpg
    sha256: c879d71c7a249f5dee6150046c5e0b15a984ab9c4f2c921e3de0b2a127bfeb40
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-assets/28075122-F3.jpg.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-assets/28075122-F4.jpg
    sha256: ee1dd3b84ab989c7187285ba55a953217cd37c8f12b1dd64479e8859a7b09974
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-assets/28075122-F4.jpg.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-assets/28075122-F5.jpg
    sha256: 91b26d3a38f4f89b03dd70d835f6ac0f2affa45fb14c121e9174aa04f66676a3
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-assets/28075122-F5.jpg.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-assets/28075122-F6.jpg
    sha256: 98e31c54d35663c42d2376d9f2d1e823a8e72a422621a3a33c7e686f3e51db60
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-assets/28075122-F6.jpg.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-assets/28075122-NIHMS868542-supplement-SI.pdf
    sha256: 078218a9ddfcc24bf95c9d1eb816d92febb125a5fbf31187ca6b05d49d02d287
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-assets/28075122-NIHMS868542-supplement-SI.pdf.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-assets/28159790-AEM.03384-16_zam999117765s1.pdf
    sha256: b3308c2815aff2844da8f99d1af4104cbac7dd0c4062da7aaddde0662dba0cfe
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-assets/28159790-AEM.03384-16_zam999117765s1.pdf.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-assets/28159790-F1.jpg
    sha256: a39e7faa1490df4a6210383f3b9d18912a5f9a94c3c3c6315c839d536967a259
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-assets/28159790-F1.jpg.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-assets/28159790-F2.jpg
    sha256: b6609c85e26754bf314e3518a85aad06ce5d59def5457f2287ae78926ff1713a
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-assets/28159790-F2.jpg.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-assets/28159790-F3.jpg
    sha256: 337a10b37f23da7d32665c181c86c93ca313a30caa719d19b18f9829402d206e
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-assets/28159790-F3.jpg.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-assets/28159790-F4.jpg
    sha256: 680f5484c0084717d962bd3ad2c1bab3a96874e1a3d110f32cae3e64198430f8
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-assets/28159790-F4.jpg.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/independent-secondary/sources/primary-fetches.json
    sha256: e070577faa6798f9a3f44470ebdc06d14905c030aad5d829a5cb9890d3438c12
    role: context
  - path: .temp/pr2061/independent-secondary/sources/taxonomy.xml
    sha256: d01a7af036e9fddf8ae484475154c47d414e96767c704c44bbd40f34b44ff93e
    role: context
  - path: .temp/pr2061/independent-secondary/sources/taxonomy.xml.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: AGENTS.md
    sha256: 7c35deb79ce874239f1080c2f575756ff47d1985483030878eaeb07df02d7529
    role: context
  - path: conf/record_review.yaml
    sha256: c4ad25505a87a040c57eb93f1ee9673a09389a474c6d4e1136781456ff190fc8
    role: context
  - path: conf/reference_validator.yaml
    sha256: 5cd4781c7e15b7c5472f0b008e41764842cc023a7ba99f4273298f421be36652
    role: context
  - path: docs/record-review-profile.md
    sha256: 285f79747999f83edbe63e5efde349a5cc063e9e486ce1a748b47b76c6631f31
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: history/README.md
    sha256: 86c0347d77402bcecdec466b01974ad53beddb9cf1bd17cf085674970542a101
    role: context
  - path: history/infrastructure/paywalled-text-removal/2026-09-11T025818Z-claude-code-366122.yaml
    sha256: 317990e487936c8020d2c3160ec10b4e31b8676637a23a49ca266177a1ac01e6
    role: context
  - path: history/records/Dehalococcoides_Desulfovibrio_Lactate_TCE_Syntrophy/2026-10-06T054824Z-codex-33c8ca.yaml
    sha256: 3a870c60f6e1cbeba74545fd49fc33a6f8a295cb12ce6b63d93ce17c26e3ac89
    role: context
  - path: history/records/Dehalococcoides_Desulfovibrio_Pelosinus_Corrinoid_Triculture/2026-10-06T054824Z-codex-290d65.yaml
    sha256: 50b79b96818647aef72b689be1ae95fb6345496fda7e7c753413529682646581
    role: context
  - path: history/records/Dehalococcoides_Pelobacter_Acetylene_TCE_Coculture/2026-10-06T061823Z-codex-d74031.yaml
    sha256: ac733d15084452c279c29136f5c94c217f9ddd1eec2c146e44e6ecaf12de7a1e
    role: context
  - path: history/records/Dehalococcoides_Syntrophomonas_TCE_Dechlorination_Coculture/2026-10-06T061823Z-codex-91ce0c.yaml
    sha256: d477fbef995508b0c74179c73c2628802a8e545cd04cdcc2f4bc16be007340a0
    role: context
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: kb/communities/Dehalococcoides_Desulfovibrio_Lactate_TCE_Syntrophy.yaml
    sha256: bc9eebbdf57b937cc87c72ee439f404bb7ab51b99b2f06e2f11fd240a454c629
    role: target
  - path: kb/communities/Dehalococcoides_Desulfovibrio_Pelosinus_Corrinoid_Triculture.yaml
    sha256: 2d771dc7df594f59d55d100bdf4e7ed6bbc571dfea0a4e37a774583e831910dc
    role: context
  - path: kb/communities/Dehalococcoides_Pelobacter_Acetylene_TCE_Coculture.yaml
    sha256: ab28a71ff971a76db7e6bc3989a24ff65fbf03b0eb1177ae70c85fab1d04c813
    role: context
  - path: kb/communities/Dehalococcoides_Syntrophomonas_TCE_Dechlorination_Coculture.yaml
    sha256: b0c182ee42aa14442f77f15b8a8ada5172fbbd989f8175c399af7f83877b6dd2
    role: context
  - path: references_cache/PMID_21881617.md
    sha256: 249f0e7a6b71343881d648f2f539d8f9096fa2dab0e4f2692e370b47ff3fbae7
    role: context
  - path: references_cache/PMID_24015929.md
    sha256: 5a8edfdf6d765c4eb0e041310e03ca88fb53a96c64f2d36383ed22f773f4ff49
    role: context
  - path: references_cache/PMID_24463969.md
    sha256: 630100bad057e96e0bca2800ca31a2f1eae6ab54bccfb38c03375a70cc116de1
    role: context
  - path: references_cache/PMID_25576615.md
    sha256: 3a02cd4c98774aee7e14e54cee4f54b87fd60188d31e1135386d057115a42fde
    role: context
  - path: references_cache/PMID_27881975.txt
    sha256: 529f74223be883253a613f17cb1b5018b662c35daa16b2708d40b189579692fb
    role: context
  - path: references_cache/PMID_28075122.md
    sha256: 9ff2ad42fd8c164b8779258503d2f08241e105d3b5f35b684f7508be4c9dfb48
    role: context
  - path: references_cache/PMID_28159790.md
    sha256: 8a89860f58e10545a3986b093decf43cadec8ac10d8c994b815d497d356e819b
    role: context
  - path: references_cache/doi_10.3389_fmicb.2016.01795.md
    sha256: 9bfa7cce73e10ae4946b239c265c4e7039b6880190833fc076b2052889f457c9
    role: context
  - path: reports/causal_graph_review/adversarial-review-20261006-batch30.yaml
    sha256: 173e2bfe58bed7b38cbf3e535062651728c15533668958b6e56dc8332b5c9e2f
    role: context
  - path: reports/causal_graph_review/adversarial-review-20261006-batch31.yaml
    sha256: 2c1e54bb636d8534313e280c6a19fdee4bedaa235c76d0e5ff5a17f71d573541
    role: context
  - path: reports/causal_graph_review/decisions/20261006-three-records-batch30.yaml
    sha256: cb60e4a113592fd34842090d5f2db473831a31066febb469d2438a8d8b217c3c
    role: context
  - path: reports/causal_graph_review/decisions/20261006-three-records-batch31.yaml
    sha256: 3ae6fd42367e69f8ffe653271b91ef4cabc271b302f7f729d6d1204a1d7e7b88
    role: context
  - path: reviews/structured/20261021T101100Z-stage4-frozen-cohort-review/review.md
    sha256: e432615b147787c8d009d96d2f11e5b78a45927bf9c69e45ec0d31123d1fc2e9
    role: context
  - path: reviews/structured/20261021T101100Z-stage4-frozen-cohort-review/review.yaml
    sha256: 37d089fd55c077793dd20d868b50c47cb1cceab6dae6a82887cc938bee05fa6d
    role: context
  - path: reviews/structured/20261022T044407Z-dehalococcoides-desulfovibrio-record-review/review.md
    sha256: e411f0b738fba5035671bff4087d222d6c9cfeda6fe751f08703318c2f083903
    role: context
  - path: reviews/structured/20261022T044407Z-dehalococcoides-desulfovibrio-record-review/review.yaml
    sha256: 47f0d590fdfbd5d210c0ac4521d4c8a2d201f7c4c7cfe8b1fb8dce525cdac1eb
    role: context
  - path: reviews/structured/20261022T045256Z-dehalococcoides-pelosinus-triculture-record-review/review.md
    sha256: 7ba84592494d5299ad3a381890713a10d2133719cbf0b9a9d513e1185f8fc888
    role: context
  - path: reviews/structured/20261022T045256Z-dehalococcoides-pelosinus-triculture-record-review/review.yaml
    sha256: 2bf1343379c4efb35a23219e608e53d7d7fc98c3f3f3a72c59e468d541203566
    role: context
  - path: reviews/structured/20261022T051602Z-sfb93-195-acetylene-record-review/review.md
    sha256: 6c2d1ce363745ce05e8225eeebd54e19d689f3a8d0e3bf59c0c6e9ebb6bc616c
    role: context
  - path: reviews/structured/20261022T051602Z-sfb93-195-acetylene-record-review/review.yaml
    sha256: 0ff208ff211b9c3cefc2716797e7abe6613bf3a6739de809fdd4b57783b6d79d
    role: context
  - path: reviews/structured/20261022T053021Z-syntrophomonas-195-record-review/review.md
    sha256: 3837e6d9a5e9d99d157f62bf82e73afc8ac580266726143ee4f0df53f63e3b15
    role: context
  - path: reviews/structured/20261022T053021Z-syntrophomonas-195-record-review/review.yaml
    sha256: c161fe70376a4c4d3a93868a38d34a7d394d41ed5005bbfea8c3fc3ffb174940
    role: context
  - path: reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-04/revision-0001/frozen_inventory_metrics.tsv
    sha256: d5a47bbcc3745a489ff507680aa7360a6a65ce070ce4ec88f886b70128791313
    role: context
  - path: reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-04/revision-0001/review_report.md
    sha256: 4e7781aa8cdfc4bb42d896ebe75920719d9dcade92ffc4a0ae07af7481cb37b3
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/adhoc/pr2043_009_correction.py
    sha256: fde4e6e174c58e3596eff98cf529cb38a8953e871cfa6d323a2110312ccbcd87
    role: context
  - path: scripts/adhoc/pr2058_020_authority_observation.py
    sha256: d662a31de67991a503f019f97c8e17f365dd1a7df11866e894d0e3059938777c
    role: context
  - path: scripts/adhoc/pr2061_199_cultivation_locator.py
    sha256: a087f7bbd717d9dae524631ea1b4e3eb9244fa8bf6edda7e4c8f74e91268b6be
    role: context
  - path: scripts/audit_completeness.py
    sha256: 77344c3bfc87f1a0d76bd977651c3e10d35b0944cb4e242c19545db2b73b4586
    role: context
  - path: scripts/gtdb_ground.py
    sha256: 0fc1ba926a56e5be85cdf064db0cf56452aeeee93f15b0ced98e8f11b5296175
    role: context
  - path: scripts/normalize_cache_names.py
    sha256: d87b5d001c1dac3f213637523651fd87b71a54806b1114c83f5fb0ea3528ef5e
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: src/communitymech/network/auditor.py
    sha256: fe32aa2eddf9e09c153c47576f943bf08a6019f650bf2575e3ddc8e14675049b
    role: context
  - path: src/communitymech/schema/communitymech.yaml
    sha256: 7355e14f0f17c5d3b875abd33af6474ddc1aad08cc3305313686fede337e259a
    role: context
  - path: src/communitymech/schema/history.yaml
    sha256: b01b06f1b9a37db205c26c31ec0fd910690848507c7e1bfb73b424ac0829c52d
    role: context
  - path: src/communitymech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
targets:
- target_id: CommunityMech:000199
  path: kb/communities/Dehalococcoides_Desulfovibrio_Lactate_TCE_Syntrophy.yaml
  label: Dehalococcoides-Desulfovibrio Lactate-Fed TCE Dechlorination Coculture
  kind: maintained
  record_class: MicrobialCommunity
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Dehalococcoides_Desulfovibrio_Lactate_TCE_Syntrophy.yaml
    role: canonical_record
scope:
  description: Source-based reassessment of the cultivation finding and its exact
    source locator only; completion applies to this bounded scope, not a new whole-record
    scientific certification or canonical repair.
  selection: Exactly CommunityMech:000199 and cm-000199-cultivation; other original
    findings and the other three records in the frozen context are not superseded.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000199
checks:
- check_id: focused-1
  name: validate
  status: passed
  required: true
  target_ids:
  - CommunityMech:000199
  command: just --no-dotenv validate kb/communities/Dehalococcoides_Desulfovibrio_Lactate_TCE_Syntrophy.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - focused-qc
  summary: Actual current-target check executed during the preceding read-only pass;
    target and validator inputs remain unchanged and are frozen here.
- check_id: focused-2
  name: validate-strict
  status: passed
  required: true
  target_ids:
  - CommunityMech:000199
  command: just --no-dotenv validate-strict kb/communities/Dehalococcoides_Desulfovibrio_Lactate_TCE_Syntrophy.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - focused-qc
  summary: Actual current-target check executed during the preceding read-only pass;
    target and validator inputs remain unchanged and are frozen here.
- check_id: focused-3
  name: validate-terms
  status: passed
  required: true
  target_ids:
  - CommunityMech:000199
  command: just --no-dotenv validate-terms kb/communities/Dehalococcoides_Desulfovibrio_Lactate_TCE_Syntrophy.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - focused-qc
  summary: Actual current-target check executed during the preceding read-only pass;
    target and validator inputs remain unchanged and are frozen here.
- check_id: focused-4
  name: validate-references-explained
  status: passed
  required: true
  target_ids:
  - CommunityMech:000199
  command: just --no-dotenv validate-references-explained kb/communities/Dehalococcoides_Desulfovibrio_Lactate_TCE_Syntrophy.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - focused-qc
  summary: Actual current-target check executed during the preceding read-only pass;
    target and validator inputs remain unchanged and are frozen here.
- check_id: focused-5
  name: validate-gtdb
  status: passed
  required: true
  target_ids:
  - CommunityMech:000199
  command: just --no-dotenv validate-gtdb kb/communities/Dehalococcoides_Desulfovibrio_Lactate_TCE_Syntrophy.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - focused-qc
  summary: Actual current-target check executed during the preceding read-only pass;
    target and validator inputs remain unchanged and are frozen here.
- check_id: focused-6
  name: validate-gtdb-domain
  status: passed
  required: true
  target_ids:
  - CommunityMech:000199
  command: just --no-dotenv validate-gtdb-domain kb/communities/Dehalococcoides_Desulfovibrio_Lactate_TCE_Syntrophy.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - focused-qc
  summary: Actual current-target check executed during the preceding read-only pass;
    target and validator inputs remain unchanged and are frozen here.
- check_id: focused-7
  name: validate-history
  status: passed
  required: true
  target_ids:
  - CommunityMech:000199
  command: just --no-dotenv validate-history history/records/Dehalococcoides_Desulfovibrio_Lactate_TCE_Syntrophy
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - focused-qc
  summary: Actual current-target check executed during the preceding read-only pass;
    target and validator inputs remain unchanged and are frozen here.
evidence:
- evidence_id: current-record
  kind: record_content
  reference: kb/communities/Dehalococcoides_Desulfovibrio_Lactate_TCE_Syntrophy.yaml
  locator: growth_media[0], cultivation_setup, discussions[0]; unchanged exact target
    bytes
  summary: The source-specific cultivation omissions remain open; no canonical field
    is repaired.
  support: supports
  accessed_at: '2026-11-06T19:22:26.994037Z'
  snapshot_sha256: bc9eebbdf57b937cc87c72ee439f404bb7ab51b99b2f06e2f11fd240a454c629
- evidence_id: prior-review
  kind: prior_review
  reference: reviews/structured/20261022T044407Z-dehalococcoides-desulfovibrio-record-review/review.yaml
  locator: evidence[cultivation].locator and actions[enrich-cultivation].acceptance_checks[0]
  summary: The original paragraph-2 locator is wrong. All five scientific findings
    and their acceptance scopes remain unresolved; only cultivation receives a new
    open occurrence.
  support: supports
  accessed_at: '2026-11-06T19:22:26.994037Z'
  snapshot_sha256: 47f0d590fdfbd5d210c0ac4521d4c8a2d201f7c4c7cfe8b1fb8dce525cdac1eb
- evidence_id: culture-2012
  kind: primary_source
  reference: .temp/pr2061/independent-secondary/sources/21881617-main.html
  locator: 'PMID:21881617 / PMC3260503: culture Methods #sec3; Discussion #sec26 fifth
    direct paragraph, not second; complete scientific narrative and Table1 inspected'
  summary: The fifth paragraph explicitly describes unshaken conditions. Methods separately
    supports vessel, working volume, gas, amendments and transfer stages; 5 m typography
    is not silently normalized into a direct concentration quote.
  support: supports
  accessed_at: '2026-11-06T19:22:26.994037Z'
  snapshot_sha256: 1901c5d00dc3894b024df1868610c7ae63eb13b1482195dcf2e67426abd382a1
- evidence_id: culture-2014
  kind: primary_source
  reference: .temp/pr2061/independent-secondary/sources/24463969-main.html
  locator: 'PMID:24463969 / PMC3993147: #sec2-1 sole direct culture Methods paragraph'
  summary: Pair and triculture cultivation are source-specific; pure-PfR7 pH and bioassay
    conditions must not migrate into the pair.
  support: supports
  accessed_at: '2026-11-06T19:22:26.994037Z'
  snapshot_sha256: 4b15df78b9c312024337e876f7d24aaf97b03bfb58a9af42d9753efbc0f2313c
- evidence_id: culture-2017
  kind: primary_source
  reference: .temp/pr2061/independent-secondary/sources/28159790-main.html
  locator: 'PMID:28159790 / PMC5377507: culture Methods and donor-excess/donor-limited
    Results'
  summary: Maintenance, acceptor-limited pair and donor-limited triculture remain
    separate; the original ancillary-mechanism and threshold limitations are preserved.
  support: supports
  accessed_at: '2026-11-06T19:22:26.994037Z'
  snapshot_sha256: 3ffc67bb0e5d0bf60c3e671823b9ec9752c0b353df23f9b914ceef2fad19235c
- evidence_id: focused-qc
  kind: validation
  reference: .temp/pr2061/independent-secondary/000199-focused-checks.json
  locator: Seven actual focused commands, with concrete stdout/stderr inputs also
    frozen
  summary: All seven focused schema/strict/terms/references/GTDB/domain/history checks
    exited0. Their deterministic success is distinct from this source-based locator
    correction.
  support: supports
  accessed_at: '2026-11-06T19:22:26.994037Z'
  snapshot_sha256: 39de026943fec95c29128d59cb5939389aca7d7347c31ee9cea4b74a560c35be
- evidence_id: science-context
  kind: validation
  reference: .temp/pr2061/independent-secondary/independent-science-four-records.json
  locator: Earlier independent read-only pass, frozen before switching to author role
  summary: Records the locator defect and bounded scientific source scope. This author
    does not claim independent approval of the new successor.
  support: supports
  accessed_at: '2026-11-06T19:22:26.994037Z'
  snapshot_sha256: 519313736a8d0415e08badb79b84adb83c7556ac8a927218e9eb4dc8b4d9d568
assessments:
- assessment_id: cultivation-source
  area: evidence
  topic: Exact culture-source paragraph and treatment separation
  outcome: supported
  summary: 'Fresh primary text supports unshaken conditions in Discussion #sec26 direct
    paragraph5 and the remaining source-bounded cultivation guidance.'
  target_ids:
  - CommunityMech:000199
  evidence_ids:
  - culture-2012
  - culture-2014
  - culture-2017
  - prior-review
  details: 'This explicitly corrects both the original evidence locator and enrich-cultivation
    acceptance check. The corrected phrase is: Discussion section #sec26, fifth direct
    paragraph, states unshaken conditions (the paragraph beginning ''Another possible
    reason for more robust growth'').'
- assessment_id: retained-curation
  area: completeness
  topic: Still-open source-specific cultivation and independent finding heads
  outcome: concern
  summary: The current target still lacks the bounded culture details. No record change,
    terminal disposition or status promotion occurs.
  target_ids:
  - CommunityMech:000199
  evidence_ids:
  - current-record
  - prior-review
  - focused-qc
  details: The original dvh-roles, dataset-type, omics-evidence and gtdb-provenance
    heads retain their original complete actions. The shared validate-curation acceptance
    is repeated here for the cultivation head only.
findings:
- finding_id: cultivation
  issue_key: cm-000199-cultivation
  category: completeness
  severity: minor
  native_severity: P3
  normalization_reason: Bounded recoverable protocol, evidence placement or provenance;
    core community and qualified graph remain supported.
  rule_id: review-checklist.claim-specific-support-and-context
  status: open
  certainty: confirmed
  title: Recover source-specific culture and transfer details
  description: The partial lactate/TCE entry omits available vessel, working volume,
    gas, cobalamin and transfer information. Add bounded study arms without merging
    the pair, triculture and bioassay conditions.
  target_ids:
  - CommunityMech:000199
  field_paths:
  - growth_media[0]
  - cultivation_setup
  - discussions[0].rationale
  evidence_ids:
  - current-record
  - culture-2012
  - culture-2014
  - culture-2017
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Dehalococcoides_Desulfovibrio_Lactate_TCE_Syntrophy.yaml
    role: canonical_record
  ownership_note: Maintained focal YAML owns future authorized repairs; no shared
    issue or historical finding is closed.
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261022T044407Z-dehalococcoides-desulfovibrio-record-review
    finding_id: cultivation
actions:
- action_id: enrich-cultivation
  description: Add separate source-specific cultivation details and an access follow-up.
  finding_ids:
  - cultivation
  target_ids:
  - CommunityMech:000199
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Dehalococcoides_Desulfovibrio_Lactate_TCE_Syntrophy.yaml
    role: canonical_record
  acceptance_checks:
  - 'For PMID21881617, cite Materials and methods → Bacterial cultures and growth
    conditions: 160 mL serum bottle, 100 mL working volume, N2:CO2 90:10, 100 µg/L
    cyanocobalamin, initial 195:DvH 10:1, 10% transfers every 10 days for 20 passages
    with 78 µmol TCE; distinguish the 40 µmol lower-TCE arm. Discussion section #sec26,
    fifth direct paragraph, states unshaken conditions (the paragraph beginning ''Another
    possible reason for more robust growth''). The PMC 5 m rendering is not a direct
    5 mM quote; Results 500 µmol/100 mL gives 5 mM only by labeled calculation.'
  - 'For PMID24463969, cite the sole culture Methods paragraph: 160 mL sealed serum
    bottle, 100 mL basal medium / 60 mL N2:CO2 90:10, about 0.7 mmol lactate / 77
    µmol TCE, 74 nM cobalamin, 34°C, dark, no shaking, and six 3% transfers. Keep
    the cobalamin-free/DMB/PfR7 comparisons distinct. Do not transfer pure-PfR7 pH
    7.5 or Lactobacillus bioassay incubation to the pair.'
  - Keep PMID28159790 maintenance, acceptor-limited and donor-limited arms separate.
    Add a dated follow-up that the original main body is now available; preserve the
    factual historical 2026-10-06 access statement and open ancillary-mechanism uncertainty.
- action_id: validate-curation
  description: Validate any separately authorized maintained-record repair.
  finding_ids:
  - cultivation
  target_ids:
  - CommunityMech:000199
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Dehalococcoides_Desulfovibrio_Lactate_TCE_Syntrophy.yaml
    role: canonical_record
  acceptance_checks:
  - Recheck exact strain, assay and treatment scope, then focused schema, strict,
    term, explained-reference, GTDB/domain and history checks. Run just gen-html and
    just check-docs-current when canonical curation is authorized.
  - Preserve caches, source responses, histories and previous decisions. This review
    does not authorize record, issue, Git or status mutations.
related_reviews:
- repository: CultureBotAI/CommunityMech
  review_id: 20261022T044407Z-dehalococcoides-desulfovibrio-record-review
  relationship: Bounded open cultivation successor; corrects its source locator only,
    preserving four other original finding heads and all history.
limitations:
- Historical unpublished scratch inputs were not recovered. Current concrete sources
  are not reconstructed historical bytes; the original review is immutable.
- No new full-record scientific verdict, source-stage harmonization, full medium recipe
  reconstruction, raw-data analysis, graph revision or KB edit is claimed.
- 2012/2014/2017 declared supplementary routes returned access/error bodies. This
  locator and culture finding is supported by the complete primary main text; unread
  supplements are not claimed inspected.
- The earlier source-reviewer now authors this correction; independent approval must
  come from another reviewer on the final committed bytes.
notes:
- 'PR #2061 bundle remediation issue #2635; canonical cultivation stays open.'
tags:
- pr2061
- append-only
- source-locator-correction
- bounded-science
```
