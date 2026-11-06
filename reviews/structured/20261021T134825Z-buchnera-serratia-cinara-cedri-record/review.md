# Buchnera–Serratia Cinara cedri consortium record review

- Review: 20261021T134825Z-buchnera-serratia-cinara-cedri-record
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-21T13:42:36.299641Z
- Finished UTC: 2026-10-21T13:48:25.230034Z
- Reviewer: codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The natural two-bacterium identity and three qualified nodes/two hypothesized arrows are supported by comparative genomic reconstruction. One major finding concerns the unqualified STABLE equilibrium label; one minor concerns missing structured reconstruction provenance. Broad nutritional-cooperation roles/category remain bounded, and current source identity is verified despite the disclosed cache-header mismatch.

## Scope And Provenance

Whole record, each node and each arrow reviewed against the complete primary main, relevant figures/SI, current ontology, source genome metadata and provenance.

Selection: Only released CommunityMech:000148 in the owned batch08 checkout.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 00a4a35e57d262d57b5f1a66fc3b5bdc03ae715b.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000148 | kb/communities/Buchnera_Serratia_Cinara_Cedri_Endosymbiont_Consortium.yaml | maintained | Buchnera-Serratia Cinara cedri Endosymbiont Consortium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000148 | Schema validation passed. |
| validate-strict | passed | True | CommunityMech:000148 | Strict validation passed. |
| validate-terms | passed | True | CommunityMech:000148 | Term validation passed. |
| validate-gtdb | passed | True | CommunityMech:000148 | GTDB syntax/status validation passed. |
| validate-gtdb-domain | passed | True | CommunityMech:000148 | GTDB domain validation passed. |
| validate-history | passed | True | CommunityMech:000148 | History validation passed. |
| normalize-cache-names-check | passed | True | CommunityMech:000148 | Read-only cache-filename preflight passed. |
| validate-references-explained | passed | True | CommunityMech:000148 | Reference validation passed against the pinned cache. |
| audit-network | failed | True | CommunityMech:000148 | Fresh batch08 corpus check reports 57 warnings across 21 of 477 records; the focal network separately reports COMPLETE. |
| check-network-quality | failed | True | CommunityMech:000148 | Fresh batch08 corpus check reports 57 warnings across 21 of 477 records; the focal network separately reports COMPLETE. |
| Primary bibliographic identity | passed | True | CommunityMech:000148 | Exact DOI, PMID and correct PMC body agree; erroneous cache header is excluded. |
| Primary main and critical supplemental verification | passed | True | CommunityMech:000148 | Whole primary main, all five main/five supplementary figures and complete TableS1 were inspected; no raw genomic reanalysis. |
| Source genome and project correspondence | passed | True | CommunityMech:000148 | Both encoded project UIDs and focal chromosome identities verified at metadata scope; RefSeq and source GenBank projects distinguished. |
| Growth-medium linkage | not_applicable | False | CommunityMech:000148 | No focal bench medium is reported; microscopy preparation is not cultivation. |
| Optional structured source adapter | unavailable | False | CommunityMech:000148 | No runnable task adapter or relevant expression-module dataset established; source genomic reconstruction is directly inspected. |

## Scientific And Domain Assessments

### Host-associated BCc/SCc consortium

identity: supported. Targets: CommunityMech:000148.

The record correctly denotes two natural bacterial symbionts of C. cedri; the aphid remains an external host.

### NATURAL origin, SYNTROPHY category and functional roles

scope: supported. Targets: CommunityMech:000148.

Retain inferred nutritional cooperation at the broad category/role scope; no thermodynamic interaction is asserted.

The category and role definitions do not automatically inherit InteractionTypeEnum.SYNTROPHY product-removal language. Both CROSS_FEEDER assignments concern inferred recipient functions in the host-associated reconstruction. Improve claim-specific provenance without requiring a direct uptake assay or obligacy experiment beyond the stated hypothesis.

### ecological_state

evidence: concern. Targets: CommunityMech:000148.

The unqualified STABLE value overstates a source-proposed functional/evolutionary stability hypothesis as ecological equilibrium.

The paper does not report a population-stability time course, equilibrium test or persistence perturbation. The field is optional; omission or explicitly source-qualified representation is appropriate. Do not automatically substitute ENGINEERED or TRANSIENT, and retain NATURAL origin.

### ecological_interactions[0]

graph: supported. Targets: CommunityMech:000148.

Retain computationally inferred BCc→SCc tryptophan-pathway cross-feeding.

The proposed exchanged intermediate is anthranilate, while L-tryptophan is the pathway product already distinguished in notes. No donor-resolved transport, thermodynamic facilitation or export rate is implied.

### ecological_interactions[0].downstream[0]

graph: supported. Targets: CommunityMech:000148.

Retain the explicitly hypothesized contribution of partitioned tryptophan capacity to co-preservation.

This matches the source evolutionary interpretation. It is not a measured causal stability intervention and should not be promoted to such a claim.

### ecological_interactions[1]

graph: supported. Targets: CommunityMech:000148.

Retain source-inferred SCc complementation of lost BCc functions, including riboflavin.

The node already distinguishes genomic capacity from export and fitness effects. Do not generalize to every vitamin or membrane macromolecule, nor remove the hypothesis because direct delivery was not measured.

### ecological_interactions[1].downstream[0]

graph: supported. Targets: CommunityMech:000148.

Retain the hypothesized lost-function complementation → co-preservation contribution.

The source proposes an evolutionary mechanism. Partner necessity, transport route and persistence magnitude remain unresolved as the record states.

### ecological_interactions[2]

graph: supported. Targets: CommunityMech:000148.

Retain inferred co-obligate metabolic complementation with no stronger interaction type imposed.

The narrative is explicitly hypothetical. Comparative host reactions partly derive from A. pisum rather than direct C. cedri assays; the existing discussion correctly preserves that limitation.

### Structured reconstruction and exact source linkage

provenance: concern. Targets: CommunityMech:000148.

Claim-level computational provenance is absent although the primary Methods supplies the reconstruction procedure and source genome identities.

Record the method as annotation/manual pathway reconstruction, not FBA, SMETANA or thermodynamic testing. Source-specific strain/genome metadata can strengthen traceability without declaring current species grounding wrong. Preserve GenBank/RefSeq project distinctions and qualify postulated host contributions.

### Environment, cultivation and resource scope

scope: supported. Targets: CommunityMech:000148.

Phloem nutritional constraints and natural intracellular context are appropriate; no bench growth medium is required.

Collection in Valencia and adult microscopy sampling do not supply host rearing conditions. Saline, fixation buffers and ethanol are preparation reagents. Existing projects are valid; optional canonical accession normalization or exact chromosome linkage should retain the measured versus inferred distinction.

### Cache identity and source-internal inconsistencies

provenance: supported. Targets: CommunityMech:000148.

Fresh direct metadata resolves the cache-header mismatch without invalidating the matching primary body or graph.

The wrong header PMCID is already disclosed in the record. S5 caption/panel letters conflict, and the final Discussion uses BAp in a BCc context; neither is imported as a focal identity change. Selected precursor-dependent pathways differ between prose and Table3 notation; current riboflavin support does not depend on those ambiguities.

### Native validators and authority labels

schema: supported. Targets: CommunityMech:000148.

Eight native checks and all six encoded ontology pairs pass; no mechanical failure substitutes for scientific assessment.

### Native mechanical scores

completeness: supported. Targets: CommunityMech:000148.

Native scores reflect structure and validation, including the current state value; they do not settle its scientific support.

## Findings

### stable-state: Do not promote inferred functional stability to ecological equilibrium

major / open / confirmed; issue key: cm-000148-stable-state.

ecological_state is STABLE, while the source infers functional complementation and evolutionary co-preservation from genomes. The inspected main/SI does not measure ecological equilibrium, and the graph already explicitly disclaims a stability time course or persistence intervention.

### reconstruction-provenance: Record the genomic reconstruction method with the predicted claims

