# East River floodplain core microbiome record review

- Review: 20261022T085727Z-east-river-core-record-review-v3
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-22T08:38:13.962506Z
- Finished UTC: 2026-10-22T08:57:27.919510Z
- Reviewer: codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Two major findings concern non-graph sampling/readout scope and core membership, taxonomic rank and role support. One minor finding concerns GTDB provenance. Retain the three qualified community nodes and zero arrows. Eight required checks passed; completeness 75 and validation quality 98.

## Scope And Provenance

Whole released record and main source, all main figures, relevant supplementary figures and bounded table cells, authorities and public resource metadata.

Selection: Sole released CommunityMech:000137 in owned batch16.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base cb7a782c8ba80299dca8761ad0a2c90bccd8a117.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000137 | kb/communities/East_River_Floodplain_Core_Microbiome.yaml | maintained | East River Floodplain Core Microbiome |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000137 | Actual native exit 0. |
| validate-strict | passed | True | CommunityMech:000137 | Actual native exit 0. |
| validate-terms | passed | True | CommunityMech:000137 | Actual native exit 0. |
| validate-references-explained | passed | True | CommunityMech:000137 | Actual native exit 0. |
| validate-gtdb | passed | True | CommunityMech:000137 | Actual native exit 0. |
| validate-gtdb-domain | passed | True | CommunityMech:000137 | Actual native exit 0. |
| validate-history | passed | True | CommunityMech:000137 | Actual native exit 0. |
| normalize-cache-names-check | passed | True | CommunityMech:000137 | Actual native exit 0. |
| audit-network corpus context | failed | False | CommunityMech:000137 | Actual corpus exit 1. |
| check-network-quality corpus context | failed | False | CommunityMech:000137 | Actual corpus exit 1. |
| Source-specific structured adapter | unavailable | False | CommunityMech:000137 | Owned-runtime runner unavailable; gene relevance documented. |

## Scientific And Domain Assessments

### Community and sampling units

identity: supported. Targets: CommunityMech:000137.

The record identifies the correct natural field study; non-graph scope needs refinement.

The 2015 G/L/Z survey produced 248 representative genomes at 98% ANI from 94 quality samples; 42 met the operational core rule. The 2016 L RNA study used a distinct 95% ANI reference set. These are field genome groupings, not cultured strains or a defined four-member consortium.

### Non-graph sampling, readout and ecological state

scope: concern. Targets: CommunityMech:000137.

Separate core gene enrichment from L-only transcription and equilibrium.

Description and environmental_factors[1] extend RNA findings to all three meanders and pool rare high-transcription functions with enriched core capacities. STABLE denotes ecological equilibrium; spatial prevalence and inferred persistence of gene inventories do not demonstrate that state. The source abstract itself uses broader wording, already qualified in node 2.

### Core membership, rank and functional roles

grounding: concern. Targets: CommunityMech:000137.

Resolve the roster boundary and use source-linked capability evidence.

Acidobacteriota belong to the broader reconstruction, not the 42-genome core. Historical Nitrospirae is a phylum; NCBITaxon:1234 is genus Nitrospira, while verified NCBITaxon:40117 Nitrospirota matches the source rank. Nitrification alone does not establish PRIMARY_PRODUCER. S6 X201:X213 are zero, but POSSIBLE S4 fragments prevent a universal inability claim. Retain qualified Beta producer potential (core genomes X39/X83), source-local Beta CAZy evidence, and Gemma degradative potential (S5 row 11 matches S8 row 66). Add those role-local citations rather than infer every genome performs the role.

### Core Floodplain Biogeochemical Potential Reservoir

graph: supported. Targets: CommunityMech:000137.

Retain the qualified COMMUNITY_LEVEL claim.

Exact selector ecological_interactions[0]. Participants: {"participating_taxa": [{"preferred_term": "Betaproteobacteria-dominated core floodplain microbiome", "term": {"id": "NCBITaxon:28216", "label": "Betaproteobacteria"}}, {"preferred_term": "Gemmatimonadota floodplain representatives", "term": {"id": "NCBITaxon:142182", "label": "Gemmatimonadota"}}]}. Exact canonical snippet bindings: [{"selector": "ecological_interactions[0].evidence[0].snippet", "sha256": "551b28509b9d79500f6eff134ec948051cc5c654c7ab1fb96c64cafe7605a351", "reference": "PMID:34022966", "supports": "SUPPORT", "evidence_source": "COMPUTATIONAL"}, {"selector": "ecological_interactions[0].evidence[1].snippet", "sha256": "048ee32715246f066e774317865f1bb3428a6049f12c6dba05f7a4828e6c5a17", "reference": "PMID:34022966", "supports": "SUPPORT", "evidence_source": "COMPUTATIONAL"}]. Source: PMID:34022966; DOI:10.1186/s40168-020-00957-z. Locator: Uncovering a core floodplain microbiome (Sec6), direct paragraphs 1–2. Operational core capacity is supported. The Beta/Gemma list is partial, and the explicit Acidobacteria exclusion is correct. Gene inventories do not establish activation, flux or exchange.

### Core Floodplain Aerobic and Sulfur Oxidation Capacity

graph: supported. Targets: CommunityMech:000137.

Retain the qualified COMMUNITY_LEVEL claim.

Exact selector ecological_interactions[1]. Participants: {"participating_taxa": [{"preferred_term": "Betaproteobacteria-dominated core floodplain microbiome", "term": {"id": "NCBITaxon:28216", "label": "Betaproteobacteria"}}, {"preferred_term": "Gemmatimonadota floodplain representatives", "term": {"id": "NCBITaxon:142182", "label": "Gemmatimonadota"}}]}. Exact canonical snippet bindings: [{"selector": "ecological_interactions[1].evidence[0].snippet", "sha256": "708b7e3efedb0d6034a9fcb526a1cbdaa438a5d09d4219f7a5d1268a7c9a8d74", "reference": "PMID:34022966", "supports": "SUPPORT", "evidence_source": "COMPUTATIONAL"}]. Source: PMID:34022966; DOI:10.1186/s40168-020-00957-z. Locator: Geochemical functions, including those enriched in the core floodplain microbiome (Sec7), direct paragraphs 6. Retain comparative aerobic/CO-or-other-small-molecule and thiosulfate gene enrichment. Neither cooperation nor niche partitioning follows from gene-content overlap.

### Low-Organic-Carbon-Associated Gene Transcription in Floodplain L

graph: supported. Targets: CommunityMech:000137.

Retain the qualified COMMUNITY_LEVEL claim.

Exact selector ecological_interactions[2]. Participants: {"participating_taxa": [{"preferred_term": "Betaproteobacteria-dominated core floodplain microbiome", "term": {"id": "NCBITaxon:28216", "label": "Betaproteobacteria"}}]}. Exact canonical snippet bindings: [{"selector": "ecological_interactions[2].evidence[0].snippet", "sha256": "7c921e11d333ed514f8b30bd2fccb7480969263d8e9339e5823ce4a58c3071d8", "reference": "PMID:34022966", "supports": "PARTIAL", "evidence_source": "COMPUTATIONAL"}, {"selector": "ecological_interactions[2].evidence[1].snippet", "sha256": "44afd00d9cf329b355e10a0dd81f7a3f319869c2dbf499bf5428884e3ca4a5b2", "reference": "PMID:34022966", "supports": "SUPPORT", "evidence_source": "COMPUTATIONAL"}, {"selector": "ecological_interactions[2].evidence[2].snippet", "sha256": "3d0a9b65ac2be4ab6f4edfd90584204e83f0b5cdf9b35918a5d46eecf3d89c08", "reference": "PMID:34022966", "supports": "SUPPORT", "evidence_source": "COMPUTATIONAL"}, {"selector": "ecological_interactions[2].evidence[3].snippet", "sha256": "755657d10edb31ed301f2422229469dbc723a3d99488cfd2ca4a77228c8107d6", "reference": "PMID:34022966", "supports": "SUPPORT", "evidence_source": "COMPUTATIONAL"}]. Source: PMID:34022966; DOI:10.1186/s40168-020-00957-z. Locator: Potentially active genes encoding key biogeochemical transformations in the riparian zone (Sec9), direct paragraphs 1–8. Retain the September 2016 L-only RNA association, PARTIAL abstract qualification and limited Beta CBB participant. Overall Beta transcription favored higher organic carbon; no manipulation, all-three-site RNA replication or whole-core activation is established.

### Three community claims and no arrows

graph: supported. Targets: CommunityMech:000137.

No causal arrows are warranted by the present evidence.

All three nodes omit interaction_type and have COMMUNITY_LEVEL scope. The two native DISCONNECTED warnings concern Nitrospira and Acidobacteriota; they do not justify fabricated links or invalidate the correctly bounded nodes. Preserve zero downstream edges.

### Field setting and cultivation applicability

scope: supported. Targets: CommunityMech:000137.

No culture recipe or reactor setup is required for this natural survey.

