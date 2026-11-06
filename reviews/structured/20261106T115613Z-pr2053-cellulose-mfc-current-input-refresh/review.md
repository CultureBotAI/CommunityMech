# Cellulose MFC coculture: current taxon-link and source-scope refresh

- Review: 20261106T115613Z-pr2053-cellulose-mfc-current-input-refresh
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-11-06T11:44:11.968768Z
- Finished UTC: 2026-11-06T11:56:13.815708Z
- Reviewer: codex (self_review)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

The new reusable Geobacter link resolves to the correct species and preserves focal-system scope. Four existing curation findings remain open: metabolite/recipient-role evidence, CMC identity, study-specific cultivation, and strain/mapping provenance. Both primary full-text extractions are now read; unverified figure pixels and typography keep scientific completion partial. All eight focused native checks pass.

## Scope And Provenance

Entire current maintained record, three interaction nodes and one arrow; new common-taxon identity link, both fresh primary abstracts and publicly accessible complete article text/captions. Figure pixels, raw data and the reusable taxon's unrelated experimental claims are not certified.

Selection: The sole stale record identified in PR 2053 after merging current main.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 14116595da5faed13c3b4298cf4d63a078532fcf.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000175 | kb/communities/Clostridium_Cellulolyticum_Geobacter_Cellulose_MFC_Coculture.yaml | maintained | Clostridium cellulolyticum-Geobacter sulfurreducens Cellulose MFC Coculture |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000175 | Focused native command exit 0. |
| validate-strict | passed | True | CommunityMech:000175 | Focused native command exit 0. |
| validate-terms | passed | True | CommunityMech:000175 | Focused native command exit 0. |
| validate-gtdb | passed | True | CommunityMech:000175 | Focused native command exit 0. |
| validate-gtdb-domain | passed | True | CommunityMech:000175 | Focused native command exit 0. |
| validate-history | passed | True | CommunityMech:000175 | Focused native command exit 0. |
| normalize-cache-names-check | passed | True | CommunityMech:000175 | Focused native command exit 0. |
| validate-references-explained | passed | True | CommunityMech:000175 | Focused native command exit 0. |
| audit-network | failed | False | CommunityMech:000175 | Actual corpus warning-only diagnostic retained; no validator weakened. |
| check-network-quality | failed | False | CommunityMech:000175 | Actual corpus warning-only diagnostic retained; no validator weakened. |
| Claim-critical visual/source verification | unavailable | True | CommunityMech:000175 | Both main text extractions read; original figure pixels and ambiguous typography not verified. Partial scientific status retained. |
| Fresh reference-specific excerpts | passed | True | CommunityMech:000175 | All 28 abstract excerpt occurrences match; no current cache enrichment performed. |
| Identifier, schema and taxon-link scope | passed | True | CommunityMech:000175 | Encoded labels, species/type-material identity, exact crosswalk rows and new reusable link independently checked; semantic concerns retained. |
| Focal structured expression adapter | not_applicable | False | CommunityMech:000175 | No focal organism in the current public catalogue; this is not negative biological evidence. |
| Raw-data and experimental reproduction | skipped | False | CommunityMech:000175 | No raw-image, qPCR, current-trace, sequence or culture reanalysis. |

## Scientific And Domain Assessments

### Defined binary MFC and study boundaries

identity: supported. Targets: CommunityMech:000175.

The record denotes the intended laboratory pair.

SYNTHETIC origin, ENGINEERED state and BIOTECHNOLOGY category fit deliberate assembly. Activated-sludge mixed cultures, monoculture controls, cloning hosts and catalogue environments are excluded.

### Species, strains and GTDB provenance

grounding: concern. Targets: CommunityMech:000175.

Species identities are valid; exact 2008 culture and mapping provenance can be improved.

Both primary texts identify the same collection stocks; current species terms and the new reusable Geobacter identity link are consistent. Optional strain refinement must retain the species-versus-strain mapping denominators. The link does not import unrelated DIET/gene experiments into this community.

### Recipient roles and ordinal abundance

scope: concern. Targets: CommunityMech:000175.

Donor CROSS_FEEDER needs local recipient evidence; other supported roles and ordinals remain.

Improved CMC degradation or product removal does not identify a Geobacter product utilized by Clostridium. Retain PRIMARY_DEGRADER, Geobacter CROSS_FEEDER and broad SYNTROPHIC_PARTNER. ABUNDANT is not a fixed percentage; qPCR/FISH context may clarify it without inventing a numerical threshold.

### ecological_interactions[0]

graph: supported. Targets: CommunityMech:000175.

Qualified fermentation-to-anode-respiration CROSS_FEEDING is supported.

Keep the C. cellulolyticum to G. sulfurreducens direction and residual-pool caveats. No obligacy, reciprocal fitness, direct electron transfer or molecule-resolved flux is established.

### ecological_interactions[1]

graph: supported. Targets: CommunityMech:000175.

The untyped binary-current and degradation endpoint is appropriately bounded.

Negative pure-culture current controls and greater CMC degradation support functional complementarity. They do not independently identify a unique product-removal mechanism or reciprocal fitness.

### ecological_interactions[2]

graph: supported. Targets: CommunityMech:000175.

The untyped spatial observation preserves both substrate conditions.

Retain FISH/qPCR substrate and compartment scope without restoring a causal localization arrow or niche-partitioning claim. Text and captions were read; no figure pixels were independently assessed.

### ecological_interactions[0].downstream[0]

graph: supported. Targets: CommunityMech:000175.

The single retained supply-to-current arrow is appropriately qualified.

Preserve the functional conversion link. No additional edge is justified by localization observations or residual-metabolite identity alone.

### related_ingredients acetate and dihydrogen

consistency: concern. Targets: CommunityMech:000175.

Off-graph recipient-use wording exceeds its residual-pool evidence.

Apply the graph’s existing uncertainty to related_ingredients[1] and [3]. Keep ethanol as a residual intermediate; generic fermentation-product supply remains supported.

### growth_media[0].composition[0].chebi_term

grounding: concern. Targets: CommunityMech:000175.

CMC is a derivative and is not represented by unmodified cellulose.

The 2008 reagent is sodium CMC. Preserve derivative and salt scope without inventing substitution degree. Valid cellulose/MN301 graph and ingredient annotations should not be globally replaced.

### Medium, substrate arms and MFC operation

scope: concern. Targets: CommunityMech:000175.

Recoverable study-specific Methods should replace stale workflow prose while preserving distinct protocols.

Separate precursor cultures, final substrate arms, anode/catholyte compartments, capacity/working volume and study-specific power results. Both sources describe medium replacement. Author terminology does not override the native operation definition. The 2008 extraction's ambiguous glyphs require visual verification.

### Environment, processes and metal scope

grounding: supported. Targets: CommunityMech:000175.

Laboratory environment, source-qualified processes and metal categorization are appropriate.

Cellulose catabolism and fermentation describe the cellulolytic process; anode respiration is not thereby assigned the same process. Ferricyanide and trace nutrients do not establish a metal-processing purpose. Preserve NOT_APPLICABLE metal relevance.

### Claim-local excerpts and source accessibility

evidence: concern. Targets: CommunityMech:000175.

All 28 abstract excerpts match, but expanded claims require narrower support.

Both maintained caches remain correctly abstract-only; newly read complete public text extractions can support separately authorized evidence enrichment with precise provenance. Figure pixels and original PDF equivalence remain unverified; completion remains partial.

### External publications and dataset scope

representation: supported. Targets: CommunityMech:000175.

Both article links are correctly typed and identified.

No deposit is inferred from primer-design databases or catalogue records, and the empty dataset list creates no separate finding. No media or ingredient cross-Mech IDs are encoded.

### Prior review chain and current follow-up

provenance: supported. Targets: CommunityMech:000175.

The current common-taxon change and prior review lineage are reconciled without retiring unrelated findings.

Only the four original single-target findings receive previous_occurrences. The multi-target Cycle 2 link-gap dispositions and closed 2073 remain context; other affected communities are not reassessed. Open 1327 remains the curation owner.

### Native checks and source completion

schema: supported. Targets: CommunityMech:000175.

Eight focused native checks pass; scientific review remains partial.

Eight focused native gates pass. Corpus diagnostics retain 48 warnings/zero errors; target connectivity is complete. Full-source text access improved, but no figure-pixel certification or canonical change occurred.

### Native completeness and validation quality

completeness: supported. Targets: CommunityMech:000175.

Completeness 85; raw quality 111, capped 100.

## Findings

### qualify-metabolite-use: Qualify metabolite use and donor recipient-role claims

major / open / confirmed; issue key: cm-000175-qualify-metabolite-use.

The donor's optional CROSS_FEEDER role still lacks evidence of utilization of a Geobacter product. Ingredient assertions attach only a residual-metabolite snippet; strengthen their local source attribution or qualify the inferred molecule-specific transfer. Newly accessible main-text controls and author interpretations inform this repair without establishing partner-resolved flux or a reciprocal recipient role. Preserve the qualified graph.

### ground-cmc-derivative: Ground the CMC component as a chemical derivative

major / open / confirmed; issue key: cm-000175-ground-cmc-derivative.

growth_media[0].composition[0] names CMC but grounds it to CHEBI:18246, unsubstituted cellulose. Use a verified derivative identity and source-specific sodium-salt context. Keep valid generic cellulose and MN301 annotations; no global replacement or invented substitution degree.

### recover-study-protocol: Recover study-specific cultivation and evidence context

minor / open / confirmed; issue key: cm-000175-recover-study-protocol.

Current cultivation notes retain unrelated workflow history and unavailable-Methods statements. Both primary text extractions are now accessible. Recover study-specific preparation, substrate arms and apparatus without merging recipes, power values or compartments; distinguish author fed-batch terminology from medium replacement and native mode semantics.

### document-strain-mapping: Document source strains and reproducible mapping provenance

minor / open / confirmed; issue key: cm-000175-document-strain-mapping.

Both primary texts name exact culture stocks, while mapping_source still asserts a latest release/build date without sufficient provenance. Add source-specific strain context and the examined snapshot/method; preserve current species mappings and ordinal abundance. The newly added common_taxon link is valid and should remain.

## Recommended Actions And Acceptance Checks

### qualify-recipient-use

Align non-graph metabolite and role claims with their actual evidence.

- At related_ingredients[1].relevance and [3].relevance, distinguish residual acetate/hydrogen from inferred partner use and directly measured uptake. Attach exact source-local support for any stronger molecule-specific claim; do not turn absent uptake evidence into proof that uptake cannot occur.
- At taxonomy[0].functional_role, identify the other-taxon provider, metabolite and utilization evidence before retaining CROSS_FEEDER; otherwise omit or qualify this optional recipient role. Improved CMC conversion and donor fermentation alone do not establish it. No carbon/energy-only or obligacy requirement is imposed.
- Retain C. cellulolyticum PRIMARY_DEGRADER, Geobacter CROSS_FEEDER and broad SYNTROPHIC_PARTNER with source attribution. Preserve all three nodes and the single qualified arrow, residual-pool limits, untyped endpoints and lack of a localization-causality edge.

### ground-cmc

Correct only the derivative-specific medium identity.