minor / open / confirmed; issue key: cm-000148-reconstruction-provenance.

The interaction evidence is correctly labeled COMPUTATIONAL/PARTIAL, but it lacks structured computational_provenance. Methods identifies annotation-based pathway reconstruction using KAAS/KEGG and manual BRENDA/EcoCyc checks; specific genome and comparator identities can make the inference traceable.

## Recommended Actions And Acceptance Checks

### repair-stable-state

Omit the unsupported optional STABLE value or represent the source-qualified state without asserting measured ecological equilibrium.

- Retain the source-proposed functional/evolutionary stability interpretation in the explicitly hypothetical node and arrows. Do not convert that interpretation into an equilibrium measurement.
- ecological_state is optional in the schema; native completeness scoring is not a requirement to retain unsupported data. Do not automatically replace STABLE with ENGINEERED or TRANSIENT. Preserve NATURAL origin.
- Retain the three qualified nodes and two hypothesized contributions, with no invented transport, persistence or thermodynamic causal claim. Run focused schema, strict, term, reference and history checks after separately authorized curation.

### record-reconstruction-provenance

Attach source-specific genomic reconstruction provenance to predicted interaction evidence and preserve exact source/genome boundaries.

- Record KAAS/KEGG reconstruction and manual BRENDA/EcoCyc pathway checking with an appropriate schema-supported prediction type and specific notes. Do not label the method FBA, SMETANA, thermodynamic testing or measured flux. Do not invent software versions or an SBML model.
- Link the focal SCc chromosome CP002295.1 and its PRJNA32211 identity as relevant, keeping BCc GenBank CP000263.1/PRJNA16372 distinct from RefSeq NC_008513.1/project224116. Do not replace valid source projects with comparator or derived projects.
- Preserve that some host reactions were postulated from A. pisum comparative biology rather than directly measured in C. cedri. Identity-only taxon excerpts should not alone certify functional roles; use the inspected pathway discussion for inferred nutritional cooperation.
- Optional SCc refinement may use verified NCBITaxon568817 and its separately pinned exact-taxid GTDB candidate, but current species138074 is a compatible ancestor. If adopted, update all matching taxon descriptors consistently and revalidate GTDB; do not claim a formal release or new genome analysis.
- Keep the verified focal DOI/PMID/PMC identity separate from the erroneous cache header; any cache correction is separate authorized provenance maintenance. Optional anthranilate annotation must preserve the intermediate-versus-tryptophan-product distinction and the inference qualifier.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | kb/communities/Buchnera_Serratia_Cinara_Cedri_Endosymbiont_Consortium.yaml; Entire record, three nodes and two downstream hypotheses | supports | The maintained record already distinguishes genomic nutritional complementation from measured transport and persistence, but the standalone STABLE value is unqualified. |
| pubmed | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=22102823&amp;retmode=xml; Article-level metadata | supports | Exact PMID22102823, DOI and PMC3213167 identify the focal 2011 paper. |
| epmc | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:22102823%20AND%20SRC:MED&amp;format=json&amp;resultType=core; Article-level metadata | supports | Article identity and complete primary XML agree; the cache header PMCID is not the focal article. |
| crossref | https://api.crossref.org/works/10.1371/journal.pgen.1002357; Article-level metadata | supports | DOI bibliographic identity agrees with the directly inspected primary publication. |
| identity | doi:10.1371/journal.pgen.1002357; Abstract; Introduction; Results: Genome of S. symbiotica SCc strain | supports | BCc and SCc are the two focal bacterial endosymbionts of C. cedri. Other aphids and bacterial strains are comparators, not additional microbial members. |
| tryptophan | doi:10.1371/journal.pgen.1002357; Results: Metabolic pathway reconstruction; Discussion tryptophan paragraph; Figure1; Table2 | supports | BCc trpEG capacity supplies the proposed anthranilate intermediate to SCc trpABCD. The source reconstructs capacity and proposes exchange; it does not trace transport across bacteriocytes. |
| riboflavin | doi:10.1371/journal.pgen.1002357; Abstract; Results: cofactor and vitamin paragraph; Table3 | supports | SCc retains riboflavin capacity absent from BCc. Broader conditional vitamin pathways do not establish export of every product; membrane macromolecule transfer is explicitly considered unlikely. |
| stability | doi:10.1371/journal.pgen.1002357; Abstract/Author Summary and Discussion: evolutionary consortium interpretation | supports | The authors propose functional stability and evolutionary co-preservation from complementary gene repertoires. No population-equilibrium measurement or persistence intervention is reported. |
| methods | doi:10.1371/journal.pgen.1002357; Materials and Methods: Inferred metabolism; Genome sequencing and assembling; Gene annotation and pseudogene prediction | supports | Metabolism was reconstructed using KAAS/KEGG annotation and manual pathway checking against BRENDA and EcoCyc. This is comparative genomic inference, not FBA, exchange simulation or thermodynamic testing. |
| host | doi:10.1371/journal.pgen.1002357; Introduction; Figures2–4 captions; Materials and Methods: Aphid collection and Electron microscopy | supports | Aphids were collected in Valencia. Some host reactions are postulated from A. pisum comparative biology; microscopy preparation is not a cultivation recipe. The nutritional phloem-sap constraint is environmental context. |
| figures | doi:10.1371/journal.pgen.1002357; All five main figures, five supplementary figures and extracted TableS1; source-audit.json | supports | Figure1 is an inferred pathway scheme; Figures2–4 include postulated host reactions. S5 visualizes bacterial/bacteriocyte structure rather than metabolite movement. S1–S4 and TableS1 provide genomic context, not stability experiments. |
| schema | src/communitymech/schema/communitymech.yaml; MicrobialCommunity.ecological_state; EcologicalStateEnum.STABLE; CommunityCategoryEnum.SYNTROPHY; FunctionalRoleEnum; ComputationalProvenance | supports | STABLE denotes ecological equilibrium and ecological_state is optional. Category/role syntrophy definitions are broader than InteractionTypeEnum.SYNTROPHY. ComputationalProvenance represents the method supporting each predicted claim. |
| ontology | ontology-authority.json; Whole bounded receipt | supports | All six encoded ontology pairs across fourteen occurrences match current local labels. Current Serratia species138074 is a compatible ancestor, not wrong identity. |
| semantics | ontology-semantic-notes.json; Whole bounded receipt | supports | Exact enum definitions distinguish optional state, broad nutritional-cooperation roles and the fuller interaction definition; no obligacy criterion is imported. |
| strain | serratia-strain-grounding-candidate.json; Whole bounded receipt | supports | Local OAK verifies SCc candidate NCBITaxon568817 as a strain beneath species138074; source/archive linkage is independently verified. |
| gtdb-candidate | serratia-strain-gtdb-candidate.json; Whole bounded receipt | supports | The exact strain crosswalk supports Serratia_D symbiotica_A with two genomes and majority1.0. This is an optional source-specific refinement, not new genomic analysis or a formally verified numbered GTDB release. |
| intermediate | anthranilate-grounding-candidates.json; Whole bounded receipt | supports | Anthranilate CHEBI16567 is a verified anion and optional intermediate annotation. Current tryptophan correctly denotes the final product. |
| resources | dataset-verification.json; Whole bounded receipt | supports | The two encoded project UIDs identify BCc and SCc. GenBank and RefSeq accessions/projects are kept distinct; the erroneous cache header points to a different paper while the appended primary body is correctly identified. |
| snippets | snippet-audit.json; Whole bounded receipt | supports | All eight excerpts match direct primary XML and the appended cache body; six also match the direct abstract. Editorial cache notes are not evidence. |
| history | provenance-audit.json; Whole bounded receipt | supports | Both sidecars, exact historical decision and linked issue provenance were checked. The earlier three-node/two-arrow qualification is retained. |
| native-target | support-audit.json; Whole bounded receipt | supports | Native metrics and graph completeness are separate from the scientific assessment; the graph is COMPLETE. |
| source-scope | source-audit.json; Whole bounded receipt | supports | Full main, all relevant images and the complete supplementary table were inspected with explicit source-internal discrepancies and no raw-data reanalysis. |
| independent-source | root-independent-source-audit.json; Whole bounded receipt | supports | Root independently assessed the primary scientific claims and agreed final grading and scope. |
| inspection-extension | inspect-extension-provenance.json; Whole bounded receipt | supports | Two child-used GTDB guidance/script inputs were added through a new official inspection; the initial24 hashes were unchanged and the original receipt is preserved. |
| local-search | Maintained local corpus; local-search.json | supports | Ignored-inclusive local searches define resource reuse and provenance boundaries. |
| adapter | Optional structured source adapter; adapter-check.json | supports | No usable task adapter was established; this paper is comparative-genomic reconstruction, not an identified expression-module dataset. |
| check-validate | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src just --no-dotenv validate kb/communities/Buchnera_Serratia_Cinara_Cedri_Endosymbiont_Consortium.yaml; Actual execution 2026-10-21T13:42:57.290623+00:00 to 2026-10-21T13:42:57.881536+00:00 | supports | Schema validation passed. |
| check-validate-strict | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src just --no-dotenv validate-strict kb/communities/Buchnera_Serratia_Cinara_Cedri_Endosymbiont_Consortium.yaml --out /private/tmp/cm-review-session/batch-08/000148/strict-report.tsv; Actual execution 2026-10-21T13:42:57.290756+00:00 to 2026-10-21T13:42:59.042774+00:00 | supports | Strict validation passed. |
| check-validate-terms | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src just --no-dotenv validate-terms kb/communities/Buchnera_Serratia_Cinara_Cedri_Endosymbiont_Consortium.yaml; Actual execution 2026-10-21T13:42:57.290822+00:00 to 2026-10-21T13:42:58.825531+00:00 | supports | Term validation passed. |
| check-validate-gtdb | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src just --no-dotenv validate-gtdb kb/communities/Buchnera_Serratia_Cinara_Cedri_Endosymbiont_Consortium.yaml; Actual execution 2026-10-21T13:42:57.881883+00:00 to 2026-10-21T13:42:57.946607+00:00 | supports | GTDB syntax/status validation passed. |
| check-validate-gtdb-domain | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src just --no-dotenv validate-gtdb-domain kb/communities/Buchnera_Serratia_Cinara_Cedri_Endosymbiont_Consortium.yaml; Actual execution 2026-10-21T13:42:57.946888+00:00 to 2026-10-21T13:42:59.073888+00:00 | supports | GTDB domain validation passed. |
| check-validate-history | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src just --no-dotenv validate-history history/records/Buchnera_Serratia_Cinara_Cedri_Endosymbiont_Consortium; Actual execution 2026-10-21T13:42:58.825804+00:00 to 2026-10-21T13:42:59.660791+00:00 | supports | History validation passed. |
| check-normalize-cache-names-check | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src uv run python scripts/normalize_cache_names.py --check; Actual execution 2026-10-21T13:42:59.661329+00:00 to 2026-10-21T13:42:59.702721+00:00 | supports | Read-only cache-filename preflight passed. |
| check-validate-references-explained | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src just --no-dotenv validate-references-explained kb/communities/Buchnera_Serratia_Cinara_Cedri_Endosymbiont_Consortium.yaml; Actual execution 2026-10-21T13:42:59.702952+00:00 to 2026-10-21T13:43:00.625482+00:00 | supports | Reference validation passed against the pinned cache. |
| check-audit-network | PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv audit-network; Actual execution 2026-10-21T13:06:00.734617+00:00 to 2026-10-21T13:06:11.311177+00:00 | supports | Fresh batch08 corpus check reports 57 warnings across 21 of 477 records; the focal network separately reports COMPLETE. |
| check-check-network-quality | PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv check-network-quality; Actual execution 2026-10-21T13:06:00.741568+00:00 to 2026-10-21T13:06:15.408522+00:00 | supports | Fresh batch08 corpus check reports 57 warnings across 21 of 477 records; the focal network separately reports COMPLETE. |

