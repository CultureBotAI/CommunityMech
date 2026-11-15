# Alseth phage community: species references and complete Burkholderia ambiguity

- Review: 20261115T110020Z-alseth-species-reference-diagnostic
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-11-15T11:00:20.153567Z
- Finished UTC: 2026-11-15T11:00:20.335101Z
- Reviewer: codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: false

## Summary

Three existing bacterial species descriptors now carry native reference correspondences and GROUNDED status. The Burkholderia cenocepacia descriptor carries the complete two-way native ambiguity without selecting a species for J2315. Stock descriptions, the virus exclusion, biological graph, source quotations and old history are preserved. This diagnostic does not newly approve the whole scientific record.

## Scope And Provenance

Four declared bacterial taxonomy occurrences in CommunityMech:000467: three native species correspondence blocks/statuses, one complete ambiguous status/candidate list, two native inline events and the actual source/application/history/gate chain. The phage descriptor and all biological assertions remain outside the changed fields.

Selection: One whole-record species-plus-ambiguity canary from the prepared 467/468 pair. The reviewed population is exactly one record. The five-genus PHA record 468 is excluded from this diagnostic and cannot be counted complete from this canary.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9276e66296f8063522d34e553e91260fbe9f1a5f.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000467 | kb/communities/Alseth_FourSpecies_Pathogen_Phage_Community.yaml # taxonomy[0:4].taxon_term.gtdb_classification; gtdb_grounding_status; gtdb_candidates | maintained | Species-reference correspondences and complete J2315 descriptor ambiguity |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000467 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-strict | passed | True | CommunityMech:000467 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-gtdb | passed | True | CommunityMech:000467 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-gtdb-domain | passed | True | CommunityMech:000467 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-scalars | passed | True | CommunityMech:000467 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-history | passed | True | CommunityMech:000467 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| new-history | passed | True | CommunityMech:000467 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-terms | passed | True | CommunityMech:000467 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |

## Scientific And Domain Assessments

### Existing species descriptors and experimental-stock boundaries

grounding: supported. Targets: CommunityMech:000467.

The four selected bacterial descriptors retain their source-compatible species anchors and named stock fields. The PA14 treatment backgrounds remain distinct and no phage, genotype or exact assembly is newly identified by this mapping.

### Three reference populations and complete two-way ambiguity

grounding: supported. Targets: CommunityMech:000467.

The accepted native results support the three exact species-reference blocks and preserve both Burkholderia alternatives through AMBIGUOUS status. Pseudomonas fraction 0.99 is a reference majority rather than unanimity; no candidate choice or study-stock genome claim is introduced.

### Guarded actual transition and preserved historical science

provenance: supported. Targets: CommunityMech:000467.

The independently reviewed candidate and exact source bytes were applied through the guarded native writer, followed by the eight scoped commands and actual appended history. The prior biological contract and scientific uncertainty remain unchanged; strict successor and composed integration checks are separate follow-up work.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| 000467-schema | .temp/gtdb-code006-20261115/phage-pair-467-run-schema-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000467-strict | .temp/gtdb-code006-20261115/phage-pair-467-run-strict-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000467-gtdb | .temp/gtdb-code006-20261115/phage-pair-467-run-gtdb-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000467-domain | .temp/gtdb-code006-20261115/phage-pair-467-run-domain-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000467-scalars | .temp/gtdb-code006-20261115/phage-pair-467-run-scalars-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000467-history | .temp/gtdb-code006-20261115/phage-pair-467-run-history-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000467-new-history | .temp/gtdb-code006-20261115/phage-pair-467-run-new-history-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000467-terms | .temp/gtdb-code006-20261115/phage-pair-467-run-terms-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000467-paper | https://doi.org/10.1371/journal.pbio.3002346; Retained main-text Methods bacterial-strain paragraphs and Results resistance-classification passage; exact primary_locators in bound source metadata | supports | The source identifies the PA14 backgrounds and the FZ21, 13 S44 S9 and J2315 stocks. It separates phenotypic resistance from unperformed receptor-mutant sequencing and distinguishes phage-free abundance observations from phage effects. These passages do not classify an experimental assembly into GTDB. |
| 000467-database | reports/gtdb-code006-20261115/phage-pair-467-source-evidence-001.json; occurrences[taxonomy_index=0,1,2,3], native_result, lookup_indexes and ncbi_identity_rows | supports | The exact pinned table and unchanged native resolver return three species correspondences through exact NCBI IDs and the complete two-option Burkholderia name route. Local NCBI authority confirms the existing species ranks and labels. The reference populations do not identify the study stocks' genomes. |
| 000467-application | .temp/gtdb-code006-20261115/phage-pair-467-applied-001/receipt.json; actual before/after, externally reviewed candidate/receipt hashes and source inputs; two native events and appended sidecar | supports | The exact reviewed candidate was persisted on isolated M5. The semantic delta is limited to the four selected descriptors and two native inline events; stock notes, viral exclusion, biological graph, source quotes and old history remain unchanged. |
| 000467-prior | reports/causal_graph_review/decisions/20261014-phage-graphs-batch130.yaml; CommunityMech:000467 historical decisions and current test_causal_review_batch130.py contract/mutation controls | context_only | The immutable graph ledger and current biological predicates preserve five nodes, three directed edges, qualified mediation, model conditions and the open scientific discussions. This scoped technical successor does not rewrite the historical scientific decisions or certify an additional whole-record review. |

