# PR 2034: current-source successor for the KRP BioModels isolate

- Review: 20261105T202026Z-pr2034-kefir-rothia-successor
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-11-05T20:11:18.492562Z
- Finished UTC: 2026-11-05T20:20:26.977078Z
- Reviewer: codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The three predecessor findings remain open. Current evidence also identifies an unsupported KRP cross-feeder role, an unlinked GAM formulation and a publication-only dataset entry: 3 P2 and 3 P3. Model identity, the qualified computational node, RARE and GAM isolation conditions are supported. All focused checks passed; two executed corpus gates retain unrelated warning failures.

## Scope And Provenance

Whole current isolate record and all predecessor findings, with current primary model/genome retrieval, paper/source and ontology reassessment.

Selection: Explicit PR 2034 canary refresh of the stale CommunityMech:000321 review only.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 85dd2c055582c12509c38b011e5034ab2774293f.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000321 | data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml | maintained | BioModels MODEL2204300002 Kefir Rothia Model |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000321 | Focused current-record check passed. |
| validate-strict | passed | True | CommunityMech:000321 | Focused current-record check passed. |
| validate-terms | passed | True | CommunityMech:000321 | Focused current-record check passed. |
| validate-references-explained | passed | True | CommunityMech:000321 | Focused current-record check passed; the reference summary counts reported issues, not checked excerpts. |
| validate-gtdb | passed | True | CommunityMech:000321 | Focused current-record check passed. |
| validate-gtdb-domain | passed | True | CommunityMech:000321 | Focused current-record check passed. |
| validate-history | passed | True | CommunityMech:000321 | Focused current-record check passed. |
| audit-network | failed | True | CommunityMech:000321 | Corpus warnings retain a failed required gate; they are not attributed to this target. |
| check-network-quality | failed | True | CommunityMech:000321 | Corpus warnings retain a failed required gate; they are not attributed to this target. |

## Scientific And Domain Assessments

### KRP computational model and source strain

identity: supported. Targets: CommunityMech:000321.

Current primary metadata and both model artifacts identify KRP. This is one isolate-derived computational model, not the whole kefir community and not proof that the isolate was genetically engineered.

### New role and abundance annotations

scope: concern. Targets: CommunityMech:000321.

RARE is supported in the source grain context. CROSS_FEEDER still needs KRP-specific attribution: generic expected uptake/secretion and whole-community cooperation do not identify KRP consumption of another taxon's products. Preserve computational potential without inventing a replacement ecological role.

### Existing computational graph

graph: supported. Targets: CommunityMech:000321.

Preserve the sole qualified node, amino-acid metabolite/process context, genus participant and absent edges. The source models amino-acid uptake and secretion; neither transport terms nor exchange reactions demonstrate donor-to-KRP transfer. The current graph already keeps that boundary.

### Isolation setting and represented kefir environment

grounding: concern. Targets: CommunityMech:000321.

Laboratory isolation is defensible. The dairy building term is not supported as the modeled kefir material/environment, even though its label validates.

### Genome and model versions

provenance: concern. Targets: CommunityMech:000321.

The published KRP/NDFM and deposited Olga/NDFM01 relationship remains unreconciled. Model identity is positive; the shared 156 key partly bridges names. Assembly size/contig differences and current QC flags require explicit version/filtering provenance, not an automatic taxon replacement or blanket rejection of modeled predictions.

### KRP isolation and exact GAM linkage

completeness: concern. Targets: CommunityMech:000321.

Retain GAM agar, 30 degrees C, two days and ground-kefir serial-dilution isolation. Source does not establish an exact GAM formulation/catalogue match or an isolate-specific atmosphere; neither recipe nor model exchange constraints should be invented.

### Claim-local citation and resource representation

evidence: concern. Targets: CommunityMech:000321.

The model and WGS accessions are positive resources. Design/resource title snippets do not establish their specific claims, despite independently available Methods/deposit support. The paper DOI is a publication, not a separate deposited dataset.

### Current taxonomic semantic checks

grounding: supported. Targets: CommunityMech:000321.

Current labels and genus rank are correct; GTDB lineage and domain gates pass. These checks do not regenerate the historical 1,075-genome mapping aggregate or establish KRP/Olga strain equivalence. No automatic species-level replacement is proposed.

### Native metrics and executed gates

completeness: concern. Targets: CommunityMech:000321.

All focused gates pass. Both required corpus gates executed and retain unrelated warning failures. Native completeness counts field presence, including the role under review; neither metric certifies scientific correctness.

## Findings

### environment: Modeled environment still denotes a dairy building

major / open / confirmed; issue key: cm-000321-dairy-building-grounding.

ENVO:00003862 has the correct dairy label but denotes a building for milk harvesting/processing. The record represents an isolate-derived kefir model; no building-specific modeled setting is established. This semantic finding survives a passing label check.

Disposition: Remains open after independent current-source reassessment; the relevant canonical field is unchanged.

### genome-provenance: Exact genome input remains unreconciled

major / open / confirmed; issue key: cm-000321-genome-input-provenance.

The paper reports KRP/NDFM with 81 contigs and 2,522,693 bp; current NDFM01/Olga and assembly metadata report 401 contigs and 2,756,010 bp with contamination and RefSeq suppression. Sample 156 partially bridges aliases, so these sources do not prove distinct isolates. The exact version/preprocessing used for the KRP model remains unsupported by an unqualified accession assertion.

Disposition: Remains open after independent current-source reassessment; the relevant canonical field is unchanged.

### citation-placement: Design and model-resource evidence still use a title only

minor / open / confirmed; issue key: cm-000321-title-only-evidence.

The unchanged title-only snippets provide study context but do not substantiate KRP reconstruction/FBA endpoints or the exact BioModels artifact. Current Methods, authors mapping and retrieved model metadata supply positive evidence for those claims, so the correction is claim-local placement rather than model-identity rejection.

Disposition: Remains open after independent current-source reassessment; the relevant canonical field is unchanged.

### role-attribution: Generic FBA does not establish a KRP cross-feeder role

major / open / confirmed; issue key: cm-000321-cross-feeder-attribution.

The new functional_role CROSS_FEEDER asserts utilization of metabolites from other taxa. Its attached evidence describes all-species simulated amino-acid uptake/secretion. The inspected paper and artifact identity do not establish the origin of a KRP-consumed metabolite or KRP-specific partner exchange. Computational evidence could support a properly specified prediction, but the present generic workflow does not support this particular role.

### medium-link: GAM isolation medium lacks an exact external linkage

minor / open / confirmed; issue key: cm-000321-gam-medium-linkage.

The GAM agar entry has no CultureMech or MediaIngredientMech linkage. The paper supports the medium name and isolation conditions but not an exact recipe/catalogue identity; this is an enrichment gap, not evidence that cultivation values are wrong.

### publication-placement: A publication is represented as a dataset

minor / open / confirmed; issue key: cm-000321-publication-as-dataset.

associated_datasets[1] is the primary article DOI/title and landing page rather than an identified dataset. The schema separates dataset accessions from associated publications. Retain the paper as literature context and preserve the independently positive BioModels and WGS entries.

## Recommended Actions And Acceptance Checks

### address-environment

Modeled environment still denotes a dairy building. Use an authoritative term matching the source-supported kefir/milk setting, or withhold the unsupported class.

- Use an authoritative term matching the source-supported kefir/milk setting, or withhold the unsupported class.
- Check the proposed definition against the source; preserve laboratory isolation versus modeled natural context.
- After separately authorized curation, run focused schema, strict, term and reference checks for data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml; append the required record history.

### address-genome-provenance

Exact genome input remains unreconciled. Document KRP/ISC 156/Olga aliases and distinguish published statistics from current deposited assembly metadata.

- Document KRP/ISC 156/Olga aliases and distinguish published statistics from current deposited assembly metadata.
- Identify the sequence/protein input version and filtering used for reconstruction before asserting exact equivalence.
- Preserve current QC limitations and the difference between authors and BioModels model revisions without declaring every prediction invalid.
- After separately authorized curation, run focused schema, strict, term and reference checks for data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml; append the required record history.

### address-citation-placement

Design and model-resource evidence still use a title only. Attach concise Methods evidence to reconstruction/FBA claims and exact deposit provenance to the model-resource identity.

- Attach concise Methods evidence to reconstruction/FBA claims and exact deposit provenance to the model-resource identity.
- Keep publication workflow, authors artifact and later BioModels revision distinct; quotations must match the source.
- After separately authorized curation, run focused schema, strict, term and reference checks for data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml; append the required record history.

### address-role-attribution

Generic FBA does not establish a KRP cross-feeder role. Remove or qualify the unsupported role until exact KRP-specific partner-product evidence or a defined computational cross-feeding result is attached.

- Remove or qualify the unsupported role until exact KRP-specific partner-product evidence or a defined computational cross-feeding result is attached.
- Retain the supported computational-potential node and RARE annotation; do not invent an alternative role or a measured exchange edge.
- After separately authorized curation, run focused schema, strict, term and reference checks for data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml; append the required record history.