## Limits And Additional Notes

- No raw genomes, sequence assembly, flux, thermodynamics, statistical or evolutionary analysis was rerun. Public genome/project metadata checks are separate from sequence inspection.
- Full precursor papers were not reread, and historical experiments cited in the Introduction are not presented as new focal perturbation assays.
- S5 microscopy supports structural localization, not metabolite movement or physiological necessity. No figure establishes ecological equilibrium.
- Current SCc species ID is a valid ancestor. Optional strain refinement must update every matching descriptor and recompute GTDB from the verified strain-specific mapping; no culture-collection alias or formal numbered GTDB release is invented.
- Source-internal S5 caption/panel lettering and final Discussion BCc/BAp inconsistencies are preserved, not propagated into record identity.
- Local OAK and GTDB snapshots establish canonical labels and a bounded mapping candidate, not a new phylogenomic analysis.
- No canonical, cache, history, generated or saved-review file changed. The official inspection was explicitly extended from24 to26 inputs; all initial hashes remained unchanged.
- All eight source excerpts match direct full XML and the matching primary cache body; six also match the abstract. Editorial source notes and the erroneous header are excluded.
- Completeness75 and quality100/raw119.6666667 are mechanical metrics. The scientific review covers the declared source scopes without raw genome reconstruction or flux experiments.
- Existing species grounding is not wrong merely because a verified strain-specific candidate now provides optional precision. No new interaction or medium is required to fill optional fields.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T134825Z-buchnera-serratia-cinara-cedri-record
kind: record
repository: CultureBotAI/CommunityMech
title: Buchnera–Serratia Cinara cedri consortium record review
started_at: '2026-10-21T13:42:36.299641Z'
finished_at: '2026-10-21T13:48:25.230034Z'
reviewer:
  identity: codex
  kind: agent
  independence: unknown
  independence_basis: Separate agents assessed primary science, local native/ontology
    checks and source/resource provenance; no person-level independence asserted.
skill: review-yaml-record
completion: completed
verdict: needs_curation
scientific_review: true
summary: The natural two-bacterium identity and three qualified nodes/two hypothesized
  arrows are supported by comparative genomic reconstruction. One major finding concerns
  the unqualified STABLE equilibrium label; one minor concerns missing structured
  reconstruction provenance. Broad nutritional-cooperation roles/category remain bounded,
  and current source identity is verified despite the disclosed cache-header mismatch.
source:
  git_revision: 00a4a35e57d262d57b5f1a66fc3b5bdc03ae715b
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
  - path: history/records/Buchnera_Serratia_Cinara_Cedri_Endosymbiont_Consortium/2026-08-31T075009Z-claude-code-3de0d5.yaml
    sha256: b45bb13552b15b4466db26995710532648b3d764b170745db80acea6094ddeb5
    role: context
  - path: history/records/Buchnera_Serratia_Cinara_Cedri_Endosymbiont_Consortium/2026-10-05T142600Z-codex-0218e1.yaml
    sha256: 19b45ffa34b2539c14020b39909b036b962c3902fd09e1a3841a5e46008a86fa
    role: context
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: kb/communities/Buchnera_Serratia_Cinara_Cedri_Endosymbiont_Consortium.yaml
    sha256: 5a47f483406c1d5cc040a713c08304ac178492cd5c3ea20a815d6251024c95f1
    role: target
  - path: references_cache/doi_10.1371_journal.pgen.1002357.md
    sha256: e70e97e3beb0fabdc708b258ca430f3c80dc64df4a1e8896052258a4e18fd154
    role: context
  - path: reports/causal_graph_review/decisions/20261005-twelve-records-batch8.yaml
    sha256: a03eceb4ca205fdd9092a4f18c0fa4c068e8ec91ee5a62d09da97b87a4f50a25
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
- target_id: CommunityMech:000148
  path: kb/communities/Buchnera_Serratia_Cinara_Cedri_Endosymbiont_Consortium.yaml
  label: Buchnera-Serratia Cinara cedri Endosymbiont Consortium
  kind: maintained
  record_class: MicrobialCommunity
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Buchnera_Serratia_Cinara_Cedri_Endosymbiont_Consortium.yaml
    role: canonical_record