Soils were sampled at East River meander-bound floodplains in Colorado. September 2015 baseflow sampling and 2016 L resampling are distinct. Tubes, frozen storage and molecular processing are analytical handling, not growth conditions.

### Ontology correspondence and GTDB provenance

grounding: concern. Targets: CommunityMech:000137.

Labels match; source taxonomic rank and mapping provenance need separate repair.

The curated Beta order vote reproduces 41903/41937 classified genomes: Burkholderiales plus 31 Enterobacterales and three Pseudomonadales. Preserve that override and the 203/203 Acidobacteriota and 36/36 Gemmatimonadota mappings. Reference-genome counts are not field abundance. Filesystem mtime does not establish a GTDB release or build; the source marker-profile R95 context also does not establish the local crosswalk version.

### Literal excerpts and scientific interpretation

evidence: supported. Targets: CommunityMech:000137.

All 16 excerpts match; their placement still requires the specified scope repairs.

Seven placements also match MED Abstract; all 16 match fresh JATS and cache under case-preserving NFKC/whitespace normalization. Field sampling, computed genome capacities and mapped RNA abundance are separate evidence layers. Metabolites and GO processes are contextual potential, not measured flux. CARBON_SEQUESTRATION and Beta DOMINANT remain qualified context.

### Sequence and environmental resources

evidence: supported. Targets: CommunityMech:000137.

Both encoded resources resolve; no resource finding.

PRJNA630765 is a 144-project umbrella; ESS-DIVE supplies genome sets and environmental metadata. S1 has 143 exact project-ID matches; PRJNA405311 versus PRJNA405415 identifies the same sample/JGI/GOLD context. Preserve the separate S1 Z/L label conflict. No sequence download or expression reanalysis was performed.

### Source coverage and limits

scope: supported. Targets: CommunityMech:000137.

Every encoded claim was assessed against the whole main and relevant supplements.

Lead read all 112,926 main-text characters including 68 references, all six main figure pixels, all 11 supplementary figure pages and the separate S3 tree overview. Eight workbook inventories and selected membership/function/CAZy cells were inspected; S7 was read completely. Other declared tables/trees and the video were not exhaustively read or reanalyzed. Genuine publisher assets supersede failed transport routes as evidence; failed files remain preserved.

### Prior context and maintained owner

ownership: supported. Targets: CommunityMech:000137.

Retain the prior graph repair and address the current metadata findings.

Exact batch35 records[1], whole sole history/adversarial and relevant cohort context were read. Issue 1418 is closed; 1421 remains open. Issues 401/451 are closed and do not override source rank or the independently reproduced Beta vote. Cache-header authors disagree with the genuine article; canonical PMID/DOI remain valid. No record, cache, history or issue was edited.

### Actual checks and limitations

schema: supported. Targets: CommunityMech:000137.

Eight required checks passed; structural warnings remain explicit.

Native success does not certify scientific entailment. Two disconnected warnings remove the network score bonus. Optional structured-adapter unavailability and transport/reader/helper failures are separate from native failures.

### Literal profile scores

completeness: supported. Targets: CommunityMech:000137.

Completeness 75; validation quality 98.

Scores describe record presence and rubric deductions, not scientific completeness.

## Findings

### non-graph-scope: Separate field cohorts, measurements and ecological state

major / open / confirmed; issue key: cm-000137-non-graph-scope.

Non-graph prose combines three-site core gene enrichment with L-only RNA associations; STABLE asserts equilibrium beyond spatial prevalence.

### roster-rank-roles: Align core membership, source rank and role evidence

major / open / confirmed; issue key: cm-000137-roster-rank-roles.

The named core roster includes non-core Acidobacteriota and uses a Nitrospira genus ID for the source phylum. Current role excerpts support membership or nitrification rather than all assigned capabilities.

### gtdb-provenance: Correct mapping release and build provenance

minor / open / confirmed; issue key: cm-000137-gtdb-provenance.

Latest/build-date wording is unsupported by the local mapping file date, although the curated numerical mappings reproduce.

## Recommended Actions And Acceptance Checks

### repair-field-scope

Align non-graph assertions with their sampling and measurement scope.

- Separate the 2015 G/L/Z 248-genome reconstruction and 42-genome core from the 2016 L-only RNA snapshot and distinct reference set.
- Restrict core enrichment to the demonstrated comparative capacities; describe rare high-transcription functions as RNA associations, not whole-core activation or flux. Apply this to description and environmental_factors[1], including evidence explanation/support.
- Omit STABLE unless ecological-equilibrium evidence is supplied; do not infer another state from its removal. Retain the existing three qualified nodes and zero arrows.

### repair-roster-and-roles

Separate core membership from contextual taxa and ground source-specific capabilities.

- Move or explicitly segregate non-core Acidobacteriota from the named operational core while preserving its broader-dataset occurrence and potential. Do not expand the partial roster to invented isolates.
- Replace genus NCBITaxon:1234 with verified source-rank NCBITaxon:40117 Nitrospirota (historical Nitrospirae) where representing that phylum; reassess GTDB at that rank and propagate any identity change consistently.
- Attach exact MAG-level role evidence: retain qualified Beta carbon-fixation and CAZy potential and core Gemma CAZy potential. Omit or justify Nitrospirae PRIMARY_PRODUCER with carbon-fixation evidence; nitrification alone is insufficient. Preserve incomplete/POSSIBLE pathways and avoid universal negative physiology.
- Preserve ordinal Beta dominance and the qualified graph participant scopes. Do not add causal arrows merely to remove disconnected warnings.

### repair-gtdb-provenance

State verified mapping provenance without changing valid numerical cores.

