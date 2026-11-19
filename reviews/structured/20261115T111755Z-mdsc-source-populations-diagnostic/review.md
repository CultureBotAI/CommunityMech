# MDSC reference correspondences with distinct R232 populations and study stocks preserved

- Review: 20261115T111755Z-mdsc-source-populations-diagnostic
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-11-15T11:17:55.383926Z
- Finished UTC: 2026-11-15T11:17:55.542984Z
- Reviewer: codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: false

## Summary

Two actual guarded M5 transitions correct the Faecalibacterium duncaniae and Desulfovibrio piger population notes, then store their native reference correspondences. Exact-ID411483 yields5099 genomes/fraction1.0; the species-name901 route yields156/fraction1.0 with no exact901 row. These separate populations do not identify DSM17677T or DSM749T genomes and do not replace the independently inspected R232 worksheet populations. Both corrected notes, fourteen members, four manual R232 blocks and all biology remain preserved.

## Scope And Provenance

CommunityMech:000392 taxonomy[10/13] source notes and GTDB descriptor fields, actual two-transition provenance, primary stock/population boundaries and final-byte native checks. Partial technical/source-provenance assessment; not whole-record scientific review.

Selection: One source-held whole record. Original4ef59255 became note-only07e623ed through actual note execution71e2. Real maintained ROOT0794bf80ebd15a073dc2103cfd1ed0c5234e6d74 contains that exact intermediate. A separate M5 checkout atf4e10146a77ebb0b5e697abc56d9683becfaaf5d applied final native mapping5beb7303 and ran eight final-byte native checks.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f4e10146a77ebb0b5e697abc56d9683becfaaf5d.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000392 | kb/communities/Mucin_Glycan_MDSC_Synthetic_Gut_Community.yaml # taxonomy[10].taxon_term.notes; taxonomy[10].taxon_term.gtdb_classification; taxonomy[10].taxon_term.gtdb_grounding_status; taxonomy[13].taxon_term.notes; taxonomy[13].taxon_term.gtdb_classification; taxonomy[13].taxon_term.gtdb_grounding_status; taxonomy[13].taxon_term.gtdb_candidates | maintained | Two reference correspondences with source-stock and population distinctions preserved |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000392 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-strict | passed | True | CommunityMech:000392 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-gtdb | passed | True | CommunityMech:000392 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-gtdb-domain | passed | True | CommunityMech:000392 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-scalars | passed | True | CommunityMech:000392 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-history | passed | True | CommunityMech:000392 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| new-history | passed | True | CommunityMech:000392 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-terms | passed | True | CommunityMech:000392 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |

## Scientific And Domain Assessments

### Named study stocks remain separate from descriptor populations

grounding: supported. Targets: CommunityMech:000392.

DSM17677T and DSM749T, all fourteen members and existing culture/type-strain assertions remain unchanged. The reference routes do not independently identify experimental assemblies, establish stock-level GTDB classification, quantify community abundance or rename study members.

### Corrected notes retain the distinct native and official R232 populations

grounding: supported. Targets: CommunityMech:000392.

The no-majority and absence claims were replaced by exact population distinctions. Native5099/1 and156/1 remain separate from R23276/six,948/57 and five GTDB-column mentions. The R232 unnamed majority is not a stock assignment, and no exact current-name NCBI row does not mean the GTDB species is absent. Crosswalk release order remains unestablished.

### Two native blocks and GROUNDED descriptor statuses

grounding: supported. Targets: CommunityMech:000392.

Taxonomy[10] stores the exact-ID F.duncaniae5099/1 result; taxonomy[13] stores the name-route D.piger156/1 result and removes its old six alternatives. GROUNDED describes the encoded reference correspondence, not a verified experimental stock genome. Both corrected notes and four unselected manual blocks remain exact.

### Actual note and mapping transitions with final-byte native checks

provenance: supported. Targets: CommunityMech:000392.

