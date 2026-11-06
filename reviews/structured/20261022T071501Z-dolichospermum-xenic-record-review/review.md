# Dolichospermum FBCC-A233 xenic culture record review

- Review: 20261022T071501Z-dolichospermum-xenic-record-review
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-22T07:02:36.860177Z
- Finished UTC: 2026-10-22T07:15:01.070820Z
- Reviewer: codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The culture identity and two qualified genome-inferred cofactor observations are supported. One major finding concerns stability and associate abundance; three minor findings concern cultivation mode, GTDB classification scope and one excerpt capitalization. All eight required native checks passed. Completeness is 25; raw quality 119 is capped at 100.

## Scope And Provenance

Whole released record and primary article, all four main figures, complete S2/S4 and explicitly bounded S1/S3, local ontology/native checks and source-linked archive metadata.

Selection: Only released CommunityMech:000441 in owned batch 16.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base cb7a782c8ba80299dca8761ad0a2c90bccd8a117.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000441 | kb/communities/Dolichospermum_FBCC_A233_Xenic_Phycosphere_Community.yaml | maintained | Dolichospermum FBCC-A233 Xenic Phycosphere Community |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000441 | Actual native exit 0. |
| validate-strict | passed | True | CommunityMech:000441 | Actual native exit 0. |
| validate-terms | passed | True | CommunityMech:000441 | Actual native exit 0. |
| validate-references-explained | passed | True | CommunityMech:000441 | Actual native exit 0. |
| validate-gtdb | passed | True | CommunityMech:000441 | Actual native exit 0. |
| validate-gtdb-domain | passed | True | CommunityMech:000441 | Actual native exit 0. |
| validate-history | passed | True | CommunityMech:000441 | Actual native exit 0. |
| normalize-cache-names-check | passed | True | CommunityMech:000441 | Actual native exit 0. |
| audit-network corpus context | failed | False | CommunityMech:000441 | Actual corpus exit 1, zero structural errors. |
| check-network-quality corpus context | failed | False | CommunityMech:000441 | Actual corpus exit 1, zero structural errors. |
| Gene-specific structured source adapter | unavailable | False | CommunityMech:000441 | Runner unavailable in the owned runtime; actual gene queries identified. |

## Scientific And Domain Assessments

### Culture and recovered genome scope

identity: supported. Targets: CommunityMech:000441.

The record identifies the source-maintained FBCC-A233 xenic culture correctly.

NATURAL describes reservoir origin; the reviewed system is a laboratory-maintained unialgal xenic culture. The three recovered genomes are not an exhaustive environmental census or a defined three-isolate consortium. PRIMARY_PRODUCER is supported for the cyanobacterium; optional heterotroph roles are not invented.

### Stability and relative prominence

evidence: concern. Targets: CommunityMech:000441.

STABLE and unqualified associate RARE assignments exceed the method-resolved evidence.

The source expressly lacks longitudinal profiling. Sphingorhabdus has a low marker estimate (0.071254072%), while its genome maps 14.29% of trimmed reads; these metrics are not interchangeable. Brevundimonas has 5.37% genome mapping but no clear marker assignment. Mapping supports assemblies, not cell abundance or ecological non-driver status. Cyanobacterial DOMINANT remains qualitatively supported by the culture and dominant classified fraction. No percentage cutoff or forced replacement abundance is proposed.

### Genome-inferred biotin asymmetry

graph: supported. Targets: CommunityMech:000441.

Retain the qualified COMMUNITY_LEVEL computational observation.

Exact selector ecological_interactions[0]. No interaction_type, source_taxon, target_taxon or downstream direction is asserted. Participants: [{"preferred_term": "Dolichospermum flosaquae FBCC-A233", "term": {"id": "NCBITaxon:1166", "label": "Dolichospermum flos-aquae"}}, {"preferred_term": "Sphingorhabdus sp. FBCC-A233 associate", "term": {"id": "NCBITaxon:1434046", "label": "Sphingorhabdus"}}, {"preferred_term": "Brevundimonas sp. FBCC-A233 associate", "term": {"id": "NCBITaxon:41275", "label": "Brevundimonas"}}]. Exact canonical snippet bindings: [{"selector": "ecological_interactions[0].evidence[0].snippet", "sha256": "85d12b9c40d1f5c43a215fc40b6f220701161cb556cb1799921f925bffff0f08", "reference": "PMID:42535840", "supports": "PARTIAL", "evidence_source": "COMPUTATIONAL"}, {"selector": "ecological_interactions[0].evidence[1].snippet", "sha256": "b0e1fad0802e167706083b0fb8dee00a2714b17588dda84f67eb06478bb2f58c", "reference": "PMID:42535840", "supports": "PARTIAL", "evidence_source": "COMPUTATIONAL"}]. Source: PMID:42535840; DOI:10.1128/spectrum.01014-26. Locator: Results, Comparative genome architecture and genome-inferred metabolic potential across the three genomes, paragraph 3; Figures 2–3; Discussion paragraph 4; Tables S3–S4. BioU/bioF/bioD/bioB and biotin-utilization annotations support asymmetric potential. CHEBI biotin and GO vitamin biosynthesis are pathway context, not measured metabolite production. No complete biotin uptake machinery or growth rescue was demonstrated. PARTIAL evidence and explicit unresolved chemistry/transfer limits are appropriate.

### Genome-inferred corrinoid utilization asymmetry

graph: supported. Targets: CommunityMech:000441.

Retain the qualified COMMUNITY_LEVEL computational observation.

Exact selector ecological_interactions[1]. No interaction_type, source_taxon, target_taxon or downstream direction is asserted. Participants: [{"preferred_term": "Dolichospermum flosaquae FBCC-A233", "term": {"id": "NCBITaxon:1166", "label": "Dolichospermum flos-aquae"}}, {"preferred_term": "Sphingorhabdus sp. FBCC-A233 associate", "term": {"id": "NCBITaxon:1434046", "label": "Sphingorhabdus"}}, {"preferred_term": "Brevundimonas sp. FBCC-A233 associate", "term": {"id": "NCBITaxon:41275", "label": "Brevundimonas"}}]. Exact canonical snippet bindings: [{"selector": "ecological_interactions[1].evidence[0].snippet", "sha256": "90a61863d102edcef7bc72284ffa97b5674507b63605d5862c303a78c6753213", "reference": "PMID:42535840", "supports": "PARTIAL", "evidence_source": "COMPUTATIONAL"}, {"selector": "ecological_interactions[1].evidence[1].snippet", "sha256": "df771d948a11fcf7c5ae0ff89c979b134bdfd200c34b2f223c2d69a569b5488d", "reference": "PMID:42535840", "supports": "PARTIAL", "evidence_source": "COMPUTATIONAL"}]. Source: PMID:42535840; DOI:10.1128/spectrum.01014-26. Locator: Results, Comparative genome architecture and genome-inferred metabolic potential across the three genomes, paragraph 4; Figure 4; Discussion paragraph 4; Tables S3–S4. Most anaerobic corrinoid-ring genes coexist with an unresolved ring step and absent canonical DMB branch. metH in all three and metE in Sphingorhabdus support predicted repertoire differences. Candidate btuB/general TonB components and methionine uptake do not establish cobamide import or exchange. PARTIAL evidence and explicit unresolved chemistry/transfer limits are appropriate.

### Two parallel observations, zero arrows

graph: supported. Targets: CommunityMech:000441.

No causal arrow is supported or required between these predictions.

Both downstream lists are absent. No edge assessment is omitted; genome co-occurrence does not establish biotin-to-corrinoid causation, metabolite exchange, mutualism or syntrophy.

### Maintenance conditions and mode

evidence: concern. Targets: CommunityMech:000441.

BG11, temperature and illumination are supported; SEMI_CONTINUOUS is not established.

The source describes single-filament serial subculture at approximately ten-day intervals. It does not specify a draw-and-fill fraction, partial harvest, vessel geometry or working volume. OTHER with explicit maintenance notes is a conservative mode representation. Do not infer closed batch operation, a generic BG11 recipe, pH, aeration or shaking.

### NCBI descriptors and study-specific GTDB

grounding: concern. Targets: CommunityMech:000441.

All encoded IDs are valid; the paper supplies recoverable GTDB classifications.

Table 2 and Results classify the three study genomes under GTDB-Tk r226 as Dolichospermum flosaquae, Sphingorhabdus_B sp023910635 and Brevundimonas sp040380105. These are not automatically named-species NCBI replacements. RefSeq labels and ANI/dDDH differ from GTDB-Tk species clusters and ANI/alignment fractions. The local crosswalk separately maps Sphingorhabdus to genus Sphingorhabdus_B (27/27) and Brevundimonas to its genus (221/221), while the cyanobacterial name route has three alternatives. No local fallback overrides the actual FBCC-A233 genome analysis.

### Exact excerpts and genomic interpretation

evidence: concern. Targets: CommunityMech:000441.

One initial-capitalization discrepancy needs a verbatim repair.

The discussion correctly states that exchange is unproven, but its excerpt changes lowercase these to These. All other eighteen placements strictly match fresh source and cache. Native reference validation passes but does not completely cover Discussion evidence. This minor lexical repair does not weaken the negative biological conclusion.

### Verified source project and sample scope

representation: supported. Targets: CommunityMech:000441.

The existing BioProject reference resolves to the correct xenic culture.

