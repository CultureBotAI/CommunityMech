# Scoped technical correspondence: Pelagerythrobacter isolate 000552

- Review: 20261115T060539Z-gtdb-genus-000552-canary
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-11-15T05:50:50.071830Z
- Finished UTC: 2026-11-15T06:05:39.281491Z
- Reviewer: codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: false

## Summary

One source-backed same-genus reference correspondence for Pelagerythrobacter is now GROUNDED, with seven scoped gates and both unchanged completion tests passing. All biological payload, original stock identity and historical scientific findings remain unchanged; no full scientific review or corpus-QC pass is asserted.

## Scope And Provenance

Only the database correspondence, guarded application/history chain and technical checks were assessed.

Selection: First independently accepted pure same-name higher-rank isolate candidate; original basename and source identity retained.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 90a00bc2781266cb315a8295ca40e8f1c01e46fc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000552 | data/isolates/Pelagerythrobacter_N7_Halophilic_Pyrene_Oxidation_Isolate_Baseline.yaml # taxonomy[0].taxon_term | maintained | Pelagerythrobacter study-stock genus correspondence |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | CommunityMech:000552 | Actual scoped native gate passed with a nonempty hash-verified log. |
| strict | passed | True | CommunityMech:000552 | Actual scoped native gate passed with a nonempty hash-verified log. |
| gtdb | passed | True | CommunityMech:000552 | Actual scoped native gate passed with a nonempty hash-verified log. |
| domain | passed | True | CommunityMech:000552 | Actual scoped native gate passed with a nonempty hash-verified log. |
| scalars | passed | True | CommunityMech:000552 | Actual scoped native gate passed with a nonempty hash-verified log. |
| history | passed | True | CommunityMech:000552 | Actual scoped native gate passed with a nonempty hash-verified log. |
| completion | passed | True | CommunityMech:000552 | Both unchanged native outstanding-grounding tests passed; not full QC. |
| Native LTV with explicit local adapters | passed | True | CommunityMech:000552 | Native LTV binding/label check used explicit existing SQLite adapters and blocked network; database stat identities stayed unchanged, byte hashes were not measured. |

## Scientific And Domain Assessments

### Same-genus database correspondence

grounding: supported. Targets: CommunityMech:000552.

The existing declared Pelagerythrobacter genus maps to GTDB:g__Pelagerythrobacter at 16/16 named-binomial reference genomes, not reclassified. This database correspondence does not establish the exact study-stock species, genome or mechanisms.

### Preserved biological bytes and earlier assessment

provenance: supported. Targets: CommunityMech:000552.

The exact old full record remains retained; only the genus block, GROUNDED status and two native inline events changed. Native sidecar and actual application evidence are bound. Earlier UNRESOLVED reflects the prior database result and is not overwritten in its immutable review. Historical scientific needs-curation findings remain open.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| schema | .temp/gtdb-code006-20261115/isolate-000552-run-schema-001.log | supports | Actual scoped native gate passed with a nonempty hash-verified log. |
| strict | .temp/gtdb-code006-20261115/isolate-000552-run-strict-001.log | supports | Actual scoped native gate passed with a nonempty hash-verified log. |
| gtdb | .temp/gtdb-code006-20261115/isolate-000552-run-gtdb-001.log | supports | Actual scoped native gate passed with a nonempty hash-verified log. |
| domain | .temp/gtdb-code006-20261115/isolate-000552-run-domain-001.log | supports | Actual scoped native gate passed with a nonempty hash-verified log. |
| scalars | .temp/gtdb-code006-20261115/isolate-000552-run-scalars-001.log | supports | Actual scoped native gate passed with a nonempty hash-verified log. |
| history | .temp/gtdb-code006-20261115/isolate-000552-run-history-001.log | supports | Actual scoped native gate passed with a nonempty hash-verified log. |
| completion | .temp/gtdb-code006-20261115/isolate-000552-run-completion-001.log | supports | Both unchanged native outstanding-grounding tests passed; not full QC. |
| terms | .temp/gtdb-code006-20261115/isolate-000552-terms-001/native.log | supports | Native LTV binding/label check used explicit existing SQLite adapters and blocked network; database stat identities stayed unchanged, byte hashes were not measured. |
| application | .temp/gtdb-code006-20261115/isolate-000552-applied-001/receipt.json | supports | Exact actual guarded application, retained original bytes and append-only history; biology outside the mapping/status is unchanged. |
| mapping | .temp/gtdb-code006-20261115/isolate-000552-native-recomputation-001.json | supports | Native same-genus NCBITaxon:2800685 correspondence to GTDB:g__Pelagerythrobacter: 16/16 named reference genomes. This does not identify the study stock species or genome. |
| primary | references_cache/PMID_42666409.txt | supports | Existing primary Section3.1 supports the named genus of this study stock. This bounded check preserves all other source and biological assertions. |
| previous | reviews/structured/20261111T121000Z-c15s4-record-deep-audit/review.yaml | context_only | Immutable earlier full scientific review and all unresolved findings retained; this is not its replacement. |

