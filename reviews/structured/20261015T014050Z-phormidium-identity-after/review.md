# Phormidium graph identity repaired; extension research remains open

- Review: 20261015T014050Z-phormidium-identity-after
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-15T01:14:32Z
- Finished UTC: 2026-10-15T01:40:50.304367Z
- Reviewer: codex (self_review)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Resolve #2009 across the canonical member, four graph references and two policy waivers. Retain the species scope, four bounded nodes and one arrow. The broader graph extension and non-graph claims remain open; no corpus-completion or independent-approval claim.

## Scope And Provenance

One member identity, its four graph references, and two exact-pair policy exceptions.

Selection: Confirmed issue #2009 during Phormidium graph research.
Coverage: partial; 2 reviewed / 462 in the declared population.
Source: git_commit at Git base 12ca19c2ad185a3a22a9e11c735de50683dada8c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000054 | kb/communities/Phormidium_Alkaline_Consortium.yaml | maintained | Phormidium alkaline consortium |
| id-label-policy | conf/id_label_targets.yaml | maintained | ID-label correspondence policy |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| preservation | passed | True | CommunityMech:000054, id-label-policy | {<br>  "records_including_hidden_and_ignored": 462,<br>  "changed_records": [<br>    "kb/communities/Phormidium_Alkaline_Consortium.yaml"<br>  ],<br>  "unchanged_records": 461,<br>  "corrected_term_objects": 5,<br>  "removed_exact_pair_waivers": 2,<br>  "graph_topology_and_evidence_preserved": true,<br>  "old_curation_history_semantically_preserved": true,<br>  "canonical_cache_unchanged": true,<br>  "public_source_hashes_verified": 2<br>} |
| after-regression | passed | True | CommunityMech:000054, id-label-policy | ......................................................                   [100%]<br>=============================== warnings summary ===============================<br>.venv/lib/python3.13/site-packages/linkml/generators/pydanticgen/template.py:553: 12 warnings<br>  /private/tmp/communitymech-causal-20261014/.venv/lib/python3.13/site-packages/linkml/generators/pydanticgen/template.py:553: PydanticDeprecatedSince211: Accessing the 'model_fields' attribute on the instance is deprecated. Instead, you should access this attribute from the model class. Deprecated in Pydantic V2.11 to be removed in V3.0.<br>    imports=imports, **{k: getattr(self, k, None) for k in self.model_fields if k != "imports"}<br><br>-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html<br>54 passed, 12 warnings in 52.55s |
| validate | passed | True | CommunityMech:000054, id-label-policy | No issues found |
| strict | passed | True | CommunityMech:000054, id-label-policy | Command completed with exit 0; exact output in receipt. |
| terms | passed | True | CommunityMech:000054, id-label-policy | ✅ Validation passed |
| gtdb-coherence | passed | True | CommunityMech:000054, id-label-policy | Command completed with exit 0; exact output in receipt. |
| gtdb-domain | passed | True | CommunityMech:000054, id-label-policy | files checked: 1<br>contradictory lineages: 0 |
| explicit-excerpts | passed | True | CommunityMech:000054, id-label-policy | {<br>  "record": "CommunityMech:000054",<br>  "native_count": 21,<br>  "native_fields": [<br>    "taxonomy[0].evidence[0].snippet",<br>    "taxonomy[0].evidence[1].snippet",<br>    "taxonomy[1].evidence[0].snippet",<br>    "taxonomy[2].evidence[0].snippet",<br>    "taxonomy[3].evidence[0].snippet",<br>    "taxonomy[4].evidence[0].snippet",<br>    "taxonomy[5].evidence[0].snippet",<br>    "ecological_interactions[0].evidence[0].snippet",<br>    "ecological_interactions[1].evidence[0].snippet",<br>    "ecological_interactions[2].evidence[0].snippet",<br>    "ecological_interactions[3].evidence[0].snippet",<br>    "environmental_factors[0].evidence[0].snippet",<br>    "environmental_factors[1].evidence[0].snippet",<br>    "environmental_factors[2].evidence[0].snippet",<br>    "environmental_factors[3].evidence[0].snippet",<br>    "environmental_factors[4].evidence[0].snippet",<br>    "environmental_factors[5].evidence[0].snippet",<br>    "related_ingredients[0].evidence[0].snippet",<br>    "growth_media[0].evidence[0].snippet",<br>    "growth_media[0].evidence[1].snippet",<br>    "cultivation_setup[0].evidence[0].snippet"<br>  ],<br>  "explicit_excerpt_count": 23,<br>  "native_omitted_discussions": [<br>    "discussions[0].evidence[0].snippet",<br>    "discussions[0].evidence[1].snippet"<br>  ],<br>  "identity_control_mutation_restoration": "passed",<br>  "discussion_negative_controls": "passed",<br>  "network_forbidden": true,<br>  "limit": "Lexical matches do not establish scientific support; known Discussion traversal gap #476 is compensated, not fixed."<br>} |
| history | passed | True | CommunityMech:000054, id-label-policy | No issues found |
| rank | passed | True | CommunityMech:000054, id-label-policy | rank	score	path	id	name	taxonomy	connected_taxa	disconnected_taxa	ecological_interactions	downstream_edges	interaction_evidence	missing	dangling_downstream	self_downstream<br>1	81.7	kb/communities/Phormidium_Alkaline_Consortium.yaml	CommunityMech:000054	Phormidium Alkaline Consortium	6	5	1	4	1	4	additional_downstream,metabolites_or_biological_processes,interaction_type,disconnected_taxa	0	0 |
| kgx-export | passed | True | CommunityMech:000054, id-label-policy | Wrote 1423 nodes / 2177 edges to output/kgx |
| products | passed | True | CommunityMech:000054, id-label-policy | all configured ontologies are reachable<br><br>id↔label correspondence summary:<br>          OK_CANONICAL: 9787<br>            OK_SYNONYM: 4<br>          OK_EXCEPTION: 3<br>    SKIPPED_NO_ADAPTER: 924<br><br>✅ All id↔label pairs correspond. |
| gen-html | passed | True | CommunityMech:000054, id-label-policy | at_CrownRot_TB_CrossKingdom_SynCom.html<br>  ✓ Wheat_DT_Rhizosphere_SynCom.yaml → /private/tmp/communitymech-causal-20261014/docs/communities/Wheat_DT_Rhizosphere_SynCom.html<br>  ✓ Wheat_Straw_Biogas_Pretreatment_SynCom.yaml → /private/tmp/communitymech-causal-20261014/docs/communities/Wheat_Straw_Biogas_Pretreatment_SynCom.html<br>  ✓ Wheat_SynCom_SASW01_Drought_Inoculant.yaml → /private/tmp/communitymech-causal-20261014/docs/communities/Wheat_SynCom_SASW01_Drought_Inoculant.html<br>  ✓ Wine_Yeast_FiveSpecies_Strain_Substitution_Consortium.yaml → /private/tmp/communitymech-causal-20261014/docs/communities/Wine_Yeast_FiveSpecies_Strain_Substitution_Consortium.html<br>  ✓ Wine_Yeast_ThreeSpecies_Contact_Consortium.yaml → /private/tmp/communitymech-causal-20261014/docs/communities/Wine_Yeast_ThreeSpecies_Contact_Consortium.html<br>  ✓ Wolffia_Mankai_Endosphere_Cobamide_Guild.yaml → /private/tmp/communitymech-causal-20261014/docs/communities/Wolffia_Mankai_Endosphere_Cobamide_Guild.html<br>  ✓ Wollastonite_Ramichloridium_Talaromyces_Fungal_Consortium.yaml → /private/tmp/communitymech-causal-20261014/docs/communities/Wollastonite_Ramichloridium_Talaromyces_Fungal_Consortium.html<br>  ✓ Yarrowia_lipolytica_Division_of_Labor_Lipid_Consortium.yaml → /private/tmp/communitymech-causal-20261014/docs/communities/Yarrowia_lipolytica_Division_of_Labor_Lipid_Consortium.html<br>  ✓ Yogurt_TwoSpecies_Starter_Culture.yaml → /private/tmp/communitymech-causal-20261014/docs/communities/Yogurt_TwoSpecies_Starter_Culture.html<br>  ✓ Zymomonas_Ecoli_Exometabolomics_Obligate_Mutualism.yaml → /private/tmp/communitymech-causal-20261014/docs/communities/Zymomonas_Ecoli_Exometabolomics_Obligate_Mutualism.html<br>  ✓ hCom2_Complex_Gut_Microbiome.yaml → /private/tmp/communitymech-causal-20261014/docs/communities/hCom2_Complex_Gut_Microbiome.html<br>  ✓ mCAFEs_Brachypodium_RCC.yaml → /private/tmp/communitymech-causal-20261014/docs/communities/mCAFEs_Brachypodium_RCC.html<br><br>✅ Rendered 458 communities to /private/tmp/communitymech-causal-20261014/docs/communities<br>  ✓ Generated browser at /private/tmp/communitymech-causal-20261014/docs/browser.html<br>  ✓ Generated landing at /private/tmp/communitymech-causal-20261014/docs/index.html |
| docs-current | passed | True | CommunityMech:000054, id-label-policy | gdom_SynCom.html<br>  ✓ Wheat_DT_Rhizosphere_SynCom.yaml → /private/tmp/communitymech-causal-20261014/docs/communities/Wheat_DT_Rhizosphere_SynCom.html<br>  ✓ Wheat_Straw_Biogas_Pretreatment_SynCom.yaml → /private/tmp/communitymech-causal-20261014/docs/communities/Wheat_Straw_Biogas_Pretreatment_SynCom.html<br>  ✓ Wheat_SynCom_SASW01_Drought_Inoculant.yaml → /private/tmp/communitymech-causal-20261014/docs/communities/Wheat_SynCom_SASW01_Drought_Inoculant.html<br>  ✓ Wine_Yeast_FiveSpecies_Strain_Substitution_Consortium.yaml → /private/tmp/communitymech-causal-20261014/docs/communities/Wine_Yeast_FiveSpecies_Strain_Substitution_Consortium.html<br>  ✓ Wine_Yeast_ThreeSpecies_Contact_Consortium.yaml → /private/tmp/communitymech-causal-20261014/docs/communities/Wine_Yeast_ThreeSpecies_Contact_Consortium.html<br>  ✓ Wolffia_Mankai_Endosphere_Cobamide_Guild.yaml → /private/tmp/communitymech-causal-20261014/docs/communities/Wolffia_Mankai_Endosphere_Cobamide_Guild.html<br>  ✓ Wollastonite_Ramichloridium_Talaromyces_Fungal_Consortium.yaml → /private/tmp/communitymech-causal-20261014/docs/communities/Wollastonite_Ramichloridium_Talaromyces_Fungal_Consortium.html<br>  ✓ Yarrowia_lipolytica_Division_of_Labor_Lipid_Consortium.yaml → /private/tmp/communitymech-causal-20261014/docs/communities/Yarrowia_lipolytica_Division_of_Labor_Lipid_Consortium.html<br>  ✓ Yogurt_TwoSpecies_Starter_Culture.yaml → /private/tmp/communitymech-causal-20261014/docs/communities/Yogurt_TwoSpecies_Starter_Culture.html<br>  ✓ Zymomonas_Ecoli_Exometabolomics_Obligate_Mutualism.yaml → /private/tmp/communitymech-causal-20261014/docs/communities/Zymomonas_Ecoli_Exometabolomics_Obligate_Mutualism.html<br>  ✓ hCom2_Complex_Gut_Microbiome.yaml → /private/tmp/communitymech-causal-20261014/docs/communities/hCom2_Complex_Gut_Microbiome.html<br>  ✓ mCAFEs_Brachypodium_RCC.yaml → /private/tmp/communitymech-causal-20261014/docs/communities/mCAFEs_Brachypodium_RCC.html<br><br>✅ Rendered 458 communities to /private/tmp/communitymech-causal-20261014/docs/communities<br>  ✓ Generated browser at /private/tmp/communitymech-causal-20261014/docs/browser.html<br>  ✓ Generated landing at /private/tmp/communitymech-causal-20261014/docs/index.html<br>✅ docs/ matches the KB |
| lint | passed | True | CommunityMech:000054, id-label-policy | All checks passed!<br>Success: no issues found in 49 source files |
| diff-check | passed | True | CommunityMech:000054, id-label-policy | Command completed with exit 0; exact output in receipt. |
| artifact-identity | passed | True | CommunityMech:000054, id-label-policy | {<br>  "html": "docs/communities/Phormidium_Alkaline_Consortium.html",<br>  "taxonomy_link": "3723519",<br>  "graph_node_id": "NCBITaxon:3723519",<br>  "source_name_retained": true,<br>  "kgx_name": "Candidatus Sodalinema alkaliphilum",<br>  "kgx_member_edge_present": true,<br>  "old_taxon_absent_from_generated_identity_links_nodes_and_edges": true,<br>  "limit": "Historical notes may name the former identifier; this checks active links and identities, not all text occurrences."<br>} |
| review-contract-before | passed | True | CommunityMech:000054, id-label-policy | {<br>  "repository": "culturebotai/CommunityMech",<br>  "valid_reviews": 23,<br>  "coverage": "declared_scopes_only"<br>} |
| Native zero-warning network diagnostic | failed | False | CommunityMech:000054 | Exit 1 for the unchanged pre-existing warning set; exact JSON matches the baseline. Not a zero-warning pass. |
| Native reference CLI coverage | failed | False | CommunityMech:000054 | The command exits 0 but reports zero checks. Explicit offline plugin/excerpt validation supplies the actual checked coverage. |
| Additional GTDB grounding | unavailable | False | CommunityMech:000054 | Configured crosswalk lookup failed. The pre-existing UNRESOLVED status is retained; native coherence/domain checks passed without inventing a lineage. |
| Required research for new graph structure | unavailable | True | CommunityMech:000054 | No Edison extension workflow or primary-only substitution was performed in this identity repair. Prior open extension scope remains under #1699. |
| Remote CI and protected queue | unavailable | True | CommunityMech:000054, id-label-policy | Not completed at this immutable local review snapshot; required checks must pass before merge. |

