# Sulfobacillus reference mapping: one-record M5 diagnostic canary

- Review: 20261115T050549Z-sulfobacillus-gtdb-diagnostic
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-11-15T05:05:48.861238Z
- Finished UTC: 2026-11-15T05:05:49.402216Z
- Reviewer: codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: false

## Summary

Only the reference-taxon GTDB correspondence and its actual M5 application/provenance are assessed. The corrected block reproduces native computation on exact761 crosswalk bytes, with six passing native gates and one native sidecar. No whole-record scientific approval, exact strain identity or issue1509 resolution is claimed.

## Scope And Provenance

One taxonomy mapping, before/after scope, database evidence and deterministic gate/provenance chain only.

Selection: First of the three stored-block discrepancies in2849, chosen as the required single end-to-end canary before further record changes.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base cb642708f04b12d3a30ecdb662854dd26816014c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000035 | kb/communities/Industrial_Bioreactor_Consortium.yaml # taxonomy[6].taxon_term.gtdb_classification | maintained | Sulfobacillus acidophilus reference-taxon GTDB correspondence |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000035 | Actual native M5 command completed with exit0, exact corrected-record input and retained nonempty hash-bound log. |
| validate-strict | passed | True | CommunityMech:000035 | Actual native M5 command completed with exit0, exact corrected-record input and retained nonempty hash-bound log. |
| validate-gtdb | passed | True | CommunityMech:000035 | Actual native M5 command completed with exit0, exact corrected-record input and retained nonempty hash-bound log. |
| validate-gtdb-domain | passed | True | CommunityMech:000035 | Actual native M5 command completed with exit0, exact corrected-record input and retained nonempty hash-bound log. |
| validate-scalars | passed | True | CommunityMech:000035 | Actual native M5 command completed with exit0, exact corrected-record input and retained nonempty hash-bound log. |
| validate-history | passed | True | CommunityMech:000035 | Actual native M5 command completed with exit0, exact corrected-record input and retained nonempty hash-bound log. |
| new-history | passed | True | CommunityMech:000035 | Actual native M5 command completed with exit0, exact corrected-record input and retained nonempty hash-bound log. |

## Scientific And Domain Assessments

### Exact retained crosswalk route and denominator

grounding: supported. Targets: CommunityMech:000035.

Exact species-name rows679936/1051632 agree on Sulfobacillus_A acidophilus; native computation gives total4/fraction1.0/name difference true. Preserve NCBITaxon53633 and source species name, remove unsupported latest/build wording, add no curated exemption.

### One actual M5 guarded write and append-only history

provenance: supported. Targets: CommunityMech:000035.

Native validated writer persisted the exact reviewed candidate; every field outside the one GTDB block and appended inline event remains semantically unchanged. The external sidecar records actual application and limitations; old history and batch53 review remain immutable.

### Reference species versus study strain and composite community

scope: supported. Targets: CommunityMech:000035.

