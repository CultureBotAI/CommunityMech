# Current-main refresh of the defined three-strain nitrifying community review

- Review: 20261106T191707Z-defined-three-strain-nitrifying-current-main
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-11-06T19:08:25.037608Z
- Finished UTC: 2026-11-06T19:17:07.036478Z
- Reviewer: codex (self_review)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Current-main roles and abundance annotations were reassessed against fresh abstract, public SI/graphical evidence and exact stock authorities. Both original findings remain open with their full acceptance; one minor local-evidence finding separates carbon-fixation capacity from focal nitrogen-study evidence. ABUNDANT is retained as qualitative prominence, not measured fraction. Eight focused checks pass, but the main manuscript remains inaccessible and scientific completion is false.

## Scope And Provenance

Whole current maintained record, exact main delta, original findings/actions, accessible primary/SI/graphic, relevant current stock/taxonomic authorities, history and native controls; main manuscript unavailable.

Selection: Only stale CommunityMech:000397 in PR #2061; other records and other review finding heads are not superseded.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 693a801ca3660240c6c5c0e5192400cbfac24c07.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000397 | kb/communities/Defined_ThreeStrain_Organic_Nitrogen_Nitrifying_Community.yaml | maintained | Defined Three-Strain Organic-Nitrogen Nitrifying Community |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000397 | Actual current command exit 0. |
| validate-strict | passed | True | CommunityMech:000397 | Actual current command exit 0. |
| validate-terms | passed | True | CommunityMech:000397 | Actual current command exit 0. |
| validate-references-explained | passed | True | CommunityMech:000397 | Actual current command exit 0. |
| validate-gtdb | passed | True | CommunityMech:000397 | Actual current command exit 0. |
| validate-gtdb-domain | passed | True | CommunityMech:000397 | Actual current command exit 0. |
| validate-history | passed | True | CommunityMech:000397 | Actual current command exit 0. |
| cache-name-check | passed | True | CommunityMech:000397 | Actual current command exit 0. |
| audit-network | failed | False | CommunityMech:000397 | Shared current corpus run: 48 warnings in 17 of 510 records, zero errors, actual exit 1; existing warning baseline retained. |
| check-network-quality | failed | False | CommunityMech:000397 | Shared current corpus run: 48 warnings in 17 of 510 records, zero errors, actual exit 1; existing warning baseline retained. |

## Scientific And Domain Assessments

### Three-stock laboratory model

identity: supported. Targets: CommunityMech:000397.

The three source-named NBRC stocks remain a defined engineered laboratory community.

Retain SYNTHETIC origin, ENGINEERED state and BIOTECHNOLOGY category. Source Bacillus badius and canonical Pseudobacillus badius refer to the same species; NBRC stock descriptors are distinct from species/genome classification. The soil analogy in the graphical abstract is not a natural origin or a live host experiment.

### Sequential organic-nitrogen conversion

graph: supported. Targets: CommunityMech:000397.

Retain the single community-level CROSS_FEEDING node and its bounded selected-condition outcome.

Exact selector ecological_interactions[0]. All three participating taxa are canonical members, no pairwise source/target or downstream arrows are encoded. The two SUPPORT / IN_VITRO snippets are the abstract's construction and endpoint statements, hashes 0a1d0d1dfaa1379ba9df48f9ff7cde142aa2368507165e66cab0b42214c443c4 and 4faa31e56824f4e0abc9b81d22331b4d573b7b3e6deb98a8b1b0782dd5402b0a. Graphical arrows assign organic N to ammonium to nitrite to nitrate at the named functional stages. Retain aggregate sequential exchange without inferring donor-resolved flux, obligate reciprocity, necessity or all-substrate success. GO:0019329 ammonia oxidation denotes one component; ammonium/nitrite/nitrate CHEBI ions retain mg-N/L nitrogen-equivalent units.

### Added roles and qualitative abundance

evidence: concern. Targets: CommunityMech:000397.

Nitrogen roles and qualitative major-partner prominence are supportable; the carbon-fixation role needs its own bounded evidence.

PRIMARY_DEGRADER for B. badius fits the organic-N/Polypepton transformation and CROSS_FEEDER for the nitrifiers fits successive intermediate utilization. ABUNDANT is accepted only as qualitative prominence of these three central partners, not a percentage band, equal proportions, a fixed inoculum ratio or stability across days/arms. The graphical estimated-ratio time series and S1 absolute counts do not establish those stronger claims. PRIMARY_PRODUCER specifically means fixes carbon; the local taxon evidence currently quotes membership and nitrifier abundance association from the focal abstract, which does not make that assertion. NITE's exact-stock list supports background capacity, not focal community carbon flux; this narrows the new finding to local evidence/provenance rather than false organism identity or disproven physiology.

### Supplementary context and unresolved main protocol

completeness: concern. Targets: CommunityMech:000397.

The original supplementary-cultivation finding remains open with all three acceptance checks.

S2 physical page 2 supports 2 g/L Polypepton NF and separately the nitrifiers' inoculation two days after B. badius. S1 physical page 1 supports repeated culture using post-nitrification cells and day 3 feeding. S3 physical page 3 concerns separate nitrifier cultures in HEPES/Boon media over 20–37 degrees C; it cannot supply a common community temperature. Main Figure 4(d), basal recipe, inoculum ratio, atmosphere and vessel remain unread or unresolved. Preserve the dated organic_nitrogen_cultivation_details KNOWLEDGE_GAP and trace later recovery; do not treat a schematic flask or collection maintenance recipe as the experimental protocol.

### Species mapping and immutable provenance

grounding: concern. Targets: CommunityMech:000397.

The original mapping-completion and provenance finding remains open with exact existing acceptance.

Fresh community-mode lookup reproduces all three mapping routes and denominators in the original action. Retain the Nitrobacter name difference as a name comparison, not a new taxonomic event. The copied crosswalk is byte-identical to the external source; its local mtime is not an upstream release/build date.

### Publication and source/cache boundaries

evidence: supported. Targets: CommunityMech:000397.

Both publication identifiers and all 18 existing snippets remain valid at their actual source tiers.

No full main-paper or raw dataset review is claimed. The cache is plain PubMed-format abstract text with no false full-text content_type claim. The inspected public abstract/SI/graphic declares no focal data deposit; main availability is unknown. Stock genome links are not silently promoted to focal deposits. No separate cache repair is inferred from successful fresh-source access. iModulonDB is not applicable because no gene, locus, regulator, pathway dataset or expression module is named in this target.

### Exact predecessor retention and Cycle 4 context

provenance: supported. Targets: CommunityMech:000397.

Both original open findings are explicitly continued; the separate Cycle 4 missing-field disposition is not reopened or superseded.

The October 31 enum additions satisfy the historical field-presence observation. This refresh does not retire, reopen or scientifically re-review other targets in the Cycle 4 reports. It separately distinguishes field presence from claim-local carbon-fixation support. All four history sidecars and inline events remain immutable; a later authorized curation must append its own exact source/claim scope.

### Current focused validation and corpus context

schema: supported. Targets: CommunityMech:000397.

Eight focused checks passed; current shared network warnings remain explicit.

Passing schema, strict, labels, references, GTDB/domain, history and cache naming checks do not complete an access-limited scientific review. The historical 44-warning/477-record baseline is not reused as current; current parent receipts show 48 warnings across 17 of 510 records and no errors.

### Actual author reading and unavailable main

scope: unknown. Targets: CommunityMech:000397.

The refresh remains partial and scientific_review is false.

The accessible abstract, all three SI pages, graphical abstract and relevant authority pages were read. Main Methods/results, main figures and full treatment comparisons remain unavailable through the bounded public routes used. No paid access, contact, experiments, digitization or raw-data reanalysis occurred.

### Literal native metrics

completeness: supported. Targets: CommunityMech:000397.

Completeness is 65; raw validation quality is 129 and capped quality is 100.

These are structural rubric values, not evidence strength. Adding roles raises the literal required-field block while the new local evidence gap remains open.

## Findings

### cultivation-context: Recover supplementary cultivation context while keeping the main-protocol gap

minor / open / confirmed; issue key: cm-000397-cultivation-context.

The open discussion accurately described the cached abstract. Accessible S1/S2 now provide bounded assay information that the record does not capture; this supports enrichment rather than inventing a complete recipe.

### gtdb-provenance: Complete the recoverable species mapping and correct provenance

minor / open / confirmed; issue key: cm-000397-gtdb-provenance.

Pseudobacillus badius is currently resolvable. The valid two existing GTDB cores carry unsupported latest-release/build-date wording inferred from a local snapshot mtime.

### carbon-role-evidence: Separate background carbon-fixation capacity from focal nitrogen evidence

minor / open / confirmed; issue key: cm-000397-carbon-role-evidence-scope.

taxonomy[1] and taxonomy[2] now include PRIMARY_PRODUCER, defined as carbon fixation, while their local PMID:42668143 evidence quotes only membership and nitrifier abundance association. The accessible focal abstract, graphical abstract and SI do not report carbon-fixation flux. NITE's exact-stock CO2-fixing list supports background capacity, which requires its own source and scope if retained; it is not a focal in-vitro carbon-flux result.

## Recommended Actions And Acceptance Checks

### enrich-cultivation

Add the recovered supplementary assay context and narrow the remaining open gap.

- Cite Supplement Figure S2 caption, physical page 2: Polypepton NF 2 g/L and the separate arm with N. europaea NBRC 14298 and N. winogradskyi NBRC 14297 introduced two days after B. badius NBRC 15713. Do not assign either arm to the approximately 56 mg-N/L abstract endpoint without main experimental mapping.
- Cite Figure S1 caption and physical page 1 feed arrow for transfer of post-nitrification cells to fresh medium and day 3 organic feeding. Preserve assay context without inventing operating mode, basal composition, feed quantity, inoculum ratio, atmosphere or vessel.
- Keep the main protocol unresolved. Figure S3 HEPES/Boon media and 20–37°C tests concern separate isolates; NBRC maintenance media and the schematic flask cannot supply community conditions. Preserve the dated discussion rationale and add a traceable follow-up rather than rewriting historical facts.

### repair-gtdb

Use current species-level mapping evidence and accurate snapshot provenance.

