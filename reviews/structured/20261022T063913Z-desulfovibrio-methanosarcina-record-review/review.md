# Desulfovibrio–Methanosarcina lactate syntrophy record review

- Review: 20261022T063913Z-desulfovibrio-methanosarcina-record-review
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-22T06:29:07.974946Z
- Finished UTC: 2026-10-22T06:39:13.322365Z
- Reviewer: codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The defined pair and qualified three-node, two-arrow mechanism are supported by the complete scanned article. One major finding concerns medium and assay conflation; three minor findings concern strain metadata, exact claim evidence and publication-as-dataset typing. All eight required native checks passed. Literal completeness is 85 and quality is capped at 100 (raw 109).

## Scope And Provenance

Whole released target and encoded claims, using the complete nine-page primary article, all tables/figures, bounded authority/resource metadata and actual native checks.

Selection: Only released CommunityMech:000150 in owned batch16.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base cb7a782c8ba80299dca8761ad0a2c90bccd8a117.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000150 | kb/communities/Desulfovibrio_Methanosarcina_Lactate_Syntrophy.yaml | maintained | Desulfovibrio-Methanosarcina Lactate Syntrophy |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000150 | Actual native exit 0. |
| validate-strict | passed | True | CommunityMech:000150 | Actual native exit 0. |
| validate-terms | passed | True | CommunityMech:000150 | Actual native exit 0. |
| validate-references-explained | passed | True | CommunityMech:000150 | Actual native exit 0. |
| validate-gtdb | passed | True | CommunityMech:000150 | Actual native exit 0. |
| validate-gtdb-domain | passed | True | CommunityMech:000150 | Actual native exit 0. |
| validate-history | passed | True | CommunityMech:000150 | Actual native exit 0. |
| normalize-cache-names-check | passed | True | CommunityMech:000150 | Actual native exit 0. |
| audit-network corpus context | failed | False | CommunityMech:000150 | Actual corpus exit 1 retained. |
| check-network-quality corpus context | failed | False | CommunityMech:000150 | Actual corpus exit 1 retained. |
| Optional structured source adapter | unavailable | False | CommunityMech:000150 | Unavailable in the owned runtime. |

## Scientific And Domain Assessments

### Exact source pair and stock metadata

identity: concern. Targets: CommunityMech:000150.

The community identity is sound; structured strain metadata can be made exact.

Retain SYNTHETIC origin, ENGINEERED state and SYNTROPHY category. Essex 6 and MS occur in node 0, but member records lack the source stock identifiers. EC1 and PS comparisons are not additional members.

### Lactate Degradation to Acetate and Methane

graph: supported. Targets: CommunityMech:000150.

Retain positive lactate degradation and product provision.

Exact selector ecological_interactions[0]; scope PAIRWISE; interaction_type SYNTROPHY. Participants: {"source_taxon": {"preferred_term": "Desulfovibrio desulfuricans", "term": {"id": "NCBITaxon:876", "label": "Desulfovibrio desulfuricans"}}, "target_taxon": {"preferred_term": "Methanosarcina barkeri", "term": {"id": "NCBITaxon:2208", "label": "Methanosarcina barkeri"}}}. Exact canonical snippet bindings: [{"selector": "ecological_interactions[0].evidence[0].snippet", "sha256": "1ba31b86afd428c3c4f8bdaa0e4e3f213cf7afc9d68dd29bf383d444baff0ee4", "reference": "PMID:16345708", "supports": "SUPPORT", "evidence_source": "IN_VITRO"}]. PMID:16345708 locator: Tables 1–3, printed pages 347, 349–350; Figures 2–3, pages 350–351. Exact-pair carbon and gas time courses support donor products and methanogenesis. Table 1 is reaction accounting, not a complete measured coculture carbon balance.

### Acetate Conversion by Methanosarcina

graph: supported. Targets: CommunityMech:000150.

Retain intrinsic recipient acetate methanogenesis.

Exact selector ecological_interactions[1]; scope PAIRWISE; interaction_type None. Participants: {"source_taxon": {"preferred_term": "Methanosarcina barkeri", "term": {"id": "NCBITaxon:2208", "label": "Methanosarcina barkeri"}}, "target_taxon": null}. Exact canonical snippet bindings: [{"selector": "ecological_interactions[1].evidence[0].snippet", "sha256": "c865bc5328df999187fabc50065f20ce5346bd88e1684bd70f3ba5421fc27480", "reference": "PMID:16345708", "supports": "SUPPORT", "evidence_source": "IN_VITRO"}]. PMID:16345708 locator: Results Fermentation products. and time course, printed pages 349–351; Figures 1–3, pages 350–351. This source-only PAIRWISE process is not reverse cross-feeding. Coculture CO2 is presumed; pure MS CO2 measurement is a separate assay.

### Hydrogen Inhibition of Acetate Degradation

graph: supported. Targets: CommunityMech:000150.

Retain conditional hydrogen inhibition with PARTIAL donor attribution.

Exact selector ecological_interactions[2]; scope PAIRWISE; interaction_type None. Participants: {"source_taxon": {"preferred_term": "Desulfovibrio desulfuricans", "term": {"id": "NCBITaxon:876", "label": "Desulfovibrio desulfuricans"}}, "target_taxon": {"preferred_term": "Methanosarcina barkeri", "term": {"id": "NCBITaxon:2208", "label": "Methanosarcina barkeri"}}}. Exact canonical snippet bindings: [{"selector": "ecological_interactions[2].evidence[0].snippet", "sha256": "eb6af80aef4e7793343faf93dc534720d13c7915682f519283bc2d338472e103", "reference": "PMID:16345708", "supports": "PARTIAL", "evidence_source": "IN_VITRO"}]. PMID:16345708 locator: Results Effect of lactate and H2 on acetate degradation by M. barkeri., printed page 351; Figures 4–5, page 352; Discussion pages 352–353. Pure-MS H2 perturbation and exact-pair time courses support conditional delay. Hydrogen can increase growth and methane; enzyme repression is proposed, not directly resolved.

### Lactate Degradation to Acetate and Methane → Acetate Conversion by Methanosarcina

graph: supported. Targets: CommunityMech:000150.

Retain donor acetate provision to later recipient use.

Exact selector ecological_interactions[0].downstream[0]; source Lactate Degradation to Acetate and Methane; target Acetate Conversion by Methanosarcina. Participants and exact excerpts are bound in node assessments. Exact description: Donor-produced acetate supplies the later methanogenic substrate. Its utilization timing also depends on hydrogen and medium conditions. Description SHA256 a02384dcdd5a66a81b603520a8251f9dceefcab49d2559ab5075dd080688a227. PMID:16345708, Figures 2–3 on pages 350–351. Timing also depends on hydrogen and medium; provision does not establish a universal sequence.

### Lactate Degradation to Acetate and Methane → Hydrogen Inhibition of Acetate Degradation

graph: supported. Targets: CommunityMech:000150.

Retain the PARTIAL donor-hydrogen attribution.

Exact selector ecological_interactions[0].downstream[1]; source Lactate Degradation to Acetate and Methane; target Hydrogen Inhibition of Acetate Degradation. Participants and exact excerpts are bound in node assessments. Exact description: PARTIAL - donor hydrogen production is implicated in delayed acetate use by coculture time courses and separate pure-culture hydrogen perturbation, not selective removal of donor hydrogen in the exact pair. Description SHA256 cec93796be5ed7e9a98cba317f2dd33b5380636c550ec332d82c652ef9e88afc. PMID:16345708, Figures 2–3 on pages 350–351 and pure-culture Figures 4–5 on page 352. No exact-pair selective hydrogen-removal intervention was performed. Adding a negative arrow is optional new structure, not a prerequisite for this review.

### YE, RV and inoculum/assay separation

evidence: concern. Targets: CommunityMech:000150.

The record presents RV generally even though the principal pair time course uses YE.

RV contains 5% rumen fluid, minerals, B vitamins and reducing agents. YE is otherwise identical to RV. Rumen fluid, B vitamins and the Pfennig mineral/metal solution are omitted; 0.1% yeast extract, nitrogen/sulfur-free mineral solution 3 and 10 mM NH4Cl are added, while the reducing agents are retained. The paper refers elsewhere for full recipes. Record no added Na2SO4 rather than chemical sulfate zero. Recover source conditions without importing a generic modern recipe.

### Exact partner and interpretation context

evidence: concern. Targets: CommunityMech:000150.

Two authentic Abstract fragments come from the M. smithii comparator sentence.

Replace taxonomy[0].evidence[0] and related_ingredients[0].evidence[0] with exact focal-pair context; the underlying biology is supported by the next Abstract sentence and body. Preserve presumed CO2 in the summary and source-attributed, conditional hydrogen regulation in related_ingredients[2].relevance, consistent with the graph.

### Valid species ambiguity and optional stock routes

grounding: supported. Targets: CommunityMech:000150.

All ten ID/label pairs match and both current GTDB candidate sets reproduce.

Optional exact stock routes NCBITaxon:1121445 and NCBITaxon:1434108 map through source-linked IDs to GTDB D. desulfuricans (1.0/6) and M. barkeri (1.0/2). These reference counts are not culture abundance. No release/build string is encoded, and no forced replacement follows from species ambiguity.