The source abstract's species name is retained. A database name correspondence does not identify the paper's exact strain, resolve the composite roster or establish biological mechanism. The record remains subject to1509; the existing nine nodes/zero arrows are preserved rather than newly certified.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| schema | .temp/gtdb-source-routes-2849-20261115/canary-run-schema-001/native.log | supports | Actual native M5 command completed with exit0, exact corrected-record input and retained nonempty hash-bound log. |
| strict | .temp/gtdb-source-routes-2849-20261115/canary-run-strict-001/native.log | supports | Actual native M5 command completed with exit0, exact corrected-record input and retained nonempty hash-bound log. |
| gtdb | .temp/gtdb-source-routes-2849-20261115/canary-run-gtdb-001/native.log | supports | Actual native M5 command completed with exit0, exact corrected-record input and retained nonempty hash-bound log. |
| domain | .temp/gtdb-source-routes-2849-20261115/canary-run-domain-001/native.log | supports | Actual native M5 command completed with exit0, exact corrected-record input and retained nonempty hash-bound log. |
| scalars | .temp/gtdb-source-routes-2849-20261115/canary-run-scalars-001/native.log | supports | Actual native M5 command completed with exit0, exact corrected-record input and retained nonempty hash-bound log. |
| history | .temp/gtdb-source-routes-2849-20261115/canary-run-history-001/native.log | supports | Actual native M5 command completed with exit0, exact corrected-record input and retained nonempty hash-bound log. |
| new-history | .temp/gtdb-source-routes-2849-20261115/canary-run-new-history-001/native.log | supports | Actual native M5 command completed with exit0, exact corrected-record input and retained nonempty hash-bound log. |
| mapping | .temp/gtdb-source-routes-2849-20261115/sulfobacillus-route-001.json; native_lookup.exact_species_name_rows.sulfobacillus acidophilus; taxonID NCBI679936/1051632; total genomes/majority fraction/species(GTDB) | supports | Two exact-name rows each report2 genomes and fraction1.0 for Sulfobacillus_A acidophilus; no53633 row exists in this exact table. The native name route produces total4, fraction1.0, and GTDB suffix_A, independently recomputed after M5 apply. |
| recomputed | .temp/gtdb-source-routes-2849-20261115/diagnostic-001/native-route.json; result | supports | Actual unchanged native classifier and exact761 table reproduce every stored numerical/classification field after application; mapping_source explicitly records the route and its study-strain limit. |
| application | .temp/gtdb-source-routes-2849-20261115/sulfobacillus-applied-m5-001/receipt.json; applied/before_sha256/after_sha256/inputs | supports | Actual M5 guarded apply changed only the reviewed GTDB block and appended native inline history; exact reviewed staging receipt and all source hashes were rechecked before replacement. |
| prior | reports/causal_graph_review/adversarial-review-20261006-batch53.yaml; findings.issue1509; adversarial_checks; limitations | context_only | The preserved batch53 review explicitly left canonical roster and non-graph claims uncertified, with composite community identity unresolved under1509. Its nine current nodes and zero arrows are unchanged by this mapping correction. |
| abstract | https://pubmed.ncbi.nlm.nih.gov/24242252/; Abstract; committed PMID_24242252.md content | context_only | The inspected primary abstract names Sulfobacillus acidophilus in the mixed culture. It supplies no study-strain genome identity or GTDB mapping. This assessment read the abstract, not the inaccessible main paper or supplements. |

## Limits And Additional Notes

- Diagnostic-only partial assessment; no full scientific review, new primary full-text/supplement acquisition, exact study-strain genome grounding or issue closure.
- The mapping is bound to SHA761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd. File modification time does not establish a GTDB release/build; no such release assertion is made.
- Full-record native completeness/quality metrics were not recomputed because this assessment covers only one database mapping; passing deterministic gates do not supply scientific approval.
- Six native scoped gates plus new-history ran on M5 Python3.13.2 atcb642708 with explicitly hashed additive check/builder source. References, term labels, corpus QC and generated docs are not claimed passed by this diagnostic; no source quotation or NCBITaxon label changed.
- Existing source/roster/functional concerns under1509 and other2849 records remain unresolved. An empty finding list is only the result for this corrected mapping scope.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261115T050549Z-sulfobacillus-gtdb-diagnostic
kind: record
repository: CultureBotAI/CommunityMech
title: 'Sulfobacillus reference mapping: one-record M5 diagnostic canary'
started_at: '2026-11-15T05:05:48.861238Z'
finished_at: '2026-11-15T05:05:49.402216Z'
reviewer:
  identity: codex
  kind: agent
  independence: self_review
  independence_basis: Authored the source diagnosis and correction; root independently
    accepted source rows, guarded helper, local candidate and timestamp-only M5 candidate
    before the one actual M5 apply.
