# A2-165 monoculture: native species-descriptor ambiguity diagnostic

- Review: 20261115T061642Z-faecalibacterium-ambiguity-diagnostic
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-11-15T06:16:41.650526Z
- Finished UTC: 2026-11-15T06:16:42.119862Z
- Reviewer: codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: false

## Summary

One existing species descriptor now records AMBIGUOUS and all three native GTDB alternatives. Actual guarded M5 application, append-only history and eight required native commands are bound to their evidence. No GTDB species is assigned to A2-165/JCM31915 and no whole-record scientific approval is claimed.

## Scope And Provenance

Status/candidate computability and actual application provenance only.

Selection: First end-to-end canary for the15 pure ambiguous records within the30-record assigned ambiguity lane; other records have not been applied by this canary.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 4a5999d5f9299a26e1aff0ffc1262bfff03a035f.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000546 | data/isolates/Faecalibacterium_Prausnitzii_A2_165_2FL_FOS_Monoculture_Baseline.yaml # taxonomy[0].taxon_term.gtdb_grounding_status; taxonomy[0].taxon_term.gtdb_candidates | maintained | A2-165 monoculture existing-species-descriptor ambiguity |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000546 | Actual M5 native command completed with exit0 and retained hash-bound log against the exact corrected record. |
| validate-strict | passed | True | CommunityMech:000546 | Actual M5 native command completed with exit0 and retained hash-bound log against the exact corrected record. |
| validate-gtdb | passed | True | CommunityMech:000546 | Actual M5 native command completed with exit0 and retained hash-bound log against the exact corrected record. |
| validate-gtdb-domain | passed | True | CommunityMech:000546 | Actual M5 native command completed with exit0 and retained hash-bound log against the exact corrected record. |
| validate-scalars | passed | True | CommunityMech:000546 | Actual M5 native command completed with exit0 and retained hash-bound log against the exact corrected record. |
| validate-terms | passed | True | CommunityMech:000546 | Actual M5 native command completed with exit0 and retained hash-bound log against the exact corrected record. |
| validate-history | passed | True | CommunityMech:000546 | Actual M5 native command completed with exit0 and retained hash-bound log against the exact corrected record. |
| new-history | passed | True | CommunityMech:000546 | Actual M5 native command completed with exit0 and retained hash-bound log against the exact corrected record. |

## Scientific And Domain Assessments

### Complete ambiguity on the unchanged species descriptor

grounding: supported. Targets: CommunityMech:000546.

NCBI853 remains the declared descriptor. Native761 yields three alternatives; AMBIGUOUS plus the complete list reproduces that result without a grounding block or a selected stock species.

### Actual guarded write and append-only history

provenance: supported. Targets: CommunityMech:000546.

The accepted after bytes persist on M5. Full native inline event reconstruction, captured source checks and the validated writer guarded replacement. Existing sidecars and the immutable historical ledger remain unchanged; exactly one new sidecar records the bounded correction.

### Species-descriptor alternatives do not resolve study-stock nomenclature

scope: supported. Targets: CommunityMech:000546.

