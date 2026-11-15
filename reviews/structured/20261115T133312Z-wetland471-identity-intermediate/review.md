# Wetland471 identity intermediate: distinguish Y13/M, Enterococcus isolates and sediment MAGs

- Review: 20261115T133312Z-wetland471-identity-intermediate
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-11-15T13:33:12.095514Z
- Finished UTC: 2026-11-15T13:33:12.272811Z
- Reviewer: codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: false

## Summary

The persisted source-identity intermediate corrects top-down Y13 versus bottom-up M, limits the E. casseliflavus descriptor to R12 rather than PseS3/R1/R3, and separates the R12 isolate from sediment MAG bin436. Exactly four scalars, one open six-quotation discussion and one native inline event changed. All original terms, GTDB states, source snippets, functional roles, three graph nodes, two arrows and older history remain unchanged. Eight native identity gates and two separate reference checks passed. All16 snippet surfaces were actually compared and matched. Incomplete membership and mechanistic interpretation remain open under2898/2899; taxonomy mapping and strict composite successor admission have not occurred.

## Scope And Provenance

Four source-identity scalars, one open evidence-backed discussion, actual application/history/native-check chain and lexical comparison of current reference snippets.

Selection: The fixed source correction for CommunityMech:000471 is isolated from all other records and from the subsequent GTDB mapping transition.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base af80bc0970b2b495b16c2c5c237cdfbbaa771ce8.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000471 | kb/communities/Wetland_Lindane_Degrading_Organochlorine_Consortium.yaml # description; taxonomy[0].taxon_term.notes; taxonomy[0].evidence[0].explanation; taxonomy[4].taxon_term.notes; discussions[0]; appended curation_history | maintained | Wetland471 bounded source-identity intermediate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | CommunityMech:000471 | Actual scoped native command passed on the exact identity-corrected intermediate with unchanged captured inputs. |
| strict | passed | True | CommunityMech:000471 | Actual scoped native command passed on the exact identity-corrected intermediate with unchanged captured inputs. |
| gtdb | passed | True | CommunityMech:000471 | Actual scoped native command passed on the exact identity-corrected intermediate with unchanged captured inputs. |
| domain | passed | True | CommunityMech:000471 | Actual scoped native command passed on the exact identity-corrected intermediate with unchanged captured inputs. |
| scalars | passed | True | CommunityMech:000471 | Actual scoped native command passed on the exact identity-corrected intermediate with unchanged captured inputs. |
| new-history | passed | True | CommunityMech:000471 | Actual scoped native command passed on the exact identity-corrected intermediate with unchanged captured inputs. |
| history | passed | True | CommunityMech:000471 | Actual scoped native command passed on the exact identity-corrected intermediate with unchanged captured inputs. |
| terms | passed | True | CommunityMech:000471 | Actual scoped native command passed on the exact identity-corrected intermediate with unchanged captured inputs. |
| references | passed | True | CommunityMech:000471 | Actual native validate-references-explained passed on the identity-corrected record with zero reported issues. The issue counter alone is not a comparison count; the separate measured check supplies actual coverage. |
| reference-measurement | passed | True | CommunityMech:000471 | The unchanged maintained native collector/matcher compared all16 snippet surfaces, including all six newly added Discussion SupportingReference quotations;16 matched and0 native issues were observed. This is lexical source matching, not verification of scientific interpretation. |

## Scientific And Domain Assessments

### Source treatment labels and isolate/MAG assignment

identity: supported. Targets: CommunityMech:000471.

The four scalar corrections follow exact primary passages: Y13 is top-down and M bottom-up; R12 is the E. casseliflavus isolate while PseS3 and R1/R3 belong to other Enterococcus species. R12 and bin436 share a reported species comparison but remain distinct isolate and sediment MAG inputs. No new stock accession or study-genome assignment is inferred.

### Open membership, revival and graph limits

scope: concern. Targets: CommunityMech:000471.

The five retained descriptors are a partial representation of M and do not establish a complete Y13 roster. Intended inoculation does not prove each stock revived or colonized sediment. The six new discussion quotations match the source, but the retained pceA, syntrophy and methane causal graph remains an explicit separate concern under2899.

### Exact persisted intermediate and separate technical checks

provenance: supported. Targets: CommunityMech:000471.

Actual source/candidate/application receipts, the native inline event, one native EDIT sidecar and all ten scoped checks bind the exact current identity intermediate. Original terms, mapping states, snippets, functional roles, graph and older history are preserved. Mapping, composite historical admission, generated products and aggregate QC remain separate.

## Findings

### 000471-incomplete-roster: Full M/Y13 membership and stock establishment remain unresolved

major / open / confirmed; issue key: communitymech-2898.

The source describes four named partner taxa plus seven isolated degraders for M; the five retained descriptors are incomplete. Y13 is a distinct sediment enrichment. Full TableS1 stock representation and strain-specific revival/endpoint establishment are not established by this correction.

### 000471-retained-graph-limits: Existing mechanistic graph remains outside identity approval

major / open / confirmed; issue key: communitymech-2899.

The three nodes and two arrows are preserved; the separate pceA acquisition, syntrophy and methane causal claims remain open under2899. Matching source snippets or technical gate success does not resolve those interpretation gaps.

## Recommended Actions And Acceptance Checks

### 000471-resolve-membership

Resolve the separate M and Y13 membership boundary against full primary stock evidence before claiming a complete participant roster or endpoint stock establishment.

- Identify all intended M stocks from the primary supplementary roster with source locators, preserving separate Y13 enrichment scope.
- Keep inoculated membership, observed revival and endpoint colonization distinct; add no unsupported stock accession or strain equivalence.

### 000471-reassess-graph

Resolve the existing graph interpretation findings through a separate source-backed scientific assessment and bounded correction if justified.

