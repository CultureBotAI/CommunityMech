# Current-main refresh of the Corynebacterium–Shewanella succinate review

- Review: 20261106T154646Z-corynebacterium-shewanella-current-main
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-11-06T15:31:42.952400Z
- Finished UTC: 2026-11-06T15:46:46.171211Z
- Reviewer: codex (self_review)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

The added MR-1 reusable-taxon link is supported at the indexed primary publisher source tier and by current NCBI strain ancestry. All three original findings remain open: categorical roles, non-graph causal wording, and GTDB provenance. Seven snippets match the fresh abstract. Full Methods, Results, figures and authenticated supplements remain unavailable; the refresh remains partial. No canonical record was edited.

## Scope And Provenance

Current maintained 000294 record, its sole main delta, fresh abstract/indexed publisher sections, current MR-1 reference scope, authorities, local checks and exact predecessor lineage. Full main/SI unavailable.

Selection: Only stale CommunityMech:000294 in PR #2058; other records and grouped findings are not scientifically superseded.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 342358f024aafa1f88b1e9d1f3df172a431a2aeb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000294 | kb/communities/Corynebacterium_glutamicum_Shewanella_oneidensis_Succinic_Acid_Coculture.yaml | maintained | Corynebacterium glutamicum + Shewanella oneidensis Succinic-acid Co-culture |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000294 | Current command exit 0; stdout/stderr pinned. |
| strict | passed | True | CommunityMech:000294 | Current command exit 0; stdout/stderr pinned. |
| terms | passed | True | CommunityMech:000294 | Current command exit 0; stdout/stderr pinned. |
| references | passed | True | CommunityMech:000294 | Current command exit 0; stdout/stderr pinned. |
| gtdb | passed | True | CommunityMech:000294 | Current command exit 0; stdout/stderr pinned. |
| gtdb-domain | passed | True | CommunityMech:000294 | Current command exit 0; stdout/stderr pinned. |
| history | passed | True | CommunityMech:000294 | Current command exit 0; stdout/stderr pinned. |
| original-review-validate | passed | True | CommunityMech:000294 | Current command exit 0; stdout/stderr pinned. |
| audit-network | failed | False | CommunityMech:000294 | Current full-corpus diagnostic retains 48 warnings across 17 of 510 records and zero errors; exit 1 is preserved. |
| check-network-quality | failed | False | CommunityMech:000294 | Current full-corpus diagnostic retains 48 warnings across 17 of 510 records and zero errors; exit 1 is preserved. |

## Scientific And Domain Assessments

### current identity and link

identity: supported. Targets: CommunityMech:000294.

The added MR-1 link is supported within explicit source limits.

Current species 1718 and 70863 remain appropriate. Indexed primary Establishment text names ATCC 13032 and MR-1, and live NCBI places strain 211586 beneath species 70863. common_taxon 000001 therefore refers to the matching stock. K1 remains an ldhA-deleted derivative; neither this linkage nor other-study MR-1 gene annotations assign every assay to K1 or establish the focal mechanism. No catalogue growth protocol is imported.

### roles

scope: concern. Targets: CommunityMech:000294.

The original categorical-role finding remains open.

PRIMARY_PRODUCER means autotrophy, not industrial succinate production. Accessible focal evidence does not establish ELECTROGEN's solid extracellular acceptor or ELECTRON_DONOR's donation direction. Optional roles may be omitted while keeping source-qualified electroactivity; no substitute role is required.

### non graph

evidence: concern. Targets: CommunityMech:000294.

The original prose-scope finding remains open.

Restore the source's not-markedly qualifier for glucose consumption, identify flux redistribution as transcript-based interpretation, and qualify the Shewanella transfer/redox note. Measured production gains remain valid at their separate comparison scopes.

### node 0

graph: supported. Targets: CommunityMech:000294.

Retain Riboflavin-Supplemented Coculture Response.

ecological_interactions[0]: Community-level externally supplied 0.1 mM riboflavin response; both species participate. SUPPORT/IN_VITRO concerns the additive intervention, not endogenous mediator secretion or directed transfer. Exact evidence selector/hashes are in the seven-excerpt audit; PMID:42203120 abstract is the inspected source.

### edge 0 0

graph: supported. Targets: CommunityMech:000294.

Retain the explicitly qualified causal arrow.

ecological_interactions[0].downstream[0] from Riboflavin-Supplemented Coculture Response to Corynebacterium Coculture Transcript Response: HYPOTHESIZED - altered coculture redox conditions could contribute to the Corynebacterium transcript response. Additive screening and the transcriptomic interpretation support this candidate link, but the accessible abstract does not selectively establish riboflavin-dependent electron transfer as its cause. Accessible abstract does not supply selective blockade, rescue or direct flux proving this mediation.

### node 1

graph: supported. Targets: CommunityMech:000294.

Retain Corynebacterium Coculture Transcript Response.

ecological_interactions[1]: Source-only PAIRWISE C. glutamicum transcript response; PARTIAL/IN_VITRO supports interpretation without direct carbon/electron flux. No recipient, obligatory syntrophy or unreported K1 assay assignment is added. Exact evidence selector/hashes are in the seven-excerpt audit; PMID:42203120 abstract is the inspected source.

### edge 1 0

graph: supported. Targets: CommunityMech:000294.

Retain the explicitly qualified causal arrow.

ecological_interactions[1].downstream[0] from Corynebacterium Coculture Transcript Response to Enhanced Succinic Acid Production: PARTIAL - the transcript-based interpretation is consistent with metabolic changes contributing to increased succinic acid yield. Positive coculture, riboflavin and ldhA-deletion outcomes support the production strategy, but do not selectively establish this transcript response or inferred flux redistribution as the mediator of each yield comparison. Accessible abstract does not supply selective blockade, rescue or direct flux proving this mediation.

### node 2

graph: supported. Targets: CommunityMech:000294.

Retain Enhanced Succinic Acid Production.

ecological_interactions[2]: Community-level production outcome, both species: separate parent 0.169 g/g and 45.65% comparison from K1 0.686 g/g and up to 23.4%. SUPPORT/IN_VITRO concerns measured output, not a uniquely demonstrated electron-transfer pathway. Exact evidence selector/hashes are in the seven-excerpt audit; PMID:42203120 abstract is the inspected source.

### grounding

grounding: concern. Targets: CommunityMech:000294.

Current ontology identities and mapping results remain consistent; provenance wording still needs repair.

Focused term checks pass. C. glutamicum species exact-ID 0.99/159 and S. oneidensis name route 1.0/3 reproduce; exact stock candidates 196627 and 211586 remain separate. The full snapshot SHA is pinned, release/build remains unknown, and filesystem mtime is not a build date.

### cultivation and resources

completeness: unknown. Targets: CommunityMech:000294.

Production protocol and focal deposited data remain incompletely assessed.

Anaerobic glucose-associated production and external riboflavin are supported. Indexed 20 mL BHI seed preparation and 24 h transfer cannot supply production medium, temperature, pH, vessel, gas regimen or mode; indexed 36 h conclusion context is bounded. No complete main/SI or focal accession audit was possible. Reusable assembly/protein IDs are reference context, not focal experimental deposits.

### lineage context

provenance: supported. Targets: CommunityMech:000294.

Only the original single-record scientific findings receive new occurrences.

The existing c2s4 grouped linkage finding and its resolved Stage 5 disposition remain intact; only the 000294 link is checked here. Other grouped targets and issue states are not reassessed. The historic graph repair remains qualified; no old review, record, cache or append-only history was rewritten.

### checks and inputs

provenance: supported. Targets: CommunityMech:000294.

Current checks and every concrete author input are frozen.

Eight focused commands pass. An initial optional GTDB replay failed because the nested worktree could not discover kg-microbe; the documented explicit-directory replay then succeeded, and both receipts remain. Corpus diagnostics retain their actual warning exits. New inspection/candidate/post-save outputs are excluded from their own input set to avoid self-reference. Partial source access prevents complete scientific status.

### Literal review metrics

completeness: supported. Targets: CommunityMech:000294.

Completeness 80; raw validation quality 103, capped at 100.

Recomputed from current record: required-field/roles block 50, environment 5, three nodes 10, medium 10, node metabolites 5 = 80. Three node evidence items / three nodes = 1 average; 2 P2 and 1 P3, network COMPLETE, raw quality 103 capped 100. Literal scoring does not validate the disputed roles or remove access limits.

## Findings

### functional-roles: Align hard functional roles with their literal meanings

