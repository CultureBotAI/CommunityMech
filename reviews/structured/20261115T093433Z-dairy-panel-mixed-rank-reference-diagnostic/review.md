# Dairy cultivation panel: bounded genus and species reference correspondences

- Review: 20261115T093433Z-dairy-panel-mixed-rank-reference-diagnostic
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-11-15T09:34:33.285428Z
- Finished UTC: 2026-11-15T09:34:33.627789Z
- Reviewer: codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: false

## Summary

The existing Synechocystis genus descriptor and Desertifilum tharense species descriptor now carry their exact native reference correspondences and matching statuses. No experimental stock or assembly identity is added. The four descriptors, eukaryotic exclusions, distinct cultivation treatments, source quotations, empty biological graph and historical uncertainty remain unchanged.

## Scope And Provenance

Exactly two declared GTDB blocks/statuses, two native inline events and the actual source/application/history/gate provenance for CommunityMech:000384. This is a partial mixed-rank database-correspondence diagnostic, not a complete scientific review of the cultivation panel.

Selection: One whole-record mixed-rank canary selected from six source-prepared records. Only CommunityMech:000384 is reviewed here; the six-record source-report denominator is preparation context, not the reviewed population. No remaining mixed or family-route application is approved by this diagnostic alone.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 70ef731cc6c35d9ffe08a391c9db2b4adb10abf4.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000384 | kb/communities/Dairy_Wastewater_Algal_Cyanobacterial_Cultivation_Panel.yaml # taxonomy[0:2].taxon_term.gtdb_classification; gtdb_grounding_status | maintained | Synechocystis genus and Desertifilum species descriptors without stock-genome identification |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000384 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-strict | passed | True | CommunityMech:000384 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-gtdb | passed | True | CommunityMech:000384 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-gtdb-domain | passed | True | CommunityMech:000384 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-scalars | passed | True | CommunityMech:000384 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-history | passed | True | CommunityMech:000384 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| new-history | passed | True | CommunityMech:000384 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-terms | passed | True | CommunityMech:000384 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |

## Scientific And Domain Assessments

### Source-compatible rank and treatment identity

grounding: supported. Targets: CommunityMech:000384.

The genus-only Synechocystis and named Desertifilum species descriptors retain their original scope and absent strain identifiers. All four panel descriptors and treatment memberships remain distinct.

### Mixed-rank reference populations without stock assignment

grounding: supported. Targets: CommunityMech:000384.

The native 8/8 genus population and one-genome exact-ID species result establish bounded database correspondences. They do not identify study genomes, infer a four-member inoculum or change the two eukaryotic exclusions.

### Actual guarded transition with historical science preserved

provenance: supported. Targets: CommunityMech:000384.

The accepted candidate was applied on the isolated frozen M5 revision, with eight scoped native commands and one appended sidecar. Old scientific uncertainty, biological predicates, source quotations and history remain unchanged; remaining mixed-route units await the complete saved canary proof.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| 000384-schema | .temp/gtdb-code006-20261115/genus-mixed-384-run-schema-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000384-strict | .temp/gtdb-code006-20261115/genus-mixed-384-run-strict-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000384-gtdb | .temp/gtdb-code006-20261115/genus-mixed-384-run-gtdb-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000384-domain | .temp/gtdb-code006-20261115/genus-mixed-384-run-domain-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000384-scalars | .temp/gtdb-code006-20261115/genus-mixed-384-run-scalars-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000384-history | .temp/gtdb-code006-20261115/genus-mixed-384-run-history-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000384-new-history | .temp/gtdb-code006-20261115/genus-mixed-384-run-new-history-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000384-terms | .temp/gtdb-code006-20261115/genus-mixed-384-run-terms-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000384-paper | https://pubmed.ncbi.nlm.nih.gov/41561919/; Retained data-article Methods and Table 3; exact MC1/MC2 anchor and primary_contexts in the bound source metadata | supports | The source names Synechocystis sp. and Desertifilum tharense without formal strain identifiers and assigns them to distinct mono-, paired and sequential cultivation groups. This does not establish exact reference-genome identity. |
| 000384-database | reports/gtdb-code006-20261115/genus-mixed-384-source-evidence-001.json; occurrences[taxonomy_index=0,1], exact term selectors, native_result and ncbi_identity_rows | supports | NCBITaxon1142 remains genus rank with the native 8/8 Synechocystis reference population. NCBITaxon1185873 remains species rank with one exact-ID Desertifilum tharense reference genome. No new taxon label, stock or assembly assertion follows. |
| 000384-application | .temp/gtdb-code006-20261115/genus-mixed-384-applied-m5-001/receipt.json; actual before/after/input binding, two native inline events and bound appended sidecar | supports | The guarded M5 application persisted the independently accepted candidate. Its only semantic changes are the two declared correspondence blocks/statuses and native events; all biology, quotations, prior history and exclusions remain protected. |
| 000384-prior | reports/causal_graph_review/decisions/20261006-kefir-dairy-batch59.yaml; Dairy record needs_research disposition and unchanged source/graph boundaries; separate kefir record remains outside this unit | context_only | The historical scientific review leaves treatment-specific interaction structure unresolved. The empty graph is not evidence that biological interactions are absent; source-grounded descriptor correspondence does not revise that assessment. |