### Publication versus deposited dataset

representation: concern. Targets: CommunityMech:000150.

The exact PMID is valid but is represented as a PHENOTYPE dataset.

Retain the paper as a publication/source resource. Do not invent an archive accession or treat the paper URL as a deposited phenotype dataset. No raw data or archive-absence search was performed.

### Complete scanned article and real access limits

scope: supported. Targets: CommunityMech:000150.

All nine authentic source pages were visually read.

This includes all three tables, five figures/captions, main narrative and 26 references. EPMC XML returned an error and the PDF route returned HTML; neither was used as article content. The original page images supplied the complete article. No supplement is declared in the inspected article/landing metadata; no wider absence claim.

### Maintained owner and historical scope

ownership: supported. Targets: CommunityMech:000150.

Future repairs belong to the canonical YAML under separate curation authorization.

Ignored-inclusive discovery pinned all eight focal contexts. Prior graph repair is preserved; open discussions and issues are not closed by this review. No canonical, cache, history, issue or Git mutation was performed.

### Actual native validation

schema: supported. Targets: CommunityMech:000150.

All eight required native checks passed.

Reference zero-issue output does not count reviewed excerpts; twelve independent lexical matches do not establish claim entailment.

### Literal native metrics

completeness: supported. Targets: CommunityMech:000150.

Completeness 85; raw quality 109, capped 100.

## Findings

### medium-assay: Separate YE and RV experiments

major / open / confirmed; issue key: cm-000150-medium-assay.

The general RV assignment obscures the YE principal coculture and assay-specific gases, inocula and conditions. Sulfate-free shorthand exceeds no added sulfate.

### strain-metadata: Represent exact source strains

minor / open / confirmed; issue key: cm-000150-strain-metadata.

The source establishes Essex 6/DSM 642 and MS/DSM 800, while structured members remain only species-level.

### claim-evidence: Use exact focal-pair evidence and qualifications

minor / open / confirmed; issue key: cm-000150-claim-evidence.

Two excerpts come from the M. smithii comparator sentence. The focal biology is supported elsewhere, while summary CO2 and hydrogen interpretation need the existing graph qualifications.

### publication-dataset: Represent the PMID as a publication resource

minor / open / confirmed; issue key: cm-000150-publication-dataset.

PMID:16345708 identifies the source article, not a deposited PHENOTYPE dataset.

## Recommended Actions And Acceptance Checks

### repair-medium

Separate source formulations and assay stages.

- Represent YE as the routine pair maintenance and Figure 2 medium; retain RV and YE/RV comparison as separate contexts. Do not replace every RV mention, because RV is valid in specific experiments.
- Recover source 35 °C, basal 80:20 N2/CO2 and preparation pH 7.2. For Figure 2 record 50 mL medium in 125 mL bottles, 25 mM lactate and 10 mL inoculum, with static incubation. Keep Figure 3 tube assays and pure-MS hydrogen/shaking treatments separate.
- Document pair establishment with 1 mL of each partner, serial 2 mL transfer into 8 mL YE every two weeks and at least four transfers before experiments. Do not confuse this with the methanogen acetate adaptation protocol.
- Use no added Na2SO4 instead of chemically zero sulfate. Preserve source recipe references where composition is not fully specified; no generic catalogue recipe import.

### repair-strains

Add source-stock metadata without losing current mapping scope.

- Record Essex 6/DSM 642 and MS/DSM 800 at their taxonomy entries using the Methods stock paragraph. The current species IDs and AMBIGUOUS sets are valid.
- If selecting exact strain IDs, use the verified source-linked NCBITaxon:1121445 and NCBITaxon:1434108 routes and update all participant copies consistently. Do not infer culture abundance or unverified collection type status from reference mappings.

### repair-claims

Place evidence at the correct partner and assay scope.

- Replace the comparator excerpts with contiguous source text that explicitly supports the focal M. barkeri pair; do not characterize the underlying lactate phenotype as false.
- Carry presumed coculture CO2 and conditional donor-H2 interpretation into summary/non-graph wording. Preserve pure-culture perturbation versus exact-pair inference, increased growth/methane and proposed enzyme repression.
- Retain all three current nodes and two arrows with their existing limits. A proposed extra negative arrow remains separately scoped research, not a mandatory connectivity repair.

### repair-resource

Retain the article under appropriate bibliographic representation.

- Remove or reclassify the publication-only dataset entry using a supported publication/external-resource representation. Keep exact PMID/DOI/PMC identity; do not invent a deposit or claim none exists globally.

### validate-curation

Validate any separately authorized canonical changes.

