# JN4/GD17 successor: preserve S1 correction with complete local input pins

- Review: 20261106T140446Z-jn4-gd17-complete-input-provenance
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-11-06T14:01:20Z
- Finished UTC: 2026-11-06T14:04:46.017116Z
- Reviewer: codex (self_review)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Append-only qualification for issue #2544: S1 cannot independently certify primer-specific membership because its G/J/C lane-band assignments and caption conflict. Preserve author-reported JN4/GD17 identity, all three open record-curation findings and their full acceptance checks. The 2016 full-source limit remains unresolved; no canonical records or previous reviews are changed. This linked successor also corrects issue #2566 by pinning the actual local source/check/helper inputs omitted from the first correction's input set.

## Scope And Provenance

Current unchanged 000180 target and all three predecessor findings/actions; fresh 2019 body/figures/SI and available 2016 abstract; bounded correction of the predecessor's S1 inference.

Selection: Only CommunityMech:000180 in PR #2054.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base c7d1aa4de06112c5aa139870228ce46269f403ef.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000180 | kb/communities/Clostridium_Thermoanaerobacterium_JN4_GD17_Cellulosic_Biofuel_Coculture.yaml | maintained | Clostridium-Thermoanaerobacterium JN4-GD17 Cellulosic Biofuel Coculture |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused validate | passed | True | CommunityMech:000180 | Exit 0 on the unchanged current target; exact receipt retained. |
| Focused strict | passed | True | CommunityMech:000180 | Exit 0 on the unchanged current target; exact receipt retained. |
| Focused terms | passed | True | CommunityMech:000180 | Exit 0 on the unchanged current target; exact receipt retained. |
| Focused references | passed | True | CommunityMech:000180 | Exit 0 on the unchanged current target; exact receipt retained. |
| Focused gtdb | passed | True | CommunityMech:000180 | Exit 0 on the unchanged current target; exact receipt retained. |
| Focused gtdb-domain | passed | True | CommunityMech:000180 | Exit 0 on the unchanged current target; exact receipt retained. |
| Focused history | passed | True | CommunityMech:000180 | Exit 0 on the unchanged current target; exact receipt retained. |
| Full repository lint before helper freeze | passed | True | CommunityMech:000180 | Black, Ruff and mypy passed before the helper was committed and pinned. |
| Full lint before second helper freeze | passed | True | CommunityMech:000180 | Full Black, Ruff and mypy passed before the new helper was frozen. |

## Scientific And Domain Assessments

### Bound the predecessor S1 inference

evidence: concern. Targets: CommunityMech:000180.

Withdraw independent primer-specific membership proof from S1.

Issue #2544 concerns this review-metadata sentence only. Attribute the pair and the authors' PCR-confirmation statement to Methods. Explicitly preserve the G/J/C band-label conflict and separate caption typo. Do not relabel lanes, infer another member, assert failed reconstruction or redesign primers. The independent predecessor audit identified this defect; this document is the author remediation and requires a separate read-only re-review.

### Exact reconstructed pair

identity: supported. Targets: CommunityMech:000180.

The source-reported JN4/GD17 identity remains appropriate.

Historical names, current NCBI species labels and author-reported strain accessions remain distinct. The ambiguous S1 controls do not independently certify specificity or justify changing canonical membership.

### CTFUD and assay-specific cultivation

scope: concern. Targets: CommunityMech:000180.

The original cultivation finding and all its acceptance checks remain open.

The full source contradicts the record's no-working-volume/abstract-only limitations. Preserve exact source forms, separate culture arms and omit invented static-operation rationale; no canonical change occurs here.

### Proposed hemicellulose benefit

evidence: concern. Targets: CommunityMech:000180.

The original xylose hypothesis-qualification finding remains open.

Weak corncob growth and a tentative model do not establish GD17 xylose release or JN4 uptake. The different NOI-1 background reference stays scoped.

### Valid mappings and unsupported provenance shorthand

grounding: concern. Targets: CommunityMech:000180.

The original GTDB snapshot finding remains open; core mappings reproduce.

Retain exact IDs, lineages, 1.0 fractions and 18-genome counts for both species. A local file date does not establish a release called latest.

### Measured outcomes versus inferred mechanisms

graph: supported. Targets: CommunityMech:000180.

Three nodes and two qualified arrows remain appropriately bounded.

Community products, independent sugar conversion, estimated JN4 biomass, DNA proportions and transcription are distinct. Preserve confounding from added carbon and different sampling times; no direct flux, viable-cell count, reciprocal harm, obligatory dependence or required abundance is inferred.

### Current access and historical limits

scope: unknown. Targets: CommunityMech:000180.

Partial scientific scope remains necessary because the 2016 full assay is unavailable.

Fresh 2019 body, seven main figures, three SI figures and complete primer table were read. The first SI transfer timed out and the second completed. The predecessor's dates and source limits remain historical; no unavailable /private/tmp artifact is an active input or claimed newly read source.

### Native focused gates and current guidance

schema: supported. Targets: CommunityMech:000180.

Current record validators pass independently of the scientific limitations.

The existing source caches have accurate content-type headers and remain unchanged. Existing append-only graph history and the open flux/growth knowledge-gap discussion remain bounded. No new cache/history repair or request to perform experiments is introduced.

### Native rubric arithmetic

completeness: supported. Targets: CommunityMech:000180.

Completeness 85; raw quality 121, capped 100.

Rechecked against the unchanged current record and three retained curation findings. Presence scores do not certify scientific completion or make optional state mandatory.

### Complete input attestation for the current 000180 successor

provenance: supported. Targets: CommunityMech:000180.

