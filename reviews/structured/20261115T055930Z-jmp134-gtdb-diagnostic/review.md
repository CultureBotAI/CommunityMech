# JMP134 exact-strain GTDB correspondence: scoped M5 diagnostic

- Review: 20261115T055930Z-jmp134-gtdb-diagnostic
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-11-15T05:59:30.507638Z
- Finished UTC: 2026-11-15T05:59:30.903727Z
- Reviewer: codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: false

## Summary

Scoped native database correspondence and actual provenance only. Exact JMP134 stock identity and pinned one-genome crosswalk row support this species block; existing biological claims and their scientific uncertainty remain unchanged.

## Scope And Provenance

One native GTDB species block, grounding status, exact stock/source identity and actual bounded application.

Selection: Representative exact-ID canary from the29 whole-record same-name species/strain planning group under issue2848; no group fanout preceded this canary.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f95ad0d731bc53634336ae7b794a7b23aa96a3c0.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000555 | data/isolates/Cupriavidus_Necator_JMP134_24DBP_Hydroxylase_Isolate_Baseline.yaml # taxonomy[0].taxon_term.gtdb_classification; gtdb_grounding_status | maintained | JMP134 exact-strain native GTDB correspondence and status |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000555 | Actual native M5 command passed on the exact applied record, with nonempty retained output and unchanged bound inputs. |
| validate-strict | passed | True | CommunityMech:000555 | Actual native M5 command passed on the exact applied record, with nonempty retained output and unchanged bound inputs. |
| validate-gtdb | passed | True | CommunityMech:000555 | Actual native M5 command passed on the exact applied record, with nonempty retained output and unchanged bound inputs. |
| validate-gtdb-domain | passed | True | CommunityMech:000555 | Actual native M5 command passed on the exact applied record, with nonempty retained output and unchanged bound inputs. |
| validate-scalars | passed | True | CommunityMech:000555 | Actual native M5 command passed on the exact applied record, with nonempty retained output and unchanged bound inputs. |
| validate-history | passed | True | CommunityMech:000555 | Actual native M5 command passed on the exact applied record, with nonempty retained output and unchanged bound inputs. |
| new-history | passed | True | CommunityMech:000555 | Actual native M5 command passed on the exact applied record, with nonempty retained output and unchanged bound inputs. |
| validate-terms | passed | True | CommunityMech:000555 | Actual native M5 command passed on the exact applied record, with nonempty retained output and unchanged bound inputs. |

## Scientific And Domain Assessments

### Exact source stock and database name scope

grounding: supported. Targets: CommunityMech:000555.

Preserve NCBITaxon264198 and both recorded names. The inspected NCBI synonym connects the paper's C.necator JMP134 to canonical C.pinatubonensis JMP134. No formal nomenclatural change or identity of other stocks is asserted.

### Exact-ID native result and one-genome population

grounding: supported. Targets: CommunityMech:000555.

Add the independently reviewed native species block for the exact strain-ID row and mark its presence GROUNDED. Fraction1.0 and total_genomes1 describe this pinned table row; is_reclassified:false is the native cleaned-name comparison, not a formal nomenclatural claim.

### Bounded actual application and retained scientific limits

provenance: supported. Targets: CommunityMech:000555.