- Replace latest/build-date claims with verified snapshot hash and retrieval context; leave release/build unknown unless separately documented.
- Retain the curated Beta Burkholderiales 41903/41937 vote, fraction 0.999, with three distinct target orders in total; preserve Acidobacteriota 203/203 and Gemmatimonadota 36/36. Do not substitute the default Beta class vote or interpret mapping counts as abundance.
- After separately authorized curation, run focused native schema, ontology, reference, GTDB/domain and history gates and recheck all graph participants.
- After separately authorized record curation, regenerate HTML with just gen-html and run just check-docs-current, as required by CLAUDE.md.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | kb/communities/East_River_Floodplain_Core_Microbiome.yaml; Whole canonical record | supports | Natural floodplain community, four taxon groupings and three COMMUNITY_LEVEL nodes; no arrows. |
| core | PMID:34022966; DOI:10.1186/s40168-020-00957-z; Uncovering a core floodplain microbiome (Sec6), direct paragraphs 1–2; Figure 3b | supports | The 2015 operational core contains 42 genomes; Acidobacteria are outside it. |
| enrichment | PMID:34022966; DOI:10.1186/s40168-020-00957-z; Geochemical functions, including those enriched in the core floodplain microbiome (Sec7), direct paragraph 6; Figure 4 | supports | Core enrichment concerns gene inventories for aerobic and sulfur oxidation. |
| RNA | PMID:34022966; DOI:10.1186/s40168-020-00957-z; Potentially active genes encoding key biogeochemical transformations in the riparian zone (Sec9), direct paragraphs 1–8; Figures 5–6 | supports | Later transcription is a floodplain L snapshot; rare high-expression functions are distinct from core enrichment. |
| field | PMID:34022966; DOI:10.1186/s40168-020-00957-z; Study site and sample collection (Sec13), fifth direct paragraph | supports | The 2016 RNA survey resampled floodplain L. |
| core-method | PMID:34022966; DOI:10.1186/s40168-020-00957-z; Identification of a core floodplain microbiome (Sec23), sole direct paragraph | supports | Core membership requires detection in at least 89 of 94 samples and no significant site association. |
| RNA-method | PMID:34022966; DOI:10.1186/s40168-020-00957-z; Metatranscriptomic analyses (Sec27), sole direct paragraph | supports | RNA reads were mapped to the distinct 215-genome, 95%-ANI reference assembled from both years. |
| membership-table | PMID:34022966; DOI:10.1186/s40168-020-00957-z; Supplementary Table S5: header, all 42 core rows selected by C&gt;=89 and H=7, and focal Acidobacteria/Gemmatimonadetes/Nitrospirae rows | supports | The core includes 30 Beta, five Nitrospirae and one Gemmatimonadetes representative, but no Acidobacteria. |
| function-table | PMID:34022966; DOI:10.1186/s40168-020-00957-z; Supplementary Table S6: header X1; X39/X83 and X201:X213 | supports | Two exact core Beta genomes have carbon-fixation positives; all 13 Nitrospirae rows have zero in this complete-function summary. |
| pathway-table | PMID:34022966; DOI:10.1186/s40168-020-00957-z; Supplementary Table S4: carbon-fixation headers and selected 13 Nitrospirae rows, including ED30/ED41/ED136 | supports | Some pathway fragments are classified POSSIBLE; the S6 zeros do not establish universal physiological inability. |
| cazy-table | PMID:34022966; DOI:10.1186/s40168-020-00957-z; Supplementary Table S8: row 66, exact S5 row 11 genome; AJ66/CE11=8, AP66/CE14=3, ET66/GH16=1 | supports | The core Gemmatimonadetes genome has source-linked degradative potential, not measured substrate flux. |
| SI-figures | PMID:34022966; DOI:10.1186/s40168-020-00957-z; Supplementary Figures S1–S9: all 11 physical pages and separate S3 tree overview | supports | Legends and plots were read; the separate large S3 tree was inspected as an overview, not tip-by-tip or reanalyzed. |
| ontology | /private/tmp/cm-review-session/batch-16/000137/ontology-authority.json; 12 distinct pairs, 21 placements | supports | Encoded labels match local authority; source rank and applicability require separate assessment. |
| semantics | /private/tmp/cm-review-session/batch-16/000137/ontology-semantic-notes.json; Final schema, taxon and selected-supplement assessment | supports | Current role/state definitions and verified Nitrospirota phylum candidate; qualified Beta/Gemma roles retained. |
| gtdb | /private/tmp/cm-review-session/batch-16/000137/child-gtdb-crosswalk.json; Encoded mapping routes | supports | Acidobacteriota 203/203 and Gemmatimonadota 36/36 reproduce; mapping provenance requires repair. |
| beta-mapping | /private/tmp/cm-review-session/batch-16/000137/child-curated-beta-mapping-classified.json; Curated order route, classified genomes only | supports | Burkholderiales 41903/41937; 31 Enterobacterales and three Pseudomonadales. One blank order is excluded. |
| adapter | /private/tmp/cm-review-session/batch-16/000137/child-structured-adapter-applicability.json; amoCAB/nxrAB, carbon fixation, CAZy and oxidation genes | supports | Exact MAG/gene scope assessed; optional runner unavailable in the owned runtime, provider coverage not queried. |
| snippets | /private/tmp/cm-review-session/batch-16/000137/snippet-audit.json; All 16 canonical placements | supports | All strictly match fresh JATS and cache; seven also match fresh MED Abstract. |
| resources | /private/tmp/cm-review-session/batch-16/000137/dataset-verification.json; PRJNA630765 and ESS-DIVE DOI:10.15485/1631979 | supports | Both public resources resolve at the source-declared genome/environmental scope. |
| resource-bridge | /private/tmp/cm-review-session/batch-16/000137/dataset-s1-bridge.json; All 144 S1 project IDs and 14 RNA sample metadata rows | supports | 143 IDs match the umbrella exactly; the differing pair identifies the same source sample context. All RNA samples are 2016 L. |
| provenance | /private/tmp/cm-review-session/batch-16/000137/provenance-audit.json; Exact batch35 records[1], history, cohort and four current issues | supports | Graph repair is retained; 1421 remains open. Cache header authors differ from genuine source metadata. |
| read-scope | /private/tmp/cm-review-session/batch-16/000137/lead-primary-read-scope.json; Whole fresh main and bounded supplements | supports | Whole main with 68 references, six main figures, all SI figure pages and selected table cells read. |
| assets | /private/tmp/cm-review-session/batch-16/000137/lead-source-assets.json; Actual source and transport inventory | supports | Failed partial ZIP, 404 HTML and DNS routes are distinguished from genuine source payloads. |
| locators | /private/tmp/cm-review-session/batch-16/000137/source-locator-verification.json; Direct headings, paragraphs and field quote | supports | Exact source locators verified. |
| source-audit | /private/tmp/cm-review-session/batch-16/000137/source-audit.json; Final scientific judgment | supports | Two major findings and one minor finding; all three qualified nodes retained. |
| root-source | /private/tmp/cm-review-session/batch-16/000137/root-independent-source-audit.json; Independent source acceptance and read limits | supports | Completed scientific review; 2 P2 + 1 P3, completeness 75 and quality 98. |
| support | /private/tmp/cm-review-session/batch-16/000137/support-final-audit.json; Final supporting reconciliation | supports | Thirty unchanged inputs; 16 strict snippets; native network has two disconnected warnings. |
| support-manifest | /private/tmp/cm-review-session/batch-16/000137/support-frozen-manifest.json; Supporting source pins | supports | Frozen provenance, resources, source and authority outputs verified. |
| auxiliary | /private/tmp/cm-review-session/batch-16/000137/auxiliary-frozen-manifest.json; Final auxiliary checks and source scope | supports | Eight required native checks passed; ancillary helper failure is separate. |
| selected-functions | /private/tmp/cm-review-session/batch-16/000137/selected-function-presence-verification.json; All 50 selected S6 positive maps compared with raw cells | supports | All maps match; 46 are nonempty. Empty row 14 is genuine, not an extraction error. |
| check-validate | /private/tmp/cm-review-session/batch-16/000137/validate.json; Actual command, stdout and stderr | supports | Required native exit 0. |
| check-validate-strict | /private/tmp/cm-review-session/batch-16/000137/validate-strict.json; Actual command, stdout and stderr | supports | Required native exit 0. |
| check-validate-terms | /private/tmp/cm-review-session/batch-16/000137/validate-terms.json; Actual command, stdout and stderr | supports | Required native exit 0. |
| check-validate-references-explained | /private/tmp/cm-review-session/batch-16/000137/validate-references-explained.json; Actual command, stdout and stderr | supports | Required native exit 0. |
| check-validate-gtdb | /private/tmp/cm-review-session/batch-16/000137/validate-gtdb.json; Actual command, stdout and stderr | supports | Required native exit 0. |
| check-validate-gtdb-domain | /private/tmp/cm-review-session/batch-16/000137/validate-gtdb-domain.json; Actual command, stdout and stderr | supports | Required native exit 0. |
| check-validate-history | /private/tmp/cm-review-session/batch-16/000137/validate-history.json; Actual command, stdout and stderr | supports | Required native exit 0. |
| check-normalize-cache-names-check | /private/tmp/cm-review-session/batch-16/000137/normalize-cache-names-check.json; Actual command, stdout and stderr | supports | Required native exit 0. |
| context-audit-network | /private/tmp/cm-review-session/batch-16/audit-network.json; Fresh batch16 corpus baseline | supports | Nonrequired corpus result; not the target scientific verdict. |
| context-check-network-quality | /private/tmp/cm-review-session/batch-16/check-network-quality.json; Fresh batch16 corpus baseline | supports | Nonrequired corpus result; not the target scientific verdict. |

## Limits And Additional Notes

- Genomic potential and RNA abundance do not establish environmental flux or partner exchange. Spatial core prevalence does not establish equilibrium.
- Source abstract all-three RNA wording conflicts with L-only Methods. Figure 3 caption reports 242 non-core genomes despite 248 total and 42 core; no numerical repair is inferred here.
- The 2015 98% ANI core and the combined 2015/2016 215-genome, 95% ANI reference set are distinct. Supplement joins use exact genome identifiers only, not reannotation or universal physiology.
- Eight workbook inventories and bounded cells were assessed, not all 23 declared supplementary objects. The separate large S3 tree received overview inspection only; no raw sequence, tree or transcript reanalysis.
- The S1 project-ID and Z/L metadata discrepancies are retained at their exact source scope. Cache front-author metadata differs from the genuine source, without invalidating canonical publication identity.
- A partial bulk ZIP, 404 image responses and DNS failures are preserved as failed transport, not scientific evidence. Optional structured adapter unavailable in the owned runtime.
- Exact source/target arrays and original command strings are verified before native candidate validation.
- Three nodes, seven canonical snippet hashes, zero arrows and eight evidence-linked dimensions are bound. The sole direct primary quotation has two words.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T085727Z-east-river-core-record-review-v3
kind: record
repository: CultureBotAI/CommunityMech
title: East River floodplain core microbiome record review
started_at: '2026-10-22T08:38:13.962506Z'
finished_at: '2026-10-22T08:57:27.919510Z'
reviewer:
  identity: codex
  kind: agent
  independence: unknown
  independence_basis: Separate lead, root, auxiliary and supporting reviews; no person-level
    independence claim.
skill: review-yaml-record
completion: completed
verdict: needs_curation
scientific_review: true
summary: Two major findings concern non-graph sampling/readout scope and core membership,
  taxonomic rank and role support. One minor finding concerns GTDB provenance. Retain
  the three qualified community nodes and zero arrows. Eight required checks passed;
  completeness 75 and validation quality 98.
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
  - path: history/records/East_River_Floodplain_Core_Microbiome/2026-10-06T080104Z-codex-11f2db.yaml
    sha256: 16061623d3fca5fcb4cb58514527557b4575b7018918799207b3f611b9a62757
    role: context
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: kb/communities/East_River_Floodplain_Core_Microbiome.yaml
    sha256: 152ced119bc2c3699bd6d14465561ce7fa7e5010c0defbeb40f027303b9b83e7
    role: target
  - path: references_cache/PMID_34022966.md
    sha256: 7c3af4c3f819ab55c95b03d2032f6eec054d0d30513114d779d1238f0e023040
    role: context
  - path: reports/causal_graph_review/adversarial-review-20261006-batch35.yaml
    sha256: 2e8c17652af5c990e8600b5a935001b812414cde2f26fae7629c1e7601de7a49
    role: context
  - path: reports/causal_graph_review/decisions/20261006-three-records-batch35.yaml
    sha256: efba701bb04cf8492e807965e000cefb04855d64aadd2bf2d8d41eab6c48cd91
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
- target_id: CommunityMech:000137
  path: kb/communities/East_River_Floodplain_Core_Microbiome.yaml
  label: East River Floodplain Core Microbiome
  kind: maintained
  record_class: MicrobialCommunity
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/East_River_Floodplain_Core_Microbiome.yaml
    role: canonical_record
