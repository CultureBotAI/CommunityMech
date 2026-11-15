# PES N7/A11 genus-reference correspondences: scoped M5 diagnostic

- Review: 20261115T070439Z-pes-two-genus-reference-diagnostic
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-11-15T07:04:39.513225Z
- Finished UTC: 2026-11-15T07:04:39.627818Z
- Reviewer: codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: false

## Summary

The unchanged Pelagerythrobacter N7 and Salinicola A11 genus identities now carry their native GTDB genus-reference correspondences, with filtered reference populations 16/16 and 46/46. These are database correspondences for the declared genera, not exact species or assembly placements of the study stocks. The actual M5 application preserved all other scientific content and prior history, appended native provenance, and passed eight scoped commands.

## Scope And Provenance

Two declared taxonomy genus-reference blocks, statuses, exact source/authority bindings and actual provenance in one PES record. Existing experimental, ecological and mechanism assertions are preserved without new full scientific clearance.

Selection: One whole record, CommunityMech:000340, selected as the first community record using the shared higher-rank source-binding/application/check/review path. Prior isolated N7 and A11 canaries are separate evidence; the prepared three-record group has not been canonically applied.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 23d84a2d5567559a9693303c3ac9c07ff498e037.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000340 | kb/communities/Pelagerythrobacter_Salinicola_PES_Pyrene_Degradation_SynCom.yaml # taxonomy[0:2].taxon_term.gtdb_classification; gtdb_grounding_status | maintained | PES N7/A11 genus correspondences with study-stock limits retained |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000340 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-strict | passed | True | CommunityMech:000340 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-gtdb | passed | True | CommunityMech:000340 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-gtdb-domain | passed | True | CommunityMech:000340 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-scalars | passed | True | CommunityMech:000340 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-history | passed | True | CommunityMech:000340 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| new-history | passed | True | CommunityMech:000340 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-terms | passed | True | CommunityMech:000340 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |

## Scientific And Domain Assessments

### Source genus and exact study-stock boundary

grounding: supported. Targets: CommunityMech:000340.

The two declared genera and stock names remain unchanged and source-compatible. The added database correspondences do not select an exact N7/A11 species, strain taxon or reference genome.

### Native higher-rank correspondence and filtered reference population

grounding: supported. Targets: CommunityMech:000340.

The exact native crosswalk route supports GTDB:g__Pelagerythrobacter from 16/16 and GTDB:g__Salinicola from 46/46 named-binomial reference genomes, each with one genus outcome. Native names and lineages pass scoped coherence/domain checks without any species or stock-genome inference.

### Exact bounded application and unchanged original scientific projection

provenance: supported. Targets: CommunityMech:000340.