major / open / confirmed; issue key: cm-000294-functional-roles.

C. glutamicum is labeled PRIMARY_PRODUCER although available evidence establishes industrial succinate production, not autotrophy. S. oneidensis is labeled ELECTROGEN and ELECTRON_DONOR although the accessible focal source establishes an electroactive partner and proposes transfer, without identifying a solid acceptor or resolved donation direction. Other-study MR-1 capabilities cannot serve as measured focal-role evidence.

### non-graph-scope: Qualify transfer and flux prose consistently with the graph

major / open / confirmed; issue key: cm-000294-non-graph-scope.

description omits markedly from the glucose-consumption comparison and presents transcript-based carbon redistribution too directly. taxonomy[1].taxon_term.notes states contribution to interspecies electron transfer/redox coupling without the existing graph’s uncertainty. Accessible evidence supports positive production outcomes and transcript-based interpretation, not direct resolved carbon/electron flux.

### gtdb-provenance: Replace unsupported GTDB release/build wording

minor / open / confirmed; issue key: cm-000294-gtdb-provenance.

Both mapping_source fields claim latest release and a build date that the local file mtime does not establish. The current species mappings themselves reproduce, including the documented Shewanella name fallback.

## Recommended Actions And Acceptance Checks

### repair-roles

Repair unsupported categorical member functions without inventing replacement roles.

- Remove or withhold PRIMARY_PRODUCER unless focal evidence establishes autotrophy consistent with the native definition. Keep the source-supported succinate-producing description; anaplerotic carboxylation or product production alone is not proof of autotrophy.
- For ELECTROGEN, require source-local evidence of transfer to a solid extracellular acceptor; for ELECTRON_DONOR, require local donation direction or retain only an explicitly proposed transfer description. Do not infer focal mechanism from other-study Mtr annotations, external riboflavin or yield gains.
- Retain S. oneidensis as an electroactive partner. Optional functional_role can be omitted; do not automatically substitute CROSS_FEEDER, SYNTROPHIC_PARTNER or a recipient role. Do not claim that MR-1 universally lacks electron-transfer capability.
- If optional ATCC 13032/MR-1 identity details are added, cite the exact indexed source tier and verified local stock labels, keeping K1 as a source-reported engineered derivative. No automatic genotype/assay reassignment or species-mapping replacement.

### qualify-prose

Bring non-graph wording into line with the measured outcomes and qualified causal graph.

- Restore the source qualifier that glucose consumption was not markedly altered; do not equate this with identical consumption or independently tested equivalence.
- Attribute electron-transport reinforcement and reductive-TCA redistribution to transcript-based metabolic interpretation. Describe Shewanella-to-Corynebacterium transfer/redox coupling as proposed or unresolved unless direct focal evidence is obtained.
- Preserve separate 0.169 g/g/45.65% parent comparison, externally supplied 0.1 mM riboflavin response, and K1 0.686 g/g/up-to 23.4% comparison with abolished lactate after ldhA deletion. Do not assign every transcript or additive assay to K1.
- Retain all three untyped nodes and the existing HYPOTHESIZED/PARTIAL arrows, including source-only PAIRWISE node 1. No mediator secretion, thermodynamic syntrophy, obligatory cooperation or causal mediation is added without source support.
- Keep indexed seed BHI details separate from production conditions and maintain the full-Methods/SI access limitation. Any 36 h detail remains indexed Conclusion context until full experimental scope is checked; do not merge the conflicting Highlight attribution of 45.65% with the Abstract.

### repair-gtdb

Make the two mapping provenance strings reproducible.

- Retain C. glutamicum 1718 exact-ID 0.99/159 and S. oneidensis 70863 name-route 1.0/3, including the explicit lack of an exact species 70863 crosswalk row.
- Record actual snapshot SHA256 761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd and lookup route. Label filesystem mtime only as mtime; leave GTDB release/build unknown unless independently verified.
- Keep optional ATCC 13032 exact 1.0/15 and MR-1 exact 1.0/3 candidates separate from species aggregates and the engineered K1 designation. Mapping genome counts are not study abundance.

### validate-future-curation

Validate separately authorized repairs and retain the review evidence.

- After authorized edits, attach exact claim-local evidence, update history and run schema, strict, terms, explained references, GTDB, domain and history checks, then just gen-html and just check-docs-current. This review does not edit canonical records, caches, history or generated pages.
- Preserve all original inspections, preliminary/final support and public access failures. Recovered full main/SI should receive a distinct source review before adding production conditions, dataset accessions or stronger mechanisms. No paid retrieval, author contact, external issue closure or unrelated record edit follows from this bundle.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | kb/communities/Corynebacterium_glutamicum_Shewanella_oneidensis_Succinic_Acid_Coculture.yaml; Whole current record | supports | Two species, three untyped nodes and two qualified arrows; new taxonomy[1].common_taxon plus its history entry. |
| abstract | .temp/pr2058/294-author/pmid42203120.json; PMID:42203120 / DOI:10.1016/j.biortech.2026.134987, complete abstract | supports | Reported production improvements and externally added riboflavin; transcript-based interpretation is distinct from demonstrated flux or donation direction. |
| indexed | .temp/pr2058/294-author/web-indexed-primary-sections.json; ScienceDirect S0960852426010692, Cell cultivation; Establishment and functional validation; Conclusion | supports | Indexed primary sections identify ATCC 13032 and MR-1 as the constructed pair; seed and conclusion snippets are truncated context, not complete Methods. |
| schema | src/communitymech/schema/communitymech.yaml; FunctionalRoleEnum; TaxonomicComposition.common_taxon; ecological_state | supports | Roles retain literal meanings, common_taxon shares organism reference annotations, and ecological_state is optional. |
| taxonomy | .temp/pr2058/294-author/ncbi-taxonomy.xml; Taxa 1718, 70863, 196627 and 211586 | supports | Current NCBI verifies species and exact parent-stock strains; MR-1 is a strain under S. oneidensis 70863. |
| reusable | kb/taxa/Shewanella_oneidensis_MR1.yaml; Identity and all five gene annotation blocks | supports | The referenced MR-1 record includes other-study electrochemical, bioleaching and computational annotations. None is focal evidence for succinate-coculture electron direction, a solid acceptor or K1 assay identity. |
| gtdb | .temp/pr2058/294-author/gtdb-replay-explicit.stdout; Current community-mode replay with explicit kg-microbe location | supports | Species mappings reproduce: C. glutamicum 0.99/159; S. oneidensis name fallback 1.0/3. Snapshot identity and mtime do not establish a release or build date. |
| gtdb-rows | .temp/pr2058/294-author/gtdb-exact-rows.json; Whole snapshot row scan; exact IDs and candidate stock rows | supports | No exact 70863 row in this snapshot; 1718 is exact, 196627 gives 1.0/15 and 211586 gives 1.0/3. These counts are crosswalk support, not study abundance. |
| snippets | .temp/pr2058/294-author/snippet-audit.json; All seven canonical excerpt selectors and hashes | supports | All seven match the fresh abstract after Unicode/whitespace normalization; exact text match does not establish causal entailment. |
| delta | .temp/pr2058/294-author/main-record-diff.txt; Frozen e117e3d to main 5086593a record diff | supports | The only community additions are the common_taxon link and its history event; no measured outcome or graph changed. |
| lineage | reviews/structured/20261025T161500Z-c2s5-remediation-verification/review.yaml; c2s4-shewanella-common-taxon-linkage-gap | supports | The grouped historical resolved disposition is context only. This refresh confirms only 000294 linkage and does not supersede 000288 or the reusable-record target. |
| access | .temp/pr2058/294-author/elsevier.xml; Anonymous public Elsevier response | supports | Only coredata was returned; direct publisher retrieval was an access-error page. No full Methods, figures, tables, authenticated SI or complete bibliography was inspected. |
| checks | .temp/pr2058/294-author/focused-checks.json; Eight current focused commands | supports | All eight commands returned 0; the original bundle validation is a native contract check, not fresh scientific approval. |
| network | .temp/pr2058/294-author/network-inputs.json; Root's shared read-only current corpus diagnostic receipts | supports | Actual corpus diagnostic outputs are pinned separately; warnings remain contextual and are not hidden by a passing focused record gate. |

## Limits And Additional Notes

