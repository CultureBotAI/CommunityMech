# HT RW8: scoped species-name GTDB correspondence diagnostic

- Review: 20261115T083337Z-ht-rw8-species-name-correspondence-diagnostic
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-11-15T08:33:37.517251Z
- Finished UTC: 2026-11-15T08:33:37.649025Z
- Reviewer: codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: false

## Summary

The existing Bacillus vallismortis RW8 descriptor now carries the native species-name GTDB correspondence with one reference genome and fraction 1.0. The native crosswalk has no row for species identifier 72361, so this is explicitly the ncbi_name fallback, not an exact-stock genome assignment. Actual guarded M5 application, append-only native history and eight scoped native commands are bound. HT membership, RW5, source quotations and all existing biological claims remain unchanged.

## Scope And Provenance

One selected taxonomy descriptor's GTDB block/status, its source-species and reference-population boundary, and actual application/check/history provenance. Other biological claims remain outside new scientific certification.

Selection: One whole record, CommunityMech:000347, is the first actual name-fallback canary of the replacement nine-record plan. Record 392 is explicitly held under issue 2877; none of the remaining eight records was applied before this canary's saved proof and complete input checkpoint.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 10810fc7c1346fbceb05503e7c2485ee4edc21e3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000347 | kb/communities/Bacillus_siamensis_vallismortis_HT_Masson_Pine_SynCom.yaml # taxonomy[1].taxon_term.gtdb_classification; gtdb_grounding_status | maintained | Bacillus vallismortis RW8 species-name correspondence |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000347 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-strict | passed | True | CommunityMech:000347 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-gtdb | passed | True | CommunityMech:000347 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-gtdb-domain | passed | True | CommunityMech:000347 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-scalars | passed | True | CommunityMech:000347 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-history | passed | True | CommunityMech:000347 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| new-history | passed | True | CommunityMech:000347 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-terms | passed | True | CommunityMech:000347 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |

## Scientific And Domain Assessments

### Preserved HT and RW8 source identity

grounding: supported. Targets: CommunityMech:000347.

Preserve RW8 as the B. vallismortis member of the two-strain HT community, keeping RW5 and five-member C2 distinct. The available primary cache supports only the declared abstract/transcription coverage. The 16S label does not establish a stock-genome identity.

### Explicit species-name reference population

grounding: supported. Targets: CommunityMech:000347.

The exact crosswalk and native resolver reproduce the name-fallback species correspondence with one reference genome and fraction 1.0. No exact species-ID row, experimental-stock assembly membership, additional genotype or formal nomenclatural change is inferred. Existing NCBI identity and source stock remain unchanged.

### Actual bounded write, history and retained biological limits

provenance: supported. Targets: CommunityMech:000347.