Actual guarded application, eight native commands and append-only sidecar are retained. Entire remaining record semantics, earlier inline events and scientific reviews are preserved, including the open paralog-expression/flux question. The historical hash guard requires its separate strict successor integration.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| schema | .temp/gtdb-species-status-20261115/canary-run-schema-001/native.log | supports | Actual native M5 command passed on the exact applied record, with nonempty retained output and unchanged bound inputs. |
| strict | .temp/gtdb-species-status-20261115/canary-run-strict-001/native.log | supports | Actual native M5 command passed on the exact applied record, with nonempty retained output and unchanged bound inputs. |
| gtdb | .temp/gtdb-species-status-20261115/canary-run-gtdb-001/native.log | supports | Actual native M5 command passed on the exact applied record, with nonempty retained output and unchanged bound inputs. |
| domain | .temp/gtdb-species-status-20261115/canary-run-domain-001/native.log | supports | Actual native M5 command passed on the exact applied record, with nonempty retained output and unchanged bound inputs. |
| scalars | .temp/gtdb-species-status-20261115/canary-run-scalars-001/native.log | supports | Actual native M5 command passed on the exact applied record, with nonempty retained output and unchanged bound inputs. |
| history | .temp/gtdb-species-status-20261115/canary-run-history-001/native.log | supports | Actual native M5 command passed on the exact applied record, with nonempty retained output and unchanged bound inputs. |
| new-history | .temp/gtdb-species-status-20261115/canary-run-new-history-001/native.log | supports | Actual native M5 command passed on the exact applied record, with nonempty retained output and unchanged bound inputs. |
| terms | .temp/gtdb-species-status-20261115/canary-run-terms-001/native.log | supports | Actual native M5 command passed on the exact applied record, with nonempty retained output and unchanged bound inputs. |
| paper | https://pubmed.ncbi.nlm.nih.gov/42364169/; Methods/Results; retained cache offsets16009 and28959 | supports | The inspected study identifies C.necator JMP134. Its stock name remains unchanged in preferred_term and scientific prose; the paper is not used as a GTDB database assignment. |
| stock | reports/gtdb-species-status-20261115/jmp134-source-evidence-001.json; ncbi_identity_rows | supports | Local NCBITaxon264198 query identifies canonical C.pinatubonensis JMP134 and the related synonym C.necator JMP134. This exact-stock connection does not equate other C.necator strains. |
| mapping | reports/gtdb-species-status-20261115/jmp134-source-evidence-001.json; crosswalk_exact_rows[0] line71828; native_result | supports | Exact761 crosswalk contains one row for NCBITaxon264198/strainJMP134: one genome, fraction1.0 and GTDB:s__Cupriavidus_pinatubonensis. Fresh native ncbi_id resolution reproduces the same current block; no additional population is inferred. |
| application | .temp/gtdb-species-status-20261115/jmp134-applied-m5-001/receipt.json; applied/before_sha256/after_sha256/inputs | supports | Actual M5 guarded replacement persisted only the accepted block, GROUNDED status and two native inline events. All source and raw application inputs, native sidecar and current bytes are bound. |
| prior | reports/causal_graph_review/decisions/20261110-stage2-seven-records-batch147.yaml; records[id=CommunityMech:000555] | context_only | Original batch147 evidence and deep audit remain historical. The open relative in-vivo expression/flux contribution of tfdBI versus tfdBII remains unchanged; no new graph or full scientific review is claimed. |

## Limits And Additional Notes

- Scoped technical/provenance assessment with scientific_review:false. It neither completes the entire scientific record nor closes broader issue2848.
- The NCBI query output is retained but the whole local SQLite database/release was not hash-certified by that query. Exact crosswalk bytes, row, native resolver and source context are separately bound.
- One genome in this exact strain-ID row is a thin database population. No species-wide count, other stock identity, genome assembly accession or ANI measurement is inferred.
- Seven native scoped validation commands and one history scaffolder passed. Corpus QC, source-snippet matching and generated documentation are separate, unclaimed work.
- Original historical hash/biology assertions and immutable scientific reviews remain; a separately reviewed batch147 successor must integrate this actual diagnostic before historical-current tests can accept changed bytes.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261115T055930Z-jmp134-gtdb-diagnostic
kind: record
repository: CultureBotAI/CommunityMech
title: 'JMP134 exact-strain GTDB correspondence: scoped M5 diagnostic'
started_at: '2026-11-15T05:59:30.507638Z'
finished_at: '2026-11-15T05:59:30.903727Z'
reviewer:
  identity: codex
  kind: agent
  independence: self_review
  independence_basis: Authored source proof and correction; parent independently inspected
    primary contexts, NCBI query, exact crosswalk row, candidate semantics and guarded
    writer before actual application.
skill: curate-yaml-record
completion: completed
verdict: pass_with_limitations
scientific_review: false
summary: Scoped native database correspondence and actual provenance only. Exact JMP134
  stock identity and pinned one-genome crosswalk row support this species block; existing
  biological claims and their scientific uncertainty remain unchanged.