- For taxonomy[0].taxon_term, use GROUNDED with GTDB:s__Pseudobacillus_badius; lineage d__Bacteria;p__Bacillota;c__Bacilli;o__Bacillales_B;f__Domibacillaceae;g__Pseudobacillus;s__Pseudobacillus badius; NCBITaxon:1455, fraction 1.0,26 genomes, is_reclassified false, exact ncbi_id route.
- Retain taxonomy[1] Nitrosomonas europaea via ncbi_name, fraction 1.0/2 genomes, and taxonomy[2] Nitrobacter winogradskyi_A via ncbi_id, fraction 0.88/8 genomes. Record mapping snapshot SHA256 761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd. Label filesystem mtime as mtime; leave unknown upstream release/build metadata unknown.
- Species aggregates do not classify the exact experimental genome. Existing NBRC stock descriptors remain valid; optional finer NCBI terms require their own labels and mapping denominators rather than silent substitution.

### validate-curation

Validate any separately authorized record repair.

- Recheck exact source/treatment scope, ontology labels and excerpt support; run focused schema, strict, terms, explained references, GTDB/domain and history gates, then just gen-html and just check-docs-current for authorized record changes.
- Preserve original source responses, caches, histories and prior decisions. This review changes no canonical record or scientific status and authorizes no contact, paid research, issue or Git mutation.

### scope-carbon-role-evidence

Support or qualify the two optional PRIMARY_PRODUCER annotations without conflating background capacity and focal measured function.

- For taxonomy[1] NBRC 14298 and taxonomy[2] NBRC 14297, inspect appropriate exact-stock physiological evidence and attach an allowed stable reference, exact snippet and honest evidence tier to any retained carbon-fixation role; otherwise omit or qualify the optional role without declaring the organisms incapable of carbon fixation.
- Explicitly distinguish source-backed background stock capability from carbon fixation measured in the PMID:42668143 community. The inspected NITE stock list is printed slide 34 / PDF physical page 35; it cannot certify coculture carbon flux. Do not relabel the focal nitrogen-conversion abstract as carbon-fixation evidence.
- Retain supported PRIMARY_DEGRADER/CROSS_FEEDER nitrogen roles and the bounded three-member identity. ABUNDANT remains qualitative major-partner prominence; infer no percentage threshold, equal proportions, fixed inoculum ratio or abundance stable across treatment/time.
- For any separately authorized repair, append exact source/scope history while preserving the October 31 event, then run focused schema/strict/terms/references/GTDB/domain/history checks and regenerate/check derived docs. Keep unavailable main-protocol details explicitly unresolved.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | kb/communities/Defined_ThreeStrain_Organic_Nitrogen_Nitrifying_Community.yaml; Whole current maintained YAML | supports | Three defined NBRC stocks, one aggregate conversion node, no downstream arrows; only roles, abundance categories and October 31 history changed. |
| abstract | .temp/pr2061/refresh397/sources/epmc.json; PMID:42668143 / DOI:10.1093/bbb/zbag131; full MED abstract and metadata | supports | The three stocks, selected-condition nitrate endpoint and relative-abundance association are reported; carbon fixation is not a focal reported measurement. |
| publisher | .temp/pr2061/refresh397/sources/publisher-web.txt; Public publisher Abstract and access notice; web-tool response captured locally | supports | The article identity matches. The public page exposes abstract, graphical abstract and supplementary link but states no access to the main article. |
| supplement | .temp/pr2061/refresh397/sources/supplement.pdf; All three physical PDF pages: Figures S1, S2 and S3 | supports | S1 repeat/refeeding, S2 Polypepton NF and delayed-inoculation arms, and S3 separate-isolate media/temperature tests were read and visually checked. These do not supply the complete focal protocol. |
| graphical | .temp/pr2061/refresh397/sources/graphical.jpeg; Named three-stock conversion schematic and nitrogen/estimated-ratio time course | supports | The schematic supports organic-N transformation and sequential ammonium/nitrite utilization. It neither depicts carbon fixation nor establishes equal or time-invariant cell fractions. |
| stock-carbon | .temp/pr2061/refresh397/sources/nedo-carbon-stocks.pdf; Printed slide 34, PDF physical page 35: NITE CO2-fixing stock list | supports | NBRC 14298 and 14297 appear in NITE's CO2-fixing-stock list. This is background stock-capability context, not measured carbon flux in the 2026 coculture. |
| stock-15713 | .temp/pr2061/refresh397/sources/nbrc-15713.html; NBRC 15713 exact stock catalogue | supports | The stock identity resolves. Collection-maintenance conditions and stock sequence links are not the focal community protocol or study deposits. |
| stock-14298 | .temp/pr2061/refresh397/sources/nbrc-14298.html; NBRC 14298 exact stock catalogue | supports | The stock identity resolves. Collection-maintenance conditions and stock sequence links are not the focal community protocol or study deposits. |
| stock-14297 | .temp/pr2061/refresh397/sources/nbrc-14297.html; NBRC 14297 exact stock catalogue | supports | The stock identity resolves. Collection-maintenance conditions and stock sequence links are not the focal community protocol or study deposits. |
| taxonomy | .temp/pr2061/refresh397/sources/taxonomy.xml; Fresh NCBI taxonomy efetch entries 1455, 915 and 913 | supports | All three species labels resolve; Bacillus badius is a synonym of Pseudobacillus badius. Species identity does not certify an exact experimental genome. |
| gtdb | .temp/pr2061/refresh397/gtdb.stdout; Actual current community-mode lookup against the locally copied crosswalk | supports | Pseudobacillus badius resolves by exact species ID at 1.0/26, Nitrosomonas europaea by species name at 1.0/2, and Nitrobacter winogradskyi_A by ID at 0.88/8. Existing upstream release/build wording is not established by a filesystem mtime. |
| crosswalk | .temp/pr2061/refresh397/gtdb-copy.json; Source/copy SHA256 equality | supports | The source and local copy both hash to 761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd; no new release date is inferred. |
| schema | src/communitymech/schema/communitymech.yaml; AbundanceEnum, FunctionalRoleEnum, community, interaction and optional context slots | supports | ABUNDANT is qualitative major-member prominence, PRIMARY_PRODUCER means carbon fixation, and optional fields do not become mandatory merely because the schema permits them. |
| snippets | .temp/pr2061/refresh397/snippet-audit.json; All 18 canonical snippet placements | supports | Seventeen placements match the fresh abstract and the remaining placement is exact DOI metadata; all 18 match the committed abstract cache. Lexical agreement does not prove the newly added carbon-fixation role. |
| predecessor | reviews/structured/20261022T043046Z-defined-three-strain-nitrifying-record-review/review.yaml; Original two findings and three actions / eight acceptance checks | supports | Both original finding keys and every original acceptance check are retained; the historical source-access limits are not rewritten. |
| lineage | .temp/pr2061/refresh397/lineage-context.json; Ignored-inclusive discovery of exact 397 finding occurrences | supports | The Cycle 4 presence finding has its own resolved successor. This observation preserves that narrow presence disposition while assessing the new annotation's evidence separately. |
| history | history/records/Defined_ThreeStrain_Organic_Nitrogen_Nitrifying_Community/2026-10-31T234500Z-antigravity-2095.yaml; events[0] details and matching canonical curation_history[3] | supports | The history accurately records the added enum values; its focal PMID citation does not supply separate carbon-fixation proof. No old history is edited. |
| delta | .temp/pr2061/refresh397/target-diff.patch; Original PR head to integrated current-main target diff | supports | Five role assignments, three abundance categories and one inline history event were added; all original experimental claims and evidence snippets are unchanged. |
| reading | .temp/pr2061/refresh397/source-reading.json; Author's actual source reading and bounded-access notes | supports | Author read the complete current record, predecessor, fresh abstract, all three SI pages, graphical abstract, exact stock/NCBI authority, relevant NITE slide and local checks. This is not independent approval. |
| checks | .temp/pr2061/refresh397/checks/focused-checks.json; Eight actual focused command/exit/stdout/stderr receipts | supports | All eight focused checks exited 0. They do not establish scientific completion. |
| corpus | .temp/pr2061/root-checks/initial-checks.json; Parent-run current full-corpus diagnostics and native controls | supports | Both network diagnostics returned exit 1 with 48 warnings across 17 of 510 records and zero errors; these are nonrequired context. The author reuses the recorded parent run rather than claiming to rerun it. |
| check-validate | .temp/pr2061/refresh397/checks/validate.json; Actual focused command and output paths | supports | Actual exit 0; output artifacts are independently pinned. |
| check-validate-strict | .temp/pr2061/refresh397/checks/validate-strict.json; Actual focused command and output paths | supports | Actual exit 0; output artifacts are independently pinned. |
| check-validate-terms | .temp/pr2061/refresh397/checks/validate-terms.json; Actual focused command and output paths | supports | Actual exit 0; output artifacts are independently pinned. |
| check-validate-references-explained | .temp/pr2061/refresh397/checks/validate-references-explained.json; Actual focused command and output paths | supports | Actual exit 0; output artifacts are independently pinned. |
| check-validate-gtdb | .temp/pr2061/refresh397/checks/validate-gtdb.json; Actual focused command and output paths | supports | Actual exit 0; output artifacts are independently pinned. |
| check-validate-gtdb-domain | .temp/pr2061/refresh397/checks/validate-gtdb-domain.json; Actual focused command and output paths | supports | Actual exit 0; output artifacts are independently pinned. |
| check-validate-history | .temp/pr2061/refresh397/checks/validate-history.json; Actual focused command and output paths | supports | Actual exit 0; output artifacts are independently pinned. |
| check-cache-name-check | .temp/pr2061/refresh397/checks/cache-name-check.json; Actual focused command and output paths | supports | Actual exit 0; output artifacts are independently pinned. |

## Limits And Additional Notes