skill: review-yaml-record
completion: completed
verdict: pass_with_limitations
scientific_review: false
summary: Only the reference-taxon GTDB correspondence and its actual M5 application/provenance
  are assessed. The corrected block reproduces native computation on exact761 crosswalk
  bytes, with six passing native gates and one native sidecar. No whole-record scientific
  approval, exact strain identity or issue1509 resolution is claimed.
source:
  git_revision: cb642708f04b12d3a30ecdb662854dd26816014c
  state: working_tree
  inputs:
  - path: .temp/gtdb-source-routes-2849-20261115/canary-run-domain-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-source-routes-2849-20261115/canary-run-domain-001/native.log
    sha256: 1884d30068e44c3368e1d2b508ea968d79c03d6496dfdf969890e68802b27660
    role: context
  - path: .temp/gtdb-source-routes-2849-20261115/canary-run-domain-001/receipt.json
    sha256: c55b9818fc0ac52046b909cda52c32f1abc75da0e05c62eb146fad6b77283b66
    role: context
  - path: .temp/gtdb-source-routes-2849-20261115/canary-run-domain-001/start.json
    sha256: d4b27dba0e334282df14c38b80f5230439541ef925640a0a8dd9a968aea19a54
    role: context
  - path: .temp/gtdb-source-routes-2849-20261115/canary-run-gtdb-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-source-routes-2849-20261115/canary-run-gtdb-001/native.log
    sha256: 44c672c90bbbe51e6f4acece67398b0db7367d20a2d178990ec8c915e4f79280
    role: context
  - path: .temp/gtdb-source-routes-2849-20261115/canary-run-gtdb-001/receipt.json
    sha256: fa7a1c30e168dbe0e9847737ff5cafb0ca53cc47af889c0c6be3bae291dd8aaf
    role: context
  - path: .temp/gtdb-source-routes-2849-20261115/canary-run-gtdb-001/start.json
    sha256: daf82468fe5f7247827c0806a6986c1d7eae73fe58fe38505f9c50499c15cbe5
    role: context
  - path: .temp/gtdb-source-routes-2849-20261115/canary-run-history-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-source-routes-2849-20261115/canary-run-history-001/native.log
    sha256: 700b44227c4cf01270ac26f16b308622de0b26f48d71aec49cdfaaab87620f0a
    role: context
  - path: .temp/gtdb-source-routes-2849-20261115/canary-run-history-001/receipt.json
    sha256: 1c4dc0c28039dc3f3d2ce09956947a6f9dc9f06bcbc367020d1fd4d322cec187
    role: context
  - path: .temp/gtdb-source-routes-2849-20261115/canary-run-history-001/start.json
    sha256: 2e51ea66ca4e8d31741b8a2540ae21fdd17340193b1744d24a6d81dcc9ad7718
    role: context
  - path: .temp/gtdb-source-routes-2849-20261115/canary-run-new-history-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-source-routes-2849-20261115/canary-run-new-history-001/native.log
    sha256: 0413ed662172dee45c95271292d15bdda36fd7a3893bded47abff4dc8e915742
    role: context
  - path: .temp/gtdb-source-routes-2849-20261115/canary-run-new-history-001/receipt.json
    sha256: 0fcc986db83b5b7c12cc896e72e1505e903b38671f83089b4981f4ea7cf81de3
    role: context
  - path: .temp/gtdb-source-routes-2849-20261115/canary-run-new-history-001/start.json
    sha256: e3271435578a47b0592308dd86bc43e76a5f2810c130bb907b149d2d7d4f09cf
    role: context
  - path: .temp/gtdb-source-routes-2849-20261115/canary-run-scalars-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-source-routes-2849-20261115/canary-run-scalars-001/native.log
    sha256: c18ee245cd6df055695729b79dda6e7c07a0c6606dca0f4c317fa598091517b0
    role: context
  - path: .temp/gtdb-source-routes-2849-20261115/canary-run-scalars-001/receipt.json
    sha256: e773290953047213650e2a8ac4d59294928b9bc022b422f6e93014a8689aeae9
    role: context
  - path: .temp/gtdb-source-routes-2849-20261115/canary-run-scalars-001/start.json
    sha256: b16e3b7ffd6bab9fb5f986cc5dc015266146d46b4040f9d7c501cd560859f8b3
    role: context
  - path: .temp/gtdb-source-routes-2849-20261115/canary-run-schema-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-source-routes-2849-20261115/canary-run-schema-001/native.log
    sha256: afad2f648cd8b79e50a779a2e26834e849a20f84f0ce0c4807cbdf64f1bfa2d9
    role: context
  - path: .temp/gtdb-source-routes-2849-20261115/canary-run-schema-001/receipt.json
    sha256: acc365844961d03e0bbd142f7201df3454e2be60b1a5316e4a9e3f50740d7904
    role: context
  - path: .temp/gtdb-source-routes-2849-20261115/canary-run-schema-001/start.json
    sha256: 4ed502f71895a9f487ac345d46d09872585ebb6a019b1a0f539cb93b12d9d586
    role: context
  - path: .temp/gtdb-source-routes-2849-20261115/canary-run-strict-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-source-routes-2849-20261115/canary-run-strict-001/native.log
    sha256: f54177a7fdd6e634e165099bab00e4026368fd694356d3fd726256e607c12d76
    role: context
  - path: .temp/gtdb-source-routes-2849-20261115/canary-run-strict-001/receipt.json
    sha256: 127d2d7f09d96a2d5f2292984090fcc0c5689180ae4f82343b683d61c1357c47
    role: context
  - path: .temp/gtdb-source-routes-2849-20261115/canary-run-strict-001/start.json
    sha256: fd8205fdbfa6a161b2aac734c21e1037bd3c653221cded6aa45aafce351509b9
    role: context
  - path: .temp/gtdb-source-routes-2849-20261115/canary-run-strict-001/strict.tsv
    sha256: b184ed5450b968070bb6c75648407e388f41a1eaf7017890723cf560999fc3f7
    role: context
  - path: .temp/gtdb-source-routes-2849-20261115/diagnostic-001/native-route.json
    sha256: 7d4df488bd3badfd2c3a847e3abc0ae9ab4639881e061c78b408e829992e9f93
    role: context
  - path: .temp/gtdb-source-routes-2849-20261115/kg-microbe/data/raw/NCBI2GTDB.tsv.gz
    sha256: 761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd
    role: context
  - path: .temp/gtdb-source-routes-2849-20261115/sulfobacillus-applied-m5-001/before.yaml
    sha256: 71160959bae2c8e3f0caf63d57452a597e29967f70faea6bec59016752b9aad4
    role: context
  - path: .temp/gtdb-source-routes-2849-20261115/sulfobacillus-applied-m5-001/receipt.json
    sha256: ee8f6aec6f076b02c80539d3d47fc1a694274d6de97ca68145131910add33066
    role: context
  - path: .temp/gtdb-source-routes-2849-20261115/sulfobacillus-candidate-m5-001/candidate.yaml
    sha256: 24c55ff3c29b21fa5988c4859fdcccfacc52caf62a1902cb28887b68780f551e
    role: context
  - path: .temp/gtdb-source-routes-2849-20261115/sulfobacillus-candidate-m5-001/receipt.json
    sha256: be1fe01fca924dede859eeb8dcf1ddf562704c6f1e7558f17875b4f6c0fd0469
    role: context
  - path: .temp/gtdb-source-routes-2849-20261115/sulfobacillus-route-001.json
    sha256: f7d0c499fb05197fe39a795f5a9c1e0fc3b5b6eee891181a1b0baabd3bfeb660
    role: context
  - path: history/records/Industrial_Bioreactor_Consortium/2026-10-06T162402Z-codex-b1f92a.yaml
    sha256: 20edb891cb2b777d61f8a7da91ef59db008a8f3dfb3715a34e2b993930c08043
    role: context
  - path: history/records/Industrial_Bioreactor_Consortium/2026-11-15T050250Z-codex-3f8936.yaml
    sha256: 2e50ea4c26f5f9286b35577eaeecb1a3a8c0f08c8685453901619747ed1016e1
    role: context
  - path: justfile
    sha256: 40369611ad4531582e420df0e9ff22109e4b18adf03b34d86b54200b280f2d0f
    role: context
  - path: kb/communities/Industrial_Bioreactor_Consortium.yaml
    sha256: 24c55ff3c29b21fa5988c4859fdcccfacc52caf62a1902cb28887b68780f551e
    role: target
  - path: references_cache/PMID_24242252.md
    sha256: fdc55bb31062bcb2268c565eca1323057f66a86093f2acb2ae6df3c82cdd6841
    role: context
  - path: reports/causal_graph_review/adversarial-review-20261006-batch53.yaml
    sha256: 23593beae08648518bac7cd7ab8b1542404ec50bc0d2f252d8e21dc2d379dbc6
    role: context
  - path: reports/causal_graph_review/decisions/20261006-pitlakes-bioleach-biofilm-batch53.yaml
    sha256: 41b8d4e6971264d0890389465ca6c7c5f288097c011e3da00861fb09f49a8261
    role: context
  - path: scripts/adhoc/build_sulfobacillus_diagnostic_20261115.py
    sha256: a64b13d63b245ce2003e28bcc83619ee3f2ae1804228c50ab3bcea3a7fb9610d
    role: context
  - path: scripts/adhoc/check_sulfobacillus_canary_20261115.py
    sha256: 9a939bd9375450eae56ccc9360b9e8dbed9d421842b137487ea56d3f547e8cab
    role: context
  - path: scripts/adhoc/curate_sulfobacillus_mapping_20261115.py
    sha256: ed6caa4f0ee7d28a115b8e7e544204251050943a558eb953eb0575df102b1054
    role: context
  - path: scripts/adhoc/inspect_gtdb_source_routes_20261115.py
    sha256: d84a7ce222d78a34a43971ee0974563edc4bb46e120d101731cd0b807478e472
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
  - path: src/communitymech/validation/write_validated.py
    sha256: d19dd3b1e46856b4de67ecc17fc856aaa1034a9a97259cab3bbd54c3891fb019
    role: context
  - path: uv.lock
    sha256: 712838f8fa3d68fbd818ac8162f3f1e2f2637db1da1a8ebfaba0ef759690f3b4
    role: context