## Scientific And Domain Assessments

### Species identity preserves multi-strain source scope

identity: supported. Targets: CommunityMech:000054.

The cyanobacterial member and all four graph references now use the canonical species ID/label, retain the source name, and distinguish PBR-2020 from the whole population.

### Wrong-organism waivers removed without weakening enforcement

grounding: supported. Targets: id-label-policy.

Only the two obsolete exact-pair exceptions were removed. Canonical and KGX surfaces pass the native product validator without a replacement waiver.

### Evidence-bounded existing nodes and arrow

graph: supported. Targets: CommunityMech:000054.

Retain measured carbon transfer, the PARTIAL genomic polymer-use hypothesis and qualified low-peptide alphaproteobacterial evidence. Identity correction does not strengthen mechanistic claims or add topology.

### Unfinished source and niche reconciliation

completeness: concern. Targets: CommunityMech:000054.

A corrected cyanobacterial ID is not completion of seven niche candidates, MAG reconciliation, source conflicts or non-graph claims. Keep needs_research and the existing follow-ups open.

## Findings

### wrong-cyanobacterial-id: Cyanobacterial graph references point to an unrelated organism

blocker / resolved / confirmed; issue key: communitymech-2009-phormidium-identity.

1807132 is an alternative ID for Syntrophocurvum, not Phormidium/Sodalinema. Five maintained fields and two policy waivers require coordinated repair.

Disposition: Five species groundings corrected and two stale waivers removed, with canonical label, source-population scope, preserved graph, regression controls and native product gates verified.

### phormidium-coverage: Phormidium niche coverage remains incomplete

major / open / confirmed; issue key: communitymech-1699-coverage.

The bounded four-node graph does not yet represent the source's other proposed ecological niches. Source conflicts and MAG-level participant reconciliation must be assessed before adding supported structure; a connected graph is not itself the acceptance criterion.

## Recommended Actions And Acceptance Checks

### extend-phormidium

Complete authorized one-community research, reconcile MAG/source discrepancies and curate only supported graph structure.