## Limits And Additional Notes

- Partial technical review with scientific_review:false. Native technical completion does not establish full scientific review, source-snippet validation, generated-page integration, final corpus QC or campaign completion.
- The native Synechocystis genus result is 8/8 filtered reference genomes. The Desertifilum tharense exact-ID species result contains one reference genome. Neither population identifies the unnamed experimental stocks or establishes that the study used a particular reference assembly.
- Source examination was limited to retained data-article Methods and Table 3 passages. This pass did not newly acquire or completely review the associated research article, supplements, figure pixels, raw amplicon data or study assemblies.
- Four monocultures, four paired cultures and four sequential cultures remain separate treatments. The four listed descriptors are not a universal four-member inoculum; indigenous non-sterile bacteria remain outside the exact canonical roster.
- Chlorella sorokiniana and Euglena gracilis retain NO_GTDB_EQUIVALENT. Source-supported genus versus species rank, absent formal strain fields and all treatment memberships remain unchanged.
- The empty ecological graph remains an unresolved research gap under the historical batch 59 assessment and issue 1537. Endpoint profiles, predicted functions and associations do not establish gene activity, exchanged flux or selective mediation. This correspondence correction makes no issue disposition.
- Source reporting, binding and the first private stage ran locally at ead20c0392805c2810d49e9a57aa2fd710578145. The actual M5 stage, application and scoped gates ran at published 70ef731cc6c35d9ffe08a391c9db2b4adb10abf4 with native Python 3.13.2. Post-application receipts are not clean-tree runs. The original local candidate remains retained; its only content difference from the accepted M5 candidate is the two actual native timestamps.
- The exact crosswalk hash is 761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd; file mtime is not a release identifier. Local NCBI identity/rank observations are stat-bound, not full database checksum claims.
- Native terms report Validation passed without an assertion denominator. Strict successor admission, historical caller checks and generated-page integration remain separate follow-up checks; technical gates do not count examined scientific assertions.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261115T093433Z-dairy-panel-mixed-rank-reference-diagnostic
kind: record
repository: CultureBotAI/CommunityMech
title: 'Dairy cultivation panel: bounded genus and species reference correspondences'
started_at: '2026-11-15T09:34:33.285428Z'
finished_at: '2026-11-15T09:34:33.627789Z'
reviewer:
  identity: codex
  kind: agent
  independence: self_review
  independence_basis: Parent independently read the primary-source context, authored
    configuration, native source populations, full local and actual M5 candidate diffs
    and external candidate/receipt hashes before the guarded application. The unchanged
    shared binder, engine, gate runner and diagnostic builder have separate code reviews
    and mutation controls. This is self-review of the resulting scoped technical correction.