- Reassess each pceA acquisition, syntrophy and methane causal claim against the relevant experimental or metagenomic evidence.
- Retain direct observations while qualifying or removing unsupported causal relations; preserve immutable previous reviews and append actual correction history.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| 000471-primary | references_cache/PMID_42663479.txt; Retained Methods top-down/bottom-up construction, consortium composition, Enterococcus ANI comparison, MAG-versus-isolate comparison and stock revival caveat; seven exact anchors pinned in471-identity-plan-001.json. | supports | Methods assign Y13 to top-down enrichment and M to the bottom-up mixture. The ANI paragraph distinguishes PseS3/E. avium, R1/R3/E. thailandicus and R12/E. casseliflavus. The MAG comparison and revival caveat limit isolate/MAG and stock-establishment inference. |
| 000471-plan | reports/gtdb-wetland-identity-20261115/471-identity-plan-001.json; Exactly four before/after scalar paths, source anchor indices, one OPEN discussion with six snippets, and intended native inline event. | supports | The reviewed plan preserves all five original taxonomy descriptors and three-node/two-arrow graph while correcting source labels and the Enterococcus explanation. Its discussion explicitly retains incomplete membership and establishment limits. |
| 000471-application | .temp/gtdb-wetland-identity-20261115/m5-applied-001/receipt.json; Actual applied flag, original2191214b to acceptedb3234d5f, reviewed stagebfee943e, source plan24250d0c, direct writer hash and one native inline event; sidecar1f593c32 bound through new-history. | supports | The guarded writer persisted the exact accepted M5 candidate at af80bc09. The independently reviewed local/M5 difference was only the inline event timestamp. Native history records the actual applied receipt and changed sections. |
| 000471-measured-source | .temp/gtdb-wetland-identity-20261115/reference-measurement-001/measurement.json; One completed record;16 surfaces/16 comparisons/16 matches; discussions[0].evidence[0..5] all traversed as SupportingReference with consistent PMID42663479 binding. | supports | Every current snippet occurrence was compared to the existing captured source. Lexical matching does not establish the truth of a causal or membership interpretation attached to a quotation. |
| 000471-prior | reports/causal_graph_review/decisions/20261020-stage2-fifteen-records-batch133.yaml; Immutable CommunityMech:000471 original85c78730 to2191214b lineage and three-node community graph decision; current batch133 remains unchanged in this intermediate. | context_only | The historical decision and earlier record/history remain immutable. Its graph is preserved as an explicit unresolved mechanism boundary, not recertified by the current source-identity correction. A later exact composite successor must preserve unrelated batch133 admissions. |
| 000471-schema | .temp/gtdb-wetland-identity-20261115/471-schema-001/native.log | supports | Actual scoped native command passed on the exact identity-corrected intermediate with unchanged captured inputs. |
| 000471-strict | .temp/gtdb-wetland-identity-20261115/471-strict-001/native.log | supports | Actual scoped native command passed on the exact identity-corrected intermediate with unchanged captured inputs. |
| 000471-gtdb | .temp/gtdb-wetland-identity-20261115/471-gtdb-001/native.log | supports | Actual scoped native command passed on the exact identity-corrected intermediate with unchanged captured inputs. |
| 000471-domain | .temp/gtdb-wetland-identity-20261115/471-domain-001/native.log | supports | Actual scoped native command passed on the exact identity-corrected intermediate with unchanged captured inputs. |
| 000471-scalars | .temp/gtdb-wetland-identity-20261115/471-scalars-001/native.log | supports | Actual scoped native command passed on the exact identity-corrected intermediate with unchanged captured inputs. |
| 000471-new-history | .temp/gtdb-wetland-identity-20261115/471-new-history-001/native.log | supports | Actual scoped native command passed on the exact identity-corrected intermediate with unchanged captured inputs. |
| 000471-history | .temp/gtdb-wetland-identity-20261115/471-history-001/native.log | supports | Actual scoped native command passed on the exact identity-corrected intermediate with unchanged captured inputs. |
| 000471-terms | .temp/gtdb-wetland-identity-20261115/471-terms-001/native.log | supports | Actual scoped native command passed on the exact identity-corrected intermediate with unchanged captured inputs. |
| 000471-references | .temp/phase2-schema-20261115/wetland-m5-references-002.log | supports | Actual native validate-references-explained passed on the identity-corrected record with zero reported issues. The issue counter alone is not a comparison count; the separate measured check supplies actual coverage. |
| 000471-reference-measurement | .temp/phase2-schema-20261115/wetland-m5-measurement-001.log | supports | The unchanged maintained native collector/matcher compared all16 snippet surfaces, including all six newly added Discussion SupportingReference quotations;16 matched and0 native issues were observed. This is lexical source matching, not verification of scientific interpretation. |

## Limits And Additional Notes

- This completed declared-scope assessment has partial coverage and scientific_review:false. It is not a full scientific review or approval of the complete record.
- The source is the retained PMID42663479 cache with SHA489eb292. No new paper acquisition, full supplementary roster reconstruction, sequence classification, figure inspection or exhaustive causal re-review occurred.
- The actual M5 intermediate ran on frozen af80bc0970b2b495b16c2c5c237cdfbbaa771ce8 with Python3.13.2 and current recordb3234d5f. The record differs from HEAD; the measurement explicitly binds those working bytes rather than calling them a clean committed input.
- Eight native gates include seven validators and one history scaffold. Separate validate-references-explained and instrumented native comparison passed;16 matching snippets certify lexical comparison only. No zero-issue-to-coverage inference is used.
- The first reference attempt failed before validation because the recorder supplied JUST_NO_DOTENV=1 to nested Just. Issue2908 retains that exit2; the successful second invocation explicitly supplies true without changing the recorder. The stale Discussion-coverage footer is recorded under476 and preserved in the raw log.
- GTDB descriptors, functional roles, existing snippets, three nodes, two arrows and prior history are unchanged. The full roster and stock-establishment concern2898 and mechanistic concern2899 remain open. No scientific approval or closure is inferred from this identity correction.
- A subsequent GTDB mapping transition must bind this exact intermediate and its immutable source/checkpoint evidence. Strict composite historical admission, generated HTML, combined technical QC and broader campaign completion remain pending.
- Unexecuted authored config001 had a passing verdict and no proposed actions despite retaining open major findings. Issue2911 records that native-contract inconsistency. Config002 corrected the verdict and actions; config003 preserves those corrections. No valid saved review was produced with001 or002.
- The measurement receipt inventories all runtime cache files. The builder verifies that complete inventory before and after preparation, while native review inputs archive the exact article cache actually loaded by all16 assertions plus schema, configuration, implementation and proof inputs. Unrelated cache bytes are not individually archived or scientifically assessed; their observed hashes remain in the exact measurement receipt. Issue2912 retains the first builder refusal caused by an unrelated legacy cache filename, with no review saved or source cache renamed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
kind: record
repository: CultureBotAI/CommunityMech
title: 'Wetland471 identity intermediate: distinguish Y13/M, Enterococcus isolates
  and sediment MAGs'
reviewer:
  identity: codex
  kind: agent
  independence: self_review
  independence_basis: The full original record and retained primary Methods, ANI,
    genome-comparison and revival passages were read before authoring four bounded
    scalar corrections and an open discussion. The parent independently reviewed the
    source plan, fixed writer/checker and actual M5 candidate; a peer separately read
    the source/candidate and input pins. Actual checks and source comparison are assessed
    here without a full record-science verdict.