Both actual application inputs and sidecars are captured. Eight final-byte native commands passed separately from the note-only checks. Real maintained0794 is distinct from actual finalf4e execution. Composite historical admission, generated products and combined QC remain subsequent integration work, with all prior biological findings and immutable history preserved.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| 000392-schema | .temp/gtdb-source-holds-20261115/mdsc392-mapping-schema-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000392-strict | .temp/gtdb-source-holds-20261115/mdsc392-mapping-strict-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000392-gtdb | .temp/gtdb-source-holds-20261115/mdsc392-mapping-gtdb-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000392-domain | .temp/gtdb-source-holds-20261115/mdsc392-mapping-domain-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000392-scalars | .temp/gtdb-source-holds-20261115/mdsc392-mapping-scalars-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000392-history | .temp/gtdb-source-holds-20261115/mdsc392-mapping-history-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000392-new-history | .temp/gtdb-source-holds-20261115/mdsc392-mapping-new-history-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000392-terms | .temp/gtdb-source-holds-20261115/mdsc392-mapping-terms-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000392-primary | PMID:42109165; Retained primary Methods2.1 strain roster and current/former names; Methods2.2 treatment context; exact source metadata primary_locators | supports | The source names F.duncaniae DSM17677T, previously F.prausnitzii, and D.piger DSM749T within the MDSC roster. These stock identities remain distinct from population-level reference mappings; no new study-stock assembly placement was established. |
| 000392-native | reports/gtdb-source-holds-20261115/mdsc392-final-source-evidence-001.json; Selected taxonomy[10/13] occurrences, full native_result, classify_status and matching source rows | supports | The pinned native exact411483 route yields F.duncaniae5099/fraction1.0. D.piger901 resolves via ncbi_name to156/fraction1.0, with no exact901 row. Complete native lineages/source IDs are retained. Pre-application NOT_ATTEMPTED described absent stored blocks, not absent database correspondence. |
| 000392-r232 | reports/phase2-completion-20261115/mdsc-r232-correspondence-001.json; Official retained workbook SHAe401d80c, Species worksheet row544 and row136; complete extracted matching rows and NCBI-name/GTDB-column separation | supports | R232 D.piger76/six taxa includes an unnamed57.89% majority; named D.piger22.37% and D.piger_A15.79% are separate entries. F.duncaniae has no exact NCBI-name row but appears in five GTDB result cells; F.prausnitzii948/57clusters is a distinct historical-name population. Counts cannot be pooled or substituted for the native reference populations or experimental stock identities. |
| 000392-note-transition | reports/gtdb-source-holds-20261115/mdsc392-note-checkpoint-001.json; Actual note plan/rawstage/rawapply/before.yaml, native102847Z sidecar and61-input checkpoint | supports | The first actual transition changed exactly notes10/13 and appended one native event,4ef59255→07e623ed. Eight note-only native checks passed. Real maintained ROOT0794bf80 preserves the intermediate separately from actual note execution71e2. |
| 000392-mapping-transition | .temp/gtdb-source-holds-20261115/mdsc392-mapping-applied-m5-001/receipt.json; Actual applied/before/after/source inputs and independently accepted final candidate | supports | Native ground-and-status persisted07e623ed→5beb7303: two reference blocks/statuses, removal of taxonomy[13]'s old six alternatives and two native events. The two corrected notes, four manual R232 blocks, all other taxonomy, stock/biological content and prior history remain unchanged. |
| 000392-prior | reports/causal_graph_review/decisions/20261007-four-records-batch74.yaml; Original batch74 ledger and test_causal_review_batch74.py | context_only | The original digest and historical FIX_MDSC/last-LLM clauses remain bound to their real predecessor, while current mucin/glycan/fermentation/discussion predicates remain current. Later admission must prove the exact note transition to maintained0794 and unchanged mapping-only proof to final bytes; no old assessment is relabelled as fresh full-record approval. |

## Limits And Additional Notes

- Partial diagnostic scientific_review:false. Native validity and reference correspondence do not provide whole-record scientific approval, corpus QC, automatic issue closure or release clearance.
- The complete canonical record and selected retained primary Methods stock/cultivation passages were inspected. No new full-paper, figure, supplement or sequence-assembly review was performed. Absence of independently verified stock genomes in this bounded evidence is not an absence claim about uninspected sources.
- The primary roster names F.duncaniae DSM17677T with former F.prausnitzii name and D.piger DSM749T. Reference counts/fractions are not study-stock assignments, community abundances or identity probabilities. Culture/type-strain labels and all source-preferred names remain unchanged.
- The native exact411483 population5099/fraction1.0 and ncbi_name901 population156/fraction1.0 come from the pinned761 crosswalk. Its release remains unestablished; file mtime cannot establish release order relative to R232. The name route is explicitly not an exact901 row.
- The independently inspected official R232 worksheet row544 has76 D.piger-labelled reference genomes across six GTDB taxa, including an unnamed cluster at57.89%. This population must not be pooled with the native156 or used to assign DSM749T. No exact F.duncaniae NCBI-name row occurs in that worksheet, while five other NCBI-name rows mention the GTDB species. Historical-name row136 F.prausnitzii948/57clusters is a distinct population, not species absence or an exact current-species denominator.
- All fourteen members, four unselected manual R232 blocks at0/1/6/12, unselected taxonomy[2] ambiguity, other mapping provenance, biology and original FIX_MDSC_GTDB_GROUNDINGS history remain unchanged. Their preservation is not new verification of those unselected classifications or release claims. Current scientific discussions and causal/source limitations are not silently retired.
- The first transition's eight checks and61-input checkpoint apply to the note-only intermediate. The eight required checks below are separate actual commands against final mapping bytes, including a distinct native sidecar. Actual execution revisions remain separate from the maintained intermediate.
- Local and M5 NCBI file-stat observations are separate provenance, not a whole-database checksum or certified build identity. Exact source/code/crosswalk/application inputs are individually hash-bound.
- The original batch74 ledger, penultimate historical FIX_MDSC event and last-LLM/hash obligations require later explicit composite admission while current scientific predicates remain current. Reference-snippet validation, generated products and combined QC are separate subsequent work. No source-population waiver or generic note exemption is introduced.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261115T111755Z-mdsc-source-populations-diagnostic
kind: record
repository: CultureBotAI/CommunityMech
title: MDSC reference correspondences with distinct R232 populations and study stocks
  preserved
started_at: '2026-11-15T11:17:55.383926Z'
finished_at: '2026-11-15T11:17:55.542984Z'
reviewer:
  identity: codex
  kind: agent
  independence: self_review
  independence_basis: Authored bounded source-provenance/database assessment. The
    parent independently reviewed both complete candidates, source plans, retained
    R232 evidence, actual note checkpoint and final mapping candidate. The shared
    native writer, engine, checker and builder were independently reviewed previously.
    This saved assessment is self-review, not independent whole-record scientific
    approval.
skill: curate-yaml-record
completion: completed
verdict: pass_with_limitations
scientific_review: false
summary: Two actual guarded M5 transitions correct the Faecalibacterium duncaniae
  and Desulfovibrio piger population notes, then store their native reference correspondences.
  Exact-ID411483 yields5099 genomes/fraction1.0; the species-name901 route yields156/fraction1.0
  with no exact901 row. These separate populations do not identify DSM17677T or DSM749T
  genomes and do not replace the independently inspected R232 worksheet populations.
  Both corrected notes, fourteen members, four manual R232 blocks and all biology
  remain preserved.
