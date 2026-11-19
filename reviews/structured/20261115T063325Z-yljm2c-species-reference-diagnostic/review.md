# YL-JM2C species-reference GTDB correspondence: scoped M5 diagnostic

- Review: 20261115T063325Z-yljm2c-species-reference-diagnostic
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-11-15T06:33:25.585735Z
- Finished UTC: 2026-11-15T06:33:25.691200Z
- Reviewer: codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: false

## Summary

The paper supports identifying stock YL-JM2C as Rhizorhabdus wittichii. The unchanged NCBI species identifier maps through the pinned native crosswalk to the same GTDB species, with seven reference genomes and rounded fraction 0.86. This adds a species-reference correspondence; it does not certify that the study stock's genome belongs to that GTDB cluster. Actual application, native history and eight required commands are bound.

## Scope And Provenance

One GTDB species-reference block, grounding status, source identity and bounded actual provenance; preserve the rest of the scientific record.

Selection: One complete record, CommunityMech:000554, selected as the first species-reference and shared-runner canary after exact-strain 000555. No wider batch execution preceded this end-to-end canary.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base c86a898df4c5206efc683da9394d3eb68d06661b.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000554 | data/isolates/Rhizorhabdus_Wittichii_YL_JM2C_BDE47_Dioxygenase_Isolate_Baseline.yaml # taxonomy[0].taxon_term.gtdb_classification; gtdb_grounding_status | maintained | YL-JM2C species-reference correspondence and retained stock boundary |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000554 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-strict | passed | True | CommunityMech:000554 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-gtdb | passed | True | CommunityMech:000554 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-gtdb-domain | passed | True | CommunityMech:000554 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-scalars | passed | True | CommunityMech:000554 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-history | passed | True | CommunityMech:000554 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| new-history | passed | True | CommunityMech:000554 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-terms | passed | True | CommunityMech:000554 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |

## Scientific And Domain Assessments

### Source stock and species authority boundary

grounding: supported. Targets: CommunityMech:000554.

Preserve stock YL-JM2C, the source's ANI-based species assignment, BioProject and unchanged NCBITaxon species identity. The new GTDB block represents that species-reference correspondence, not a separately verified genome classification of YL-JM2C.

### Exact native species-reference population and name comparison

grounding: supported. Targets: CommunityMech:000554.

Retain native total_genomes 7 and majority_fraction 0.86 from the exact species-ID row, without deriving a support numerator or equating reference genomes with study stocks. Native is_reclassified:false records agreement of the current species names, without denying the paper's earlier stock reassignment.

### Actual bounded application and unchanged scientific uncertainty

provenance: supported. Targets: CommunityMech:000554.

The current record equals the approved candidate after a native validated guarded write. Eight required commands and one new native history sidecar persisted. Existing stock names, source quotations, ecological graph, RwTfdB discussion and prior history are unchanged. Separate strict batch147 successor and combined generated pages/QC remain integration work.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| 000554-schema | .temp/gtdb-species-status-20261115/yljm2c-run-schema-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000554-strict | .temp/gtdb-species-status-20261115/yljm2c-run-strict-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000554-gtdb | .temp/gtdb-species-status-20261115/yljm2c-run-gtdb-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000554-domain | .temp/gtdb-species-status-20261115/yljm2c-run-domain-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000554-scalars | .temp/gtdb-species-status-20261115/yljm2c-run-scalars-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000554-history | .temp/gtdb-species-status-20261115/yljm2c-run-history-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000554-new-history | .temp/gtdb-species-status-20261115/yljm2c-run-new-history-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000554-terms | .temp/gtdb-species-status-20261115/yljm2c-run-terms-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000554-paper | https://pubmed.ncbi.nlm.nih.gov/42364169/; Results, retained main-text offset 22937; Data availability offset 50466 | supports | The inspected paper reports approximately 97% ANI between YL-JM2C and R. wittichii RW1 and identifies the complete study-stock assembly by BioProject PRJNA1397584. This supports the paper's species identification, not an independent GTDB classification of that stock. |
| 000554-database | reports/gtdb-species-status-20261115/yljm2c-source-evidence-001.json; occurrences[0].ncbi_identity_rows/crosswalk_exact_rows/native_result | supports | The local authority labels NCBITaxon:160791 Rhizorhabdus wittichii at species rank. Exact pinned crosswalk row 7583 reports seven genomes and fraction 0.86, and the native ncbi_id resolver reproduces GTDB:s__Rhizorhabdus_wittichii. No exact YL-JM2C assembly membership or numerator is inferred. |
| 000554-application | .temp/gtdb-species-status-20261115/yljm2c-applied-m5-001/receipt.json; applied/before_sha256/after_sha256/inputs | supports | The actual guarded M5 application persisted only the accepted block, status and two native inline events. The native append-only sidecar and all eight current gate receipts are retained and bound. |
| 000554-prior | reports/causal_graph_review/decisions/20261110-stage2-seven-records-batch147.yaml; records[id=CommunityMech:000554] and immutable c15s4 deep audit | context_only | Original scientific assertions and the unresolved RwTfdB structural-determinants question remain historical evidence. The isolated baseline retains one community-level node and no inferred consortium cross-feeding arrow; no mechanism claim was changed by this database correction. |