skill: curate-yaml-record
completion: completed
verdict: needs_curation
scientific_review: false
summary: The persisted source-identity intermediate corrects top-down Y13 versus bottom-up
  M, limits the E. casseliflavus descriptor to R12 rather than PseS3/R1/R3, and separates
  the R12 isolate from sediment MAG bin436. Exactly four scalars, one open six-quotation
  discussion and one native inline event changed. All original terms, GTDB states,
  source snippets, functional roles, three graph nodes, two arrows and older history
  remain unchanged. Eight native identity gates and two separate reference checks
  passed. All16 snippet surfaces were actually compared and matched. Incomplete membership
  and mechanistic interpretation remain open under2898/2899; taxonomy mapping and
  strict composite successor admission have not occurred.
targets:
- target_id: CommunityMech:000471
  path: kb/communities/Wetland_Lindane_Degrading_Organochlorine_Consortium.yaml
  selector: description; taxonomy[0].taxon_term.notes; taxonomy[0].evidence[0].explanation;
    taxonomy[4].taxon_term.notes; discussions[0]; appended curation_history
  label: Wetland471 bounded source-identity intermediate
  kind: maintained
  ownership_note: CommunityMech owns the record. This diagnostic assesses the exact
    source-identity correction and actual provenance; unchanged biology and future
    mapping remain separate.
scope:
  description: Four source-identity scalars, one open evidence-backed discussion,
    actual application/history/native-check chain and lexical comparison of current
    reference snippets.
  selection: The fixed source correction for CommunityMech:000471 is isolated from
    all other records and from the subsequent GTDB mapping transition.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000471
  exclusions:
  - target: Complete M/Y13 stock membership, endpoint establishment, ecological mechanisms
      and taxonomy mapping
    reason: These are not established by the bounded identity correction or lexical/native
      validator results.
evidence:
- evidence_id: 000471-primary
  kind: primary_source
  reference: references_cache/PMID_42663479.txt
  locator: Retained Methods top-down/bottom-up construction, consortium composition,
    Enterococcus ANI comparison, MAG-versus-isolate comparison and stock revival caveat;
    seven exact anchors pinned in471-identity-plan-001.json.
  support: supports
  summary: Methods assign Y13 to top-down enrichment and M to the bottom-up mixture.
    The ANI paragraph distinguishes PseS3/E. avium, R1/R3/E. thailandicus and R12/E.
    casseliflavus. The MAG comparison and revival caveat limit isolate/MAG and stock-establishment
    inference.
  accessed_at: '2026-11-15T13:33:12.095514Z'
- evidence_id: 000471-plan
  kind: record_content
  reference: reports/gtdb-wetland-identity-20261115/471-identity-plan-001.json
  locator: Exactly four before/after scalar paths, source anchor indices, one OPEN
    discussion with six snippets, and intended native inline event.
  support: supports
  summary: The reviewed plan preserves all five original taxonomy descriptors and
    three-node/two-arrow graph while correcting source labels and the Enterococcus
    explanation. Its discussion explicitly retains incomplete membership and establishment
    limits.
  accessed_at: '2026-11-15T13:33:12.095514Z'
- evidence_id: 000471-application
  kind: record_content
  reference: .temp/gtdb-wetland-identity-20261115/m5-applied-001/receipt.json
  locator: Actual applied flag, original2191214b to acceptedb3234d5f, reviewed stagebfee943e,
    source plan24250d0c, direct writer hash and one native inline event; sidecar1f593c32
    bound through new-history.
  support: supports
  summary: The guarded writer persisted the exact accepted M5 candidate at af80bc09.
    The independently reviewed local/M5 difference was only the inline event timestamp.
    Native history records the actual applied receipt and changed sections.
  accessed_at: '2026-11-15T13:33:12.095514Z'
- evidence_id: 000471-measured-source
  kind: validation
  reference: .temp/gtdb-wetland-identity-20261115/reference-measurement-001/measurement.json
  locator: One completed record;16 surfaces/16 comparisons/16 matches; discussions[0].evidence[0..5]
    all traversed as SupportingReference with consistent PMID42663479 binding.
  support: supports
  summary: Every current snippet occurrence was compared to the existing captured
    source. Lexical matching does not establish the truth of a causal or membership
    interpretation attached to a quotation.
  accessed_at: '2026-11-15T13:33:12.095514Z'
- evidence_id: 000471-prior
  kind: prior_review
  reference: reports/causal_graph_review/decisions/20261020-stage2-fifteen-records-batch133.yaml
  locator: Immutable CommunityMech:000471 original85c78730 to2191214b lineage and
    three-node community graph decision; current batch133 remains unchanged in this
    intermediate.
  support: context_only
  summary: The historical decision and earlier record/history remain immutable. Its
    graph is preserved as an explicit unresolved mechanism boundary, not recertified
    by the current source-identity correction. A later exact composite successor must
    preserve unrelated batch133 admissions.
  accessed_at: '2026-11-15T13:33:12.095514Z'
- evidence_id: 000471-schema
  kind: validation
  reference: .temp/gtdb-wetland-identity-20261115/471-schema-001/native.log
  accessed_at: '2026-11-15T13:33:12.095514Z'
  support: supports
  summary: Actual scoped native command passed on the exact identity-corrected intermediate
    with unchanged captured inputs.
- evidence_id: 000471-strict
  kind: validation
  reference: .temp/gtdb-wetland-identity-20261115/471-strict-001/native.log
  accessed_at: '2026-11-15T13:33:12.095514Z'
  support: supports
  summary: Actual scoped native command passed on the exact identity-corrected intermediate
    with unchanged captured inputs.
- evidence_id: 000471-gtdb
  kind: validation
  reference: .temp/gtdb-wetland-identity-20261115/471-gtdb-001/native.log
  accessed_at: '2026-11-15T13:33:12.095514Z'
  support: supports
  summary: Actual scoped native command passed on the exact identity-corrected intermediate
    with unchanged captured inputs.
- evidence_id: 000471-domain
  kind: validation
  reference: .temp/gtdb-wetland-identity-20261115/471-domain-001/native.log
  accessed_at: '2026-11-15T13:33:12.095514Z'
  support: supports
  summary: Actual scoped native command passed on the exact identity-corrected intermediate
    with unchanged captured inputs.
- evidence_id: 000471-scalars
  kind: validation
  reference: .temp/gtdb-wetland-identity-20261115/471-scalars-001/native.log
  accessed_at: '2026-11-15T13:33:12.095514Z'
  support: supports
  summary: Actual scoped native command passed on the exact identity-corrected intermediate
    with unchanged captured inputs.