The study's A2-165/JCM31915 designation, biological content and quotations are preserved. Alternative species names from a species-level crosswalk do not identify this stock; the duncaniae naming question remains outside the correction. Historical assay conclusions and knowledge gaps are not newly certified.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| schema | .temp/gtdb-ambiguity-20261115/ambiguity-canary-run-schema-001/native.log | supports | Actual M5 native command completed with exit0 and retained hash-bound log against the exact corrected record. |
| strict | .temp/gtdb-ambiguity-20261115/ambiguity-canary-run-strict-001/native.log | supports | Actual M5 native command completed with exit0 and retained hash-bound log against the exact corrected record. |
| gtdb | .temp/gtdb-ambiguity-20261115/ambiguity-canary-run-gtdb-001/native.log | supports | Actual M5 native command completed with exit0 and retained hash-bound log against the exact corrected record. |
| domain | .temp/gtdb-ambiguity-20261115/ambiguity-canary-run-domain-001/native.log | supports | Actual M5 native command completed with exit0 and retained hash-bound log against the exact corrected record. |
| scalars | .temp/gtdb-ambiguity-20261115/ambiguity-canary-run-scalars-001/native.log | supports | Actual M5 native command completed with exit0 and retained hash-bound log against the exact corrected record. |
| terms | .temp/gtdb-ambiguity-20261115/ambiguity-canary-run-terms-001/native.log | supports | Actual M5 native command completed with exit0 and retained hash-bound log against the exact corrected record. |
| history | .temp/gtdb-ambiguity-20261115/ambiguity-canary-run-history-001/native.log | supports | Actual M5 native command completed with exit0 and retained hash-bound log against the exact corrected record. |
| new-history | .temp/gtdb-ambiguity-20261115/ambiguity-canary-run-new-history-001/native.log | supports | Actual M5 native command completed with exit0 and retained hash-bound log against the exact corrected record. |
| native-route | .temp/gtdb-ambiguity-20261115/ambiguity-diagnostic-002/native-route.json; result/status/candidates | supports | Actual native recomputation against exact761 returns AMBIGUOUS and all three GTDB alternatives for NCBI853/Faecalibacterium prausnitzii. The stored list matches in full; no candidate is selected as a strain identity. |
| primary-stock | https://doi.org/10.3390/microorganisms14081812; Methods2.1, sec2dot1-microorganisms-14-01812; retained PMC13515949 XML | context_only | The inspected primary Methods names 'Faecalibacterium prausnitzii A2-165 (JCM31915)'. This supports retaining the source stock and name, not choosing a GTDB species. The bibliography also cites a2024 paper naming A2-165 Faecalibacterium duncaniae; independent stock/genome nomenclature adjudication is outside this correction. |
| actual-application | .temp/gtdb-ambiguity-20261115/ambiguity-apply-001/receipt.json; applied/before_sha256/after_sha256/inputs | supports | One actual M5 guarded apply persisted the exact independently accepted candidate. Captured pre-apply canonical bytes remain in before.yaml; the current canonical hash is separately bound to the accepted after state. |
| historical-science | reports/causal_graph_review/decisions/20261110-stage2-seven-records-batch146.yaml; records[id=CommunityMech:000546], node_decisions/source_backed_gaps | context_only | The original batch146 ledger remains unchanged. Its one-node/zero-arrow monoculture assessment,5 graph evidence snippets and unresolved metabolic-flux gap are preserved, not newly certified. Its historical UNRESOLVED wording describes the predecessor state. |

## Limits And Additional Notes

- Diagnostic-only partial scope. No full scientific review, study-strain assembly analysis, selected GTDB species, higher-priority issue closure or campaign completion is claimed.
- The exact crosswalk SHA761 is pinned; file time does not establish release/build provenance. Native results describe the existing species-level input, not strain-level classification.
- Eight native scoped commands passed on M5 Python3.13.2 at4a5999d5, including seven validation gates and one sidecar creation. References, corpus QC and generated pages are not claimed passed by this diagnostic.
- Full-record completeness/quality scores are not recomputed for this narrow status/provenance assessment. Deterministic validation does not establish scientific correctness.
- The original local301 stage001 and M5 stage001 remain preserved. A fresh M5 stage002 used the same published4a5999d5 launcher and avoided overwriting the local predecessor evidence namespace.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261115T061642Z-faecalibacterium-ambiguity-diagnostic
kind: record
repository: CultureBotAI/CommunityMech
title: 'A2-165 monoculture: native species-descriptor ambiguity diagnostic'
started_at: '2026-11-15T06:16:41.650526Z'
finished_at: '2026-11-15T06:16:42.119862Z'
reviewer:
  identity: codex
  kind: agent
  independence: self_review
  independence_basis: Authored the scoped correction; root independently reviewed
    primary-source scope, local and exact M5 candidates, guarded application and native
    gate wrapper before execution.
skill: review-yaml-record
completion: completed
verdict: pass_with_limitations
scientific_review: false
summary: One existing species descriptor now records AMBIGUOUS and all three native
  GTDB alternatives. Actual guarded M5 application, append-only history and eight
  required native commands are bound to their evidence. No GTDB species is assigned
  to A2-165/JCM31915 and no whole-record scientific approval is claimed.
