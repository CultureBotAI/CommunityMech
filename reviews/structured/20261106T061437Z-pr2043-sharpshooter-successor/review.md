# Sharpshooter BioModels record: current-main review successor

- Review: 20261106T061437Z-pr2043-sharpshooter-successor
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-11-06T06:05:51.976535Z
- Finished UTC: 2026-11-06T06:14:37.011891Z
- Reviewer: codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Current main adds a supported broad animal-associated environment and matching embedded history. Fresh primary main text, figures, supplementary methods, focal tables and deposited model metadata retain all four original findings: host membership and unsupported ecological STABLE (P2), structured computational provenance and publication-as-dataset organization (P3). A new P3 identifies an unrelated PMID in the external environment-history sidecar. The environment addition itself remains valid. Eight focused checks pass; corpus network checks report 44 warnings across 16 of 508 records, with no target-native issues. No simulation was rerun.

## Scope And Provenance

Entire current target and its two history sidecars; three qualified interaction nodes, zero downstream arrows and all nine source snippets. Fresh complete primary scientific main, all seven main and three supplementary figures, full Text S1, focal S1e/f/g and S1h/i rows, S5o run bounds, S6 model headers, BioModels metadata/SBML and focal BioProject metadata. Supplement workbook extraction is broader than the human-assessed slices; no exhaustive reaction-list or executable-model audit.

Selection: Refresh stale CommunityMech:000007 in PR 2043 against merged main. Environment and one embedded history event are the only canonical delta; every original finding is reassessed with its stable key and exact predecessor.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base c1846ce378828d0a2e2d80312ac784a47430a617.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000007 | kb/communities/BioModels_MODEL1806250004_Sharpshooter_Sulcia_Baumannia.yaml | maintained | BioModels MODEL1806250004 Sharpshooter Sulcia-Baumannia Symbiosis |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000007 | Target schema validation passed. |
| validate-strict | passed | True | CommunityMech:000007 | Target strict validation passed. |
| validate-terms | passed | True | CommunityMech:000007 | Target term validation passed. |
| validate-gtdb | passed | True | CommunityMech:000007 | Target GTDB syntax/status validation passed. |
| validate-gtdb-domain | passed | True | CommunityMech:000007 | Target GTDB domain validation passed. |
| validate-history | passed | True | CommunityMech:000007 | Target history validation passed. |
| normalize-cache-names-check | passed | True | CommunityMech:000007 | Read-only corpus cache-filename preflight passed. |
| validate-references-explained | passed | True | CommunityMech:000007 | Target reference validation passed against the pinned cache. |
| audit-network | failed | True | CommunityMech:000007 | Fresh corpus check reports 44 baseline warnings across 16 of 508 records; the focal native audit is empty. |
| check-network-quality | failed | True | CommunityMech:000007 | Fresh corpus check reports 44 baseline warnings across 16 of 508 records; the focal native audit is empty. |
| Primary publication and model identity | passed | True | CommunityMech:000007 | Fresh public source identity, model metadata and declared scientific slices inspected by the author; no executable reproduction. |
| Whole-record scientific assessment | passed | True | CommunityMech:000007 | Fresh public source identity, model metadata and declared scientific slices inspected by the author; no executable reproduction. |
| Encoded medium and ingredient links | not_applicable | False | CommunityMech:000007 | No CultureMech or MediaIngredientMech identifier is encoded; simulated hemolymph is not a wet-lab culture recipe. |
| Structured source catalog applicability | not_applicable | False | CommunityMech:000007 | Fresh iModulonDB organism catalog has no focal partner or insect dataset; no target-module claim was inferred. |

## Scientific And Domain Assessments

### Exact model and biological actors

identity: concern. Targets: CommunityMech:000007.

MODEL1806250004 is the intended iNA629 sharpshooter model; the host should remain external to microbial membership.

### Membership, roles and names

grounding: concern. Targets: CommunityMech:000007.

Remove the host from the membership list while retaining its supported graph endpoints.

The microbial partners and broad syntrophic-metabolism roles are compatible with model-predicted cooperative metabolism. No extra obligacy or product-removal test is imported into these broad category/role definitions. The current source-based bacterial ranks are retained; no unverified exact strain or extra taxon is added. Historical GTDB mapping statistics were not re-certified.

### ecological_interactions[0]: Sulcia provisioning

graph: supported. Targets: CommunityMech:000007.

Retain the COMPUTATIONAL Sulcia → G. coccinea provisioning and modeled reciprocal benefit.

Eight EAA exports, including the two encoded L-amino acids, support the node. The nitrogen percentage is weighted transport flux relative to host-derived nitrogen input, not concentration or a tracer measurement. The current 66–80% wording is explicitly pooled across systems; the sharpshooter figure/table is approximately 66%. No downstream arrow is needed.

### ecological_interactions[1]: Baumannia complementarity

graph: supported. Targets: CommunityMech:000007.

Retain the COMPUTATIONAL Baumannia → G. coccinea model interpretation and its limitations.

The two exported EAAs are histidine and methionine. The approximately 10% nitrogen return is not the separate 8% contribution to total EAA release. Host support and three Sulcia-to-Baumannia intermediates are modeled; they prevent an absolute segregation claim. Host regulatory control remains PARTIAL.

### ecological_interactions[2]: Host-mediated complementarity

graph: supported. Targets: CommunityMech:000007.

Retain community-level modeled reciprocal nutrition with PARTIAL host-control interpretation.

The modeled actors are Sulcia, Baumannia and their host; three intermediates (homoserine, LL-2,6-diaminoheptanedioate and 3-methyl-2-oxobutanoate) pass from Sulcia to Baumannia through the modeled host compartment. This does not experimentally establish host regulation or absence of bacterial cross-feeding. The broad GO:0044419 term is compatible with interspecies processes. The existing zero-arrow graph correctly avoids component-to-summary causation.

### Ecological state versus computational steady state

evidence: concern. Targets: CommunityMech:000007.

STABLE is not established as ecological equilibrium by the inspected source.

The source describes an ancient, vertically transmitted natural association and optimizes constrained metabolic fluxes. It does not measure community dynamics or recovery to equilibrium. NATURAL remains appropriate to the modeled biological association; creating a model does not imply ENGINEERED biological origin.

### Structured computational provenance

completeness: concern. Targets: CommunityMech:000007.

Recoverable model/run settings remain only in source text and the existing discussion.

Record FBA/FVA, COBRA Toolbox 3.0, MATLAB/Gurobi without invented versions, iNA629 and source accessions, objective and simulated hemolymph. Distinguish ordinary growth from maintenance-cost simulations. BioModels glucose/ammonium defaults of −1000 differ from published −100 run bounds; stored zero flux fields are not observed optimal outputs. The discussion already captures important assumptions and should be preserved.

### Models, publication and input data

completeness: concern. Targets: CommunityMech:000007.

The model file is valid; the primary publication belongs in evidence/resources rather than as a dataset.

PRJNA341855 is the focal sharpshooter project; PRJNA342845 and PRJNA343314 are other insect systems. The author repository is pinned to commit bb20c83c112331442b19a7b5f16f6cd6389221b4. Its model blob differs bytewise from BioModels; identity is supported, but scientific or executable equivalence was not tested. NON_CURATED is archive status, not proof of an invalid model.

### Snippets and previous graph repairs

provenance: concern. Targets: CommunityMech:000007.

Original graph qualifications and all nine source snippets remain supported, but the new external environment-history event cites an unrelated paper.

The MD cache remains labeled abstract_only despite appended main text; the TXT is abstract/bibliographic material. Fresh full XML and PubMed were independently matched. The external sidecar requires append-only correction; its historical bytes must not be rewritten. No current GitHub issue status is inferred from the predecessor.

### Native checks and source assessment

schema: supported. Targets: CommunityMech:000007.

All eight native checks pass; semantic and evidence findings remain despite those passes.

### Native completeness and quality

completeness: supported. Targets: CommunityMech:000007.

Mechanical scores do not certify host membership, equilibrium or simulation reproducibility.

### Current-main habitat addition and bounded prior disposition

grounding: supported. Targets: CommunityMech:000007.

The new broad ENVO term and focal insect note match primary host-associated modeling context; the earlier grouped missing-field resolution is preserved.

The environment is natural intracellular symbiosis represented computationally, not a wet-lab medium or evidence of ecological equilibrium. The single-target review does not retire a multi-target predecessor. Correcting the sidecar source attribution is separate from retaining this field.

## Findings

### host-membership: Separate the insect host from microbial membership

major / open / confirmed; issue key: cm-000007-host-membership.

taxonomy[0] contains G. coccinea despite the schema excluding hosts from the microbial roster.

### ecological-equilibrium: Qualify the unsupported STABLE designation

major / open / confirmed; issue key: cm-000007-ecological-equilibrium.

The source supports a natural symbiosis and steady-state metabolic predictions, not the ecological equilibrium asserted by STABLE.

### computational-provenance: Structure the model and run assumptions

minor / open / confirmed; issue key: cm-000007-computational-provenance.

The eight interaction evidence items lack computational_provenance despite recoverable methods and existing narrative assumptions.

### resource-types: Separate the publication from study resources

minor / open / confirmed; issue key: cm-000007-resource-types.

The Primary publication entry is classified as an associated dataset, while verified focal input/repository links remain unstructured.

### environment-history-source: Append a correction for the environment-history source PMID

minor / open / confirmed; issue key: cm-000007-environment-history-source.

history/records/BioModels_MODEL1806250004_Sharpshooter_Sulcia_Baumannia/2026-10-25T151200Z-antigravity-2072.yaml:events[0].details attributes the environment addition to PMID:29944653, an unrelated human clinical questionnaire study. The target environment_term.notes and actual insect model source use PMID:30254121. Preserve the original event and append a precise corrective provenance entry.

## Recommended Actions And Acceptance Checks

### repair-host-membership

Separate the insect host from microbial membership.

- Remove the insect from microbial taxonomy during authorized curation; retain Sulcia and Baumannia as microbial members.
- Preserve G. coccinea as the external recipient/participant in the model graph and narrative. Do not delete the host compartment from the scientific interpretation.
- Do not reinsert the host merely to satisfy external-participant network warnings; assess those warnings against the schema.

### repair-ecological-equilibrium

Qualify the unsupported STABLE designation.

- Supply ecological evidence for stable equilibrium or explicitly document the unresolved state; distinguish long evolutionary association from demonstrated equilibrium.
- Do not automatically substitute ENGINEERED or TRANSIENT: neither follows from creating a metabolic model.
- If the required enum cannot represent uncertainty truthfully, record the bounded schema issue for separately authorized follow-up rather than inventing biological dynamics.

### repair-computational-provenance

Structure the model and run assumptions.

- Populate claim-level computational provenance with FBA/FVA, COBRA Toolbox 3.0, MATLAB/Gurobi, iNA629, model source/input accession and modeled bacteriocyte/hemolymph context; leave unreported software versions unset.
- Preserve oxygen uptake 20, published run uptake caps, equal bacterial biomass lower bounds 0.01, objective and transport-cost assumptions with their units and source scope. Distinguish maintenance-cost simulations from baseline growth.
- Retain the discrepancy between deposited exchange bounds and published runtime settings, and S5o cystathionine versus closed proteinogenic-amino-acid exchanges. Do not turn default zero FLUX_VALUE entries into results.
- Keep wet-lab growth_media absent; retain the existing discussion and all three qualified nodes with no arrows.

### repair-resource-types

Separate the publication from study resources.

- Move PMID:30254121 to an appropriate publication/evidence resource; preserve the actual BioModels MODEL1806250004 file entry.
- Link the verified focal PRJNA341855 host-transcriptome/symbiont-genome project and immutable author repository commit with their exact host/model scope. Do not import the two other insect projects as focal data.
- Keep archive status, byte differences and unexecuted model boundaries explicit; do not claim raw-data inspection, reproducibility or strain-resolution from this metadata check.

### preserve-model-graph

Preserve computational scope and the three-node, zero-arrow graph during separately authorized curation.

- Keep host-mediated regulation PARTIAL, the three bacterial exchanges explicit and all nitrogen quantities source-scoped.
- Do not restore component-to-summary arrows or assert measured transfer, fitness, equilibrium or model reproducibility.
- Preserve append-only history and rerun schema, strict, term, reference, history and target/corpus network checks after authorized changes.
- Keep insect_model_nitrogen_and_host_control as an explicit source-boundary discussion. Any future evidence update must distinguish measured transfer/regulation from model predictions; no new experiment, paid research or author contact is requested.

### correct-environment-history-source

During separately authorized curation, append a correction identifying the erroneous historical source citation.