- evidence_id: 000471-new-history
  kind: validation
  reference: .temp/gtdb-wetland-identity-20261115/471-new-history-001/native.log
  accessed_at: '2026-11-15T13:33:12.095514Z'
  support: supports
  summary: Actual scoped native command passed on the exact identity-corrected intermediate
    with unchanged captured inputs.
- evidence_id: 000471-history
  kind: validation
  reference: .temp/gtdb-wetland-identity-20261115/471-history-001/native.log
  accessed_at: '2026-11-15T13:33:12.095514Z'
  support: supports
  summary: Actual scoped native command passed on the exact identity-corrected intermediate
    with unchanged captured inputs.
- evidence_id: 000471-terms
  kind: validation
  reference: .temp/gtdb-wetland-identity-20261115/471-terms-001/native.log
  accessed_at: '2026-11-15T13:33:12.095514Z'
  support: supports
  summary: Actual scoped native command passed on the exact identity-corrected intermediate
    with unchanged captured inputs.
- evidence_id: 000471-references
  kind: validation
  reference: .temp/phase2-schema-20261115/wetland-m5-references-002.log
  accessed_at: '2026-11-15T13:33:12.095514Z'
  support: supports
  summary: Actual native validate-references-explained passed on the identity-corrected
    record with zero reported issues. The issue counter alone is not a comparison
    count; the separate measured check supplies actual coverage.
- evidence_id: 000471-reference-measurement
  kind: validation
  reference: .temp/phase2-schema-20261115/wetland-m5-measurement-001.log
  accessed_at: '2026-11-15T13:33:12.095514Z'
  support: supports
  summary: The unchanged maintained native collector/matcher compared all16 snippet
    surfaces, including all six newly added Discussion SupportingReference quotations;16
    matched and0 native issues were observed. This is lexical source matching, not
    verification of scientific interpretation.
assessments:
- assessment_id: 000471-source-identity
  area: identity
  topic: Source treatment labels and isolate/MAG assignment
  outcome: supported
  target_ids:
  - CommunityMech:000471
  evidence_ids:
  - 000471-primary
  - 000471-plan
  - 000471-application
  - 000471-references
  - 000471-reference-measurement
  summary: 'The four scalar corrections follow exact primary passages: Y13 is top-down
    and M bottom-up; R12 is the E. casseliflavus isolate while PseS3 and R1/R3 belong
    to other Enterococcus species. R12 and bin436 share a reported species comparison
    but remain distinct isolate and sediment MAG inputs. No new stock accession or
    study-genome assignment is inferred.'
- assessment_id: 000471-source-boundaries
  area: scope
  topic: Open membership, revival and graph limits
  outcome: concern
  target_ids:
  - CommunityMech:000471
  evidence_ids:
  - 000471-primary
  - 000471-plan
  - 000471-prior
  - 000471-measured-source
  summary: The five retained descriptors are a partial representation of M and do
    not establish a complete Y13 roster. Intended inoculation does not prove each
    stock revived or colonized sediment. The six new discussion quotations match the
    source, but the retained pceA, syntrophy and methane causal graph remains an explicit
    separate concern under2899.
- assessment_id: 000471-identity-provenance
  area: provenance
  topic: Exact persisted intermediate and separate technical checks
  outcome: supported
  target_ids:
  - CommunityMech:000471
  evidence_ids:
  - 000471-application
  - 000471-schema
  - 000471-strict
  - 000471-gtdb
  - 000471-domain
  - 000471-scalars
  - 000471-new-history
  - 000471-history
  - 000471-terms
  - 000471-references
  - 000471-reference-measurement
  summary: Actual source/candidate/application receipts, the native inline event,
    one native EDIT sidecar and all ten scoped checks bind the exact current identity
    intermediate. Original terms, mapping states, snippets, functional roles, graph
    and older history are preserved. Mapping, composite historical admission, generated
    products and aggregate QC remain separate.
findings:
- finding_id: 000471-incomplete-roster
  issue_key: communitymech-2898
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Full M/Y13 membership and stock establishment remain unresolved
  description: The source describes four named partner taxa plus seven isolated degraders
    for M; the five retained descriptors are incomplete. Y13 is a distinct sediment
    enrichment. Full TableS1 stock representation and strain-specific revival/endpoint
    establishment are not established by this correction.
  target_ids:
  - CommunityMech:000471
  field_paths:
  - taxonomy
  - discussions[0]
  evidence_ids:
  - 000471-primary
  - 000471-plan
  ownership_note: CommunityMech owns the record taxonomy and open membership discussion;
    source-specific roster work remains under2898.
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/2898
- finding_id: 000471-retained-graph-limits
  issue_key: communitymech-2899
  category: graph
  severity: major
  status: open
  certainty: confirmed
  title: Existing mechanistic graph remains outside identity approval
  description: The three nodes and two arrows are preserved; the separate pceA acquisition,
    syntrophy and methane causal claims remain open under2899. Matching source snippets
    or technical gate success does not resolve those interpretation gaps.
  target_ids:
  - CommunityMech:000471
  field_paths:
  - ecological_interactions
  evidence_ids:
  - 000471-prior
  - 000471-plan
  - 000471-measured-source
  ownership_note: CommunityMech owns the existing ecological_interactions; the separate
    scientific interpretation issue2899 is retained.
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/2899
actions:
- action_id: 000471-resolve-membership
  description: Resolve the separate M and Y13 membership boundary against full primary
    stock evidence before claiming a complete participant roster or endpoint stock
    establishment.
  finding_ids:
  - 000471-incomplete-roster
  target_ids:
  - CommunityMech:000471
  ownership_note: CommunityMech owns the maintained taxonomy and discussion; issue2898
    remains open. This action is proposed, not completed by the identity intermediate.
  acceptance_checks:
  - Identify all intended M stocks from the primary supplementary roster with source
    locators, preserving separate Y13 enrichment scope.
  - Keep inoculated membership, observed revival and endpoint colonization distinct;
    add no unsupported stock accession or strain equivalence.
- action_id: 000471-reassess-graph
  description: Resolve the existing graph interpretation findings through a separate
    source-backed scientific assessment and bounded correction if justified.
  finding_ids:
  - 000471-retained-graph-limits
  target_ids:
  - CommunityMech:000471
  ownership_note: CommunityMech owns ecological_interactions; issue2899 retains the
    separate causal-scope work. Existing graph bytes are preserved by this intermediate.
  acceptance_checks:
  - Reassess each pceA acquisition, syntrophy and methane causal claim against the
    relevant experimental or metagenomic evidence.
  - Retain direct observations while qualifying or removing unsupported causal relations;
    preserve immutable previous reviews and append actual correction history.