Both raw runs use SAMN54770858; the two associate BioSamples describe reconstructed genomes. Source-reported assemblies were not resolved to exact public assembly IDs by bounded project queries; no global absence or failed-deposit claim follows. No raw read or genome reanalysis was performed.

### Whole article and bounded supplementary review

scope: supported. Targets: CommunityMech:000441.

All declared source objects were recovered and reviewed at explicit scopes.

Lead read all 61,602 projected article characters including 47 references, three tables and four captions; all four WEBP figures were viewed. S2 and S4 cells were read completely; S3 covered all 32 existing rows for 18 Figure 2 module IDs plus inventory/headers, and S1 covered headers/first row plus representative rows 52/552. Other S1/S3 data were not independently reanalysed. Figure 4 ring-path KO labels differ from S4; no canonical KO assertion is imported. Optional BioU/metH/metE structured-adapter queries could not run in the owned environment; dataset coverage remains unknown.

### Maintained record and prior decisions

ownership: supported. Targets: CommunityMech:000441.

Future corrections belong to the canonical record under separate curation authorization.

The exact batch 33 row repaired graph scope and left metadata uncertified. Its historical nineteen-MATCH result is not inherited as exact case-sensitive proof. Current issues remain at their observed states; this review changes no issue, history, cache, canonical record or Git state. Cohort proportional completeness 80 is not the literal metric below.

### Actual native checks

schema: supported. Targets: CommunityMech:000441.

All eight required checks passed.

The actual two-node network has no reported structural issues. Native COMPLETE does not establish biological stability, exchange or complete census.

### Literal rubric scores

completeness: supported. Targets: CommunityMech:000441.

Completeness 25; raw quality 119, capped 100.

## Findings

### community-metadata: Qualify stability and associate abundance

major / open / confirmed; issue key: cm-000441-community-metadata.

STABLE is unsupported by longitudinal evidence. Associate RARE values are not tied to a comparable whole-community estimate, especially for Brevundimonas.

### culture-mode: Distinguish serial transfer from draw-and-fill

minor / open / confirmed; issue key: cm-000441-culture-mode.

Single-filament serial maintenance does not establish SEMI_CONTINUOUS as defined by the current schema.

### gtdb-source: Record available GTDB classifications with scope

minor / open / confirmed; issue key: cm-000441-gtdb-source.

All three UNRESOLVED statuses omit recoverable source study-genome classifications; two local genus routes also resolve. These sources must remain distinct.

### snippet-case: Restore the exact discussion excerpt

minor / open / confirmed; issue key: cm-000441-snippet-case.

The excerpt capitalizes these despite its lowercase occurrence after However, in the source sentence.

## Recommended Actions And Acceptance Checks

### repair-community-metadata

Remove unsupported equilibrium and attach method-specific abundance context.

- Omit unsupported STABLE or explicitly retain unresolved state without forcing TRANSIENT or ENGINEERED. Source maintenance alone is not equilibrium.
- For Sphingorhabdus, qualify any RARE value to its marker-based observation and uncertainty; for Brevundimonas, leave ordinal prominence unassigned unless separately supported. Do not substitute genome mapping fractions as cell abundance.
- Retain cyanobacterial DOMINANT with source context, three recovered-genome scope and incomplete census. Do not impose historic numerical enum cutoffs or invent optional roles.

### repair-culture-mode

Represent the reported maintenance regime directly.

- Use OTHER with the approximately ten-day single-filament transfer description, or omit an unsupported mode. Do not infer partial harvest, working volume or closed batch operation.
- Retain source BG11, 20 °C, 16:8 h and approximately 3,000 lux with exact local evidence.

### repair-gtdb

Separate study-genome classification from taxon-level crosswalk grounding.

- Capture source GTDB-Tk v2.5.2/r226, full Table 2 lineages and Results representative-specific ANI/alignment fractions for the three exact recovered genomes. Preserve Sphingorhabdus_B sp023910635 and Brevundimonas sp040380105 as unnamed genome species clusters, not formally named species.
- If adding generic taxon-level blocks, use verified genus routes with current snapshot/method/counts: Sphingorhabdus_B 27/27 and Brevundimonas 221/221. Do not override the source genome result with the ambiguous cyanobacterial local name fallback.
- Retain valid NCBI species/genus labels and ADA naming context. Keep RefSeq ANIb/dDDH distinct from GTDB-Tk ANI/AF. Reference genomes and BioSamples are not automatically isolate stocks or NCBI Assembly accessions.

### repair-snippet

Make the negative cross-feeding excerpt verbatim.

- Restore source lowercase these or include its exact preceding context; do not change the supported negative inference or fabricate a sentence.
- Run the native reference validator and an independent case-preserving literal check after separately authorized curation.

### validate-curation

Validate any separately authorized record changes.