- Create a new history entry for CommunityMech:000007 naming history/records/BioModels_MODEL1806250004_Sharpshooter_Sulcia_Baumannia/2026-10-25T151200Z-antigravity-2072.yaml:events[0].details, its incorrect PMID:29944653, and the supported replacement PMID:30254121.
- Preserve the original historical file byte-for-byte; explain that the canonical environment field and embedded citation were already supported and remain unchanged.
- Keep the resolved grouped missing-environment disposition intact and retain the four unrelated original findings until their separate curation is verified.
- Validate the new history entry, inspect the append-only diff and verify no unsupported ecological-state or host-membership promotion.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | kb/communities/BioModels_MODEL1806250004_Sharpshooter_Sulcia_Baumannia.yaml; Whole record: three taxonomy entries, three nodes, zero arrows, two dataset entries | supports | The intended sharpshooter model is identifiable and its graph is qualified; microbial membership, ecological state and structured provenance require follow-up. |
| pubmed | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=30254121&amp;retmode=xml; Article-level metadata | supports | Article-level PMID, DOI, title and abstract are verified. |
| crossref | https://api.crossref.org/works/10.1128/mBio.01433-18; Article-level metadata | supports | DOI, publication title and bibliographic identity are verified. |
| epmc | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:30254121&amp;format=json&amp;resultType=core; Article-level metadata | supports | Article-level identifiers and the open-access full-text route are verified. |
| sulcia | PMID:30254121; Fresh XML s2, Metabolic outputs and metabolic cost subsections; Figures 2a/d/g and 7b; Table S1f and S1i rows 56–84 | supports | The sharpshooter model releases eight Sulcia essential amino acids. Nitrogen-weighted output is about 66% in this model; 66–80% is the explicitly pooled three-system range. |
| baumannia | PMID:30254121; Fresh XML s2, Metabolic outputs and metabolic cost subsections; Figures 2a/d/g and 7b; Table S1f and S1i rows 87–121 | supports | Baumannia exports histidine and methionine, complementing the eight Sulcia EAAs; approximately 10% refers to returned EAA nitrogen relative to host-derived input. |
| reciprocal | PMID:30254121; Fresh XML s2, Metabolic inputs and cross-feeding paragraphs; s3 Discussion; Figure 4 organism-labeled sharpshooter panel a | partial | The model predicts extensive host–symbiont exchange and three Sulcia-to-Baumannia intermediates serving methionine, peptidoglycan and pantothenate synthesis. Host regulatory control remains a hypothesis. |
| methods | PMID:30254121; Fresh XML s4, The insects, Metabolic model reconstruction and analysis, Calculation of symbiont maintenance costs and data statements | supports | Field-derived bacteriome genomes/transcriptomes inform iNA629; COBRA Toolbox 3.0, MATLAB and Gurobi support FBA/FVA. The simulations are not a wet-lab coculture or ecological stability experiment. |
| inference | PMID:30254121; Fresh XML s3, opening Discussion paragraph; s1 vertical-transmission background | partial | The paper frames model outputs as hypotheses for empirical testing. Long-standing vertically transmitted associations do not themselves demonstrate a stable ecological equilibrium for this record. |
| supplement | PMID:30254121; Text S1, all modeling methods; Table S1f, focal S1h/S1i/S5o rows and S6d; all three supplementary figures; fresh EPMC supplementaryFiles archive, Text S1 and all three SI figures; table-audit.json preserves extraction with focal human-reading scope stated separately | supports | Supplementary constraints and tabulated predicted fluxes support the bounded graph. S5o gives run-specific exchange bounds; this is simulated hemolymph, not a culture recipe. |
| schema | src/communitymech/schema/communitymech.yaml; MicrobialCommunity.taxonomy; EcologicalStateEnum; CommunityCategoryEnum; FunctionalRoleEnum; EvidenceSourceEnum; ComputationalProvenance | supports | Hosts are excluded from microbial membership but allowed as outside interaction participants. STABLE requires equilibrium; computational provenance has dedicated model, tools, input and simulated-medium fields. |
| ontology | kb/communities/BioModels_MODEL1806250004_Sharpshooter_Sulcia_Baumannia.yaml; .temp/pr2043/insects/000007/replay-qualified.json | supports | All seven unique curated term pairs across eleven occurrences match local OAK labels; fresh NCBI independently confirms all focal taxon names and OLS confirms ENVO:01001002. Label validity does not establish microbial membership. |
| snippets | kb/communities/BioModels_MODEL1806250004_Sharpshooter_Sulcia_Baumannia.yaml; .temp/pr2043/insects/000007/replay-qualified.json | supports | All nine excerpts match fresh primary sources after NFKC/whitespace normalization: eight interaction snippets occur in the full article XML and the resource quotation is the exact punctuated PubMed title. The initial article-only replay correctly misses that PubMed-specific terminal period; the qualified replay preserves source boundaries. |
| history | history/records/BioModels_MODEL1806250004_Sharpshooter_Sulcia_Baumannia/2026-10-25T151200Z-antigravity-2072.yaml; events[0].details, compared with current environment_term.notes and embedded curation_history[1] | supports | The new external history sidecar wrongly cites PMID:29944653 for the insect environment addition. That PMID resolves to an unrelated human urinary-symptom questionnaire study. The current record correctly cites insect modeling paper PMID:30254121; the source-backed ENVO addition and grouped missing-field resolution remain valid. |
| resources | kb/communities/BioModels_MODEL1806250004_Sharpshooter_Sulcia_Baumannia.yaml; Fresh MODEL1806250004 metadata and file list; verified SBML payload, focal BioProject XML, immutable author tree/payload at bb20c83c112331442b19a7b5f16f6cd6389221b4 | supports | BioModels file identity is verified; focal project PRJNA341855 and the immutable author repository are distinct resources. PMID:30254121 is a publication, not a dataset deposit. |
| model-boundary | kb/communities/BioModels_MODEL1806250004_Sharpshooter_Sulcia_Baumannia.yaml; .temp/pr2043/insects/shared/model-audit.json: focal model identity, archive digest, compartments and selected exchange bounds | context_only | Read-only SBML inspection distinguishes three biological actors, extracellular compartment, stored defaults and published run constraints; it does not reproduce the simulation. |
| native-target | kb/communities/BioModels_MODEL1806250004_Sharpshooter_Sulcia_Baumannia.yaml; .temp/pr2043/insects/000007/replay-qualified.json | supports | Target-native audit returns no issues for the three-node, zero-arrow graph; eight interaction evidence occurrences are counted separately from one resource-title citation. Structural consistency does not certify equilibrium or membership. |
| source-scope | PMID:30254121; Fresh shared retrieval receipts and archive-inventory.json; article Sections 1–4, all main/SI figures, Text S1 and focal table/model slices | supports | The author read fresh primary main text and the stated asset slices. Supplement bytes and model identity were independently retrieved in this author pass; computational outputs were not recomputed, raw sequences were not inspected, and no independent approval is claimed. |
| search | Owned maintained roots; .temp/pr2043/insects/000007/local-search.stdout.txt | supports | Ignored-inclusive exact ID/slug and source-PMID search found source caches, target sidecars and relevant graph-decision files. No focal match was returned from kb/taxa; this bounded result does not establish machine-wide absence. |
| adapter | https://imodulondb.org/api/datasets; Fresh public organism/dataset catalog | supports | The structured iModulonDB catalog has no Sulcia/Karelsulcia, Sodalis, Baumannia/Palibaumannia, Hodgkinia or focal insect entry. E. coli is a reconstruction reference, not the focal symbiosis; its expression modules do not establish insect-host mechanisms. No matching module query is applicable and catalog absence is not negative biological evidence. |
| current-delta | kb/communities/BioModels_MODEL1806250004_Sharpshooter_Sulcia_Baumannia.yaml; .temp/pr2043/insects/000007/target-diff.stdout.txt | supports | Only environment_term and the corresponding embedded history event were added; the four previously flagged fields remain unchanged. |
| environment-authority | https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FENVO_01001002; Fresh ENVO:01001002 label and definition plus primary Introduction/Methods and Figure 1 | supports | ENVO:01001002 is animal-associated environment, an environmental system determined by an animal. The broad term fits the modeled intracellular insect bacteriome; the preferred term supplies host detail without claiming a more specific ENVO identity. |
| history-wrong-source | PMID:29944653; Fresh PubMed ArticleTitle and Abstract, compared with external history events[0].details | refutes | This identifier denotes a clinical comparison of nocturia and prostate-symptom questionnaires in men, not insect endosymbiont modeling. PMID:30254121 supplies the supported focal environment context. |
| environment-lineage | reviews/structured/20261025T161500Z-c2s5-remediation-verification/review.yaml; c2s4-biomodels-missing-environment-term, including its two exact c2s4 grouped predecessors | context_only | The resolved grouped finding covers 000006, 000007, 000008 and 000013. This single-target successor confirms only its own source-supported field addition; it does not supersede the four-target disposition or reassess the other members. A separate history-PMID defect does not undo field presence. |
| check-validate | just --no-dotenv validate kb/communities/BioModels_MODEL1806250004_Sharpshooter_Sulcia_Baumannia.yaml; .temp/pr2043/insects/000007/validate.json | supports | Target schema validation passed. |
| check-validate-strict | just --no-dotenv validate-strict kb/communities/BioModels_MODEL1806250004_Sharpshooter_Sulcia_Baumannia.yaml --out /Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2043-batch07/.temp/pr2043/insects/000007/strict.tsv; .temp/pr2043/insects/000007/validate-strict.json | supports | Target strict validation passed. |
| check-validate-terms | just --no-dotenv validate-terms kb/communities/BioModels_MODEL1806250004_Sharpshooter_Sulcia_Baumannia.yaml; .temp/pr2043/insects/000007/validate-terms.json | supports | Target term validation passed. |
| check-validate-gtdb | just --no-dotenv validate-gtdb kb/communities/BioModels_MODEL1806250004_Sharpshooter_Sulcia_Baumannia.yaml; .temp/pr2043/insects/000007/validate-gtdb.json | supports | Target GTDB syntax/status validation passed. |
| check-validate-gtdb-domain | just --no-dotenv validate-gtdb-domain kb/communities/BioModels_MODEL1806250004_Sharpshooter_Sulcia_Baumannia.yaml; .temp/pr2043/insects/000007/validate-gtdb-domain.json | supports | Target GTDB domain validation passed. |
| check-validate-history | just --no-dotenv validate-history history/records/BioModels_MODEL1806250004_Sharpshooter_Sulcia_Baumannia; .temp/pr2043/insects/000007/validate-history.json | supports | Target history validation passed. |
| check-normalize-cache-names-check | uv run python scripts/normalize_cache_names.py --check; .temp/pr2043/insects/000007/normalize-cache-names-check.json | supports | Read-only corpus cache-filename preflight passed. |
| check-validate-references-explained | just --no-dotenv validate-references-explained kb/communities/BioModels_MODEL1806250004_Sharpshooter_Sulcia_Baumannia.yaml; .temp/pr2043/insects/000007/validate-references-explained.json | supports | Target reference validation passed against the pinned cache. |
| check-audit-network | just --no-dotenv audit-network; .temp/pr2043/insects/shared/audit-network.json | context_only | Fresh corpus check reports 44 baseline warnings across 16 of 508 records; the focal native audit is empty. |
| check-check-network-quality | just --no-dotenv check-network-quality; .temp/pr2043/insects/shared/check-network-quality.json | context_only | Fresh corpus check reports 44 baseline warnings across 16 of 508 records; the focal native audit is empty. |

## Limits And Additional Notes

- No FBA/FVA optimization, model/code execution, MATLAB payload, transcriptome reconstruction or raw-sequence analysis was performed. Archive metadata and structural XML checks do not establish reproducibility.
- Supplementary workbook reading was bounded to inventories/headers and declared focal sheets/rows; large reaction lists and other-insect numerical tables were not exhaustively audited.
- BioModels defaults differ from published runtime constraints; the author-repository model is not byte-identical. Neither fact establishes wrong model identity, and stored zero flux values are not published results.
- Figure 4 caption and panel labels disagree on sharpshooter panel lettering. S5o permits cystathionine despite prose amino-acid exclusion; the twenty listed proteinogenic amino-acid exchanges are closed. S6d uses component-model header names iNA81/iNA258 whereas main Methods uses iNA74/iNA234; preserve that source naming discrepancy. These source nuances constrain future provenance expansion.
- Exact culture-collection strains, historical GTDB mapping statistics, replacement ecological-state classification and executable model equivalence were not established; no empirical host-control or dynamic-equilibrium assay is inferred.
- Supplementary human reading was limited to focal EAA outputs and exchange scope in S1e/f/g, S1h, nitrogen definitions/summaries in S1i, all S5o medium bounds, S6 component headers, Text S1 and all SI figures. Extracting every workbook cell is not an exhaustive scientific audit of those cells.
- Fresh corpus network checks return baseline exit 1 with 44 warnings across 16 of 508 records. The focal native audit is empty; unrelated records were not scientifically reviewed.
- Author refresh only; no canonical record, cache, history, schema or generated-product edit, no executable-model reproduction and no independent-approval claim.
- Initial input pins were captured before assessment and rechecked before final inspection. The four original open findings retain exact previous_occurrences; only the separate external-history source finding is new.
- The grouped c2s5 missing-environment resolution is contextual only. Its four-target scope is not superseded or narrowed by this one-target observation.
- Completeness rises from 75 to 80 because environment_term is present. Quality is capped at 100 from 109 and does not negate two major and three minor findings.
- The existing source-boundary discussion is covered by the preserve-model-graph acceptance checks; it is not a demand to perform experiments. Primary quoted excerpts remain the predecessor's short quotations.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261106T061437Z-pr2043-sharpshooter-successor
kind: record
repository: CultureBotAI/CommunityMech
title: 'Sharpshooter BioModels record: current-main review successor'
started_at: '2026-11-06T06:05:51.976535Z'
finished_at: '2026-11-06T06:14:37.011891Z'
reviewer:
  identity: codex
  kind: agent
  independence: unknown
  independence_basis: Author refresh of a stale PR 2043 review. Earlier Codex graph
    curation exists; this pass does not claim independent adversarial approval.
skill: review-yaml-record
completion: completed
verdict: needs_curation
scientific_review: true
summary: 'Current main adds a supported broad animal-associated environment and matching
  embedded history. Fresh primary main text, figures, supplementary methods, focal
  tables and deposited model metadata retain all four original findings: host membership
  and unsupported ecological STABLE (P2), structured computational provenance and
  publication-as-dataset organization (P3). A new P3 identifies an unrelated PMID
  in the external environment-history sidecar. The environment addition itself remains
  valid. Eight focused checks pass; corpus network checks report 44 warnings across
  16 of 508 records, with no target-native issues. No simulation was rerun.'