scope:
  description: Whole record, each node and each arrow reviewed against the complete
    primary main, relevant figures/SI, current ontology, source genome metadata and
    provenance.
  selection: Only released CommunityMech:000148 in the owned batch08 checkout.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000148
checks:
- check_id: validate
  name: validate
  status: passed
  required: true
  summary: Schema validation passed.
  target_ids:
  - CommunityMech:000148
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate kb/communities/Buchnera_Serratia_Cinara_Cedri_Endosymbiont_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate
  scope_note: Fresh focused checks and corpus cache-filename preflight; mechanical
    success does not certify source science.
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Strict validation passed.
  target_ids:
  - CommunityMech:000148
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-strict kb/communities/Buchnera_Serratia_Cinara_Cedri_Endosymbiont_Consortium.yaml
    --out /private/tmp/cm-review-session/batch-08/000148/strict-report.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-strict
  scope_note: Fresh focused checks and corpus cache-filename preflight; mechanical
    success does not certify source science.
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Term validation passed.
  target_ids:
  - CommunityMech:000148
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-terms kb/communities/Buchnera_Serratia_Cinara_Cedri_Endosymbiont_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-terms
  scope_note: Fresh focused checks and corpus cache-filename preflight; mechanical
    success does not certify source science.
- check_id: validate-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: GTDB syntax/status validation passed.
  target_ids:
  - CommunityMech:000148
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-gtdb kb/communities/Buchnera_Serratia_Cinara_Cedri_Endosymbiont_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb
  scope_note: Fresh focused checks and corpus cache-filename preflight; mechanical
    success does not certify source science.
- check_id: validate-gtdb-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: GTDB domain validation passed.
  target_ids:
  - CommunityMech:000148
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-gtdb-domain kb/communities/Buchnera_Serratia_Cinara_Cedri_Endosymbiont_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb-domain
  scope_note: Fresh focused checks and corpus cache-filename preflight; mechanical
    success does not certify source science.
- check_id: validate-history
  name: validate-history
  status: passed
  required: true
  summary: History validation passed.
  target_ids:
  - CommunityMech:000148
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-history history/records/Buchnera_Serratia_Cinara_Cedri_Endosymbiont_Consortium
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-history
  scope_note: Fresh focused checks and corpus cache-filename preflight; mechanical
    success does not certify source science.
- check_id: normalize-cache-names-check
  name: normalize-cache-names-check
  status: passed
  required: true
  summary: Read-only cache-filename preflight passed.
  target_ids:
  - CommunityMech:000148
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    uv run python scripts/normalize_cache_names.py --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-normalize-cache-names-check
  scope_note: Fresh focused checks and corpus cache-filename preflight; mechanical
    success does not certify source science.
- check_id: validate-references-explained
  name: validate-references-explained
  status: passed
  required: true
  summary: Reference validation passed against the pinned cache.
  target_ids:
  - CommunityMech:000148
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-references-explained kb/communities/Buchnera_Serratia_Cinara_Cedri_Endosymbiont_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-references-explained
  scope_note: Fresh focused checks and corpus cache-filename preflight; mechanical
    success does not certify source science.
- check_id: audit-network
  name: audit-network
  status: failed
  required: true
  summary: Fresh batch08 corpus check reports 57 warnings across 21 of 477 records;
    the focal network separately reports COMPLETE.
  target_ids:
  - CommunityMech:000148
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv audit-network
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-audit-network
  - native-target
  scope_note: Explicit reuse of fresh batch08 corpus receipts, not a target-specific
    pass. The corpus result is not a focal failure or source-science certification.
- check_id: check-network-quality
  name: check-network-quality
  status: failed
  required: true
  summary: Fresh batch08 corpus check reports 57 warnings across 21 of 477 records;
    the focal network separately reports COMPLETE.
  target_ids:
  - CommunityMech:000148
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv check-network-quality
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-check-network-quality
  - native-target
  scope_note: Explicit reuse of fresh batch08 corpus receipts, not a target-specific
    pass. The corpus result is not a focal failure or source-science certification.
- check_id: source-identity
  name: Primary bibliographic identity
  status: passed
  required: true
  summary: Exact DOI, PMID and correct PMC body agree; erroneous cache header is excluded.
  target_ids:
  - CommunityMech:000148
  evidence_ids:
  - pubmed
  - epmc
  - crossref
  - resources
- check_id: scientific-source
  name: Primary main and critical supplemental verification
  status: passed
  required: true
  summary: Whole primary main, all five main/five supplementary figures and complete
    TableS1 were inspected; no raw genomic reanalysis.
  target_ids:
  - CommunityMech:000148
  evidence_ids:
  - source-scope
  - independent-source
  - figures
- check_id: archive-identity
  name: Source genome and project correspondence
  status: passed
  required: true
  summary: Both encoded project UIDs and focal chromosome identities verified at metadata
    scope; RefSeq and source GenBank projects distinguished.
  target_ids:
  - CommunityMech:000148
  evidence_ids:
  - resources
  - strain
- check_id: cross-mech
  name: Growth-medium linkage
  status: not_applicable
  required: false
  summary: No focal bench medium is reported; microscopy preparation is not cultivation.
  target_ids:
  - CommunityMech:000148
  evidence_ids:
  - host
- check_id: structured-adapter
  name: Optional structured source adapter
  status: unavailable
  required: false
  summary: No runnable task adapter or relevant expression-module dataset established;
    source genomic reconstruction is directly inspected.
  target_ids:
  - CommunityMech:000148
  evidence_ids:
  - adapter
evidence:
- evidence_id: record
  kind: record_content
  reference: kb/communities/Buchnera_Serratia_Cinara_Cedri_Endosymbiont_Consortium.yaml
  locator: Entire record, three nodes and two downstream hypotheses
  summary: The maintained record already distinguishes genomic nutritional complementation
    from measured transport and persistence, but the standalone STABLE value is unqualified.
  support: supports
  accessed_at: '2026-10-21T13:48:25.224862Z'
- evidence_id: pubmed
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=22102823&retmode=xml
  locator: Article-level metadata
  summary: Exact PMID22102823, DOI and PMC3213167 identify the focal 2011 paper.
  support: supports
  accessed_at: '2026-10-21T13:43:12.061149Z'
  snapshot_sha256: 448340f25eba760baff86179ebe124fc84d5ad50ce6b1ec6edfad6515b5ca653
- evidence_id: epmc
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:22102823%20AND%20SRC:MED&format=json&resultType=core
  locator: Article-level metadata
  summary: Article identity and complete primary XML agree; the cache header PMCID
    is not the focal article.
  support: supports
  accessed_at: '2026-10-21T13:43:12.677169Z'
  snapshot_sha256: 17f6e23bd97ec6200933717df9320cd67c4a256e49479a8cdd001f293c1b063c
- evidence_id: crossref
  kind: database
  reference: https://api.crossref.org/works/10.1371/journal.pgen.1002357
  locator: Article-level metadata
  summary: DOI bibliographic identity agrees with the directly inspected primary publication.
  support: supports
  accessed_at: '2026-10-21T13:43:12.222912Z'
  snapshot_sha256: fa65d299ce434a08ac2c4523953c546bffe2cc9cfb20a07049f0d7358bf89dc5
- evidence_id: identity
  kind: primary_source
  reference: doi:10.1371/journal.pgen.1002357
  locator: 'Abstract; Introduction; Results: Genome of S. symbiotica SCc strain'
  summary: BCc and SCc are the two focal bacterial endosymbionts of C. cedri. Other
    aphids and bacterial strains are comparators, not additional microbial members.
  support: supports
  accessed_at: '2026-10-21T13:48:25.225612Z'
  snapshot_sha256: 0274814e553ed688a904820859083e15c199ad6c23f5120e2ac7175557beab70