The guarded native write changes only the accepted RW8 GTDB block/status and two appended native events. The new immutable sidecar and eight actual scoped commands are bound. All previous biology, quotations, three current nodes, absent arrows and historical findings remain unchanged; strict successor admission and combined QC are separate.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| 000347-schema | .temp/gtdb-species-status-20261115/second-347-run-schema-002/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000347-strict | .temp/gtdb-species-status-20261115/second-347-run-strict-002/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000347-gtdb | .temp/gtdb-species-status-20261115/second-347-run-gtdb-002/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000347-domain | .temp/gtdb-species-status-20261115/second-347-run-domain-002/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000347-scalars | .temp/gtdb-species-status-20261115/second-347-run-scalars-002/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000347-history | .temp/gtdb-species-status-20261115/second-347-run-history-002/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000347-new-history | .temp/gtdb-species-status-20261115/second-347-run-new-history-002/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000347-terms | .temp/gtdb-species-status-20261115/second-347-run-terms-002/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000347-paper | references_cache/PMID_42144568.txt; Abstract; labeled Figure 4 transcriptions at lines 22 and 33, character offsets 2390 and 2724 | supports | The retained source distinguishes the two-member HT community RW5/RW8 from five-member C2 and labels RW8 as B. vallismortis with 16S accession OQ996934. This pass read those cached transcriptions, not the original figure image or full paper. |
| 000347-database | reports/gtdb-species-status-20261115/second-nine-347-source-evidence-003.json; occurrences[0].ncbi_identity_rows, lookup_indexes, native_result; exact captured reporter and crosswalk input hashes | supports | The existing read-only NCBI adapter identifies 72361 as Bacillus vallismortis at species rank. Complete native lookup evidence records an empty exact-ID route and the species-name fallback to GTDB:s__Bacillus_vallismortis, one reference genome, fraction 1.0 and is_reclassified:false. |
| 000347-application | .temp/gtdb-species-status-20261115/second-347-applied-m5-002/receipt.json; applied, execution_revision, before_sha256, after_sha256, reviewed_receipt_sha256 and inputs | supports | The actual M5 guarded writer persisted the independently accepted candidate 267333e0 at revision 10810fc7. The exact stage, source proof, original bytes, native inline events and new sidecar are preserved and checked separately. |
| 000347-prior | reports/phase2-completion-20261115/species-ht-light-source-context-001.yaml; CommunityMech:000347 source and historical_guard sections, inherited findings 2352–2356/2360; current bound test_causal_review_batch6.py | context_only | The accepted source-context plan retains prior scientific limitations and distinguishes the direct batch 6 current-biological assertions from indirect batch 105/123 ledger search hits. The source plan and direct caller bytes are exact captured inputs; this mapping diagnostic does not retire their scientific findings. |

## Limits And Additional Notes

- Partial technical and provenance assessment with scientific_review:false; neither full scientific record approval nor a corpus QC pass is inferred from native checks.
- The inspected primary-source cache contains the abstract and labeled Figure 4 composition/16S transcriptions. This pass did not newly inspect the figure image, full methods/results or supplements. The retained transcription supports the narrow HT/RW8 context only within that declared coverage.
- NCBITaxon:72361 is the source species identity. The current crosswalk has no exact species-ID row and resolves the same species name through one reference genome. OQ996934 is a 16S accession, not an assembly; experimental stock RW8 is not assigned that reference genome.
- The table's exact SHA256 binds its bytes. File mtime is not a release date, and this diagnostic does not certify an upstream GTDB release. Local NCBI file-stat observations are not a content hash or a database release assertion.
- The unselected RW5 block, all original source quotations, three current biological endpoints and absence of causal arrows remain unchanged. Mapping does not resolve the retained source-plan issues 2352–2356/2360 concerning endpoints, timing, gene panels, cultivation, aliases or historical prose.
- Seven scoped validators plus native history scaffolding are separate from source-snippet comparison, generated pages, strict historical successor admission and combined full QC. Those integration outcomes remain independently accounted.
- Original ten-record preparation 001 remains historical evidence. The replacement 002 plan preserves the whole-record 392 hold for its deliberate R232 manual dispositions rather than replacing them with this pinned crosswalk's result.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261115T083337Z-ht-rw8-species-name-correspondence-diagnostic
kind: record
repository: CultureBotAI/CommunityMech
title: 'HT RW8: scoped species-name GTDB correspondence diagnostic'
started_at: '2026-11-15T08:33:37.517251Z'
finished_at: '2026-11-15T08:33:37.649025Z'
reviewer:
  identity: codex
  kind: agent
  independence: self_review
  independence_basis: The source context, local authority rows and complete native
    name-fallback population were read before staging. Parent independently read the
    exact source plan, accepted candidate and receipt. A separate peer source pass
    identified record 392's conflicting R232 dispositions; the replacement nine-record
    plan excludes that whole record. This is the first real name-fallback canary for
    the replacement plan.