- Obtain the one-community Edison research report required by the invoked skill, or explicit authorization to use direct-primary-source research in its place.
- Keep the corrected prompt and explicit warning about non-graph context claims tracked in issue 1701.
- Resolve MAG-level participant mapping against source taxonomy and canonical identifiers without transferring related-species phenotypes.
- Verify exact snippets and keep supplemental evidence separate from article caches.
- Apply only supported nodes/arrows with guarded writes, append-only history, validators, generated-doc checks and a successor review.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ncbi | reports/causal_graph_review/sources/20261015-phormidium-identity-batch132/ncbi-taxonomy.xml; Taxon 2293317/AkaTaxIds, 3723519/name and synonym, 2839084/parent and rank | refutes | Legacy 1807132 resolves to a Bacillota/Clostridia species, not the cyanobacterium. The source name is a synonym of cyanobacterial species 3723519; PBR-2020 is its child strain 2839084. |
| oak | reports/causal_graph_review/sources/20261015-phormidium-identity-batch132/oak-taxonomy.json; Selected statements; ontology version 2026-07-12 | supports | The installed ontology independently represents the same legacy alias, species canonical label and source-name synonym; neither replacement candidate needs a missing-term waiver in this snapshot. |
| paper2022 | doi:10.3389/fmicb.2022.780346; Results, community composition; five metagenomes from different cultures/time points; distinct OSCR comparison | supports | The named Phormidium population is the only cyanobacterium and the most abundant member. The combined record spans multiple conditions and sampling times, not one isolated strain. |
| paper2021 | PMID:34877483; https://pmc.ncbi.nlm.nih.gov/articles/PMC8633866/ ; identity/strain Results p0085-p0110, conclusion p0205, limitations p0215, data availability p0255 | supports | Species naming, persistent strain diversity and the PBR-2020 reference-genome accession support species-level grounding while retaining the publication name; one reference strain must not absorb all conditions. |
| canonical | kb/communities/Phormidium_Alkaline_Consortium.yaml; taxonomy[0], four graph references, appended history and unchanged remaining graph; policy has two fewer exceptions | supports | Five corrected species pairs retain the publication name. Identity notes distinguish the reference strain and species population. A short exact member-identity excerpt is appended; all existing graph evidence and topology are unchanged. |
| before | reviews/structured/20261015T011216Z-phormidium-identity-before/review.yaml; wrong-cyanobacterial-id | context_only | Immutable predecessor establishes the wrong-organism identifier and two stale exact-pair waivers. |
| handoff | reviews/structured/20261014T235318Z-causal-prompt-phormidium-after/review.yaml; phormidium-coverage and source assessment from batch131 | partial | Seven candidate niches and four source discrepancies remain a research handoff, not completed extension. Correcting one participant identity does not resolve all MAG mapping or source conflicts. |
| preservation | reports/causal_graph_review/20261015-batch132/preservation.json; command, hashes, timestamps, exit_code, stdout and stderr | supports | Actual command receipt for preservation |
| after-regression | reports/causal_graph_review/20261015-batch132/final-regression.json; command, hashes, timestamps, exit_code, stdout and stderr | supports | Actual command receipt for after-regression |
| validate | reports/causal_graph_review/20261015-batch132/validate.json; command, hashes, timestamps, exit_code, stdout and stderr | supports | Actual command receipt for validate |
| strict | reports/causal_graph_review/20261015-batch132/strict.json; command, hashes, timestamps, exit_code, stdout and stderr | supports | Actual command receipt for strict |
| terms | reports/causal_graph_review/20261015-batch132/terms.json; command, hashes, timestamps, exit_code, stdout and stderr | supports | Actual command receipt for terms |
| gtdb-coherence | reports/causal_graph_review/20261015-batch132/gtdb-coherence.json; command, hashes, timestamps, exit_code, stdout and stderr | supports | Actual command receipt for gtdb-coherence |
| gtdb-domain | reports/causal_graph_review/20261015-batch132/gtdb-domain.json; command, hashes, timestamps, exit_code, stdout and stderr | supports | Actual command receipt for gtdb-domain |
| explicit-excerpts | reports/causal_graph_review/20261015-batch132/explicit-excerpts.json; command, hashes, timestamps, exit_code, stdout and stderr | supports | Actual command receipt for explicit-excerpts |
| history | reports/causal_graph_review/20261015-batch132/history.json; command, hashes, timestamps, exit_code, stdout and stderr | supports | Actual command receipt for history |
| rank | reports/causal_graph_review/20261015-batch132/rank.json; command, hashes, timestamps, exit_code, stdout and stderr | supports | Actual command receipt for rank |
| kgx-export | reports/causal_graph_review/20261015-batch132/kgx-export.json; command, hashes, timestamps, exit_code, stdout and stderr | supports | Actual command receipt for kgx-export |
| products | reports/causal_graph_review/20261015-batch132/products.json; command, hashes, timestamps, exit_code, stdout and stderr | supports | Actual command receipt for products |
| gen-html | reports/causal_graph_review/20261015-batch132/gen-html.json; command, hashes, timestamps, exit_code, stdout and stderr | supports | Actual command receipt for gen-html |
| docs-current | reports/causal_graph_review/20261015-batch132/docs-current-final.json; command, hashes, timestamps, exit_code, stdout and stderr | supports | Actual command receipt for docs-current |
| lint | reports/causal_graph_review/20261015-batch132/lint-final.json; command, hashes, timestamps, exit_code, stdout and stderr | supports | Actual command receipt for lint |
| diff-check | reports/causal_graph_review/20261015-batch132/diff-check.json; command, hashes, timestamps, exit_code, stdout and stderr | supports | Actual command receipt for diff-check |
| artifact-identity | reports/causal_graph_review/20261015-batch132/artifact-identity.json; command, hashes, timestamps, exit_code, stdout and stderr | supports | Actual command receipt for artifact-identity |
| review-contract-before | reports/causal_graph_review/20261015-batch132/review-contract-before.json; command, hashes, timestamps, exit_code, stdout and stderr | supports | Actual command receipt for review-contract-before |
| network | reports/causal_graph_review/20261015-batch132/network.json; Baseline-equivalent JSON and actual exit 1 | context_only | Unchanged warnings do not establish scientific completeness or justify adding unsupported arrows. |

## Limits And Additional Notes

- Partial source-based self-review, not independent approval, whole-record certification or corpus completion; 54 records remain needs_research.
- Native completeness/quality metrics are not computed for this one-member identity repair. Readiness score is structural only.
- The 2021 article is read in bounded identity/strain spans; raw data, all supplementary files and other member groundings are not recertified.
- GTDB crosswalk was unavailable in the configured locations. Bounded ignored-inclusive directory searches had permission-denied areas; no claim of global absence is made.
- The reference CLI reports zero checks; explicit plugin traversal and Discussion compensation are recorded. Lexical matching does not prove scientific support.
- Initial failing regressions, guarded rejection of an invalid evidence-source enum and a formatting-boundary failure are retained as historical receipts, not final passes. Both failed writes left the canonical bytes unchanged.
- Initial lint errors were corrected and rerun. The first docs-current run rejected the uncommitted generated page; the final native run verifies the committed page. Earlier failed receipts remain unchanged.
- The first committed docs-current retry failed before rendering because nested just requires JUST_NO_DOTENV=true rather than 1. The corrected invocation propagates true, retains the failure receipt, and does not read dotenv files.
- No new nodes/arrows, provider submission or paid research. Wider extension and #1701 non-graph issues remain open.
- Remote CI and queue acceptance are pending at this immutable input snapshot; later publication receipts must verify them separately.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T014050Z-phormidium-identity-after
kind: repository
repository: CultureBotAI/CommunityMech
title: Phormidium graph identity repaired; extension research remains open
started_at: '2026-10-15T01:14:32Z'
finished_at: '2026-10-15T01:40:50.304367Z'
reviewer:
  identity: codex
  kind: agent
  independence: self_review
  independence_basis: Implementing-agent scientific source review, not independent
    approval.