skill: curate-yaml-record
completion: completed
verdict: pass_with_limitations
scientific_review: false
summary: The existing Synechocystis genus descriptor and Desertifilum tharense species
  descriptor now carry their exact native reference correspondences and matching statuses.
  No experimental stock or assembly identity is added. The four descriptors, eukaryotic
  exclusions, distinct cultivation treatments, source quotations, empty biological
  graph and historical uncertainty remain unchanged.
source:
  git_revision: 70ef731cc6c35d9ffe08a391c9db2b4adb10abf4
  state: working_tree
  inputs:
  - path: .temp/gtdb-code006-20261115/genus-mixed-384-applied-m5-001/before.yaml
    sha256: 4fc81cfb17b74f44b121440c5375d5a8e2f42e76b60ee057fdc53deafa263831
    role: context
  - path: .temp/gtdb-code006-20261115/genus-mixed-384-applied-m5-001/receipt.json
    sha256: 1aad8d549e9ba0a799d39acf76998467cfa85c76d1f5babe23aa576f6fb96383
    role: context
  - path: .temp/gtdb-code006-20261115/genus-mixed-384-candidate-m5-001/Dairy_Wastewater_Algal_Cyanobacterial_Cultivation_Panel.yaml
    sha256: 0b837a73e603469d21643996c0564bdbc93d1f9852833fb789529257965dbce1
    role: context
  - path: .temp/gtdb-code006-20261115/genus-mixed-384-candidate-m5-001/receipt.json
    sha256: c13d4f12187f40218d19cc547bba55ce7bba8056a53ca26f36e956c26f8149a8
    role: context
  - path: .temp/gtdb-code006-20261115/genus-mixed-384-check-config-001.json
    sha256: 9d238ca7bc6a84f19e0c199d2017a3ca726fae7330979348c3ccfd020c6ca307
    role: context
  - path: .temp/gtdb-code006-20261115/genus-mixed-384-run-domain-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-mixed-384-run-domain-001/native.log
    sha256: 703e3b46f53fe10d66905e66c76ff0302fbf984f17e3b97de56f228a344c2c70
    role: context
  - path: .temp/gtdb-code006-20261115/genus-mixed-384-run-domain-001/receipt.json
    sha256: 2b31f6e37d0e9250591e58c08ce788807d88eacac79a84764bc57b2550ffb383
    role: context
  - path: .temp/gtdb-code006-20261115/genus-mixed-384-run-domain-001/start.json
    sha256: d019594eae026abce46a1322b217b709ba9516eba0f01a97c51af6d183962a55
    role: context
  - path: .temp/gtdb-code006-20261115/genus-mixed-384-run-gtdb-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-mixed-384-run-gtdb-001/native.log
    sha256: 64cc4cdf8c0b9b5ce86477ee23005375d3b30c50263452c603ce14ec9c3fda19
    role: context
  - path: .temp/gtdb-code006-20261115/genus-mixed-384-run-gtdb-001/receipt.json
    sha256: 7ec7b0dc7cac3d0027ac64d3a4319bd1792df44d9c747dd195c9686158631489
    role: context
  - path: .temp/gtdb-code006-20261115/genus-mixed-384-run-gtdb-001/start.json
    sha256: 60a4a47e502b30d75fdb2a9ab43bf034c4daf66b9d142fbddfeaa0ba3b3c6d00
    role: context
  - path: .temp/gtdb-code006-20261115/genus-mixed-384-run-history-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-mixed-384-run-history-001/native.log
    sha256: 700b44227c4cf01270ac26f16b308622de0b26f48d71aec49cdfaaab87620f0a
    role: context
  - path: .temp/gtdb-code006-20261115/genus-mixed-384-run-history-001/receipt.json
    sha256: 71f907d80a3ef973406ba83684526d82795cc52af9da79d3e5355692196be89e
    role: context
  - path: .temp/gtdb-code006-20261115/genus-mixed-384-run-history-001/start.json
    sha256: 2a99ad8d8532544af83a91c0524916736b9225b77603eae96dbc57766615c703
    role: context
  - path: .temp/gtdb-code006-20261115/genus-mixed-384-run-new-history-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-mixed-384-run-new-history-001/native.log
    sha256: 486e187f2b709bbbed42c8e0699f74b44a49988b8011c9a486886d17abd38af4
    role: context
  - path: .temp/gtdb-code006-20261115/genus-mixed-384-run-new-history-001/receipt.json
    sha256: f70eb37c47bda733abdc43b04136d03c32c4012e0b10173756e78b8281f75846
    role: context
  - path: .temp/gtdb-code006-20261115/genus-mixed-384-run-new-history-001/start.json
    sha256: a4541342e71876187b7a79c613101467aa89c0030334d474917bd2c2901cb0cb
    role: context
  - path: .temp/gtdb-code006-20261115/genus-mixed-384-run-scalars-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-mixed-384-run-scalars-001/native.log
    sha256: 9f4baede7b9b5c42f99d257c43e214c468c5e1ec246dceb331a33e16fd46c949
    role: context
  - path: .temp/gtdb-code006-20261115/genus-mixed-384-run-scalars-001/receipt.json
    sha256: 1450aba0260ad9c7a9d6e6abda0b74202d2cc29ce0d3e000d76f57f43c95f73c
    role: context
  - path: .temp/gtdb-code006-20261115/genus-mixed-384-run-scalars-001/start.json
    sha256: 284ff528e4530ea87c7732352254cfdeef41054e7b71d42512e65c1047c10746
    role: context
  - path: .temp/gtdb-code006-20261115/genus-mixed-384-run-schema-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-mixed-384-run-schema-001/native.log
    sha256: fae6e56c52fbfaa31da075d63277ccc80c1a523d6119eb6335dae93f5edf40f9
    role: context
  - path: .temp/gtdb-code006-20261115/genus-mixed-384-run-schema-001/receipt.json
    sha256: c6bd6a5f6284a87ae59ee970e427e2e0605cba8ef1aa8c287a5070accac0fd36
    role: context
  - path: .temp/gtdb-code006-20261115/genus-mixed-384-run-schema-001/start.json
    sha256: 035d893617536cf15efdf8e269eadc17e7cdba8a102a84e228f215dca7527684
    role: context
  - path: .temp/gtdb-code006-20261115/genus-mixed-384-run-strict-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-mixed-384-run-strict-001/native.log
    sha256: 94326dedac7b81b152bf24d09fef4822041d8ec9c6c3062d2d6d4811e197bf50
    role: context
  - path: .temp/gtdb-code006-20261115/genus-mixed-384-run-strict-001/receipt.json
    sha256: 36b56eb1f59ce4b8d4931902d955fa83fccccf68ef89b0836719900bd1632a6b
    role: context
  - path: .temp/gtdb-code006-20261115/genus-mixed-384-run-strict-001/start.json
    sha256: d65174eaf170eb34df70cadeb1af4ffd94162e7bbeed93f4acb4c560b6f40edb
    role: context
  - path: .temp/gtdb-code006-20261115/genus-mixed-384-run-strict-001/strict.tsv
    sha256: b184ed5450b968070bb6c75648407e388f41a1eaf7017890723cf560999fc3f7
    role: context
  - path: .temp/gtdb-code006-20261115/genus-mixed-384-run-terms-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/genus-mixed-384-run-terms-001/native.log
    sha256: 7418d6889c3700114c65084b18f7c4a61138720d62661500fa9c401ceccbbdb3
    role: context
  - path: .temp/gtdb-code006-20261115/genus-mixed-384-run-terms-001/receipt.json
    sha256: fc535a7d2b579e30bcffa6b284bcf55fb87b1b23e3bc03cb376effe6406ba7e9
    role: context
  - path: .temp/gtdb-code006-20261115/genus-mixed-384-run-terms-001/start.json
    sha256: dc3cd666131542ac88d2d1b27ebb973fc020ac6574929cdf93351b834d1bb874
    role: context
  - path: .temp/gtdb-code006-20261115/genus-mixed-six-route-plan-001.json
    sha256: 60d4e9a06c8a1ef6c203eb47aa9b13369807e6bc38ca8997131468e578ea1512
    role: context
  - path: .temp/gtdb-code006-20261115/kg-microbe/data/raw/NCBI2GTDB.tsv.gz
    sha256: 761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd
    role: context
  - path: .temp/phase2-schema-20261115/genus-mixed-384-bind-canary-001.log
    sha256: 2807c5a43b6221eb4fc372abd3d36d293166cc3f1973cc0f65fd229bb7c39a4f
    role: context
  - path: .temp/phase2-schema-20261115/genus-mixed-six-route-batch-001.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/phase2-schema-20261115/genus-mixed-six-route-batch-001.json
    sha256: 9c771fde6e5e231057fddc9dca050b1dad10fb83f63644e8304f73b54f876cf5
    role: context
  - path: .temp/phase2-schema-20261115/genus-mixed-six-route-batch-001.log
    sha256: b43cd1b413f8b8045fb05985912d2d2d891f39c3236bb5e8ac19a52cb4b42e25
    role: context
  - path: history/records/Dairy_Wastewater_Algal_Cyanobacterial_Cultivation_Panel/2026-09-15T103307Z-codex-c7ce53.yaml
    sha256: c006f934e9c7513b3db2ba73e63b3934e0e48a26200f6a063d97708d0d328db9
    role: context
  - path: history/records/Dairy_Wastewater_Algal_Cyanobacterial_Cultivation_Panel/2026-10-06T195342Z-codex-bf5610.yaml
    sha256: 756bc94254624bb359bdee5473199c69c24cd0c94953c93f19ae198a7baf9694
    role: context
  - path: history/records/Dairy_Wastewater_Algal_Cyanobacterial_Cultivation_Panel/2026-11-15T093248Z-codex-3f2d44.yaml
    sha256: 2da658ef8b90e3836e62c80f053fe83e43a1756b1477ee6e3bcd19dcb17cbd5d
    role: context
  - path: justfile
    sha256: 40369611ad4531582e420df0e9ff22109e4b18adf03b34d86b54200b280f2d0f
    role: context
  - path: kb/communities/Dairy_Wastewater_Algal_Cyanobacterial_Cultivation_Panel.yaml
    sha256: 0b837a73e603469d21643996c0564bdbc93d1f9852833fb789529257965dbce1
    role: target
  - path: pyproject.toml
    sha256: be952f0f137f85fed66bda0908f12014f1797a2dd229b44d832afc0c00471655
    role: context
  - path: references_cache/PMID_41561919.txt
    sha256: 815ea25a152efcf13f2c82c6f96165671cfa5ab978ce71207cd6de6f51bf4f21
    role: context
  - path: reports/causal_graph_review/decisions/20261006-kefir-dairy-batch59.yaml
    sha256: 6eb7cba4bcbbfee3ba456be7cc886f59f3a032845a7c2ad252174cf2afb9f5f0
    role: context
  - path: reports/gtdb-code006-20261115/genus-mixed-384-authored-source-context-001.json
    sha256: 1b1d8840b2d1179a8bf23767282ad679c019cdc8e305a9cf85d500bb956a2c80
    role: context
  - path: reports/gtdb-code006-20261115/genus-mixed-384-review-config-001.json
    sha256: acfceabe0bc98b53599dd4f081d944f64b3e224d434b1ff96306fec2364c187a
    role: context
  - path: reports/gtdb-code006-20261115/genus-mixed-384-source-config-001.json
    sha256: bced18d04d14f0ffdf5accb056eb222b80c2244c2b04f475955bb5855800d8a9
    role: context
  - path: reports/gtdb-code006-20261115/genus-mixed-384-source-evidence-001.json
    sha256: 5790f4b06985803431aa2064689a674f6bdfc35718ba8d930b649c23433efc29
    role: context
  - path: reports/phase2-completion-20261115/genus-mixed-three-source-context-001.yaml
    sha256: a2d816364a8c8906e68a1c8401a5b0df0755c21ee6173ea514851ff730fd4d2a
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
  - path: scripts/adhoc/compose_gtdb_source_config_20261115.jq
    sha256: 45f228d7cbd89ac7b39ff0f470d6a7602e822b866133d2f9a1b462ce38f9d5a5
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
  - path: tests/test_causal_review_batch59.py
    sha256: e0f66a2803e94f4b35920fdc3296f504753b05761427427c5f411d4fe811afea
    role: context
  - path: uv.lock
    sha256: 712838f8fa3d68fbd818ac8162f3f1e2f2637db1da1a8ebfaba0ef759690f3b4
    role: context