- Run focused schema, strict, term, reference, GTDB and history checks after actual edits, plus required generated-document checks. Preserve original caches/history and graph review decisions. Root alone saves this review and runs post-save gates.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | kb/communities/Desulfovibrio_Methanosarcina_Lactate_Syntrophy.yaml; Whole maintained YAML | supports | Two species-level members, three nodes and two directed arrows. |
| abstract | PMID:16345708; DOI:10.1128/aem.41.2.346-354.1981; Fresh MED resultList.result[0].abstractText, all sentences | supports | All twelve excerpts are authentic; the first sentence concerns M. smithii comparator pairs. |
| identity | PMID:16345708; DOI:10.1128/aem.41.2.346-354.1981; Printed page 347, Materials and Methods, Bacterial strains., sole paragraph | supports | Essex 6 = DSM 642 and MS = DSM 800 are the exact focal stocks. EC1 and PS/DSM 861 are comparators. |
| cultivation | PMID:16345708; DOI:10.1128/aem.41.2.346-354.1981; Printed page 348, left column, Materials and Methods, Media and conditions of cultivation., paragraph beginning The cocultures of D. desulfuricans or D. vulgaris; quoted words in this paragraph. | supports | Routine pair establishment and serial maintenance use YE. Incubation and hydrogen-added shaking are separately specified below. |
| medium-definition | PMID:16345708; DOI:10.1128/aem.41.2.346-354.1981; Printed page 347, right column, Media and conditions of cultivation., paragraph beginning The basal RV medium | supports | RV and YE differ in rumen fluid, vitamins, mineral stocks, yeast extract and ammonium. Prior references supply additional recipe details. |
| products | PMID:16345708; DOI:10.1128/aem.41.2.346-354.1981; Printed page 349, Table 2 with all footnotes; Results Growth and methane formation. and Fermentation products. | supports | Positive lactate and acetate phenotypes belong to specific strains and media; pure M. barkeri and M. smithii controls differ. |
| time-course | PMID:16345708; DOI:10.1128/aem.41.2.346-354.1981; Printed page 350, Table 3 and Figure 2 with captions; Results Time course of lactate and acetate degradation in M. barkeri-D. desulfuricans cocultures. | supports | Figure 2 uses YE, 25 mM lactate and 50 mL medium in 125 mL bottles. Methane is observed; coculture CO2 remains presumed. |
| medium-comparison | PMID:16345708; DOI:10.1128/aem.41.2.346-354.1981; Printed page 351, Figure 3 and caption; Results Effect of lactate and H2 on acetate degradation by M. barkeri. | supports | YE and RV are compared at 20 mM acetate with 0, 5 or 20 mM lactate; pure methanogen lactate controls are distinct. |
| hydrogen-perturbation | PMID:16345708; DOI:10.1128/aem.41.2.346-354.1981; Printed page 352, Figures 4 and 5 with complete captions and Discussion | supports | Pure MS in RV is exposed to added H2. Acetate use is delayed while growth and methane can increase; this is not donor-specific hydrogen removal in the pair. |
| mechanism-limits | PMID:16345708; DOI:10.1128/aem.41.2.346-354.1981; Printed page 353, Discussion first paragraph continuing from page 352 | supports | Enzyme repression is proposed and alternative explanations remain. Continuous-culture and three-member follow-ups are suggestions, not current assays. |
| thermodynamics | PMID:16345708; DOI:10.1128/aem.41.2.346-354.1981; Printed page 347, Table 1 and footnote; read with Discussion on page 352 | supports | Hydrogen consumption supports donor metabolism. Whole-fermentation standard free energy must not be conflated with the hydrogen-sensitive physiological step. |
| ontology | /private/tmp/cm-review-session/batch-16/000150/ontology-authority.json; Ten exact ID/label pairs and 23 placements | supports | All encoded labels match the current authority; source scope is assessed separately. |
| schema | /private/tmp/cm-review-session/batch-16/000150/child-schema-semantics.json; Current role, interaction, cultivation and identity definitions | supports | Syntrophy requires beneficial product removal, not obligacy. Publication identity does not by itself establish a dataset. |
| gtdb | /private/tmp/cm-review-session/batch-16/000150/child-gtdb-crosswalk.json; Both current species-level candidate sets | supports | Existing AMBIGUOUS sets reproduce; no release/build provenance error is encoded. |
| strains | /private/tmp/cm-review-session/batch-16/000150/child-strain-candidates.json; Source-linked exact stock candidates and parents | supports | NCBITaxon:1121445 and NCBITaxon:1434108 are optional narrower stock routes; no forced species replacement. |
| semantics | /private/tmp/cm-review-session/batch-16/000150/ontology-semantic-notes.json; Final whole-source semantic assessment | supports | Positive roles and qualified graph remain supported; repair medium, member metadata, claim evidence and publication typing. |
| resources | /private/tmp/cm-review-session/batch-16/000150/dataset-verification.json; Whole encoded publication resource and fresh MED identity | supports | The PMID identifies the paper, not a deposited PHENOTYPE dataset. No archive-absence claim. |
| external-links | /private/tmp/cm-review-session/batch-16/000150/external-resource-verification.json; Whole canonical resource-link inventory | supports | No cross-Mech or assembly link is encoded; no unrelated archive request was needed. |
| snippets | /private/tmp/cm-review-session/batch-16/000150/snippet-audit.json; Twelve actual excerpt placements | supports | All match fresh MED Abstract and cache; two excerpts belong to comparator context. |
| provenance | /private/tmp/cm-review-session/batch-16/000150/provenance-audit.json; Exact focal history, batch32 row, cohort and current issue scopes | supports | Prior qualified graph is retained; historical needs_research discussion is not a failed native check. |
| inspection | /private/tmp/cm-review-session/batch-16/000150/inspect.json; Official 30-input inspection | supports | Target, 21 authorities and eight focal contexts were pinned before assessment. |
| assets | /private/tmp/cm-review-session/batch-16/000150/lead-source-assets.json; Nine authentic scanned pages and bounded failed routes | supports | All pages were read visually; failed PDF/XML responses are not source content. |
| lead-read | /private/tmp/cm-review-session/batch-16/000150/lead-primary-read-scope.json; Actual source and local-context reading | supports | Whole scanned article, all five figures and three tables read. OCR is a derivative aid, not a separate whole-text reading claim. |
| locators | /private/tmp/cm-review-session/batch-16/000150/source-locator-verification.json; Direct printed page, heading, table and caption locators | supports | The sole two-word quotation was verified visually on printed page 348. |
| source-audit | /private/tmp/cm-review-session/batch-16/000150/source-audit.json; Final lead source assessment | supports | One major and three minor findings; all three nodes and two arrows retained. |
| root-erratum | /private/tmp/cm-review-session/batch-16/000150/root-fig2-inoculum-erratum.json; Printed page 350 Figure 2 inoculum clarification | supports | The preserved root reading-note typo is corrected: Figure 2 uses 10 mL inoculum, distinct from 50 mL starting medium. |
| root-source | /private/tmp/cm-review-session/batch-16/000150/root-independent-source-audit.json; Independent root source assessment | supports | Independent whole-page and authority reading agrees with the scoped conclusions. |
| metrics | /private/tmp/cm-review-session/batch-16/000150/support-final-audit.json; Final independent reconciliation | supports | Literal completeness 85; base 125 less 16 gives raw 109, capped 100. |
| support-manifest | /private/tmp/cm-review-session/batch-16/000150/support-frozen-manifest.json; Frozen supporting dependencies | supports | Current source and input pins verified. |
| auxiliary | /private/tmp/cm-review-session/batch-16/000150/auxiliary-frozen-manifest.json; Frozen authority/native dependencies | supports | All eight actual required native checks passed. |
| native-summary | /private/tmp/cm-review-session/batch-16/000150/final-validator-summary.json; Eight actual required checks | supports | No native target failure; deterministic success is separate from source support. |
| corpus-context | /private/tmp/cm-review-session/batch-16/000150/child-corpus-context.json; Fresh batch16 corpus baseline | supports | Nonrequired corpus exits and warnings remain explicit. |
| adapter | /private/tmp/cm-review-session/batch-16/000150/adapter-check.json; Current owned-runtime availability and bounded reused discovery | supports | Optional adapter unavailable in this runtime; no global or biological absence claim. |
| check-validate | /private/tmp/cm-review-session/batch-16/000150/validate.json; Actual command/stdout/stderr | supports | Actual native exit 0; scientific support assessed separately. |
| check-validate-strict | /private/tmp/cm-review-session/batch-16/000150/validate-strict.json; Actual command/stdout/stderr | supports | Actual native exit 0; scientific support assessed separately. |
| check-validate-terms | /private/tmp/cm-review-session/batch-16/000150/validate-terms.json; Actual command/stdout/stderr | supports | Actual native exit 0; scientific support assessed separately. |
| check-validate-references-explained | /private/tmp/cm-review-session/batch-16/000150/validate-references-explained.json; Actual command/stdout/stderr | supports | Actual native exit 0; scientific support assessed separately. |
| check-validate-gtdb | /private/tmp/cm-review-session/batch-16/000150/validate-gtdb.json; Actual command/stdout/stderr | supports | Actual native exit 0; scientific support assessed separately. |
| check-validate-gtdb-domain | /private/tmp/cm-review-session/batch-16/000150/validate-gtdb-domain.json; Actual command/stdout/stderr | supports | Actual native exit 0; scientific support assessed separately. |
| check-validate-history | /private/tmp/cm-review-session/batch-16/000150/validate-history.json; Actual command/stdout/stderr | supports | Actual native exit 0; scientific support assessed separately. |
| check-normalize-cache-names-check | /private/tmp/cm-review-session/batch-16/000150/normalize-cache-names-check.json; Actual command/stdout/stderr | supports | Actual native exit 0; scientific support assessed separately. |
| context-audit-network | /private/tmp/cm-review-session/batch-16/audit-network.json; Fresh batch16 corpus baseline | supports | Actual exit 1 with warning-only corpus findings; zero errors. |
| context-check-network-quality | /private/tmp/cm-review-session/batch-16/check-network-quality.json; Fresh batch16 corpus baseline | supports | Actual exit 1 with warning-only corpus findings; zero errors. |

## Limits And Additional Notes

- The article was read as all nine authentic scanned pages. EPMC XML and PDF requests failed to return full-text payloads; original page images supplied the complete main. OCR is a derivative aid, not an independent whole-text read.
- No supplement was declared in the inspected article or public landing metadata; no global absence search or raw-data reanalysis was performed. Full recipe details delegated by the paper to older references remain bounded.
- Coculture CO2 is presumed; pure-MS CO2 measurements do not resolve the pair carbon balance. Donor-H2 attribution remains partial, and enzyme repression is an interpretation with alternatives.
- Exact stock candidates do not invalidate current species ambiguity. No catalogue maintenance conditions or unverified current type-status claims were imported.
- Open historical research discussions are preserved. Completion of this scientific review does not close issues, promote native record status or authorize canonical curation.
- Eight evidence-linked dimensions are present. Three exact node-excerpt hashes and two exact arrow descriptions bind the current graph.
- The sole primary-source quote contains two words. All 30 official inputs remain unchanged; required native failures: zero.
- Root owns persistence and post-save gates; this candidate itself makes no canonical/cache/history/Git change.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T063913Z-desulfovibrio-methanosarcina-record-review
kind: record
repository: CultureBotAI/CommunityMech
title: Desulfovibrio–Methanosarcina lactate syntrophy record review
started_at: '2026-10-22T06:29:07.974946Z'
finished_at: '2026-10-22T06:39:13.322365Z'
reviewer:
  identity: codex
  kind: agent
  independence: unknown
  independence_basis: Separate lead, root, auxiliary and supporting reviewers; no
    person-level independence claim.
skill: review-yaml-record
completion: completed
verdict: needs_curation
scientific_review: true
summary: The defined pair and qualified three-node, two-arrow mechanism are supported
  by the complete scanned article. One major finding concerns medium and assay conflation;
  three minor findings concern strain metadata, exact claim evidence and publication-as-dataset
  typing. All eight required native checks passed. Literal completeness is 85 and
  quality is capped at 100 (raw 109).
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
  - path: history/records/Desulfovibrio_Methanosarcina_Lactate_Syntrophy/2026-10-06T063854Z-codex-d0c15a.yaml
    sha256: 1d7ed9282445ffcc764493927832f4ac1533ce78992d1a01199689c08eaaad4b
    role: context
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: kb/communities/Desulfovibrio_Methanosarcina_Lactate_Syntrophy.yaml
    sha256: 21a3574175a120649f4dac15a262cf4ec861891f16f8beb1faae6d2ecd01913d
    role: target
  - path: references_cache/PMID_16345708.md
    sha256: 5e0e85bae63d540c243ab12bdc2a3d3fef677857206075289d73efb6c617cf02
    role: context
  - path: reports/causal_graph_review/adversarial-review-20261006-batch32.yaml
    sha256: fb31af941ac34e88b7c749a987c6fef46ab8a95dc173b8ccbdd890e23ee1c279
    role: context
  - path: reports/causal_graph_review/decisions/20261006-three-records-batch32.yaml
    sha256: 400a8403214d7c2fbd88bb8e533cc5e22c2982013a5c900f6ebd62c9a0263f16
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
- target_id: CommunityMech:000150
  path: kb/communities/Desulfovibrio_Methanosarcina_Lactate_Syntrophy.yaml
  label: Desulfovibrio-Methanosarcina Lactate Syntrophy
  kind: maintained
  record_class: MicrobialCommunity
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Desulfovibrio_Methanosarcina_Lactate_Syntrophy.yaml
    role: canonical_record
scope:
  description: Whole released target and encoded claims, using the complete nine-page
    primary article, all tables/figures, bounded authority/resource metadata and actual
    native checks.
  selection: Only released CommunityMech:000150 in owned batch16.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000150