skill: communitymech-causal-graphs
completion: partial
verdict: needs_curation
scientific_review: true
source:
  git_revision: 12ca19c2ad185a3a22a9e11c735de50683dada8c
  state: git_commit
  inputs:
  - path: .github/workflows/label-correspondence.yaml
    sha256: f718dceea46b70014fbd915c837c911b37e42b69d0af5f65744def28ad21377b
    role: context
  - path: conf/id_label_targets.yaml
    sha256: 944f6060ef93c1e508e7e99079ebd18eb6f90ed567e900b752f807fb93bf60c4
    role: target
  - path: conf/record_review.yaml
    sha256: 8cbd8f9d209f78de47a8c35091e43bf1dadbe41ee07492c7860b6d4be30112a8
    role: context
  - path: docs/communities/Phormidium_Alkaline_Consortium.html
    sha256: 6ca92efc0120013ffab82d8edcfdccd28a16c2abd3217db8ad6508aa876c24bc
    role: context
  - path: docs/record-review-profile.md
    sha256: 285f79747999f83edbe63e5efde349a5cc063e9e486ce1a748b47b76c6631f31
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: history/records/Phormidium_Alkaline_Consortium/2026-10-15T011536Z-codex-932c6d.yaml
    sha256: 8d366d916330ca87720e4df4c4cfe5744fc0c7807e27c1ec7dab5093263e047b
    role: context
  - path: kb/communities/Phormidium_Alkaline_Consortium.yaml
    sha256: 0f03389e79ddcf2e97ebb0f32bd51a776b6bcbaea3ddad52c21ada8feca2939b
    role: target
  - path: references_cache/doi_10.3389_fmicb.2022.780346.md
    sha256: a3ba7f3dfd3bd6b6ae6338a05beead53f2cb15c89f70f0a89700cbfa0dc2b929
    role: context
  - path: reports/causal_graph_review/20261015-batch132/after-regression.json
    sha256: feaf316e2fca90de5237f643bcdd63755f27c45ab44c88e6b662a658e1fad5d3
    role: context
  - path: reports/causal_graph_review/20261015-batch132/artifact-identity.json
    sha256: 933fc57ec0d4a4857f597667d436d051caf05a36b4141dda003b33af8fe3b3ec
    role: context
  - path: reports/causal_graph_review/20261015-batch132/baseline-network.json
    sha256: 1cfcd0081f37d8b7d1fe31e7476a69da6e019c73dc37e372fa84c571627d28e9
    role: context
  - path: reports/causal_graph_review/20261015-batch132/baseline-rank.json
    sha256: 9fd1107144f6aa87d8305c001760974e1720e1527f6b0100c8293487cfdce956
    role: context
  - path: reports/causal_graph_review/20261015-batch132/baseline-references.json
    sha256: 3baff05486b40e489c6e58fe6dd5077096b2cdb336988da5afb1ae216db2506d
    role: context
  - path: reports/causal_graph_review/20261015-batch132/baseline-strict.json
    sha256: 83316e3f11375b5ddb2caed362f859a9d6cf4fef81b0032d9e0e361ddb643303
    role: context
  - path: reports/causal_graph_review/20261015-batch132/baseline-terms.json
    sha256: 65ca6849b04e1531363ba07160d9245dcb334c84519cd83c23f1db6c6e457fe4
    role: context
  - path: reports/causal_graph_review/20261015-batch132/baseline-validate.json
    sha256: ccdd0d74e25129a29b742b5892d742ffc9d90df9996c1d8803961710af7f73a0
    role: context
  - path: reports/causal_graph_review/20261015-batch132/before-regression.json
    sha256: 56cfbfbd6c7ce807992bfd71e328ea121efa5f73353235554f8059b9ca7de95b
    role: context
  - path: reports/causal_graph_review/20261015-batch132/check_artifacts.py
    sha256: a2adcbc21558b825c7a4b57046b6d962be229eb841f0522f6b54f9ba95de9453
    role: context
  - path: reports/causal_graph_review/20261015-batch132/check_preservation.py
    sha256: fda6f1aac0bf7a08e9e52afae6639af576dd4204356752ef641d3ee13885e023
    role: context
  - path: reports/causal_graph_review/20261015-batch132/check_snippets.py
    sha256: 48f9c373001312c8a3898bce2649a8d92ff7ce91c760db1afaa316cd9684a7e9
    role: context
  - path: reports/causal_graph_review/20261015-batch132/diff-check.json
    sha256: 9bc9fbd91e5280b74a6b814e129a8e994de3406cd64e80a9840d8ae8e512fadc
    role: context
  - path: reports/causal_graph_review/20261015-batch132/docs-current-committed.json
    sha256: 8db2a14608c04c74e64b58a7b1a8c38a85eedbc46f76eb8943e712de2fdfa485
    role: context
  - path: reports/causal_graph_review/20261015-batch132/docs-current-final.json
    sha256: 78670925efc93e532da7d28b1a4263fcc8852aea8a8c67ae967eec8c7a675af3
    role: context
  - path: reports/causal_graph_review/20261015-batch132/docs-current.json
    sha256: 2a74a3502a8b3a723684925c4198eee7825f3b9db81a76635f08478f5daf0798
    role: context
  - path: reports/causal_graph_review/20261015-batch132/explicit-excerpts.json
    sha256: 11356de4ca86f3d395a8ef89bc9bbe6b9a116cb49cb89ebf88c4f4c7403060b8
    role: context
  - path: reports/causal_graph_review/20261015-batch132/final-inventory.json
    sha256: c8d77aa5d63492f7bff4c373921a033e466c87756ceb6b5cd1aee02d8a761b43
    role: context
  - path: reports/causal_graph_review/20261015-batch132/final-regression.json
    sha256: 7f97ed973ea01c7d008f024b2de6bd7ef992fe664b345a19d7f8ea287e73d570
    role: context
  - path: reports/causal_graph_review/20261015-batch132/gen-html.json
    sha256: 35ea4dbf17483e6e8308fe38b312f85c09380f1be47a9ca0009cbb4a67a3c2b9
    role: context
  - path: reports/causal_graph_review/20261015-batch132/gtdb-coherence.json
    sha256: 0099e46751a2077d5f7218eb1ce1153a7685fea347233dcb2050113a0be7b97b
    role: context
  - path: reports/causal_graph_review/20261015-batch132/gtdb-domain.json
    sha256: 9e1997bda87b40ab64b1755b0df5ee470035194a2ae18b12ad44ebb76768f4c6
    role: context
  - path: reports/causal_graph_review/20261015-batch132/gtdb-lookup.json
    sha256: 9aaae6e4ed46288d512adfdf82eef8b5b58e21a021e9e295914be4bfd07c76d2
    role: context
  - path: reports/causal_graph_review/20261015-batch132/guarded-write-invalid-evidence-source.json
    sha256: 78bfd7d1e86d483f6994da6214ae91666b4c774f5e684d3254b9506ce840cdcf
    role: context
  - path: reports/causal_graph_review/20261015-batch132/guarded-write.json
    sha256: 54b61ded45e7665d1a1d5a4f724993138ebe81692e11b62564b09e70e7d7bce2
    role: context
  - path: reports/causal_graph_review/20261015-batch132/history.json
    sha256: 2f05e6703e7764110a621785df3abc97c5362f5804fc437fd7eb3d830a1a9744
    role: context
  - path: reports/causal_graph_review/20261015-batch132/kgx-export.json
    sha256: c4ad3cc3706afae9a8dcc9622b58de373850a080bfbff9cc2bc9142a28b7747d
    role: context
  - path: reports/causal_graph_review/20261015-batch132/lint-final.json
    sha256: 40bd1c6a164b646c6d7093e09eda93d6a5158a27a302c42f83c2519acdd74cf3
    role: context
  - path: reports/causal_graph_review/20261015-batch132/lint.json
    sha256: 9c57c5776cdc4b5ef7210bdeaedaabca6855f37f1337023fd912b533056f5f36
    role: context
  - path: reports/causal_graph_review/20261015-batch132/network.json
    sha256: ace0c40b7d0dad85f3fe76da405ddb2ac183263a67337f9747d43879d0735383
    role: context
  - path: reports/causal_graph_review/20261015-batch132/new-history.json
    sha256: 2b13081ef4a0a67726447ed9782e745e4c0413da3eea35d945defa721a02ff1d
    role: context
  - path: reports/causal_graph_review/20261015-batch132/preservation.json
    sha256: 8803ce4e7d57caeca5928cb0f3fe4aa26fb9adf1ec07a9c0fbbeb888145b936b
    role: context
  - path: reports/causal_graph_review/20261015-batch132/preserve-format-boundaries.json
    sha256: 7cbabdc7c33e29f6d736de07af71e097e1a8c8e253af6c56c8b89614cfb4d246
    role: context
  - path: reports/causal_graph_review/20261015-batch132/preserve-format.json
    sha256: 8384eee8931dcfce8b8ee059a7d2a6a4948bfa14a3740361a0d0576c1c290bb7
    role: context
  - path: reports/causal_graph_review/20261015-batch132/products.json
    sha256: ff11dd94349072907456615930169d122110ba9e2f5efea0b45bedaa518bb0d6
    role: context
  - path: reports/causal_graph_review/20261015-batch132/rank.json
    sha256: e212710d672e4a7620d9ade72b4f7a0f6a8959aac52e75999c23f46581d425bd
    role: context
  - path: reports/causal_graph_review/20261015-batch132/references.json
    sha256: 3baa8857c46b9944011690f4771c321d96f0ae9959c2d9dd81218f42c0126c6d
    role: context
  - path: reports/causal_graph_review/20261015-batch132/review-contract-before.json
    sha256: 1b7b19c52e074cda3b1b102e47e480c1640d1ebcc21f299c5a9609e79afd3ec2
    role: context
  - path: reports/causal_graph_review/20261015-batch132/strict.json
    sha256: 431ddadf68c6a89ddda4de0d453012e85eba6fdac71d6173807379750eaa228d
    role: context
  - path: reports/causal_graph_review/20261015-batch132/terms.json
    sha256: 479b9174bb63e5f2eb688eab1766b93429138b217b384968a39b0527922a3ae1
    role: context
  - path: reports/causal_graph_review/20261015-batch132/validate.json
    sha256: 4def3eec67d50bbf5ecadf70da776eed7fb586c5c1fd68c3b45eeb65e91ac754
    role: context
  - path: reports/causal_graph_review/decisions/20261015-phormidium-identity-batch132.yaml
    sha256: 400c7514d7a6855a7204ce7db68267fbf59a596d9c0eb62692c3c6ffa83d88f7
    role: context
  - path: reports/causal_graph_review/inventory.tsv
    sha256: 4165a82bbbcdedc0e5230134095af1f98830812f68a943cf855c059ed452f26a
    role: context
  - path: reports/causal_graph_review/sources/20261014-phormidium-batch131/article.xml
    sha256: 3c62edb9012494e345827fe35d4a76c11a96f9c2decc36ffabfdfef43d0e14f5
    role: context
  - path: reports/causal_graph_review/sources/20261014-phormidium-batch131/assessment.yaml
    sha256: 2a60b9c521a35f667416739a3173a0875c22c060de1cc4edc1d3ea932addd5ac
    role: context
  - path: reports/causal_graph_review/sources/20261015-phormidium-identity-batch132/manifest.json
    sha256: 18b6fd51c762c339a957efb4664c0f33612048c3b41e972e7c4659bb1f47aa10
    role: context
  - path: reports/causal_graph_review/sources/20261015-phormidium-identity-batch132/ncbi-taxonomy.xml
    sha256: cfee5fecfe1e5362eb32f516f341c16d6cf0eab8992c1f665021fc2d931258c3
    role: context
  - path: reports/causal_graph_review/sources/20261015-phormidium-identity-batch132/oak-taxonomy.json
    sha256: f9a6a4e2c0aab63008c54e77db6cd2b1382260dc24881aa8928786609121b5b6
    role: context
  - path: reports/causal_graph_review/summary.json
    sha256: d4e452ae6d6b3a8c12a77274e08723406b5c97fb702a4df58d15c1e547e92819
    role: context
  - path: reviews/structured/20261014T235318Z-causal-prompt-phormidium-after/review.yaml
    sha256: a99c60c0784cf08aa251e1786ac19b4aabf11714b6c5522c70c1bf7eec3d4b5b
    role: context
  - path: reviews/structured/20261015T011216Z-phormidium-identity-before/review.md
    sha256: ac5b2b1e5dd64dec73e3c1cd0a4ff3f417f73661903f34b33ca22e4c5ebd55f9
    role: context
  - path: reviews/structured/20261015T011216Z-phormidium-identity-before/review.yaml
    sha256: 76fa4af6da4c3dbb6e890ea9d1355be0b154ef36d01313f9695aaae3ac0968a8
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/term_fix_apply.py
    sha256: 0deb9d3452a9ad77f87852c5f1983483b6077fa8603a7e3dc54c49c125da53bd
    role: context
  - path: src/communitymech/schema/communitymech.yaml
    sha256: e5a87e5367609334ec0d6361f6ddafbe6bc4a1f7d93e5264c64688c28325910f
    role: context
  - path: tests/test_causal_review_batch84.py
    sha256: cf4fa49389e6f896cf793474bfada4dd524f39c78909c9c363ad70e1f5a6907c
    role: context
  - path: tests/test_every_ontology_id_resolves.py
    sha256: 65974e9a061790df32b169465ce13fb82fd0503dfd6042fdb7755baf59904bb9
    role: context
  - path: tests/test_phormidium_identity.py
    sha256: 25c770387dec1606153e29715e5c635a69c3b6d6ce0e63d21b5109de6b1dfec7
    role: context
  snapshot_id: review-provenance/20261015-batch132-after-inputs