limitations:
- This completed declared-scope assessment has partial coverage and scientific_review:false.
  It is not a full scientific review or approval of the complete record.
- The source is the retained PMID42663479 cache with SHA489eb292. No new paper acquisition,
  full supplementary roster reconstruction, sequence classification, figure inspection
  or exhaustive causal re-review occurred.
- The actual M5 intermediate ran on frozen af80bc0970b2b495b16c2c5c237cdfbbaa771ce8
  with Python3.13.2 and current recordb3234d5f. The record differs from HEAD; the
  measurement explicitly binds those working bytes rather than calling them a clean
  committed input.
- Eight native gates include seven validators and one history scaffold. Separate validate-references-explained
  and instrumented native comparison passed;16 matching snippets certify lexical comparison
  only. No zero-issue-to-coverage inference is used.
- The first reference attempt failed before validation because the recorder supplied
  JUST_NO_DOTENV=1 to nested Just. Issue2908 retains that exit2; the successful second
  invocation explicitly supplies true without changing the recorder. The stale Discussion-coverage
  footer is recorded under476 and preserved in the raw log.
- GTDB descriptors, functional roles, existing snippets, three nodes, two arrows and
  prior history are unchanged. The full roster and stock-establishment concern2898
  and mechanistic concern2899 remain open. No scientific approval or closure is inferred
  from this identity correction.
- A subsequent GTDB mapping transition must bind this exact intermediate and its immutable
  source/checkpoint evidence. Strict composite historical admission, generated HTML,
  combined technical QC and broader campaign completion remain pending.
- Unexecuted authored config001 had a passing verdict and no proposed actions despite
  retaining open major findings. Issue2911 records that native-contract inconsistency.
  Config002 corrected the verdict and actions; config003 preserves those corrections.
  No valid saved review was produced with001 or002.
- The measurement receipt inventories all runtime cache files. The builder verifies
  that complete inventory before and after preparation, while native review inputs
  archive the exact article cache actually loaded by all16 assertions plus schema,
  configuration, implementation and proof inputs. Unrelated cache bytes are not individually
  archived or scientifically assessed; their observed hashes remain in the exact measurement
  receipt. Issue2912 retains the first builder refusal caused by an unrelated legacy
  cache filename, with no review saved or source cache renamed.