- Run focused schema, strict, ontology-label, reference, GTDB/domain and history gates; preserve the two computational PARTIAL nodes and zero arrows.
- Do not alter source caches or prior history to make evidence pass; root alone saves this review and runs its post-save checks.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | kb/communities/Dolichospermum_FBCC_A233_Xenic_Phycosphere_Community.yaml; Whole maintained YAML | supports | Naturally sourced, maintained xenic culture; three recovered genomes represented in two qualified computational nodes. |
| cultivation | PMID:42535840; DOI:10.1128/spectrum.01014-26; Materials and Methods, Sample information, sole direct paragraph; XPath //*[@id="s2-1"]/p[1] | supports | FBCC-A233 was supplied by NNIBR/FBCC, established from an April 2019 reservoir sample and maintained by single-filament transfers about every ten days in BG11. |
| community | PMID:42535840; DOI:10.1128/spectrum.01014-26; Results, Community profiling and recovery of three complete circular genomes from a unialgal xenic culture, paragraphs 1–2 and Table 1; Discussion paragraph 5 | supports | Marker composition and genome-wide read mapping answer different questions. No longitudinal community profiling or complete census was performed. |
| study-taxonomy | PMID:42535840; DOI:10.1128/spectrum.01014-26; Methods, Species identification, sole paragraph; Results, Genome-based taxonomic placement and species-cluster assignment of the three reconstructed genomes, paragraphs 2–3; Table 2 | supports | GTDB-Tk v2.5.2 r226 supplies three study-genome species clusters, full lineages and representative-specific ANI/AF. RefSeq ANIb/dDDH is a separate comparison. |
| biotin | PMID:42535840; DOI:10.1128/spectrum.01014-26; Results, Comparative genome architecture and genome-inferred metabolic potential across the three genomes, paragraph 3; Figures 2–3; Discussion paragraph 4; Tables S3–S4 | supports | BioU-mediated pathway potential occurs in the cyanobacterial genome; associates lack complete routes. Utilization genes do not prove biotin production, transfer or dependence. |
| corrinoid | PMID:42535840; DOI:10.1128/spectrum.01014-26; Results, Comparative genome architecture and genome-inferred metabolic potential across the three genomes, paragraph 4; Figure 4; Discussion paragraph 4; Tables S3–S4 | supports | The unresolved ring step, DMB branch, transport and molecular identity prevent a canonical-cobalamin or exchange claim. metH/metE annotations remain predictions. |
| snippet-context | PMID:42535840; DOI:10.1128/spectrum.01014-26; Discussion, fourth direct paragraph, sentence beginning However, these profiles; XPath //*[@id="s4"]/p[4] | supports | The negative exchange statement is supported, but the canonical excerpt changes initial lowercase these to capital These. |
| supplement | PMID:42535840; DOI:10.1128/spectrum.01014-26; Tables S1–S4 and legends; four main figure pixels | supports | All S2/S4 cells and 32 selected S3 module rows were read; S1 reference reading was bounded. Figure 4 ring-path KO labels conflict with S4, so no new locus-level assertion is inferred. |
| inspection | /private/tmp/cm-review-session/batch-16/000441/inspect.json; Official 31-input inspection | supports | Target, 21 authorities and nine focal contexts pinned before assessment. |
| ontology | /private/tmp/cm-review-session/batch-16/000441/ontology-authority.json; Six distinct ID/label pairs and twelve placements | supports | All labels match current local OAK; species/genus labels are separate from exact study genomes. |
| schema | /private/tmp/cm-review-session/batch-16/000441/child-schema-semantics.json; Current state, abundance and cultivation definitions | supports | STABLE asserts equilibrium; RARE is ordinal; SEMI_CONTINUOUS requires periodic partial harvest/replacement. |
| gtdb | /private/tmp/cm-review-session/batch-16/000441/child-gtdb-crosswalk.json; All three encoded taxon routes | supports | Two genus mappings resolve; cyanobacterial name fallback remains ambiguous. Local reference counts are not study abundance. |
| stock | /private/tmp/cm-review-session/batch-16/000441/child-fbcc-stock-authority.json; Primary stock statement and bounded official catalogue check | supports | FBCC-A233 is directly source-supported; the exact catalogue entry was not independently recovered. The failed DNS response is retained. |
| adapter | /private/tmp/cm-review-session/batch-16/000441/child-structured-adapter-applicability.json; Actual BioU, metH and metE query applicability | supports | Relevant genes were considered, but no runner was available in the task runtime; organism coverage is unknown. Inspected primary annotations provide the fallback. |
| semantics | /private/tmp/cm-review-session/batch-16/000441/ontology-semantic-notes.json; Final source-aware auxiliary conclusions | supports | One major and three minor findings; retain two genomic-potential nodes and zero arrows. |
| resources | /private/tmp/cm-review-session/batch-16/000441/dataset-verification.json; Whole project, two runs and three BioSamples; bounded assembly queries | supports | PRJNA1404972 matches the mixed culture. Raw runs share SAMN54770858; associate samples describe reconstructed genomes. |
| links | /private/tmp/cm-review-session/batch-16/000441/external-resource-verification.json; All three encoded publication/project links | supports | PubMed, DOI and project identities verified. No missing-dataset finding. |
| snippets | /private/tmp/cm-review-session/batch-16/000441/snippet-audit.json; All nineteen canonical excerpt placements | supports | Eighteen strict fresh/cache matches and one initial-case discrepancy; native reference coverage is not literal identity. |
| provenance | /private/tmp/cm-review-session/batch-16/000441/provenance-audit.json; Exact batch 33 records[1], histories, cohort and current issues | supports | Prior graph repair is preserved; current 1403 is closed, 1406 and 765 remain open. No issue disposition changes. |
| assets | /private/tmp/cm-review-session/batch-16/000441/lead-source-assets.json; Fresh public manuscript, figures and declared supplements | supports | All principal retrievals succeeded; source objects and extraction hashes are preserved. |
| read-scope | /private/tmp/cm-review-session/batch-16/000441/lead-primary-read-scope.json; Actual lead main and supplement reading | supports | Whole 61,602-character primary projection, all four figure pixels, full S2/S4 and bounded S1/S3 were read. |
| locators | /private/tmp/cm-review-session/batch-16/000441/source-locator-verification.json; Direct heading and paragraph inventory | supports | Quote and all cited section/table locators checked against actual JATS. |
| source-audit | /private/tmp/cm-review-session/batch-16/000441/source-audit.json; Final lead scientific audit | supports | Completed scientific review, one P2 and three P3; all four graph excerpt hashes bound. |
| root-source | /private/tmp/cm-review-session/batch-16/000441/root-independent-source-audit.json; Independent root source review | supports | Independent source, figure, supplement and authority assessment agrees with final findings. |
| support | /private/tmp/cm-review-session/batch-16/000441/support-final-audit.json; Final supporting reconciliation | supports | Completeness 25; quality base 135 minus 16 gives raw 119, capped 100. |
| support-manifest | /private/tmp/cm-review-session/batch-16/000441/support-frozen-manifest.json; Frozen supporting artifacts | supports | Actual source, provenance and input integrity retained. |
| auxiliary | /private/tmp/cm-review-session/batch-16/000441/auxiliary-frozen-manifest.json; Frozen native/authority artifacts | supports | Eight required native checks pass; ancillary retrieval limits are separate. |
| native-summary | /private/tmp/cm-review-session/batch-16/000441/final-validator-summary.json; Actual eight command receipts | supports | All eight required checks exited 0. |
| corpus-context | /private/tmp/cm-review-session/batch-16/000441/child-corpus-context.json; Fresh batch 16 corpus context | supports | Warning-only corpus exits retained separately from focused record checks. |
| failed-response | /private/tmp/cm-review-session/batch-16/000441/failed-artifact-classification.json; Exact failed catalogue request classification | supports | One DNS-failure body is empty and is not read source content or a native failure. |
| check-validate | /private/tmp/cm-review-session/batch-16/000441/validate.json; Actual command/stdout/stderr | supports | Required native command exited 0. |
| check-validate-strict | /private/tmp/cm-review-session/batch-16/000441/validate-strict.json; Actual command/stdout/stderr | supports | Required native command exited 0. |
| check-validate-terms | /private/tmp/cm-review-session/batch-16/000441/validate-terms.json; Actual command/stdout/stderr | supports | Required native command exited 0. |
| check-validate-references-explained | /private/tmp/cm-review-session/batch-16/000441/validate-references-explained.json; Actual command/stdout/stderr | supports | Required native command exited 0. |
| check-validate-gtdb | /private/tmp/cm-review-session/batch-16/000441/validate-gtdb.json; Actual command/stdout/stderr | supports | Required native command exited 0. |
| check-validate-gtdb-domain | /private/tmp/cm-review-session/batch-16/000441/validate-gtdb-domain.json; Actual command/stdout/stderr | supports | Required native command exited 0. |
| check-validate-history | /private/tmp/cm-review-session/batch-16/000441/validate-history.json; Actual command/stdout/stderr | supports | Required native command exited 0. |
| check-normalize-cache-names-check | /private/tmp/cm-review-session/batch-16/000441/normalize-cache-names-check.json; Actual command/stdout/stderr | supports | Required native command exited 0. |
| context-audit-network | /private/tmp/cm-review-session/batch-16/audit-network.json; Fresh batch 16 corpus baseline | supports | Warning-only actual corpus exit 1 retained. |
| context-check-network-quality | /private/tmp/cm-review-session/batch-16/check-network-quality.json; Fresh batch 16 corpus baseline | supports | Warning-only actual corpus exit 1 retained. |

## Limits And Additional Notes

- No longitudinal community profile, axenic comparator, bacterial localization, cofactor production/transfer, expression or growth-rescue assay is established by this source.
- S1 reading is limited to headers/first row and two source representative rows. S3 covers inventory/headers and 32 selected rows; no claim of reanalysing every reference genome, module, raw sequence or annotation.
- Figure 4 ring-path KO labels conflict with S4. BioU EC typography and repeated coordinates were not independently adjudicated. These unencoded source details are not added to the record.
- Source-specific GTDB classifications, generic local taxon routes and formally named NCBI taxa have different scopes. The exact FBCC catalogue entry and public assembly IDs were not recovered by bounded checks; no global absence is asserted.
- The optional structured adapter could not run in the owned environment; BioU/metH/metE relevance is explicit and organism coverage remains unknown.
- Completion concerns this bounded record review and does not close issues, promote native record status or authorize curation.
- All 31 official input hashes remain unchanged. Eight linked dimensions, four exact graph excerpt hashes and zero-arrow scope are explicit.
- Required native checks passed; ancillary display/retrieval failures are distinct. No candidate failure is presumed before actual validation.
- Lead subsequently read exact batch 33 records[1] and shared metadata, whole adversarial report and first 20,000 cache characters; support read the entire cache and current issue/cohort scopes.
- The only direct source quote has two words. Root owns saving and post-save gates.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T071501Z-dolichospermum-xenic-record-review
kind: record
repository: CultureBotAI/CommunityMech
title: Dolichospermum FBCC-A233 xenic culture record review
started_at: '2026-10-22T07:02:36.860177Z'
finished_at: '2026-10-22T07:15:01.070820Z'
reviewer:
  identity: codex
  kind: agent
  independence: unknown
  independence_basis: Separate lead, root, auxiliary and support reviews; no person-level
    independence claim.
skill: review-yaml-record
completion: completed
verdict: needs_curation
scientific_review: true
summary: The culture identity and two qualified genome-inferred cofactor observations
  are supported. One major finding concerns stability and associate abundance; three
  minor findings concern cultivation mode, GTDB classification scope and one excerpt
  capitalization. All eight required native checks passed. Completeness is 25; raw
  quality 119 is capped at 100.
source:
  git_revision: cb7a782c8ba80299dca8761ad0a2c90bccd8a117
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: d2f94c87b82f59663bc2b0c91ac04a245e56fab52d8c11e6bddb559eb9237c84
    role: context
  - path: .claude/skills/ground-taxa-gtdb/SKILL.md
    sha256: 6358a4324781ce2598554dca18ef952ec03c9d4a9df33f82f5db8ea5e986969b
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
  - path: AGENTS.md
    sha256: 4a3fccdfa03ff1f7f6ecd68465064bfaba97a0efbc1efd4f7809c3ca0529a557
    role: context
  - path: CLAUDE.md
    sha256: 8458fc2ca6663fea0e94c8e5b79730aafe6f4b3ac2c0f1079a3b64a2bb4d3d98
    role: context
  - path: conf/record_review.yaml
    sha256: 8cbd8f9d209f78de47a8c35091e43bf1dadbe41ee07492c7860b6d4be30112a8
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
  - path: history/records/Dolichospermum_FBCC_A233_Xenic_Phycosphere_Community/2026-09-26T203153Z-codex-441.yaml
    sha256: 9249cf51e3b070eef045d7cdd8afadbec47ba62d19f0e4831e2cee2b0e4b44fe
    role: context
  - path: history/records/Dolichospermum_FBCC_A233_Xenic_Phycosphere_Community/2026-10-06T070209Z-codex-ce5f1c.yaml
    sha256: 30ea4b902d5c97b197dc16c1731e9140c50291133289026998aa5a2fb281764f
    role: context
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: kb/communities/Dolichospermum_FBCC_A233_Xenic_Phycosphere_Community.yaml
    sha256: d4da92fc50e4b006fcaaf2d830d5c668e1e2671cea3b00655909a97a8c5e4bd1
    role: target
  - path: references_cache/PMID_42535840.txt
    sha256: 949af1239c94dc73a9edd58804b1aa90d97d3a2401be6432e7e52e63a4892094
    role: context
  - path: reports/causal_graph_review/adversarial-review-20261006-batch33.yaml
    sha256: bbc95a9fdbe89641db5ed5315e01160fea0aed3524a6252080b2aa806e81d4ae
    role: context
  - path: reports/causal_graph_review/decisions/20261006-three-records-batch33.yaml
    sha256: a8fb32ab2e18b2b6cba09c2d4a607c74cb4d2d60a4871712ed26fdf4b03a2e4a
    role: context
  - path: reviews/structured/20261021T101100Z-stage4-frozen-cohort-review/review.md
    sha256: e432615b147787c8d009d96d2f11e5b78a45927bf9c69e45ec0d31123d1fc2e9
    role: context
  - path: reviews/structured/20261021T101100Z-stage4-frozen-cohort-review/review.yaml
    sha256: 37d089fd55c077793dd20d868b50c47cb1cceab6dae6a82887cc938bee05fa6d
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
    sha256: c41630d09def826256ddb6678c1ce31fa71e3b074219bb9d217d98035a5324ee
    role: context
  - path: src/communitymech/schema/history.yaml
    sha256: b01b06f1b9a37db205c26c31ec0fd910690848507c7e1bfb73b424ac0829c52d
    role: context
  - path: src/communitymech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