- Replace the unmodified-cellulose grounding at growth_media[0].composition[0].chebi_term with verified CHEBI:85146 carboxymethylcellulose, or a separately justified exact sodium-salt grounding. The 2008 Methods explicitly says sodium CMC; CHEBI:234035 is a verified salt label with limited definition metadata. Preserve the distinction between chemical family and exact reagent.
- Keep CHEBI:18246 for MN301 and generic cellulose contexts. Both study texts name sodium CMC; do not infer a shared formulation, substitution degree or grade from another study or ambiguous extraction. Verify any proposed numerical reagent specification against the exact original.

### recover-protocol

Represent the two recovered protocols without merging study stages or compartments.

- Replace off-topic infant-HMO/#183/#543 and cache-size narrative in cultivation_setup[0].notes with biological study context. Retain the 2007 abstract as the source of 143/59.2 mW/m² and its author-described fed-batch tests; record 2008 power 153/83 separately if added.
- Represent 2008 sodium CMC and MN301 as alternative 1 g/L reactor arms. Recover the per-litre recipe from MFC inoculum, construction, and operation: NH4Cl 1.05 g, KCl 0.1 g, NaH2PO4·H2O 4.90 g, Na2HPO4 9.15 g, yeast extract 0.2 g, NaHCO3 2.5 g, and 10 mL each trace-mineral/vitamin mixtures. Preserve the cited but unverified stock recipes. Do not call this chemically defined sole-carbon medium.
- Record 310-mL bottle capacity only as capacity until working volume is verified; keep 16-cm² electrode geometry and ferricyanide/phosphate catholyte separate from anode medium. Catholyte pH 7.0 is not an anode pH setpoint, and external circuit resistance is not an applied potential. Do not transfer analytical or cloning-host conditions.
- Preserve the authors' fed-batch wording alongside actual medium/catholyte replacement. The 2007 text specifies complete replacement below 40 mV. Select a native mode from the literal operation; do not force FED_BATCH with broth removal, partial-harvest SEMI_CONTINUOUS or an unperformed settle/draw cycle. Keep the 2008 operation and proposed optimization distinct.
- Verify ambiguous 2008 degree/ohm/micro-unit glyphs against readable page images before numerical curation. The newly accessible 2007 text provides separate stage-specific Methods; do not copy the 2008 recipe into it. Preserve exact author-copy/source version and actual access limits if enriching caches. Update current access rationale without altering historical review receipts.

### document-taxonomy

Add exact strain context and verifiable GTDB provenance.

- Attach the independently inspected Methods from both studies and current NCBI type-material aliases for ATCC 35319/H10/DSM 5812 and ATCC 51573/PCA/DSM 12127. Preserve valid species terms and the resolved common_taxon link; optional strain refinement is not mandatory. Do not import unrelated reusable-gene mechanisms into the focal pair.
- Replace unverified latest/build-date text with the examined crosswalk hash and exact-ID route. Preserve NCBITaxon 1521 mapping 1.0/one genome and 35554 mapping 1.0/19. Optional 394503/243231 strain rows each have 1.0/two genomes and must remain separate from species support counts.
- Keep ordinal ABUNDANT. If adding abundance context, label substrate, compartment, time and FISH/qPCR method; gene-copy ratios are not universal cell fractions. Do not require percentages or silently reconcile qualitative FISH and quantitative sampling comparisons.

### verify-future-curation

Validate separately authorized curation and retain access boundaries.

- Both primary text extractions are now read. Before declaring complete scientific verification, inspect critical original figures and ambiguous typography, retain version/locator provenance and reassess any resulting interpretation changes. Do not treat a current abstract cache or a web response hash as original-PDF equivalence.
- Attach precise reference/section evidence to each changed field and preserve the current graph qualifications. After authorized canonical edits, append history and run schema, strict, terms, references, GTDB, domain and history checks, then just gen-html and just check-docs-current.
- Canonical YAML, caches, histories, schema and products remain unchanged in PR 2053. Save only the new immutable linked review and its reproducible helpers; obtain a separate read-only review of the committed head before merge.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | kb/communities/Clostridium_Cellulolyticum_Geobacter_Cellulose_MFC_Coculture.yaml; Entire current maintained YAML | supports | The only record delta since the original review is taxonomy[1].common_taxon and its append-only history. All four original concern areas remain unchanged. |
| delta | .temp/pr2053/175/initial-target-diff.stdout.txt; Historical input versus current main | supports | Exact diff contains the reusable taxon link and corresponding history entry; it does not alter graph, media, evidence, or species assignments. |
| common | kb/taxa/Geobacter_sulfurreducens.yaml; Identifier, taxon_term, PCA context, genes and curation history | supports | CommunityMech:taxon:000002 has the same Geobacter sulfurreducens NCBITaxon:35554 identity. Its other-community gene, DIET and assembly examples do not establish those mechanisms in the cellulose MFC. |
| abstracts | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=17695929,18725730&amp;retmode=xml; Two exact PMID/DOI/title records and complete primary abstracts | supports | The two records identify the exact binary MFC studies, distinguish the activated-sludge comparison, and support the source-specific current/degradation and spatial endpoints. |
| main-2007 | https://www.academia.edu/11977828/Electricity_production_from_cellulose_in_a_microbial_fuel_cell_using_a_defined_binary_culture; Public text extraction; full coverage is distributed across this snapshot and the separately pinned source-range receipts: Materials and Methods, Results, Discussion, Table 1, four captions and references; snapshot is the web-reader response, not original PDF bytes | supports | Both study stocks are named. The text reports complete medium/catholyte replacement, separate preparation and experimental stages, acetate controls and endpoint metabolite comparisons. Product-inhibition relief is the authors' interpretation; metabolite-specific partner flux and a Geobacter-derived resource consumed by Clostridium are not isolated. Figure pixels remain unverified. |
| main-2008 | https://www.academia.edu/11977824/Electricity_production_and_microbial_biofilm_characterization_in_cellulose_fed_microbial_fuel_cells; Public text extraction; full coverage is distributed across this snapshot and the separately pinned source-range receipts: Methods, Results/Discussion, five captions and references; snapshot is the web-reader response, not original PDF bytes | supports | The source separates CMC and MN301 reactors, anode and catholyte, source-specific medium and electrode geometry, FISH localization and qPCR gene-copy comparisons. The proposed settling/decanting improvement was not a tested causal perturbation. Extraction corrupts some degree, ohm and micro-unit glyphs; those values require independently readable rendering. |
| access | .temp/pr2053/175/web-primary-main.json; Public web-reader article extractions; separate direct-curl receipts retained; complete coverage requires both separately pinned source-range supplements | supports | Both complete article text extractions were inspected. Direct curl returned 403 challenge pages, not PDF or visual evidence. No original PDF equivalence or figure-pixel inspection is claimed. Earlier unavailable-2007 statements remain historical, not the current access assessment. |
| support | .temp/pr2053/175/support-final.json; Fresh abstract replay, native term labels, target graph and linked identity | supports | All 28 reference-specific abstract snippet occurrences match after NFKC/whitespace normalization; all 25 encoded ID-label occurrences match. Target graph is structurally COMPLETE. These checks do not establish biological entailment or correct CMC semantic identity. |
| cmc | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:85146; Current ChEBI derivative definition | supports | CHEBI:85146 is carboxymethylcellulose, a substituted cellulose derivative; CHEBI:18246 represents the unmodified backbone. Preserve generic cellulose and MN301 contexts. |
| cmc-salt | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:234035; Current label and available definition fields | supports | CHEBI:234035 is carboxymethylcellulose sodium salt. This response has no definition; source-specific reagent wording remains necessary. |
| taxa | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=1521,35554,394503,243231&amp;retmode=xml; Species, strain parents and type-material aliases | supports | Species 1521/35554 and strains 394503/243231 resolve consistently. Type-material aliases connect ATCC 35319, DSM 5812 and H10, and ATCC 51573, DSM 12127 and PCA. Catalogue maintenance is not the study protocol. |
| gtdb | .temp/pr2053/independent-secondary/gtdb-exact-rows.json; Independent current exact-ID crosswalk replay, with community-mode control | supports | Snapshot SHA256 761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd supports species counts 1 and 19 at majority 1.0. Optional strain rows each have two genomes. File mtime does not establish a release or build date. |
| schema | src/communitymech/schema/communitymech.yaml; FunctionalRoleEnum, InteractionTypeEnum, AbundanceEnum, CultivationModeEnum and common_taxon | supports | Recipient CROSS_FEEDER requires utilization; SYNTROPHY does not require obligacy. Ordinal ABUNDANT has no fixed percentage threshold. FED_BATCH excludes broth removal; the literal operation must determine mode. |
| history | .temp/pr2053/175/initial-lineage.json; Original four single-target findings and Cycle 2 multi-target link findings/remediation | supports | The prior single-target findings are reassessed explicitly. The later common-taxon remediation and closed issue 2073 are preserved; this narrower review does not supersede multi-target dispositions. |
| issues | .temp/pr2053/issue1327.json; Current issue body and all returned comments; other issue states separately pinned | supports | Issue 1327 remains open for non-graph curation. Closed 1324 preserves the graph repair; open 1744 explicitly retains this record's classification. No closure of these curation issues follows from this review. |
| inspection | .temp/pr2053/175/initial-inspection.json; Native current-input inspection using the current AGENTS rubric | supports | Initial target/context hashes were rechecked before adding current source, authority, check and helper pins. The final working-tree snapshot remains a reviewer byte attestation, not a claim that ignored research artifacts were committed. |
| adapter | https://imodulondb.org/api/datasets; Complete returned public organism catalogue | supports | No focal Geobacter or cellulolyticum organism match occurs in this catalogue. No expression-module evidence is used to infer focal phenotype or transfer. |
| source-175-missing-source-ranges | .temp/pr2053/adversarial/175-missing-source-ranges.json; Supplemental public-reader ranges, independently retrieved and author-read before final input freezing | supports | Together with web-primary-main.json these receipts cover all 79 lines of the 2007 extraction and all 60 lines of the 2008 extraction. They are parsed web responses, not original PDF bytes or figure pixels. |
| source-175-final-source-ranges | .temp/pr2053/adversarial/175-final-source-ranges.json; Supplemental public-reader ranges, independently retrieved and author-read before final input freezing | supports | Together with web-primary-main.json these receipts cover all 79 lines of the 2007 extraction and all 60 lines of the 2008 extraction. They are parsed web responses, not original PDF bytes or figure pixels. |
| source-175-extraction-coverage | .temp/pr2053/adversarial/175-extraction-coverage.json; Supplemental public-reader ranges, independently retrieved and author-read before final input freezing | supports | Together with web-primary-main.json these receipts cover all 79 lines of the 2007 extraction and all 60 lines of the 2008 extraction. They are parsed web responses, not original PDF bytes or figure pixels. |
| check-validate | .temp/pr2053/175/validate.json; Actual command, times, exit and output digests | supports | Focused native command and immutable output receipts. |
| check-validate-strict | .temp/pr2053/175/validate-strict.json; Actual command, times, exit and output digests | supports | Focused native command and immutable output receipts. |
| check-validate-terms | .temp/pr2053/175/validate-terms.json; Actual command, times, exit and output digests | supports | Focused native command and immutable output receipts. |
| check-validate-gtdb | .temp/pr2053/175/validate-gtdb.json; Actual command, times, exit and output digests | supports | Focused native command and immutable output receipts. |
| check-validate-gtdb-domain | .temp/pr2053/175/validate-gtdb-domain.json; Actual command, times, exit and output digests | supports | Focused native command and immutable output receipts. |
| check-validate-history | .temp/pr2053/175/validate-history.json; Actual command, times, exit and output digests | supports | Focused native command and immutable output receipts. |
| check-normalize-cache-names-check | .temp/pr2053/175/normalize-cache-names-check.json; Actual command, times, exit and output digests | supports | Focused native command and immutable output receipts. |
| check-validate-references-explained | .temp/pr2053/175/validate-references-explained.json; Actual command, times, exit and output digests | supports | Focused native command and immutable output receipts. |
| check-audit-network | .temp/pr2053/175/audit-network.json; Actual command, times, exit and output digests | supports | Corpus diagnostic: 48 warnings, zero errors across 17/510 records; target-specific graph has no issue. |
| check-check-network-quality | .temp/pr2053/175/check-network-quality.json; Actual command, times, exit and output digests | supports | Corpus diagnostic: 48 warnings, zero errors across 17/510 records; target-specific graph has no issue. |

