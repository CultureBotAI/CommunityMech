# Amsterdam gut panel: six reference correspondences and three preserved ambiguity sets

- Review: 20261115T115727Z-amsterdam-gut-species-reference-diagnostic
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-11-15T11:57:27.552914Z
- Finished UTC: 2026-11-15T11:57:27.692838Z
- Reviewer: codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: false

## Summary

Nine existing taxonomy descriptors now have six native reference blocks with GROUNDED status and three complete ordered ambiguity sets with AMBIGUOUS status. The unselected Lachnospiraceae bacterium DSM 24404 remains UNRESOLVED. All ten DSM stocks, original notes and source quotations, one community-level conditioned-medium node, absent participants, zero arrows and earlier history remain unchanged. The reference populations do not establish stock genomes or resolve the record's scientific findings.

## Scope And Provenance

CommunityMech:000382 taxonomy indices 0, 1, 2, 3, 4, 5, 6, 8 and 9: six correspondence blocks, three complete ambiguity sets, nine changed statuses and two actual native inline events, with guarded application, appended native sidecar and eight scoped native checks. Index 7 and all biological content are preserved.

Selection: The first complete whole-record canary in the separately prepared 382/466 pair. The reviewed population is exactly one record; the second record is not applied or assessed by this diagnostic. Complete saved evidence and strict successor controls remain required before the second application.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base e4dc49afd89482371a84ea71829eee6e27d94a1d.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000382 | kb/communities/Amsterdam_10Species_Gut_Invasion_SynCom.yaml # taxonomy[0,1,2,3,4,5,6,8,9].taxon_term.gtdb_classification; taxonomy[0,1,2,3,4,5,6,8,9].taxon_term.gtdb_grounding_status; taxonomy[4,6,8].taxon_term.gtdb_candidates | maintained | Six species-reference mappings and three preserved name-route ambiguities |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000382 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-strict | passed | True | CommunityMech:000382 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-gtdb | passed | True | CommunityMech:000382 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-gtdb-domain | passed | True | CommunityMech:000382 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-scalars | passed | True | CommunityMech:000382 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-history | passed | True | CommunityMech:000382 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| new-history | passed | True | CommunityMech:000382 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-terms | passed | True | CommunityMech:000382 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |

## Scientific And Domain Assessments

### Species descriptors retain distinct DSM stock and experimental contexts

grounding: supported. Targets: CommunityMech:000382.

The selected existing species descriptors retain their source-supported stock identities and current authority ranks. Ten-stock, later nine-species model and separate assay contexts remain distinct. Source 16S attribution is not an independently verified study-stock genome correspondence.

### Six reference populations and three complete ordered ambiguities

grounding: supported. Targets: CommunityMech:000382.

The actual native change reproduces all six reviewed reference blocks and the complete two-, three- and three-way ambiguity lists. The two rounded 0.99 populations remain non-unanimous; no stock-specific assignment is inferred. The unselected DSM 24404 descriptor remains null/UNRESOLVED.

### Exact bounded application preserves scientific and historical scope

provenance: supported. Targets: CommunityMech:000382.

The accepted candidate, actual receipt and sidecar bind the nine changed descriptors and two native events. Eight scoped commands passed on actual bytes, including a one-file strict check with zero errors. Original biology, earlier findings and the prior partial review remain unchanged; strict saved-successor and composed renderer controls are subsequent acceptance steps, not assumed results.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| 000382-schema | .temp/gtdb-code006-20261115/gut-pair-382-run-schema-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000382-strict | .temp/gtdb-code006-20261115/gut-pair-382-run-strict-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000382-gtdb | .temp/gtdb-code006-20261115/gut-pair-382-run-gtdb-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000382-domain | .temp/gtdb-code006-20261115/gut-pair-382-run-domain-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000382-scalars | .temp/gtdb-code006-20261115/gut-pair-382-run-scalars-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000382-history | .temp/gtdb-code006-20261115/gut-pair-382-run-history-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000382-new-history | .temp/gtdb-code006-20261115/gut-pair-382-run-new-history-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000382-terms | .temp/gtdb-code006-20261115/gut-pair-382-run-terms-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000382-paper | https://doi.org/10.1128/msystems.00113-26; Retained main text line 75: Bacteria and growth conditions, DSMZ roster, conditioned-medium preparation, co-culture/invasion and qPCR Methods; exact primary_locators retained in captured source metadata | supports | The inspected source passages name the ten DSMZ stocks and report 16S confirmation, while distinguishing the original panel from subsequent modeling and assays. They do not independently assign each study stock to a GTDB genome or identify the molecular cause of each conditioned-medium effect. |
| 000382-database | reports/gtdb-code006-20261115/gut-pair-382-source-evidence-001.json; Selected taxonomy indices 0,1,2,3,4,5,6,8,9: full native_result, classify_status, lookup_indexes, crosswalk_rows and ncbi_identity_rows | supports | The pinned native resolver and current authority observations support six species-reference correspondences and three complete ambiguity sets. The name route for Akkermansia differs from the five exact-ID routes. No stock assembly or single choice within an ambiguity is established; index 7 remains outside the selected correction. |
| 000382-application | .temp/gtdb-code006-20261115/gut-pair-382-applied-001/receipt.json; Actual before/after, external reviewed candidate and receipt pins, complete captured inputs, six-block/nine-status native inline events and appended native sidecar | supports | The exact independently reviewed candidate was persisted on isolated M5. Only selected GTDB fields and two native events change; all ten stock identities, the null placeholder, source quotations, biological assertions and prior history remain unchanged. |
| 000382-prior | reviews/structured/20261020T071158Z-amsterdam-gut-panel-metadata-review/review.yaml; Immutable partial metadata assessment, role-metadata and repository-version findings; original batch 4 ledger and current tests/test_site_audit_fixes.py renderer contract are also bound inputs | context_only | The earlier assessment explicitly excludes scientific/mechanistic certification. Its unresolved roles and repository provenance, the historical graph removals and the renderer's prohibition on inferred participant links remain preserved. This technical successor does not overwrite or reinterpret that assessment as a full review. |