checks:
- check_id: validate
  name: validate
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000150
  command: just --no-dotenv validate kb/communities/Desulfovibrio_Methanosarcina_Lactate_Syntrophy.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate
  scope_note: Target/history checks; cache-name preflight is corpus-wide. All 30 official
    inputs unchanged.
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000150
  command: just --no-dotenv validate-strict kb/communities/Desulfovibrio_Methanosarcina_Lactate_Syntrophy.yaml
    --out /private/tmp/cm-review-session/batch-16/000150/strict-report.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-strict
  scope_note: Target/history checks; cache-name preflight is corpus-wide. All 30 official
    inputs unchanged.
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000150
  command: just --no-dotenv validate-terms kb/communities/Desulfovibrio_Methanosarcina_Lactate_Syntrophy.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-terms
  scope_note: Target/history checks; cache-name preflight is corpus-wide. All 30 official
    inputs unchanged.
- check_id: validate-references-explained
  name: validate-references-explained
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000150
  command: just --no-dotenv validate-references-explained kb/communities/Desulfovibrio_Methanosarcina_Lactate_Syntrophy.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-references-explained
  scope_note: Target/history checks; cache-name preflight is corpus-wide. All 30 official
    inputs unchanged.
- check_id: validate-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000150
  command: just --no-dotenv validate-gtdb kb/communities/Desulfovibrio_Methanosarcina_Lactate_Syntrophy.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb
  scope_note: Target/history checks; cache-name preflight is corpus-wide. All 30 official
    inputs unchanged.
- check_id: validate-gtdb-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000150
  command: just --no-dotenv validate-gtdb-domain kb/communities/Desulfovibrio_Methanosarcina_Lactate_Syntrophy.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb-domain
  scope_note: Target/history checks; cache-name preflight is corpus-wide. All 30 official
    inputs unchanged.
- check_id: validate-history
  name: validate-history
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000150
  command: just --no-dotenv validate-history history/records/Desulfovibrio_Methanosarcina_Lactate_Syntrophy
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-history
  scope_note: Target/history checks; cache-name preflight is corpus-wide. All 30 official
    inputs unchanged.
- check_id: normalize-cache-names-check
  name: normalize-cache-names-check
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000150
  command: uv run python scripts/normalize_cache_names.py --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-normalize-cache-names-check
  scope_note: Target/history checks; cache-name preflight is corpus-wide. All 30 official
    inputs unchanged.
- check_id: context-audit-network
  name: audit-network corpus context
  status: failed
  required: false
  summary: Actual corpus exit 1 retained.
  target_ids:
  - CommunityMech:000150
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-16/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv audit-network
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - context-audit-network
  - corpus-context
  scope_note: Nonrequired corpus context, not a target or candidate failure.
- check_id: context-check-network-quality
  name: check-network-quality corpus context
  status: failed
  required: false
  summary: Actual corpus exit 1 retained.
  target_ids:
  - CommunityMech:000150
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-16/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv check-network-quality
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - context-check-network-quality
  - corpus-context
  scope_note: Nonrequired corpus context, not a target or candidate failure.
- check_id: optional-structured-adapter
  name: Optional structured source adapter
  status: unavailable
  required: false
  summary: Unavailable in the owned runtime.
  target_ids:
  - CommunityMech:000150
  evidence_ids:
  - adapter
  scope_note: No other checkout execution, installation or biological absence inference.
evidence:
- evidence_id: record
  kind: record_content
  reference: kb/communities/Desulfovibrio_Methanosarcina_Lactate_Syntrophy.yaml
  locator: Whole maintained YAML
  summary: Two species-level members, three nodes and two directed arrows.
  support: supports
  accessed_at: '2026-10-22T06:36:27.064016Z'
- evidence_id: abstract
  kind: primary_source
  reference: PMID:16345708; DOI:10.1128/aem.41.2.346-354.1981
  locator: Fresh MED resultList.result[0].abstractText, all sentences
  summary: All twelve excerpts are authentic; the first sentence concerns M. smithii
    comparator pairs.
  support: supports
  accessed_at: '2026-10-22T06:36:27.064079Z'
  snapshot_sha256: 0c9c874bfbc58d761fca6dbd7c6206f258c50aff1290aa182eeabe709576c423
- evidence_id: identity
  kind: primary_source
  reference: PMID:16345708; DOI:10.1128/aem.41.2.346-354.1981
  locator: Printed page 347, Materials and Methods, Bacterial strains., sole paragraph
  summary: Essex 6 = DSM 642 and MS = DSM 800 are the exact focal stocks. EC1 and
    PS/DSM 861 are comparators.
  support: supports
  accessed_at: '2026-10-22T06:36:27.064111Z'
  snapshot_sha256: 3ee6d6477c490b5939a7a61babbde5964f31da8bdb09db5fcf8b87349acf6f75
- evidence_id: cultivation
  kind: primary_source
  reference: PMID:16345708; DOI:10.1128/aem.41.2.346-354.1981
  locator: Printed page 348, left column, Materials and Methods, Media and conditions
    of cultivation., paragraph beginning The cocultures of D. desulfuricans or D.
    vulgaris; quoted words in this paragraph.
  summary: Routine pair establishment and serial maintenance use YE. Incubation and
    hydrogen-added shaking are separately specified below.
  support: supports
  accessed_at: '2026-10-22T06:36:27.064187Z'
  snapshot_sha256: bed13add728d4a7304a30b97fdb0a045a0f32481471cc58dc8935aedb114ea35
  quote: YE medium
- evidence_id: medium-definition
  kind: primary_source
  reference: PMID:16345708; DOI:10.1128/aem.41.2.346-354.1981
  locator: Printed page 347, right column, Media and conditions of cultivation., paragraph
    beginning The basal RV medium
  summary: RV and YE differ in rumen fluid, vitamins, mineral stocks, yeast extract
    and ammonium. Prior references supply additional recipe details.
  support: supports
  accessed_at: '2026-10-22T06:36:27.064268Z'
  snapshot_sha256: 3ee6d6477c490b5939a7a61babbde5964f31da8bdb09db5fcf8b87349acf6f75
- evidence_id: products
  kind: primary_source
  reference: PMID:16345708; DOI:10.1128/aem.41.2.346-354.1981
  locator: Printed page 349, Table 2 with all footnotes; Results Growth and methane
    formation. and Fermentation products.
  summary: Positive lactate and acetate phenotypes belong to specific strains and
    media; pure M. barkeri and M. smithii controls differ.
  support: supports
  accessed_at: '2026-10-22T06:36:27.064330Z'
  snapshot_sha256: 64c370d315ff3ec5a69efbbf0b522767c2c8336c31f551bd9279a845b11c07bf
- evidence_id: time-course
  kind: primary_source
  reference: PMID:16345708; DOI:10.1128/aem.41.2.346-354.1981
  locator: Printed page 350, Table 3 and Figure 2 with captions; Results Time course
    of lactate and acetate degradation in M. barkeri-D. desulfuricans cocultures.
  summary: Figure 2 uses YE, 25 mM lactate and 50 mL medium in 125 mL bottles. Methane
    is observed; coculture CO2 remains presumed.
  support: supports
  accessed_at: '2026-10-22T06:36:27.064391Z'
  snapshot_sha256: d5f5813e79e351af70fcc904cdb5a3967829276fb8c9e3801db6d8aded5a7c01
- evidence_id: medium-comparison
  kind: primary_source
  reference: PMID:16345708; DOI:10.1128/aem.41.2.346-354.1981
  locator: Printed page 351, Figure 3 and caption; Results Effect of lactate and H2
    on acetate degradation by M. barkeri.
  summary: YE and RV are compared at 20 mM acetate with 0, 5 or 20 mM lactate; pure
    methanogen lactate controls are distinct.
  support: supports
  accessed_at: '2026-10-22T06:36:27.064445Z'
  snapshot_sha256: 04ae44c415d843c16dd0c789ef356e049f6e62717458cd30c9248a64a17e81bc
- evidence_id: hydrogen-perturbation
  kind: primary_source
  reference: PMID:16345708; DOI:10.1128/aem.41.2.346-354.1981
  locator: Printed page 352, Figures 4 and 5 with complete captions and Discussion
  summary: Pure MS in RV is exposed to added H2. Acetate use is delayed while growth
    and methane can increase; this is not donor-specific hydrogen removal in the pair.
  support: supports
  accessed_at: '2026-10-22T06:36:27.064504Z'
  snapshot_sha256: 1196a3ff69e286d34d44189b4be0fb0232ed9051ef55bbfd5484c116e41103a5
- evidence_id: mechanism-limits
  kind: primary_source
  reference: PMID:16345708; DOI:10.1128/aem.41.2.346-354.1981
  locator: Printed page 353, Discussion first paragraph continuing from page 352
  summary: Enzyme repression is proposed and alternative explanations remain. Continuous-culture
    and three-member follow-ups are suggestions, not current assays.
  support: supports
  accessed_at: '2026-10-22T06:36:27.064563Z'
  snapshot_sha256: 8ad9e33f918df9085bab908919fc94d21b8ae5038ebcec8a67981040e8916c89
