# FOS gut community: two reference correspondences and complete reuteri alternatives

- Review: 20261115T121824Z-fos-gut-reference-correspondence-diagnostic
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-11-15T12:18:23.904988Z
- Finished UTC: 2026-11-15T12:18:24.055009Z
- Reviewer: codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: false

## Summary

Three existing taxonomy descriptors now have two native species-reference blocks with GROUNDED status and one complete four-option ambiguity set with AMBIGUOUS status. All four existing blocks remain unchanged, including the two explicitly curated R232 mappings. All seven stocks, original source notes, three community-level nodes with participant counts 7/3/7, zero arrows, two open discussions and prior history are preserved. The reference populations do not identify stock genomes or resolve biological findings.

## Scope And Provenance

CommunityMech:000466 taxonomy indices 2, 3 and 5: two reference blocks, one complete ambiguity set, three changed statuses and two native inline events, with guarded application, appended native sidecar and eight scoped native checks. All four unselected descriptors and all biological content are preserved.

Selection: The second whole record in the separately prepared 382/466 pair, after the complete Amsterdam canary and its saved-input checkpoint, public proof and actual strict controls were verified and published. This diagnostic reviews exactly one record. It does not repeat or supersede the Amsterdam assessment.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base e4dc49afd89482371a84ea71829eee6e27d94a1d.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000466 | kb/communities/FOS_Lactobacillus_MinimalCore_GutLiver_SynCom.yaml # taxonomy[3,5].taxon_term.gtdb_classification; taxonomy[2,3,5].taxon_term.gtdb_grounding_status; taxonomy[2].taxon_term.gtdb_candidates | maintained | Two species-reference mappings and four preserved reuteri alternatives |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000466 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-strict | passed | True | CommunityMech:000466 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-gtdb | passed | True | CommunityMech:000466 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-gtdb-domain | passed | True | CommunityMech:000466 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-scalars | passed | True | CommunityMech:000466 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-history | passed | True | CommunityMech:000466 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| new-history | passed | True | CommunityMech:000466 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| validate-terms | passed | True | CommunityMech:000466 | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |

## Scientific And Domain Assessments

### Existing species descriptors retain their distinct source stocks and assay contexts

grounding: supported. Targets: CommunityMech:000466.

PBS072, CL02T12C19 and 1_3_50AFAA retain their source identities and authority species ranks without stock-genome inference. The three probiotic stocks, four minimal-core stocks and seven-stock whole community remain distinct; DNA enumeration, expression and metabolite profiling are not conflated.

### Two native reference populations and the complete reuteri ambiguity

grounding: supported. Targets: CommunityMech:000466.

The actual change reproduces cellulosilyticus 1018/1.0 by species name and plautii 142/0.98 by exact species ID, plus all four ordered reuteri alternatives. The rounded fraction 0.98 is not unanimity. All four old blocks, especially the two curated R232 mappings, remain exact; no new stock assembly or single ambiguous choice is inferred.

### Bounded persisted application preserves scientific and historical constraints

provenance: supported. Targets: CommunityMech:000466.

The accepted candidate, actual receipt and sidecar bind three changed descriptors and two native inline events. All eight scoped commands passed on the actual record, including one-file strict validation with zero errors. Three nodes, zero arrows, both discussions and prior needs_research scope remain unchanged. Strict saved-successor and historical caller controls are subsequent acceptance steps, not assumed results.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| 000466-schema | .temp/gtdb-code006-20261115/gut-pair-466-run-schema-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000466-strict | .temp/gtdb-code006-20261115/gut-pair-466-run-strict-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000466-gtdb | .temp/gtdb-code006-20261115/gut-pair-466-run-gtdb-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000466-domain | .temp/gtdb-code006-20261115/gut-pair-466-run-domain-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000466-scalars | .temp/gtdb-code006-20261115/gut-pair-466-run-scalars-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000466-history | .temp/gtdb-code006-20261115/gut-pair-466-run-history-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000466-new-history | .temp/gtdb-code006-20261115/gut-pair-466-run-new-history-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000466-terms | .temp/gtdb-code006-20261115/gut-pair-466-run-terms-001/native.log | supports | Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs. |
| 000466-paper | https://doi.org/10.3389/fmicb.2026.1866842; Retained Methods 2.1 and Table 1 stock roster and DNA-qPCR calibration, flattened line 77; active-compound limitation on line 78; exact primary_locators retained in captured source metadata | supports | The inspected source names the three selected stocks within distinct probiotic, minimal-core and whole-community contexts. It reports genomic-DNA calibration for enumeration. It does not independently place a study-stock genome into a GTDB cluster or establish a causal host-active mediator. |
| 000466-database | reports/gtdb-code006-20261115/gut-pair-466-source-evidence-001.json; Selected indices 2,3,5: full native_result, classify_status, lookup_indexes, crosswalk_rows and ncbi_identity_rows; explicit unselected curated-block boundary | supports | Pinned native results support the name-route cellulosilyticus population, exact-ID plautii population and complete four-way reuteri ambiguity. These reference correspondences do not identify stock assemblies; the four pre-existing blocks, including two manual R232 pins, remain unchanged. |
| 000466-application | .temp/gtdb-code006-20261115/gut-pair-466-applied-001/receipt.json; Actual before/after, external reviewed candidate/receipt pins, all captured inputs, two-block/three-status native inline events and appended sidecar | supports | The exact peer-reviewed candidate was persisted on isolated M5. Only three selected GTDB field groups and two native events change; the seven stocks, four earlier mappings, all scientific assertions and prior history remain unchanged. |
| 000466-prior | reports/causal_graph_review/decisions/20261006-three-records-batch39.yaml; FOS needs_research disposition, historical source/figure scope and follow-ups; all eight tests/test_causal_review_batch39.py predicates are captured unchanged | context_only | The earlier ledger preserves assay distinctions and a pending host-response expansion. Its historical scientific observations and cache pins remain unchanged. This technical diagnostic does not resolve the existing biological findings or reclassify the record as scientifically complete. |