skill: curate-yaml-record
completion: completed
verdict: pass_with_limitations
scientific_review: false
summary: The existing Bacillus vallismortis RW8 descriptor now carries the native
  species-name GTDB correspondence with one reference genome and fraction 1.0. The
  native crosswalk has no row for species identifier 72361, so this is explicitly
  the ncbi_name fallback, not an exact-stock genome assignment. Actual guarded M5
  application, append-only native history and eight scoped native commands are bound.
  HT membership, RW5, source quotations and all existing biological claims remain
  unchanged.
source:
  git_revision: 10810fc7c1346fbceb05503e7c2485ee4edc21e3
  state: working_tree
  inputs:
  - path: .temp/gtdb-species-status-20261115/kg-microbe/data/raw/NCBI2GTDB.tsv.gz
    sha256: 761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd
    role: context
  - path: .temp/gtdb-species-status-20261115/second-347-applied-m5-002/before.yaml
    sha256: 27ce7cf055aef35383089e1adeac31ea1cbab0c5c3b9765537b188da34a48cff
    role: context
  - path: .temp/gtdb-species-status-20261115/second-347-applied-m5-002/receipt.json
    sha256: a66b9c572d69741e09f8daf15449b2d29660de7a8b516227ab81c4952b222789
    role: context
  - path: .temp/gtdb-species-status-20261115/second-347-run-domain-002/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-species-status-20261115/second-347-run-domain-002/native.log
    sha256: f21d8ac5ca91675bdaf291a9a44ecb769a7b5cbe13448ab024b6789cd16412df
    role: context
  - path: .temp/gtdb-species-status-20261115/second-347-run-domain-002/receipt.json
    sha256: 0afd1ddaa66b7e2807ed47466bc4f6762331c7f03d55d0ba81e95841a3b9d376
    role: context
  - path: .temp/gtdb-species-status-20261115/second-347-run-domain-002/start.json
    sha256: 46559d5b092e81a14833eb642a6f114e115db878e0efadd60fbc3263b4c90cc3
    role: context
  - path: .temp/gtdb-species-status-20261115/second-347-run-gtdb-002/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-species-status-20261115/second-347-run-gtdb-002/native.log
    sha256: 3717da27a451c447c66abcf28ed266e14c659ee6983d59d4cd5e38b683453d19
    role: context
  - path: .temp/gtdb-species-status-20261115/second-347-run-gtdb-002/receipt.json
    sha256: 54828844782563c03a79c54bf49e574d3f675cc13e81ec205d16f0e5c5a6f789
    role: context
  - path: .temp/gtdb-species-status-20261115/second-347-run-gtdb-002/start.json
    sha256: 7b0ce168d755d0abbedcbc4db59e7288975495e6d5737c4c9e9702146f5deaeb
    role: context
  - path: .temp/gtdb-species-status-20261115/second-347-run-history-002/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-species-status-20261115/second-347-run-history-002/native.log
    sha256: 700b44227c4cf01270ac26f16b308622de0b26f48d71aec49cdfaaab87620f0a
    role: context
  - path: .temp/gtdb-species-status-20261115/second-347-run-history-002/receipt.json
    sha256: cb406f7622a201ccd6ea5b57e931115dd5162b75a7958bf95e6597a5184acf11
    role: context
  - path: .temp/gtdb-species-status-20261115/second-347-run-history-002/start.json
    sha256: 688e6475c39fe3513e80b108431546311b378a8b89d169e52d9c5a12f4f43c88
    role: context
  - path: .temp/gtdb-species-status-20261115/second-347-run-new-history-002/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-species-status-20261115/second-347-run-new-history-002/native.log
    sha256: 3b646982c13d3fb277f6b4604440f2ccf4e2da6880e05843f7ac9ea63171eb45
    role: context
  - path: .temp/gtdb-species-status-20261115/second-347-run-new-history-002/receipt.json
    sha256: 704caff431e6ed177bb0e4b09ce1574aad5b9297dc10ca87c1f8dc5b9c3c7808
    role: context
  - path: .temp/gtdb-species-status-20261115/second-347-run-new-history-002/start.json
    sha256: f16d8fc97eaa4ff72c22495487159ee40d4e62d09131be1dbf1235bea6ff869c
    role: context
  - path: .temp/gtdb-species-status-20261115/second-347-run-scalars-002/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-species-status-20261115/second-347-run-scalars-002/native.log
    sha256: b5e6ddf6a3806c975221409dccba79ca79a6963cecdf3a3a5f1dfce83333d2de
    role: context
  - path: .temp/gtdb-species-status-20261115/second-347-run-scalars-002/receipt.json
    sha256: 3fcd5fe96edf5ede20df065a392646e971cd6c2b5f293d40dc5c769b235507ee
    role: context
  - path: .temp/gtdb-species-status-20261115/second-347-run-scalars-002/start.json
    sha256: 8dd118cb932fd7b7dd8a88ec37660ce3e68d034f97783ab38906b570e1c324a5
    role: context
  - path: .temp/gtdb-species-status-20261115/second-347-run-schema-002/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-species-status-20261115/second-347-run-schema-002/native.log
    sha256: 93f13ca6549a0e826f7380dc0bdf7bfdf9b2278062365e89b08cb7be16304230
    role: context
  - path: .temp/gtdb-species-status-20261115/second-347-run-schema-002/receipt.json
    sha256: fc3df0edde1beed7cbb650a2118eee111b87c8746e4f84b2fe11cc98fa1c0251
    role: context
  - path: .temp/gtdb-species-status-20261115/second-347-run-schema-002/start.json
    sha256: 792a552004bb33cafa71133ad8a34f70267aaff0e6a60b69269cabfcbeee5fd8
    role: context
  - path: .temp/gtdb-species-status-20261115/second-347-run-strict-002/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-species-status-20261115/second-347-run-strict-002/native.log
    sha256: 0b796ac0e831c180724eb5918946189d44a29aa83b0d664ce3460318a2b1425f
    role: context
  - path: .temp/gtdb-species-status-20261115/second-347-run-strict-002/receipt.json
    sha256: b8471c7411ab854c725793cd5079f57dcf5a457d0e5db96146cb58df1822ca7e
    role: context
  - path: .temp/gtdb-species-status-20261115/second-347-run-strict-002/start.json
    sha256: 4bd36e4880b666cf5160b80ceeadc9e5216ddc933614357dfc30007bfd7afbdc
    role: context
  - path: .temp/gtdb-species-status-20261115/second-347-run-strict-002/strict.tsv
    sha256: b184ed5450b968070bb6c75648407e388f41a1eaf7017890723cf560999fc3f7
    role: context
  - path: .temp/gtdb-species-status-20261115/second-347-run-terms-002/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-species-status-20261115/second-347-run-terms-002/native.log
    sha256: a7eeb5faba97ca0933dbde1af31e993537ef47cd4c8d2f1bf74f4dce39458d4f
    role: context
  - path: .temp/gtdb-species-status-20261115/second-347-run-terms-002/receipt.json
    sha256: 30d03b6010a83b7a7b450c120b2e1a98ec7a43c4df55d9b4f0d64cc1cd56ad91
    role: context
  - path: .temp/gtdb-species-status-20261115/second-347-run-terms-002/start.json
    sha256: afe98262ab76af4ad7d6884ae1a9ae9c2f37b3a4aab0b89943d15876fa3c02ef
    role: context
  - path: .temp/gtdb-species-status-20261115/second-347-staged-002/Bacillus_siamensis_vallismortis_HT_Masson_Pine_SynCom.yaml
    sha256: 267333e05958810b27ef081f9a14d7782ebbf7412a5981d861f0c9d3e34d073e
    role: context
  - path: .temp/gtdb-species-status-20261115/second-347-staged-002/receipt.json
    sha256: 3325ae3a150350b796d019614e0abe6b06ed4a33e2a5ad4d10f9b0216a3bbe63
    role: context
  - path: .temp/phase2-schema-20261115/species-second-context-347-002.log
    sha256: 9266d458de5c29276516cdfcf6516ba72e9508ea601fb6b2c8cf4a460ff16d59
    role: context
  - path: .temp/phase2-schema-20261115/species-second-route-ten-001.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/phase2-schema-20261115/species-second-route-ten-001.json
    sha256: 01507cda7ceac6116a466ec9103b202c17a6908ece560d7dd6af8b13f64b68e9
    role: context
  - path: .temp/phase2-schema-20261115/species-second-route-ten-001.log
    sha256: 6637cd67369cd53d77223836be30fb9170e106bfc84290d093343ffce0a7e913
    role: context
  - path: history/records/Bacillus_siamensis_vallismortis_HT_Masson_Pine_SynCom/2026-09-11T143458Z-codex-421445.yaml
    sha256: 541be9584126f96f148581dc0135fdaf1de6d4fdd13208ce843a81320e5eb012
    role: context
  - path: history/records/Bacillus_siamensis_vallismortis_HT_Masson_Pine_SynCom/2026-10-05T112951Z-codex-12cf22.yaml
    sha256: cc1e18295e8ef2c698c439c39b041cf6d3d934f72b8fc1c2113473be05413298
    role: context
  - path: history/records/Bacillus_siamensis_vallismortis_HT_Masson_Pine_SynCom/2026-10-21T190000Z-claude-2049.yaml
    sha256: 5dc080b0ca418ccc5eefe755e646d229dcc3e19aca9cfac9c4fcaff0be0fb0b5
    role: context
  - path: history/records/Bacillus_siamensis_vallismortis_HT_Masson_Pine_SynCom/2026-11-15T082919Z-codex-94f925.yaml
    sha256: 0363505738a9820edb2b7208b14fe79bc5438e26324425ae3c67ea09a808bb09
    role: context
  - path: justfile
    sha256: 40369611ad4531582e420df0e9ff22109e4b18adf03b34d86b54200b280f2d0f
    role: context
  - path: kb/communities/Bacillus_siamensis_vallismortis_HT_Masson_Pine_SynCom.yaml
    sha256: 267333e05958810b27ef081f9a14d7782ebbf7412a5981d861f0c9d3e34d073e
    role: target
  - path: pyproject.toml
    sha256: be952f0f137f85fed66bda0908f12014f1797a2dd229b44d832afc0c00471655
    role: context
  - path: references_cache/PMID_42144568.txt
    sha256: d2cf960eca50e700df52316443b8a45c78b6509ea83982aa984c0768ed9ae006
    role: context
  - path: reports/gtdb-species-status-20261115/second-nine-347-gate-config-002.json
    sha256: 91e3055a5fa952808d89fa7b462788e284dc879418d0979488a7a144a44c0a3e
    role: context
  - path: reports/gtdb-species-status-20261115/second-nine-347-review-config-003.json
    sha256: 282f138cbde982c6f12ab2f3f06f7798ef7014a428c2546722f729218c6e18f3
    role: context
  - path: reports/gtdb-species-status-20261115/second-nine-347-source-canary-config-002.json
    sha256: 9012865edb4672c186398032fc11287cf404819c89aef687684206b6d7d9edfd
    role: context
  - path: reports/gtdb-species-status-20261115/second-nine-347-source-evidence-003.json
    sha256: 9743695872c1780cbb20458b1e837d238cb330a72c64fc11049b8cf12eefaa00
    role: context
  - path: reports/gtdb-species-status-20261115/second-nine-authored-source-context-002.json
    sha256: 1a030a25515b829984dcccaf3a9b43e4fd9179dbc7a5d09d47dce314fd361174
    role: context
  - path: reports/gtdb-species-status-20261115/second-nine-source-config-002.json
    sha256: 620595fb2e6818f29af36be00f8aa97d276f15af2b3d1c751d589ef65af96ff4
    role: context
  - path: reports/gtdb-species-status-20261115/species-second-ten-route-plan-001.json
    sha256: 287b29673e0a1d4dab7c0e0c67eeb6a87e19190bf2301b98ba745d4eb0852b98
    role: context
  - path: reports/phase2-completion-20261115/species-ht-light-source-context-001.yaml
    sha256: b74d5bca95b91a06b87805cbd8fcf82e75433650bd804ffbeb3fbd6ab4e779e1
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
  - path: scripts/adhoc/gtdb_source_unit_transfer_paths_v2_20261115.jq
    sha256: 3ba4321c79ba9e4fa7632c49423fc1259d6a061518c5c729a8f05d0379c63cc8
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
- target_id: CommunityMech:000347
  path: kb/communities/Bacillus_siamensis_vallismortis_HT_Masson_Pine_SynCom.yaml
  selector: taxonomy[1].taxon_term.gtdb_classification; gtdb_grounding_status
  label: Bacillus vallismortis RW8 species-name correspondence
  kind: maintained
  ownership_note: CommunityMech owns this record; only declared GTDB correspondence/status
    and actual provenance are assessed.