source:
  git_revision: f95ad0d731bc53634336ae7b794a7b23aa96a3c0
  state: working_tree
  inputs:
  - path: .temp/gtdb-species-status-20261115/canary-run-domain-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-species-status-20261115/canary-run-domain-001/native.log
    sha256: 332ecf51346fa3f2d11ffd899c61ba909008a78931e007de79751f531fcacbf9
    role: context
  - path: .temp/gtdb-species-status-20261115/canary-run-domain-001/receipt.json
    sha256: ae936eccfc8f5799245f4c6bb595346bc545106d7c06b8a3f9d61269daf8f661
    role: context
  - path: .temp/gtdb-species-status-20261115/canary-run-domain-001/start.json
    sha256: 71debd270e39315b90462e309b7d4f477577a769fb77460614f27e91c3bc4f73
    role: context
  - path: .temp/gtdb-species-status-20261115/canary-run-gtdb-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-species-status-20261115/canary-run-gtdb-001/native.log
    sha256: c9141e15bcc2300bea51a8003a2bebe6266d050ce872a8c93f00a4e66d2418ba
    role: context
  - path: .temp/gtdb-species-status-20261115/canary-run-gtdb-001/receipt.json
    sha256: 1d72278563d4752b2bd9c5c807e1e25b456f21f7ad31767922d7e3af05610aae
    role: context
  - path: .temp/gtdb-species-status-20261115/canary-run-gtdb-001/start.json
    sha256: 1ef4e77710723ab0499e1486aacdd594da64897ad26f09117bdf6c623500b36c
    role: context
  - path: .temp/gtdb-species-status-20261115/canary-run-history-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-species-status-20261115/canary-run-history-001/native.log
    sha256: 700b44227c4cf01270ac26f16b308622de0b26f48d71aec49cdfaaab87620f0a
    role: context
  - path: .temp/gtdb-species-status-20261115/canary-run-history-001/receipt.json
    sha256: a6f955df9f729ee0d20787b79b1a90e866f7381f68a67a76c386977126e91e1b
    role: context
  - path: .temp/gtdb-species-status-20261115/canary-run-history-001/start.json
    sha256: d8fce1e8580e2be961741db9737d6f3b20616cddd2e84cc7dd765ee66cf99b6b
    role: context
  - path: .temp/gtdb-species-status-20261115/canary-run-new-history-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-species-status-20261115/canary-run-new-history-001/native.log
    sha256: db6faa8c1e2a198114876392be02007dde8c4925e5c5eb9188e2c1c210850b6a
    role: context
  - path: .temp/gtdb-species-status-20261115/canary-run-new-history-001/receipt.json
    sha256: 7b9fe5a03827179a9c0f772a6272acf23b9a091f1a5e174aef38cefbadf497ce
    role: context
  - path: .temp/gtdb-species-status-20261115/canary-run-new-history-001/start.json
    sha256: dd0e9d990d09d7ed97f2cd21f7eb34d0824583ab631bbde6d01c7c0b211ea442
    role: context
  - path: .temp/gtdb-species-status-20261115/canary-run-scalars-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-species-status-20261115/canary-run-scalars-001/native.log
    sha256: 223b9bbf07c83143c1a3a077b25986f6ca5fdb2a50a9c88d38c1069e6e8331f2
    role: context
  - path: .temp/gtdb-species-status-20261115/canary-run-scalars-001/receipt.json
    sha256: 29e6cee8d8af56c1a530425e858b063571a1ca4d13ac282ba24b7e645acdc814
    role: context
  - path: .temp/gtdb-species-status-20261115/canary-run-scalars-001/start.json
    sha256: 54676b4a52d29af566589070398663c0e484dca6162147459f9fa2a17eab46ab
    role: context
  - path: .temp/gtdb-species-status-20261115/canary-run-schema-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-species-status-20261115/canary-run-schema-001/native.log
    sha256: 1c16a8c7832d9617ab727ec34b76689aca91ce2cd547ed259f6850a9be1c7c4f
    role: context
  - path: .temp/gtdb-species-status-20261115/canary-run-schema-001/receipt.json
    sha256: 84bda1a1e2979776ea9588014bf5d7900ad8111d6d0f2732614273d339f79cb0
    role: context
  - path: .temp/gtdb-species-status-20261115/canary-run-schema-001/start.json
    sha256: 355d4b90d36deaf86c3bd9ed0e7d713592a202111d4c127bd385e9665922092a
    role: context
  - path: .temp/gtdb-species-status-20261115/canary-run-strict-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-species-status-20261115/canary-run-strict-001/native.log
    sha256: 131faf4566fc5f9c509b02999ca65b6a8d8cc416954ebcba0d48730db74d7a06
    role: context
  - path: .temp/gtdb-species-status-20261115/canary-run-strict-001/receipt.json
    sha256: 997c24ff0e2d7ab20a38b1ec66c1baf51302391c2b83cd6c037fcb6eaab34bac
    role: context
  - path: .temp/gtdb-species-status-20261115/canary-run-strict-001/start.json
    sha256: b59631114a2b54ef143e609e1753c0e46dc073d56b49315632178c04390b9b18
    role: context
  - path: .temp/gtdb-species-status-20261115/canary-run-strict-001/strict.tsv
    sha256: b184ed5450b968070bb6c75648407e388f41a1eaf7017890723cf560999fc3f7
    role: context
  - path: .temp/gtdb-species-status-20261115/canary-run-terms-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-species-status-20261115/canary-run-terms-001/native.log
    sha256: e162acdf60e8b8830803316fa453ae85174ef422a993251f7a97de203272e64e
    role: context
  - path: .temp/gtdb-species-status-20261115/canary-run-terms-001/receipt.json
    sha256: 1ad8f522205ce4937b81b2cca5bb0ce546553b36a8c60b755b7c2bc178ab5331
    role: context
  - path: .temp/gtdb-species-status-20261115/canary-run-terms-001/start.json
    sha256: 732138281989a3f14cb33f32dc37985cf70a0c7f9369758139da2684a1bfd97c
    role: context
  - path: .temp/gtdb-species-status-20261115/jmp134-applied-m5-001/before.yaml
    sha256: 429964cbf945c41b2e89b57a072718158cf674e03786ef34b1ef96fe9247995e
    role: context
  - path: .temp/gtdb-species-status-20261115/jmp134-applied-m5-001/receipt.json
    sha256: d6d0af2d04990111aca3e7dd6c7437c3243e1bdb6f33f5afcc91feb857e83010
    role: context
  - path: .temp/gtdb-species-status-20261115/jmp134-candidate-001/Cupriavidus_Necator_JMP134_24DBP_Hydroxylase_Isolate_Baseline.yaml
    sha256: fede5211f0911d1a0543f1e19f8c53bf4c6dfc4ee306a6a3b8ee5d184ed7e786
    role: context
  - path: .temp/gtdb-species-status-20261115/jmp134-candidate-001/receipt.json
    sha256: ae389232cfd08f583b4979337e930b72b17efdca84691ea9c67e8359a3889132
    role: context
  - path: .temp/gtdb-species-status-20261115/jmp134-ncbi-001.json
    sha256: 769339350094249087509691f22c7cdd849a16a76befb2c464159ac46812e7d1
    role: context
  - path: .temp/gtdb-species-status-20261115/jmp134-source-001.json
    sha256: a6294d17526c05649b26e490918a69bacaa62cf524296f77e28b8c11f457c9e7
    role: context
  - path: .temp/gtdb-species-status-20261115/kg-microbe/data/raw/NCBI2GTDB.tsv.gz
    sha256: 761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd
    role: context
  - path: data/isolates/Cupriavidus_Necator_JMP134_24DBP_Hydroxylase_Isolate_Baseline.yaml
    sha256: fede5211f0911d1a0543f1e19f8c53bf4c6dfc4ee306a6a3b8ee5d184ed7e786
    role: target
  - path: history/records/Cupriavidus_Necator_JMP134_24DBP_Hydroxylase_Isolate_Baseline/2026-11-11T001200Z-antigravity-000555.yaml
    sha256: acb2b678752e4580f42ad07af8fc8ebf7d04a553264748d64338d09c84aa1a26
    role: context
  - path: history/records/Cupriavidus_Necator_JMP134_24DBP_Hydroxylase_Isolate_Baseline/2026-11-11T080000Z-antigravity-000555-causal-graph.yaml
    sha256: 2551806895414b8ca9c24df0e053a0c6ac3b9ab053c848566d12d07b61a30c13
    role: context
  - path: history/records/Cupriavidus_Necator_JMP134_24DBP_Hydroxylase_Isolate_Baseline/2026-11-15T055420Z-codex-edf3d2.yaml
    sha256: 4ce51b644bdab92f1ea7702ce4261045097c4a03280dc483d62aa8695637596a
    role: context
  - path: justfile
    sha256: 40369611ad4531582e420df0e9ff22109e4b18adf03b34d86b54200b280f2d0f
    role: context
  - path: references_cache/PMID_42364169.txt
    sha256: 76ae187fe615a75d522443b9deb085bc8499efb54df080407563f901c514a4d4
    role: context
  - path: reports/causal_graph_review/decisions/20261110-stage2-seven-records-batch147.yaml
    sha256: 732db4d507546996774aca3835d77c4a2b7feba7c2690522700488e2b8c4fe19
    role: context
  - path: reports/gtdb-species-status-20261115/jmp134-source-evidence-001.json
    sha256: 97fea5d3d87de7879155a45b29e8f0a754821f27fd87f4b875653bfc70e18d7f
    role: context
  - path: reviews/structured/20261111T121000Z-c15s4-record-deep-audit/review.yaml
    sha256: d6273b3c8723adc01ea4d71bc589e99bb8952da3cbd9067c6a0680979a4e7c71
    role: context
  - path: scripts/adhoc/apply_jmp134_grounding_20261115.py
    sha256: 1fb36dfe2583a139ed4c8428c270a459d8fedb736374562329dd43495be9cbda
    role: context
  - path: scripts/adhoc/build_species_grounding_diagnostic_20261115.py
    sha256: faae6fb9e0ddf3ba3e9e7963c5d078a4ae7a30fea584e07d93cc59b439cf4a03
    role: context
  - path: scripts/adhoc/check_jmp134_grounding_20261115.py
    sha256: 8fb2ba519b1c7fc166bcf3e9b78d3140a474adc348cf81a892383a268c089640
    role: context
  - path: scripts/adhoc/inspect_jmp134_grounding_20261115.py
    sha256: ff0230a4b400b33ec339df3585d5e2122cdb45c3b763670bcf93d18852f59a5f
    role: context
  - path: scripts/adhoc/query_jmp134_ncbi_identity_20261115.sql
    sha256: 83900e3f27194222c2f5db18402c99a7eb0e8cf58b8560994e02f845c2b9c019
    role: context
  - path: scripts/adhoc/stage_jmp134_grounding_20261115.py
    sha256: 75dbaaea7473894e2429fef117387f6ba63591bb2c9eb3b78a10008d01c42dd7
    role: context
  - path: scripts/gtdb_ground.py
    sha256: 0fc1ba926a56e5be85cdf064db0cf56452aeeee93f15b0ced98e8f11b5296175
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
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
  - path: src/communitymech/schema/mech_shared.yaml
    sha256: cf32864df1626201128e9311054b075bfc4ad3d8345491ac144122a5d5e67d11
    role: context
  - path: src/communitymech/validation/write_validated.py
    sha256: d19dd3b1e46856b4de67ecc17fc856aaa1034a9a97259cab3bbd54c3891fb019
    role: context
  - path: src/communitymech/validators/ncbi_domain.py
    sha256: b1e7ffc3c35c237e36c2c19fab42f1d42a14161397de9c5e726ed85897f1e262
    role: context
  - path: tests/test_causal_review_batch147.py
    sha256: dc6618679c150174a29fa1dea603ae63d6af9f485d948f9bfb13805b9a627816
    role: context
  - path: uv.lock
    sha256: 712838f8fa3d68fbd818ac8162f3f1e2f2637db1da1a8ebfaba0ef759690f3b4
    role: context