## Limits And Additional Notes

- Partial technical assessment with scientific_review:false. Diagnostic completion and eight native scoped gates do not establish a full scientific review, measured source-assertion coverage, final corpus QC, generated-page integration or campaign completion.
- The three species reference populations are 17191 genomes at native fraction 0.99 for Pseudomonas aeruginosa, 15884 at 1.0 for Acinetobacter baumannii and 37403 at 1.0 for Staphylococcus aureus. These are crosswalk populations, not experimental stock genomes, isolate counts, relative abundances or identity probabilities. The first native fraction is rounded and is not a unanimity claim.
- The complete Burkholderia cenocepacia name route has two alternatives, GTDB:s__Burkholderia_cenocepacia and GTDB:s__Burkholderia_orbicola. No single assignment, exact assembly classification or stock renaming is inferred for J2315.
- Both streptomycin-marked UCBPP-PA14 wild type and the isogenic CRISPR-KO background remain separate experimental contexts. FZ21, 13 S44 S9 and J2315 retain their source stock identities. DMS3vir remains excluded from GTDB bacterial/archaeal correspondence; the acrF1 experimental derivative does not become an additional canonical member.
- Source examination was limited to the retained main-text Methods and Results passages identified in the source context, the whole current record and its historical scientific guard. No new full-paper review, supplemental reanalysis, figure-pixel inspection or stock-assembly analysis was performed for this technical successor.
- Resistance categories remain phenotype-based; the receptor mutants were not sequenced. The no-phage abundance experiments remain distinct from phage effects. Competitive-release mediation and the condition-specific gLV model remain qualified, with the existing open discussions unchanged.
- All five graph nodes, three directed edges, original quotations, clinical-isolation notes, culture conditions and old history remain unchanged. The historical notes about unavailable mapping data describe the earlier curation context; this successor does not rewrite those observations or imply that no mapping table exists now.
- Source reporting and binding ran locally at ab770f2602416a54835b382e881c7535b5b3e576 with the recorded untracked preparation files. Actual M5 staging, application and native gates ran at frozen 9276e66296f8063522d34e553e91260fbe9f1a5f with native Python 3.13.2. Post-application receipts disclose the accepted record change and subsequent native sidecar.
- The mapping table is pinned by SHA-256 761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd. Its mtime is not a release identifier. Native local ontology observations retain their actual stat-based provenance rather than an invented fresh full-database digest.
- Native term validation is reported literally without an assertion denominator. Historical scientific callers and strict successor admission are separate follow-up controls; passing technical validators does not establish biological truth. No issue is closed by this review.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261115T110020Z-alseth-species-reference-diagnostic
kind: record
repository: CultureBotAI/CommunityMech
title: 'Alseth phage community: species references and complete Burkholderia ambiguity'
started_at: '2026-11-15T11:00:20.153567Z'
finished_at: '2026-11-15T11:00:20.335101Z'
reviewer:
  identity: codex
  kind: agent
  independence: self_review
  independence_basis: A peer independently read the authored source contexts, retained
    primary Methods and Results, current records and historical caller. Parent independently
    reviewed the exact actual M5 candidate and receipt before the guarded application.
    The unchanged shared native engine, checker, review builder and evidence exporter
    have separate code reviews and mutation controls. This is self-review of the resulting
    partial technical correction.