source:
  git_revision: 4a5999d5f9299a26e1aff0ffc1262bfff03a035f
  state: working_tree
  inputs:
  - path: .temp/gtdb-ambiguity-20261115/ambiguity-apply-001/before.yaml
    sha256: b6dc768bf6f705611933fc50882d91957225ef1e32c61330e1adb717fe175790
    role: context
  - path: .temp/gtdb-ambiguity-20261115/ambiguity-apply-001/receipt.json
    sha256: 9aae41ac2845de3d650de74e2913d0b469c30fc8fddd332eb70eb9fa8293e785
    role: context
  - path: .temp/gtdb-ambiguity-20261115/ambiguity-canary-run-domain-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-ambiguity-20261115/ambiguity-canary-run-domain-001/native.log
    sha256: 5245459e45625c1c6fdf695f7ff7ef7e212e3aac20a477d85e86bc35b31003d9
    role: context
  - path: .temp/gtdb-ambiguity-20261115/ambiguity-canary-run-domain-001/receipt.json
    sha256: 90a6ef742c6ce1240e3f375be73a9c39e98a5e5b71646978e1c268e840b34d9c
    role: context
  - path: .temp/gtdb-ambiguity-20261115/ambiguity-canary-run-domain-001/start.json
    sha256: ff888ae09b7c8bfc0403c198c13013e0cc527be7040ffacec2c56b9b5d4f28f9
    role: context
  - path: .temp/gtdb-ambiguity-20261115/ambiguity-canary-run-gtdb-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-ambiguity-20261115/ambiguity-canary-run-gtdb-001/native.log
    sha256: c2ed85a81727aebb9b24129e3bc8d17525666ddf04b65bcbe3a20aded2400a75
    role: context
  - path: .temp/gtdb-ambiguity-20261115/ambiguity-canary-run-gtdb-001/receipt.json
    sha256: 2a04f3489d50291dbeeeb2fc8a2ec68100cec039d52e89b89eeafa5ecf2a58ca
    role: context
  - path: .temp/gtdb-ambiguity-20261115/ambiguity-canary-run-gtdb-001/start.json
    sha256: 690dc9b93f3ddcc6ce3b4c1390590bdcc427fb860a2d6ddb14ccfee8f20ce6dc
    role: context
  - path: .temp/gtdb-ambiguity-20261115/ambiguity-canary-run-history-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-ambiguity-20261115/ambiguity-canary-run-history-001/native.log
    sha256: 700b44227c4cf01270ac26f16b308622de0b26f48d71aec49cdfaaab87620f0a
    role: context
  - path: .temp/gtdb-ambiguity-20261115/ambiguity-canary-run-history-001/receipt.json
    sha256: 30f85dc609a3809797c6e8bbe6ff16193f3c7bfad4ea51d980c1ee138e1d4de8
    role: context
  - path: .temp/gtdb-ambiguity-20261115/ambiguity-canary-run-history-001/start.json
    sha256: b8c401562c823587d635b85b5f27b1bcd21107ee13cf3adeb4c8d6ffb743c7d8
    role: context
  - path: .temp/gtdb-ambiguity-20261115/ambiguity-canary-run-new-history-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-ambiguity-20261115/ambiguity-canary-run-new-history-001/native.log
    sha256: a436f53ae8052afaf0ca9f05420a123695f6061a0cb0eca1640bd5fc256256e3
    role: context
  - path: .temp/gtdb-ambiguity-20261115/ambiguity-canary-run-new-history-001/receipt.json
    sha256: 12fcd45c1038377ffef83c7cf0cd67ed064caf1812a4739caba8495a870327a7
    role: context
  - path: .temp/gtdb-ambiguity-20261115/ambiguity-canary-run-new-history-001/start.json
    sha256: 99aecfcbc546648edc9278d5be5e2277dc9452b6d5fa94d38ef26b6a39717426
    role: context
  - path: .temp/gtdb-ambiguity-20261115/ambiguity-canary-run-scalars-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-ambiguity-20261115/ambiguity-canary-run-scalars-001/native.log
    sha256: 0875129edb9998dc392d048d817e0570bfd46b127271d6f8aa2b5f0d83650ba9
    role: context
  - path: .temp/gtdb-ambiguity-20261115/ambiguity-canary-run-scalars-001/receipt.json
    sha256: d8320d560733c108c9579b1b327bfa237e671b65e174e7589f163befa3e32b7e
    role: context
  - path: .temp/gtdb-ambiguity-20261115/ambiguity-canary-run-scalars-001/start.json
    sha256: ff7f2f492bd80f129f283ea8190ea03be676322de3ce7661ab02a0efc31cd5c4
    role: context
  - path: .temp/gtdb-ambiguity-20261115/ambiguity-canary-run-schema-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-ambiguity-20261115/ambiguity-canary-run-schema-001/native.log
    sha256: 373b7045ffd2b6f0a76de435e848d003f85fc889b64ab7626f640c26c522b257
    role: context
  - path: .temp/gtdb-ambiguity-20261115/ambiguity-canary-run-schema-001/receipt.json
    sha256: 2987e7ea79d0e9761e16b2a85855a507bac133b3a112fdefec23a4911bd87a85
    role: context
  - path: .temp/gtdb-ambiguity-20261115/ambiguity-canary-run-schema-001/start.json
    sha256: d893406410c1773fd38ec64f9c8b1627f8c54326b46a9f538a51f0f5be758ce4
    role: context
  - path: .temp/gtdb-ambiguity-20261115/ambiguity-canary-run-strict-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-ambiguity-20261115/ambiguity-canary-run-strict-001/native.log
    sha256: 0e46923619a129446f9c2c09cf89f3950decb47fd9000f9aa929d654be61a86f
    role: context
  - path: .temp/gtdb-ambiguity-20261115/ambiguity-canary-run-strict-001/receipt.json
    sha256: 94c64cc98312f755c24d6f2f8c7aba99891d83066bd727e6ad89ffd6033aa64e
    role: context
  - path: .temp/gtdb-ambiguity-20261115/ambiguity-canary-run-strict-001/start.json
    sha256: 43abe32aba37aa56fc4a736c7310864d47b8878f803996c797aeb7ba5997b421
    role: context
  - path: .temp/gtdb-ambiguity-20261115/ambiguity-canary-run-strict-001/strict.tsv
    sha256: b184ed5450b968070bb6c75648407e388f41a1eaf7017890723cf560999fc3f7
    role: context
  - path: .temp/gtdb-ambiguity-20261115/ambiguity-canary-run-terms-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-ambiguity-20261115/ambiguity-canary-run-terms-001/native.log
    sha256: 06509789ea90f51ebf118ba928651c866deef1ae177f0185c91263fb7ed05587
    role: context
  - path: .temp/gtdb-ambiguity-20261115/ambiguity-canary-run-terms-001/receipt.json
    sha256: 4d3b98fef4fa24bc92b5912e4e5ef6173194c1a580e9f4e13487344f627d1b5a
    role: context
  - path: .temp/gtdb-ambiguity-20261115/ambiguity-canary-run-terms-001/start.json
    sha256: 10893afaeb857d33bcb06ebfab180479432e7fa83d19aefb7389b653157bdd0a
    role: context
  - path: .temp/gtdb-ambiguity-20261115/ambiguity-candidate-002/Faecalibacterium_Prausnitzii_A2_165_2FL_FOS_Monoculture_Baseline.yaml
    sha256: d1843b01c495ca1a2c44820435e3a60b76e65089eff627590c26b5d0e003bcb6
    role: context
  - path: .temp/gtdb-ambiguity-20261115/ambiguity-candidate-002/candidate.diff
    sha256: e3721e212ff7cdbfeeb72f6ff616f30d170aed2c953534b58f38d9bffa80c5c1
    role: context
  - path: .temp/gtdb-ambiguity-20261115/ambiguity-candidate-002/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-ambiguity-20261115/ambiguity-candidate-002/native.log
    sha256: 1469fd1b893db4f0bed3e32d06210d41cb0669a7e4d299e2172ff890839aae76
    role: context
  - path: .temp/gtdb-ambiguity-20261115/ambiguity-candidate-002/receipt.json
    sha256: 119857aa803307d6656f0c31a44f707a8d5d6a9ca3c60a0134e7bc113a5196d9
    role: context
  - path: .temp/gtdb-ambiguity-20261115/ambiguity-diagnostic-002/native-route.json
    sha256: 14eac1a65940bb8315b53c2c39cfa3ec1585c8f157e0e950ab448eb092076756
    role: context
  - path: .temp/gtdb-ambiguity-20261115/faecalibacterium-source-001/article.xml
    sha256: c5b4d94fcd98543be47d7eb623a69180ae15cc98dbe1a3b1ad772818f65d421e
    role: context
  - path: .temp/gtdb-ambiguity-20261115/faecalibacterium-source-001/receipt.json
    sha256: 994309faf073afbdb272fcb08bf7c905b2bec72f92db0adca14b442361ea0fcb
    role: context
  - path: .temp/gtdb-ambiguity-20261115/faecalibacterium-source-001/stock-identity.json
    sha256: ccdda3eb06aa62a6d56a1fe31521333b05d5740dd4dd2817faa1d1b2de4681ef
    role: context
  - path: .temp/gtdb-ambiguity-20261115/kg-microbe/data/raw/NCBI2GTDB.tsv.gz
    sha256: 761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd
    role: context
  - path: .temp/gtdb-ambiguity-20261115/residual-groups-001.json
    sha256: eaf78e16c342e36a0aa82c52c45888e8efb667fc2b70aa8d77ead956024f5f7c
    role: context
  - path: data/isolates/Faecalibacterium_Prausnitzii_A2_165_2FL_FOS_Monoculture_Baseline.yaml
    sha256: d1843b01c495ca1a2c44820435e3a60b76e65089eff627590c26b5d0e003bcb6
    role: target
  - path: history/records/Faecalibacterium_Prausnitzii_A2_165_2FL_FOS_Monoculture_Baseline/2026-11-10T085200Z-antigravity-000546.yaml
    sha256: f5fbf994cfbb25266abbe84ba6f8d72656736aaeae16347d386be0b017e8de80
    role: context
  - path: history/records/Faecalibacterium_Prausnitzii_A2_165_2FL_FOS_Monoculture_Baseline/2026-11-10T113505Z-antigravity-c14s205.yaml
    sha256: d3e8f5a15d4b46018f377db26858fdefdc385c14f630b79756f13de0b556a7d2
    role: context
  - path: history/records/Faecalibacterium_Prausnitzii_A2_165_2FL_FOS_Monoculture_Baseline/2026-11-15T060616Z-codex-7ba0d3.yaml
    sha256: 145993854de6f4e6fc6a74ef03761367f8f9b20994b84117bb4bbc46e9b47f33
    role: context
  - path: justfile
    sha256: 40369611ad4531582e420df0e9ff22109e4b18adf03b34d86b54200b280f2d0f
    role: context
  - path: references_cache/PMID_42655156.txt
    sha256: f40ae202ccae35dad94ef7ed446f94adc2d089879ac64cec97302fc090b35e4c
    role: context
  - path: reports/causal_graph_review/decisions/20261110-stage2-seven-records-batch146.yaml
    sha256: 158e6c4f1e69e14e8b9827f04f1664a8dcbc661a652a7d4f94a3eb316f576015
    role: context
  - path: scripts/adhoc/apply_ambiguity_status_canary_20261115.py
    sha256: 80be1c10840b3f475ce43893d9a24a132749dbd70bcf997e0e6314273bae53e1
    role: context
  - path: scripts/adhoc/build_ambiguity_diagnostic_20261115.py
    sha256: bcdac9cecdaf81dde55519f4f623e65c48d8d9454be7fd35dc243b660af35ab2
    role: context
  - path: scripts/adhoc/capture_faecalibacterium_ambiguity_source_20261115.py
    sha256: 262957ef84c89ee23f4f1cb8a6ae7d9751f50a267b7acf0d1d6ffb694a7a2064
    role: context
  - path: scripts/adhoc/check_ambiguity_canary_20261115.py
    sha256: 7338e43dcb1056d8b0189c2a91c8d73ee14a6133bbb8b10c17dc3f448cbdfec8
    role: context
  - path: scripts/adhoc/stage_ambiguity_status_canary_20261115.py
    sha256: 3971c367bc04db09aa378a15a227cb6ecf0aeb7139f5011de215eeca32b0524e
    role: context
  - path: scripts/gtdb_ground.py
    sha256: 0fc1ba926a56e5be85cdf064db0cf56452aeeee93f15b0ced98e8f11b5296175
    role: context
  - path: src/communitymech/curate/curation_event.py
    sha256: 58ebdb58ac39d7a319156ec735db9ef2e9afb4c7350613039ad9dc49d65a5afc
    role: context
  - path: src/communitymech/ontology_adapters.py
    sha256: 7e0a621831b28ac0f718a29c22af8052f93e006012fff77e11d92849e4852c45
    role: context
  - path: src/communitymech/schema/communitymech.yaml
    sha256: c6f6e4a5cf42e450cf55d8fcb12817591c736198e24bcd217142b4f86712b4c3
    role: context
  - path: src/communitymech/schema/history.yaml
    sha256: b01b06f1b9a37db205c26c31ec0fd910690848507c7e1bfb73b424ac0829c52d
    role: context
  - path: src/communitymech/validation/write_validated.py
    sha256: d19dd3b1e46856b4de67ecc17fc856aaa1034a9a97259cab3bbd54c3891fb019
    role: context
  - path: src/communitymech/validators/ncbi_domain.py
    sha256: b1e7ffc3c35c237e36c2c19fab42f1d42a14161397de9c5e726ed85897f1e262
    role: context
  - path: tests/test_causal_review_batch146.py
    sha256: c8a4eaeeb1eff403648edfe7886bbe4abd4165def97dbdae6b31f7ef7ad30cf9
    role: context
  - path: uv.lock
    sha256: 712838f8fa3d68fbd818ac8162f3f1e2f2637db1da1a8ebfaba0ef759690f3b4
    role: context