## Limits And Additional Notes

- Partial technical database-correspondence diagnostic with scientific_review:false. Completion of these scoped checks is not whole-record scientific approval, reference-snippet coverage, generated-page validation, final corpus QC or campaign completion.
- Six reference populations reproduce: Akkermansia muciniphila by species name, 4983 genomes/fraction 1.0; Bacteroides ovatus by species ID, 3107/0.99; B. thetaiotaomicron 1011/0.99; Bifidobacterium adolescentis 599/1.0; Escherichia coli 166397/1.0; Roseburia intestinalis 78/1.0. Rounded fractions of 0.99 are not unanimity or exact recoverable numerators. These populations are not experimental stock counts, inoculum ratios, abundance estimates or identity probabilities.
- Blautia obeum retains both intestinalis/obeum alternatives; Faecalibacterium prausnitzii retains longum/prausnitzii/prausnitzii_D; Lactobacillus johnsonii retains johnsonii/sp945980025/sp947171515. These ordered native name ambiguities do not select a study-stock genome. The unchanged DSM 24404 placeholder has a null native result and remains UNRESOLVED, without a guessed species or a biological/domain-absence claim.
- The source names ten DSMZ stocks and reports 16S identity confirmation. That source attribution is distinct from an independent stock-sequence or GTDB assembly analysis, which was not performed. Source stock names, collection identifiers, canonical species labels and prior notes remain unchanged.
- The original ten-stock conditioned-medium panel, the later nine-species model after Roseburia exclusion, two-to-four-species validation co-cultures and the E. coli/B. ovatus invasion assays remain distinct. This work does not restore the previously removed gLV or invasion graph nodes or create member-to-node links.
- The one COMMUNITY_LEVEL conditioned-medium node, absent participating_taxa and zero directed edges remain unchanged. Negative endpoint-density effects do not uniquely identify competition, toxins or a mediator; growth rate and final density are distinct. The ninety donor-acceptor conditions and 60% fresh/40% spent YCFA ratio remain literal source context.
- The source phrase '8 mL flasks' does not establish an 8 mL working volume. Finding 2887 remains outside this correction; no claim is made that uninspected supplementary material lacks the quantity. Prior partial-review findings 2232/2233 concerning roles and an unpinned data resource remain unresolved. Historical caption and model-size discrepancies are not resolved by taxonomy.
- DNA-qPCR relative frequencies are not direct viable-cell counts. Model predictions, observed co-culture/invasion outcomes and any in-vivo or pathogen inference remain distinct. No mechanism, biological role or cultivation recommendation is added.
- Examination covered the whole current record, the previous partial metadata assessment and ledger, the current renderer guard and selected retained primary Methods/Results passages. No fresh full scientific paper review, separate supplementary inspection, figure-pixel audit, pinned repository snapshot, stock sequence or study-assembly verification was performed.
- Historical missing-crosswalk notes and the October partial assessment remain unchanged evidence of their earlier scope. Their historical unresolved mapping statements are not rewritten or promoted to current scientific clearance. Original scientific findings, ledgers and issue dispositions remain preserved.
- Source reporting and binding ran locally at 9bf78f54f83f88f954a309f351d862b4e0495c7a with preparation files disclosed. The isolated M5 stage and application began clean at e4dc49afd89482371a84ea71829eee6e27d94a1d, with frozen offline dependencies and native Python 3.13.2. Later gates correctly observe the applied record. The native status log processed ten taxa while its actual event records nine changed statuses.
- Crosswalk SHA-256 is 761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd; file mtime does not identify its upstream release. Local NCBITaxon/ENVO/GO readiness and identity observations retain actual stat-based provenance, without an invented full-database hash. Native terms reports Validation passed without an assertion denominator. Strict successor and composed renderer/caller checks remain separate follow-up work.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261115T115727Z-amsterdam-gut-species-reference-diagnostic
kind: record
repository: CultureBotAI/CommunityMech
title: 'Amsterdam gut panel: six reference correspondences and three preserved ambiguity
  sets'