## Limits And Additional Notes

- Scoped technical/provenance assessment with scientific_review:false; no full scientific record approval or corpus QC completion.
- The seven-genome crosswalk population is keyed to species NCBITaxon:160791, not stock YL-JM2C or BioProject PRJNA1397584. Membership of that stock in the GTDB species cluster was not independently established. The rounded fraction 0.86 is retained without inventing a support-genome numerator.
- Local NCBI label/rank query output is retained; the complete SQLite database and release were not hash-certified. Exact source cache, crosswalk and resolver bytes are bound separately.
- The source's earlier Sphingomonas-to-Rhizorhabdus stock reassignment is preserved. Native is_reclassified:false only compares current canonical and GTDB names.
- The open RwTfdB structural-determinants discussion and all prior biological claims remain unchanged; this diagnostic does not answer that scientific question.
- Seven native scoped validators plus native history scaffolding passed. Source-snippet matching, generated pages, the strict historical successor integration and final combined full QC remain separately accounted work.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261115T063325Z-yljm2c-species-reference-diagnostic
kind: record
repository: CultureBotAI/CommunityMech
title: 'YL-JM2C species-reference GTDB correspondence: scoped M5 diagnostic'
started_at: '2026-11-15T06:33:25.585735Z'
finished_at: '2026-11-15T06:33:25.691200Z'
reviewer:
  identity: codex
  kind: agent
  independence: self_review
  independence_basis: Authored source proof and bounded correction. Parent independently
    inspected primary ANI/BioProject passages, NCBI species identity, the exact crosswalk
    row, candidate diff, shared native writer and controls before actual M5 application.
skill: curate-yaml-record
completion: completed
verdict: pass_with_limitations
scientific_review: false
summary: The paper supports identifying stock YL-JM2C as Rhizorhabdus wittichii. The
  unchanged NCBI species identifier maps through the pinned native crosswalk to the
  same GTDB species, with seven reference genomes and rounded fraction 0.86. This
  adds a species-reference correspondence; it does not certify that the study stock's
  genome belongs to that GTDB cluster. Actual application, native history and eight
  required commands are bound.