source:
  git_revision: f4e10146a77ebb0b5e697abc56d9683becfaaf5d
  state: working_tree
  inputs:
  - path: .temp/gtdb-r232-mdsc-20261115/source-001/ncbi_vs_gtdb_r232_bacteria.xlsx
    sha256: e401d80c914c727268c184d19201aa35dcd23aabfd027a0d6e5a57476e71f3de
    role: context
  - path: .temp/gtdb-r232-mdsc-20261115/source-001/source-receipt.json
    sha256: 9f0222100c6b5b4952d83ac0733ffba4d07e39471e69caa0420a8aa233157cf2
    role: context
  - path: .temp/gtdb-source-holds-20261115/kg-microbe/data/raw/NCBI2GTDB.tsv.gz
    sha256: 761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd
    role: context
  - path: .temp/gtdb-source-holds-20261115/mdsc392-mapping-applied-m5-001/before.yaml
    sha256: 07e623ed5425480b5303ec3a191fadb4b2959598533494ffcb98c3902551f2b5
    role: context
  - path: .temp/gtdb-source-holds-20261115/mdsc392-mapping-applied-m5-001/receipt.json
    sha256: 19ea31710d1ba8e0788199203dc1d57bdf90bbe1decfc7ea8f0fe5d2375321ba
    role: context
  - path: .temp/gtdb-source-holds-20261115/mdsc392-mapping-domain-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-source-holds-20261115/mdsc392-mapping-domain-001/native.log
    sha256: abba7ab881e52a5ba9d3452c93df83215d92525830fb275db53572f7da8decf5
    role: context
  - path: .temp/gtdb-source-holds-20261115/mdsc392-mapping-domain-001/receipt.json
    sha256: 5d8e140a8f5a02765407c9c22afebafb98a6211223f2894371ddefe0abf3b751
    role: context
  - path: .temp/gtdb-source-holds-20261115/mdsc392-mapping-domain-001/start.json
    sha256: 5acf032889361df0f4bb1bdfb8f7168c549ab637c49d0634e1af183856e276a4
    role: context
  - path: .temp/gtdb-source-holds-20261115/mdsc392-mapping-gtdb-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-source-holds-20261115/mdsc392-mapping-gtdb-001/native.log
    sha256: 35ab1a864208718f12300dda24893cf24843df73560a8443b0e38cf4edd39184
    role: context
  - path: .temp/gtdb-source-holds-20261115/mdsc392-mapping-gtdb-001/receipt.json
    sha256: db76b0b9ae0e5e89098e9f496d2f88c4b4cb8c3ef6aed68978dcfde823ff4763
    role: context
  - path: .temp/gtdb-source-holds-20261115/mdsc392-mapping-gtdb-001/start.json
    sha256: 88bf865216246f56ad320de2f8630eae24da5de5742c0bf5e0210901272796b9
    role: context
  - path: .temp/gtdb-source-holds-20261115/mdsc392-mapping-history-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-source-holds-20261115/mdsc392-mapping-history-001/native.log
    sha256: 700b44227c4cf01270ac26f16b308622de0b26f48d71aec49cdfaaab87620f0a
    role: context
  - path: .temp/gtdb-source-holds-20261115/mdsc392-mapping-history-001/receipt.json
    sha256: ab29b43c6749c4fcb1426ac61d5b34570a0771e65f6ef943627a4df9b1bca1a5
    role: context
  - path: .temp/gtdb-source-holds-20261115/mdsc392-mapping-history-001/start.json
    sha256: 5da48da077e9034bc6ae3f8e423568d3b1acca70ef4c61742f315c4167e0d8df
    role: context
  - path: .temp/gtdb-source-holds-20261115/mdsc392-mapping-new-history-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-source-holds-20261115/mdsc392-mapping-new-history-001/native.log
    sha256: 8593b155fd017cf8b3feb82571c5b5aa0b713aeefa2ef1c9809e4dc9494d2bba
    role: context
  - path: .temp/gtdb-source-holds-20261115/mdsc392-mapping-new-history-001/receipt.json
    sha256: b7c5c0af29288a7871d06915e8c642a0bc646d99f90b6e3df8902b57d10faec2
    role: context
  - path: .temp/gtdb-source-holds-20261115/mdsc392-mapping-new-history-001/start.json
    sha256: a330153eebbb85d950aa176abb79b2e951439d077afaf4922509980b5dbdc993
    role: context
  - path: .temp/gtdb-source-holds-20261115/mdsc392-mapping-scalars-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-source-holds-20261115/mdsc392-mapping-scalars-001/native.log
    sha256: 22b157a886e941dbb02dc24fca332cd484369c13af3c2fc720b346e94a41201e
    role: context
  - path: .temp/gtdb-source-holds-20261115/mdsc392-mapping-scalars-001/receipt.json
    sha256: 1d7a42aa5e55c7b07a3b36608d2416af18757099642916f40314949b33493ac8
    role: context
  - path: .temp/gtdb-source-holds-20261115/mdsc392-mapping-scalars-001/start.json
    sha256: 39ff7e8d4479a8f4c3c198208cdba0d6b7cfbb5986cd58da7576e48296fb93e6
    role: context
  - path: .temp/gtdb-source-holds-20261115/mdsc392-mapping-schema-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-source-holds-20261115/mdsc392-mapping-schema-001/native.log
    sha256: 36c77323c3d68a901880c8ef78e7cc02d0ceecae70c0cf659287059b9fb1e837
    role: context
  - path: .temp/gtdb-source-holds-20261115/mdsc392-mapping-schema-001/receipt.json
    sha256: 8b1a52be0c6839c16984075e532b855f132a0d94af606efb2d22cd47bc05e5a8
    role: context
  - path: .temp/gtdb-source-holds-20261115/mdsc392-mapping-schema-001/start.json
    sha256: faf58b5349458483768d34fea2502d70359dbd9c625ad67e5547f87b02b57204
    role: context
  - path: .temp/gtdb-source-holds-20261115/mdsc392-mapping-stage-m5-001/Mucin_Glycan_MDSC_Synthetic_Gut_Community.yaml
    sha256: 5beb7303470d09713d43acaeca51691badf905e3d8044341a5402695ead28393
    role: context
  - path: .temp/gtdb-source-holds-20261115/mdsc392-mapping-stage-m5-001/receipt.json
    sha256: f330055ae83c6c79924a8536588cd47ee67aba193848888b0fbc1bb382a2905b
    role: context
  - path: .temp/gtdb-source-holds-20261115/mdsc392-mapping-strict-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-source-holds-20261115/mdsc392-mapping-strict-001/native.log
    sha256: 8858014aa47292eca850122a3ae4e78a22040b3835de8d4b6c09e434c7c82a4f
    role: context
  - path: .temp/gtdb-source-holds-20261115/mdsc392-mapping-strict-001/receipt.json
    sha256: 098ab89999635ed2cd8ea7a44666c5b0611ad4172c8291c74048e629bdb69f3b
    role: context
  - path: .temp/gtdb-source-holds-20261115/mdsc392-mapping-strict-001/start.json
    sha256: 0ae3b9cfa0b1c1630929f57cae7a173d067f15b79c1588adc88dff8d9cd6126d
    role: context
  - path: .temp/gtdb-source-holds-20261115/mdsc392-mapping-strict-001/strict.tsv
    sha256: b184ed5450b968070bb6c75648407e388f41a1eaf7017890723cf560999fc3f7
    role: context
  - path: .temp/gtdb-source-holds-20261115/mdsc392-mapping-terms-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-source-holds-20261115/mdsc392-mapping-terms-001/native.log
    sha256: a0833945243fa1227e4a84287add9366a9363f48a3ea418bbfee41bd33be60eb
    role: context
  - path: .temp/gtdb-source-holds-20261115/mdsc392-mapping-terms-001/receipt.json
    sha256: 2313e9725ded3ebecec74933e1433ca0ed52fb44ed4ac769248b6e01e08e69a3
    role: context
  - path: .temp/gtdb-source-holds-20261115/mdsc392-mapping-terms-001/start.json
    sha256: 84518cc7e6eacc201b3c2691d52c5db7e1c582d3f7123f5b9ce6ba4457e8262d
    role: context
  - path: .temp/gtdb-source-holds-20261115/mdsc392-note-applied-m5-001/before.yaml
    sha256: 4ef5925538ded3549c72fd84eaa0786922b4f9565de33946289104cef18a5d49
    role: context
  - path: .temp/gtdb-source-holds-20261115/mdsc392-note-applied-m5-001/receipt.json
    sha256: 3e3e8c802378ad0e0c8eca2cb5e6f835abf206ebd8f6473520cdc917c1480d6d
    role: context
  - path: .temp/gtdb-source-holds-20261115/mdsc392-note-stage-m5-001/receipt.json
    sha256: b24549302ca46418c84b477e9822d3902a18ec8b812047c54c79307206c0a76c
    role: context
  - path: .temp/phase2-schema-20261115/mdsc392-after-note-native-route-001.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/phase2-schema-20261115/mdsc392-after-note-native-route-001.json
    sha256: 7ea9dd2acb004043a37b0bc13076f9a827e4f01f10ab4aad916495f396818f51
    role: context
  - path: .temp/phase2-schema-20261115/mdsc392-after-note-native-route-001.log
    sha256: 6e00633e317cd181808ec1680d9bfef25104dc45f790d867fbc2df370f0fcf8a
    role: context
  - path: .temp/phase2-schema-20261115/mdsc392-mapping-binder-m5-001.log
    sha256: a6a72d1c4676b3f2f1be0072798a8931187534ae40840c7aa934d12d39503d09
    role: context
  - path: .temp/phase2-schema-20261115/mdsc392-native-route-001.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/phase2-schema-20261115/mdsc392-native-route-001.json
    sha256: 8929e0a377c94bd2791866dc065d3d724522a42fd3f0b0c71a76a85716834f2e
    role: context
  - path: .temp/phase2-schema-20261115/mdsc392-native-route-001.log
    sha256: 5f79494df687892ccf64fad685c6cd919f4751dd2ad08d68da9360df6308dc81
    role: context
  - path: history/records/Mucin_Glycan_MDSC_Synthetic_Gut_Community/2026-09-20T102604Z-claude-code-4a1d47.yaml
    sha256: a0dcc83581b751742b5ab2a3ab0c1f433f7cb89034299dafa41ddae0a5aa040a
    role: context
  - path: history/records/Mucin_Glycan_MDSC_Synthetic_Gut_Community/2026-09-20T103111Z-claude-code-78ca12.yaml
    sha256: 2b8baf2a1f58778ee807411f8b64ce5ba384aca4e8b324af14be699babeccf8d
    role: context
  - path: history/records/Mucin_Glycan_MDSC_Synthetic_Gut_Community/2026-09-20T110416Z-claude-code-4f4fe0.yaml
    sha256: 632f9613ae2dfeed97ad424309b3de8d838ac04ee9aff5259e9ab4f53274d01a
    role: context
  - path: history/records/Mucin_Glycan_MDSC_Synthetic_Gut_Community/2026-10-07T024304Z-codex-132d35.yaml
    sha256: a12ea6cfafc66c591c9816790af50f82bba626408deb454999259ef02af62ccd
    role: context
  - path: history/records/Mucin_Glycan_MDSC_Synthetic_Gut_Community/2026-11-15T102847Z-codex-f51d56.yaml
    sha256: 215ed9b17c26841180dd210e2a004c8dfbb1b715d5367f7a9fc2cc638db74867
    role: context
  - path: history/records/Mucin_Glycan_MDSC_Synthetic_Gut_Community/2026-11-15T111234Z-codex-22dfa8.yaml
    sha256: 003a1686c44bfd2a98acdd2f9430551dc54986b4e14dbdde6d96e2f63485af21
    role: context
  - path: justfile
    sha256: 40369611ad4531582e420df0e9ff22109e4b18adf03b34d86b54200b280f2d0f
    role: context
  - path: kb/communities/Mucin_Glycan_MDSC_Synthetic_Gut_Community.yaml
    sha256: 5beb7303470d09713d43acaeca51691badf905e3d8044341a5402695ead28393
    role: target
  - path: pyproject.toml
    sha256: be952f0f137f85fed66bda0908f12014f1797a2dd229b44d832afc0c00471655
    role: context
  - path: references_cache/PMID_42109165.txt
    sha256: d71d87dee9cbb64e6c2abebcc53b4f84558cc5a04770846235dbba131cf7b24a
    role: context
  - path: reports/causal_graph_review/decisions/20261007-four-records-batch74.yaml
    sha256: 4d975cf5114b018229e3fc8408b87ea6b43e50d5e40569c564aeefa4daffa8ca
    role: context
  - path: reports/gtdb-source-holds-20261115/mdsc392-final-review-config-001.json
    sha256: 128b72f9784474d6089a613b606dbca6dd5fc0742fb2e5e0986e4d1a3a75d831
    role: context
  - path: reports/gtdb-source-holds-20261115/mdsc392-final-source-evidence-001.json
    sha256: 8c78c58d9289beceff6407f41a46559aaff0729882bebe8ddec6a7821c951d75
    role: context
  - path: reports/gtdb-source-holds-20261115/mdsc392-mapping-check-config-001.json
    sha256: 68cd561a94f5933ec561bb14e5d3108bf96abdb6377a5b22c13ea76acd81721d
    role: context
  - path: reports/gtdb-source-holds-20261115/mdsc392-mapping-route-plan-001.json
    sha256: 3488edbcb95a60cc4a6909b587ce491cfb08ed2945b9ee4892d5bb1594ea465c
    role: context
  - path: reports/gtdb-source-holds-20261115/mdsc392-mapping-source-config-001.json
    sha256: 1c15269a635795249676599fdef43cc1aaedf3392c2ecb5da35d8a85af42c606
    role: context
  - path: reports/gtdb-source-holds-20261115/mdsc392-note-apply-001.raw.json
    sha256: 3e3e8c802378ad0e0c8eca2cb5e6f835abf206ebd8f6473520cdc917c1480d6d
    role: context
  - path: reports/gtdb-source-holds-20261115/mdsc392-note-check-config-001.json
    sha256: 53c5cf5b82c94d28b20bfcd996c943a1aef3ea894dc3aa47e59d443b71011dfe
    role: context
  - path: reports/gtdb-source-holds-20261115/mdsc392-note-checkpoint-001.json
    sha256: 655fac0850ba60b574f806ccb7ef5a6459735c87be63813317131e434081478e
    role: context
  - path: reports/gtdb-source-holds-20261115/mdsc392-note-intermediate-001.md
    sha256: e41f100c3751b8dc673c5629c90ca8f37ec07aee52c72c9630c60ed425c5f3a9
    role: context
  - path: reports/gtdb-source-holds-20261115/mdsc392-note-plan-001.json
    sha256: d22433ab79e52bf9f4e7a43f543185e09a7115ebec0ac5077c09b79dd5452bf3
    role: context
  - path: reports/gtdb-source-holds-20261115/mdsc392-note-stage-001.raw.json
    sha256: b24549302ca46418c84b477e9822d3902a18ec8b812047c54c79307206c0a76c
    role: context
  - path: reports/gtdb-source-holds-20261115/mdsc392-route-plan-001.json
    sha256: d042a6c81d33624720ba69ee8b3e80b51c74e49a1a01c2d7d08992082347abc5
    role: context
  - path: reports/phase2-completion-20261115/mdsc-r232-correspondence-001.json
    sha256: c72f3372b3382ff7193121332e3c2a66ab09f627e657f47b3915509cec45b71c
    role: context
  - path: reports/phase2-completion-20261115/mdsc-r232-source-disposition-001.md
    sha256: 6cad42f85c7f66112c613ed68bbc8c51890dae7669a5ec3ceb51eb49823bfb50
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
  - path: scripts/adhoc/curate_gtdb_source_notes_20261115.py
    sha256: 77ff86d185c6b04634c1bd83531463e42e5ece9f116873bf1d81c7af1de80380
    role: context
  - path: scripts/adhoc/export_m5_technical_evidence_20261114.py
    sha256: a0f43f617e8921443e660d262d28713f40b4c23770b684203c37b65330cc4a5d
    role: context
  - path: scripts/adhoc/gtdb_batch_curation_20261115.py
    sha256: 867e974e9c55325fb1b7e32f81dcf6b7a65b6720941fd303040f5570e46ba232
    role: context
  - path: scripts/adhoc/inspect_gtdb_note_checkpoint_20261115.py
    sha256: b7e0af9dc1834582a16b7cc2dfefb54a1131e706f12b300a6cd75d603089e134
    role: context
  - path: scripts/adhoc/inspect_mdsc_r232_correspondence_20261115.py
    sha256: f7a2a8e93c84a362e9f5ffe9f8f68f3aae8f48ffb694a18e5c452f2c2712b6b4
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
  - path: tests/source_note_gtdb_successor.py
    sha256: f343d60ebcb1fb68e2139ff689004aeadd2a5826cbd0e806db809ef25c5d02ef
    role: context
  - path: tests/test_causal_review_batch74.py
    sha256: 46f1cbe401d385001730f356bb6349965b3452c00c0f88f7b714d62f2b0c2cff
    role: context
  - path: uv.lock
    sha256: 712838f8fa3d68fbd818ac8162f3f1e2f2637db1da1a8ebfaba0ef759690f3b4
    role: context