scope:
  description: Whole released record and main source, all main figures, relevant supplementary
    figures and bounded table cells, authorities and public resource metadata.
  selection: Sole released CommunityMech:000137 in owned batch16.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000137
checks:
- check_id: validate
  name: validate
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000137
  command: just --no-dotenv validate kb/communities/East_River_Floodplain_Core_Microbiome.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate
  scope_note: Focused record/history check; cache-name preflight is corpus-wide.
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000137
  command: just --no-dotenv validate-strict kb/communities/East_River_Floodplain_Core_Microbiome.yaml
    --out /private/tmp/cm-review-session/batch-16/000137/strict-report.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-strict
  scope_note: Focused record/history check; cache-name preflight is corpus-wide.
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000137
  command: just --no-dotenv validate-terms kb/communities/East_River_Floodplain_Core_Microbiome.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-terms
  scope_note: Focused record/history check; cache-name preflight is corpus-wide.
- check_id: validate-references-explained
  name: validate-references-explained
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000137
  command: just --no-dotenv validate-references-explained kb/communities/East_River_Floodplain_Core_Microbiome.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-references-explained
  scope_note: Focused record/history check; cache-name preflight is corpus-wide.
- check_id: validate-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000137
  command: just --no-dotenv validate-gtdb kb/communities/East_River_Floodplain_Core_Microbiome.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb
  scope_note: Focused record/history check; cache-name preflight is corpus-wide.
- check_id: validate-gtdb-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000137
  command: just --no-dotenv validate-gtdb-domain kb/communities/East_River_Floodplain_Core_Microbiome.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb-domain
  scope_note: Focused record/history check; cache-name preflight is corpus-wide.
- check_id: validate-history
  name: validate-history
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000137
  command: just --no-dotenv validate-history history/records/East_River_Floodplain_Core_Microbiome
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-history
  scope_note: Focused record/history check; cache-name preflight is corpus-wide.
- check_id: normalize-cache-names-check
  name: normalize-cache-names-check
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000137
  command: uv run python scripts/normalize_cache_names.py --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-normalize-cache-names-check
  scope_note: Focused record/history check; cache-name preflight is corpus-wide.
- check_id: context-audit-network
  name: audit-network corpus context
  status: failed
  required: false
  summary: Actual corpus exit 1.
  target_ids:
  - CommunityMech:000137
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-16/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv audit-network
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - context-audit-network
- check_id: context-check-network-quality
  name: check-network-quality corpus context
  status: failed
  required: false
  summary: Actual corpus exit 1.
  target_ids:
  - CommunityMech:000137
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-16/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv check-network-quality
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - context-check-network-quality
- check_id: structured-adapter
  name: Source-specific structured adapter
  status: unavailable
  required: false
  summary: Owned-runtime runner unavailable; gene relevance documented.
  target_ids:
  - CommunityMech:000137
  evidence_ids:
  - adapter
  scope_note: No provider query or other-checkout execution; exact organism coverage
    remains unknown.
evidence:
- evidence_id: record
  kind: record_content
  reference: kb/communities/East_River_Floodplain_Core_Microbiome.yaml
  locator: Whole canonical record
  summary: Natural floodplain community, four taxon groupings and three COMMUNITY_LEVEL
    nodes; no arrows.
  support: supports
  accessed_at: '2026-10-22T08:55:52.196721Z'
- evidence_id: core
  kind: primary_source
  reference: PMID:34022966; DOI:10.1186/s40168-020-00957-z
  locator: Uncovering a core floodplain microbiome (Sec6), direct paragraphs 1–2;
    Figure 3b
  summary: The 2015 operational core contains 42 genomes; Acidobacteria are outside
    it.
  support: supports
  accessed_at: '2026-10-22T08:55:52.196824Z'
  snapshot_sha256: b75ba52c1fe45947ec64c8fa0807775cbbca4c14ad1a14eced07f7d5190c2cdd
- evidence_id: enrichment
  kind: primary_source
  reference: PMID:34022966; DOI:10.1186/s40168-020-00957-z
  locator: Geochemical functions, including those enriched in the core floodplain
    microbiome (Sec7), direct paragraph 6; Figure 4
  summary: Core enrichment concerns gene inventories for aerobic and sulfur oxidation.
  support: supports
  accessed_at: '2026-10-22T08:55:52.197406Z'
  snapshot_sha256: b75ba52c1fe45947ec64c8fa0807775cbbca4c14ad1a14eced07f7d5190c2cdd
- evidence_id: RNA
  kind: primary_source
  reference: PMID:34022966; DOI:10.1186/s40168-020-00957-z
  locator: Potentially active genes encoding key biogeochemical transformations in
    the riparian zone (Sec9), direct paragraphs 1–8; Figures 5–6
  summary: Later transcription is a floodplain L snapshot; rare high-expression functions
    are distinct from core enrichment.
  support: supports
  accessed_at: '2026-10-22T08:55:52.197544Z'
  snapshot_sha256: b75ba52c1fe45947ec64c8fa0807775cbbca4c14ad1a14eced07f7d5190c2cdd
- evidence_id: field
  kind: primary_source
  reference: PMID:34022966; DOI:10.1186/s40168-020-00957-z
  locator: Study site and sample collection (Sec13), fifth direct paragraph
  summary: The 2016 RNA survey resampled floodplain L.
  support: supports
  accessed_at: '2026-10-22T08:55:52.197652Z'
  snapshot_sha256: b75ba52c1fe45947ec64c8fa0807775cbbca4c14ad1a14eced07f7d5190c2cdd
  quote: floodplain L
- evidence_id: core-method
  kind: primary_source
  reference: PMID:34022966; DOI:10.1186/s40168-020-00957-z
  locator: Identification of a core floodplain microbiome (Sec23), sole direct paragraph
  summary: Core membership requires detection in at least 89 of 94 samples and no
    significant site association.
  support: supports
  accessed_at: '2026-10-22T08:55:52.197752Z'
  snapshot_sha256: b75ba52c1fe45947ec64c8fa0807775cbbca4c14ad1a14eced07f7d5190c2cdd
- evidence_id: RNA-method
  kind: primary_source
  reference: PMID:34022966; DOI:10.1186/s40168-020-00957-z
  locator: Metatranscriptomic analyses (Sec27), sole direct paragraph
  summary: RNA reads were mapped to the distinct 215-genome, 95%-ANI reference assembled
    from both years.
  support: supports
  accessed_at: '2026-10-22T08:55:52.197851Z'
  snapshot_sha256: b75ba52c1fe45947ec64c8fa0807775cbbca4c14ad1a14eced07f7d5190c2cdd
- evidence_id: membership-table
  kind: primary_source
  reference: PMID:34022966; DOI:10.1186/s40168-020-00957-z
  locator: 'Supplementary Table S5: header, all 42 core rows selected by C>=89 and
    H=7, and focal Acidobacteria/Gemmatimonadetes/Nitrospirae rows'
  summary: The core includes 30 Beta, five Nitrospirae and one Gemmatimonadetes representative,
    but no Acidobacteria.
  support: supports
  accessed_at: '2026-10-22T08:55:52.197949Z'
  snapshot_sha256: bac68fa8c85e3d9c9e094f6b131107a2300a5b51c5a0a38d4c7a8481ffb3b96c
- evidence_id: function-table
  kind: primary_source
  reference: PMID:34022966; DOI:10.1186/s40168-020-00957-z
  locator: 'Supplementary Table S6: header X1; X39/X83 and X201:X213'
  summary: Two exact core Beta genomes have carbon-fixation positives; all 13 Nitrospirae
    rows have zero in this complete-function summary.
  support: supports
  accessed_at: '2026-10-22T08:55:52.198220Z'
  snapshot_sha256: ff276181fa5998d362a89ef0213da63286e40b5e0d3f42d2fe5d4f475ca2bdb1
- evidence_id: pathway-table
  kind: primary_source
  reference: PMID:34022966; DOI:10.1186/s40168-020-00957-z
  locator: 'Supplementary Table S4: carbon-fixation headers and selected 13 Nitrospirae
    rows, including ED30/ED41/ED136'
  summary: Some pathway fragments are classified POSSIBLE; the S6 zeros do not establish
    universal physiological inability.
  support: supports
  accessed_at: '2026-10-22T08:55:52.198463Z'
  snapshot_sha256: 584d46eb65fa72a20ebc9f6467ec26a0c4d113d12a764443e23f6a7b93f3695e