- evidence_id: tryptophan
  kind: primary_source
  reference: doi:10.1371/journal.pgen.1002357
  locator: 'Results: Metabolic pathway reconstruction; Discussion tryptophan paragraph;
    Figure1; Table2'
  summary: BCc trpEG capacity supplies the proposed anthranilate intermediate to SCc
    trpABCD. The source reconstructs capacity and proposes exchange; it does not trace
    transport across bacteriocytes.
  support: supports
  accessed_at: '2026-10-21T13:48:25.225697Z'
  snapshot_sha256: 0274814e553ed688a904820859083e15c199ad6c23f5120e2ac7175557beab70
  quote: anthranilate provision
- evidence_id: riboflavin
  kind: primary_source
  reference: doi:10.1371/journal.pgen.1002357
  locator: 'Abstract; Results: cofactor and vitamin paragraph; Table3'
  summary: SCc retains riboflavin capacity absent from BCc. Broader conditional vitamin
    pathways do not establish export of every product; membrane macromolecule transfer
    is explicitly considered unlikely.
  support: supports
  accessed_at: '2026-10-21T13:48:25.225776Z'
  snapshot_sha256: 0274814e553ed688a904820859083e15c199ad6c23f5120e2ac7175557beab70
- evidence_id: stability
  kind: primary_source
  reference: doi:10.1371/journal.pgen.1002357
  locator: 'Abstract/Author Summary and Discussion: evolutionary consortium interpretation'
  summary: The authors propose functional stability and evolutionary co-preservation
    from complementary gene repertoires. No population-equilibrium measurement or
    persistence intervention is reported.
  support: supports
  accessed_at: '2026-10-21T13:48:25.225848Z'
  snapshot_sha256: 0274814e553ed688a904820859083e15c199ad6c23f5120e2ac7175557beab70
  quote: functional stability
- evidence_id: methods
  kind: primary_source
  reference: doi:10.1371/journal.pgen.1002357
  locator: 'Materials and Methods: Inferred metabolism; Genome sequencing and assembling;
    Gene annotation and pseudogene prediction'
  summary: Metabolism was reconstructed using KAAS/KEGG annotation and manual pathway
    checking against BRENDA and EcoCyc. This is comparative genomic inference, not
    FBA, exchange simulation or thermodynamic testing.
  support: supports
  accessed_at: '2026-10-21T13:48:25.225921Z'
  snapshot_sha256: 0274814e553ed688a904820859083e15c199ad6c23f5120e2ac7175557beab70
  quote: each pathway was examined
- evidence_id: host
  kind: primary_source
  reference: doi:10.1371/journal.pgen.1002357
  locator: 'Introduction; Figures2–4 captions; Materials and Methods: Aphid collection
    and Electron microscopy'
  summary: Aphids were collected in Valencia. Some host reactions are postulated from
    A. pisum comparative biology; microscopy preparation is not a cultivation recipe.
    The nutritional phloem-sap constraint is environmental context.
  support: supports
  accessed_at: '2026-10-21T13:48:25.225991Z'
  snapshot_sha256: 0274814e553ed688a904820859083e15c199ad6c23f5120e2ac7175557beab70
- evidence_id: figures
  kind: primary_source
  reference: doi:10.1371/journal.pgen.1002357
  locator: All five main figures, five supplementary figures and extracted TableS1;
    source-audit.json
  summary: Figure1 is an inferred pathway scheme; Figures2–4 include postulated host
    reactions. S5 visualizes bacterial/bacteriocyte structure rather than metabolite
    movement. S1–S4 and TableS1 provide genomic context, not stability experiments.
  support: supports
  accessed_at: '2026-10-21T13:48:25.226017Z'
  snapshot_sha256: 87fceccf7311d38984120a72b7a168516f9ade3575f06ddc054c2fa09be191df
- evidence_id: schema
  kind: authority
  reference: src/communitymech/schema/communitymech.yaml
  locator: MicrobialCommunity.ecological_state; EcologicalStateEnum.STABLE; CommunityCategoryEnum.SYNTROPHY;
    FunctionalRoleEnum; ComputationalProvenance
  summary: STABLE denotes ecological equilibrium and ecological_state is optional.
    Category/role syntrophy definitions are broader than InteractionTypeEnum.SYNTROPHY.
    ComputationalProvenance represents the method supporting each predicted claim.
  support: supports
  accessed_at: '2026-10-21T13:48:25.226074Z'
  snapshot_sha256: c41630d09def826256ddb6678c1ce31fa71e3b074219bb9d217d98035a5324ee
- evidence_id: ontology
  kind: authority
  reference: ontology-authority.json
  locator: Whole bounded receipt
  summary: All six encoded ontology pairs across fourteen occurrences match current
    local labels. Current Serratia species138074 is a compatible ancestor, not wrong
    identity.
  support: supports
  accessed_at: '2026-10-21T13:48:25.226227Z'
  snapshot_sha256: 541b07d001019f94dd34cee936e13d0986a8ec6b693afbbfebd4da996ab50d3a
- evidence_id: semantics
  kind: authority
  reference: ontology-semantic-notes.json
  locator: Whole bounded receipt
  summary: Exact enum definitions distinguish optional state, broad nutritional-cooperation
    roles and the fuller interaction definition; no obligacy criterion is imported.
  support: supports
  accessed_at: '2026-10-21T13:48:25.226372Z'
  snapshot_sha256: 0e2fa54770d562d55e947e8b5f3a553d1d14e3594a367a3b7a5479978f77d415
- evidence_id: strain
  kind: authority
  reference: serratia-strain-grounding-candidate.json
  locator: Whole bounded receipt
  summary: Local OAK verifies SCc candidate NCBITaxon568817 as a strain beneath species138074;
    source/archive linkage is independently verified.
  support: supports
  accessed_at: '2026-10-21T13:48:25.226500Z'
  snapshot_sha256: 13802912f51e5ef301d8da8de9bc06763f85ec95ff1568ec55ecd7550d9725f5
- evidence_id: gtdb-candidate
  kind: authority
  reference: serratia-strain-gtdb-candidate.json
  locator: Whole bounded receipt
  summary: The exact strain crosswalk supports Serratia_D symbiotica_A with two genomes
    and majority1.0. This is an optional source-specific refinement, not new genomic
    analysis or a formally verified numbered GTDB release.
  support: supports
  accessed_at: '2026-10-21T13:48:25.226626Z'
  snapshot_sha256: 56b4afa0c9f7b0fb8bb6ca3e1d7cf6116234e4f4e6ba4257dc8dd9be8b89b4d3
- evidence_id: intermediate
  kind: authority
  reference: anthranilate-grounding-candidates.json
  locator: Whole bounded receipt
  summary: Anthranilate CHEBI16567 is a verified anion and optional intermediate annotation.
    Current tryptophan correctly denotes the final product.
  support: supports
  accessed_at: '2026-10-21T13:48:25.226886Z'
  snapshot_sha256: fa2a293b5c07cb234c07a15f1787f3afb6438bc41d8647ffb2d724e34b8f9c64
- evidence_id: resources
  kind: database
  reference: dataset-verification.json
  locator: Whole bounded receipt
  summary: The two encoded project UIDs identify BCc and SCc. GenBank and RefSeq accessions/projects
    are kept distinct; the erroneous cache header points to a different paper while
    the appended primary body is correctly identified.
  support: supports
  accessed_at: '2026-10-21T13:48:25.226923Z'
  snapshot_sha256: 3b6ca45a81bb1f5247aa8fce1b019873523a4f617da72cd5e39f7c9efb7afe9e
- evidence_id: snippets
  kind: validation
  reference: snippet-audit.json
  locator: Whole bounded receipt
  summary: All eight excerpts match direct primary XML and the appended cache body;
    six also match the direct abstract. Editorial cache notes are not evidence.
  support: supports
  accessed_at: '2026-10-21T13:48:25.227048Z'
  snapshot_sha256: dc1102aadb97b18d5543197f5cd167ad3f9d672b482ec08e03ec77e20c2e6ee5
