# Coculture Faecalibacterium descriptor: scoped M5 ambiguity diagnostic

- Review: 20261115T070517Z-coculture-faecalibacterium-ambiguity-diagnostic
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-11-15T07:05:17.779350Z
- Finished UTC: 2026-11-15T07:05:17.904080Z
- Reviewer: codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: false

## Summary

The existing Faecalibacterium prausnitzii species descriptor has three native alternatives in the exact pinned crosswalk. The guarded M5 correction records AMBIGUOUS and all three alternatives without selecting a GTDB identity for study stock A2-165/JCM31915. B. bifidum's existing classification, both study stocks, all biological claims and prior history remain unchanged. Actual application, native append-only history and eight required commands are bound.

## Scope And Provenance

The taxonomy[1] GTDB status and complete alternatives, source/stock boundary, actual application and scoped native checks. This is not a new whole-record scientific review.

Selection: One whole record, CommunityMech:000401, chosen as the first status-only unit through the shared engine after its accepted species-reference canary and the completed separate 000546 ambiguity canary. No wider status-only batch precedes this saved unit.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 506038c07f3395bce2d8d6bde20d5992f79b3490.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000401 | kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml # taxonomy[1].taxon_term.gtdb_grounding_status; taxonomy[1].taxon_term.gtdb_candidates | maintained | Complete native descriptor alternatives with study-stock uncertainty preserved |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000401 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-strict | passed | True | CommunityMech:000401 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-gtdb | passed | True | CommunityMech:000401 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-gtdb-domain | passed | True | CommunityMech:000401 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-scalars | passed | True | CommunityMech:000401 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-history | passed | True | CommunityMech:000401 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| new-history | passed | True | CommunityMech:000401 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-terms | passed | True | CommunityMech:000401 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |

## Scientific And Domain Assessments

### Reported stock versus descriptor correspondence

grounding: supported. Targets: CommunityMech:000401.

Retain source A2-165/JCM31915 naming and canonical NCBITaxon:853. The complete database alternative set does not establish the study strain's species cluster or settle the cited F. duncaniae nomenclature context.

### Complete native ambiguity set without stock inference

grounding: supported. Targets: CommunityMech:000401.

AMBIGUOUS and all three native candidates now reproduce the exact current descriptor route. No new GTDB classification block, chosen species, probability or denominator was invented; the B. bifidum block is unchanged.

### Actual bounded write and native checks with historical science retained

provenance: supported. Targets: CommunityMech:000401.

The actual receipt, preserved predecessor, native candidate, exact source inputs, append-only sidecar and eight completed commands support this partial technical disposition. Original scientific ledgers remain immutable; full scientific approval and corpus completion are not asserted.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| 000401-schema | .temp/gtdb-ambiguity-20261115/status401-check-schema-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000401-strict | .temp/gtdb-ambiguity-20261115/status401-check-strict-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000401-gtdb | .temp/gtdb-ambiguity-20261115/status401-check-gtdb-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000401-domain | .temp/gtdb-ambiguity-20261115/status401-check-domain-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000401-scalars | .temp/gtdb-ambiguity-20261115/status401-check-scalars-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000401-history | .temp/gtdb-ambiguity-20261115/status401-check-history-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000401-new-history | .temp/gtdb-ambiguity-20261115/status401-check-new-history-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000401-terms | .temp/gtdb-ambiguity-20261115/status401-check-terms-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000401-paper | https://doi.org/10.3390/microorganisms14081812; Methods2.1; retained cache character1763/line12, Discussion character6818/line32; independently retained PMC13515949 XML | supports | Methods identifies A2-165/JCM31915 and B. bifidum JCM1254. The Discussion explicitly says metabolic flux was not directly measured. This supports preserving the reported stocks and inference limits; it does not select an exact-stock GTDB species. |
| 000401-database | reports/gtdb-ambiguity-20261115/status401-source-evidence-001.json; occurrences[0].native_result/classify_status/ncbi_identity_rows; primary_locators | supports | Exact pinned native species-name resolution of NCBITaxon:853 yields F. longum, F. prausnitzii and F. prausnitzii_D. The current M5 NCBI label/rank agrees with the captured descriptor; all alternatives remain explicit with no stock placement or population denominator inferred. |
| 000401-application | .temp/gtdb-ambiguity-20261115/status401-m5-applied-001/receipt.json; applied/before_sha256/after_sha256/inputs | supports | Actual guarded M5 replacement persisted the independently accepted candidate: one status, three candidate identifiers and one native inline event. All other canonical science and previous history remain exact. The native sidecar and all eight current command receipts are separately hash-bound. |
| 000401-prior | reports/causal_graph_review/decisions/20261005-eleven-records-batch6.yaml; CommunityMech:000401 plus immutable20261104-c6s5-review-remediation.yaml current-predecessor chain | context_only | Historical scientific decisions and later abundance remediation remain unchanged. The two graph nodes distinguish an observed ratio-dependent butyrate peak from inferred donor transfer; this diagnostic does not replace those judgments or resolve the open pH/substrate/flux discussion. |