targets:
- target_id: CommunityMech:000054
  path: kb/communities/Phormidium_Alkaline_Consortium.yaml
  label: Phormidium alkaline consortium
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Phormidium_Alkaline_Consortium.yaml
    role: canonical member and graph participants
- target_id: id-label-policy
  path: conf/id_label_targets.yaml
  label: ID-label correspondence policy
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: conf/id_label_targets.yaml
    role: canonical and export exact-pair exceptions
summary: 'Resolve #2009 across the canonical member, four graph references and two
  policy waivers. Retain the species scope, four bounded nodes and one arrow. The
  broader graph extension and non-graph claims remain open; no corpus-completion or
  independent-approval claim.'
scope:
  description: One member identity, its four graph references, and two exact-pair
    policy exceptions.
  selection: 'Confirmed issue #2009 during Phormidium graph research.'
  coverage: partial
  population_size: 462
  reviewed_target_ids:
  - CommunityMech:000054
  - id-label-policy
  exclusions:
  - target: Other 461 records and other Phormidium member identities
    reason: Not newly assessed.
  - target: Whole-record scores and completion of graph research
    reason: 'Existing #1699 and #1701 remain open; no whole-record metric is inferred.'
checks:
- check_id: preservation
  name: preservation
  status: passed
  required: true
  summary: "{\n  \"records_including_hidden_and_ignored\": 462,\n  \"changed_records\"\
    : [\n    \"kb/communities/Phormidium_Alkaline_Consortium.yaml\"\n  ],\n  \"unchanged_records\"\
    : 461,\n  \"corrected_term_objects\": 5,\n  \"removed_exact_pair_waivers\": 2,\n\
    \  \"graph_topology_and_evidence_preserved\": true,\n  \"old_curation_history_semantically_preserved\"\
    : true,\n  \"canonical_cache_unchanged\": true,\n  \"public_source_hashes_verified\"\
    : 2\n}"
  command: /private/tmp/communitymech-causal-20261014/.venv/bin/python reports/causal_graph_review/20261015-batch132/check_preservation.py
  exit_code: 0
  target_ids:
  - CommunityMech:000054
  - id-label-policy
  evidence_ids:
  - preservation
- check_id: after-regression
  name: after-regression
  status: passed
  required: true
  summary: "......................................................               \
    \    [100%]\n=============================== warnings summary ===============================\n\
    .venv/lib/python3.13/site-packages/linkml/generators/pydanticgen/template.py:553:\
    \ 12 warnings\n  /private/tmp/communitymech-causal-20261014/.venv/lib/python3.13/site-packages/linkml/generators/pydanticgen/template.py:553:\
    \ PydanticDeprecatedSince211: Accessing the 'model_fields' attribute on the instance\
    \ is deprecated. Instead, you should access this attribute from the model class.\
    \ Deprecated in Pydantic V2.11 to be removed in V3.0.\n    imports=imports, **{k:\
    \ getattr(self, k, None) for k in self.model_fields if k != \"imports\"}\n\n--\
    \ Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html\n54 passed,\
    \ 12 warnings in 52.55s"
  command: .venv/bin/python -m pytest tests/test_phormidium_identity.py tests/test_causal_review_batch84.py
    tests/test_causal_review_inventory.py tests/test_participating_taxa.py --no-cov
    -q
  exit_code: 0
  target_ids:
  - CommunityMech:000054
  - id-label-policy
  evidence_ids:
  - after-regression
- check_id: validate
  name: validate
  status: passed
  required: true
  summary: No issues found
  command: just --no-dotenv validate kb/communities/Phormidium_Alkaline_Consortium.yaml
  exit_code: 0
  target_ids:
  - CommunityMech:000054
  - id-label-policy
  evidence_ids:
  - validate
- check_id: strict
  name: strict
  status: passed
  required: true
  summary: Command completed with exit 0; exact output in receipt.
  command: just --no-dotenv validate-strict kb/communities/Phormidium_Alkaline_Consortium.yaml
  exit_code: 0
  target_ids:
  - CommunityMech:000054
  - id-label-policy
  evidence_ids:
  - strict
- check_id: terms
  name: terms
  status: passed
  required: true
  summary: ✅ Validation passed
  command: just --no-dotenv validate-terms kb/communities/Phormidium_Alkaline_Consortium.yaml
  exit_code: 0
  target_ids:
  - CommunityMech:000054
  - id-label-policy
  evidence_ids:
  - terms
- check_id: gtdb-coherence
  name: gtdb-coherence
  status: passed
  required: true
  summary: Command completed with exit 0; exact output in receipt.
  command: just --no-dotenv validate-gtdb kb/communities/Phormidium_Alkaline_Consortium.yaml
  exit_code: 0
  target_ids:
  - CommunityMech:000054
  - id-label-policy
  evidence_ids:
  - gtdb-coherence
- check_id: gtdb-domain
  name: gtdb-domain
  status: passed
  required: true
  summary: 'files checked: 1

    contradictory lineages: 0'
  command: just --no-dotenv validate-gtdb-domain kb/communities/Phormidium_Alkaline_Consortium.yaml
  exit_code: 0
  target_ids:
  - CommunityMech:000054
  - id-label-policy
  evidence_ids:
  - gtdb-domain