### address-medium-link

GAM isolation medium lacks an exact external linkage. Verify the source GAM formulation or product identity and match an exact maintained medium entry before adding a link.

- Verify the source GAM formulation or product identity and match an exact maintained medium entry before adding a link.
- If exact identity remains unresolved, document that limit rather than substituting a similarly named recipe or modifying source-positive temperature/time.
- After separately authorized curation, run focused schema, strict, term and reference checks for data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml; append the required record history.

### address-publication-placement

A publication is represented as a dataset. Move the publication-only entry to a supported publication/external-resource relationship or identify a genuine deposited dataset before retaining it in associated_datasets.

- Move the publication-only entry to a supported publication/external-resource relationship or identify a genuine deposited dataset before retaining it in associated_datasets.
- Do not invent a data accession or remove the valid BioModels/WGS resources.
- After separately authorized curation, run focused schema, strict, term and reference checks for data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml; append the required record history.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml; Whole current record, including all nine EvidenceItems, one community-level node and no arrows. | supports | Current KRP model, source isolation, taxonomy, resource/dataset claims and the October 21 role/abundance additions were assessed. |
| predecessor | reviews/structured/20261019T074329Z-kefir-rothia-model-record/review.yaml; All three findings, actions, limitations, current-source comparisons and predecessor input identity. | supports | The two major and one minor predecessor findings are independently rechecked and retained open; no terminal disposition is inferred from a newer review. |
| change-proof | .temp/pr2034/321/target-change-proof.json; Exact Git diff and parsed field paths from a4611c913c8da9619673df63a0c2cce3aa206a83 to current HEAD. | supports | Only CROSS_FEEDER, RARE, two associated EvidenceItems and their history event changed. The three previously flagged claim surfaces remain unchanged. |
| genome-paper | https://pmc.ncbi.nlm.nih.gov/articles/PMC5624747/; PMID:28963201; DOI:10.1128/genomeA.00869-17. Retained scientific body characters 2849:6360; KRP isolation at 3787, accession at 6252. | supports | The genome report identifies KRP as ISC 156 from kefir grain, describes GAM agar isolation for two days at 30 degrees C, and reports 81 contigs, 2,522,693 bp and NDFM00000000. The low-abundance species context supports RARE without a numerical abundance claim. |
| modeling-paper | https://pmc.ncbi.nlm.nih.gov/articles/PMC7610452/; PMID:33398099; DOI:10.1038/s41564-020-00816-5. Entire retained scientific main characters 3567:62478 read; Metabolic modelling paragraph begins 56565. | supports | The authors reconstruct bacterial metabolic models and combine simulated amino-acid fluxes with measured community abundance. Specific experimental cooperation results concern other named pairs. Generic FBA and whole-kefir cooperation do not establish KRP utilization of a partner-derived metabolite. |
| biomodels | https://www.biomodels.org/MODEL2204300002?format=json; name, description, submissionId, files.main, modelLevelAnnotations, curationStatus and revision comments; author/contact fields excluded. Retrieved 2026-11-05T20:12:11.090977+00:00. | supports | Current BioModels names the KRP model, links the paper and authors repository, identifies the downloaded XML checksum, and records a 2024 gene-reaction-association update. NON_CURATED is the repository status, not a failed scientific identity check. |
| biomodels-sbml | https://www.biomodels.org/model/download/MODEL2204300002?filename=MODEL2204300002.xml; SBML model id and structural counts only; no solver execution. Retrieved 2026-11-05T20:12:11.381246+00:00. | supports | Downloaded model m_156_03182016 has 962 species, 1,336 reactions and 542 gene products. Its bytes agree with the current metadata checksum. |
| authors-model | https://raw.githubusercontent.com/cdanielmachado/kefir_paper/master/models/156_03182016.xml; SBML model id and structural counts; compared with authors species mapping. Retrieved 2026-11-05T20:12:11.994844+00:00. | supports | The authors artifact m_156_03182016 has 893 species, 1,274 reactions and 451 gene products. It supports model provenance but is not byte- or structure-identical to the current BioModels revision. |
| authors-species | https://raw.githubusercontent.com/cdanielmachado/kefir_paper/master/species_list.tsv; Exact row with key 156_03182016; other Rothia dentocariosa rows remain distinct. Retrieved 2026-11-05T20:12:11.274912+00:00. | supports | The authors map 156_03182016 to Rothia kefirresidentii KRP, supporting the KRP model identity without identifying every genome-processing step. |
| nuccore | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&amp;id=NDFM00000000&amp;rettype=gb&amp;retmode=text; ACCESSION, VERSION, ORGANISM, WGS comment and source organism/strain qualifiers; submitter/contact fields excluded. Retrieved 2026-11-05T20:12:11.917323+00:00. | supports | NDFM00000000.1 is deposited as Rothia sp. Olga with NDFM01 components 1 through 401 and BioSample SAMN06718477. |
| ena | https://www.ebi.ac.uk/ena/browser/api/embl/NDFM00000000.1?download=false; ID, AC, DE, BioSample cross-reference, WGS comment and source qualifiers. Retrieved 2026-11-05T20:12:12.717595+00:00. | supports | ENA independently exposes the NDFM01 Olga project and 401 sequences; this corroborates deposit metadata, not exact KRP model-input equivalence. |
| biosample | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=biosample&amp;id=SAMN06718477&amp;retmode=xml; BioSample accession, Sample name, organism and strain/isolation-source attributes only. Retrieved 2026-11-05T20:12:12.318550+00:00. | supports | SAMN06718477 uses sample name 156 - R.dentocariosa, organism Rothia sp. Olga and strain Olga, isolated from kefir. The shared 156 stock code is a partial bridge, not proof of a different isolate or a complete alias reconciliation. |
| assembly | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=assembly&amp;id=1163481&amp;retmode=json; result.1163481 accession/synonym, organism, biosource, WGS, assembly statistics, update date and QC flags. Retrieved 2026-11-05T20:12:12.610661+00:00. | supports | GCA/GCF_002238135.1 reports 401 contigs and 2,756,010 bp, with contamination/excluded-from-RefSeq/suppressed-RefSeq flags updated September 23, 2026. These differ from the paper statistics; they do not alone invalidate all model predictions. |
| artifact-proof | .temp/pr2034/321/primary-artifact-projection.json; Scientific projection and all nine retrieved source hashes; parsed SBML counts. | supports | The helper retains source hash/version evidence and excludes personal metadata from the scientific projection. |
| ontology | .temp/pr2034/321/ontology-authority.json; All six distinct ontology terms at seven placements, current labels, definitions and taxon rank from existing OAK SQLite builds. | supports | Labels all match. NCBITaxon:32207 is genus Rothia. ENVO:00003862 denotes a building, whereas GO amino-acid metabolism/transport and CHEBI amino acid fit the expressly computational node scope. |
| schema | src/communitymech/schema/communitymech.yaml; FunctionalRoleEnum.CROSS_FEEDER, AbundanceEnum, TaxonomicComposition, GrowthMedia and modeled_environment semantics. | supports | CROSS_FEEDER means utilization of metabolites from other taxa, not generic amino-acid transport or a modeled exchange reaction. RARE is an ordinal community annotation, not a percentage. |
| dataset-schema | src/communitymech/schema/mech_shared.yaml; Dataset definition, accession and separate publication attribute. | supports | A publication-only DOI entry is bibliographic context; the model XML and WGS accession remain positive data resources. |
| rubric | .claude/skills/review-communities/reference/validation-rules.md; P3.1 growth-media linkage and impact-based P1-P4 interpretation. | supports | GAM lacks CultureMech/MediaIngredientMech linkage. Exact formulation verification is required before linking; the published medium name alone is not recipe equivalence. |
| replay | .temp/pr2034/321/snippet-replay.json; All nine recursive EvidenceItems; whitespace-only normalization, no spelling/punctuation repair. | supports | Nine snippets match after whitespace normalization; eight match raw. Both graph snippets are raw exact. Literal matching does not establish the role, accession or claim-local support. |
| check-validate | .temp/pr2034/321/validate.json; Actual command, environment, start/finish, exit code and complete stdout/stderr. | supports | No issues found |
| check-validate-strict | .temp/pr2034/321/validate-strict.json; Actual command, environment, start/finish, exit code and complete stdout/stderr. | supports | uv run python scripts/validate_strict.py data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml --out /Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.temp/pr2034/321/strict.tsv<br>Validating 1 files with 17 workers; schema=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/src/communitymech/schema/communitymech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.temp/pr2034/321/strict.tsv |
| check-validate-terms | .temp/pr2034/321/validate-terms.json; Actual command, environment, start/finish, exit code and complete stdout/stderr. | supports | ✅ Validation passed |
| check-validate-references-explained | .temp/pr2034/321/validate-references-explained.json; Actual command, environment, start/finish, exit code and complete stdout/stderr. | supports | Validating data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml against schema src/communitymech/schema/communitymech.yaml<br>Cache directory: references_cache<br><br>Validation Summary:<br>  Reported validation issues: 0<br>  All validations passed!<br><br>[annotate] This is not a count of checked excerpts (#1469). Native Discussion evidence coverage remains incomplete (#476). |
| check-validate-gtdb | .temp/pr2034/321/validate-gtdb.json; Actual command, environment, start/finish, exit code and complete stdout/stderr. | supports | PYTHONPATH=src uv run python scripts/validate_gtdb_coherence.py data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml<br><br>files checked: 1<br>incoherent blocks: 0<br>malformed lineages: 0<br>lineage conflicts: 0 |
| check-validate-gtdb-domain | .temp/pr2034/321/validate-gtdb-domain.json; Actual command, environment, start/finish, exit code and complete stdout/stderr. | supports | files checked: 1<br>contradictory lineages: 0 |
| check-validate-history | .temp/pr2034/321/validate-history.json; Actual command, environment, start/finish, exit code and complete stdout/stderr. | supports | No issues found |
| check-audit-network | .temp/pr2034/273/audit-network.json; Actual same-session corpus command; output hashes and files; network-corpus-inputs.json independently rehashed for all 503 inputs. | supports | Actual exit 1: 44 warnings in 16 of 503 records, zero errors. No KRP target finding. The unchanged-corpus result is reused rather than rerun. |
| check-check-network-quality | .temp/pr2034/273/check-network-quality.json; Actual same-session corpus command; output hashes and files; network-corpus-inputs.json independently rehashed for all 503 inputs. | supports | Actual exit 1: 44 warnings in 16 of 503 records, zero errors. No KRP target finding. The unchanged-corpus result is reused rather than rerun. |

## Limits And Additional Notes

- No FBA optimization or FROG rerun was performed. Structural model checks and artifact hashes do not prove numerical reproducibility or revision equivalence.
- The exact model-input assembly/version/filtering and complete KRP/Olga alias relationship remain unresolved and are an explicit finding. This does not prevent completing the evidence assessment.
- The historical 1,075-genome GTDB aggregate was not regenerated. Current local ontology rank/labels, lineage coherence and prokaryotic domain were independently checked; no strain identity is inferred from genus grounding.
- Current sources identify GAM agar but do not settle exact formulation, isolate-specific atmosphere or FBA medium exchange bounds. No values are inferred from whole-kefir fermentation.
- Both required corpus network gates returned warning failures elsewhere. These remain failed checks; the target itself has one connected computational node and no dangling edges.
- Public model/genome metadata initially displayed some author/contact fields during an overbroad projection. They were excluded from scientific use; the persisted scientific projection and evidence locators select only model, organism, accession and QC fields.
- Downloaded snapshots and command outputs are retained in current session scratch and hash-pinned through native inspection; this successor does not depend on deleted historical /tmp artifacts.
- No canonical record, history event, ontology, schema, generated product or scientific-status field was edited. All curation actions are proposals.
- CLAUDE.md is a symlink to the regular AGENTS.md. Native inspection rejected the symlink before assessment; the corrected inspection pins AGENTS.md. The initial administrative failure remains in a separate receipt.
- The initial sandbox source-download attempt failed DNS resolution. The authorized public-source retry succeeded for all nine URLs; neither attempt is represented as a scientific validator failure.
- The historical #2050 role/abundance curation is context, not a resolution of the three predecessor findings. This review does not itself change any GitHub issue disposition.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261105T202026Z-pr2034-kefir-rothia-successor
kind: record
repository: CultureBotAI/CommunityMech
title: 'PR 2034: current-source successor for the KRP BioModels isolate'
started_at: '2026-11-05T20:11:18.492562Z'
finished_at: '2026-11-05T20:20:26.977078Z'
reviewer:
  identity: codex
  kind: agent
  independence: unknown
  independence_basis: This author did not curate the current target. Earlier curation/review
    used agent identities, so personal independence is not established. Root and a
    separately assigned adversary review this successor independently.
skill: review-yaml-record
completion: completed
verdict: needs_curation
scientific_review: true
summary: 'The three predecessor findings remain open. Current evidence also identifies
  an unsupported KRP cross-feeder role, an unlinked GAM formulation and a publication-only
  dataset entry: 3 P2 and 3 P3. Model identity, the qualified computational node,
  RARE and GAM isolation conditions are supported. All focused checks passed; two
  executed corpus gates retain unrelated warning failures.'
source:
  git_revision: 85dd2c055582c12509c38b011e5034ab2774293f
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: d2f94c87b82f59663bc2b0c91ac04a245e56fab52d8c11e6bddb559eb9237c84
    role: context
  - path: .claude/skills/evidence-curation/SKILL.md
    sha256: 5c5e3c62dc733c762afbf790b270b978b5c523930dbe6c74a88beda81007f396
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
  - path: .temp/pr2034/273/audit-network.json
    sha256: a28133e5b388d1a0594bc58b16fd237618943e054345e296e4ef2737ae6be810
    role: context
  - path: .temp/pr2034/273/audit-network.stderr.txt
    sha256: a71fb29e950f3eaf0eb2b834a43c59d4a1b6aa85a2a89473ae99b0e408a27a36
    role: context
  - path: .temp/pr2034/273/audit-network.stdout.txt
    sha256: f5dc190f832300fc5a73fcf3e7e8e3cd53d560ba09b17179ce6c7fcc8aa022e8
    role: context
  - path: .temp/pr2034/273/check-network-quality.json
    sha256: b9be72f7ae4be274768f3b981005323c04d3397265763147b37e92395aae49e6
    role: context
  - path: .temp/pr2034/273/check-network-quality.stderr.txt
    sha256: f9a8e9fb5a4e4ea545236a809393dbc1ce4325b14579c65a3130bcfe713e798a
    role: context
  - path: .temp/pr2034/273/check-network-quality.stdout.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2034/273/network-corpus-inputs.json
    sha256: 2b94a172a8f7176be6b61c613eea0051c487a91dd14fb552445168b9298c6c8c
    role: context
  - path: .temp/pr2034/321/candidate-native-v1.json
    sha256: 62de0fe0584ba4000f428e43cbade0031131a3889bd0edc73d8372c37762c9c1
    role: context
  - path: .temp/pr2034/321/inspect-command-v2.json
    sha256: fe937f665fdf72d961173f05d7fc86915cbd353a41930d44af0186664d85824e
    role: context
  - path: .temp/pr2034/321/inspect-command.json
    sha256: 7a4251ae0c19651f4b2db369f19b3186563fbd313d0ac618fa8d124feab031e1
    role: context
  - path: .temp/pr2034/321/network-reuse.json
    sha256: b9f3222318bed20c20d8f75f9e341efc666c7191c813eba5bb85b0265fb5cc66
    role: context
  - path: .temp/pr2034/321/ontology-authority.json
    sha256: 05434b7750c2c67f72aae22a501d632fb03e3219ada5e3aab922ed5ba0265b50
    role: context
  - path: .temp/pr2034/321/primary-artifact-projection.json
    sha256: 6b033b600f3a11aeb6a6543ba20c3aa15a31ca24db1e54d7d5838e43a77e3d16
    role: context
  - path: .temp/pr2034/321/snippet-replay.json
    sha256: bf3c2fcc110140b6eedc47d4ec526734d2c7aa2db7953caa556f3c8a4ec261df
    role: context
  - path: .temp/pr2034/321/source-retrieval-v2.json
    sha256: c83f3fbc11b1dba063bff289712d8d38dd9454de6661a4f16f344eb56bdf8cae
    role: context
  - path: .temp/pr2034/321/source-retrieval.json
    sha256: f0c1fda5ab75d9ae831a057ced3ebd41361049040cfd52adfdca3d29ad890349
    role: context
  - path: .temp/pr2034/321/sources/assembly.json
    sha256: 8dac93eb670fc178aadecca5d1033f455c7a5a5ef498eddf6c130e7fac4bf5a2
    role: context
  - path: .temp/pr2034/321/sources/authors-model.xml
    sha256: 255cf2e2757c3498f1c6ae27be0221a68bcce579f7e756f53a599111136494af
    role: context
  - path: .temp/pr2034/321/sources/authors-readme.md
    sha256: e69fb590cb722a061de36a3d4d595baea4668a8291eb1b2997477a626951a033
    role: context
  - path: .temp/pr2034/321/sources/authors-species.tsv
    sha256: c045a104428a64d237425c889cf5a88b26bce51b94fa968b0a2381212046eb62
    role: context
  - path: .temp/pr2034/321/sources/biomodels-metadata.json
    sha256: 530de72cc3dd54cea63c233b9b01584c303fd9faa8ab447a2928ae5960e1f22a
    role: context
  - path: .temp/pr2034/321/sources/biomodels-model.xml
    sha256: 5c167d59905454e0d8ebb5da5ea0dda43f70fa2d281c28bb3926eec23529e3dc
    role: context
  - path: .temp/pr2034/321/sources/biosample.xml
    sha256: 2c11227f6e1d89b2192479ee461d4d42175fb6abd36317adedb59d33befd7b1d
    role: context
  - path: .temp/pr2034/321/sources/ena.embl
    sha256: 7beee9f1a195902c4f44ce1428a0e880db4527ee885e9cfd31576cb4087fb611
    role: context
  - path: .temp/pr2034/321/sources/nuccore.gb
    sha256: 57721bf6711536c95f8a697add9f2b01640ed183293d1fc32361e26d4859d567
    role: context
  - path: .temp/pr2034/321/strict.tsv
    sha256: b184ed5450b968070bb6c75648407e388f41a1eaf7017890723cf560999fc3f7
    role: context
  - path: .temp/pr2034/321/target-change-proof.json
    sha256: 00e1794a43925462c69a4292f44478d70f443454715b41ac83b9b26d07a949fc
    role: context
  - path: .temp/pr2034/321/validate-gtdb-domain.json
    sha256: ee94fd68b54b19a1ab259ea039ae36c5506eac4208ca50cd8ee0b557f079c0e6
    role: context
  - path: .temp/pr2034/321/validate-gtdb.json
    sha256: cea258f2493189165bcbcff995eb3314c184ad2464c34833611ec13384f56eaf
    role: context
  - path: .temp/pr2034/321/validate-history.json
    sha256: d1ff807f98fef174aa5a855fa94b3f02a4e8a117e003a2968f5bf316f273e6bd
    role: context
  - path: .temp/pr2034/321/validate-references-explained.json
    sha256: a45701f02ef92ff710b77aba27d79b61190e5e4ea348a6d4602f6901d5611839
    role: context
  - path: .temp/pr2034/321/validate-strict.json
    sha256: d1abd576231e02e5b2ea136b5256fc86d976dbdd1e13fb5444b4c058c47c0704
    role: context
  - path: .temp/pr2034/321/validate-terms.json
    sha256: d3c2c155090bef49c9f1e5e84dbe53a99e4cd8d52868be350e3c41148e2fde95
    role: context
  - path: .temp/pr2034/321/validate.json
    sha256: 3cfcb5adc6a716d56c8bc34d6358a0c347d85ebd9aa786b2e3efacdfe11e2232
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
  - path: data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml
    sha256: 3f3fe69bc250a439ff851305a95d485ad1deee50602335de11b36601542e04d4
    role: target
  - path: docs/record-review-profile.md
    sha256: 285f79747999f83edbe63e5efde349a5cc063e9e486ce1a748b47b76c6631f31
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: history/records/BioModels_MODEL2204300002_Kefir_Rothia_Model/2026-10-05T071439Z-codex-9feb28.yaml
    sha256: 8a81483f7c5e516d05a4ca41c850c4dc7955bc942202b3113b76c1e8e6335b81
    role: context
  - path: history/records/BioModels_MODEL2204300002_Kefir_Rothia_Model/2026-10-21T190000Z-claude-2050.yaml
    sha256: 854baa4a04d605e87f9363f72e898443bdf36103061b3b4b9dd072e975d62b31
    role: context
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: references_cache/PMID_28963201.txt
    sha256: 9c7771620800e1a3a7f4947c4f6b8c17f3914b4fa00a16f2a5977a06a46dd0ad
    role: context
  - path: references_cache/PMID_33398099.md
    sha256: 354e026bfc49347f90ada79c14aa18776d7a0b9e2525868f0006ab50d4c8f4d2
    role: context
  - path: reports/causal_graph_review/decisions/20261005-six-records-batch3.yaml
    sha256: 3e0877c63e94f1c87d6c78b6d5480a0be07d80f1cd18f8db5efda4e8e2ea4d26
    role: context
  - path: reports/causal_graph_review/decisions/20261021-stage5-review-remediation.yaml
    sha256: efe4b6b56ae2ad5cb78452493088e5c046f10602461d581920791b19f9178119
    role: context
  - path: reviews/structured/20261019T074329Z-kefir-rothia-model-record/review.yaml
    sha256: 81ede05378251db77bffad76f40efd8fc70b1a0c076ea35791248bdc27d5c0ef
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/adhoc/pr2034_321_capture.py
    sha256: aca1fddabffcc57a7b73116dec338e7d406cc2b84d060463173fb482cb7eb5f1
    role: context
  - path: scripts/adhoc/pr2034_321_evidence.py
    sha256: 2b3e9ec37b56e7d48732401b4e8426ec3685623fe7b1e9b420cb40ad7686fb40
    role: context
  - path: scripts/adhoc/pr2034_321_finish.py
    sha256: f7147c6ba738c6e7ffd82d41437a1d2ce38bed277e4916964bce1d6bba30df09
    role: context
  - path: scripts/adhoc/pr2034_321_review.py
    sha256: 038d1da048c7e48302ce1b17cb268d32799519f5669f15568f7d083cb2bf7189
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
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
- target_id: CommunityMech:000321
  path: data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml
  label: BioModels MODEL2204300002 Kefir Rothia Model
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml
    role: canonical_record
scope:
  description: Whole current isolate record and all predecessor findings, with current
    primary model/genome retrieval, paper/source and ontology reassessment.
  selection: Explicit PR 2034 canary refresh of the stale CommunityMech:000321 review
    only.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000321
checks:
- check_id: validate
  name: validate
  status: passed
  required: true
  target_ids:
  - CommunityMech:000321
  command: just --no-dotenv validate data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate
  summary: Focused current-record check passed.
  scope_note: Single target; history checks use its exact history directory. Shared
    main .venv used with UV_NO_SYNC=1; full environment is recorded in the receipt.
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  target_ids:
  - CommunityMech:000321
  command: just --no-dotenv validate-strict data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml
    --out /Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.temp/pr2034/321/strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-strict
  summary: Focused current-record check passed.
  scope_note: Single target; history checks use its exact history directory. Shared
    main .venv used with UV_NO_SYNC=1; full environment is recorded in the receipt.
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  target_ids:
  - CommunityMech:000321
  command: just --no-dotenv validate-terms data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-terms
  summary: Focused current-record check passed.
  scope_note: Single target; history checks use its exact history directory. Shared
    main .venv used with UV_NO_SYNC=1; full environment is recorded in the receipt.
- check_id: validate-references-explained
  name: validate-references-explained
  status: passed
  required: true
  target_ids:
  - CommunityMech:000321
  command: just --no-dotenv validate-references-explained data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-references-explained
  summary: Focused current-record check passed; the reference summary counts reported
    issues, not checked excerpts.
  scope_note: Single target; history checks use its exact history directory. Shared
    main .venv used with UV_NO_SYNC=1; full environment is recorded in the receipt.
- check_id: validate-gtdb
  name: validate-gtdb
  status: passed
  required: true
  target_ids:
  - CommunityMech:000321
  command: just --no-dotenv validate-gtdb data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb
  summary: Focused current-record check passed.
  scope_note: Single target; history checks use its exact history directory. Shared
    main .venv used with UV_NO_SYNC=1; full environment is recorded in the receipt.
- check_id: validate-gtdb-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  target_ids:
  - CommunityMech:000321
  command: just --no-dotenv validate-gtdb-domain data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb-domain
  summary: Focused current-record check passed.
  scope_note: Single target; history checks use its exact history directory. Shared
    main .venv used with UV_NO_SYNC=1; full environment is recorded in the receipt.
- check_id: validate-history
  name: validate-history
  status: passed
  required: true
  target_ids:
  - CommunityMech:000321
  command: just --no-dotenv validate-history history/records/BioModels_MODEL2204300002_Kefir_Rothia_Model
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-history
  summary: Focused current-record check passed.
  scope_note: Single target; history checks use its exact history directory. Shared
    main .venv used with UV_NO_SYNC=1; full environment is recorded in the receipt.
- check_id: audit-network
  name: audit-network
  status: failed
  required: true
  target_ids:
  - CommunityMech:000321
  command: just --no-dotenv audit-network
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-audit-network
  summary: Corpus warnings retain a failed required gate; they are not attributed
    to this target.
  scope_note: All 503 direct records in both default roots, including ignored files;
    exact manifest hashes verified at reuse.
- check_id: check-network-quality
  name: check-network-quality
  status: failed
  required: true
  target_ids:
  - CommunityMech:000321
  command: just --no-dotenv check-network-quality
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-check-network-quality
  summary: Corpus warnings retain a failed required gate; they are not attributed
    to this target.
  scope_note: All 503 direct records in both default roots, including ignored files;
    exact manifest hashes verified at reuse.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml
  locator: Whole current record, including all nine EvidenceItems, one community-level
    node and no arrows.
  accessed_at: '2026-11-05T20:20:26.977078Z'
  support: supports
  summary: Current KRP model, source isolation, taxonomy, resource/dataset claims
    and the October 21 role/abundance additions were assessed.
  snapshot_sha256: 3f3fe69bc250a439ff851305a95d485ad1deee50602335de11b36601542e04d4
- evidence_id: predecessor
  kind: prior_review
  reference: reviews/structured/20261019T074329Z-kefir-rothia-model-record/review.yaml
  locator: All three findings, actions, limitations, current-source comparisons and
    predecessor input identity.
  accessed_at: '2026-11-05T20:20:26.977078Z'
  support: supports
  summary: The two major and one minor predecessor findings are independently rechecked
    and retained open; no terminal disposition is inferred from a newer review.
  snapshot_sha256: 81ede05378251db77bffad76f40efd8fc70b1a0c076ea35791248bdc27d5c0ef
- evidence_id: change-proof
  kind: record_content
  reference: .temp/pr2034/321/target-change-proof.json
  locator: Exact Git diff and parsed field paths from a4611c913c8da9619673df63a0c2cce3aa206a83
    to current HEAD.
  accessed_at: '2026-11-05T20:20:26.977078Z'
  support: supports
  summary: Only CROSS_FEEDER, RARE, two associated EvidenceItems and their history
    event changed. The three previously flagged claim surfaces remain unchanged.
  snapshot_sha256: 00e1794a43925462c69a4292f44478d70f443454715b41ac83b9b26d07a949fc
- evidence_id: genome-paper
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC5624747/
  locator: PMID:28963201; DOI:10.1128/genomeA.00869-17. Retained scientific body characters
    2849:6360; KRP isolation at 3787, accession at 6252.
  accessed_at: '2026-11-05T20:20:26.977078Z'
  support: supports
  summary: The genome report identifies KRP as ISC 156 from kefir grain, describes
    GAM agar isolation for two days at 30 degrees C, and reports 81 contigs, 2,522,693
    bp and NDFM00000000. The low-abundance species context supports RARE without a
    numerical abundance claim.
  snapshot_sha256: 9c7771620800e1a3a7f4947c4f6b8c17f3914b4fa00a16f2a5977a06a46dd0ad
- evidence_id: modeling-paper
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC7610452/
  locator: PMID:33398099; DOI:10.1038/s41564-020-00816-5. Entire retained scientific
    main characters 3567:62478 read; Metabolic modelling paragraph begins 56565.
  accessed_at: '2026-11-05T20:20:26.977078Z'
  support: supports
  summary: The authors reconstruct bacterial metabolic models and combine simulated
    amino-acid fluxes with measured community abundance. Specific experimental cooperation
    results concern other named pairs. Generic FBA and whole-kefir cooperation do
    not establish KRP utilization of a partner-derived metabolite.
  snapshot_sha256: 354e026bfc49347f90ada79c14aa18776d7a0b9e2525868f0006ab50d4c8f4d2
- evidence_id: biomodels
  kind: database
  reference: https://www.biomodels.org/MODEL2204300002?format=json
  locator: name, description, submissionId, files.main, modelLevelAnnotations, curationStatus
    and revision comments; author/contact fields excluded. Retrieved 2026-11-05T20:12:11.090977+00:00.
  accessed_at: '2026-11-05T20:20:26.977078Z'
  support: supports
  summary: Current BioModels names the KRP model, links the paper and authors repository,
    identifies the downloaded XML checksum, and records a 2024 gene-reaction-association
    update. NON_CURATED is the repository status, not a failed scientific identity
    check.
  snapshot_sha256: 530de72cc3dd54cea63c233b9b01584c303fd9faa8ab447a2928ae5960e1f22a
- evidence_id: biomodels-sbml
  kind: database
  reference: https://www.biomodels.org/model/download/MODEL2204300002?filename=MODEL2204300002.xml
  locator: SBML model id and structural counts only; no solver execution. Retrieved
    2026-11-05T20:12:11.381246+00:00.
  accessed_at: '2026-11-05T20:20:26.977078Z'
  support: supports
  summary: Downloaded model m_156_03182016 has 962 species, 1,336 reactions and 542
    gene products. Its bytes agree with the current metadata checksum.
  snapshot_sha256: 5c167d59905454e0d8ebb5da5ea0dda43f70fa2d281c28bb3926eec23529e3dc
- evidence_id: authors-model
  kind: database
  reference: https://raw.githubusercontent.com/cdanielmachado/kefir_paper/master/models/156_03182016.xml
  locator: SBML model id and structural counts; compared with authors species mapping.
    Retrieved 2026-11-05T20:12:11.994844+00:00.
  accessed_at: '2026-11-05T20:20:26.977078Z'
  support: supports
  summary: The authors artifact m_156_03182016 has 893 species, 1,274 reactions and
    451 gene products. It supports model provenance but is not byte- or structure-identical
    to the current BioModels revision.
  snapshot_sha256: 255cf2e2757c3498f1c6ae27be0221a68bcce579f7e756f53a599111136494af
- evidence_id: authors-species
  kind: database
  reference: https://raw.githubusercontent.com/cdanielmachado/kefir_paper/master/species_list.tsv
  locator: Exact row with key 156_03182016; other Rothia dentocariosa rows remain
    distinct. Retrieved 2026-11-05T20:12:11.274912+00:00.
  accessed_at: '2026-11-05T20:20:26.977078Z'
  support: supports
  summary: The authors map 156_03182016 to Rothia kefirresidentii KRP, supporting
    the KRP model identity without identifying every genome-processing step.
  snapshot_sha256: c045a104428a64d237425c889cf5a88b26bce51b94fa968b0a2381212046eb62
- evidence_id: nuccore
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=NDFM00000000&rettype=gb&retmode=text
  locator: ACCESSION, VERSION, ORGANISM, WGS comment and source organism/strain qualifiers;
    submitter/contact fields excluded. Retrieved 2026-11-05T20:12:11.917323+00:00.
  accessed_at: '2026-11-05T20:20:26.977078Z'
  support: supports
  summary: NDFM00000000.1 is deposited as Rothia sp. Olga with NDFM01 components 1
    through 401 and BioSample SAMN06718477.
  snapshot_sha256: 57721bf6711536c95f8a697add9f2b01640ed183293d1fc32361e26d4859d567
- evidence_id: ena
  kind: database
  reference: https://www.ebi.ac.uk/ena/browser/api/embl/NDFM00000000.1?download=false
  locator: ID, AC, DE, BioSample cross-reference, WGS comment and source qualifiers.
    Retrieved 2026-11-05T20:12:12.717595+00:00.
  accessed_at: '2026-11-05T20:20:26.977078Z'
  support: supports
  summary: ENA independently exposes the NDFM01 Olga project and 401 sequences; this
    corroborates deposit metadata, not exact KRP model-input equivalence.
  snapshot_sha256: 7beee9f1a195902c4f44ce1428a0e880db4527ee885e9cfd31576cb4087fb611
- evidence_id: biosample
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=biosample&id=SAMN06718477&retmode=xml
  locator: BioSample accession, Sample name, organism and strain/isolation-source
    attributes only. Retrieved 2026-11-05T20:12:12.318550+00:00.
  accessed_at: '2026-11-05T20:20:26.977078Z'
  support: supports
  summary: SAMN06718477 uses sample name 156 - R.dentocariosa, organism Rothia sp.
    Olga and strain Olga, isolated from kefir. The shared 156 stock code is a partial
    bridge, not proof of a different isolate or a complete alias reconciliation.
  snapshot_sha256: 2c11227f6e1d89b2192479ee461d4d42175fb6abd36317adedb59d33befd7b1d
- evidence_id: assembly
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=assembly&id=1163481&retmode=json
  locator: result.1163481 accession/synonym, organism, biosource, WGS, assembly statistics,
    update date and QC flags. Retrieved 2026-11-05T20:12:12.610661+00:00.
  accessed_at: '2026-11-05T20:20:26.977078Z'
  support: supports
  summary: GCA/GCF_002238135.1 reports 401 contigs and 2,756,010 bp, with contamination/excluded-from-RefSeq/suppressed-RefSeq
    flags updated September 23, 2026. These differ from the paper statistics; they
    do not alone invalidate all model predictions.
  snapshot_sha256: 8dac93eb670fc178aadecca5d1033f455c7a5a5ef498eddf6c130e7fac4bf5a2
- evidence_id: artifact-proof
  kind: database
  reference: .temp/pr2034/321/primary-artifact-projection.json
  locator: Scientific projection and all nine retrieved source hashes; parsed SBML
    counts.
  accessed_at: '2026-11-05T20:20:26.977078Z'
  support: supports
  summary: The helper retains source hash/version evidence and excludes personal metadata
    from the scientific projection.
  snapshot_sha256: 6b033b600f3a11aeb6a6543ba20c3aa15a31ca24db1e54d7d5838e43a77e3d16
- evidence_id: ontology
  kind: authority
  reference: .temp/pr2034/321/ontology-authority.json
  locator: All six distinct ontology terms at seven placements, current labels, definitions
    and taxon rank from existing OAK SQLite builds.
  accessed_at: '2026-11-05T20:20:26.977078Z'
  support: supports
  summary: Labels all match. NCBITaxon:32207 is genus Rothia. ENVO:00003862 denotes
    a building, whereas GO amino-acid metabolism/transport and CHEBI amino acid fit
    the expressly computational node scope.
  snapshot_sha256: 05434b7750c2c67f72aae22a501d632fb03e3219ada5e3aab922ed5ba0265b50
- evidence_id: schema
  kind: authority
  reference: src/communitymech/schema/communitymech.yaml
  locator: FunctionalRoleEnum.CROSS_FEEDER, AbundanceEnum, TaxonomicComposition, GrowthMedia
    and modeled_environment semantics.
  accessed_at: '2026-11-05T20:20:26.977078Z'
  support: supports
  summary: CROSS_FEEDER means utilization of metabolites from other taxa, not generic
    amino-acid transport or a modeled exchange reaction. RARE is an ordinal community
    annotation, not a percentage.
  snapshot_sha256: a00434e0d75020b2926c9f755d625c09cc78b6f88135805991fcb0ecd4230c83
- evidence_id: dataset-schema
  kind: authority
  reference: src/communitymech/schema/mech_shared.yaml
  locator: Dataset definition, accession and separate publication attribute.
  accessed_at: '2026-11-05T20:20:26.977078Z'
  support: supports
  summary: A publication-only DOI entry is bibliographic context; the model XML and
    WGS accession remain positive data resources.
  snapshot_sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
- evidence_id: rubric
  kind: authority
  reference: .claude/skills/review-communities/reference/validation-rules.md
  locator: P3.1 growth-media linkage and impact-based P1-P4 interpretation.
  accessed_at: '2026-11-05T20:20:26.977078Z'
  support: supports
  summary: GAM lacks CultureMech/MediaIngredientMech linkage. Exact formulation verification
    is required before linking; the published medium name alone is not recipe equivalence.
  snapshot_sha256: 3860e91a64f7c1f55f80e3d7a361d0798bbd00cbaf5cb7720a7533673e5afe2e
- evidence_id: replay
  kind: validation
  reference: .temp/pr2034/321/snippet-replay.json
  locator: All nine recursive EvidenceItems; whitespace-only normalization, no spelling/punctuation
    repair.
  accessed_at: '2026-11-05T20:20:26.977078Z'
  support: supports
  summary: Nine snippets match after whitespace normalization; eight match raw. Both
    graph snippets are raw exact. Literal matching does not establish the role, accession
    or claim-local support.
  snapshot_sha256: bf3c2fcc110140b6eedc47d4ec526734d2c7aa2db7953caa556f3c8a4ec261df
- evidence_id: check-validate
  kind: validation
  reference: .temp/pr2034/321/validate.json
  locator: Actual command, environment, start/finish, exit code and complete stdout/stderr.
  accessed_at: '2026-11-05T20:20:26.977078Z'
  support: supports
  summary: No issues found
  snapshot_sha256: 3cfcb5adc6a716d56c8bc34d6358a0c347d85ebd9aa786b2e3efacdfe11e2232
- evidence_id: check-validate-strict
  kind: validation
  reference: .temp/pr2034/321/validate-strict.json
  locator: Actual command, environment, start/finish, exit code and complete stdout/stderr.
  accessed_at: '2026-11-05T20:20:26.977078Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml\
    \ --out /Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.temp/pr2034/321/strict.tsv\n\
    Validating 1 files with 17 workers; schema=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/src/communitymech/schema/communitymech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.temp/pr2034/321/strict.tsv"
  snapshot_sha256: d1abd576231e02e5b2ea136b5256fc86d976dbdd1e13fb5444b4c058c47c0704
- evidence_id: check-validate-terms
  kind: validation
  reference: .temp/pr2034/321/validate-terms.json
  locator: Actual command, environment, start/finish, exit code and complete stdout/stderr.
  accessed_at: '2026-11-05T20:20:26.977078Z'
  support: supports
  summary: ✅ Validation passed
  snapshot_sha256: d3c2c155090bef49c9f1e5e84dbe53a99e4cd8d52868be350e3c41148e2fde95
- evidence_id: check-validate-references-explained
  kind: validation
  reference: .temp/pr2034/321/validate-references-explained.json
  locator: Actual command, environment, start/finish, exit code and complete stdout/stderr.
  accessed_at: '2026-11-05T20:20:26.977078Z'
  support: supports
  summary: "Validating data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml\
    \ against schema src/communitymech/schema/communitymech.yaml\nCache directory:\
    \ references_cache\n\nValidation Summary:\n  Reported validation issues: 0\n \
    \ All validations passed!\n\n[annotate] This is not a count of checked excerpts\
    \ (#1469). Native Discussion evidence coverage remains incomplete (#476)."
  snapshot_sha256: a45701f02ef92ff710b77aba27d79b61190e5e4ea348a6d4602f6901d5611839
- evidence_id: check-validate-gtdb
  kind: validation
  reference: .temp/pr2034/321/validate-gtdb.json
  locator: Actual command, environment, start/finish, exit code and complete stdout/stderr.
  accessed_at: '2026-11-05T20:20:26.977078Z'
  support: supports
  summary: 'PYTHONPATH=src uv run python scripts/validate_gtdb_coherence.py data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml


    files checked: 1

    incoherent blocks: 0

    malformed lineages: 0

    lineage conflicts: 0'
  snapshot_sha256: cea258f2493189165bcbcff995eb3314c184ad2464c34833611ec13384f56eaf
- evidence_id: check-validate-gtdb-domain
  kind: validation
  reference: .temp/pr2034/321/validate-gtdb-domain.json
  locator: Actual command, environment, start/finish, exit code and complete stdout/stderr.
  accessed_at: '2026-11-05T20:20:26.977078Z'
  support: supports
  summary: 'files checked: 1

    contradictory lineages: 0'
  snapshot_sha256: ee94fd68b54b19a1ab259ea039ae36c5506eac4208ca50cd8ee0b557f079c0e6
- evidence_id: check-validate-history
  kind: validation
  reference: .temp/pr2034/321/validate-history.json
  locator: Actual command, environment, start/finish, exit code and complete stdout/stderr.
  accessed_at: '2026-11-05T20:20:26.977078Z'
  support: supports
  summary: No issues found
  snapshot_sha256: d1ff807f98fef174aa5a855fa94b3f02a4e8a117e003a2968f5bf316f273e6bd
- evidence_id: check-audit-network
  kind: validation
  reference: .temp/pr2034/273/audit-network.json
  locator: Actual same-session corpus command; output hashes and files; network-corpus-inputs.json
    independently rehashed for all 503 inputs.
  accessed_at: '2026-11-05T20:20:26.977078Z'
  support: supports
  summary: 'Actual exit 1: 44 warnings in 16 of 503 records, zero errors. No KRP target
    finding. The unchanged-corpus result is reused rather than rerun.'
  snapshot_sha256: a28133e5b388d1a0594bc58b16fd237618943e054345e296e4ef2737ae6be810
- evidence_id: check-check-network-quality
  kind: validation
  reference: .temp/pr2034/273/check-network-quality.json
  locator: Actual same-session corpus command; output hashes and files; network-corpus-inputs.json
    independently rehashed for all 503 inputs.
  accessed_at: '2026-11-05T20:20:26.977078Z'
  support: supports
  summary: 'Actual exit 1: 44 warnings in 16 of 503 records, zero errors. No KRP target
    finding. The unchanged-corpus result is reused rather than rerun.'
  snapshot_sha256: b9be72f7ae4be274768f3b981005323c04d3397265763147b37e92395aae49e6
assessments:
- assessment_id: identity
  area: identity
  topic: KRP computational model and source strain
  outcome: supported
  summary: Current primary metadata and both model artifacts identify KRP. This is
    one isolate-derived computational model, not the whole kefir community and not
    proof that the isolate was genetically engineered.
  target_ids:
  - CommunityMech:000321
  evidence_ids:
  - record
  - genome-paper
  - biomodels
  - authors-model
  - authors-species
  dimensions:
  - name: source-strain
    value: Rothia kefirresidentii KRP; ISC 156
    definition: Publication and authors model identity; deposited Olga naming is separately
      unresolved.
    evidence_ids:
    - genome-paper
    - authors-species
    - biosample
  - name: taxon-rank
    value: NCBITaxon:32207 and GTDB:g__Rothia are genus-level
    definition: A conservative genus identity does not authenticate an exact genome.
    evidence_ids:
    - ontology
    - record
  - name: community-scope
    value: Single-member computational model
    definition: No measured KRP coculture, partner-specific transfer or causal arrow
      is encoded.
    evidence_ids:
    - record
    - modeling-paper
  - name: biomass-state
    value: Cultured isolate supplies genomic provenance; metabolism is simulated
    definition: GAM cultivation is not an FBA exchange-bound specification.
    evidence_ids:
    - genome-paper
    - biomodels
  - name: source-category
    value: Two retained primary papers and freshly downloaded primary model/genome
      repositories
    definition: Paper claims, original author model and later BioModels revision remain
      distinct.
    evidence_ids:
    - genome-paper
    - modeling-paper
    - artifact-proof
- assessment_id: roles
  area: scope
  topic: New role and abundance annotations
  outcome: concern
  summary: 'RARE is supported in the source grain context. CROSS_FEEDER still needs
    KRP-specific attribution: generic expected uptake/secretion and whole-community
    cooperation do not identify KRP consumption of another taxon''s products. Preserve
    computational potential without inventing a replacement ecological role.'
  target_ids:
  - CommunityMech:000321
  evidence_ids:
  - record
  - schema
  - genome-paper
  - modeling-paper
  - change-proof
- assessment_id: graph
  area: graph
  topic: Existing computational graph
  outcome: supported
  summary: Preserve the sole qualified node, amino-acid metabolite/process context,
    genus participant and absent edges. The source models amino-acid uptake and secretion;
    neither transport terms nor exchange reactions demonstrate donor-to-KRP transfer.
    The current graph already keeps that boundary.
  target_ids:
  - CommunityMech:000321
  evidence_ids:
  - record
  - modeling-paper
  - authors-species
  - biomodels-sbml
  - ontology
  - replay
  dimensions:
  - name: node-0
    value: ecological_interactions[0]; community-level; one participant NCBITaxon:32207;
      zero arrows
    definition: The computational node is not a measured pairwise ecological interaction.
    evidence_ids:
    - record
    - modeling-paper
    - biomodels
  - name: node-0-evidence-0
    value: 'references_cache/PMID_33398099.md characters 56565:56639. Inspected record
      snippet: Genome-scale metabolic models were reconstructed for all bacterial
      species'
    definition: Raw exact source match; model-method evidence with the recorded computational
      provenance, not direct biological transfer.
    evidence_ids:
    - modeling-paper
    - replay
  - name: node-0-evidence-1
    value: 'references_cache/PMID_33398099.md characters 56726:56837. Inspected record
      snippet: The models were used to simulate the expected uptake/secretion rates
      of amino acids using flux balance analysis'
    definition: Raw exact source match; model-method evidence with the recorded computational
      provenance, not direct biological transfer.
    evidence_ids:
    - modeling-paper
    - replay
- assessment_id: environment
  area: grounding
  topic: Isolation setting and represented kefir environment
  outcome: concern
  summary: Laboratory isolation is defensible. The dairy building term is not supported
    as the modeled kefir material/environment, even though its label validates.
  target_ids:
  - CommunityMech:000321
  evidence_ids:
  - record
  - genome-paper
  - ontology
- assessment_id: genome
  area: provenance
  topic: Genome and model versions
  outcome: concern
  summary: The published KRP/NDFM and deposited Olga/NDFM01 relationship remains unreconciled.
    Model identity is positive; the shared 156 key partly bridges names. Assembly
    size/contig differences and current QC flags require explicit version/filtering
    provenance, not an automatic taxon replacement or blanket rejection of modeled
    predictions.
  target_ids:
  - CommunityMech:000321
  evidence_ids:
  - genome-paper
  - authors-species
  - nuccore
  - ena
  - biosample
  - assembly
  - biomodels
  - artifact-proof
- assessment_id: cultivation
  area: completeness
  topic: KRP isolation and exact GAM linkage
  outcome: concern
  summary: Retain GAM agar, 30 degrees C, two days and ground-kefir serial-dilution
    isolation. Source does not establish an exact GAM formulation/catalogue match
    or an isolate-specific atmosphere; neither recipe nor model exchange constraints
    should be invented.
  target_ids:
  - CommunityMech:000321
  evidence_ids:
  - record
  - genome-paper
  - rubric
  dimensions:
  - name: cultivation-stage
    value: 'GAM agar isolation: 30 degrees C, two days'
    definition: Natural-community fermentation conditions and computational medium
      are distinct.
    evidence_ids:
    - genome-paper
    - modeling-paper
- assessment_id: resources
  area: evidence
  topic: Claim-local citation and resource representation
  outcome: concern
  summary: The model and WGS accessions are positive resources. Design/resource title
    snippets do not establish their specific claims, despite independently available
    Methods/deposit support. The paper DOI is a publication, not a separate deposited
    dataset.
  target_ids:
  - CommunityMech:000321
  evidence_ids:
  - record
  - modeling-paper
  - biomodels
  - dataset-schema
- assessment_id: gtdb
  area: grounding
  topic: Current taxonomic semantic checks
  outcome: supported
  summary: Current labels and genus rank are correct; GTDB lineage and domain gates
    pass. These checks do not regenerate the historical 1,075-genome mapping aggregate
    or establish KRP/Olga strain equivalence. No automatic species-level replacement
    is proposed.
  target_ids:
  - CommunityMech:000321
  evidence_ids:
  - ontology
  - record
  - check-validate-gtdb
  - check-validate-gtdb-domain
- assessment_id: metrics
  area: completeness
  topic: Native metrics and executed gates
  outcome: concern
  summary: All focused gates pass. Both required corpus gates executed and retain
    unrelated warning failures. Native completeness counts field presence, including
    the role under review; neither metric certifies scientific correctness.
  target_ids:
  - CommunityMech:000321
  evidence_ids:
  - record
  - replay
  - check-audit-network
  - check-check-network-quality
  metrics:
  - name: Completeness score
    value: 80
    unit: points
    minimum: 0
    maximum: 100
    definition: 'Literal native formula: 50 required-field points (including role
      presence), 5 environment, 5 external resources, 10 growth_media, 5 datasets,
      5 interaction metabolites; no environmental-factor or three-node bonus.'
  - name: Validation quality score
    value: 99
    unit: points
    minimum: 0
    maximum: 100
    definition: 100 - 3 P2*10 - 3 P3*2 + min((2 evidence/1 interaction)/2,1)*20 +
      15 for complete target network = 99. Corpus warnings remain separate failed
      checks.
  - name: P2 findings
    value: 3
    unit: findings
    definition: Target-specific major scientific/grounding findings.
  - name: P3 findings
    value: 3
    unit: findings
    definition: Target-specific bounded evidence, medium-linkage and publication-placement
      findings.
  - name: Evidence per interaction
    value: 2
    unit: EvidenceItems per interaction
    denominator: 1
    definition: Two excerpts on the single computational node; both from the same
      paper, not independent replication.