scope:
  description: One selected taxonomy descriptor's GTDB block/status, its source-species
    and reference-population boundary, and actual application/check/history provenance.
    Other biological claims remain outside new scientific certification.
  selection: One whole record, CommunityMech:000347, is the first actual name-fallback
    canary of the replacement nine-record plan. Record 392 is explicitly held under
    issue 2877; none of the remaining eight records was applied before this canary's
    saved proof and complete input checkpoint.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000347
  exclusions:
  - target: Other scientific claims and records
    reason: Existing biology is preserved, not newly certified by this database diagnostic.
checks:
- check_id: 000347-schema
  name: validate
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000347
  command: just --verbose --no-dotenv --color never validate kb/communities/Bacillus_siamensis_vallismortis_HT_Masson_Pine_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000347-schema
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000347-strict
  name: validate-strict
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000347
  command: just --verbose --no-dotenv --color never validate-strict kb/communities/Bacillus_siamensis_vallismortis_HT_Masson_Pine_SynCom.yaml
    --out .temp/gtdb-species-status-20261115/second-347-run-strict-002/strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000347-strict
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000347-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000347
  command: just --verbose --no-dotenv --color never validate-gtdb kb/communities/Bacillus_siamensis_vallismortis_HT_Masson_Pine_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000347-gtdb
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000347-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000347
  command: just --verbose --no-dotenv --color never validate-gtdb-domain kb/communities/Bacillus_siamensis_vallismortis_HT_Masson_Pine_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000347-domain
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000347-scalars
  name: validate-scalars
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000347
  command: just --verbose --no-dotenv --color never validate-scalars kb/communities/Bacillus_siamensis_vallismortis_HT_Masson_Pine_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000347-scalars
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000347-history
  name: validate-history
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000347
  command: just --verbose --no-dotenv --color never validate-history history/records/Bacillus_siamensis_vallismortis_HT_Masson_Pine_SynCom
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000347-history
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000347-new-history
  name: new-history
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000347
  command: just --verbose --no-dotenv --color never new-history --kind record --slug
    Bacillus_siamensis_vallismortis_HT_Masson_Pine_SynCom --target-root kb/communities
    --event EDIT --outcome changed --sections taxonomy,curation_history --actor-name
    codex --model gpt-6 --agent-tool codex --issue https://github.com/CultureBotAI/CommunityMech/issues/2848
    --summary 'Add the species-name GTDB correspondence for the existing Bacillus
    vallismortis RW8 descriptor' --details 'Preserve the two-strain HT identity and
    the distinct RW5 mapping. The native species-name fallback for Bacillus vallismortis
    reproduces one reference genome and fraction 1.0; it does not assign an assembly
    to study stock RW8. OQ996934 remains 16S evidence, not a genome accession. Only
    taxonomy[1] GTDB block/status and two native inline events changed. Existing source
    quotations, three biological endpoints, lack of causal arrows, uncertainty and
    prior history remain unchanged. Scoped database and provenance correction; full
    scientific approval and corpus QC are separate. Actual apply receipt .temp/gtdb-species-status-20261115/second-347-applied-m5-002/receipt.json
    sha256:a66b9c572d69741e09f8daf15449b2d29660de7a8b516227ab81c4952b222789.'
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000347-new-history
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000347-terms
  name: validate-terms
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000347
  command: just --verbose --no-dotenv --color never validate-terms kb/communities/Bacillus_siamensis_vallismortis_HT_Masson_Pine_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000347-terms
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
evidence:
- evidence_id: 000347-schema
  kind: validation
  reference: .temp/gtdb-species-status-20261115/second-347-run-schema-002/native.log
  accessed_at: '2026-11-15T08:33:37.517251Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000347-strict
  kind: validation
  reference: .temp/gtdb-species-status-20261115/second-347-run-strict-002/native.log
  accessed_at: '2026-11-15T08:33:37.517251Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000347-gtdb
  kind: validation
  reference: .temp/gtdb-species-status-20261115/second-347-run-gtdb-002/native.log
  accessed_at: '2026-11-15T08:33:37.517251Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000347-domain
  kind: validation
  reference: .temp/gtdb-species-status-20261115/second-347-run-domain-002/native.log
  accessed_at: '2026-11-15T08:33:37.517251Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000347-scalars
  kind: validation
  reference: .temp/gtdb-species-status-20261115/second-347-run-scalars-002/native.log
  accessed_at: '2026-11-15T08:33:37.517251Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000347-history
  kind: validation
  reference: .temp/gtdb-species-status-20261115/second-347-run-history-002/native.log
  accessed_at: '2026-11-15T08:33:37.517251Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000347-new-history
  kind: validation
  reference: .temp/gtdb-species-status-20261115/second-347-run-new-history-002/native.log
  accessed_at: '2026-11-15T08:33:37.517251Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000347-terms
  kind: validation
  reference: .temp/gtdb-species-status-20261115/second-347-run-terms-002/native.log
  accessed_at: '2026-11-15T08:33:37.517251Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000347-paper
  kind: primary_source
  reference: references_cache/PMID_42144568.txt
  locator: Abstract; labeled Figure 4 transcriptions at lines 22 and 33, character
    offsets 2390 and 2724
  support: supports
  summary: The retained source distinguishes the two-member HT community RW5/RW8 from
    five-member C2 and labels RW8 as B. vallismortis with 16S accession OQ996934.
    This pass read those cached transcriptions, not the original figure image or full
    paper.
  accessed_at: '2026-11-15T08:33:37.517251Z'