## Limits And Additional Notes

- Partial technical/provenance assessment with scientific_review:false; no full scientific approval, corpus QC pass, or release clearance.
- The alternatives belong to the current stored NCBI species descriptor, not an independently verified assembly classification of A2-165. Primary Methods uses F. prausnitzii, while a cited 2024 title uses F. duncaniae; that strain-level nomenclature question remains outside this bounded correction.
- The complete candidate set is preserved in native order. No exact-stock identity, support-genome denominator, candidate probability or majority is inferred from an ambiguous route.
- Local and M5 source binders retain separate database file-stat observations. Their label/rank rows agree, but neither the complete NCBI database content nor its release is certified by a whole-database checksum. The crosswalk, source cache, XML, native resolver and all captured assessment files have exact hashes.
- The existing 472-genome B. bifidum block remains byte-for-byte unchanged, including its historical mapping-source wording. This status-only assessment does not independently re-certify that block's release/build claim or exact study-stock placement.
- The open bifido_faecali_2fl_fos_flux_unresolved discussion remains unchanged. Donor-resolved acetate flux, pH and residual-substrate limitations, functional roles and other whole-record scientific questions are not cleared here.
- Seven scoped native validators and native history scaffolding passed. Reference-snippet matching, generated pages, strict historical successor integration and final combined full QC are separately accounted work. Required passing native checks do not make this a full scientific review.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261115T070517Z-coculture-faecalibacterium-ambiguity-diagnostic
kind: record
repository: CultureBotAI/CommunityMech
title: 'Coculture Faecalibacterium descriptor: scoped M5 ambiguity diagnostic'
started_at: '2026-11-15T07:05:17.779350Z'
finished_at: '2026-11-15T07:05:17.904080Z'
reviewer:
  identity: codex
  kind: agent
  independence: self_review
  independence_basis: Authored source and database assessment. Parent independently
    inspected the source plan, actual source anchors, native alternatives, unchanged
    partner block and local candidate; then independently verified the M5 candidate
    and receipt before application. A peer separately reviewed the shared source binder
    and its actual-consumer locator regression. This saved assessment remains authored,
    not an independent full scientific approval.
skill: curate-yaml-record
completion: completed
verdict: pass_with_limitations
scientific_review: false
summary: The existing Faecalibacterium prausnitzii species descriptor has three native
  alternatives in the exact pinned crosswalk. The guarded M5 correction records AMBIGUOUS
  and all three alternatives without selecting a GTDB identity for study stock A2-165/JCM31915.
  B. bifidum's existing classification, both study stocks, all biological claims and
  prior history remain unchanged. Actual application, native append-only history and
  eight required commands are bound.