- Bounded ordinary public routes recovered the abstract, declared three-page supplement and graphical abstract, but not the main Methods/results or main figures. This is not a global assertion that no full text exists.
- The supplement does not identify the complete basal coculture recipe, common temperature, vessel, atmosphere or inoculum ratio, nor map the approximately 56 mg-N/L abstract outcome to its S2 arms. S3 is separate-isolate evidence.
- Supplement curves were visually inspected without digitization, statistical reanalysis or inferred detection limits. No raw sequence, assay dataset or taxon-specific flux was analyzed.
- The NITE/NEDO stock list is a background capability authority, not a substitute for focal community carbon-flux evidence. Exact stock physiology should be sourced and scoped before adding local support.
- The author reused parent-owned current corpus diagnostics with their true exit codes. This refresh is author work and is separately reviewed; no canonical record, cache, history or scientific status was changed.
- All original two keys, three actions and eight acceptance checks are retained; one additional key/action adds four checks. Original saved bundles remain immutable.
- All actual local inputs are native-pinned, including fresh sources, authority/validator receipts, helper, initial inspection and byte-identical GTDB copy. The final inspection, candidate and subsequent validation outputs are generated metadata, not circular inputs.
- No separate source-recovery action is invented: the existing cultivation action explicitly retains the main-protocol gap. No extra cache/header or study-deposit finding was established in the inspected source scope.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261106T191707Z-defined-three-strain-nitrifying-current-main
kind: record
repository: CultureBotAI/CommunityMech
title: Current-main refresh of the defined three-strain nitrifying community review
started_at: '2026-11-06T19:08:25.037608Z'
finished_at: '2026-11-06T19:17:07.036478Z'
reviewer:
  identity: codex
  kind: agent
  independence: self_review
  independence_basis: Author of this refresh; a separate agent performs the independent
    adversarial pass. This document claims no independent approval of itself.
skill: review-yaml-record
completion: partial
verdict: needs_curation
scientific_review: false
summary: Current-main roles and abundance annotations were reassessed against fresh
  abstract, public SI/graphical evidence and exact stock authorities. Both original
  findings remain open with their full acceptance; one minor local-evidence finding
  separates carbon-fixation capacity from focal nitrogen-study evidence. ABUNDANT
  is retained as qualitative prominence, not measured fraction. Eight focused checks
  pass, but the main manuscript remains inaccessible and scientific completion is
  false.