## Limits And Additional Notes

- Complete public author-copy text extractions, captions and references for both focal papers were read. Direct curl requests returned 403 challenge HTML. No original PDF byte equivalence, figure pixels or raw data were verified; scientific completion remains partial.
- The two-column extraction has ambiguous scientific glyphs and interleaved layout, particularly in the 2008 article. Do not silently normalize uncertain units or import measurements across studies, stages or compartments.
- Bulk residual pools, current/degradation comparisons and the authors' product-removal interpretation do not quantify molecule-specific partner flux or establish a metabolite utilized by the cellulolytic donor. No obligacy test is required to use the repository's syntrophy semantics.
- The new common_taxon link is assessed for identity and scope. Generic gene, assembly and other-community DIET claims in the reusable record are not independently certified as focal cellulose-MFC evidence.
- Both original caches remain abstract-only and all 28 current snippets match fresh reference-specific abstracts. Neither the caches nor the canonical history was enriched or rewritten.
- Corpus network diagnostics return exit 1 for 48 warnings/zero errors across 17/510 records; this target has no structural network issue. Native presence/validation scores do not certify the science.
- Only the original four single-target findings are superseded as continuing open observations. Multi-target Cycle 2 dispositions and other communities remain outside this review's adjudication scope.
- Two major and two minor findings remain open; completeness 85 and validation quality 100 (raw 111) retain their documented native formulas.
- The new record hash includes the valid common-taxon link/history. Source access has improved relative to the original review; no unavailable historical scratch file was recovered or invented.
- All helper scripts feeding this result are versioned under scripts/adhoc. Ignored source receipts are frozen working-tree attestations, not committed source bodies.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261106T115613Z-pr2053-cellulose-mfc-current-input-refresh
kind: record
repository: CultureBotAI/CommunityMech
title: 'Cellulose MFC coculture: current taxon-link and source-scope refresh'
started_at: '2026-11-06T11:44:11.968768Z'
finished_at: '2026-11-06T11:56:13.815708Z'
reviewer:
  identity: codex
  kind: agent
  independence: self_review
  independence_basis: Author refresh of PR 2053's stale record 175 observation. A
    separate read-only adversarial pass evaluates the committed result; this bundle
    does not claim independent approval.
skill: review-yaml-record
completion: partial
verdict: needs_curation
scientific_review: false
summary: 'The new reusable Geobacter link resolves to the correct species and preserves
  focal-system scope. Four existing curation findings remain open: metabolite/recipient-role
  evidence, CMC identity, study-specific cultivation, and strain/mapping provenance.
  Both primary full-text extractions are now read; unverified figure pixels and typography
  keep scientific completion partial. All eight focused native checks pass.'