The canonical M5 bytes equal the accepted candidate. Native history persistence and seven scoped validators passed, with 34-byte strict output and zero error rows. Full old biology, source quotations, hypotheses and history are preserved. The separate historical-admission and generated-page integration will consume this immutable technical proof without replacing the prior scientific ledger.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| 000340-schema | .temp/gtdb-code006-20261115/pes-run-schema-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000340-strict | .temp/gtdb-code006-20261115/pes-run-strict-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000340-gtdb | .temp/gtdb-code006-20261115/pes-run-gtdb-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000340-domain | .temp/gtdb-code006-20261115/pes-run-domain-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000340-scalars | .temp/gtdb-code006-20261115/pes-run-scalars-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000340-history | .temp/gtdb-code006-20261115/pes-run-history-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000340-new-history | .temp/gtdb-code006-20261115/pes-run-new-history-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000340-terms | .temp/gtdb-code006-20261115/pes-run-terms-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000340-paper | https://pubmed.ncbi.nlm.nih.gov/42666409/; Section 3.1 Composition and genome sequencing, retained character offsets 31010 and 31215; source-binding primary_contexts | supports | The inspected primary passages place N7 in Pelagerythrobacter and A11 in Salinicola. Existing notes explicitly withhold exact strain taxa. This supports the two existing genus names without resolving study-stock species or reference-assembly membership. |
| 000340-database | reports/gtdb-code006-20261115/pes-source-evidence-001.json; occurrences[0:2].ncbi_identity_rows/native_result/population_scope; source_inputs and retained full native report | supports | Read-only local authority queries preserve the exact NCBI labels and genus rank. The pinned native route yields Pelagerythrobacter 16/16 and Salinicola 46/46 at genus rank; complete original lookup rows are retained in the bound report. The reference denominator is distinct from study-stock identity. |
| 000340-application | .temp/gtdb-code006-20261115/pes-applied-m5-001/receipt.json; applied/before_sha256/after_sha256/inputs | supports | The actual M5 guarded write persisted the exact independently accepted candidate, consisting only of two native genus blocks, statuses and substantive inline history events. The appended native sidecar binds this exact receipt and all eight gate artifacts are retained. |
| 000340-prior | reports/causal_graph_review/decisions/20261007-four-records-batch83.yaml; records[id=CommunityMech:000340], node/edge decisions and record hash; original 2026-10-07 inline history | context_only | Preserve the prior distinctions between candidate enzyme/handoff mechanisms and measured removal, soybean-oil emulsification and pyrene mass transfer, and removal and mineralization. The old ledger and full preexisting scientific/history projection remain unchanged; no previous scientific finding is closed. |

## Limits And Additional Notes

- Partial technical and provenance assessment with scientific_review:false. It does not complete a full scientific record review, the outstanding taxonomy repair campaign or corpus QC.
- The native 16/16 and 46/46 denominators count named-binomial reference genomes retained by the exact 761d5537 crosswalk algorithm at genus rank. They do not count study stocks or establish that N7 or A11 is represented by an assembly in the crosswalk.
- The primary genus/stock anchors and local NCBI label/rank evidence were inspected; no new complete paper, supplement, figure, sequence or assembly audit was performed. The local NCBI database was stat-bound, not fully hash-certified or assigned a release.
- Primary/source binding and private candidate staging used local Python 3.13.12; actual guarded application and the eight commands used M5 Python 3.13.2 at the same 23d84a2d code revision. The earlier native route report explicitly retains its 52c740b6 execution revision. No clean-tree claim is made for gates after the approved canonical application.
- The mapping_source date records the mapping file's mtime only, not a GTDB or NCBI release. Native is_reclassified:false compares current genus names and does not independently reconstruct nomenclatural history.
- The hphtC-5 enzyme assignment, intermember intermediate transfer, emulsifier contribution and reciprocal fitness remain qualified/open. Pyrene removal remains distinct from carbon mineralization; no biological assertion or prior scientific decision was changed.
- Native term validation reported Validation passed without an assertion denominator. Source-snippet matching, affected-page generation, strict historical successor admission and final combined QC are separate work, not implied by these eight successful commands.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261115T070439Z-pes-two-genus-reference-diagnostic
kind: record
repository: CultureBotAI/CommunityMech
title: 'PES N7/A11 genus-reference correspondences: scoped M5 diagnostic'
started_at: '2026-11-15T07:04:39.513225Z'
finished_at: '2026-11-15T07:04:39.627818Z'
reviewer:
  identity: codex
  kind: agent
  independence: self_review
  independence_basis: Parent independently inspected the retained primary Section
    3.1 anchors, exact stock notes, native route report, authored source config and
    candidate hashes before application. The shared binder, writer, check runner and
    diagnostic builder received separate read-only reviews and meaningful controls.
    This authored technical assessment is self-review of the resulting bounded correction.
skill: curate-yaml-record
completion: completed
verdict: pass_with_limitations
scientific_review: false
summary: The unchanged Pelagerythrobacter N7 and Salinicola A11 genus identities now
  carry their native GTDB genus-reference correspondences, with filtered reference
  populations 16/16 and 46/46. These are database correspondences for the declared
  genera, not exact species or assembly placements of the study stocks. The actual
  M5 application preserved all other scientific content and prior history, appended
  native provenance, and passed eight scoped commands.