targets:
- target_id: CommunityMech:000441
  path: kb/communities/Dolichospermum_FBCC_A233_Xenic_Phycosphere_Community.yaml
  label: Dolichospermum FBCC-A233 Xenic Phycosphere Community
  kind: maintained
  record_class: MicrobialCommunity
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Dolichospermum_FBCC_A233_Xenic_Phycosphere_Community.yaml
    role: canonical_record
scope:
  description: Whole released record and primary article, all four main figures, complete
    S2/S4 and explicitly bounded S1/S3, local ontology/native checks and source-linked
    archive metadata.
  selection: Only released CommunityMech:000441 in owned batch 16.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000441
checks:
- check_id: validate
  name: validate
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000441
  command: just --no-dotenv validate kb/communities/Dolichospermum_FBCC_A233_Xenic_Phycosphere_Community.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate
  scope_note: Focused record/history check; cache-name preflight is corpus-wide. Scientific
    support assessed separately.
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000441
  command: just --no-dotenv validate-strict kb/communities/Dolichospermum_FBCC_A233_Xenic_Phycosphere_Community.yaml
    --out /private/tmp/cm-review-session/batch-16/000441/strict-report.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-strict
  scope_note: Focused record/history check; cache-name preflight is corpus-wide. Scientific
    support assessed separately.
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000441
  command: just --no-dotenv validate-terms kb/communities/Dolichospermum_FBCC_A233_Xenic_Phycosphere_Community.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-terms
  scope_note: Focused record/history check; cache-name preflight is corpus-wide. Scientific
    support assessed separately.
- check_id: validate-references-explained
  name: validate-references-explained
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000441
  command: just --no-dotenv validate-references-explained kb/communities/Dolichospermum_FBCC_A233_Xenic_Phycosphere_Community.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-references-explained
  scope_note: Focused record/history check; cache-name preflight is corpus-wide. Scientific
    support assessed separately.
- check_id: validate-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000441
  command: just --no-dotenv validate-gtdb kb/communities/Dolichospermum_FBCC_A233_Xenic_Phycosphere_Community.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb
  scope_note: Focused record/history check; cache-name preflight is corpus-wide. Scientific
    support assessed separately.
- check_id: validate-gtdb-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000441
  command: just --no-dotenv validate-gtdb-domain kb/communities/Dolichospermum_FBCC_A233_Xenic_Phycosphere_Community.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb-domain
  scope_note: Focused record/history check; cache-name preflight is corpus-wide. Scientific
    support assessed separately.
- check_id: validate-history
  name: validate-history
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000441
  command: just --no-dotenv validate-history history/records/Dolichospermum_FBCC_A233_Xenic_Phycosphere_Community
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-history
  scope_note: Focused record/history check; cache-name preflight is corpus-wide. Scientific
    support assessed separately.
- check_id: normalize-cache-names-check
  name: normalize-cache-names-check
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000441
  command: uv run python scripts/normalize_cache_names.py --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-normalize-cache-names-check
  scope_note: Focused record/history check; cache-name preflight is corpus-wide. Scientific
    support assessed separately.
- check_id: context-audit-network
  name: audit-network corpus context
  status: failed
  required: false
  summary: Actual corpus exit 1, zero structural errors.
  target_ids:
  - CommunityMech:000441
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-16/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv audit-network
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - context-audit-network
  - corpus-context
  scope_note: Nonrequired corpus context, not a focused native or candidate failure.
- check_id: context-check-network-quality
  name: check-network-quality corpus context
  status: failed
  required: false
  summary: Actual corpus exit 1, zero structural errors.
  target_ids:
  - CommunityMech:000441
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-16/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv check-network-quality
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - context-check-network-quality
  - corpus-context
  scope_note: Nonrequired corpus context, not a focused native or candidate failure.
- check_id: structured-adapter
  name: Gene-specific structured source adapter
  status: unavailable
  required: false
  summary: Runner unavailable in the owned runtime; actual gene queries identified.
  target_ids:
  - CommunityMech:000441
  evidence_ids:
  - adapter
  scope_note: BioU/metH/metE are relevant; organism/dataset coverage unknown. No installation,
    other-checkout execution or negative biological inference.
evidence:
- evidence_id: record
  kind: record_content
  reference: kb/communities/Dolichospermum_FBCC_A233_Xenic_Phycosphere_Community.yaml
  locator: Whole maintained YAML
  summary: Naturally sourced, maintained xenic culture; three recovered genomes represented
    in two qualified computational nodes.
  support: supports
  accessed_at: '2026-10-22T07:15:01.064935Z'
- evidence_id: cultivation
  kind: primary_source
  reference: PMID:42535840; DOI:10.1128/spectrum.01014-26
  locator: Materials and Methods, Sample information, sole direct paragraph; XPath
    //*[@id="s2-1"]/p[1]
  summary: FBCC-A233 was supplied by NNIBR/FBCC, established from an April 2019 reservoir
    sample and maintained by single-filament transfers about every ten days in BG11.
  support: supports
  accessed_at: '2026-10-22T07:15:01.064992Z'
  snapshot_sha256: fca8e5eef0bdd4fd2bc11a874ac53b02f5091ddc89876f2ddc47ee879a716394
  quote: serial subculture
- evidence_id: community
  kind: primary_source
  reference: PMID:42535840; DOI:10.1128/spectrum.01014-26
  locator: Results, Community profiling and recovery of three complete circular genomes
    from a unialgal xenic culture, paragraphs 1–2 and Table 1; Discussion paragraph
    5
  summary: Marker composition and genome-wide read mapping answer different questions.
    No longitudinal community profiling or complete census was performed.
  support: supports
  accessed_at: '2026-10-22T07:15:01.065326Z'
  snapshot_sha256: fca8e5eef0bdd4fd2bc11a874ac53b02f5091ddc89876f2ddc47ee879a716394
- evidence_id: study-taxonomy
  kind: primary_source
  reference: PMID:42535840; DOI:10.1128/spectrum.01014-26
  locator: Methods, Species identification, sole paragraph; Results, Genome-based
    taxonomic placement and species-cluster assignment of the three reconstructed
    genomes, paragraphs 2–3; Table 2
  summary: GTDB-Tk v2.5.2 r226 supplies three study-genome species clusters, full
    lineages and representative-specific ANI/AF. RefSeq ANIb/dDDH is a separate comparison.
  support: supports
  accessed_at: '2026-10-22T07:15:01.065396Z'
  snapshot_sha256: fca8e5eef0bdd4fd2bc11a874ac53b02f5091ddc89876f2ddc47ee879a716394
- evidence_id: biotin
  kind: primary_source
  reference: PMID:42535840; DOI:10.1128/spectrum.01014-26
  locator: Results, Comparative genome architecture and genome-inferred metabolic
    potential across the three genomes, paragraph 3; Figures 2–3; Discussion paragraph
    4; Tables S3–S4
  summary: BioU-mediated pathway potential occurs in the cyanobacterial genome; associates
    lack complete routes. Utilization genes do not prove biotin production, transfer
    or dependence.
  support: supports
  accessed_at: '2026-10-22T07:15:01.065459Z'
  snapshot_sha256: fca8e5eef0bdd4fd2bc11a874ac53b02f5091ddc89876f2ddc47ee879a716394
- evidence_id: corrinoid
  kind: primary_source
  reference: PMID:42535840; DOI:10.1128/spectrum.01014-26
  locator: Results, Comparative genome architecture and genome-inferred metabolic
    potential across the three genomes, paragraph 4; Figure 4; Discussion paragraph
    4; Tables S3–S4
  summary: The unresolved ring step, DMB branch, transport and molecular identity
    prevent a canonical-cobalamin or exchange claim. metH/metE annotations remain
    predictions.
  support: supports
  accessed_at: '2026-10-22T07:15:01.065519Z'
  snapshot_sha256: fca8e5eef0bdd4fd2bc11a874ac53b02f5091ddc89876f2ddc47ee879a716394
- evidence_id: snippet-context
  kind: primary_source
  reference: PMID:42535840; DOI:10.1128/spectrum.01014-26
  locator: Discussion, fourth direct paragraph, sentence beginning However, these
    profiles; XPath //*[@id="s4"]/p[4]
  summary: The negative exchange statement is supported, but the canonical excerpt
    changes initial lowercase these to capital These.
  support: supports
  accessed_at: '2026-10-22T07:15:01.065578Z'
  snapshot_sha256: fca8e5eef0bdd4fd2bc11a874ac53b02f5091ddc89876f2ddc47ee879a716394