source:
  git_revision: 693a801ca3660240c6c5c0e5192400cbfac24c07
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
  - path: .temp/pr2061/refresh397/NCBI2GTDB.tsv.gz
    sha256: 761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd
    role: context
  - path: .temp/pr2061/refresh397/checks/cache-name-check.json
    sha256: ae807705066c385d30205b41a672f535c825db2059cb911a8614ee92af1bfba5
    role: context
  - path: .temp/pr2061/refresh397/checks/cache-name-check.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/refresh397/checks/cache-name-check.stdout
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/refresh397/checks/focused-checks.json
    sha256: d2a909f9ced2b6b98b1d7d074dff827d98983b456b77bc763a4c1509a5b54bcd
    role: context
  - path: .temp/pr2061/refresh397/checks/strict.tsv
    sha256: b184ed5450b968070bb6c75648407e388f41a1eaf7017890723cf560999fc3f7
    role: context
  - path: .temp/pr2061/refresh397/checks/validate-gtdb-domain.json
    sha256: f3c564bf7cbd18b78fca2032dee3466604bb74cc76493a8ff066a2abbff74f1f
    role: context
  - path: .temp/pr2061/refresh397/checks/validate-gtdb-domain.stderr
    sha256: 2def66e7a7d91fdcf88708ac587c685bff72e0c08e52e3f389fe9c4c5d3f1a6a
    role: context
  - path: .temp/pr2061/refresh397/checks/validate-gtdb-domain.stdout
    sha256: ede937293c42cad366f434dce49a485a9a0c56fe86620b52ca243ad10e09ecae
    role: context
  - path: .temp/pr2061/refresh397/checks/validate-gtdb.json
    sha256: cb24211e99cddd348912aa47ff870df7ae65947395b24e7d8bdd456cf84b5bf0
    role: context
  - path: .temp/pr2061/refresh397/checks/validate-gtdb.stderr
    sha256: 05d5dc632278ccb5d1737da19e812916b1c21e3fd766a3b5190ddc1bf9c78e77
    role: context
  - path: .temp/pr2061/refresh397/checks/validate-gtdb.stdout
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/refresh397/checks/validate-history.json
    sha256: c322027c1e4c372e4675702b7996b478c330036e8a44517c3cb4980dace92238
    role: context
  - path: .temp/pr2061/refresh397/checks/validate-history.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/refresh397/checks/validate-history.stdout
    sha256: de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
    role: context
  - path: .temp/pr2061/refresh397/checks/validate-references-explained.json
    sha256: 1c8558e5ca7c3a48b366fbbfc9a8515982b203cea7b7769fd25edd87c626565d
    role: context
  - path: .temp/pr2061/refresh397/checks/validate-references-explained.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/refresh397/checks/validate-references-explained.stdout
    sha256: 10d0d060d0ce00a57f6d832b9b9e310bafbc9732c960dc48e894fd6738968403
    role: context
  - path: .temp/pr2061/refresh397/checks/validate-strict.json
    sha256: 4a3405de1536712af00296240aa48e8078b4c26475293a07c22f49256b621d9c
    role: context
  - path: .temp/pr2061/refresh397/checks/validate-strict.stderr
    sha256: b5a9103395f16d3e985edad061dfaa94b6321ceac920658bf10e2b5b8e82c721
    role: context
  - path: .temp/pr2061/refresh397/checks/validate-strict.stdout
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/refresh397/checks/validate-terms.json
    sha256: f1f21f8d5bf07ed0401fb9e3264f67ad67439964c784e26d3cf3da7eff13dde5
    role: context
  - path: .temp/pr2061/refresh397/checks/validate-terms.stderr
    sha256: c0d3b1880f8844fea69963524e1263caaf389a54b8b0e7e1565bcd88c0de76b4
    role: context
  - path: .temp/pr2061/refresh397/checks/validate-terms.stdout
    sha256: 23acda1c1d3194d12bc947d897d07de83f4a076a9d93c135148885108530e018
    role: context
  - path: .temp/pr2061/refresh397/checks/validate.json
    sha256: 2e40841d3b141430a01558396dd008b9621859f7ca056f3796048591e23d8e49
    role: context
  - path: .temp/pr2061/refresh397/checks/validate.stderr
    sha256: ad19888eb93cd6ecae4eb10269b525f889504ee49d61a43ed16ce96b48bfd3e1
    role: context
  - path: .temp/pr2061/refresh397/checks/validate.stdout
    sha256: de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
    role: context
  - path: .temp/pr2061/refresh397/gtdb-command.json
    sha256: 637d68bd4aef737c191de18b1a0f05f32971ac22df295e7b37f497165cb5bc19
    role: context
  - path: .temp/pr2061/refresh397/gtdb-copy.json
    sha256: ce4df46aaba541157006058f98f9f16fcbf6dcaa257262e305029f05296bfafd
    role: context
  - path: .temp/pr2061/refresh397/gtdb.stderr
    sha256: cc689986c1b406899056aded4b105238643067cb9c1d7ca6969db082fe3a56b7
    role: context
  - path: .temp/pr2061/refresh397/gtdb.stdout
    sha256: 7f6ff0139743e2b84bfd38e41039b562a67d368232a19cb11e53b201aba9a96b
    role: context
  - path: .temp/pr2061/refresh397/initial-candidate-validation.stderr
    sha256: d6e4dfb0f1a3ca147daf19192c6f6f9372dbb589d078ff10a5e31319285c5fd4
    role: context
  - path: .temp/pr2061/refresh397/initial-candidate-validation.stdout
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/refresh397/initial-candidate.json
    sha256: 147237c38673dd78803ac8ee94f865c4049648167dd16a0fbf964f024b5ae8a3
    role: context
  - path: .temp/pr2061/refresh397/initial-final-inspection.json
    sha256: 595b7a75acdfef997b5a4a91bd0dd2fc43d7e9728db26f39e344261eb802fb15
    role: context
  - path: .temp/pr2061/refresh397/initial-inspect.json
    sha256: ad6dd772a3bb9560760b6eac974854db2d300ccebf44acca8e46eed7e0817c14
    role: context
  - path: .temp/pr2061/refresh397/initial-inspect.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/refresh397/initial-pre-freeze-lint.json
    sha256: 75a87c47e17cba7157bd2b2c485e2fa3aaaed5d5a216b3c0d7ab969605613093
    role: context
  - path: .temp/pr2061/refresh397/initial-pre-freeze-lint.stderr
    sha256: 9325c6b2d2de126dc0bbe7ff741d8aa81bf78b2d12672d3dad0448f6453adc4a
    role: context
  - path: .temp/pr2061/refresh397/initial-pre-freeze-lint.stdout
    sha256: 1cffccf768da50ca84db43e973c69c47f795b57101ebfc1825d52472c790ab4d
    role: context
  - path: .temp/pr2061/refresh397/input-paths.json
    sha256: 5c69823246a59cc7c14bf3d937f0dcd83ecd60cc49ebf32c8d0854451beab8a0
    role: context
  - path: .temp/pr2061/refresh397/lineage-context.json
    sha256: 78dc8c96ac27dfba946f8abd758ae698e1576dbfeef8f88abd8f8d0e8ed0e8c3
    role: context
  - path: .temp/pr2061/refresh397/ontology-authority.json
    sha256: d35d36e2a950702b0f6de6fa43072aa5c137b9e9019974650957d77ce90f7547
    role: context
  - path: .temp/pr2061/refresh397/pre-freeze-lint.json
    sha256: 288080e52e3777e21655a0052e2362f97d7925b7ea56751be7bc592a5989af9a
    role: context
  - path: .temp/pr2061/refresh397/pre-freeze-lint.stderr
    sha256: d96da05d18c501dde9a6fc2d92598b2acc1b3065f94142174400ad8427c80eb1
    role: context
  - path: .temp/pr2061/refresh397/pre-freeze-lint.stdout
    sha256: 1cffccf768da50ca84db43e973c69c47f795b57101ebfc1825d52472c790ab4d
    role: context
  - path: .temp/pr2061/refresh397/snippet-audit.json
    sha256: 8c50749b3e188e094daa6fd0b663c1f357cb79436c7ca894872f117a891aae1c
    role: context
  - path: .temp/pr2061/refresh397/source-reading.json
    sha256: 22ca6117e8cb60cbfcd73f2e7e23dcaec2ab63585357497ed5062a1b0ed0f756
    role: context
  - path: .temp/pr2061/refresh397/sources/asset-retrievals.json
    sha256: b3b2f131c5a64576e46b9e9d13cc474c49ec9a26ac27eed231ed2b167617faaf
    role: context
  - path: .temp/pr2061/refresh397/sources/epmc.json
    sha256: e1ac6d2e6801fd7b51363841bb0f4903fdeb4a2b518e64f95c21f47c3cb475f8
    role: context
  - path: .temp/pr2061/refresh397/sources/graphical.jpeg
    sha256: 178e3488b4a2c40f8eef5aedfe0428beef3e50ed7648ff8758a26cdc73a8f98e
    role: context
  - path: .temp/pr2061/refresh397/sources/initial-retrievals.json
    sha256: cac639f4a7f9cb3ca4022f64a3974749fad50244098c0093879d49f48074f98e
    role: context
  - path: .temp/pr2061/refresh397/sources/mifup-14298.html
    sha256: e25bf6afdc2f1db71c902f55614dd11e29e61951e677bbdbe5f778f695dd0252
    role: context
  - path: .temp/pr2061/refresh397/sources/nbrc-14297.html
    sha256: 99bdda1ea1469903ce8200f4425acf017b09ae13db956c166a139ed200f14380
    role: context
  - path: .temp/pr2061/refresh397/sources/nbrc-14297.txt
    sha256: c80512ddc5dcf907960eaf794110c4e38083c348c5c9624deda13b866f9fed0c
    role: context
  - path: .temp/pr2061/refresh397/sources/nbrc-14298.html
    sha256: b6d70996595c0e315ed14cc144822b78a40ed5f7349f70032ce98f5f10335166
    role: context
  - path: .temp/pr2061/refresh397/sources/nbrc-14298.txt
    sha256: f28ee1d530a9441cde8a7ffc3368fa7ae119245d74808a908672015eeeb34951
    role: context
  - path: .temp/pr2061/refresh397/sources/nbrc-15713.html
    sha256: 9694496131c425997b3437fdaa1584fefb4a72a62a35e1381faf69784e991a0b
    role: context
  - path: .temp/pr2061/refresh397/sources/nbrc-15713.txt
    sha256: 2fdc9990f278a339575ce871d61517a7579bdbf11732eef4d31408f99754b196
    role: context
  - path: .temp/pr2061/refresh397/sources/nedo-carbon-stocks.pdf
    sha256: 4aeb9850f88b151ca4646dcfc4c8d88abd0a03ec51015dd85a03c6a8f32a62c5
    role: context
  - path: .temp/pr2061/refresh397/sources/nedo-carbon-stocks.txt
    sha256: fb65f48098e3331b7ba153110e408eb7463782f45d399af0438fa9c366c2dbe1
    role: context
  - path: .temp/pr2061/refresh397/sources/nedo-stock-page-35.png
    sha256: a540b4fc1cc7f045a16be02a29bb14c3b7da107e8728499005b4d9fdf4fac6b8
    role: context
  - path: .temp/pr2061/refresh397/sources/publisher-abstract.html
    sha256: b15940788427af3544b8a3a58a449ea1d48d28ac5b2a7a4aaa037febc1e2f49b
    role: context
  - path: .temp/pr2061/refresh397/sources/publisher-web.txt
    sha256: 3278cf3d240f3ae44f6af4fed42e2392b59de8a6b89273693f1496555aa4a056
    role: context
  - path: .temp/pr2061/refresh397/sources/publisher.html
    sha256: 510101311ecba63c1a1819b7430d7c2ba4009991995b58074c4a24066b55088c
    role: context
  - path: .temp/pr2061/refresh397/sources/stock-retrievals.json
    sha256: 1c003f6f7689cbaff55b819238339ae794fa1abaa6bf3fefaae81ce0cf5664b5
    role: context
  - path: .temp/pr2061/refresh397/sources/supplement-page-1.png
    sha256: 919bf66bf25201a45fa616e0f67be6697f4e35478ee744f464d2c9748464a669
    role: context
  - path: .temp/pr2061/refresh397/sources/supplement-page-2.png
    sha256: ad295027eae7b96fcd35f5cc1f6b9de224dba9fe3e26e968c72c79b85d64ba99
    role: context
  - path: .temp/pr2061/refresh397/sources/supplement-page-3.png
    sha256: 0756d613ed4f124e8cd04406bf1ccfb7dbc1ee454eb1c0fd2d89e523e144ffef
    role: context
  - path: .temp/pr2061/refresh397/sources/supplement.pdf
    sha256: e42576f83d113d7f1e546913483f1ac35628a3d28cc365abd3456b6428a36d3d
    role: context
  - path: .temp/pr2061/refresh397/sources/supplement.txt
    sha256: 18ac4b6d2814a926f61529503883a577d4f5778fbc02a0441700745e6d7655d9
    role: context
  - path: .temp/pr2061/refresh397/sources/taxonomy.xml
    sha256: 66cddf8c5d2cda103b85df2eddb9937ad88e439a50cb9414d3b10c4552b9f829
    role: context
  - path: .temp/pr2061/refresh397/sources/web-assets.json
    sha256: 4250c08b141ef356b0fc55c9eac94f1044ac3af35cc4c8d336baaa7376a90d00
    role: context
  - path: .temp/pr2061/refresh397/started.json
    sha256: 125a7a7ef027a115a3a64643c3c26613004a265eaf435bac47499bc1b49ac4d5
    role: context
  - path: .temp/pr2061/refresh397/target-diff.patch
    sha256: 5f5977aba6e1e55d9119377bc8d8ae7adccaa5baf8f98367ab2c95be1ca3333e
    role: context
  - path: .temp/pr2061/refresh397/targets.json
    sha256: 5fe6b59a7c8a194f94ddaae557f1c9530094d26628ba01c5b14afdcd1e7de1b4
    role: context
  - path: .temp/pr2061/root-checks/audit-network.stderr
    sha256: a71fb29e950f3eaf0eb2b834a43c59d4a1b6aa85a2a89473ae99b0e408a27a36
    role: context
  - path: .temp/pr2061/root-checks/audit-network.stdout
    sha256: 1f337893714a80173f5b305ba0c11da1d8a3caf53f1060bd5acf2aa42b40aece
    role: context
  - path: .temp/pr2061/root-checks/check-network-quality.stderr
    sha256: e060873ec46d56a6fddbc2fe78b0d2f1438639923dd9f410686090ae4efa3aa3
    role: context
  - path: .temp/pr2061/root-checks/check-network-quality.stdout
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2061/root-checks/contracts.stderr
    sha256: 3c78da6b640c526eabf9a236bbdd4c569f4c4c3158dcf2972c817e175e9dc3b1
    role: context
  - path: .temp/pr2061/root-checks/contracts.stdout
    sha256: 0b77f334f09a1520b078f97c2847df576911190e4a6bf13f7bf99fdd098ada6f
    role: context
  - path: .temp/pr2061/root-checks/initial-checks.json
    sha256: 31ce4f0855ea80c212fca3b2efd608e489e78ec75855232f9863931c342abea2
    role: context
  - path: .temp/pr2061/root-checks/native.stderr
    sha256: e948da1cfe774485c5a8d36849ac71a894c7899192ba8c72909995dd668c8f75
    role: context
  - path: .temp/pr2061/root-checks/native.stdout
    sha256: 0be86c22677771fd2f43c5d1ee5bee7718a414e845fb0586fa59373741a8c8ef
    role: context
  - path: .temp/pr2061/staleness.json
    sha256: 0c87693a92639201293b3ac62d6df276ff667849400f456f0c6a38861e772c25
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
  - path: history/records/Defined_ThreeStrain_Organic_Nitrogen_Nitrifying_Community/2026-09-20T191942Z-claude-code-4905aa.yaml
    sha256: 122732c407ccb2a0a58020c25219384c6204f8ce7a7f5e56a26d0b6a1a2e400f
    role: context
  - path: history/records/Defined_ThreeStrain_Organic_Nitrogen_Nitrifying_Community/2026-09-20T192210Z-claude-code-fcd5a0.yaml
    sha256: a841d7e498ef6266fb004e675984ab485fdc577211535bbd00db5a80cba504d5
    role: context
  - path: history/records/Defined_ThreeStrain_Organic_Nitrogen_Nitrifying_Community/2026-09-20T193925Z-claude-code-62165d.yaml
    sha256: 3fdb5db759f7f16756a32e1027c53cb01ca1198d192a0c9205dc598fdf73c77b
    role: context
  - path: history/records/Defined_ThreeStrain_Organic_Nitrogen_Nitrifying_Community/2026-10-31T234500Z-antigravity-2095.yaml
    sha256: a7511e88c03d8930a5ee37e9973d8d4273c49fa9a0668bec63f48439a5a479a7
    role: context
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: kb/communities/Defined_ThreeStrain_Organic_Nitrogen_Nitrifying_Community.yaml
    sha256: c70bbd5b522140d6b6cf6a2c4ea9ae97cdf10dda7d45534071997a5b1786dbcd
    role: target
  - path: references_cache/PMID_42668143.txt
    sha256: 534023632f8dd66866ee7d231899d31656d90877316f87f60448b2a3e2adc4c6
    role: context
  - path: reports/causal_graph_review/adversarial-review-20261006-batch27.yaml
    sha256: e643b8f12adfc71acdd4f9bca108689885b70c32ea93b44b1055d73f3022cad0
    role: context
  - path: reports/causal_graph_review/decisions/20261006-three-records-batch27.yaml
    sha256: 90e6a0ad3e095a1301744958f706782510d03bdf40852999837d12401019ded0
    role: context
  - path: reports/causal_graph_review/decisions/20261031-c4s5-review-remediation.yaml
    sha256: e94a577398d3f50a8446bf0ef63955bfee72b23626c21db30ac629af9ccd1b4f
    role: context
  - path: reviews/structured/20261021T101100Z-stage4-frozen-cohort-review/review.md
    sha256: e432615b147787c8d009d96d2f11e5b78a45927bf9c69e45ec0d31123d1fc2e9
    role: context
  - path: reviews/structured/20261021T101100Z-stage4-frozen-cohort-review/review.yaml
    sha256: 37d089fd55c077793dd20d868b50c47cb1cceab6dae6a82887cc938bee05fa6d
    role: context
  - path: reviews/structured/20261022T043046Z-defined-three-strain-nitrifying-record-review/review.md
    sha256: 515ff07fd06a4584db92626a0d9341f79872302763c90228383d627d96236689
    role: context
  - path: reviews/structured/20261022T043046Z-defined-three-strain-nitrifying-record-review/review.yaml
    sha256: 8661d3f3d66676898a08f730b914b44c1911641480683242e067e6f9ecd6b961
    role: context
  - path: reviews/structured/20261031T200000Z-c4s4-record-deep-audit/review.yaml
    sha256: 32b1343c3fc88618d1f00c03b2bee744447ca770c21b2e47438de8753f2339ac
    role: context
  - path: reviews/structured/20261031T200100Z-c4s4-frozen-cohort-review/review.yaml
    sha256: 1364a3486fba6c55bdd0d7d8547bce86b09c1f8bd9df10fd5b83164154975a1a
    role: context
  - path: reviews/structured/20261031T235500Z-c4s5-remediation-verification/review.yaml
    sha256: 3a41e2e9b271073123031559f91a5d64b08ac7da92fdf1c71dedf54746648e86
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
  - path: scripts/adhoc/pr2058_294_refresh.py
    sha256: 9736f264aaf98ad1b14310160e25f293a3ba5e838a3b889338a295db7e92523b
    role: context
  - path: scripts/adhoc/pr2061_397_refresh.py
    sha256: 32cb4f53e9de703301b43bd313d723646e731876710f3e5150128dd6b73a33be
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
  - path: src/communitymech/ontology_adapters.py
    sha256: 24fc4f6d5b786a15f38194ed902e9b7941e30c17f001532598e20e2898f595a0
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
- target_id: CommunityMech:000397
  path: kb/communities/Defined_ThreeStrain_Organic_Nitrogen_Nitrifying_Community.yaml
  label: Defined Three-Strain Organic-Nitrogen Nitrifying Community
  kind: maintained
  record_class: MicrobialCommunity
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Defined_ThreeStrain_Organic_Nitrogen_Nitrifying_Community.yaml
    role: canonical_record