targets:
- target_id: CommunityMech:000555
  path: data/isolates/Cupriavidus_Necator_JMP134_24DBP_Hydroxylase_Isolate_Baseline.yaml
  selector: taxonomy[0].taxon_term.gtdb_classification; gtdb_grounding_status
  label: JMP134 exact-strain native GTDB correspondence and status
  kind: maintained
  ownership_note: CommunityMech owns the record; this review assesses one database
    correspondence and actual provenance, preserving prior biological claims.
scope:
  description: One native GTDB species block, grounding status, exact stock/source
    identity and actual bounded application.
  selection: Representative exact-ID canary from the29 whole-record same-name species/strain
    planning group under issue2848; no group fanout preceded this canary.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000555
  exclusions:
  - target: All other experimental claims/graph/discussions and other records
    reason: Preserved original science is not newly reassessed by this database diagnostic;
      no whole-record or corpus scientific approval.
checks:
- check_id: schema
  name: validate
  status: passed
  required: true
  summary: Actual native M5 command passed on the exact applied record, with nonempty
    retained output and unchanged bound inputs.
  target_ids:
  - CommunityMech:000555
  command: just --verbose --no-dotenv --color never validate data/isolates/Cupriavidus_Necator_JMP134_24DBP_Hydroxylase_Isolate_Baseline.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - schema
  scope_note: One exact record; no corpus or whole-record scientific approval.