- evidence_id: thermodynamics
  kind: primary_source
  reference: PMID:16345708; DOI:10.1128/aem.41.2.346-354.1981
  locator: Printed page 347, Table 1 and footnote; read with Discussion on page 352
  summary: Hydrogen consumption supports donor metabolism. Whole-fermentation standard
    free energy must not be conflated with the hydrogen-sensitive physiological step.
  support: supports
  accessed_at: '2026-10-22T06:36:27.064637Z'
  snapshot_sha256: 3ee6d6477c490b5939a7a61babbde5964f31da8bdb09db5fcf8b87349acf6f75
- evidence_id: ontology
  kind: authority
  reference: /private/tmp/cm-review-session/batch-16/000150/ontology-authority.json
  locator: Ten exact ID/label pairs and 23 placements
  summary: All encoded labels match the current authority; source scope is assessed
    separately.
  support: supports
  accessed_at: '2026-10-22T06:36:27.064703Z'
  snapshot_sha256: adf9d84f772ac76af4ddbc1339a92de9f81b77048a964c774b193007d70d3132
- evidence_id: schema
  kind: authority
  reference: /private/tmp/cm-review-session/batch-16/000150/child-schema-semantics.json
  locator: Current role, interaction, cultivation and identity definitions
  summary: Syntrophy requires beneficial product removal, not obligacy. Publication
    identity does not by itself establish a dataset.
  support: supports
  accessed_at: '2026-10-22T06:36:27.064738Z'
  snapshot_sha256: 4e1324ea67abc7f84db3c7e959cfd14042fa1c09b94e7063a80310dc1f82f8d6
- evidence_id: gtdb
  kind: authority
  reference: /private/tmp/cm-review-session/batch-16/000150/child-gtdb-crosswalk.json
  locator: Both current species-level candidate sets
  summary: Existing AMBIGUOUS sets reproduce; no release/build provenance error is
    encoded.
  support: supports
  accessed_at: '2026-10-22T06:36:27.064771Z'
  snapshot_sha256: 486fda0eeb930b4734f998b7677b54bde7cd248cafb9732440454b32d4cd0fce
- evidence_id: strains
  kind: authority
  reference: /private/tmp/cm-review-session/batch-16/000150/child-strain-candidates.json
  locator: Source-linked exact stock candidates and parents
  summary: NCBITaxon:1121445 and NCBITaxon:1434108 are optional narrower stock routes;
    no forced species replacement.
  support: supports
  accessed_at: '2026-10-22T06:36:27.064798Z'
  snapshot_sha256: 8d9e7fc827a49b52ac2b514b956e57e41c95b71f9561d361c19bf6530cb2f14d
- evidence_id: semantics
  kind: authority
  reference: /private/tmp/cm-review-session/batch-16/000150/ontology-semantic-notes.json
  locator: Final whole-source semantic assessment
  summary: Positive roles and qualified graph remain supported; repair medium, member
    metadata, claim evidence and publication typing.
  support: supports
  accessed_at: '2026-10-22T06:36:27.064824Z'
  snapshot_sha256: 6ba3b1a3aaf4e4535ab6954b8d0927d23ff6c74c575091aa6b30fc340ab80e71
- evidence_id: resources
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000150/dataset-verification.json
  locator: Whole encoded publication resource and fresh MED identity
  summary: The PMID identifies the paper, not a deposited PHENOTYPE dataset. No archive-absence
    claim.
  support: supports
  accessed_at: '2026-10-22T06:36:27.064854Z'
  snapshot_sha256: aa36a3432df4281174b14573f0e3f1d515c790780d35ee717ee06397d1ea41c6
- evidence_id: external-links
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000150/external-resource-verification.json
  locator: Whole canonical resource-link inventory
  summary: No cross-Mech or assembly link is encoded; no unrelated archive request
    was needed.
  support: supports
  accessed_at: '2026-10-22T06:36:27.064879Z'
  snapshot_sha256: ee6da0d09decc20838ccea4e22045aa5579d63bdda92069ee620fb2d19056231
- evidence_id: snippets
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000150/snippet-audit.json
  locator: Twelve actual excerpt placements
  summary: All match fresh MED Abstract and cache; two excerpts belong to comparator
    context.
  support: supports
  accessed_at: '2026-10-22T06:36:27.064905Z'
  snapshot_sha256: a750928a9575b350455afa2ada2b0c484b4d2e02f34f0e2fa51ad9eb78aba712
- evidence_id: provenance
  kind: prior_review
  reference: /private/tmp/cm-review-session/batch-16/000150/provenance-audit.json
  locator: Exact focal history, batch32 row, cohort and current issue scopes
  summary: Prior qualified graph is retained; historical needs_research discussion
    is not a failed native check.
  support: supports
  accessed_at: '2026-10-22T06:36:27.064932Z'
  snapshot_sha256: c35feafa069e433563f9ec04b78ba182664f802506d7111bd77952aad5706f15
- evidence_id: inspection
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000150/inspect.json
  locator: Official 30-input inspection
  summary: Target, 21 authorities and eight focal contexts were pinned before assessment.
  support: supports
  accessed_at: '2026-10-22T06:36:27.064960Z'
  snapshot_sha256: 2e66f4d6a0bfde531ed9eaa16d2c2c1165885e8ea1a2d9eefadb388f0d08aaf8
- evidence_id: assets
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000150/lead-source-assets.json
  locator: Nine authentic scanned pages and bounded failed routes
  summary: All pages were read visually; failed PDF/XML responses are not source content.
  support: supports
  accessed_at: '2026-10-22T06:36:27.064981Z'
  snapshot_sha256: 90956e9412e4c6b71d727611f72e7c73c12e1413b1e1f0a23212d0eb41abbaa1
- evidence_id: lead-read
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000150/lead-primary-read-scope.json
  locator: Actual source and local-context reading
  summary: Whole scanned article, all five figures and three tables read. OCR is a
    derivative aid, not a separate whole-text reading claim.
  support: supports
  accessed_at: '2026-10-22T06:36:27.065008Z'
  snapshot_sha256: 95a31cbfd12a7b25128bfe0d57a9f777f0823a38ac267ca8edbdb134e303aa0f
- evidence_id: locators
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000150/source-locator-verification.json
  locator: Direct printed page, heading, table and caption locators
  summary: The sole two-word quotation was verified visually on printed page 348.
  support: supports
  accessed_at: '2026-10-22T06:36:27.065033Z'
  snapshot_sha256: 6d6d42019c42330e43b4f8010e9989f227681a45da1f4d2b48037e014016a3bf
- evidence_id: source-audit
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000150/source-audit.json
  locator: Final lead source assessment
  summary: One major and three minor findings; all three nodes and two arrows retained.
  support: supports
  accessed_at: '2026-10-22T06:36:27.065059Z'
  snapshot_sha256: ae8771e4f62424bdf718a38f355206fa28d8055d7f94c84737dccd25645ec16d
- evidence_id: root-erratum
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000150/root-fig2-inoculum-erratum.json
  locator: Printed page 350 Figure 2 inoculum clarification
  summary: 'The preserved root reading-note typo is corrected: Figure 2 uses 10 mL
    inoculum, distinct from 50 mL starting medium.'
  support: supports
  accessed_at: '2026-10-22T06:36:27.065140Z'
  snapshot_sha256: 596c3e2703719e3a9035742d4030c592618744903b4e41217dbd546021539974
- evidence_id: root-source
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000150/root-independent-source-audit.json
  locator: Independent root source assessment
  summary: Independent whole-page and authority reading agrees with the scoped conclusions.
  support: supports
  accessed_at: '2026-10-22T06:36:27.065216Z'
  snapshot_sha256: b1b7480d89d5586d807f812ae01b9ae9ad02a57d35f7291f0ce42f4be4da6451
- evidence_id: metrics
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000150/support-final-audit.json
  locator: Final independent reconciliation
  summary: Literal completeness 85; base 125 less 16 gives raw 109, capped 100.
  support: supports
  accessed_at: '2026-10-22T06:36:27.065248Z'
  snapshot_sha256: 6fc5f8434479e9f937e8adb96512d548605149a4ed482b5e409190c66246f9ce
- evidence_id: support-manifest
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000150/support-frozen-manifest.json
  locator: Frozen supporting dependencies
  summary: Current source and input pins verified.
  support: supports
  accessed_at: '2026-10-22T06:36:27.065273Z'
  snapshot_sha256: e9b2478513702469ba22b8cbad2f8af3c067b8c32a69ed172a5372248b78d5a8
- evidence_id: auxiliary
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000150/auxiliary-frozen-manifest.json
  locator: Frozen authority/native dependencies
  summary: All eight actual required native checks passed.
  support: supports
  accessed_at: '2026-10-22T06:36:27.065300Z'
  snapshot_sha256: 03f20a0872cfee1e1b3be5998052685c80783f41764ed75bdc41fb4306288916
- evidence_id: native-summary
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000150/final-validator-summary.json
  locator: Eight actual required checks
  summary: No native target failure; deterministic success is separate from source
    support.
  support: supports
  accessed_at: '2026-10-22T06:36:27.065331Z'
  snapshot_sha256: 7a6bca37d83825bc0e50690c2a50c4a439cbaf0d84eacb9926b94e0587440a1e