source:
  git_revision: 23d84a2d5567559a9693303c3ac9c07ff498e037
  state: working_tree
  inputs:
  - path: .temp/gtdb-code006-20261115/kg-microbe/data/raw/NCBI2GTDB.tsv.gz
    sha256: 761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd
    role: context
  - path: .temp/gtdb-code006-20261115/pes-applied-m5-001/before.yaml
    sha256: c3ce655c53db89daeab6cf8ee8ca02ab7eb3bf597d6fe0dd7171ba33194dde1a
    role: context
  - path: .temp/gtdb-code006-20261115/pes-applied-m5-001/receipt.json
    sha256: 2ac04267b5ba42570c80984291b370d4c5f33dff22867d464e0d17ea632ce07f
    role: context
  - path: .temp/gtdb-code006-20261115/pes-candidate-001/Pelagerythrobacter_Salinicola_PES_Pyrene_Degradation_SynCom.yaml
    sha256: fd80ffd72ba9e2e1909a4d1f165d642af2dda9e5f04e91128a63a7903fef27b8
    role: context
  - path: .temp/gtdb-code006-20261115/pes-candidate-001/receipt.json
    sha256: fa8231b80ddc3679f23d5ec380b004fcf2bfaef75311b982c185f094c672ba70
    role: context
  - path: .temp/gtdb-code006-20261115/pes-check-config-002.json
    sha256: 0a6efba41cdbe6941d85b7060e12c6f259a553f95a33500639f3b45df669da43
    role: context
  - path: .temp/gtdb-code006-20261115/pes-route-plan-001.json
    sha256: 388f7e2053c3ce3fad7a5b27e0471498c7f72925b9015e9404e53ba3c72a14ad
    role: context
  - path: .temp/gtdb-code006-20261115/pes-run-domain-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/pes-run-domain-001/native.log
    sha256: 214f1596c28ef68974ef2134a82605e87be1a09543b3ed4b3877983ecae37fac
    role: context
  - path: .temp/gtdb-code006-20261115/pes-run-domain-001/receipt.json
    sha256: 0c455e473ae98f9145e4ed4a077ba6e5f757051ee031fc53d3746bc12b72dbc5
    role: context
  - path: .temp/gtdb-code006-20261115/pes-run-domain-001/start.json
    sha256: 077e9f3c319b88b8860e1bdd74194feed6ad8ee1f8bd217f4857187e9da3af22
    role: context
  - path: .temp/gtdb-code006-20261115/pes-run-gtdb-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/pes-run-gtdb-001/native.log
    sha256: e61ee21c2076d12afd5ff975b428227e4f0c59a1f87438150201fce1d7c92205
    role: context
  - path: .temp/gtdb-code006-20261115/pes-run-gtdb-001/receipt.json
    sha256: f833788ddd4fb5046958d017fe3d5a5f80c5249e48d26d89971ac37eedc69be5
    role: context
  - path: .temp/gtdb-code006-20261115/pes-run-gtdb-001/start.json
    sha256: d283099650ce2d7b90a6044a0789a0a10d6688abac7a3ef711978297d27481db
    role: context
  - path: .temp/gtdb-code006-20261115/pes-run-history-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/pes-run-history-001/native.log
    sha256: 700b44227c4cf01270ac26f16b308622de0b26f48d71aec49cdfaaab87620f0a
    role: context
  - path: .temp/gtdb-code006-20261115/pes-run-history-001/receipt.json
    sha256: 6d8a27eb941480a53abad4f0cc1b1b558b3bfbe07e2865e39f35353140802f29
    role: context
  - path: .temp/gtdb-code006-20261115/pes-run-history-001/start.json
    sha256: 5cefa0f75b3d05e51637d4b0562f20253aeb78109181b8f313178d09a0bd371b
    role: context
  - path: .temp/gtdb-code006-20261115/pes-run-new-history-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/pes-run-new-history-001/native.log
    sha256: 2dc10f62b4c042d30aecf8760db3e418e0078cfb6eba4751bbc61ca40a9ea2c0
    role: context
  - path: .temp/gtdb-code006-20261115/pes-run-new-history-001/receipt.json
    sha256: 403ff5da0e0437417e88726baa603505e0ea8c5b6c807043d7158d567e493a7b
    role: context
  - path: .temp/gtdb-code006-20261115/pes-run-new-history-001/start.json
    sha256: 4d2fe70789fa2507f57634542daf49d2d9453a89d7d5ba2d78a499b64ecb0a39
    role: context
  - path: .temp/gtdb-code006-20261115/pes-run-scalars-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/pes-run-scalars-001/native.log
    sha256: 9e81f5404ea711ea67ee37f8e8947a651114283c628396222dc15e278dd125d1
    role: context
  - path: .temp/gtdb-code006-20261115/pes-run-scalars-001/receipt.json
    sha256: 4a56bb4044e6e9fdda188e8e9ccf1950167af553fbb26bf69149a51c2824aed1
    role: context
  - path: .temp/gtdb-code006-20261115/pes-run-scalars-001/start.json
    sha256: 93f5f7361c5d2023f0828560d5c01056f7495aad51116640f284726562b9cf82
    role: context
  - path: .temp/gtdb-code006-20261115/pes-run-schema-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/pes-run-schema-001/native.log
    sha256: 01f2a7fd90177de0231dc2ec0de09bdbf7d04c3577feba94e0cdcddc9461f518
    role: context
  - path: .temp/gtdb-code006-20261115/pes-run-schema-001/receipt.json
    sha256: 3075cb8b19a0146003a02552e5f96e43c863e453fd99cef845cd6f3a6512080c
    role: context
  - path: .temp/gtdb-code006-20261115/pes-run-schema-001/start.json
    sha256: c988099297015b68ebf82471870337a1ca24548f7ef03101fa5d2245ed66901a
    role: context
  - path: .temp/gtdb-code006-20261115/pes-run-strict-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/pes-run-strict-001/native.log
    sha256: ef73dc855a47c536f7a0e8967464de24713adb21eed07a904f58e841bf352534
    role: context
  - path: .temp/gtdb-code006-20261115/pes-run-strict-001/receipt.json
    sha256: e1c9612f0c4d9059f9325ae5c882714c1949aeedf40094043930dad4528c91c9
    role: context
  - path: .temp/gtdb-code006-20261115/pes-run-strict-001/start.json
    sha256: e45bc10d36be239dbd69b18a051437dec18d5e646c552e06f2286a07bd3ed217
    role: context
  - path: .temp/gtdb-code006-20261115/pes-run-strict-001/strict.tsv
    sha256: b184ed5450b968070bb6c75648407e388f41a1eaf7017890723cf560999fc3f7
    role: context
  - path: .temp/gtdb-code006-20261115/pes-run-terms-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/pes-run-terms-001/native.log
    sha256: 2993e0ffe2b4b131f62cccaffbaef9111ca7e6efeea4ea4fa6e72cc2cd94b156
    role: context
  - path: .temp/gtdb-code006-20261115/pes-run-terms-001/receipt.json
    sha256: 1f68592723b902dab35d54b9aa296ead0a9a8c29b9bf108126ddbd8888b311b8
    role: context
  - path: .temp/gtdb-code006-20261115/pes-run-terms-001/start.json
    sha256: 129113f2e9583c63db890d330ca9475e0ce422147a39686970c4222a9d0845cb
    role: context
  - path: .temp/gtdb-code006-20261115/pes-source-assessment-plan-001.json
    sha256: dcd8cf3150753b79412950edf045d38b65a56bf1cf693fb6226de303a0184f32
    role: context
  - path: .temp/phase2-schema-20261115/pes-bound-source-001.log
    sha256: 2f22f0a2525a7a4475517e8a42d3008b147ea67952e36740fe795365e2e0bad5
    role: context
  - path: .temp/phase2-schema-20261115/pes-shared-route-002.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/phase2-schema-20261115/pes-shared-route-002.json
    sha256: ac0b81f4e01d11e27bc71e711a6072f324b75f319412507e0cc8548abc32c81d
    role: context
  - path: .temp/phase2-schema-20261115/pes-shared-route-002.log
    sha256: b29b7054a1b0f3ea6539c5e6183f62cd5a48dd80930f071c689b84204c3313b7
    role: context
  - path: history/records/Pelagerythrobacter_Salinicola_PES_Pyrene_Degradation_SynCom/2026-09-11T090554Z-claude-code-13a040.yaml
    sha256: 8c49b3f3c33eb4ffa7b3c7094f463abe56f6aabe9081e092d0d110ca4fb61046
    role: context
  - path: history/records/Pelagerythrobacter_Salinicola_PES_Pyrene_Degradation_SynCom/2026-10-07T074131Z-codex-d4a2ed.yaml
    sha256: 8b65d88b77e366da0e00160cc606ed0b54bac4e7d48d39067e448ac4a74e7f87
    role: context
  - path: history/records/Pelagerythrobacter_Salinicola_PES_Pyrene_Degradation_SynCom/2026-11-15T070055Z-codex-290a0e.yaml
    sha256: ea435cd905ffa88409944288374300f91742abf58db73678e53897d7911387e5
    role: context
  - path: justfile
    sha256: 40369611ad4531582e420df0e9ff22109e4b18adf03b34d86b54200b280f2d0f
    role: context
  - path: kb/communities/Pelagerythrobacter_Salinicola_PES_Pyrene_Degradation_SynCom.yaml
    sha256: fd80ffd72ba9e2e1909a4d1f165d642af2dda9e5f04e91128a63a7903fef27b8
    role: target
  - path: pyproject.toml
    sha256: be952f0f137f85fed66bda0908f12014f1797a2dd229b44d832afc0c00471655
    role: context
  - path: references_cache/PMID_42666409.txt
    sha256: 3442799f20b033c3a010c14a4f32c4be15485fb0a501aed059921a5006cbe698
    role: context
  - path: reports/causal_graph_review/decisions/20261007-four-records-batch83.yaml
    sha256: e13924aca3b858e78dcfa2074352e5a9a381bba97a83b2b94b8e864419dd9efe
    role: context
  - path: reports/gtdb-code006-20261115/pes-review-config-001.json
    sha256: 3becece01f1944fee843c7d60a7087dc28b9ecc799cb382104dbab0907c77ff8
    role: context
  - path: reports/gtdb-code006-20261115/pes-source-config-001.json
    sha256: 7f5c4af8682911582c15b4e4417f26172bcca3474b748b0132a0a7bee9eebbfb
    role: context
  - path: reports/gtdb-code006-20261115/pes-source-evidence-001.json
    sha256: dab5b6d77ec9ba3145c9adb38a8cb61ab173c226954fb8a92ecb28b12a6d1c55
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/adhoc/bind_gtdb_batch_source_context_20261115.py
    sha256: 6cdeb82122c130cd5b2e7e73bbe66bc5123fc951892f9f87edb589fb4929aac3
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
  - path: scripts/adhoc/report_gtdb_batch_routes_20261115.py
    sha256: 2d4732edafccba24741b728b9e672ca7fada5e50d8220162a9ccf3c5d8d875ef
    role: context
  - path: scripts/gtdb_ground.py
    sha256: 0fc1ba926a56e5be85cdf064db0cf56452aeeee93f15b0ced98e8f11b5296175
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: src/communitymech/__init__.py
    sha256: c003d906fef500e765c59c8f15ee821054e26c43e59a1be70dbc23c33f8aae66
    role: context
  - path: src/communitymech/curate/__init__.py
    sha256: a591b57cbf73ef2ddb0da6d0b7be0dd784258115ae20cf4883f6f379bcad9324
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
  - path: src/communitymech/validators/__init__.py
    sha256: 975d33a39c8e7173d25aa0de711f25a19158228ecfd837908c829b3f9f14cf93
    role: context
  - path: src/communitymech/validators/ncbi_domain.py
    sha256: b1e7ffc3c35c237e36c2c19fab42f1d42a14161397de9c5e726ed85897f1e262
    role: context
  - path: tests/test_causal_review_batch83.py
    sha256: 87f8c8edf2a8cdb81a55501765c0eac166fe7d2f61c70dbc902ea941067410eb
    role: context
  - path: uv.lock
    sha256: 712838f8fa3d68fbd818ac8162f3f1e2f2637db1da1a8ebfaba0ef759690f3b4
    role: context