- check_id: strict
  name: validate-strict
  status: passed
  required: true
  summary: Actual native M5 command passed on the exact applied record, with nonempty
    retained output and unchanged bound inputs.
  target_ids:
  - CommunityMech:000555
  command: just --verbose --no-dotenv --color never validate-strict data/isolates/Cupriavidus_Necator_JMP134_24DBP_Hydroxylase_Isolate_Baseline.yaml
    --out .temp/gtdb-species-status-20261115/canary-run-strict-001/strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - strict
  scope_note: One exact record; no corpus or whole-record scientific approval.
- check_id: gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: Actual native M5 command passed on the exact applied record, with nonempty
    retained output and unchanged bound inputs.
  target_ids:
  - CommunityMech:000555
  command: just --verbose --no-dotenv --color never validate-gtdb data/isolates/Cupriavidus_Necator_JMP134_24DBP_Hydroxylase_Isolate_Baseline.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - gtdb
  scope_note: One exact record; no corpus or whole-record scientific approval.
- check_id: domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: Actual native M5 command passed on the exact applied record, with nonempty
    retained output and unchanged bound inputs.
  target_ids:
  - CommunityMech:000555
  command: just --verbose --no-dotenv --color never validate-gtdb-domain data/isolates/Cupriavidus_Necator_JMP134_24DBP_Hydroxylase_Isolate_Baseline.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - domain
  scope_note: One exact record; no corpus or whole-record scientific approval.
