# MetG2 parent-only host and expression participants repaired

- Review: 20261015T044333Z-metg2-host-after
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-15T04:25:47.462501Z
- Finished UTC: 2026-10-15T04:43:33.798629Z
- Reviewer: codex (self_review)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Resolve unsupported host species precision and implicit cross-kingdom expression participants. Preserve three nodes, the qualified arrow and eight evidence occurrences. Exact inoculant membership, strain spelling, experimental host and aggregate attribution remain open under #1847.

## Scope And Provenance

Whole target read; scoped host identity and participants of two existing expression nodes assessed against abstract and taxonomy.

Selection: One record selected under existing #1847 from the 462-record corpus and 54 needs_research records.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 1fa2e2544c9bbc1d7678db33981cd38807038c31.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000302 | kb/communities/SynCom_MetG2_Rhizobacteria_Sugarcane_Stress_Resilience.yaml | maintained | MetG2 sugarcane rhizosphere |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| final-regression | passed | True | CommunityMech:000302 | ..........................................................               [100%]<br>=============================== warnings summary ===============================<br>.venv/lib/python3.13/site-packages/linkml/generators/pydanticgen/template.py:553: 12 warnings<br>  /private/tmp/communitymech-causal-20261014/.venv/lib/python3.13/site-packages/linkml/generators/pydanticgen/template.py:553: PydanticDeprecatedSince211: Accessing the 'model_fields' attribute on the instance is deprecated. Instead, you should access this attribute from the model class. Deprecated in Pydantic V2.11 to be removed in V3.0.<br>    imports=imports, **{k: getattr(self, k, None) for k in self.model_fields if k != "imports"}<br><br>-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html<br>58 passed, 12 warnings in 48.19s |
| connectivity-check | passed | True | CommunityMech:000302 | ......                                                                   [100%]<br>6 passed in 42.01s |
| validate | passed | True | CommunityMech:000302 | No issues found |
| strict | passed | True | CommunityMech:000302 | Passed; exact command output retained in receipt. |
| terms | passed | True | CommunityMech:000302 | ✅ Validation passed |
| gtdb | passed | True | CommunityMech:000302 | Passed; exact command output retained in receipt. |
| gtdb-domain | passed | True | CommunityMech:000302 | files checked: 1<br>contradictory lineages: 0 |
| references | passed | True | CommunityMech:000302 | Validating kb/communities/SynCom_MetG2_Rhizobacteria_Sugarcane_Stress_Resilience.yaml against schema src/communitymech/schema/communitymech.yaml<br>Cache directory: references_cache<br><br>Validation Summary:<br>  Reported validation issues: 0<br>  All validations passed!<br><br>[annotate] This is not a count of checked excerpts (#1469). Native Discussion evidence coverage remains incomplete (#476). |
| explicit-excerpts | passed | True | CommunityMech:000302 | Real native CLI traces six excerpts and returns 0/1/0 for control/fabricated graph snippet/restoration. Its two Discussion omissions remain #476; all eight are separately checked by the unmodified matcher with source-network lookup forbidden. Discussion mutation is rejected and restoration passes under the explicit check. |
| history | passed | True | CommunityMech:000302 | No issues found |
| rank | passed | True | CommunityMech:000302 | rank	score	path	id	name	taxonomy	connected_taxa	disconnected_taxa	ecological_interactions	downstream_edges	interaction_evidence	missing	dangling_downstream	self_downstream<br>1	80.0	kb/communities/SynCom_MetG2_Rhizobacteria_Sugarcane_Stress_Resilience.yaml	CommunityMech:000302	SynCom MetG2 Rhizobacteria Sugarcane Stress Resilience	2	2	0	3	1	4	additional_downstream,interaction_type	0	0 |
| inventory | passed | True | CommunityMech:000302 | {<br>  "scope": "Every YAML under kb/communities and data/isolates; filesystem discovery includes hidden/ignored files.",<br>  "semantic_review_rule": "Structural checks and readiness scores do not establish causal support. Completed reviews must match the current record SHA-256, cover every node once with a rationale, and reproduce the current edge list.",<br>  "records": 462,<br>  "nodes": 1383,<br>  "edges": 533,<br>  "records_without_nodes": 10,<br>  "records_without_edges": 190,<br>  "review_status_counts": {<br>    "needs_research": 54,<br>    "reviewed": 408<br>  },<br>  "structural_defects": []<br>} |
| preservation | passed | True | CommunityMech:000302 | {<br>  "changed_canonical_paths": [<br>    "kb/communities/SynCom_MetG2_Rhizobacteria_Sugarcane_Stress_Resilience.yaml"<br>  ],<br>  "unchanged_excerpt_occurrences": 8,<br>  "old_cache_schema_and_config_unchanged": true,<br>  "native_network_json_identical": true,<br>  "native_network_exit_code": 1,<br>  "network_severity_counts": {<br>    "warning": 57<br>  },<br>  "records": 462,<br>  "review_status_counts": {<br>    "needs_research": 54,<br>    "reviewed": 408<br>  },<br>  "structural_defects": []<br>} |
| gen-html | passed | True | CommunityMech:000302 | Contact_Consortium.html<br>  ✓ Wolffia_Mankai_Endosphere_Cobamide_Guild.yaml → /private/tmp/communitymech-causal-20261014/docs/communities/Wolffia_Mankai_Endosphere_Cobamide_Guild.html<br>  ✓ Wollastonite_Ramichloridium_Talaromyces_Fungal_Consortium.yaml → /private/tmp/communitymech-causal-20261014/docs/communities/Wollastonite_Ramichloridium_Talaromyces_Fungal_Consortium.html<br>  ✓ Yarrowia_lipolytica_Division_of_Labor_Lipid_Consortium.yaml → /private/tmp/communitymech-causal-20261014/docs/communities/Yarrowia_lipolytica_Division_of_Labor_Lipid_Consortium.html<br>  ✓ Yogurt_TwoSpecies_Starter_Culture.yaml → /private/tmp/communitymech-causal-20261014/docs/communities/Yogurt_TwoSpecies_Starter_Culture.html<br>  ✓ Zymomonas_Ecoli_Exometabolomics_Obligate_Mutualism.yaml → /private/tmp/communitymech-causal-20261014/docs/communities/Zymomonas_Ecoli_Exometabolomics_Obligate_Mutualism.html<br>  ✓ hCom2_Complex_Gut_Microbiome.yaml → /private/tmp/communitymech-causal-20261014/docs/communities/hCom2_Complex_Gut_Microbiome.html<br>  ✓ mCAFEs_Brachypodium_RCC.yaml → /private/tmp/communitymech-causal-20261014/docs/communities/mCAFEs_Brachypodium_RCC.html<br><br>✅ Rendered 458 communities to /private/tmp/communitymech-causal-20261014/docs/communities<br>  ✓ Generated browser at /private/tmp/communitymech-causal-20261014/docs/browser.html<br>  ✓ Generated landing at /private/tmp/communitymech-causal-20261014/docs/index.html |
| docs-current | passed | True | CommunityMech:000302 | <br>  ✓ Wolffia_Mankai_Endosphere_Cobamide_Guild.yaml → /private/tmp/communitymech-causal-20261014/docs/communities/Wolffia_Mankai_Endosphere_Cobamide_Guild.html<br>  ✓ Wollastonite_Ramichloridium_Talaromyces_Fungal_Consortium.yaml → /private/tmp/communitymech-causal-20261014/docs/communities/Wollastonite_Ramichloridium_Talaromyces_Fungal_Consortium.html<br>  ✓ Yarrowia_lipolytica_Division_of_Labor_Lipid_Consortium.yaml → /private/tmp/communitymech-causal-20261014/docs/communities/Yarrowia_lipolytica_Division_of_Labor_Lipid_Consortium.html<br>  ✓ Yogurt_TwoSpecies_Starter_Culture.yaml → /private/tmp/communitymech-causal-20261014/docs/communities/Yogurt_TwoSpecies_Starter_Culture.html<br>  ✓ Zymomonas_Ecoli_Exometabolomics_Obligate_Mutualism.yaml → /private/tmp/communitymech-causal-20261014/docs/communities/Zymomonas_Ecoli_Exometabolomics_Obligate_Mutualism.html<br>  ✓ hCom2_Complex_Gut_Microbiome.yaml → /private/tmp/communitymech-causal-20261014/docs/communities/hCom2_Complex_Gut_Microbiome.html<br>  ✓ mCAFEs_Brachypodium_RCC.yaml → /private/tmp/communitymech-causal-20261014/docs/communities/mCAFEs_Brachypodium_RCC.html<br><br>✅ Rendered 458 communities to /private/tmp/communitymech-causal-20261014/docs/communities<br>  ✓ Generated browser at /private/tmp/communitymech-causal-20261014/docs/browser.html<br>  ✓ Generated landing at /private/tmp/communitymech-causal-20261014/docs/index.html<br>✅ docs/ matches the KB |
| lint-final | passed | True | CommunityMech:000302 | All checks passed!<br>Success: no issues found in 49 source files |
| diff-check-final | passed | True | CommunityMech:000302 | Passed; exact command output retained in receipt. |
| review-contract-before | passed | True | CommunityMech:000302 | {<br>  "repository": "culturebotai/CommunityMech",<br>  "valid_reviews": 27,<br>  "coverage": "declared_scopes_only"<br>} |
| Native zero-warning network diagnostic | failed | False | CommunityMech:000302 | Native exit 1 for an exactly baseline-identical warning set; preservation check verifies no structural errors. This is not a zero-warning pass. |
| Complete experimental identity verification | unavailable | True | CommunityMech:000302 | Complete Methods, experimental cultivar and conflicting strain spelling remain unverified; #1847 stays open. |
| Protected PR and merge-queue gates | unavailable | True | CommunityMech:000302 | Pending at this immutable local review snapshot; subsequent remote receipts must establish completion before merge. |

## Scientific And Domain Assessments

### Host rank and response attribution

grounding: supported. Targets: CommunityMech:000302.

The explicit parent-only genus anchor removes false species precision. Named participants distinguish host expression from bacterial colonization-associated expression, with native auditor mutation/restoration tests.

### Unresolved experimental identity

completeness: concern. Targets: CommunityMech:000302.

Do not equate responding native taxa with the inoculant or silently resolve the conflicting strain spelling.

### Retained source-bounded graph and evidence

graph: supported. Targets: CommunityMech:000302.

All three nodes and the one HYPOTHESIZED/PARTIAL contribution remain; no measured stress-tolerance phenotype, temporal order, isolated mediation or new topology is asserted by this repair.

## Findings

### host-scope: Unsupported host species and implicit expression participants

major / resolved / confirmed; issue key: communitymech-1847-metg2-host-scope.

The species assignment exceeds the inspected host evidence; unspecified participants also credit bacteria with plant transcription and the plant with bacterial colonization-associated expression. Correct the parent-rank anchor and explicitly name participants without changing topology.

Disposition: Verified parent-only host grounding, two explicit participant lists, native schema/ontology gates and behavioral auditor tests; topology, all snippets and source cache preserved.

### membership: Exact MetG2 membership and host identity remain unresolved

major / open / confirmed; issue key: communitymech-1847-metg2-membership.

The responding phylum is not the defined inoculant; primary methods and conflicting strain designation still require reconciliation. A parent-only host anchor does not finish this identity work.

## Recommended Actions And Acceptance Checks

### resolve-membership

Retrieve primary experimental methods/member evidence and reconcile the inoculant, spelling conflict and exact host without attributing native-community observations to all inoculants.

- Exact source-backed inoculant roster and spelling disposition retained.
- Host experimental identity and native-versus-inoculant graph attribution verified.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| abstract | doi:10.1016/j.rhisph.2025.101142; references_cache/doi_10.1016_j.rhisph.2025.101142.md: complete abstract; sugarcane host and separate microbial/host expression sentences | supports | The inspected abstract supports generic sugarcane and separates bacterial colonization-associated transcription from host hormone/nutrient-transporter transcription. It does not verify the experimental cultivar or species. |
| taxonomy | reports/causal_graph_review/sources/20261015-metg2-host/ncbi-taxonomy.xml; Taxa 4546 and 4547: names, ranks and lineage | supports | NCBI distinguishes Saccharum genus from S. officinarum species. The genus can provide an explicitly broader anchor, not an exact experimental identity. |
| limits | https://github.com/CultureBotAI/CommunityMech/issues/1847; Live issue body/comment and source manifest | context_only | Issue remains open for inoculant identity, Chiliseed2/Chileseed2 discrepancy and exact host. Bounded searches did not retrieve complete primary methods; search previews were not accepted as new membership evidence. |
| record | kb/communities/SynCom_MetG2_Rhizobacteria_Sugarcane_Stress_Resilience.yaml; taxonomy[0], ecological_interactions[0,2].participating_taxa and discussions[0] | supports | The study host is anchored to Saccharum with explicit species/cultivar uncertainty. Two existing expression nodes name their source-supported plant or responding-phylum participants. The aggregate functional node and the one hypothetical arrow remain unchanged. |
| ledger | reports/causal_graph_review/decisions/20261015-metg2-host.yaml; All three node decisions and retained arrow | supports | Hash-linked successor retains claim-level evidence, exact paths, participant boundaries, no topology extension and needs_research status. |
| final-regression | reports/causal_graph_review/20261015-metg2-host/final-regression-clean.json; Actual command, timestamps, input hashes, exit code and stdout/stderr | supports | Retained execution receipt for final-regression |
| connectivity-check | reports/causal_graph_review/20261015-metg2-host/connectivity-check.json; Actual command, timestamps, input hashes, exit code and stdout/stderr | supports | Retained execution receipt for connectivity-check |
| validate | reports/causal_graph_review/20261015-metg2-host/validate.json; Actual command, timestamps, input hashes, exit code and stdout/stderr | supports | Retained execution receipt for validate |
| strict | reports/causal_graph_review/20261015-metg2-host/strict.json; Actual command, timestamps, input hashes, exit code and stdout/stderr | supports | Retained execution receipt for strict |
| terms | reports/causal_graph_review/20261015-metg2-host/terms.json; Actual command, timestamps, input hashes, exit code and stdout/stderr | supports | Retained execution receipt for terms |
| gtdb | reports/causal_graph_review/20261015-metg2-host/gtdb.json; Actual command, timestamps, input hashes, exit code and stdout/stderr | supports | Retained execution receipt for gtdb |
| gtdb-domain | reports/causal_graph_review/20261015-metg2-host/gtdb-domain.json; Actual command, timestamps, input hashes, exit code and stdout/stderr | supports | Retained execution receipt for gtdb-domain |
| references | reports/causal_graph_review/20261015-metg2-host/references.json; Actual command, timestamps, input hashes, exit code and stdout/stderr | supports | Retained execution receipt for references |
| explicit-excerpts | reports/causal_graph_review/20261015-metg2-host/explicit-excerpts.json; Actual command, timestamps, input hashes, exit code and stdout/stderr | supports | Retained execution receipt for explicit-excerpts |
| history | reports/causal_graph_review/20261015-metg2-host/history.json; Actual command, timestamps, input hashes, exit code and stdout/stderr | supports | Retained execution receipt for history |
| rank | reports/causal_graph_review/20261015-metg2-host/rank.json; Actual command, timestamps, input hashes, exit code and stdout/stderr | supports | Retained execution receipt for rank |
| inventory | reports/causal_graph_review/20261015-metg2-host/inventory.json; Actual command, timestamps, input hashes, exit code and stdout/stderr | supports | Retained execution receipt for inventory |
| preservation | reports/causal_graph_review/20261015-metg2-host/preservation-final.json; Actual command, timestamps, input hashes, exit code and stdout/stderr | supports | Retained execution receipt for preservation |
| gen-html | reports/causal_graph_review/20261015-metg2-host/gen-html.json; Actual command, timestamps, input hashes, exit code and stdout/stderr | supports | Retained execution receipt for gen-html |
| docs-current | reports/causal_graph_review/20261015-metg2-host/docs-current.json; Actual command, timestamps, input hashes, exit code and stdout/stderr | supports | Retained execution receipt for docs-current |
| lint-final | reports/causal_graph_review/20261015-metg2-host/lint-final.json; Actual command, timestamps, input hashes, exit code and stdout/stderr | supports | Retained execution receipt for lint-final |
| diff-check-final | reports/causal_graph_review/20261015-metg2-host/diff-check-final.json; Actual command, timestamps, input hashes, exit code and stdout/stderr | supports | Retained execution receipt for diff-check-final |
| review-contract-before | reports/causal_graph_review/20261015-metg2-host/review-contract-before.json; Actual command, timestamps, input hashes, exit code and stdout/stderr | supports | Retained execution receipt for review-contract-before |

## Limits And Additional Notes

- Scoped partial scientific self-review, not independent approval, whole-record certification or corpus completion.
- No native whole-record completeness/quality score is assigned to this focused identity correction.
- No full methods, all figures/supplements, or raw experimental data inspected. Search previews are leads only.
- No new topology or paid provider submission; source caches and historical reviews remain unchanged.
- The aggregate functional-gene node remains unchanged; native/inoculant participant reconciliation is not complete.
- Reference CLI zero issues is not zero coverage: six native excerpt calls were traced; two Discussion excerpts needed explicit validation (#476). Lexical matching is not scientific proof.
- Initial post-repair tests exposed a mutation-harness KeyError and the new participant-census entry. Lint caught import ordering and the fixture XML annotation; the preservation helper initially used the wrong summary key. These were corrected and rerun; failed receipts remain intact. No schema, threshold, validator or source policy was weakened.
- The inventory remains 408 reviewed and 54 needs_research; no status was promoted by this scoped correction.
- Remote CI/queue completion remains pending at the immutable review snapshot.
- Post-repair observation at the exact committed inputs. The predecessor explicitly assesses the retained historical pre-fix tree.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T044333Z-metg2-host-after
kind: record
repository: CultureBotAI/CommunityMech
title: MetG2 parent-only host and expression participants repaired
started_at: '2026-10-15T04:25:47.462501Z'
finished_at: '2026-10-15T04:43:33.798629Z'
reviewer:
  identity: codex
  kind: agent
  independence: self_review
  independence_basis: Implementing-agent source-based review, not independent approval.
skill: communitymech-causal-graphs
completion: partial
verdict: needs_curation
scientific_review: true
source:
  git_revision: 1fa2e2544c9bbc1d7678db33981cd38807038c31
  state: git_commit
  inputs:
  - path: conf/record_review.yaml
    sha256: 8cbd8f9d209f78de47a8c35091e43bf1dadbe41ee07492c7860b6d4be30112a8
    role: context
  - path: docs/communities/SynCom_MetG2_Rhizobacteria_Sugarcane_Stress_Resilience.html
    sha256: 2fe5dada1ab994903dfa81c205ce8dc21ad3dc312fd91f357c8541ea6c3d2000
    role: context
  - path: docs/record-review-profile.md
    sha256: 285f79747999f83edbe63e5efde349a5cc063e9e486ce1a748b47b76c6631f31
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: history/records/SynCom_MetG2_Rhizobacteria_Sugarcane_Stress_Resilience/2026-10-15T043151Z-codex-18bb87.yaml
    sha256: e2cb497d1178156f9add4c364e6c11af2c88f8c9ac03f4a3c61c2f148d169197
    role: context
  - path: kb/communities/SynCom_MetG2_Rhizobacteria_Sugarcane_Stress_Resilience.yaml
    sha256: 75f43d8ae7e953f895bf8b2e13cd26de63c288cf9200c2476fd60750ba87afcd
    role: target
  - path: references_cache/doi_10.1016_j.rhisph.2025.101142.md
    sha256: 2651ef5f596a41fc8a30d3f77b706f806b9867e7aa5ff132911e396968be3c60
    role: context
  - path: reports/causal_graph_review/20261015-metg2-host/README.md
    sha256: 9500def09aed9c33dc786144a8479b9ebc348756656d2492ac1cc70817b2ccdf
    role: context
  - path: reports/causal_graph_review/20261015-metg2-host/after-regression.json
    sha256: 0031c9189bf372729a592b34e8be27254fb699048eb0db6196262b78924272c4
    role: context
  - path: reports/causal_graph_review/20261015-metg2-host/baseline-audit.json
    sha256: 4658e938edd1478ef7a96a55e17214c037b2560b695711b3ba987843809b5519
    role: context
  - path: reports/causal_graph_review/20261015-metg2-host/baseline-inventory.json
    sha256: 83d9fd39975d8df851f72c056928f94f88a2a6db251a2d6e652487ab84bcbf49
    role: context
  - path: reports/causal_graph_review/20261015-metg2-host/baseline-rank.json
    sha256: 59cca0dce736f7fe40e09f3644f7c26c36efc09d1f4d87313e8c5ba88456863d
    role: context
  - path: reports/causal_graph_review/20261015-metg2-host/before-regression.json
    sha256: 72bcb759110186ccc2d2a497972b7950d705b9b144adbbbae7e3aa10e6ccf724
    role: context
  - path: reports/causal_graph_review/20261015-metg2-host/check_preservation.py
    sha256: bf6ff8c150904b4a9a6c8b6bac023ca4b197614f117b8d3067c43f41d9d048d2
    role: context
  - path: reports/causal_graph_review/20261015-metg2-host/check_snippets.py
    sha256: a427eeb235eefd364ecf4b6a5e479639388ec800d4335c32f6246720d97b3b8d
    role: context
  - path: reports/causal_graph_review/20261015-metg2-host/connectivity-check.json
    sha256: 5970f70f5950630e87d21a469f6c46af522ccd7566cf11b1a5e16f01ba483934
    role: context
  - path: reports/causal_graph_review/20261015-metg2-host/diff-check-final.json
    sha256: 1a6ac7cef3a51ec990519c3b1cc64b0d44fb842af064a83f63627222e7087db7
    role: context
  - path: reports/causal_graph_review/20261015-metg2-host/diff-check.json
    sha256: 98fedd155d2f60680f2c8fba24179d946fb9b10dad7d5db3d2a56e5f84de056f
    role: context
  - path: reports/causal_graph_review/20261015-metg2-host/docs-current.json
    sha256: e142c4d6ff652f8aebfbb6e3d5a51061a5581cb95cd0cfb00a30f51c7f254d24
    role: context
  - path: reports/causal_graph_review/20261015-metg2-host/explicit-excerpts.json
    sha256: 0b3eeea5d671a510f833e2960635af923684835d8a6829456f401c2cc47b0850
    role: context
  - path: reports/causal_graph_review/20261015-metg2-host/final-regression-clean.json
    sha256: 3bcc041536149de7a2f4a54f1b2ff4a05cb9c63968018471aafed4ca7df647e3
    role: context
  - path: reports/causal_graph_review/20261015-metg2-host/final-regression.json
    sha256: e7f8db274014cede4485f909a42f6859234631b36b52850a519044f80fc4f8d3
    role: context
  - path: reports/causal_graph_review/20261015-metg2-host/gen-html.json
    sha256: 53a6d762174b7f1148f00b7c98587c9375ed72522238b1af42edfd4bf38e1705
    role: context
  - path: reports/causal_graph_review/20261015-metg2-host/gtdb-domain.json
    sha256: 9e6576c4a1bed9a5f4ecdcc1876569a1035e0d6d1f855dda05b2718a0ef47969
    role: context
  - path: reports/causal_graph_review/20261015-metg2-host/gtdb.json
    sha256: 66e0402768892d96b9bf1d87aea2443a8eb5f15bfd0ba05b86077c055467a7a8
    role: context
  - path: reports/causal_graph_review/20261015-metg2-host/guarded-repair.json
    sha256: 508731b513ba571f9f1384d80b61cef9d70f51b798d2c1c13abc3c5a092af454
    role: context
  - path: reports/causal_graph_review/20261015-metg2-host/history-create.json
    sha256: 08bb2f0c673834d6e049975645e7fe95b86965452243275bdec171dbef61a64d
    role: context
  - path: reports/causal_graph_review/20261015-metg2-host/history.json
    sha256: 28f985ee8bcbc020f076105ba3872c6dc9ef873fb154773b56a9a0740ef3aa13
    role: context
  - path: reports/causal_graph_review/20261015-metg2-host/inventory.json
    sha256: 740fb0aee258a6aa61638565b9d0ebf5c00b857789e4a77f58f9d4aca949d0bd
    role: context
  - path: reports/causal_graph_review/20261015-metg2-host/lint-final.json
    sha256: 70c6ee11c91be12cf65b00fee4a1438c7db0da105ff359a6eb882413f86c7110
    role: context
  - path: reports/causal_graph_review/20261015-metg2-host/lint.json
    sha256: 38ed26444bbc54763ac673c9f58e0932aa26a796eaa2be18f208cd90ffbbbf63
    role: context
  - path: reports/causal_graph_review/20261015-metg2-host/network.json
    sha256: a710bce09d60fa9c94315149233260f33ec72b95d7b280f0fc67f16598a5a1bd
    role: context
  - path: reports/causal_graph_review/20261015-metg2-host/preservation-final.json
    sha256: 8699f78613423abafbc644f2bf49fde7024450e0c88dc00ef3d13ea0fa1fd01e
    role: context
  - path: reports/causal_graph_review/20261015-metg2-host/preservation.json
    sha256: b74c6926f084a11a5d05c60de9867fd46fbe2f3cd9bb494d44a45afad33a0455
    role: context
  - path: reports/causal_graph_review/20261015-metg2-host/rank.json
    sha256: 4e9a77b0677adc6dc8e38ac31c82af817878035de48b86b62584c700a8b797f4
    role: context
  - path: reports/causal_graph_review/20261015-metg2-host/references.json
    sha256: 6383a227afe792899b5158d37799d98f05e9186a030535ba56cb58553d7c9418
    role: context
  - path: reports/causal_graph_review/20261015-metg2-host/review-contract-before.json
    sha256: f9b434d7867b77c69f07f4c14a3479c1b1e26d8d6e014d366866452a380d21ee
    role: context
  - path: reports/causal_graph_review/20261015-metg2-host/strict.json
    sha256: e13abdb076c391183bfea2c2b3660fd7fcab33a1595d80f54109a77754c0a7b0
    role: context
  - path: reports/causal_graph_review/20261015-metg2-host/terms.json
    sha256: 6af392b675c115cc554d2d466367b6a7dbc78193df0f6ea571d04e01e2398e2e
    role: context
  - path: reports/causal_graph_review/20261015-metg2-host/validate.json
    sha256: 1e9969a5b2696d2ee32823e8d07c6bdb2bd5aa6a044d77cac3b2221832f2c9d8
    role: context
  - path: reports/causal_graph_review/decisions/20261008-four-records-batch108.yaml
    sha256: 4004aaf9719161201cb0135d82c2f0ba2e7231ef9f7473ec99760465993bdaeb
    role: context
  - path: reports/causal_graph_review/decisions/20261015-metg2-host.yaml
    sha256: 368278d8b3c8e477772f9d07bb664b96a90a65161d98d31f8c83ca62068d3996
    role: context
  - path: reports/causal_graph_review/inventory.tsv
    sha256: 805ff8aa5fbb0cacd6c0449ec5198f553a9df3c88059b013dadece1153d6b4ce
    role: context
  - path: reports/causal_graph_review/sources/20261015-metg2-host/manifest.json
    sha256: 72902dae1b78c6b1b6eea6a325d682d819862cea05ecf7f772643e5e0f9478e2
    role: context
  - path: reports/causal_graph_review/sources/20261015-metg2-host/ncbi-taxonomy.xml
    sha256: 4d93c64556be377014f2deb493de13b74a43fd4a087b7479f106d1bb20bda2aa
    role: context
  - path: reports/causal_graph_review/summary.json
    sha256: d4e452ae6d6b3a8c12a77274e08723406b5c97fb702a4df58d15c1e547e92819
    role: context
  - path: reports/reference_cli_coverage/probe.py
    sha256: 8e3782125ca5f5b022ec94527993bebca3e9a74fe93dc9d52037678dd4c127bd
    role: context
  - path: reviews/structured/20261015T043154Z-metg2-host-before/review.md
    sha256: d3aef7ef436a8248e88795e4ef1e556a234df8cac8f04ee5c054cee430463347
    role: context
  - path: reviews/structured/20261015T043154Z-metg2-host-before/review.yaml
    sha256: e53a81f44e897acf895742ca592e7d7d395b158e75998eb6181abe74e75828d3
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: src/communitymech/network/auditor.py
    sha256: fe32aa2eddf9e09c153c47576f943bf08a6019f650bf2575e3ddc8e14675049b
    role: context
  - path: src/communitymech/schema/communitymech.yaml
    sha256: e5a87e5367609334ec0d6361f6ddafbe6bc4a1f7d93e5264c64688c28325910f
    role: context
  - path: tests/test_causal_review_batch108.py
    sha256: 9a7dacf3875cc526ed91956f25aae42893528db2c71bb3798f154b5c7c3674cd
    role: context
  - path: tests/test_community_level_connectivity_credit.py
    sha256: b3cdd10b1e214bc96f78ab74153f60d28338d37f4b068b22744def9019779e8e
    role: context
  - path: tests/test_metg2_host_scope.py
    sha256: 670c2c5e444f6a3b0c1dd6453d6028c384038b5f9936d31b3a6f28f7788b5386
    role: context
  - path: tests/test_participating_taxa.py
    sha256: f8a6ceab84987199e515f799317072ff0a3f520582f2382392f2705d9b5613ed
    role: context
  snapshot_id: review-provenance/20261015-metg2-host-after-inputs
targets:
- target_id: CommunityMech:000302
  path: kb/communities/SynCom_MetG2_Rhizobacteria_Sugarcane_Stress_Resilience.yaml
  label: MetG2 sugarcane rhizosphere
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/SynCom_MetG2_Rhizobacteria_Sugarcane_Stress_Resilience.yaml
    role: canonical host and graph participants
summary: 'Resolve unsupported host species precision and implicit cross-kingdom expression
  participants. Preserve three nodes, the qualified arrow and eight evidence occurrences.
  Exact inoculant membership, strain spelling, experimental host and aggregate attribution
  remain open under #1847.'
scope:
  description: Whole target read; scoped host identity and participants of two existing
    expression nodes assessed against abstract and taxonomy.
  selection: 'One record selected under existing #1847 from the 462-record corpus
    and 54 needs_research records.'
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000302
  exclusions:
  - target: Other 461 records and complete MetG2 source/strain reconciliation
    reason: Not newly certified; methods access remains incomplete.
checks:
- check_id: final-regression
  name: final-regression
  status: passed
  required: true
  summary: "..........................................................           \
    \    [100%]\n=============================== warnings summary ===============================\n\
    .venv/lib/python3.13/site-packages/linkml/generators/pydanticgen/template.py:553:\
    \ 12 warnings\n  /private/tmp/communitymech-causal-20261014/.venv/lib/python3.13/site-packages/linkml/generators/pydanticgen/template.py:553:\
    \ PydanticDeprecatedSince211: Accessing the 'model_fields' attribute on the instance\
    \ is deprecated. Instead, you should access this attribute from the model class.\
    \ Deprecated in Pydantic V2.11 to be removed in V3.0.\n    imports=imports, **{k:\
    \ getattr(self, k, None) for k in self.model_fields if k != \"imports\"}\n\n--\
    \ Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html\n58 passed,\
    \ 12 warnings in 48.19s"
  command: .venv/bin/python -m pytest tests/test_metg2_host_scope.py tests/test_causal_review_batch108.py
    tests/test_causal_review_inventory.py tests/test_participating_taxa.py --no-cov
    -q
  exit_code: 0
  target_ids:
  - CommunityMech:000302
  evidence_ids:
  - final-regression
- check_id: connectivity-check
  name: connectivity-check
  status: passed
  required: true
  summary: '......                                                                   [100%]

    6 passed in 42.01s'
  command: .venv/bin/python -m pytest tests/test_community_level_connectivity_credit.py
    --no-cov -q
  exit_code: 0
  target_ids:
  - CommunityMech:000302
  evidence_ids:
  - connectivity-check
- check_id: validate
  name: validate
  status: passed
  required: true
  summary: No issues found
  command: just --no-dotenv validate kb/communities/SynCom_MetG2_Rhizobacteria_Sugarcane_Stress_Resilience.yaml
  exit_code: 0
  target_ids:
  - CommunityMech:000302
  evidence_ids:
  - validate
- check_id: strict
  name: strict
  status: passed
  required: true
  summary: Passed; exact command output retained in receipt.
  command: just --no-dotenv validate-strict kb/communities/SynCom_MetG2_Rhizobacteria_Sugarcane_Stress_Resilience.yaml
  exit_code: 0
  target_ids:
  - CommunityMech:000302
  evidence_ids:
  - strict
- check_id: terms
  name: terms
  status: passed
  required: true
  summary: ✅ Validation passed
  command: just --no-dotenv validate-terms kb/communities/SynCom_MetG2_Rhizobacteria_Sugarcane_Stress_Resilience.yaml
  exit_code: 0
  target_ids:
  - CommunityMech:000302
  evidence_ids:
  - terms
- check_id: gtdb
  name: gtdb
  status: passed
  required: true
  summary: Passed; exact command output retained in receipt.
  command: just --no-dotenv validate-gtdb kb/communities/SynCom_MetG2_Rhizobacteria_Sugarcane_Stress_Resilience.yaml
  exit_code: 0
  target_ids:
  - CommunityMech:000302
  evidence_ids:
  - gtdb
- check_id: gtdb-domain
  name: gtdb-domain
  status: passed
  required: true
  summary: 'files checked: 1

    contradictory lineages: 0'
  command: just --no-dotenv validate-gtdb-domain kb/communities/SynCom_MetG2_Rhizobacteria_Sugarcane_Stress_Resilience.yaml
  exit_code: 0
  target_ids:
  - CommunityMech:000302
  evidence_ids:
  - gtdb-domain
- check_id: references
  name: references
  status: passed
  required: true
  summary: "Validating kb/communities/SynCom_MetG2_Rhizobacteria_Sugarcane_Stress_Resilience.yaml\
    \ against schema src/communitymech/schema/communitymech.yaml\nCache directory:\
    \ references_cache\n\nValidation Summary:\n  Reported validation issues: 0\n \
    \ All validations passed!\n\n[annotate] This is not a count of checked excerpts\
    \ (#1469). Native Discussion evidence coverage remains incomplete (#476)."
  command: just --no-dotenv validate-references-explained kb/communities/SynCom_MetG2_Rhizobacteria_Sugarcane_Stress_Resilience.yaml
  exit_code: 0
  target_ids:
  - CommunityMech:000302
  evidence_ids:
  - references
- check_id: explicit-excerpts
  name: explicit-excerpts
  status: passed
  required: true
  summary: 'Real native CLI traces six excerpts and returns 0/1/0 for control/fabricated
    graph snippet/restoration. Its two Discussion omissions remain #476; all eight
    are separately checked by the unmodified matcher with source-network lookup forbidden.
    Discussion mutation is rejected and restoration passes under the explicit check.'
  command: /private/tmp/communitymech-causal-20261014/.venv/bin/python reports/causal_graph_review/20261015-metg2-host/check_snippets.py
  exit_code: 0
  target_ids:
  - CommunityMech:000302
  evidence_ids:
  - explicit-excerpts
- check_id: history
  name: history
  status: passed
  required: true
  summary: No issues found
  command: just --no-dotenv validate-history history/records/SynCom_MetG2_Rhizobacteria_Sugarcane_Stress_Resilience
  exit_code: 0
  target_ids:
  - CommunityMech:000302
  evidence_ids:
  - history
- check_id: rank
  name: rank
  status: passed
  required: true
  summary: "rank\tscore\tpath\tid\tname\ttaxonomy\tconnected_taxa\tdisconnected_taxa\t\
    ecological_interactions\tdownstream_edges\tinteraction_evidence\tmissing\tdangling_downstream\t\
    self_downstream\n1\t80.0\tkb/communities/SynCom_MetG2_Rhizobacteria_Sugarcane_Stress_Resilience.yaml\t\
    CommunityMech:000302\tSynCom MetG2 Rhizobacteria Sugarcane Stress Resilience\t\
    2\t2\t0\t3\t1\t4\tadditional_downstream,interaction_type\t0\t0"
  command: just --no-dotenv rank-causal-graphs kb/communities/SynCom_MetG2_Rhizobacteria_Sugarcane_Stress_Resilience.yaml
  exit_code: 0
  target_ids:
  - CommunityMech:000302
  evidence_ids:
  - rank
- check_id: inventory
  name: inventory
  status: passed
  required: true
  summary: "{\n  \"scope\": \"Every YAML under kb/communities and data/isolates; filesystem\
    \ discovery includes hidden/ignored files.\",\n  \"semantic_review_rule\": \"\
    Structural checks and readiness scores do not establish causal support. Completed\
    \ reviews must match the current record SHA-256, cover every node once with a\
    \ rationale, and reproduce the current edge list.\",\n  \"records\": 462,\n  \"\
    nodes\": 1383,\n  \"edges\": 533,\n  \"records_without_nodes\": 10,\n  \"records_without_edges\"\
    : 190,\n  \"review_status_counts\": {\n    \"needs_research\": 54,\n    \"reviewed\"\
    : 408\n  },\n  \"structural_defects\": []\n}"
  command: /private/tmp/communitymech-causal-20261014/.venv/bin/python reports/causal_graph_review/build_inventory.py
  exit_code: 0
  target_ids:
  - CommunityMech:000302
  evidence_ids:
  - inventory
- check_id: preservation
  name: preservation
  status: passed
  required: true
  summary: "{\n  \"changed_canonical_paths\": [\n    \"kb/communities/SynCom_MetG2_Rhizobacteria_Sugarcane_Stress_Resilience.yaml\"\
    \n  ],\n  \"unchanged_excerpt_occurrences\": 8,\n  \"old_cache_schema_and_config_unchanged\"\
    : true,\n  \"native_network_json_identical\": true,\n  \"native_network_exit_code\"\
    : 1,\n  \"network_severity_counts\": {\n    \"warning\": 57\n  },\n  \"records\"\
    : 462,\n  \"review_status_counts\": {\n    \"needs_research\": 54,\n    \"reviewed\"\
    : 408\n  },\n  \"structural_defects\": []\n}"
  command: .venv/bin/python reports/causal_graph_review/20261015-metg2-host/check_preservation.py
  exit_code: 0
  target_ids:
  - CommunityMech:000302
  evidence_ids:
  - preservation
- check_id: gen-html
  name: gen-html
  status: passed
  required: true
  summary: "Contact_Consortium.html\n  ✓ Wolffia_Mankai_Endosphere_Cobamide_Guild.yaml\
    \ → /private/tmp/communitymech-causal-20261014/docs/communities/Wolffia_Mankai_Endosphere_Cobamide_Guild.html\n\
    \  ✓ Wollastonite_Ramichloridium_Talaromyces_Fungal_Consortium.yaml → /private/tmp/communitymech-causal-20261014/docs/communities/Wollastonite_Ramichloridium_Talaromyces_Fungal_Consortium.html\n\
    \  ✓ Yarrowia_lipolytica_Division_of_Labor_Lipid_Consortium.yaml → /private/tmp/communitymech-causal-20261014/docs/communities/Yarrowia_lipolytica_Division_of_Labor_Lipid_Consortium.html\n\
    \  ✓ Yogurt_TwoSpecies_Starter_Culture.yaml → /private/tmp/communitymech-causal-20261014/docs/communities/Yogurt_TwoSpecies_Starter_Culture.html\n\
    \  ✓ Zymomonas_Ecoli_Exometabolomics_Obligate_Mutualism.yaml → /private/tmp/communitymech-causal-20261014/docs/communities/Zymomonas_Ecoli_Exometabolomics_Obligate_Mutualism.html\n\
    \  ✓ hCom2_Complex_Gut_Microbiome.yaml → /private/tmp/communitymech-causal-20261014/docs/communities/hCom2_Complex_Gut_Microbiome.html\n\
    \  ✓ mCAFEs_Brachypodium_RCC.yaml → /private/tmp/communitymech-causal-20261014/docs/communities/mCAFEs_Brachypodium_RCC.html\n\
    \n✅ Rendered 458 communities to /private/tmp/communitymech-causal-20261014/docs/communities\n\
    \  ✓ Generated browser at /private/tmp/communitymech-causal-20261014/docs/browser.html\n\
    \  ✓ Generated landing at /private/tmp/communitymech-causal-20261014/docs/index.html"
  command: just --no-dotenv gen-html
  exit_code: 0
  target_ids:
  - CommunityMech:000302
  evidence_ids:
  - gen-html
- check_id: docs-current
  name: docs-current
  status: passed
  required: true
  summary: "\n  ✓ Wolffia_Mankai_Endosphere_Cobamide_Guild.yaml → /private/tmp/communitymech-causal-20261014/docs/communities/Wolffia_Mankai_Endosphere_Cobamide_Guild.html\n\
    \  ✓ Wollastonite_Ramichloridium_Talaromyces_Fungal_Consortium.yaml → /private/tmp/communitymech-causal-20261014/docs/communities/Wollastonite_Ramichloridium_Talaromyces_Fungal_Consortium.html\n\
    \  ✓ Yarrowia_lipolytica_Division_of_Labor_Lipid_Consortium.yaml → /private/tmp/communitymech-causal-20261014/docs/communities/Yarrowia_lipolytica_Division_of_Labor_Lipid_Consortium.html\n\
    \  ✓ Yogurt_TwoSpecies_Starter_Culture.yaml → /private/tmp/communitymech-causal-20261014/docs/communities/Yogurt_TwoSpecies_Starter_Culture.html\n\
    \  ✓ Zymomonas_Ecoli_Exometabolomics_Obligate_Mutualism.yaml → /private/tmp/communitymech-causal-20261014/docs/communities/Zymomonas_Ecoli_Exometabolomics_Obligate_Mutualism.html\n\
    \  ✓ hCom2_Complex_Gut_Microbiome.yaml → /private/tmp/communitymech-causal-20261014/docs/communities/hCom2_Complex_Gut_Microbiome.html\n\
    \  ✓ mCAFEs_Brachypodium_RCC.yaml → /private/tmp/communitymech-causal-20261014/docs/communities/mCAFEs_Brachypodium_RCC.html\n\
    \n✅ Rendered 458 communities to /private/tmp/communitymech-causal-20261014/docs/communities\n\
    \  ✓ Generated browser at /private/tmp/communitymech-causal-20261014/docs/browser.html\n\
    \  ✓ Generated landing at /private/tmp/communitymech-causal-20261014/docs/index.html\n\
    ✅ docs/ matches the KB"
  command: just --no-dotenv check-docs-current
  exit_code: 0
  target_ids:
  - CommunityMech:000302
  evidence_ids:
  - docs-current
- check_id: lint-final
  name: lint-final
  status: passed
  required: true
  summary: 'All checks passed!

    Success: no issues found in 49 source files'
  command: just --no-dotenv lint
  exit_code: 0
  target_ids:
  - CommunityMech:000302
  evidence_ids:
  - lint-final
- check_id: diff-check-final
  name: diff-check-final
  status: passed
  required: true
  summary: Passed; exact command output retained in receipt.
  command: git diff --check
  exit_code: 0
  target_ids:
  - CommunityMech:000302
  evidence_ids:
  - diff-check-final
- check_id: review-contract-before
  name: review-contract-before
  status: passed
  required: true
  summary: "{\n  \"repository\": \"culturebotai/CommunityMech\",\n  \"valid_reviews\"\
    : 27,\n  \"coverage\": \"declared_scopes_only\"\n}"
  command: .venv/bin/python scripts/record_review.py check --base 737a95eed17f606b30dd99fbec7dc82c19ad3f40
  exit_code: 0
  target_ids:
  - CommunityMech:000302
  evidence_ids:
  - review-contract-before
- check_id: network-warnings
  name: Native zero-warning network diagnostic
  status: failed
  required: false
  summary: Native exit 1 for an exactly baseline-identical warning set; preservation
    check verifies no structural errors. This is not a zero-warning pass.
  command: just --no-dotenv audit-network-json
  exit_code: 1
  target_ids:
  - CommunityMech:000302
  evidence_ids:
  - preservation
- check_id: complete-methods
  name: Complete experimental identity verification
  status: unavailable
  required: true
  summary: 'Complete Methods, experimental cultivar and conflicting strain spelling
    remain unverified; #1847 stays open.'
  target_ids:
  - CommunityMech:000302
  evidence_ids:
  - limits
- check_id: remote-ci
  name: Protected PR and merge-queue gates
  status: unavailable
  required: true
  summary: Pending at this immutable local review snapshot; subsequent remote receipts
    must establish completion before merge.
  target_ids:
  - CommunityMech:000302
  evidence_ids:
  - final-regression
evidence:
- evidence_id: abstract
  kind: primary_source
  reference: doi:10.1016/j.rhisph.2025.101142
  locator: 'references_cache/doi_10.1016_j.rhisph.2025.101142.md: complete abstract;
    sugarcane host and separate microbial/host expression sentences'
  accessed_at: '2026-10-15T04:31:54.034072Z'
  support: supports
  summary: The inspected abstract supports generic sugarcane and separates bacterial
    colonization-associated transcription from host hormone/nutrient-transporter transcription.
    It does not verify the experimental cultivar or species.
- evidence_id: taxonomy
  kind: database
  reference: reports/causal_graph_review/sources/20261015-metg2-host/ncbi-taxonomy.xml
  locator: 'Taxa 4546 and 4547: names, ranks and lineage'
  accessed_at: '2026-10-15T04:25:47.462501Z'
  support: supports
  summary: NCBI distinguishes Saccharum genus from S. officinarum species. The genus
    can provide an explicitly broader anchor, not an exact experimental identity.
- evidence_id: limits
  kind: prior_review
  reference: https://github.com/CultureBotAI/CommunityMech/issues/1847
  locator: Live issue body/comment and source manifest
  accessed_at: '2026-10-15T04:31:54.034072Z'
  support: context_only
  summary: Issue remains open for inoculant identity, Chiliseed2/Chileseed2 discrepancy
    and exact host. Bounded searches did not retrieve complete primary methods; search
    previews were not accepted as new membership evidence.
- evidence_id: record
  kind: record_content
  reference: kb/communities/SynCom_MetG2_Rhizobacteria_Sugarcane_Stress_Resilience.yaml
  locator: taxonomy[0], ecological_interactions[0,2].participating_taxa and discussions[0]
  accessed_at: '2026-10-15T04:43:33.798629Z'
  support: supports
  summary: The study host is anchored to Saccharum with explicit species/cultivar
    uncertainty. Two existing expression nodes name their source-supported plant or
    responding-phylum participants. The aggregate functional node and the one hypothetical
    arrow remain unchanged.
- evidence_id: ledger
  kind: prior_review
  reference: reports/causal_graph_review/decisions/20261015-metg2-host.yaml
  locator: All three node decisions and retained arrow
  accessed_at: '2026-10-15T04:43:33.798629Z'
  support: supports
  summary: Hash-linked successor retains claim-level evidence, exact paths, participant
    boundaries, no topology extension and needs_research status.
- evidence_id: final-regression
  kind: validation
  reference: reports/causal_graph_review/20261015-metg2-host/final-regression-clean.json
  locator: Actual command, timestamps, input hashes, exit code and stdout/stderr
  accessed_at: '2026-10-15T04:43:33.798629Z'
  support: supports
  summary: Retained execution receipt for final-regression
- evidence_id: connectivity-check
  kind: validation
  reference: reports/causal_graph_review/20261015-metg2-host/connectivity-check.json
  locator: Actual command, timestamps, input hashes, exit code and stdout/stderr
  accessed_at: '2026-10-15T04:43:33.798629Z'
  support: supports
  summary: Retained execution receipt for connectivity-check
- evidence_id: validate
  kind: validation
  reference: reports/causal_graph_review/20261015-metg2-host/validate.json
  locator: Actual command, timestamps, input hashes, exit code and stdout/stderr
  accessed_at: '2026-10-15T04:43:33.798629Z'
  support: supports
  summary: Retained execution receipt for validate
- evidence_id: strict
  kind: validation
  reference: reports/causal_graph_review/20261015-metg2-host/strict.json
  locator: Actual command, timestamps, input hashes, exit code and stdout/stderr
  accessed_at: '2026-10-15T04:43:33.798629Z'
  support: supports
  summary: Retained execution receipt for strict
- evidence_id: terms
  kind: validation
  reference: reports/causal_graph_review/20261015-metg2-host/terms.json
  locator: Actual command, timestamps, input hashes, exit code and stdout/stderr
  accessed_at: '2026-10-15T04:43:33.798629Z'
  support: supports
  summary: Retained execution receipt for terms
- evidence_id: gtdb
  kind: validation
  reference: reports/causal_graph_review/20261015-metg2-host/gtdb.json
  locator: Actual command, timestamps, input hashes, exit code and stdout/stderr
  accessed_at: '2026-10-15T04:43:33.798629Z'
  support: supports
  summary: Retained execution receipt for gtdb
- evidence_id: gtdb-domain
  kind: validation
  reference: reports/causal_graph_review/20261015-metg2-host/gtdb-domain.json
  locator: Actual command, timestamps, input hashes, exit code and stdout/stderr
  accessed_at: '2026-10-15T04:43:33.798629Z'
  support: supports
  summary: Retained execution receipt for gtdb-domain
- evidence_id: references
  kind: validation
  reference: reports/causal_graph_review/20261015-metg2-host/references.json
  locator: Actual command, timestamps, input hashes, exit code and stdout/stderr
  accessed_at: '2026-10-15T04:43:33.798629Z'
  support: supports
  summary: Retained execution receipt for references
- evidence_id: explicit-excerpts
  kind: validation
  reference: reports/causal_graph_review/20261015-metg2-host/explicit-excerpts.json
  locator: Actual command, timestamps, input hashes, exit code and stdout/stderr
  accessed_at: '2026-10-15T04:43:33.798629Z'
  support: supports
  summary: Retained execution receipt for explicit-excerpts
- evidence_id: history
  kind: validation
  reference: reports/causal_graph_review/20261015-metg2-host/history.json
  locator: Actual command, timestamps, input hashes, exit code and stdout/stderr
  accessed_at: '2026-10-15T04:43:33.798629Z'
  support: supports
  summary: Retained execution receipt for history
- evidence_id: rank
  kind: validation
  reference: reports/causal_graph_review/20261015-metg2-host/rank.json
  locator: Actual command, timestamps, input hashes, exit code and stdout/stderr
  accessed_at: '2026-10-15T04:43:33.798629Z'
  support: supports
  summary: Retained execution receipt for rank
- evidence_id: inventory
  kind: validation
  reference: reports/causal_graph_review/20261015-metg2-host/inventory.json
  locator: Actual command, timestamps, input hashes, exit code and stdout/stderr
  accessed_at: '2026-10-15T04:43:33.798629Z'
  support: supports
  summary: Retained execution receipt for inventory
- evidence_id: preservation
  kind: validation
  reference: reports/causal_graph_review/20261015-metg2-host/preservation-final.json
  locator: Actual command, timestamps, input hashes, exit code and stdout/stderr
  accessed_at: '2026-10-15T04:43:33.798629Z'
  support: supports
  summary: Retained execution receipt for preservation
- evidence_id: gen-html
  kind: validation
  reference: reports/causal_graph_review/20261015-metg2-host/gen-html.json
  locator: Actual command, timestamps, input hashes, exit code and stdout/stderr
  accessed_at: '2026-10-15T04:43:33.798629Z'
  support: supports
  summary: Retained execution receipt for gen-html
- evidence_id: docs-current
  kind: validation
  reference: reports/causal_graph_review/20261015-metg2-host/docs-current.json
  locator: Actual command, timestamps, input hashes, exit code and stdout/stderr
  accessed_at: '2026-10-15T04:43:33.798629Z'
  support: supports
  summary: Retained execution receipt for docs-current
- evidence_id: lint-final
  kind: validation
  reference: reports/causal_graph_review/20261015-metg2-host/lint-final.json
  locator: Actual command, timestamps, input hashes, exit code and stdout/stderr
  accessed_at: '2026-10-15T04:43:33.798629Z'
  support: supports
  summary: Retained execution receipt for lint-final
- evidence_id: diff-check-final
  kind: validation
  reference: reports/causal_graph_review/20261015-metg2-host/diff-check-final.json
  locator: Actual command, timestamps, input hashes, exit code and stdout/stderr
  accessed_at: '2026-10-15T04:43:33.798629Z'
  support: supports
  summary: Retained execution receipt for diff-check-final
- evidence_id: review-contract-before
  kind: validation
  reference: reports/causal_graph_review/20261015-metg2-host/review-contract-before.json
  locator: Actual command, timestamps, input hashes, exit code and stdout/stderr
  accessed_at: '2026-10-15T04:43:33.798629Z'
  support: supports
  summary: Retained execution receipt for review-contract-before
assessments:
- assessment_id: host
  area: grounding
  topic: Host rank and response attribution
  outcome: supported
  target_ids:
  - CommunityMech:000302
  evidence_ids:
  - abstract
  - taxonomy
  - record
  - final-regression
  - ledger
  summary: The explicit parent-only genus anchor removes false species precision.
    Named participants distinguish host expression from bacterial colonization-associated
    expression, with native auditor mutation/restoration tests.
- assessment_id: coverage
  area: completeness
  topic: Unresolved experimental identity
  outcome: concern
  target_ids:
  - CommunityMech:000302
  evidence_ids:
  - abstract
  - limits
  summary: Do not equate responding native taxa with the inoculant or silently resolve
    the conflicting strain spelling.
- assessment_id: graph
  area: graph
  topic: Retained source-bounded graph and evidence
  outcome: supported
  target_ids:
  - CommunityMech:000302
  evidence_ids:
  - abstract
  - record
  - ledger
  - preservation
  - explicit-excerpts
  summary: All three nodes and the one HYPOTHESIZED/PARTIAL contribution remain; no
    measured stress-tolerance phenotype, temporal order, isolated mediation or new
    topology is asserted by this repair.
findings:
- finding_id: host-scope
  issue_key: communitymech-1847-metg2-host-scope
  category: grounding
  severity: major
  status: resolved
  certainty: confirmed
  title: Unsupported host species and implicit expression participants
  description: The species assignment exceeds the inspected host evidence; unspecified
    participants also credit bacteria with plant transcription and the plant with
    bacterial colonization-associated expression. Correct the parent-rank anchor and
    explicitly name participants without changing topology.
  target_ids:
  - CommunityMech:000302
  field_paths:
  - taxonomy[0].taxon_term
  - ecological_interactions[0].participating_taxa
  - ecological_interactions[2].participating_taxa
  evidence_ids:
  - abstract
  - taxonomy
  - record
  - ledger
  - final-regression
  - preservation
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/SynCom_MetG2_Rhizobacteria_Sugarcane_Stress_Resilience.yaml
    role: canonical host and graph participants
  rule_id: causal-participant-scope
  native_severity: P2
  normalization_reason: Unsupported rank precision and cross-kingdom attribution affect
    graph meaning.
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/1847
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261015T043154Z-metg2-host-before
    finding_id: host-scope
  disposition_reason: Verified parent-only host grounding, two explicit participant
    lists, native schema/ontology gates and behavioral auditor tests; topology, all
    snippets and source cache preserved.
- finding_id: membership
  issue_key: communitymech-1847-metg2-membership
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Exact MetG2 membership and host identity remain unresolved
  description: The responding phylum is not the defined inoculant; primary methods
    and conflicting strain designation still require reconciliation. A parent-only
    host anchor does not finish this identity work.
  target_ids:
  - CommunityMech:000302
  field_paths:
  - taxonomy
  - discussions[0]
  evidence_ids:
  - abstract
  - record
  - limits
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/SynCom_MetG2_Rhizobacteria_Sugarcane_Stress_Resilience.yaml
    role: canonical host and graph participants
  rule_id: causal-community-identity
  native_severity: P2
  normalization_reason: Unresolved inoculant/host identity prevents complete graph
    participant certification.
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/1847
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261015T043154Z-metg2-host-before
    finding_id: membership
actions:
- action_id: resolve-membership
  description: Retrieve primary experimental methods/member evidence and reconcile
    the inoculant, spelling conflict and exact host without attributing native-community
    observations to all inoculants.
  finding_ids:
  - membership
  target_ids:
  - CommunityMech:000302
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/SynCom_MetG2_Rhizobacteria_Sugarcane_Stress_Resilience.yaml
    role: canonical host and graph participants
  acceptance_checks:
  - Exact source-backed inoculant roster and spelling disposition retained.
  - Host experimental identity and native-versus-inoculant graph attribution verified.
limitations:
- Scoped partial scientific self-review, not independent approval, whole-record certification
  or corpus completion.
- No native whole-record completeness/quality score is assigned to this focused identity
  correction.
- No full methods, all figures/supplements, or raw experimental data inspected. Search
  previews are leads only.
- No new topology or paid provider submission; source caches and historical reviews
  remain unchanged.
- The aggregate functional-gene node remains unchanged; native/inoculant participant
  reconciliation is not complete.
- 'Reference CLI zero issues is not zero coverage: six native excerpt calls were traced;
  two Discussion excerpts needed explicit validation (#476). Lexical matching is not
  scientific proof.'
- Initial post-repair tests exposed a mutation-harness KeyError and the new participant-census
  entry. Lint caught import ordering and the fixture XML annotation; the preservation
  helper initially used the wrong summary key. These were corrected and rerun; failed
  receipts remain intact. No schema, threshold, validator or source policy was weakened.
- The inventory remains 408 reviewed and 54 needs_research; no status was promoted
  by this scoped correction.
- Remote CI/queue completion remains pending at the immutable review snapshot.
notes:
- Post-repair observation at the exact committed inputs. The predecessor explicitly
  assesses the retained historical pre-fix tree.
links:
- https://github.com/CultureBotAI/CommunityMech/issues/1847
```