started_at: '2026-11-15T11:57:27.552914Z'
finished_at: '2026-11-15T11:57:27.692838Z'
reviewer:
  identity: codex
  kind: agent
  independence: self_review
  independence_basis: A peer independently read both complete records, primary stock
    passages, source plans, historical guards and the frozen source configurations.
    The same peer separately read the exact actual Amsterdam candidate and receipt
    before application, rehashing all 31 staged inputs. The parent authorized that
    accepted bounded correction. The shared native engine, checker, builder and exporter
    have separate reviews and mutation controls. This is self-review of the technical
    correspondence correction, not an independent full scientific assessment.
skill: curate-yaml-record
completion: completed
verdict: pass_with_limitations
scientific_review: false
summary: Nine existing taxonomy descriptors now have six native reference blocks with
  GROUNDED status and three complete ordered ambiguity sets with AMBIGUOUS status.
  The unselected Lachnospiraceae bacterium DSM 24404 remains UNRESOLVED. All ten DSM
  stocks, original notes and source quotations, one community-level conditioned-medium
  node, absent participants, zero arrows and earlier history remain unchanged. The
  reference populations do not establish stock genomes or resolve the record's scientific
  findings.
source:
  git_revision: e4dc49afd89482371a84ea71829eee6e27d94a1d
  state: working_tree
  inputs:
  - path: .temp/gtdb-code006-20261115/gut-pair-382-applied-001/before.yaml
    sha256: 01d41a601dba3f750e87784a28d97ef169dbd17de44d4fbe64f37f3d19d5cf3a
    role: context
  - path: .temp/gtdb-code006-20261115/gut-pair-382-applied-001/receipt.json
    sha256: 9a8063eac9c98573b2f161430939b05b83beab2b1054377fff56f09a563edb46
    role: context
  - path: .temp/gtdb-code006-20261115/gut-pair-382-candidate-001/Amsterdam_10Species_Gut_Invasion_SynCom.yaml
    sha256: 215177f0e7ebc45fa0b436e3877625722a6b5b1f3f0245e974fe7cda5abc2076
    role: context
  - path: .temp/gtdb-code006-20261115/gut-pair-382-candidate-001/receipt.json
    sha256: 8666541e8f997bfa318c713f16b91db12cf0b6a44cc2cf32830f39170043762a
    role: context
  - path: .temp/gtdb-code006-20261115/gut-pair-382-check-config-001.json
    sha256: 76f09143ea69e504f234eb9e7b7c03d284956e6fab1bb5ead78fe127cd7bacea
    role: context
  - path: .temp/gtdb-code006-20261115/gut-pair-382-run-domain-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/gut-pair-382-run-domain-001/native.log
    sha256: f11e77599b701966fc5d2f88be8648dbb07cd66cb56cf764fe54aa9d9603957d
    role: context
  - path: .temp/gtdb-code006-20261115/gut-pair-382-run-domain-001/receipt.json
    sha256: e2b23fa9b73cdfb697bce8c1a2325cb23d19ad7a68c8aaaa1e30dd89641be201
    role: context
  - path: .temp/gtdb-code006-20261115/gut-pair-382-run-domain-001/start.json
    sha256: 7ffc599523b3338fc23831bec8c7b71836198a49de93945a0ac043396f61b723
    role: context
  - path: .temp/gtdb-code006-20261115/gut-pair-382-run-gtdb-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/gut-pair-382-run-gtdb-001/native.log
    sha256: 152e02f93e37b248bd05a426367533342f74d9c43d099e6114399a487c1f9e3f
    role: context
  - path: .temp/gtdb-code006-20261115/gut-pair-382-run-gtdb-001/receipt.json
    sha256: cfa9598404ed0ab7a41faa9b898b237b5e57049d99a875c87bad21035e164285
    role: context
  - path: .temp/gtdb-code006-20261115/gut-pair-382-run-gtdb-001/start.json
    sha256: 2db51fe9ce8aa50fc81229369acbe3f138098bada7b94f19a1824118a98b2fed
    role: context
  - path: .temp/gtdb-code006-20261115/gut-pair-382-run-history-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/gut-pair-382-run-history-001/native.log
    sha256: 700b44227c4cf01270ac26f16b308622de0b26f48d71aec49cdfaaab87620f0a
    role: context
  - path: .temp/gtdb-code006-20261115/gut-pair-382-run-history-001/receipt.json
    sha256: c56438b5f49d5303b1e2798f84a674d50cb4b1aac89674a696400cf15fb39067
    role: context
  - path: .temp/gtdb-code006-20261115/gut-pair-382-run-history-001/start.json
    sha256: ec525ee17e47e1e7ea13f59494ce91fa37c0114115db6aedf369c0fdf56a3268
    role: context
  - path: .temp/gtdb-code006-20261115/gut-pair-382-run-new-history-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/gut-pair-382-run-new-history-001/native.log
    sha256: ed283f9805a4bc8c707b48bc12a6f8724c370e2b3978011e72033ee79b13141b
    role: context
  - path: .temp/gtdb-code006-20261115/gut-pair-382-run-new-history-001/receipt.json
    sha256: 61257cc9516da30d0da0405f2bff90b92a87131108c9ade29095de1a338440f8
    role: context
  - path: .temp/gtdb-code006-20261115/gut-pair-382-run-new-history-001/start.json
    sha256: 77d86522445696df7765afa5ca3273486dded70f81ac205256618d4dfae3579d
    role: context
  - path: .temp/gtdb-code006-20261115/gut-pair-382-run-scalars-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/gut-pair-382-run-scalars-001/native.log
    sha256: 98c63fe2d97395d42b93b0a1f081983c5be4762e6513bd5e2197d88d3131be32
    role: context
  - path: .temp/gtdb-code006-20261115/gut-pair-382-run-scalars-001/receipt.json
    sha256: 88c287ba99e65f1462d698da7f68ef2467bbce71f9a019a9e4aa340303945b3c
    role: context
  - path: .temp/gtdb-code006-20261115/gut-pair-382-run-scalars-001/start.json
    sha256: f21e81005057dfb0feeb50b4df77d5555e6a0886633e71b1c671b56f2cabe1b3
    role: context
  - path: .temp/gtdb-code006-20261115/gut-pair-382-run-schema-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/gut-pair-382-run-schema-001/native.log
    sha256: 42609befe91d2b43001331f2c7869c6f9a6e37bb846b3da2715f2664e3831c2e
    role: context
  - path: .temp/gtdb-code006-20261115/gut-pair-382-run-schema-001/receipt.json
    sha256: 923d917de2ba13f68a88e48cc1b4b76a3ed1fb902848341b6ca75e1d4a5087db
    role: context
  - path: .temp/gtdb-code006-20261115/gut-pair-382-run-schema-001/start.json
    sha256: 2c629990c48a121396a3c295634c02260a27036812cf8a5934169c7362c9d01b
    role: context
  - path: .temp/gtdb-code006-20261115/gut-pair-382-run-strict-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/gut-pair-382-run-strict-001/native.log
    sha256: 76716cf25cd31ea8504dbe40b743a79d1c10de3de8edc9840ddc2cf6684fe1f6
    role: context
  - path: .temp/gtdb-code006-20261115/gut-pair-382-run-strict-001/receipt.json
    sha256: 235fa9842ce503ae6033356509d4daf6a920c77c0743cbeb356e0102c1b25c61
    role: context
  - path: .temp/gtdb-code006-20261115/gut-pair-382-run-strict-001/start.json
    sha256: 8ad2902d494061d5a8345bff2d9d7841c42d5183124c19b2c306c94a45d687dc
    role: context
  - path: .temp/gtdb-code006-20261115/gut-pair-382-run-strict-001/strict.tsv
    sha256: b184ed5450b968070bb6c75648407e388f41a1eaf7017890723cf560999fc3f7
    role: context
  - path: .temp/gtdb-code006-20261115/gut-pair-382-run-terms-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/gut-pair-382-run-terms-001/native.log
    sha256: 6af220f0bcd8e146f131baaa5c35ca88dc6c58010afb640f50118b051f615009
    role: context
  - path: .temp/gtdb-code006-20261115/gut-pair-382-run-terms-001/receipt.json
    sha256: 41edae0458f6aa664745b54f4b14b96ebb10f609119d0b13ce0373d2e8a01ad1
    role: context
  - path: .temp/gtdb-code006-20261115/gut-pair-382-run-terms-001/start.json
    sha256: 5a6df3d50ffa5edbeb6799b6cb07aee47f25e54d72602edc8de83ed5dd4c5bc4
    role: context
  - path: .temp/gtdb-code006-20261115/gut-pair-route-plan-001.json
    sha256: 5d553d94c6a33a8bb09057a39498a4821dc613c7906cef59be63c91d5fd3d25f
    role: context
  - path: .temp/gtdb-code006-20261115/kg-microbe/data/raw/NCBI2GTDB.tsv.gz
    sha256: 761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd
    role: context
  - path: .temp/phase2-schema-20261115/gut-pair-route-001.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/phase2-schema-20261115/gut-pair-route-001.json
    sha256: 80ff6bcadcecaf97c32df24ced712f15d892b0a8158aa3c60256e2334d7c804e
    role: context
  - path: .temp/phase2-schema-20261115/gut-pair-route-001.log
    sha256: 62c6fc611c54ffd7ee480366741f96589179aed2e05b233d7609503111ae8000
    role: context
  - path: .temp/phase2-schema-20261115/gut-pair-source-binding-001.log
    sha256: d7f50210f6ed4c89786ceeeca7246989047a12dd5b67cab682e172a5549fea51
    role: context
  - path: history/records/Amsterdam_10Species_Gut_Invasion_SynCom/2026-09-15T063606Z-codex-708f6927.yaml
    sha256: b36da2a5c8cfc9e11e7b470c361349b35aa397cd71b8a151ed372933c0e04506
    role: context
  - path: history/records/Amsterdam_10Species_Gut_Invasion_SynCom/2026-09-15T064553Z-codex-1e06dac5.yaml
    sha256: c42aa98f7ea22b4164e91924b9ab01e05b5ff2c108985c973aa1f1dd1f95b577
    role: context
  - path: history/records/Amsterdam_10Species_Gut_Invasion_SynCom/2026-10-05T084241Z-codex-3ce1e3.yaml
    sha256: 7b7ace567857e96a9bdb544d6526528fa2b68abfb4fb5d905f73c0c012857a53
    role: context
  - path: history/records/Amsterdam_10Species_Gut_Invasion_SynCom/2026-11-15T115253Z-codex-fbfd0b.yaml
    sha256: d71c50aa5158b2b67cf53614e1dde905ff65a4d3a3d362bad70bd51afd8cc5fd
    role: context
  - path: justfile
    sha256: 40369611ad4531582e420df0e9ff22109e4b18adf03b34d86b54200b280f2d0f
    role: context
  - path: kb/communities/Amsterdam_10Species_Gut_Invasion_SynCom.yaml
    sha256: 215177f0e7ebc45fa0b436e3877625722a6b5b1f3f0245e974fe7cda5abc2076
    role: target
  - path: pyproject.toml
    sha256: be952f0f137f85fed66bda0908f12014f1797a2dd229b44d832afc0c00471655
    role: context
  - path: references_cache/PMID_41960919.txt
    sha256: c1f6c5bf8a394d6ac0727cfb4ccbe7175410aeb54d777f993f6252c096841609
    role: context
  - path: reports/causal_graph_review/decisions/20261005-twelve-records-batch4.yaml
    sha256: e21a355f676730e8e7e6de6ea663017c9b09e05a824ff383a272ab9f1399fd70
    role: context
  - path: reports/gtdb-code006-20261115/gut-pair-382-review-config-001.json
    sha256: c91a33da0620d16e96327ffc7311eb727c8895f358a833b2bb1a66a13d975778
    role: context
  - path: reports/gtdb-code006-20261115/gut-pair-382-source-evidence-001.json
    sha256: ce0d0aedaecc45d61db8575c131145f9380670a1d171e0eff145f32199b89a0d
    role: context
  - path: reports/gtdb-code006-20261115/gut-pair-authored-source-context-001.json
    sha256: 4d8cfb57fd549fc049469951abad91bc316b63fd7a21925f572c2e38da1c3c17
    role: context
  - path: reports/gtdb-code006-20261115/gut-pair-source-config-001.json
    sha256: dcae8a3a905aa15ce721e1867a9cda68981fda663b58db1b96f00b3c6c68dec0
    role: context
  - path: reports/phase2-completion-20261115/amsterdam382-source-context-001.yaml
    sha256: a06514371888570c95f356de1742a4c7e28b146d18b24beb84de5198147751c3
    role: context
  - path: reviews/structured/20261020T071158Z-amsterdam-gut-panel-metadata-review/review.yaml
    sha256: 50f4c1150ee45e40e6795bd61ba20099708818cd64cc523ba64740060e03bba9
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
  - path: tests/test_site_audit_fixes.py
    sha256: d3d65c1ea1e02b4637b6dd84d195d0ee20add931ac99649375583c4847059947
    role: context
  - path: uv.lock
    sha256: 712838f8fa3d68fbd818ac8162f3f1e2f2637db1da1a8ebfaba0ef759690f3b4
    role: context