## Limits And Additional Notes

- Partial technical assessment only: no new full-paper/supplement review, reference sweep, stock genome/species inference, mechanism approval or scientific status promotion.
- The term check is the installed native CLI with explicit local NCBI/ENVO/CHEBI adapters, not literally the just validate-terms recipe. Adapter stat identities were checked; database byte hashes were not measured.
- Seven scoped gates and two outstanding-grounding tests passed; full corpus status reproducibility, historical successor acceptance and full QC are separate gates.
- Exact M5 native execution revision is recorded, with additional hashed orchestration helpers. No record or issue outside this target is declared completed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261115T060539Z-gtdb-genus-000552-canary
kind: record
repository: CultureBotAI/CommunityMech
title: 'Scoped technical correspondence: Pelagerythrobacter isolate 000552'
started_at: '2026-11-15T05:50:50.071830Z'
finished_at: '2026-11-15T06:05:39.281491Z'
reviewer:
  identity: codex
  kind: agent
  independence: self_review
  independence_basis: Authored application and assessment; parent independently reviewed
    exact candidate, source limits and guard before application.
skill: review-yaml-record
completion: completed
verdict: pass_with_limitations
scientific_review: false
summary: One source-backed same-genus reference correspondence for Pelagerythrobacter
  is now GROUNDED, with seven scoped gates and both unchanged completion tests passing.
  All biological payload, original stock identity and historical scientific findings
  remain unchanged; no full scientific review or corpus-QC pass is asserted.