scope:
  description: Whole current maintained record, exact main delta, original findings/actions,
    accessible primary/SI/graphic, relevant current stock/taxonomic authorities, history
    and native controls; main manuscript unavailable.
  selection: 'Only stale CommunityMech:000397 in PR #2061; other records and other
    review finding heads are not superseded.'
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000397
checks:
- check_id: validate
  name: validate
  status: passed
  required: true
  summary: Actual current command exit 0.
  target_ids:
  - CommunityMech:000397
  command: just --no-dotenv validate kb/communities/Defined_ThreeStrain_Organic_Nitrogen_Nitrifying_Community.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate
  scope_note: Focused record/history; cache-name preflight is corpus-wide.
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Actual current command exit 0.
  target_ids:
  - CommunityMech:000397
  command: just --no-dotenv validate-strict kb/communities/Defined_ThreeStrain_Organic_Nitrogen_Nitrifying_Community.yaml
    --out .temp/pr2061/refresh397/checks/strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-strict
  scope_note: Focused record/history; cache-name preflight is corpus-wide.
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Actual current command exit 0.
  target_ids:
  - CommunityMech:000397
  command: just --no-dotenv validate-terms kb/communities/Defined_ThreeStrain_Organic_Nitrogen_Nitrifying_Community.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-terms
  scope_note: Focused record/history; cache-name preflight is corpus-wide.
- check_id: validate-references-explained
  name: validate-references-explained
  status: passed
  required: true
  summary: Actual current command exit 0.
  target_ids:
  - CommunityMech:000397
  command: just --no-dotenv validate-references-explained kb/communities/Defined_ThreeStrain_Organic_Nitrogen_Nitrifying_Community.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-references-explained
  scope_note: Focused record/history; cache-name preflight is corpus-wide.
- check_id: validate-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: Actual current command exit 0.
  target_ids:
  - CommunityMech:000397
  command: just --no-dotenv validate-gtdb kb/communities/Defined_ThreeStrain_Organic_Nitrogen_Nitrifying_Community.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb
  scope_note: Focused record/history; cache-name preflight is corpus-wide.
- check_id: validate-gtdb-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: Actual current command exit 0.
  target_ids:
  - CommunityMech:000397
  command: just --no-dotenv validate-gtdb-domain kb/communities/Defined_ThreeStrain_Organic_Nitrogen_Nitrifying_Community.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb-domain
  scope_note: Focused record/history; cache-name preflight is corpus-wide.
- check_id: validate-history
  name: validate-history
  status: passed
  required: true
  summary: Actual current command exit 0.
  target_ids:
  - CommunityMech:000397
  command: just --no-dotenv validate-history history/records/Defined_ThreeStrain_Organic_Nitrogen_Nitrifying_Community
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-history
  scope_note: Focused record/history; cache-name preflight is corpus-wide.
- check_id: cache-name-check
  name: cache-name-check
  status: passed
  required: true
  summary: Actual current command exit 0.
  target_ids:
  - CommunityMech:000397
  command: /Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.venv/bin/python
    scripts/normalize_cache_names.py --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-cache-name-check
  scope_note: Focused record/history; cache-name preflight is corpus-wide.
- check_id: audit-network
  name: audit-network
  status: failed
  required: false
  summary: 'Shared current corpus run: 48 warnings in 17 of 510 records, zero errors,
    actual exit 1; existing warning baseline retained.'
  command: just --no-dotenv audit-network
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - corpus
  target_ids:
  - CommunityMech:000397
  scope_note: Parent-owned full corpus run, not a new author invocation.
- check_id: check-network-quality
  name: check-network-quality
  status: failed
  required: false
  summary: 'Shared current corpus run: 48 warnings in 17 of 510 records, zero errors,
    actual exit 1; existing warning baseline retained.'
  command: just --no-dotenv check-network-quality
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - corpus
  target_ids:
  - CommunityMech:000397
  scope_note: Parent-owned full corpus run, not a new author invocation.
evidence:
- evidence_id: record
  kind: record_content
  reference: kb/communities/Defined_ThreeStrain_Organic_Nitrogen_Nitrifying_Community.yaml
  locator: Whole current maintained YAML
  summary: Three defined NBRC stocks, one aggregate conversion node, no downstream
    arrows; only roles, abundance categories and October 31 history changed.
  support: supports
  accessed_at: '2026-11-06T19:17:07.036478Z'
  snapshot_sha256: c70bbd5b522140d6b6cf6a2c4ea9ae97cdf10dda7d45534071997a5b1786dbcd
- evidence_id: abstract
  kind: primary_source
  reference: .temp/pr2061/refresh397/sources/epmc.json
  locator: PMID:42668143 / DOI:10.1093/bbb/zbag131; full MED abstract and metadata
  summary: The three stocks, selected-condition nitrate endpoint and relative-abundance
    association are reported; carbon fixation is not a focal reported measurement.
  support: supports
  accessed_at: '2026-11-06T19:17:07.036478Z'
  snapshot_sha256: e1ac6d2e6801fd7b51363841bb0f4903fdeb4a2b518e64f95c21f47c3cb475f8
- evidence_id: publisher
  kind: primary_source
  reference: .temp/pr2061/refresh397/sources/publisher-web.txt
  locator: Public publisher Abstract and access notice; web-tool response captured
    locally
  summary: The article identity matches. The public page exposes abstract, graphical
    abstract and supplementary link but states no access to the main article.
  support: supports
  accessed_at: '2026-11-06T19:17:07.036478Z'
  snapshot_sha256: 3278cf3d240f3ae44f6af4fed42e2392b59de8a6b89273693f1496555aa4a056
- evidence_id: supplement
  kind: primary_source
  reference: .temp/pr2061/refresh397/sources/supplement.pdf
  locator: 'All three physical PDF pages: Figures S1, S2 and S3'
  summary: S1 repeat/refeeding, S2 Polypepton NF and delayed-inoculation arms, and
    S3 separate-isolate media/temperature tests were read and visually checked. These
    do not supply the complete focal protocol.
  support: supports
  accessed_at: '2026-11-06T19:17:07.036478Z'
  snapshot_sha256: e42576f83d113d7f1e546913483f1ac35628a3d28cc365abd3456b6428a36d3d
- evidence_id: graphical
  kind: primary_source
  reference: .temp/pr2061/refresh397/sources/graphical.jpeg
  locator: Named three-stock conversion schematic and nitrogen/estimated-ratio time
    course
  summary: The schematic supports organic-N transformation and sequential ammonium/nitrite
    utilization. It neither depicts carbon fixation nor establishes equal or time-invariant
    cell fractions.
  support: supports
  accessed_at: '2026-11-06T19:17:07.036478Z'
  snapshot_sha256: 178e3488b4a2c40f8eef5aedfe0428beef3e50ed7648ff8758a26cdc73a8f98e
- evidence_id: stock-carbon
  kind: authority
  reference: .temp/pr2061/refresh397/sources/nedo-carbon-stocks.pdf
  locator: 'Printed slide 34, PDF physical page 35: NITE CO2-fixing stock list'
  summary: NBRC 14298 and 14297 appear in NITE's CO2-fixing-stock list. This is background
    stock-capability context, not measured carbon flux in the 2026 coculture.
  support: supports
  accessed_at: '2026-11-06T19:17:07.036478Z'
  snapshot_sha256: 4aeb9850f88b151ca4646dcfc4c8d88abd0a03ec51015dd85a03c6a8f32a62c5
- evidence_id: stock-15713
  kind: authority
  reference: .temp/pr2061/refresh397/sources/nbrc-15713.html
  locator: NBRC 15713 exact stock catalogue
  summary: The stock identity resolves. Collection-maintenance conditions and stock
    sequence links are not the focal community protocol or study deposits.
  support: supports
  accessed_at: '2026-11-06T19:17:07.036478Z'
  snapshot_sha256: 9694496131c425997b3437fdaa1584fefb4a72a62a35e1381faf69784e991a0b
- evidence_id: stock-14298
  kind: authority
  reference: .temp/pr2061/refresh397/sources/nbrc-14298.html
  locator: NBRC 14298 exact stock catalogue
  summary: The stock identity resolves. Collection-maintenance conditions and stock
    sequence links are not the focal community protocol or study deposits.
  support: supports
  accessed_at: '2026-11-06T19:17:07.036478Z'
  snapshot_sha256: b6d70996595c0e315ed14cc144822b78a40ed5f7349f70032ce98f5f10335166