- check_id: scalars
  name: validate-scalars
  status: passed
  required: true
  summary: Actual native M5 command passed on the exact applied record, with nonempty
    retained output and unchanged bound inputs.
  target_ids:
  - CommunityMech:000555
  command: just --verbose --no-dotenv --color never validate-scalars data/isolates/Cupriavidus_Necator_JMP134_24DBP_Hydroxylase_Isolate_Baseline.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - scalars
  scope_note: One exact record; no corpus or whole-record scientific approval.
- check_id: history
  name: validate-history
  status: passed
  required: true
  summary: Actual native M5 command passed on the exact applied record, with nonempty
    retained output and unchanged bound inputs.
  target_ids:
  - CommunityMech:000555
  command: just --verbose --no-dotenv --color never validate-history history/records/Cupriavidus_Necator_JMP134_24DBP_Hydroxylase_Isolate_Baseline
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - history
  scope_note: One exact record; no corpus or whole-record scientific approval.
- check_id: new-history
  name: new-history
  status: passed
  required: true
  summary: Actual native M5 command passed on the exact applied record, with nonempty
    retained output and unchanged bound inputs.
  target_ids:
  - CommunityMech:000555
  command: just --verbose --no-dotenv --color never new-history --kind record --slug
    Cupriavidus_Necator_JMP134_24DBP_Hydroxylase_Isolate_Baseline --target-root data/isolates
    --event EDIT --outcome changed --sections taxonomy,curation_history --actor-name
    codex --model gpt-6 --agent-tool codex --issue https://github.com/CultureBotAI/CommunityMech/issues/2848
    --summary 'Ground exact JMP134 stock through its native NCBI crosswalk row' --details
    'Applied only the reviewed native GTDB block, GROUNDED status and two native inline
    events. Exact crosswalk SHA256761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd
    row71828 maps unchanged NCBITaxon264198 strain JMP134 to GTDB:s__Cupriavidus_pinatubonensis,
    one genome and fraction1. The primary C.necator JMP134 name is a retained NCBI
    synonym of canonical C.pinatubonensis JMP134. No formal nomenclatural event, other
    stock identity or additional genome population is inferred. All experimental claims,
    source quotations, graph, open paralog-expression discussion and prior history
    remain unchanged. This is a scoped database correction, not a full-record scientific
    review. Actual application receipt .temp/gtdb-species-status-20261115/jmp134-applied-m5-001/receipt.json
    sha256:d6d0af2d04990111aca3e7dd6c7437c3243e1bdb6f33f5afcc91feb857e83010.'
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - new-history
  scope_note: One exact record; no corpus or whole-record scientific approval.