source:
  git_revision: 90a00bc2781266cb315a8295ca40e8f1c01e46fc
  state: working_tree
  inputs:
  - path: .temp/gtdb-code006-20261115/genus-subset-plan-001.json
    sha256: 1501b8ec1b52aaf7936c9da2a48f4ee208b9e22f4b7bac135dcf5856a4363ae2
    role: context
  - path: .temp/gtdb-code006-20261115/isolate-000552-applied-001/before.yaml
    sha256: 16d14ed3792a286afedaa4f17ba1c1773ebb04c6a7e8fc622cb7d946ce4c9610
    role: context
  - path: .temp/gtdb-code006-20261115/isolate-000552-applied-001/receipt.json
    sha256: a7028694096f20d8cc2823d54e9e39059ed2ba881ffe5d0b781cf2d2e803657f
    role: context
  - path: .temp/gtdb-code006-20261115/isolate-000552-candidate-001/Pelagerythrobacter_N7_Halophilic_Pyrene_Oxidation_Isolate_Baseline.yaml
    sha256: 829a5326f0770993ee3cb06dbdcc275f489942a84c1206f7bb5adb43468b1896
    role: context
  - path: .temp/gtdb-code006-20261115/isolate-000552-candidate-001/native.exit
    sha256: 7211ad359c55dcd75c38c53c5da3fe7c80724fec884b8ac9042a261f3e14caa4
    role: context
  - path: .temp/gtdb-code006-20261115/isolate-000552-candidate-001/native.log
    sha256: d5005413e5a7c92b5bfef5cf2dfd1da7cc75903e515eb4f793ee9bd7956bbe3b
    role: context
  - path: .temp/gtdb-code006-20261115/isolate-000552-candidate-001/receipt.json
    sha256: 0f00e5a783ff0906673e443d90d04af06169e4127d61d31cf4879adf6cbcfdaa
    role: context
  - path: .temp/gtdb-code006-20261115/isolate-000552-native-recomputation-001.json
    sha256: bf035a797cc17a8d1919437e7c17329fde289b173a3ac3767e9f6a513340f3c8
    role: context
  - path: .temp/gtdb-code006-20261115/isolate-000552-run-completion-001.command.txt
    sha256: b0c70c864716d2d7b1579f7581420b5c77c6b1082dccb168aa10ec211e879f39
    role: context
  - path: .temp/gtdb-code006-20261115/isolate-000552-run-completion-001.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/isolate-000552-run-completion-001.finished.txt
    sha256: 58c4865d9e83f4a85efaeb8941e9a06690014e7d0832cb09dbc5d4c5bcdd2df7
    role: context
  - path: .temp/gtdb-code006-20261115/isolate-000552-run-completion-001.log
    sha256: d6c43d7380dc621915a95897251e55f226a1f9be015a502eb28f937fd80206c3
    role: context
  - path: .temp/gtdb-code006-20261115/isolate-000552-run-completion-001.log.sha256
    sha256: 66e1270d80b63961217262861d3f6cd88314c08d72a9283929434a6bc3470903
    role: context
  - path: .temp/gtdb-code006-20261115/isolate-000552-run-completion-001.start.txt
    sha256: c676b2d783407929c62e37f0050abedc7794fdff87b929a67aa4b0911b717ee3
    role: context
  - path: .temp/gtdb-code006-20261115/isolate-000552-run-domain-001.command.txt
    sha256: ade42c371953f20962679b53aaa42d2c8647fd128b2c04c2b16dfba1dbf8aa0a
    role: context
  - path: .temp/gtdb-code006-20261115/isolate-000552-run-domain-001.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/isolate-000552-run-domain-001.finished.txt
    sha256: bff6eee14b8154fbc84206bc5079bb8800e819d1249d10de0caff9670b694118
    role: context
  - path: .temp/gtdb-code006-20261115/isolate-000552-run-domain-001.log
    sha256: ce11a2c8459835466cc47f32da44e6268e1b07d1f03f50600dc2c49077162b6e
    role: context
  - path: .temp/gtdb-code006-20261115/isolate-000552-run-domain-001.log.sha256
    sha256: 25db2abee0e63c595a4e9bc23688b9f7a234db33531197d7d636c100e4afe55f
    role: context
  - path: .temp/gtdb-code006-20261115/isolate-000552-run-domain-001.start.txt
    sha256: 14c71510e69a82f13207ffcf12e692cb18541feda57800018951a6d0d78cf441
    role: context
  - path: .temp/gtdb-code006-20261115/isolate-000552-run-gtdb-001.command.txt
    sha256: b27e9b57dcf58590ad99f99c2567f306aef74f87ddc44086cd4dc63f50411f89
    role: context
  - path: .temp/gtdb-code006-20261115/isolate-000552-run-gtdb-001.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/isolate-000552-run-gtdb-001.finished.txt
    sha256: 1618d302d9af4eff5e9cf68d04175ce6ca39db85e10fd7d992d44b145bf961f5
    role: context
  - path: .temp/gtdb-code006-20261115/isolate-000552-run-gtdb-001.log
    sha256: 1b37d1414fda8d03a6da8442d83cd1ba1002d0c031727263990470cc270aa6fe
    role: context
  - path: .temp/gtdb-code006-20261115/isolate-000552-run-gtdb-001.log.sha256
    sha256: d3755a71fe11c31c423a7bb77371db8db0a631276dc84b56a74718778e61b0a7
    role: context
  - path: .temp/gtdb-code006-20261115/isolate-000552-run-gtdb-001.start.txt
    sha256: 40820a56d2301a4bfc3df09c1769246d54cf4bdda16bcac930b94c8fb7f0091e
    role: context
  - path: .temp/gtdb-code006-20261115/isolate-000552-run-history-001.command.txt
    sha256: 6f113d0c089361778922e8e3ea00ebc711381d847bf0aed1b8ec851ef0fe1a94
    role: context
  - path: .temp/gtdb-code006-20261115/isolate-000552-run-history-001.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/isolate-000552-run-history-001.finished.txt
    sha256: fa2e94caf7c76ef63e4200eff0943a165312fd6aa034038c7fd8f491db927c19
    role: context
  - path: .temp/gtdb-code006-20261115/isolate-000552-run-history-001.log
    sha256: 700b44227c4cf01270ac26f16b308622de0b26f48d71aec49cdfaaab87620f0a
    role: context
  - path: .temp/gtdb-code006-20261115/isolate-000552-run-history-001.log.sha256
    sha256: caef09aead88fe47c3692f1818755ec7185313fec6f2e2936bc96bb58974f5fc
    role: context
  - path: .temp/gtdb-code006-20261115/isolate-000552-run-history-001.start.txt
    sha256: 79168009b7b2029d9f96a4b41426782c73589fc91782c2fe2725ed0608128439
    role: context
  - path: .temp/gtdb-code006-20261115/isolate-000552-run-new-history-001.command.txt
    sha256: b3338c8fb819eb6d36e9d392687dc752522367d869bb66ea5b328b75a2acbf32
    role: context
  - path: .temp/gtdb-code006-20261115/isolate-000552-run-new-history-001.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/isolate-000552-run-new-history-001.finished.txt
    sha256: efb2a2da8d70523a467e43901199eb13221775036a24f0b026b198b13f4ed6da
    role: context
  - path: .temp/gtdb-code006-20261115/isolate-000552-run-new-history-001.log
    sha256: 43c747afaef3cafbabfeb6a88fe561af1c117d1f5807f0fe62d98b72430ac7e1
    role: context
  - path: .temp/gtdb-code006-20261115/isolate-000552-run-new-history-001.log.sha256
    sha256: 01acd4a7af7ea7bec03a53af6a27f34d133223ca8e7017510068d774af775c1b
    role: context
  - path: .temp/gtdb-code006-20261115/isolate-000552-run-new-history-001.start.txt
    sha256: b461e42fac9b8ed00157b3e3a7c69fa3d528c2e0cccb9688c78afda4cdfbbdc5
    role: context
  - path: .temp/gtdb-code006-20261115/isolate-000552-run-scalars-001.command.txt
    sha256: d7e7b4a074418159498713082e7b30288bc5fd739c9d3e9061f7d53d49b1f615
    role: context
  - path: .temp/gtdb-code006-20261115/isolate-000552-run-scalars-001.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/isolate-000552-run-scalars-001.finished.txt
    sha256: 9284e6005e4b7ba8af64bba8f45ed9cc6c0da5979d80347d795c27b5872d5ca3
    role: context
  - path: .temp/gtdb-code006-20261115/isolate-000552-run-scalars-001.log
    sha256: 437676ec4cfad2741501da7b082ca057a72f5aecc5ad19b696d6d1602006c43f
    role: context
  - path: .temp/gtdb-code006-20261115/isolate-000552-run-scalars-001.log.sha256
    sha256: fc0a35639c2ba3619986af75048a8407bfdbba03a5d478847b2673728ecc2796
    role: context
  - path: .temp/gtdb-code006-20261115/isolate-000552-run-scalars-001.start.txt
    sha256: e5a062c7e6cfb32063b170e3ea1504789faea370064e7dfbbb9d0825b9a8de47
    role: context
  - path: .temp/gtdb-code006-20261115/isolate-000552-run-schema-001.command.txt
    sha256: 70d861b07e9ea39cef609ef7bf25147059d64f247afc5b44e4c1a05606f60907
    role: context
  - path: .temp/gtdb-code006-20261115/isolate-000552-run-schema-001.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/isolate-000552-run-schema-001.finished.txt
    sha256: 0fc07b203b7a1625bf007a81b181778a275c9f042c80f4bfd7c575c89ee53ccb
    role: context
  - path: .temp/gtdb-code006-20261115/isolate-000552-run-schema-001.log
    sha256: 44334e617a3222da5fd512e885d55124a8963f8eccf1f918ef0455bb595b0ee1
    role: context
  - path: .temp/gtdb-code006-20261115/isolate-000552-run-schema-001.log.sha256
    sha256: cd8434bdeca2ab7628658f16394c2dc35b0b8d120aa5c91b88481f519a55f303
    role: context
  - path: .temp/gtdb-code006-20261115/isolate-000552-run-schema-001.start.txt
    sha256: 4f8f2ffbb79cf359b6d1cd70ce210931c3e2f408deb3db3f6acd5e11669891bc
    role: context
  - path: .temp/gtdb-code006-20261115/isolate-000552-run-strict-001.command.txt
    sha256: f8a4f907fe329e3b81b8214c0687d36b361f9a5596975f65cf0d484c1a23b406
    role: context
  - path: .temp/gtdb-code006-20261115/isolate-000552-run-strict-001.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/isolate-000552-run-strict-001.finished.txt
    sha256: 2980c40274e26314a88ffb8a657260aa18a66a6ec3e45088bcbe422b65c5a2a0
    role: context
  - path: .temp/gtdb-code006-20261115/isolate-000552-run-strict-001.log
    sha256: 7624077d415492a240ef8974afbea939d06f8aecd7e18122c5f43368c8377779
    role: context
  - path: .temp/gtdb-code006-20261115/isolate-000552-run-strict-001.log.sha256
    sha256: bb45f14e7b1b6362ed0a90c2e62274b226f4a9abe791a560aff4d6961e994c1f
    role: context
  - path: .temp/gtdb-code006-20261115/isolate-000552-run-strict-001.start.txt
    sha256: cfdd91acfb64d6d8f6a7ae643e9b511cf332e4a385c6eb42feda55c11da5dbec
    role: context
  - path: .temp/gtdb-code006-20261115/isolate-000552-strict-001.tsv
    sha256: b184ed5450b968070bb6c75648407e388f41a1eaf7017890723cf560999fc3f7
    role: context
  - path: .temp/gtdb-code006-20261115/isolate-000552-terms-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/isolate-000552-terms-001/native.log
    sha256: 23acda1c1d3194d12bc947d897d07de83f4a076a9d93c135148885108530e018
    role: context
  - path: .temp/gtdb-code006-20261115/isolate-000552-terms-001/oak.yaml
    sha256: 269dcd5f0527422b7c04d3fee5f80db88350630e1786577d1622cf872ee263bb
    role: context
  - path: .temp/gtdb-code006-20261115/isolate-000552-terms-001/receipt.json
    sha256: adc4b9421575c159f0baca75f644a79ee056936c31fd72020d1053618b062e93
    role: context
  - path: .temp/gtdb-code006-20261115/kg-microbe/data/raw/NCBI2GTDB.tsv.gz
    sha256: 761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd
    role: context
  - path: data/isolates/Pelagerythrobacter_N7_Halophilic_Pyrene_Oxidation_Isolate_Baseline.yaml
    sha256: 829a5326f0770993ee3cb06dbdcc275f489942a84c1206f7bb5adb43468b1896
    role: target
  - path: history/records/Pelagerythrobacter_N7_Halophilic_Pyrene_Oxidation_Isolate_Baseline/2026-11-11T001200Z-antigravity-000552.yaml
    sha256: c3e167d23723e5be8048e12857f85bbdb87eecffc43026bf13b78f76aad7207a
    role: context
  - path: history/records/Pelagerythrobacter_N7_Halophilic_Pyrene_Oxidation_Isolate_Baseline/2026-11-11T080000Z-antigravity-000552-causal-graph.yaml
    sha256: c1e862e52a22ef663c94f23718ec8c5d46b2ce508198e6eb209aa0f1f9cc70bc
    role: context
  - path: history/records/Pelagerythrobacter_N7_Halophilic_Pyrene_Oxidation_Isolate_Baseline/2026-11-15T055434Z-codex-ee7eb1.yaml
    sha256: 031b5023559f76eadd8ec080111afb66aeca7341c0305a0b9942619d91dbf8ef
    role: context
  - path: references_cache/PMID_42666409.txt
    sha256: 3442799f20b033c3a010c14a4f32c4be15485fb0a501aed059921a5006cbe698
    role: context
  - path: reports/causal_graph_review/decisions/20261110-stage2-seven-records-batch147.yaml
    sha256: 732db4d507546996774aca3835d77c4a2b7feba7c2690522700488e2b8c4fe19
    role: context
  - path: reviews/structured/20261111T121000Z-c15s4-record-deep-audit/review.md
    sha256: b50530c53d3bfede09c3d7943df0e25972de80edd92701ffab41cdf4c3635af3
    role: context
  - path: reviews/structured/20261111T121000Z-c15s4-record-deep-audit/review.yaml
    sha256: d6273b3c8723adc01ea4d71bc589e99bb8952da3cbd9067c6a0680979a4e7c71
    role: context
  - path: scripts/adhoc/apply_code006_isolate_genus_20261115.py
    sha256: 9e97d6abaed2c7a06b811e2abb0792b47585f91799e70da2e089ae913048b13b
    role: context
  - path: scripts/adhoc/build_code006_isolate_assessment_20261115.py
    sha256: 8acffe20189b31ec89aa3b8aaa914140af4422cf047bf8ea919dbbc1bcb58d6f
    role: context
  - path: scripts/adhoc/check_code006_isolate_genus_20261115.sh
    sha256: b7c103b7e36f3d8664703abf1298189e8533f1d5c358baab206687a00fd1da79
    role: context
  - path: scripts/adhoc/check_code006_local_terms_20261115.py
    sha256: 64ab1b9313e98e9db507bee3033b618e43cf60708e4d54dd9ffbb0c8e8fcfc75
    role: context
  - path: scripts/adhoc/recompute_code006_isolate_genus_20261115.py
    sha256: 8962b9ca7067bc142b301cb346e22c4ac8c71a14e7afd371ea653eee79d57137
    role: context
  - path: scripts/adhoc/stage_code006_isolate_genus_20261115.py
    sha256: 15574e36f3b0bd6f2c6b6b6293fb856ab863d7ef3297b7f649e62d1166b9a5e0
    role: context
  - path: scripts/gtdb_ground.py
    sha256: 0fc1ba926a56e5be85cdf064db0cf56452aeeee93f15b0ced98e8f11b5296175
    role: context
  - path: src/communitymech/curate/curation_event.py
    sha256: 58ebdb58ac39d7a319156ec735db9ef2e9afb4c7350613039ad9dc49d65a5afc
    role: context
  - path: src/communitymech/schema/communitymech.yaml
    sha256: c6f6e4a5cf42e450cf55d8fcb12817591c736198e24bcd217142b4f86712b4c3
    role: context
  - path: src/communitymech/schema/history.yaml
    sha256: b01b06f1b9a37db205c26c31ec0fd910690848507c7e1bfb73b424ac0829c52d
    role: context
  - path: src/communitymech/schema/mech_shared.yaml
    sha256: cf32864df1626201128e9311054b075bfc4ad3d8345491ac144122a5d5e67d11
    role: context
  - path: src/communitymech/validation/write_validated.py
    sha256: d19dd3b1e46856b4de67ecc17fc856aaa1034a9a97259cab3bbd54c3891fb019
    role: context
  - path: tests/batch147_genus_successor.py
    sha256: e1b6efa17958c0dc9ff7cde28cfb95af905e5d0d158b5553a758d5ed3b3d034c
    role: context
  - path: uv.lock
    sha256: 712838f8fa3d68fbd818ac8162f3f1e2f2637db1da1a8ebfaba0ef759690f3b4
    role: context