- evidence_id: corpus-context
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000150/child-corpus-context.json
  locator: Fresh batch16 corpus baseline
  summary: Nonrequired corpus exits and warnings remain explicit.
  support: supports
  accessed_at: '2026-10-22T06:36:27.065357Z'
  snapshot_sha256: eaa2b5591d66c22e71092e8714e4b3dee61fa8ba7335b0b6487e9d96915a4761
- evidence_id: adapter
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000150/adapter-check.json
  locator: Current owned-runtime availability and bounded reused discovery
  summary: Optional adapter unavailable in this runtime; no global or biological absence
    claim.
  support: supports
  accessed_at: '2026-10-22T06:36:27.065382Z'
  snapshot_sha256: d8f989c73462e82a40c33e20b8aa8866a9259716efa39cd63bc8bf7557bd3617
- evidence_id: check-validate
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000150/validate.json
  locator: Actual command/stdout/stderr
  summary: Actual native exit 0; scientific support assessed separately.
  support: supports
  accessed_at: '2026-10-22T06:36:27.065516Z'
  snapshot_sha256: 3ed8cd2a1de4d3d2472e1bbadf8734603466d535095a2fd84bb55d86f3dc2d39
- evidence_id: check-validate-strict
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000150/validate-strict.json
  locator: Actual command/stdout/stderr
  summary: Actual native exit 0; scientific support assessed separately.
  support: supports
  accessed_at: '2026-10-22T06:36:27.065570Z'
  snapshot_sha256: 2e5a4c62fc5f78c1ab86450611dd25f70f671bf5db6dabf0c3ab9246e9b53a35
- evidence_id: check-validate-terms
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000150/validate-terms.json
  locator: Actual command/stdout/stderr
  summary: Actual native exit 0; scientific support assessed separately.
  support: supports
  accessed_at: '2026-10-22T06:36:27.065618Z'
  snapshot_sha256: 7bc0f2c12d678c8e73a7fe74556b18fa5de357004dde7d602c28ce3f2d99ac03
- evidence_id: check-validate-references-explained
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000150/validate-references-explained.json
  locator: Actual command/stdout/stderr
  summary: Actual native exit 0; scientific support assessed separately.
  support: supports
  accessed_at: '2026-10-22T06:36:27.065664Z'
  snapshot_sha256: 5b8914c9498205182f0b121c7c6bc195bfa128c257d9b3a8f56b487bd207147a
- evidence_id: check-validate-gtdb
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000150/validate-gtdb.json
  locator: Actual command/stdout/stderr
  summary: Actual native exit 0; scientific support assessed separately.
  support: supports
  accessed_at: '2026-10-22T06:36:27.065709Z'
  snapshot_sha256: 541a607c36b8604495528a75c448ca054f54698ec26c95b70418574e9b205d7d
- evidence_id: check-validate-gtdb-domain
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000150/validate-gtdb-domain.json
  locator: Actual command/stdout/stderr
  summary: Actual native exit 0; scientific support assessed separately.
  support: supports
  accessed_at: '2026-10-22T06:36:27.065755Z'
  snapshot_sha256: 8c1b11b63122c6c9f225912a15a4c2496ebe050a2fb08608c832a8ebcf7e11cf
- evidence_id: check-validate-history
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000150/validate-history.json
  locator: Actual command/stdout/stderr
  summary: Actual native exit 0; scientific support assessed separately.
  support: supports
  accessed_at: '2026-10-22T06:36:27.065799Z'
  snapshot_sha256: aca4af844c83dca3fd959ad9757c18ad660a7c5e6dd76b1eb59d8884fa2bbf5f
- evidence_id: check-normalize-cache-names-check
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000150/normalize-cache-names-check.json
  locator: Actual command/stdout/stderr
  summary: Actual native exit 0; scientific support assessed separately.
  support: supports
  accessed_at: '2026-10-22T06:36:27.065843Z'
  snapshot_sha256: 6ef0ef2b7fc66f49c73e73b52edb1e5551365eeb37ecba61fbe88a74287b2c49
- evidence_id: context-audit-network
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/audit-network.json
  locator: Fresh batch16 corpus baseline
  summary: Actual exit 1 with warning-only corpus findings; zero errors.
  support: supports
  accessed_at: '2026-10-22T06:36:27.065913Z'
  snapshot_sha256: f4809c6a349f1496dbfe0243fb5ce661f469f7235f2aa00e6294ee3aa04f3123
- evidence_id: context-check-network-quality
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/check-network-quality.json
  locator: Fresh batch16 corpus baseline
  summary: Actual exit 1 with warning-only corpus findings; zero errors.
  support: supports
  accessed_at: '2026-10-22T06:36:27.065966Z'
  snapshot_sha256: 759ba13f2cda067251275491bbafc401d0be8bddf7907c7f962eb4369f61688f
assessments:
- assessment_id: identity
  area: identity
  topic: Exact source pair and stock metadata
  outcome: concern
  summary: The community identity is sound; structured strain metadata can be made
    exact.
  target_ids:
  - CommunityMech:000150
  evidence_ids:
  - identity
  - strains
  - schema
  - record
  dimensions:
  - name: stable_id
    value: CommunityMech:000150
    definition: Maintained community and exact PMID:16345708 / DOI:10.1128/aem.41.2.346-354.1981.
    evidence_ids:
    - record
    - inspection
    - abstract
  - name: source_strains
    value: D. desulfuricans Essex 6 (DSM 642) and M. barkeri MS (DSM 800)
    definition: Paper-specific type-strain wording is source-attributed; current collection
      certification was not independently requested.
    evidence_ids:
    - identity
    - strains
  - name: community_scope
    value: Defined two-member anaerobic laboratory coculture
    definition: Recipient H2/CO2 and acetate use are distinct; pure methanogen and
      other partner comparisons remain separate.
    evidence_ids:
    - identity
    - products
    - hydrogen-perturbation
  details: Retain SYNTHETIC origin, ENGINEERED state and SYNTROPHY category. Essex
    6 and MS occur in node 0, but member records lack the source stock identifiers.
    EC1 and PS comparisons are not additional members.
- assessment_id: node-0
  area: graph
  topic: Lactate Degradation to Acetate and Methane
  outcome: supported
  summary: Retain positive lactate degradation and product provision.
  target_ids:
  - CommunityMech:000150
  evidence_ids:
  - products
  - time-course
  - thermodynamics
  - snippets
  details: 'Exact selector ecological_interactions[0]; scope PAIRWISE; interaction_type
    SYNTROPHY. Participants: {"source_taxon": {"preferred_term": "Desulfovibrio desulfuricans",
    "term": {"id": "NCBITaxon:876", "label": "Desulfovibrio desulfuricans"}}, "target_taxon":
    {"preferred_term": "Methanosarcina barkeri", "term": {"id": "NCBITaxon:2208",
    "label": "Methanosarcina barkeri"}}}. Exact canonical snippet bindings: [{"selector":
    "ecological_interactions[0].evidence[0].snippet", "sha256": "1ba31b86afd428c3c4f8bdaa0e4e3f213cf7afc9d68dd29bf383d444baff0ee4",
    "reference": "PMID:16345708", "supports": "SUPPORT", "evidence_source": "IN_VITRO"}].
    PMID:16345708 locator: Tables 1–3, printed pages 347, 349–350; Figures 2–3, pages
    350–351. Exact-pair carbon and gas time courses support donor products and methanogenesis.
    Table 1 is reaction accounting, not a complete measured coculture carbon balance.'
- assessment_id: node-1
  area: graph
  topic: Acetate Conversion by Methanosarcina
  outcome: supported
  summary: Retain intrinsic recipient acetate methanogenesis.
  target_ids:
  - CommunityMech:000150
  evidence_ids:
  - products
  - time-course
  - medium-comparison
  - snippets
  details: 'Exact selector ecological_interactions[1]; scope PAIRWISE; interaction_type
    None. Participants: {"source_taxon": {"preferred_term": "Methanosarcina barkeri",
    "term": {"id": "NCBITaxon:2208", "label": "Methanosarcina barkeri"}}, "target_taxon":
    null}. Exact canonical snippet bindings: [{"selector": "ecological_interactions[1].evidence[0].snippet",
    "sha256": "c865bc5328df999187fabc50065f20ce5346bd88e1684bd70f3ba5421fc27480",
    "reference": "PMID:16345708", "supports": "SUPPORT", "evidence_source": "IN_VITRO"}].
    PMID:16345708 locator: Results Fermentation products. and time course, printed
    pages 349–351; Figures 1–3, pages 350–351. This source-only PAIRWISE process is
    not reverse cross-feeding. Coculture CO2 is presumed; pure MS CO2 measurement
    is a separate assay.'