- check_id: explicit-excerpts
  name: explicit-excerpts
  status: passed
  required: true
  summary: "{\n  \"record\": \"CommunityMech:000054\",\n  \"native_count\": 21,\n\
    \  \"native_fields\": [\n    \"taxonomy[0].evidence[0].snippet\",\n    \"taxonomy[0].evidence[1].snippet\"\
    ,\n    \"taxonomy[1].evidence[0].snippet\",\n    \"taxonomy[2].evidence[0].snippet\"\
    ,\n    \"taxonomy[3].evidence[0].snippet\",\n    \"taxonomy[4].evidence[0].snippet\"\
    ,\n    \"taxonomy[5].evidence[0].snippet\",\n    \"ecological_interactions[0].evidence[0].snippet\"\
    ,\n    \"ecological_interactions[1].evidence[0].snippet\",\n    \"ecological_interactions[2].evidence[0].snippet\"\
    ,\n    \"ecological_interactions[3].evidence[0].snippet\",\n    \"environmental_factors[0].evidence[0].snippet\"\
    ,\n    \"environmental_factors[1].evidence[0].snippet\",\n    \"environmental_factors[2].evidence[0].snippet\"\
    ,\n    \"environmental_factors[3].evidence[0].snippet\",\n    \"environmental_factors[4].evidence[0].snippet\"\
    ,\n    \"environmental_factors[5].evidence[0].snippet\",\n    \"related_ingredients[0].evidence[0].snippet\"\
    ,\n    \"growth_media[0].evidence[0].snippet\",\n    \"growth_media[0].evidence[1].snippet\"\
    ,\n    \"cultivation_setup[0].evidence[0].snippet\"\n  ],\n  \"explicit_excerpt_count\"\
    : 23,\n  \"native_omitted_discussions\": [\n    \"discussions[0].evidence[0].snippet\"\
    ,\n    \"discussions[0].evidence[1].snippet\"\n  ],\n  \"identity_control_mutation_restoration\"\
    : \"passed\",\n  \"discussion_negative_controls\": \"passed\",\n  \"network_forbidden\"\
    : true,\n  \"limit\": \"Lexical matches do not establish scientific support; known\
    \ Discussion traversal gap #476 is compensated, not fixed.\"\n}"
  command: /private/tmp/communitymech-causal-20261014/.venv/bin/python reports/causal_graph_review/20261015-batch132/check_snippets.py
  exit_code: 0
  target_ids:
  - CommunityMech:000054
  - id-label-policy
  evidence_ids:
  - explicit-excerpts
- check_id: history
  name: history
  status: passed
  required: true
  summary: No issues found
  command: just --no-dotenv validate-history history/records/Phormidium_Alkaline_Consortium
  exit_code: 0
  target_ids:
  - CommunityMech:000054
  - id-label-policy
  evidence_ids:
  - history
- check_id: rank
  name: rank
  status: passed
  required: true
  summary: "rank\tscore\tpath\tid\tname\ttaxonomy\tconnected_taxa\tdisconnected_taxa\t\
    ecological_interactions\tdownstream_edges\tinteraction_evidence\tmissing\tdangling_downstream\t\
    self_downstream\n1\t81.7\tkb/communities/Phormidium_Alkaline_Consortium.yaml\t\
    CommunityMech:000054\tPhormidium Alkaline Consortium\t6\t5\t1\t4\t1\t4\tadditional_downstream,metabolites_or_biological_processes,interaction_type,disconnected_taxa\t\
    0\t0"
  command: just --no-dotenv rank-causal-graphs kb/communities/Phormidium_Alkaline_Consortium.yaml
  exit_code: 0
  target_ids:
  - CommunityMech:000054
  - id-label-policy
  evidence_ids:
  - rank
- check_id: kgx-export
  name: kgx-export
  status: passed
  required: true
  summary: Wrote 1423 nodes / 2177 edges to output/kgx
  command: just --no-dotenv kgx-export
  exit_code: 0
  target_ids:
  - CommunityMech:000054
  - id-label-policy
  evidence_ids:
  - kgx-export
- check_id: products
  name: products
  status: passed
  required: true
  summary: "all configured ontologies are reachable\n\nid↔label correspondence summary:\n\
    \          OK_CANONICAL: 9787\n            OK_SYNONYM: 4\n          OK_EXCEPTION:\
    \ 3\n    SKIPPED_NO_ADAPTER: 924\n\n✅ All id↔label pairs correspond."
  command: just --no-dotenv validate-products
  exit_code: 0
  target_ids:
  - CommunityMech:000054
  - id-label-policy
  evidence_ids:
  - products
- check_id: gen-html
  name: gen-html
  status: passed
  required: true
  summary: "at_CrownRot_TB_CrossKingdom_SynCom.html\n  ✓ Wheat_DT_Rhizosphere_SynCom.yaml\
    \ → /private/tmp/communitymech-causal-20261014/docs/communities/Wheat_DT_Rhizosphere_SynCom.html\n\
    \  ✓ Wheat_Straw_Biogas_Pretreatment_SynCom.yaml → /private/tmp/communitymech-causal-20261014/docs/communities/Wheat_Straw_Biogas_Pretreatment_SynCom.html\n\
    \  ✓ Wheat_SynCom_SASW01_Drought_Inoculant.yaml → /private/tmp/communitymech-causal-20261014/docs/communities/Wheat_SynCom_SASW01_Drought_Inoculant.html\n\
    \  ✓ Wine_Yeast_FiveSpecies_Strain_Substitution_Consortium.yaml → /private/tmp/communitymech-causal-20261014/docs/communities/Wine_Yeast_FiveSpecies_Strain_Substitution_Consortium.html\n\
    \  ✓ Wine_Yeast_ThreeSpecies_Contact_Consortium.yaml → /private/tmp/communitymech-causal-20261014/docs/communities/Wine_Yeast_ThreeSpecies_Contact_Consortium.html\n\
    \  ✓ Wolffia_Mankai_Endosphere_Cobamide_Guild.yaml → /private/tmp/communitymech-causal-20261014/docs/communities/Wolffia_Mankai_Endosphere_Cobamide_Guild.html\n\
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
  - CommunityMech:000054
  - id-label-policy
  evidence_ids:
  - gen-html
- check_id: docs-current
  name: docs-current
  status: passed
  required: true
  summary: "gdom_SynCom.html\n  ✓ Wheat_DT_Rhizosphere_SynCom.yaml → /private/tmp/communitymech-causal-20261014/docs/communities/Wheat_DT_Rhizosphere_SynCom.html\n\
    \  ✓ Wheat_Straw_Biogas_Pretreatment_SynCom.yaml → /private/tmp/communitymech-causal-20261014/docs/communities/Wheat_Straw_Biogas_Pretreatment_SynCom.html\n\
    \  ✓ Wheat_SynCom_SASW01_Drought_Inoculant.yaml → /private/tmp/communitymech-causal-20261014/docs/communities/Wheat_SynCom_SASW01_Drought_Inoculant.html\n\
    \  ✓ Wine_Yeast_FiveSpecies_Strain_Substitution_Consortium.yaml → /private/tmp/communitymech-causal-20261014/docs/communities/Wine_Yeast_FiveSpecies_Strain_Substitution_Consortium.html\n\
    \  ✓ Wine_Yeast_ThreeSpecies_Contact_Consortium.yaml → /private/tmp/communitymech-causal-20261014/docs/communities/Wine_Yeast_ThreeSpecies_Contact_Consortium.html\n\
    \  ✓ Wolffia_Mankai_Endosphere_Cobamide_Guild.yaml → /private/tmp/communitymech-causal-20261014/docs/communities/Wolffia_Mankai_Endosphere_Cobamide_Guild.html\n\
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
  - CommunityMech:000054
  - id-label-policy
  evidence_ids:
  - docs-current
- check_id: lint
  name: lint
  status: passed
  required: true
  summary: 'All checks passed!

    Success: no issues found in 49 source files'
  command: just --no-dotenv lint
  exit_code: 0
  target_ids:
  - CommunityMech:000054
  - id-label-policy
  evidence_ids:
  - lint
- check_id: diff-check
  name: diff-check
  status: passed
  required: true
  summary: Command completed with exit 0; exact output in receipt.
  command: git diff --check
  exit_code: 0
  target_ids:
  - CommunityMech:000054
  - id-label-policy
  evidence_ids:
  - diff-check
- check_id: artifact-identity
  name: artifact-identity
  status: passed
  required: true
  summary: "{\n  \"html\": \"docs/communities/Phormidium_Alkaline_Consortium.html\"\
    ,\n  \"taxonomy_link\": \"3723519\",\n  \"graph_node_id\": \"NCBITaxon:3723519\"\
    ,\n  \"source_name_retained\": true,\n  \"kgx_name\": \"Candidatus Sodalinema\
    \ alkaliphilum\",\n  \"kgx_member_edge_present\": true,\n  \"old_taxon_absent_from_generated_identity_links_nodes_and_edges\"\
    : true,\n  \"limit\": \"Historical notes may name the former identifier; this\
    \ checks active links and identities, not all text occurrences.\"\n}"
  command: .venv/bin/python reports/causal_graph_review/20261015-batch132/check_artifacts.py
  exit_code: 0
  target_ids:
  - CommunityMech:000054
  - id-label-policy
  evidence_ids:
  - artifact-identity
- check_id: review-contract-before
  name: review-contract-before
  status: passed
  required: true
  summary: "{\n  \"repository\": \"culturebotai/CommunityMech\",\n  \"valid_reviews\"\
    : 23,\n  \"coverage\": \"declared_scopes_only\"\n}"
  command: just --no-dotenv check-record-reviews
  exit_code: 0
  target_ids:
  - CommunityMech:000054
  - id-label-policy
  evidence_ids:
  - review-contract-before