source:
  git_revision: c1846ce378828d0a2e2d80312ac784a47430a617
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: d2f94c87b82f59663bc2b0c91ac04a245e56fab52d8c11e6bddb559eb9237c84
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
  - path: .temp/pr2043/insects/000007/frozen-target.json
    sha256: 1bfc19730e028f342c2f7bf014ce37f084864f742e7621003d96885b55b344fa
    role: context
  - path: .temp/pr2043/insects/000007/frozen-target.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2043/insects/000007/frozen-target.stdout.txt
    sha256: 3c0c3ec94b77750f8583de5ef0d9a8380bf28bd62a1857cdb28c95cc9ff4601b
    role: context
  - path: .temp/pr2043/insects/000007/inspect.json
    sha256: 1469a15bfe1d9044e2270f8453d4c5c501e0430bf6aa530036f3fa3b37d66776
    role: context
  - path: .temp/pr2043/insects/000007/inspect.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2043/insects/000007/inspect.stdout.txt
    sha256: 98999b708ff0938667a2c1c5c161c19d5a0616976aa31421c4c0f062d1416c35
    role: context
  - path: .temp/pr2043/insects/000007/inspection.json
    sha256: 98999b708ff0938667a2c1c5c161c19d5a0616976aa31421c4c0f062d1416c35
    role: context
  - path: .temp/pr2043/insects/000007/lineage.json
    sha256: 3709b0be5ed9944370788a932dd45b373b328f7864e9fbfd3af80c6136fbd5c0
    role: context
  - path: .temp/pr2043/insects/000007/local-search.json
    sha256: d634056c260109305de20cb8557c20c3948b55b530474f80da2b3d434af5db9f
    role: context
  - path: .temp/pr2043/insects/000007/local-search.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2043/insects/000007/local-search.stdout.txt
    sha256: d489a9e52c503764c89fc576a982a96b2bce4c03685f15deac0384bdad4678d7
    role: context
  - path: .temp/pr2043/insects/000007/normalize-cache-names-check.json
    sha256: 765eb86e1e224d4d2753ed196726ffb7bc3fda8d5b3a4e6ccb11532a1413cffb
    role: context
  - path: .temp/pr2043/insects/000007/normalize-cache-names-check.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2043/insects/000007/normalize-cache-names-check.stdout.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2043/insects/000007/replay-qualified.json
    sha256: 38722e1caa8d1311d52b61d1b54c2c7f11298be3d5d48dee36d64619f30ca0e8
    role: context
  - path: .temp/pr2043/insects/000007/replay.json
    sha256: 7ff681da525cb96bb62860c78315269d30fc2de7a21c09a15596284e6e8d6523
    role: context
  - path: .temp/pr2043/insects/000007/strict.tsv
    sha256: b184ed5450b968070bb6c75648407e388f41a1eaf7017890723cf560999fc3f7
    role: context
  - path: .temp/pr2043/insects/000007/target-diff.json
    sha256: 88de428770faa268677c59d1af61258f0d5181c00248d0d340ea697929c9e822
    role: context
  - path: .temp/pr2043/insects/000007/target-diff.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2043/insects/000007/target-diff.stdout.txt
    sha256: 1a2454506079a379dd72a169c98af60a82997b16a55f9644bc80058655790f98
    role: context
  - path: .temp/pr2043/insects/000007/targets.json
    sha256: 535f97543198ccb58bba2384a3abef905fea94c1bb955ab2e78a49d71ea72813
    role: context
  - path: .temp/pr2043/insects/000007/validate-gtdb-domain.json
    sha256: a80f0f4e2cfaf70e7873454b8aad876140de13ac1846d548a23c28f91476a1c3
    role: context
  - path: .temp/pr2043/insects/000007/validate-gtdb-domain.stderr.txt
    sha256: 0888bc9e538c1bfada10dc28ac3fb777e10b576324653840e1214f62e5efb4cd
    role: context
  - path: .temp/pr2043/insects/000007/validate-gtdb-domain.stdout.txt
    sha256: ede937293c42cad366f434dce49a485a9a0c56fe86620b52ca243ad10e09ecae
    role: context
  - path: .temp/pr2043/insects/000007/validate-gtdb.json
    sha256: 3e5d2618985bc2ecda773086c41eb54d1ac4dea259095e9f70994f8960ca8e66
    role: context
  - path: .temp/pr2043/insects/000007/validate-gtdb.stderr.txt
    sha256: 4bcead0454bbcb80e3a71b3cd18f30ee6e9e3d242d60071b5822b848403fd400
    role: context
  - path: .temp/pr2043/insects/000007/validate-gtdb.stdout.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2043/insects/000007/validate-history.json
    sha256: 01c6ab2d08965555980963389139847c571b7c75cff3036d97266250594b76b2
    role: context
  - path: .temp/pr2043/insects/000007/validate-history.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2043/insects/000007/validate-history.stdout.txt
    sha256: de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
    role: context
  - path: .temp/pr2043/insects/000007/validate-references-explained.json
    sha256: a71c7270d09be546922d91185f3853fd2bfcb9521ee78c59ab816d93698d1c06
    role: context
  - path: .temp/pr2043/insects/000007/validate-references-explained.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2043/insects/000007/validate-references-explained.stdout.txt
    sha256: 0cbc23aed97803edd7e6ca55de7192aef9f2bbad73db816af56466d3387541d4
    role: context
  - path: .temp/pr2043/insects/000007/validate-strict.json
    sha256: 3c203e914a5cbeb115f282d8cbc240bdb34c429b065bae6983d1c9107427446d
    role: context
  - path: .temp/pr2043/insects/000007/validate-strict.stderr.txt
    sha256: 3ea49fb73fd38976ab065dabc611f39457010800783b4c547dba2fab6bfc2c11
    role: context
  - path: .temp/pr2043/insects/000007/validate-strict.stdout.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2043/insects/000007/validate-terms.json
    sha256: dd0a003163617a16b42ab77143a63d858e969e4a41b43a974a0192394de83e0b
    role: context
  - path: .temp/pr2043/insects/000007/validate-terms.stderr.txt
    sha256: 40e5a8fa467b9163eaccbca8fb900053bdd2d716db305326aa72915286bc3b14
    role: context
  - path: .temp/pr2043/insects/000007/validate-terms.stdout.txt
    sha256: 23acda1c1d3194d12bc947d897d07de83f4a076a9d93c135148885108530e018
    role: context
  - path: .temp/pr2043/insects/000007/validate.json
    sha256: 9201460664db409dbd5e16146c3e4b89628ed5e313b06bb1fc11cb34736c78b1
    role: context
  - path: .temp/pr2043/insects/000007/validate.stderr.txt
    sha256: 1af59c70d9ea0db7bd0e0e1192e77b0faf75dd2499cb5d5d6d1bb25defbec1ee
    role: context
  - path: .temp/pr2043/insects/000007/validate.stdout.txt
    sha256: de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
    role: context
  - path: .temp/pr2043/insects/shared/Graphocephala_iNA629.xml
    sha256: f44fa2a1889f3698f46ea2c54f55f841a37fb67c871b776fc89a927ccb6547c8
    role: context
  - path: .temp/pr2043/insects/shared/Graphocephala_iNA629.xml.receipt.json
    sha256: fed3484c952e1387eed837c9bc60f1dec239d0b5c778a0aeb68e6d3372810133
    role: context
  - path: .temp/pr2043/insects/shared/MODEL1806250003-files.json
    sha256: 3dbc354a2275999d9761fb51a9bf9f40652bd7e486c15db9bb5333a1184daa26
    role: context
  - path: .temp/pr2043/insects/shared/MODEL1806250003-files.json.receipt.json
    sha256: c48a0c184f7182ed9818d661bc14e847584f95f3f290545ad0992728aa493771
    role: context
  - path: .temp/pr2043/insects/shared/MODEL1806250003.json
    sha256: b9c70c5d3d1939d2cd92007d822188aa56c0bbd19bcdcb0facc55ce61c28a853
    role: context
  - path: .temp/pr2043/insects/shared/MODEL1806250003.json.receipt.json
    sha256: d56242e9aa37430a8dbd39745bed31d4cefbe914d059ecbf8241f067a6129174
    role: context
  - path: .temp/pr2043/insects/shared/MODEL1806250004-files.json
    sha256: c8e63b78b628420a20b6f7427ab3a0d30ca2ec839b29e1e4b8bb314a02d43324
    role: context
  - path: .temp/pr2043/insects/shared/MODEL1806250004-files.json.receipt.json
    sha256: 633f0d29abd1072c0288750f6efd0b698d7981ba587795ebee2eb0ba9d63a8da
    role: context
  - path: .temp/pr2043/insects/shared/MODEL1806250004.json
    sha256: 0d7c21addfaba17a2a1ffe52c101561388a56c2c144133036173801ebb5d82d1
    role: context
  - path: .temp/pr2043/insects/shared/MODEL1806250004.json.receipt.json
    sha256: 72514b52809957ee70bc509283e0e134f3b2ee9817ba3b8aead8b25f1bf0d825
    role: context
  - path: .temp/pr2043/insects/shared/MODEL1806250005-files.json
    sha256: 50202a50f2f6188c832b0ec3e136dcc8d5c925f19cf47423687d02b10b9b7f80
    role: context
  - path: .temp/pr2043/insects/shared/MODEL1806250005-files.json.receipt.json
    sha256: d5f5bdd77fa576a8476fdeec9a3d0a9b76856acb8aa754784e3c238de7368a00
    role: context
  - path: .temp/pr2043/insects/shared/MODEL1806250005.json
    sha256: 9ab536bf1330cc5ed046865c02bb6956e4d78d4fe239ba70dff4a2d23e3637e7
    role: context
  - path: .temp/pr2043/insects/shared/MODEL1806250005.json.receipt.json
    sha256: 3888abf71e85024f282aaaee42c15d2c9032b73a5930b70a47b8ed2751e02292
    role: context
  - path: .temp/pr2043/insects/shared/Neotibicen_iNA533.xml
    sha256: 3c1d1659c84a83b496b4f69ec17a855d1f3249f99c113220c1b126e683422d1c
    role: context
  - path: .temp/pr2043/insects/shared/Neotibicen_iNA533.xml.receipt.json
    sha256: 43326bbc3acd6fa96dfd13f3ea757ba1e34bef866d1f0abea9cda711ce41b717
    role: context
  - path: .temp/pr2043/insects/shared/Philaenus_iNA761.xml
    sha256: 4f82725783bec612c011291746f9996f0ee72c6028b1323eee5b55c8b9a2a6ee
    role: context
  - path: .temp/pr2043/insects/shared/Philaenus_iNA761.xml.receipt.json
    sha256: 8c9ced46e4ae9508b1aaa885b51d894f3c1dcaced9de7be0f071818ae51f1b74
    role: context
  - path: .temp/pr2043/insects/shared/archive-inventory.json
    sha256: 57e630a2d82ca134d56d13a75d6889fbf312c8b6fc4ce092db7d543511eb9fec
    role: context
  - path: .temp/pr2043/insects/shared/audit-network.json
    sha256: 4951fc69e06675f2f5b033664f43499cde41341ad343d0595050a00e484088a6
    role: context
  - path: .temp/pr2043/insects/shared/audit-network.stderr.txt
    sha256: a71fb29e950f3eaf0eb2b834a43c59d4a1b6aa85a2a89473ae99b0e408a27a36
    role: context
  - path: .temp/pr2043/insects/shared/audit-network.stdout.txt
    sha256: e8ebf9ba0a67e945a00eb7ee67c5cc886a3fa5165ceeea6dad115d754cbb144a
    role: context
  - path: .temp/pr2043/insects/shared/author-Graphocephala_iNA629.xml
    sha256: 83911ccfbd07d7f5df5981a950fceced3c7bdac6b0d5ca56feb308e922b3a286
    role: context
  - path: .temp/pr2043/insects/shared/author-Graphocephala_iNA629.xml.receipt.json
    sha256: 114449987eac57b82c88200b8f6a49816c37a5fc3ee5c9ffd446e725c6b4ab10
    role: context
  - path: .temp/pr2043/insects/shared/author-Neotibicen_iNA533.xml
    sha256: 37859414e17ccc716db4fd596d5b9ec56b8e05b1887e489ff73966d6916ba670
    role: context
  - path: .temp/pr2043/insects/shared/author-Neotibicen_iNA533.xml.receipt.json
    sha256: efeed63ec3748904ba5ab08adc8ca2fcf40c7481c88352778152d248661ac6d2
    role: context
  - path: .temp/pr2043/insects/shared/author-Philaenus_iNA761.xml
    sha256: b37f8f4d2d8aa85b84968a017921832e7b87c0ca2f09f501a68f6d47440344b8
    role: context
  - path: .temp/pr2043/insects/shared/author-Philaenus_iNA761.xml.receipt.json
    sha256: 84530e0e3f2391a4ad77ec14e641c45f23a61b198aefac5c39f78861e45a12ad
    role: context
  - path: .temp/pr2043/insects/shared/author-tree.json
    sha256: d2f516d0f57078c7612056eb386f81d771b5e9ae43a94221e5a0152e32bbe475
    role: context
  - path: .temp/pr2043/insects/shared/author-tree.json.receipt.json
    sha256: c9f3c2dbc633b6bf796cb6697482b8b4ff968c07f503f986358129294b42a73f
    role: context
  - path: .temp/pr2043/insects/shared/bioproject.xml
    sha256: 970135e3125dff2c18ab8202bdbd6967bcbfb4225b0bb8f692592242e11e21dd
    role: context
  - path: .temp/pr2043/insects/shared/bioproject.xml.receipt.json
    sha256: 68cdba9459e4a9f791d85c379823a47f04682b92a1422843a3f7339c1b671cd9
    role: context
  - path: .temp/pr2043/insects/shared/check-network-quality.json
    sha256: 0d248716d7e391d66134536d180d38abe777321a72d997e04606f0ba1d27e8a2
    role: context
  - path: .temp/pr2043/insects/shared/check-network-quality.stderr.txt
    sha256: f9a8e9fb5a4e4ea545236a809393dbc1ce4325b14579c65a3130bcfe713e798a
    role: context
  - path: .temp/pr2043/insects/shared/check-network-quality.stdout.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2043/insects/shared/crossref.json
    sha256: ddc17288f4fe1f4781ced1dc88991b00b7102bc6fceada424d0da1f9042d405c
    role: context
  - path: .temp/pr2043/insects/shared/crossref.json.receipt.json
    sha256: c0885ab7869eb5c8d9ea2a3518dd89a400383bc1248e02c93eeb06aff64eedea
    role: context
  - path: .temp/pr2043/insects/shared/envo.json
    sha256: a06ca8fc5dc0ec836640503fbfa61f174a7e0a2afb91ff77b0a66c97c1f7b8d4
    role: context
  - path: .temp/pr2043/insects/shared/envo.json.receipt.json
    sha256: d380711c3601cc243d0d8d7cc9d0cdbe52635a11cc08fe76682e14223b0a417d
    role: context
  - path: .temp/pr2043/insects/shared/epmc.json
    sha256: 3956d4f5dbf3f85480eaea96e971bea6af882a1269613faca010bf9bd06f48ef
    role: context
  - path: .temp/pr2043/insects/shared/epmc.json.receipt.json
    sha256: 0e5bbcbef038425ad514659b43e0b998be9178fce220c4e1ce4903f6b8548648
    role: context
  - path: .temp/pr2043/insects/shared/fetch-Graphocephala_iNA629.xml.json
    sha256: e5309667c7aa1fb2914691af9f882dbac916e382858fcb371e52ece90f426a51
    role: context
  - path: .temp/pr2043/insects/shared/fetch-Graphocephala_iNA629.xml.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2043/insects/shared/fetch-Graphocephala_iNA629.xml.stdout.txt
    sha256: f44fa2a1889f3698f46ea2c54f55f841a37fb67c871b776fc89a927ccb6547c8
    role: context
  - path: .temp/pr2043/insects/shared/fetch-MODEL1806250003-files.json.json
    sha256: 544c4ba3a95f05ee8d8b43c78ffac1ad9f562e6d66637b9509608fca7d0dca87
    role: context
  - path: .temp/pr2043/insects/shared/fetch-MODEL1806250003-files.json.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2043/insects/shared/fetch-MODEL1806250003-files.json.stdout.txt
    sha256: 3dbc354a2275999d9761fb51a9bf9f40652bd7e486c15db9bb5333a1184daa26
    role: context
  - path: .temp/pr2043/insects/shared/fetch-MODEL1806250003.json.json
    sha256: 51cfed12dd638b006b480aec23810ff7097bb21682b89b2baa8903c5f777c73b
    role: context
  - path: .temp/pr2043/insects/shared/fetch-MODEL1806250003.json.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2043/insects/shared/fetch-MODEL1806250003.json.stdout.txt
    sha256: b9c70c5d3d1939d2cd92007d822188aa56c0bbd19bcdcb0facc55ce61c28a853
    role: context
  - path: .temp/pr2043/insects/shared/fetch-MODEL1806250004-files.json.json
    sha256: 83264f87beea48a1876fa0d894976b3654aad6a0cc782b697a2f794f5a0d393b
    role: context
  - path: .temp/pr2043/insects/shared/fetch-MODEL1806250004-files.json.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2043/insects/shared/fetch-MODEL1806250004-files.json.stdout.txt
    sha256: c8e63b78b628420a20b6f7427ab3a0d30ca2ec839b29e1e4b8bb314a02d43324
    role: context
  - path: .temp/pr2043/insects/shared/fetch-MODEL1806250004.json.json
    sha256: 705e95f3ca75d921fe06f1becd2dbb6cf4e26678ac35188a585059078ef05779
    role: context
  - path: .temp/pr2043/insects/shared/fetch-MODEL1806250004.json.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2043/insects/shared/fetch-MODEL1806250004.json.stdout.txt
    sha256: 0d7c21addfaba17a2a1ffe52c101561388a56c2c144133036173801ebb5d82d1
    role: context
  - path: .temp/pr2043/insects/shared/fetch-MODEL1806250005-files.json.json
    sha256: 0d33a6a9dbf772e1e2a031d25294e793fceaff4f0f93ddc77a4987c8adbf9cbd
    role: context
  - path: .temp/pr2043/insects/shared/fetch-MODEL1806250005-files.json.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2043/insects/shared/fetch-MODEL1806250005-files.json.stdout.txt
    sha256: 50202a50f2f6188c832b0ec3e136dcc8d5c925f19cf47423687d02b10b9b7f80
    role: context
  - path: .temp/pr2043/insects/shared/fetch-MODEL1806250005.json.json
    sha256: d5459d63d34c16f3cbe699e9a3e8a1afa1a3b9a73cb6ed6224aca38d4a4e867f
    role: context
  - path: .temp/pr2043/insects/shared/fetch-MODEL1806250005.json.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2043/insects/shared/fetch-MODEL1806250005.json.stdout.txt
    sha256: 9ab536bf1330cc5ed046865c02bb6956e4d78d4fe239ba70dff4a2d23e3637e7
    role: context
  - path: .temp/pr2043/insects/shared/fetch-Neotibicen_iNA533.xml.json
    sha256: dd3c08593c5e1755c7fe6c7af358c2739e9a4e0d0d3ff330ca1ae4709466f814
    role: context
  - path: .temp/pr2043/insects/shared/fetch-Neotibicen_iNA533.xml.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2043/insects/shared/fetch-Neotibicen_iNA533.xml.stdout.txt
    sha256: 3c1d1659c84a83b496b4f69ec17a855d1f3249f99c113220c1b126e683422d1c
    role: context
  - path: .temp/pr2043/insects/shared/fetch-Philaenus_iNA761.xml.json
    sha256: 2991918c69e98463b25ec59b6b861e8a3fe00f594ea084a013aefeccc9e36331
    role: context
  - path: .temp/pr2043/insects/shared/fetch-Philaenus_iNA761.xml.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2043/insects/shared/fetch-Philaenus_iNA761.xml.stdout.txt
    sha256: 4f82725783bec612c011291746f9996f0ee72c6028b1323eee5b55c8b9a2a6ee
    role: context
  - path: .temp/pr2043/insects/shared/fetch-author-Graphocephala_iNA629.xml.json
    sha256: 38a78a1aa681f30b608a2e7f9b686dfe9df9aac4d6d4b9a526e4fa4503d97236
    role: context
  - path: .temp/pr2043/insects/shared/fetch-author-Graphocephala_iNA629.xml.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2043/insects/shared/fetch-author-Graphocephala_iNA629.xml.stdout.txt
    sha256: 83911ccfbd07d7f5df5981a950fceced3c7bdac6b0d5ca56feb308e922b3a286
    role: context
  - path: .temp/pr2043/insects/shared/fetch-author-Neotibicen_iNA533.xml.json
    sha256: bb92482205e5b8c5231a26c9af671adedfa4c9a2860408343ea68de26947a9fd
    role: context
  - path: .temp/pr2043/insects/shared/fetch-author-Neotibicen_iNA533.xml.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2043/insects/shared/fetch-author-Neotibicen_iNA533.xml.stdout.txt
    sha256: 37859414e17ccc716db4fd596d5b9ec56b8e05b1887e489ff73966d6916ba670
    role: context
  - path: .temp/pr2043/insects/shared/fetch-author-Philaenus_iNA761.xml.json
    sha256: cb53e216ce7f1a62dbd23c5193be934ccf968c10d197d932a48e0909cd528011
    role: context
  - path: .temp/pr2043/insects/shared/fetch-author-Philaenus_iNA761.xml.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2043/insects/shared/fetch-author-Philaenus_iNA761.xml.stdout.txt
    sha256: b37f8f4d2d8aa85b84968a017921832e7b87c0ca2f09f501a68f6d47440344b8
    role: context
  - path: .temp/pr2043/insects/shared/fetch-author-tree.json.json
    sha256: 4d069eccfe8e3a4258fc247b5ff7f8c9091890c30ee1f1856312404ed95ad833
    role: context
  - path: .temp/pr2043/insects/shared/fetch-author-tree.json.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2043/insects/shared/fetch-author-tree.json.stdout.txt
    sha256: d2f516d0f57078c7612056eb386f81d771b5e9ae43a94221e5a0152e32bbe475
    role: context
  - path: .temp/pr2043/insects/shared/fetch-bioproject.xml.json
    sha256: 3ad4cf752ca1237290af2e82a18171cb398f0ab5be10242384d9f3e2eb035d94
    role: context
  - path: .temp/pr2043/insects/shared/fetch-bioproject.xml.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2043/insects/shared/fetch-bioproject.xml.stdout.txt
    sha256: 970135e3125dff2c18ab8202bdbd6967bcbfb4225b0bb8f692592242e11e21dd
    role: context
  - path: .temp/pr2043/insects/shared/fetch-crossref.json.json
    sha256: 07f4c171c98bb5e81064bcd91ffdbf92117b75317142051441c6757f83abec00
    role: context
  - path: .temp/pr2043/insects/shared/fetch-crossref.json.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2043/insects/shared/fetch-crossref.json.stdout.txt
    sha256: ddc17288f4fe1f4781ced1dc88991b00b7102bc6fceada424d0da1f9042d405c
    role: context
  - path: .temp/pr2043/insects/shared/fetch-envo.json.json
    sha256: 7955a3748e5e6184b56a15e9877ac7f30af9d3a467122cb1600334403a02e8fa
    role: context
  - path: .temp/pr2043/insects/shared/fetch-envo.json.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2043/insects/shared/fetch-envo.json.stdout.txt
    sha256: a06ca8fc5dc0ec836640503fbfa61f174a7e0a2afb91ff77b0a66c97c1f7b8d4
    role: context
  - path: .temp/pr2043/insects/shared/fetch-epmc.json.json
    sha256: 1b8fa14418a3f766212b298174c093e5a9e196bf892a22b1174ecc40760cee4e
    role: context
  - path: .temp/pr2043/insects/shared/fetch-epmc.json.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2043/insects/shared/fetch-epmc.json.stdout.txt
    sha256: 3956d4f5dbf3f85480eaea96e971bea6af882a1269613faca010bf9bd06f48ef
    role: context
  - path: .temp/pr2043/insects/shared/fetch-history-pmid-29944653.xml.json
    sha256: 4c0ab31f66ce7ad36499ee7582431cbb23c75c3fb4d0eaf41b674cd913e84958
    role: context
  - path: .temp/pr2043/insects/shared/fetch-history-pmid-29944653.xml.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2043/insects/shared/fetch-history-pmid-29944653.xml.stdout.txt
    sha256: a49539c5097172b4eba31c6d2935a918fe06c40012e272ab58198361e53b9008
    role: context
  - path: .temp/pr2043/insects/shared/fetch-imodulon-catalog.json.json
    sha256: 9e5f74c50d8bea0a074c9ae9ebe1800bd09b6ee92b687d1be557ed57962fce48
    role: context
  - path: .temp/pr2043/insects/shared/fetch-imodulon-catalog.json.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2043/insects/shared/fetch-imodulon-catalog.json.stdout.txt
    sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
    role: context
  - path: .temp/pr2043/insects/shared/fetch-ncbi-taxonomy.xml.json
    sha256: 1f153f3387f91a015a4ac1e6cb5a310a6d818eb88218b4a3073e40f58a88470a
    role: context
  - path: .temp/pr2043/insects/shared/fetch-ncbi-taxonomy.xml.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2043/insects/shared/fetch-ncbi-taxonomy.xml.stdout.txt
    sha256: 39ab98b2869443d2261ccfb5da1b6496b27c143ae50cb160979dc8ba9b12d658
    role: context
  - path: .temp/pr2043/insects/shared/fetch-primary.xml.json
    sha256: 464632c71715bc5a4a0d585010d41dd95fdb62f146cc5583e30010dd5538c532
    role: context
  - path: .temp/pr2043/insects/shared/fetch-primary.xml.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2043/insects/shared/fetch-primary.xml.stdout.txt
    sha256: 0cac2dc3b4e28fd1686a41fd36364bdb57aca39edec3cc2818fe58e02405fdd1
    role: context
  - path: .temp/pr2043/insects/shared/fetch-pubmed.xml.json
    sha256: d6a3b731ece9bfca6d0e8084fe04d8d66f212dd914ec372e5c84eebb327e605b
    role: context
  - path: .temp/pr2043/insects/shared/fetch-pubmed.xml.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2043/insects/shared/fetch-pubmed.xml.stdout.txt
    sha256: 67c9b795c61ef6b233cd3653148d2fceadd2d9d358db392a799b95f1cff1aab9
    role: context
  - path: .temp/pr2043/insects/shared/fetch-supplement.zip.json
    sha256: 4244cfe1bdfeb9acc8e330de473c561a0dc676ac1c1e6b6734ddfa34243af4f8
    role: context
  - path: .temp/pr2043/insects/shared/fetch-supplement.zip.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2043/insects/shared/fetch-supplement.zip.stdout.txt
    sha256: 976d9b7e8b0fef40a84ac913596437b8b4c7551537d347b2679d1d10138cb911
    role: context
  - path: .temp/pr2043/insects/shared/history-pmid-29944653.xml
    sha256: a49539c5097172b4eba31c6d2935a918fe06c40012e272ab58198361e53b9008
    role: context
  - path: .temp/pr2043/insects/shared/history-pmid-29944653.xml.receipt.json
    sha256: 9181b4a866a0a6a8cffe4be7fb00858b253db5ebce897cd6df174f84b17a0759
    role: context
  - path: .temp/pr2043/insects/shared/imodulon-catalog.json
    sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
    role: context
  - path: .temp/pr2043/insects/shared/imodulon-catalog.json.receipt.json
    sha256: 114a377353c36fe5f2b6fc3b9ce7b39fca52acc662319237cadedda5ea01d036
    role: context
  - path: .temp/pr2043/insects/shared/mbo0051840750001.jpg
    sha256: 4c853904c18c871175e4f664caf2bf4d99f14ac407849bb5819339324a822468
    role: context
  - path: .temp/pr2043/insects/shared/mbo0051840750002.jpg
    sha256: a032782e94c7b252d5fb71984efbccf92bfa40108a70218b36af4088ac1db390
    role: context
  - path: .temp/pr2043/insects/shared/mbo0051840750003.jpg
    sha256: 890d39513da11f492ebb83f083995d69a1d3a44ab66d0ec5b5985ceb59114077
    role: context
  - path: .temp/pr2043/insects/shared/mbo0051840750004.jpg
    sha256: 7abb894e5756b910a47459d1ea501dccfcccebffc958df3fd3e8bf0ee7ee9b6e
    role: context
  - path: .temp/pr2043/insects/shared/mbo0051840750005.jpg
    sha256: 83d9b1e5fdd06a7b37e98ac41c23c5d4c6d1cd46fb52fb514341d631c008d303
    role: context
  - path: .temp/pr2043/insects/shared/mbo0051840750006.jpg
    sha256: be0ad10d2efa74b609ca56e379691c9a3cdc9426b2984f9bdd1ba8cf85d4b01f
    role: context
  - path: .temp/pr2043/insects/shared/mbo0051840750007.jpg
    sha256: dc9a71931bf54fcadf7cf3d0fc9a0aa99d6d42b726a33b6479417c868d4f076e
    role: context
  - path: .temp/pr2043/insects/shared/mbo005184075s1.docx
    sha256: e60bc3acda102989e2f6876877c73341f33f4651e7d65880568a6c6fe2208408
    role: context
  - path: .temp/pr2043/insects/shared/mbo005184075s1.docx.txt
    sha256: 169f61578a4234ec5b910fa0f164782bf4950f53fa5e872677127c8aea9d96c4
    role: context
  - path: .temp/pr2043/insects/shared/mbo005184075sf1.pdf
    sha256: f4e54ec90c4fc201eb31b3e9d8bc29ec5bdf12b3a1b33348e17998773fa03c99
    role: context
  - path: .temp/pr2043/insects/shared/mbo005184075sf1.pdf-1.png
    sha256: b6556c6d7c94ec31a6851e6fb7ef6dac1c885ca6eb88fbf5abd038997c55ba60
    role: context
  - path: .temp/pr2043/insects/shared/mbo005184075sf1.pdf.txt
    sha256: 604904d02aaecc08555b756703b27ce39a14bfc9e086658e5c065ca54c02fa13
    role: context
  - path: .temp/pr2043/insects/shared/mbo005184075sf2.pdf
    sha256: 269471221431743bee519549795624a00cde04034bb9307ffe401cc38685347f
    role: context
  - path: .temp/pr2043/insects/shared/mbo005184075sf2.pdf-1.png
    sha256: 5f9e4ab28c55443382fee68619193c028c7a58ca0604d07100c4a4b6a4c3be12
    role: context
  - path: .temp/pr2043/insects/shared/mbo005184075sf2.pdf.txt
    sha256: eaabc469bdb1dbc55ece48470fda56d62e138f193c7202ad4712e96e79b9b7bd
    role: context
  - path: .temp/pr2043/insects/shared/mbo005184075sf3.pdf
    sha256: fc9cc23bd123cce9d3b073a32e5986cd81a0ee8b7ec6a7205d24214751fc8d2b
    role: context
  - path: .temp/pr2043/insects/shared/mbo005184075sf3.pdf-1.png
    sha256: 0d8058fa53c077546788a0765925a9b6db7bf87bf8e6a18e9bbcd508304c6810
    role: context
  - path: .temp/pr2043/insects/shared/mbo005184075sf3.pdf.txt
    sha256: f802eecc713eb43c6f115c97aeac0e9d4cd57707dcbee9cb04a26f7868c2d8a1
    role: context
  - path: .temp/pr2043/insects/shared/mbo005184075st1.xlsx
    sha256: 68f16a988cc74640cf9c689385abd20a779962b83363b29fa1985b07ae4ce61c
    role: context
  - path: .temp/pr2043/insects/shared/mbo005184075st2.xlsx
    sha256: 723af2f436283187183e894e895d9fdcd2c5209abd14aa44f93556c111b001fa
    role: context
  - path: .temp/pr2043/insects/shared/mbo005184075st3.xlsx
    sha256: 4c1d603995b5f10a422e18badb4aac62eef72033c4ec35f91a9dc19a819b481f
    role: context
  - path: .temp/pr2043/insects/shared/mbo005184075st4.xlsx
    sha256: 5fae337481ae2353d9db20094339881b45b72b9a34e463c91841dace15cbec5e
    role: context
  - path: .temp/pr2043/insects/shared/mbo005184075st5.xlsx
    sha256: dd0cdbcd74401eb32aed171289856cebfe9643011f299e05b96eb263afedda74
    role: context
  - path: .temp/pr2043/insects/shared/mbo005184075st6.xlsx
    sha256: 3e124350c525592d5239b3e3f36ca7c87c2afe8100b8681d422e7b758abc8680
    role: context
  - path: .temp/pr2043/insects/shared/model-audit.json
    sha256: 3c0da359b258f5ce404ea4f975e0bdf919c3a7024efa762c58ec4e2f65cc3f61
    role: context
  - path: .temp/pr2043/insects/shared/ncbi-taxonomy.xml
    sha256: 39ab98b2869443d2261ccfb5da1b6496b27c143ae50cb160979dc8ba9b12d658
    role: context
  - path: .temp/pr2043/insects/shared/ncbi-taxonomy.xml.receipt.json
    sha256: ed3ebf8d66638a73f69bf25ef7a8fa6d7cd705db42ed7a02301598dd7fcbd4a2
    role: context
  - path: .temp/pr2043/insects/shared/pdftotext-mbo005184075sf1.pdf.json
    sha256: 6c1f527dd71932417c1aec3d48b10cf6f7859b47405b8f98c26b32e873e76ddd
    role: context
  - path: .temp/pr2043/insects/shared/pdftotext-mbo005184075sf1.pdf.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2043/insects/shared/pdftotext-mbo005184075sf1.pdf.stdout.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2043/insects/shared/pdftotext-mbo005184075sf2.pdf.json
    sha256: c22dd5fc353aaf4c35c03c7264e9aa72a7bb86c8b767d29d049482b59fc4f758
    role: context
  - path: .temp/pr2043/insects/shared/pdftotext-mbo005184075sf2.pdf.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2043/insects/shared/pdftotext-mbo005184075sf2.pdf.stdout.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2043/insects/shared/pdftotext-mbo005184075sf3.pdf.json
    sha256: 71303042de1eff64b97df481d2a4201ee85815811684a0bd3abcc9ffcedd697a
    role: context
  - path: .temp/pr2043/insects/shared/pdftotext-mbo005184075sf3.pdf.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2043/insects/shared/pdftotext-mbo005184075sf3.pdf.stdout.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2043/insects/shared/primary.xml
    sha256: 0cac2dc3b4e28fd1686a41fd36364bdb57aca39edec3cc2818fe58e02405fdd1
    role: context
  - path: .temp/pr2043/insects/shared/primary.xml.receipt.json
    sha256: 99cbcfa74dbb4294f9d7ce567006bcdaa236cc36ad8504b68d2337a58957c1de
    role: context
  - path: .temp/pr2043/insects/shared/pubmed.xml
    sha256: 67c9b795c61ef6b233cd3653148d2fceadd2d9d358db392a799b95f1cff1aab9
    role: context
  - path: .temp/pr2043/insects/shared/pubmed.xml.receipt.json
    sha256: 98d01fbec585a7ba6a5e305ee73f92a81e00ec1cb14445141761a88629a7cf6a
    role: context
  - path: .temp/pr2043/insects/shared/render-mbo005184075sf1.pdf.json
    sha256: 54f5dd8d665f3c59b196ee5574fea5ca2d2a0bd9ac239601761bff387930ef28
    role: context
  - path: .temp/pr2043/insects/shared/render-mbo005184075sf1.pdf.stderr.txt
    sha256: 9421bc8acacf952ac1bc436cc50d5086156156ab4a9e2bb397c3bdc2d77552c7
    role: context
  - path: .temp/pr2043/insects/shared/render-mbo005184075sf1.pdf.stdout.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2043/insects/shared/render-mbo005184075sf2.pdf.json
    sha256: 4fcac58a2acee0b0234ccaff7ad39ef21ebc8a102180b318b491ec4bf26a4737
    role: context
  - path: .temp/pr2043/insects/shared/render-mbo005184075sf2.pdf.stderr.txt
    sha256: 9421bc8acacf952ac1bc436cc50d5086156156ab4a9e2bb397c3bdc2d77552c7
    role: context
  - path: .temp/pr2043/insects/shared/render-mbo005184075sf2.pdf.stdout.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2043/insects/shared/render-mbo005184075sf3.pdf.json
    sha256: c45ac10364410bed7d90d53f8a68173441179a2cdce8a311f0a296229a0e65fa
    role: context
  - path: .temp/pr2043/insects/shared/render-mbo005184075sf3.pdf.stderr.txt
    sha256: 9421bc8acacf952ac1bc436cc50d5086156156ab4a9e2bb397c3bdc2d77552c7
    role: context
  - path: .temp/pr2043/insects/shared/render-mbo005184075sf3.pdf.stdout.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2043/insects/shared/s1.txt
    sha256: 295fe3351c815e0d98760f738e61cc3064e1627a5f3ab3540d5e636d0f633bae
    role: context
  - path: .temp/pr2043/insects/shared/s2.txt
    sha256: e1b3cb38e9e09e8be43928d5b598c9c9d717cf5cf67e4b470287a67ab37acd08
    role: context
  - path: .temp/pr2043/insects/shared/s3.txt
    sha256: ab2c7608a0eee93cc662b07a06e9020ea9bf545eec9f4bd1e6121e941a1bcff1
    role: context
  - path: .temp/pr2043/insects/shared/s4.txt
    sha256: abbefa9d8f124067aaf4fac785c3da248f4e86b1e705bab5bf0c812c4df3dc96
    role: context
  - path: .temp/pr2043/insects/shared/supplement.zip
    sha256: 976d9b7e8b0fef40a84ac913596437b8b4c7551537d347b2679d1d10138cb911
    role: context
  - path: .temp/pr2043/insects/shared/supplement.zip.receipt.json
    sha256: 8f95eb086006bc195ebdcd8b48ef16a5ab801fa287e12de418537c5b68d1c054
    role: context
  - path: .temp/pr2043/insects/shared/table-audit.json
    sha256: e4346c62ddc41910fdec5b812b4a72c8737c2de2217f6a1c79724d3870c6bf72
    role: context
  - path: AGENTS.md
    sha256: 8f23dcad7ed9c9873f00058995d1219cca8810c27ed5d787cb9b66a8abf96728
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
  - path: history/records/BioModels_MODEL1806250004_Sharpshooter_Sulcia_Baumannia/2026-10-05T124958Z-codex-06c5c7.yaml
    sha256: 5611edb5b42b2d192ca8f0d838e2f35ac71722109ea1f6efe1bad22a5712ee00
    role: context
  - path: history/records/BioModels_MODEL1806250004_Sharpshooter_Sulcia_Baumannia/2026-10-25T151200Z-antigravity-2072.yaml
    sha256: b5b5cf152359cca34ece1f1fb16a77c04aa49c84827fc66bf9e780d571696e8c
    role: context
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: kb/communities/BioModels_MODEL1806250004_Sharpshooter_Sulcia_Baumannia.yaml
    sha256: 9cbcf07ed58d956c7b6da920f88893ba96bcad2d481afbda647e56ea7340f9ac
    role: target
  - path: references_cache/PMID_30254121.md
    sha256: a63558f5a1ea983a198551fa17e038566f4b07480182dce49161d50dbd8a9341
    role: context
  - path: references_cache/PMID_30254121.txt
    sha256: bc2fabd308e36c1cfc6b596a80f0de06a9f320e15437e21cf66de7631aa7f6e1
    role: context
  - path: reports/causal_graph_review/decisions/20261005-twelve-records-batch7.yaml
    sha256: c96f00489d2ad14f63cd035adc778adbf72d7fe6a11c2dffd81cd1a904cc0a75
    role: context
  - path: reports/causal_graph_review/decisions/20261025-c2s5-review-remediation.yaml
    sha256: 1296c3021a25078a1a02b3d6554e71e455ba69d157c935c16d6ef6d3c02c348f
    role: context
  - path: reviews/structured/20261021T114716Z-sharpshooter-sulcia-baumannia-model-record/review.yaml
    sha256: aff11413f8cb2b6478af8ed28d36eb135e5b7dc9cca04269fc88c996a4bdc9d6
    role: context
  - path: reviews/structured/20261025T113500Z-c2s4-record-deep-audit/review.yaml
    sha256: 440a518b290067b197bb4b8549bc71408076d6fe93fe3ef5ce4a316f17edacef
    role: context
  - path: reviews/structured/20261025T113600Z-c2s4-frozen-cohort-review/review.yaml
    sha256: 702d202105025d44fc469e588a43967388443aad84a355bc80ea45ebab36338a
    role: context
  - path: reviews/structured/20261025T161500Z-c2s5-remediation-verification/review.yaml
    sha256: c8b7bd9b8e462081a734db496e8314848c4474a56deadbec891cf4af6f9ea644
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/adhoc/pr2043_insect_audit.py
    sha256: dd8692bf52aa61aecefc20f90db8b4a06f7867e9d54477d7bc03656c49c0eb4a
    role: context
  - path: scripts/adhoc/pr2043_insect_review.py
    sha256: 2eb359a251f8f01d3a979307777fadc4431f93bf44bacd03d254de8cd497ba47
    role: context
  - path: scripts/adhoc/pr2043_insect_sources.py
    sha256: 7d7ce4b99582f712e451aaaad46e64ac31e96d2120eef75dad2eec9c34786096
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: src/communitymech/network/auditor.py
    sha256: fe32aa2eddf9e09c153c47576f943bf08a6019f650bf2575e3ddc8e14675049b
    role: context
  - path: src/communitymech/ontology_adapters.py
    sha256: bb3803581ac2946b2ca8e14278e36cd660faf12db9237f9688a6cef577fa9016
    role: context
  - path: src/communitymech/schema/communitymech.yaml
    sha256: a00434e0d75020b2926c9f755d625c09cc78b6f88135805991fcb0ecd4230c83
    role: context
  - path: src/communitymech/schema/history.yaml
    sha256: b01b06f1b9a37db205c26c31ec0fd910690848507c7e1bfb73b424ac0829c52d
    role: context
  - path: src/communitymech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