- evidence_id: history
  kind: record_content
  reference: provenance-audit.json
  locator: Whole bounded receipt
  summary: Both sidecars, exact historical decision and linked issue provenance were
    checked. The earlier three-node/two-arrow qualification is retained.
  support: supports
  accessed_at: '2026-10-21T13:48:25.227195Z'
  snapshot_sha256: dc5595a313e550f9458bc05ff55943b3585bf8dca63b14bd9daa2c285581a472
- evidence_id: native-target
  kind: validation
  reference: support-audit.json
  locator: Whole bounded receipt
  summary: Native metrics and graph completeness are separate from the scientific
    assessment; the graph is COMPLETE.
  support: supports
  accessed_at: '2026-10-21T13:48:25.227229Z'
  snapshot_sha256: 4d1ab4a78a744b4b4ce1481d4548143a2160ac6be58a7efe617d7b372283f5a2
- evidence_id: source-scope
  kind: validation
  reference: source-audit.json
  locator: Whole bounded receipt
  summary: Full main, all relevant images and the complete supplementary table were
    inspected with explicit source-internal discrepancies and no raw-data reanalysis.
  support: supports
  accessed_at: '2026-10-21T13:48:25.227257Z'
  snapshot_sha256: 87fceccf7311d38984120a72b7a168516f9ade3575f06ddc054c2fa09be191df
- evidence_id: independent-source
  kind: validation
  reference: root-independent-source-audit.json
  locator: Whole bounded receipt
  summary: Root independently assessed the primary scientific claims and agreed final
    grading and scope.
  support: supports
  accessed_at: '2026-10-21T13:48:25.227287Z'
  snapshot_sha256: ff8f245f96400f10673338aec8ed690db92bec7004ec647f61557cb2c73e53f8
- evidence_id: inspection-extension
  kind: validation
  reference: inspect-extension-provenance.json
  locator: Whole bounded receipt
  summary: Two child-used GTDB guidance/script inputs were added through a new official
    inspection; the initial24 hashes were unchanged and the original receipt is preserved.
  support: supports
  accessed_at: '2026-10-21T13:48:25.227414Z'
  snapshot_sha256: 441e48a9321d7680fc2564f365f1e3779b30dad9ec161f6156e7b8d2bb8383cf
- evidence_id: local-search
  kind: search
  reference: Maintained local corpus
  locator: local-search.json
  summary: Ignored-inclusive local searches define resource reuse and provenance boundaries.
  support: supports
  accessed_at: '2026-10-21T13:48:25.227531Z'
  snapshot_sha256: 41aadf90c22047dfd97d7e3c785b54274a743d3d60a637665d891fccf4417ea7
  search_scope: Maintained record, taxon, cache and mapping roots including ignored
    files, as recorded in the receipt.
- evidence_id: adapter
  kind: search
  reference: Optional structured source adapter
  locator: adapter-check.json
  summary: No usable task adapter was established; this paper is comparative-genomic
    reconstruction, not an identified expression-module dataset.
  support: supports
  accessed_at: '2026-10-21T13:48:25.227677Z'
  snapshot_sha256: 6de47166f261ff1b35d8b62c9ae418129f990c26313be08db84a13da3637d9cc
  search_scope: Fresh task runtime and ignored-inclusive module/file discovery; no
    global absence claim.
- evidence_id: check-validate
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate kb/communities/Buchnera_Serratia_Cinara_Cedri_Endosymbiont_Consortium.yaml
  locator: Actual execution 2026-10-21T13:42:57.290623+00:00 to 2026-10-21T13:42:57.881536+00:00
  summary: Schema validation passed.
  support: supports
  accessed_at: '2026-10-21T13:42:57.881536Z'
  snapshot_sha256: 52d6eba93a616c16da29191a6d0f0f616e675e8ddc6cf5335d472bf613466c0f
- evidence_id: check-validate-strict
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-strict kb/communities/Buchnera_Serratia_Cinara_Cedri_Endosymbiont_Consortium.yaml
    --out /private/tmp/cm-review-session/batch-08/000148/strict-report.tsv
  locator: Actual execution 2026-10-21T13:42:57.290756+00:00 to 2026-10-21T13:42:59.042774+00:00
  summary: Strict validation passed.
  support: supports
  accessed_at: '2026-10-21T13:42:59.042774Z'
  snapshot_sha256: 6e415d502b06fc5eca2fb171fba650f8b2b3d9074ee4bc4fbd10fc0c917f59c3
- evidence_id: check-validate-terms
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-terms kb/communities/Buchnera_Serratia_Cinara_Cedri_Endosymbiont_Consortium.yaml
  locator: Actual execution 2026-10-21T13:42:57.290822+00:00 to 2026-10-21T13:42:58.825531+00:00
  summary: Term validation passed.
  support: supports
  accessed_at: '2026-10-21T13:42:58.825531Z'
  snapshot_sha256: 7257606c060f588105b4ec3aa0f11e0b7a139c3d709e054fc787130bc7ab57a9
- evidence_id: check-validate-gtdb
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-gtdb kb/communities/Buchnera_Serratia_Cinara_Cedri_Endosymbiont_Consortium.yaml
  locator: Actual execution 2026-10-21T13:42:57.881883+00:00 to 2026-10-21T13:42:57.946607+00:00
  summary: GTDB syntax/status validation passed.
  support: supports
  accessed_at: '2026-10-21T13:42:57.946607Z'
  snapshot_sha256: 1410c5c3ace352d6d482920fe7631d79a33ba0a781ac5317aca5710a912cec8c
- evidence_id: check-validate-gtdb-domain
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-gtdb-domain kb/communities/Buchnera_Serratia_Cinara_Cedri_Endosymbiont_Consortium.yaml
  locator: Actual execution 2026-10-21T13:42:57.946888+00:00 to 2026-10-21T13:42:59.073888+00:00
  summary: GTDB domain validation passed.
  support: supports
  accessed_at: '2026-10-21T13:42:59.073888Z'
  snapshot_sha256: 94fdaaf7556b1cec02fd9d586ef141061366f1e5795b471e13c56e02cd7a2813
- evidence_id: check-validate-history
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-history history/records/Buchnera_Serratia_Cinara_Cedri_Endosymbiont_Consortium
  locator: Actual execution 2026-10-21T13:42:58.825804+00:00 to 2026-10-21T13:42:59.660791+00:00
  summary: History validation passed.
  support: supports
  accessed_at: '2026-10-21T13:42:59.660791Z'
  snapshot_sha256: 7a64f5e60e1dc35b1b193560216aa42020e7fbf567919cd3d5595864a16da588
- evidence_id: check-normalize-cache-names-check
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    uv run python scripts/normalize_cache_names.py --check
  locator: Actual execution 2026-10-21T13:42:59.661329+00:00 to 2026-10-21T13:42:59.702721+00:00
  summary: Read-only cache-filename preflight passed.
  support: supports
  accessed_at: '2026-10-21T13:42:59.702721Z'
  snapshot_sha256: a4713a530919c3ba87ea1646e0fa35c2d2e411b2a39ba2cc3eaa0e9b351aab8e
- evidence_id: check-validate-references-explained
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-references-explained kb/communities/Buchnera_Serratia_Cinara_Cedri_Endosymbiont_Consortium.yaml
  locator: Actual execution 2026-10-21T13:42:59.702952+00:00 to 2026-10-21T13:43:00.625482+00:00
  summary: Reference validation passed against the pinned cache.
  support: supports
  accessed_at: '2026-10-21T13:43:00.625482Z'
  snapshot_sha256: 000e1b4464bdfebfda4bb2f7f7f4863300547c93dd0ba808527109a70b20e0ed