targets:
- target_id: CommunityMech:000392
  path: kb/communities/Mucin_Glycan_MDSC_Synthetic_Gut_Community.yaml
  selector: taxonomy[10].taxon_term.notes; taxonomy[10].taxon_term.gtdb_classification;
    taxonomy[10].taxon_term.gtdb_grounding_status; taxonomy[13].taxon_term.notes;
    taxonomy[13].taxon_term.gtdb_classification; taxonomy[13].taxon_term.gtdb_grounding_status;
    taxonomy[13].taxon_term.gtdb_candidates
  label: Two reference correspondences with source-stock and population distinctions
    preserved
  kind: maintained
  ownership_note: CommunityMech owns this record; only declared GTDB correspondence/status
    and actual provenance are assessed.
scope:
  description: CommunityMech:000392 taxonomy[10/13] source notes and GTDB descriptor
    fields, actual two-transition provenance, primary stock/population boundaries
    and final-byte native checks. Partial technical/source-provenance assessment;
    not whole-record scientific review.
  selection: One source-held whole record. Original4ef59255 became note-only07e623ed
    through actual note execution71e2. Real maintained ROOT0794bf80ebd15a073dc2103cfd1ed0c5234e6d74
    contains that exact intermediate. A separate M5 checkout atf4e10146a77ebb0b5e697abc56d9683becfaaf5d
    applied final native mapping5beb7303 and ran eight final-byte native checks.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000392
  exclusions:
  - target: Other scientific claims and records
    reason: Existing biology is preserved, not newly certified by this database diagnostic.