targets:
- target_id: CommunityMech:000007
  path: kb/communities/BioModels_MODEL1806250004_Sharpshooter_Sulcia_Baumannia.yaml
  label: BioModels MODEL1806250004 Sharpshooter Sulcia-Baumannia Symbiosis
  kind: maintained
  record_class: MicrobialCommunity
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/BioModels_MODEL1806250004_Sharpshooter_Sulcia_Baumannia.yaml
    role: canonical_record
scope:
  description: Entire current target and its two history sidecars; three qualified
    interaction nodes, zero downstream arrows and all nine source snippets. Fresh
    complete primary scientific main, all seven main and three supplementary figures,
    full Text S1, focal S1e/f/g and S1h/i rows, S5o run bounds, S6 model headers,
    BioModels metadata/SBML and focal BioProject metadata. Supplement workbook extraction
    is broader than the human-assessed slices; no exhaustive reaction-list or executable-model
    audit.
  selection: Refresh stale CommunityMech:000007 in PR 2043 against merged main. Environment
    and one embedded history event are the only canonical delta; every original finding
    is reassessed with its stable key and exact predecessor.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000007
checks:
- check_id: validate
  name: validate
  status: passed
  required: true
  summary: Target schema validation passed.
  target_ids:
  - CommunityMech:000007
  command: just --no-dotenv validate kb/communities/BioModels_MODEL1806250004_Sharpshooter_Sulcia_Baumannia.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate
  scope_note: Actual focused target/history execution, except corpus cache-name preflight;
    structural success does not establish scientific support.
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Target strict validation passed.
  target_ids:
  - CommunityMech:000007
  command: just --no-dotenv validate-strict kb/communities/BioModels_MODEL1806250004_Sharpshooter_Sulcia_Baumannia.yaml
    --out /Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2043-batch07/.temp/pr2043/insects/000007/strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-strict
  scope_note: Actual focused target/history execution, except corpus cache-name preflight;
    structural success does not establish scientific support.
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Target term validation passed.
  target_ids:
  - CommunityMech:000007
  command: just --no-dotenv validate-terms kb/communities/BioModels_MODEL1806250004_Sharpshooter_Sulcia_Baumannia.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-terms
  scope_note: Actual focused target/history execution, except corpus cache-name preflight;
    structural success does not establish scientific support.