source:
  git_revision: 14116595da5faed13c3b4298cf4d63a078532fcf
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
  - path: .temp/pr2053/175/CHEBI18246.json
    sha256: b8496e279cdd9da6284e444e86d967da09fde803756b9307c7acb53504af9f6b
    role: context
  - path: .temp/pr2053/175/CHEBI18246.json.receipt.json
    sha256: 7887827c95cf999b04f51e4fcbb5bc47e1a9f44858620acca0da978cc9fb42c4
    role: context
  - path: .temp/pr2053/175/CHEBI234035.json
    sha256: 06a31711d40294ccbde1dea1688e3638cc7593210387e655027b3792bd884722
    role: context
  - path: .temp/pr2053/175/CHEBI234035.json.receipt.json
    sha256: 1def50419879aa0bea7b9e87bd2a8d66a2de4ad28c83c39674ed9daae64d0d3c
    role: context
  - path: .temp/pr2053/175/CHEBI85146.json
    sha256: e9d98930edc9fa9057a20f6886f4cf45f8512ce889fe32b4d7355db321d09571
    role: context
  - path: .temp/pr2053/175/CHEBI85146.json.receipt.json
    sha256: ee4138509dde95a4f327c675fc76016437f8d0f9799b4cf6c199abfe8310006d
    role: context
  - path: .temp/pr2053/175/academia-2007.html
    sha256: 9315743b01c00726b95ea73dd8413d7f37da9112833560b2e52fe45e38667a13
    role: context
  - path: .temp/pr2053/175/academia-2007.html.receipt.json
    sha256: 0875bd856886ac7177e57297db39f6341029fa38fe4ed3663355b4a7cf3a7241
    role: context
  - path: .temp/pr2053/175/academia-2008.html
    sha256: b0d1e94a409a2e1d3864d264e2e0c85d906ddb9a3b4733c1c6f25f4d54eb038e
    role: context
  - path: .temp/pr2053/175/academia-2008.html.receipt.json
    sha256: 7b19cbc4bdc475372b5ea634e7020f0347867749fa66af3d77668c4e50ac9b69
    role: context
  - path: .temp/pr2053/175/audit-network.json
    sha256: 1223179f1c952fa93f2344d0d88760497c97005f159591ee8337602ac4919f1d
    role: context
  - path: .temp/pr2053/175/audit-network.stderr.txt
    sha256: a71fb29e950f3eaf0eb2b834a43c59d4a1b6aa85a2a89473ae99b0e408a27a36
    role: context
  - path: .temp/pr2053/175/audit-network.stdout.txt
    sha256: 1f337893714a80173f5b305ba0c11da1d8a3caf53f1060bd5acf2aa42b40aece
    role: context
  - path: .temp/pr2053/175/check-network-quality.json
    sha256: 87c26873c41961dc15e6a70764907d1d0f9e9012e4a4f95e515f1d88982191ca
    role: context
  - path: .temp/pr2053/175/check-network-quality.stderr.txt
    sha256: e060873ec46d56a6fddbc2fe78b0d2f1438639923dd9f410686090ae4efa3aa3
    role: context
  - path: .temp/pr2053/175/check-network-quality.stdout.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2053/175/epmc-175.json
    sha256: 9237ca3b69d2e95e943a790ae6ab8d1c4bc8e60783f9777da1d8cab97fe39c0e
    role: context
  - path: .temp/pr2053/175/epmc-175.json.receipt.json
    sha256: 6c3e08185b239f0044ed1ad75008b41e9d434bb45df005562075250d8cebb1c5
    role: context
  - path: .temp/pr2053/175/imodulon-catalog.json
    sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
    role: context
  - path: .temp/pr2053/175/imodulon-catalog.json.receipt.json
    sha256: d15dc2477f70f96194fd2ccc36dc9db68bed7fb8c8c759d4238f1a9ad9729705
    role: context
  - path: .temp/pr2053/175/initial-frozen-target.stdout.txt
    sha256: bafb8c0e58150b2e586e92c84725b0e3ad88001a64c2d1acb1d2889ede2810b3
    role: context
  - path: .temp/pr2053/175/initial-inspect.json
    sha256: f5d4eb9b3fb70470579201486a66ac7c1c5e367cf1f8984294e5f9964f7f3413
    role: context
  - path: .temp/pr2053/175/initial-inspection.json
    sha256: d1992d55cee5decffeb8ba02e5fec5544e02f4d580553a24454b318f317e9333
    role: context
  - path: .temp/pr2053/175/initial-lineage.json
    sha256: 81be7a3dcf5e4c67eeec0720772cbc02dd0f72c1f92ad5d88a3a453afab09dd6
    role: context
  - path: .temp/pr2053/175/initial-local-search.stdout.txt
    sha256: 38795119fcb013c42341008ce00fde2de105c3924bccfc546f491b6c93f441b5
    role: context
  - path: .temp/pr2053/175/initial-target-diff.stdout.txt
    sha256: 3456a0951d095ac6120c3d6bede7038c8382b59b087c09aea8c01ba8d09ee526
    role: context
  - path: .temp/pr2053/175/initial-targets.json
    sha256: 37d81534768a0d1b0da603575da0b78a6135d0cb15beea2410083005ff8edb5c
    role: context
  - path: .temp/pr2053/175/normalize-cache-names-check.json
    sha256: 6080f7c0d95fd0e87d0b7092c1900b3d7e4dbad830e53cce6c5bc333700d571d
    role: context
  - path: .temp/pr2053/175/normalize-cache-names-check.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2053/175/normalize-cache-names-check.stdout.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2053/175/pubmed-175.xml
    sha256: eebf99bf67d1db6f5b41276f3b60c5e0e1163ab32490ea3b71a50da6d6be91ad
    role: context
  - path: .temp/pr2053/175/pubmed-175.xml.receipt.json
    sha256: 3e3fd3903fdbb2fa9f08e0327daa4562c17164c95b79bd970ac2b67b583791f1
    role: context
  - path: .temp/pr2053/175/strict.tsv
    sha256: b184ed5450b968070bb6c75648407e388f41a1eaf7017890723cf560999fc3f7
    role: context
  - path: .temp/pr2053/175/support-final.json
    sha256: 983227be36af24abcb94c7d408becd46b3f8f26391b2803fbd7fdc7f7840a6d4
    role: context
  - path: .temp/pr2053/175/taxonomy-175.xml
    sha256: c74b5ea69fb2703fee57afb420ec821c1d4e2480f7f5f7ff39844e5c409505f8
    role: context
  - path: .temp/pr2053/175/taxonomy-175.xml.receipt.json
    sha256: 2e9975c6071c57b51f642219a5e1dc372fdef979725622eee1b4521a9d32d9a5
    role: context
  - path: .temp/pr2053/175/validate-gtdb-domain.json
    sha256: 8e44b64172c4b429fe73b20b3ee20320796f38b81afad1829cbbc81fa7e88676
    role: context
  - path: .temp/pr2053/175/validate-gtdb-domain.stderr.txt
    sha256: 525b04df0e9c6a00b8644265a5a95928ddc0f3e7ecbd5a2d33c08482065bb472
    role: context
  - path: .temp/pr2053/175/validate-gtdb-domain.stdout.txt
    sha256: ede937293c42cad366f434dce49a485a9a0c56fe86620b52ca243ad10e09ecae
    role: context
  - path: .temp/pr2053/175/validate-gtdb.json
    sha256: 5d65db3436f375af7f254116d4da72084e609cf7c252c397d9b8f43daab13822
    role: context
  - path: .temp/pr2053/175/validate-gtdb.stderr.txt
    sha256: 5e9b14a1f795835a7b62dfae98aefccb053a28e66c06506243191e618c92f422
    role: context
  - path: .temp/pr2053/175/validate-gtdb.stdout.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2053/175/validate-history.json
    sha256: 9b25b4c5aebbaded8044ac2b589558b5fb868de9099f8369cb4ad7cac3941b4e
    role: context
  - path: .temp/pr2053/175/validate-history.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2053/175/validate-history.stdout.txt
    sha256: de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
    role: context
  - path: .temp/pr2053/175/validate-references-explained.json
    sha256: 8c238d6f58c3b8b0cb0b71452e95a16bd6b88a613fce9568ae34f0af54eba4b0
    role: context
  - path: .temp/pr2053/175/validate-references-explained.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2053/175/validate-references-explained.stdout.txt
    sha256: 7692fecd80f3af5c75d5cda96c2c1f9922756ec5754ce6521133ab0823691630
    role: context
  - path: .temp/pr2053/175/validate-strict.json
    sha256: cd1e147f4655a718677cac2e936c2837a9e655b79c4d1f3fd6f167f43def8fb1
    role: context
  - path: .temp/pr2053/175/validate-strict.stderr.txt
    sha256: 57290124eb5b8d75bbd4dac6bdada1f08dd0878ae6c2ea13c32ad9ef80db9b65
    role: context
  - path: .temp/pr2053/175/validate-strict.stdout.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2053/175/validate-terms.json
    sha256: 755834859519f24e379d46b107da65ef23c878164a02c3fbd95b74bf7b206a61
    role: context
  - path: .temp/pr2053/175/validate-terms.stderr.txt
    sha256: d029df15e7a674881eac68d22128708ede99e45d9e72618b7cf82b196f48e5ca
    role: context
  - path: .temp/pr2053/175/validate-terms.stdout.txt
    sha256: 23acda1c1d3194d12bc947d897d07de83f4a076a9d93c135148885108530e018
    role: context
  - path: .temp/pr2053/175/validate.json
    sha256: a931de9e95ead07d773b892a25fe60af986b087f8327331f49745de055f4d6ec
    role: context
  - path: .temp/pr2053/175/validate.stderr.txt
    sha256: 87014fa0ab041639bbefac139b351d13718f955796867ed89a2a4e2d410051f2
    role: context
  - path: .temp/pr2053/175/validate.stdout.txt
    sha256: de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
    role: context
  - path: .temp/pr2053/175/web-primary-main.json
    sha256: 1aeb4b4a6c6b5fef2c1a1ce3a557a45272c6c247a335004818c6e33c230e8200
    role: context
  - path: .temp/pr2053/adversarial/175-extraction-coverage.json
    sha256: 0c747f45b03aac3a67f0e4fffcc017d05c8be9c90915a1aa160031d332b1268d
    role: context
  - path: .temp/pr2053/adversarial/175-final-source-ranges.json
    sha256: 3d13cefc160e52f8d2655d161a9317ff7225ab0bb227fd39f8d9b9eaf57150f7
    role: context
  - path: .temp/pr2053/adversarial/175-missing-source-ranges.json
    sha256: 899a2234a8895537c404a51d9c64e665b9d5a2ea075b811f7598b0d8edefeefa
    role: context
  - path: .temp/pr2053/independent-secondary/175-gtdb-authority.txt
    sha256: 0f573b74f59852d1a2c4af60bf92317ae70d3c76c6dcaaee4baee5da51e6255d
    role: context
  - path: .temp/pr2053/independent-secondary/gtdb-community-mode.json
    sha256: b5b0422faf3d1e0c64e08392ad4edbb902dd5fd9f8e14eaf636bb9c23bd5325f
    role: context
  - path: .temp/pr2053/independent-secondary/gtdb-exact-rows.json
    sha256: 83aa24abdb988107a7ffcfae691b39c76ff454137b2ba263317ea51032cee289
    role: context
  - path: .temp/pr2053/issue1324.json
    sha256: 9a46bdd3e7977e3568c79da7858a0a5f8dc03ecb592f4dd8fe07eae66a44cfe0
    role: context
  - path: .temp/pr2053/issue1327.json
    sha256: 4059a49977b3b124625b569c1740d7b62be5685bb695fd221ba3bbc3e6ca96fe
    role: context
  - path: .temp/pr2053/issue1744.json
    sha256: 58d91bae966ccc4916efe2082f1402288974c39812b011160467a7bc4e444ae2
    role: context
  - path: .temp/pr2053/issue2073.json
    sha256: 1c1b7507db7b6016cd67cfc29307f6f56a8ec8748bad689cc94cc2bd8940bb18
    role: context
  - path: .temp/pr2053/staleness.json
    sha256: ef3e28c02bf3f93dd58956b95a40c7a2acbdc895af47e0a66b9e5d86301f84a5
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
  - path: history/records/Clostridium_Cellulolyticum_Geobacter_Cellulose_MFC_Coculture/2026-10-05T234230Z-codex-ce1a08.yaml
    sha256: 8150812414eb1d2848f41aa078bea972aca0c7e78c50c2b06bfb58588d5fec12
    role: context
  - path: history/records/Clostridium_Cellulolyticum_Geobacter_Cellulose_MFC_Coculture/2026-10-25T151200Z-antigravity-2073.yaml
    sha256: 8f503e8fb3314ad3ec588a5cf78fd75556c2508e1bbdaf423b42823fd6ac7940
    role: context
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: kb/communities/Clostridium_Cellulolyticum_Geobacter_Cellulose_MFC_Coculture.yaml
    sha256: 20a878c274695f48d5ad4fd8fe4475e576d4210926f3a9cb901ff85001bf3eff
    role: target
  - path: kb/taxa/Geobacter_sulfurreducens.yaml
    sha256: bbf7fd94c91da0e099b05a8f48aec4d8904c09453ab15f41d4dec9845fd606ab
    role: context
  - path: references_cache/PMID_17695929.md
    sha256: 0a6d3e9ad135d3fe881f76e15e22b3e279efa320996df6bb82d2b598a2f07c87
    role: context
  - path: references_cache/PMID_18725730.md
    sha256: 474fa53897b2d368427ee153d7dca517de6deb0a4282fda7c8c68d52e4b7b5d3
    role: context
  - path: reports/causal_graph_review/adversarial-review-20261005-batch19.yaml
    sha256: 08d6f18b92836076a26b7aad98a6bfdbfbcfcea4a27124ead6d0546fa7b0e70b
    role: context
  - path: reports/causal_graph_review/adversarial-review-20261007-batch91.yaml
    sha256: 973b2a59f1e53a1bb9405f813af5a20a8593a8f4efb1837e4fa847772636105e
    role: context
  - path: reports/causal_graph_review/decisions/20261005-three-records-batch19.yaml
    sha256: 2f4684d88aa8b70f6ed84c0726aadad8dfb5f1b31c8a2e93b5f682264da69490
    role: context
  - path: reports/causal_graph_review/decisions/20261007-five-records-batch91.yaml
    sha256: 55c2dafc3c10346c37f864ef5acc1fdadefd37967c51f21696eef562a0296bbe
    role: context
  - path: reviews/structured/20261021T212006Z-cellulose-mfc-record-review/review.yaml
    sha256: 00a6c6be998259f31c5cb26666cac3775d22c9cf643596ea958eeb5c53a5f1c0
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
  - path: scripts/adhoc/pr2053_175_audit.py
    sha256: 44dca4fd61b35b9ecf7ab07b472e7fe05f299dac1deaae412453ae1987da4e73
    role: context
  - path: scripts/adhoc/pr2053_175_review.py
    sha256: a3008543f7ca3f0e3dcf2ebefff43d3f4a93b0d47b343c6da552087daeb1f89c
    role: context
  - path: scripts/adhoc/pr2053_175_support.py
    sha256: 5c698f976dce0ad687298243495e388eec5c549648222822831530bca5b8d2a2
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
    sha256: 7355e14f0f17c5d3b875abd33af6474ddc1aad08cc3305313686fede337e259a
    role: context
  - path: src/communitymech/schema/history.yaml
    sha256: b01b06f1b9a37db205c26c31ec0fd910690848507c7e1bfb73b424ac0829c52d
    role: context
  - path: src/communitymech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
targets:
- target_id: CommunityMech:000175
  path: kb/communities/Clostridium_Cellulolyticum_Geobacter_Cellulose_MFC_Coculture.yaml
  label: Clostridium cellulolyticum-Geobacter sulfurreducens Cellulose MFC Coculture
  kind: maintained
  record_class: MicrobialCommunity
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Clostridium_Cellulolyticum_Geobacter_Cellulose_MFC_Coculture.yaml
    role: canonical_record
scope:
  description: Entire current maintained record, three interaction nodes and one arrow;
    new common-taxon identity link, both fresh primary abstracts and publicly accessible
    complete article text/captions. Figure pixels, raw data and the reusable taxon's
    unrelated experimental claims are not certified.
  selection: The sole stale record identified in PR 2053 after merging current main.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000175
checks:
- check_id: validate
  name: validate
  status: passed
  required: true
  command: just --no-dotenv validate kb/communities/Clostridium_Cellulolyticum_Geobacter_Cellulose_MFC_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - CommunityMech:000175
  evidence_ids:
  - check-validate
  summary: Focused native command exit 0.
  scope_note: Current record-only gate.
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  command: just --no-dotenv validate-strict kb/communities/Clostridium_Cellulolyticum_Geobacter_Cellulose_MFC_Coculture.yaml
    --out /Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2053-batch11/.temp/pr2053/175/strict.tsv
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - CommunityMech:000175
  evidence_ids:
  - check-validate-strict
  summary: Focused native command exit 0.
  scope_note: Current record-only gate.
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  command: just --no-dotenv validate-terms kb/communities/Clostridium_Cellulolyticum_Geobacter_Cellulose_MFC_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - CommunityMech:000175
  evidence_ids:
  - check-validate-terms
  summary: Focused native command exit 0.
  scope_note: Current record-only gate.
- check_id: validate-gtdb
  name: validate-gtdb
  status: passed
  required: true
  command: just --no-dotenv validate-gtdb kb/communities/Clostridium_Cellulolyticum_Geobacter_Cellulose_MFC_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - CommunityMech:000175
  evidence_ids:
  - check-validate-gtdb
  summary: Focused native command exit 0.
  scope_note: Current record-only gate.
- check_id: validate-gtdb-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  command: just --no-dotenv validate-gtdb-domain kb/communities/Clostridium_Cellulolyticum_Geobacter_Cellulose_MFC_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - CommunityMech:000175
  evidence_ids:
  - check-validate-gtdb-domain
  summary: Focused native command exit 0.
  scope_note: Current record-only gate.
- check_id: validate-history
  name: validate-history
  status: passed
  required: true
  command: just --no-dotenv validate-history history/records/Clostridium_Cellulolyticum_Geobacter_Cellulose_MFC_Coculture
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - CommunityMech:000175
  evidence_ids:
  - check-validate-history
  summary: Focused native command exit 0.
  scope_note: Current record-only gate.
- check_id: normalize-cache-names-check
  name: normalize-cache-names-check
  status: passed
  required: true
  command: uv run python scripts/normalize_cache_names.py --check
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - CommunityMech:000175
  evidence_ids:
  - check-normalize-cache-names-check
  summary: Focused native command exit 0.
  scope_note: Current record-only gate.