## Limits And Additional Notes

- Partial technical database-correspondence diagnostic with scientific_review:false. These scoped checks are not whole-record scientific approval, reference-snippet coverage, generated-page validation, final corpus QC or campaign completion.
- Bacteroides cellulosilyticus uses the species-name route with 1018 reference genomes and fraction 1.0. Flavonifractor plautii uses the exact species-ID route with 142 genomes and rounded fraction 0.98, which is not unanimity or an exactly recoverable numerator. These are reference populations, not inoculum composition, experimental abundance, stock genomes or identity probabilities.
- Limosilactobacillus reuteri PBS072 retains all four ordered native alternatives: reuteri, reuteri_E, reuteri_G and rodentium. No single correspondence block or study-stock genome is selected from this ambiguity.
- The four original plantarum, acidophilus, symbiosum and Escherichia coli blocks remain unchanged. In particular, the curated R232 acidophilus mapping at 158/0.994 and symbiosum mapping at 112/0.964 are not overwritten by the differing fresh uncurated populations. This correction does not newly certify their release or source statements.
- Methods 2.1 and Table 1 identify PBS072/DSM 25175, CL02T12C19/HM-726 and 1_3_50AFAA/HM-303. Stock identifiers, former names and the BEI/HM notes remain literal source context; no independent stock sequence or assembly placement was performed. The three probiotic stocks, four-stock minimal core and seven-stock whole community remain distinct.
- DNA-qPCR genomic-DNA calibration is not a viable-cell count or an RNA-expression assay. RNA/cDNA expression and strain enumeration remain separate. The 2% FOS versus 1% glucose comparison is not carbon-mass matched; qualitative GC-MS profiles are not quantified yields, ionic speciation or partner-resolved metabolic flux.
- The three COMMUNITY_LEVEL nodes retain seven, three and seven participants and zero directed edges. Historical Figure 7C panel-label observations do not establish physiological absence, and the active host compound, Cd36 mediation and requested HepG2 expansion remain unresolved. No cross-feeding arrow, uniform degrader role or clinical efficacy claim is introduced.
- The prior batch 39 needs_research disposition, two open discussions and historical follow-ups 1449/1450 remain unchanged. No current issue-state change or provider job is claimed. The earlier full caption/figure observations are historical evidence, not a new pixel inspection in this technical pass.
- Examination covered the complete current record, original batch 39 ledger/caller, selected retained primary stock and assay passages and the captured native mapping/authority results. No fresh full scientific review, separate supplementary audit, figure-pixel inspection, stock sequence or study-assembly analysis was performed.
- Source reporting and binding ran locally at 9bf78f54f83f88f954a309f351d862b4e0495c7a with preparation files disclosed. Actual FOS staging, application and gates ran at frozen M5 e4dc49afd89482371a84ea71829eee6e27d94a1d using native Python 3.13.2 and frozen offline dependencies. The earlier Amsterdam correction and saved evidence were present; this is not a new clean-tree claim. Seven processed taxa are distinct from three changed statuses and two added blocks.
- Crosswalk SHA-256 is 761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd; file mtime does not establish its upstream release. Local authority observations retain their actual stat-based provenance without an invented full-database hash. Native terms reports Validation passed without an assertion denominator. Strict saved-successor and historical caller controls remain separate follow-up work.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261115T121824Z-fos-gut-reference-correspondence-diagnostic
kind: record
repository: CultureBotAI/CommunityMech
title: 'FOS gut community: two reference correspondences and complete reuteri alternatives'
started_at: '2026-11-15T12:18:23.904988Z'
finished_at: '2026-11-15T12:18:24.055009Z'
reviewer:
  identity: codex
  kind: agent
  independence: self_review
  independence_basis: A peer independently read the complete source configurations,
    both records, selected primary stock passages and historical guards. The same
    peer separately read the exact actual FOS candidate, receipt and source proof,
    rehashing all 30 staged inputs before application. The parent authorized the accepted
    bounded correction. The shared engine, checker, builder and exporter have separate
    reviews and mutation controls. This is self-review of the technical correspondence
    correction, not an independent full scientific assessment.