targets:
- target_id: CommunityMech:000384
  path: kb/communities/Dairy_Wastewater_Algal_Cyanobacterial_Cultivation_Panel.yaml
  selector: taxonomy[0:2].taxon_term.gtdb_classification; gtdb_grounding_status
  label: Synechocystis genus and Desertifilum species descriptors without stock-genome
    identification
  kind: maintained
  ownership_note: CommunityMech owns this record; only declared GTDB correspondence/status
    and actual provenance are assessed.
scope:
  description: Exactly two declared GTDB blocks/statuses, two native inline events
    and the actual source/application/history/gate provenance for CommunityMech:000384.
    This is a partial mixed-rank database-correspondence diagnostic, not a complete
    scientific review of the cultivation panel.
  selection: One whole-record mixed-rank canary selected from six source-prepared
    records. Only CommunityMech:000384 is reviewed here; the six-record source-report
    denominator is preparation context, not the reviewed population. No remaining
    mixed or family-route application is approved by this diagnostic alone.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000384
  exclusions:
  - target: Other scientific claims and records
    reason: Existing biology is preserved, not newly certified by this database diagnostic.
checks:
- check_id: 000384-schema
  name: validate
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000384
  command: just --verbose --no-dotenv --color never validate kb/communities/Dairy_Wastewater_Algal_Cyanobacterial_Cultivation_Panel.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000384-schema
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000384-strict
  name: validate-strict
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000384
  command: just --verbose --no-dotenv --color never validate-strict kb/communities/Dairy_Wastewater_Algal_Cyanobacterial_Cultivation_Panel.yaml
    --out .temp/gtdb-code006-20261115/genus-mixed-384-run-strict-001/strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000384-strict
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000384-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000384
  command: just --verbose --no-dotenv --color never validate-gtdb kb/communities/Dairy_Wastewater_Algal_Cyanobacterial_Cultivation_Panel.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000384-gtdb
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000384-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000384
  command: just --verbose --no-dotenv --color never validate-gtdb-domain kb/communities/Dairy_Wastewater_Algal_Cyanobacterial_Cultivation_Panel.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000384-domain
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000384-scalars
  name: validate-scalars
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000384
  command: just --verbose --no-dotenv --color never validate-scalars kb/communities/Dairy_Wastewater_Algal_Cyanobacterial_Cultivation_Panel.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000384-scalars
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000384-history
  name: validate-history
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000384
  command: just --verbose --no-dotenv --color never validate-history history/records/Dairy_Wastewater_Algal_Cyanobacterial_Cultivation_Panel
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000384-history
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000384-new-history
  name: new-history
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000384
  command: just --verbose --no-dotenv --color never new-history --kind record --slug
    Dairy_Wastewater_Algal_Cyanobacterial_Cultivation_Panel --target-root kb/communities
    --event EDIT --outcome changed --sections taxonomy,curation_history --actor-name
    codex --model gpt-6 --agent-tool codex --issue https://github.com/CultureBotAI/CommunityMech/issues/2848
    --summary 'Add bounded genus and species reference correspondences to the dairy
    cultivation panel' --details 'The reviewed native candidate adds the Synechocystis
    genus correspondence (8/8 filtered reference genomes), the existing Desertifilum
    tharense descriptor'"'"'s exact-ID species correspondence (one reference genome),
    matching statuses and two native inline events. Preserve all four descriptors,
    absent strain identifiers, both eukaryotic NO_GTDB_EQUIVALENT statuses, source
    quotations, old history and the empty ecological graph. Four monocultures, four
    paired cultures and four sequential cultures remain distinct treatments; these
    reference correspondences do not identify experimental stocks or assemblies, establish
    a four-member inoculum or demonstrate nutrient exchange. Retain non-sterile background
    and unresolved treatment-specific causal structure under issue 1537. Source binding
    and local staging ran at ead20c0; actual M5 staging/application ran at published
    70ef731c using the same captured inputs. The mapping table'"'"'s file mtime is
    not its release. This is partial database-correspondence work, not a full scientific
    review. Actual apply receipt .temp/gtdb-code006-20261115/genus-mixed-384-applied-m5-001/receipt.json
    sha256:1aad8d549e9ba0a799d39acf76998467cfa85c76d1f5babe23aa576f6fb96383.'
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000384-new-history
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000384-terms
  name: validate-terms
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000384
  command: just --verbose --no-dotenv --color never validate-terms kb/communities/Dairy_Wastewater_Algal_Cyanobacterial_Cultivation_Panel.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000384-terms
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
evidence:
- evidence_id: 000384-schema
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-mixed-384-run-schema-001/native.log
  accessed_at: '2026-11-15T09:34:33.285428Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000384-strict
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-mixed-384-run-strict-001/native.log
  accessed_at: '2026-11-15T09:34:33.285428Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000384-gtdb
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-mixed-384-run-gtdb-001/native.log
  accessed_at: '2026-11-15T09:34:33.285428Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000384-domain
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-mixed-384-run-domain-001/native.log
  accessed_at: '2026-11-15T09:34:33.285428Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000384-scalars
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-mixed-384-run-scalars-001/native.log
  accessed_at: '2026-11-15T09:34:33.285428Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000384-history
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-mixed-384-run-history-001/native.log
  accessed_at: '2026-11-15T09:34:33.285428Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000384-new-history
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-mixed-384-run-new-history-001/native.log
  accessed_at: '2026-11-15T09:34:33.285428Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000384-terms
  kind: validation
  reference: .temp/gtdb-code006-20261115/genus-mixed-384-run-terms-001/native.log
  accessed_at: '2026-11-15T09:34:33.285428Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000384-paper
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/41561919/
  locator: Retained data-article Methods and Table 3; exact MC1/MC2 anchor and primary_contexts
    in the bound source metadata
  support: supports
  summary: The source names Synechocystis sp. and Desertifilum tharense without formal
    strain identifiers and assigns them to distinct mono-, paired and sequential cultivation
    groups. This does not establish exact reference-genome identity.
  accessed_at: '2026-11-15T09:34:33.285428Z'