source:
  git_revision: c86a898df4c5206efc683da9394d3eb68d06661b
  state: working_tree
  inputs:
  - path: .temp/gtdb-species-status-20261115/kg-microbe/data/raw/NCBI2GTDB.tsv.gz
    sha256: 761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd
    role: context
  - path: .temp/gtdb-species-status-20261115/yljm2c-applied-m5-001/before.yaml
    sha256: e70a8434bd8db3852302899814f08a19d97c0e9d73a6636cb7715295642fdf59
    role: context
  - path: .temp/gtdb-species-status-20261115/yljm2c-applied-m5-001/receipt.json
    sha256: 4158807ea699f981ed96fdb3e966878f95df84ea1c0b1682d9541305646e56d9
    role: context
  - path: .temp/gtdb-species-status-20261115/yljm2c-candidate-001/Rhizorhabdus_Wittichii_YL_JM2C_BDE47_Dioxygenase_Isolate_Baseline.yaml
    sha256: dd333d36e5ed9169cf2ddda11bc5d53466dc838895bfee5a8d71336f9c360673
    role: context
  - path: .temp/gtdb-species-status-20261115/yljm2c-candidate-001/receipt.json
    sha256: aba4beda095a64b5bbd8beffd7db3190b8755407ba84bb835512d2706fc08663
    role: context
  - path: .temp/gtdb-species-status-20261115/yljm2c-check-config-001.json
    sha256: b6022abdfcb86af856599bfce582faad1fda5c644204fb31c5256a67bf3fd6cb
    role: context
  - path: .temp/gtdb-species-status-20261115/yljm2c-run-domain-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-species-status-20261115/yljm2c-run-domain-001/native.log
    sha256: 2b33e720656d73eb27fbcfcec5135c4fda1b1b880aab1090269ccf1c7b25281b
    role: context
  - path: .temp/gtdb-species-status-20261115/yljm2c-run-domain-001/receipt.json
    sha256: f240cbb1c31722a01f988af6b07851df1b066c2b7b4f30f664447fd88b081ac1
    role: context
  - path: .temp/gtdb-species-status-20261115/yljm2c-run-domain-001/start.json
    sha256: 63dec79da8d98c46efcc7d91a662b7a76bda80d2c542c168a322a2fe659e12a3
    role: context
  - path: .temp/gtdb-species-status-20261115/yljm2c-run-gtdb-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-species-status-20261115/yljm2c-run-gtdb-001/native.log
    sha256: de2e1651d5e2bc6fec1c8611906066ef574abd142a7adfb5ab388adb8790053e
    role: context
  - path: .temp/gtdb-species-status-20261115/yljm2c-run-gtdb-001/receipt.json
    sha256: 9ccf3c0d5ea0e9c016635975594d4094d60ce81b67e6fa531fce8b84c2883721
    role: context
  - path: .temp/gtdb-species-status-20261115/yljm2c-run-gtdb-001/start.json
    sha256: b3497b0f5523983468d5943a4d9a13305abcc68776e629f632b901723c7f7eba
    role: context
  - path: .temp/gtdb-species-status-20261115/yljm2c-run-history-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-species-status-20261115/yljm2c-run-history-001/native.log
    sha256: 700b44227c4cf01270ac26f16b308622de0b26f48d71aec49cdfaaab87620f0a
    role: context
  - path: .temp/gtdb-species-status-20261115/yljm2c-run-history-001/receipt.json
    sha256: 2be214f4645db20af8c26dd5342f7c7883b583d6f61e0eb598f1b4793d5ebdc0
    role: context
  - path: .temp/gtdb-species-status-20261115/yljm2c-run-history-001/start.json
    sha256: 4139107f133f4fbffdaae3b512d590ff7141239ae1f2dc678bf7f0ea0d8efa3d
    role: context
  - path: .temp/gtdb-species-status-20261115/yljm2c-run-new-history-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-species-status-20261115/yljm2c-run-new-history-001/native.log
    sha256: 0c5f1dc8b1e84cec8e9139da0c9ac8c29ab4e2766eebf2425d61edba78173b81
    role: context
  - path: .temp/gtdb-species-status-20261115/yljm2c-run-new-history-001/receipt.json
    sha256: 738282dce732440ac2b760ed0b9dd4be6f224690e35b1015fda13edead08b89d
    role: context
  - path: .temp/gtdb-species-status-20261115/yljm2c-run-new-history-001/start.json
    sha256: bd321982cc6cfd7080173600ea37de6d3c8db6912c2886731c48644dcb67d83b
    role: context
  - path: .temp/gtdb-species-status-20261115/yljm2c-run-scalars-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-species-status-20261115/yljm2c-run-scalars-001/native.log
    sha256: 39a9e77964022c4680fc96ab41f68bfd0d685dc54243056f085e8971b4327ad2
    role: context
  - path: .temp/gtdb-species-status-20261115/yljm2c-run-scalars-001/receipt.json
    sha256: 3f26e9a9912772a42f82baac3df2f63df8a4f484cce63d6b89314556f4ba6da6
    role: context
  - path: .temp/gtdb-species-status-20261115/yljm2c-run-scalars-001/start.json
    sha256: ec85d8a45861749129b452c5686cba825fff57710605fc2917e182530c7c69b7
    role: context
  - path: .temp/gtdb-species-status-20261115/yljm2c-run-schema-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-species-status-20261115/yljm2c-run-schema-001/native.log
    sha256: d7ad9d098c51778036b5612eae5d2b399ce185fd05a71d9e177ad6aed7ad8b2d
    role: context
  - path: .temp/gtdb-species-status-20261115/yljm2c-run-schema-001/receipt.json
    sha256: 0c66b7eec6940cbc9565a1c25f9fa7534cdc3f0d60921e8f1ade385276653b91
    role: context
  - path: .temp/gtdb-species-status-20261115/yljm2c-run-schema-001/start.json
    sha256: e83dfde33a249b5c727f029345772fab017a975eaf4df8daeea432f1509fb141
    role: context
  - path: .temp/gtdb-species-status-20261115/yljm2c-run-strict-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-species-status-20261115/yljm2c-run-strict-001/native.log
    sha256: b5591316c4b3abd4f9ac8c90e1f1a20e5897d342ae722b45a6d5d4d033b783d0
    role: context
  - path: .temp/gtdb-species-status-20261115/yljm2c-run-strict-001/receipt.json
    sha256: b43f7542f7aca90bc3b8593569a8664c079301d677c4cbd64c7492a41d56686e
    role: context
  - path: .temp/gtdb-species-status-20261115/yljm2c-run-strict-001/start.json
    sha256: 5397cea206a54d510369503e8dad439e20df2d39f0b5ef3307d551d1bea99d92
    role: context
  - path: .temp/gtdb-species-status-20261115/yljm2c-run-strict-001/strict.tsv
    sha256: b184ed5450b968070bb6c75648407e388f41a1eaf7017890723cf560999fc3f7
    role: context
  - path: .temp/gtdb-species-status-20261115/yljm2c-run-terms-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-species-status-20261115/yljm2c-run-terms-001/native.log
    sha256: 9515851863978d0a1b77fb20c1af2252884c829bc84584f29925cec842ac803e
    role: context
  - path: .temp/gtdb-species-status-20261115/yljm2c-run-terms-001/receipt.json
    sha256: 6c4e2a3996773f1a187b9dc352b2b368268020f90784871c9fc4f0fe4951602a
    role: context
  - path: .temp/gtdb-species-status-20261115/yljm2c-run-terms-001/start.json
    sha256: 38ce4b0a4fa00cb3502db75bab933402678c5eff81a85f38b83faa2a06ed2180
    role: context
  - path: .temp/gtdb-species-status-20261115/yljm2c-source-001.json
    sha256: b26b8382f0cb9ceea6f357c807e9b2b1f772c285e4ad81b6591532203a6f9ac1
    role: context
  - path: data/isolates/Rhizorhabdus_Wittichii_YL_JM2C_BDE47_Dioxygenase_Isolate_Baseline.yaml
    sha256: dd333d36e5ed9169cf2ddda11bc5d53466dc838895bfee5a8d71336f9c360673
    role: target
  - path: history/records/Rhizorhabdus_Wittichii_YL_JM2C_BDE47_Dioxygenase_Isolate_Baseline/2026-11-11T001200Z-antigravity-000554.yaml
    sha256: 45c376655260b1714f84e60a1e2c68ae1fe872581bcb235bb5a9906bb2881ef1
    role: context
  - path: history/records/Rhizorhabdus_Wittichii_YL_JM2C_BDE47_Dioxygenase_Isolate_Baseline/2026-11-11T080000Z-antigravity-000554-causal-graph.yaml
    sha256: fd24c1a8410387101810717acc514358a0433a4341b3dc717ec04d6b9c3d5465
    role: context
  - path: history/records/Rhizorhabdus_Wittichii_YL_JM2C_BDE47_Dioxygenase_Isolate_Baseline/2026-11-15T062832Z-codex-867208.yaml
    sha256: bcdda802d16bcfa466ab90ac7b77a6b3ba447dd4c79bcbd6746dceeb1f432755
    role: context
  - path: justfile
    sha256: 40369611ad4531582e420df0e9ff22109e4b18adf03b34d86b54200b280f2d0f
    role: context
  - path: pyproject.toml
    sha256: be952f0f137f85fed66bda0908f12014f1797a2dd229b44d832afc0c00471655
    role: context
  - path: references_cache/PMID_42364169.txt
    sha256: 76ae187fe615a75d522443b9deb085bc8499efb54df080407563f901c514a4d4
    role: context
  - path: reports/causal_graph_review/decisions/20261110-stage2-seven-records-batch147.yaml
    sha256: 732db4d507546996774aca3835d77c4a2b7feba7c2690522700488e2b8c4fe19
    role: context
  - path: reports/gtdb-species-status-20261115/yljm2c-review-config-001.json
    sha256: 755e1f0bc8a0287bfe8a0ea693f825b6d917c140874cd956cced6709d2091463
    role: context
  - path: reports/gtdb-species-status-20261115/yljm2c-source-config-001.json
    sha256: 3586e68ae1dda98c3620839c3b2bab4e24f1b859d113958f84a25f00ca1e1e73
    role: context
  - path: reports/gtdb-species-status-20261115/yljm2c-source-evidence-001.json
    sha256: 7741938514a8f5ff8d4336e12716c9f53207eb1806ee6339891a8a178ae9bad0
    role: context
  - path: reviews/structured/20261111T121000Z-c15s4-record-deep-audit/review.yaml
    sha256: d6273b3c8723adc01ea4d71bc589e99bb8952da3cbd9067c6a0680979a4e7c71
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/adhoc/build_gtdb_batch_diagnostic_20261115.py
    sha256: c6bf0d09dc3d01797ab5d956a4f7458a9a153a8704508f50e656729e4ee1b860
    role: context
  - path: scripts/adhoc/check_gtdb_batch_unit_20261115.py
    sha256: 723047d1ec66fa752d6cedddbb6d399b18fa7f5b7a0e27fc435c76abfeb10493
    role: context
  - path: scripts/adhoc/export_m5_technical_evidence_20261114.py
    sha256: a0f43f617e8921443e660d262d28713f40b4c23770b684203c37b65330cc4a5d
    role: context
  - path: scripts/adhoc/gtdb_batch_curation_20261115.py
    sha256: 867e974e9c55325fb1b7e32f81dcf6b7a65b6720941fd303040f5570e46ba232
    role: context
  - path: scripts/adhoc/inspect_gtdb_batch_sources_20261115.py
    sha256: 3b46d37e81d3943618668178f729d36f63d85ecedf209d23516050e42a09ac02
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
- target_id: CommunityMech:000554
  path: data/isolates/Rhizorhabdus_Wittichii_YL_JM2C_BDE47_Dioxygenase_Isolate_Baseline.yaml
  selector: taxonomy[0].taxon_term.gtdb_classification; gtdb_grounding_status
  label: YL-JM2C species-reference correspondence and retained stock boundary
  kind: maintained
  ownership_note: CommunityMech owns this record; only declared GTDB correspondence/status
    and actual provenance are assessed.