- evidence_id: check-audit-network
  kind: validation
  reference: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv audit-network
  locator: Actual execution 2026-10-21T13:06:00.734617+00:00 to 2026-10-21T13:06:11.311177+00:00
  summary: Fresh batch08 corpus check reports 57 warnings across 21 of 477 records;
    the focal network separately reports COMPLETE.
  support: supports
  accessed_at: '2026-10-21T13:06:11.311177Z'
  snapshot_sha256: 2d17097db768619fa7fea156f7c37781fa9cd463a6abdce6f529112518848cf0
- evidence_id: check-check-network-quality
  kind: validation
  reference: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv check-network-quality
  locator: Actual execution 2026-10-21T13:06:00.741568+00:00 to 2026-10-21T13:06:15.408522+00:00
  summary: Fresh batch08 corpus check reports 57 warnings across 21 of 477 records;
    the focal network separately reports COMPLETE.
  support: supports
  accessed_at: '2026-10-21T13:06:15.408522Z'
  snapshot_sha256: 1332cfd7980ec54d517d625aff43fa6328c1a19fd405a7aef071f78af9774f3f
assessments:
- assessment_id: identity
  area: identity
  topic: Host-associated BCc/SCc consortium
  outcome: supported
  summary: The record correctly denotes two natural bacterial symbionts of C. cedri;
    the aphid remains an external host.
  target_ids:
  - CommunityMech:000148
  evidence_ids:
  - identity
  - ontology
  - host
  dimensions:
  - name: community_scope
    value: BCc and SCc within Cinara cedri
    definition: Do not add host or comparator organisms to microbial membership.
    evidence_ids:
    - identity
  - name: taxon_rank
    value: BCc strain; SCc species with explicit source designation
    definition: The SCc strain authority is available as optional more precise grounding.
    evidence_ids:
    - ontology
    - strain
    - resources
  - name: grounding_status
    value: BCc GROUNDED; SCc AMBIGUOUS at species level
    definition: Species-level ambiguity is not evidence of a wrong organism.
    evidence_ids:
    - ontology
    - gtdb-candidate
  - name: environment
    value: Animal-associated intracellular symbiosis
    definition: Separate bacteriocytes create an unresolved transport boundary.
    evidence_ids:
    - host
    - figures
  - name: medium
    value: No focal culture recipe reported
    definition: Collection and microscopy reagents do not define growth conditions.
    evidence_ids:
    - host
  - name: evidence_tier
    value: Comparative genome reconstruction plus microscopy
    definition: Pathway capacity and proposed transfer are distinct from measured
      flux.
    evidence_ids:
    - methods
    - figures
- assessment_id: category-roles
  area: scope
  topic: NATURAL origin, SYNTROPHY category and functional roles
  outcome: supported
  summary: Retain inferred nutritional cooperation at the broad category/role scope;
    no thermodynamic interaction is asserted.
  target_ids:
  - CommunityMech:000148
  evidence_ids:
  - schema
  - tryptophan
  - riboflavin
  - semantics
  details: The category and role definitions do not automatically inherit InteractionTypeEnum.SYNTROPHY
    product-removal language. Both CROSS_FEEDER assignments concern inferred recipient
    functions in the host-associated reconstruction. Improve claim-specific provenance
    without requiring a direct uptake assay or obligacy experiment beyond the stated
    hypothesis.
- assessment_id: state
  area: evidence
  topic: ecological_state
  outcome: concern
  summary: The unqualified STABLE value overstates a source-proposed functional/evolutionary
    stability hypothesis as ecological equilibrium.
  target_ids:
  - CommunityMech:000148
  evidence_ids:
  - stability
  - schema
  - record
  details: The paper does not report a population-stability time course, equilibrium
    test or persistence perturbation. The field is optional; omission or explicitly
    source-qualified representation is appropriate. Do not automatically substitute
    ENGINEERED or TRANSIENT, and retain NATURAL origin.
- assessment_id: node-0
  area: graph
  topic: ecological_interactions[0]
  outcome: supported
  summary: Retain computationally inferred BCc→SCc tryptophan-pathway cross-feeding.
  target_ids:
  - CommunityMech:000148
  evidence_ids:
  - tryptophan
  - figures
  - intermediate
  details: The proposed exchanged intermediate is anthranilate, while L-tryptophan
    is the pathway product already distinguished in notes. No donor-resolved transport,
    thermodynamic facilitation or export rate is implied.
- assessment_id: arrow-0
  area: graph
  topic: ecological_interactions[0].downstream[0]
  outcome: supported
  summary: Retain the explicitly hypothesized contribution of partitioned tryptophan
    capacity to co-preservation.
  target_ids:
  - CommunityMech:000148
  evidence_ids:
  - tryptophan
  - stability
  details: This matches the source evolutionary interpretation. It is not a measured
    causal stability intervention and should not be promoted to such a claim.
- assessment_id: node-1
  area: graph
  topic: ecological_interactions[1]
  outcome: supported
  summary: Retain source-inferred SCc complementation of lost BCc functions, including
    riboflavin.
  target_ids:
  - CommunityMech:000148
  evidence_ids:
  - riboflavin
  - methods
  details: The node already distinguishes genomic capacity from export and fitness
    effects. Do not generalize to every vitamin or membrane macromolecule, nor remove
    the hypothesis because direct delivery was not measured.
- assessment_id: arrow-1
  area: graph
  topic: ecological_interactions[1].downstream[0]
  outcome: supported
  summary: Retain the hypothesized lost-function complementation → co-preservation
    contribution.
  target_ids:
  - CommunityMech:000148
  evidence_ids:
  - riboflavin
  - stability
  details: The source proposes an evolutionary mechanism. Partner necessity, transport
    route and persistence magnitude remain unresolved as the record states.
- assessment_id: node-2
  area: graph
  topic: ecological_interactions[2]
  outcome: supported
  summary: Retain inferred co-obligate metabolic complementation with no stronger
    interaction type imposed.
  target_ids:
  - CommunityMech:000148
  evidence_ids:
  - stability
  - identity
  - host
  details: The narrative is explicitly hypothetical. Comparative host reactions partly
    derive from A. pisum rather than direct C. cedri assays; the existing discussion
    correctly preserves that limitation.
- assessment_id: provenance
  area: provenance
  topic: Structured reconstruction and exact source linkage
  outcome: concern
  summary: Claim-level computational provenance is absent although the primary Methods
    supplies the reconstruction procedure and source genome identities.
  target_ids:
  - CommunityMech:000148
  evidence_ids:
  - methods
  - resources
  - strain
  - gtdb-candidate
  - schema
  details: Record the method as annotation/manual pathway reconstruction, not FBA,
    SMETANA or thermodynamic testing. Source-specific strain/genome metadata can strengthen
    traceability without declaring current species grounding wrong. Preserve GenBank/RefSeq
    project distinctions and qualify postulated host contributions.
- assessment_id: context
  area: scope
  topic: Environment, cultivation and resource scope
  outcome: supported
  summary: Phloem nutritional constraints and natural intracellular context are appropriate;
    no bench growth medium is required.
  target_ids:
  - CommunityMech:000148
  evidence_ids:
  - host
  - resources
  details: Collection in Valencia and adult microscopy sampling do not supply host
    rearing conditions. Saline, fixation buffers and ethanol are preparation reagents.
    Existing projects are valid; optional canonical accession normalization or exact
    chromosome linkage should retain the measured versus inferred distinction.
- assessment_id: source-conflicts
  area: provenance
  topic: Cache identity and source-internal inconsistencies
  outcome: supported
  summary: Fresh direct metadata resolves the cache-header mismatch without invalidating
    the matching primary body or graph.
  target_ids:
  - CommunityMech:000148
  evidence_ids:
  - resources
  - source-scope
  - snippets
  details: The wrong header PMCID is already disclosed in the record. S5 caption/panel
    letters conflict, and the final Discussion uses BAp in a BCc context; neither
    is imported as a focal identity change. Selected precursor-dependent pathways
    differ between prose and Table3 notation; current riboflavin support does not
    depend on those ambiguities.