source:
  git_revision: 506038c07f3395bce2d8d6bde20d5992f79b3490
  state: working_tree
  inputs:
  - path: .temp/gtdb-ambiguity-20261115/faecalibacterium-source-001/article.xml
    sha256: c5b4d94fcd98543be47d7eb623a69180ae15cc98dbe1a3b1ad772818f65d421e
    role: context
  - path: .temp/gtdb-ambiguity-20261115/kg-microbe/data/raw/NCBI2GTDB.tsv.gz
    sha256: 761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd
    role: context
  - path: .temp/gtdb-ambiguity-20261115/shared-route-plan-001.json
    sha256: 6e20ddacc922535f097fe70f5921c145a0e0bb7544ec283601e394116ff05485
    role: context
  - path: .temp/gtdb-ambiguity-20261115/status401-check-config-001.json
    sha256: 883f6c43639e108f2acab691fd3eebc481cdde181963d9e29be4502f18a4b15a
    role: context
  - path: .temp/gtdb-ambiguity-20261115/status401-check-domain-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-ambiguity-20261115/status401-check-domain-001/native.log
    sha256: 683e6dcf7d00a865c94530f92c220a987f38c0377da22c6a0986e33ef98d3afc
    role: context
  - path: .temp/gtdb-ambiguity-20261115/status401-check-domain-001/receipt.json
    sha256: 658ecf3da5e94c0857811d2d3db0c02f349fe8ea5f1feb1af750264402a62cc9
    role: context
  - path: .temp/gtdb-ambiguity-20261115/status401-check-domain-001/start.json
    sha256: feca4841899b024dc36ec8e4707dc7a8bdf7bb18d3846bfd62ae191bcc20a336
    role: context
  - path: .temp/gtdb-ambiguity-20261115/status401-check-gtdb-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-ambiguity-20261115/status401-check-gtdb-001/native.log
    sha256: 70772f50bee1120e999ecd6a0a56e4f95d3eb97cff84bd7a8ba9d97c4733e445
    role: context
  - path: .temp/gtdb-ambiguity-20261115/status401-check-gtdb-001/receipt.json
    sha256: e5ca8b8826fc7ffb7e1ec9663194485697e696c89d605c4a46a4f1adc040bbd1
    role: context
  - path: .temp/gtdb-ambiguity-20261115/status401-check-gtdb-001/start.json
    sha256: 6253077b3cce0cda62fd09aeedf3863ebb225c7e04559539d9d0aa069f9c8568
    role: context
  - path: .temp/gtdb-ambiguity-20261115/status401-check-history-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-ambiguity-20261115/status401-check-history-001/native.log
    sha256: 700b44227c4cf01270ac26f16b308622de0b26f48d71aec49cdfaaab87620f0a
    role: context
  - path: .temp/gtdb-ambiguity-20261115/status401-check-history-001/receipt.json
    sha256: 7db72a93a4a84493cbdaf5fabda37e34c3b44a4ef075523f6c80b2cfd8e75624
    role: context
  - path: .temp/gtdb-ambiguity-20261115/status401-check-history-001/start.json
    sha256: 582ee6fac2c1f1f9f6d8ec0d23f9eeaa1054fd640121c960a5a57a7b17b91a45
    role: context
  - path: .temp/gtdb-ambiguity-20261115/status401-check-new-history-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-ambiguity-20261115/status401-check-new-history-001/native.log
    sha256: 17fbdb199a9d2c13ff63bb450a1b458dc2141f3939fdeae8c245bc6b4c9dfb5b
    role: context
  - path: .temp/gtdb-ambiguity-20261115/status401-check-new-history-001/receipt.json
    sha256: 536a26298e96e40a9f41f64b408377376a674ee762e131556288479e4550a9f2
    role: context
  - path: .temp/gtdb-ambiguity-20261115/status401-check-new-history-001/start.json
    sha256: b6b7b282c901ea4cfc674ebae8e5a43bb933f1eaaad433f38923d302011198a4
    role: context
  - path: .temp/gtdb-ambiguity-20261115/status401-check-scalars-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-ambiguity-20261115/status401-check-scalars-001/native.log
    sha256: 2a9814814a0396b0f0b5858460c1b163dacfb413faa09adb3e00021030c18187
    role: context
  - path: .temp/gtdb-ambiguity-20261115/status401-check-scalars-001/receipt.json
    sha256: 5da9552d342443e8e3530f73b456ae118e67a7b9ff9ee64a1229f5456a4c980a
    role: context
  - path: .temp/gtdb-ambiguity-20261115/status401-check-scalars-001/start.json
    sha256: e8b4ee40896c2de995f8d2aa6adde45a15e4d70aa5b0df2fc5e22c1b2917a943
    role: context
  - path: .temp/gtdb-ambiguity-20261115/status401-check-schema-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-ambiguity-20261115/status401-check-schema-001/native.log
    sha256: f110ad47fd4166a1dd4e31754a7733afe13d3d361b52022db7b567e2a928d541
    role: context
  - path: .temp/gtdb-ambiguity-20261115/status401-check-schema-001/receipt.json
    sha256: 5b7ef3490d21bf2378dda794d9c58d9dbcd2116c6102554a21061125c5494610
    role: context
  - path: .temp/gtdb-ambiguity-20261115/status401-check-schema-001/start.json
    sha256: b7f10b625d86cc412ecd8b36e3442286c6bfe684bab1426841902323d76f1967
    role: context
  - path: .temp/gtdb-ambiguity-20261115/status401-check-strict-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-ambiguity-20261115/status401-check-strict-001/native.log
    sha256: b2ff43535348b3af7e839d2b7e9c98d9ee06fa34e0fde053c051774ebc7538a7
    role: context
  - path: .temp/gtdb-ambiguity-20261115/status401-check-strict-001/receipt.json
    sha256: 729317a5945306e30b9b6ddeb041eefedd40189084d710bab88814f5cdfd4e10
    role: context
  - path: .temp/gtdb-ambiguity-20261115/status401-check-strict-001/start.json
    sha256: 7b121a6ea4a27fb8aa7687da3316bb1efcdcd4ff1aa8cd2126b460cc7e3af861
    role: context
  - path: .temp/gtdb-ambiguity-20261115/status401-check-strict-001/strict.tsv
    sha256: b184ed5450b968070bb6c75648407e388f41a1eaf7017890723cf560999fc3f7
    role: context
  - path: .temp/gtdb-ambiguity-20261115/status401-check-terms-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-ambiguity-20261115/status401-check-terms-001/native.log
    sha256: 975c2125d2f2baa09dea93acc1b926ba823100732037954349b6e2501c01b0bb
    role: context
  - path: .temp/gtdb-ambiguity-20261115/status401-check-terms-001/receipt.json
    sha256: 241e2b62c163789e9462e3634d34d86d4e31b2b67efbeb3aafb9f2383c91d825
    role: context
  - path: .temp/gtdb-ambiguity-20261115/status401-check-terms-001/start.json
    sha256: dc9b2ea0df99d806eafaea2d97bffe0460fab828c6dd3c232d6ed066d8304891
    role: context
  - path: .temp/gtdb-ambiguity-20261115/status401-m5-applied-001/before.yaml
    sha256: c751d65f77ac054c5c8686bb6fd9d0ecf503fe729c1bb5c1d2409bbfe781169e
    role: context
  - path: .temp/gtdb-ambiguity-20261115/status401-m5-applied-001/receipt.json
    sha256: 2416216aa2bc23be9f4963357ba85741e8ad4fea71efada081a7504b68352d58
    role: context
  - path: .temp/gtdb-ambiguity-20261115/status401-m5-stage-001/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml
    sha256: 155b6bb835a8025ba6af96b61ce1d311be1cc6e258391c35a1ccc7985830c76c
    role: context
  - path: .temp/gtdb-ambiguity-20261115/status401-m5-stage-001/receipt.json
    sha256: db846d4e048ea44b97afec0b5c9e993c0057f3bcf1a1cb2014d8e447aec2c985
    role: context
  - path: .temp/phase2-schema-20261115/shared-context-401-m5-001.log
    sha256: 55692a3cba0f798f00f50df156c2c7f67bb21edeaf0a421f4a6603dfe84a4a7e
    role: context
  - path: .temp/phase2-schema-20261115/shared-route-401-001.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/phase2-schema-20261115/shared-route-401-001.json
    sha256: e442eb1328087511c23e7e8035fe50a20c7c6e065fc429388cc5e4989c760155
    role: context
  - path: .temp/phase2-schema-20261115/shared-route-401-001.log
    sha256: 43ad7e32374e657440173e4b25b48768c348e2ad1be2bb3d9481303e1f2aab41
    role: context
  - path: history/records/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture/2026-09-21T023720Z-codex-64dd83.yaml
    sha256: 39c5386f7abbed87c36316495f9b44c7f40ae157e77f2371fc43e0a3529e108f
    role: context
  - path: history/records/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture/2026-09-21T024109Z-codex-f468fd.yaml
    sha256: ecd3755e9bfb361ff922f29791f7da2f4792c709ceb538b6a42e9f4bffd72a29
    role: context
  - path: history/records/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture/2026-10-05T112950Z-codex-4bd70f.yaml
    sha256: 33d82b7786f0178a39bd4c9c935288511e7223b1ed85842764acf7a8a4532472
    role: context
  - path: history/records/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture/2026-11-04T202200Z-antigravity-2113a1.yaml
    sha256: 11dc5adba5073e0acf749722b3fcaf2c072d884cedd2d033dc32894fea0848ff
    role: context
  - path: history/records/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture/2026-11-15T070320Z-codex-3f0524.yaml
    sha256: b8d5afb45b44951f2385a7f83b2339a9428f37862883a82748a2da748b3b4d34
    role: context
  - path: justfile
    sha256: 40369611ad4531582e420df0e9ff22109e4b18adf03b34d86b54200b280f2d0f
    role: context
  - path: kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml
    sha256: 155b6bb835a8025ba6af96b61ce1d311be1cc6e258391c35a1ccc7985830c76c
    role: target
  - path: pyproject.toml
    sha256: be952f0f137f85fed66bda0908f12014f1797a2dd229b44d832afc0c00471655
    role: context
  - path: references_cache/PMID_42655156.txt
    sha256: f40ae202ccae35dad94ef7ed446f94adc2d089879ac64cec97302fc090b35e4c
    role: context
  - path: reports/causal_graph_review/decisions/20261005-eleven-records-batch6.yaml
    sha256: 23f5fa6fc197e020f7cb3469749ebe4aa78886f8973cb6ed63fde321470a7f96
    role: context
  - path: reports/causal_graph_review/decisions/20261104-c6s5-review-remediation.yaml
    sha256: 66e9447171a3a8fe64dc01cea5fecbe01785236b19a2fa21842ad439a7cb22f0
    role: context
  - path: reports/gtdb-ambiguity-20261115/next-status-source-context-001.yaml
    sha256: f2327859cebb6eef868667d8b1e74dacd35ca7a229571885b8c51b9b14e681bb
    role: context
  - path: reports/gtdb-ambiguity-20261115/status401-review-config-001.json
    sha256: f6129485ca99539895678cc2f2fe08094087a1a76df2e33190164b9c2c46b390
    role: context
  - path: reports/gtdb-ambiguity-20261115/status401-source-config-001.json
    sha256: 51a50d66f6bf9d9a89cf52ba1d13f82cfd725663693327660e00b29064030ab6
    role: context
  - path: reports/gtdb-ambiguity-20261115/status401-source-evidence-001.json
    sha256: 34d6cbf11177b94f7a209bc6a317bc9121f100cbb07d59c8df94b7bb9ace8137
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
  - path: tests/test_causal_review_batch6.py
    sha256: ca8cb78977a96609778ce7b102f02fe0b42d32267fdd3781bf6492284c1caec3
    role: context
  - path: uv.lock
    sha256: 712838f8fa3d68fbd818ac8162f3f1e2f2637db1da1a8ebfaba0ef759690f3b4
    role: context