- check_id: validate-references-explained
  name: validate-references-explained
  status: passed
  required: true
  command: just --no-dotenv validate-references-explained kb/communities/Clostridium_Cellulolyticum_Geobacter_Cellulose_MFC_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - CommunityMech:000175
  evidence_ids:
  - check-validate-references-explained
  summary: Focused native command exit 0.
  scope_note: Current record-only gate.
- check_id: audit-network
  name: audit-network
  status: failed
  required: false
  command: just --no-dotenv audit-network
  exit_code: 1
  expected_exit_code: 0
  target_ids:
  - CommunityMech:000175
  evidence_ids:
  - check-audit-network
  summary: Actual corpus warning-only diagnostic retained; no validator weakened.
  scope_note: Corpus diagnostic, not a new all-record scientific assessment.
- check_id: check-network-quality
  name: check-network-quality
  status: failed
  required: false
  command: just --no-dotenv check-network-quality
  exit_code: 1
  expected_exit_code: 0
  target_ids:
  - CommunityMech:000175
  evidence_ids:
  - check-check-network-quality
  summary: Actual corpus warning-only diagnostic retained; no validator weakened.
  scope_note: Corpus diagnostic, not a new all-record scientific assessment.
- check_id: scientific-source
  name: Claim-critical visual/source verification
  status: unavailable
  required: true
  summary: Both main text extractions read; original figure pixels and ambiguous typography
    not verified. Partial scientific status retained.
  target_ids:
  - CommunityMech:000175
  evidence_ids:
  - main-2007
  - main-2008
  - access
- check_id: direct-excerpts
  name: Fresh reference-specific excerpts
  status: passed
  required: true
  summary: All 28 abstract excerpt occurrences match; no current cache enrichment
    performed.
  target_ids:
  - CommunityMech:000175
  evidence_ids:
  - support
- check_id: authority-review
  name: Identifier, schema and taxon-link scope
  status: passed
  required: true
  summary: Encoded labels, species/type-material identity, exact crosswalk rows and
    new reusable link independently checked; semantic concerns retained.
  target_ids:
  - CommunityMech:000175
  evidence_ids:
  - support
  - taxa
  - gtdb
  - cmc
  - cmc-salt
  - schema
  - common
- check_id: adapter
  name: Focal structured expression adapter
  status: not_applicable
  required: false
  summary: No focal organism in the current public catalogue; this is not negative
    biological evidence.
  target_ids:
  - CommunityMech:000175
  evidence_ids:
  - adapter
- check_id: reanalysis
  name: Raw-data and experimental reproduction
  status: skipped
  required: false
  summary: No raw-image, qPCR, current-trace, sequence or culture reanalysis.
  target_ids:
  - CommunityMech:000175
  evidence_ids:
  - access
evidence:
- evidence_id: record
  kind: record_content
  reference: kb/communities/Clostridium_Cellulolyticum_Geobacter_Cellulose_MFC_Coculture.yaml
  locator: Entire current maintained YAML
  summary: The only record delta since the original review is taxonomy[1].common_taxon
    and its append-only history. All four original concern areas remain unchanged.
  support: supports
  accessed_at: '2026-11-06T11:56:13.814550Z'
  snapshot_sha256: 20a878c274695f48d5ad4fd8fe4475e576d4210926f3a9cb901ff85001bf3eff
- evidence_id: delta
  kind: validation
  reference: .temp/pr2053/175/initial-target-diff.stdout.txt
  locator: Historical input versus current main
  summary: Exact diff contains the reusable taxon link and corresponding history entry;
    it does not alter graph, media, evidence, or species assignments.
  support: supports
  accessed_at: '2026-11-06T11:56:13.814587Z'
  snapshot_sha256: 3456a0951d095ac6120c3d6bede7038c8382b59b087c09aea8c01ba8d09ee526
- evidence_id: common
  kind: record_content
  reference: kb/taxa/Geobacter_sulfurreducens.yaml
  locator: Identifier, taxon_term, PCA context, genes and curation history
  summary: CommunityMech:taxon:000002 has the same Geobacter sulfurreducens NCBITaxon:35554
    identity. Its other-community gene, DIET and assembly examples do not establish
    those mechanisms in the cellulose MFC.
  support: supports
  accessed_at: '2026-11-06T11:56:13.814619Z'
  snapshot_sha256: bbf7fd94c91da0e099b05a8f48aec4d8904c09453ab15f41d4dec9845fd606ab
- evidence_id: abstracts
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=17695929,18725730&retmode=xml
  locator: Two exact PMID/DOI/title records and complete primary abstracts
  summary: The two records identify the exact binary MFC studies, distinguish the
    activated-sludge comparison, and support the source-specific current/degradation
    and spatial endpoints.
  support: supports
  accessed_at: '2026-11-06T11:56:13.814651Z'
  snapshot_sha256: eebf99bf67d1db6f5b41276f3b60c5e0e1163ab32490ea3b71a50da6d6be91ad
- evidence_id: main-2007
  kind: primary_source
  reference: https://www.academia.edu/11977828/Electricity_production_from_cellulose_in_a_microbial_fuel_cell_using_a_defined_binary_culture
  locator: 'Public text extraction; full coverage is distributed across this snapshot
    and the separately pinned source-range receipts: Materials and Methods, Results,
    Discussion, Table 1, four captions and references; snapshot is the web-reader
    response, not original PDF bytes'
  summary: Both study stocks are named. The text reports complete medium/catholyte
    replacement, separate preparation and experimental stages, acetate controls and
    endpoint metabolite comparisons. Product-inhibition relief is the authors' interpretation;
    metabolite-specific partner flux and a Geobacter-derived resource consumed by
    Clostridium are not isolated. Figure pixels remain unverified.
  support: supports
  accessed_at: '2026-11-06T11:56:13.814679Z'
  snapshot_sha256: 1aeb4b4a6c6b5fef2c1a1ce3a557a45272c6c247a335004818c6e33c230e8200
- evidence_id: main-2008
  kind: primary_source
  reference: https://www.academia.edu/11977824/Electricity_production_and_microbial_biofilm_characterization_in_cellulose_fed_microbial_fuel_cells
  locator: 'Public text extraction; full coverage is distributed across this snapshot
    and the separately pinned source-range receipts: Methods, Results/Discussion,
    five captions and references; snapshot is the web-reader response, not original
    PDF bytes'
  summary: The source separates CMC and MN301 reactors, anode and catholyte, source-specific
    medium and electrode geometry, FISH localization and qPCR gene-copy comparisons.
    The proposed settling/decanting improvement was not a tested causal perturbation.
    Extraction corrupts some degree, ohm and micro-unit glyphs; those values require
    independently readable rendering.
  support: supports
  accessed_at: '2026-11-06T11:56:13.814712Z'
  snapshot_sha256: 1aeb4b4a6c6b5fef2c1a1ce3a557a45272c6c247a335004818c6e33c230e8200
- evidence_id: access
  kind: validation
  reference: .temp/pr2053/175/web-primary-main.json
  locator: Public web-reader article extractions; separate direct-curl receipts retained;
    complete coverage requires both separately pinned source-range supplements
  summary: Both complete article text extractions were inspected. Direct curl returned
    403 challenge pages, not PDF or visual evidence. No original PDF equivalence or
    figure-pixel inspection is claimed. Earlier unavailable-2007 statements remain
    historical, not the current access assessment.
  support: supports
  accessed_at: '2026-11-06T11:56:13.814756Z'
  snapshot_sha256: 1aeb4b4a6c6b5fef2c1a1ce3a557a45272c6c247a335004818c6e33c230e8200
- evidence_id: support
  kind: validation
  reference: .temp/pr2053/175/support-final.json
  locator: Fresh abstract replay, native term labels, target graph and linked identity
  summary: All 28 reference-specific abstract snippet occurrences match after NFKC/whitespace
    normalization; all 25 encoded ID-label occurrences match. Target graph is structurally
    COMPLETE. These checks do not establish biological entailment or correct CMC semantic
    identity.
  support: supports
  accessed_at: '2026-11-06T11:56:13.814787Z'
  snapshot_sha256: 983227be36af24abcb94c7d408becd46b3f8f26391b2803fbd7fdc7f7840a6d4
- evidence_id: cmc
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:85146
  locator: Current ChEBI derivative definition
  summary: CHEBI:85146 is carboxymethylcellulose, a substituted cellulose derivative;
    CHEBI:18246 represents the unmodified backbone. Preserve generic cellulose and
    MN301 contexts.
  support: supports
  accessed_at: '2026-11-06T11:56:13.814816Z'
  snapshot_sha256: e9d98930edc9fa9057a20f6886f4cf45f8512ce889fe32b4d7355db321d09571
- evidence_id: cmc-salt
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:234035
  locator: Current label and available definition fields
  summary: CHEBI:234035 is carboxymethylcellulose sodium salt. This response has no
    definition; source-specific reagent wording remains necessary.
  support: supports
  accessed_at: '2026-11-06T11:56:13.814838Z'
  snapshot_sha256: 06a31711d40294ccbde1dea1688e3638cc7593210387e655027b3792bd884722
- evidence_id: taxa
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1521,35554,394503,243231&retmode=xml
  locator: Species, strain parents and type-material aliases
  summary: Species 1521/35554 and strains 394503/243231 resolve consistently. Type-material
    aliases connect ATCC 35319, DSM 5812 and H10, and ATCC 51573, DSM 12127 and PCA.
    Catalogue maintenance is not the study protocol.
  support: supports
  accessed_at: '2026-11-06T11:56:13.814856Z'
  snapshot_sha256: c74b5ea69fb2703fee57afb420ec821c1d4e2480f7f5f7ff39844e5c409505f8
- evidence_id: gtdb
  kind: authority
  reference: .temp/pr2053/independent-secondary/gtdb-exact-rows.json
  locator: Independent current exact-ID crosswalk replay, with community-mode control
  summary: Snapshot SHA256 761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd
    supports species counts 1 and 19 at majority 1.0. Optional strain rows each have
    two genomes. File mtime does not establish a release or build date.
  support: supports
  accessed_at: '2026-11-06T11:56:13.814877Z'
  snapshot_sha256: 83aa24abdb988107a7ffcfae691b39c76ff454137b2ba263317ea51032cee289
- evidence_id: schema
  kind: authority
  reference: src/communitymech/schema/communitymech.yaml
  locator: FunctionalRoleEnum, InteractionTypeEnum, AbundanceEnum, CultivationModeEnum
    and common_taxon
  summary: Recipient CROSS_FEEDER requires utilization; SYNTROPHY does not require
    obligacy. Ordinal ABUNDANT has no fixed percentage threshold. FED_BATCH excludes
    broth removal; the literal operation must determine mode.
  support: supports
  accessed_at: '2026-11-06T11:56:13.814900Z'
  snapshot_sha256: 7355e14f0f17c5d3b875abd33af6474ddc1aad08cc3305313686fede337e259a
- evidence_id: history
  kind: prior_review
  reference: .temp/pr2053/175/initial-lineage.json
  locator: Original four single-target findings and Cycle 2 multi-target link findings/remediation
  summary: The prior single-target findings are reassessed explicitly. The later common-taxon
    remediation and closed issue 2073 are preserved; this narrower review does not
    supersede multi-target dispositions.
  support: supports
  accessed_at: '2026-11-06T11:56:13.814973Z'
  snapshot_sha256: 81be7a3dcf5e4c67eeec0720772cbc02dd0f72c1f92ad5d88a3a453afab09dd6