- Only the complete fresh abstract and bounded indexed primary sections were available. Direct publisher retrieval failed and the anonymous API supplied coredata; no full Methods, Results, figures, tables, authenticated SI or full bibliography was inspected.
- The stock link is supported at indexed source tier. K1 assay assignment, directed electron transfer, solid-acceptor evidence, direct flux and selective mediation remain unresolved. Other-study reusable annotations are not focal proof.
- Seed preparation is distinct from production; indexed conclusion timing is not a recovered full protocol. A historical Highlight/Abstract attribution discrepancy is not silently harmonized, and missing accessible data is not global absence.
- Fresh whole-snapshot GTDB replay verifies mapping results but not an upstream release/build. Optional fields, including ecological_state, are not made mandatory by a rubric score.
- Only 000294 is scientifically refreshed. Grouped linkage findings retain their full original target scopes and dispositions. Root and independent reviewers own issue-state checks and final adversarial approval.
- Refresh for stale-review issue #2569. Original bundle remains immutable; historical local-source provenance limitation is separately tracked by #2570.
- All local input bytes used by this author are included through native --input, including public source bodies/receipts, initial inspection, mapping copy, checks, guidance and this frozen JSON builder. No YAML writer is introduced.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261106T154646Z-corynebacterium-shewanella-current-main
kind: record
repository: CultureBotAI/CommunityMech
title: Current-main refresh of the Corynebacterium–Shewanella succinate review
started_at: '2026-11-06T15:31:42.952400Z'
finished_at: '2026-11-06T15:46:46.171211Z'
reviewer:
  identity: codex
  kind: agent
  independence: self_review
  independence_basis: Author of this refresh; another agent performs the independent
    adversarial pass. No self-approval is claimed.
skill: review-yaml-record
completion: partial
verdict: needs_curation
scientific_review: false
summary: 'The added MR-1 reusable-taxon link is supported at the indexed primary publisher
  source tier and by current NCBI strain ancestry. All three original findings remain
  open: categorical roles, non-graph causal wording, and GTDB provenance. Seven snippets
  match the fresh abstract. Full Methods, Results, figures and authenticated supplements
  remain unavailable; the refresh remains partial. No canonical record was edited.'