targets:
- target_id: CommunityMech:000401
  path: kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml
  selector: taxonomy[1].taxon_term.gtdb_grounding_status; taxonomy[1].taxon_term.gtdb_candidates
  label: Complete native descriptor alternatives with study-stock uncertainty preserved
  kind: maintained
  ownership_note: CommunityMech owns this record; only declared GTDB correspondence/status
    and actual provenance are assessed.
scope:
  description: The taxonomy[1] GTDB status and complete alternatives, source/stock
    boundary, actual application and scoped native checks. This is not a new whole-record
    scientific review.
  selection: One whole record, CommunityMech:000401, chosen as the first status-only
    unit through the shared engine after its accepted species-reference canary and
    the completed separate 000546 ambiguity canary. No wider status-only batch precedes
    this saved unit.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000401
  exclusions:
  - target: Other scientific claims and records
    reason: Existing biology is preserved, not newly certified by this database diagnostic.
checks:
- check_id: 000401-schema
  name: validate
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000401
  command: just --verbose --no-dotenv --color never validate kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000401-schema
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000401-strict
  name: validate-strict
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000401
  command: just --verbose --no-dotenv --color never validate-strict kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml
    --out .temp/gtdb-ambiguity-20261115/status401-check-strict-001/strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000401-strict
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000401-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000401
  command: just --verbose --no-dotenv --color never validate-gtdb kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000401-gtdb
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000401-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000401
  command: just --verbose --no-dotenv --color never validate-gtdb-domain kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000401-domain
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000401-scalars
  name: validate-scalars
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000401
  command: just --verbose --no-dotenv --color never validate-scalars kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000401-scalars
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000401-history
  name: validate-history
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000401
  command: just --verbose --no-dotenv --color never validate-history history/records/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000401-history
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000401-new-history
  name: new-history
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000401
  command: just --verbose --no-dotenv --color never new-history --kind record --slug
    Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture --target-root kb/communities
    --event EDIT --outcome changed --sections taxonomy,curation_history --actor-name
    codex --model gpt-6 --agent-tool codex --issue https://github.com/CultureBotAI/CommunityMech/issues/2848
    --summary 'Retain all native GTDB alternatives for the coculture Faecalibacterium
    descriptor' --details 'Applied only the independently reviewed UNRESOLVED-to-AMBIGUOUS
    status, all three native candidate identifiers in native order, and one substantive
    native inline event for taxonomy[1], unchanged NCBITaxon:853. The pinned crosswalk
    resolves the existing species descriptor by species name to Faecalibacterium longum,
    Faecalibacterium prausnitzii and Faecalibacterium prausnitzii_D. No candidate
    is selected as the identity of A2-165/JCM31915. Primary Methods stock naming,
    the bibliography'"'"'s unresolved F. duncaniae nomenclature context, source quotes,
    all experimental biology, and the B. bifidum 472-genome classification remain
    unchanged. Exact local and M5 source proofs retain their separate database observations.
    This is a bounded database-status correction, not a full scientific review or
    a new exact-stock genome assignment. Actual apply receipt .temp/gtdb-ambiguity-20261115/status401-m5-applied-001/receipt.json
    sha256:2416216aa2bc23be9f4963357ba85741e8ad4fea71efada081a7504b68352d58.'
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000401-new-history
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000401-terms
  name: validate-terms
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000401
  command: just --verbose --no-dotenv --color never validate-terms kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000401-terms
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
evidence:
- evidence_id: 000401-schema
  kind: validation
  reference: .temp/gtdb-ambiguity-20261115/status401-check-schema-001/native.log
  accessed_at: '2026-11-15T07:05:17.779350Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000401-strict
  kind: validation
  reference: .temp/gtdb-ambiguity-20261115/status401-check-strict-001/native.log
  accessed_at: '2026-11-15T07:05:17.779350Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000401-gtdb
  kind: validation
  reference: .temp/gtdb-ambiguity-20261115/status401-check-gtdb-001/native.log
  accessed_at: '2026-11-15T07:05:17.779350Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000401-domain
  kind: validation
  reference: .temp/gtdb-ambiguity-20261115/status401-check-domain-001/native.log
  accessed_at: '2026-11-15T07:05:17.779350Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000401-scalars
  kind: validation
  reference: .temp/gtdb-ambiguity-20261115/status401-check-scalars-001/native.log
  accessed_at: '2026-11-15T07:05:17.779350Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000401-history
  kind: validation
  reference: .temp/gtdb-ambiguity-20261115/status401-check-history-001/native.log
  accessed_at: '2026-11-15T07:05:17.779350Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000401-new-history
  kind: validation
  reference: .temp/gtdb-ambiguity-20261115/status401-check-new-history-001/native.log
  accessed_at: '2026-11-15T07:05:17.779350Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000401-terms
  kind: validation
  reference: .temp/gtdb-ambiguity-20261115/status401-check-terms-001/native.log
  accessed_at: '2026-11-15T07:05:17.779350Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000401-paper
  kind: primary_source
  reference: https://doi.org/10.3390/microorganisms14081812
  locator: Methods2.1; retained cache character1763/line12, Discussion character6818/line32;
    independently retained PMC13515949 XML
  support: supports
  summary: Methods identifies A2-165/JCM31915 and B. bifidum JCM1254. The Discussion
    explicitly says metabolic flux was not directly measured. This supports preserving
    the reported stocks and inference limits; it does not select an exact-stock GTDB
    species.
  accessed_at: '2026-11-15T07:05:17.779350Z'