- evidence_id: supplement
  kind: primary_source
  reference: PMID:42535840; DOI:10.1128/spectrum.01014-26
  locator: Tables S1–S4 and legends; four main figure pixels
  summary: All S2/S4 cells and 32 selected S3 module rows were read; S1 reference
    reading was bounded. Figure 4 ring-path KO labels conflict with S4, so no new
    locus-level assertion is inferred.
  support: supports
  accessed_at: '2026-10-22T07:15:01.065638Z'
  snapshot_sha256: a60098d96a25598521c9a33d9ff2e64540bfe7614343f8659adc5887880a5555
- evidence_id: inspection
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000441/inspect.json
  locator: Official 31-input inspection
  summary: Target, 21 authorities and nine focal contexts pinned before assessment.
  support: supports
  accessed_at: '2026-10-22T07:15:01.065821Z'
  snapshot_sha256: 3f92898bff4f2c6a2b8e89f918356ebdfd8c9f19d8df50f2280d96c7f355b5d5
- evidence_id: ontology
  kind: authority
  reference: /private/tmp/cm-review-session/batch-16/000441/ontology-authority.json
  locator: Six distinct ID/label pairs and twelve placements
  summary: All labels match current local OAK; species/genus labels are separate from
    exact study genomes.
  support: supports
  accessed_at: '2026-10-22T07:15:01.065864Z'
  snapshot_sha256: 7a84f9151f1a5ac612834576bc80e2b97f09a0bb69a2da5709790ece18d3f643
- evidence_id: schema
  kind: authority
  reference: /private/tmp/cm-review-session/batch-16/000441/child-schema-semantics.json
  locator: Current state, abundance and cultivation definitions
  summary: STABLE asserts equilibrium; RARE is ordinal; SEMI_CONTINUOUS requires periodic
    partial harvest/replacement.
  support: supports
  accessed_at: '2026-10-22T07:15:01.066047Z'
  snapshot_sha256: 912ccdd467766d5ebb54cfc57e186b353b3bae49d7edbaaa5c8195eb70771a93
- evidence_id: gtdb
  kind: authority
  reference: /private/tmp/cm-review-session/batch-16/000441/child-gtdb-crosswalk.json
  locator: All three encoded taxon routes
  summary: Two genus mappings resolve; cyanobacterial name fallback remains ambiguous.
    Local reference counts are not study abundance.
  support: supports
  accessed_at: '2026-10-22T07:15:01.066289Z'
  snapshot_sha256: 03d268f724cfa6db504348c6bf73f719c8ff85883909e36c26484110b47e5feb
- evidence_id: stock
  kind: authority
  reference: /private/tmp/cm-review-session/batch-16/000441/child-fbcc-stock-authority.json
  locator: Primary stock statement and bounded official catalogue check
  summary: FBCC-A233 is directly source-supported; the exact catalogue entry was not
    independently recovered. The failed DNS response is retained.
  support: supports
  accessed_at: '2026-10-22T07:15:01.066388Z'
  snapshot_sha256: 0134cd0bc82ec5f985a85d3529f9859d1922e8c041e81f6469deb696f9f20498
- evidence_id: adapter
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000441/child-structured-adapter-applicability.json
  locator: Actual BioU, metH and metE query applicability
  summary: Relevant genes were considered, but no runner was available in the task
    runtime; organism coverage is unknown. Inspected primary annotations provide the
    fallback.
  support: supports
  accessed_at: '2026-10-22T07:15:01.066589Z'
  snapshot_sha256: c600f30da8540c5f9d3991278aeeb3875b9b29404ce3b699d79158f5fd069b99
- evidence_id: semantics
  kind: authority
  reference: /private/tmp/cm-review-session/batch-16/000441/ontology-semantic-notes.json
  locator: Final source-aware auxiliary conclusions
  summary: One major and three minor findings; retain two genomic-potential nodes
    and zero arrows.
  support: supports
  accessed_at: '2026-10-22T07:15:01.066660Z'
  snapshot_sha256: 1c29afbfd28de662c7769f0867d6141040699c8027bb6a8093cdd682cda3f02a
- evidence_id: resources
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000441/dataset-verification.json
  locator: Whole project, two runs and three BioSamples; bounded assembly queries
  summary: PRJNA1404972 matches the mixed culture. Raw runs share SAMN54770858; associate
    samples describe reconstructed genomes.
  support: supports
  accessed_at: '2026-10-22T07:15:01.066854Z'
  snapshot_sha256: 7c5d526531ef1a9e0bde39df224b635b330f37893621171565b88704150f1293
- evidence_id: links
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000441/external-resource-verification.json
  locator: All three encoded publication/project links
  summary: PubMed, DOI and project identities verified. No missing-dataset finding.
  support: supports
  accessed_at: '2026-10-22T07:15:01.067071Z'
  snapshot_sha256: f30f4bc4bb3fc26525b61c764f4bf6381f5e43c5e382266b2b81333187e24c00
- evidence_id: snippets
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000441/snippet-audit.json
  locator: All nineteen canonical excerpt placements
  summary: Eighteen strict fresh/cache matches and one initial-case discrepancy; native
    reference coverage is not literal identity.
  support: supports
  accessed_at: '2026-10-22T07:15:01.067227Z'
  snapshot_sha256: bf279ebd9c532d0d7f2035c87c7b3030eda971fceab2fb075b680397d1e1ea10
- evidence_id: provenance
  kind: prior_review
  reference: /private/tmp/cm-review-session/batch-16/000441/provenance-audit.json
  locator: Exact batch 33 records[1], histories, cohort and current issues
  summary: Prior graph repair is preserved; current 1403 is closed, 1406 and 765 remain
    open. No issue disposition changes.
  support: supports
  accessed_at: '2026-10-22T07:15:01.067412Z'
  snapshot_sha256: 73d4651d307f2a973039f0de27bc4bcabd492e5eaf2f079a3d200991dc29af34
- evidence_id: assets
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000441/lead-source-assets.json
  locator: Fresh public manuscript, figures and declared supplements
  summary: All principal retrievals succeeded; source objects and extraction hashes
    are preserved.
  support: supports
  accessed_at: '2026-10-22T07:15:01.067530Z'
  snapshot_sha256: a60098d96a25598521c9a33d9ff2e64540bfe7614343f8659adc5887880a5555
- evidence_id: read-scope
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000441/lead-primary-read-scope.json
  locator: Actual lead main and supplement reading
  summary: Whole 61,602-character primary projection, all four figure pixels, full
    S2/S4 and bounded S1/S3 were read.
  support: supports
  accessed_at: '2026-10-22T07:15:01.067555Z'
  snapshot_sha256: f7f40681a58a8dd48bf2d0dcd092309bbf91d6c96c2a4bb79c9a47e293a1f9d9
- evidence_id: locators
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000441/source-locator-verification.json
  locator: Direct heading and paragraph inventory
  summary: Quote and all cited section/table locators checked against actual JATS.
  support: supports
  accessed_at: '2026-10-22T07:15:01.067655Z'
  snapshot_sha256: 0621771949ddc860f53e3a1a37e38ff3ca0876714d6ee09ccbaa8458d0aab5a9
- evidence_id: source-audit
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000441/source-audit.json
  locator: Final lead scientific audit
  summary: Completed scientific review, one P2 and three P3; all four graph excerpt
    hashes bound.
  support: supports
  accessed_at: '2026-10-22T07:15:01.067789Z'
  snapshot_sha256: ddaac0a27e1f50b5863b639360d4703262edda92db5747f016519fe31337d041
- evidence_id: root-source
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000441/root-independent-source-audit.json
  locator: Independent root source review
  summary: Independent source, figure, supplement and authority assessment agrees
    with final findings.
  support: supports
  accessed_at: '2026-10-22T07:15:01.067884Z'
  snapshot_sha256: aaee0cfce3024129a927add10b5b878c5afa0d623860cce6a023b3de6e0d4b44
- evidence_id: support
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000441/support-final-audit.json
  locator: Final supporting reconciliation
  summary: Completeness 25; quality base 135 minus 16 gives raw 119, capped 100.
  support: supports
  accessed_at: '2026-10-22T07:15:01.068037Z'
  snapshot_sha256: 228eb73b92225e6fa9e1a42b5cc86276c441c3dd8c2e1776f3b558ebbe73559f
- evidence_id: support-manifest
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000441/support-frozen-manifest.json
  locator: Frozen supporting artifacts
  summary: Actual source, provenance and input integrity retained.
  support: supports
  accessed_at: '2026-10-22T07:15:01.068070Z'
  snapshot_sha256: 0f55469b81eb4428b7a7d425a8b4f8eeb8e331c12c3613c19495584e62a742a9
- evidence_id: auxiliary
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000441/auxiliary-frozen-manifest.json
  locator: Frozen native/authority artifacts
  summary: Eight required native checks pass; ancillary retrieval limits are separate.
  support: supports
  accessed_at: '2026-10-22T07:15:01.068266Z'
  snapshot_sha256: 16f2ac72f84a1dfc8e5c88145c2164fb5563021116f3b868f8413059040ba5e7
- evidence_id: native-summary
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000441/final-validator-summary.json
  locator: Actual eight command receipts
  summary: All eight required checks exited 0.
  support: supports
  accessed_at: '2026-10-22T07:15:01.068379Z'
  snapshot_sha256: fd7d288b174ca502437d1fcccbf8ef454ab90bf94fb9e31ed7ff5ae89d32b313