- evidence_id: stock-14297
  kind: authority
  reference: .temp/pr2061/refresh397/sources/nbrc-14297.html
  locator: NBRC 14297 exact stock catalogue
  summary: The stock identity resolves. Collection-maintenance conditions and stock
    sequence links are not the focal community protocol or study deposits.
  support: supports
  accessed_at: '2026-11-06T19:17:07.036478Z'
  snapshot_sha256: 99bdda1ea1469903ce8200f4425acf017b09ae13db956c166a139ed200f14380
- evidence_id: taxonomy
  kind: authority
  reference: .temp/pr2061/refresh397/sources/taxonomy.xml
  locator: Fresh NCBI taxonomy efetch entries 1455, 915 and 913
  summary: All three species labels resolve; Bacillus badius is a synonym of Pseudobacillus
    badius. Species identity does not certify an exact experimental genome.
  support: supports
  accessed_at: '2026-11-06T19:17:07.036478Z'
  snapshot_sha256: 66cddf8c5d2cda103b85df2eddb9937ad88e439a50cb9414d3b10c4552b9f829
- evidence_id: gtdb
  kind: authority
  reference: .temp/pr2061/refresh397/gtdb.stdout
  locator: Actual current community-mode lookup against the locally copied crosswalk
  summary: Pseudobacillus badius resolves by exact species ID at 1.0/26, Nitrosomonas
    europaea by species name at 1.0/2, and Nitrobacter winogradskyi_A by ID at 0.88/8.
    Existing upstream release/build wording is not established by a filesystem mtime.
  support: supports
  accessed_at: '2026-11-06T19:17:07.036478Z'
  snapshot_sha256: 7f6ff0139743e2b84bfd38e41039b562a67d368232a19cb11e53b201aba9a96b
- evidence_id: crosswalk
  kind: validation
  reference: .temp/pr2061/refresh397/gtdb-copy.json
  locator: Source/copy SHA256 equality
  summary: The source and local copy both hash to 761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd;
    no new release date is inferred.
  support: supports
  accessed_at: '2026-11-06T19:17:07.036478Z'
  snapshot_sha256: ce4df46aaba541157006058f98f9f16fcbf6dcaa257262e305029f05296bfafd
- evidence_id: schema
  kind: authority
  reference: src/communitymech/schema/communitymech.yaml
  locator: AbundanceEnum, FunctionalRoleEnum, community, interaction and optional
    context slots
  summary: ABUNDANT is qualitative major-member prominence, PRIMARY_PRODUCER means
    carbon fixation, and optional fields do not become mandatory merely because the
    schema permits them.
  support: supports
  accessed_at: '2026-11-06T19:17:07.036478Z'
  snapshot_sha256: 7355e14f0f17c5d3b875abd33af6474ddc1aad08cc3305313686fede337e259a
- evidence_id: snippets
  kind: validation
  reference: .temp/pr2061/refresh397/snippet-audit.json
  locator: All 18 canonical snippet placements
  summary: Seventeen placements match the fresh abstract and the remaining placement
    is exact DOI metadata; all 18 match the committed abstract cache. Lexical agreement
    does not prove the newly added carbon-fixation role.
  support: supports
  accessed_at: '2026-11-06T19:17:07.036478Z'
  snapshot_sha256: 8c50749b3e188e094daa6fd0b663c1f357cb79436c7ca894872f117a891aae1c
- evidence_id: predecessor
  kind: prior_review
  reference: reviews/structured/20261022T043046Z-defined-three-strain-nitrifying-record-review/review.yaml
  locator: Original two findings and three actions / eight acceptance checks
  summary: Both original finding keys and every original acceptance check are retained;
    the historical source-access limits are not rewritten.
  support: supports
  accessed_at: '2026-11-06T19:17:07.036478Z'
  snapshot_sha256: 8661d3f3d66676898a08f730b914b44c1911641480683242e067e6f9ecd6b961
- evidence_id: lineage
  kind: prior_review
  reference: .temp/pr2061/refresh397/lineage-context.json
  locator: Ignored-inclusive discovery of exact 397 finding occurrences
  summary: The Cycle 4 presence finding has its own resolved successor. This observation
    preserves that narrow presence disposition while assessing the new annotation's
    evidence separately.
  support: supports
  accessed_at: '2026-11-06T19:17:07.036478Z'
  snapshot_sha256: 78dc8c96ac27dfba946f8abd758ae698e1576dbfeef8f88abd8f8d0e8ed0e8c3
- evidence_id: history
  kind: record_content
  reference: history/records/Defined_ThreeStrain_Organic_Nitrogen_Nitrifying_Community/2026-10-31T234500Z-antigravity-2095.yaml
  locator: events[0] details and matching canonical curation_history[3]
  summary: The history accurately records the added enum values; its focal PMID citation
    does not supply separate carbon-fixation proof. No old history is edited.
  support: supports
  accessed_at: '2026-11-06T19:17:07.036478Z'
  snapshot_sha256: a7511e88c03d8930a5ee37e9973d8d4273c49fa9a0668bec63f48439a5a479a7
- evidence_id: delta
  kind: validation
  reference: .temp/pr2061/refresh397/target-diff.patch
  locator: Original PR head to integrated current-main target diff
  summary: Five role assignments, three abundance categories and one inline history
    event were added; all original experimental claims and evidence snippets are unchanged.
  support: supports
  accessed_at: '2026-11-06T19:17:07.036478Z'
  snapshot_sha256: 5f5977aba6e1e55d9119377bc8d8ae7adccaa5baf8f98367ab2c95be1ca3333e
- evidence_id: reading
  kind: validation
  reference: .temp/pr2061/refresh397/source-reading.json
  locator: Author's actual source reading and bounded-access notes
  summary: Author read the complete current record, predecessor, fresh abstract, all
    three SI pages, graphical abstract, exact stock/NCBI authority, relevant NITE
    slide and local checks. This is not independent approval.
  support: supports
  accessed_at: '2026-11-06T19:17:07.036478Z'
  snapshot_sha256: 22ca6117e8cb60cbfcd73f2e7e23dcaec2ab63585357497ed5062a1b0ed0f756
- evidence_id: checks
  kind: validation
  reference: .temp/pr2061/refresh397/checks/focused-checks.json
  locator: Eight actual focused command/exit/stdout/stderr receipts
  summary: All eight focused checks exited 0. They do not establish scientific completion.
  support: supports
  accessed_at: '2026-11-06T19:17:07.036478Z'
  snapshot_sha256: d2a909f9ced2b6b98b1d7d074dff827d98983b456b77bc763a4c1509a5b54bcd
- evidence_id: corpus
  kind: validation
  reference: .temp/pr2061/root-checks/initial-checks.json
  locator: Parent-run current full-corpus diagnostics and native controls
  summary: Both network diagnostics returned exit 1 with 48 warnings across 17 of
    510 records and zero errors; these are nonrequired context. The author reuses
    the recorded parent run rather than claiming to rerun it.
  support: supports
  accessed_at: '2026-11-06T19:17:07.036478Z'
  snapshot_sha256: 31ce4f0855ea80c212fca3b2efd608e489e78ec75855232f9863931c342abea2
- evidence_id: check-validate
  kind: validation
  reference: .temp/pr2061/refresh397/checks/validate.json
  locator: Actual focused command and output paths
  summary: Actual exit 0; output artifacts are independently pinned.
  support: supports
  accessed_at: '2026-11-06T19:17:07.036478Z'
  snapshot_sha256: 2e40841d3b141430a01558396dd008b9621859f7ca056f3796048591e23d8e49
- evidence_id: check-validate-strict
  kind: validation
  reference: .temp/pr2061/refresh397/checks/validate-strict.json
  locator: Actual focused command and output paths
  summary: Actual exit 0; output artifacts are independently pinned.
  support: supports
  accessed_at: '2026-11-06T19:17:07.036478Z'
  snapshot_sha256: 4a3405de1536712af00296240aa48e8078b4c26475293a07c22f49256b621d9c
- evidence_id: check-validate-terms
  kind: validation
  reference: .temp/pr2061/refresh397/checks/validate-terms.json
  locator: Actual focused command and output paths
  summary: Actual exit 0; output artifacts are independently pinned.
  support: supports
  accessed_at: '2026-11-06T19:17:07.036478Z'
  snapshot_sha256: f1f21f8d5bf07ed0401fb9e3264f67ad67439964c784e26d3cf3da7eff13dde5
- evidence_id: check-validate-references-explained
  kind: validation
  reference: .temp/pr2061/refresh397/checks/validate-references-explained.json
  locator: Actual focused command and output paths
  summary: Actual exit 0; output artifacts are independently pinned.
  support: supports
  accessed_at: '2026-11-06T19:17:07.036478Z'
  snapshot_sha256: 1c8558e5ca7c3a48b366fbbfc9a8515982b203cea7b7769fd25edd87c626565d
- evidence_id: check-validate-gtdb
  kind: validation
  reference: .temp/pr2061/refresh397/checks/validate-gtdb.json
  locator: Actual focused command and output paths
  summary: Actual exit 0; output artifacts are independently pinned.
  support: supports
  accessed_at: '2026-11-06T19:17:07.036478Z'
  snapshot_sha256: cb24211e99cddd348912aa47ff870df7ae65947395b24e7d8bdd456cf84b5bf0
- evidence_id: check-validate-gtdb-domain
  kind: validation
  reference: .temp/pr2061/refresh397/checks/validate-gtdb-domain.json
  locator: Actual focused command and output paths
  summary: Actual exit 0; output artifacts are independently pinned.
  support: supports
  accessed_at: '2026-11-06T19:17:07.036478Z'
  snapshot_sha256: f3c564bf7cbd18b78fca2032dee3466604bb74cc76493a8ff066a2abbff74f1f
- evidence_id: check-validate-history
  kind: validation
  reference: .temp/pr2061/refresh397/checks/validate-history.json
  locator: Actual focused command and output paths
  summary: Actual exit 0; output artifacts are independently pinned.
  support: supports
  accessed_at: '2026-11-06T19:17:07.036478Z'
  snapshot_sha256: c322027c1e4c372e4675702b7996b478c330036e8a44517c3cb4980dace92238