findings:
- finding_id: environment
  issue_key: cm-000321-dairy-building-grounding
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Modeled environment still denotes a dairy building
  description: ENVO:00003862 has the correct dairy label but denotes a building for
    milk harvesting/processing. The record represents an isolate-derived kefir model;
    no building-specific modeled setting is established. This semantic finding survives
    a passing label check.
  target_ids:
  - CommunityMech:000321
  field_paths:
  - modeled_environment[0].term.id
  - modeled_environment[0].preferred_term
  evidence_ids:
  - record
  - ontology
  - genome-paper
  rule_id: review-checklist.environment
  native_severity: P2
  normalization_reason: Materially unsupported ecological/identity/grounding inference.
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml
    role: canonical_record
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261019T074329Z-kefir-rothia-model-record
    finding_id: environment
  disposition_reason: Remains open after independent current-source reassessment;
    the relevant canonical field is unchanged.
- finding_id: genome-provenance
  issue_key: cm-000321-genome-input-provenance
  category: provenance
  severity: major
  status: open
  certainty: confirmed
  title: Exact genome input remains unreconciled
  description: The paper reports KRP/NDFM with 81 contigs and 2,522,693 bp; current
    NDFM01/Olga and assembly metadata report 401 contigs and 2,756,010 bp with contamination
    and RefSeq suppression. Sample 156 partially bridges aliases, so these sources
    do not prove distinct isolates. The exact version/preprocessing used for the KRP
    model remains unsupported by an unqualified accession assertion.
  target_ids:
  - CommunityMech:000321
  field_paths:
  - taxonomy[0].taxon_term.notes
  - taxonomy[0].evidence[1]
  - taxonomy[0].evidence[3].computational_provenance.input_accession
  - ecological_interactions[0].evidence[0].computational_provenance.input_accession
  - ecological_interactions[0].evidence[1].computational_provenance.input_accession
  - associated_datasets[2]
  evidence_ids:
  - record
  - genome-paper
  - authors-species
  - nuccore
  - ena
  - biosample
  - assembly
  - biomodels
  rule_id: CLAUDE.claim-level-evidence
  native_severity: P2
  normalization_reason: Materially unsupported ecological/identity/grounding inference.
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml
    role: canonical_record
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261019T074329Z-kefir-rothia-model-record
    finding_id: genome-provenance
  disposition_reason: Remains open after independent current-source reassessment;
    the relevant canonical field is unchanged.