- check_id: validate-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: Target GTDB syntax/status validation passed.
  target_ids:
  - CommunityMech:000007
  command: just --no-dotenv validate-gtdb kb/communities/BioModels_MODEL1806250004_Sharpshooter_Sulcia_Baumannia.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb
  scope_note: Actual focused target/history execution, except corpus cache-name preflight;
    structural success does not establish scientific support.
- check_id: validate-gtdb-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: Target GTDB domain validation passed.
  target_ids:
  - CommunityMech:000007
  command: just --no-dotenv validate-gtdb-domain kb/communities/BioModels_MODEL1806250004_Sharpshooter_Sulcia_Baumannia.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb-domain
  scope_note: Actual focused target/history execution, except corpus cache-name preflight;
    structural success does not establish scientific support.
- check_id: validate-history
  name: validate-history
  status: passed
  required: true
  summary: Target history validation passed.
  target_ids:
  - CommunityMech:000007
  command: just --no-dotenv validate-history history/records/BioModels_MODEL1806250004_Sharpshooter_Sulcia_Baumannia
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-history
  scope_note: Actual focused target/history execution, except corpus cache-name preflight;
    structural success does not establish scientific support.
- check_id: normalize-cache-names-check
  name: normalize-cache-names-check
  status: passed
  required: true
  summary: Read-only corpus cache-filename preflight passed.
  target_ids:
  - CommunityMech:000007
  command: uv run python scripts/normalize_cache_names.py --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-normalize-cache-names-check
  scope_note: Actual focused target/history execution, except corpus cache-name preflight;
    structural success does not establish scientific support.
- check_id: validate-references-explained
  name: validate-references-explained
  status: passed
  required: true
  summary: Target reference validation passed against the pinned cache.
  target_ids:
  - CommunityMech:000007
  command: just --no-dotenv validate-references-explained kb/communities/BioModels_MODEL1806250004_Sharpshooter_Sulcia_Baumannia.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-references-explained
  scope_note: Actual focused target/history execution, except corpus cache-name preflight;
    structural success does not establish scientific support.
- check_id: audit-network
  name: audit-network
  status: failed
  required: true
  summary: Fresh corpus check reports 44 baseline warnings across 16 of 508 records;
    the focal native audit is empty.
  target_ids:
  - CommunityMech:000007
  command: just --no-dotenv audit-network
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-audit-network
  scope_note: Actual local execution with pinned canary Python/UV environment; corpus
    network diagnostics remain failed and are not represented as a target pass.