targets:
- target_id: CommunityMech:000546
  path: data/isolates/Faecalibacterium_Prausnitzii_A2_165_2FL_FOS_Monoculture_Baseline.yaml
  selector: taxonomy[0].taxon_term.gtdb_grounding_status; taxonomy[0].taxon_term.gtdb_candidates
  label: A2-165 monoculture existing-species-descriptor ambiguity
  kind: maintained
  ownership_note: CommunityMech owns the stored status/candidate fields; the unchanged
    native classifier computes the full ambiguity set for the existing NCBI853 descriptor.
    Exact study-strain species/genome identity is not inferred.
scope:
  description: Status/candidate computability and actual application provenance only.
  selection: First end-to-end canary for the15 pure ambiguous records within the30-record
    assigned ambiguity lane; other records have not been applied by this canary.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000546
  exclusions:
  - target: Study-strain species/genome identity and all experimental, ecological,
      cultivation or mechanism claims
    reason: Existing content is preserved; independent full scientific and nomenclature
      reassessment is outside this diagnostic.
  - target: Other29 assigned records and corpus
    reason: Metadata intake is not a current classifier result, application, or scientific
      review.
checks:
- check_id: schema
  name: validate
  status: passed
  required: true
  summary: Actual M5 native command completed with exit0 and retained hash-bound log
    against the exact corrected record.
  target_ids:
  - CommunityMech:000546
  command: just --verbose --no-dotenv --color never validate data/isolates/Faecalibacterium_Prausnitzii_A2_165_2FL_FOS_Monoculture_Baseline.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - schema
  scope_note: One record; history validates its complete sidecar directory. Not corpus
    QC or scientific evidence validation.