- evidence_id: check-cache-name-check
  kind: validation
  reference: .temp/pr2061/refresh397/checks/cache-name-check.json
  locator: Actual focused command and output paths
  summary: Actual exit 0; output artifacts are independently pinned.
  support: supports
  accessed_at: '2026-11-06T19:17:07.036478Z'
  snapshot_sha256: ae807705066c385d30205b41a672f535c825db2059cb911a8614ee92af1bfba5
assessments:
- assessment_id: identity
  area: identity
  topic: Three-stock laboratory model
  outcome: supported
  summary: The three source-named NBRC stocks remain a defined engineered laboratory
    community.
  target_ids:
  - CommunityMech:000397
  evidence_ids:
  - record
  - abstract
  - taxonomy
  - stock-15713
  - stock-14298
  - stock-14297
  details: Retain SYNTHETIC origin, ENGINEERED state and BIOTECHNOLOGY category. Source
    Bacillus badius and canonical Pseudobacillus badius refer to the same species;
    NBRC stock descriptors are distinct from species/genome classification. The soil
    analogy in the graphical abstract is not a natural origin or a live host experiment.
  dimensions:
  - name: taxon_scope
    value: NBRC 15713, 14298 and 14297
    definition: Three exact collection stocks within their current NCBI species; no
      experimental-genome reassignment.
    evidence_ids:
    - taxonomy
    - stock-15713
    - stock-14298
    - stock-14297
  - name: experimental_setting
    value: Selected organic-nitrogen laboratory coculture
    definition: Engineered model; source diagram's soil comparison is not the culture
      environment.
    evidence_ids:
    - abstract
    - graphical
- assessment_id: node-0
  area: graph
  topic: Sequential organic-nitrogen conversion
  outcome: supported
  summary: Retain the single community-level CROSS_FEEDING node and its bounded selected-condition
    outcome.
  target_ids:
  - CommunityMech:000397
  evidence_ids:
  - record
  - abstract
  - graphical
  - supplement
  - snippets
  details: Exact selector ecological_interactions[0]. All three participating taxa
    are canonical members, no pairwise source/target or downstream arrows are encoded.
    The two SUPPORT / IN_VITRO snippets are the abstract's construction and endpoint
    statements, hashes 0a1d0d1dfaa1379ba9df48f9ff7cde142aa2368507165e66cab0b42214c443c4
    and 4faa31e56824f4e0abc9b81d22331b4d573b7b3e6deb98a8b1b0782dd5402b0a. Graphical
    arrows assign organic N to ammonium to nitrite to nitrate at the named functional
    stages. Retain aggregate sequential exchange without inferring donor-resolved
    flux, obligate reciprocity, necessity or all-substrate success. GO:0019329 ammonia
    oxidation denotes one component; ammonium/nitrite/nitrate CHEBI ions retain mg-N/L
    nitrogen-equivalent units.
- assessment_id: new-annotations
  area: evidence
  topic: Added roles and qualitative abundance
  outcome: concern
  summary: Nitrogen roles and qualitative major-partner prominence are supportable;
    the carbon-fixation role needs its own bounded evidence.
  target_ids:
  - CommunityMech:000397
  evidence_ids:
  - delta
  - abstract
  - graphical
  - supplement
  - stock-carbon
  - schema
  - history
  details: PRIMARY_DEGRADER for B. badius fits the organic-N/Polypepton transformation
    and CROSS_FEEDER for the nitrifiers fits successive intermediate utilization.
    ABUNDANT is accepted only as qualitative prominence of these three central partners,
    not a percentage band, equal proportions, a fixed inoculum ratio or stability
    across days/arms. The graphical estimated-ratio time series and S1 absolute counts
    do not establish those stronger claims. PRIMARY_PRODUCER specifically means fixes
    carbon; the local taxon evidence currently quotes membership and nitrifier abundance
    association from the focal abstract, which does not make that assertion. NITE's
    exact-stock list supports background capacity, not focal community carbon flux;
    this narrows the new finding to local evidence/provenance rather than false organism
    identity or disproven physiology.
- assessment_id: cultivation
  area: completeness
  topic: Supplementary context and unresolved main protocol
  outcome: concern
  summary: The original supplementary-cultivation finding remains open with all three
    acceptance checks.
  target_ids:
  - CommunityMech:000397
  evidence_ids:
  - supplement
  - publisher
  - predecessor
  details: S2 physical page 2 supports 2 g/L Polypepton NF and separately the nitrifiers'
    inoculation two days after B. badius. S1 physical page 1 supports repeated culture
    using post-nitrification cells and day 3 feeding. S3 physical page 3 concerns
    separate nitrifier cultures in HEPES/Boon media over 20–37 degrees C; it cannot
    supply a common community temperature. Main Figure 4(d), basal recipe, inoculum
    ratio, atmosphere and vessel remain unread or unresolved. Preserve the dated organic_nitrogen_cultivation_details
    KNOWLEDGE_GAP and trace later recovery; do not treat a schematic flask or collection
    maintenance recipe as the experimental protocol.
  dimensions:
  - name: medium
    value: S2 Polypepton NF 2 g/L; basal community formulation unresolved
    definition: Arm-specific supplementary condition, not a universal recipe or proven
      mapping to the 56 mg-N/L abstract arm.
    evidence_ids:
    - supplement
  - name: environmental_context
    value: ENVO:01001405 laboratory environment
    definition: No mandatory host or soil annotation is inferred from optional current
      slots or an illustrative soil comparison.
    evidence_ids:
    - record
    - graphical
    - schema
- assessment_id: gtdb
  area: grounding
  topic: Species mapping and immutable provenance
  outcome: concern
  summary: The original mapping-completion and provenance finding remains open with
    exact existing acceptance.
  target_ids:
  - CommunityMech:000397
  evidence_ids:
  - gtdb
  - crosswalk
  - taxonomy
  - predecessor
  details: Fresh community-mode lookup reproduces all three mapping routes and denominators
    in the original action. Retain the Nitrobacter name difference as a name comparison,
    not a new taxonomic event. The copied crosswalk is byte-identical to the external
    source; its local mtime is not an upstream release/build date.
- assessment_id: resources
  area: evidence
  topic: Publication and source/cache boundaries
  outcome: supported
  summary: Both publication identifiers and all 18 existing snippets remain valid
    at their actual source tiers.
  target_ids:
  - CommunityMech:000397
  evidence_ids:
  - abstract
  - publisher
  - snippets
  - reading
  details: No full main-paper or raw dataset review is claimed. The cache is plain
    PubMed-format abstract text with no false full-text content_type claim. The inspected
    public abstract/SI/graphic declares no focal data deposit; main availability is
    unknown. Stock genome links are not silently promoted to focal deposits. No separate
    cache repair is inferred from successful fresh-source access. iModulonDB is not
    applicable because no gene, locus, regulator, pathway dataset or expression module
    is named in this target.
- assessment_id: lineage
  area: provenance
  topic: Exact predecessor retention and Cycle 4 context
  outcome: supported
  summary: Both original open findings are explicitly continued; the separate Cycle
    4 missing-field disposition is not reopened or superseded.
  target_ids:
  - CommunityMech:000397
  evidence_ids:
  - predecessor
  - lineage
  - history
  - delta
  details: The October 31 enum additions satisfy the historical field-presence observation.
    This refresh does not retire, reopen or scientifically re-review other targets
    in the Cycle 4 reports. It separately distinguishes field presence from claim-local
    carbon-fixation support. All four history sidecars and inline events remain immutable;
    a later authorized curation must append its own exact source/claim scope.
- assessment_id: native
  area: schema
  topic: Current focused validation and corpus context
  outcome: supported
  summary: Eight focused checks passed; current shared network warnings remain explicit.
  target_ids:
  - CommunityMech:000397
  evidence_ids:
  - checks
  - corpus
  - schema
  details: Passing schema, strict, labels, references, GTDB/domain, history and cache
    naming checks do not complete an access-limited scientific review. The historical
    44-warning/477-record baseline is not reused as current; current parent receipts
    show 48 warnings across 17 of 510 records and no errors.
- assessment_id: access
  area: scope
  topic: Actual author reading and unavailable main
  outcome: unknown
  summary: The refresh remains partial and scientific_review is false.
  target_ids:
  - CommunityMech:000397
  evidence_ids:
  - reading
  - publisher
  - supplement
  details: The accessible abstract, all three SI pages, graphical abstract and relevant
    authority pages were read. Main Methods/results, main figures and full treatment
    comparisons remain unavailable through the bounded public routes used. No paid
    access, contact, experiments, digitization or raw-data reanalysis occurred.
- assessment_id: metrics
  area: completeness
  topic: Literal native metrics
  outcome: supported
  summary: Completeness is 65; raw validation quality is 129 and capped quality is
    100.
  target_ids:
  - CommunityMech:000397
  evidence_ids:
  - record
  - schema
  - corpus
  - checks
  details: These are structural rubric values, not evidence strength. Adding roles
    raises the literal required-field block while the new local evidence gap remains
    open.
  metrics:
  - name: completeness
    value: 65
    unit: points
    minimum: 0
    maximum: 100
    definition: Required field/role block 50 + environment 5 + external resources
      5 + interaction metabolites 5; fewer than 3 factors/nodes and absent growth_media/datasets
      add 0.
  - name: validation_quality
    value: 100
    unit: points
    minimum: 0
    maximum: 100
    definition: 100 - 0 P1*50 - 0 P2*10 - 3 P3*2 + 20*min((2 evidence/1 node)/2,1)
      + 15 structural COMPLETE = 129 raw, capped at 100. One node, zero arrows; the
      corpus network auditor reports no focal issue.
  - name: P1
    value: 0
    unit: findings
    definition: Native severity count in this scoped successor.
  - name: P2
    value: 0
    unit: findings
    definition: Native severity count in this scoped successor.
  - name: P3
    value: 3
    unit: findings
    definition: Native severity count in this scoped successor.
  - name: P4
    value: 0
    unit: findings
    definition: Native severity count in this scoped successor.