- finding_id: citation-placement
  issue_key: cm-000321-title-only-evidence
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Design and model-resource evidence still use a title only
  description: The unchanged title-only snippets provide study context but do not
    substantiate KRP reconstruction/FBA endpoints or the exact BioModels artifact.
    Current Methods, authors mapping and retrieved model metadata supply positive
    evidence for those claims, so the correction is claim-local placement rather than
    model-identity rejection.
  target_ids:
  - CommunityMech:000321
  field_paths:
  - engineering_design.evidence[0]
  - external_resources[0].evidence[0]
  evidence_ids:
  - record
  - modeling-paper
  - authors-species
  - biomodels
  - biomodels-sbml
  rule_id: CLAUDE.claim-level-evidence
  native_severity: P3
  normalization_reason: Bounded, non-blocking evidence, representation or external-linkage
    correction.
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml
    role: canonical_record
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261019T074329Z-kefir-rothia-model-record
    finding_id: citation-placement
  disposition_reason: Remains open after independent current-source reassessment;
    the relevant canonical field is unchanged.
- finding_id: role-attribution
  issue_key: cm-000321-cross-feeder-attribution
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: Generic FBA does not establish a KRP cross-feeder role
  description: The new functional_role CROSS_FEEDER asserts utilization of metabolites
    from other taxa. Its attached evidence describes all-species simulated amino-acid
    uptake/secretion. The inspected paper and artifact identity do not establish the
    origin of a KRP-consumed metabolite or KRP-specific partner exchange. Computational
    evidence could support a properly specified prediction, but the present generic
    workflow does not support this particular role.
  target_ids:
  - CommunityMech:000321
  field_paths:
  - taxonomy[0].functional_role
  - taxonomy[0].evidence[3].explanation
  evidence_ids:
  - record
  - schema
  - modeling-paper
  - authors-species
  - change-proof
  rule_id: P2.4; CLAUDE.claim-level-evidence
  native_severity: P2
  normalization_reason: Materially unsupported ecological/identity/grounding inference.
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml
    role: canonical_record