checks:
- check_id: 000392-schema
  name: validate
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000392
  command: just --verbose --no-dotenv --color never validate kb/communities/Mucin_Glycan_MDSC_Synthetic_Gut_Community.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000392-schema
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000392-strict
  name: validate-strict
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000392
  command: just --verbose --no-dotenv --color never validate-strict kb/communities/Mucin_Glycan_MDSC_Synthetic_Gut_Community.yaml
    --out .temp/gtdb-source-holds-20261115/mdsc392-mapping-strict-001/strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000392-strict
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000392-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000392
  command: just --verbose --no-dotenv --color never validate-gtdb kb/communities/Mucin_Glycan_MDSC_Synthetic_Gut_Community.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000392-gtdb
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000392-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000392
  command: just --verbose --no-dotenv --color never validate-gtdb-domain kb/communities/Mucin_Glycan_MDSC_Synthetic_Gut_Community.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000392-domain
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000392-scalars
  name: validate-scalars
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000392
  command: just --verbose --no-dotenv --color never validate-scalars kb/communities/Mucin_Glycan_MDSC_Synthetic_Gut_Community.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000392-scalars
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000392-history
  name: validate-history
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000392
  command: just --verbose --no-dotenv --color never validate-history history/records/Mucin_Glycan_MDSC_Synthetic_Gut_Community
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000392-history
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000392-new-history
  name: new-history
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000392
  command: just --verbose --no-dotenv --color never new-history --kind record --slug
    Mucin_Glycan_MDSC_Synthetic_Gut_Community --target-root kb/communities --event
    EDIT --outcome changed --sections taxonomy,curation_history --actor-name codex
    --model gpt-6 --agent-tool codex --issue https://github.com/CultureBotAI/CommunityMech/issues/2848
    --summary 'Ground two MDSC reference descriptors after source-population note
    corrections' --details 'Applied the accepted native ground-and-status transition
    to taxonomy[10] NCBITaxon411483 and taxonomy[13] NCBITaxon901 from the actual
    note-only intermediate. The exact-ID Faecalibacterium duncaniae reference population5099/fraction1.0
    and species-name Desulfovibrio piger reference population156/fraction1.0 are distinct
    from study-stock genomes and the separately inspected R232 populations. No exact901
    crosswalk row or established release for the pinned761 table is asserted. Both
    corrected notes, all fourteen members, four manual R232 blocks, unselected ambiguity
    and biological content remain unchanged. Historical FIX_MDSC_GTDB_GROUNDINGS is
    preserved; existing scientific limits and2877 remain outside this mapping-only
    step. Final strict two-transition admission uses real maintained ROOT0794bf80ebd15a073dc2103cfd1ed0c5234e6d74;
    actual note execution71e2 and final executionf4e remain distinct provenance metadata.
    No whole-record scientific approval or corpus QC is claimed. Actual apply receipt
    .temp/gtdb-source-holds-20261115/mdsc392-mapping-applied-m5-001/receipt.json sha256:19ea31710d1ba8e0788199203dc1d57bdf90bbe1decfc7ea8f0fe5d2375321ba.'
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000392-new-history
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000392-terms
  name: validate-terms
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000392
  command: just --verbose --no-dotenv --color never validate-terms kb/communities/Mucin_Glycan_MDSC_Synthetic_Gut_Community.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000392-terms
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
evidence:
- evidence_id: 000392-schema
  kind: validation
  reference: .temp/gtdb-source-holds-20261115/mdsc392-mapping-schema-001/native.log
  accessed_at: '2026-11-15T11:17:55.383926Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000392-strict
  kind: validation
  reference: .temp/gtdb-source-holds-20261115/mdsc392-mapping-strict-001/native.log
  accessed_at: '2026-11-15T11:17:55.383926Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000392-gtdb
  kind: validation
  reference: .temp/gtdb-source-holds-20261115/mdsc392-mapping-gtdb-001/native.log
  accessed_at: '2026-11-15T11:17:55.383926Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000392-domain
  kind: validation
  reference: .temp/gtdb-source-holds-20261115/mdsc392-mapping-domain-001/native.log
  accessed_at: '2026-11-15T11:17:55.383926Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000392-scalars
  kind: validation
  reference: .temp/gtdb-source-holds-20261115/mdsc392-mapping-scalars-001/native.log
  accessed_at: '2026-11-15T11:17:55.383926Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000392-history
  kind: validation
  reference: .temp/gtdb-source-holds-20261115/mdsc392-mapping-history-001/native.log
  accessed_at: '2026-11-15T11:17:55.383926Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000392-new-history
  kind: validation
  reference: .temp/gtdb-source-holds-20261115/mdsc392-mapping-new-history-001/native.log
  accessed_at: '2026-11-15T11:17:55.383926Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000392-terms
  kind: validation
  reference: .temp/gtdb-source-holds-20261115/mdsc392-mapping-terms-001/native.log
  accessed_at: '2026-11-15T11:17:55.383926Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000392-primary
  kind: primary_source
  reference: PMID:42109165
  locator: Retained primary Methods2.1 strain roster and current/former names; Methods2.2
    treatment context; exact source metadata primary_locators
  support: supports
  summary: The source names F.duncaniae DSM17677T, previously F.prausnitzii, and D.piger
    DSM749T within the MDSC roster. These stock identities remain distinct from population-level
    reference mappings; no new study-stock assembly placement was established.
  accessed_at: '2026-11-15T11:17:55.383926Z'