- check_id: strict
  name: validate-strict
  status: passed
  required: true
  summary: Actual M5 native command completed with exit0 and retained hash-bound log
    against the exact corrected record.
  target_ids:
  - CommunityMech:000546
  command: just --verbose --no-dotenv --color never validate-strict data/isolates/Faecalibacterium_Prausnitzii_A2_165_2FL_FOS_Monoculture_Baseline.yaml
    --out .temp/gtdb-ambiguity-20261115/ambiguity-canary-run-strict-001/strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - strict
  scope_note: One record; history validates its complete sidecar directory. Not corpus
    QC or scientific evidence validation.
- check_id: gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: Actual M5 native command completed with exit0 and retained hash-bound log
    against the exact corrected record.
  target_ids:
  - CommunityMech:000546
  command: just --verbose --no-dotenv --color never validate-gtdb data/isolates/Faecalibacterium_Prausnitzii_A2_165_2FL_FOS_Monoculture_Baseline.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - gtdb
  scope_note: One record; history validates its complete sidecar directory. Not corpus
    QC or scientific evidence validation.
- check_id: domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: Actual M5 native command completed with exit0 and retained hash-bound log
    against the exact corrected record.
  target_ids:
  - CommunityMech:000546
  command: just --verbose --no-dotenv --color never validate-gtdb-domain data/isolates/Faecalibacterium_Prausnitzii_A2_165_2FL_FOS_Monoculture_Baseline.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - domain
  scope_note: One record; history validates its complete sidecar directory. Not corpus
    QC or scientific evidence validation.