targets:
- target_id: CommunityMech:000035
  path: kb/communities/Industrial_Bioreactor_Consortium.yaml
  selector: taxonomy[6].taxon_term.gtdb_classification
  label: Sulfobacillus acidophilus reference-taxon GTDB correspondence
  kind: maintained
  ownership_note: CommunityMech owns the canonical mapping; native gtdb_ground.py
    computes the database correspondence from the retained kg-microbe table. Broader
    composite-community scope remains issue1509.
scope:
  description: One taxonomy mapping, before/after scope, database evidence and deterministic
    gate/provenance chain only.
  selection: First of the three stored-block discrepancies in2849, chosen as the required
    single end-to-end canary before further record changes.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000035
  exclusions:
  - target: All other taxonomy mappings and all ecological/cultivation/community claims
      of000035
    reason: Existing biological content preserved; source support and composite community
      identity were not reassessed.
  - target: Other two issue2849 records and remaining corpus
    reason: No batch application or scientific review is represented by this one-record
      canary.
checks:
- check_id: schema
  name: validate
  status: passed
  required: true
  summary: Actual native M5 command completed with exit0, exact corrected-record input
    and retained nonempty hash-bound log.
  target_ids:
  - CommunityMech:000035
  command: just --verbose --no-dotenv --color never validate kb/communities/Industrial_Bioreactor_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - schema
  scope_note: One corrected record; new-history creates its sidecar and history validates
    its complete history directory. This is not corpus QC or literature validation.