scope:
  description: One GTDB species-reference block, grounding status, source identity
    and bounded actual provenance; preserve the rest of the scientific record.
  selection: One complete record, CommunityMech:000554, selected as the first species-reference
    and shared-runner canary after exact-strain 000555. No wider batch execution preceded
    this end-to-end canary.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000554
  exclusions:
  - target: Other scientific claims and records
    reason: Existing biology is preserved, not newly certified by this database diagnostic.
checks:
- check_id: 000554-schema
  name: validate
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000554
  command: just --verbose --no-dotenv --color never validate data/isolates/Rhizorhabdus_Wittichii_YL_JM2C_BDE47_Dioxygenase_Isolate_Baseline.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000554-schema
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000554-strict
  name: validate-strict
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000554
  command: just --verbose --no-dotenv --color never validate-strict data/isolates/Rhizorhabdus_Wittichii_YL_JM2C_BDE47_Dioxygenase_Isolate_Baseline.yaml
    --out .temp/gtdb-species-status-20261115/yljm2c-run-strict-001/strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000554-strict
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000554-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000554
  command: just --verbose --no-dotenv --color never validate-gtdb data/isolates/Rhizorhabdus_Wittichii_YL_JM2C_BDE47_Dioxygenase_Isolate_Baseline.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000554-gtdb
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000554-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000554
  command: just --verbose --no-dotenv --color never validate-gtdb-domain data/isolates/Rhizorhabdus_Wittichii_YL_JM2C_BDE47_Dioxygenase_Isolate_Baseline.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000554-domain
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000554-scalars
  name: validate-scalars
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000554
  command: just --verbose --no-dotenv --color never validate-scalars data/isolates/Rhizorhabdus_Wittichii_YL_JM2C_BDE47_Dioxygenase_Isolate_Baseline.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000554-scalars
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000554-history
  name: validate-history
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000554
  command: just --verbose --no-dotenv --color never validate-history history/records/Rhizorhabdus_Wittichii_YL_JM2C_BDE47_Dioxygenase_Isolate_Baseline
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000554-history
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000554-new-history
  name: new-history
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000554
  command: just --verbose --no-dotenv --color never new-history --kind record --slug
    Rhizorhabdus_Wittichii_YL_JM2C_BDE47_Dioxygenase_Isolate_Baseline --target-root
    data/isolates --event EDIT --outcome changed --sections taxonomy,curation_history
    --actor-name codex --model gpt-6 --agent-tool codex --issue https://github.com/CultureBotAI/CommunityMech/issues/2848
    --summary 'Add the reviewed species-reference GTDB correspondence for YL-JM2C'
    --details 'Applied only the accepted native block for unchanged NCBITaxon:160791
    Rhizorhabdus wittichii, GROUNDED status, and two native inline events. The exact
    crosswalk SHA256 761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd
    row 7583 reports seven species-reference genomes and rounded fraction 0.86. The
    paper identifies stock YL-JM2C by approximately 97 percent ANI to RW1; this does
    not establish that the stock'"'"'s BioProject PRJNA1397584 is represented among
    those seven genomes. No numerator, exact-stock GTDB assembly identity, or formal
    nomenclatural event is inferred. All other experimental claims, source quotations,
    stock names, graph, open RwTfdB structural-determinants discussion and previous
    history remain unchanged. This is a scoped database correspondence correction,
    not a full scientific record review. Actual apply receipt .temp/gtdb-species-status-20261115/yljm2c-applied-m5-001/receipt.json
    sha256:4158807ea699f981ed96fdb3e966878f95df84ea1c0b1682d9541305646e56d9.'
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000554-new-history
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000554-terms
  name: validate-terms
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000554
  command: just --verbose --no-dotenv --color never validate-terms data/isolates/Rhizorhabdus_Wittichii_YL_JM2C_BDE47_Dioxygenase_Isolate_Baseline.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000554-terms
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
evidence:
- evidence_id: 000554-schema
  kind: validation
  reference: .temp/gtdb-species-status-20261115/yljm2c-run-schema-001/native.log
  accessed_at: '2026-11-15T06:33:25.585735Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000554-strict
  kind: validation
  reference: .temp/gtdb-species-status-20261115/yljm2c-run-strict-001/native.log
  accessed_at: '2026-11-15T06:33:25.585735Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000554-gtdb
  kind: validation
  reference: .temp/gtdb-species-status-20261115/yljm2c-run-gtdb-001/native.log
  accessed_at: '2026-11-15T06:33:25.585735Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000554-domain
  kind: validation
  reference: .temp/gtdb-species-status-20261115/yljm2c-run-domain-001/native.log
  accessed_at: '2026-11-15T06:33:25.585735Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000554-scalars
  kind: validation
  reference: .temp/gtdb-species-status-20261115/yljm2c-run-scalars-001/native.log
  accessed_at: '2026-11-15T06:33:25.585735Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000554-history
  kind: validation
  reference: .temp/gtdb-species-status-20261115/yljm2c-run-history-001/native.log
  accessed_at: '2026-11-15T06:33:25.585735Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000554-new-history
  kind: validation
  reference: .temp/gtdb-species-status-20261115/yljm2c-run-new-history-001/native.log
  accessed_at: '2026-11-15T06:33:25.585735Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000554-terms
  kind: validation
  reference: .temp/gtdb-species-status-20261115/yljm2c-run-terms-001/native.log
  accessed_at: '2026-11-15T06:33:25.585735Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000554-paper
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/42364169/
  locator: Results, retained main-text offset 22937; Data availability offset 50466
  support: supports
  summary: The inspected paper reports approximately 97% ANI between YL-JM2C and R.
    wittichii RW1 and identifies the complete study-stock assembly by BioProject PRJNA1397584.
    This supports the paper's species identification, not an independent GTDB classification
    of that stock.
  accessed_at: '2026-11-15T06:33:25.585735Z'