- finding_id: medium-link
  issue_key: cm-000321-gam-medium-linkage
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: GAM isolation medium lacks an exact external linkage
  description: The GAM agar entry has no CultureMech or MediaIngredientMech linkage.
    The paper supports the medium name and isolation conditions but not an exact recipe/catalogue
    identity; this is an enrichment gap, not evidence that cultivation values are
    wrong.
  target_ids:
  - CommunityMech:000321
  field_paths:
  - growth_media[0]
  evidence_ids:
  - record
  - genome-paper
  - rubric
  rule_id: P3.1
  native_severity: P3
  normalization_reason: Bounded, non-blocking evidence, representation or external-linkage
    correction.
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml
    role: canonical_record
- finding_id: publication-placement
  issue_key: cm-000321-publication-as-dataset
  category: representation
  severity: minor
  status: open
  certainty: confirmed
  title: A publication is represented as a dataset
  description: associated_datasets[1] is the primary article DOI/title and landing
    page rather than an identified dataset. The schema separates dataset accessions
    from associated publications. Retain the paper as literature context and preserve
    the independently positive BioModels and WGS entries.
  target_ids:
  - CommunityMech:000321
  field_paths:
  - associated_datasets[1]
  evidence_ids:
  - record
  - dataset-schema
  - modeling-paper
  - biomodels
  - nuccore
  rule_id: review-checklist.resource-semantics
  native_severity: P3
  normalization_reason: Bounded, non-blocking evidence, representation or external-linkage
    correction.
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml
    role: canonical_record