- check_id: scalars
  name: validate-scalars
  status: passed
  required: true
  summary: Actual M5 native command completed with exit0 and retained hash-bound log
    against the exact corrected record.
  target_ids:
  - CommunityMech:000546
  command: just --verbose --no-dotenv --color never validate-scalars data/isolates/Faecalibacterium_Prausnitzii_A2_165_2FL_FOS_Monoculture_Baseline.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - scalars
  scope_note: One record; history validates its complete sidecar directory. Not corpus
    QC or scientific evidence validation.
- check_id: terms
  name: validate-terms
  status: passed
  required: true
  summary: Actual M5 native command completed with exit0 and retained hash-bound log
    against the exact corrected record.
  target_ids:
  - CommunityMech:000546
  command: just --verbose --no-dotenv --color never validate-terms data/isolates/Faecalibacterium_Prausnitzii_A2_165_2FL_FOS_Monoculture_Baseline.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - terms
  scope_note: One record; history validates its complete sidecar directory. Not corpus
    QC or scientific evidence validation.
- check_id: history
  name: validate-history
  status: passed
  required: true
  summary: Actual M5 native command completed with exit0 and retained hash-bound log
    against the exact corrected record.
  target_ids:
  - CommunityMech:000546
  command: just --verbose --no-dotenv --color never validate-history history/records/Faecalibacterium_Prausnitzii_A2_165_2FL_FOS_Monoculture_Baseline
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - history
  scope_note: One record; history validates its complete sidecar directory. Not corpus
    QC or scientific evidence validation.