source:
  git_revision: 342358f024aafa1f88b1e9d1f3df172a431a2aeb
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: d2f94c87b82f59663bc2b0c91ac04a245e56fab52d8c11e6bddb559eb9237c84
    role: context
  - path: .claude/skills/ground-taxa-gtdb/SKILL.md
    sha256: 0f7f4423eca28dd0605784d0a01b0886618d0d0f8f1739acb1aae7702e4560a1
    role: context
  - path: .claude/skills/review-communities/reference/execution-protocol.md
    sha256: 0d4448074611c020c54b6b20c478b24e2cf2a195f7fc4f7dbcfac19134f731c4
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
  - path: .temp/pr2058/294-author/NCBI2GTDB.tsv.gz
    sha256: 761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd
    role: context
  - path: .temp/pr2058/294-author/elsevier.xml
    sha256: 476b8cf3bf5ee82911add480709a3e140e1e0439a1173593fe3b559457f8a245
    role: context
  - path: .temp/pr2058/294-author/elsevier.xml-receipt.json
    sha256: 9f77d4ed8cfea686bc57b41d2f6be3f8dbce0dc05cc6f8676a63892df069f037
    role: context
  - path: .temp/pr2058/294-author/focused-checks.json
    sha256: ebd167d9a7a13c948783c0243061be28aa465150dc4251584b51d2005f5e4509
    role: context
  - path: .temp/pr2058/294-author/full-lint.json
    sha256: a9a96aa779e3ca6a05fa896d1f822e72ab45e5c9ec1735a76aacef50782543c3
    role: context
  - path: .temp/pr2058/294-author/full-lint.stderr
    sha256: 8c8cb4b9789347a1b513903bfe64c3a3b8b2caeeb43926885749f6443d26c6f5
    role: context
  - path: .temp/pr2058/294-author/full-lint.stdout
    sha256: 1cffccf768da50ca84db43e973c69c47f795b57101ebfc1825d52472c790ab4d
    role: context
  - path: .temp/pr2058/294-author/gtdb-copy.json
    sha256: 722c81cf703f701a387db12fd1d73fb06a261c7e1d3419a170ec58a423399c21
    role: context
  - path: .temp/pr2058/294-author/gtdb-domain.stderr
    sha256: e3d1bbe61469528284f875601424676618228bda958fb0ce8360e0f4d161ab89
    role: context
  - path: .temp/pr2058/294-author/gtdb-domain.stdout
    sha256: ede937293c42cad366f434dce49a485a9a0c56fe86620b52ca243ad10e09ecae
    role: context
  - path: .temp/pr2058/294-author/gtdb-exact-rows.json
    sha256: 28616cf564356ebd8c4f17548098f41afd5e9fdbe5c7cddbc159fc37fb316879
    role: context
  - path: .temp/pr2058/294-author/gtdb-replay-explicit.json
    sha256: 5505a8a4e0cb7ffbdd9a14180c0a1699af930c6891f29053c278cdb6b4ad28b5
    role: context
  - path: .temp/pr2058/294-author/gtdb-replay-explicit.stderr
    sha256: 76dca8b7edb2ec8256ef6ef5d0999a6e136718130a4f3258f75161c051b9c92b
    role: context
  - path: .temp/pr2058/294-author/gtdb-replay-explicit.stdout
    sha256: f1f33e657f7d61a169f9aba4dd0f0ba604a26186660bd8b278f207ba380c2c20
    role: context
  - path: .temp/pr2058/294-author/gtdb-replay.json
    sha256: 660189dca8571f1499d9b5c5a1d4dce1ddf1e26ad0634d421aecbc85f95dd4e6
    role: context
  - path: .temp/pr2058/294-author/gtdb-replay.stderr
    sha256: 822372df365288a707c73bb07d612219bf9ac0fd32f0591434a494fa50f788aa
    role: context
  - path: .temp/pr2058/294-author/gtdb-replay.stdout
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2058/294-author/gtdb.stderr
    sha256: 17de24e3af9806a6345aec3cb6e4cf810a3c9f33387e2d37784f28faf42cf0a4
    role: context
  - path: .temp/pr2058/294-author/gtdb.stdout
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2058/294-author/history.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2058/294-author/history.stdout
    sha256: de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
    role: context
  - path: .temp/pr2058/294-author/initial-inspect-receipt.json
    sha256: 59ae68017a87469675bbbfb7ae9c3983e5da2f6264bef662cad342a4d32de6ec
    role: context
  - path: .temp/pr2058/294-author/initial-inspect.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2058/294-author/initial-inspect.stdout
    sha256: a293b9edd4cd60f7fa98369aac5f00d0c9389ca8c73790edc1e8a39df40f4551
    role: context
  - path: .temp/pr2058/294-author/input-paths.json
    sha256: 5dedcd5bdaee4426b608e9993ea43f1ea880bc148b2b5d5bbffa7c74ad626c19
    role: context
  - path: .temp/pr2058/294-author/main-record-diff.txt
    sha256: 812302bbd7ca74fafe13c692c41bb93faf1798741423ec8a9b15bc4c074f9b6f
    role: context
  - path: .temp/pr2058/294-author/ncbi-taxonomy.parsed.json
    sha256: e27bfaa9203e520d98d113d45577240143ff160e7faef330c982d0218dba4498
    role: context
  - path: .temp/pr2058/294-author/ncbi-taxonomy.receipt.json
    sha256: f4ca246f6e19a68f764f8714c03e3dbb4a7551ac9300170d89a45875886bc947
    role: context
  - path: .temp/pr2058/294-author/ncbi-taxonomy.xml
    sha256: bc34a480d5c125ee49dd6d2636372846a7944df08e8bdec7753ed8dfa780f912
    role: context
  - path: .temp/pr2058/294-author/network-inputs.json
    sha256: 9eb11ce4cd9c79670eeb6fb666b1c3371ea37bdec124a5134368eac2ce25fed1
    role: context
  - path: .temp/pr2058/294-author/original-review-validate.stderr
    sha256: e2cf5a8ee56373cb7afeb23be8ac2a30d67f13afa55bb51424877fc908e2a25f
    role: context
  - path: .temp/pr2058/294-author/original-review-validate.stdout
    sha256: b42ee0197bdb886694684431f9da0d2fba4020263ed572ff756b9eaf0b042ba6
    role: context
  - path: .temp/pr2058/294-author/original-review.json
    sha256: 449a95cd6e0339377e05c7a4148f22d5a9201e4a4cda17429b943f280e4bd334
    role: context
  - path: .temp/pr2058/294-author/pmid42203120-receipt.json
    sha256: faf01649d8798661796b33eaeefd8d135bf4c664491af22506d17716b8a5df10
    role: context
  - path: .temp/pr2058/294-author/pmid42203120.json
    sha256: 80e2ca76db66f32c633993a93f3c6c87392ea82281f16a5df5aa0f1a5543a68b
    role: context
  - path: .temp/pr2058/294-author/publisher-visible.txt
    sha256: 49bb4944ff84d7bdb59cd07c790e780b0f36a9da4448bb6c5fc3296dcca720e1
    role: context
  - path: .temp/pr2058/294-author/publisher.html
    sha256: c4f8ade66833834b34bf71925f881eccef38533abaa0e15b8861be5dd0ffd913
    role: context
  - path: .temp/pr2058/294-author/publisher.html-receipt.json
    sha256: 6e4ee6a92fa63e0d198355e099f7af15cbf4280bcc035167b69fe11a939e7207
    role: context
  - path: .temp/pr2058/294-author/references.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2058/294-author/references.stdout
    sha256: 5eb4c68204cfa51aa5392a3bfe478d1085dbbb4942681e1681d9e83cffaabcc3
    role: context
  - path: .temp/pr2058/294-author/snippet-audit.json
    sha256: 808ce8a14c99c220b57d132f61e43d9234362e77e100b69c1f3d0da8d23800cb
    role: context
  - path: .temp/pr2058/294-author/strict.stderr
    sha256: d9d593341380f2f6910904a2b38c4073b4302aa412d65cbdd80d0fec7bc10c5a
    role: context
  - path: .temp/pr2058/294-author/strict.stdout
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2058/294-author/strict.tsv
    sha256: b184ed5450b968070bb6c75648407e388f41a1eaf7017890723cf560999fc3f7
    role: context
  - path: .temp/pr2058/294-author/targets.json
    sha256: 7521db5fcb0aefa8c43136e47194a577297307923d6d9800e70ab445e94a8a41
    role: context
  - path: .temp/pr2058/294-author/terms.stderr
    sha256: 2801ae4e95e6f943320b8772ea10c224846570764ae0fd900a8ebe28ae696a45
    role: context
  - path: .temp/pr2058/294-author/terms.stdout
    sha256: 23acda1c1d3194d12bc947d897d07de83f4a076a9d93c135148885108530e018
    role: context
  - path: .temp/pr2058/294-author/validate.stderr
    sha256: 2e63180b346a04796c72ad437f5f6366619d6bb3bc6d69b846c39763e6ac2142
    role: context
  - path: .temp/pr2058/294-author/validate.stdout
    sha256: de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
    role: context
  - path: .temp/pr2058/294-author/web-indexed-primary-sections.json
    sha256: 833ae81ce052f11881ea0c0be634f03a2956808a87e36996a3a68a92d9e827b3
    role: context
  - path: .temp/pr2058/294-author/web-primary-search.json
    sha256: aeed787309af1f6df8615042e2e8cd9a0a7328b44bcce8dd9614c475c5659934
    role: context
  - path: .temp/pr2058/294-author/web-source-search-empty.json
    sha256: 1048ddaf93c0dfa7b1304db3ffef722f4a37db0018ad2c63d0062118c5d92b42
    role: context
  - path: .temp/pr2058/root-checks/audit-network.stderr
    sha256: a71fb29e950f3eaf0eb2b834a43c59d4a1b6aa85a2a89473ae99b0e408a27a36
    role: context
  - path: .temp/pr2058/root-checks/audit-network.stdout
    sha256: 1f337893714a80173f5b305ba0c11da1d8a3caf53f1060bd5acf2aa42b40aece
    role: context
  - path: .temp/pr2058/root-checks/check-network-quality.stderr
    sha256: e060873ec46d56a6fddbc2fe78b0d2f1438639923dd9f410686090ae4efa3aa3
    role: context
  - path: .temp/pr2058/root-checks/check-network-quality.stdout
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2058/root-checks/network-checks.json
    sha256: c3a7f4637e3e4c4c6de73d08239c22a5ae5095444ee077b8173449d02eb32df8
    role: context
  - path: .temp/pr2058/staleness.json
    sha256: 6022366d4a7d842168c10d2f0ba8f8601411ae9f989abea20a28e54ebd28e580
    role: context
  - path: AGENTS.md
    sha256: 7c35deb79ce874239f1080c2f575756ff47d1985483030878eaeb07df02d7529
    role: context
  - path: conf/record_review.yaml
    sha256: c4ad25505a87a040c57eb93f1ee9673a09389a474c6d4e1136781456ff190fc8
    role: context
  - path: conf/reference_validator.yaml
    sha256: 5cd4781c7e15b7c5472f0b008e41764842cc023a7ba99f4273298f421be36652
    role: context
  - path: docs/record-review-profile.md
    sha256: 285f79747999f83edbe63e5efde349a5cc063e9e486ce1a748b47b76c6631f31
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: history/README.md
    sha256: 86c0347d77402bcecdec466b01974ad53beddb9cf1bd17cf085674970542a101
    role: context
  - path: history/records/Corynebacterium_glutamicum_Shewanella_oneidensis_Succinic_Acid_Coculture/2026-10-06T022828Z-codex-9a496b.yaml
    sha256: 86d4eea2bfbd21496db515aa5aaf3f82441dddf68bfcff4a18fa945f2f2376a2
    role: context
  - path: history/records/Corynebacterium_glutamicum_Shewanella_oneidensis_Succinic_Acid_Coculture/2026-10-25T151200Z-antigravity-2073.yaml
    sha256: c5c9accc0eff57c6cfcc2540daf0b6c08784f54932eb8d7500847b379317ca0e
    role: context
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: kb/communities/Corynebacterium_glutamicum_Shewanella_oneidensis_Succinic_Acid_Coculture.yaml
    sha256: 12ec7d94161d772e79598564ae50e6f322c9cfd82e889a2fd5e0fbcde687f8f6
    role: target
  - path: kb/taxa/Shewanella_oneidensis_MR1.yaml
    sha256: 372e95f725bca699a349a6aaccf39a0bb781e1c19f4aa491d72f18a704037b69
    role: context
  - path: references_cache/PMID_42203120.md
    sha256: 7b567b431f735bc1384c900944b5828baf891f73e51c02e45443529afd4da156
    role: context
  - path: reports/causal_graph_review/adversarial-review-20261005-batch24.yaml
    sha256: e85c631d1b0762a661c513d1c1ca07407d0c97351ae631a7b8207c87d8eaeb8c
    role: context
  - path: reports/causal_graph_review/decisions/20261005-three-records-batch24.yaml
    sha256: c643f50b402cf23b8e756e43adfdfca7d6a93e64033a5d0accf0169f7ca97a63
    role: context
  - path: reviews/structured/20261021T101100Z-stage4-frozen-cohort-review/review.md
    sha256: e432615b147787c8d009d96d2f11e5b78a45927bf9c69e45ec0d31123d1fc2e9
    role: context
  - path: reviews/structured/20261021T101100Z-stage4-frozen-cohort-review/review.yaml
    sha256: 37d089fd55c077793dd20d868b50c47cb1cceab6dae6a82887cc938bee05fa6d
    role: context
  - path: reviews/structured/20261022T011317Z-corynebacterium-shewanella-record-review/review.md
    sha256: d27902ea6b1f406c7a0db4ed900322d3708bf65216717929e6e5902d87b13c5b
    role: context
  - path: reviews/structured/20261022T011317Z-corynebacterium-shewanella-record-review/review.yaml
    sha256: cf3bac3bd4b4bad051151a7ca936e45af1d85d7b2ad5d46e8d79567be1e01e51
    role: context
  - path: reviews/structured/20261025T113600Z-c2s4-frozen-cohort-review/review.yaml
    sha256: 702d202105025d44fc469e588a43967388443aad84a355bc80ea45ebab36338a
    role: context
  - path: reviews/structured/20261025T161500Z-c2s5-remediation-verification/review.yaml
    sha256: c8b7bd9b8e462081a734db496e8314848c4474a56deadbec891cf4af6f9ea644
    role: context
  - path: reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-04/revision-0001/frozen_inventory_metrics.tsv
    sha256: d5a47bbcc3745a489ff507680aa7360a6a65ce070ce4ec88f886b70128791313
    role: context
  - path: reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-04/revision-0001/review_report.md
    sha256: 4e7781aa8cdfc4bb42d896ebe75920719d9dcade92ffc4a0ae07af7481cb37b3
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/adhoc/pr2054_180_input_provenance.py
    sha256: 47f586e75deb2103f7f0787376c17eb0b5c98663b22dac8862f393f9c8f14a2a
    role: context
  - path: scripts/adhoc/pr2058_294_refresh.py
    sha256: 9736f264aaf98ad1b14310160e25f293a3ba5e838a3b889338a295db7e92523b
    role: context
  - path: scripts/gtdb_ground.py
    sha256: 0fc1ba926a56e5be85cdf064db0cf56452aeeee93f15b0ced98e8f11b5296175
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: src/communitymech/network/auditor.py
    sha256: fe32aa2eddf9e09c153c47576f943bf08a6019f650bf2575e3ddc8e14675049b
    role: context
  - path: src/communitymech/schema/communitymech.yaml
    sha256: 7355e14f0f17c5d3b875abd33af6474ddc1aad08cc3305313686fede337e259a
    role: context
  - path: src/communitymech/schema/history.yaml
    sha256: b01b06f1b9a37db205c26c31ec0fd910690848507c7e1bfb73b424ac0829c52d
    role: context
  - path: src/communitymech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