actions:
- action_id: address-environment
  description: Modeled environment still denotes a dairy building. Use an authoritative
    term matching the source-supported kefir/milk setting, or withhold the unsupported
    class.
  finding_ids:
  - environment
  target_ids:
  - CommunityMech:000321
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml
    role: canonical_record
  acceptance_checks:
  - Use an authoritative term matching the source-supported kefir/milk setting, or
    withhold the unsupported class.
  - Check the proposed definition against the source; preserve laboratory isolation
    versus modeled natural context.
  - After separately authorized curation, run focused schema, strict, term and reference
    checks for data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml; append
    the required record history.
- action_id: address-genome-provenance
  description: Exact genome input remains unreconciled. Document KRP/ISC 156/Olga
    aliases and distinguish published statistics from current deposited assembly metadata.
  finding_ids:
  - genome-provenance
  target_ids:
  - CommunityMech:000321
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml
    role: canonical_record
  acceptance_checks:
  - Document KRP/ISC 156/Olga aliases and distinguish published statistics from current
    deposited assembly metadata.
  - Identify the sequence/protein input version and filtering used for reconstruction
    before asserting exact equivalence.
  - Preserve current QC limitations and the difference between authors and BioModels
    model revisions without declaring every prediction invalid.
  - After separately authorized curation, run focused schema, strict, term and reference
    checks for data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml; append
    the required record history.