- evidence_id: cazy-table
  kind: primary_source
  reference: PMID:34022966; DOI:10.1186/s40168-020-00957-z
  locator: 'Supplementary Table S8: row 66, exact S5 row 11 genome; AJ66/CE11=8, AP66/CE14=3,
    ET66/GH16=1'
  summary: The core Gemmatimonadetes genome has source-linked degradative potential,
    not measured substrate flux.
  support: supports
  accessed_at: '2026-10-22T08:55:52.198963Z'
  snapshot_sha256: c3061372f71a148b44697d35acb0b3f90210ce0dc41aab5fbaa434ebcaae8f7f
- evidence_id: SI-figures
  kind: primary_source
  reference: PMID:34022966; DOI:10.1186/s40168-020-00957-z
  locator: 'Supplementary Figures S1–S9: all 11 physical pages and separate S3 tree
    overview'
  summary: Legends and plots were read; the separate large S3 tree was inspected as
    an overview, not tip-by-tip or reanalyzed.
  support: supports
  accessed_at: '2026-10-22T08:55:52.199220Z'
  snapshot_sha256: abc6abcb72d995b8f38f892dc9b4ab58fee321140408d50386ab3093c3e7f46f
- evidence_id: ontology
  kind: authority
  reference: /private/tmp/cm-review-session/batch-16/000137/ontology-authority.json
  locator: 12 distinct pairs, 21 placements
  summary: Encoded labels match local authority; source rank and applicability require
    separate assessment.
  support: supports
  accessed_at: '2026-10-22T08:55:52.202073Z'
  snapshot_sha256: afe8b7c40dfaff2989f8ce7710e0b0f048db04b51c6a0c09027ff26bac8691a2
- evidence_id: semantics
  kind: authority
  reference: /private/tmp/cm-review-session/batch-16/000137/ontology-semantic-notes.json
  locator: Final schema, taxon and selected-supplement assessment
  summary: Current role/state definitions and verified Nitrospirota phylum candidate;
    qualified Beta/Gemma roles retained.
  support: supports
  accessed_at: '2026-10-22T08:55:52.202310Z'
  snapshot_sha256: adcaa0310b6a3683487a8de80f6f1d09e6614eb19486991e4b74ed9b8801d03e
- evidence_id: gtdb
  kind: authority
  reference: /private/tmp/cm-review-session/batch-16/000137/child-gtdb-crosswalk.json
  locator: Encoded mapping routes
  summary: Acidobacteriota 203/203 and Gemmatimonadota 36/36 reproduce; mapping provenance
    requires repair.
  support: supports
  accessed_at: '2026-10-22T08:55:52.202499Z'
  snapshot_sha256: d4da40fc97c139f021e10c16ba0d7b7a63724bcd80ba072e84a4ffe2f75146ac
- evidence_id: beta-mapping
  kind: authority
  reference: /private/tmp/cm-review-session/batch-16/000137/child-curated-beta-mapping-classified.json
  locator: Curated order route, classified genomes only
  summary: Burkholderiales 41903/41937; 31 Enterobacterales and three Pseudomonadales.
    One blank order is excluded.
  support: supports
  accessed_at: '2026-10-22T08:55:52.202657Z'
  snapshot_sha256: 4ce13b3aaab23ee7d21663577469657f8e46e9c08d062c9665ddc9d36c63ba9b
- evidence_id: adapter
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000137/child-structured-adapter-applicability.json
  locator: amoCAB/nxrAB, carbon fixation, CAZy and oxidation genes
  summary: Exact MAG/gene scope assessed; optional runner unavailable in the owned
    runtime, provider coverage not queried.
  support: supports
  accessed_at: '2026-10-22T08:55:52.202816Z'
  snapshot_sha256: 21781843cb72127d7b4ce76e578350cf535a335d4a42dde7596dad8493ff7c45
- evidence_id: snippets
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000137/snippet-audit.json
  locator: All 16 canonical placements
  summary: All strictly match fresh JATS and cache; seven also match fresh MED Abstract.
  support: supports
  accessed_at: '2026-10-22T08:55:52.202969Z'
  snapshot_sha256: d5ceae48683c0eec4a0e4bdeca38f8eaa395065e02982cbe3d5b52e500464646
- evidence_id: resources
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000137/dataset-verification.json
  locator: PRJNA630765 and ESS-DIVE DOI:10.15485/1631979
  summary: Both public resources resolve at the source-declared genome/environmental
    scope.
  support: supports
  accessed_at: '2026-10-22T08:55:52.203182Z'
  snapshot_sha256: 8fd0963482c865a5582d8ae6252cfaacb9eee4c1a9101d0a364f80aeb515241d
- evidence_id: resource-bridge
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000137/dataset-s1-bridge.json
  locator: All 144 S1 project IDs and 14 RNA sample metadata rows
  summary: 143 IDs match the umbrella exactly; the differing pair identifies the same
    source sample context. All RNA samples are 2016 L.
  support: supports
  accessed_at: '2026-10-22T08:55:52.203332Z'
  snapshot_sha256: aecaf56628e475a7a0b1bfe95fc0110d49009a30dcd2c1866d87841330448c3d
- evidence_id: provenance
  kind: prior_review
  reference: /private/tmp/cm-review-session/batch-16/000137/provenance-audit.json
  locator: Exact batch35 records[1], history, cohort and four current issues
  summary: Graph repair is retained; 1421 remains open. Cache header authors differ
    from genuine source metadata.
  support: supports
  accessed_at: '2026-10-22T08:55:52.203518Z'
  snapshot_sha256: 768236210cc7c55c22f9ef923fa8310bb77008a417d93b4f7ca7261ceca1275b
- evidence_id: read-scope
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000137/lead-primary-read-scope.json
  locator: Whole fresh main and bounded supplements
  summary: Whole main with 68 references, six main figures, all SI figure pages and
    selected table cells read.
  support: supports
  accessed_at: '2026-10-22T08:55:52.203703Z'
  snapshot_sha256: b3c3078d7d6230073bba2c823eb95f9cc28f6b76185a46d88d42cdf74791fb94
- evidence_id: assets
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000137/lead-source-assets.json
  locator: Actual source and transport inventory
  summary: Failed partial ZIP, 404 HTML and DNS routes are distinguished from genuine
    source payloads.
  support: supports
  accessed_at: '2026-10-22T08:55:52.203877Z'
  snapshot_sha256: 0cd9e16173ddfd836ee069124f6c91e44768d0982a8dd5c14e8dc1fb719bda5b
- evidence_id: locators
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000137/source-locator-verification.json
  locator: Direct headings, paragraphs and field quote
  summary: Exact source locators verified.
  support: supports
  accessed_at: '2026-10-22T08:55:52.204110Z'
  snapshot_sha256: 1eb4ae4b7b6203fc41829f09b5435322daf73b35703a9130196ecbe67e43d990
- evidence_id: source-audit
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000137/source-audit.json
  locator: Final scientific judgment
  summary: Two major findings and one minor finding; all three qualified nodes retained.
  support: supports
  accessed_at: '2026-10-22T08:55:52.204157Z'
  snapshot_sha256: cc77250a5107122b67b8004302b6ef8ec665a6a3dfd6f1b55068d365431fc6a7
- evidence_id: root-source
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000137/root-independent-source-audit.json
  locator: Independent source acceptance and read limits
  summary: Completed scientific review; 2 P2 + 1 P3, completeness 75 and quality 98.
  support: supports
  accessed_at: '2026-10-22T08:55:52.204317Z'
  snapshot_sha256: 50c22ef145d487c0e78c651c897d5d82046746303ba79800e9517f02ed6b5ba5
- evidence_id: support
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000137/support-final-audit.json
  locator: Final supporting reconciliation
  summary: Thirty unchanged inputs; 16 strict snippets; native network has two disconnected
    warnings.
  support: supports
  accessed_at: '2026-10-22T08:55:52.204518Z'
  snapshot_sha256: d9aea8d71e84d9dd8d5bdeba5d7f2a4ab2f4c1705c10edf63b36750d1bfe6eaf
- evidence_id: support-manifest
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000137/support-frozen-manifest.json
  locator: Supporting source pins
  summary: Frozen provenance, resources, source and authority outputs verified.
  support: supports
  accessed_at: '2026-10-22T08:55:52.204714Z'
  snapshot_sha256: 3a249b9abb4625ed219bc503b3868017b83f6cd53d1391e00ea6d2b006d780c6
- evidence_id: auxiliary
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000137/auxiliary-frozen-manifest.json
  locator: Final auxiliary checks and source scope
  summary: Eight required native checks passed; ancillary helper failure is separate.
  support: supports
  accessed_at: '2026-10-22T08:55:52.204859Z'
  snapshot_sha256: 9ae614986c646cbcf0c910395585c9affb4112b011de7e3f2eb9cb4ba3e7a3c2