targets:
- target_id: CommunityMech:000294
  path: kb/communities/Corynebacterium_glutamicum_Shewanella_oneidensis_Succinic_Acid_Coculture.yaml
  label: Corynebacterium glutamicum + Shewanella oneidensis Succinic-acid Co-culture
  kind: maintained
  record_class: MicrobialCommunity
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Corynebacterium_glutamicum_Shewanella_oneidensis_Succinic_Acid_Coculture.yaml
    role: canonical_record
scope:
  description: Current maintained 000294 record, its sole main delta, fresh abstract/indexed
    publisher sections, current MR-1 reference scope, authorities, local checks and
    exact predecessor lineage. Full main/SI unavailable.
  selection: 'Only stale CommunityMech:000294 in PR #2058; other records and grouped
    findings are not scientifically superseded.'
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000294
checks:
- check_id: validate
  name: validate
  status: passed
  required: true
  summary: Current command exit 0; stdout/stderr pinned.
  target_ids:
  - CommunityMech:000294
  command: just --no-dotenv validate kb/communities/Corynebacterium_glutamicum_Shewanella_oneidensis_Succinic_Acid_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - checks
  scope_note: Current focused command; no historical output replayed as a fresh run.
- check_id: strict
  name: strict
  status: passed
  required: true
  summary: Current command exit 0; stdout/stderr pinned.
  target_ids:
  - CommunityMech:000294
  command: just --no-dotenv validate-strict kb/communities/Corynebacterium_glutamicum_Shewanella_oneidensis_Succinic_Acid_Coculture.yaml
    --out .temp/pr2058/294-author/strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - checks
  scope_note: Current focused command; no historical output replayed as a fresh run.
- check_id: terms
  name: terms
  status: passed
  required: true
  summary: Current command exit 0; stdout/stderr pinned.
  target_ids:
  - CommunityMech:000294
  command: just --no-dotenv validate-terms kb/communities/Corynebacterium_glutamicum_Shewanella_oneidensis_Succinic_Acid_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - checks
  scope_note: Current focused command; no historical output replayed as a fresh run.
- check_id: references
  name: references
  status: passed
  required: true
  summary: Current command exit 0; stdout/stderr pinned.
  target_ids:
  - CommunityMech:000294
  command: just --no-dotenv validate-references-explained kb/communities/Corynebacterium_glutamicum_Shewanella_oneidensis_Succinic_Acid_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - checks
  scope_note: Current focused command; no historical output replayed as a fresh run.
- check_id: gtdb
  name: gtdb
  status: passed
  required: true
  summary: Current command exit 0; stdout/stderr pinned.
  target_ids:
  - CommunityMech:000294
  command: just --no-dotenv validate-gtdb kb/communities/Corynebacterium_glutamicum_Shewanella_oneidensis_Succinic_Acid_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - checks
  scope_note: Current focused command; no historical output replayed as a fresh run.
- check_id: gtdb-domain
  name: gtdb-domain
  status: passed
  required: true
  summary: Current command exit 0; stdout/stderr pinned.
  target_ids:
  - CommunityMech:000294
  command: just --no-dotenv validate-gtdb-domain kb/communities/Corynebacterium_glutamicum_Shewanella_oneidensis_Succinic_Acid_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - checks
  scope_note: Current focused command; no historical output replayed as a fresh run.
- check_id: history
  name: history
  status: passed
  required: true
  summary: Current command exit 0; stdout/stderr pinned.
  target_ids:
  - CommunityMech:000294
  command: just --no-dotenv validate-history history/records/Corynebacterium_glutamicum_Shewanella_oneidensis_Succinic_Acid_Coculture
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - checks
  scope_note: Current focused command; no historical output replayed as a fresh run.
- check_id: original-review-validate
  name: original-review-validate
  status: passed
  required: true
  summary: Current command exit 0; stdout/stderr pinned.
  target_ids:
  - CommunityMech:000294
  command: uv run python scripts/record_review.py validate reviews/structured/20261022T011317Z-corynebacterium-shewanella-record-review/review.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - checks
  scope_note: Current focused command; no historical output replayed as a fresh run.
- check_id: audit-network
  name: audit-network
  status: failed
  required: false
  summary: Current full-corpus diagnostic retains 48 warnings across 17 of 510 records
    and zero errors; exit 1 is preserved.
  target_ids:
  - CommunityMech:000294
  command: just --no-dotenv audit-network
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - network
  scope_note: Shared current full-corpus diagnostic executed by root; not a focal-record
    failure or a scientific review.
- check_id: check-network-quality
  name: check-network-quality
  status: failed
  required: false
  summary: Current full-corpus diagnostic retains 48 warnings across 17 of 510 records
    and zero errors; exit 1 is preserved.
  target_ids:
  - CommunityMech:000294
  command: just --no-dotenv check-network-quality
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - network
  scope_note: Shared current full-corpus diagnostic executed by root; not a focal-record
    failure or a scientific review.
evidence:
- evidence_id: record
  kind: record_content
  reference: kb/communities/Corynebacterium_glutamicum_Shewanella_oneidensis_Succinic_Acid_Coculture.yaml
  locator: Whole current record
  summary: Two species, three untyped nodes and two qualified arrows; new taxonomy[1].common_taxon
    plus its history entry.
  support: supports
  accessed_at: '2026-11-06T15:46:46.171211Z'
  snapshot_sha256: 12ec7d94161d772e79598564ae50e6f322c9cfd82e889a2fd5e0fbcde687f8f6
- evidence_id: abstract
  kind: primary_source
  reference: .temp/pr2058/294-author/pmid42203120.json
  locator: PMID:42203120 / DOI:10.1016/j.biortech.2026.134987, complete abstract
  summary: Reported production improvements and externally added riboflavin; transcript-based
    interpretation is distinct from demonstrated flux or donation direction.
  support: supports
  accessed_at: '2026-11-06T15:46:46.171211Z'
  snapshot_sha256: 80e2ca76db66f32c633993a93f3c6c87392ea82281f16a5df5aa0f1a5543a68b
- evidence_id: indexed
  kind: primary_source
  reference: .temp/pr2058/294-author/web-indexed-primary-sections.json
  locator: ScienceDirect S0960852426010692, Cell cultivation; Establishment and functional
    validation; Conclusion
  summary: Indexed primary sections identify ATCC 13032 and MR-1 as the constructed
    pair; seed and conclusion snippets are truncated context, not complete Methods.
  support: supports
  accessed_at: '2026-11-06T15:46:46.171211Z'
  snapshot_sha256: 833ae81ce052f11881ea0c0be634f03a2956808a87e36996a3a68a92d9e827b3
- evidence_id: schema
  kind: record_content
  reference: src/communitymech/schema/communitymech.yaml
  locator: FunctionalRoleEnum; TaxonomicComposition.common_taxon; ecological_state
  summary: Roles retain literal meanings, common_taxon shares organism reference annotations,
    and ecological_state is optional.
  support: supports
  accessed_at: '2026-11-06T15:46:46.171211Z'
  snapshot_sha256: 7355e14f0f17c5d3b875abd33af6474ddc1aad08cc3305313686fede337e259a