- evidence_id: 000347-database
  kind: database
  reference: reports/gtdb-species-status-20261115/second-nine-347-source-evidence-003.json
  locator: occurrences[0].ncbi_identity_rows, lookup_indexes, native_result; exact
    captured reporter and crosswalk input hashes
  support: supports
  summary: The existing read-only NCBI adapter identifies 72361 as Bacillus vallismortis
    at species rank. Complete native lookup evidence records an empty exact-ID route
    and the species-name fallback to GTDB:s__Bacillus_vallismortis, one reference
    genome, fraction 1.0 and is_reclassified:false.
  accessed_at: '2026-11-15T08:33:37.517251Z'
- evidence_id: 000347-application
  kind: record_content
  reference: .temp/gtdb-species-status-20261115/second-347-applied-m5-002/receipt.json
  locator: applied, execution_revision, before_sha256, after_sha256, reviewed_receipt_sha256
    and inputs
  support: supports
  summary: The actual M5 guarded writer persisted the independently accepted candidate
    267333e0 at revision 10810fc7. The exact stage, source proof, original bytes,
    native inline events and new sidecar are preserved and checked separately.
  accessed_at: '2026-11-15T08:33:37.517251Z'
- evidence_id: 000347-prior
  kind: prior_review
  reference: reports/phase2-completion-20261115/species-ht-light-source-context-001.yaml
  locator: CommunityMech:000347 source and historical_guard sections, inherited findings
    2352–2356/2360; current bound test_causal_review_batch6.py
  support: context_only
  summary: The accepted source-context plan retains prior scientific limitations and
    distinguishes the direct batch 6 current-biological assertions from indirect batch
    105/123 ledger search hits. The source plan and direct caller bytes are exact
    captured inputs; this mapping diagnostic does not retire their scientific findings.
  accessed_at: '2026-11-15T08:33:37.517251Z'