targets:
- target_id: CommunityMech:000340
  path: kb/communities/Pelagerythrobacter_Salinicola_PES_Pyrene_Degradation_SynCom.yaml
  selector: taxonomy[0:2].taxon_term.gtdb_classification; gtdb_grounding_status
  label: PES N7/A11 genus correspondences with study-stock limits retained
  kind: maintained
  ownership_note: CommunityMech owns this record; only declared GTDB correspondence/status
    and actual provenance are assessed.
scope:
  description: Two declared taxonomy genus-reference blocks, statuses, exact source/authority
    bindings and actual provenance in one PES record. Existing experimental, ecological
    and mechanism assertions are preserved without new full scientific clearance.
  selection: One whole record, CommunityMech:000340, selected as the first community
    record using the shared higher-rank source-binding/application/check/review path.
    Prior isolated N7 and A11 canaries are separate evidence; the prepared three-record
    group has not been canonically applied.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000340
  exclusions:
  - target: Other scientific claims and records
    reason: Existing biology is preserved, not newly certified by this database diagnostic.
checks:
- check_id: 000340-schema
  name: validate
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000340
  command: just --verbose --no-dotenv --color never validate kb/communities/Pelagerythrobacter_Salinicola_PES_Pyrene_Degradation_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000340-schema
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000340-strict
  name: validate-strict
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000340
  command: just --verbose --no-dotenv --color never validate-strict kb/communities/Pelagerythrobacter_Salinicola_PES_Pyrene_Degradation_SynCom.yaml
    --out .temp/gtdb-code006-20261115/pes-run-strict-001/strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000340-strict
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000340-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000340
  command: just --verbose --no-dotenv --color never validate-gtdb kb/communities/Pelagerythrobacter_Salinicola_PES_Pyrene_Degradation_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000340-gtdb
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000340-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000340
  command: just --verbose --no-dotenv --color never validate-gtdb-domain kb/communities/Pelagerythrobacter_Salinicola_PES_Pyrene_Degradation_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000340-domain
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000340-scalars
  name: validate-scalars
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000340
  command: just --verbose --no-dotenv --color never validate-scalars kb/communities/Pelagerythrobacter_Salinicola_PES_Pyrene_Degradation_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000340-scalars
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000340-history
  name: validate-history
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000340
  command: just --verbose --no-dotenv --color never validate-history history/records/Pelagerythrobacter_Salinicola_PES_Pyrene_Degradation_SynCom
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000340-history
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000340-new-history
  name: new-history
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000340
  command: just --verbose --no-dotenv --color never new-history --kind record --slug
    Pelagerythrobacter_Salinicola_PES_Pyrene_Degradation_SynCom --target-root kb/communities
    --event EDIT --outcome changed --sections taxonomy,curation_history --actor-name
    codex --model gpt-6 --agent-tool codex --issue https://github.com/CultureBotAI/CommunityMech/issues/2848
    --summary 'Add source-bound genus-reference correspondences for the two PES taxa'
    --details 'The guarded native application adds Pelagerythrobacter and Salinicola
    genus correspondences from exact crosswalk 761d5537, with native named-binomial
    reference populations 16/16 and 46/46, grounding statuses and two substantive
    inline events. Preserve N7 and A11 study-stock notes, exact species/genome uncertainty,
    all source quotations, experimental claims, causal qualifications and original
    history. This is a scoped database correspondence correction, not a new full scientific
    review or resolution of hphtC-5 and emulsifier-mechanism gaps. Local source binding
    and candidate staging occurred at 23d84a2d; actual application occurred on isolated
    M5 at the same code revision. Actual apply receipt .temp/gtdb-code006-20261115/pes-applied-m5-001/receipt.json
    sha256:2ac04267b5ba42570c80984291b370d4c5f33dff22867d464e0d17ea632ce07f.'
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000340-new-history
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000340-terms
  name: validate-terms
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000340
  command: just --verbose --no-dotenv --color never validate-terms kb/communities/Pelagerythrobacter_Salinicola_PES_Pyrene_Degradation_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000340-terms
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
evidence:
- evidence_id: 000340-schema
  kind: validation
  reference: .temp/gtdb-code006-20261115/pes-run-schema-001/native.log
  accessed_at: '2026-11-15T07:04:39.513225Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000340-strict
  kind: validation
  reference: .temp/gtdb-code006-20261115/pes-run-strict-001/native.log
  accessed_at: '2026-11-15T07:04:39.513225Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000340-gtdb
  kind: validation
  reference: .temp/gtdb-code006-20261115/pes-run-gtdb-001/native.log
  accessed_at: '2026-11-15T07:04:39.513225Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000340-domain
  kind: validation
  reference: .temp/gtdb-code006-20261115/pes-run-domain-001/native.log
  accessed_at: '2026-11-15T07:04:39.513225Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000340-scalars
  kind: validation
  reference: .temp/gtdb-code006-20261115/pes-run-scalars-001/native.log
  accessed_at: '2026-11-15T07:04:39.513225Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000340-history
  kind: validation
  reference: .temp/gtdb-code006-20261115/pes-run-history-001/native.log
  accessed_at: '2026-11-15T07:04:39.513225Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000340-new-history
  kind: validation
  reference: .temp/gtdb-code006-20261115/pes-run-new-history-001/native.log
  accessed_at: '2026-11-15T07:04:39.513225Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000340-terms
  kind: validation
  reference: .temp/gtdb-code006-20261115/pes-run-terms-001/native.log
  accessed_at: '2026-11-15T07:04:39.513225Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000340-paper
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/42666409/
  locator: Section 3.1 Composition and genome sequencing, retained character offsets
    31010 and 31215; source-binding primary_contexts
  support: supports
  summary: The inspected primary passages place N7 in Pelagerythrobacter and A11 in
    Salinicola. Existing notes explicitly withhold exact strain taxa. This supports
    the two existing genus names without resolving study-stock species or reference-assembly
    membership.
  accessed_at: '2026-11-15T07:04:39.513225Z'