- evidence_id: 000392-native
  kind: database
  reference: reports/gtdb-source-holds-20261115/mdsc392-final-source-evidence-001.json
  locator: Selected taxonomy[10/13] occurrences, full native_result, classify_status
    and matching source rows
  support: supports
  summary: The pinned native exact411483 route yields F.duncaniae5099/fraction1.0.
    D.piger901 resolves via ncbi_name to156/fraction1.0, with no exact901 row. Complete
    native lineages/source IDs are retained. Pre-application NOT_ATTEMPTED described
    absent stored blocks, not absent database correspondence.
  accessed_at: '2026-11-15T11:17:55.383926Z'
- evidence_id: 000392-r232
  kind: database
  reference: reports/phase2-completion-20261115/mdsc-r232-correspondence-001.json
  locator: Official retained workbook SHAe401d80c, Species worksheet row544 and row136;
    complete extracted matching rows and NCBI-name/GTDB-column separation
  support: supports
  summary: R232 D.piger76/six taxa includes an unnamed57.89% majority; named D.piger22.37%
    and D.piger_A15.79% are separate entries. F.duncaniae has no exact NCBI-name row
    but appears in five GTDB result cells; F.prausnitzii948/57clusters is a distinct
    historical-name population. Counts cannot be pooled or substituted for the native
    reference populations or experimental stock identities.
  accessed_at: '2026-11-15T11:17:55.383926Z'