- evidence_id: corpus-context
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000441/child-corpus-context.json
  locator: Fresh batch 16 corpus context
  summary: Warning-only corpus exits retained separately from focused record checks.
  support: supports
  accessed_at: '2026-10-22T07:15:01.068638Z'
  snapshot_sha256: 92d7b464798e0a748eb61881fca2caca7df40fac1de34f503b670b873eaf60fa
- evidence_id: failed-response
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000441/failed-artifact-classification.json
  locator: Exact failed catalogue request classification
  summary: One DNS-failure body is empty and is not read source content or a native
    failure.
  support: supports
  accessed_at: '2026-10-22T07:15:01.068765Z'
  snapshot_sha256: d9c6448c719044d6155b333c3b0d0d31a5d902367de073b7486ded5bdba0f05c
- evidence_id: check-validate
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000441/validate.json
  locator: Actual command/stdout/stderr
  summary: Required native command exited 0.
  support: supports
  accessed_at: '2026-10-22T07:15:01.069064Z'
  snapshot_sha256: 3b90015b4f6737d95ec3de5eac80f5153249f4a35f03f365c96b8741d7186780
- evidence_id: check-validate-strict
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000441/validate-strict.json
  locator: Actual command/stdout/stderr
  summary: Required native command exited 0.
  support: supports
  accessed_at: '2026-10-22T07:15:01.069282Z'
  snapshot_sha256: 67d16ccce64dddba3ece6f6cffe2524a6bdcb5a3818ce4fbe921509a8f193499
- evidence_id: check-validate-terms
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000441/validate-terms.json
  locator: Actual command/stdout/stderr
  summary: Required native command exited 0.
  support: supports
  accessed_at: '2026-10-22T07:15:01.069457Z'
  snapshot_sha256: b0dd8dcd93c05aaf3fa9af1693b47c00436fa27b2c11cdfc4682546185ba5326
- evidence_id: check-validate-references-explained
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000441/validate-references-explained.json
  locator: Actual command/stdout/stderr
  summary: Required native command exited 0.
  support: supports
  accessed_at: '2026-10-22T07:15:01.069702Z'
  snapshot_sha256: a236e067d8611a471c9382dcb58c9dabaee8eefc4837e17ec6ee0e2ff6e6111a
- evidence_id: check-validate-gtdb
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000441/validate-gtdb.json
  locator: Actual command/stdout/stderr
  summary: Required native command exited 0.
  support: supports
  accessed_at: '2026-10-22T07:15:01.069841Z'
  snapshot_sha256: d3dca54075ca5e1b43ff1458cab2802470cb7bdb3417d223969bc65b59fd4946
- evidence_id: check-validate-gtdb-domain
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000441/validate-gtdb-domain.json
  locator: Actual command/stdout/stderr
  summary: Required native command exited 0.
  support: supports
  accessed_at: '2026-10-22T07:15:01.069997Z'
  snapshot_sha256: c2c07ff01d0706446170e06d5e5422f32ed0632747e5561f16d094c5a65bf6e2
- evidence_id: check-validate-history
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000441/validate-history.json
  locator: Actual command/stdout/stderr
  summary: Required native command exited 0.
  support: supports
  accessed_at: '2026-10-22T07:15:01.070142Z'
  snapshot_sha256: 9ee9b86734af3453b0481481cbf8e7e42d9f6abe88add69791a9a174da5eaaab
- evidence_id: check-normalize-cache-names-check
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000441/normalize-cache-names-check.json
  locator: Actual command/stdout/stderr
  summary: Required native command exited 0.
  support: supports
  accessed_at: '2026-10-22T07:15:01.070267Z'
  snapshot_sha256: 85c1215a537a34d3e60ec0bf6a104112f76f18e5f0380c9bd93f2c0c8380ca5c
- evidence_id: context-audit-network
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/audit-network.json
  locator: Fresh batch 16 corpus baseline
  summary: Warning-only actual corpus exit 1 retained.
  support: supports
  accessed_at: '2026-10-22T07:15:01.070574Z'
  snapshot_sha256: f4809c6a349f1496dbfe0243fb5ce661f469f7235f2aa00e6294ee3aa04f3123
- evidence_id: context-check-network-quality
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/check-network-quality.json
  locator: Fresh batch 16 corpus baseline
  summary: Warning-only actual corpus exit 1 retained.
  support: supports
  accessed_at: '2026-10-22T07:15:01.070707Z'
  snapshot_sha256: 759ba13f2cda067251275491bbafc401d0be8bddf7907c7f962eb4369f61688f
assessments:
- assessment_id: identity
  area: identity
  topic: Culture and recovered genome scope
  outcome: supported
  summary: The record identifies the source-maintained FBCC-A233 xenic culture correctly.
  target_ids:
  - CommunityMech:000441
  evidence_ids:
  - record
  - cultivation
  - community
  - study-taxonomy
  - stock
  dimensions:
  - name: stable_id
    value: CommunityMech:000441; PMID:42535840; PMC13532358; DOI:10.1128/spectrum.01014-26
    definition: Exact record and primary publication identity.
    evidence_ids:
    - record
    - inspection
    - links
  - name: source_strains
    value: FBCC-A233 cyanobacterial culture; two recovered associate genomes without
      named species or collection stocks
    definition: FBCC/NNIBR source statement is verified. Reference strains in S1/S2
      are comparators, not study stock identities.
    evidence_ids:
    - cultivation
    - study-taxonomy
    - stock
  - name: community_scope
    value: Reservoir-derived unialgal xenic culture with three selected circular genome
      reconstructions
    definition: Culture maintenance and assembly selection do not establish a complete
      census or symbiotic dependence.
    evidence_ids:
    - community
    - study-taxonomy
  details: NATURAL describes reservoir origin; the reviewed system is a laboratory-maintained
    unialgal xenic culture. The three recovered genomes are not an exhaustive environmental
    census or a defined three-isolate consortium. PRIMARY_PRODUCER is supported for
    the cyanobacterium; optional heterotroph roles are not invented.
- assessment_id: community-metadata
  area: evidence
  topic: Stability and relative prominence
  outcome: concern
  summary: STABLE and unqualified associate RARE assignments exceed the method-resolved
    evidence.
  target_ids:
  - CommunityMech:000441
  evidence_ids:
  - community
  - schema
  details: The source expressly lacks longitudinal profiling. Sphingorhabdus has a
    low marker estimate (0.071254072%), while its genome maps 14.29% of trimmed reads;
    these metrics are not interchangeable. Brevundimonas has 5.37% genome mapping
    but no clear marker assignment. Mapping supports assemblies, not cell abundance
    or ecological non-driver status. Cyanobacterial DOMINANT remains qualitatively
    supported by the culture and dominant classified fraction. No percentage cutoff
    or forced replacement abundance is proposed.
- assessment_id: node-0
  area: graph
  topic: Genome-inferred biotin asymmetry
  outcome: supported
  summary: Retain the qualified COMMUNITY_LEVEL computational observation.
  target_ids:
  - CommunityMech:000441
  evidence_ids:
  - record
  - biotin
  - supplement
  - snippets
  - ontology
  - semantics
  details: 'Exact selector ecological_interactions[0]. No interaction_type, source_taxon,
    target_taxon or downstream direction is asserted. Participants: [{"preferred_term":
    "Dolichospermum flosaquae FBCC-A233", "term": {"id": "NCBITaxon:1166", "label":
    "Dolichospermum flos-aquae"}}, {"preferred_term": "Sphingorhabdus sp. FBCC-A233
    associate", "term": {"id": "NCBITaxon:1434046", "label": "Sphingorhabdus"}}, {"preferred_term":
    "Brevundimonas sp. FBCC-A233 associate", "term": {"id": "NCBITaxon:41275", "label":
    "Brevundimonas"}}]. Exact canonical snippet bindings: [{"selector": "ecological_interactions[0].evidence[0].snippet",
    "sha256": "85d12b9c40d1f5c43a215fc40b6f220701161cb556cb1799921f925bffff0f08",
    "reference": "PMID:42535840", "supports": "PARTIAL", "evidence_source": "COMPUTATIONAL"},
    {"selector": "ecological_interactions[0].evidence[1].snippet", "sha256": "b0e1fad0802e167706083b0fb8dee00a2714b17588dda84f67eb06478bb2f58c",
    "reference": "PMID:42535840", "supports": "PARTIAL", "evidence_source": "COMPUTATIONAL"}].
    Source: PMID:42535840; DOI:10.1128/spectrum.01014-26. Locator: Results, Comparative
    genome architecture and genome-inferred metabolic potential across the three genomes,
    paragraph 3; Figures 2–3; Discussion paragraph 4; Tables S3–S4. BioU/bioF/bioD/bioB
    and biotin-utilization annotations support asymmetric potential. CHEBI biotin
    and GO vitamin biosynthesis are pathway context, not measured metabolite production.
    No complete biotin uptake machinery or growth rescue was demonstrated. PARTIAL
    evidence and explicit unresolved chemistry/transfer limits are appropriate.'