- check_id: check-network-quality
  name: check-network-quality
  status: failed
  required: true
  summary: Fresh corpus check reports 44 baseline warnings across 16 of 508 records;
    the focal native audit is empty.
  target_ids:
  - CommunityMech:000007
  command: just --no-dotenv check-network-quality
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-check-network-quality
  scope_note: Actual local execution with pinned canary Python/UV environment; corpus
    network diagnostics remain failed and are not represented as a target pass.
- check_id: source-identity
  name: Primary publication and model identity
  status: passed
  required: true
  summary: Fresh public source identity, model metadata and declared scientific slices
    inspected by the author; no executable reproduction.
  target_ids:
  - CommunityMech:000007
  evidence_ids:
  - pubmed
  - crossref
  - epmc
  - resources
- check_id: scientific-source
  name: Whole-record scientific assessment
  status: passed
  required: true
  summary: Fresh public source identity, model metadata and declared scientific slices
    inspected by the author; no executable reproduction.
  target_ids:
  - CommunityMech:000007
  evidence_ids:
  - source-scope
  - supplement
  - model-boundary
- check_id: cross-mech
  name: Encoded medium and ingredient links
  status: not_applicable
  required: false
  summary: No CultureMech or MediaIngredientMech identifier is encoded; simulated
    hemolymph is not a wet-lab culture recipe.
  target_ids:
  - CommunityMech:000007
  evidence_ids:
  - record
  - methods
- check_id: structured-adapter
  name: Structured source catalog applicability
  status: not_applicable
  required: false
  summary: Fresh iModulonDB organism catalog has no focal partner or insect dataset;
    no target-module claim was inferred.
  target_ids:
  - CommunityMech:000007
  evidence_ids:
  - adapter
evidence:
- evidence_id: record
  kind: record_content
  reference: kb/communities/BioModels_MODEL1806250004_Sharpshooter_Sulcia_Baumannia.yaml
  locator: 'Whole record: three taxonomy entries, three nodes, zero arrows, two dataset
    entries'
  summary: The intended sharpshooter model is identifiable and its graph is qualified;
    microbial membership, ecological state and structured provenance require follow-up.
  support: supports
  accessed_at: '2026-11-06T06:14:37.011891Z'
  snapshot_sha256: 9cbcf07ed58d956c7b6da920f88893ba96bcad2d481afbda647e56ea7340f9ac
- evidence_id: pubmed
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=30254121&retmode=xml
  locator: Article-level metadata
  summary: Article-level PMID, DOI, title and abstract are verified.
  support: supports
  accessed_at: '2026-11-06T06:05:56.824092Z'
  snapshot_sha256: 67c9b795c61ef6b233cd3653148d2fceadd2d9d358db392a799b95f1cff1aab9
- evidence_id: crossref
  kind: database
  reference: https://api.crossref.org/works/10.1128/mBio.01433-18
  locator: Article-level metadata
  summary: DOI, publication title and bibliographic identity are verified.
  support: supports
  accessed_at: '2026-11-06T06:05:57.485666Z'
  snapshot_sha256: ddc17288f4fe1f4781ced1dc88991b00b7102bc6fceada424d0da1f9042d405c
- evidence_id: epmc
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:30254121&format=json&resultType=core
  locator: Article-level metadata
  summary: Article-level identifiers and the open-access full-text route are verified.
  support: supports
  accessed_at: '2026-11-06T06:05:58.629689Z'
  snapshot_sha256: 3956d4f5dbf3f85480eaea96e971bea6af882a1269613faca010bf9bd06f48ef
- evidence_id: sulcia
  kind: primary_source
  reference: PMID:30254121
  locator: Fresh XML s2, Metabolic outputs and metabolic cost subsections; Figures
    2a/d/g and 7b; Table S1f and S1i rows 56–84
  summary: The sharpshooter model releases eight Sulcia essential amino acids. Nitrogen-weighted
    output is about 66% in this model; 66–80% is the explicitly pooled three-system
    range.
  support: supports
  accessed_at: '2026-11-06T06:06:00.294404Z'
  quote: 8 EAAs by Sulcia
  snapshot_sha256: 0cac2dc3b4e28fd1686a41fd36364bdb57aca39edec3cc2818fe58e02405fdd1
- evidence_id: baumannia
  kind: primary_source
  reference: PMID:30254121
  locator: Fresh XML s2, Metabolic outputs and metabolic cost subsections; Figures
    2a/d/g and 7b; Table S1f and S1i rows 87–121
  summary: Baumannia exports histidine and methionine, complementing the eight Sulcia
    EAAs; approximately 10% refers to returned EAA nitrogen relative to host-derived
    input.
  support: supports
  accessed_at: '2026-11-06T06:06:00.294404Z'
  quote: 10% for Baumannia
  snapshot_sha256: 0cac2dc3b4e28fd1686a41fd36364bdb57aca39edec3cc2818fe58e02405fdd1
- evidence_id: reciprocal
  kind: primary_source
  reference: PMID:30254121
  locator: Fresh XML s2, Metabolic inputs and cross-feeding paragraphs; s3 Discussion;
    Figure 4 organism-labeled sharpshooter panel a
  summary: The model predicts extensive host–symbiont exchange and three Sulcia-to-Baumannia
    intermediates serving methionine, peptidoglycan and pantothenate synthesis. Host
    regulatory control remains a hypothesis.
  support: partial
  accessed_at: '2026-11-06T06:06:00.294404Z'
  quote: three instances of transfer
  snapshot_sha256: 0cac2dc3b4e28fd1686a41fd36364bdb57aca39edec3cc2818fe58e02405fdd1
- evidence_id: methods
  kind: primary_source
  reference: PMID:30254121
  locator: Fresh XML s4, The insects, Metabolic model reconstruction and analysis,
    Calculation of symbiont maintenance costs and data statements
  summary: Field-derived bacteriome genomes/transcriptomes inform iNA629; COBRA Toolbox
    3.0, MATLAB and Gurobi support FBA/FVA. The simulations are not a wet-lab coculture
    or ecological stability experiment.
  support: supports
  accessed_at: '2026-11-06T06:06:00.294404Z'
  snapshot_sha256: 0cac2dc3b4e28fd1686a41fd36364bdb57aca39edec3cc2818fe58e02405fdd1
- evidence_id: inference
  kind: primary_source
  reference: PMID:30254121
  locator: Fresh XML s3, opening Discussion paragraph; s1 vertical-transmission background
  summary: The paper frames model outputs as hypotheses for empirical testing. Long-standing
    vertically transmitted associations do not themselves demonstrate a stable ecological
    equilibrium for this record.
  support: partial
  accessed_at: '2026-11-06T06:06:00.294404Z'
  quote: quantitative hypotheses for empirical testing
  snapshot_sha256: 0cac2dc3b4e28fd1686a41fd36364bdb57aca39edec3cc2818fe58e02405fdd1
- evidence_id: supplement
  kind: primary_source
  reference: PMID:30254121
  locator: Text S1, all modeling methods; Table S1f, focal S1h/S1i/S5o rows and S6d;
    all three supplementary figures; fresh EPMC supplementaryFiles archive, Text S1
    and all three SI figures; table-audit.json preserves extraction with focal human-reading
    scope stated separately
  summary: Supplementary constraints and tabulated predicted fluxes support the bounded
    graph. S5o gives run-specific exchange bounds; this is simulated hemolymph, not
    a culture recipe.
  support: supports
  accessed_at: '2026-11-06T06:07:02.386453Z'
  snapshot_sha256: 976d9b7e8b0fef40a84ac913596437b8b4c7551537d347b2679d1d10138cb911
- evidence_id: schema
  kind: authority
  reference: src/communitymech/schema/communitymech.yaml
  locator: MicrobialCommunity.taxonomy; EcologicalStateEnum; CommunityCategoryEnum;
    FunctionalRoleEnum; EvidenceSourceEnum; ComputationalProvenance
  summary: Hosts are excluded from microbial membership but allowed as outside interaction
    participants. STABLE requires equilibrium; computational provenance has dedicated
    model, tools, input and simulated-medium fields.
  support: supports
  accessed_at: '2026-11-06T06:14:37.011891Z'
  snapshot_sha256: a00434e0d75020b2926c9f755d625c09cc78b6f88135805991fcb0ecd4230c83
- evidence_id: ontology
  kind: authority
  reference: kb/communities/BioModels_MODEL1806250004_Sharpshooter_Sulcia_Baumannia.yaml
  locator: .temp/pr2043/insects/000007/replay-qualified.json
  summary: All seven unique curated term pairs across eleven occurrences match local
    OAK labels; fresh NCBI independently confirms all focal taxon names and OLS confirms
    ENVO:01001002. Label validity does not establish microbial membership.
  support: supports
  accessed_at: '2026-11-06T06:14:37.011891Z'
  snapshot_sha256: 38722e1caa8d1311d52b61d1b54c2c7f11298be3d5d48dee36d64619f30ca0e8
- evidence_id: snippets
  kind: validation
  reference: kb/communities/BioModels_MODEL1806250004_Sharpshooter_Sulcia_Baumannia.yaml
  locator: .temp/pr2043/insects/000007/replay-qualified.json
  summary: 'All nine excerpts match fresh primary sources after NFKC/whitespace normalization:
    eight interaction snippets occur in the full article XML and the resource quotation
    is the exact punctuated PubMed title. The initial article-only replay correctly
    misses that PubMed-specific terminal period; the qualified replay preserves source
    boundaries.'
  support: supports
  accessed_at: '2026-11-06T06:14:37.011891Z'
  snapshot_sha256: 38722e1caa8d1311d52b61d1b54c2c7f11298be3d5d48dee36d64619f30ca0e8
- evidence_id: history
  kind: record_content
  reference: history/records/BioModels_MODEL1806250004_Sharpshooter_Sulcia_Baumannia/2026-10-25T151200Z-antigravity-2072.yaml
  locator: events[0].details, compared with current environment_term.notes and embedded
    curation_history[1]
  summary: The new external history sidecar wrongly cites PMID:29944653 for the insect
    environment addition. That PMID resolves to an unrelated human urinary-symptom
    questionnaire study. The current record correctly cites insect modeling paper
    PMID:30254121; the source-backed ENVO addition and grouped missing-field resolution
    remain valid.
  support: supports
  accessed_at: '2026-11-06T06:14:37.011891Z'
  snapshot_sha256: b5b5cf152359cca34ece1f1fb16a77c04aa49c84827fc66bf9e780d571696e8c
- evidence_id: resources
  kind: database
  reference: kb/communities/BioModels_MODEL1806250004_Sharpshooter_Sulcia_Baumannia.yaml
  locator: Fresh MODEL1806250004 metadata and file list; verified SBML payload, focal
    BioProject XML, immutable author tree/payload at bb20c83c112331442b19a7b5f16f6cd6389221b4
  summary: BioModels file identity is verified; focal project PRJNA341855 and the
    immutable author repository are distinct resources. PMID:30254121 is a publication,
    not a dataset deposit.
  support: supports
  accessed_at: '2026-11-06T06:07:06.656446Z'
  snapshot_sha256: 0d7c21addfaba17a2a1ffe52c101561388a56c2c144133036173801ebb5d82d1
- evidence_id: model-boundary
  kind: validation
  reference: kb/communities/BioModels_MODEL1806250004_Sharpshooter_Sulcia_Baumannia.yaml
  locator: '.temp/pr2043/insects/shared/model-audit.json: focal model identity, archive
    digest, compartments and selected exchange bounds'
  summary: Read-only SBML inspection distinguishes three biological actors, extracellular
    compartment, stored defaults and published run constraints; it does not reproduce
    the simulation.
  support: context_only
  accessed_at: '2026-11-06T06:14:37.011891Z'
  snapshot_sha256: 3c0da359b258f5ce404ea4f975e0bdf919c3a7024efa762c58ec4e2f65cc3f61
- evidence_id: native-target
  kind: validation
  reference: kb/communities/BioModels_MODEL1806250004_Sharpshooter_Sulcia_Baumannia.yaml
  locator: .temp/pr2043/insects/000007/replay-qualified.json
  summary: Target-native audit returns no issues for the three-node, zero-arrow graph;
    eight interaction evidence occurrences are counted separately from one resource-title
    citation. Structural consistency does not certify equilibrium or membership.
  support: supports
  accessed_at: '2026-11-06T06:14:37.011891Z'
  snapshot_sha256: 38722e1caa8d1311d52b61d1b54c2c7f11298be3d5d48dee36d64619f30ca0e8
- evidence_id: source-scope
  kind: validation
  reference: PMID:30254121
  locator: Fresh shared retrieval receipts and archive-inventory.json; article Sections
    1–4, all main/SI figures, Text S1 and focal table/model slices
  summary: The author read fresh primary main text and the stated asset slices. Supplement
    bytes and model identity were independently retrieved in this author pass; computational
    outputs were not recomputed, raw sequences were not inspected, and no independent
    approval is claimed.
  support: supports
  accessed_at: '2026-11-06T06:14:37.011891Z'
  snapshot_sha256: 57e630a2d82ca134d56d13a75d6889fbf312c8b6fc4ce092db7d543511eb9fec
- evidence_id: search
  kind: search
  reference: Owned maintained roots
  locator: .temp/pr2043/insects/000007/local-search.stdout.txt
  summary: Ignored-inclusive exact ID/slug and source-PMID search found source caches,
    target sidecars and relevant graph-decision files. No focal match was returned
    from kb/taxa; this bounded result does not establish machine-wide absence.
  support: supports
  accessed_at: '2026-11-06T06:14:37.011891Z'
  search_scope: rg --no-ignore --hidden over references_cache, history, reports/causal_graph_review/decisions
    and kb/taxa, including ignored files.
  snapshot_sha256: d489a9e52c503764c89fc576a982a96b2bce4c03685f15deac0384bdad4678d7
- evidence_id: adapter
  kind: search
  reference: https://imodulondb.org/api/datasets
  locator: Fresh public organism/dataset catalog
  summary: The structured iModulonDB catalog has no Sulcia/Karelsulcia, Sodalis, Baumannia/Palibaumannia,
    Hodgkinia or focal insect entry. E. coli is a reconstruction reference, not the
    focal symbiosis; its expression modules do not establish insect-host mechanisms.
    No matching module query is applicable and catalog absence is not negative biological
    evidence.
  support: supports
  accessed_at: '2026-11-06T06:07:45.901602Z'
  search_scope: All organism entries in the fresh public structured catalog; no machine-wide
    adapter-availability assertion.
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
- evidence_id: current-delta
  kind: record_content
  reference: kb/communities/BioModels_MODEL1806250004_Sharpshooter_Sulcia_Baumannia.yaml
  locator: .temp/pr2043/insects/000007/target-diff.stdout.txt
  summary: Only environment_term and the corresponding embedded history event were
    added; the four previously flagged fields remain unchanged.
  support: supports
  accessed_at: '2026-11-06T06:14:37.011891Z'
  snapshot_sha256: 1a2454506079a379dd72a169c98af60a82997b16a55f9644bc80058655790f98