- check_id: network-diagnostic
  name: Native zero-warning network diagnostic
  status: failed
  required: false
  summary: Exit 1 for the unchanged pre-existing warning set; exact JSON matches the
    baseline. Not a zero-warning pass.
  command: just --no-dotenv audit-network-json
  exit_code: 1
  target_ids:
  - CommunityMech:000054
  evidence_ids:
  - network
- check_id: reference-cli
  name: Native reference CLI coverage
  status: failed
  required: false
  summary: The command exits 0 but reports zero checks. Explicit offline plugin/excerpt
    validation supplies the actual checked coverage.
  command: just --no-dotenv validate-references-explained kb/communities/Phormidium_Alkaline_Consortium.yaml
  exit_code: 0
  target_ids:
  - CommunityMech:000054
  evidence_ids:
  - explicit-excerpts
- check_id: new-gtdb-assignment
  name: Additional GTDB grounding
  status: unavailable
  required: false
  summary: Configured crosswalk lookup failed. The pre-existing UNRESOLVED status
    is retained; native coherence/domain checks passed without inventing a lineage.
  target_ids:
  - CommunityMech:000054
  evidence_ids:
  - gtdb-coherence
  - gtdb-domain
- check_id: extension-workflow
  name: Required research for new graph structure
  status: unavailable
  required: true
  summary: 'No Edison extension workflow or primary-only substitution was performed
    in this identity repair. Prior open extension scope remains under #1699.'
  target_ids:
  - CommunityMech:000054
  evidence_ids:
  - handoff
- check_id: remote-ci
  name: Remote CI and protected queue
  status: unavailable
  required: true
  summary: Not completed at this immutable local review snapshot; required checks
    must pass before merge.
  target_ids:
  - CommunityMech:000054
  - id-label-policy
  evidence_ids:
  - after-regression
evidence:
- evidence_id: ncbi
  kind: database
  reference: reports/causal_graph_review/sources/20261015-phormidium-identity-batch132/ncbi-taxonomy.xml
  locator: Taxon 2293317/AkaTaxIds, 3723519/name and synonym, 2839084/parent and rank
  accessed_at: '2026-10-15T01:09:00.508795Z'
  support: refutes
  summary: Legacy 1807132 resolves to a Bacillota/Clostridia species, not the cyanobacterium.
    The source name is a synonym of cyanobacterial species 3723519; PBR-2020 is its
    child strain 2839084.
- evidence_id: oak
  kind: database
  reference: reports/causal_graph_review/sources/20261015-phormidium-identity-batch132/oak-taxonomy.json
  locator: Selected statements; ontology version 2026-07-12
  accessed_at: '2026-10-15T01:12:16.472646Z'
  support: supports
  summary: The installed ontology independently represents the same legacy alias,
    species canonical label and source-name synonym; neither replacement candidate
    needs a missing-term waiver in this snapshot.
- evidence_id: paper2022
  kind: primary_source
  reference: doi:10.3389/fmicb.2022.780346
  locator: Results, community composition; five metagenomes from different cultures/time
    points; distinct OSCR comparison
  accessed_at: '2026-10-15T01:12:16.472646Z'
  support: supports
  summary: The named Phormidium population is the only cyanobacterium and the most
    abundant member. The combined record spans multiple conditions and sampling times,
    not one isolated strain.
- evidence_id: paper2021
  kind: primary_source
  reference: PMID:34877483
  locator: https://pmc.ncbi.nlm.nih.gov/articles/PMC8633866/ ; identity/strain Results
    p0085-p0110, conclusion p0205, limitations p0215, data availability p0255
  accessed_at: '2026-10-15T01:12:16.472646Z'
  support: supports
  summary: Species naming, persistent strain diversity and the PBR-2020 reference-genome
    accession support species-level grounding while retaining the publication name;
    one reference strain must not absorb all conditions.
- evidence_id: canonical
  kind: record_content
  reference: kb/communities/Phormidium_Alkaline_Consortium.yaml
  locator: taxonomy[0], four graph references, appended history and unchanged remaining
    graph; policy has two fewer exceptions
  accessed_at: '2026-10-15T01:40:50.304367Z'
  support: supports
  summary: Five corrected species pairs retain the publication name. Identity notes
    distinguish the reference strain and species population. A short exact member-identity
    excerpt is appended; all existing graph evidence and topology are unchanged.
- evidence_id: before
  kind: prior_review
  reference: reviews/structured/20261015T011216Z-phormidium-identity-before/review.yaml
  locator: wrong-cyanobacterial-id
  accessed_at: '2026-10-15T01:40:50.304367Z'
  support: context_only
  summary: Immutable predecessor establishes the wrong-organism identifier and two
    stale exact-pair waivers.
- evidence_id: handoff
  kind: prior_review
  reference: reviews/structured/20261014T235318Z-causal-prompt-phormidium-after/review.yaml
  locator: phormidium-coverage and source assessment from batch131
  accessed_at: '2026-10-15T01:40:50.304367Z'
  support: partial
  summary: Seven candidate niches and four source discrepancies remain a research
    handoff, not completed extension. Correcting one participant identity does not
    resolve all MAG mapping or source conflicts.
- evidence_id: preservation
  kind: validation
  reference: reports/causal_graph_review/20261015-batch132/preservation.json
  locator: command, hashes, timestamps, exit_code, stdout and stderr
  accessed_at: '2026-10-15T01:40:50.304367Z'
  support: supports
  summary: Actual command receipt for preservation
- evidence_id: after-regression
  kind: validation
  reference: reports/causal_graph_review/20261015-batch132/final-regression.json
  locator: command, hashes, timestamps, exit_code, stdout and stderr
  accessed_at: '2026-10-15T01:40:50.304367Z'
  support: supports
  summary: Actual command receipt for after-regression
- evidence_id: validate
  kind: validation
  reference: reports/causal_graph_review/20261015-batch132/validate.json
  locator: command, hashes, timestamps, exit_code, stdout and stderr
  accessed_at: '2026-10-15T01:40:50.304367Z'
  support: supports
  summary: Actual command receipt for validate
- evidence_id: strict
  kind: validation
  reference: reports/causal_graph_review/20261015-batch132/strict.json
  locator: command, hashes, timestamps, exit_code, stdout and stderr
  accessed_at: '2026-10-15T01:40:50.304367Z'
  support: supports
  summary: Actual command receipt for strict
- evidence_id: terms
  kind: validation
  reference: reports/causal_graph_review/20261015-batch132/terms.json
  locator: command, hashes, timestamps, exit_code, stdout and stderr
  accessed_at: '2026-10-15T01:40:50.304367Z'
  support: supports
  summary: Actual command receipt for terms
- evidence_id: gtdb-coherence
  kind: validation
  reference: reports/causal_graph_review/20261015-batch132/gtdb-coherence.json
  locator: command, hashes, timestamps, exit_code, stdout and stderr
  accessed_at: '2026-10-15T01:40:50.304367Z'
  support: supports
  summary: Actual command receipt for gtdb-coherence
- evidence_id: gtdb-domain
  kind: validation
  reference: reports/causal_graph_review/20261015-batch132/gtdb-domain.json
  locator: command, hashes, timestamps, exit_code, stdout and stderr
  accessed_at: '2026-10-15T01:40:50.304367Z'
  support: supports
  summary: Actual command receipt for gtdb-domain
- evidence_id: explicit-excerpts
  kind: validation
  reference: reports/causal_graph_review/20261015-batch132/explicit-excerpts.json
  locator: command, hashes, timestamps, exit_code, stdout and stderr
  accessed_at: '2026-10-15T01:40:50.304367Z'
  support: supports
  summary: Actual command receipt for explicit-excerpts
- evidence_id: history
  kind: validation
  reference: reports/causal_graph_review/20261015-batch132/history.json
  locator: command, hashes, timestamps, exit_code, stdout and stderr
  accessed_at: '2026-10-15T01:40:50.304367Z'
  support: supports
  summary: Actual command receipt for history
- evidence_id: rank
  kind: validation
  reference: reports/causal_graph_review/20261015-batch132/rank.json
  locator: command, hashes, timestamps, exit_code, stdout and stderr
  accessed_at: '2026-10-15T01:40:50.304367Z'
  support: supports
  summary: Actual command receipt for rank
- evidence_id: kgx-export
  kind: validation
  reference: reports/causal_graph_review/20261015-batch132/kgx-export.json
  locator: command, hashes, timestamps, exit_code, stdout and stderr
  accessed_at: '2026-10-15T01:40:50.304367Z'
  support: supports
  summary: Actual command receipt for kgx-export
- evidence_id: products
  kind: validation
  reference: reports/causal_graph_review/20261015-batch132/products.json
  locator: command, hashes, timestamps, exit_code, stdout and stderr
  accessed_at: '2026-10-15T01:40:50.304367Z'
  support: supports
  summary: Actual command receipt for products