targets:
- target_id: CommunityMech:000552
  path: data/isolates/Pelagerythrobacter_N7_Halophilic_Pyrene_Oxidation_Isolate_Baseline.yaml
  label: Pelagerythrobacter study-stock genus correspondence
  selector: taxonomy[0].taxon_term
  kind: maintained
  ownership_note: CommunityMech owns this canonical isolate and its native source-grounding/history
    tooling.
scope:
  description: Only the database correspondence, guarded application/history chain
    and technical checks were assessed.
  selection: First independently accepted pure same-name higher-rank isolate candidate;
    original basename and source identity retained.
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000552
  coverage: partial
  exclusions:
  - target: Other assigned records and unchanged biological claims
    reason: No wider or full scientific assessment was performed.
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  summary: Actual scoped native gate passed with a nonempty hash-verified log.
  target_ids:
  - CommunityMech:000552
  command: just --verbose --no-dotenv --color never validate data/isolates/Pelagerythrobacter_N7_Halophilic_Pyrene_Oxidation_Isolate_Baseline.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - schema
- check_id: strict
  name: strict
  status: passed
  required: true
  summary: Actual scoped native gate passed with a nonempty hash-verified log.
  target_ids:
  - CommunityMech:000552
  command: just --verbose --no-dotenv --color never validate-strict data/isolates/Pelagerythrobacter_N7_Halophilic_Pyrene_Oxidation_Isolate_Baseline.yaml
    --out .temp/gtdb-code006-20261115/isolate-000552-strict-001.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - strict