- evidence_id: issues
  kind: prior_review
  reference: .temp/pr2053/issue1327.json
  locator: Current issue body and all returned comments; other issue states separately
    pinned
  summary: Issue 1327 remains open for non-graph curation. Closed 1324 preserves the
    graph repair; open 1744 explicitly retains this record's classification. No closure
    of these curation issues follows from this review.
  support: supports
  accessed_at: '2026-11-06T11:56:13.815004Z'
  snapshot_sha256: 4059a49977b3b124625b569c1740d7b62be5685bb695fd221ba3bbc3e6ca96fe
- evidence_id: inspection
  kind: validation
  reference: .temp/pr2053/175/initial-inspection.json
  locator: Native current-input inspection using the current AGENTS rubric
  summary: Initial target/context hashes were rechecked before adding current source,
    authority, check and helper pins. The final working-tree snapshot remains a reviewer
    byte attestation, not a claim that ignored research artifacts were committed.
  support: supports
  accessed_at: '2026-11-06T11:56:13.815024Z'
  snapshot_sha256: d1992d55cee5decffeb8ba02e5fec5544e02f4d580553a24454b318f317e9333
- evidence_id: adapter
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: Complete returned public organism catalogue
  summary: No focal Geobacter or cellulolyticum organism match occurs in this catalogue.
    No expression-module evidence is used to infer focal phenotype or transfer.
  support: supports
  accessed_at: '2026-11-06T11:56:13.815045Z'
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
- evidence_id: source-175-missing-source-ranges
  kind: validation
  reference: .temp/pr2053/adversarial/175-missing-source-ranges.json
  locator: Supplemental public-reader ranges, independently retrieved and author-read
    before final input freezing
  summary: Together with web-primary-main.json these receipts cover all 79 lines of
    the 2007 extraction and all 60 lines of the 2008 extraction. They are parsed web
    responses, not original PDF bytes or figure pixels.
  support: supports
  accessed_at: '2026-11-06T11:56:13.815065Z'
  snapshot_sha256: 899a2234a8895537c404a51d9c64e665b9d5a2ea075b811f7598b0d8edefeefa
- evidence_id: source-175-final-source-ranges
  kind: validation
  reference: .temp/pr2053/adversarial/175-final-source-ranges.json
  locator: Supplemental public-reader ranges, independently retrieved and author-read
    before final input freezing
  summary: Together with web-primary-main.json these receipts cover all 79 lines of
    the 2007 extraction and all 60 lines of the 2008 extraction. They are parsed web
    responses, not original PDF bytes or figure pixels.
  support: supports
  accessed_at: '2026-11-06T11:56:13.815103Z'
  snapshot_sha256: 3d13cefc160e52f8d2655d161a9317ff7225ab0bb227fd39f8d9b9eaf57150f7
- evidence_id: source-175-extraction-coverage
  kind: validation
  reference: .temp/pr2053/adversarial/175-extraction-coverage.json
  locator: Supplemental public-reader ranges, independently retrieved and author-read
    before final input freezing
  summary: Together with web-primary-main.json these receipts cover all 79 lines of
    the 2007 extraction and all 60 lines of the 2008 extraction. They are parsed web
    responses, not original PDF bytes or figure pixels.
  support: supports
  accessed_at: '2026-11-06T11:56:13.815141Z'
  snapshot_sha256: 0c747f45b03aac3a67f0e4fffcc017d05c8be9c90915a1aa160031d332b1268d
- evidence_id: check-validate
  kind: validation
  reference: .temp/pr2053/175/validate.json
  locator: Actual command, times, exit and output digests
  summary: Focused native command and immutable output receipts.
  support: supports
  accessed_at: '2026-11-06T11:56:13.815197Z'
  snapshot_sha256: a931de9e95ead07d773b892a25fe60af986b087f8327331f49745de055f4d6ec
- evidence_id: check-validate-strict
  kind: validation
  reference: .temp/pr2053/175/validate-strict.json
  locator: Actual command, times, exit and output digests
  summary: Focused native command and immutable output receipts.
  support: supports
  accessed_at: '2026-11-06T11:56:13.815244Z'
  snapshot_sha256: cd1e147f4655a718677cac2e936c2837a9e655b79c4d1f3fd6f167f43def8fb1
- evidence_id: check-validate-terms
  kind: validation
  reference: .temp/pr2053/175/validate-terms.json
  locator: Actual command, times, exit and output digests
  summary: Focused native command and immutable output receipts.
  support: supports
  accessed_at: '2026-11-06T11:56:13.815283Z'
  snapshot_sha256: 755834859519f24e379d46b107da65ef23c878164a02c3fbd95b74bf7b206a61
- evidence_id: check-validate-gtdb
  kind: validation
  reference: .temp/pr2053/175/validate-gtdb.json
  locator: Actual command, times, exit and output digests
  summary: Focused native command and immutable output receipts.
  support: supports
  accessed_at: '2026-11-06T11:56:13.815325Z'
  snapshot_sha256: 5d65db3436f375af7f254116d4da72084e609cf7c252c397d9b8f43daab13822
- evidence_id: check-validate-gtdb-domain
  kind: validation
  reference: .temp/pr2053/175/validate-gtdb-domain.json
  locator: Actual command, times, exit and output digests
  summary: Focused native command and immutable output receipts.
  support: supports
  accessed_at: '2026-11-06T11:56:13.815372Z'
  snapshot_sha256: 8e44b64172c4b429fe73b20b3ee20320796f38b81afad1829cbbc81fa7e88676
- evidence_id: check-validate-history
  kind: validation
  reference: .temp/pr2053/175/validate-history.json
  locator: Actual command, times, exit and output digests
  summary: Focused native command and immutable output receipts.
  support: supports
  accessed_at: '2026-11-06T11:56:13.815417Z'
  snapshot_sha256: 9b25b4c5aebbaded8044ac2b589558b5fb868de9099f8369cb4ad7cac3941b4e
- evidence_id: check-normalize-cache-names-check
  kind: validation
  reference: .temp/pr2053/175/normalize-cache-names-check.json
  locator: Actual command, times, exit and output digests
  summary: Focused native command and immutable output receipts.
  support: supports
  accessed_at: '2026-11-06T11:56:13.815454Z'
  snapshot_sha256: 6080f7c0d95fd0e87d0b7092c1900b3d7e4dbad830e53cce6c5bc333700d571d
- evidence_id: check-validate-references-explained
  kind: validation
  reference: .temp/pr2053/175/validate-references-explained.json
  locator: Actual command, times, exit and output digests
  summary: Focused native command and immutable output receipts.
  support: supports
  accessed_at: '2026-11-06T11:56:13.815494Z'
  snapshot_sha256: 8c238d6f58c3b8b0cb0b71452e95a16bd6b88a613fce9568ae34f0af54eba4b0
- evidence_id: check-audit-network
  kind: validation
  reference: .temp/pr2053/175/audit-network.json
  locator: Actual command, times, exit and output digests
  summary: 'Corpus diagnostic: 48 warnings, zero errors across 17/510 records; target-specific
    graph has no issue.'
  support: supports
  accessed_at: '2026-11-06T11:56:13.815541Z'
  snapshot_sha256: 1223179f1c952fa93f2344d0d88760497c97005f159591ee8337602ac4919f1d
- evidence_id: check-check-network-quality
  kind: validation
  reference: .temp/pr2053/175/check-network-quality.json
  locator: Actual command, times, exit and output digests
  summary: 'Corpus diagnostic: 48 warnings, zero errors across 17/510 records; target-specific
    graph has no issue.'
  support: supports
  accessed_at: '2026-11-06T11:56:13.815583Z'
  snapshot_sha256: 87c26873c41961dc15e6a70764907d1d0f9e9012e4a4f95e515f1d88982191ca
assessments:
- assessment_id: identity
  area: identity
  topic: Defined binary MFC and study boundaries
  outcome: supported
  summary: The record denotes the intended laboratory pair.
  target_ids:
  - CommunityMech:000175
  evidence_ids:
  - record
  - abstracts
  - main-2007
  - main-2008
  - support
  - schema
  details: SYNTHETIC origin, ENGINEERED state and BIOTECHNOLOGY category fit deliberate
    assembly. Activated-sludge mixed cultures, monoculture controls, cloning hosts
    and catalogue environments are excluded.
  dimensions:
  - name: community_scope
    value: Defined two-member laboratory MFC
    definition: Excludes activated-sludge comparators and analytical cloning hosts.
    evidence_ids:
    - record
    - abstracts
  - name: study_stocks
    value: ATCC 35319 and ATCC 51573
    definition: Explicit focal stock designations, linked to H10 and PCA type-material
      authority without transferring catalogue maintenance conditions.
    evidence_ids:
    - main-2007
    - main-2008
    - taxa
- assessment_id: taxonomy
  area: grounding
  topic: Species, strains and GTDB provenance
  outcome: concern
  summary: Species identities are valid; exact 2008 culture and mapping provenance
    can be improved.
  target_ids:
  - CommunityMech:000175
  evidence_ids:
  - taxa
  - gtdb
  - common
  - main-2007
  - main-2008
  details: Both primary texts identify the same collection stocks; current species
    terms and the new reusable Geobacter identity link are consistent. Optional strain
    refinement must retain the species-versus-strain mapping denominators. The link
    does not import unrelated DIET/gene experiments into this community.
- assessment_id: roles
  area: scope
  topic: Recipient roles and ordinal abundance
  outcome: concern
  summary: Donor CROSS_FEEDER needs local recipient evidence; other supported roles
    and ordinals remain.
  target_ids:
  - CommunityMech:000175
  evidence_ids:
  - record
  - abstracts
  - main-2007
  - main-2008
  - support
  - schema
  details: Improved CMC degradation or product removal does not identify a Geobacter
    product utilized by Clostridium. Retain PRIMARY_DEGRADER, Geobacter CROSS_FEEDER
    and broad SYNTROPHIC_PARTNER. ABUNDANT is not a fixed percentage; qPCR/FISH context
    may clarify it without inventing a numerical threshold.
- assessment_id: supply-node
  area: graph
  topic: ecological_interactions[0]
  outcome: supported
  summary: Qualified fermentation-to-anode-respiration CROSS_FEEDING is supported.
  target_ids:
  - CommunityMech:000175
  evidence_ids:
  - record
  - abstracts
  - main-2007
  - main-2008
  - support
  - schema
  details: Keep the C. cellulolyticum to G. sulfurreducens direction and residual-pool
    caveats. No obligacy, reciprocal fitness, direct electron transfer or molecule-resolved
    flux is established.
- assessment_id: current-node
  area: graph
  topic: ecological_interactions[1]
  outcome: supported
  summary: The untyped binary-current and degradation endpoint is appropriately bounded.
  target_ids:
  - CommunityMech:000175
  evidence_ids:
  - record
  - abstracts
  - main-2007
  - main-2008
  - support
  - schema
  details: Negative pure-culture current controls and greater CMC degradation support
    functional complementarity. They do not independently identify a unique product-removal
    mechanism or reciprocal fitness.