Correct the incomplete input set of the 135321 predecessor (#2566).

The earlier 19 hashes matched their files but omitted other actual local sources and check receipts. Those omissions are explicitly acknowledged. This review retains the accepted S1 lane/caption qualification, partial scientific status, all three open scientific findings and all four actions unchanged. Native inspection output cannot hash itself; the new candidate and subsequent post-save validation receipts are generated outputs, not prior judgment inputs. This correction does not reassess the other nine original batch records.

## Findings

### recover-cultivation-scope: Recover CTFUD and assay-specific cultivation scope

major / open / confirmed; issue key: cm-000180-recover-cultivation-scope.

The record falsely says no working volume is reported, omits available CTFUD formulation, merges substrate assay contexts and adds an unsupported explanation for static operation. The abstract-only preparation note is stale.

### qualify-xylose-model: Qualify the proposed GD17 xylose benefit

minor / open / confirmed; issue key: cm-000180-qualify-xylose-model.

The xylose entry converts a tentative hemicellulose-to-xylose benefit into categorical GD17 digestion. The paper reports weak corncob growth and a possible reciprocal benefit; its background citation concerns NOI-1 rather than GD17.

### document-gtdb-snapshot: Document the verified GTDB snapshot

minor / open / confirmed; issue key: cm-000180-document-gtdb-snapshot.

Both exact species mappings reproduce, but latest-release/build wording is not established by the snapshot modification time.

## Recommended Actions And Acceptance Checks

### recover-protocols

Recover available experiment-specific cultivation information.

- Replace stale abstract-only and no-working-volume prose with source-local Methods. Enter the CTFUD formulation at the reported amounts, preserving hydrate/salt forms and resazurin 0.5 mL/L with stock strength unspecified. Do not invent culture pH, gas ratio, vessel capacity or missing vitamins.
- Represent cellulose/Avicel, cellobiose, glucose and ground-corncob assay arms explicitly. The default listed cellobiose recipe does not mean cellobiose was co-added to every alternative substrate. Carbon source is 0.5%; Avicel plus dextrin/sucrose treatments contain 0.5% of each.
- Scope 80 mL to cellulose-grown JN4 monoculture/coculture and 50 mL to glucose/cellobiose member-monoculture conversion tests. Adjust growth_media[0].name and evidence[0].explanation so independent sugar tests are not described as demonstrated sugar coculture arms.
- Retain anaerobic tubes/serum bottles, 60 °C, no agitation and BATCH. Remove the invented cellulosome/settled-substrate rationale and unrelated neighboring-record/issue discussion from cultivation notes.
- Keep 10% v/v seed separate from the reconstruction 1:1 cell ratio and at least five passages. Match seed substrates to the stated assays; neither value establishes an endpoint species fraction.
- Do not import 200 rpm milling, centrifugation, 105 °C drying, citrate pH 4.8, 45 °C enzymatic hydrolysis or six-day analytical incubation into culture fields. Preserve the existing biomass, sampling-time and added-carbon interpretation limits.

### qualify-xylose

Restore hypothesis wording to the two xylose prose fields.

- Change related_ingredients[3].relevance and evidence[0].explanation to state the authors proposed hemicellulose-to-xylose benefit. Preserve the exact may-benefit snippet if retained.
- Cite weak GD17 corncob growth and tentative Figure 6B; distinguish the background NOI-1 paper from GD17. No measured xylose release, transfer or JN4 benefit is asserted, and the route is not declared impossible.

### document-mapping

Make both valid species mappings reproducible.

- Use crosswalk SHA 761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd and exact ncbi_id lookup route. Describe 2026-07-25 as local mtime, not a verified latest release/build.
- Retain NCBITaxon:1515→Hungateiclostridium thermocellum and NCBITaxon:1517→Thermoanaerobacterium thermosaccharolyticum, each 1.0/18 genomes, current lineages and name-comparison flags. Keep JN4/GD17 and source-reported CGMCC accessions separate; no unverified strain CURIE or catalogue equivalence.

### validate-future-curation

Validate bounded repairs and resolve remaining source access separately.

- Preserve both members, all four roles and three untyped nodes/two qualified arrows. No reciprocal-harm, obligatory dependence, direct flux, viable count or mandatory abundance percentage is introduced.
- Recover the exact 2016 full paper before certifying complete hydrogen-assay review. Keep its DOI/PMID distinct from the 2008 publication and preserve the 2019 bibliography discrepancy without silently rewriting evidence.
- After separately authorized curation, append history and run schema, strict, term, reference, GTDB/domain, history and the actual generated-page recipes just gen-html and just check-docs-current. This review mutates no canonical record, cache, history, generated product or issue.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | PMID:31551972; doi:10.3389/fmicb.2019.02035; Strains and Chemicals; Enhanced End-Product Formation | supports | Methods identifies JN4 (CGMCC 1.5210) and GD17 (CGMCC 1.5209). The authors report reconstruction with both strains and present PCR as confirmation. This is author-reported identity, not independent certification of the S1 controls. |
| recipe | PMID:31551972; doi:10.3389/fmicb.2019.02035; Bacterial Growth | supports | The complete CTFUD formulation and substrate alternatives are available. Keep salt forms, unspecified resazurin stock strength, seed context, and 0.5% substrate arms separate; do not infer missing gas ratios or culture pH. |
| growth | PMID:31551972; doi:10.3389/fmicb.2019.02035; Bacterial Growth; Enhanced End-Product Formation | supports | Anaerobic tubes/serum bottles at 60 C without agitation, 10% seed addition, and a separately stated 1:1 reconstruction ratio are reported. At least five passages is a reconstruction statement, not an endpoint abundance. |
| volumes | PMID:31551972; doi:10.3389/fmicb.2019.02035; Analytical Methods | supports | Cellulose-grown JN4 monoculture and coculture use 80 mL; independent glucose/cellobiose member-monoculture assays use 50 mL. These are not demonstrated sugar-coculture arms or interchangeable vessel capacities. |
| analytical | PMID:31551972; doi:10.3389/fmicb.2019.02035; Analytical Methods; Biomass and Bacterial Ratio Determination; Real-Time PCR | supports | Products, protein-based biomass estimates, 16S DNA proportions and recA-normalized transcription are different measurements. Added-carbon and sampling-time differences prevent selective flux or viable-growth attribution. |
| xylose | PMID:31551972; doi:10.3389/fmicb.2019.02035; GD17 growth/biomass results; Figure 4C; tentative Figure 6B | supports | Weak GD17 corncob growth and a proposed hemicellulose-to-xylose benefit do not demonstrate xylose release, transfer or JN4 benefit. The route should remain an authors' hypothesis, not be declared impossible. |
| contexts | PMID:31551972; doi:10.3389/fmicb.2019.02035; Reference Chimtong et al. 2011; Reference Liu et al. 2008; Figures 1-7 | supports | The cited hemicellulose isolate is NOI-1, not GD17. The 2019 bibliography misattaches PMID 27538932 to the distinct 2008 DOI. Seven fresh main figures were inspected; their outcomes and conceptual model do not override these identity or inferential boundaries. |
| supplement | PMID:31551972; doi:10.3389/fmicb.2019.02035; Supplementary Figure S1, Image_1.TIF; Table S1; S2-S3 | context_only | Fresh S1 displays G/J/C lanes in every primer group; the JN-1/JN-2 bands appear in G and C while J is blank. The caption additionally names G as T. thermocellum and J as C. thermocellum JN4. The positive C lanes are compatible with the authors' report but cannot independently certify the stated strain specificity while these labels conflict. S2 compares expression and S3 compares stimulant growth. The full primer table retains duplicated licB rows. No sequence reanalysis was done. |
| strain | NCBI Taxonomy efetch: 1515 and 1517; Species names/ranks; source-local JN4/GD17 designations | supports | NCBI confirms species-level Acetivibrio thermocellus and Thermoanaerobacterium thermosaccharolyticum. Source collection accessions remain author-reported; no direct CGMCC catalogue certification or invented strain CURIE is asserted. |
| gtdb | KG-Microbe NCBI2GTDB.tsv.gz; scripts/gtdb_ground.py --community; Exact ncbi_id mappings for 1515 and 1517 | supports | Fresh community-mode replay preserves both 1.0/18 mappings. Crosswalk SHA256 is 761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd. July 25 is file metadata, not a verified latest release/build. The name-comparison flag does not establish biological reclassification. |
| schema | src/communitymech/schema/communitymech.yaml; AGENTS.md; FunctionalRoleEnum; cultivation and evidence definitions; optional state | supports | Current role, evidence and cultivation semantics support the retained actions. Ecological state remains optional. Host, soils and community relations do not create mandatory omissions for this liquid bacterial pair. |
| predecessor | reviews/structured/20261021T231001Z-jn4-gd17-record-review/review.yaml; evidence[evidence_id=supplement].summary; findings and all four actions | context_only | The predecessor positively described S1 as supporting primer-specific membership while mentioning only its caption-name discrepancy. This successor withdraws that independent proof inference, preserves the immutable old bytes, and retains all three open record findings. |
| focused-qc | .temp/pr2054/independent-third/focused-checks.json; CommunityMech:000180 entries; current unchanged target | supports | Seven focused record gates passed with real exit 0 before this agent switched from independent reader to correction author. The record and relevant validator bytes are unchanged; these receipts are reused explicitly, not claimed as independent approval of this successor. |
| access | PMID:27538932; doi:10.1007/s00253-016-7776-1; Fresh Europe PMC abstract and publisher subscription preview | context_only | The 2016 hydrogen paper remains abstract/preview only. Its reported comparative rate does not certify the full assay. The 2008 API returns bibliographic coredata, not a complete body. Current partial status is preserved despite complete fresh access to the 2019 SI. |
| metrics | kb/communities/Clostridium_Thermoanaerobacterium_JN4_GD17_Cellulosic_Biofuel_Coculture.yaml; Current native rubric presence and evidence counts | supports | Unchanged record has three nodes, two qualified arrows and six node evidence occurrences. The three retained findings are one P2 and two P3. Presence completeness is 85; quality raw 121, capped 100. Rubric required-field wording is a scoring rule, not LinkML requiredness. |
| complete-input-manifest | .temp/pr2054/180-input-provenance/input-paths.json; Exact files passed to native inspect; GTDB byte-copy receipt | supports | The complete bounded local input surface is now hashed in source.inputs. Fresh main/SI figures, XML/text, authority/source-access data, actual check logs, both helpers and immutable predecessors are included. Shared receipt entries outside 000180 remain context only. The copied GTDB bytes equal the source snapshot. |

## Limits And Additional Notes

- The 2016 hydrogen paper remains abstract/preview only; 2008 body is unavailable. Do not certify complete hydrogen-assay review or import their missing Methods.
- S1 contains unresolved lane/control-label ambiguity and a caption typo. No lane relabeling, contamination finding, failed reconstruction or new member follows.
- No raw sequencing, numerical, viable-cell or flux reanalysis was performed. Protein-based biomass and comparative metabolism do not establish selective causality.
- All prior bundles are immutable. Their old /private/tmp source paths are historical references only, not recoverable current inputs.
- This is an author remediation, not the independent re-review. Native save, bundle/contract and writer-gate receipts are reported separately after saving.
- The original 000180 evidence summary is explicitly qualified rather than silently rewritten.
- The open jn4_gd17_flux_and_growth_partition discussion remains an evidence-watch boundary. No action demands experiments.
- AGENTS.md is pinned directly; the CLAUDE.md symlink is not a current input.
- Includes prior native inspection, candidate and post-save receipts as historical inputs.
- The new inspection manifest defines the hashes and cannot hash itself.
- The new candidate and later save/check logs are outputs, not prior judgment inputs.
- Shared source/check receipts include other records; only 000180 is reassessed here.
- The external GTDB source is represented by a verified byte-identical scratch copy.
- Pinned scratch inputs attest to inspected bytes; they are not claimed to be committed source caches or durable raw-source publication. Current native input checks verified them before saving; later absence must not be described as source access.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261106T140446Z-jn4-gd17-complete-input-provenance
kind: record
repository: CultureBotAI/CommunityMech
title: 'JN4/GD17 successor: preserve S1 correction with complete local input pins'
started_at: '2026-11-06T14:01:20Z'
finished_at: '2026-11-06T14:04:46.017116Z'
reviewer:
  identity: codex
  kind: agent
  independence: self_review
  independence_basis: Author of both correction successors; a different agent identified
    the input-pin defect and will independently re-review. No independent self-approval
    is claimed.
skill: review-yaml-record
completion: partial
verdict: needs_curation
scientific_review: false
summary: 'Append-only qualification for issue #2544: S1 cannot independently certify
  primer-specific membership because its G/J/C lane-band assignments and caption conflict.
  Preserve author-reported JN4/GD17 identity, all three open record-curation findings
  and their full acceptance checks. The 2016 full-source limit remains unresolved;
  no canonical records or previous reviews are changed. This linked successor also
  corrects issue #2566 by pinning the actual local source/check/helper inputs omitted
  from the first correction''s input set.'
source:
  git_revision: c7d1aa4de06112c5aa139870228ce46269f403ef
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: d2f94c87b82f59663bc2b0c91ac04a245e56fab52d8c11e6bddb559eb9237c84
    role: context
  - path: .claude/skills/ground-taxa-gtdb/SKILL.md
    sha256: 0f7f4423eca28dd0605784d0a01b0886618d0d0f8f1739acb1aae7702e4560a1
    role: context
  - path: .claude/skills/review-communities/reference/metrics-and-reports.md
    sha256: 2647416ac98a8f9569e0afbd826a0d1229bb4262639934848639ce536b0974fc
    role: context
  - path: .claude/skills/review-communities/reference/validation-rules.md
    sha256: 3860e91a64f7c1f55f80e3d7a361d0798bbd00cbaf5cb7720a7533673e5afe2e
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: 1005e1b9eb7f83306a1f88a6d22ec7954a54c2bf2e2fc15923fdaaa1111a3d2b
    role: context
  - path: .temp/pr2054/180-correction/author-integrity.json
    sha256: 056b352b7a415c89c71770c33742f511c4d070d3f00fd98bb278a4c616a75faf
    role: context
  - path: .temp/pr2054/180-correction/build.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2054/180-correction/build.stdout
    sha256: f21c5ffde7bf7d113cd00bf5aecb7db756cc985bda6fe7fd1fff03de6ec1d0ec
    role: context
  - path: .temp/pr2054/180-correction/candidate.json
    sha256: 13998e9c958aed6afc80bf41b9683ccca0763182a2bdee7ff8ad4d3a02040d2a
    role: context
  - path: .temp/pr2054/180-correction/check-record-reviews.stderr
    sha256: e948da1cfe774485c5a8d36849ac71a894c7899192ba8c72909995dd668c8f75
    role: context
  - path: .temp/pr2054/180-correction/check-record-reviews.stdout
    sha256: b8fd45cb15e7359e2d65f839512743b62e1dd3e9552d37f4378b019339610685
    role: context
  - path: .temp/pr2054/180-correction/diff-check.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2054/180-correction/diff-check.stdout
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2054/180-correction/draft.json
    sha256: f587dfbf2a9e5ffa4ec64d499ea1847250fc6e95ab524aa0fbc8831f08294403
    role: context
  - path: .temp/pr2054/180-correction/full-lint.json
    sha256: cc25b642e2a0458dce7c55391bb9e77ea2c52d6a4bb0475aef4e188a5e59a930
    role: context
  - path: .temp/pr2054/180-correction/full-lint.stderr
    sha256: 5d1b2cf5a66581c046631618f824d762ed6e3160abaff0ae75213d57cf4dbaa0
    role: context
  - path: .temp/pr2054/180-correction/full-lint.stdout
    sha256: 1cffccf768da50ca84db43e973c69c47f795b57101ebfc1825d52472c790ab4d
    role: context
  - path: .temp/pr2054/180-correction/inspect.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2054/180-correction/inspect.stdout
    sha256: 11d56c5f397b3e94813cfc29a75eb10f1519e09d9f940f69cb3d7f74f69fba68
    role: context
  - path: .temp/pr2054/180-correction/native-author-receipts.json
    sha256: 53edf55da7a180c0914d11a5a7d78ee0d80b77442481fcd02c46fad9f0e7f104
    role: context
  - path: .temp/pr2054/180-correction/post-save-qc.json
    sha256: d3d90fb5ab4e59fa4321e35719751c7219a73357dc31a71302185bab53f51352
    role: context
  - path: .temp/pr2054/180-correction/save.stderr
    sha256: e2cf5a8ee56373cb7afeb23be8ac2a30d67f13afa55bb51424877fc908e2a25f
    role: context
  - path: .temp/pr2054/180-correction/save.stdout
    sha256: 768b264f6ebb4549d68d4b9d5ba27622568a8c36e5cbbbdf30b88c4f6a595c6b
    role: context
  - path: .temp/pr2054/180-correction/test-record-reviews.stderr
    sha256: 3c78da6b640c526eabf9a236bbdd4c569f4c4c3158dcf2972c817e175e9dc3b1
    role: context
  - path: .temp/pr2054/180-correction/test-record-reviews.stdout
    sha256: ae53e08edd105655463b0df8b9aa3bfda06afa076e6c9fea5106fa605ddc9624
    role: context
  - path: .temp/pr2054/180-correction/validate.stderr
    sha256: e2cf5a8ee56373cb7afeb23be8ac2a30d67f13afa55bb51424877fc908e2a25f
    role: context
  - path: .temp/pr2054/180-correction/validate.stdout
    sha256: b42ee0197bdb886694684431f9da0d2fba4020263ed572ff756b9eaf0b042ba6
    role: context
  - path: .temp/pr2054/180-correction/writers.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2054/180-correction/writers.stdout
    sha256: f28b28997a0b90e861a713418a6a180eda01619172d33708b9f0e14e4c63308d
    role: context
  - path: .temp/pr2054/180-input-provenance/NCBI2GTDB.tsv.gz
    sha256: 761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd
    role: context
  - path: .temp/pr2054/180-input-provenance/full-lint.json
    sha256: 3eba82d7ea980c74235b476355da9a3ab7e2daf4e490aaadad118863e55276c0
    role: context
  - path: .temp/pr2054/180-input-provenance/full-lint.stderr
    sha256: ad389b0e6ff41ee264a18a5995db7b897901af5e1d27e518214f796d95aa9537
    role: context
  - path: .temp/pr2054/180-input-provenance/full-lint.stdout
    sha256: 1cffccf768da50ca84db43e973c69c47f795b57101ebfc1825d52472c790ab4d
    role: context
  - path: .temp/pr2054/180-input-provenance/gtdb-copy.json
    sha256: 77ae47976a1f35fb0337b4ca3cba9dc2da9a0a0aef141e73d4b0a6f0bd31da67
    role: context
  - path: .temp/pr2054/180-input-provenance/input-paths.json
    sha256: 0ba87f9ba87cb292ac6f403504ee12c6ff52cdee5dc7cce6f8aa120dbb638553
    role: context
  - path: .temp/pr2054/independent-third/000180/focused-checks.json
    sha256: 76518380da2b7d8fa5bfb3dc479b54aab3b2025b47aab120afd504cf4423ae9a
    role: context
  - path: .temp/pr2054/independent-third/000180/gtdb-domain.stderr
    sha256: 1a6b869dfaabd8556fcb46c6a1cc08ef9b0d98d9fec8a3c85bebe573317d7b4a
    role: context
  - path: .temp/pr2054/independent-third/000180/gtdb-domain.stdout
    sha256: ede937293c42cad366f434dce49a485a9a0c56fe86620b52ca243ad10e09ecae
    role: context
  - path: .temp/pr2054/independent-third/000180/gtdb-ground.stderr
    sha256: d767f6f71f49b458bbc7a095014fe1f5d5c95357e23e96fca9a73bc56d0347ff
    role: context
  - path: .temp/pr2054/independent-third/000180/gtdb-ground.stdout
    sha256: 6457708b4a1d862b020e022dd503ad7d43062ba8e3a6c4699e867a2cb3e9560b
    role: context
  - path: .temp/pr2054/independent-third/000180/gtdb.stderr
    sha256: b54945119d9657c502b0500b9e6b964300491946153b69cf9306c6c4fb975777
    role: context
  - path: .temp/pr2054/independent-third/000180/gtdb.stdout
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2054/independent-third/000180/history.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2054/independent-third/000180/history.stdout
    sha256: de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
    role: context
  - path: .temp/pr2054/independent-third/000180/inspect.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2054/independent-third/000180/inspect.stdout
    sha256: aa512bf1da25af258ab605edd42831d015ae20a4dd7ac376a4e7b1ef5a91e4ef
    role: context
  - path: .temp/pr2054/independent-third/000180/references.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2054/independent-third/000180/references.stdout
    sha256: a922e9ab30810a981fa9e81ace6a2eb68a2cb986ff53bcfab830f7f8f20f96b9
    role: context
  - path: .temp/pr2054/independent-third/000180/review-validate.stderr
    sha256: e2cf5a8ee56373cb7afeb23be8ac2a30d67f13afa55bb51424877fc908e2a25f
    role: context
  - path: .temp/pr2054/independent-third/000180/review-validate.stdout
    sha256: b42ee0197bdb886694684431f9da0d2fba4020263ed572ff756b9eaf0b042ba6
    role: context
  - path: .temp/pr2054/independent-third/000180/strict.stderr
    sha256: 609d4d87475aeed78850a3031bebeb128503824af3ef8fff022a4d5c8b8bae3a
    role: context
  - path: .temp/pr2054/independent-third/000180/strict.stdout
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2054/independent-third/000180/strict.tsv
    sha256: b184ed5450b968070bb6c75648407e388f41a1eaf7017890723cf560999fc3f7
    role: context
  - path: .temp/pr2054/independent-third/000180/targets.json
    sha256: 1ebe51314e129843d64361a4732396f951680f000b5eaa27dae852c07b7ac325
    role: context
  - path: .temp/pr2054/independent-third/000180/terms.stderr
    sha256: 7003c928c52d763a92008c3aa6ee3e42cab780e8df7c4c4b1996be5785d453dc
    role: context
  - path: .temp/pr2054/independent-third/000180/terms.stdout
    sha256: 23acda1c1d3194d12bc947d897d07de83f4a076a9d93c135148885108530e018
    role: context
  - path: .temp/pr2054/independent-third/000180/validate.stderr
    sha256: bdea47670bb59855fe19d07f0fe407a762d75319eea2de100a2835fad84c8d90
    role: context
  - path: .temp/pr2054/independent-third/000180/validate.stdout
    sha256: de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
    role: context
  - path: .temp/pr2054/independent-third/180-si-membership-concern.json
    sha256: cd813f2a5d641d1fe195e7310e28a5f4ae9de922b23ef50325423ee9fd0d61c2
    role: context
  - path: .temp/pr2054/independent-third/PMC6746925-supplementary-second.zip
    sha256: e4c2065e5f0ce45861af933914da78186fd36a93052bb3125bee86a8ce45ef26
    role: context
  - path: .temp/pr2054/independent-third/PMC6746925-supplementary.zip
    sha256: 6c4932732afe0eef75c2eec8dd147958feb251bf211b72a0595290348a622665
    role: context
  - path: .temp/pr2054/independent-third/PMC6746925.html
    sha256: f242c4e2040cf4ca27b98cd00ceaf6926a7eeb683e9bfbe25d1b3683f5e9ae49
    role: context
  - path: .temp/pr2054/independent-third/PMC6746925.read.txt
    sha256: 5f36f053f9b56963d73a99a462f8ccd1fdf5ebb7b006cb6f48a7042888240aa0
    role: context
  - path: .temp/pr2054/independent-third/PMC6746925.xml
    sha256: 8c035478025c2fad39825a1f810184b58eb435cf92e628ac1af912ce37404e10
    role: context
  - path: .temp/pr2054/independent-third/asset-inventory.json
    sha256: a792b724e0f8526f61ace29deb2e804b22c6fd5e2d1740b1881bf89c7600369e
    role: context
  - path: .temp/pr2054/independent-third/assets/frontiers180-fmicb-10-02035-g001.webp
    sha256: 5e8b014e95dff31d91e4eb54ac09c8c15e4ec2436274aa2ef6419a43d7c9b2cf
    role: context
  - path: .temp/pr2054/independent-third/assets/frontiers180-fmicb-10-02035-g002.webp
    sha256: fbdb83a6e0cc1a0effe2f818f2971fc224f127a2def8fd20e7eb844d7ed189e3
    role: context
  - path: .temp/pr2054/independent-third/assets/frontiers180-fmicb-10-02035-g003.webp
    sha256: 00d5b06018f5d9bd15f01942c6a9da48ca0c9b7a93ed35a73efd076a6acdb6e5
    role: context
  - path: .temp/pr2054/independent-third/assets/frontiers180-fmicb-10-02035-g004.webp
    sha256: aab36886319cfdd0aa661ef8321cd361cbb1d8d93f899d872e39edcfd6dd031c
    role: context
  - path: .temp/pr2054/independent-third/assets/frontiers180-fmicb-10-02035-g005.webp
    sha256: bc292c5f7ebb8da423c8562d28235503c8c9f5c4a2958b18105aef2174cea430
    role: context
  - path: .temp/pr2054/independent-third/assets/frontiers180-fmicb-10-02035-g006.webp
    sha256: 76f74dedf2405c8a3c8456e878904e249653256640db87619d11aa83e0623bba
    role: context
  - path: .temp/pr2054/independent-third/assets/frontiers180-fmicb-10-02035-g007.webp
    sha256: ed06b180b6b400a351f3415b2a6325ddbb388be063c85cd6b790a0e2d4ba6097
    role: context
  - path: .temp/pr2054/independent-third/crossref-j.biortech.2011.07.098.json
    sha256: 1ad8e14d43f2af7720a7925969e0a7326add68f8ff7883bbc32d7f8dea6391a2
    role: context
  - path: .temp/pr2054/independent-third/crossref-j.biortech.2015.03.061.json
    sha256: 59d983accb896bd8ebefde77e4cd6f6a40cc4cea0b36071ebc0c61672371677c
    role: context
  - path: .temp/pr2054/independent-third/crossref-j.ijhydene.2008.04.004.json
    sha256: dcda8515406e0486af778bc4b6e5c3b1505dce3ab5e617f9a36b8a60636d4e9f
    role: context
  - path: .temp/pr2054/independent-third/crossref-j.ijhydene.2015.05.135.json
    sha256: 34d316b352a0345d98410a4ace2c8e3ed13b060ca29800a543163f06a9fdf94c
    role: context
  - path: .temp/pr2054/independent-third/crossref-j.jbiosc.2012.08.020.json
    sha256: 0005ac3207e1cc048d80010180892ecb587e338635dd058faa5cddd287167da0
    role: context
  - path: .temp/pr2054/independent-third/crossref-s00253-016-7776-1.json
    sha256: f9d7c020738c85e1c2a20f3c247ed2b13a99753a160b8e918169a68d7c7784cb
    role: context
  - path: .temp/pr2054/independent-third/doi-j.ijhydene.2008.04.004.html
    sha256: 81e97a4be59b7432c21112484d077aceb941d2f4399ff4fe7a88bfbbb5c6b873
    role: context
  - path: .temp/pr2054/independent-third/doi-s00253-016-7776-1.html
    sha256: de246f8901d247c4b6cd77c84c8c061744495d35755140f5251ed9426c3d57ff
    role: context
  - path: .temp/pr2054/independent-third/doi180-2008.json
    sha256: 8c217938c694087b06a5ee2cf7db434fae3320c81aa4583a2ff9f997bb16bde0
    role: context
  - path: .temp/pr2054/independent-third/doi264-2015.json
    sha256: e1ef85832f662f33702566a39d1cac14930cad54b6d8d3f7128b84b157cc2480
    role: context
  - path: .temp/pr2054/independent-third/elsevier-j.ijhydene.2008.04.004.xml
    sha256: 6a29c87f69d437c1493638009eea5d873f12f4adbc85ffa5abac0af27ed20862
    role: context
  - path: .temp/pr2054/independent-third/figure-inventory.json
    sha256: 049d65dfa94909cec649d15f041960113460c96e32c48e408f339c44d00f454e
    role: context
  - path: .temp/pr2054/independent-third/focused-checks.json
    sha256: 6499b8cd711b59a9265fa9c06c3aa856ceeb97c5e723aac2de83de19a649a972
    role: context
  - path: .temp/pr2054/independent-third/fresh-alternate-receipts.json
    sha256: 25ebfb494587564c042571641b22d2895336067dbf38083d9198c36a676d7bd1
    role: context
  - path: .temp/pr2054/independent-third/fresh-archive-and-alias-receipts.json
    sha256: ad387724f2c3e15aa7298661afffd2c894c92804c71b37858ed33abb798b9cec
    role: context
  - path: .temp/pr2054/independent-third/fresh-asset-receipts.json
    sha256: e44c8b076248e3761918ced31e3aa389cd001291cab99b7114e411bef83b41dd
    role: context
  - path: .temp/pr2054/independent-third/fresh-authority-and-access-receipts.json
    sha256: a18657cbd5288e30ff158c22f986e687f627548eca5862fe3edf4529f777c030
    role: context
  - path: .temp/pr2054/independent-third/fresh-final-access-receipts.json
    sha256: b22faf1ef55af5f35b2e8fbcfa8fa16c9f65f930da071995f2d851cd378ba84e
    role: context
  - path: .temp/pr2054/independent-third/fresh-fulltext-receipts.json
    sha256: 5bb027fe43fa28d79db0a310f84cc51a1a98888db87f2831ab6c36f224df1675
    role: context
  - path: .temp/pr2054/independent-third/fresh-metadata-receipts.json
    sha256: b4ceba675a7a34f1be1adac593d5ef731ad9d945045af50c546e32c11b66ccdb
    role: context
  - path: .temp/pr2054/independent-third/fresh-snippet-replay.json
    sha256: 93741ef7e2679230707bcece9c7bd83de310eda2d3cf58ae8cd083498a448714
    role: context
  - path: .temp/pr2054/independent-third/frontiers180.html
    sha256: 20e132e661f3f728dc5db84930801a7f6d22883d0d186ae48b8a507896379abe
    role: context
  - path: .temp/pr2054/independent-third/frozen-input-audit.json
    sha256: 814f13ce8cbdde12a0cb7f203002b5034e6bc7ad23abfddf97c67dbccbf547b5
    role: context
  - path: .temp/pr2054/independent-third/go0015979.json
    sha256: 7860edb17d31745618f5899628e2f34c03eb5d2a9d78364b6a84ddf8c46702ae
    role: context
  - path: .temp/pr2054/independent-third/gtdb-replay.json
    sha256: 95c0882bdcb8f4b130528c901e189d61aaeab1a99a3b9e21ce4587c92ea07286
    role: context
  - path: .temp/pr2054/independent-third/independent-science-final.json
    sha256: dc7605bfa1201ed141daf5c1a6aba3c463a1d2bf4eb52f3f2d6ef389b2f2ad84
    role: context
  - path: .temp/pr2054/independent-third/independent-three-records-final.json
    sha256: 581f20273889f0112f7c830520fed337461dffdf546a2bc3576a6d3d454c4472
    role: context
  - path: .temp/pr2054/independent-third/pmid21764954.json
    sha256: 95d87dd19962960781aa890e641901d9d7584e26b1835f75d31b089ec706dfd0
    role: context
  - path: .temp/pr2054/independent-third/pmid21868218.json
    sha256: 9878365e000f3605da908d1a649ef080b325f5ef5f26a47c960df852f946aa7a
    role: context
  - path: .temp/pr2054/independent-third/pmid22999358.json
    sha256: d550cb08809de4adf65654b9cc37ab50c4126841b493e4057aa60c8add945974
    role: context
  - path: .temp/pr2054/independent-third/pmid23275517.json
    sha256: 354ab9f74e3da285b568ea410f21db928322bdaf754bbb72bf0282cb590771ac
    role: context
  - path: .temp/pr2054/independent-third/pmid25818258.json
    sha256: a99a8f1baf21d7a16edb07602d661c9da2fee0e27a149b140cad423e589007ba
    role: context
  - path: .temp/pr2054/independent-third/pmid27208134.json
    sha256: 1751948290c9cd21ca54b60e7968cbac2ce7c0faac1a0039c5cac27668c5ea0d
    role: context
  - path: .temp/pr2054/independent-third/pmid27538932.json
    sha256: 61eb0b043dfbdf953ab4b5de1fd304bcce73bd8aac56e7bc4618228c52f66de4
    role: context
  - path: .temp/pr2054/independent-third/pmid31551972.json
    sha256: 416f417d4fa5e1b04c4c3574ed37888cf3517af76087da6418f30792513081f6
    role: context
  - path: .temp/pr2054/independent-third/selected-inventory.json
    sha256: f2ae4c41addf24e0f75eac1a43bf93415a702cb2b92fc9b47d48962d677fff93
    role: context
  - path: .temp/pr2054/independent-third/springer180.read.txt
    sha256: 3f75f9b9faedb561ed1025a74f8222a86f95995b092f98d093bf92ada0995b40
    role: context
  - path: .temp/pr2054/independent-third/supplement-180-manifest.json
    sha256: 8737b55eb2b990d032158b7d1dcad8287b5dc15357cfe07fdc4c10b2e3deeee6
    role: context
  - path: .temp/pr2054/independent-third/supplement-180/Image_1.TIF
    sha256: 04f92aced977f564e03f0637e8935d35ecf1218953aa87e45172d415c73048db
    role: context
  - path: .temp/pr2054/independent-third/supplement-180/Image_2.TIF
    sha256: 61a7758df8bffb4c081ef92c624d8a89ac53f72ebf29fbf746c445666d50415c
    role: context
  - path: .temp/pr2054/independent-third/supplement-180/Image_3.TIF
    sha256: 09a12398fa4f184a9e60f330670a83559bf7aeb7892d784c5c8dafe18f1d1b5d
    role: context
  - path: .temp/pr2054/independent-third/supplement-180/Table_1.DOCX
    sha256: 1df77737bbe4626a73d3d0a9ca68465925d0790ef3e2b871fce9eb318ec97b19
    role: context
  - path: .temp/pr2054/independent-third/supplement-180/Table_1.txt
    sha256: 95ab87ce69f5fd3b45d9f1abae8d29c87305087455695442ac2d29de473f2482
    role: context
  - path: .temp/pr2054/independent-third/supplement-180/fmicb-10-02035-g001.gif
    sha256: 1bc912f9053d173a3708748596e6e38e0b3f6a8a245170a81727954a6b3d3632
    role: context
  - path: .temp/pr2054/independent-third/supplement-180/fmicb-10-02035-g001.jpg
    sha256: caaba5a271f8ddd5dcd99814d3405f268c664f4ce6271f21793e78f9acc21eb7
    role: context
  - path: .temp/pr2054/independent-third/supplement-180/fmicb-10-02035-g002.gif
    sha256: c0fb0776a9b6e14deb1851801d4e0d5c69202ceb5b035d56fd826ba5f8592dc4
    role: context
  - path: .temp/pr2054/independent-third/supplement-180/fmicb-10-02035-g002.jpg
    sha256: 6502cf59811a12d43f18ecbbc003ffc1086807ad965ba23d6fb555c4e086b10e
    role: context
  - path: .temp/pr2054/independent-third/supplement-180/fmicb-10-02035-g003.gif
    sha256: 45b55d7133fd7a12550904aaebaef6193422ec80a70c46dca004f8e88d0e4954
    role: context
  - path: .temp/pr2054/independent-third/supplement-180/fmicb-10-02035-g003.jpg
    sha256: 5b24c48d52c09f3f48c3c700052417436a3b72ab10fbb4c7e8a569e42de3956f
    role: context
  - path: .temp/pr2054/independent-third/supplement-180/fmicb-10-02035-g004.gif
    sha256: ad1050c21c25a82d8bbea31f67a8c227017f97cb76bf089385816913bf6c6d03
    role: context
  - path: .temp/pr2054/independent-third/supplement-180/fmicb-10-02035-g004.jpg
    sha256: 0f94db17125eac0b9bdca7cb3849653da684f17e0581ff27db5ba466bd7d5fbc
    role: context
  - path: .temp/pr2054/independent-third/supplement-180/fmicb-10-02035-g005.gif
    sha256: 3e7e8b0e08f759573676c873cd3f3c44262e2d7df48d5119eaba98923d7ae486
    role: context
  - path: .temp/pr2054/independent-third/supplement-180/fmicb-10-02035-g005.jpg
    sha256: 13858f54bef8ceff41f4895a6d0b775da354917e42782afdd30f362471705a78
    role: context
  - path: .temp/pr2054/independent-third/supplement-180/fmicb-10-02035-g006.gif
    sha256: 12cf099a806b960b8de1402bccdcaf3d8f95874b0ca163a54c73164ae8c8b9e7
    role: context
  - path: .temp/pr2054/independent-third/supplement-180/fmicb-10-02035-g006.jpg
    sha256: f8c0c9459dbcb99270551d4342ca4e74cb704eb2c168e5a64f20e1eae2af02cf
    role: context
  - path: .temp/pr2054/independent-third/supplement-180/fmicb-10-02035-g007.gif
    sha256: 7a8e910a4a92f921e7eac80206dd640e617e9a3e0f481ef1fcb1f2674b4b3ab4
    role: context
  - path: .temp/pr2054/independent-third/supplement-180/fmicb-10-02035-g007.jpg
    sha256: 57beb49ae16db41669837c0a88b614eb4ebabb6ed1fd2b228ca978476eb7d5ab
    role: context
  - path: .temp/pr2054/independent-third/supplement-retry-receipt.json
    sha256: 6d999ad710589dc5196b9721cf3d112d7c24480eeea5b192bb14aec9cd3b0702
    role: context
  - path: .temp/pr2054/independent-third/taxonomy.xml
    sha256: 407b3178ec84214dfd0b0b0657b7011beb5acfbc51f6215a0255664fee0d3685
    role: context
  - path: AGENTS.md
    sha256: 7c35deb79ce874239f1080c2f575756ff47d1985483030878eaeb07df02d7529
    role: context
  - path: conf/record_review.yaml
    sha256: c4ad25505a87a040c57eb93f1ee9673a09389a474c6d4e1136781456ff190fc8
    role: context
  - path: docs/record-review-profile.md
    sha256: 285f79747999f83edbe63e5efde349a5cc063e9e486ce1a748b47b76c6631f31
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: history/records/Clostridium_Thermoanaerobacterium_JN4_GD17_Cellulosic_Biofuel_Coculture/2026-10-06T012901Z-codex-8cf494.yaml
    sha256: 405f1fa13c36292db7491fb074ded016b5193ff91e93c4060b8804acf52f7c21
    role: context
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: kb/communities/Clostridium_Thermoanaerobacterium_JN4_GD17_Cellulosic_Biofuel_Coculture.yaml
    sha256: 5dfcac09163ce6ac2930e58230d3d82efda7d5f63cda1afeba33bc16c05d2ecd
    role: target
  - path: references_cache/PMID_27538932.md
    sha256: 4708db048b9db30409e896e5a52dda9fbf35c31a41a6da6b09afcbb0dcc00bef
    role: context
  - path: references_cache/PMID_31551972.md
    sha256: b8dd7f4edd84b1d7b3af2d310bdb5150ad0af8e830a9e08ed526ca2e3101a268
    role: context
  - path: references_cache/PMID_31551972.txt
    sha256: 706c98a05a78a0cba0660a603bdcea89b44248e91f1a94d38464c56d3dea6ec8
    role: context
  - path: reviews/structured/20261021T231001Z-jn4-gd17-record-review/review.md
    sha256: 1002dfc180fc1183a6ed11b1e51f40cded0c37fe894eba6377314ab3a363a91e
    role: context
  - path: reviews/structured/20261021T231001Z-jn4-gd17-record-review/review.yaml
    sha256: 943a1118023956b9049bd90df39a0d699c185953eb84b0ee08eb73d5f1498b3c
    role: context
  - path: reviews/structured/20261106T135321Z-jn4-gd17-s1-proof-correction/review.md
    sha256: 36656cc1ec1279f1686ec0fc7a9d64cdc1642f48b533300ab60541207cd31fbe
    role: context
  - path: reviews/structured/20261106T135321Z-jn4-gd17-s1-proof-correction/review.yaml
    sha256: b0fc52320f0ae803775299edadd09a43b7168dd3ece318bc8e28d12fbb1bd8c9
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/adhoc/pr2054_180_input_provenance.py
    sha256: 47f586e75deb2103f7f0787376c17eb0b5c98663b22dac8862f393f9c8f14a2a
    role: context
  - path: scripts/adhoc/pr2054_180_s1_review_correction.py
    sha256: dfc502e78633ab4c8652d7535d74fe99830766983dfe90496d560c090afb2ba8
    role: context
  - path: scripts/gtdb_ground.py
    sha256: 0fc1ba926a56e5be85cdf064db0cf56452aeeee93f15b0ced98e8f11b5296175
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: src/communitymech/schema/communitymech.yaml
    sha256: 7355e14f0f17c5d3b875abd33af6474ddc1aad08cc3305313686fede337e259a
    role: context
targets:
- target_id: CommunityMech:000180
  path: kb/communities/Clostridium_Thermoanaerobacterium_JN4_GD17_Cellulosic_Biofuel_Coculture.yaml
  label: Clostridium-Thermoanaerobacterium JN4-GD17 Cellulosic Biofuel Coculture
  kind: maintained
  record_class: MicrobialCommunity
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Clostridium_Thermoanaerobacterium_JN4_GD17_Cellulosic_Biofuel_Coculture.yaml
    role: canonical_record
scope:
  description: Current unchanged 000180 target and all three predecessor findings/actions;
    fresh 2019 body/figures/SI and available 2016 abstract; bounded correction of
    the predecessor's S1 inference.
  selection: 'Only CommunityMech:000180 in PR #2054.'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000180
  exclusions:
  - target: 'Other PR #2054 records'
    reason: Outside this author successor.
checks:
- check_id: validate
  name: Focused validate
  status: passed
  required: true
  summary: Exit 0 on the unchanged current target; exact receipt retained.
  target_ids:
  - CommunityMech:000180
  command: just --no-dotenv validate kb/communities/Clostridium_Thermoanaerobacterium_JN4_GD17_Cellulosic_Biofuel_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - focused-qc
  scope_note: Run before the author's role switch; no target/validator edit.
- check_id: strict
  name: Focused strict
  status: passed
  required: true
  summary: Exit 0 on the unchanged current target; exact receipt retained.
  target_ids:
  - CommunityMech:000180
  command: just --no-dotenv validate-strict kb/communities/Clostridium_Thermoanaerobacterium_JN4_GD17_Cellulosic_Biofuel_Coculture.yaml
    --out .temp/pr2054/independent-third/000180/strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - focused-qc
  scope_note: Run before the author's role switch; no target/validator edit.
- check_id: terms
  name: Focused terms
  status: passed
  required: true
  summary: Exit 0 on the unchanged current target; exact receipt retained.
  target_ids:
  - CommunityMech:000180
  command: just --no-dotenv validate-terms kb/communities/Clostridium_Thermoanaerobacterium_JN4_GD17_Cellulosic_Biofuel_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - focused-qc
  scope_note: Run before the author's role switch; no target/validator edit.
- check_id: references
  name: Focused references
  status: passed
  required: true
  summary: Exit 0 on the unchanged current target; exact receipt retained.
  target_ids:
  - CommunityMech:000180
  command: just --no-dotenv validate-references-explained kb/communities/Clostridium_Thermoanaerobacterium_JN4_GD17_Cellulosic_Biofuel_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - focused-qc
  scope_note: Run before the author's role switch; no target/validator edit.
- check_id: gtdb
  name: Focused gtdb
  status: passed
  required: true
  summary: Exit 0 on the unchanged current target; exact receipt retained.
  target_ids:
  - CommunityMech:000180
  command: just --no-dotenv validate-gtdb kb/communities/Clostridium_Thermoanaerobacterium_JN4_GD17_Cellulosic_Biofuel_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - focused-qc
  scope_note: Run before the author's role switch; no target/validator edit.
- check_id: gtdb-domain
  name: Focused gtdb-domain
  status: passed
  required: true
  summary: Exit 0 on the unchanged current target; exact receipt retained.
  target_ids:
  - CommunityMech:000180
  command: just --no-dotenv validate-gtdb-domain kb/communities/Clostridium_Thermoanaerobacterium_JN4_GD17_Cellulosic_Biofuel_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - focused-qc
  scope_note: Run before the author's role switch; no target/validator edit.
- check_id: history
  name: Focused history
  status: passed
  required: true
  summary: Exit 0 on the unchanged current target; exact receipt retained.
  target_ids:
  - CommunityMech:000180
  command: just --no-dotenv validate-history history/records/Clostridium_Thermoanaerobacterium_JN4_GD17_Cellulosic_Biofuel_Coculture
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - focused-qc
  scope_note: Run before the author's role switch; no target/validator edit.
- check_id: full-lint
  name: Full repository lint before helper freeze
  status: passed
  required: true
  summary: Black, Ruff and mypy passed before the helper was committed and pinned.
  target_ids:
  - CommunityMech:000180
  command: just --no-dotenv lint
  exit_code: 0
  expected_exit_code: 0
  evidence_ids: []
- check_id: provenance-helper-full-lint
  name: Full lint before second helper freeze
  status: passed
  required: true
  summary: Full Black, Ruff and mypy passed before the new helper was frozen.
  target_ids:
  - CommunityMech:000180
  command: just --no-dotenv lint
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - complete-input-manifest
evidence:
- evidence_id: identity
  kind: primary_source
  reference: PMID:31551972; doi:10.3389/fmicb.2019.02035
  locator: Strains and Chemicals; Enhanced End-Product Formation
  summary: Methods identifies JN4 (CGMCC 1.5210) and GD17 (CGMCC 1.5209). The authors
    report reconstruction with both strains and present PCR as confirmation. This
    is author-reported identity, not independent certification of the S1 controls.
  snapshot_sha256: 8c035478025c2fad39825a1f810184b58eb435cf92e628ac1af912ce37404e10
  accessed_at: '2026-11-06T13:39:26.609555Z'
  support: supports
- evidence_id: recipe
  kind: primary_source
  reference: PMID:31551972; doi:10.3389/fmicb.2019.02035
  locator: Bacterial Growth
  summary: The complete CTFUD formulation and substrate alternatives are available.
    Keep salt forms, unspecified resazurin stock strength, seed context, and 0.5%
    substrate arms separate; do not infer missing gas ratios or culture pH.
  snapshot_sha256: 8c035478025c2fad39825a1f810184b58eb435cf92e628ac1af912ce37404e10
  accessed_at: '2026-11-06T13:39:26.609555Z'
  support: supports
- evidence_id: growth
  kind: primary_source
  reference: PMID:31551972; doi:10.3389/fmicb.2019.02035
  locator: Bacterial Growth; Enhanced End-Product Formation
  summary: Anaerobic tubes/serum bottles at 60 C without agitation, 10% seed addition,
    and a separately stated 1:1 reconstruction ratio are reported. At least five passages
    is a reconstruction statement, not an endpoint abundance.
  snapshot_sha256: 8c035478025c2fad39825a1f810184b58eb435cf92e628ac1af912ce37404e10
  accessed_at: '2026-11-06T13:39:26.609555Z'
  support: supports
- evidence_id: volumes
  kind: primary_source
  reference: PMID:31551972; doi:10.3389/fmicb.2019.02035
  locator: Analytical Methods
  summary: Cellulose-grown JN4 monoculture and coculture use 80 mL; independent glucose/cellobiose
    member-monoculture assays use 50 mL. These are not demonstrated sugar-coculture
    arms or interchangeable vessel capacities.
  snapshot_sha256: 8c035478025c2fad39825a1f810184b58eb435cf92e628ac1af912ce37404e10
  accessed_at: '2026-11-06T13:39:26.609555Z'
  support: supports
- evidence_id: analytical
  kind: primary_source
  reference: PMID:31551972; doi:10.3389/fmicb.2019.02035
  locator: Analytical Methods; Biomass and Bacterial Ratio Determination; Real-Time
    PCR
  summary: Products, protein-based biomass estimates, 16S DNA proportions and recA-normalized
    transcription are different measurements. Added-carbon and sampling-time differences
    prevent selective flux or viable-growth attribution.
  snapshot_sha256: 8c035478025c2fad39825a1f810184b58eb435cf92e628ac1af912ce37404e10
  accessed_at: '2026-11-06T13:39:26.609555Z'
  support: supports
- evidence_id: xylose
  kind: primary_source
  reference: PMID:31551972; doi:10.3389/fmicb.2019.02035
  locator: GD17 growth/biomass results; Figure 4C; tentative Figure 6B
  summary: Weak GD17 corncob growth and a proposed hemicellulose-to-xylose benefit
    do not demonstrate xylose release, transfer or JN4 benefit. The route should remain
    an authors' hypothesis, not be declared impossible.
  snapshot_sha256: 8c035478025c2fad39825a1f810184b58eb435cf92e628ac1af912ce37404e10
  accessed_at: '2026-11-06T13:39:26.609555Z'
  support: supports
- evidence_id: contexts
  kind: primary_source
  reference: PMID:31551972; doi:10.3389/fmicb.2019.02035
  locator: Reference Chimtong et al. 2011; Reference Liu et al. 2008; Figures 1-7
  summary: The cited hemicellulose isolate is NOI-1, not GD17. The 2019 bibliography
    misattaches PMID 27538932 to the distinct 2008 DOI. Seven fresh main figures were
    inspected; their outcomes and conceptual model do not override these identity
    or inferential boundaries.
  snapshot_sha256: 8c035478025c2fad39825a1f810184b58eb435cf92e628ac1af912ce37404e10
  accessed_at: '2026-11-06T13:39:26.609555Z'
  support: supports
- evidence_id: supplement
  kind: primary_source
  reference: PMID:31551972; doi:10.3389/fmicb.2019.02035
  locator: Supplementary Figure S1, Image_1.TIF; Table S1; S2-S3
  summary: Fresh S1 displays G/J/C lanes in every primer group; the JN-1/JN-2 bands
    appear in G and C while J is blank. The caption additionally names G as T. thermocellum
    and J as C. thermocellum JN4. The positive C lanes are compatible with the authors'
    report but cannot independently certify the stated strain specificity while these
    labels conflict. S2 compares expression and S3 compares stimulant growth. The
    full primer table retains duplicated licB rows. No sequence reanalysis was done.
  snapshot_sha256: 04f92aced977f564e03f0637e8935d35ecf1218953aa87e45172d415c73048db
  accessed_at: '2026-11-06T13:45:54.562891Z'
  support: context_only
- evidence_id: strain
  kind: authority
  reference: 'NCBI Taxonomy efetch: 1515 and 1517'
  locator: Species names/ranks; source-local JN4/GD17 designations
  summary: NCBI confirms species-level Acetivibrio thermocellus and Thermoanaerobacterium
    thermosaccharolyticum. Source collection accessions remain author-reported; no
    direct CGMCC catalogue certification or invented strain CURIE is asserted.
  snapshot_sha256: 407b3178ec84214dfd0b0b0657b7011beb5acfbc51f6215a0255664fee0d3685
  accessed_at: '2026-11-06T13:41:15.623022Z'
  support: supports
- evidence_id: gtdb
  kind: authority
  reference: KG-Microbe NCBI2GTDB.tsv.gz; scripts/gtdb_ground.py --community
  locator: Exact ncbi_id mappings for 1515 and 1517
  summary: Fresh community-mode replay preserves both 1.0/18 mappings. Crosswalk SHA256
    is 761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd. July 25 is
    file metadata, not a verified latest release/build. The name-comparison flag does
    not establish biological reclassification.
  snapshot_sha256: 6457708b4a1d862b020e022dd503ad7d43062ba8e3a6c4699e867a2cb3e9560b
  accessed_at: '2026-11-06T13:53:21.815488Z'
  support: supports
- evidence_id: schema
  kind: authority
  reference: src/communitymech/schema/communitymech.yaml; AGENTS.md
  locator: FunctionalRoleEnum; cultivation and evidence definitions; optional state
  summary: Current role, evidence and cultivation semantics support the retained actions.
    Ecological state remains optional. Host, soils and community relations do not
    create mandatory omissions for this liquid bacterial pair.
  snapshot_sha256: 7355e14f0f17c5d3b875abd33af6474ddc1aad08cc3305313686fede337e259a
  accessed_at: '2026-11-06T13:53:21.815488Z'
  support: supports
- evidence_id: predecessor
  kind: prior_review
  reference: reviews/structured/20261021T231001Z-jn4-gd17-record-review/review.yaml
  locator: evidence[evidence_id=supplement].summary; findings and all four actions
  summary: The predecessor positively described S1 as supporting primer-specific membership
    while mentioning only its caption-name discrepancy. This successor withdraws that
    independent proof inference, preserves the immutable old bytes, and retains all
    three open record findings.
  snapshot_sha256: 943a1118023956b9049bd90df39a0d699c185953eb84b0ee08eb73d5f1498b3c
  accessed_at: '2026-11-06T13:53:21.815488Z'
  support: context_only
- evidence_id: focused-qc
  kind: validation
  reference: .temp/pr2054/independent-third/focused-checks.json
  locator: CommunityMech:000180 entries; current unchanged target
  summary: Seven focused record gates passed with real exit 0 before this agent switched
    from independent reader to correction author. The record and relevant validator
    bytes are unchanged; these receipts are reused explicitly, not claimed as independent
    approval of this successor.
  snapshot_sha256: 6499b8cd711b59a9265fa9c06c3aa856ceeb97c5e723aac2de83de19a649a972
  accessed_at: '2026-11-06T13:53:21.815488Z'
  support: supports
- evidence_id: access
  kind: primary_source
  reference: PMID:27538932; doi:10.1007/s00253-016-7776-1
  locator: Fresh Europe PMC abstract and publisher subscription preview
  summary: The 2016 hydrogen paper remains abstract/preview only. Its reported comparative
    rate does not certify the full assay. The 2008 API returns bibliographic coredata,
    not a complete body. Current partial status is preserved despite complete fresh
    access to the 2019 SI.
  snapshot_sha256: 61eb0b043dfbdf953ab4b5de1fd304bcce73bd8aac56e7bc4618228c52f66de4
  accessed_at: '2026-11-06T13:53:21.815488Z'
  support: context_only
- evidence_id: metrics
  kind: validation
  reference: kb/communities/Clostridium_Thermoanaerobacterium_JN4_GD17_Cellulosic_Biofuel_Coculture.yaml
  locator: Current native rubric presence and evidence counts
  summary: Unchanged record has three nodes, two qualified arrows and six node evidence
    occurrences. The three retained findings are one P2 and two P3. Presence completeness
    is 85; quality raw 121, capped 100. Rubric required-field wording is a scoring
    rule, not LinkML requiredness.
  snapshot_sha256: 5dfcac09163ce6ac2930e58230d3d82efda7d5f63cda1afeba33bc16c05d2ecd
  accessed_at: '2026-11-06T13:53:21.815488Z'
  support: supports
- evidence_id: complete-input-manifest
  kind: validation
  reference: .temp/pr2054/180-input-provenance/input-paths.json
  locator: Exact files passed to native inspect; GTDB byte-copy receipt
  summary: The complete bounded local input surface is now hashed in source.inputs.
    Fresh main/SI figures, XML/text, authority/source-access data, actual check logs,
    both helpers and immutable predecessors are included. Shared receipt entries outside
    000180 remain context only. The copied GTDB bytes equal the source snapshot.
  snapshot_sha256: 0ba87f9ba87cb292ac6f403504ee12c6ff52cdee5dc7cce6f8aa120dbb638553
  accessed_at: '2026-11-06T14:04:46.017116Z'
  support: supports
assessments:
- assessment_id: s1-proof-correction
  area: evidence
  topic: Bound the predecessor S1 inference
  outcome: concern
  summary: Withdraw independent primer-specific membership proof from S1.
  target_ids:
  - CommunityMech:000180
  evidence_ids:
  - supplement
  - predecessor
  - identity
  details: 'Issue #2544 concerns this review-metadata sentence only. Attribute the
    pair and the authors'' PCR-confirmation statement to Methods. Explicitly preserve
    the G/J/C band-label conflict and separate caption typo. Do not relabel lanes,
    infer another member, assert failed reconstruction or redesign primers. The independent
    predecessor audit identified this defect; this document is the author remediation
    and requires a separate read-only re-review.'
- assessment_id: identity
  area: identity
  topic: Exact reconstructed pair
  outcome: supported
  summary: The source-reported JN4/GD17 identity remains appropriate.
  target_ids:
  - CommunityMech:000180
  evidence_ids:
  - identity
  - strain
  - supplement
  details: Historical names, current NCBI species labels and author-reported strain
    accessions remain distinct. The ambiguous S1 controls do not independently certify
    specificity or justify changing canonical membership.
- assessment_id: culture
  area: scope
  topic: CTFUD and assay-specific cultivation
  outcome: concern
  summary: The original cultivation finding and all its acceptance checks remain open.
  target_ids:
  - CommunityMech:000180
  evidence_ids:
  - recipe
  - growth
  - volumes
  - analytical
  - schema
  details: The full source contradicts the record's no-working-volume/abstract-only
    limitations. Preserve exact source forms, separate culture arms and omit invented
    static-operation rationale; no canonical change occurs here.
- assessment_id: xylose
  area: evidence
  topic: Proposed hemicellulose benefit
  outcome: concern
  summary: The original xylose hypothesis-qualification finding remains open.
  target_ids:
  - CommunityMech:000180
  evidence_ids:
  - xylose
  - contexts
  details: Weak corncob growth and a tentative model do not establish GD17 xylose
    release or JN4 uptake. The different NOI-1 background reference stays scoped.
- assessment_id: taxonomy
  area: grounding
  topic: Valid mappings and unsupported provenance shorthand
  outcome: concern
  summary: The original GTDB snapshot finding remains open; core mappings reproduce.
  target_ids:
  - CommunityMech:000180
  evidence_ids:
  - gtdb
  - strain
  details: Retain exact IDs, lineages, 1.0 fractions and 18-genome counts for both
    species. A local file date does not establish a release called latest.
- assessment_id: graph
  area: graph
  topic: Measured outcomes versus inferred mechanisms
  outcome: supported
  summary: Three nodes and two qualified arrows remain appropriately bounded.
  target_ids:
  - CommunityMech:000180
  evidence_ids:
  - analytical
  - contexts
  - access
  details: Community products, independent sugar conversion, estimated JN4 biomass,
    DNA proportions and transcription are distinct. Preserve confounding from added
    carbon and different sampling times; no direct flux, viable-cell count, reciprocal
    harm, obligatory dependence or required abundance is inferred.
- assessment_id: coverage
  area: scope
  topic: Current access and historical limits
  outcome: unknown
  summary: Partial scientific scope remains necessary because the 2016 full assay
    is unavailable.
  target_ids:
  - CommunityMech:000180
  evidence_ids:
  - access
  - supplement
  - predecessor
  details: Fresh 2019 body, seven main figures, three SI figures and complete primer
    table were read. The first SI transfer timed out and the second completed. The
    predecessor's dates and source limits remain historical; no unavailable /private/tmp
    artifact is an active input or claimed newly read source.
- assessment_id: validation
  area: schema
  topic: Native focused gates and current guidance
  outcome: supported
  summary: Current record validators pass independently of the scientific limitations.
  target_ids:
  - CommunityMech:000180
  evidence_ids:
  - focused-qc
  - schema
  details: The existing source caches have accurate content-type headers and remain
    unchanged. Existing append-only graph history and the open flux/growth knowledge-gap
    discussion remain bounded. No new cache/history repair or request to perform experiments
    is introduced.
- assessment_id: metrics
  area: completeness
  topic: Native rubric arithmetic
  outcome: supported
  summary: Completeness 85; raw quality 121, capped 100.
  target_ids:
  - CommunityMech:000180
  evidence_ids:
  - metrics
  metrics:
  - name: completeness
    value: 85
    unit: points
    minimum: 0
    maximum: 100
    definition: Required fields/roles 50 + environment 5 + three-environmental-factors
      bonus 0 + at least three interaction nodes 10 + external resources 5 + medium
      10 + datasets 0 + metabolites 5 = 85. Count nodes, not typed nodes.
  - name: validation_quality
    value: 100
    unit: points
    minimum: 0
    maximum: 100
    definition: clamp(100−50P1−10P2−2P3+20min(mean evidence/2,1)+15 if COMPLETE,0,100).
      Evidence counts [1,2,3] across three nodes give mean 2, bonus 20; COMPLETE adds
      15; one P2/two P3 gives raw 121/cap 100.
  - name: P1
    value: 0
    unit: findings
    definition: Native severity count.
  - name: P2
    value: 1
    unit: findings
    definition: Native severity count.
  - name: P3
    value: 2
    unit: findings
    definition: Native severity count.
  - name: P4
    value: 0
    unit: findings
    definition: Native severity count.
  details: Rechecked against the unchanged current record and three retained curation
    findings. Presence scores do not certify scientific completion or make optional
    state mandatory.
- assessment_id: complete-local-input-provenance
  area: provenance
  topic: Complete input attestation for the current 000180 successor
  outcome: supported
  summary: Correct the incomplete input set of the 135321 predecessor (#2566).
  target_ids:
  - CommunityMech:000180
  evidence_ids:
  - complete-input-manifest
  details: The earlier 19 hashes matched their files but omitted other actual local
    sources and check receipts. Those omissions are explicitly acknowledged. This
    review retains the accepted S1 lane/caption qualification, partial scientific
    status, all three open scientific findings and all four actions unchanged. Native
    inspection output cannot hash itself; the new candidate and subsequent post-save
    validation receipts are generated outputs, not prior judgment inputs. This correction
    does not reassess the other nine original batch records.
findings:
- finding_id: recover-cultivation-scope
  issue_key: cm-000180-recover-cultivation-scope
  category: scope
  severity: major
  native_severity: P2
  normalization_reason: False volume/recipe limits and conflated assay contexts materially
    impair reproducibility.
  rule_id: review-checklist.claim-specific-scope-and-grounding
  status: open
  certainty: confirmed
  title: Recover CTFUD and assay-specific cultivation scope
  description: The record falsely says no working volume is reported, omits available
    CTFUD formulation, merges substrate assay contexts and adds an unsupported explanation
    for static operation. The abstract-only preparation note is stale.
  target_ids:
  - CommunityMech:000180
  field_paths:
  - growth_media[0].name
  - growth_media[0].composition
  - growth_media[0].preparation_notes
  - growth_media[0].evidence[0].explanation
  - cultivation_setup[0].instrument_detail
  - cultivation_setup[0].notes
  evidence_ids:
  - recipe
  - growth
  - volumes
  - analytical
  - identity
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Clostridium_Thermoanaerobacterium_JN4_GD17_Cellulosic_Biofuel_Coculture.yaml
    role: canonical_record
  ownership_note: Maintained YAML owns future repair. Coordinate current 1343 and
    scoped 746 without closing unrelated issue content.
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261021T231001Z-jn4-gd17-record-review
    finding_id: recover-cultivation-scope
  - repository: CultureBotAI/CommunityMech
    review_id: 20261106T135321Z-jn4-gd17-s1-proof-correction
    finding_id: recover-cultivation-scope
- finding_id: qualify-xylose-model
  issue_key: cm-000180-qualify-xylose-model
  category: evidence
  severity: minor
  native_severity: P3
  normalization_reason: Bounded non-graph wording overstates a tentative route; the
    core graph is already qualified.
  rule_id: review-checklist.claim-specific-scope-and-grounding
  status: open
  certainty: confirmed
  title: Qualify the proposed GD17 xylose benefit
  description: The xylose entry converts a tentative hemicellulose-to-xylose benefit
    into categorical GD17 digestion. The paper reports weak corncob growth and a possible
    reciprocal benefit; its background citation concerns NOI-1 rather than GD17.
  target_ids:
  - CommunityMech:000180
  field_paths:
  - related_ingredients[3].relevance
  - related_ingredients[3].evidence[0].explanation
  evidence_ids:
  - xylose
  - contexts
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Clostridium_Thermoanaerobacterium_JN4_GD17_Cellulosic_Biofuel_Coculture.yaml
    role: canonical_record
  ownership_note: Maintained YAML owns future repair. Coordinate current 1343 and
    scoped 746 without closing unrelated issue content.
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261021T231001Z-jn4-gd17-record-review
    finding_id: qualify-xylose-model
  - repository: CultureBotAI/CommunityMech
    review_id: 20261106T135321Z-jn4-gd17-s1-proof-correction
    finding_id: qualify-xylose-model
- finding_id: document-gtdb-snapshot
  issue_key: cm-000180-document-gtdb-snapshot
  category: provenance
  severity: minor
  native_severity: P3
  normalization_reason: Core mappings are valid; the reproducibility statement is
    unsupported.
  rule_id: review-checklist.claim-specific-scope-and-grounding
  status: open
  certainty: confirmed
  title: Document the verified GTDB snapshot
  description: Both exact species mappings reproduce, but latest-release/build wording
    is not established by the snapshot modification time.
  target_ids:
  - CommunityMech:000180
  field_paths:
  - taxonomy[0].taxon_term.gtdb_classification.mapping_source
  - taxonomy[1].taxon_term.gtdb_classification.mapping_source
  evidence_ids:
  - gtdb
  - strain
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Clostridium_Thermoanaerobacterium_JN4_GD17_Cellulosic_Biofuel_Coculture.yaml
    role: canonical_record
  ownership_note: Maintained YAML owns future repair. Coordinate current 1343 and
    scoped 746 without closing unrelated issue content.
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261021T231001Z-jn4-gd17-record-review
    finding_id: document-gtdb-snapshot
  - repository: CultureBotAI/CommunityMech
    review_id: 20261106T135321Z-jn4-gd17-s1-proof-correction
    finding_id: document-gtdb-snapshot
actions:
- action_id: recover-protocols
  description: Recover available experiment-specific cultivation information.
  finding_ids:
  - recover-cultivation-scope
  target_ids:
  - CommunityMech:000180
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Clostridium_Thermoanaerobacterium_JN4_GD17_Cellulosic_Biofuel_Coculture.yaml
    role: canonical_record
  acceptance_checks:
  - Replace stale abstract-only and no-working-volume prose with source-local Methods.
    Enter the CTFUD formulation at the reported amounts, preserving hydrate/salt forms
    and resazurin 0.5 mL/L with stock strength unspecified. Do not invent culture
    pH, gas ratio, vessel capacity or missing vitamins.
  - Represent cellulose/Avicel, cellobiose, glucose and ground-corncob assay arms
    explicitly. The default listed cellobiose recipe does not mean cellobiose was
    co-added to every alternative substrate. Carbon source is 0.5%; Avicel plus dextrin/sucrose
    treatments contain 0.5% of each.
  - Scope 80 mL to cellulose-grown JN4 monoculture/coculture and 50 mL to glucose/cellobiose
    member-monoculture conversion tests. Adjust growth_media[0].name and evidence[0].explanation
    so independent sugar tests are not described as demonstrated sugar coculture arms.
  - Retain anaerobic tubes/serum bottles, 60 °C, no agitation and BATCH. Remove the
    invented cellulosome/settled-substrate rationale and unrelated neighboring-record/issue
    discussion from cultivation notes.
  - Keep 10% v/v seed separate from the reconstruction 1:1 cell ratio and at least
    five passages. Match seed substrates to the stated assays; neither value establishes
    an endpoint species fraction.
  - Do not import 200 rpm milling, centrifugation, 105 °C drying, citrate pH 4.8,
    45 °C enzymatic hydrolysis or six-day analytical incubation into culture fields.
    Preserve the existing biomass, sampling-time and added-carbon interpretation limits.
- action_id: qualify-xylose
  description: Restore hypothesis wording to the two xylose prose fields.
  finding_ids:
  - qualify-xylose-model
  target_ids:
  - CommunityMech:000180
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Clostridium_Thermoanaerobacterium_JN4_GD17_Cellulosic_Biofuel_Coculture.yaml
    role: canonical_record
  acceptance_checks:
  - Change related_ingredients[3].relevance and evidence[0].explanation to state the
    authors proposed hemicellulose-to-xylose benefit. Preserve the exact may-benefit
    snippet if retained.
  - Cite weak GD17 corncob growth and tentative Figure 6B; distinguish the background
    NOI-1 paper from GD17. No measured xylose release, transfer or JN4 benefit is
    asserted, and the route is not declared impossible.
- action_id: document-mapping
  description: Make both valid species mappings reproducible.
  finding_ids:
  - document-gtdb-snapshot
  target_ids:
  - CommunityMech:000180
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Clostridium_Thermoanaerobacterium_JN4_GD17_Cellulosic_Biofuel_Coculture.yaml
    role: canonical_record
  acceptance_checks:
  - Use crosswalk SHA 761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd
    and exact ncbi_id lookup route. Describe 2026-07-25 as local mtime, not a verified
    latest release/build.
  - Retain NCBITaxon:1515→Hungateiclostridium thermocellum and NCBITaxon:1517→Thermoanaerobacterium
    thermosaccharolyticum, each 1.0/18 genomes, current lineages and name-comparison
    flags. Keep JN4/GD17 and source-reported CGMCC accessions separate; no unverified
    strain CURIE or catalogue equivalence.
- action_id: validate-future-curation
  description: Validate bounded repairs and resolve remaining source access separately.
  finding_ids:
  - recover-cultivation-scope
  - qualify-xylose-model
  - document-gtdb-snapshot
  target_ids:
  - CommunityMech:000180
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Clostridium_Thermoanaerobacterium_JN4_GD17_Cellulosic_Biofuel_Coculture.yaml
    role: canonical_record
  acceptance_checks:
  - Preserve both members, all four roles and three untyped nodes/two qualified arrows.
    No reciprocal-harm, obligatory dependence, direct flux, viable count or mandatory
    abundance percentage is introduced.
  - Recover the exact 2016 full paper before certifying complete hydrogen-assay review.
    Keep its DOI/PMID distinct from the 2008 publication and preserve the 2019 bibliography
    discrepancy without silently rewriting evidence.
  - After separately authorized curation, append history and run schema, strict, term,
    reference, GTDB/domain, history and the actual generated-page recipes just gen-html
    and just check-docs-current. This review mutates no canonical record, cache, history,
    generated product or issue.
limitations:
- The 2016 hydrogen paper remains abstract/preview only; 2008 body is unavailable.
  Do not certify complete hydrogen-assay review or import their missing Methods.
- S1 contains unresolved lane/control-label ambiguity and a caption typo. No lane
  relabeling, contamination finding, failed reconstruction or new member follows.
- No raw sequencing, numerical, viable-cell or flux reanalysis was performed. Protein-based
  biomass and comparative metabolism do not establish selective causality.
- All prior bundles are immutable. Their old /private/tmp source paths are historical
  references only, not recoverable current inputs.
- This is an author remediation, not the independent re-review. Native save, bundle/contract
  and writer-gate receipts are reported separately after saving.
notes:
- The original 000180 evidence summary is explicitly qualified rather than silently
  rewritten.
- The open jn4_gd17_flux_and_growth_partition discussion remains an evidence-watch
  boundary. No action demands experiments.
- AGENTS.md is pinned directly; the CLAUDE.md symlink is not a current input.
- Includes prior native inspection, candidate and post-save receipts as historical
  inputs.
- The new inspection manifest defines the hashes and cannot hash itself.
- The new candidate and later save/check logs are outputs, not prior judgment inputs.
- Shared source/check receipts include other records; only 000180 is reassessed here.
- The external GTDB source is represented by a verified byte-identical scratch copy.
- Pinned scratch inputs attest to inspected bytes; they are not claimed to be committed
  source caches or durable raw-source publication. Current native input checks verified
  them before saving; later absence must not be described as source access.
related_reviews:
- repository: CultureBotAI/CommunityMech
  review_id: 20261021T231001Z-jn4-gd17-record-review
  relationship: Current-input successor retaining all three open findings; explicitly
    qualifies the predecessor evidence_id supplement S1 proof statement.
- repository: CultureBotAI/CommunityMech
  review_id: 20261106T135321Z-jn4-gd17-s1-proof-correction
  relationship: Retain identical science, three open findings and four actions; correct
    incomplete local input provenance without rewriting the saved predecessor.
links:
- https://github.com/CultureBotAI/CommunityMech/issues/2544
- https://github.com/CultureBotAI/CommunityMech/issues/2566
tags:
- pr-2054
- append-only
- author-remediation
- s1-proof-boundary
- complete-local-input-provenance
```