- evidence_id: environment-authority
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FENVO_01001002
  locator: Fresh ENVO:01001002 label and definition plus primary Introduction/Methods
    and Figure 1
  summary: ENVO:01001002 is animal-associated environment, an environmental system
    determined by an animal. The broad term fits the modeled intracellular insect
    bacteriome; the preferred term supplies host detail without claiming a more specific
    ENVO identity.
  support: supports
  accessed_at: '2026-11-06T06:07:44.701097Z'
  snapshot_sha256: a06ca8fc5dc0ec836640503fbfa61f174a7e0a2afb91ff77b0a66c97c1f7b8d4
- evidence_id: history-wrong-source
  kind: database
  reference: PMID:29944653
  locator: Fresh PubMed ArticleTitle and Abstract, compared with external history
    events[0].details
  summary: This identifier denotes a clinical comparison of nocturia and prostate-symptom
    questionnaires in men, not insect endosymbiont modeling. PMID:30254121 supplies
    the supported focal environment context.
  support: refutes
  accessed_at: '2026-11-06T06:10:57.553642Z'
  snapshot_sha256: a49539c5097172b4eba31c6d2935a918fe06c40012e272ab58198361e53b9008
- evidence_id: environment-lineage
  kind: prior_review
  reference: reviews/structured/20261025T161500Z-c2s5-remediation-verification/review.yaml
  locator: c2s4-biomodels-missing-environment-term, including its two exact c2s4 grouped
    predecessors
  summary: The resolved grouped finding covers 000006, 000007, 000008 and 000013.
    This single-target successor confirms only its own source-supported field addition;
    it does not supersede the four-target disposition or reassess the other members.
    A separate history-PMID defect does not undo field presence.
  support: context_only
  accessed_at: '2026-11-06T06:14:37.011891Z'
  snapshot_sha256: 3709b0be5ed9944370788a932dd45b373b328f7864e9fbfd3af80c6136fbd5c0
- evidence_id: check-validate
  kind: validation
  reference: just --no-dotenv validate kb/communities/BioModels_MODEL1806250004_Sharpshooter_Sulcia_Baumannia.yaml
  locator: .temp/pr2043/insects/000007/validate.json
  summary: Target schema validation passed.
  support: supports
  accessed_at: '2026-11-06T06:06:31.317780Z'
  snapshot_sha256: 9201460664db409dbd5e16146c3e4b89628ed5e313b06bb1fc11cb34736c78b1
- evidence_id: check-validate-strict
  kind: validation
  reference: just --no-dotenv validate-strict kb/communities/BioModels_MODEL1806250004_Sharpshooter_Sulcia_Baumannia.yaml
    --out /Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2043-batch07/.temp/pr2043/insects/000007/strict.tsv
  locator: .temp/pr2043/insects/000007/validate-strict.json
  summary: Target strict validation passed.
  support: supports
  accessed_at: '2026-11-06T06:06:32.726393Z'
  snapshot_sha256: 3c203e914a5cbeb115f282d8cbc240bdb34c429b065bae6983d1c9107427446d
- evidence_id: check-validate-terms
  kind: validation
  reference: just --no-dotenv validate-terms kb/communities/BioModels_MODEL1806250004_Sharpshooter_Sulcia_Baumannia.yaml
  locator: .temp/pr2043/insects/000007/validate-terms.json
  summary: Target term validation passed.
  support: supports
  accessed_at: '2026-11-06T06:06:33.698901Z'
  snapshot_sha256: dd0a003163617a16b42ab77143a63d858e969e4a41b43a974a0192394de83e0b
- evidence_id: check-validate-gtdb
  kind: validation
  reference: just --no-dotenv validate-gtdb kb/communities/BioModels_MODEL1806250004_Sharpshooter_Sulcia_Baumannia.yaml
  locator: .temp/pr2043/insects/000007/validate-gtdb.json
  summary: Target GTDB syntax/status validation passed.
  support: supports
  accessed_at: '2026-11-06T06:06:33.751440Z'
  snapshot_sha256: 3e5d2618985bc2ecda773086c41eb54d1ac4dea259095e9f70994f8960ca8e66
- evidence_id: check-validate-gtdb-domain
  kind: validation
  reference: just --no-dotenv validate-gtdb-domain kb/communities/BioModels_MODEL1806250004_Sharpshooter_Sulcia_Baumannia.yaml
  locator: .temp/pr2043/insects/000007/validate-gtdb-domain.json
  summary: Target GTDB domain validation passed.
  support: supports
  accessed_at: '2026-11-06T06:06:34.643304Z'
  snapshot_sha256: a80f0f4e2cfaf70e7873454b8aad876140de13ac1846d548a23c28f91476a1c3
- evidence_id: check-validate-history
  kind: validation
  reference: just --no-dotenv validate-history history/records/BioModels_MODEL1806250004_Sharpshooter_Sulcia_Baumannia
  locator: .temp/pr2043/insects/000007/validate-history.json
  summary: Target history validation passed.
  support: supports
  accessed_at: '2026-11-06T06:06:35.176798Z'
  snapshot_sha256: 01c6ab2d08965555980963389139847c571b7c75cff3036d97266250594b76b2
- evidence_id: check-normalize-cache-names-check
  kind: validation
  reference: uv run python scripts/normalize_cache_names.py --check
  locator: .temp/pr2043/insects/000007/normalize-cache-names-check.json
  summary: Read-only corpus cache-filename preflight passed.
  support: supports
  accessed_at: '2026-11-06T06:06:35.216098Z'
  snapshot_sha256: 765eb86e1e224d4d2753ed196726ffb7bc3fda8d5b3a4e6ccb11532a1413cffb
- evidence_id: check-validate-references-explained
  kind: validation
  reference: just --no-dotenv validate-references-explained kb/communities/BioModels_MODEL1806250004_Sharpshooter_Sulcia_Baumannia.yaml
  locator: .temp/pr2043/insects/000007/validate-references-explained.json
  summary: Target reference validation passed against the pinned cache.
  support: supports
  accessed_at: '2026-11-06T06:06:35.944983Z'
  snapshot_sha256: a71c7270d09be546922d91185f3853fd2bfcb9521ee78c59ab816d93698d1c06
- evidence_id: check-audit-network
  kind: validation
  reference: just --no-dotenv audit-network
  locator: .temp/pr2043/insects/shared/audit-network.json
  summary: Fresh corpus check reports 44 baseline warnings across 16 of 508 records;
    the focal native audit is empty.
  support: context_only
  accessed_at: '2026-11-06T06:06:45.380860Z'
  snapshot_sha256: 4951fc69e06675f2f5b033664f43499cde41341ad343d0595050a00e484088a6
- evidence_id: check-check-network-quality
  kind: validation
  reference: just --no-dotenv check-network-quality
  locator: .temp/pr2043/insects/shared/check-network-quality.json
  summary: Fresh corpus check reports 44 baseline warnings across 16 of 508 records;
    the focal native audit is empty.
  support: context_only
  accessed_at: '2026-11-06T06:06:49.626525Z'
  snapshot_sha256: 0d248716d7e391d66134536d180d38abe777321a72d997e04606f0ba1d27e8a2
assessments:
- assessment_id: identity
  area: identity
  topic: Exact model and biological actors
  outcome: concern
  summary: MODEL1806250004 is the intended iNA629 sharpshooter model; the host should
    remain external to microbial membership.
  target_ids:
  - CommunityMech:000007
  evidence_ids:
  - record
  - methods
  - schema
  - resources
  dimensions:
  - name: community_scope
    value: Two endosymbiotic bacteria modeled with their insect host
    definition: Three biological model compartments do not make the insect a microbial
      community member.
    evidence_ids:
    - schema
    - resources
  - name: source_strain
    value: Field-derived Sulcia and Baumannia associated with G. coccinea
    definition: The paper identifies the host and source bacteriomes; the source supports
      Sulcia at its recorded broad rank and Baumannia cicadellinicola; neither identifies
      a culture-collection strain.
    evidence_ids:
    - methods
    - ontology
  - name: environment
    value: ENVO:01001002 animal-associated environment; modeled intracellular bacteriome
      and external hemolymph
    definition: Fresh primary host/bacteriocyte context supports the broad canonical
      ENVO term, while the preferred term preserves the focal insect habitat.
    evidence_ids:
    - methods
    - environment-authority
  - name: medium
    value: In-silico minimal hemolymph with constrained exchange
    definition: Use computational_provenance.simulated_medium, preserving published
      run bounds and the S5o cystathionine detail; no growth_media recipe is warranted.
    evidence_ids:
    - methods
    - supplement
    - model-boundary
  - name: experimental_setting
    value: Genome/transcriptome-informed FBA and FVA
    definition: G. coccinea adults were field-collected in Ithaca in July 2015; four
      transcriptome samples informed reconstruction, not a dynamic stability assay.
    evidence_ids:
    - methods
  - name: evidence_tier
    value: Computational predictions with explicit assumptions
    definition: Nitrogen accounting, reciprocal benefit and limited cross-feeding
      are model outputs; host-control mediation and ecological equilibrium were not
      demonstrated.
    evidence_ids:
    - sulcia
    - baumannia
    - reciprocal
    - inference
  - name: grounding_status
    value: Valid host and Baumannia species, Sulcia genus, amino acids and broad GO
      term
    definition: Canonical Karelsulcia and Palibaumannia labels coexist with source
      preferred names; encoded bacterial GTDB grounding and host NO_GTDB_EQUIVALENT
      remain bounded.
    evidence_ids:
    - ontology
- assessment_id: taxonomy
  area: grounding
  topic: Membership, roles and names
  outcome: concern
  summary: Remove the host from the membership list while retaining its supported
    graph endpoints.
  target_ids:
  - CommunityMech:000007
  evidence_ids:
  - schema
  - ontology
  - methods
  - reciprocal
  details: The microbial partners and broad syntrophic-metabolism roles are compatible
    with model-predicted cooperative metabolism. No extra obligacy or product-removal
    test is imported into these broad category/role definitions. The current source-based
    bacterial ranks are retained; no unverified exact strain or extra taxon is added.
    Historical GTDB mapping statistics were not re-certified.
- assessment_id: node-0
  area: graph
  topic: 'ecological_interactions[0]: Sulcia provisioning'
  outcome: supported
  summary: Retain the COMPUTATIONAL Sulcia → G. coccinea provisioning and modeled
    reciprocal benefit.
  target_ids:
  - CommunityMech:000007
  evidence_ids:
  - sulcia
  - methods
  - supplement
  details: Eight EAA exports, including the two encoded L-amino acids, support the
    node. The nitrogen percentage is weighted transport flux relative to host-derived
    nitrogen input, not concentration or a tracer measurement. The current 66–80%
    wording is explicitly pooled across systems; the sharpshooter figure/table is
    approximately 66%. No downstream arrow is needed.
- assessment_id: node-1
  area: graph
  topic: 'ecological_interactions[1]: Baumannia complementarity'
  outcome: supported
  summary: Retain the COMPUTATIONAL Baumannia → G. coccinea model interpretation and
    its limitations.
  target_ids:
  - CommunityMech:000007
  evidence_ids:
  - baumannia
  - reciprocal
  - methods
  details: The two exported EAAs are histidine and methionine. The approximately 10%
    nitrogen return is not the separate 8% contribution to total EAA release. Host
    support and three Sulcia-to-Baumannia intermediates are modeled; they prevent
    an absolute segregation claim. Host regulatory control remains PARTIAL.
- assessment_id: node-2
  area: graph
  topic: 'ecological_interactions[2]: Host-mediated complementarity'
  outcome: supported
  summary: Retain community-level modeled reciprocal nutrition with PARTIAL host-control
    interpretation.
  target_ids:
  - CommunityMech:000007
  evidence_ids:
  - reciprocal
  - methods
  - inference
  - supplement
  details: The modeled actors are Sulcia, Baumannia and their host; three intermediates
    (homoserine, LL-2,6-diaminoheptanedioate and 3-methyl-2-oxobutanoate) pass from
    Sulcia to Baumannia through the modeled host compartment. This does not experimentally
    establish host regulation or absence of bacterial cross-feeding. The broad GO:0044419
    term is compatible with interspecies processes. The existing zero-arrow graph
    correctly avoids component-to-summary causation.
- assessment_id: state
  area: evidence
  topic: Ecological state versus computational steady state
  outcome: concern
  summary: STABLE is not established as ecological equilibrium by the inspected source.
  target_ids:
  - CommunityMech:000007
  evidence_ids:
  - schema
  - inference
  - methods
  details: The source describes an ancient, vertically transmitted natural association
    and optimizes constrained metabolic fluxes. It does not measure community dynamics
    or recovery to equilibrium. NATURAL remains appropriate to the modeled biological
    association; creating a model does not imply ENGINEERED biological origin.
- assessment_id: conditions
  area: completeness
  topic: Structured computational provenance
  outcome: concern
  summary: Recoverable model/run settings remain only in source text and the existing
    discussion.
  target_ids:
  - CommunityMech:000007
  evidence_ids:
  - schema
  - methods
  - supplement
  - model-boundary
  details: Record FBA/FVA, COBRA Toolbox 3.0, MATLAB/Gurobi without invented versions,
    iNA629 and source accessions, objective and simulated hemolymph. Distinguish ordinary
    growth from maintenance-cost simulations. BioModels glucose/ammonium defaults
    of −1000 differ from published −100 run bounds; stored zero flux fields are not
    observed optimal outputs. The discussion already captures important assumptions
    and should be preserved.
- assessment_id: resources
  area: completeness
  topic: Models, publication and input data
  outcome: concern
  summary: The model file is valid; the primary publication belongs in evidence/resources
    rather than as a dataset.
  target_ids:
  - CommunityMech:000007
  evidence_ids:
  - resources
  - methods
  details: PRJNA341855 is the focal sharpshooter project; PRJNA342845 and PRJNA343314
    are other insect systems. The author repository is pinned to commit bb20c83c112331442b19a7b5f16f6cd6389221b4.
    Its model blob differs bytewise from BioModels; identity is supported, but scientific
    or executable equivalence was not tested. NON_CURATED is archive status, not proof
    of an invalid model.
- assessment_id: provenance
  area: provenance
  topic: Snippets and previous graph repairs
  outcome: concern
  summary: Original graph qualifications and all nine source snippets remain supported,
    but the new external environment-history event cites an unrelated paper.
  target_ids:
  - CommunityMech:000007
  evidence_ids:
  - snippets
  - history
  - history-wrong-source
  - current-delta
  details: The MD cache remains labeled abstract_only despite appended main text;
    the TXT is abstract/bibliographic material. Fresh full XML and PubMed were independently
    matched. The external sidecar requires append-only correction; its historical
    bytes must not be rewritten. No current GitHub issue status is inferred from the
    predecessor.