- evidence_id: 000384-database
  kind: database
  reference: reports/gtdb-code006-20261115/genus-mixed-384-source-evidence-001.json
  locator: occurrences[taxonomy_index=0,1], exact term selectors, native_result and
    ncbi_identity_rows
  support: supports
  summary: NCBITaxon1142 remains genus rank with the native 8/8 Synechocystis reference
    population. NCBITaxon1185873 remains species rank with one exact-ID Desertifilum
    tharense reference genome. No new taxon label, stock or assembly assertion follows.
  accessed_at: '2026-11-15T09:34:33.285428Z'
- evidence_id: 000384-application
  kind: record_content
  reference: .temp/gtdb-code006-20261115/genus-mixed-384-applied-m5-001/receipt.json
  locator: actual before/after/input binding, two native inline events and bound appended
    sidecar
  support: supports
  summary: The guarded M5 application persisted the independently accepted candidate.
    Its only semantic changes are the two declared correspondence blocks/statuses
    and native events; all biology, quotations, prior history and exclusions remain
    protected.
  accessed_at: '2026-11-15T09:34:33.285428Z'
- evidence_id: 000384-prior
  kind: prior_review
  reference: reports/causal_graph_review/decisions/20261006-kefir-dairy-batch59.yaml
  locator: Dairy record needs_research disposition and unchanged source/graph boundaries;
    separate kefir record remains outside this unit
  support: context_only
  summary: The historical scientific review leaves treatment-specific interaction
    structure unresolved. The empty graph is not evidence that biological interactions
    are absent; source-grounded descriptor correspondence does not revise that assessment.
  accessed_at: '2026-11-15T09:34:33.285428Z'