- check_id: strict
  name: validate-strict
  status: passed
  required: true
  summary: Actual native M5 command completed with exit0, exact corrected-record input
    and retained nonempty hash-bound log.
  target_ids:
  - CommunityMech:000035
  command: just --verbose --no-dotenv --color never validate-strict kb/communities/Industrial_Bioreactor_Consortium.yaml
    --out .temp/gtdb-source-routes-2849-20261115/canary-run-strict-001/strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - strict
  scope_note: One corrected record; new-history creates its sidecar and history validates
    its complete history directory. This is not corpus QC or literature validation.
- check_id: gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: Actual native M5 command completed with exit0, exact corrected-record input
    and retained nonempty hash-bound log.
  target_ids:
  - CommunityMech:000035
  command: just --verbose --no-dotenv --color never validate-gtdb kb/communities/Industrial_Bioreactor_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - gtdb
  scope_note: One corrected record; new-history creates its sidecar and history validates
    its complete history directory. This is not corpus QC or literature validation.
- check_id: domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: Actual native M5 command completed with exit0, exact corrected-record input
    and retained nonempty hash-bound log.
  target_ids:
  - CommunityMech:000035
  command: just --verbose --no-dotenv --color never validate-gtdb-domain kb/communities/Industrial_Bioreactor_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - domain
  scope_note: One corrected record; new-history creates its sidecar and history validates
    its complete history directory. This is not corpus QC or literature validation.