- evidence_id: taxonomy
  kind: authority
  reference: .temp/pr2058/294-author/ncbi-taxonomy.xml
  locator: Taxa 1718, 70863, 196627 and 211586
  summary: Current NCBI verifies species and exact parent-stock strains; MR-1 is a
    strain under S. oneidensis 70863.
  support: supports
  accessed_at: '2026-11-06T15:46:46.171211Z'
  snapshot_sha256: bc34a480d5c125ee49dd6d2636372846a7944df08e8bdec7753ed8dfa780f912
- evidence_id: reusable
  kind: record_content
  reference: kb/taxa/Shewanella_oneidensis_MR1.yaml
  locator: Identity and all five gene annotation blocks
  summary: The referenced MR-1 record includes other-study electrochemical, bioleaching
    and computational annotations. None is focal evidence for succinate-coculture
    electron direction, a solid acceptor or K1 assay identity.
  support: supports
  accessed_at: '2026-11-06T15:46:46.171211Z'
  snapshot_sha256: 372e95f725bca699a349a6aaccf39a0bb781e1c19f4aa491d72f18a704037b69
- evidence_id: gtdb
  kind: validation
  reference: .temp/pr2058/294-author/gtdb-replay-explicit.stdout
  locator: Current community-mode replay with explicit kg-microbe location
  summary: 'Species mappings reproduce: C. glutamicum 0.99/159; S. oneidensis name
    fallback 1.0/3. Snapshot identity and mtime do not establish a release or build
    date.'
  support: supports
  accessed_at: '2026-11-06T15:46:46.171211Z'
  snapshot_sha256: f1f33e657f7d61a169f9aba4dd0f0ba604a26186660bd8b278f207ba380c2c20
- evidence_id: gtdb-rows
  kind: validation
  reference: .temp/pr2058/294-author/gtdb-exact-rows.json
  locator: Whole snapshot row scan; exact IDs and candidate stock rows
  summary: No exact 70863 row in this snapshot; 1718 is exact, 196627 gives 1.0/15
    and 211586 gives 1.0/3. These counts are crosswalk support, not study abundance.
  support: supports
  accessed_at: '2026-11-06T15:46:46.171211Z'
  snapshot_sha256: 28616cf564356ebd8c4f17548098f41afd5e9fdbe5c7cddbc159fc37fb316879
- evidence_id: snippets
  kind: validation
  reference: .temp/pr2058/294-author/snippet-audit.json
  locator: All seven canonical excerpt selectors and hashes
  summary: All seven match the fresh abstract after Unicode/whitespace normalization;
    exact text match does not establish causal entailment.
  support: supports
  accessed_at: '2026-11-06T15:46:46.171211Z'
  snapshot_sha256: 808ce8a14c99c220b57d132f61e43d9234362e77e100b69c1f3d0da8d23800cb
- evidence_id: delta
  kind: validation
  reference: .temp/pr2058/294-author/main-record-diff.txt
  locator: Frozen e117e3d to main 5086593a record diff
  summary: The only community additions are the common_taxon link and its history
    event; no measured outcome or graph changed.
  support: supports
  accessed_at: '2026-11-06T15:46:46.171211Z'
  snapshot_sha256: 812302bbd7ca74fafe13c692c41bb93faf1798741423ec8a9b15bc4c074f9b6f
- evidence_id: lineage
  kind: prior_review
  reference: reviews/structured/20261025T161500Z-c2s5-remediation-verification/review.yaml
  locator: c2s4-shewanella-common-taxon-linkage-gap
  summary: The grouped historical resolved disposition is context only. This refresh
    confirms only 000294 linkage and does not supersede 000288 or the reusable-record
    target.
  support: supports
  accessed_at: '2026-11-06T15:46:46.171211Z'
  snapshot_sha256: c8b7bd9b8e462081a734db496e8314848c4474a56deadbec891cf4af6f9ea644
- evidence_id: access
  kind: primary_source
  reference: .temp/pr2058/294-author/elsevier.xml
  locator: Anonymous public Elsevier response
  summary: Only coredata was returned; direct publisher retrieval was an access-error
    page. No full Methods, figures, tables, authenticated SI or complete bibliography
    was inspected.
  support: supports
  accessed_at: '2026-11-06T15:46:46.171211Z'
  snapshot_sha256: 476b8cf3bf5ee82911add480709a3e140e1e0439a1173593fe3b559457f8a245
- evidence_id: checks
  kind: validation
  reference: .temp/pr2058/294-author/focused-checks.json
  locator: Eight current focused commands
  summary: All eight commands returned 0; the original bundle validation is a native
    contract check, not fresh scientific approval.
  support: supports
  accessed_at: '2026-11-06T15:46:46.171211Z'
  snapshot_sha256: ebd167d9a7a13c948783c0243061be28aa465150dc4251584b51d2005f5e4509
- evidence_id: network
  kind: validation
  reference: .temp/pr2058/294-author/network-inputs.json
  locator: Root's shared read-only current corpus diagnostic receipts
  summary: Actual corpus diagnostic outputs are pinned separately; warnings remain
    contextual and are not hidden by a passing focused record gate.
  support: supports
  accessed_at: '2026-11-06T15:46:46.171211Z'
  snapshot_sha256: 9eb11ce4cd9c79670eeb6fb666b1c3371ea37bdec124a5134368eac2ce25fed1
assessments:
- assessment_id: current-identity-and-link
  area: identity
  topic: current identity and link
  outcome: supported
  summary: The added MR-1 link is supported within explicit source limits.
  details: Current species 1718 and 70863 remain appropriate. Indexed primary Establishment
    text names ATCC 13032 and MR-1, and live NCBI places strain 211586 beneath species
    70863. common_taxon 000001 therefore refers to the matching stock. K1 remains
    an ldhA-deleted derivative; neither this linkage nor other-study MR-1 gene annotations
    assign every assay to K1 or establish the focal mechanism. No catalogue growth
    protocol is imported.
  target_ids:
  - CommunityMech:000294
  evidence_ids:
  - record
  - indexed
  - taxonomy
  - reusable
  - delta
  dimensions:
  - name: source_tier
    value: Fresh complete abstract; indexed primary sections; full main/SI unavailable
    definition: Actual reviewed primary-source scope
    evidence_ids:
    - abstract
    - indexed
    - access
  - name: strain_scope
    value: ATCC 13032 / MR-1 parent stocks; reported C. glutamicum K1 derivative
    definition: Indexed parent-stock identity remains separate from unresolved assay-specific
      derivative use
    evidence_ids:
    - indexed
    - taxonomy
  - name: community_scope
    value: ENGINEERED, SYNTHETIC laboratory coculture
    definition: Neither a natural assemblage nor a universal species interaction
    evidence_ids:
    - record
    - abstract
  - name: culture_context
    value: Anaerobic glucose-associated production; seed protocol is a separate indexed
      context
    definition: Do not extrapolate truncated seed conditions to the production assay
    evidence_ids:
    - abstract
    - indexed
- assessment_id: roles
  area: scope
  topic: roles
  outcome: concern
  summary: The original categorical-role finding remains open.
  details: PRIMARY_PRODUCER means autotrophy, not industrial succinate production.
    Accessible focal evidence does not establish ELECTROGEN's solid extracellular
    acceptor or ELECTRON_DONOR's donation direction. Optional roles may be omitted
    while keeping source-qualified electroactivity; no substitute role is required.
  target_ids:
  - CommunityMech:000294
  evidence_ids:
  - abstract
  - schema
  - reusable
- assessment_id: non-graph
  area: evidence
  topic: non graph
  outcome: concern
  summary: The original prose-scope finding remains open.
  details: Restore the source's not-markedly qualifier for glucose consumption, identify
    flux redistribution as transcript-based interpretation, and qualify the Shewanella
    transfer/redox note. Measured production gains remain valid at their separate
    comparison scopes.
  target_ids:
  - CommunityMech:000294
  evidence_ids:
  - abstract
  - record
  - indexed
- assessment_id: node-0
  area: graph
  topic: node 0
  outcome: supported
  summary: Retain Riboflavin-Supplemented Coculture Response.
  details: 'ecological_interactions[0]: Community-level externally supplied 0.1 mM
    riboflavin response; both species participate. SUPPORT/IN_VITRO concerns the additive
    intervention, not endogenous mediator secretion or directed transfer. Exact evidence
    selector/hashes are in the seven-excerpt audit; PMID:42203120 abstract is the
    inspected source.'
  target_ids:
  - CommunityMech:000294
  evidence_ids:
  - record
  - abstract
  - snippets