- assessment_id: validation
  area: schema
  topic: Native checks and source assessment
  outcome: supported
  summary: All eight native checks pass; semantic and evidence findings remain despite
    those passes.
  target_ids:
  - CommunityMech:000007
  evidence_ids:
  - check-validate
  - check-validate-references-explained
  - ontology
  - source-scope
- assessment_id: metrics
  area: completeness
  topic: Native completeness and quality
  outcome: supported
  summary: Mechanical scores do not certify host membership, equilibrium or simulation
    reproducibility.
  target_ids:
  - CommunityMech:000007
  evidence_ids:
  - native-target
  - record
  metrics:
  - name: completeness
    value: 80
    unit: points
    minimum: 0
    maximum: 100
    definition: 'min(100, 50 required metadata including roles + 5 environment + 10
      at least 3 factors + 10 at least 3 nodes + 5 resources + 10 media + 5 datasets
      + 5 node metabolites). Current record: 50 + 5 + 0 + 10 + 5 + 0 + 5 + 5 = 80.'
  - name: validation_quality
    value: 100
    unit: points
    minimum: 0
    maximum: 100
    definition: 'clamp(100 - 50 P1 - 10 P2 - 2 P3 + 20 min(mean node evidence / 2,
      1) + 15 if native COMPLETE, 0, 100). P1 = 0, P2 = 2, P3 = 3, P4 = 0; 8 evidence
      / 3 nodes gives 20 evidence bonus and 15 network bonus: 109 before capping.
      Scores are not scientific approval.'
  - name: P1
    value: 0
    unit: findings
    definition: Observed native severity count.
  - name: P2
    value: 2
    unit: findings
    definition: Observed native severity count.
  - name: P3
    value: 3
    unit: findings
    definition: Observed native severity count.
  - name: P4
    value: 0
    unit: findings
    definition: Observed native severity count.
- assessment_id: environment-refresh
  area: grounding
  topic: Current-main habitat addition and bounded prior disposition
  outcome: supported
  summary: The new broad ENVO term and focal insect note match primary host-associated
    modeling context; the earlier grouped missing-field resolution is preserved.
  details: The environment is natural intracellular symbiosis represented computationally,
    not a wet-lab medium or evidence of ecological equilibrium. The single-target
    review does not retire a multi-target predecessor. Correcting the sidecar source
    attribution is separate from retaining this field.
  target_ids:
  - CommunityMech:000007
  evidence_ids:
  - current-delta
  - environment-authority
  - methods
  - environment-lineage
findings:
- finding_id: host-membership
  issue_key: cm-000007-host-membership
  category: scope
  severity: major
  native_severity: P2
  normalization_reason: 'P2 major: the field materially misrepresents community membership
    or asserts an unsupported ecological property; valid model identity and graph
    are preserved.'
  rule_id: review-checklist.claim-scope-and-completeness
  status: open
  certainty: confirmed
  title: Separate the insect host from microbial membership
  description: taxonomy[0] contains G. coccinea despite the schema excluding hosts
    from the microbial roster.
  target_ids:
  - CommunityMech:000007
  field_paths:
  - taxonomy[0]
  evidence_ids:
  - schema
  - methods
  - resources
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/BioModels_MODEL1806250004_Sharpshooter_Sulcia_Baumannia.yaml
    role: canonical_record
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261021T114716Z-sharpshooter-sulcia-baumannia-model-record
    finding_id: host-membership
- finding_id: ecological-equilibrium
  issue_key: cm-000007-ecological-equilibrium
  category: evidence
  severity: major
  native_severity: P2
  normalization_reason: 'P2 major: the field materially misrepresents community membership
    or asserts an unsupported ecological property; valid model identity and graph
    are preserved.'
  rule_id: review-checklist.claim-scope-and-completeness
  status: open
  certainty: confirmed
  title: Qualify the unsupported STABLE designation
  description: The source supports a natural symbiosis and steady-state metabolic
    predictions, not the ecological equilibrium asserted by STABLE.
  target_ids:
  - CommunityMech:000007
  field_paths:
  - ecological_state
  evidence_ids:
  - schema
  - methods
  - inference
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/BioModels_MODEL1806250004_Sharpshooter_Sulcia_Baumannia.yaml
    role: canonical_record
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261021T114716Z-sharpshooter-sulcia-baumannia-model-record
    finding_id: ecological-equilibrium
- finding_id: computational-provenance
  issue_key: cm-000007-computational-provenance
  category: completeness
  severity: minor
  native_severity: P3
  normalization_reason: 'P3 minor: bounded structured-provenance/resource correction
    preserves the identified model and scientific interpretation.'
  rule_id: review-checklist.claim-scope-and-completeness
  status: open
  certainty: confirmed
  title: Structure the model and run assumptions
  description: The eight interaction evidence items lack computational_provenance
    despite recoverable methods and existing narrative assumptions.
  target_ids:
  - CommunityMech:000007
  field_paths:
  - ecological_interactions[0].evidence
  - ecological_interactions[1].evidence
  - ecological_interactions[2].evidence
  evidence_ids:
  - schema
  - methods
  - supplement
  - model-boundary
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/BioModels_MODEL1806250004_Sharpshooter_Sulcia_Baumannia.yaml
    role: canonical_record
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261021T114716Z-sharpshooter-sulcia-baumannia-model-record
    finding_id: computational-provenance
- finding_id: resource-types
  issue_key: cm-000007-resource-types
  category: completeness
  severity: minor
  native_severity: P3
  normalization_reason: 'P3 minor: bounded structured-provenance/resource correction
    preserves the identified model and scientific interpretation.'
  rule_id: review-checklist.claim-scope-and-completeness
  status: open
  certainty: confirmed
  title: Separate the publication from study resources
  description: The Primary publication entry is classified as an associated dataset,
    while verified focal input/repository links remain unstructured.
  target_ids:
  - CommunityMech:000007
  field_paths:
  - associated_datasets[1]
  - associated_datasets
  - external_resources
  evidence_ids:
  - resources
  - methods
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/BioModels_MODEL1806250004_Sharpshooter_Sulcia_Baumannia.yaml
    role: canonical_record
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261021T114716Z-sharpshooter-sulcia-baumannia-model-record
    finding_id: resource-types
- finding_id: environment-history-source
  issue_key: cm-000007-environment-history-source
  category: provenance
  severity: minor
  native_severity: P3
  normalization_reason: 'P3 minor: an external provenance event cites an unrelated
    source, while record identity, supported environment grounding and the embedded
    citation remain correct.'
  rule_id: review-checklist.audit
  status: open
  certainty: confirmed
  title: Append a correction for the environment-history source PMID
  description: history/records/BioModels_MODEL1806250004_Sharpshooter_Sulcia_Baumannia/2026-10-25T151200Z-antigravity-2072.yaml:events[0].details
    attributes the environment addition to PMID:29944653, an unrelated human clinical
    questionnaire study. The target environment_term.notes and actual insect model
    source use PMID:30254121. Preserve the original event and append a precise corrective
    provenance entry.
  target_ids:
  - CommunityMech:000007
  field_paths:
  - history/records/BioModels_MODEL1806250004_Sharpshooter_Sulcia_Baumannia/2026-10-25T151200Z-antigravity-2072.yaml:events[0].details
  evidence_ids:
  - history
  - history-wrong-source
  - methods
  - environment-authority
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: history/records/BioModels_MODEL1806250004_Sharpshooter_Sulcia_Baumannia
    role: append_only_provenance
actions:
- action_id: repair-host-membership
  description: Separate the insect host from microbial membership.
  finding_ids:
  - host-membership
  target_ids:
  - CommunityMech:000007
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/BioModels_MODEL1806250004_Sharpshooter_Sulcia_Baumannia.yaml
    role: canonical_record
  acceptance_checks:
  - Remove the insect from microbial taxonomy during authorized curation; retain Sulcia
    and Baumannia as microbial members.
  - Preserve G. coccinea as the external recipient/participant in the model graph
    and narrative. Do not delete the host compartment from the scientific interpretation.
  - Do not reinsert the host merely to satisfy external-participant network warnings;
    assess those warnings against the schema.
- action_id: repair-ecological-equilibrium
  description: Qualify the unsupported STABLE designation.
  finding_ids:
  - ecological-equilibrium
  target_ids:
  - CommunityMech:000007
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/BioModels_MODEL1806250004_Sharpshooter_Sulcia_Baumannia.yaml
    role: canonical_record
  acceptance_checks:
  - Supply ecological evidence for stable equilibrium or explicitly document the unresolved
    state; distinguish long evolutionary association from demonstrated equilibrium.
  - 'Do not automatically substitute ENGINEERED or TRANSIENT: neither follows from
    creating a metabolic model.'
  - If the required enum cannot represent uncertainty truthfully, record the bounded
    schema issue for separately authorized follow-up rather than inventing biological
    dynamics.
- action_id: repair-computational-provenance
  description: Structure the model and run assumptions.
  finding_ids:
  - computational-provenance
  target_ids:
  - CommunityMech:000007
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/BioModels_MODEL1806250004_Sharpshooter_Sulcia_Baumannia.yaml
    role: canonical_record
  acceptance_checks:
  - Populate claim-level computational provenance with FBA/FVA, COBRA Toolbox 3.0,
    MATLAB/Gurobi, iNA629, model source/input accession and modeled bacteriocyte/hemolymph
    context; leave unreported software versions unset.
  - Preserve oxygen uptake 20, published run uptake caps, equal bacterial biomass
    lower bounds 0.01, objective and transport-cost assumptions with their units and
    source scope. Distinguish maintenance-cost simulations from baseline growth.
  - Retain the discrepancy between deposited exchange bounds and published runtime
    settings, and S5o cystathionine versus closed proteinogenic-amino-acid exchanges.
    Do not turn default zero FLUX_VALUE entries into results.
  - Keep wet-lab growth_media absent; retain the existing discussion and all three
    qualified nodes with no arrows.
- action_id: repair-resource-types
  description: Separate the publication from study resources.
  finding_ids:
  - resource-types
  target_ids:
  - CommunityMech:000007
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/BioModels_MODEL1806250004_Sharpshooter_Sulcia_Baumannia.yaml
    role: canonical_record
  acceptance_checks:
  - Move PMID:30254121 to an appropriate publication/evidence resource; preserve the
    actual BioModels MODEL1806250004 file entry.
  - Link the verified focal PRJNA341855 host-transcriptome/symbiont-genome project
    and immutable author repository commit with their exact host/model scope. Do not
    import the two other insect projects as focal data.
  - Keep archive status, byte differences and unexecuted model boundaries explicit;
    do not claim raw-data inspection, reproducibility or strain-resolution from this
    metadata check.
- action_id: preserve-model-graph
  description: Preserve computational scope and the three-node, zero-arrow graph during
    separately authorized curation.
  finding_ids:
  - host-membership
  - ecological-equilibrium
  - computational-provenance
  - resource-types
  target_ids:
  - CommunityMech:000007
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/BioModels_MODEL1806250004_Sharpshooter_Sulcia_Baumannia.yaml
    role: canonical_record
  acceptance_checks:
  - Keep host-mediated regulation PARTIAL, the three bacterial exchanges explicit
    and all nitrogen quantities source-scoped.
  - Do not restore component-to-summary arrows or assert measured transfer, fitness,
    equilibrium or model reproducibility.
  - Preserve append-only history and rerun schema, strict, term, reference, history
    and target/corpus network checks after authorized changes.
  - Keep insect_model_nitrogen_and_host_control as an explicit source-boundary discussion.
    Any future evidence update must distinguish measured transfer/regulation from
    model predictions; no new experiment, paid research or author contact is requested.
- action_id: correct-environment-history-source
  description: During separately authorized curation, append a correction identifying
    the erroneous historical source citation.
  finding_ids:
  - environment-history-source
  target_ids:
  - CommunityMech:000007
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: history/records/BioModels_MODEL1806250004_Sharpshooter_Sulcia_Baumannia
    role: append_only_provenance
  acceptance_checks:
  - Create a new history entry for CommunityMech:000007 naming history/records/BioModels_MODEL1806250004_Sharpshooter_Sulcia_Baumannia/2026-10-25T151200Z-antigravity-2072.yaml:events[0].details,
    its incorrect PMID:29944653, and the supported replacement PMID:30254121.
  - Preserve the original historical file byte-for-byte; explain that the canonical
    environment field and embedded citation were already supported and remain unchanged.
  - Keep the resolved grouped missing-environment disposition intact and retain the
    four unrelated original findings until their separate curation is verified.
  - Validate the new history entry, inspect the append-only diff and verify no unsupported
    ecological-state or host-membership promotion.
limitations:
- No FBA/FVA optimization, model/code execution, MATLAB payload, transcriptome reconstruction
  or raw-sequence analysis was performed. Archive metadata and structural XML checks
  do not establish reproducibility.
- Supplementary workbook reading was bounded to inventories/headers and declared focal
  sheets/rows; large reaction lists and other-insect numerical tables were not exhaustively
  audited.
- BioModels defaults differ from published runtime constraints; the author-repository
  model is not byte-identical. Neither fact establishes wrong model identity, and
  stored zero flux values are not published results.
- Figure 4 caption and panel labels disagree on sharpshooter panel lettering. S5o
  permits cystathionine despite prose amino-acid exclusion; the twenty listed proteinogenic
  amino-acid exchanges are closed. S6d uses component-model header names iNA81/iNA258
  whereas main Methods uses iNA74/iNA234; preserve that source naming discrepancy.
  These source nuances constrain future provenance expansion.
- Exact culture-collection strains, historical GTDB mapping statistics, replacement
  ecological-state classification and executable model equivalence were not established;
  no empirical host-control or dynamic-equilibrium assay is inferred.
- Supplementary human reading was limited to focal EAA outputs and exchange scope
  in S1e/f/g, S1h, nitrogen definitions/summaries in S1i, all S5o medium bounds, S6
  component headers, Text S1 and all SI figures. Extracting every workbook cell is
  not an exhaustive scientific audit of those cells.
- Fresh corpus network checks return baseline exit 1 with 44 warnings across 16 of
  508 records. The focal native audit is empty; unrelated records were not scientifically
  reviewed.
notes:
- Author refresh only; no canonical record, cache, history, schema or generated-product
  edit, no executable-model reproduction and no independent-approval claim.
- Initial input pins were captured before assessment and rechecked before final inspection.
  The four original open findings retain exact previous_occurrences; only the separate
  external-history source finding is new.
- The grouped c2s5 missing-environment resolution is contextual only. Its four-target
  scope is not superseded or narrowed by this one-target observation.
- Completeness rises from 75 to 80 because environment_term is present. Quality is
  capped at 100 from 109 and does not negate two major and three minor findings.
- The existing source-boundary discussion is covered by the preserve-model-graph acceptance
  checks; it is not a demand to perform experiments. Primary quoted excerpts remain
  the predecessor's short quotations.
tags:
- record-review
- metabolic-model
- endosymbiosis
- batch-07
- pr-2043-refresh
```