- assessment_id: node-1
  area: graph
  topic: Genome-inferred corrinoid utilization asymmetry
  outcome: supported
  summary: Retain the qualified COMMUNITY_LEVEL computational observation.
  target_ids:
  - CommunityMech:000441
  evidence_ids:
  - record
  - corrinoid
  - supplement
  - snippets
  - ontology
  - semantics
  details: 'Exact selector ecological_interactions[1]. No interaction_type, source_taxon,
    target_taxon or downstream direction is asserted. Participants: [{"preferred_term":
    "Dolichospermum flosaquae FBCC-A233", "term": {"id": "NCBITaxon:1166", "label":
    "Dolichospermum flos-aquae"}}, {"preferred_term": "Sphingorhabdus sp. FBCC-A233
    associate", "term": {"id": "NCBITaxon:1434046", "label": "Sphingorhabdus"}}, {"preferred_term":
    "Brevundimonas sp. FBCC-A233 associate", "term": {"id": "NCBITaxon:41275", "label":
    "Brevundimonas"}}]. Exact canonical snippet bindings: [{"selector": "ecological_interactions[1].evidence[0].snippet",
    "sha256": "90a61863d102edcef7bc72284ffa97b5674507b63605d5862c303a78c6753213",
    "reference": "PMID:42535840", "supports": "PARTIAL", "evidence_source": "COMPUTATIONAL"},
    {"selector": "ecological_interactions[1].evidence[1].snippet", "sha256": "df771d948a11fcf7c5ae0ff89c979b134bdfd200c34b2f223c2d69a569b5488d",
    "reference": "PMID:42535840", "supports": "PARTIAL", "evidence_source": "COMPUTATIONAL"}].
    Source: PMID:42535840; DOI:10.1128/spectrum.01014-26. Locator: Results, Comparative
    genome architecture and genome-inferred metabolic potential across the three genomes,
    paragraph 4; Figure 4; Discussion paragraph 4; Tables S3–S4. Most anaerobic corrinoid-ring
    genes coexist with an unresolved ring step and absent canonical DMB branch. metH
    in all three and metE in Sphingorhabdus support predicted repertoire differences.
    Candidate btuB/general TonB components and methionine uptake do not establish
    cobamide import or exchange. PARTIAL evidence and explicit unresolved chemistry/transfer
    limits are appropriate.'
- assessment_id: graph-topology
  area: graph
  topic: Two parallel observations, zero arrows
  outcome: supported
  summary: No causal arrow is supported or required between these predictions.
  target_ids:
  - CommunityMech:000441
  evidence_ids:
  - record
  - biotin
  - corrinoid
  - semantics
  details: Both downstream lists are absent. No edge assessment is omitted; genome
    co-occurrence does not establish biotin-to-corrinoid causation, metabolite exchange,
    mutualism or syntrophy.
- assessment_id: cultivation
  area: evidence
  topic: Maintenance conditions and mode
  outcome: concern
  summary: BG11, temperature and illumination are supported; SEMI_CONTINUOUS is not
    established.
  target_ids:
  - CommunityMech:000441
  evidence_ids:
  - cultivation
  - schema
  dimensions:
  - name: medium
    value: Blue-Green Medium BG11; no source-specific formulation supplied
    definition: Preserve the reported medium name without importing catalogue stock
      recipes.
    evidence_ids:
    - cultivation
  - name: experimental_setting
    value: NNIBR/FBCC maintenance by repeated single-filament transfer about every
      ten days
    definition: Vessel and working volume remain unreported; serial transfer is distinct
      from partial-harvest semi-continuous operation.
    evidence_ids:
    - cultivation
    - schema
  - name: environment
    value: 20 °C; 16:8 h light:dark; approximately 3,000 lux; laboratory environment
    definition: Reservoir collection in April 2019 is origin metadata, separate from
      controlled maintenance.
    evidence_ids:
    - cultivation
    - ontology
  details: The source describes single-filament serial subculture at approximately
    ten-day intervals. It does not specify a draw-and-fill fraction, partial harvest,
    vessel geometry or working volume. OTHER with explicit maintenance notes is a
    conservative mode representation. Do not infer closed batch operation, a generic
    BG11 recipe, pH, aeration or shaking.
- assessment_id: grounding
  area: grounding
  topic: NCBI descriptors and study-specific GTDB
  outcome: concern
  summary: All encoded IDs are valid; the paper supplies recoverable GTDB classifications.
  target_ids:
  - CommunityMech:000441
  evidence_ids:
  - ontology
  - gtdb
  - study-taxonomy
  - supplement
  dimensions:
  - name: taxon_grounding
    value: NCBITaxon:1166 species; NCBITaxon:1434046 and NCBITaxon:41275 genera
    definition: Preserve valid nomenclatural labels and source study-genome classifications
      with their distinct method, rank and release provenance.
    evidence_ids:
    - ontology
    - study-taxonomy
    - gtdb
  details: Table 2 and Results classify the three study genomes under GTDB-Tk r226
    as Dolichospermum flosaquae, Sphingorhabdus_B sp023910635 and Brevundimonas sp040380105.
    These are not automatically named-species NCBI replacements. RefSeq labels and
    ANI/dDDH differ from GTDB-Tk species clusters and ANI/alignment fractions. The
    local crosswalk separately maps Sphingorhabdus to genus Sphingorhabdus_B (27/27)
    and Brevundimonas to its genus (221/221), while the cyanobacterial name route
    has three alternatives. No local fallback overrides the actual FBCC-A233 genome
    analysis.
- assessment_id: evidence-quality
  area: evidence
  topic: Exact excerpts and genomic interpretation
  outcome: concern
  summary: One initial-capitalization discrepancy needs a verbatim repair.
  target_ids:
  - CommunityMech:000441
  evidence_ids:
  - snippet-context
  - snippets
  - biotin
  - corrinoid
  dimensions:
  - name: evidence_tier
    value: COMPUTATIONAL gene/pathway potential; IN_VITRO culture maintenance
    definition: Genome annotation is not expression, secretion, uptake, cofactor chemistry,
      flux or demonstrated growth dependence.
    evidence_ids:
    - biotin
    - corrinoid
    - cultivation
    - snippets
  details: The discussion correctly states that exchange is unproven, but its excerpt
    changes lowercase these to These. All other eighteen placements strictly match
    fresh source and cache. Native reference validation passes but does not completely
    cover Discussion evidence. This minor lexical repair does not weaken the negative
    biological conclusion.
- assessment_id: resources
  area: representation
  topic: Verified source project and sample scope
  outcome: supported
  summary: The existing BioProject reference resolves to the correct xenic culture.
  target_ids:
  - CommunityMech:000441
  evidence_ids:
  - resources
  - links
  details: Both raw runs use SAMN54770858; the two associate BioSamples describe reconstructed
    genomes. Source-reported assemblies were not resolved to exact public assembly
    IDs by bounded project queries; no global absence or failed-deposit claim follows.
    No raw read or genome reanalysis was performed.
- assessment_id: source-scope
  area: scope
  topic: Whole article and bounded supplementary review
  outcome: supported
  summary: All declared source objects were recovered and reviewed at explicit scopes.
  target_ids:
  - CommunityMech:000441
  evidence_ids:
  - assets
  - read-scope
  - locators
  - root-source
  - supplement
  details: Lead read all 61,602 projected article characters including 47 references,
    three tables and four captions; all four WEBP figures were viewed. S2 and S4 cells
    were read completely; S3 covered all 32 existing rows for 18 Figure 2 module IDs
    plus inventory/headers, and S1 covered headers/first row plus representative rows
    52/552. Other S1/S3 data were not independently reanalysed. Figure 4 ring-path
    KO labels differ from S4; no canonical KO assertion is imported. Optional BioU/metH/metE
    structured-adapter queries could not run in the owned environment; dataset coverage
    remains unknown.
- assessment_id: ownership
  area: ownership
  topic: Maintained record and prior decisions
  outcome: supported
  summary: Future corrections belong to the canonical record under separate curation
    authorization.
  target_ids:
  - CommunityMech:000441
  evidence_ids:
  - inspection
  - provenance
  details: The exact batch 33 row repaired graph scope and left metadata uncertified.
    Its historical nineteen-MATCH result is not inherited as exact case-sensitive
    proof. Current issues remain at their observed states; this review changes no
    issue, history, cache, canonical record or Git state. Cohort proportional completeness
    80 is not the literal metric below.
- assessment_id: native
  area: schema
  topic: Actual native checks
  outcome: supported
  summary: All eight required checks passed.
  target_ids:
  - CommunityMech:000441
  evidence_ids:
  - native-summary
  - auxiliary
  - schema
  - corpus-context
  details: The actual two-node network has no reported structural issues. Native COMPLETE
    does not establish biological stability, exchange or complete census.
- assessment_id: metrics
  area: completeness
  topic: Literal rubric scores
  outcome: supported
  summary: Completeness 25; raw quality 119, capped 100.
  target_ids:
  - CommunityMech:000441
  evidence_ids:
  - support
  metrics:
  - name: completeness
    value: 25
    unit: points
    minimum: 0
    maximum: 100
    definition: 0 required-fields-and-all-taxon-roles +5 environment +0 at least three
      factors +0 at least three nodes +5 external resources +10 growth medium +0 associated
      datasets +5 node metabolites = 25. Missing optional heterotroph roles suppress
      the combined 50-point component but are not independently graded defects.
  - name: validation_quality
    value: 100
    unit: points
    minimum: 0
    maximum: 100
    definition: 100 +20*min((4 evidence/2 nodes)/2,1) +15 COMPLETE -10*1 P2 -2*3 P3
      = 119, capped at 100. Evidence bonus 20 and structural bonus 15 are not scientific
      truth.
  - name: P1
    value: 0
    unit: findings
    definition: Native severity count.
  - name: P2
    value: 1
    unit: findings
    definition: Native severity count.
  - name: P3
    value: 3
    unit: findings
    definition: Native severity count.
  - name: P4
    value: 0
    unit: findings
    definition: Native severity count.