- assessment_id: edge-0-0
  area: graph
  topic: edge 0 0
  outcome: supported
  summary: Retain the explicitly qualified causal arrow.
  details: 'ecological_interactions[0].downstream[0] from Riboflavin-Supplemented
    Coculture Response to Corynebacterium Coculture Transcript Response: HYPOTHESIZED
    - altered coculture redox conditions could contribute to the Corynebacterium transcript
    response. Additive screening and the transcriptomic interpretation support this
    candidate link, but the accessible abstract does not selectively establish riboflavin-dependent
    electron transfer as its cause. Accessible abstract does not supply selective
    blockade, rescue or direct flux proving this mediation.'
  target_ids:
  - CommunityMech:000294
  evidence_ids:
  - record
  - abstract
- assessment_id: node-1
  area: graph
  topic: node 1
  outcome: supported
  summary: Retain Corynebacterium Coculture Transcript Response.
  details: 'ecological_interactions[1]: Source-only PAIRWISE C. glutamicum transcript
    response; PARTIAL/IN_VITRO supports interpretation without direct carbon/electron
    flux. No recipient, obligatory syntrophy or unreported K1 assay assignment is
    added. Exact evidence selector/hashes are in the seven-excerpt audit; PMID:42203120
    abstract is the inspected source.'
  target_ids:
  - CommunityMech:000294
  evidence_ids:
  - record
  - abstract
  - snippets
- assessment_id: edge-1-0
  area: graph
  topic: edge 1 0
  outcome: supported
  summary: Retain the explicitly qualified causal arrow.
  details: 'ecological_interactions[1].downstream[0] from Corynebacterium Coculture
    Transcript Response to Enhanced Succinic Acid Production: PARTIAL - the transcript-based
    interpretation is consistent with metabolic changes contributing to increased
    succinic acid yield. Positive coculture, riboflavin and ldhA-deletion outcomes
    support the production strategy, but do not selectively establish this transcript
    response or inferred flux redistribution as the mediator of each yield comparison.
    Accessible abstract does not supply selective blockade, rescue or direct flux
    proving this mediation.'
  target_ids:
  - CommunityMech:000294
  evidence_ids:
  - record
  - abstract
- assessment_id: node-2
  area: graph
  topic: node 2
  outcome: supported
  summary: Retain Enhanced Succinic Acid Production.
  details: 'ecological_interactions[2]: Community-level production outcome, both species:
    separate parent 0.169 g/g and 45.65% comparison from K1 0.686 g/g and up to 23.4%.
    SUPPORT/IN_VITRO concerns measured output, not a uniquely demonstrated electron-transfer
    pathway. Exact evidence selector/hashes are in the seven-excerpt audit; PMID:42203120
    abstract is the inspected source.'
  target_ids:
  - CommunityMech:000294
  evidence_ids:
  - record
  - abstract
  - snippets
- assessment_id: grounding
  area: grounding
  topic: grounding
  outcome: concern
  summary: Current ontology identities and mapping results remain consistent; provenance
    wording still needs repair.
  details: Focused term checks pass. C. glutamicum species exact-ID 0.99/159 and S.
    oneidensis name route 1.0/3 reproduce; exact stock candidates 196627 and 211586
    remain separate. The full snapshot SHA is pinned, release/build remains unknown,
    and filesystem mtime is not a build date.
  target_ids:
  - CommunityMech:000294
  evidence_ids:
  - taxonomy
  - gtdb
  - gtdb-rows
  - checks
- assessment_id: cultivation-and-resources
  area: completeness
  topic: cultivation and resources
  outcome: unknown
  summary: Production protocol and focal deposited data remain incompletely assessed.
  details: Anaerobic glucose-associated production and external riboflavin are supported.
    Indexed 20 mL BHI seed preparation and 24 h transfer cannot supply production
    medium, temperature, pH, vessel, gas regimen or mode; indexed 36 h conclusion
    context is bounded. No complete main/SI or focal accession audit was possible.
    Reusable assembly/protein IDs are reference context, not focal experimental deposits.
  target_ids:
  - CommunityMech:000294
  evidence_ids:
  - abstract
  - indexed
  - access
  - reusable
- assessment_id: lineage-context
  area: provenance
  topic: lineage context
  outcome: supported
  summary: Only the original single-record scientific findings receive new occurrences.
  details: The existing c2s4 grouped linkage finding and its resolved Stage 5 disposition
    remain intact; only the 000294 link is checked here. Other grouped targets and
    issue states are not reassessed. The historic graph repair remains qualified;
    no old review, record, cache or append-only history was rewritten.
  target_ids:
  - CommunityMech:000294
  evidence_ids:
  - lineage
  - delta
  - record
- assessment_id: checks-and-inputs
  area: provenance
  topic: checks and inputs
  outcome: supported
  summary: Current checks and every concrete author input are frozen.
  details: Eight focused commands pass. An initial optional GTDB replay failed because
    the nested worktree could not discover kg-microbe; the documented explicit-directory
    replay then succeeded, and both receipts remain. Corpus diagnostics retain their
    actual warning exits. New inspection/candidate/post-save outputs are excluded
    from their own input set to avoid self-reference. Partial source access prevents
    complete scientific status.
  target_ids:
  - CommunityMech:000294
  evidence_ids:
  - checks
  - network
  - gtdb
  - access
- assessment_id: metrics
  area: completeness
  topic: Literal review metrics
  outcome: supported
  summary: Completeness 80; raw validation quality 103, capped at 100.
  target_ids:
  - CommunityMech:000294
  evidence_ids:
  - record
  - checks
  - network
  metrics:
  - name: completeness
    value: 80
    unit: points
    minimum: 0
    maximum: 100
    definition: Required-fields/taxon-roles50 + environment5 + at least3nodes10 +
      medium10 + node metabolites5 =80. Roles are counted mechanically even when their
      scientific meaning needs repair.
  - name: validation_quality
    value: 100
    unit: points
    minimum: 0
    maximum: 100
    definition: 100 −10×2major −2×1minor +20×min((3/3)/2,1) +15COMPLETE =103 raw,
      capped100. Metrics do not certify science.
  - name: P1
    value: 0
    unit: findings
    definition: Native severity count.
  - name: P2
    value: 2
    unit: findings
    definition: Native severity count.
  - name: P3
    value: 1
    unit: findings
    definition: Native severity count.
  - name: P4
    value: 0
    unit: findings
    definition: Native severity count.
  details: 'Recomputed from current record: required-field/roles block 50, environment
    5, three nodes 10, medium 10, node metabolites 5 = 80. Three node evidence items
    / three nodes = 1 average; 2 P2 and 1 P3, network COMPLETE, raw quality 103 capped
    100. Literal scoring does not validate the disputed roles or remove access limits.'
findings:
- finding_id: functional-roles
  issue_key: cm-000294-functional-roles
  category: evidence
  severity: major
  native_severity: P2
  normalization_reason: Categorical biological roles alter the asserted function;
    this is more than missing optional detail.
  rule_id: review-checklist.claim-specific-support-and-context
  status: open
  certainty: confirmed
  title: Align hard functional roles with their literal meanings
  description: C. glutamicum is labeled PRIMARY_PRODUCER although available evidence
    establishes industrial succinate production, not autotrophy. S. oneidensis is
    labeled ELECTROGEN and ELECTRON_DONOR although the accessible focal source establishes
    an electroactive partner and proposes transfer, without identifying a solid acceptor
    or resolved donation direction. Other-study MR-1 capabilities cannot serve as
    measured focal-role evidence.
  target_ids:
  - CommunityMech:000294
  field_paths:
  - taxonomy[0].functional_role
  - taxonomy[1].functional_role
  evidence_ids:
  - record
  - abstract
  - schema
  - indexed
  - reusable
  - gtdb
  - gtdb-rows
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Corynebacterium_glutamicum_Shewanella_oneidensis_Succinic_Acid_Coculture.yaml
    role: canonical_record
  ownership_note: The focal community record owns this still-open repair. This refresh
    neither edits canonical data nor closes any curation issue.
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261022T011317Z-corynebacterium-shewanella-record-review
    finding_id: functional-roles