- evidence_id: 000392-note-transition
  kind: record_content
  reference: reports/gtdb-source-holds-20261115/mdsc392-note-checkpoint-001.json
  locator: Actual note plan/rawstage/rawapply/before.yaml, native102847Z sidecar and61-input
    checkpoint
  support: supports
  summary: The first actual transition changed exactly notes10/13 and appended one
    native event,4ef59255→07e623ed. Eight note-only native checks passed. Real maintained
    ROOT0794bf80 preserves the intermediate separately from actual note execution71e2.
  accessed_at: '2026-11-15T11:17:55.383926Z'
- evidence_id: 000392-mapping-transition
  kind: record_content
  reference: .temp/gtdb-source-holds-20261115/mdsc392-mapping-applied-m5-001/receipt.json
  locator: Actual applied/before/after/source inputs and independently accepted final
    candidate
  support: supports
  summary: 'Native ground-and-status persisted07e623ed→5beb7303: two reference blocks/statuses,
    removal of taxonomy[13]''s old six alternatives and two native events. The two
    corrected notes, four manual R232 blocks, all other taxonomy, stock/biological
    content and prior history remain unchanged.'
  accessed_at: '2026-11-15T11:17:55.383926Z'
- evidence_id: 000392-prior
  kind: prior_review
  reference: reports/causal_graph_review/decisions/20261007-four-records-batch74.yaml
  locator: Original batch74 ledger and test_causal_review_batch74.py
  support: context_only
  summary: The original digest and historical FIX_MDSC/last-LLM clauses remain bound
    to their real predecessor, while current mucin/glycan/fermentation/discussion
    predicates remain current. Later admission must prove the exact note transition
    to maintained0794 and unchanged mapping-only proof to final bytes; no old assessment
    is relabelled as fresh full-record approval.
  accessed_at: '2026-11-15T11:17:55.383926Z'