- assessment_id: node-2
  area: graph
  topic: Hydrogen Inhibition of Acetate Degradation
  outcome: supported
  summary: Retain conditional hydrogen inhibition with PARTIAL donor attribution.
  target_ids:
  - CommunityMech:000150
  evidence_ids:
  - medium-comparison
  - hydrogen-perturbation
  - mechanism-limits
  - snippets
  details: 'Exact selector ecological_interactions[2]; scope PAIRWISE; interaction_type
    None. Participants: {"source_taxon": {"preferred_term": "Desulfovibrio desulfuricans",
    "term": {"id": "NCBITaxon:876", "label": "Desulfovibrio desulfuricans"}}, "target_taxon":
    {"preferred_term": "Methanosarcina barkeri", "term": {"id": "NCBITaxon:2208",
    "label": "Methanosarcina barkeri"}}}. Exact canonical snippet bindings: [{"selector":
    "ecological_interactions[2].evidence[0].snippet", "sha256": "eb6af80aef4e7793343faf93dc534720d13c7915682f519283bc2d338472e103",
    "reference": "PMID:16345708", "supports": "PARTIAL", "evidence_source": "IN_VITRO"}].
    PMID:16345708 locator: Results Effect of lactate and H2 on acetate degradation
    by M. barkeri., printed page 351; Figures 4–5, page 352; Discussion pages 352–353.
    Pure-MS H2 perturbation and exact-pair time courses support conditional delay.
    Hydrogen can increase growth and methane; enzyme repression is proposed, not directly
    resolved.'
- assessment_id: edge-0-0
  area: graph
  topic: Lactate Degradation to Acetate and Methane → Acetate Conversion by Methanosarcina
  outcome: supported
  summary: Retain donor acetate provision to later recipient use.
  target_ids:
  - CommunityMech:000150
  evidence_ids:
  - time-course
  - medium-comparison
  - hydrogen-perturbation
  details: 'Exact selector ecological_interactions[0].downstream[0]; source Lactate
    Degradation to Acetate and Methane; target Acetate Conversion by Methanosarcina.
    Participants and exact excerpts are bound in node assessments. Exact description:
    Donor-produced acetate supplies the later methanogenic substrate. Its utilization
    timing also depends on hydrogen and medium conditions. Description SHA256 a02384dcdd5a66a81b603520a8251f9dceefcab49d2559ab5075dd080688a227.
    PMID:16345708, Figures 2–3 on pages 350–351. Timing also depends on hydrogen and
    medium; provision does not establish a universal sequence.'
- assessment_id: edge-0-1
  area: graph
  topic: Lactate Degradation to Acetate and Methane → Hydrogen Inhibition of Acetate
    Degradation
  outcome: supported
  summary: Retain the PARTIAL donor-hydrogen attribution.
  target_ids:
  - CommunityMech:000150
  evidence_ids:
  - time-course
  - medium-comparison
  - hydrogen-perturbation
  details: 'Exact selector ecological_interactions[0].downstream[1]; source Lactate
    Degradation to Acetate and Methane; target Hydrogen Inhibition of Acetate Degradation.
    Participants and exact excerpts are bound in node assessments. Exact description:
    PARTIAL - donor hydrogen production is implicated in delayed acetate use by coculture
    time courses and separate pure-culture hydrogen perturbation, not selective removal
    of donor hydrogen in the exact pair. Description SHA256 cec93796be5ed7e9a98cba317f2dd33b5380636c550ec332d82c652ef9e88afc.
    PMID:16345708, Figures 2–3 on pages 350–351 and pure-culture Figures 4–5 on page
    352. No exact-pair selective hydrogen-removal intervention was performed. Adding
    a negative arrow is optional new structure, not a prerequisite for this review.'
- assessment_id: cultivation
  area: evidence
  topic: YE, RV and inoculum/assay separation
  outcome: concern
  summary: The record presents RV generally even though the principal pair time course
    uses YE.
  target_ids:
  - CommunityMech:000150
  evidence_ids:
  - cultivation
  - medium-definition
  - time-course
  - medium-comparison
  dimensions:
  - name: medium
    value: Routine YE pair culture; RV comparison and pure-MS assays
    definition: Figures 2 and 3 must not be collapsed into a single RV formulation.
    evidence_ids:
    - medium-definition
    - cultivation
    - time-course
    - medium-comparison
  - name: experimental_setting
    value: 'Figure 2: 50 mL YE in 125 mL bottles, inoculated with 10 mL culture'
    definition: The caption specifies medium and inoculum separately; do not infer
      an unqualified final working-volume total. Other tube assays differ.
    evidence_ids:
    - time-course
    - cultivation
  - name: environment
    value: 35 °C; basal 80:20 N2/CO2, final preparation pH 7.2
    definition: Vertical incubations are distinct from H2-added cultures on a reciprocal
      shaker. Figure 2 explicitly uses static incubation. pH is not described as continuously
      controlled.
    evidence_ids:
    - cultivation
    - medium-definition
    - medium-comparison
  details: RV contains 5% rumen fluid, minerals, B vitamins and reducing agents. YE
    is otherwise identical to RV. Rumen fluid, B vitamins and the Pfennig mineral/metal
    solution are omitted; 0.1% yeast extract, nitrogen/sulfur-free mineral solution
    3 and 10 mM NH4Cl are added, while the reducing agents are retained. The paper
    refers elsewhere for full recipes. Record no added Na2SO4 rather than chemical
    sulfate zero. Recover source conditions without importing a generic modern recipe.
- assessment_id: claim-evidence
  area: evidence
  topic: Exact partner and interpretation context
  outcome: concern
  summary: Two authentic Abstract fragments come from the M. smithii comparator sentence.
  target_ids:
  - CommunityMech:000150
  evidence_ids:
  - abstract
  - identity
  - products
  - snippets
  details: Replace taxonomy[0].evidence[0] and related_ingredients[0].evidence[0]
    with exact focal-pair context; the underlying biology is supported by the next
    Abstract sentence and body. Preserve presumed CO2 in the summary and source-attributed,
    conditional hydrogen regulation in related_ingredients[2].relevance, consistent
    with the graph.
- assessment_id: grounding
  area: grounding
  topic: Valid species ambiguity and optional stock routes
  outcome: supported
  summary: All ten ID/label pairs match and both current GTDB candidate sets reproduce.
  target_ids:
  - CommunityMech:000150
  evidence_ids:
  - ontology
  - gtdb
  - strains
  - schema
  dimensions:
  - name: taxon_grounding
    value: NCBITaxon:876 and NCBITaxon:2208; current species GTDB AMBIGUOUS sets retained
    definition: Source strain metadata and optional narrower grounded routes are separate
      from valid current species-level mappings.
    evidence_ids:
    - ontology
    - gtdb
    - strains
  details: Optional exact stock routes NCBITaxon:1121445 and NCBITaxon:1434108 map
    through source-linked IDs to GTDB D. desulfuricans (1.0/6) and M. barkeri (1.0/2).
    These reference counts are not culture abundance. No release/build string is encoded,
    and no forced replacement follows from species ambiguity.
- assessment_id: resources
  area: representation
  topic: Publication versus deposited dataset
  outcome: concern
  summary: The exact PMID is valid but is represented as a PHENOTYPE dataset.
  target_ids:
  - CommunityMech:000150
  evidence_ids:
  - resources
  - external-links
  - abstract
  details: Retain the paper as a publication/source resource. Do not invent an archive
    accession or treat the paper URL as a deposited phenotype dataset. No raw data
    or archive-absence search was performed.
- assessment_id: source-scope
  area: scope
  topic: Complete scanned article and real access limits
  outcome: supported
  summary: All nine authentic source pages were visually read.
  target_ids:
  - CommunityMech:000150
  evidence_ids:
  - assets
  - lead-read
  - locators
  - root-source
  dimensions:
  - name: evidence_tier
    value: IN_VITRO pair phenotypes and separate pure-culture perturbations; proposed
      repression mechanism
    definition: Whole original scan pixels establish source scope. OCR is a derivative
      aid and no whole OCR read is claimed.
    evidence_ids:
    - assets
    - lead-read
    - time-course
    - hydrogen-perturbation
    - mechanism-limits
  details: This includes all three tables, five figures/captions, main narrative and
    26 references. EPMC XML returned an error and the PDF route returned HTML; neither
    was used as article content. The original page images supplied the complete article.
    No supplement is declared in the inspected article/landing metadata; no wider
    absence claim.
- assessment_id: ownership
  area: ownership
  topic: Maintained owner and historical scope
  outcome: supported
  summary: Future repairs belong to the canonical YAML under separate curation authorization.
  target_ids:
  - CommunityMech:000150
  evidence_ids:
  - inspection
  - provenance
  details: Ignored-inclusive discovery pinned all eight focal contexts. Prior graph
    repair is preserved; open discussions and issues are not closed by this review.
    No canonical, cache, history, issue or Git mutation was performed.
- assessment_id: native
  area: schema
  topic: Actual native validation
  outcome: supported
  summary: All eight required native checks passed.
  target_ids:
  - CommunityMech:000150
  evidence_ids:
  - native-summary
  - auxiliary
  - corpus-context
  - adapter
  details: Reference zero-issue output does not count reviewed excerpts; twelve independent
    lexical matches do not establish claim entailment.