- evidence_id: 000554-database
  kind: database
  reference: reports/gtdb-species-status-20261115/yljm2c-source-evidence-001.json
  locator: occurrences[0].ncbi_identity_rows/crosswalk_exact_rows/native_result
  support: supports
  summary: The local authority labels NCBITaxon:160791 Rhizorhabdus wittichii at species
    rank. Exact pinned crosswalk row 7583 reports seven genomes and fraction 0.86,
    and the native ncbi_id resolver reproduces GTDB:s__Rhizorhabdus_wittichii. No
    exact YL-JM2C assembly membership or numerator is inferred.
  accessed_at: '2026-11-15T06:33:25.585735Z'
- evidence_id: 000554-application
  kind: record_content
  reference: .temp/gtdb-species-status-20261115/yljm2c-applied-m5-001/receipt.json
  locator: applied/before_sha256/after_sha256/inputs
  support: supports
  summary: The actual guarded M5 application persisted only the accepted block, status
    and two native inline events. The native append-only sidecar and all eight current
    gate receipts are retained and bound.
  accessed_at: '2026-11-15T06:33:25.585735Z'
- evidence_id: 000554-prior
  kind: prior_review
  reference: reports/causal_graph_review/decisions/20261110-stage2-seven-records-batch147.yaml
  locator: records[id=CommunityMech:000554] and immutable c15s4 deep audit
  support: context_only
  summary: Original scientific assertions and the unresolved RwTfdB structural-determinants
    question remain historical evidence. The isolated baseline retains one community-level
    node and no inferred consortium cross-feeding arrow; no mechanism claim was changed
    by this database correction.
  accessed_at: '2026-11-15T06:33:25.585735Z'