- evidence_id: selected-functions
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000137/selected-function-presence-verification.json
  locator: All 50 selected S6 positive maps compared with raw cells
  summary: All maps match; 46 are nonempty. Empty row 14 is genuine, not an extraction
    error.
  support: supports
  accessed_at: '2026-10-22T08:55:52.205003Z'
  snapshot_sha256: c9a8d03de0b10c5e4ffabb25919c43debbeb17a6f1e96dc671b625cf7dbd6692
- evidence_id: check-validate
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000137/validate.json
  locator: Actual command, stdout and stderr
  summary: Required native exit 0.
  support: supports
  accessed_at: '2026-10-22T08:55:52.205343Z'
  snapshot_sha256: 4633386d0fc9bc9b9bb9ca69dfcca53c3cb6b4142318da610b4842edabdde705
- evidence_id: check-validate-strict
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000137/validate-strict.json
  locator: Actual command, stdout and stderr
  summary: Required native exit 0.
  support: supports
  accessed_at: '2026-10-22T08:55:52.205533Z'
  snapshot_sha256: 4399462e8775a2bdf6af040e2b3fa645cef48b5f28df50e19ff977d3e7c668bd
- evidence_id: check-validate-terms
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000137/validate-terms.json
  locator: Actual command, stdout and stderr
  summary: Required native exit 0.
  support: supports
  accessed_at: '2026-10-22T08:55:52.205718Z'
  snapshot_sha256: 89a8450d35167509a4c757bab149497c95a8296aea142e38933bfe1f71e4ef9d
- evidence_id: check-validate-references-explained
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000137/validate-references-explained.json
  locator: Actual command, stdout and stderr
  summary: Required native exit 0.
  support: supports
  accessed_at: '2026-10-22T08:55:52.205898Z'
  snapshot_sha256: 558c86b87908a90d641a622ded81ba90ccbd668be29f8dc7147a758ac52f85ad
- evidence_id: check-validate-gtdb
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000137/validate-gtdb.json
  locator: Actual command, stdout and stderr
  summary: Required native exit 0.
  support: supports
  accessed_at: '2026-10-22T08:55:52.206057Z'
  snapshot_sha256: 0a327c256808dd6e31cab1aff18003599df6df14dc123baf74865622f75ac796
- evidence_id: check-validate-gtdb-domain
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000137/validate-gtdb-domain.json
  locator: Actual command, stdout and stderr
  summary: Required native exit 0.
  support: supports
  accessed_at: '2026-10-22T08:55:52.206249Z'
  snapshot_sha256: d02a7b543cdfbf93ff36dd103de07d2e084113b9e5910c48e47f12a8ab704c50
- evidence_id: check-validate-history
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000137/validate-history.json
  locator: Actual command, stdout and stderr
  summary: Required native exit 0.
  support: supports
  accessed_at: '2026-10-22T08:55:52.206479Z'
  snapshot_sha256: fc84d43c3f40125254ddfd1f43d0bb2c448707de351342f2abc1ec67379e00a3
- evidence_id: check-normalize-cache-names-check
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000137/normalize-cache-names-check.json
  locator: Actual command, stdout and stderr
  summary: Required native exit 0.
  support: supports
  accessed_at: '2026-10-22T08:55:52.206656Z'
  snapshot_sha256: 4e30eb784bebbad01381de7b9c329aedc63279769206f741f2e3fec84db27be2
- evidence_id: context-audit-network
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/audit-network.json
  locator: Fresh batch16 corpus baseline
  summary: Nonrequired corpus result; not the target scientific verdict.
  support: supports
  accessed_at: '2026-10-22T08:55:52.206880Z'
  snapshot_sha256: f4809c6a349f1496dbfe0243fb5ce661f469f7235f2aa00e6294ee3aa04f3123
- evidence_id: context-check-network-quality
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/check-network-quality.json
  locator: Fresh batch16 corpus baseline
  summary: Nonrequired corpus result; not the target scientific verdict.
  support: supports
  accessed_at: '2026-10-22T08:55:52.207071Z'
  snapshot_sha256: 759ba13f2cda067251275491bbafc401d0be8bddf7907c7f962eb4369f61688f
assessments:
- assessment_id: identity
  area: identity
  topic: Community and sampling units
  outcome: supported
  summary: The record identifies the correct natural field study; non-graph scope
    needs refinement.
  target_ids:
  - CommunityMech:000137
  evidence_ids:
  - record
  - core
  - field
  - membership-table
  details: The 2015 G/L/Z survey produced 248 representative genomes at 98% ANI from
    94 quality samples; 42 met the operational core rule. The 2016 L RNA study used
    a distinct 95% ANI reference set. These are field genome groupings, not cultured
    strains or a defined four-member consortium.
  dimensions:
  - name: stable_id
    value: CommunityMech:000137; PMID:34022966; PMC8141241; DOI:10.1186/s40168-020-00957-z
    definition: Canonical record and verified publication identity.
    evidence_ids:
    - record
    - source-audit
  - name: source_strains
    value: No isolate strains; operational field MAG sets
    definition: Exact MAG identifiers support selected capabilities without inventing
      culture stocks.
    evidence_ids:
    - membership-table
    - function-table
    - cazy-table
  - name: community_scope
    value: '2015 G/L/Z core: 42 of 248 genomes; 2016 RNA: L only'
    definition: Different sampling years, genome thresholds and measurements remain
      explicit.
    evidence_ids:
    - core
    - field
    - RNA-method
- assessment_id: field-scope
  area: scope
  topic: Non-graph sampling, readout and ecological state
  outcome: concern
  summary: Separate core gene enrichment from L-only transcription and equilibrium.
  target_ids:
  - CommunityMech:000137
  evidence_ids:
  - core
  - enrichment
  - RNA
  - field
  - core-method
  - semantics
  details: Description and environmental_factors[1] extend RNA findings to all three
    meanders and pool rare high-transcription functions with enriched core capacities.
    STABLE denotes ecological equilibrium; spatial prevalence and inferred persistence
    of gene inventories do not demonstrate that state. The source abstract itself
    uses broader wording, already qualified in node 2.
- assessment_id: roster
  area: grounding
  topic: Core membership, rank and functional roles
  outcome: concern
  summary: Resolve the roster boundary and use source-linked capability evidence.
  target_ids:
  - CommunityMech:000137
  evidence_ids:
  - core
  - membership-table
  - function-table
  - pathway-table
  - cazy-table
  - semantics
  details: Acidobacteriota belong to the broader reconstruction, not the 42-genome
    core. Historical Nitrospirae is a phylum; NCBITaxon:1234 is genus Nitrospira,
    while verified NCBITaxon:40117 Nitrospirota matches the source rank. Nitrification
    alone does not establish PRIMARY_PRODUCER. S6 X201:X213 are zero, but POSSIBLE
    S4 fragments prevent a universal inability claim. Retain qualified Beta producer
    potential (core genomes X39/X83), source-local Beta CAZy evidence, and Gemma degradative
    potential (S5 row 11 matches S8 row 66). Add those role-local citations rather
    than infer every genome performs the role.
- assessment_id: node-0
  area: graph
  topic: Core Floodplain Biogeochemical Potential Reservoir
  outcome: supported
  summary: Retain the qualified COMMUNITY_LEVEL claim.
  target_ids:
  - CommunityMech:000137
  evidence_ids:
  - record
  - core
  - field
  - snippets
  details: 'Exact selector ecological_interactions[0]. Participants: {"participating_taxa":
    [{"preferred_term": "Betaproteobacteria-dominated core floodplain microbiome",
    "term": {"id": "NCBITaxon:28216", "label": "Betaproteobacteria"}}, {"preferred_term":
    "Gemmatimonadota floodplain representatives", "term": {"id": "NCBITaxon:142182",
    "label": "Gemmatimonadota"}}]}. Exact canonical snippet bindings: [{"selector":
    "ecological_interactions[0].evidence[0].snippet", "sha256": "551b28509b9d79500f6eff134ec948051cc5c654c7ab1fb96c64cafe7605a351",
    "reference": "PMID:34022966", "supports": "SUPPORT", "evidence_source": "COMPUTATIONAL"},
    {"selector": "ecological_interactions[0].evidence[1].snippet", "sha256": "048ee32715246f066e774317865f1bb3428a6049f12c6dba05f7a4828e6c5a17",
    "reference": "PMID:34022966", "supports": "SUPPORT", "evidence_source": "COMPUTATIONAL"}].
    Source: PMID:34022966; DOI:10.1186/s40168-020-00957-z. Locator: Uncovering a core
    floodplain microbiome (Sec6), direct paragraphs 1–2. Operational core capacity
    is supported. The Beta/Gemma list is partial, and the explicit Acidobacteria exclusion
    is correct. Gene inventories do not establish activation, flux or exchange.'