- finding_id: non-graph-scope
  issue_key: cm-000294-non-graph-scope
  category: evidence
  severity: major
  native_severity: P2
  normalization_reason: Unqualified mechanistic prose changes evidence strength independently
    of role-enum selection.
  rule_id: review-checklist.claim-specific-support-and-context
  status: open
  certainty: confirmed
  title: Qualify transfer and flux prose consistently with the graph
  description: description omits markedly from the glucose-consumption comparison
    and presents transcript-based carbon redistribution too directly. taxonomy[1].taxon_term.notes
    states contribution to interspecies electron transfer/redox coupling without the
    existing graph’s uncertainty. Accessible evidence supports positive production
    outcomes and transcript-based interpretation, not direct resolved carbon/electron
    flux.
  target_ids:
  - CommunityMech:000294
  field_paths:
  - description
  - taxonomy[1].taxon_term.notes
  evidence_ids:
  - record
  - abstract
  - schema
  - indexed
  - reusable
  - gtdb
  - gtdb-rows
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Corynebacterium_glutamicum_Shewanella_oneidensis_Succinic_Acid_Coculture.yaml
    role: canonical_record
  ownership_note: The focal community record owns this still-open repair. This refresh
    neither edits canonical data nor closes any curation issue.
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261022T011317Z-corynebacterium-shewanella-record-review
    finding_id: non-graph-scope
- finding_id: gtdb-provenance
  issue_key: cm-000294-gtdb-provenance
  category: provenance
  severity: minor
  native_severity: P3
  normalization_reason: Bounded provenance correction preserves valid taxonomic cores.
  rule_id: review-checklist.claim-specific-support-and-context
  status: open
  certainty: confirmed
  title: Replace unsupported GTDB release/build wording
  description: Both mapping_source fields claim latest release and a build date that
    the local file mtime does not establish. The current species mappings themselves
    reproduce, including the documented Shewanella name fallback.
  target_ids:
  - CommunityMech:000294
  field_paths:
  - taxonomy[0].taxon_term.gtdb_classification.mapping_source
  - taxonomy[1].taxon_term.gtdb_classification.mapping_source
  evidence_ids:
  - record
  - abstract
  - schema
  - indexed
  - reusable
  - gtdb
  - gtdb-rows
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Corynebacterium_glutamicum_Shewanella_oneidensis_Succinic_Acid_Coculture.yaml
    role: canonical_record
  ownership_note: The focal community record owns this still-open repair. This refresh
    neither edits canonical data nor closes any curation issue.
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261022T011317Z-corynebacterium-shewanella-record-review
    finding_id: gtdb-provenance
actions:
- action_id: repair-roles
  description: Repair unsupported categorical member functions without inventing replacement
    roles.
  finding_ids:
  - functional-roles
  target_ids:
  - CommunityMech:000294
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Corynebacterium_glutamicum_Shewanella_oneidensis_Succinic_Acid_Coculture.yaml
    role: canonical_record
  acceptance_checks:
  - Remove or withhold PRIMARY_PRODUCER unless focal evidence establishes autotrophy
    consistent with the native definition. Keep the source-supported succinate-producing
    description; anaplerotic carboxylation or product production alone is not proof
    of autotrophy.
  - For ELECTROGEN, require source-local evidence of transfer to a solid extracellular
    acceptor; for ELECTRON_DONOR, require local donation direction or retain only
    an explicitly proposed transfer description. Do not infer focal mechanism from
    other-study Mtr annotations, external riboflavin or yield gains.
  - Retain S. oneidensis as an electroactive partner. Optional functional_role can
    be omitted; do not automatically substitute CROSS_FEEDER, SYNTROPHIC_PARTNER or
    a recipient role. Do not claim that MR-1 universally lacks electron-transfer capability.
  - If optional ATCC 13032/MR-1 identity details are added, cite the exact indexed
    source tier and verified local stock labels, keeping K1 as a source-reported engineered
    derivative. No automatic genotype/assay reassignment or species-mapping replacement.
- action_id: qualify-prose
  description: Bring non-graph wording into line with the measured outcomes and qualified
    causal graph.
  finding_ids:
  - non-graph-scope
  target_ids:
  - CommunityMech:000294
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Corynebacterium_glutamicum_Shewanella_oneidensis_Succinic_Acid_Coculture.yaml
    role: canonical_record
  acceptance_checks:
  - Restore the source qualifier that glucose consumption was not markedly altered;
    do not equate this with identical consumption or independently tested equivalence.
  - Attribute electron-transport reinforcement and reductive-TCA redistribution to
    transcript-based metabolic interpretation. Describe Shewanella-to-Corynebacterium
    transfer/redox coupling as proposed or unresolved unless direct focal evidence
    is obtained.
  - Preserve separate 0.169 g/g/45.65% parent comparison, externally supplied 0.1
    mM riboflavin response, and K1 0.686 g/g/up-to 23.4% comparison with abolished
    lactate after ldhA deletion. Do not assign every transcript or additive assay
    to K1.
  - Retain all three untyped nodes and the existing HYPOTHESIZED/PARTIAL arrows, including
    source-only PAIRWISE node 1. No mediator secretion, thermodynamic syntrophy, obligatory
    cooperation or causal mediation is added without source support.
  - Keep indexed seed BHI details separate from production conditions and maintain
    the full-Methods/SI access limitation. Any 36 h detail remains indexed Conclusion
    context until full experimental scope is checked; do not merge the conflicting
    Highlight attribution of 45.65% with the Abstract.
- action_id: repair-gtdb
  description: Make the two mapping provenance strings reproducible.
  finding_ids:
  - gtdb-provenance
  target_ids:
  - CommunityMech:000294
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Corynebacterium_glutamicum_Shewanella_oneidensis_Succinic_Acid_Coculture.yaml
    role: canonical_record
  acceptance_checks:
  - Retain C. glutamicum 1718 exact-ID 0.99/159 and S. oneidensis 70863 name-route
    1.0/3, including the explicit lack of an exact species 70863 crosswalk row.
  - Record actual snapshot SHA256 761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd
    and lookup route. Label filesystem mtime only as mtime; leave GTDB release/build
    unknown unless independently verified.
  - Keep optional ATCC 13032 exact 1.0/15 and MR-1 exact 1.0/3 candidates separate
    from species aggregates and the engineered K1 designation. Mapping genome counts
    are not study abundance.
- action_id: validate-future-curation
  description: Validate separately authorized repairs and retain the review evidence.
  finding_ids:
  - functional-roles
  - non-graph-scope
  - gtdb-provenance
  target_ids:
  - CommunityMech:000294
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Corynebacterium_glutamicum_Shewanella_oneidensis_Succinic_Acid_Coculture.yaml
    role: canonical_record
  acceptance_checks:
  - After authorized edits, attach exact claim-local evidence, update history and
    run schema, strict, terms, explained references, GTDB, domain and history checks,
    then just gen-html and just check-docs-current. This review does not edit canonical
    records, caches, history or generated pages.
  - Preserve all original inspections, preliminary/final support and public access
    failures. Recovered full main/SI should receive a distinct source review before
    adding production conditions, dataset accessions or stronger mechanisms. No paid
    retrieval, author contact, external issue closure or unrelated record edit follows
    from this bundle.
limitations:
- Only the complete fresh abstract and bounded indexed primary sections were available.
  Direct publisher retrieval failed and the anonymous API supplied coredata; no full
  Methods, Results, figures, tables, authenticated SI or full bibliography was inspected.
- The stock link is supported at indexed source tier. K1 assay assignment, directed
  electron transfer, solid-acceptor evidence, direct flux and selective mediation
  remain unresolved. Other-study reusable annotations are not focal proof.
- Seed preparation is distinct from production; indexed conclusion timing is not a
  recovered full protocol. A historical Highlight/Abstract attribution discrepancy
  is not silently harmonized, and missing accessible data is not global absence.
- Fresh whole-snapshot GTDB replay verifies mapping results but not an upstream release/build.
  Optional fields, including ecological_state, are not made mandatory by a rubric
  score.
- Only 000294 is scientifically refreshed. Grouped linkage findings retain their full
  original target scopes and dispositions. Root and independent reviewers own issue-state
  checks and final adversarial approval.
notes:
- 'Refresh for stale-review issue #2569. Original bundle remains immutable; historical
  local-source provenance limitation is separately tracked by #2570.'
- All local input bytes used by this author are included through native --input, including
  public source bodies/receipts, initial inspection, mapping copy, checks, guidance
  and this frozen JSON builder. No YAML writer is introduced.
tags:
- pr2058
- staleness-refresh
- current-main
- partial-source-access
related_reviews:
- repository: CultureBotAI/CommunityMech
  review_id: 20261022T011317Z-corynebacterium-shewanella-record-review
  relationship: Immutable current-main successor preserving all three open finding
    keys and all four actions after the MR-1 common_taxon addition.
```