- evidence_id: 000401-database
  kind: database
  reference: reports/gtdb-ambiguity-20261115/status401-source-evidence-001.json
  locator: occurrences[0].native_result/classify_status/ncbi_identity_rows; primary_locators
  support: supports
  summary: Exact pinned native species-name resolution of NCBITaxon:853 yields F.
    longum, F. prausnitzii and F. prausnitzii_D. The current M5 NCBI label/rank agrees
    with the captured descriptor; all alternatives remain explicit with no stock placement
    or population denominator inferred.
  accessed_at: '2026-11-15T07:05:17.779350Z'
- evidence_id: 000401-application
  kind: record_content
  reference: .temp/gtdb-ambiguity-20261115/status401-m5-applied-001/receipt.json
  locator: applied/before_sha256/after_sha256/inputs
  support: supports
  summary: 'Actual guarded M5 replacement persisted the independently accepted candidate:
    one status, three candidate identifiers and one native inline event. All other
    canonical science and previous history remain exact. The native sidecar and all
    eight current command receipts are separately hash-bound.'
  accessed_at: '2026-11-15T07:05:17.779350Z'
- evidence_id: 000401-prior
  kind: prior_review
  reference: reports/causal_graph_review/decisions/20261005-eleven-records-batch6.yaml
  locator: CommunityMech:000401 plus immutable20261104-c6s5-review-remediation.yaml
    current-predecessor chain
  support: context_only
  summary: Historical scientific decisions and later abundance remediation remain
    unchanged. The two graph nodes distinguish an observed ratio-dependent butyrate
    peak from inferred donor transfer; this diagnostic does not replace those judgments
    or resolve the open pH/substrate/flux discussion.
  accessed_at: '2026-11-15T07:05:17.779350Z'