skill: curate-yaml-record
completion: completed
verdict: pass_with_limitations
scientific_review: false
summary: Three existing taxonomy descriptors now have two native species-reference
  blocks with GROUNDED status and one complete four-option ambiguity set with AMBIGUOUS
  status. All four existing blocks remain unchanged, including the two explicitly
  curated R232 mappings. All seven stocks, original source notes, three community-level
  nodes with participant counts 7/3/7, zero arrows, two open discussions and prior
  history are preserved. The reference populations do not identify stock genomes or
  resolve biological findings.
source:
  git_revision: e4dc49afd89482371a84ea71829eee6e27d94a1d
  state: working_tree
  inputs:
  - path: .temp/gtdb-code006-20261115/gut-pair-466-applied-001/before.yaml
    sha256: 0ca3ae19e967be3786f5495c5633b088efc2afd4dbe18c322eb2a3a6447d29ef
    role: context
  - path: .temp/gtdb-code006-20261115/gut-pair-466-applied-001/receipt.json
    sha256: 12ded3e3e38941bf3aeab5a5e6b3fef4aca4dedaf3a0e295548990adefbfaca8
    role: context
  - path: .temp/gtdb-code006-20261115/gut-pair-466-candidate-001/FOS_Lactobacillus_MinimalCore_GutLiver_SynCom.yaml
    sha256: e3be57fc8ea10f165adb310f066907c763f13798ffc76a13e948a1b217e605ff
    role: context
  - path: .temp/gtdb-code006-20261115/gut-pair-466-candidate-001/receipt.json
    sha256: ea1cb432fe417896f906562030d772ad5ebb17e72d48ee17ba5b7369ca110e44
    role: context
  - path: .temp/gtdb-code006-20261115/gut-pair-466-check-config-001.json
    sha256: e50d9b5a394aefe702ae43de5ad1cba7156200bcf906965c0c6a821964b5d1db
    role: context
  - path: .temp/gtdb-code006-20261115/gut-pair-466-run-domain-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/gut-pair-466-run-domain-001/native.log
    sha256: 89952b4c7756943c14b3e400fa5a2aab4a447bf4140dbee8b21eae4be674c934
    role: context
  - path: .temp/gtdb-code006-20261115/gut-pair-466-run-domain-001/receipt.json
    sha256: 13af08fd4bd3bf35eb8067774e57fa93d101c0aa61a77562bbc15cb89b6c8fb0
    role: context
  - path: .temp/gtdb-code006-20261115/gut-pair-466-run-domain-001/start.json
    sha256: 511adddd55f6a9091a6342897e67359b5cc737e9bdc88d748f138b9c5396b33d
    role: context
  - path: .temp/gtdb-code006-20261115/gut-pair-466-run-gtdb-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/gut-pair-466-run-gtdb-001/native.log
    sha256: abbf9d05a704a7a6e6b9dc8e27a525b91abd42f07fdc2043286d2d44970d6399
    role: context
  - path: .temp/gtdb-code006-20261115/gut-pair-466-run-gtdb-001/receipt.json
    sha256: d52bc173cde2d1dbfdbca54535f4dae4ae1c76ea512b91db2ee980b8591e2034
    role: context
  - path: .temp/gtdb-code006-20261115/gut-pair-466-run-gtdb-001/start.json
    sha256: c42d01dc2c834dba4276ab3c2e8f5738f580a7859c927a2778339e871abef875
    role: context
  - path: .temp/gtdb-code006-20261115/gut-pair-466-run-history-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/gut-pair-466-run-history-001/native.log
    sha256: 700b44227c4cf01270ac26f16b308622de0b26f48d71aec49cdfaaab87620f0a
    role: context
  - path: .temp/gtdb-code006-20261115/gut-pair-466-run-history-001/receipt.json
    sha256: 7b2827e6a1263e173f94be70eed22c78bd302573fdef22aa87a71995fa52522a
    role: context
  - path: .temp/gtdb-code006-20261115/gut-pair-466-run-history-001/start.json
    sha256: 29c2089c355bfb7ec69982c76141b9c59b558e8c32314ab77dfeb0f87c4305c9
    role: context
  - path: .temp/gtdb-code006-20261115/gut-pair-466-run-new-history-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/gut-pair-466-run-new-history-001/native.log
    sha256: d92732e6621ca191b94b37e4d38e8b92a84520c39868813f76ab5cc48824ea7f
    role: context
  - path: .temp/gtdb-code006-20261115/gut-pair-466-run-new-history-001/receipt.json
    sha256: 3227753e2aa852fd81892ce4d49499817f365d44d8c5173dfde55a010dec0bfa
    role: context
  - path: .temp/gtdb-code006-20261115/gut-pair-466-run-new-history-001/start.json
    sha256: 913493439bdecd85bdc821a94de69dc5d18ec01c2ec9aca41cdf10e05b322fca
    role: context
  - path: .temp/gtdb-code006-20261115/gut-pair-466-run-scalars-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/gut-pair-466-run-scalars-001/native.log
    sha256: 37c7f4fdce9fb06a33abe1c4e507a3e3f9d70198e2cf711b60c2d57490799616
    role: context
  - path: .temp/gtdb-code006-20261115/gut-pair-466-run-scalars-001/receipt.json
    sha256: add8a3c70d2b29a625d07c8f1dba958d96e26e71a76dbcc947d7f8049975f4bd
    role: context
  - path: .temp/gtdb-code006-20261115/gut-pair-466-run-scalars-001/start.json
    sha256: 38f0c60edc8e2bd0cd8cc400dae55b578994c14486b0e633b0000126c6946d1a
    role: context
  - path: .temp/gtdb-code006-20261115/gut-pair-466-run-schema-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/gut-pair-466-run-schema-001/native.log
    sha256: 74d7344f57b4cb979054775d38ee6e4939357c851ed832e68a42fe5b466b2af2
    role: context
  - path: .temp/gtdb-code006-20261115/gut-pair-466-run-schema-001/receipt.json
    sha256: 634ba8ab450720a49e92c05ddc7dcecd8e22dc5b5ba9b2bb28fabe6d24e5a9d5
    role: context
  - path: .temp/gtdb-code006-20261115/gut-pair-466-run-schema-001/start.json
    sha256: 4c5fe4638c8d1763e92a101cc41cf3c65c21bcb4414eb171c6271a45912e9c08
    role: context
  - path: .temp/gtdb-code006-20261115/gut-pair-466-run-strict-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/gut-pair-466-run-strict-001/native.log
    sha256: 1d43df83b8989d80614072f65023ab484351f298c47aa425dac141c69a1d99ee
    role: context
  - path: .temp/gtdb-code006-20261115/gut-pair-466-run-strict-001/receipt.json
    sha256: 1ae9d1807f1e60e05fa6441754e8ce0d76f193ecc2205e0d751f2f74718dcf0a
    role: context
  - path: .temp/gtdb-code006-20261115/gut-pair-466-run-strict-001/start.json
    sha256: c1197c980041c1551e46decb386f8d30c09cd1b8d485e704f52e46acd414e1b3
    role: context
  - path: .temp/gtdb-code006-20261115/gut-pair-466-run-strict-001/strict.tsv
    sha256: b184ed5450b968070bb6c75648407e388f41a1eaf7017890723cf560999fc3f7
    role: context
  - path: .temp/gtdb-code006-20261115/gut-pair-466-run-terms-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-code006-20261115/gut-pair-466-run-terms-001/native.log
    sha256: 087370ab478b532e4ca5728d7f7ceaac4bdd5d2526134cf8fc356fad1029d3b7
    role: context
  - path: .temp/gtdb-code006-20261115/gut-pair-466-run-terms-001/receipt.json
    sha256: 15ae1fec717a2a86e396a77c1f76c5d6003eb2b1cc4bfdb9930f0115e83ef995
    role: context
  - path: .temp/gtdb-code006-20261115/gut-pair-466-run-terms-001/start.json
    sha256: 07d47b6881a1a350292782ca7ae75492cc949dfba5cd3d0baaad524d4896ca68
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
  - path: history/records/FOS_Lactobacillus_MinimalCore_GutLiver_SynCom/2026-09-28T180219Z-claude-code-8ee97f.yaml
    sha256: 9b84171659c474e204e2e72ba52ffa068fcfb9a389fdeccf71d2eeab6a4d377a
    role: context
  - path: history/records/FOS_Lactobacillus_MinimalCore_GutLiver_SynCom/2026-09-28T180634Z-claude-code-0cd199.yaml
    sha256: 2d33d8f5ebfd308201210add9453cbe402bcefed00437b1963d27a105dec01ad
    role: context
  - path: history/records/FOS_Lactobacillus_MinimalCore_GutLiver_SynCom/2026-10-06T094747Z-codex-bb2e7e.yaml
    sha256: 304fa4a9bc9024e58e2e2bc781f804e8734fbff013948ab4409f29e505cb066d
    role: context
  - path: history/records/FOS_Lactobacillus_MinimalCore_GutLiver_SynCom/2026-11-15T121633Z-codex-31f437.yaml
    sha256: 025a1613e03df87ef0ebd1a52f8708c59348748bc7179ce73e5aba88eb9d8511
    role: context
  - path: justfile
    sha256: 40369611ad4531582e420df0e9ff22109e4b18adf03b34d86b54200b280f2d0f
    role: context
  - path: kb/communities/FOS_Lactobacillus_MinimalCore_GutLiver_SynCom.yaml
    sha256: e3be57fc8ea10f165adb310f066907c763f13798ffc76a13e948a1b217e605ff
    role: target
  - path: pyproject.toml
    sha256: be952f0f137f85fed66bda0908f12014f1797a2dd229b44d832afc0c00471655
    role: context
  - path: references_cache/PMID_42781020.txt
    sha256: 1d7403bbc62cf62cbd5793103be8e00982e4f8e13a53897a334d7ddd8c90201b
    role: context
  - path: reports/causal_graph_review/decisions/20261006-three-records-batch39.yaml
    sha256: a1dee2681584def997c377ad6ae941a5595a60c864f2efbd465d907812d1ffe2
    role: context
  - path: reports/gtdb-code006-20261115/gut-pair-466-review-config-001.json
    sha256: 20f56854d8ca8d43d42d7fb8f18a4fd0f7f1be5d14a0a19a61edb61e460f4d9e
    role: context
  - path: reports/gtdb-code006-20261115/gut-pair-466-source-evidence-001.json
    sha256: 8b287fa16e39b6d8b984bdd2b76aa23d52492a1e7429332d697d50936eafe080
    role: context
  - path: reports/gtdb-code006-20261115/gut-pair-authored-source-context-001.json
    sha256: 4d8cfb57fd549fc049469951abad91bc316b63fd7a21925f572c2e38da1c3c17
    role: context
  - path: reports/gtdb-code006-20261115/gut-pair-source-config-001.json
    sha256: dcae8a3a905aa15ce721e1867a9cda68981fda663b58db1b96f00b3c6c68dec0
    role: context
  - path: reports/phase2-completion-20261115/fos466-source-context-001.yaml
    sha256: 5a35923e6e4b1b168758d8252167958c8e925e655fbb86e676f0774ee302156d
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
  - path: tests/test_causal_review_batch39.py
    sha256: b76b69039c1ae43beb42e957cc0cd508042adfa3d9d2786617eabeccc5c18a81
    role: context
  - path: uv.lock
    sha256: 712838f8fa3d68fbd818ac8162f3f1e2f2637db1da1a8ebfaba0ef759690f3b4
    role: context