- check_id: scalars
  name: validate-scalars
  status: passed
  required: true
  summary: Actual native M5 command completed with exit0, exact corrected-record input
    and retained nonempty hash-bound log.
  target_ids:
  - CommunityMech:000035
  command: just --verbose --no-dotenv --color never validate-scalars kb/communities/Industrial_Bioreactor_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - scalars
  scope_note: One corrected record; new-history creates its sidecar and history validates
    its complete history directory. This is not corpus QC or literature validation.
- check_id: history
  name: validate-history
  status: passed
  required: true
  summary: Actual native M5 command completed with exit0, exact corrected-record input
    and retained nonempty hash-bound log.
  target_ids:
  - CommunityMech:000035
  command: just --verbose --no-dotenv --color never validate-history history/records/Industrial_Bioreactor_Consortium
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - history
  scope_note: One corrected record; new-history creates its sidecar and history validates
    its complete history directory. This is not corpus QC or literature validation.
- check_id: new-history
  name: new-history
  status: passed
  required: true
  summary: Actual native M5 command completed with exit0, exact corrected-record input
    and retained nonempty hash-bound log.
  target_ids:
  - CommunityMech:000035
  command: just --verbose --no-dotenv --color never new-history --kind record --slug
    Industrial_Bioreactor_Consortium --target-root kb/communities --event EDIT --outcome
    changed --sections taxonomy,curation_history --actor-name codex --model gpt-6
    --agent-tool codex --issue https://github.com/CultureBotAI/CommunityMech/issues/2849
    --pr https://github.com/CultureBotAI/CommunityMech/pull/2804 --summary 'Reconcile
    the Sulfobacillus reference-taxon GTDB mapping' --details 'Applied the independently
    reviewed one-block M5 candidate24c55ff3. Retained NCBI2GTDB snapshot SHA256761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd
    has no53633 row; exact species-name rows679936 and1051632 each report2 genomes,
    fraction1.0, and Sulfobacillus_A acidophilus. Native name mapping yields4 genomes
    and changed GTDB name. Preserve NCBITaxon53633, all biological claims, graphs,
    source quotations and historical batch53 review. This is reference-taxon correspondence,
    not exact study-strain identification or full scientific approval; composite-community
    issue1509 remains unresolved. Actual raw application receipt .temp/gtdb-source-routes-2849-20261115/sulfobacillus-applied-m5-001/receipt.json
    SHA256ee8f6aec6f076b02c80539d3d47fc1a694274d6de97ca68145131910add33066. A scoped
    diagnostic assessment and actual native focused gates follow.'
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - new-history
  scope_note: One corrected record; new-history creates its sidecar and history validates
    its complete history directory. This is not corpus QC or literature validation.