- check_id: gtdb
  name: gtdb
  status: passed
  required: true
  summary: Actual scoped native gate passed with a nonempty hash-verified log.
  target_ids:
  - CommunityMech:000552
  command: just --verbose --no-dotenv --color never validate-gtdb data/isolates/Pelagerythrobacter_N7_Halophilic_Pyrene_Oxidation_Isolate_Baseline.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - gtdb
- check_id: domain
  name: domain
  status: passed
  required: true
  summary: Actual scoped native gate passed with a nonempty hash-verified log.
  target_ids:
  - CommunityMech:000552
  command: just --verbose --no-dotenv --color never validate-gtdb-domain data/isolates/Pelagerythrobacter_N7_Halophilic_Pyrene_Oxidation_Isolate_Baseline.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - domain
- check_id: scalars
  name: scalars
  status: passed
  required: true
  summary: Actual scoped native gate passed with a nonempty hash-verified log.
  target_ids:
  - CommunityMech:000552
  command: just --verbose --no-dotenv --color never validate-scalars data/isolates/Pelagerythrobacter_N7_Halophilic_Pyrene_Oxidation_Isolate_Baseline.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - scalars
- check_id: history
  name: history
  status: passed
  required: true
  summary: Actual scoped native gate passed with a nonempty hash-verified log.
  target_ids:
  - CommunityMech:000552
  command: just --verbose --no-dotenv --color never validate-history history/records/Pelagerythrobacter_N7_Halophilic_Pyrene_Oxidation_Isolate_Baseline
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - history
- check_id: completion
  name: completion
  status: passed
  required: true
  summary: Both unchanged native outstanding-grounding tests passed; not full QC.
  target_ids:
  - CommunityMech:000552
  command: uv run pytest tests/test_gtdb_coherence_validator.py::test_the_status_distribution_is_what_was_measured
    tests/test_gtdb_not_attempted.py::test_no_taxon_is_silently_outstanding -q
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - completion
- check_id: terms
  name: Native LTV with explicit local adapters
  status: passed
  required: true
  summary: Native LTV binding/label check used explicit existing SQLite adapters and
    blocked network; database stat identities stayed unchanged, byte hashes were not
    measured.
  target_ids:
  - CommunityMech:000552
  command: linkml-term-validator validate-data data/isolates/Pelagerythrobacter_N7_Halophilic_Pyrene_Oxidation_Isolate_Baseline.yaml
    -s src/communitymech/schema/communitymech.yaml --labels --config .temp/gtdb-code006-20261115/isolate-000552-terms-001/oak.yaml
    --cache-dir .temp/gtdb-code006-20261115/isolate-000552-terms-001/labels
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - terms
evidence:
- evidence_id: schema
  kind: validation
  reference: .temp/gtdb-code006-20261115/isolate-000552-run-schema-001.log
  accessed_at: '2026-11-15T06:05:38.894873Z'
  support: supports
  summary: Actual scoped native gate passed with a nonempty hash-verified log.