assessments:
- assessment_id: 000392-stock-boundaries
  area: grounding
  topic: Named study stocks remain separate from descriptor populations
  outcome: supported
  target_ids:
  - CommunityMech:000392
  evidence_ids:
  - 000392-primary
  - 000392-native
  - 000392-terms
  summary: DSM17677T and DSM749T, all fourteen members and existing culture/type-strain
    assertions remain unchanged. The reference routes do not independently identify
    experimental assemblies, establish stock-level GTDB classification, quantify community
    abundance or rename study members.
- assessment_id: 000392-source-populations
  area: grounding
  topic: Corrected notes retain the distinct native and official R232 populations
  outcome: supported
  target_ids:
  - CommunityMech:000392
  evidence_ids:
  - 000392-native
  - 000392-r232
  - 000392-note-transition
  summary: The no-majority and absence claims were replaced by exact population distinctions.
    Native5099/1 and156/1 remain separate from R23276/six,948/57 and five GTDB-column
    mentions. The R232 unnamed majority is not a stock assignment, and no exact current-name
    NCBI row does not mean the GTDB species is absent. Crosswalk release order remains
    unestablished.
- assessment_id: 000392-reference-mappings
  area: grounding
  topic: Two native blocks and GROUNDED descriptor statuses
  outcome: supported
  target_ids:
  - CommunityMech:000392
  evidence_ids:
  - 000392-native
  - 000392-mapping-transition
  - 000392-gtdb
  - 000392-domain
  summary: Taxonomy[10] stores the exact-ID F.duncaniae5099/1 result; taxonomy[13]
    stores the name-route D.piger156/1 result and removes its old six alternatives.
    GROUNDED describes the encoded reference correspondence, not a verified experimental
    stock genome. Both corrected notes and four unselected manual blocks remain exact.
- assessment_id: 000392-two-transitions
  area: provenance
  topic: Actual note and mapping transitions with final-byte native checks
  outcome: supported
  target_ids:
  - CommunityMech:000392
  evidence_ids:
  - 000392-note-transition
  - 000392-mapping-transition
  - 000392-new-history
  - 000392-history
  - 000392-schema
  - 000392-strict
  - 000392-scalars
  - 000392-prior
  summary: Both actual application inputs and sidecars are captured. Eight final-byte
    native commands passed separately from the note-only checks. Real maintained0794
    is distinct from actual finalf4e execution. Composite historical admission, generated
    products and combined QC remain subsequent integration work, with all prior biological
    findings and immutable history preserved.
findings: []
actions: []
limitations:
- Partial diagnostic scientific_review:false. Native validity and reference correspondence
  do not provide whole-record scientific approval, corpus QC, automatic issue closure
  or release clearance.
- The complete canonical record and selected retained primary Methods stock/cultivation
  passages were inspected. No new full-paper, figure, supplement or sequence-assembly
  review was performed. Absence of independently verified stock genomes in this bounded
  evidence is not an absence claim about uninspected sources.
- The primary roster names F.duncaniae DSM17677T with former F.prausnitzii name and
  D.piger DSM749T. Reference counts/fractions are not study-stock assignments, community
  abundances or identity probabilities. Culture/type-strain labels and all source-preferred
  names remain unchanged.
- The native exact411483 population5099/fraction1.0 and ncbi_name901 population156/fraction1.0
  come from the pinned761 crosswalk. Its release remains unestablished; file mtime
  cannot establish release order relative to R232. The name route is explicitly not
  an exact901 row.
- The independently inspected official R232 worksheet row544 has76 D.piger-labelled
  reference genomes across six GTDB taxa, including an unnamed cluster at57.89%. This
  population must not be pooled with the native156 or used to assign DSM749T. No exact
  F.duncaniae NCBI-name row occurs in that worksheet, while five other NCBI-name rows
  mention the GTDB species. Historical-name row136 F.prausnitzii948/57clusters is
  a distinct population, not species absence or an exact current-species denominator.
- All fourteen members, four unselected manual R232 blocks at0/1/6/12, unselected
  taxonomy[2] ambiguity, other mapping provenance, biology and original FIX_MDSC_GTDB_GROUNDINGS
  history remain unchanged. Their preservation is not new verification of those unselected
  classifications or release claims. Current scientific discussions and causal/source
  limitations are not silently retired.
- The first transition's eight checks and61-input checkpoint apply to the note-only
  intermediate. The eight required checks below are separate actual commands against
  final mapping bytes, including a distinct native sidecar. Actual execution revisions
  remain separate from the maintained intermediate.
- Local and M5 NCBI file-stat observations are separate provenance, not a whole-database
  checksum or certified build identity. Exact source/code/crosswalk/application inputs
  are individually hash-bound.
- The original batch74 ledger, penultimate historical FIX_MDSC event and last-LLM/hash
  obligations require later explicit composite admission while current scientific
  predicates remain current. Reference-snippet validation, generated products and
  combined QC are separate subsequent work. No source-population waiver or generic
  note exemption is introduced.
links:
- https://github.com/CultureBotAI/CommunityMech/issues/2848
- https://github.com/CultureBotAI/CommunityMech/issues/2877
- https://github.com/CultureBotAI/CommunityMech/pull/2804
```