- check_id: terms
  name: validate-terms
  status: passed
  required: true
  summary: Actual native M5 command passed on the exact applied record, with nonempty
    retained output and unchanged bound inputs.
  target_ids:
  - CommunityMech:000555
  command: just --verbose --no-dotenv --color never validate-terms data/isolates/Cupriavidus_Necator_JMP134_24DBP_Hydroxylase_Isolate_Baseline.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - terms
  scope_note: One exact record; no corpus or whole-record scientific approval.
evidence:
- evidence_id: schema
  kind: validation
  reference: .temp/gtdb-species-status-20261115/canary-run-schema-001/native.log
  accessed_at: '2026-11-15T05:59:30.507638Z'
  support: supports
  summary: Actual native M5 command passed on the exact applied record, with nonempty
    retained output and unchanged bound inputs.
- evidence_id: strict
  kind: validation
  reference: .temp/gtdb-species-status-20261115/canary-run-strict-001/native.log
  accessed_at: '2026-11-15T05:59:30.507638Z'
  support: supports
  summary: Actual native M5 command passed on the exact applied record, with nonempty
    retained output and unchanged bound inputs.
- evidence_id: gtdb
  kind: validation
  reference: .temp/gtdb-species-status-20261115/canary-run-gtdb-001/native.log
  accessed_at: '2026-11-15T05:59:30.507638Z'
  support: supports
  summary: Actual native M5 command passed on the exact applied record, with nonempty
    retained output and unchanged bound inputs.
- evidence_id: domain
  kind: validation
  reference: .temp/gtdb-species-status-20261115/canary-run-domain-001/native.log
  accessed_at: '2026-11-15T05:59:30.507638Z'
  support: supports
  summary: Actual native M5 command passed on the exact applied record, with nonempty
    retained output and unchanged bound inputs.
- evidence_id: scalars
  kind: validation
  reference: .temp/gtdb-species-status-20261115/canary-run-scalars-001/native.log
  accessed_at: '2026-11-15T05:59:30.507638Z'
  support: supports
  summary: Actual native M5 command passed on the exact applied record, with nonempty
    retained output and unchanged bound inputs.
- evidence_id: history
  kind: validation
  reference: .temp/gtdb-species-status-20261115/canary-run-history-001/native.log
  accessed_at: '2026-11-15T05:59:30.507638Z'
  support: supports
  summary: Actual native M5 command passed on the exact applied record, with nonempty
    retained output and unchanged bound inputs.
- evidence_id: new-history
  kind: validation
  reference: .temp/gtdb-species-status-20261115/canary-run-new-history-001/native.log
  accessed_at: '2026-11-15T05:59:30.507638Z'
  support: supports
  summary: Actual native M5 command passed on the exact applied record, with nonempty
    retained output and unchanged bound inputs.
- evidence_id: terms
  kind: validation
  reference: .temp/gtdb-species-status-20261115/canary-run-terms-001/native.log
  accessed_at: '2026-11-15T05:59:30.507638Z'
  support: supports
  summary: Actual native M5 command passed on the exact applied record, with nonempty
    retained output and unchanged bound inputs.
- evidence_id: paper
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/42364169/
  locator: Methods/Results; retained cache offsets16009 and28959
  accessed_at: '2026-11-15T05:59:30.507638Z'
  support: supports
  summary: The inspected study identifies C.necator JMP134. Its stock name remains
    unchanged in preferred_term and scientific prose; the paper is not used as a GTDB
    database assignment.