- evidence_id: strict
  kind: validation
  reference: .temp/gtdb-code006-20261115/isolate-000552-run-strict-001.log
  accessed_at: '2026-11-15T06:05:38.894873Z'
  support: supports
  summary: Actual scoped native gate passed with a nonempty hash-verified log.
- evidence_id: gtdb
  kind: validation
  reference: .temp/gtdb-code006-20261115/isolate-000552-run-gtdb-001.log
  accessed_at: '2026-11-15T06:05:38.894873Z'
  support: supports
  summary: Actual scoped native gate passed with a nonempty hash-verified log.
- evidence_id: domain
  kind: validation
  reference: .temp/gtdb-code006-20261115/isolate-000552-run-domain-001.log
  accessed_at: '2026-11-15T06:05:38.894873Z'
  support: supports
  summary: Actual scoped native gate passed with a nonempty hash-verified log.
- evidence_id: scalars
  kind: validation
  reference: .temp/gtdb-code006-20261115/isolate-000552-run-scalars-001.log
  accessed_at: '2026-11-15T06:05:38.894873Z'
  support: supports
  summary: Actual scoped native gate passed with a nonempty hash-verified log.
- evidence_id: history
  kind: validation
  reference: .temp/gtdb-code006-20261115/isolate-000552-run-history-001.log
  accessed_at: '2026-11-15T06:05:38.894873Z'
  support: supports
  summary: Actual scoped native gate passed with a nonempty hash-verified log.