targets:
- target_id: CommunityMech:000466
  path: kb/communities/FOS_Lactobacillus_MinimalCore_GutLiver_SynCom.yaml
  selector: taxonomy[3,5].taxon_term.gtdb_classification; taxonomy[2,3,5].taxon_term.gtdb_grounding_status;
    taxonomy[2].taxon_term.gtdb_candidates
  label: Two species-reference mappings and four preserved reuteri alternatives
  kind: maintained
  ownership_note: CommunityMech owns this record; only declared GTDB correspondence/status
    and actual provenance are assessed.
scope:
  description: 'CommunityMech:000466 taxonomy indices 2, 3 and 5: two reference blocks,
    one complete ambiguity set, three changed statuses and two native inline events,
    with guarded application, appended native sidecar and eight scoped native checks.
    All four unselected descriptors and all biological content are preserved.'
  selection: The second whole record in the separately prepared 382/466 pair, after
    the complete Amsterdam canary and its saved-input checkpoint, public proof and
    actual strict controls were verified and published. This diagnostic reviews exactly
    one record. It does not repeat or supersede the Amsterdam assessment.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000466
  exclusions:
  - target: Other scientific claims and records
    reason: Existing biology is preserved, not newly certified by this database diagnostic.
checks:
- check_id: 000466-schema
  name: validate
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000466
  command: just --verbose --no-dotenv --color never validate kb/communities/FOS_Lactobacillus_MinimalCore_GutLiver_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000466-schema
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000466-strict
  name: validate-strict
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000466
  command: just --verbose --no-dotenv --color never validate-strict kb/communities/FOS_Lactobacillus_MinimalCore_GutLiver_SynCom.yaml
    --out .temp/gtdb-code006-20261115/gut-pair-466-run-strict-001/strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000466-strict
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000466-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000466
  command: just --verbose --no-dotenv --color never validate-gtdb kb/communities/FOS_Lactobacillus_MinimalCore_GutLiver_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000466-gtdb
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000466-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000466
  command: just --verbose --no-dotenv --color never validate-gtdb-domain kb/communities/FOS_Lactobacillus_MinimalCore_GutLiver_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000466-domain
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000466-scalars
  name: validate-scalars
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000466
  command: just --verbose --no-dotenv --color never validate-scalars kb/communities/FOS_Lactobacillus_MinimalCore_GutLiver_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000466-scalars
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000466-history
  name: validate-history
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000466
  command: just --verbose --no-dotenv --color never validate-history history/records/FOS_Lactobacillus_MinimalCore_GutLiver_SynCom
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000466-history
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000466-new-history
  name: new-history
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000466
  command: 'just --verbose --no-dotenv --color never new-history --kind record --slug
    FOS_Lactobacillus_MinimalCore_GutLiver_SynCom --target-root kb/communities --event
    EDIT --outcome changed --sections taxonomy,curation_history --actor-name codex
    --model gpt-6 --agent-tool codex --issue https://github.com/CultureBotAI/CommunityMech/issues/2848
    --summary ''Record two reference correspondences and complete reuteri alternatives''
    --details ''The independently reviewed actual M5 candidate changes three existing
    descriptors: Bacteroides cellulosilyticus CL02T12C19 HM-726 gains the native species-name
    reference correspondence with 1018 reference genomes and fraction 1.0; Flavonifractor
    plautii 1_3_50AFAA HM-303 gains the exact-ID reference correspondence with 142
    genomes and fraction 0.98; Limosilactobacillus reuteri PBS072 DSM 25175 retains
    all four ordered native alternatives without a selected block. These reference
    populations do not identify the study-stock genomes. Preserve the four existing
    plantarum, acidophilus, symbiosum and Escherichia coli blocks byte-for-byte, including
    the two explicitly curated R232 acidophilus and symbiosum mappings. Preserve all
    seven stock labels, source quotations, original notes, old history, three nodes
    with participant counts 7/3/7 and zero arrows. DNA qPCR is not viability or RNA
    measurement; 2% FOS versus 1% glucose is not carbon matched; qualitative GC-MS
    is not metabolite flux; unknown host-active compounds and Cd36 limits remain.
    Source reporting and binding ran locally at 9bf78f54; staging and application
    ran at frozen M5 e4dc49af with captured source bytes. Two native inline events
    record two added blocks and three changed statuses; seven processed taxa are not
    seven changed taxa. This is a partial technical correspondence correction, not
    a new full scientific review, mechanistic clearance or issue closure. The crosswalk
    file mtime does not establish its release. Actual apply receipt .temp/gtdb-code006-20261115/gut-pair-466-applied-001/receipt.json
    sha256:12ded3e3e38941bf3aeab5a5e6b3fef4aca4dedaf3a0e295548990adefbfaca8.'''
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000466-new-history
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
- check_id: 000466-terms
  name: validate-terms
  status: passed
  required: true
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
  target_ids:
  - CommunityMech:000466
  command: just --verbose --no-dotenv --color never validate-terms kb/communities/FOS_Lactobacillus_MinimalCore_GutLiver_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000466-terms
  scope_note: Scoped technical record gate, not whole-record scientific approval or
    corpus QC.
evidence:
- evidence_id: 000466-schema
  kind: validation
  reference: .temp/gtdb-code006-20261115/gut-pair-466-run-schema-001/native.log
  accessed_at: '2026-11-15T12:18:23.904988Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000466-strict
  kind: validation
  reference: .temp/gtdb-code006-20261115/gut-pair-466-run-strict-001/native.log
  accessed_at: '2026-11-15T12:18:23.904988Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000466-gtdb
  kind: validation
  reference: .temp/gtdb-code006-20261115/gut-pair-466-run-gtdb-001/native.log
  accessed_at: '2026-11-15T12:18:23.904988Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000466-domain
  kind: validation
  reference: .temp/gtdb-code006-20261115/gut-pair-466-run-domain-001/native.log
  accessed_at: '2026-11-15T12:18:23.904988Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000466-scalars
  kind: validation
  reference: .temp/gtdb-code006-20261115/gut-pair-466-run-scalars-001/native.log
  accessed_at: '2026-11-15T12:18:23.904988Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000466-history
  kind: validation
  reference: .temp/gtdb-code006-20261115/gut-pair-466-run-history-001/native.log
  accessed_at: '2026-11-15T12:18:23.904988Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000466-new-history
  kind: validation
  reference: .temp/gtdb-code006-20261115/gut-pair-466-run-new-history-001/native.log
  accessed_at: '2026-11-15T12:18:23.904988Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000466-terms
  kind: validation
  reference: .temp/gtdb-code006-20261115/gut-pair-466-run-terms-001/native.log
  accessed_at: '2026-11-15T12:18:23.904988Z'
  support: supports
  summary: Actual native command passed for this accepted record with retained nonempty
    output and unchanged captured inputs.
- evidence_id: 000466-paper
  kind: primary_source
  reference: https://doi.org/10.3389/fmicb.2026.1866842
  locator: Retained Methods 2.1 and Table 1 stock roster and DNA-qPCR calibration,
    flattened line 77; active-compound limitation on line 78; exact primary_locators
    retained in captured source metadata
  support: supports
  summary: The inspected source names the three selected stocks within distinct probiotic,
    minimal-core and whole-community contexts. It reports genomic-DNA calibration
    for enumeration. It does not independently place a study-stock genome into a GTDB
    cluster or establish a causal host-active mediator.
  accessed_at: '2026-11-15T12:18:23.904988Z'
- evidence_id: 000466-database
  kind: database
  reference: reports/gtdb-code006-20261115/gut-pair-466-source-evidence-001.json
  locator: 'Selected indices 2,3,5: full native_result, classify_status, lookup_indexes,
    crosswalk_rows and ncbi_identity_rows; explicit unselected curated-block boundary'
  support: supports
  summary: Pinned native results support the name-route cellulosilyticus population,
    exact-ID plautii population and complete four-way reuteri ambiguity. These reference
    correspondences do not identify stock assemblies; the four pre-existing blocks,
    including two manual R232 pins, remain unchanged.
  accessed_at: '2026-11-15T12:18:23.904988Z'
- evidence_id: 000466-application
  kind: record_content
  reference: .temp/gtdb-code006-20261115/gut-pair-466-applied-001/receipt.json
  locator: Actual before/after, external reviewed candidate/receipt pins, all captured
    inputs, two-block/three-status native inline events and appended sidecar
  support: supports
  summary: The exact peer-reviewed candidate was persisted on isolated M5. Only three
    selected GTDB field groups and two native events change; the seven stocks, four
    earlier mappings, all scientific assertions and prior history remain unchanged.
  accessed_at: '2026-11-15T12:18:23.904988Z'
- evidence_id: 000466-prior
  kind: prior_review
  reference: reports/causal_graph_review/decisions/20261006-three-records-batch39.yaml
  locator: FOS needs_research disposition, historical source/figure scope and follow-ups;
    all eight tests/test_causal_review_batch39.py predicates are captured unchanged
  support: context_only
  summary: The earlier ledger preserves assay distinctions and a pending host-response
    expansion. Its historical scientific observations and cache pins remain unchanged.
    This technical diagnostic does not resolve the existing biological findings or
    reclassify the record as scientifically complete.
  accessed_at: '2026-11-15T12:18:23.904988Z'
assessments:
- assessment_id: 000466-source-scope
  area: grounding
  topic: Existing species descriptors retain their distinct source stocks and assay
    contexts
  outcome: supported
  target_ids:
  - CommunityMech:000466
  evidence_ids:
  - 000466-paper
  - 000466-database
  - 000466-terms
  summary: PBS072, CL02T12C19 and 1_3_50AFAA retain their source identities and authority
    species ranks without stock-genome inference. The three probiotic stocks, four
    minimal-core stocks and seven-stock whole community remain distinct; DNA enumeration,
    expression and metabolite profiling are not conflated.
- assessment_id: 000466-native-correspondence
  area: grounding
  topic: Two native reference populations and the complete reuteri ambiguity
  outcome: supported
  target_ids:
  - CommunityMech:000466
  evidence_ids:
  - 000466-database
  - 000466-gtdb
  - 000466-domain
  summary: The actual change reproduces cellulosilyticus 1018/1.0 by species name
    and plautii 142/0.98 by exact species ID, plus all four ordered reuteri alternatives.
    The rounded fraction 0.98 is not unanimity. All four old blocks, especially the
    two curated R232 mappings, remain exact; no new stock assembly or single ambiguous
    choice is inferred.
- assessment_id: 000466-persistence
  area: provenance
  topic: Bounded persisted application preserves scientific and historical constraints
  outcome: supported
  target_ids:
  - CommunityMech:000466
  evidence_ids:
  - 000466-application
  - 000466-prior
  - 000466-schema
  - 000466-strict
  - 000466-scalars
  - 000466-new-history
  - 000466-history
  summary: The accepted candidate, actual receipt and sidecar bind three changed descriptors
    and two native inline events. All eight scoped commands passed on the actual record,
    including one-file strict validation with zero errors. Three nodes, zero arrows,
    both discussions and prior needs_research scope remain unchanged. Strict saved-successor
    and historical caller controls are subsequent acceptance steps, not assumed results.
findings: []
actions: []
limitations:
- Partial technical database-correspondence diagnostic with scientific_review:false.
  These scoped checks are not whole-record scientific approval, reference-snippet
  coverage, generated-page validation, final corpus QC or campaign completion.
- Bacteroides cellulosilyticus uses the species-name route with 1018 reference genomes
  and fraction 1.0. Flavonifractor plautii uses the exact species-ID route with 142
  genomes and rounded fraction 0.98, which is not unanimity or an exactly recoverable
  numerator. These are reference populations, not inoculum composition, experimental
  abundance, stock genomes or identity probabilities.
- 'Limosilactobacillus reuteri PBS072 retains all four ordered native alternatives:
  reuteri, reuteri_E, reuteri_G and rodentium. No single correspondence block or study-stock
  genome is selected from this ambiguity.'
- The four original plantarum, acidophilus, symbiosum and Escherichia coli blocks
  remain unchanged. In particular, the curated R232 acidophilus mapping at 158/0.994
  and symbiosum mapping at 112/0.964 are not overwritten by the differing fresh uncurated
  populations. This correction does not newly certify their release or source statements.
- Methods 2.1 and Table 1 identify PBS072/DSM 25175, CL02T12C19/HM-726 and 1_3_50AFAA/HM-303.
  Stock identifiers, former names and the BEI/HM notes remain literal source context;
  no independent stock sequence or assembly placement was performed. The three probiotic
  stocks, four-stock minimal core and seven-stock whole community remain distinct.
- DNA-qPCR genomic-DNA calibration is not a viable-cell count or an RNA-expression
  assay. RNA/cDNA expression and strain enumeration remain separate. The 2% FOS versus
  1% glucose comparison is not carbon-mass matched; qualitative GC-MS profiles are
  not quantified yields, ionic speciation or partner-resolved metabolic flux.
- The three COMMUNITY_LEVEL nodes retain seven, three and seven participants and zero
  directed edges. Historical Figure 7C panel-label observations do not establish physiological
  absence, and the active host compound, Cd36 mediation and requested HepG2 expansion
  remain unresolved. No cross-feeding arrow, uniform degrader role or clinical efficacy
  claim is introduced.
- The prior batch 39 needs_research disposition, two open discussions and historical
  follow-ups 1449/1450 remain unchanged. No current issue-state change or provider
  job is claimed. The earlier full caption/figure observations are historical evidence,
  not a new pixel inspection in this technical pass.
- Examination covered the complete current record, original batch 39 ledger/caller,
  selected retained primary stock and assay passages and the captured native mapping/authority
  results. No fresh full scientific review, separate supplementary audit, figure-pixel
  inspection, stock sequence or study-assembly analysis was performed.
- Source reporting and binding ran locally at 9bf78f54f83f88f954a309f351d862b4e0495c7a
  with preparation files disclosed. Actual FOS staging, application and gates ran
  at frozen M5 e4dc49afd89482371a84ea71829eee6e27d94a1d using native Python 3.13.2
  and frozen offline dependencies. The earlier Amsterdam correction and saved evidence
  were present; this is not a new clean-tree claim. Seven processed taxa are distinct
  from three changed statuses and two added blocks.
- Crosswalk SHA-256 is 761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd;
  file mtime does not establish its upstream release. Local authority observations
  retain their actual stat-based provenance without an invented full-database hash.
  Native terms reports Validation passed without an assertion denominator. Strict
  saved-successor and historical caller controls remain separate follow-up work.
links:
- https://github.com/CultureBotAI/CommunityMech/issues/2848
- https://github.com/CultureBotAI/CommunityMech/issues/1449
- https://github.com/CultureBotAI/CommunityMech/issues/1450
- https://github.com/CultureBotAI/CommunityMech/pull/2853
```