- check_id: new-history
  name: new-history
  status: passed
  required: true
  summary: Actual M5 native command completed with exit0 and retained hash-bound log
    against the exact corrected record.
  target_ids:
  - CommunityMech:000546
  command: 'just --verbose --no-dotenv --color never new-history --kind record --slug
    Faecalibacterium_Prausnitzii_A2_165_2FL_FOS_Monoculture_Baseline --target-root
    data/isolates --event EDIT --outcome changed --sections taxonomy,curation_history
    --actor-name codex --model gpt-6 --agent-tool codex --issue https://github.com/CultureBotAI/CommunityMech/issues/2848
    --pr https://github.com/CultureBotAI/CommunityMech/pull/2804 --summary ''Retain
    all native GTDB alternatives for the existing species descriptor'' --details ''Applied
    the independently reviewed status-only M5 candidate SHA256 d1843b01c495ca1a2c44820435e3a60b76e65089eff627590c26b5d0e003bcb6.
    PMID:42655156 Methods2.1 identifies A2-165 as JCM31915, using the source name
    Faecalibacterium prausnitzii. The exact NCBI2GTDB snapshot SHA256 761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd
    returns three alternatives for the existing NCBITaxon:853 species descriptor:
    Faecalibacterium longum, Faecalibacterium prausnitzii and Faecalibacterium prausnitzii_D.
    Persist AMBIGUOUS and the complete native list without selecting a species, reidentifying
    A2-165, changing its stock designation, or modifying any biology, graph, source
    quotation or historical batch146 ledger. The cited literature also uses Faecalibacterium
    duncaniae for A2-165; stock-specific nomenclature/genome identity remains outside
    this computability correction. Actual raw application receipt .temp/gtdb-ambiguity-20261115/ambiguity-apply-001/receipt.json
    SHA256 9aae41ac2845de3d650de74e2913d0b469c30fc8fddd332eb70eb9fa8293e785. A scoped
    diagnostic assessment and actual native focused gates follow.'''
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - new-history
  scope_note: One record; history validates its complete sidecar directory. Not corpus
    QC or scientific evidence validation.
evidence:
- evidence_id: schema
  kind: validation
  reference: .temp/gtdb-ambiguity-20261115/ambiguity-canary-run-schema-001/native.log
  accessed_at: '2026-11-15T06:16:41.650526Z'
  support: supports
  summary: Actual M5 native command completed with exit0 and retained hash-bound log
    against the exact corrected record.
- evidence_id: strict
  kind: validation
  reference: .temp/gtdb-ambiguity-20261115/ambiguity-canary-run-strict-001/native.log
  accessed_at: '2026-11-15T06:16:41.650526Z'
  support: supports
  summary: Actual M5 native command completed with exit0 and retained hash-bound log
    against the exact corrected record.
- evidence_id: gtdb
  kind: validation
  reference: .temp/gtdb-ambiguity-20261115/ambiguity-canary-run-gtdb-001/native.log
  accessed_at: '2026-11-15T06:16:41.650526Z'
  support: supports
  summary: Actual M5 native command completed with exit0 and retained hash-bound log
    against the exact corrected record.
- evidence_id: domain
  kind: validation
  reference: .temp/gtdb-ambiguity-20261115/ambiguity-canary-run-domain-001/native.log
  accessed_at: '2026-11-15T06:16:41.650526Z'
  support: supports
  summary: Actual M5 native command completed with exit0 and retained hash-bound log
    against the exact corrected record.
- evidence_id: scalars
  kind: validation
  reference: .temp/gtdb-ambiguity-20261115/ambiguity-canary-run-scalars-001/native.log
  accessed_at: '2026-11-15T06:16:41.650526Z'
  support: supports
  summary: Actual M5 native command completed with exit0 and retained hash-bound log
    against the exact corrected record.
- evidence_id: terms
  kind: validation
  reference: .temp/gtdb-ambiguity-20261115/ambiguity-canary-run-terms-001/native.log
  accessed_at: '2026-11-15T06:16:41.650526Z'
  support: supports
  summary: Actual M5 native command completed with exit0 and retained hash-bound log
    against the exact corrected record.
- evidence_id: history
  kind: validation
  reference: .temp/gtdb-ambiguity-20261115/ambiguity-canary-run-history-001/native.log
  accessed_at: '2026-11-15T06:16:41.650526Z'
  support: supports
  summary: Actual M5 native command completed with exit0 and retained hash-bound log
    against the exact corrected record.
- evidence_id: new-history
  kind: validation
  reference: .temp/gtdb-ambiguity-20261115/ambiguity-canary-run-new-history-001/native.log
  accessed_at: '2026-11-15T06:16:41.650526Z'
  support: supports
  summary: Actual M5 native command completed with exit0 and retained hash-bound log
    against the exact corrected record.
- evidence_id: native-route
  kind: database
  reference: .temp/gtdb-ambiguity-20261115/ambiguity-diagnostic-002/native-route.json
  locator: result/status/candidates
  accessed_at: '2026-11-15T06:16:41.650526Z'
  support: supports
  summary: Actual native recomputation against exact761 returns AMBIGUOUS and all
    three GTDB alternatives for NCBI853/Faecalibacterium prausnitzii. The stored list
    matches in full; no candidate is selected as a strain identity.
- evidence_id: primary-stock
  kind: primary_source
  reference: https://doi.org/10.3390/microorganisms14081812
  locator: Methods2.1, sec2dot1-microorganisms-14-01812; retained PMC13515949 XML
  accessed_at: '2026-11-15T06:16:41.650526Z'
  support: context_only
  summary: The inspected primary Methods names 'Faecalibacterium prausnitzii A2-165
    (JCM31915)'. This supports retaining the source stock and name, not choosing a
    GTDB species. The bibliography also cites a2024 paper naming A2-165 Faecalibacterium
    duncaniae; independent stock/genome nomenclature adjudication is outside this
    correction.
- evidence_id: actual-application
  kind: record_content
  reference: .temp/gtdb-ambiguity-20261115/ambiguity-apply-001/receipt.json
  locator: applied/before_sha256/after_sha256/inputs
  accessed_at: '2026-11-15T06:16:41.650526Z'
  support: supports
  summary: One actual M5 guarded apply persisted the exact independently accepted
    candidate. Captured pre-apply canonical bytes remain in before.yaml; the current
    canonical hash is separately bound to the accepted after state.
- evidence_id: historical-science
  kind: prior_review
  reference: reports/causal_graph_review/decisions/20261110-stage2-seven-records-batch146.yaml
  locator: records[id=CommunityMech:000546], node_decisions/source_backed_gaps
  accessed_at: '2026-11-15T06:16:41.650526Z'
  support: context_only
  summary: The original batch146 ledger remains unchanged. Its one-node/zero-arrow
    monoculture assessment,5 graph evidence snippets and unresolved metabolic-flux
    gap are preserved, not newly certified. Its historical UNRESOLVED wording describes
    the predecessor state.
assessments:
- assessment_id: native-ambiguity
  area: grounding
  topic: Complete ambiguity on the unchanged species descriptor
  outcome: supported
  target_ids:
  - CommunityMech:000546
  evidence_ids:
  - native-route
  - gtdb
  - primary-stock
  summary: NCBI853 remains the declared descriptor. Native761 yields three alternatives;
    AMBIGUOUS plus the complete list reproduces that result without a grounding block
    or a selected stock species.
- assessment_id: actual-provenance
  area: provenance
  topic: Actual guarded write and append-only history
  outcome: supported
  target_ids:
  - CommunityMech:000546
  evidence_ids:
  - actual-application
  - new-history
  - history
  - strict
  - historical-science
  summary: The accepted after bytes persist on M5. Full native inline event reconstruction,
    captured source checks and the validated writer guarded replacement. Existing
    sidecars and the immutable historical ledger remain unchanged; exactly one new
    sidecar records the bounded correction.
- assessment_id: stock-boundary
  area: scope
  topic: Species-descriptor alternatives do not resolve study-stock nomenclature
  outcome: supported
  target_ids:
  - CommunityMech:000546
  evidence_ids:
  - primary-stock
  - historical-science
  - native-route
  summary: The study's A2-165/JCM31915 designation, biological content and quotations
    are preserved. Alternative species names from a species-level crosswalk do not
    identify this stock; the duncaniae naming question remains outside the correction.
    Historical assay conclusions and knowledge gaps are not newly certified.
findings: []
actions: []
limitations:
- Diagnostic-only partial scope. No full scientific review, study-strain assembly
  analysis, selected GTDB species, higher-priority issue closure or campaign completion
  is claimed.
- The exact crosswalk SHA761 is pinned; file time does not establish release/build
  provenance. Native results describe the existing species-level input, not strain-level
  classification.
- Eight native scoped commands passed on M5 Python3.13.2 at4a5999d5, including seven
  validation gates and one sidecar creation. References, corpus QC and generated pages
  are not claimed passed by this diagnostic.
- Full-record completeness/quality scores are not recomputed for this narrow status/provenance
  assessment. Deterministic validation does not establish scientific correctness.
- The original local301 stage001 and M5 stage001 remain preserved. A fresh M5 stage002
  used the same published4a5999d5 launcher and avoided overwriting the local predecessor
  evidence namespace.
links:
- https://github.com/CultureBotAI/CommunityMech/issues/2848
- https://github.com/CultureBotAI/CommunityMech/issues/2861
- https://github.com/CultureBotAI/CommunityMech/issues/2865
- https://github.com/CultureBotAI/CommunityMech/issues/2864
- https://github.com/CultureBotAI/CommunityMech/pull/2804
```