- evidence_id: completion
  kind: validation
  reference: .temp/gtdb-code006-20261115/isolate-000552-run-completion-001.log
  accessed_at: '2026-11-15T06:05:38.894873Z'
  support: supports
  summary: Both unchanged native outstanding-grounding tests passed; not full QC.
- evidence_id: terms
  kind: validation
  reference: .temp/gtdb-code006-20261115/isolate-000552-terms-001/native.log
  accessed_at: '2026-11-15T06:05:38.894873Z'
  support: supports
  summary: Native LTV binding/label check used explicit existing SQLite adapters and
    blocked network; database stat identities stayed unchanged, byte hashes were not
    measured.
- evidence_id: application
  kind: record_content
  reference: .temp/gtdb-code006-20261115/isolate-000552-applied-001/receipt.json
  accessed_at: '2026-11-15T06:05:38.894873Z'
  support: supports
  summary: Exact actual guarded application, retained original bytes and append-only
    history; biology outside the mapping/status is unchanged.
- evidence_id: mapping
  kind: database
  reference: .temp/gtdb-code006-20261115/isolate-000552-native-recomputation-001.json
  accessed_at: '2026-11-15T06:05:38.894873Z'
  support: supports
  summary: 'Native same-genus NCBITaxon:2800685 correspondence to GTDB:g__Pelagerythrobacter:
    16/16 named reference genomes. This does not identify the study stock species
    or genome.'