assessments:
- assessment_id: 000347-source
  area: grounding
  topic: Preserved HT and RW8 source identity
  outcome: supported
  target_ids:
  - CommunityMech:000347
  evidence_ids:
  - 000347-paper
  - 000347-database
  - 000347-terms
  summary: Preserve RW8 as the B. vallismortis member of the two-strain HT community,
    keeping RW5 and five-member C2 distinct. The available primary cache supports
    only the declared abstract/transcription coverage. The 16S label does not establish
    a stock-genome identity.
- assessment_id: 000347-population
  area: grounding
  topic: Explicit species-name reference population
  outcome: supported
  target_ids:
  - CommunityMech:000347
  evidence_ids:
  - 000347-database
  - 000347-gtdb
  - 000347-domain
  summary: The exact crosswalk and native resolver reproduce the name-fallback species
    correspondence with one reference genome and fraction 1.0. No exact species-ID
    row, experimental-stock assembly membership, additional genotype or formal nomenclatural
    change is inferred. Existing NCBI identity and source stock remain unchanged.
- assessment_id: 000347-provenance
  area: provenance
  topic: Actual bounded write, history and retained biological limits
  outcome: supported
  target_ids:
  - CommunityMech:000347
  evidence_ids:
  - 000347-application
  - 000347-schema
  - 000347-strict
  - 000347-scalars
  - 000347-new-history
  - 000347-history
  - 000347-prior
  summary: The guarded native write changes only the accepted RW8 GTDB block/status
    and two appended native events. The new immutable sidecar and eight actual scoped
    commands are bound. All previous biology, quotations, three current nodes, absent
    arrows and historical findings remain unchanged; strict successor admission and
    combined QC are separate.