- assessment_id: validation
  area: schema
  topic: Native validators and authority labels
  outcome: supported
  summary: Eight native checks and all six encoded ontology pairs pass; no mechanical
    failure substitutes for scientific assessment.
  target_ids:
  - CommunityMech:000148
  evidence_ids:
  - check-validate
  - check-validate-references-explained
  - ontology
  - native-target
- assessment_id: metrics
  area: completeness
  topic: Native mechanical scores
  outcome: supported
  summary: Native scores reflect structure and validation, including the current state
    value; they do not settle its scientific support.
  target_ids:
  - CommunityMech:000148
  evidence_ids:
  - native-target
  metrics:
  - name: completeness
    value: 75
    unit: points
    minimum: 0
    maximum: 100
    definition: 50 required-field/taxon-role component +5 environment +10 interaction
      count +5 datasets +5 node metabolites. The completeness rubric does not make
      ecological_state schema-required.
  - name: validation_quality
    value: 100
    unit: points
    minimum: 0
    maximum: 100
    definition: clamp(100−50P1−10P2−2P3+20min(mean node evidence/2,1)+15 if COMPLETE,0,100).
      P1=0/P2=1/P3=1/P4=0; five node evidence/three nodes gives16.6666667; COMPLETE
      adds15; raw119.6666667, capped100.
  - name: P1
    value: 0
    unit: findings
    definition: Native severity count.
  - name: P2
    value: 1
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
- finding_id: stable-state
  issue_key: cm-000148-stable-state
  category: evidence
  severity: major
  native_severity: P2
  normalization_reason: 'P2: unqualified ecological-equilibrium assertion exceeds
    the source evolutionary hypothesis, despite the appropriately bounded graph.'
  rule_id: review-checklist.claim-specific-evidence
  status: open
  certainty: confirmed
  title: Do not promote inferred functional stability to ecological equilibrium
  description: ecological_state is STABLE, while the source infers functional complementation
    and evolutionary co-preservation from genomes. The inspected main/SI does not
    measure ecological equilibrium, and the graph already explicitly disclaims a stability
    time course or persistence intervention.
  target_ids:
  - CommunityMech:000148
  field_paths:
  - ecological_state
  evidence_ids:
  - record
  - stability
  - schema
  - source-scope
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Buchnera_Serratia_Cinara_Cedri_Endosymbiont_Consortium.yaml
    role: canonical_record
- finding_id: reconstruction-provenance
  issue_key: cm-000148-reconstruction-provenance
  category: provenance
  severity: minor
  native_severity: P3
  normalization_reason: 'P3: source-supported method and genome provenance are recoverable
    without changing the qualified biological interpretation or current compatible
    taxon identities.'
  rule_id: review-checklist.computational-provenance
  status: open
  certainty: confirmed
  title: Record the genomic reconstruction method with the predicted claims
  description: The interaction evidence is correctly labeled COMPUTATIONAL/PARTIAL,
    but it lacks structured computational_provenance. Methods identifies annotation-based
    pathway reconstruction using KAAS/KEGG and manual BRENDA/EcoCyc checks; specific
    genome and comparator identities can make the inference traceable.
  target_ids:
  - CommunityMech:000148
  field_paths:
  - ecological_interactions[0].evidence[0].computational_provenance
  - ecological_interactions[1].evidence[0].computational_provenance
  - ecological_interactions[1].evidence[1].computational_provenance
  - ecological_interactions[2].evidence[0].computational_provenance
  - ecological_interactions[2].evidence[1].computational_provenance
  evidence_ids:
  - methods
  - resources
  - schema
  - host
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Buchnera_Serratia_Cinara_Cedri_Endosymbiont_Consortium.yaml
    role: canonical_record
actions:
- action_id: repair-stable-state
  description: Omit the unsupported optional STABLE value or represent the source-qualified
    state without asserting measured ecological equilibrium.
  finding_ids:
  - stable-state
  target_ids:
  - CommunityMech:000148
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Buchnera_Serratia_Cinara_Cedri_Endosymbiont_Consortium.yaml
    role: canonical_record
  acceptance_checks:
  - Retain the source-proposed functional/evolutionary stability interpretation in
    the explicitly hypothetical node and arrows. Do not convert that interpretation
    into an equilibrium measurement.
  - ecological_state is optional in the schema; native completeness scoring is not
    a requirement to retain unsupported data. Do not automatically replace STABLE
    with ENGINEERED or TRANSIENT. Preserve NATURAL origin.
  - Retain the three qualified nodes and two hypothesized contributions, with no invented
    transport, persistence or thermodynamic causal claim. Run focused schema, strict,
    term, reference and history checks after separately authorized curation.
- action_id: record-reconstruction-provenance
  description: Attach source-specific genomic reconstruction provenance to predicted
    interaction evidence and preserve exact source/genome boundaries.
  finding_ids:
  - reconstruction-provenance
  target_ids:
  - CommunityMech:000148
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Buchnera_Serratia_Cinara_Cedri_Endosymbiont_Consortium.yaml
    role: canonical_record
  acceptance_checks:
  - Record KAAS/KEGG reconstruction and manual BRENDA/EcoCyc pathway checking with
    an appropriate schema-supported prediction type and specific notes. Do not label
    the method FBA, SMETANA, thermodynamic testing or measured flux. Do not invent
    software versions or an SBML model.
  - Link the focal SCc chromosome CP002295.1 and its PRJNA32211 identity as relevant,
    keeping BCc GenBank CP000263.1/PRJNA16372 distinct from RefSeq NC_008513.1/project224116.
    Do not replace valid source projects with comparator or derived projects.
  - Preserve that some host reactions were postulated from A. pisum comparative biology
    rather than directly measured in C. cedri. Identity-only taxon excerpts should
    not alone certify functional roles; use the inspected pathway discussion for inferred
    nutritional cooperation.
  - Optional SCc refinement may use verified NCBITaxon568817 and its separately pinned
    exact-taxid GTDB candidate, but current species138074 is a compatible ancestor.
    If adopted, update all matching taxon descriptors consistently and revalidate
    GTDB; do not claim a formal release or new genome analysis.
  - Keep the verified focal DOI/PMID/PMC identity separate from the erroneous cache
    header; any cache correction is separate authorized provenance maintenance. Optional
    anthranilate annotation must preserve the intermediate-versus-tryptophan-product
    distinction and the inference qualifier.
limitations:
- No raw genomes, sequence assembly, flux, thermodynamics, statistical or evolutionary
  analysis was rerun. Public genome/project metadata checks are separate from sequence
  inspection.
- Full precursor papers were not reread, and historical experiments cited in the Introduction
  are not presented as new focal perturbation assays.
- S5 microscopy supports structural localization, not metabolite movement or physiological
  necessity. No figure establishes ecological equilibrium.
- Current SCc species ID is a valid ancestor. Optional strain refinement must update
  every matching descriptor and recompute GTDB from the verified strain-specific mapping;
  no culture-collection alias or formal numbered GTDB release is invented.
- Source-internal S5 caption/panel lettering and final Discussion BCc/BAp inconsistencies
  are preserved, not propagated into record identity.
- Local OAK and GTDB snapshots establish canonical labels and a bounded mapping candidate,
  not a new phylogenomic analysis.
notes:
- No canonical, cache, history, generated or saved-review file changed. The official
  inspection was explicitly extended from24 to26 inputs; all initial hashes remained
  unchanged.
- All eight source excerpts match direct full XML and the matching primary cache body;
  six also match the abstract. Editorial source notes and the erroneous header are
  excluded.
- Completeness75 and quality100/raw119.6666667 are mechanical metrics. The scientific
  review covers the declared source scopes without raw genome reconstruction or flux
  experiments.
- Existing species grounding is not wrong merely because a verified strain-specific
  candidate now provides optional precision. No new interaction or medium is required
  to fill optional fields.
tags:
- record-review
- aphid-symbiosis
- comparative-genomics
- cross-feeding
- batch-08
```