assessments:
- assessment_id: 000401-identity
  area: grounding
  topic: Reported stock versus descriptor correspondence
  outcome: supported
  target_ids:
  - CommunityMech:000401
  evidence_ids:
  - 000401-paper
  - 000401-database
  - 000401-terms
  summary: Retain source A2-165/JCM31915 naming and canonical NCBITaxon:853. The complete
    database alternative set does not establish the study strain's species cluster
    or settle the cited F. duncaniae nomenclature context.
- assessment_id: 000401-candidates
  area: grounding
  topic: Complete native ambiguity set without stock inference
  outcome: supported
  target_ids:
  - CommunityMech:000401
  evidence_ids:
  - 000401-database
  - 000401-gtdb
  - 000401-application
  summary: AMBIGUOUS and all three native candidates now reproduce the exact current
    descriptor route. No new GTDB classification block, chosen species, probability
    or denominator was invented; the B. bifidum block is unchanged.
- assessment_id: 000401-provenance
  area: provenance
  topic: Actual bounded write and native checks with historical science retained
  outcome: supported
  target_ids:
  - CommunityMech:000401
  evidence_ids:
  - 000401-application
  - 000401-new-history
  - 000401-history
  - 000401-schema
  - 000401-strict
  - 000401-domain
  - 000401-scalars
  - 000401-prior
  summary: The actual receipt, preserved predecessor, native candidate, exact source
    inputs, append-only sidecar and eight completed commands support this partial
    technical disposition. Original scientific ledgers remain immutable; full scientific
    approval and corpus completion are not asserted.