- evidence_id: stock
  kind: database
  reference: reports/gtdb-species-status-20261115/jmp134-source-evidence-001.json
  locator: ncbi_identity_rows
  accessed_at: '2026-11-15T05:59:30.507638Z'
  support: supports
  summary: Local NCBITaxon264198 query identifies canonical C.pinatubonensis JMP134
    and the related synonym C.necator JMP134. This exact-stock connection does not
    equate other C.necator strains.
- evidence_id: mapping
  kind: database
  reference: reports/gtdb-species-status-20261115/jmp134-source-evidence-001.json
  locator: crosswalk_exact_rows[0] line71828; native_result
  accessed_at: '2026-11-15T05:59:30.507638Z'
  support: supports
  summary: 'Exact761 crosswalk contains one row for NCBITaxon264198/strainJMP134:
    one genome, fraction1.0 and GTDB:s__Cupriavidus_pinatubonensis. Fresh native ncbi_id
    resolution reproduces the same current block; no additional population is inferred.'
- evidence_id: application
  kind: record_content
  reference: .temp/gtdb-species-status-20261115/jmp134-applied-m5-001/receipt.json
  locator: applied/before_sha256/after_sha256/inputs
  accessed_at: '2026-11-15T05:59:30.507638Z'
  support: supports
  summary: Actual M5 guarded replacement persisted only the accepted block, GROUNDED
    status and two native inline events. All source and raw application inputs, native
    sidecar and current bytes are bound.
- evidence_id: prior
  kind: prior_review
  reference: reports/causal_graph_review/decisions/20261110-stage2-seven-records-batch147.yaml
  locator: records[id=CommunityMech:000555]
  accessed_at: '2026-11-15T05:59:30.507638Z'
  support: context_only
  summary: Original batch147 evidence and deep audit remain historical. The open relative
    in-vivo expression/flux contribution of tfdBI versus tfdBII remains unchanged;
    no new graph or full scientific review is claimed.
assessments:
- assessment_id: identity
  area: grounding
  topic: Exact source stock and database name scope
  outcome: supported
  target_ids:
  - CommunityMech:000555
  evidence_ids:
  - paper
  - stock
  - terms
  summary: Preserve NCBITaxon264198 and both recorded names. The inspected NCBI synonym
    connects the paper's C.necator JMP134 to canonical C.pinatubonensis JMP134. No
    formal nomenclatural change or identity of other stocks is asserted.
- assessment_id: correspondence
  area: grounding
  topic: Exact-ID native result and one-genome population
  outcome: supported
  target_ids:
  - CommunityMech:000555
  evidence_ids:
  - mapping
  - gtdb
  - domain
  summary: Add the independently reviewed native species block for the exact strain-ID
    row and mark its presence GROUNDED. Fraction1.0 and total_genomes1 describe this
    pinned table row; is_reclassified:false is the native cleaned-name comparison,
    not a formal nomenclatural claim.
- assessment_id: provenance
  area: provenance
  topic: Bounded actual application and retained scientific limits
  outcome: supported
  target_ids:
  - CommunityMech:000555
  evidence_ids:
  - application
  - schema
  - strict
  - scalars
  - new-history
  - history
  - prior
  summary: Actual guarded application, eight native commands and append-only sidecar
    are retained. Entire remaining record semantics, earlier inline events and scientific
    reviews are preserved, including the open paralog-expression/flux question. The
    historical hash guard requires its separate strict successor integration.
findings: []
actions: []
limitations:
- Scoped technical/provenance assessment with scientific_review:false. It neither
  completes the entire scientific record nor closes broader issue2848.
- The NCBI query output is retained but the whole local SQLite database/release was
  not hash-certified by that query. Exact crosswalk bytes, row, native resolver and
  source context are separately bound.
- One genome in this exact strain-ID row is a thin database population. No species-wide
  count, other stock identity, genome assembly accession or ANI measurement is inferred.
- Seven native scoped validation commands and one history scaffolder passed. Corpus
  QC, source-snippet matching and generated documentation are separate, unclaimed
  work.
- Original historical hash/biology assertions and immutable scientific reviews remain;
  a separately reviewed batch147 successor must integrate this actual diagnostic before
  historical-current tests can accept changed bytes.
links:
- https://github.com/CultureBotAI/CommunityMech/issues/2848
- https://github.com/CultureBotAI/CommunityMech/pull/2862
```