assessments:
- assessment_id: 000384-identity
  area: grounding
  topic: Source-compatible rank and treatment identity
  outcome: supported
  target_ids:
  - CommunityMech:000384
  evidence_ids:
  - 000384-paper
  - 000384-database
  - 000384-terms
  summary: The genus-only Synechocystis and named Desertifilum species descriptors
    retain their original scope and absent strain identifiers. All four panel descriptors
    and treatment memberships remain distinct.
- assessment_id: 000384-population
  area: grounding
  topic: Mixed-rank reference populations without stock assignment
  outcome: supported
  target_ids:
  - CommunityMech:000384
  evidence_ids:
  - 000384-database
  - 000384-gtdb
  - 000384-domain
  summary: The native 8/8 genus population and one-genome exact-ID species result
    establish bounded database correspondences. They do not identify study genomes,
    infer a four-member inoculum or change the two eukaryotic exclusions.
- assessment_id: 000384-provenance
  area: provenance
  topic: Actual guarded transition with historical science preserved
  outcome: supported
  target_ids:
  - CommunityMech:000384
  evidence_ids:
  - 000384-application
  - 000384-prior
  - 000384-schema
  - 000384-strict
  - 000384-scalars
  - 000384-new-history
  - 000384-history
  summary: The accepted candidate was applied on the isolated frozen M5 revision,
    with eight scoped native commands and one appended sidecar. Old scientific uncertainty,
    biological predicates, source quotations and history remain unchanged; remaining
    mixed-route units await the complete saved canary proof.