findings: []
actions: []
limitations:
- Partial technical and provenance assessment with scientific_review:false; neither
  full scientific record approval nor a corpus QC pass is inferred from native checks.
- The inspected primary-source cache contains the abstract and labeled Figure 4 composition/16S
  transcriptions. This pass did not newly inspect the figure image, full methods/results
  or supplements. The retained transcription supports the narrow HT/RW8 context only
  within that declared coverage.
- NCBITaxon:72361 is the source species identity. The current crosswalk has no exact
  species-ID row and resolves the same species name through one reference genome.
  OQ996934 is a 16S accession, not an assembly; experimental stock RW8 is not assigned
  that reference genome.
- The table's exact SHA256 binds its bytes. File mtime is not a release date, and
  this diagnostic does not certify an upstream GTDB release. Local NCBI file-stat
  observations are not a content hash or a database release assertion.
- The unselected RW5 block, all original source quotations, three current biological
  endpoints and absence of causal arrows remain unchanged. Mapping does not resolve
  the retained source-plan issues 2352–2356/2360 concerning endpoints, timing, gene
  panels, cultivation, aliases or historical prose.
- Seven scoped validators plus native history scaffolding are separate from source-snippet
  comparison, generated pages, strict historical successor admission and combined
  full QC. Those integration outcomes remain independently accounted.
- Original ten-record preparation 001 remains historical evidence. The replacement
  002 plan preserves the whole-record 392 hold for its deliberate R232 manual dispositions
  rather than replacing them with this pinned crosswalk's result.
links:
- https://github.com/CultureBotAI/CommunityMech/issues/2848
- https://github.com/CultureBotAI/CommunityMech/issues/2877
- https://github.com/CultureBotAI/CommunityMech/issues/2873
- https://github.com/CultureBotAI/CommunityMech/pull/2862
```