links:
- https://github.com/CultureBotAI/CommunityMech/issues/2898
- https://github.com/CultureBotAI/CommunityMech/issues/2899
- https://github.com/CultureBotAI/CommunityMech/issues/2908
- https://github.com/CultureBotAI/CommunityMech/issues/2910
- https://github.com/CultureBotAI/CommunityMech/issues/2911
- https://github.com/CultureBotAI/CommunityMech/issues/2912
- https://github.com/CultureBotAI/CommunityMech/issues/476
- https://github.com/CultureBotAI/CommunityMech/pull/2906
review_id: 20261115T133312Z-wetland471-identity-intermediate
started_at: '2026-11-15T13:33:12.095514Z'
finished_at: '2026-11-15T13:33:12.272811Z'
source:
  git_revision: af80bc0970b2b495b16c2c5c237cdfbbaa771ce8
  state: working_tree
  inputs:
  - path: .temp/gtdb-wetland-identity-20261115/471-domain-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-wetland-identity-20261115/471-domain-001/native.log
    sha256: 83dcd8c4a53a637b90f32d89d1737924b96aed292aee925cb27b5e702a89d9e6
    role: context
  - path: .temp/gtdb-wetland-identity-20261115/471-domain-001/receipt.json
    sha256: 31811d193126d45ac63f5d33598bb0868245ae8571cd3b868ff923d66649a6b8
    role: context
  - path: .temp/gtdb-wetland-identity-20261115/471-domain-001/start.json
    sha256: ed639d9b442d68d28e15371a09d9b611b508094eb3ea06591d2fa51cdddd91dc
    role: context
  - path: .temp/gtdb-wetland-identity-20261115/471-gtdb-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-wetland-identity-20261115/471-gtdb-001/native.log
    sha256: 7c9d3904dc0544aef6c19299dad83daf4b4570f9eb6061f2236e46655077e2dd
    role: context
  - path: .temp/gtdb-wetland-identity-20261115/471-gtdb-001/receipt.json
    sha256: 3c89aad109a8de56e7cc128d9c3e07db1fa0b4c66ccf0c1eca1dd9ca00ddf68a
    role: context
  - path: .temp/gtdb-wetland-identity-20261115/471-gtdb-001/start.json
    sha256: 55f2013b1161c5d740b93f976759edf725cc0dcb3fcd6ed8489fe7b2ac55362a
    role: context
  - path: .temp/gtdb-wetland-identity-20261115/471-history-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-wetland-identity-20261115/471-history-001/native.log
    sha256: 700b44227c4cf01270ac26f16b308622de0b26f48d71aec49cdfaaab87620f0a
    role: context
  - path: .temp/gtdb-wetland-identity-20261115/471-history-001/receipt.json
    sha256: a3d1c3f8a8db964473eee1d54e5c6c430d3980eb3d61f6b568cc6238dcb1af89
    role: context
  - path: .temp/gtdb-wetland-identity-20261115/471-history-001/start.json
    sha256: 06ab5fbdf6cd3eafb23daa56b481d45265cb2fe58eed9d573da5f3a88c6d655d
    role: context
  - path: .temp/gtdb-wetland-identity-20261115/471-new-history-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-wetland-identity-20261115/471-new-history-001/native.log
    sha256: f8f86fdc8adb7d8e71ceb8acee5a1d03d9b67e9b868e39da1553ac4b62eb174a
    role: context
  - path: .temp/gtdb-wetland-identity-20261115/471-new-history-001/receipt.json
    sha256: 2bd23ec82056a3de919675f6443e9020b91dd0b03fabe962e24e4e297ac3bf26
    role: context
  - path: .temp/gtdb-wetland-identity-20261115/471-new-history-001/start.json
    sha256: 612cbafaefcc62b0850e797e11253b2e17ce361d613267d124c7ef030a47b9bd
    role: context
  - path: .temp/gtdb-wetland-identity-20261115/471-scalars-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-wetland-identity-20261115/471-scalars-001/native.log
    sha256: 075b540d0388653f0c7dff2facce2cf615d24487a37cf3493a976da996a07678
    role: context
  - path: .temp/gtdb-wetland-identity-20261115/471-scalars-001/receipt.json
    sha256: 9522c7ceae05a1a77f32d75218c105c607fb8db0aa23f4d4b282177f19c6db9d
    role: context
  - path: .temp/gtdb-wetland-identity-20261115/471-scalars-001/start.json
    sha256: c6b972e71cb4bb05c5ad4bb0dc75e040592cbc68c66a3248d1a96ea80600ae51
    role: context
  - path: .temp/gtdb-wetland-identity-20261115/471-schema-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-wetland-identity-20261115/471-schema-001/native.log
    sha256: 250d0efbaadcd9d645a4e1a3b00076dd8dd2db8bcfcac754ecd71d2f9a2c892f
    role: context
  - path: .temp/gtdb-wetland-identity-20261115/471-schema-001/receipt.json
    sha256: 90f1c961d6157c49e625ac9488729b6696856ab25a83c53dc0ad606c7b0ac253
    role: context
  - path: .temp/gtdb-wetland-identity-20261115/471-schema-001/start.json
    sha256: 92a012cd61a268227e3c49ccb3beadd299e24f7ace7e942fa96f9a2b5150b737
    role: context
  - path: .temp/gtdb-wetland-identity-20261115/471-strict-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-wetland-identity-20261115/471-strict-001/native.log
    sha256: d06d07f42910c064a3ac5d5ce1438d3c5cc0838fc27af118f456660fd8207538
    role: context
  - path: .temp/gtdb-wetland-identity-20261115/471-strict-001/receipt.json
    sha256: 39508e32cd6820e89ca1da0743c20fa3c651f055100e9a7bf55c4499a502139b
    role: context
  - path: .temp/gtdb-wetland-identity-20261115/471-strict-001/start.json
    sha256: de94f2495ff3ad5a3ac4a10e725928d3171e70bb8974234512646b8574a31432
    role: context
  - path: .temp/gtdb-wetland-identity-20261115/471-strict-001/strict.tsv
    sha256: b184ed5450b968070bb6c75648407e388f41a1eaf7017890723cf560999fc3f7
    role: context
  - path: .temp/gtdb-wetland-identity-20261115/471-terms-001/native.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/gtdb-wetland-identity-20261115/471-terms-001/native.log
    sha256: 9df744ace42d528488e87b902b0ec8e05cd756140b6335e4e12ebe6531cf3cd1
    role: context
  - path: .temp/gtdb-wetland-identity-20261115/471-terms-001/receipt.json
    sha256: 791f6d4138f9ebe047f9d3287e6bdaf844fad12fb51a9393d48e23353346367a
    role: context
  - path: .temp/gtdb-wetland-identity-20261115/471-terms-001/start.json
    sha256: b37d7d7ebb96ed6850d27517af605ec3379829e00af956801497c0212301dcbe
    role: context
  - path: .temp/gtdb-wetland-identity-20261115/m5-applied-001/before.yaml
    sha256: 2191214bbc8d7f8bb6341c6493344e2180eb63fe2098375f44aab9f49d35d199
    role: context
  - path: .temp/gtdb-wetland-identity-20261115/m5-applied-001/receipt.json
    sha256: 925eca0a9cca146eaf656b425061f8abe31153fc5841a5ca11601dacc43b1441
    role: context
  - path: .temp/gtdb-wetland-identity-20261115/m5-candidate-001/Wetland_Lindane_Degrading_Organochlorine_Consortium.yaml
    sha256: b3234d5f041636195f4c9867aaccd0df802d22ff5f2fbc28b904868ee02b901a
    role: context
  - path: .temp/gtdb-wetland-identity-20261115/m5-candidate-001/receipt.json
    sha256: bfee943e9086f0bcd47876dcf8ad0c4d1deb372162f270f5ea87c530f556c6e9
    role: context
  - path: .temp/gtdb-wetland-identity-20261115/reference-measurement-001/measurement.json
    sha256: 67e3eb1c897816c9addac3e6ed965be2ceaa9d7d02c0c6d00bd983b0b4e27bd2
    role: context
  - path: .temp/gtdb-wetland-identity-20261115/reference-measurement-001/measurement.log
    sha256: ef58fa96a6a506e9b817abd2b69362aeecf6ce0e4b3510e9976d4c75f7048487
    role: context
  - path: .temp/gtdb-wetland-identity-20261115/reference-measurement-001/receipt.json
    sha256: b732bce00d977fc12ac3a3e4fdbb854a4ae47b311e12726380176e87ac5d84f7
    role: context
  - path: .temp/gtdb-wetland-identity-20261115/reference-measurement-001/started.json
    sha256: 32c5b6c9c8ff592cdfeb9a5b666851274670d79240df4bf6137e342ca8eed5d2
    role: context
  - path: .temp/phase2-schema-20261115/wetland-m5-identity-review-build-001.exit
    sha256: 4355a46b19d348dc2f57c046f8ef63d4538ebb936000f3c9ee954a27460dd865
    role: context
  - path: .temp/phase2-schema-20261115/wetland-m5-identity-review-build-001.json
    sha256: 144e202e0b389225de62ba79f08b99bbc65d8b02e78e7f851db0bad082938a05
    role: context
  - path: .temp/phase2-schema-20261115/wetland-m5-identity-review-build-001.log
    sha256: b67ab885e578e0ed6ae68c31aa8662a1720481bc3dbae8c6dfb284efbe83b238
    role: context
  - path: .temp/phase2-schema-20261115/wetland-m5-measurement-001.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/phase2-schema-20261115/wetland-m5-measurement-001.json
    sha256: 8f3894f6ae157ccabef00697e50c0b4778c498c86d7f3f1beee3d9902db4dec9
    role: context
  - path: .temp/phase2-schema-20261115/wetland-m5-measurement-001.log
    sha256: b732bce00d977fc12ac3a3e4fdbb854a4ae47b311e12726380176e87ac5d84f7
    role: context
  - path: .temp/phase2-schema-20261115/wetland-m5-reference-after-001.log
    sha256: 8bc4d0efa137fe0d73585a7ee9fec266e379d98c82977b06b20bf1537dd0511f
    role: context
  - path: .temp/phase2-schema-20261115/wetland-m5-reference-before-001.log
    sha256: 8bc4d0efa137fe0d73585a7ee9fec266e379d98c82977b06b20bf1537dd0511f
    role: context
  - path: .temp/phase2-schema-20261115/wetland-m5-references-001.exit
    sha256: 53c234e5e8472b6ac51c1ae1cab3fe06fad053beb8ebfd8977b010655bfdd3c3
    role: context
  - path: .temp/phase2-schema-20261115/wetland-m5-references-001.json
    sha256: 961b81192807d2961dca8b550cf29ddb24ef892ffe56d27f3d49fb62b8237085
    role: context
  - path: .temp/phase2-schema-20261115/wetland-m5-references-001.log
    sha256: 84e83057f39bf9638dfa4026cb94cfa842a8f27979a6266c1075b5319a3ffc5c
    role: context
  - path: .temp/phase2-schema-20261115/wetland-m5-references-002.exit
    sha256: 9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    role: context
  - path: .temp/phase2-schema-20261115/wetland-m5-references-002.json
    sha256: 29134d0ddb35a879722709b0200eea60d3ceedd6029325a4b5c5936e47487122
    role: context
  - path: .temp/phase2-schema-20261115/wetland-m5-references-002.log
    sha256: 149d3c750fdf1423612ad0be1e63bc37a351a593cd8f9e1fac0e4f27350bb1ac
    role: context
  - path: .venv/lib/python3.13/site-packages/linkml/validator/validator.py
    sha256: 71471409f9f796ab0e886ff98cbeb4099284958d3a0d62eb762e51421077a44e
    role: context
  - path: .venv/lib/python3.13/site-packages/linkml_reference_validator/etl/reference_fetcher.py
    sha256: acf0861d3c79594c7daf39886e60f78ad772224ecd231475d8b195d0ba218426
    role: context
  - path: .venv/lib/python3.13/site-packages/linkml_reference_validator/plugins/reference_validation_plugin.py
    sha256: 533e677f42fe81381d3227da1cc93d04d3866e992e397464a8b703379eb92160
    role: context
  - path: .venv/lib/python3.13/site-packages/linkml_reference_validator/validation/supporting_text_validator.py
    sha256: 52473b443f3ad8d674457a59bf02b233f1263a09bcdb0d5957cda0dc782978da
    role: context
  - path: conf/reference_validator.yaml
    sha256: 297b1fbd8a77ba2f89ca7126339deabc0f61ee91013d054d0fa64caef59a630d
    role: context
  - path: history/records/Wetland_Lindane_Degrading_Organochlorine_Consortium/2026-10-19T053000Z-antigravity-6b00.yaml
    sha256: 43c35fa05a604ba3d69e0a9a73df2c34fd8ffe72369756e8dbf1cea874ebdf8d
    role: context
  - path: history/records/Wetland_Lindane_Degrading_Organochlorine_Consortium/2026-10-20T041800Z-antigravity-219121.yaml
    sha256: 760aed2beb2940d659abd157b38fa38bb6f63384e287c898ce130721303fd5e2
    role: context
  - path: history/records/Wetland_Lindane_Degrading_Organochlorine_Consortium/2026-11-15T131301Z-codex-0335f1.yaml
    sha256: 1f593c325e7cdb9b0c81b84da0e8b16cd23f29a5b3b8e5fb0fa97d59e3d2db9a
    role: context
  - path: justfile
    sha256: 40369611ad4531582e420df0e9ff22109e4b18adf03b34d86b54200b280f2d0f
    role: context
  - path: kb/communities/Wetland_Lindane_Degrading_Organochlorine_Consortium.yaml
    sha256: b3234d5f041636195f4c9867aaccd0df802d22ff5f2fbc28b904868ee02b901a
    role: target
  - path: pyproject.toml
    sha256: be952f0f137f85fed66bda0908f12014f1797a2dd229b44d832afc0c00471655
    role: context
  - path: references_cache/PMID_42663479.txt
    sha256: 489eb292cd49275ee0d480727b215360c2101e577aae884a4f52ff68fb7990eb
    role: context
  - path: reports/causal_graph_review/decisions/20261020-stage2-fifteen-records-batch133.yaml
    sha256: e9ded35a2333f9994869573f9f952b3af3191ab55528813a7f2c03639a362d3f
    role: context
  - path: reports/gtdb-wetland-identity-20261115/471-identity-check-config-001.json
    sha256: 411c6be33527c0e80376e8fdec3b4bdda9d440bbf0a73c28d9a5fb7385c6b7fd
    role: context
  - path: reports/gtdb-wetland-identity-20261115/471-identity-plan-001.json
    sha256: 24250d0cbdc94c4873183da81931e1f6a87afad621d1d76f471914bf567240e0
    role: context
  - path: reports/gtdb-wetland-identity-20261115/471-identity-review-config-003.json
    sha256: 576784879bd4de5fb83847290930a49c8937b67ccf5ab283d5ad346a42603d8c
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/adhoc/build_gtdb_batch_diagnostic_20261115.py
    sha256: c6bf0d09dc3d01797ab5d956a4f7458a9a153a8704508f50e656729e4ee1b860
    role: context
  - path: scripts/adhoc/build_wetland_identity_diagnostic_20261115.py
    sha256: 85d2c73ff15c08f39bd993d5a3f673bde50d49b5ddc9c0db6e400432a0711c89
    role: context
  - path: scripts/adhoc/check_gtdb_batch_unit_20261115.py
    sha256: 723047d1ec66fa752d6cedddbb6d399b18fa7f5b7a0e27fc435c76abfeb10493
    role: context
  - path: scripts/adhoc/check_wetland_identity_unit_20261115.py
    sha256: 758352347b625868fa3b4537de0147998f933331d43b60f16a80a9acc151cff1
    role: context
  - path: scripts/adhoc/curate_gtdb_source_notes_20261115.py
    sha256: 77ff86d185c6b04634c1bd83531463e42e5ece9f116873bf1d81c7af1de80380
    role: context
  - path: scripts/adhoc/curate_wetland_identity_20261115.py
    sha256: eb5a8670b9d99fc5528fecfd5b9105e7fd7427f4d48907ca7cab386de045c1af
    role: context
  - path: scripts/adhoc/measure_wetland_identity_references_20261115.py
    sha256: c01da3e40abb7e98ed809024f689a5f2daa96ba2bbc93d7612bce2f47d66c7de
    role: context
  - path: scripts/adhoc/prepare_wetland_identity_plan_20261115.py
    sha256: 42b4197f9cb91d42922a2d4d1f4939507ccc4443ecdf735933ff8a4f35b78cdc
    role: context
  - path: scripts/annotate_reference_errors.py
    sha256: 5bd5b6dd088714faed97c41230eee0f2268c7e1e1dc205dd5c04b560b51616ec
    role: context
  - path: scripts/normalize_cache_names.py
    sha256: d87b5d001c1dac3f213637523651fd87b71a54806b1114c83f5fb0ea3528ef5e
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/reference_assertion_coverage.py
    sha256: 363cffb652bdd18733cd5c8c2d22abf663cb3314410ef237e531a8b2f3298908
    role: context
  - path: src/communitymech/curate/curation_event.py
    sha256: 58ebdb58ac39d7a319156ec735db9ef2e9afb4c7350613039ad9dc49d65a5afc
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
  - path: tests/test_causal_review_batch133.py
    sha256: 60c10cf5de2737339efcd732818538e1cab80a44c939c84e46ef840dcbe2d40f
    role: context
  - path: uv.lock
    sha256: 712838f8fa3d68fbd818ac8162f3f1e2f2637db1da1a8ebfaba0ef759690f3b4
    role: context