- evidence_id: primary
  kind: primary_source
  reference: references_cache/PMID_42666409.txt
  accessed_at: '2026-11-15T06:05:38.894873Z'
  support: supports
  summary: Existing primary Section3.1 supports the named genus of this study stock.
    This bounded check preserves all other source and biological assertions.
- evidence_id: previous
  kind: prior_review
  reference: reviews/structured/20261111T121000Z-c15s4-record-deep-audit/review.yaml
  accessed_at: '2026-11-15T06:05:38.894873Z'
  support: context_only
  summary: Immutable earlier full scientific review and all unresolved findings retained;
    this is not its replacement.
assessments:
- assessment_id: genus-correspondence
  area: grounding
  topic: Same-genus database correspondence
  outcome: supported
  target_ids:
  - CommunityMech:000552
  evidence_ids:
  - mapping
  - primary
  - application
  - gtdb
  - terms
  summary: The existing declared Pelagerythrobacter genus maps to GTDB:g__Pelagerythrobacter
    at 16/16 named-binomial reference genomes, not reclassified. This database correspondence
    does not establish the exact study-stock species, genome or mechanisms.
- assessment_id: historical-boundary
  area: provenance
  topic: Preserved biological bytes and earlier assessment
  outcome: supported
  target_ids:
  - CommunityMech:000552
  evidence_ids:
  - previous
  - application
  - history
  - completion
  summary: The exact old full record remains retained; only the genus block, GROUNDED
    status and two native inline events changed. Native sidecar and actual application
    evidence are bound. Earlier UNRESOLVED reflects the prior database result and
    is not overwritten in its immutable review. Historical scientific needs-curation
    findings remain open.
findings: []
actions: []
limitations:
- 'Partial technical assessment only: no new full-paper/supplement review, reference
  sweep, stock genome/species inference, mechanism approval or scientific status promotion.'
- The term check is the installed native CLI with explicit local NCBI/ENVO/CHEBI adapters,
  not literally the just validate-terms recipe. Adapter stat identities were checked;
  database byte hashes were not measured.
- Seven scoped gates and two outstanding-grounding tests passed; full corpus status
  reproducibility, historical successor acceptance and full QC are separate gates.
- Exact M5 native execution revision is recorded, with additional hashed orchestration
  helpers. No record or issue outside this target is declared completed.
related_reviews:
- repository: CultureBotAI/CommunityMech
  review_id: 20261111T121000Z-c15s4-record-deep-audit
  relationship: Additive technical correspondence preserves all original scientific
    findings and source/stock limitations; does not supersede the multi-record scientific
    assessment.
```