findings:
- finding_id: community-metadata
  issue_key: cm-000441-community-metadata
  category: evidence
  severity: major
  native_severity: P2
  normalization_reason: Equilibrium and unqualified associate prominence materially
    overstate ecological knowledge.
  rule_id: review-checklist.claim-specific-support-and-context
  status: open
  certainty: confirmed
  title: Qualify stability and associate abundance
  description: STABLE is unsupported by longitudinal evidence. Associate RARE values
    are not tied to a comparable whole-community estimate, especially for Brevundimonas.
  target_ids:
  - CommunityMech:000441
  field_paths:
  - ecological_state
  - taxonomy[1].abundance_level
  - taxonomy[2].abundance_level
  evidence_ids:
  - community
  - schema
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Dolichospermum_FBCC_A233_Xenic_Phycosphere_Community.yaml
    role: canonical_record
  ownership_note: Future maintained YAML curation only; preserve sources, caches,
    history and prior reviews.
- finding_id: culture-mode
  issue_key: cm-000441-culture-mode
  category: representation
  severity: minor
  native_severity: P3
  normalization_reason: Bounded representation or provenance repair; identity and
    qualified genomic conclusions remain supported.
  rule_id: review-checklist.claim-specific-support-and-context
  status: open
  certainty: confirmed
  title: Distinguish serial transfer from draw-and-fill
  description: Single-filament serial maintenance does not establish SEMI_CONTINUOUS
    as defined by the current schema.
  target_ids:
  - CommunityMech:000441
  field_paths:
  - cultivation_setup[0].cultivation_mode
  - cultivation_setup[0].notes
  evidence_ids:
  - cultivation
  - schema
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Dolichospermum_FBCC_A233_Xenic_Phycosphere_Community.yaml
    role: canonical_record
  ownership_note: Future maintained YAML curation only; preserve sources, caches,
    history and prior reviews.
- finding_id: gtdb-source
  issue_key: cm-000441-gtdb-source
  category: grounding
  severity: minor
  native_severity: P3
  normalization_reason: Bounded representation or provenance repair; identity and
    qualified genomic conclusions remain supported.
  rule_id: review-checklist.claim-specific-support-and-context
  status: open
  certainty: confirmed
  title: Record available GTDB classifications with scope
  description: All three UNRESOLVED statuses omit recoverable source study-genome
    classifications; two local genus routes also resolve. These sources must remain
    distinct.
  target_ids:
  - CommunityMech:000441
  field_paths:
  - taxonomy[0].taxon_term
  - taxonomy[1].taxon_term
  - taxonomy[2].taxon_term
  evidence_ids:
  - study-taxonomy
  - gtdb
  - ontology
  - supplement
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Dolichospermum_FBCC_A233_Xenic_Phycosphere_Community.yaml
    role: canonical_record
  ownership_note: Future maintained YAML curation only; preserve sources, caches,
    history and prior reviews.
- finding_id: snippet-case
  issue_key: cm-000441-snippet-case
  category: evidence
  severity: minor
  native_severity: P3
  normalization_reason: Bounded representation or provenance repair; identity and
    qualified genomic conclusions remain supported.
  rule_id: review-checklist.claim-specific-support-and-context
  status: open
  certainty: confirmed
  title: Restore the exact discussion excerpt
  description: The excerpt capitalizes these despite its lowercase occurrence after
    However, in the source sentence.
  target_ids:
  - CommunityMech:000441
  field_paths:
  - discussions[0].evidence[0].snippet
  evidence_ids:
  - snippet-context
  - snippets
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Dolichospermum_FBCC_A233_Xenic_Phycosphere_Community.yaml
    role: canonical_record
  ownership_note: Future maintained YAML curation only; preserve sources, caches,
    history and prior reviews.
actions:
- action_id: repair-community-metadata
  description: Remove unsupported equilibrium and attach method-specific abundance
    context.
  finding_ids:
  - community-metadata
  target_ids:
  - CommunityMech:000441
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Dolichospermum_FBCC_A233_Xenic_Phycosphere_Community.yaml
    role: canonical_record
  acceptance_checks:
  - Omit unsupported STABLE or explicitly retain unresolved state without forcing
    TRANSIENT or ENGINEERED. Source maintenance alone is not equilibrium.
  - For Sphingorhabdus, qualify any RARE value to its marker-based observation and
    uncertainty; for Brevundimonas, leave ordinal prominence unassigned unless separately
    supported. Do not substitute genome mapping fractions as cell abundance.
  - Retain cyanobacterial DOMINANT with source context, three recovered-genome scope
    and incomplete census. Do not impose historic numerical enum cutoffs or invent
    optional roles.
- action_id: repair-culture-mode
  description: Represent the reported maintenance regime directly.
  finding_ids:
  - culture-mode
  target_ids:
  - CommunityMech:000441
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Dolichospermum_FBCC_A233_Xenic_Phycosphere_Community.yaml
    role: canonical_record
  acceptance_checks:
  - Use OTHER with the approximately ten-day single-filament transfer description,
    or omit an unsupported mode. Do not infer partial harvest, working volume or closed
    batch operation.
  - Retain source BG11, 20 °C, 16:8 h and approximately 3,000 lux with exact local
    evidence.
- action_id: repair-gtdb
  description: Separate study-genome classification from taxon-level crosswalk grounding.
  finding_ids:
  - gtdb-source
  target_ids:
  - CommunityMech:000441
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Dolichospermum_FBCC_A233_Xenic_Phycosphere_Community.yaml
    role: canonical_record
  acceptance_checks:
  - Capture source GTDB-Tk v2.5.2/r226, full Table 2 lineages and Results representative-specific
    ANI/alignment fractions for the three exact recovered genomes. Preserve Sphingorhabdus_B
    sp023910635 and Brevundimonas sp040380105 as unnamed genome species clusters,
    not formally named species.
  - 'If adding generic taxon-level blocks, use verified genus routes with current
    snapshot/method/counts: Sphingorhabdus_B 27/27 and Brevundimonas 221/221. Do not
    override the source genome result with the ambiguous cyanobacterial local name
    fallback.'
  - Retain valid NCBI species/genus labels and ADA naming context. Keep RefSeq ANIb/dDDH
    distinct from GTDB-Tk ANI/AF. Reference genomes and BioSamples are not automatically
    isolate stocks or NCBI Assembly accessions.
- action_id: repair-snippet
  description: Make the negative cross-feeding excerpt verbatim.
  finding_ids:
  - snippet-case
  target_ids:
  - CommunityMech:000441
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Dolichospermum_FBCC_A233_Xenic_Phycosphere_Community.yaml
    role: canonical_record
  acceptance_checks:
  - Restore source lowercase these or include its exact preceding context; do not
    change the supported negative inference or fabricate a sentence.
  - Run the native reference validator and an independent case-preserving literal
    check after separately authorized curation.
- action_id: validate-curation
  description: Validate any separately authorized record changes.
  finding_ids:
  - community-metadata
  - culture-mode
  - gtdb-source
  - snippet-case
  target_ids:
  - CommunityMech:000441
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Dolichospermum_FBCC_A233_Xenic_Phycosphere_Community.yaml
    role: canonical_record
  acceptance_checks:
  - Run focused schema, strict, ontology-label, reference, GTDB/domain and history
    gates; preserve the two computational PARTIAL nodes and zero arrows.
  - Do not alter source caches or prior history to make evidence pass; root alone
    saves this review and runs its post-save checks.
limitations:
- No longitudinal community profile, axenic comparator, bacterial localization, cofactor
  production/transfer, expression or growth-rescue assay is established by this source.
- S1 reading is limited to headers/first row and two source representative rows. S3
  covers inventory/headers and 32 selected rows; no claim of reanalysing every reference
  genome, module, raw sequence or annotation.
- Figure 4 ring-path KO labels conflict with S4. BioU EC typography and repeated coordinates
  were not independently adjudicated. These unencoded source details are not added
  to the record.
- Source-specific GTDB classifications, generic local taxon routes and formally named
  NCBI taxa have different scopes. The exact FBCC catalogue entry and public assembly
  IDs were not recovered by bounded checks; no global absence is asserted.
- The optional structured adapter could not run in the owned environment; BioU/metH/metE
  relevance is explicit and organism coverage remains unknown.
- Completion concerns this bounded record review and does not close issues, promote
  native record status or authorize curation.
notes:
- All 31 official input hashes remain unchanged. Eight linked dimensions, four exact
  graph excerpt hashes and zero-arrow scope are explicit.
- Required native checks passed; ancillary display/retrieval failures are distinct.
  No candidate failure is presumed before actual validation.
- Lead subsequently read exact batch 33 records[1] and shared metadata, whole adversarial
  report and first 20,000 cache characters; support read the entire cache and current
  issue/cohort scopes.
- The only direct source quote has two words. Root owns saving and post-save gates.
tags:
- record-review
- phytoplankton
- genomic-potential
- batch-16
```