findings: []
actions: []
limitations:
- Partial technical review with scientific_review:false. Native technical completion
  does not establish full scientific review, source-snippet validation, generated-page
  integration, final corpus QC or campaign completion.
- The native Synechocystis genus result is 8/8 filtered reference genomes. The Desertifilum
  tharense exact-ID species result contains one reference genome. Neither population
  identifies the unnamed experimental stocks or establishes that the study used a
  particular reference assembly.
- Source examination was limited to retained data-article Methods and Table 3 passages.
  This pass did not newly acquire or completely review the associated research article,
  supplements, figure pixels, raw amplicon data or study assemblies.
- Four monocultures, four paired cultures and four sequential cultures remain separate
  treatments. The four listed descriptors are not a universal four-member inoculum;
  indigenous non-sterile bacteria remain outside the exact canonical roster.
- Chlorella sorokiniana and Euglena gracilis retain NO_GTDB_EQUIVALENT. Source-supported
  genus versus species rank, absent formal strain fields and all treatment memberships
  remain unchanged.
- The empty ecological graph remains an unresolved research gap under the historical
  batch 59 assessment and issue 1537. Endpoint profiles, predicted functions and associations
  do not establish gene activity, exchanged flux or selective mediation. This correspondence
  correction makes no issue disposition.
- Source reporting, binding and the first private stage ran locally at ead20c0392805c2810d49e9a57aa2fd710578145.
  The actual M5 stage, application and scoped gates ran at published 70ef731cc6c35d9ffe08a391c9db2b4adb10abf4
  with native Python 3.13.2. Post-application receipts are not clean-tree runs. The
  original local candidate remains retained; its only content difference from the
  accepted M5 candidate is the two actual native timestamps.
- The exact crosswalk hash is 761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd;
  file mtime is not a release identifier. Local NCBI identity/rank observations are
  stat-bound, not full database checksum claims.
- Native terms report Validation passed without an assertion denominator. Strict successor
  admission, historical caller checks and generated-page integration remain separate
  follow-up checks; technical gates do not count examined scientific assertions.
links:
- https://github.com/CultureBotAI/CommunityMech/issues/2848
- https://github.com/CultureBotAI/CommunityMech/issues/1537
- https://github.com/CultureBotAI/CommunityMech/pull/2853
```