- evidence_id: 000340-database
  kind: database
  reference: reports/gtdb-code006-20261115/pes-source-evidence-001.json
  locator: occurrences[0:2].ncbi_identity_rows/native_result/population_scope; source_inputs
    and retained full native report
  support: supports
  summary: Read-only local authority queries preserve the exact NCBI labels and genus
    rank. The pinned native route yields Pelagerythrobacter 16/16 and Salinicola 46/46
    at genus rank; complete original lookup rows are retained in the bound report.
    The reference denominator is distinct from study-stock identity.
  accessed_at: '2026-11-15T07:04:39.513225Z'
- evidence_id: 000340-application
  kind: record_content
  reference: .temp/gtdb-code006-20261115/pes-applied-m5-001/receipt.json
  locator: applied/before_sha256/after_sha256/inputs
  support: supports
  summary: The actual M5 guarded write persisted the exact independently accepted
    candidate, consisting only of two native genus blocks, statuses and substantive
    inline history events. The appended native sidecar binds this exact receipt and
    all eight gate artifacts are retained.
  accessed_at: '2026-11-15T07:04:39.513225Z'
- evidence_id: 000340-prior
  kind: prior_review
  reference: reports/causal_graph_review/decisions/20261007-four-records-batch83.yaml
  locator: records[id=CommunityMech:000340], node/edge decisions and record hash;
    original 2026-10-07 inline history
  support: context_only
  summary: Preserve the prior distinctions between candidate enzyme/handoff mechanisms
    and measured removal, soybean-oil emulsification and pyrene mass transfer, and
    removal and mineralization. The old ledger and full preexisting scientific/history
    projection remain unchanged; no previous scientific finding is closed.
  accessed_at: '2026-11-15T07:04:39.513225Z'