checks:
- check_id: 000471-schema
  name: schema
  status: passed
  required: true
  summary: Actual scoped native command passed on the exact identity-corrected intermediate
    with unchanged captured inputs.
  target_ids:
  - CommunityMech:000471
  command: just --verbose --no-dotenv --color never validate kb/communities/Wetland_Lindane_Degrading_Organochlorine_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000471-schema
  scope_note: Bounded identity intermediate; not full scientific approval or corpus
    QC.
- check_id: 000471-strict
  name: strict
  status: passed
  required: true
  summary: Actual scoped native command passed on the exact identity-corrected intermediate
    with unchanged captured inputs.
  target_ids:
  - CommunityMech:000471
  command: just --verbose --no-dotenv --color never validate-strict kb/communities/Wetland_Lindane_Degrading_Organochlorine_Consortium.yaml
    --out .temp/gtdb-wetland-identity-20261115/471-strict-001/strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000471-strict
  scope_note: Bounded identity intermediate; not full scientific approval or corpus
    QC.
- check_id: 000471-gtdb
  name: gtdb
  status: passed
  required: true
  summary: Actual scoped native command passed on the exact identity-corrected intermediate
    with unchanged captured inputs.
  target_ids:
  - CommunityMech:000471
  command: just --verbose --no-dotenv --color never validate-gtdb kb/communities/Wetland_Lindane_Degrading_Organochlorine_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000471-gtdb
  scope_note: Bounded identity intermediate; not full scientific approval or corpus
    QC.