- action_id: address-citation-placement
  description: Design and model-resource evidence still use a title only. Attach concise
    Methods evidence to reconstruction/FBA claims and exact deposit provenance to
    the model-resource identity.
  finding_ids:
  - citation-placement
  target_ids:
  - CommunityMech:000321
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml
    role: canonical_record
  acceptance_checks:
  - Attach concise Methods evidence to reconstruction/FBA claims and exact deposit
    provenance to the model-resource identity.
  - Keep publication workflow, authors artifact and later BioModels revision distinct;
    quotations must match the source.
  - After separately authorized curation, run focused schema, strict, term and reference
    checks for data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml; append
    the required record history.
- action_id: address-role-attribution
  description: Generic FBA does not establish a KRP cross-feeder role. Remove or qualify
    the unsupported role until exact KRP-specific partner-product evidence or a defined
    computational cross-feeding result is attached.
  finding_ids:
  - role-attribution
  target_ids:
  - CommunityMech:000321
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml
    role: canonical_record
  acceptance_checks:
  - Remove or qualify the unsupported role until exact KRP-specific partner-product
    evidence or a defined computational cross-feeding result is attached.
  - Retain the supported computational-potential node and RARE annotation; do not
    invent an alternative role or a measured exchange edge.
  - After separately authorized curation, run focused schema, strict, term and reference
    checks for data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml; append
    the required record history.