- assessment_id: localization-node
  area: graph
  topic: ecological_interactions[2]
  outcome: supported
  summary: The untyped spatial observation preserves both substrate conditions.
  target_ids:
  - CommunityMech:000175
  evidence_ids:
  - record
  - abstracts
  - main-2007
  - main-2008
  - support
  - schema
  details: Retain FISH/qPCR substrate and compartment scope without restoring a causal
    localization arrow or niche-partitioning claim. Text and captions were read; no
    figure pixels were independently assessed.
- assessment_id: supply-edge
  area: graph
  topic: ecological_interactions[0].downstream[0]
  outcome: supported
  summary: The single retained supply-to-current arrow is appropriately qualified.
  target_ids:
  - CommunityMech:000175
  evidence_ids:
  - record
  - abstracts
  - main-2007
  - main-2008
  - support
  - schema
  details: Preserve the functional conversion link. No additional edge is justified
    by localization observations or residual-metabolite identity alone.
- assessment_id: ingredient-claims
  area: consistency
  topic: related_ingredients acetate and dihydrogen
  outcome: concern
  summary: Off-graph recipient-use wording exceeds its residual-pool evidence.
  target_ids:
  - CommunityMech:000175
  evidence_ids:
  - record
  - abstracts
  - main-2007
  - main-2008
  - support
  - schema
  details: Apply the graph’s existing uncertainty to related_ingredients[1] and [3].
    Keep ethanol as a residual intermediate; generic fermentation-product supply remains
    supported.
- assessment_id: chemical-identity
  area: grounding
  topic: growth_media[0].composition[0].chebi_term
  outcome: concern
  summary: CMC is a derivative and is not represented by unmodified cellulose.
  target_ids:
  - CommunityMech:000175
  evidence_ids:
  - cmc
  - cmc-salt
  - main-2008
  details: The 2008 reagent is sodium CMC. Preserve derivative and salt scope without
    inventing substitution degree. Valid cellulose/MN301 graph and ingredient annotations
    should not be globally replaced.
- assessment_id: cultivation
  area: scope
  topic: Medium, substrate arms and MFC operation
  outcome: concern
  summary: Recoverable study-specific Methods should replace stale workflow prose
    while preserving distinct protocols.
  target_ids:
  - CommunityMech:000175
  evidence_ids:
  - record
  - abstracts
  - main-2007
  - main-2008
  - support
  - schema
  details: Separate precursor cultures, final substrate arms, anode/catholyte compartments,
    capacity/working volume and study-specific power results. Both sources describe
    medium replacement. Author terminology does not override the native operation
    definition. The 2008 extraction's ambiguous glyphs require visual verification.
- assessment_id: environment
  area: grounding
  topic: Environment, processes and metal scope
  outcome: supported
  summary: Laboratory environment, source-qualified processes and metal categorization
    are appropriate.
  target_ids:
  - CommunityMech:000175
  evidence_ids:
  - record
  - abstracts
  - main-2007
  - main-2008
  - support
  - schema
  details: Cellulose catabolism and fermentation describe the cellulolytic process;
    anode respiration is not thereby assigned the same process. Ferricyanide and trace
    nutrients do not establish a metal-processing purpose. Preserve NOT_APPLICABLE
    metal relevance.
- assessment_id: evidence
  area: evidence
  topic: Claim-local excerpts and source accessibility
  outcome: concern
  summary: All 28 abstract excerpts match, but expanded claims require narrower support.
  target_ids:
  - CommunityMech:000175
  evidence_ids:
  - record
  - abstracts
  - main-2007
  - main-2008
  - support
  - schema
  details: Both maintained caches remain correctly abstract-only; newly read complete
    public text extractions can support separately authorized evidence enrichment
    with precise provenance. Figure pixels and original PDF equivalence remain unverified;
    completion remains partial.
- assessment_id: resources
  area: representation
  topic: External publications and dataset scope
  outcome: supported
  summary: Both article links are correctly typed and identified.
  target_ids:
  - CommunityMech:000175
  evidence_ids:
  - record
  - abstracts
  - main-2007
  - main-2008
  - support
  - schema
  details: No deposit is inferred from primer-design databases or catalogue records,
    and the empty dataset list creates no separate finding. No media or ingredient
    cross-Mech IDs are encoded.
- assessment_id: provenance
  area: provenance
  topic: Prior review chain and current follow-up
  outcome: supported
  summary: The current common-taxon change and prior review lineage are reconciled
    without retiring unrelated findings.
  target_ids:
  - CommunityMech:000175
  evidence_ids:
  - history
  - issues
  - inspection
  - delta
  - common
  details: Only the four original single-target findings receive previous_occurrences.
    The multi-target Cycle 2 link-gap dispositions and closed 2073 remain context;
    other affected communities are not reassessed. Open 1327 remains the curation
    owner.
- assessment_id: validation
  area: schema
  topic: Native checks and source completion
  outcome: supported
  summary: Eight focused native checks pass; scientific review remains partial.
  target_ids:
  - CommunityMech:000175
  evidence_ids:
  - support
  - access
  - check-validate
  - check-validate-strict
  - check-validate-terms
  - check-validate-gtdb
  - check-validate-gtdb-domain
  - check-validate-history
  - check-normalize-cache-names-check
  - check-validate-references-explained
  - check-audit-network
  - check-check-network-quality
  details: Eight focused native gates pass. Corpus diagnostics retain 48 warnings/zero
    errors; target connectivity is complete. Full-source text access improved, but
    no figure-pixel certification or canonical change occurred.
- assessment_id: metrics
  area: completeness
  topic: Native completeness and validation quality
  outcome: supported
  summary: Completeness 85; raw quality 111, capped 100.
  target_ids:
  - CommunityMech:000175
  evidence_ids:
  - support
  metrics:
  - name: completeness
    value: 85
    unit: points
    minimum: 0
    maximum: 100
    definition: Required fields with taxon roles 50 + environment term 5 + at least
      three interaction nodes 10 + external resources 5 + growth media 10 + node metabolites
      5. Two environmental factors earn no three-factor bonus; empty associated_datasets
      earns none. Presence does not establish source support.
  - name: validation_quality
    value: 100
    unit: points
    minimum: 0
    maximum: 100
    definition: clamp(100 − 50P1 − 10P2 − 2P3 + 20min(mean node evidence/2,1) + 15
      if COMPLETE,0,100). P1=0, P2=2, P3=2, P4=0. Eight evidence occurrences/three
      nodes give mean 8/3 and capped bonus 20; COMPLETE adds 15. Raw 111 caps at 100.
  - name: P1
    value: 0
    unit: findings
    definition: Native severity count.
  - name: P2
    value: 2
    unit: findings
    definition: Native severity count.
  - name: P3
    value: 2
    unit: findings
    definition: Native severity count.
  - name: P4
    value: 0
    unit: findings
    definition: Native severity count.
findings:
- finding_id: qualify-metabolite-use
  issue_key: cm-000175-qualify-metabolite-use
  category: evidence
  severity: major
  native_severity: P2
  normalization_reason: Recipient-use and molecule-specific interpretation exceed
    the local evidence, materially changing the proposed mechanism.
  rule_id: review-checklist.claim-specific-scope-and-grounding
  status: open
  certainty: confirmed
  title: Qualify metabolite use and donor recipient-role claims
  description: The donor's optional CROSS_FEEDER role still lacks evidence of utilization
    of a Geobacter product. Ingredient assertions attach only a residual-metabolite
    snippet; strengthen their local source attribution or qualify the inferred molecule-specific
    transfer. Newly accessible main-text controls and author interpretations inform
    this repair without establishing partner-resolved flux or a reciprocal recipient
    role. Preserve the qualified graph.
  target_ids:
  - CommunityMech:000175
  field_paths:
  - taxonomy[0].functional_role
  - taxonomy[0].evidence
  - related_ingredients[1].relevance
  - related_ingredients[3].relevance
  - related_ingredients[1].evidence
  - related_ingredients[3].evidence
  evidence_ids:
  - record
  - main-2007
  - main-2008
  - support
  - schema
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Clostridium_Cellulolyticum_Geobacter_Cellulose_MFC_Coculture.yaml
    role: canonical_record
  ownership_note: Canonical/source curation remains outside PR 2053. Preserve open
    1327, closed graph repair 1324 and the completed common-taxon linkage tracked
    by 2073.
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261021T212006Z-cellulose-mfc-record-review
    finding_id: qualify-metabolite-use
- finding_id: ground-cmc-derivative
  issue_key: cm-000175-ground-cmc-derivative
  category: grounding
  severity: major
  native_severity: P2
  normalization_reason: The medium ingredient represents a substituted derivative
    using an unsubstituted chemical term.
  rule_id: review-checklist.claim-specific-scope-and-grounding
  status: open
  certainty: confirmed
  title: Ground the CMC component as a chemical derivative
  description: growth_media[0].composition[0] names CMC but grounds it to CHEBI:18246,
    unsubstituted cellulose. Use a verified derivative identity and source-specific
    sodium-salt context. Keep valid generic cellulose and MN301 annotations; no global
    replacement or invented substitution degree.
  target_ids:
  - CommunityMech:000175
  field_paths:
  - growth_media[0].composition[0].chebi_term
  - growth_media[0].composition[0].name
  evidence_ids:
  - record
  - cmc
  - cmc-salt
  - main-2008
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Clostridium_Cellulolyticum_Geobacter_Cellulose_MFC_Coculture.yaml
    role: canonical_record
  ownership_note: Canonical/source curation remains outside PR 2053. Preserve open
    1327, closed graph repair 1324 and the completed common-taxon linkage tracked
    by 2073.
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261021T212006Z-cellulose-mfc-record-review
    finding_id: ground-cmc-derivative
- finding_id: recover-study-protocol
  issue_key: cm-000175-recover-study-protocol
  category: provenance
  severity: minor
  native_severity: P3
  normalization_reason: Recoverable protocol, obsolete notes and mode semantics require
    bounded clarification; no optional field is falsely treated as schema-required.
  rule_id: review-checklist.claim-specific-scope-and-grounding
  status: open
  certainty: confirmed
  title: Recover study-specific cultivation and evidence context
  description: Current cultivation notes retain unrelated workflow history and unavailable-Methods
    statements. Both primary text extractions are now accessible. Recover study-specific
    preparation, substrate arms and apparatus without merging recipes, power values
    or compartments; distinguish author fed-batch terminology from medium replacement
    and native mode semantics.
  target_ids:
  - CommunityMech:000175
  field_paths:
  - growth_media[0].composition
  - growth_media[0].preparation_notes
  - growth_media[0].evidence
  - cultivation_setup[0].cultivation_mode
  - cultivation_setup[0].instrument_detail
  - cultivation_setup[0].electrode_detail
  - cultivation_setup[0].notes
  - cultivation_setup[0].evidence
  - discussions[0].rationale
  evidence_ids:
  - record
  - main-2007
  - main-2008
  - support
  - schema
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Clostridium_Cellulolyticum_Geobacter_Cellulose_MFC_Coculture.yaml
    role: canonical_record
  - repository: CultureBotAI/CommunityMech
    path: references_cache/PMID_17695929.md
    role: source_cache
  - repository: CultureBotAI/CommunityMech
    path: references_cache/PMID_18725730.md
    role: source_cache
  ownership_note: Canonical/source curation remains outside PR 2053. Preserve open
    1327, closed graph repair 1324 and the completed common-taxon linkage tracked
    by 2073.
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261021T212006Z-cellulose-mfc-record-review
    finding_id: recover-study-protocol