- assessment_id: node-1
  area: graph
  topic: Core Floodplain Aerobic and Sulfur Oxidation Capacity
  outcome: supported
  summary: Retain the qualified COMMUNITY_LEVEL claim.
  target_ids:
  - CommunityMech:000137
  evidence_ids:
  - record
  - enrichment
  - field
  - snippets
  details: 'Exact selector ecological_interactions[1]. Participants: {"participating_taxa":
    [{"preferred_term": "Betaproteobacteria-dominated core floodplain microbiome",
    "term": {"id": "NCBITaxon:28216", "label": "Betaproteobacteria"}}, {"preferred_term":
    "Gemmatimonadota floodplain representatives", "term": {"id": "NCBITaxon:142182",
    "label": "Gemmatimonadota"}}]}. Exact canonical snippet bindings: [{"selector":
    "ecological_interactions[1].evidence[0].snippet", "sha256": "708b7e3efedb0d6034a9fcb526a1cbdaa438a5d09d4219f7a5d1268a7c9a8d74",
    "reference": "PMID:34022966", "supports": "SUPPORT", "evidence_source": "COMPUTATIONAL"}].
    Source: PMID:34022966; DOI:10.1186/s40168-020-00957-z. Locator: Geochemical functions,
    including those enriched in the core floodplain microbiome (Sec7), direct paragraphs
    6. Retain comparative aerobic/CO-or-other-small-molecule and thiosulfate gene
    enrichment. Neither cooperation nor niche partitioning follows from gene-content
    overlap.'
- assessment_id: node-2
  area: graph
  topic: Low-Organic-Carbon-Associated Gene Transcription in Floodplain L
  outcome: supported
  summary: Retain the qualified COMMUNITY_LEVEL claim.
  target_ids:
  - CommunityMech:000137
  evidence_ids:
  - record
  - RNA
  - field
  - snippets
  details: 'Exact selector ecological_interactions[2]. Participants: {"participating_taxa":
    [{"preferred_term": "Betaproteobacteria-dominated core floodplain microbiome",
    "term": {"id": "NCBITaxon:28216", "label": "Betaproteobacteria"}}]}. Exact canonical
    snippet bindings: [{"selector": "ecological_interactions[2].evidence[0].snippet",
    "sha256": "7c921e11d333ed514f8b30bd2fccb7480969263d8e9339e5823ce4a58c3071d8",
    "reference": "PMID:34022966", "supports": "PARTIAL", "evidence_source": "COMPUTATIONAL"},
    {"selector": "ecological_interactions[2].evidence[1].snippet", "sha256": "44afd00d9cf329b355e10a0dd81f7a3f319869c2dbf499bf5428884e3ca4a5b2",
    "reference": "PMID:34022966", "supports": "SUPPORT", "evidence_source": "COMPUTATIONAL"},
    {"selector": "ecological_interactions[2].evidence[2].snippet", "sha256": "3d0a9b65ac2be4ab6f4edfd90584204e83f0b5cdf9b35918a5d46eecf3d89c08",
    "reference": "PMID:34022966", "supports": "SUPPORT", "evidence_source": "COMPUTATIONAL"},
    {"selector": "ecological_interactions[2].evidence[3].snippet", "sha256": "755657d10edb31ed301f2422229469dbc723a3d99488cfd2ca4a77228c8107d6",
    "reference": "PMID:34022966", "supports": "SUPPORT", "evidence_source": "COMPUTATIONAL"}].
    Source: PMID:34022966; DOI:10.1186/s40168-020-00957-z. Locator: Potentially active
    genes encoding key biogeochemical transformations in the riparian zone (Sec9),
    direct paragraphs 1–8. Retain the September 2016 L-only RNA association, PARTIAL
    abstract qualification and limited Beta CBB participant. Overall Beta transcription
    favored higher organic carbon; no manipulation, all-three-site RNA replication
    or whole-core activation is established.'
- assessment_id: graph-topology
  area: graph
  topic: Three community claims and no arrows
  outcome: supported
  summary: No causal arrows are warranted by the present evidence.
  target_ids:
  - CommunityMech:000137
  evidence_ids:
  - record
  - core
  - enrichment
  - RNA
  - support
  details: All three nodes omit interaction_type and have COMMUNITY_LEVEL scope. The
    two native DISCONNECTED warnings concern Nitrospira and Acidobacteriota; they
    do not justify fabricated links or invalidate the correctly bounded nodes. Preserve
    zero downstream edges.
- assessment_id: cultivation
  area: scope
  topic: Field setting and cultivation applicability
  outcome: supported
  summary: No culture recipe or reactor setup is required for this natural survey.
  target_ids:
  - CommunityMech:000137
  evidence_ids:
  - field
  - core-method
  - semantics
  details: Soils were sampled at East River meander-bound floodplains in Colorado.
    September 2015 baseflow sampling and 2016 L resampling are distinct. Tubes, frozen
    storage and molecular processing are analytical handling, not growth conditions.
  dimensions:
  - name: environment
    value: ENVO:00001998 soil; East River floodplain setting
    definition: The broad term is compatible with the documented natural habitat.
    evidence_ids:
    - field
    - ontology
  - name: medium
    value: 'Not applicable: uncultured field survey'
    definition: Do not import laboratory media or infer growth requirements from annotations.
    evidence_ids:
    - field
    - semantics
  - name: experimental_setting
    value: 2015 three-floodplain metagenomes and separate 2016 L metatranscriptomes
    definition: Observational sampling, not a selective carbon manipulation or engineered
      reactor.
    evidence_ids:
    - field
    - RNA-method
- assessment_id: grounding
  area: grounding
  topic: Ontology correspondence and GTDB provenance
  outcome: concern
  summary: Labels match; source taxonomic rank and mapping provenance need separate
    repair.
  target_ids:
  - CommunityMech:000137
  evidence_ids:
  - ontology
  - semantics
  - gtdb
  - beta-mapping
  details: 'The curated Beta order vote reproduces 41903/41937 classified genomes:
    Burkholderiales plus 31 Enterobacterales and three Pseudomonadales. Preserve that
    override and the 203/203 Acidobacteriota and 36/36 Gemmatimonadota mappings. Reference-genome
    counts are not field abundance. Filesystem mtime does not establish a GTDB release
    or build; the source marker-profile R95 context also does not establish the local
    crosswalk version.'
  dimensions:
  - name: taxon_grounding
    value: Encoded NCBITaxon:28216, NCBITaxon:1234, NCBITaxon:57723 and NCBITaxon:142182;
      proposed phylum NCBITaxon:40117
    definition: Preserve source higher-rank labels; reassess GTDB for the corrected
      phylum rather than forcing a genus vote.
    evidence_ids:
    - ontology
    - semantics
    - gtdb
    - beta-mapping
- assessment_id: evidence
  area: evidence
  topic: Literal excerpts and scientific interpretation
  outcome: supported
  summary: All 16 excerpts match; their placement still requires the specified scope
    repairs.
  target_ids:
  - CommunityMech:000137
  evidence_ids:
  - snippets
  - RNA
  - function-table
  - cazy-table
  details: Seven placements also match MED Abstract; all 16 match fresh JATS and cache
    under case-preserving NFKC/whitespace normalization. Field sampling, computed
    genome capacities and mapped RNA abundance are separate evidence layers. Metabolites
    and GO processes are contextual potential, not measured flux. CARBON_SEQUESTRATION
    and Beta DOMINANT remain qualified context.
  dimensions:
  - name: evidence_tier
    value: Field observations, computational genome capacities and RNA-associated
      expression
    definition: Neither annotation nor transcription proves enzyme activity, environmental
      flux or partner exchange.
    evidence_ids:
    - snippets
    - RNA
    - function-table
    - semantics
- assessment_id: resources
  area: evidence
  topic: Sequence and environmental resources
  outcome: supported
  summary: Both encoded resources resolve; no resource finding.
  target_ids:
  - CommunityMech:000137
  evidence_ids:
  - resources
  - resource-bridge
  details: PRJNA630765 is a 144-project umbrella; ESS-DIVE supplies genome sets and
    environmental metadata. S1 has 143 exact project-ID matches; PRJNA405311 versus
    PRJNA405415 identifies the same sample/JGI/GOLD context. Preserve the separate
    S1 Z/L label conflict. No sequence download or expression reanalysis was performed.
- assessment_id: source-access
  area: scope
  topic: Source coverage and limits
  outcome: supported
  summary: Every encoded claim was assessed against the whole main and relevant supplements.
  target_ids:
  - CommunityMech:000137
  evidence_ids:
  - read-scope
  - assets
  - SI-figures
  - selected-functions
  - root-source
  details: Lead read all 112,926 main-text characters including 68 references, all
    six main figure pixels, all 11 supplementary figure pages and the separate S3
    tree overview. Eight workbook inventories and selected membership/function/CAZy
    cells were inspected; S7 was read completely. Other declared tables/trees and
    the video were not exhaustively read or reanalyzed. Genuine publisher assets supersede
    failed transport routes as evidence; failed files remain preserved.