findings: []
actions: []
limitations:
- Partial technical/provenance assessment with scientific_review:false; no full scientific
  approval, corpus QC pass, or release clearance.
- The alternatives belong to the current stored NCBI species descriptor, not an independently
  verified assembly classification of A2-165. Primary Methods uses F. prausnitzii,
  while a cited 2024 title uses F. duncaniae; that strain-level nomenclature question
  remains outside this bounded correction.
- The complete candidate set is preserved in native order. No exact-stock identity,
  support-genome denominator, candidate probability or majority is inferred from an
  ambiguous route.
- Local and M5 source binders retain separate database file-stat observations. Their
  label/rank rows agree, but neither the complete NCBI database content nor its release
  is certified by a whole-database checksum. The crosswalk, source cache, XML, native
  resolver and all captured assessment files have exact hashes.
- The existing 472-genome B. bifidum block remains byte-for-byte unchanged, including
  its historical mapping-source wording. This status-only assessment does not independently
  re-certify that block's release/build claim or exact study-stock placement.
- The open bifido_faecali_2fl_fos_flux_unresolved discussion remains unchanged. Donor-resolved
  acetate flux, pH and residual-substrate limitations, functional roles and other
  whole-record scientific questions are not cleared here.
- Seven scoped native validators and native history scaffolding passed. Reference-snippet
  matching, generated pages, strict historical successor integration and final combined
  full QC are separately accounted work. Required passing native checks do not make
  this a full scientific review.
links:
- https://github.com/CultureBotAI/CommunityMech/issues/2848
- https://github.com/CultureBotAI/CommunityMech/pull/2804
```