- finding_id: document-strain-mapping
  issue_key: cm-000175-document-strain-mapping
  category: provenance
  severity: minor
  native_severity: P3
  normalization_reason: Species identities and ordinals remain valid; exact culture
    context and snapshot provenance are localized improvements.
  rule_id: review-checklist.claim-specific-scope-and-grounding
  status: open
  certainty: confirmed
  title: Document source strains and reproducible mapping provenance
  description: Both primary texts name exact culture stocks, while mapping_source
    still asserts a latest release/build date without sufficient provenance. Add source-specific
    strain context and the examined snapshot/method; preserve current species mappings
    and ordinal abundance. The newly added common_taxon link is valid and should remain.
  target_ids:
  - CommunityMech:000175
  field_paths:
  - taxonomy[0].taxon_term.notes
  - taxonomy[1].taxon_term.notes
  - taxonomy[0].taxon_term.gtdb_classification.mapping_source
  - taxonomy[1].taxon_term.gtdb_classification.mapping_source
  - taxonomy[0].evidence
  - taxonomy[1].evidence
  evidence_ids:
  - record
  - taxa
  - gtdb
  - common
  - main-2007
  - main-2008
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Clostridium_Cellulolyticum_Geobacter_Cellulose_MFC_Coculture.yaml
    role: canonical_record
  ownership_note: Canonical/source curation remains outside PR 2053. Preserve open
    1327, closed graph repair 1324 and the completed common-taxon linkage tracked
    by 2073.
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261021T212006Z-cellulose-mfc-record-review
    finding_id: document-strain-mapping
actions:
- action_id: qualify-recipient-use
  description: Align non-graph metabolite and role claims with their actual evidence.
  finding_ids:
  - qualify-metabolite-use
  target_ids:
  - CommunityMech:000175
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Clostridium_Cellulolyticum_Geobacter_Cellulose_MFC_Coculture.yaml
    role: canonical_record
  acceptance_checks:
  - At related_ingredients[1].relevance and [3].relevance, distinguish residual acetate/hydrogen
    from inferred partner use and directly measured uptake. Attach exact source-local
    support for any stronger molecule-specific claim; do not turn absent uptake evidence
    into proof that uptake cannot occur.
  - At taxonomy[0].functional_role, identify the other-taxon provider, metabolite
    and utilization evidence before retaining CROSS_FEEDER; otherwise omit or qualify
    this optional recipient role. Improved CMC conversion and donor fermentation alone
    do not establish it. No carbon/energy-only or obligacy requirement is imposed.
  - Retain C. cellulolyticum PRIMARY_DEGRADER, Geobacter CROSS_FEEDER and broad SYNTROPHIC_PARTNER
    with source attribution. Preserve all three nodes and the single qualified arrow,
    residual-pool limits, untyped endpoints and lack of a localization-causality edge.
- action_id: ground-cmc
  description: Correct only the derivative-specific medium identity.
  finding_ids:
  - ground-cmc-derivative
  target_ids:
  - CommunityMech:000175
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Clostridium_Cellulolyticum_Geobacter_Cellulose_MFC_Coculture.yaml
    role: canonical_record
  acceptance_checks:
  - Replace the unmodified-cellulose grounding at growth_media[0].composition[0].chebi_term
    with verified CHEBI:85146 carboxymethylcellulose, or a separately justified exact
    sodium-salt grounding. The 2008 Methods explicitly says sodium CMC; CHEBI:234035
    is a verified salt label with limited definition metadata. Preserve the distinction
    between chemical family and exact reagent.
  - Keep CHEBI:18246 for MN301 and generic cellulose contexts. Both study texts name
    sodium CMC; do not infer a shared formulation, substitution degree or grade from
    another study or ambiguous extraction. Verify any proposed numerical reagent specification
    against the exact original.
- action_id: recover-protocol
  description: Represent the two recovered protocols without merging study stages
    or compartments.
  finding_ids:
  - recover-study-protocol
  target_ids:
  - CommunityMech:000175
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Clostridium_Cellulolyticum_Geobacter_Cellulose_MFC_Coculture.yaml
    role: canonical_record
  - repository: CultureBotAI/CommunityMech
    path: references_cache/PMID_17695929.md
    role: source_cache
  - repository: CultureBotAI/CommunityMech
    path: references_cache/PMID_18725730.md
    role: source_cache
  acceptance_checks:
  - Replace off-topic infant-HMO/#183/#543 and cache-size narrative in cultivation_setup[0].notes
    with biological study context. Retain the 2007 abstract as the source of 143/59.2
    mW/m² and its author-described fed-batch tests; record 2008 power 153/83 separately
    if added.
  - 'Represent 2008 sodium CMC and MN301 as alternative 1 g/L reactor arms. Recover
    the per-litre recipe from MFC inoculum, construction, and operation: NH4Cl 1.05
    g, KCl 0.1 g, NaH2PO4·H2O 4.90 g, Na2HPO4 9.15 g, yeast extract 0.2 g, NaHCO3
    2.5 g, and 10 mL each trace-mineral/vitamin mixtures. Preserve the cited but unverified
    stock recipes. Do not call this chemically defined sole-carbon medium.'
  - Record 310-mL bottle capacity only as capacity until working volume is verified;
    keep 16-cm² electrode geometry and ferricyanide/phosphate catholyte separate from
    anode medium. Catholyte pH 7.0 is not an anode pH setpoint, and external circuit
    resistance is not an applied potential. Do not transfer analytical or cloning-host
    conditions.
  - Preserve the authors' fed-batch wording alongside actual medium/catholyte replacement.
    The 2007 text specifies complete replacement below 40 mV. Select a native mode
    from the literal operation; do not force FED_BATCH with broth removal, partial-harvest
    SEMI_CONTINUOUS or an unperformed settle/draw cycle. Keep the 2008 operation and
    proposed optimization distinct.
  - Verify ambiguous 2008 degree/ohm/micro-unit glyphs against readable page images
    before numerical curation. The newly accessible 2007 text provides separate stage-specific
    Methods; do not copy the 2008 recipe into it. Preserve exact author-copy/source
    version and actual access limits if enriching caches. Update current access rationale
    without altering historical review receipts.
- action_id: document-taxonomy
  description: Add exact strain context and verifiable GTDB provenance.
  finding_ids:
  - document-strain-mapping
  target_ids:
  - CommunityMech:000175
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Clostridium_Cellulolyticum_Geobacter_Cellulose_MFC_Coculture.yaml
    role: canonical_record
  acceptance_checks:
  - Attach the independently inspected Methods from both studies and current NCBI
    type-material aliases for ATCC 35319/H10/DSM 5812 and ATCC 51573/PCA/DSM 12127.
    Preserve valid species terms and the resolved common_taxon link; optional strain
    refinement is not mandatory. Do not import unrelated reusable-gene mechanisms
    into the focal pair.
  - Replace unverified latest/build-date text with the examined crosswalk hash and
    exact-ID route. Preserve NCBITaxon 1521 mapping 1.0/one genome and 35554 mapping
    1.0/19. Optional 394503/243231 strain rows each have 1.0/two genomes and must
    remain separate from species support counts.
  - Keep ordinal ABUNDANT. If adding abundance context, label substrate, compartment,
    time and FISH/qPCR method; gene-copy ratios are not universal cell fractions.
    Do not require percentages or silently reconcile qualitative FISH and quantitative
    sampling comparisons.
- action_id: verify-future-curation
  description: Validate separately authorized curation and retain access boundaries.
  finding_ids:
  - qualify-metabolite-use
  - ground-cmc-derivative
  - recover-study-protocol
  - document-strain-mapping
  target_ids:
  - CommunityMech:000175
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Clostridium_Cellulolyticum_Geobacter_Cellulose_MFC_Coculture.yaml
    role: canonical_record
  - repository: CultureBotAI/CommunityMech
    path: references_cache/PMID_17695929.md
    role: source_cache
  - repository: CultureBotAI/CommunityMech
    path: references_cache/PMID_18725730.md
    role: source_cache
  acceptance_checks:
  - Both primary text extractions are now read. Before declaring complete scientific
    verification, inspect critical original figures and ambiguous typography, retain
    version/locator provenance and reassess any resulting interpretation changes.
    Do not treat a current abstract cache or a web response hash as original-PDF equivalence.
  - Attach precise reference/section evidence to each changed field and preserve the
    current graph qualifications. After authorized canonical edits, append history
    and run schema, strict, terms, references, GTDB, domain and history checks, then
    just gen-html and just check-docs-current.
  - Canonical YAML, caches, histories, schema and products remain unchanged in PR
    2053. Save only the new immutable linked review and its reproducible helpers;
    obtain a separate read-only review of the committed head before merge.
limitations:
- Complete public author-copy text extractions, captions and references for both focal
  papers were read. Direct curl requests returned 403 challenge HTML. No original
  PDF byte equivalence, figure pixels or raw data were verified; scientific completion
  remains partial.
- The two-column extraction has ambiguous scientific glyphs and interleaved layout,
  particularly in the 2008 article. Do not silently normalize uncertain units or import
  measurements across studies, stages or compartments.
- Bulk residual pools, current/degradation comparisons and the authors' product-removal
  interpretation do not quantify molecule-specific partner flux or establish a metabolite
  utilized by the cellulolytic donor. No obligacy test is required to use the repository's
  syntrophy semantics.
- The new common_taxon link is assessed for identity and scope. Generic gene, assembly
  and other-community DIET claims in the reusable record are not independently certified
  as focal cellulose-MFC evidence.
- Both original caches remain abstract-only and all 28 current snippets match fresh
  reference-specific abstracts. Neither the caches nor the canonical history was enriched
  or rewritten.
- Corpus network diagnostics return exit 1 for 48 warnings/zero errors across 17/510
  records; this target has no structural network issue. Native presence/validation
  scores do not certify the science.
- Only the original four single-target findings are superseded as continuing open
  observations. Multi-target Cycle 2 dispositions and other communities remain outside
  this review's adjudication scope.
notes:
- Two major and two minor findings remain open; completeness 85 and validation quality
  100 (raw 111) retain their documented native formulas.
- The new record hash includes the valid common-taxon link/history. Source access
  has improved relative to the original review; no unavailable historical scratch
  file was recovered or invented.
- All helper scripts feeding this result are versioned under scripts/adhoc. Ignored
  source receipts are frozen working-tree attestations, not committed source bodies.
tags:
- record-review
- cellulose
- microbial-fuel-cell
- batch-11
- pr2053-current-input-refresh
related_reviews:
- repository: CultureBotAI/CommunityMech
  review_id: 20261021T212006Z-cellulose-mfc-record-review
  relationship: Immutable current-input successor; four original findings remain open.
- repository: CultureBotAI/CommunityMech
  review_id: 20261025T113500Z-c2s4-record-deep-audit
  relationship: Common-taxon lineage context only; multi-target disposition not superseded.
- repository: CultureBotAI/CommunityMech
  review_id: 20261025T113600Z-c2s4-frozen-cohort-review
  relationship: Common-taxon lineage context only; multi-target disposition not superseded.
- repository: CultureBotAI/CommunityMech
  review_id: 20261025T161500Z-c2s5-remediation-verification
  relationship: Common-taxon lineage context only; multi-target disposition not superseded.
```