assessments:
- assessment_id: 000340-identity
  area: grounding
  topic: Source genus and exact study-stock boundary
  outcome: supported
  target_ids:
  - CommunityMech:000340
  evidence_ids:
  - 000340-paper
  - 000340-database
  - 000340-terms
  summary: The two declared genera and stock names remain unchanged and source-compatible.
    The added database correspondences do not select an exact N7/A11 species, strain
    taxon or reference genome.
- assessment_id: 000340-population
  area: grounding
  topic: Native higher-rank correspondence and filtered reference population
  outcome: supported
  target_ids:
  - CommunityMech:000340
  evidence_ids:
  - 000340-database
  - 000340-gtdb
  - 000340-domain
  summary: The exact native crosswalk route supports GTDB:g__Pelagerythrobacter from
    16/16 and GTDB:g__Salinicola from 46/46 named-binomial reference genomes, each
    with one genus outcome. Native names and lineages pass scoped coherence/domain
    checks without any species or stock-genome inference.
- assessment_id: 000340-provenance
  area: provenance
  topic: Exact bounded application and unchanged original scientific projection
  outcome: supported
  target_ids:
  - CommunityMech:000340
  evidence_ids:
  - 000340-application
  - 000340-schema
  - 000340-strict
  - 000340-scalars
  - 000340-new-history
  - 000340-history
  - 000340-prior
  summary: The canonical M5 bytes equal the accepted candidate. Native history persistence
    and seven scoped validators passed, with 34-byte strict output and zero error
    rows. Full old biology, source quotations, hypotheses and history are preserved.
    The separate historical-admission and generated-page integration will consume
    this immutable technical proof without replacing the prior scientific ledger.