targets:
- target_id: CommunityMech:000382
  path: kb/communities/Amsterdam_10Species_Gut_Invasion_SynCom.yaml
  selector: taxonomy[0,1,2,3,4,5,6,8,9].taxon_term.gtdb_classification; taxonomy[0,1,2,3,4,5,6,8,9].taxon_term.gtdb_grounding_status;
    taxonomy[4,6,8].taxon_term.gtdb_candidates
  label: Six species-reference mappings and three preserved name-route ambiguities
  kind: maintained
  ownership_note: CommunityMech owns this record; only declared GTDB correspondence/status
    and actual provenance are assessed.
scope:
  description: 'CommunityMech:000382 taxonomy indices 0, 1, 2, 3, 4, 5, 6, 8 and 9:
    six correspondence blocks, three complete ambiguity sets, nine changed statuses
    and two actual native inline events, with guarded application, appended native
    sidecar and eight scoped native checks. Index 7 and all biological content are
    preserved.'
  selection: The first complete whole-record canary in the separately prepared 382/466
    pair. The reviewed population is exactly one record; the second record is not
    applied or assessed by this diagnostic. Complete saved evidence and strict successor
    controls remain required before the second application.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000382
  exclusions:
  - target: Other scientific claims and records
    reason: Existing biology is preserved, not newly certified by this database diagnostic.