skill: curate-yaml-record
completion: completed
verdict: pass_with_limitations
scientific_review: false
summary: Three existing bacterial species descriptors now carry native reference correspondences
  and GROUNDED status. The Burkholderia cenocepacia descriptor carries the complete
  two-way native ambiguity without selecting a species for J2315. Stock descriptions,
  the virus exclusion, biological graph, source quotations and old history are preserved.
  This diagnostic does not newly approve the whole scientific record.
source:
  git_revision: 9276e66296f8063522d34e553e91260fbe9f1a5f
  state: working_tree
  inputs:
  - path: .temp/gtdb-code006-20261115/kg-microbe/data/raw/NCBI2GTDB.tsv.gz
    sha256: 761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd
    role: context
  - path: .temp/gtdb-code006-20261115/phage-pair-467-applied-001/before.yaml
    sha256: cef1f3c47035ef336cb809456b25a185e0397bb9f0a16c492becdb5b371529f5
    role: context
  - path: .temp/gtdb-code006-20261115/phage-pair-467-applied-001/receipt.json
    sha256: be40e2c4e677553ae3de6543651bc3c404406e9db8829d51ebb0b2d0bbd2879d
    role: context
  - path: .temp/gtdb-code006-20261115/phage-pair-467-candidate-001/Alseth_FourSpecies_Pathogen_Phage_Community.yaml
    sha256: 00bd07edc28d86c0133ed565ee28c81fe6a21aaa49a0ac2edd68639e70c21a08
    role: context
  - path: .temp/gtdb-code006-20261115/phage-pair-467-candidate-001/receipt.json
    sha256: 9732cb375add8e1292cc1da816182398658d4b720c42510fb7aeab1d9f4e92d3
    role: context
  - path: .temp/gtdb-code006-20261115/phage-pair-467-check-config-001.json
    sha256: ac1c9b2c4522a4d799697b064ff16223fb7ef2a4b714f5d6d6230978787514b1
    role: context
  - path: .temp/gtdb-code006-20261115/phage-pair-467-run-domain-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/phage-pair-467-run-domain-001/native.log
    sha256: cafce7dc40fff0df809129c20b86b7f9f262d4f2c1311e4599f1c5c24f1040ca
    role: context
  - path: .temp/gtdb-code006-20261115/phage-pair-467-run-domain-001/receipt.json
    sha256: e65b8bf029b04c65619c0d3bc00a8c2a0c29bbfb8e014e3e40890ccdabedb891
    role: context
  - path: .temp/gtdb-code006-20261115/phage-pair-467-run-domain-001/start.json
    sha256: d8e20aa42e45c68fc423bca841b866c4c4fd614fa1bf39eaf9fc5f524eb12298
    role: context
  - path: .temp/gtdb-code006-20261115/phage-pair-467-run-gtdb-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/phage-pair-467-run-gtdb-001/native.log
    sha256: 1fe5b6588ffdbbda2f385a2b0be93411525cd05a9ab05ba463e081f247fe1b12
    role: context
  - path: .temp/gtdb-code006-20261115/phage-pair-467-run-gtdb-001/receipt.json
    sha256: 9e230135bbf92a54dae575597191bed6987fcee6060590a9672a404176236eba
    role: context
  - path: .temp/gtdb-code006-20261115/phage-pair-467-run-gtdb-001/start.json
    sha256: e62641e7ae66bbf2cfbdb3dd1075c2d26257dc45088d612fad8b005d2a658fa1
    role: context
  - path: .temp/gtdb-code006-20261115/phage-pair-467-run-history-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/phage-pair-467-run-history-001/native.log
    sha256: 700b44227c4cf01270ac26f16b308622de0b26f48d71aec49cdfaaab87620f0a
    role: context
  - path: .temp/gtdb-code006-20261115/phage-pair-467-run-history-001/receipt.json
    sha256: dee7808240d2ca04806925e9e547f3f8e2e021585c2892e2975ce07b6e7a715d
    role: context
  - path: .temp/gtdb-code006-20261115/phage-pair-467-run-history-001/start.json
    sha256: e160d53760a11908c2b33225f1d48d7588ecb66f2b5c87a2dae991e3f688cba8
    role: context
  - path: .temp/gtdb-code006-20261115/phage-pair-467-run-new-history-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/phage-pair-467-run-new-history-001/native.log
    sha256: 1f107af224fae423e2cf6143ef6febef3383229c94383baaaa1825a5ba229494
    role: context
  - path: .temp/gtdb-code006-20261115/phage-pair-467-run-new-history-001/receipt.json
    sha256: 89dd893a1072709fe396e7db34fcd02e4ec5c0366ac66e0efc70e01ef20b51ed
    role: context
  - path: .temp/gtdb-code006-20261115/phage-pair-467-run-new-history-001/start.json
    sha256: f5c3c04913815c18bf7f4a5aa64e1bcc6e6c5117dba6231d923ecc6c7a17ed78
    role: context
  - path: .temp/gtdb-code006-20261115/phage-pair-467-run-scalars-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/phage-pair-467-run-scalars-001/native.log
    sha256: faf0fc846cadf0795c9109614bbdc189cc8006260b39660c6af7e980a4212694
    role: context
  - path: .temp/gtdb-code006-20261115/phage-pair-467-run-scalars-001/receipt.json
    sha256: 1210964791e352e9164eec6bec7b24c571d3b177e99d47fc1509d3738060f671
    role: context
  - path: .temp/gtdb-code006-20261115/phage-pair-467-run-scalars-001/start.json
    sha256: af8149b28bdf7bb814b9a23a0935fc2f7b3f6c86016f5757e27341ef5eade7d1
    role: context
  - path: .temp/gtdb-code006-20261115/phage-pair-467-run-schema-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/phage-pair-467-run-schema-001/native.log
    sha256: 7b7d9e2594d8f0b33189ae1b5c3e155679e06f41e7eb35464a86a599e3e12ebf
    role: context
  - path: .temp/gtdb-code006-20261115/phage-pair-467-run-schema-001/receipt.json
    sha256: 5b2c3ff604de36fe31d7ce73888d85f0cf50da1458e0653b9c7dc91bac168a44
    role: context
  - path: .temp/gtdb-code006-20261115/phage-pair-467-run-schema-001/start.json
    sha256: e7e376c129a0a8d26e4c5606d2faa41e5c0afc9e631073605ecdf3709f9b8767
    role: context
  - path: .temp/gtdb-code006-20261115/phage-pair-467-run-strict-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/phage-pair-467-run-strict-001/native.log
    sha256: ddbb99401663770adc18768e1df8bc517f4bc51be2a0850c2a2af0c499bbd8f6
    role: context
  - path: .temp/gtdb-code006-20261115/phage-pair-467-run-strict-001/receipt.json
    sha256: cbb96d04b5a2fe7fe584a69818f66a2ce6ea5170f5b9a16cbb10a946c8fd9299
    role: context
  - path: .temp/gtdb-code006-20261115/phage-pair-467-run-strict-001/start.json
    sha256: 0ec67ce7adcbc17e7b301e8a5e8f48c479b93bb3992972d26f8f9093a58147e8
    role: context
  - path: .temp/gtdb-code006-20261115/phage-pair-467-run-strict-001/strict.tsv
    sha256: b184ed5450b968070bb6c75648407e388f41a1eaf7017890723cf560999fc3f7
    role: context
  - path: .temp/gtdb-code006-20261115/phage-pair-467-run-terms-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/phage-pair-467-run-terms-001/native.log
    sha256: cabed0e368b2d2baef9d5682d61c3f529cbf1cfa4a176c2eb3c2bf67538caa06
    role: context
  - path: .temp/gtdb-code006-20261115/phage-pair-467-run-terms-001/receipt.json
    sha256: 03cf444de25a5d9f2e94b88d51ce3bb023a4da30786b7c5316f2d6c269667845
    role: context
  - path: .temp/gtdb-code006-20261115/phage-pair-467-run-terms-001/start.json
    sha256: efec63f56313e7e7a29dcbfa2719f2aae1f928bb73be9ceb468ca3225fd4bc01
    role: context
  - path: .temp/gtdb-code006-20261115/phage-pair-route-plan-001.json
    sha256: bba38bbb0987028d8c5ea3585f76f906dc9438082bebf5147f16bf1affd562dd
    role: context
  - path: .temp/phase2-schema-20261115/phage-pair-route-001.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/phase2-schema-20261115/phage-pair-route-001.json
    sha256: 4ce7fb599dd4dbcaafd9d729551f1a61c9950589a214fd0fec61ad06d7ab358a
    role: context
  - path: .temp/phase2-schema-20261115/phage-pair-route-001.log
    sha256: 02177439996da7bc6f9cab2d51742f35cc3f8619fee4aef0b2eea179f3fa108d
    role: context
  - path: .temp/phase2-schema-20261115/phage-pair-source-binding-001.log
    sha256: bb908f9a7de0ce668467e69041bd8f9ee0cd839b302d6e1f9e252beafd13929a
    role: context
  - path: history/records/Alseth_FourSpecies_Pathogen_Phage_Community/2026-10-03T194711Z-claude-code-febc49.yaml
    sha256: 7a868d46f63bace00492c149b50023ac4183174ce0a2b856061290fc278cf11a
    role: context
  - path: history/records/Alseth_FourSpecies_Pathogen_Phage_Community/2026-10-03T214846Z-claude-code-ff0e0c.yaml
    sha256: e12637a61f829e6dc1efb820af3e1dd60bc89522e9d83c7f0182110ad17e1b7c
    role: context
  - path: history/records/Alseth_FourSpecies_Pathogen_Phage_Community/2026-10-14T215856Z-codex-b473e9.yaml
    sha256: cbace6e1715cae5ccaf1963ddb7df5a6414b1f45dd246261d7b8512eccaac690
    role: context
  - path: history/records/Alseth_FourSpecies_Pathogen_Phage_Community/2026-10-14T220730Z-codex-dda3a4.yaml
    sha256: 234c0eba26f62435864b88f95a798dd02f7c158ac364f332f66302e8508827c2
    role: context
  - path: history/records/Alseth_FourSpecies_Pathogen_Phage_Community/2026-11-15T105840Z-codex-996a4e.yaml
    sha256: 97e4b97259ed2ab2b6c925d8e2389909b81f3b5fe7526e94379584264a6e833f
    role: context
  - path: justfile
    sha256: 40369611ad4531582e420df0e9ff22109e4b18adf03b34d86b54200b280f2d0f
    role: context
  - path: kb/communities/Alseth_FourSpecies_Pathogen_Phage_Community.yaml
    sha256: 00bd07edc28d86c0133ed565ee28c81fe6a21aaa49a0ac2edd68639e70c21a08
    role: target
  - path: pyproject.toml
    sha256: be952f0f137f85fed66bda0908f12014f1797a2dd229b44d832afc0c00471655
    role: context
  - path: references_cache/PMID_38648198.txt
    sha256: babc54ddb60c3ed882e817d1970ff9c7ba24069b0b06d67730e12eb974b58df3
    role: context
  - path: reports/causal_graph_review/decisions/20261014-phage-graphs-batch130.yaml
    sha256: 88a433392f6b1ad7214280eb4d71f3fb55768f2803359afb0ee5490330bea785
    role: context
  - path: reports/gtdb-code006-20261115/phage-pair-467-review-config-001.json
    sha256: 21703e1f2a4f1d1a81852c1010538647dd3c9893f8481afb90ba4fdfdd213418
    role: context
  - path: reports/gtdb-code006-20261115/phage-pair-467-source-evidence-001.json
    sha256: 5a30e4d8ce5ddceeadf7740065ceb35788f5808161392ecbe904a9983f96a84c
    role: context
  - path: reports/gtdb-code006-20261115/phage-pair-authored-source-context-001.json
    sha256: acc638d55ffb4497f9d4168de3e4c08186cfe01555939f64de33599c264b0cfa
    role: context
  - path: reports/gtdb-code006-20261115/phage-pair-source-config-001.json
    sha256: 2cc5f90edc038943f347ea9623299b72292b66bcd4aca90bfa7d3f0e03df2721
    role: context
  - path: reports/phase2-completion-20261115/phage467-source-context-001.yaml
    sha256: ab69eee5fc060977e77c617711225d905d551f5185d8c47cc9a3368ca5199bb6
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
  - path: tests/test_causal_review_batch130.py
    sha256: fc51ae1f93310f1317f78fbd11b7468b4ab6043bff4c577e8c52c1d96ac2c07b
    role: context
  - path: uv.lock
    sha256: 712838f8fa3d68fbd818ac8162f3f1e2f2637db1da1a8ebfaba0ef759690f3b4
    role: context