- check_id: 000471-domain
  name: domain
  status: passed
  required: true
  summary: Actual scoped native command passed on the exact identity-corrected intermediate
    with unchanged captured inputs.
  target_ids:
  - CommunityMech:000471
  command: just --verbose --no-dotenv --color never validate-gtdb-domain kb/communities/Wetland_Lindane_Degrading_Organochlorine_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000471-domain
  scope_note: Bounded identity intermediate; not full scientific approval or corpus
    QC.
- check_id: 000471-scalars
  name: scalars
  status: passed
  required: true
  summary: Actual scoped native command passed on the exact identity-corrected intermediate
    with unchanged captured inputs.
  target_ids:
  - CommunityMech:000471
  command: just --verbose --no-dotenv --color never validate-scalars kb/communities/Wetland_Lindane_Degrading_Organochlorine_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000471-scalars
  scope_note: Bounded identity intermediate; not full scientific approval or corpus
    QC.
- check_id: 000471-new-history
  name: new-history
  status: passed
  required: true
  summary: Actual scoped native command passed on the exact identity-corrected intermediate
    with unchanged captured inputs.
  target_ids:
  - CommunityMech:000471
  command: just --verbose --no-dotenv --color never new-history --kind record --slug
    Wetland_Lindane_Degrading_Organochlorine_Consortium --target-root kb/communities
    --event EDIT --outcome changed --sections description,taxonomy,discussions,curation_history
    --actor-name codex --model gpt-6 --agent-tool codex --issue https://github.com/CultureBotAI/CommunityMech/issues/2898
    --summary 'Correct Wetland consortium labels and Enterococcus stock identity while
    retaining roster and graph limitations.' --details 'The source Methods distinguish
    top-down enrichment Y13 from bottom-up consortium M. Four scalar corrections separate
    R12/E. casseliflavus from PseS3/E. avium and R1/R3/E. thailandicus, and distinguish
    sediment MAG bin436 from isolate R12. One open discussion retains six exact source
    quotations documenting treatment identity, incomplete membership and unverified
    stock-specific revival. The five original taxon terms, GTDB states, functional
    roles, existing source quotations, three interaction nodes, two arrows and earlier
    history are unchanged. This identity-only intermediate does not resolve full membership
    under issue2898 or the separate pceA, syntrophy and methane causal findings under
    issue2899. No new strain accession, study-genome placement, mechanism or scientific
    approval is inferred. A subsequent mapping transition must bind this actual corrected
    source-identity record. Actual apply receipt .temp/gtdb-wetland-identity-20261115/m5-applied-001/receipt.json
    sha256:925eca0a9cca146eaf656b425061f8abe31153fc5841a5ca11601dacc43b1441.'
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000471-new-history
  scope_note: Bounded identity intermediate; not full scientific approval or corpus
    QC.
- check_id: 000471-history
  name: history
  status: passed
  required: true
  summary: Actual scoped native command passed on the exact identity-corrected intermediate
    with unchanged captured inputs.
  target_ids:
  - CommunityMech:000471
  command: just --verbose --no-dotenv --color never validate-history history/records/Wetland_Lindane_Degrading_Organochlorine_Consortium
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000471-history
  scope_note: Bounded identity intermediate; not full scientific approval or corpus
    QC.
- check_id: 000471-terms
  name: terms
  status: passed
  required: true
  summary: Actual scoped native command passed on the exact identity-corrected intermediate
    with unchanged captured inputs.
  target_ids:
  - CommunityMech:000471
  command: just --verbose --no-dotenv --color never validate-terms kb/communities/Wetland_Lindane_Degrading_Organochlorine_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000471-terms
  scope_note: Bounded identity intermediate; not full scientific approval or corpus
    QC.
- check_id: 000471-references
  name: references
  status: passed
  required: true
  summary: Actual native validate-references-explained passed on the identity-corrected
    record with zero reported issues. The issue counter alone is not a comparison
    count; the separate measured check supplies actual coverage.
  target_ids:
  - CommunityMech:000471
  command: env JUST_NO_DOTENV=true just --verbose --no-dotenv --color never validate-references-explained
    kb/communities/Wetland_Lindane_Degrading_Organochlorine_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000471-references
  scope_note: Bounded identity intermediate; not full scientific approval or corpus
    QC.
- check_id: 000471-reference-measurement
  name: reference-measurement
  status: passed
  required: true
  summary: The unchanged maintained native collector/matcher compared all16 snippet
    surfaces, including all six newly added Discussion SupportingReference quotations;16
    matched and0 native issues were observed. This is lexical source matching, not
    verification of scientific interpretation.
  target_ids:
  - CommunityMech:000471
  command: .venv/bin/python scripts/adhoc/measure_wetland_identity_references_20261115.py
    --output .temp/gtdb-wetland-identity-20261115/reference-measurement-001
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - 000471-reference-measurement
  scope_note: Bounded identity intermediate; not full scientific approval or corpus
    QC.
```