evidence:
- evidence_id: schema
  kind: validation
  reference: .temp/gtdb-source-routes-2849-20261115/canary-run-schema-001/native.log
  accessed_at: '2026-11-15T05:05:48.861238Z'
  support: supports
  summary: Actual native M5 command completed with exit0, exact corrected-record input
    and retained nonempty hash-bound log.
- evidence_id: strict
  kind: validation
  reference: .temp/gtdb-source-routes-2849-20261115/canary-run-strict-001/native.log
  accessed_at: '2026-11-15T05:05:48.861238Z'
  support: supports
  summary: Actual native M5 command completed with exit0, exact corrected-record input
    and retained nonempty hash-bound log.
- evidence_id: gtdb
  kind: validation
  reference: .temp/gtdb-source-routes-2849-20261115/canary-run-gtdb-001/native.log
  accessed_at: '2026-11-15T05:05:48.861238Z'
  support: supports
  summary: Actual native M5 command completed with exit0, exact corrected-record input
    and retained nonempty hash-bound log.
- evidence_id: domain
  kind: validation
  reference: .temp/gtdb-source-routes-2849-20261115/canary-run-domain-001/native.log
  accessed_at: '2026-11-15T05:05:48.861238Z'
  support: supports
  summary: Actual native M5 command completed with exit0, exact corrected-record input
    and retained nonempty hash-bound log.
- evidence_id: scalars
  kind: validation
  reference: .temp/gtdb-source-routes-2849-20261115/canary-run-scalars-001/native.log
  accessed_at: '2026-11-15T05:05:48.861238Z'
  support: supports
  summary: Actual native M5 command completed with exit0, exact corrected-record input
    and retained nonempty hash-bound log.
- evidence_id: history
  kind: validation
  reference: .temp/gtdb-source-routes-2849-20261115/canary-run-history-001/native.log
  accessed_at: '2026-11-15T05:05:48.861238Z'
  support: supports
  summary: Actual native M5 command completed with exit0, exact corrected-record input
    and retained nonempty hash-bound log.
- evidence_id: new-history
  kind: validation
  reference: .temp/gtdb-source-routes-2849-20261115/canary-run-new-history-001/native.log
  accessed_at: '2026-11-15T05:05:48.861238Z'
  support: supports
  summary: Actual native M5 command completed with exit0, exact corrected-record input
    and retained nonempty hash-bound log.
- evidence_id: mapping
  kind: database
  reference: .temp/gtdb-source-routes-2849-20261115/sulfobacillus-route-001.json
  locator: native_lookup.exact_species_name_rows.sulfobacillus acidophilus; taxonID
    NCBI679936/1051632; total genomes/majority fraction/species(GTDB)
  accessed_at: '2026-11-15T05:05:48.861238Z'
  support: supports
  summary: Two exact-name rows each report2 genomes and fraction1.0 for Sulfobacillus_A
    acidophilus; no53633 row exists in this exact table. The native name route produces
    total4, fraction1.0, and GTDB suffix_A, independently recomputed after M5 apply.
- evidence_id: recomputed
  kind: validation
  reference: .temp/gtdb-source-routes-2849-20261115/diagnostic-001/native-route.json
  locator: result
  accessed_at: '2026-11-15T05:05:48.861238Z'
  support: supports
  summary: Actual unchanged native classifier and exact761 table reproduce every stored
    numerical/classification field after application; mapping_source explicitly records
    the route and its study-strain limit.