targets:
- target_id: CommunityMech:000467
  path: kb/communities/Alseth_FourSpecies_Pathogen_Phage_Community.yaml
  selector: taxonomy[0:4].taxon_term.gtdb_classification; gtdb_grounding_status; gtdb_candidates
  label: Species-reference correspondences and complete J2315 descriptor ambiguity
  kind: maintained
  ownership_note: CommunityMech owns this record; only declared GTDB correspondence/status
    and actual provenance are assessed.
scope:
  description: 'Four declared bacterial taxonomy occurrences in CommunityMech:000467:
    three native species correspondence blocks/statuses, one complete ambiguous status/candidate
    list, two native inline events and the actual source/application/history/gate
    chain. The phage descriptor and all biological assertions remain outside the changed
    fields.'
  selection: One whole-record species-plus-ambiguity canary from the prepared 467/468
    pair. The reviewed population is exactly one record. The five-genus PHA record
    468 is excluded from this diagnostic and cannot be counted complete from this
    canary.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000467
  exclusions:
  - target: Other scientific claims and records
    reason: Existing biology is preserved, not newly certified by this database diagnostic.
checks:
- check_id: 000467-schema
  name: validate
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000467
  command: just --verbose --no-dotenv --color never validate kb/communities/Alseth_FourSpecies_Pathogen_Phage_Community.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000467-schema
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000467-strict
  name: validate-strict
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000467
  command: just --verbose --no-dotenv --color never validate-strict kb/communities/Alseth_FourSpecies_Pathogen_Phage_Community.yaml
    --out .temp/gtdb-code006-20261115/phage-pair-467-run-strict-001/strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000467-strict
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000467-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000467
  command: just --verbose --no-dotenv --color never validate-gtdb kb/communities/Alseth_FourSpecies_Pathogen_Phage_Community.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000467-gtdb
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000467-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000467
  command: just --verbose --no-dotenv --color never validate-gtdb-domain kb/communities/Alseth_FourSpecies_Pathogen_Phage_Community.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000467-domain
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000467-scalars
  name: validate-scalars
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000467
  command: just --verbose --no-dotenv --color never validate-scalars kb/communities/Alseth_FourSpecies_Pathogen_Phage_Community.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000467-scalars
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000467-history
  name: validate-history
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000467
  command: just --verbose --no-dotenv --color never validate-history history/records/Alseth_FourSpecies_Pathogen_Phage_Community
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000467-history
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000467-new-history
  name: new-history
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000467
  command: 'just --verbose --no-dotenv --color never new-history --kind record --slug
    Alseth_FourSpecies_Pathogen_Phage_Community --target-root kb/communities --event
    EDIT --outcome changed --sections taxonomy,curation_history --actor-name codex
    --model gpt-6 --agent-tool codex --issue https://github.com/CultureBotAI/CommunityMech/issues/2848
    --summary ''Record species-reference correspondences and complete Burkholderia
    ambiguity'' --details ''The independently reviewed native candidate adds three
    existing species descriptors''"''"'' reference correspondences and matching GROUNDED
    statuses: Pseudomonas aeruginosa 17191 reference genomes/fraction 0.99, Acinetobacter
    baumannii 15884/1.0 and Staphylococcus aureus 37403/1.0. Burkholderia cenocepacia
    retains both native alternatives through AMBIGUOUS status and the complete ordered
    candidates; no single J2315 species assignment is made. Preserve UCBPP-PA14 wild-type
    and CRISPR-KO backgrounds, FZ21, 13 S44 S9 and J2315 stock notes, DMS3vir''"''"''s
    viral exclusion, all biological assertions, source quotations, graph topology
    and prior history. Reference populations do not identify experimental stock genomes.
    Phenotypic resistance classes are not sequenced genotypes, and phage-free abundance
    experiments remain distinct from phage effects. Source reporting and binding ran
    locally at ab770f26; actual M5 staging and application ran at published 9276e662
    with the same captured source bytes. Two native inline events record the bounded
    correspondence/status change. The mapping table''"''"''s mtime is not its release.
    This is a partial database-correspondence correction, not a full scientific review
    or issue closure. Actual apply receipt .temp/gtdb-code006-20261115/phage-pair-467-applied-001/receipt.json
    sha256:be40e2c4e677553ae3de6543651bc3c404406e9db8829d51ebb0b2d0bbd2879d.'''
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000467-new-history
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000467-terms
  name: validate-terms
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000467
  command: just --verbose --no-dotenv --color never validate-terms kb/communities/Alseth_FourSpecies_Pathogen_Phage_Community.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000467-terms
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
evidence:
- evidence_id: 000467-schema
  kind: validation
  reference: .temp/gtdb-code006-20261115/phage-pair-467-run-schema-001/native.log
  accessed_at: '2026-11-15T11:00:20.153567Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000467-strict
  kind: validation
  reference: .temp/gtdb-code006-20261115/phage-pair-467-run-strict-001/native.log
  accessed_at: '2026-11-15T11:00:20.153567Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000467-gtdb
  kind: validation
  reference: .temp/gtdb-code006-20261115/phage-pair-467-run-gtdb-001/native.log
  accessed_at: '2026-11-15T11:00:20.153567Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000467-domain
  kind: validation
  reference: .temp/gtdb-code006-20261115/phage-pair-467-run-domain-001/native.log
  accessed_at: '2026-11-15T11:00:20.153567Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000467-scalars
  kind: validation
  reference: .temp/gtdb-code006-20261115/phage-pair-467-run-scalars-001/native.log
  accessed_at: '2026-11-15T11:00:20.153567Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000467-history
  kind: validation
  reference: .temp/gtdb-code006-20261115/phage-pair-467-run-history-001/native.log
  accessed_at: '2026-11-15T11:00:20.153567Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000467-new-history
  kind: validation
  reference: .temp/gtdb-code006-20261115/phage-pair-467-run-new-history-001/native.log
  accessed_at: '2026-11-15T11:00:20.153567Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000467-terms
  kind: validation
  reference: .temp/gtdb-code006-20261115/phage-pair-467-run-terms-001/native.log
  accessed_at: '2026-11-15T11:00:20.153567Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000467-paper
  kind: primary_source
  reference: https://doi.org/10.1371/journal.pbio.3002346
  locator: Retained main-text Methods bacterial-strain paragraphs and Results resistance-classification
    passage; exact primary_locators in bound source metadata
  support: supports
  summary: The source identifies the PA14 backgrounds and the FZ21, 13 S44 S9 and
    J2315 stocks. It separates phenotypic resistance from unperformed receptor-mutant
    sequencing and distinguishes phage-free abundance observations from phage effects.
    These passages do not classify an experimental assembly into GTDB.
  accessed_at: '2026-11-15T11:00:20.153567Z'
- evidence_id: 000467-database
  kind: database
  reference: reports/gtdb-code006-20261115/phage-pair-467-source-evidence-001.json
  locator: occurrences[taxonomy_index=0,1,2,3], native_result, lookup_indexes and
    ncbi_identity_rows
  support: supports
  summary: The exact pinned table and unchanged native resolver return three species
    correspondences through exact NCBI IDs and the complete two-option Burkholderia
    name route. Local NCBI authority confirms the existing species ranks and labels.
    The reference populations do not identify the study stocks' genomes.
  accessed_at: '2026-11-15T11:00:20.153567Z'
- evidence_id: 000467-application
  kind: record_content
  reference: .temp/gtdb-code006-20261115/phage-pair-467-applied-001/receipt.json
  locator: actual before/after, externally reviewed candidate/receipt hashes and source
    inputs; two native events and appended sidecar
  support: supports
  summary: The exact reviewed candidate was persisted on isolated M5. The semantic
    delta is limited to the four selected descriptors and two native inline events;
    stock notes, viral exclusion, biological graph, source quotes and old history
    remain unchanged.
  accessed_at: '2026-11-15T11:00:20.153567Z'
- evidence_id: 000467-prior
  kind: prior_review
  reference: reports/causal_graph_review/decisions/20261014-phage-graphs-batch130.yaml
  locator: CommunityMech:000467 historical decisions and current test_causal_review_batch130.py
    contract/mutation controls
  support: context_only
  summary: The immutable graph ledger and current biological predicates preserve five
    nodes, three directed edges, qualified mediation, model conditions and the open
    scientific discussions. This scoped technical successor does not rewrite the historical
    scientific decisions or certify an additional whole-record review.
  accessed_at: '2026-11-15T11:00:20.153567Z'
assessments:
- assessment_id: 000467-identity
  area: grounding
  topic: Existing species descriptors and experimental-stock boundaries
  outcome: supported
  target_ids:
  - CommunityMech:000467
  evidence_ids:
  - 000467-paper
  - 000467-database
  - 000467-terms
  summary: The four selected bacterial descriptors retain their source-compatible
    species anchors and named stock fields. The PA14 treatment backgrounds remain
    distinct and no phage, genotype or exact assembly is newly identified by this
    mapping.
- assessment_id: 000467-population
  area: grounding
  topic: Three reference populations and complete two-way ambiguity
  outcome: supported
  target_ids:
  - CommunityMech:000467
  evidence_ids:
  - 000467-database
  - 000467-gtdb
  - 000467-domain
  summary: The accepted native results support the three exact species-reference blocks
    and preserve both Burkholderia alternatives through AMBIGUOUS status. Pseudomonas
    fraction 0.99 is a reference majority rather than unanimity; no candidate choice
    or study-stock genome claim is introduced.
- assessment_id: 000467-provenance
  area: provenance
  topic: Guarded actual transition and preserved historical science
  outcome: supported
  target_ids:
  - CommunityMech:000467
  evidence_ids:
  - 000467-application
  - 000467-prior
  - 000467-schema
  - 000467-strict
  - 000467-scalars
  - 000467-new-history
  - 000467-history
  summary: The independently reviewed candidate and exact source bytes were applied
    through the guarded native writer, followed by the eight scoped commands and actual
    appended history. The prior biological contract and scientific uncertainty remain
    unchanged; strict successor and composed integration checks are separate follow-up
    work.
findings: []
actions: []
limitations:
- Partial technical assessment with scientific_review:false. Diagnostic completion
  and eight native scoped gates do not establish a full scientific review, measured
  source-assertion coverage, final corpus QC, generated-page integration or campaign
  completion.
- The three species reference populations are 17191 genomes at native fraction 0.99
  for Pseudomonas aeruginosa, 15884 at 1.0 for Acinetobacter baumannii and 37403 at
  1.0 for Staphylococcus aureus. These are crosswalk populations, not experimental
  stock genomes, isolate counts, relative abundances or identity probabilities. The
  first native fraction is rounded and is not a unanimity claim.
- The complete Burkholderia cenocepacia name route has two alternatives, GTDB:s__Burkholderia_cenocepacia
  and GTDB:s__Burkholderia_orbicola. No single assignment, exact assembly classification
  or stock renaming is inferred for J2315.
- Both streptomycin-marked UCBPP-PA14 wild type and the isogenic CRISPR-KO background
  remain separate experimental contexts. FZ21, 13 S44 S9 and J2315 retain their source
  stock identities. DMS3vir remains excluded from GTDB bacterial/archaeal correspondence;
  the acrF1 experimental derivative does not become an additional canonical member.
- Source examination was limited to the retained main-text Methods and Results passages
  identified in the source context, the whole current record and its historical scientific
  guard. No new full-paper review, supplemental reanalysis, figure-pixel inspection
  or stock-assembly analysis was performed for this technical successor.
- Resistance categories remain phenotype-based; the receptor mutants were not sequenced.
  The no-phage abundance experiments remain distinct from phage effects. Competitive-release
  mediation and the condition-specific gLV model remain qualified, with the existing
  open discussions unchanged.
- All five graph nodes, three directed edges, original quotations, clinical-isolation
  notes, culture conditions and old history remain unchanged. The historical notes
  about unavailable mapping data describe the earlier curation context; this successor
  does not rewrite those observations or imply that no mapping table exists now.
- Source reporting and binding ran locally at ab770f2602416a54835b382e881c7535b5b3e576
  with the recorded untracked preparation files. Actual M5 staging, application and
  native gates ran at frozen 9276e66296f8063522d34e553e91260fbe9f1a5f with native
  Python 3.13.2. Post-application receipts disclose the accepted record change and
  subsequent native sidecar.
- The mapping table is pinned by SHA-256 761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd.
  Its mtime is not a release identifier. Native local ontology observations retain
  their actual stat-based provenance rather than an invented fresh full-database digest.
- Native term validation is reported literally without an assertion denominator. Historical
  scientific callers and strict successor admission are separate follow-up controls;
  passing technical validators does not establish biological truth. No issue is closed
  by this review.
links:
- https://github.com/CultureBotAI/CommunityMech/issues/2848
- https://github.com/CultureBotAI/CommunityMech/pull/2853
```