checks:
- check_id: 000382-schema
  name: validate
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000382
  command: just --verbose --no-dotenv --color never validate kb/communities/Amsterdam_10Species_Gut_Invasion_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000382-schema
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000382-strict
  name: validate-strict
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000382
  command: just --verbose --no-dotenv --color never validate-strict kb/communities/Amsterdam_10Species_Gut_Invasion_SynCom.yaml
    --out .temp/gtdb-code006-20261115/gut-pair-382-run-strict-001/strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000382-strict
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000382-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000382
  command: just --verbose --no-dotenv --color never validate-gtdb kb/communities/Amsterdam_10Species_Gut_Invasion_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000382-gtdb
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000382-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000382
  command: just --verbose --no-dotenv --color never validate-gtdb-domain kb/communities/Amsterdam_10Species_Gut_Invasion_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000382-domain
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000382-scalars
  name: validate-scalars
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000382
  command: just --verbose --no-dotenv --color never validate-scalars kb/communities/Amsterdam_10Species_Gut_Invasion_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000382-scalars
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000382-history
  name: validate-history
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000382
  command: just --verbose --no-dotenv --color never validate-history history/records/Amsterdam_10Species_Gut_Invasion_SynCom
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000382-history
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000382-new-history
  name: new-history
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000382
  command: 'just --verbose --no-dotenv --color never new-history --kind record --slug
    Amsterdam_10Species_Gut_Invasion_SynCom --target-root kb/communities --event EDIT
    --outcome changed --sections taxonomy,curation_history --actor-name codex --model
    gpt-6 --agent-tool codex --issue https://github.com/CultureBotAI/CommunityMech/issues/2848
    --summary ''Record six species-reference correspondences and three complete ambiguities''
    --details ''The independently reviewed actual M5 candidate changes nine existing
    descriptors: six native species-reference blocks and matching GROUNDED statuses,
    plus the complete ordered Blautia obeum, Faecalibacterium prausnitzii and Lactobacillus
    johnsonii ambiguity sets. The six reference populations are 4983/1.0 by name,
    3107/0.99, 1011/0.99, 599/1.0, 166397/1.0 and 78/1.0 by species ID; rounded fractions
    do not identify exact numerators or study-stock genomes. Preserve all ten DSM
    stocks, unselected Lachnospiraceae bacterium DSM 24404 with null native result
    and UNRESOLVED status, source quotations, original notes and prior history. The
    original ten-stock panel, later nine-species model, two-to-four-species co-cultures
    and invasion assays remain distinct. Preserve the one community-level conditioned-medium
    node, absent participants, zero arrows and all biological claims. The 8 mL flask
    wording is not proof of working volume; issue 2887 and prior metadata findings
    2232/2233 remain unresolved. Source reporting and binding ran locally at 9bf78f54;
    staging and application ran at frozen M5 e4dc49af with the exact captured source
    bytes. Two native inline events record six added blocks and nine changed statuses;
    processing ten taxa is not ten changed taxa. This is a partial technical correspondence
    correction, not a full scientific assessment, mechanistic clearance or issue closure.
    The crosswalk file mtime does not establish its release. Actual apply receipt
    .temp/gtdb-code006-20261115/gut-pair-382-applied-001/receipt.json sha256:9a8063eac9c98573b2f161430939b05b83beab2b1054377fff56f09a563edb46.'''
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000382-new-history
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000382-terms
  name: validate-terms
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000382
  command: just --verbose --no-dotenv --color never validate-terms kb/communities/Amsterdam_10Species_Gut_Invasion_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000382-terms
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
evidence:
- evidence_id: 000382-schema
  kind: validation
  reference: .temp/gtdb-code006-20261115/gut-pair-382-run-schema-001/native.log
  accessed_at: '2026-11-15T11:57:27.552914Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000382-strict
  kind: validation
  reference: .temp/gtdb-code006-20261115/gut-pair-382-run-strict-001/native.log
  accessed_at: '2026-11-15T11:57:27.552914Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000382-gtdb
  kind: validation
  reference: .temp/gtdb-code006-20261115/gut-pair-382-run-gtdb-001/native.log
  accessed_at: '2026-11-15T11:57:27.552914Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000382-domain
  kind: validation
  reference: .temp/gtdb-code006-20261115/gut-pair-382-run-domain-001/native.log
  accessed_at: '2026-11-15T11:57:27.552914Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000382-scalars
  kind: validation
  reference: .temp/gtdb-code006-20261115/gut-pair-382-run-scalars-001/native.log
  accessed_at: '2026-11-15T11:57:27.552914Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000382-history
  kind: validation
  reference: .temp/gtdb-code006-20261115/gut-pair-382-run-history-001/native.log
  accessed_at: '2026-11-15T11:57:27.552914Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000382-new-history
  kind: validation
  reference: .temp/gtdb-code006-20261115/gut-pair-382-run-new-history-001/native.log
  accessed_at: '2026-11-15T11:57:27.552914Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000382-terms
  kind: validation
  reference: .temp/gtdb-code006-20261115/gut-pair-382-run-terms-001/native.log
  accessed_at: '2026-11-15T11:57:27.552914Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000382-paper
  kind: primary_source
  reference: https://doi.org/10.1128/msystems.00113-26
  locator: 'Retained main text line 75: Bacteria and growth conditions, DSMZ roster,
    conditioned-medium preparation, co-culture/invasion and qPCR Methods; exact primary_locators
    retained in captured source metadata'
  support: supports
  summary: The inspected source passages name the ten DSMZ stocks and report 16S confirmation,
    while distinguishing the original panel from subsequent modeling and assays. They
    do not independently assign each study stock to a GTDB genome or identify the
    molecular cause of each conditioned-medium effect.
  accessed_at: '2026-11-15T11:57:27.552914Z'
- evidence_id: 000382-database
  kind: database
  reference: reports/gtdb-code006-20261115/gut-pair-382-source-evidence-001.json
  locator: 'Selected taxonomy indices 0,1,2,3,4,5,6,8,9: full native_result, classify_status,
    lookup_indexes, crosswalk_rows and ncbi_identity_rows'
  support: supports
  summary: The pinned native resolver and current authority observations support six
    species-reference correspondences and three complete ambiguity sets. The name
    route for Akkermansia differs from the five exact-ID routes. No stock assembly
    or single choice within an ambiguity is established; index 7 remains outside the
    selected correction.
  accessed_at: '2026-11-15T11:57:27.552914Z'
- evidence_id: 000382-application
  kind: record_content
  reference: .temp/gtdb-code006-20261115/gut-pair-382-applied-001/receipt.json
  locator: Actual before/after, external reviewed candidate and receipt pins, complete
    captured inputs, six-block/nine-status native inline events and appended native
    sidecar
  support: supports
  summary: The exact independently reviewed candidate was persisted on isolated M5.
    Only selected GTDB fields and two native events change; all ten stock identities,
    the null placeholder, source quotations, biological assertions and prior history
    remain unchanged.
  accessed_at: '2026-11-15T11:57:27.552914Z'
- evidence_id: 000382-prior
  kind: prior_review
  reference: reviews/structured/20261020T071158Z-amsterdam-gut-panel-metadata-review/review.yaml
  locator: Immutable partial metadata assessment, role-metadata and repository-version
    findings; original batch 4 ledger and current tests/test_site_audit_fixes.py renderer
    contract are also bound inputs
  support: context_only
  summary: The earlier assessment explicitly excludes scientific/mechanistic certification.
    Its unresolved roles and repository provenance, the historical graph removals
    and the renderer's prohibition on inferred participant links remain preserved.
    This technical successor does not overwrite or reinterpret that assessment as
    a full review.
  accessed_at: '2026-11-15T11:57:27.552914Z'
assessments:
- assessment_id: 000382-source-scope
  area: grounding
  topic: Species descriptors retain distinct DSM stock and experimental contexts
  outcome: supported
  target_ids:
  - CommunityMech:000382
  evidence_ids:
  - 000382-paper
  - 000382-database
  - 000382-terms
  summary: The selected existing species descriptors retain their source-supported
    stock identities and current authority ranks. Ten-stock, later nine-species model
    and separate assay contexts remain distinct. Source 16S attribution is not an
    independently verified study-stock genome correspondence.
- assessment_id: 000382-native-correspondence
  area: grounding
  topic: Six reference populations and three complete ordered ambiguities
  outcome: supported
  target_ids:
  - CommunityMech:000382
  evidence_ids:
  - 000382-database
  - 000382-gtdb
  - 000382-domain
  summary: The actual native change reproduces all six reviewed reference blocks and
    the complete two-, three- and three-way ambiguity lists. The two rounded 0.99
    populations remain non-unanimous; no stock-specific assignment is inferred. The
    unselected DSM 24404 descriptor remains null/UNRESOLVED.
- assessment_id: 000382-persistence
  area: provenance
  topic: Exact bounded application preserves scientific and historical scope
  outcome: supported
  target_ids:
  - CommunityMech:000382
  evidence_ids:
  - 000382-application
  - 000382-prior
  - 000382-schema
  - 000382-strict
  - 000382-scalars
  - 000382-new-history
  - 000382-history
  summary: The accepted candidate, actual receipt and sidecar bind the nine changed
    descriptors and two native events. Eight scoped commands passed on actual bytes,
    including a one-file strict check with zero errors. Original biology, earlier
    findings and the prior partial review remain unchanged; strict saved-successor
    and composed renderer controls are subsequent acceptance steps, not assumed results.
findings: []
actions: []
limitations:
- Partial technical database-correspondence diagnostic with scientific_review:false.
  Completion of these scoped checks is not whole-record scientific approval, reference-snippet
  coverage, generated-page validation, final corpus QC or campaign completion.
- 'Six reference populations reproduce: Akkermansia muciniphila by species name, 4983
  genomes/fraction 1.0; Bacteroides ovatus by species ID, 3107/0.99; B. thetaiotaomicron
  1011/0.99; Bifidobacterium adolescentis 599/1.0; Escherichia coli 166397/1.0; Roseburia
  intestinalis 78/1.0. Rounded fractions of 0.99 are not unanimity or exact recoverable
  numerators. These populations are not experimental stock counts, inoculum ratios,
  abundance estimates or identity probabilities.'
- Blautia obeum retains both intestinalis/obeum alternatives; Faecalibacterium prausnitzii
  retains longum/prausnitzii/prausnitzii_D; Lactobacillus johnsonii retains johnsonii/sp945980025/sp947171515.
  These ordered native name ambiguities do not select a study-stock genome. The unchanged
  DSM 24404 placeholder has a null native result and remains UNRESOLVED, without a
  guessed species or a biological/domain-absence claim.
- The source names ten DSMZ stocks and reports 16S identity confirmation. That source
  attribution is distinct from an independent stock-sequence or GTDB assembly analysis,
  which was not performed. Source stock names, collection identifiers, canonical species
  labels and prior notes remain unchanged.
- The original ten-stock conditioned-medium panel, the later nine-species model after
  Roseburia exclusion, two-to-four-species validation co-cultures and the E. coli/B.
  ovatus invasion assays remain distinct. This work does not restore the previously
  removed gLV or invasion graph nodes or create member-to-node links.
- The one COMMUNITY_LEVEL conditioned-medium node, absent participating_taxa and zero
  directed edges remain unchanged. Negative endpoint-density effects do not uniquely
  identify competition, toxins or a mediator; growth rate and final density are distinct.
  The ninety donor-acceptor conditions and 60% fresh/40% spent YCFA ratio remain literal
  source context.
- The source phrase '8 mL flasks' does not establish an 8 mL working volume. Finding
  2887 remains outside this correction; no claim is made that uninspected supplementary
  material lacks the quantity. Prior partial-review findings 2232/2233 concerning
  roles and an unpinned data resource remain unresolved. Historical caption and model-size
  discrepancies are not resolved by taxonomy.
- DNA-qPCR relative frequencies are not direct viable-cell counts. Model predictions,
  observed co-culture/invasion outcomes and any in-vivo or pathogen inference remain
  distinct. No mechanism, biological role or cultivation recommendation is added.
- Examination covered the whole current record, the previous partial metadata assessment
  and ledger, the current renderer guard and selected retained primary Methods/Results
  passages. No fresh full scientific paper review, separate supplementary inspection,
  figure-pixel audit, pinned repository snapshot, stock sequence or study-assembly
  verification was performed.
- Historical missing-crosswalk notes and the October partial assessment remain unchanged
  evidence of their earlier scope. Their historical unresolved mapping statements
  are not rewritten or promoted to current scientific clearance. Original scientific
  findings, ledgers and issue dispositions remain preserved.
- Source reporting and binding ran locally at 9bf78f54f83f88f954a309f351d862b4e0495c7a
  with preparation files disclosed. The isolated M5 stage and application began clean
  at e4dc49afd89482371a84ea71829eee6e27d94a1d, with frozen offline dependencies and
  native Python 3.13.2. Later gates correctly observe the applied record. The native
  status log processed ten taxa while its actual event records nine changed statuses.
- Crosswalk SHA-256 is 761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd;
  file mtime does not identify its upstream release. Local NCBITaxon/ENVO/GO readiness
  and identity observations retain actual stat-based provenance, without an invented
  full-database hash. Native terms reports Validation passed without an assertion
  denominator. Strict successor and composed renderer/caller checks remain separate
  follow-up work.
links:
- https://github.com/CultureBotAI/CommunityMech/issues/2848
- https://github.com/CultureBotAI/CommunityMech/issues/2887
- https://github.com/CultureBotAI/CommunityMech/issues/2232
- https://github.com/CultureBotAI/CommunityMech/issues/2233
- https://github.com/CultureBotAI/CommunityMech/pull/2853
```