- evidence_id: application
  kind: record_content
  reference: .temp/gtdb-source-routes-2849-20261115/sulfobacillus-applied-m5-001/receipt.json
  locator: applied/before_sha256/after_sha256/inputs
  accessed_at: '2026-11-15T05:05:48.861238Z'
  support: supports
  summary: Actual M5 guarded apply changed only the reviewed GTDB block and appended
    native inline history; exact reviewed staging receipt and all source hashes were
    rechecked before replacement.
- evidence_id: prior
  kind: prior_review
  reference: reports/causal_graph_review/adversarial-review-20261006-batch53.yaml
  locator: findings.issue1509; adversarial_checks; limitations
  accessed_at: '2026-11-15T05:05:48.861238Z'
  support: context_only
  summary: The preserved batch53 review explicitly left canonical roster and non-graph
    claims uncertified, with composite community identity unresolved under1509. Its
    nine current nodes and zero arrows are unchanged by this mapping correction.
- evidence_id: abstract
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/24242252/
  locator: Abstract; committed PMID_24242252.md content
  accessed_at: '2026-11-15T05:05:48.861238Z'
  support: context_only
  summary: The inspected primary abstract names Sulfobacillus acidophilus in the mixed
    culture. It supplies no study-strain genome identity or GTDB mapping. This assessment
    read the abstract, not the inaccessible main paper or supplements.
assessments:
- assessment_id: reference-mapping
  area: grounding
  topic: Exact retained crosswalk route and denominator
  outcome: supported
  target_ids:
  - CommunityMech:000035
  evidence_ids:
  - mapping
  - recomputed
  - gtdb
  summary: Exact species-name rows679936/1051632 agree on Sulfobacillus_A acidophilus;
    native computation gives total4/fraction1.0/name difference true. Preserve NCBITaxon53633
    and source species name, remove unsupported latest/build wording, add no curated
    exemption.
- assessment_id: bounded-application
  area: provenance
  topic: One actual M5 guarded write and append-only history
  outcome: supported
  target_ids:
  - CommunityMech:000035
  evidence_ids:
  - application
  - new-history
  - history
  - strict
  - prior
  summary: Native validated writer persisted the exact reviewed candidate; every field
    outside the one GTDB block and appended inline event remains semantically unchanged.
    The external sidecar records actual application and limitations; old history and
    batch53 review remain immutable.
- assessment_id: identity-boundary
  area: scope
  topic: Reference species versus study strain and composite community
  outcome: supported
  target_ids:
  - CommunityMech:000035
  evidence_ids:
  - abstract
  - mapping
  - prior
  summary: The source abstract's species name is retained. A database name correspondence
    does not identify the paper's exact strain, resolve the composite roster or establish
    biological mechanism. The record remains subject to1509; the existing nine nodes/zero
    arrows are preserved rather than newly certified.
findings: []
actions: []
limitations:
- Diagnostic-only partial assessment; no full scientific review, new primary full-text/supplement
  acquisition, exact study-strain genome grounding or issue closure.
- The mapping is bound to SHA761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd.
  File modification time does not establish a GTDB release/build; no such release
  assertion is made.
- Full-record native completeness/quality metrics were not recomputed because this
  assessment covers only one database mapping; passing deterministic gates do not
  supply scientific approval.
- Six native scoped gates plus new-history ran on M5 Python3.13.2 atcb642708 with
  explicitly hashed additive check/builder source. References, term labels, corpus
  QC and generated docs are not claimed passed by this diagnostic; no source quotation
  or NCBITaxon label changed.
- Existing source/roster/functional concerns under1509 and other2849 records remain
  unresolved. An empty finding list is only the result for this corrected mapping
  scope.
links:
- https://github.com/CultureBotAI/CommunityMech/issues/2849
- https://github.com/CultureBotAI/CommunityMech/issues/1509
- https://github.com/CultureBotAI/CommunityMech/pull/2804
```