- action_id: address-medium-link
  description: GAM isolation medium lacks an exact external linkage. Verify the source
    GAM formulation or product identity and match an exact maintained medium entry
    before adding a link.
  finding_ids:
  - medium-link
  target_ids:
  - CommunityMech:000321
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml
    role: canonical_record
  acceptance_checks:
  - Verify the source GAM formulation or product identity and match an exact maintained
    medium entry before adding a link.
  - If exact identity remains unresolved, document that limit rather than substituting
    a similarly named recipe or modifying source-positive temperature/time.
  - After separately authorized curation, run focused schema, strict, term and reference
    checks for data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml; append
    the required record history.
- action_id: address-publication-placement
  description: A publication is represented as a dataset. Move the publication-only
    entry to a supported publication/external-resource relationship or identify a
    genuine deposited dataset before retaining it in associated_datasets.
  finding_ids:
  - publication-placement
  target_ids:
  - CommunityMech:000321
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml
    role: canonical_record
  acceptance_checks:
  - Move the publication-only entry to a supported publication/external-resource relationship
    or identify a genuine deposited dataset before retaining it in associated_datasets.
  - Do not invent a data accession or remove the valid BioModels/WGS resources.
  - After separately authorized curation, run focused schema, strict, term and reference
    checks for data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml; append
    the required record history.
limitations:
- No FBA optimization or FROG rerun was performed. Structural model checks and artifact
  hashes do not prove numerical reproducibility or revision equivalence.
- The exact model-input assembly/version/filtering and complete KRP/Olga alias relationship
  remain unresolved and are an explicit finding. This does not prevent completing
  the evidence assessment.
- The historical 1,075-genome GTDB aggregate was not regenerated. Current local ontology
  rank/labels, lineage coherence and prokaryotic domain were independently checked;
  no strain identity is inferred from genus grounding.
- Current sources identify GAM agar but do not settle exact formulation, isolate-specific
  atmosphere or FBA medium exchange bounds. No values are inferred from whole-kefir
  fermentation.
- Both required corpus network gates returned warning failures elsewhere. These remain
  failed checks; the target itself has one connected computational node and no dangling
  edges.
- Public model/genome metadata initially displayed some author/contact fields during
  an overbroad projection. They were excluded from scientific use; the persisted scientific
  projection and evidence locators select only model, organism, accession and QC fields.
- Downloaded snapshots and command outputs are retained in current session scratch
  and hash-pinned through native inspection; this successor does not depend on deleted
  historical /tmp artifacts.
notes:
- No canonical record, history event, ontology, schema, generated product or scientific-status
  field was edited. All curation actions are proposals.
- CLAUDE.md is a symlink to the regular AGENTS.md. Native inspection rejected the
  symlink before assessment; the corrected inspection pins AGENTS.md. The initial
  administrative failure remains in a separate receipt.
- The initial sandbox source-download attempt failed DNS resolution. The authorized
  public-source retry succeeded for all nine URLs; neither attempt is represented
  as a scientific validator failure.
- 'The historical #2050 role/abundance curation is context, not a resolution of the
  three predecessor findings. This review does not itself change any GitHub issue
  disposition.'
related_reviews:
- repository: CultureBotAI/CommunityMech
  review_id: 20261019T074329Z-kefir-rothia-model-record
  relationship: Current whole-record successor; all three original issue identities
    retained open with exact previous_occurrences.
links:
- https://github.com/CultureBotAI/CommunityMech/pull/2034
- https://github.com/CultureBotAI/CommunityMech/issues/2138
tags:
- pr-2034
- record-review
- isolate
- computational-model
```