findings: []
actions: []
limitations:
- Partial technical and provenance assessment with scientific_review:false. It does
  not complete a full scientific record review, the outstanding taxonomy repair campaign
  or corpus QC.
- The native 16/16 and 46/46 denominators count named-binomial reference genomes retained
  by the exact 761d5537 crosswalk algorithm at genus rank. They do not count study
  stocks or establish that N7 or A11 is represented by an assembly in the crosswalk.
- The primary genus/stock anchors and local NCBI label/rank evidence were inspected;
  no new complete paper, supplement, figure, sequence or assembly audit was performed.
  The local NCBI database was stat-bound, not fully hash-certified or assigned a release.
- Primary/source binding and private candidate staging used local Python 3.13.12;
  actual guarded application and the eight commands used M5 Python 3.13.2 at the same
  23d84a2d code revision. The earlier native route report explicitly retains its 52c740b6
  execution revision. No clean-tree claim is made for gates after the approved canonical
  application.
- The mapping_source date records the mapping file's mtime only, not a GTDB or NCBI
  release. Native is_reclassified:false compares current genus names and does not
  independently reconstruct nomenclatural history.
- The hphtC-5 enzyme assignment, intermember intermediate transfer, emulsifier contribution
  and reciprocal fitness remain qualified/open. Pyrene removal remains distinct from
  carbon mineralization; no biological assertion or prior scientific decision was
  changed.
- Native term validation reported Validation passed without an assertion denominator.
  Source-snippet matching, affected-page generation, strict historical successor admission
  and final combined QC are separate work, not implied by these eight successful commands.
links:
- https://github.com/CultureBotAI/CommunityMech/issues/2848
- https://github.com/CultureBotAI/CommunityMech/issues/1685
- https://github.com/CultureBotAI/CommunityMech/pull/2853
```