- assessment_id: provenance
  area: ownership
  topic: Prior context and maintained owner
  outcome: supported
  summary: Retain the prior graph repair and address the current metadata findings.
  target_ids:
  - CommunityMech:000137
  evidence_ids:
  - provenance
  - source-audit
  - support
  details: Exact batch35 records[1], whole sole history/adversarial and relevant cohort
    context were read. Issue 1418 is closed; 1421 remains open. Issues 401/451 are
    closed and do not override source rank or the independently reproduced Beta vote.
    Cache-header authors disagree with the genuine article; canonical PMID/DOI remain
    valid. No record, cache, history or issue was edited.
- assessment_id: validation
  area: schema
  topic: Actual checks and limitations
  outcome: supported
  summary: Eight required checks passed; structural warnings remain explicit.
  target_ids:
  - CommunityMech:000137
  evidence_ids:
  - auxiliary
  - support
  - adapter
  details: Native success does not certify scientific entailment. Two disconnected
    warnings remove the network score bonus. Optional structured-adapter unavailability
    and transport/reader/helper failures are separate from native failures.
- assessment_id: metrics
  area: completeness
  topic: Literal profile scores
  outcome: supported
  summary: Completeness 75; validation quality 98.
  target_ids:
  - CommunityMech:000137
  evidence_ids:
  - support
  details: Scores describe record presence and rubric deductions, not scientific completeness.
  metrics:
  - name: completeness
    value: 75
    unit: points
    minimum: 0
    maximum: 100
    definition: 50 required fields and roles +5 environment +0 factors threshold +10
      nodes +0 external resources +0 medium +5 datasets +5 node metabolites =75.
  - name: validation_quality
    value: 98
    unit: points
    minimum: 0
    maximum: 100
    definition: 100 -10*2 -2*1 +20*min((7/3)/2,1) +0 =98. Three nodes have seven evidence
      entries; two DISCONNECTED warnings mean no network bonus.
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
findings:
- finding_id: non-graph-scope
  issue_key: cm-000137-non-graph-scope
  category: evidence
  severity: major
  native_severity: P2
  normalization_reason: The mismatch changes the location, measurement and ecological
    interpretation of the central community claim.
  rule_id: review-checklist.claim-specific-support-and-context
  status: open
  certainty: confirmed
  title: Separate field cohorts, measurements and ecological state
  description: Non-graph prose combines three-site core gene enrichment with L-only
    RNA associations; STABLE asserts equilibrium beyond spatial prevalence.
  target_ids:
  - CommunityMech:000137
  field_paths:
  - description
  - ecological_state
  - environmental_factors[1]
  evidence_ids:
  - core
  - enrichment
  - RNA
  - field
  - core-method
  - semantics
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/East_River_Floodplain_Core_Microbiome.yaml
    role: canonical_record
- finding_id: roster-rank-roles
  issue_key: cm-000137-roster-rank-roles
  category: grounding
  severity: major
  native_severity: P2
  normalization_reason: Community membership and taxonomic resolution are materially
    different; role repairs must retain the actual positive MAG evidence.
  rule_id: review-checklist.claim-specific-support-and-context
  status: open
  certainty: confirmed
  title: Align core membership, source rank and role evidence
  description: The named core roster includes non-core Acidobacteriota and uses a
    Nitrospira genus ID for the source phylum. Current role excerpts support membership
    or nitrification rather than all assigned capabilities.
  target_ids:
  - CommunityMech:000137
  field_paths:
  - taxonomy
  evidence_ids:
  - core
  - membership-table
  - function-table
  - pathway-table
  - cazy-table
  - semantics
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/East_River_Floodplain_Core_Microbiome.yaml
    role: canonical_record
- finding_id: gtdb-provenance
  issue_key: cm-000137-gtdb-provenance
  category: grounding
  severity: minor
  native_severity: P3
  normalization_reason: A bounded provenance defect; valid mapping results need not
    be replaced.
  rule_id: review-checklist.claim-specific-support-and-context
  status: open
  certainty: confirmed
  title: Correct mapping release and build provenance
  description: Latest/build-date wording is unsupported by the local mapping file
    date, although the curated numerical mappings reproduce.
  target_ids:
  - CommunityMech:000137
  field_paths:
  - taxonomy[0].taxon_term.gtdb_classification.mapping_source
  - taxonomy[2].taxon_term.gtdb_classification.mapping_source
  - taxonomy[3].taxon_term.gtdb_classification.mapping_source
  evidence_ids:
  - gtdb
  - beta-mapping
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/East_River_Floodplain_Core_Microbiome.yaml
    role: canonical_record
actions:
- action_id: repair-field-scope
  description: Align non-graph assertions with their sampling and measurement scope.
  finding_ids:
  - non-graph-scope
  target_ids:
  - CommunityMech:000137
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/East_River_Floodplain_Core_Microbiome.yaml
    role: canonical_record
  acceptance_checks:
  - Separate the 2015 G/L/Z 248-genome reconstruction and 42-genome core from the
    2016 L-only RNA snapshot and distinct reference set.
  - Restrict core enrichment to the demonstrated comparative capacities; describe
    rare high-transcription functions as RNA associations, not whole-core activation
    or flux. Apply this to description and environmental_factors[1], including evidence
    explanation/support.
  - Omit STABLE unless ecological-equilibrium evidence is supplied; do not infer another
    state from its removal. Retain the existing three qualified nodes and zero arrows.
- action_id: repair-roster-and-roles
  description: Separate core membership from contextual taxa and ground source-specific
    capabilities.
  finding_ids:
  - roster-rank-roles
  target_ids:
  - CommunityMech:000137
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/East_River_Floodplain_Core_Microbiome.yaml
    role: canonical_record
  acceptance_checks:
  - Move or explicitly segregate non-core Acidobacteriota from the named operational
    core while preserving its broader-dataset occurrence and potential. Do not expand
    the partial roster to invented isolates.
  - Replace genus NCBITaxon:1234 with verified source-rank NCBITaxon:40117 Nitrospirota
    (historical Nitrospirae) where representing that phylum; reassess GTDB at that
    rank and propagate any identity change consistently.
  - 'Attach exact MAG-level role evidence: retain qualified Beta carbon-fixation and
    CAZy potential and core Gemma CAZy potential. Omit or justify Nitrospirae PRIMARY_PRODUCER
    with carbon-fixation evidence; nitrification alone is insufficient. Preserve incomplete/POSSIBLE
    pathways and avoid universal negative physiology.'
  - Preserve ordinal Beta dominance and the qualified graph participant scopes. Do
    not add causal arrows merely to remove disconnected warnings.
- action_id: repair-gtdb-provenance
  description: State verified mapping provenance without changing valid numerical
    cores.
  finding_ids:
  - gtdb-provenance
  target_ids:
  - CommunityMech:000137
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/East_River_Floodplain_Core_Microbiome.yaml
    role: canonical_record
  acceptance_checks:
  - Replace latest/build-date claims with verified snapshot hash and retrieval context;
    leave release/build unknown unless separately documented.
  - Retain the curated Beta Burkholderiales 41903/41937 vote, fraction 0.999, with
    three distinct target orders in total; preserve Acidobacteriota 203/203 and Gemmatimonadota
    36/36. Do not substitute the default Beta class vote or interpret mapping counts
    as abundance.
  - After separately authorized curation, run focused native schema, ontology, reference,
    GTDB/domain and history gates and recheck all graph participants.
  - After separately authorized record curation, regenerate HTML with just gen-html
    and run just check-docs-current, as required by CLAUDE.md.
limitations:
- Genomic potential and RNA abundance do not establish environmental flux or partner
  exchange. Spatial core prevalence does not establish equilibrium.
- Source abstract all-three RNA wording conflicts with L-only Methods. Figure 3 caption
  reports 242 non-core genomes despite 248 total and 42 core; no numerical repair
  is inferred here.
- The 2015 98% ANI core and the combined 2015/2016 215-genome, 95% ANI reference set
  are distinct. Supplement joins use exact genome identifiers only, not reannotation
  or universal physiology.
- Eight workbook inventories and bounded cells were assessed, not all 23 declared
  supplementary objects. The separate large S3 tree received overview inspection only;
  no raw sequence, tree or transcript reanalysis.
- The S1 project-ID and Z/L metadata discrepancies are retained at their exact source
  scope. Cache front-author metadata differs from the genuine source, without invalidating
  canonical publication identity.
- A partial bulk ZIP, 404 image responses and DNS failures are preserved as failed
  transport, not scientific evidence. Optional structured adapter unavailable in the
  owned runtime.
notes:
- Exact source/target arrays and original command strings are verified before native
  candidate validation.
- Three nodes, seven canonical snippet hashes, zero arrows and eight evidence-linked
  dimensions are bound. The sole direct primary quotation has two words.
tags:
- record-review
- floodplain
- field-metagenomics
- batch-16
```