assessments:
- assessment_id: 000554-identity
  area: grounding
  topic: Source stock and species authority boundary
  outcome: supported
  target_ids:
  - CommunityMech:000554
  evidence_ids:
  - 000554-paper
  - 000554-database
  - 000554-terms
  summary: Preserve stock YL-JM2C, the source's ANI-based species assignment, BioProject
    and unchanged NCBITaxon species identity. The new GTDB block represents that species-reference
    correspondence, not a separately verified genome classification of YL-JM2C.
- assessment_id: 000554-population
  area: grounding
  topic: Exact native species-reference population and name comparison
  outcome: supported
  target_ids:
  - CommunityMech:000554
  evidence_ids:
  - 000554-database
  - 000554-gtdb
  - 000554-domain
  summary: Retain native total_genomes 7 and majority_fraction 0.86 from the exact
    species-ID row, without deriving a support numerator or equating reference genomes
    with study stocks. Native is_reclassified:false records agreement of the current
    species names, without denying the paper's earlier stock reassignment.
- assessment_id: 000554-provenance
  area: provenance
  topic: Actual bounded application and unchanged scientific uncertainty
  outcome: supported
  target_ids:
  - CommunityMech:000554
  evidence_ids:
  - 000554-application
  - 000554-schema
  - 000554-strict
  - 000554-scalars
  - 000554-new-history
  - 000554-history
  - 000554-prior
  summary: The current record equals the approved candidate after a native validated
    guarded write. Eight required commands and one new native history sidecar persisted.
    Existing stock names, source quotations, ecological graph, RwTfdB discussion and
    prior history are unchanged. Separate strict batch147 successor and combined generated
    pages/QC remain integration work.
findings: []
actions: []
limitations:
- Scoped technical/provenance assessment with scientific_review:false; no full scientific
  record approval or corpus QC completion.
- The seven-genome crosswalk population is keyed to species NCBITaxon:160791, not
  stock YL-JM2C or BioProject PRJNA1397584. Membership of that stock in the GTDB species
  cluster was not independently established. The rounded fraction 0.86 is retained
  without inventing a support-genome numerator.
- Local NCBI label/rank query output is retained; the complete SQLite database and
  release were not hash-certified. Exact source cache, crosswalk and resolver bytes
  are bound separately.
- The source's earlier Sphingomonas-to-Rhizorhabdus stock reassignment is preserved.
  Native is_reclassified:false only compares current canonical and GTDB names.
- The open RwTfdB structural-determinants discussion and all prior biological claims
  remain unchanged; this diagnostic does not answer that scientific question.
- Seven native scoped validators plus native history scaffolding passed. Source-snippet
  matching, generated pages, the strict historical successor integration and final
  combined full QC remain separately accounted work.
links:
- https://github.com/CultureBotAI/CommunityMech/issues/2848
- https://github.com/CultureBotAI/CommunityMech/pull/2862
```