- evidence_id: gen-html
  kind: validation
  reference: reports/causal_graph_review/20261015-batch132/gen-html.json
  locator: command, hashes, timestamps, exit_code, stdout and stderr
  accessed_at: '2026-10-15T01:40:50.304367Z'
  support: supports
  summary: Actual command receipt for gen-html
- evidence_id: docs-current
  kind: validation
  reference: reports/causal_graph_review/20261015-batch132/docs-current-final.json
  locator: command, hashes, timestamps, exit_code, stdout and stderr
  accessed_at: '2026-10-15T01:40:50.304367Z'
  support: supports
  summary: Actual command receipt for docs-current
- evidence_id: lint
  kind: validation
  reference: reports/causal_graph_review/20261015-batch132/lint-final.json
  locator: command, hashes, timestamps, exit_code, stdout and stderr
  accessed_at: '2026-10-15T01:40:50.304367Z'
  support: supports
  summary: Actual command receipt for lint
- evidence_id: diff-check
  kind: validation
  reference: reports/causal_graph_review/20261015-batch132/diff-check.json
  locator: command, hashes, timestamps, exit_code, stdout and stderr
  accessed_at: '2026-10-15T01:40:50.304367Z'
  support: supports
  summary: Actual command receipt for diff-check
- evidence_id: artifact-identity
  kind: validation
  reference: reports/causal_graph_review/20261015-batch132/artifact-identity.json
  locator: command, hashes, timestamps, exit_code, stdout and stderr
  accessed_at: '2026-10-15T01:40:50.304367Z'
  support: supports
  summary: Actual command receipt for artifact-identity
- evidence_id: review-contract-before
  kind: validation
  reference: reports/causal_graph_review/20261015-batch132/review-contract-before.json
  locator: command, hashes, timestamps, exit_code, stdout and stderr
  accessed_at: '2026-10-15T01:40:50.304367Z'
  support: supports
  summary: Actual command receipt for review-contract-before
- evidence_id: network
  kind: validation
  reference: reports/causal_graph_review/20261015-batch132/network.json
  locator: Baseline-equivalent JSON and actual exit 1
  accessed_at: '2026-10-15T01:40:50.304367Z'
  support: context_only
  summary: Unchanged warnings do not establish scientific completeness or justify
    adding unsupported arrows.
assessments:
- assessment_id: identity
  area: identity
  topic: Species identity preserves multi-strain source scope
  outcome: supported
  summary: The cyanobacterial member and all four graph references now use the canonical
    species ID/label, retain the source name, and distinguish PBR-2020 from the whole
    population.
  target_ids:
  - CommunityMech:000054
  evidence_ids:
  - ncbi
  - oak
  - paper2021
  - paper2022
  - canonical
  - after-regression
  - terms
- assessment_id: policy
  area: grounding
  topic: Wrong-organism waivers removed without weakening enforcement
  outcome: supported
  summary: Only the two obsolete exact-pair exceptions were removed. Canonical and
    KGX surfaces pass the native product validator without a replacement waiver.
  target_ids:
  - id-label-policy
  evidence_ids:
  - canonical
  - preservation
  - products
  - artifact-identity
- assessment_id: retained-graph
  area: graph
  topic: Evidence-bounded existing nodes and arrow
  outcome: supported
  summary: Retain measured carbon transfer, the PARTIAL genomic polymer-use hypothesis
    and qualified low-peptide alphaproteobacterial evidence. Identity correction does
    not strengthen mechanistic claims or add topology.
  target_ids:
  - CommunityMech:000054
  evidence_ids:
  - paper2022
  - canonical
  - preservation
  - explicit-excerpts
- assessment_id: coverage
  area: completeness
  topic: Unfinished source and niche reconciliation
  outcome: concern
  summary: A corrected cyanobacterial ID is not completion of seven niche candidates,
    MAG reconciliation, source conflicts or non-graph claims. Keep needs_research
    and the existing follow-ups open.
  target_ids:
  - CommunityMech:000054
  evidence_ids:
  - handoff
  - canonical
  - paper2022
findings:
- finding_id: wrong-cyanobacterial-id
  issue_key: communitymech-2009-phormidium-identity
  category: identity
  severity: blocker
  status: resolved
  certainty: confirmed
  title: Cyanobacterial graph references point to an unrelated organism
  description: 1807132 is an alternative ID for Syntrophocurvum, not Phormidium/Sodalinema.
    Five maintained fields and two policy waivers require coordinated repair.
  target_ids:
  - CommunityMech:000054
  - id-label-policy
  field_paths:
  - taxonomy[0].taxon_term.term
  - ecological_interactions[0,2,3].source_taxon.term
  - ecological_interactions[1].participating_taxa[0].term
  - targets[communities_yaml,kgx_nodes].exceptions
  evidence_ids:
  - ncbi
  - oak
  - paper2021
  - paper2022
  - canonical
  - before
  - after-regression
  - preservation
  - products
  - artifact-identity
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Phormidium_Alkaline_Consortium.yaml
    role: canonical member and graph participants
  - repository: CultureBotAI/CommunityMech
    path: conf/id_label_targets.yaml
    role: canonical and export exact-pair exceptions
  rule_id: causal-participant-identity
  native_severity: P1
  normalization_reason: The identifier makes the graph denote the wrong organism,
    not merely a stale label.
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/2009
  disposition_reason: Five species groundings corrected and two stale waivers removed,
    with canonical label, source-population scope, preserved graph, regression controls
    and native product gates verified.
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261015T011216Z-phormidium-identity-before
    finding_id: wrong-cyanobacterial-id
- finding_id: phormidium-coverage
  issue_key: communitymech-1699-coverage
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Phormidium niche coverage remains incomplete
  description: The bounded four-node graph does not yet represent the source's other
    proposed ecological niches. Source conflicts and MAG-level participant reconciliation
    must be assessed before adding supported structure; a connected graph is not itself
    the acceptance criterion.
  target_ids:
  - CommunityMech:000054
  field_paths:
  - ecological_interactions
  - discussions / graph extension knowledge gap
  evidence_ids:
  - paper2022
  - handoff
  - canonical
  rule_id: causal-graph-evidence-coverage
  native_severity: P2
  normalization_reason: Material missing evidence-backed graph coverage, already tracked
    as needs_research; no new unsupported edge is alleged.
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Phormidium_Alkaline_Consortium.yaml
    role: canonical record
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/1699
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261014T235318Z-causal-prompt-phormidium-after
    finding_id: phormidium-coverage
actions:
- action_id: extend-phormidium
  description: Complete authorized one-community research, reconcile MAG/source discrepancies
    and curate only supported graph structure.
  finding_ids:
  - phormidium-coverage
  target_ids:
  - CommunityMech:000054
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Phormidium_Alkaline_Consortium.yaml
    role: canonical record
  acceptance_checks:
  - Obtain the one-community Edison research report required by the invoked skill,
    or explicit authorization to use direct-primary-source research in its place.
  - Keep the corrected prompt and explicit warning about non-graph context claims
    tracked in issue 1701.
  - Resolve MAG-level participant mapping against source taxonomy and canonical identifiers
    without transferring related-species phenotypes.
  - Verify exact snippets and keep supplemental evidence separate from article caches.
  - Apply only supported nodes/arrows with guarded writes, append-only history, validators,
    generated-doc checks and a successor review.
limitations:
- Partial source-based self-review, not independent approval, whole-record certification
  or corpus completion; 54 records remain needs_research.
- Native completeness/quality metrics are not computed for this one-member identity
  repair. Readiness score is structural only.
- The 2021 article is read in bounded identity/strain spans; raw data, all supplementary
  files and other member groundings are not recertified.
- GTDB crosswalk was unavailable in the configured locations. Bounded ignored-inclusive
  directory searches had permission-denied areas; no claim of global absence is made.
- The reference CLI reports zero checks; explicit plugin traversal and Discussion
  compensation are recorded. Lexical matching does not prove scientific support.
- Initial failing regressions, guarded rejection of an invalid evidence-source enum
  and a formatting-boundary failure are retained as historical receipts, not final
  passes. Both failed writes left the canonical bytes unchanged.
- Initial lint errors were corrected and rerun. The first docs-current run rejected
  the uncommitted generated page; the final native run verifies the committed page.
  Earlier failed receipts remain unchanged.
- The first committed docs-current retry failed before rendering because nested just
  requires JUST_NO_DOTENV=true rather than 1. The corrected invocation propagates
  true, retains the failure receipt, and does not read dotenv files.
- 'No new nodes/arrows, provider submission or paid research. Wider extension and
  #1701 non-graph issues remain open.'
- Remote CI and queue acceptance are pending at this immutable input snapshot; later
  publication receipts must verify them separately.
links:
- https://github.com/CultureBotAI/CommunityMech/issues/2009
- https://github.com/CultureBotAI/CommunityMech/issues/1699
- https://github.com/CultureBotAI/CommunityMech/issues/1701
tags:
- batch132
- causal-graphs
- self-review
```