findings:
- finding_id: cultivation-context
  issue_key: cm-000397-cultivation-context
  category: completeness
  severity: minor
  native_severity: P3
  normalization_reason: Bounded recoverable context or provenance; the existing selected-condition
    community identity and outcomes remain supported.
  rule_id: review-checklist.claim-specific-support-and-context
  status: open
  certainty: confirmed
  title: Recover supplementary cultivation context while keeping the main-protocol
    gap
  description: The open discussion accurately described the cached abstract. Accessible
    S1/S2 now provide bounded assay information that the record does not capture;
    this supports enrichment rather than inventing a complete recipe.
  target_ids:
  - CommunityMech:000397
  field_paths:
  - discussions[0]
  - environmental_factors[0]
  - engineering_design.assembly_strategy
  - growth_media
  - cultivation_setup
  evidence_ids:
  - supplement
  - publisher
  - reading
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Defined_ThreeStrain_Organic_Nitrogen_Nitrifying_Community.yaml
    role: canonical_record
  ownership_note: The maintained record owns future authorized curation; this successor
    preserves the exact original finding and all original action acceptance checks.
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261022T043046Z-defined-three-strain-nitrifying-record-review
    finding_id: cultivation-context
- finding_id: gtdb-provenance
  issue_key: cm-000397-gtdb-provenance
  category: provenance
  severity: minor
  native_severity: P3
  normalization_reason: Bounded recoverable context or provenance; the existing selected-condition
    community identity and outcomes remain supported.
  rule_id: review-checklist.claim-specific-support-and-context
  status: open
  certainty: confirmed
  title: Complete the recoverable species mapping and correct provenance
  description: Pseudobacillus badius is currently resolvable. The valid two existing
    GTDB cores carry unsupported latest-release/build-date wording inferred from a
    local snapshot mtime.
  target_ids:
  - CommunityMech:000397
  field_paths:
  - taxonomy[0].taxon_term.gtdb_grounding_status
  - taxonomy[0].taxon_term
  - taxonomy[1].taxon_term.gtdb_classification.mapping_source
  - taxonomy[2].taxon_term.gtdb_classification.mapping_source
  evidence_ids:
  - gtdb
  - crosswalk
  - taxonomy
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Defined_ThreeStrain_Organic_Nitrogen_Nitrifying_Community.yaml
    role: canonical_record
  ownership_note: The maintained record owns future authorized curation; this successor
    preserves the exact original finding and all original action acceptance checks.
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261022T043046Z-defined-three-strain-nitrifying-record-review
    finding_id: gtdb-provenance
- finding_id: carbon-role-evidence
  issue_key: cm-000397-carbon-role-evidence-scope
  category: evidence
  severity: minor
  native_severity: P3
  normalization_reason: 'Bounded claim-local evidence/provenance gap: exact-stock
    authority supports background capacity, but the focal nitrogen-study evidence
    does not itself establish carbon fixation in this community. No identity failure
    or disproven physiology is asserted.'
  rule_id: review-checklist.claim-specific-support-and-context
  status: open
  certainty: confirmed
  title: Separate background carbon-fixation capacity from focal nitrogen evidence
  description: taxonomy[1] and taxonomy[2] now include PRIMARY_PRODUCER, defined as
    carbon fixation, while their local PMID:42668143 evidence quotes only membership
    and nitrifier abundance association. The accessible focal abstract, graphical
    abstract and SI do not report carbon-fixation flux. NITE's exact-stock CO2-fixing
    list supports background capacity, which requires its own source and scope if
    retained; it is not a focal in-vitro carbon-flux result.
  target_ids:
  - CommunityMech:000397
  field_paths:
  - taxonomy[1].functional_role
  - taxonomy[1].evidence
  - taxonomy[2].functional_role
  - taxonomy[2].evidence
  evidence_ids:
  - record
  - abstract
  - graphical
  - supplement
  - stock-carbon
  - schema
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Defined_ThreeStrain_Organic_Nitrogen_Nitrifying_Community.yaml
    role: canonical_record
actions:
- action_id: enrich-cultivation
  description: Add the recovered supplementary assay context and narrow the remaining
    open gap.
  finding_ids:
  - cultivation-context
  target_ids:
  - CommunityMech:000397
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Defined_ThreeStrain_Organic_Nitrogen_Nitrifying_Community.yaml
    role: canonical_record
  acceptance_checks:
  - 'Cite Supplement Figure S2 caption, physical page 2: Polypepton NF 2 g/L and the
    separate arm with N. europaea NBRC 14298 and N. winogradskyi NBRC 14297 introduced
    two days after B. badius NBRC 15713. Do not assign either arm to the approximately
    56 mg-N/L abstract endpoint without main experimental mapping.'
  - Cite Figure S1 caption and physical page 1 feed arrow for transfer of post-nitrification
    cells to fresh medium and day 3 organic feeding. Preserve assay context without
    inventing operating mode, basal composition, feed quantity, inoculum ratio, atmosphere
    or vessel.
  - Keep the main protocol unresolved. Figure S3 HEPES/Boon media and 20–37°C tests
    concern separate isolates; NBRC maintenance media and the schematic flask cannot
    supply community conditions. Preserve the dated discussion rationale and add a
    traceable follow-up rather than rewriting historical facts.
- action_id: repair-gtdb
  description: Use current species-level mapping evidence and accurate snapshot provenance.
  finding_ids:
  - gtdb-provenance
  target_ids:
  - CommunityMech:000397
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Defined_ThreeStrain_Organic_Nitrogen_Nitrifying_Community.yaml
    role: canonical_record
  acceptance_checks:
  - For taxonomy[0].taxon_term, use GROUNDED with GTDB:s__Pseudobacillus_badius; lineage
    d__Bacteria;p__Bacillota;c__Bacilli;o__Bacillales_B;f__Domibacillaceae;g__Pseudobacillus;s__Pseudobacillus
    badius; NCBITaxon:1455, fraction 1.0,26 genomes, is_reclassified false, exact
    ncbi_id route.
  - Retain taxonomy[1] Nitrosomonas europaea via ncbi_name, fraction 1.0/2 genomes,
    and taxonomy[2] Nitrobacter winogradskyi_A via ncbi_id, fraction 0.88/8 genomes.
    Record mapping snapshot SHA256 761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd.
    Label filesystem mtime as mtime; leave unknown upstream release/build metadata
    unknown.
  - Species aggregates do not classify the exact experimental genome. Existing NBRC
    stock descriptors remain valid; optional finer NCBI terms require their own labels
    and mapping denominators rather than silent substitution.
- action_id: validate-curation
  description: Validate any separately authorized record repair.
  finding_ids:
  - cultivation-context
  - gtdb-provenance
  target_ids:
  - CommunityMech:000397
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Defined_ThreeStrain_Organic_Nitrogen_Nitrifying_Community.yaml
    role: canonical_record
  acceptance_checks:
  - Recheck exact source/treatment scope, ontology labels and excerpt support; run
    focused schema, strict, terms, explained references, GTDB/domain and history gates,
    then just gen-html and just check-docs-current for authorized record changes.
  - Preserve original source responses, caches, histories and prior decisions. This
    review changes no canonical record or scientific status and authorizes no contact,
    paid research, issue or Git mutation.
- action_id: scope-carbon-role-evidence
  description: Support or qualify the two optional PRIMARY_PRODUCER annotations without
    conflating background capacity and focal measured function.
  finding_ids:
  - carbon-role-evidence
  target_ids:
  - CommunityMech:000397
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Defined_ThreeStrain_Organic_Nitrogen_Nitrifying_Community.yaml
    role: canonical_record
  acceptance_checks:
  - For taxonomy[1] NBRC 14298 and taxonomy[2] NBRC 14297, inspect appropriate exact-stock
    physiological evidence and attach an allowed stable reference, exact snippet and
    honest evidence tier to any retained carbon-fixation role; otherwise omit or qualify
    the optional role without declaring the organisms incapable of carbon fixation.
  - Explicitly distinguish source-backed background stock capability from carbon fixation
    measured in the PMID:42668143 community. The inspected NITE stock list is printed
    slide 34 / PDF physical page 35; it cannot certify coculture carbon flux. Do not
    relabel the focal nitrogen-conversion abstract as carbon-fixation evidence.
  - Retain supported PRIMARY_DEGRADER/CROSS_FEEDER nitrogen roles and the bounded
    three-member identity. ABUNDANT remains qualitative major-partner prominence;
    infer no percentage threshold, equal proportions, fixed inoculum ratio or abundance
    stable across treatment/time.
  - For any separately authorized repair, append exact source/scope history while
    preserving the October 31 event, then run focused schema/strict/terms/references/GTDB/domain/history
    checks and regenerate/check derived docs. Keep unavailable main-protocol details
    explicitly unresolved.
limitations:
- Bounded ordinary public routes recovered the abstract, declared three-page supplement
  and graphical abstract, but not the main Methods/results or main figures. This is
  not a global assertion that no full text exists.
- The supplement does not identify the complete basal coculture recipe, common temperature,
  vessel, atmosphere or inoculum ratio, nor map the approximately 56 mg-N/L abstract
  outcome to its S2 arms. S3 is separate-isolate evidence.
- Supplement curves were visually inspected without digitization, statistical reanalysis
  or inferred detection limits. No raw sequence, assay dataset or taxon-specific flux
  was analyzed.
- The NITE/NEDO stock list is a background capability authority, not a substitute
  for focal community carbon-flux evidence. Exact stock physiology should be sourced
  and scoped before adding local support.
- The author reused parent-owned current corpus diagnostics with their true exit codes.
  This refresh is author work and is separately reviewed; no canonical record, cache,
  history or scientific status was changed.
related_reviews:
- repository: CultureBotAI/CommunityMech
  review_id: 20261022T043046Z-defined-three-strain-nitrifying-record-review
  relationship: Current-input successor retaining both original open findings and
    all action acceptance.
- repository: CultureBotAI/CommunityMech
  review_id: 20261031T235500Z-c4s5-remediation-verification
  relationship: 'Context only: preserve the narrow field-presence resolution; no finding
    disposition is superseded.'
notes:
- All original two keys, three actions and eight acceptance checks are retained; one
  additional key/action adds four checks. Original saved bundles remain immutable.
- All actual local inputs are native-pinned, including fresh sources, authority/validator
  receipts, helper, initial inspection and byte-identical GTDB copy. The final inspection,
  candidate and subsequent validation outputs are generated metadata, not circular
  inputs.
- 'No separate source-recovery action is invented: the existing cultivation action
  explicitly retains the main-protocol gap. No extra cache/header or study-deposit
  finding was established in the inspected source scope.'
tags:
- record-review
- nitrification
- syncom
- partial-source
- pr2061-current-main
```