- assessment_id: metrics
  area: completeness
  topic: Literal native metrics
  outcome: supported
  summary: Completeness 85; raw quality 109, capped 100.
  target_ids:
  - CommunityMech:000150
  evidence_ids:
  - metrics
  metrics:
  - name: completeness
    value: 85
    unit: points
    minimum: 0
    maximum: 100
    definition: 50 required-and-roles +5 environment +10 nodes +10 medium +5 dataset
      +5 metabolites =85. Only two environmental factors and no external_resources.
      Literal presence does not establish correctness; the dataset bonus remains even
      though its typing requires repair.
  - name: validation_quality
    value: 100
    unit: points
    minimum: 0
    maximum: 100
    definition: Base 100 +20*min((3 evidence/3 nodes)/2,1)=10 +15 COMPLETE =125; subtract
      one P2*10 and three P3*2 to obtain raw 109, capped 100. Network completion does
      not establish causation.
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
- finding_id: medium-assay
  issue_key: cm-000150-medium-assay
  category: evidence
  severity: major
  native_severity: P2
  normalization_reason: Material experimental-arm and medium misrepresentation.
  rule_id: review-checklist.claim-specific-support-and-context
  status: open
  certainty: confirmed
  title: Separate YE and RV experiments
  description: The general RV assignment obscures the YE principal coculture and assay-specific
    gases, inocula and conditions. Sulfate-free shorthand exceeds no added sulfate.
  target_ids:
  - CommunityMech:000150
  field_paths:
  - environment_term
  - environmental_factors
  - growth_media[0]
  - cultivation_setup
  evidence_ids:
  - cultivation
  - medium-definition
  - time-course
  - medium-comparison
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Desulfovibrio_Methanosarcina_Lactate_Syntrophy.yaml
    role: canonical_record
  ownership_note: Future canonical curation only; immutable caches/history/review
    artifacts remain unchanged.
- finding_id: strain-metadata
  issue_key: cm-000150-strain-metadata
  category: completeness
  severity: minor
  native_severity: P3
  normalization_reason: Bounded member metadata, evidence placement or resource-type
    repair; core identity and mechanism remain supported.
  rule_id: review-checklist.claim-specific-support-and-context
  status: open
  certainty: confirmed
  title: Represent exact source strains
  description: The source establishes Essex 6/DSM 642 and MS/DSM 800, while structured
    members remain only species-level.
  target_ids:
  - CommunityMech:000150
  field_paths:
  - taxonomy[0]
  - taxonomy[1]
  evidence_ids:
  - identity
  - strains
  - gtdb
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Desulfovibrio_Methanosarcina_Lactate_Syntrophy.yaml
    role: canonical_record
  ownership_note: Future canonical curation only; immutable caches/history/review
    artifacts remain unchanged.
- finding_id: claim-evidence
  issue_key: cm-000150-claim-evidence
  category: evidence
  severity: minor
  native_severity: P3
  normalization_reason: Bounded member metadata, evidence placement or resource-type
    repair; core identity and mechanism remain supported.
  rule_id: review-checklist.claim-specific-support-and-context
  status: open
  certainty: confirmed
  title: Use exact focal-pair evidence and qualifications
  description: Two excerpts come from the M. smithii comparator sentence. The focal
    biology is supported elsewhere, while summary CO2 and hydrogen interpretation
    need the existing graph qualifications.
  target_ids:
  - CommunityMech:000150
  field_paths:
  - taxonomy[0].evidence[0]
  - related_ingredients[0].evidence[0]
  - related_ingredients[2].relevance
  - description
  evidence_ids:
  - abstract
  - products
  - time-course
  - hydrogen-perturbation
  - mechanism-limits
  - snippets
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Desulfovibrio_Methanosarcina_Lactate_Syntrophy.yaml
    role: canonical_record
  ownership_note: Future canonical curation only; immutable caches/history/review
    artifacts remain unchanged.
- finding_id: publication-dataset
  issue_key: cm-000150-publication-dataset
  category: representation
  severity: minor
  native_severity: P3
  normalization_reason: Bounded member metadata, evidence placement or resource-type
    repair; core identity and mechanism remain supported.
  rule_id: review-checklist.claim-specific-support-and-context
  status: open
  certainty: confirmed
  title: Represent the PMID as a publication resource
  description: PMID:16345708 identifies the source article, not a deposited PHENOTYPE
    dataset.
  target_ids:
  - CommunityMech:000150
  field_paths:
  - associated_datasets[0]
  - external_resources
  evidence_ids:
  - resources
  - abstract
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Desulfovibrio_Methanosarcina_Lactate_Syntrophy.yaml
    role: canonical_record
  ownership_note: Future canonical curation only; immutable caches/history/review
    artifacts remain unchanged.
actions:
- action_id: repair-medium
  description: Separate source formulations and assay stages.
  finding_ids:
  - medium-assay
  target_ids:
  - CommunityMech:000150
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Desulfovibrio_Methanosarcina_Lactate_Syntrophy.yaml
    role: canonical_record
  acceptance_checks:
  - Represent YE as the routine pair maintenance and Figure 2 medium; retain RV and
    YE/RV comparison as separate contexts. Do not replace every RV mention, because
    RV is valid in specific experiments.
  - Recover source 35 °C, basal 80:20 N2/CO2 and preparation pH 7.2. For Figure 2
    record 50 mL medium in 125 mL bottles, 25 mM lactate and 10 mL inoculum, with
    static incubation. Keep Figure 3 tube assays and pure-MS hydrogen/shaking treatments
    separate.
  - Document pair establishment with 1 mL of each partner, serial 2 mL transfer into
    8 mL YE every two weeks and at least four transfers before experiments. Do not
    confuse this with the methanogen acetate adaptation protocol.
  - Use no added Na2SO4 instead of chemically zero sulfate. Preserve source recipe
    references where composition is not fully specified; no generic catalogue recipe
    import.
- action_id: repair-strains
  description: Add source-stock metadata without losing current mapping scope.
  finding_ids:
  - strain-metadata
  target_ids:
  - CommunityMech:000150
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Desulfovibrio_Methanosarcina_Lactate_Syntrophy.yaml
    role: canonical_record
  acceptance_checks:
  - Record Essex 6/DSM 642 and MS/DSM 800 at their taxonomy entries using the Methods
    stock paragraph. The current species IDs and AMBIGUOUS sets are valid.
  - If selecting exact strain IDs, use the verified source-linked NCBITaxon:1121445
    and NCBITaxon:1434108 routes and update all participant copies consistently. Do
    not infer culture abundance or unverified collection type status from reference
    mappings.
- action_id: repair-claims
  description: Place evidence at the correct partner and assay scope.
  finding_ids:
  - claim-evidence
  target_ids:
  - CommunityMech:000150
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Desulfovibrio_Methanosarcina_Lactate_Syntrophy.yaml
    role: canonical_record
  acceptance_checks:
  - Replace the comparator excerpts with contiguous source text that explicitly supports
    the focal M. barkeri pair; do not characterize the underlying lactate phenotype
    as false.
  - Carry presumed coculture CO2 and conditional donor-H2 interpretation into summary/non-graph
    wording. Preserve pure-culture perturbation versus exact-pair inference, increased
    growth/methane and proposed enzyme repression.
  - Retain all three current nodes and two arrows with their existing limits. A proposed
    extra negative arrow remains separately scoped research, not a mandatory connectivity
    repair.
- action_id: repair-resource
  description: Retain the article under appropriate bibliographic representation.
  finding_ids:
  - publication-dataset
  target_ids:
  - CommunityMech:000150
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Desulfovibrio_Methanosarcina_Lactate_Syntrophy.yaml
    role: canonical_record
  acceptance_checks:
  - Remove or reclassify the publication-only dataset entry using a supported publication/external-resource
    representation. Keep exact PMID/DOI/PMC identity; do not invent a deposit or claim
    none exists globally.
- action_id: validate-curation
  description: Validate any separately authorized canonical changes.
  finding_ids:
  - medium-assay
  - strain-metadata
  - claim-evidence
  - publication-dataset
  target_ids:
  - CommunityMech:000150
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Desulfovibrio_Methanosarcina_Lactate_Syntrophy.yaml
    role: canonical_record
  acceptance_checks:
  - Run focused schema, strict, term, reference, GTDB and history checks after actual
    edits, plus required generated-document checks. Preserve original caches/history
    and graph review decisions. Root alone saves this review and runs post-save gates.
limitations:
- The article was read as all nine authentic scanned pages. EPMC XML and PDF requests
  failed to return full-text payloads; original page images supplied the complete
  main. OCR is a derivative aid, not an independent whole-text read.
- No supplement was declared in the inspected article or public landing metadata;
  no global absence search or raw-data reanalysis was performed. Full recipe details
  delegated by the paper to older references remain bounded.
- Coculture CO2 is presumed; pure-MS CO2 measurements do not resolve the pair carbon
  balance. Donor-H2 attribution remains partial, and enzyme repression is an interpretation
  with alternatives.
- Exact stock candidates do not invalidate current species ambiguity. No catalogue
  maintenance conditions or unverified current type-status claims were imported.
- Open historical research discussions are preserved. Completion of this scientific
  review does not close issues, promote native record status or authorize canonical
  curation.
notes:
- Eight evidence-linked dimensions are present. Three exact node-excerpt hashes and
  two exact arrow descriptions bind the current graph.
- 'The sole primary-source quote contains two words. All 30 official inputs remain
  unchanged; required native failures: zero.'
- Root owns persistence and post-save gates; this candidate itself makes no canonical/cache/history/Git
  change.
tags:
- record-review
- syntrophy
- methanogenesis
- batch-16
```
