# Drosophila five-species gnotobiotic microbiota record review

- Review: 20261022T073419Z-drosophila-five-species-record-review
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-22T07:18:40.584673Z
- Finished UTC: 2026-10-22T07:34:19.937956Z
- Reviewer: codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The five source stocks and three qualified host-phenotype observations are supported. Two major findings concern microbial membership/current species scope and unproven metabolic roles; three minor findings concern cultivation, GTDB provenance and publication-shaped datasets. All eight required native checks passed. Completeness is 30; raw quality 102.33333333333331 is capped at 100.

## Scope And Provenance

Whole released record and three complete source articles, eleven main figures, relevant 2015 supplements and actual corrigendum; local native/authority checks and bounded source-declared archive metadata.

Selection: Only released CommunityMech:000160 in owned batch 16.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base cb7a782c8ba80299dca8761ad0a2c90bccd8a117.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000160 | kb/communities/Drosophila_FiveSpecies_Gnotobiotic_Gut_Microbiota.yaml | maintained | Drosophila Five-Species Gnotobiotic Gut Microbiota |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000160 | Actual native exit 0. |
| validate-strict | passed | True | CommunityMech:000160 | Actual native exit 0. |
| validate-terms | passed | True | CommunityMech:000160 | Actual native exit 0. |
| validate-references-explained | passed | True | CommunityMech:000160 | Actual native exit 0. |
| validate-gtdb | passed | True | CommunityMech:000160 | Actual native exit 0. |
| validate-gtdb-domain | passed | True | CommunityMech:000160 | Actual native exit 0. |
| validate-history | passed | True | CommunityMech:000160 | Actual native exit 0. |
| normalize-cache-names-check | passed | True | CommunityMech:000160 | Actual native exit 0. |
| audit-network corpus context | failed | False | CommunityMech:000160 | Actual corpus exit 1, zero structural errors. |
| check-network-quality corpus context | failed | False | CommunityMech:000160 | Actual corpus exit 1, zero structural errors. |
| Host-specific structured adapter applicability | unavailable | False | CommunityMech:000160 | Runner unavailable in the owned environment; host dataset coverage unverified. |

## Scientific And Domain Assessments

### Defined microbial membership and source stocks

identity: concern. Targets: CommunityMech:000160.

The five-source-species identity is recoverable, but the host and historical genus aggregate need correction.

Drosophila is the host, not a sixth microbial member. Current NCBITaxon:1578 does not contain Levilactobacillus brevis, Fructilactobacillus fructivorans or Lactiplantibacillus plantarum. The two Acetobacter species remain in Acetobacter. Preserve historical source names as aliases, verified DmelCS designations and the host as an outside-community participant. Roster counts are not quantitative abundance.

### Metabolic role entailment

evidence: concern. Targets: CommunityMech:000160.

The four group-wide metabolic role tags exceed the demonstrated mechanism.

CROSS_FEEDER means utilization of metabolites from other taxa; SECONDARY_FERMENTER means fermentation of products from primary degraders. The studies report host phenotypes and CFU responses, with provisioning as one hypothesis. Neither reciprocal CFU promotion nor supplied diet/MMRS establishes those roles for all members. This does not show that exchange is impossible, and no replacement role is invented.

### Joint host triglyceride outcome

graph: supported. Targets: CommunityMech:000160.

Retain the qualified COMMUNITY_LEVEL outcome; mixed-pair effects differ and no exchange is established.

Exact selector ecological_interactions[0]. Current taxon/scope bindings: {"scope": "COMMUNITY_LEVEL", "participating_taxa": [{"preferred_term": "Drosophila gut Acetobacter isolates", "term": {"id": "NCBITaxon:434", "label": "Acetobacter"}}, {"preferred_term": "Drosophila gut Lactobacillus isolates", "term": {"id": "NCBITaxon:1578", "label": "Lactobacillus"}}, {"preferred_term": "Drosophila melanogaster", "term": {"id": "NCBITaxon:7227", "label": "Drosophila melanogaster"}}]}. Exact canonical excerpt bindings: [{"selector": "ecological_interactions[0].evidence[0].snippet", "sha256": "9e61c0454017de30ba4e2634d196afdb92b8141e4208c28768c75900b31db789", "reference": "PMID:24242251", "supports": "SUPPORT", "evidence_source": "IN_VIVO"}]. PMID:24242251, Results single- and dual-species comparisons and Figures 2–3 support host TAG effects. Host lipid-process and interspecies GO terms are context, not direct molecular flux. Species descriptors need the separately graded roster repair; no new interaction type is required.

### Species-specific abundance promotion

graph: supported. Targets: CommunityMech:000160.

Retain the observed PAIRWISE promotion in L. brevis/L. fructivorans contexts and the nonsignificant L. plantarum boundary.

Exact selector ecological_interactions[1]. Current taxon/scope bindings: {"scope": "PAIRWISE", "source_taxon": {"preferred_term": "Drosophila gut Lactobacillus isolates", "term": {"id": "NCBITaxon:1578", "label": "Lactobacillus"}}, "target_taxon": {"preferred_term": "Drosophila gut Acetobacter isolates", "term": {"id": "NCBITaxon:434", "label": "Acetobacter"}}}. Exact canonical excerpt bindings: [{"selector": "ecological_interactions[1].evidence[0].snippet", "sha256": "ba4dd83d44e876d874912d34eb5255083267371033f1d8f7d18f03db907ce843", "reference": "PMID:24242251", "supports": "SUPPORT", "evidence_source": "IN_VIVO"}]. PMID:24242251, Results abundance subsection paragraph 2 and Figure 5 support whole-fly CFU endpoints. CFU does not establish stable gut residence or growth rate. L. fructivorans is reduced in pairs and cannot be resolved in the mixed five-species CFU assay; do not infer biological absence.

### Context-dependent host nutrition

graph: supported. Targets: CommunityMech:000160.

Retain distinct 2014 and 2015 outcomes, including null and opposite-direction responses.

Exact selector ecological_interactions[2]. Current taxon/scope bindings: {"scope": "COMMUNITY_LEVEL", "participating_taxa": [{"preferred_term": "Drosophila gut Acetobacter isolates", "term": {"id": "NCBITaxon:434", "label": "Acetobacter"}}, {"preferred_term": "Drosophila gut Lactobacillus isolates", "term": {"id": "NCBITaxon:1578", "label": "Lactobacillus"}}, {"preferred_term": "Drosophila melanogaster", "term": {"id": "NCBITaxon:7227", "label": "Drosophila melanogaster"}}]}. Exact canonical excerpt bindings: [{"selector": "ecological_interactions[2].evidence[0].snippet", "sha256": "39772b5f4bea5a61f20ccb14cd8218c02842d635d96d71889bc54a2baa8052c6", "reference": "PMID:24242251", "supports": "SUPPORT", "evidence_source": "IN_VIVO"}, {"selector": "ecological_interactions[2].evidence[1].snippet", "sha256": "247eccd82c5323a643ff4e2001e4ed7b8f8950dc5f7197ab97e3624d7345cea7", "reference": "PMID:25692519", "supports": "SUPPORT", "evidence_source": "IN_VIVO"}]. PMID:24242251 Results and Figures 2–3 support glucose responses and the single/five-member null weight/protein/glycogen context. PMID:25692519 Figures 1–2 and Discussion paragraph 1 establish genotype-dependent responses. Growth/glucose GO terms and glucose/TAG CHEBI terms are host phenotype context, not exchange or universal benefit. The S5b correction is confined to its actual panels.

### Abundance promotion to host TAG outcome

graph: supported. Targets: CommunityMech:000160.

Retain the explicitly PARTIAL proposed mediation.

Exact selector ecological_interactions[1].downstream[0]; target Acetobacter-Lactobacillus Nutrient Allocation Interaction. Exact description: PARTIAL - greater Acetobacter abundance could contribute to lower host triglycerides. Inoculum perturbations support this model but do not selectively establish abundance as the mediator. Description SHA256 8423b6c667b022baaf8d2fd052126648851e3eb6b6380af8b70dc1df4cceb97a. Figure 6 fixes A. tropicalis inoculum while varying L. brevis, with CFU/TAG associations; varying A. tropicalis alone did not establish the mediator. This supports a proposed direction without selective causal proof. When repairing species descriptors, attach this specific source evidence to the arrow; no additional arrow or grading penalty is warranted.

### Source-specific microbial and host conditions

evidence: concern. Targets: CommunityMech:000160.

Recover the documented recipes and stages, with claim-local evidence.

The 2014 MMRS recipe is 1.25% vegetable peptone, 0.75% yeast extract, 2% glucose, 0.5% sodium acetate, 0.2% dipotassium hydrogen phosphate, 0.2% triammonium citrate, 0.02% magnesium sulfate heptahydrate, 0.005% manganese sulfate tetrahydrate and 1.2% agar. Retain reported units/forms. The current FACULTATIVE_ANAEROBIC category is not a substitute for source-specific aerobic/CO2 plate handling. The 2015 MRS broths use overnight shaking for Acetobacter, overnight static L. brevis/L. plantarum and seven days static L. fructivorans; do not transfer these durations into the principal 2014 assay.

### Current species scope and GTDB provenance

grounding: concern. Targets: CommunityMech:000160.

Valid labels and numeric genus mappings do not settle source isolate classification.

Encoded descriptors are NCBITaxon:434 Acetobacter, NCBITaxon:1578 Lactobacillus and host NCBITaxon:7227 Drosophila melanogaster. Proposed source species IDs are NCBITaxon:65959 Acetobacter pomorum, NCBITaxon:104102 Acetobacter tropicalis, NCBITaxon:1580 Levilactobacillus brevis, NCBITaxon:1614 Fructilactobacillus fructivorans and NCBITaxon:1590 Lactiplantibacillus plantarum; these are species descriptors, not exact DmelCS strain identifiers. Both Acetobacter species have ambiguous local name routes; the other species have verified local routes, each distinct from exact DmelCS strain classification. The existing genus totals 395/395 and 5369/5379 reproduce, but latest/built 2026-07-25 is not validated release metadata.

### Claim-local evidence and phenotype interpretation

evidence: supported. Targets: CommunityMech:000160.

All twelve canonical snippets match; their scope still matters.

The survey excerpts establish taxonomic OTUs, not exact stock genomes or cross-feeding. The graph correctly uses in-vivo host outcomes and keeps mediation partial. The corrected SI panel labels must accompany any later panel-specific host-gene interpretation.

### Publication references versus actual datasets

representation: concern. Targets: CommunityMech:000160.

Move bibliography-shaped dataset entries to publication links and scope genuine survey data separately.

All three PMID/PubMed identifiers are correct publications. SRA023605.3 resolves to SRP003313, SRX025956, SRR155572 and SAMN00109755: one pooled 454 16S survey run. HQ173707–HQ173711 are 270 bp uncultured clone markers. These are not exact cultured DmelCS isolate genomes, new phenotype datasets or strain-specific reference assemblies. No broad missing-archive search or raw-read reanalysis was performed.

### Full main evidence and bounded supplements

scope: supported. Targets: CommunityMech:000160.

Current encoded claims were adjudicated from all three full articles, figures and relevant follow-up supplements.

Lead read complete 2014, 2011 and 2015 main projections, including tables, captions and references, and all eleven main figures. The 2015 SI review covers all seven figures on nine pages, complete Tables S1/S2/S5/S6/S7 and Note 1. Bulk SNP/GO Tables S3/S4 were inventoried with headers/initial displayed rows only. Five 2011 supplements were not recovered; no claim depends on unseen supplementary details. Actual corrigendum text and corrected thumbnail were separately read. The optional structured adapter is unavailable in the owned runtime and host dataset coverage remains unknown.

### Prior reviews and maintained-record ownership

ownership: supported. Targets: CommunityMech:000160.

The present audit preserves source history and existing graph qualifications.

Support read the exact prior row, whole focal caches/history and bounded cohort/current issue context. Historical repair or issue status is not substituted for fresh source entailment. Any future curation belongs to the maintained record under separate authorization; this review changes no canonical YAML, cache, history or issue.

### Actual native validation

schema: supported. Targets: CommunityMech:000160.

All eight required checks passed; the current network has no reported structural issues.

Native COMPLETE does not establish correct community membership, metabolic exchange or complete source coverage. Retrieval and ad hoc display failures are distinct from native validation.

### Literal rubric scores

completeness: supported. Targets: CommunityMech:000160.

Completeness 30; raw quality 102.33333333333331, capped at 100.

## Findings

### membership: Resolve microbial members and preserve host context

major / open / confirmed; issue key: cm-000160-membership.

Host inclusion violates the membership slot, and the current Lactobacillus genus descriptor does not contain the three source species.

### roles: Qualify unsupported metabolic roles

major / open / confirmed; issue key: cm-000160-roles.

CROSS_FEEDER and SECONDARY_FERMENTER are asserted for both groups without demonstrated partner-product utilization or fermentation.

### cultivation: Separate source-specific media and preparation stages

minor / open / confirmed; issue key: cm-000160-cultivation.

The maintained medium lacks source-local evidence and its physiological atmosphere category does not convey the distinct reported protocols. Recover the available recipe and study-specific stages.

### gtdb-provenance: Replace unsupported GTDB release wording

minor / open / confirmed; issue key: cm-000160-gtdb-provenance.

Both mapping_source strings assert latest release and a build date not established by the local crosswalk metadata.

### datasets: Distinguish publications from data resources

minor / open / confirmed; issue key: cm-000160-datasets.

The three associated dataset accessions are publication PMIDs rather than genuine dataset identifiers.

## Recommended Actions And Acceptance Checks

### repair-membership

Represent the five source bacteria and external host consistently.

- Use verified current species IDs and canonical labels with historical source names and exact DmelCS codes retained; do not invent strain CURIEs or attach clone markers as stock genomes.
- Remove the fly from microbial taxonomy while keeping it in host/environment and appropriate ecological interaction participation. Preserve the named mono-, dual- and five-member experimental scopes.
- Align node participants and pair descriptors with the measured species combinations. Preserve all three qualified observations and the PARTIAL 1→0 arrow, attaching the specific Figure 6 evidence to its mediation statement; do not universalize genus-level responses or add exchange arrows.
- Move roster-count prose from deprecated abundance_value into appropriate notes without inventing quantitative abundance.

### repair-roles

Remove unsupported unqualified metabolic role assertions.

- Retain only role tags supported by actual utilization/fermentation evidence; source-attributed provisioning hypotheses can remain explicitly hypothetical.
- Preserve observed CFU/host traits and mechanistic alternatives. Do not substitute another speculative role or treat missing optional roles as a defect.

### repair-cultivation

Document source-specific recipes, preparation and host assay context.

- Add the complete nine-component 2014 MMRS recipe with reported forms/units and direct Methods evidence. Preserve 30 °C stocks, CO2 plate handling, 25 °C host conditions and 12:12 h cycle.
- Keep 2014 equal-part 50 µL inoculation separate from 2015 MRS broth durations, 7.5 mL food/50 mL tubes and different preservatives. Do not import the 2011 survey diet into the defined assay.
- Qualify or remove FACULTATIVE_ANAEROBIC if it lacks source-specific physiological support; report actual aerobic/CO2 stages without inferring exact oxygen concentration or anaerobic mixture.

### repair-gtdb

Record reproducible mapping provenance at the correct taxon scope.

- Replace latest/build wording with verified local snapshot hash, retrieval context and mapping method. Filesystem mtime is not a GTDB release/build date.
- Re-ground resolved species independently; preserve two Acetobacter ambiguities and distinguish other verified species routes from exact DmelCS genome classification. Do not transplant old genus confidence/counts to strains.

### repair-resources

Keep publication citations and actual datasets distinct.

- Retain all three verified articles as publication/external references with their study roles.
- If adding source survey data, use verified SRA study/run metadata and explicitly pooled 454 16S scope; keep HQ173707–HQ173711 as clone markers, not isolate genomes or phenotype datasets.
- Do not infer an absent deposit from unqueried archives or the unavailable 2011 supplement details.

### validate-curation

Validate any separately authorized future curation.

- Run focused schema, strict, term-label, reference, GTDB/domain and history checks after changes.
- Preserve all source/correction receipts and existing causal limitations; do not edit caches or histories to make validation pass.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | kb/communities/Drosophila_FiveSpecies_Gnotobiotic_Gut_Microbiota.yaml; Whole maintained YAML | supports | Defined five-species gnotobiotic microbiota, three qualified phenotype nodes and one PARTIAL abundance-mediated arrow. |
| cultivation | PMID:24242251; DOI:10.1128/AEM.02742-13; Materials and Methods, Preparation of axenic and gnotobiotic flies, sole direct paragraph; XPath //*[@id="sec2-2"]/p[1] | supports | Fifty microliters at 10^8 cells/mL supplies five million cells per vial, with one million of each species in the five-member treatment. |
| medium | PMID:24242251; DOI:10.1128/AEM.02742-13; Materials and Methods, Cultivation of bacteria and flies, sole direct paragraph; XPath //*[@id="sec2-1"]/p[1] | supports | The nine-component MMRS formulation and 30 °C stock maintenance are separate from 25 °C host Y-G culture. Lactobacillus plates were in CO2-gassed sealed containers. |
| stocks | PMID:25692519; DOI:10.1038/ncomms7312; Methods, The flies, first direct paragraph; XPath //*[@id="S8"]/p[1] | supports | All five DmelCS codes are explicit. This study separately specifies MRS plate/broth stages, food volume, tube capacity and host diet. |
| tag | PMID:24242251; DOI:10.1128/AEM.02742-13; Results, Effects of defined microbiota on nutritional indices of Drosophila and Impacts of dual-species microbiota; Figures 2–3; Abstract | supports | Tested mixed communities alter host triglycerides, with different effects among species pairs. This is not a demonstrated nutrient exchange. |
| abundance | PMID:24242251; DOI:10.1128/AEM.02742-13; Results, Impact of interspecies interactions on bacterial abundance, second direct paragraph; Figure 5; XPath //*[@id="sec3-4"]/p[2] | supports | L. brevis and L. fructivorans promote whole-fly Acetobacter CFU in tested pairs; L. plantarum does not significantly do so. Reciprocal effects differ. |
| mediation | PMID:24242251; DOI:10.1128/AEM.02742-13; Results, Correlation between Acetobacter abundance and host phenotypes, second direct paragraph; Figure 6; XPath //*[@id="sec3-5"]/p[2] | supports | Changing L. brevis inoculum with fixed A. tropicalis supports an abundance-associated TAG model but does not selectively establish Acetobacter abundance as the mediator. |
| role-limits | PMID:24242251; DOI:10.1128/AEM.02742-13; Discussion, fourth and fifth direct paragraphs; XPath //*[@id="sec4"]/p[4] and p[5] | supports | Nutrient provisioning is proposed alongside host-environment and diet-mediated alternatives. Metabolite utilization and secondary fermentation are not demonstrated for the four group-wide role assignments. |
| host-genotype | PMID:25692519; DOI:10.1038/ncomms7312; Results and Figures 1–2; Discussion, first direct paragraph; Methods The flies | supports | The direction and magnitude of host nutritional responses vary among genetic lines. Host GWAS and mutant tests are distinct from microbial gene expression or exchange. |
| survey | PMID:21631690; DOI:10.1111/j.1462-2920.2011.02511.x; Results, Taxonomic composition of bacteria identified by pyrosequencing; Discussion, fifth paragraph; Experimental procedures | supports | The survey identifies five dominant OTUs across developmental contexts and explicitly lacks bacterial functional-gene information. It is not the defined five-stock inoculation experiment. |
| supplement | PMID:25692519; DOI:10.1038/ncomms7312; Publisher supplementary PDF: physical pages 1–14 and 67–75; Figures S1–S7, Tables S1/S2/S5/S6/S7 and Note 1 | supports | All selected text and nine figure pages were read. Bulk SNP and GO Tables S3/S4 were inventoried with headers/initial displayed rows, not fully reanalysed. |
| correction | PMID:25976209; DOI:10.1038/ncomms8296; Corrigendum body and corrected Figure 1, corresponding to parent Supplementary Figure 5b | supports | The top-row glycogen and glucose panels were switched. The correction was read and its official thumbnail viewed separately from the original SI; no global result reversal is inferred. |
| inspection | /private/tmp/cm-review-session/batch-16/000160/inspect.json; Official 33-input inspection | supports | Target, 21 authorities and eleven focal contexts pinned before assessment. |
| ontology | /private/tmp/cm-review-session/batch-16/000160/ontology-authority.json; Ten distinct OAK pairs and nineteen placements | supports | All encoded labels match; label validity does not establish microbial membership or historical genus circumscription. |
| schema | /private/tmp/cm-review-session/batch-16/000160/child-schema-semantics.json; Current role, interaction and growth-medium definitions | supports | Cross-feeder utilization and secondary fermentation require their literal source support; no added obligacy criterion. |
| schema-fields | /private/tmp/cm-review-session/batch-16/000160/child-schema-field-addendum.json; Taxonomy membership and atmosphere definitions | supports | Hosts are excluded from microbial taxonomy membership but can remain interaction participants. Atmosphere is a requirement category, distinct from the reported protocol. |
| species | /private/tmp/cm-review-session/batch-16/000160/child-source-species-candidates.json; Exact five source species and current NCBI parents | supports | All five stock codes are verified; the three historical Lactobacillus species now belong to different genera. Species identifiers are not strain identifiers. |
| gtdb | /private/tmp/cm-review-session/batch-16/000160/child-gtdb-crosswalk.json; Both encoded genus mapping cores | supports | The numerical mappings reproduce within their taxon scope; latest/build wording is not verified release metadata. |
| adapter | /private/tmp/cm-review-session/batch-16/000160/child-structured-adapter-applicability.json; Host GWAS/P-element and rg context | supports | The runner is unavailable in the owned runtime, so host dataset coverage is unverified. No bacterial namesake or expression inference is made. |
| semantics | /private/tmp/cm-review-session/batch-16/000160/ontology-semantic-notes.json; Final source-aware auxiliary conclusions | supports | Two major and three minor groups; preserve observed graph phenotypes and partial mediation. |
| resources | /private/tmp/cm-review-session/batch-16/000160/dataset-verification.json; Source-declared SRA study/run and five clone-marker metadata | supports | One pooled 454 16S survey run and five 270 bp uncultured clone markers are verified; none is an exact DmelCS isolate genome. |
| links | /private/tmp/cm-review-session/batch-16/000160/external-resource-verification.json; Three publication identities and bibliography/data distinction | supports | Current PubMed links identify publications, not independent dataset accessions. |
| snippets | /private/tmp/cm-review-session/batch-16/000160/snippet-audit.json; All twelve canonical excerpt placements | supports | All twelve strictly match fresh Abstracts and selected caches. |
| provenance | /private/tmp/cm-review-session/batch-16/000160/provenance-audit.json; Focal histories, exact batch 33 row, cohort and current issues | supports | Historical graph repairs are independently tested; issue state and prior decisions are preserved. |
| assets | /private/tmp/cm-review-session/batch-16/000160/lead-source-assets.json; Primary retrievals, actual file magic and source assets | supports | All three main articles and eleven main figures recovered. Failed XML and 2011 SI responses are classified separately from scientific content. |
| read-scope | /private/tmp/cm-review-session/batch-16/000160/lead-primary-read-scope.json; Actual lead whole-main and bounded supplementary reading | supports | All three complete main projections, eleven main figures, selected 2015 SI and actual corrigendum were read. |
| locators | /private/tmp/cm-review-session/batch-16/000160/source-locator-verification.json; Actual heading and paragraph inventory | supports | Direct source locators and the two-word quote were checked against current HTML. |
| source-audit | /private/tmp/cm-review-session/batch-16/000160/source-audit.json; Final lead scientific assessment | supports | Completed scientific review: two P2 and three P3 findings, with all four node hashes and one arrow bound. |
| root-source | /private/tmp/cm-review-session/batch-16/000160/root-independent-source-audit.json; Independent root source review | supports | Independent source, figure, supplement, correction and authority review agrees with the final findings. |
| support | /private/tmp/cm-review-session/batch-16/000160/support-final-audit.json; Final supporting reconciliation | supports | Literal completeness 30; quality base 128.33333333333331 minus 26 gives 102.33333333333331, capped at 100. |
| support-manifest | /private/tmp/cm-review-session/batch-16/000160/support-frozen-manifest.json; Frozen supporting artifacts | supports | Current provenance, source, resource and input hashes retained. |
| auxiliary | /private/tmp/cm-review-session/batch-16/000160/auxiliary-frozen-manifest.json; Frozen native and authority artifacts | supports | All eight required native checks pass; no source failure is counted as a candidate failure. |
| native-summary | /private/tmp/cm-review-session/batch-16/000160/final-validator-summary.json; Actual eight native receipts | supports | All required commands exited 0; reference validation and scientific support remain separate. |
| corpus-context | /private/tmp/cm-review-session/batch-16/000160/child-corpus-context.json; Fresh batch 16 corpus baseline | supports | Actual warning-only corpus exits are contextual, not target failures. |
| check-validate | /private/tmp/cm-review-session/batch-16/000160/validate.json; Actual command/stdout/stderr | supports | Required native command exited 0. |
| check-validate-strict | /private/tmp/cm-review-session/batch-16/000160/validate-strict.json; Actual command/stdout/stderr | supports | Required native command exited 0. |
| check-validate-terms | /private/tmp/cm-review-session/batch-16/000160/validate-terms.json; Actual command/stdout/stderr | supports | Required native command exited 0. |
| check-validate-references-explained | /private/tmp/cm-review-session/batch-16/000160/validate-references-explained.json; Actual command/stdout/stderr | supports | Required native command exited 0. |
| check-validate-gtdb | /private/tmp/cm-review-session/batch-16/000160/validate-gtdb.json; Actual command/stdout/stderr | supports | Required native command exited 0. |
| check-validate-gtdb-domain | /private/tmp/cm-review-session/batch-16/000160/validate-gtdb-domain.json; Actual command/stdout/stderr | supports | Required native command exited 0. |
| check-validate-history | /private/tmp/cm-review-session/batch-16/000160/validate-history.json; Actual command/stdout/stderr | supports | Required native command exited 0. |
| check-normalize-cache-names-check | /private/tmp/cm-review-session/batch-16/000160/normalize-cache-names-check.json; Actual command/stdout/stderr | supports | Required native command exited 0. |
| context-audit-network | /private/tmp/cm-review-session/batch-16/audit-network.json; Fresh batch 16 corpus baseline | supports | Warning-only actual corpus exit 1 retained. |
| context-check-network-quality | /private/tmp/cm-review-session/batch-16/check-network-quality.json; Fresh batch 16 corpus baseline | supports | Warning-only actual corpus exit 1 retained. |

## Limits And Additional Notes

- The five 2011 supplementary objects were not recovered by the preserved public routes. Current claims were adjudicated from the complete main survey; no conclusion relies on unseen supplementary data.
- 2015 SI bulk SNP and GO Tables S3/S4 were only inventoried with headers and initial displayed rows. Selected Tables S1/S2/S5/S6/S7, Note 1 and all Figures S1–S7 were read; no GWAS or raw-sequence reanalysis was performed.
- The original S5b panels and actual corrigendum were kept separate. The corrected image was a thumbnail, used for panel arrangement rather than quantitative extraction. The main and SI table/cross-reference numbering differ in places.
- Whole-fly CFU does not establish persistent intestinal residence or growth rates; the PARTIAL mediation arrow is not a selective causal experiment. No microbial metabolite exchange is demonstrated by the reported host outcomes.
- Source species, historical names, DmelCS stock codes, survey OTUs and generic GTDB mappings have different scopes. Exact stock genomes and strain CURIEs were not established.
- The optional structured adapter could not run in the owned environment. Host GWAS/P-element relevance was considered explicitly, but organism/dataset coverage remains unknown.
- Completion concerns this record review at the stated scope; it does not authorize curation, issue changes or source-cache restoration.
- All 33 official input hashes remain unchanged. Eight evidence-linked dimensions, four exact graph snippet hashes and the single arrow binding are explicit.
- Required native checks passed. Access and ad hoc display failures are retained separately; candidate validation is recorded after this actual file is rendered.
- Lead read the whole canonical record and focal histories; supporting reviewers independently own the full cache, prior/cohort and current issue scopes recorded in their receipts.
- The direct source quote contains two words. Root alone saves the accepted review and runs post-save gates.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T073419Z-drosophila-five-species-record-review
kind: record
repository: CultureBotAI/CommunityMech
title: Drosophila five-species gnotobiotic microbiota record review
started_at: '2026-10-22T07:18:40.584673Z'
finished_at: '2026-10-22T07:34:19.937956Z'
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
summary: The five source stocks and three qualified host-phenotype observations are
  supported. Two major findings concern microbial membership/current species scope
  and unproven metabolic roles; three minor findings concern cultivation, GTDB provenance
  and publication-shaped datasets. All eight required native checks passed. Completeness
  is 30; raw quality 102.33333333333331 is capped at 100.
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
  - path: history/infrastructure/paywalled-text-removal/2026-09-13T010148Z-codex-8e69ec.yaml
    sha256: 6c63fb0af1321aba4741fdc11f601840bae0a08feb79a4d617ad59e64c05e0fe
    role: context
  - path: history/records/Drosophila_FiveSpecies_Gnotobiotic_Gut_Microbiota/2026-10-06T070210Z-codex-1499d8.yaml
    sha256: ac4c7f1848af50f53ab3d17c28dc6fa2c856c3ad22b844f43d0bf97bade947d6
    role: context
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: kb/communities/Drosophila_FiveSpecies_Gnotobiotic_Gut_Microbiota.yaml
    sha256: b4b58e41f802bbff0ca7c31fd870d6b11bea6c7ead8bd8201b896c45ebfb6efe
    role: target
  - path: references_cache/PMID_21631690.txt
    sha256: b9ffb3711a98344a5be9ced41ca190b05192e3e8281a4a9ca58d1baa87f339aa
    role: context
  - path: references_cache/PMID_24242251.txt
    sha256: a42381b59ad449f49cf605dc11072110ab668bc07b7d9bc6054a6e5ce4285701
    role: context
  - path: references_cache/PMID_25692519.txt
    sha256: 3f7a62ba602c81e5624dfb09272305fdbe8f21f34e213a15b93b29ddb4c27ec5
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
- target_id: CommunityMech:000160
  path: kb/communities/Drosophila_FiveSpecies_Gnotobiotic_Gut_Microbiota.yaml
  label: Drosophila Five-Species Gnotobiotic Gut Microbiota
  kind: maintained
  record_class: MicrobialCommunity
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Drosophila_FiveSpecies_Gnotobiotic_Gut_Microbiota.yaml
    role: canonical_record
scope:
  description: Whole released record and three complete source articles, eleven main
    figures, relevant 2015 supplements and actual corrigendum; local native/authority
    checks and bounded source-declared archive metadata.
  selection: Only released CommunityMech:000160 in owned batch 16.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000160
checks:
- check_id: validate
  name: validate
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000160
  command: just --no-dotenv validate kb/communities/Drosophila_FiveSpecies_Gnotobiotic_Gut_Microbiota.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate
  scope_note: Focused record/history check; cache-name preflight is corpus-wide. Scientific
    support is separately assessed.
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000160
  command: just --no-dotenv validate-strict kb/communities/Drosophila_FiveSpecies_Gnotobiotic_Gut_Microbiota.yaml
    --out /private/tmp/cm-review-session/batch-16/000160/strict-report.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-strict
  scope_note: Focused record/history check; cache-name preflight is corpus-wide. Scientific
    support is separately assessed.
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000160
  command: just --no-dotenv validate-terms kb/communities/Drosophila_FiveSpecies_Gnotobiotic_Gut_Microbiota.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-terms
  scope_note: Focused record/history check; cache-name preflight is corpus-wide. Scientific
    support is separately assessed.
- check_id: validate-references-explained
  name: validate-references-explained
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000160
  command: just --no-dotenv validate-references-explained kb/communities/Drosophila_FiveSpecies_Gnotobiotic_Gut_Microbiota.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-references-explained
  scope_note: Focused record/history check; cache-name preflight is corpus-wide. Scientific
    support is separately assessed.
- check_id: validate-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000160
  command: just --no-dotenv validate-gtdb kb/communities/Drosophila_FiveSpecies_Gnotobiotic_Gut_Microbiota.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb
  scope_note: Focused record/history check; cache-name preflight is corpus-wide. Scientific
    support is separately assessed.
- check_id: validate-gtdb-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000160
  command: just --no-dotenv validate-gtdb-domain kb/communities/Drosophila_FiveSpecies_Gnotobiotic_Gut_Microbiota.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb-domain
  scope_note: Focused record/history check; cache-name preflight is corpus-wide. Scientific
    support is separately assessed.
- check_id: validate-history
  name: validate-history
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000160
  command: just --no-dotenv validate-history history/records/Drosophila_FiveSpecies_Gnotobiotic_Gut_Microbiota
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-history
  scope_note: Focused record/history check; cache-name preflight is corpus-wide. Scientific
    support is separately assessed.
- check_id: normalize-cache-names-check
  name: normalize-cache-names-check
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000160
  command: uv run python scripts/normalize_cache_names.py --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-normalize-cache-names-check
  scope_note: Focused record/history check; cache-name preflight is corpus-wide. Scientific
    support is separately assessed.
- check_id: context-audit-network
  name: audit-network corpus context
  status: failed
  required: false
  summary: Actual corpus exit 1, zero structural errors.
  target_ids:
  - CommunityMech:000160
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-16/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv audit-network
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - context-audit-network
  - corpus-context
  scope_note: Nonrequired corpus context; not a focused native or candidate failure.
- check_id: context-check-network-quality
  name: check-network-quality corpus context
  status: failed
  required: false
  summary: Actual corpus exit 1, zero structural errors.
  target_ids:
  - CommunityMech:000160
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-16/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv check-network-quality
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - context-check-network-quality
  - corpus-context
  scope_note: Nonrequired corpus context; not a focused native or candidate failure.
- check_id: structured-adapter
  name: Host-specific structured adapter applicability
  status: unavailable
  required: false
  summary: Runner unavailable in the owned environment; host dataset coverage unverified.
  target_ids:
  - CommunityMech:000160
  evidence_ids:
  - adapter
  scope_note: The actual study concerns Drosophila GWAS and host perturbations, not
    bacterial genes. Primary sources provide the available evidence; no biological
    absence inference.
evidence:
- evidence_id: record
  kind: record_content
  reference: kb/communities/Drosophila_FiveSpecies_Gnotobiotic_Gut_Microbiota.yaml
  locator: Whole maintained YAML
  summary: Defined five-species gnotobiotic microbiota, three qualified phenotype
    nodes and one PARTIAL abundance-mediated arrow.
  support: supports
  accessed_at: '2026-10-22T07:32:34.884988Z'
- evidence_id: cultivation
  kind: primary_source
  reference: PMID:24242251; DOI:10.1128/AEM.02742-13
  locator: Materials and Methods, Preparation of axenic and gnotobiotic flies, sole
    direct paragraph; XPath //*[@id="sec2-2"]/p[1]
  summary: Fifty microliters at 10^8 cells/mL supplies five million cells per vial,
    with one million of each species in the five-member treatment.
  support: supports
  accessed_at: '2026-10-22T07:32:34.885075Z'
  snapshot_sha256: 04e54de1170e139b6f9586df0034219996d98bc60c0911058d4abe21799ad04c
  quote: equal parts
- evidence_id: medium
  kind: primary_source
  reference: PMID:24242251; DOI:10.1128/AEM.02742-13
  locator: Materials and Methods, Cultivation of bacteria and flies, sole direct paragraph;
    XPath //*[@id="sec2-1"]/p[1]
  summary: The nine-component MMRS formulation and 30 °C stock maintenance are separate
    from 25 °C host Y-G culture. Lactobacillus plates were in CO2-gassed sealed containers.
  support: supports
  accessed_at: '2026-10-22T07:32:34.885537Z'
  snapshot_sha256: 04e54de1170e139b6f9586df0034219996d98bc60c0911058d4abe21799ad04c
- evidence_id: stocks
  kind: primary_source
  reference: PMID:25692519; DOI:10.1038/ncomms7312
  locator: Methods, The flies, first direct paragraph; XPath //*[@id="S8"]/p[1]
  summary: All five DmelCS codes are explicit. This study separately specifies MRS
    plate/broth stages, food volume, tube capacity and host diet.
  support: supports
  accessed_at: '2026-10-22T07:32:34.885652Z'
  snapshot_sha256: 5e2b1b4697fef0f3395d0a95491e056e059712a4924d81c4292f124a93eeb613
- evidence_id: tag
  kind: primary_source
  reference: PMID:24242251; DOI:10.1128/AEM.02742-13
  locator: Results, Effects of defined microbiota on nutritional indices of Drosophila
    and Impacts of dual-species microbiota; Figures 2–3; Abstract
  summary: Tested mixed communities alter host triglycerides, with different effects
    among species pairs. This is not a demonstrated nutrient exchange.
  support: supports
  accessed_at: '2026-10-22T07:32:34.886078Z'
  snapshot_sha256: 04e54de1170e139b6f9586df0034219996d98bc60c0911058d4abe21799ad04c
- evidence_id: abundance
  kind: primary_source
  reference: PMID:24242251; DOI:10.1128/AEM.02742-13
  locator: Results, Impact of interspecies interactions on bacterial abundance, second
    direct paragraph; Figure 5; XPath //*[@id="sec3-4"]/p[2]
  summary: L. brevis and L. fructivorans promote whole-fly Acetobacter CFU in tested
    pairs; L. plantarum does not significantly do so. Reciprocal effects differ.
  support: supports
  accessed_at: '2026-10-22T07:32:34.886179Z'
  snapshot_sha256: 04e54de1170e139b6f9586df0034219996d98bc60c0911058d4abe21799ad04c
- evidence_id: mediation
  kind: primary_source
  reference: PMID:24242251; DOI:10.1128/AEM.02742-13
  locator: Results, Correlation between Acetobacter abundance and host phenotypes,
    second direct paragraph; Figure 6; XPath //*[@id="sec3-5"]/p[2]
  summary: Changing L. brevis inoculum with fixed A. tropicalis supports an abundance-associated
    TAG model but does not selectively establish Acetobacter abundance as the mediator.
  support: supports
  accessed_at: '2026-10-22T07:32:34.886277Z'
  snapshot_sha256: 04e54de1170e139b6f9586df0034219996d98bc60c0911058d4abe21799ad04c
- evidence_id: role-limits
  kind: primary_source
  reference: PMID:24242251; DOI:10.1128/AEM.02742-13
  locator: Discussion, fourth and fifth direct paragraphs; XPath //*[@id="sec4"]/p[4]
    and p[5]
  summary: Nutrient provisioning is proposed alongside host-environment and diet-mediated
    alternatives. Metabolite utilization and secondary fermentation are not demonstrated
    for the four group-wide role assignments.
  support: supports
  accessed_at: '2026-10-22T07:32:34.886373Z'
  snapshot_sha256: 04e54de1170e139b6f9586df0034219996d98bc60c0911058d4abe21799ad04c
- evidence_id: host-genotype
  kind: primary_source
  reference: PMID:25692519; DOI:10.1038/ncomms7312
  locator: Results and Figures 1–2; Discussion, first direct paragraph; Methods The
    flies
  summary: The direction and magnitude of host nutritional responses vary among genetic
    lines. Host GWAS and mutant tests are distinct from microbial gene expression
    or exchange.
  support: supports
  accessed_at: '2026-10-22T07:32:34.886470Z'
  snapshot_sha256: 5e2b1b4697fef0f3395d0a95491e056e059712a4924d81c4292f124a93eeb613
- evidence_id: survey
  kind: primary_source
  reference: PMID:21631690; DOI:10.1111/j.1462-2920.2011.02511.x
  locator: Results, Taxonomic composition of bacteria identified by pyrosequencing;
    Discussion, fifth paragraph; Experimental procedures
  summary: The survey identifies five dominant OTUs across developmental contexts
    and explicitly lacks bacterial functional-gene information. It is not the defined
    five-stock inoculation experiment.
  support: supports
  accessed_at: '2026-10-22T07:32:34.886569Z'
  snapshot_sha256: c9f77e8e71e1f9fe41613148653704af345e7b90330a6dd13071ae7f558052fc
- evidence_id: supplement
  kind: primary_source
  reference: PMID:25692519; DOI:10.1038/ncomms7312
  locator: 'Publisher supplementary PDF: physical pages 1–14 and 67–75; Figures S1–S7,
    Tables S1/S2/S5/S6/S7 and Note 1'
  summary: All selected text and nine figure pages were read. Bulk SNP and GO Tables
    S3/S4 were inventoried with headers/initial displayed rows, not fully reanalysed.
  support: supports
  accessed_at: '2026-10-22T07:32:34.887028Z'
  snapshot_sha256: 279d6484d85fdb9418132cdef60084f5b23b93baa355e2a4aeeda779354e1714
- evidence_id: correction
  kind: primary_source
  reference: PMID:25976209; DOI:10.1038/ncomms8296
  locator: Corrigendum body and corrected Figure 1, corresponding to parent Supplementary
    Figure 5b
  summary: The top-row glycogen and glucose panels were switched. The correction was
    read and its official thumbnail viewed separately from the original SI; no global
    result reversal is inferred.
  support: supports
  accessed_at: '2026-10-22T07:32:34.887223Z'
  snapshot_sha256: eb1267635ccf0ea0d7c3809448d868ab8cf3f87719edf847ee57588071cad59b
- evidence_id: inspection
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000160/inspect.json
  locator: Official 33-input inspection
  summary: Target, 21 authorities and eleven focal contexts pinned before assessment.
  support: supports
  accessed_at: '2026-10-22T07:32:34.887658Z'
  snapshot_sha256: a782be79b5c0c8329f4b205662008d4e9730fd6090085b27be2a6d97ef065042
- evidence_id: ontology
  kind: authority
  reference: /private/tmp/cm-review-session/batch-16/000160/ontology-authority.json
  locator: Ten distinct OAK pairs and nineteen placements
  summary: All encoded labels match; label validity does not establish microbial membership
    or historical genus circumscription.
  support: supports
  accessed_at: '2026-10-22T07:32:34.887692Z'
  snapshot_sha256: 79057eade2356cf1e1d4a7757e26145b991293c5533e43fccb1ffd9ecccfe117
- evidence_id: schema
  kind: authority
  reference: /private/tmp/cm-review-session/batch-16/000160/child-schema-semantics.json
  locator: Current role, interaction and growth-medium definitions
  summary: Cross-feeder utilization and secondary fermentation require their literal
    source support; no added obligacy criterion.
  support: supports
  accessed_at: '2026-10-22T07:32:34.887857Z'
  snapshot_sha256: e5c4a57da6171c49b34fa7b1a908d6ba66e3dbfeb868b37f4c321387de2c0a4b
- evidence_id: schema-fields
  kind: authority
  reference: /private/tmp/cm-review-session/batch-16/000160/child-schema-field-addendum.json
  locator: Taxonomy membership and atmosphere definitions
  summary: Hosts are excluded from microbial taxonomy membership but can remain interaction
    participants. Atmosphere is a requirement category, distinct from the reported
    protocol.
  support: supports
  accessed_at: '2026-10-22T07:32:34.888053Z'
  snapshot_sha256: ac06099e00859d17400c339366334b1c73e0ccbb3811f444518c15277df650a8
- evidence_id: species
  kind: authority
  reference: /private/tmp/cm-review-session/batch-16/000160/child-source-species-candidates.json
  locator: Exact five source species and current NCBI parents
  summary: All five stock codes are verified; the three historical Lactobacillus species
    now belong to different genera. Species identifiers are not strain identifiers.
  support: supports
  accessed_at: '2026-10-22T07:32:34.888182Z'
  snapshot_sha256: 38d13820543bc06ff0276c73e22f0e1f0f8e53cc0228da58cd232fcdae3f8888
- evidence_id: gtdb
  kind: authority
  reference: /private/tmp/cm-review-session/batch-16/000160/child-gtdb-crosswalk.json
  locator: Both encoded genus mapping cores
  summary: The numerical mappings reproduce within their taxon scope; latest/build
    wording is not verified release metadata.
  support: supports
  accessed_at: '2026-10-22T07:32:34.888370Z'
  snapshot_sha256: 10469e272438a4d99f0cf9c71c0309edc36b6d06f9ef0ec0a758d5c4756b4cc4
- evidence_id: adapter
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000160/child-structured-adapter-applicability.json
  locator: Host GWAS/P-element and rg context
  summary: The runner is unavailable in the owned runtime, so host dataset coverage
    is unverified. No bacterial namesake or expression inference is made.
  support: supports
  accessed_at: '2026-10-22T07:32:34.888502Z'
  snapshot_sha256: 173d3aa0ea59d800bd4bdb81b314b6afcc2964b8d5fda0e637b80f5db2dda782
- evidence_id: semantics
  kind: authority
  reference: /private/tmp/cm-review-session/batch-16/000160/ontology-semantic-notes.json
  locator: Final source-aware auxiliary conclusions
  summary: Two major and three minor groups; preserve observed graph phenotypes and
    partial mediation.
  support: supports
  accessed_at: '2026-10-22T07:32:34.888590Z'
  snapshot_sha256: 617b232ef9858207e81f4cb1ea65b052f3711a820a00582b37d69f08eaff54c6
- evidence_id: resources
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000160/dataset-verification.json
  locator: Source-declared SRA study/run and five clone-marker metadata
  summary: One pooled 454 16S survey run and five 270 bp uncultured clone markers
    are verified; none is an exact DmelCS isolate genome.
  support: supports
  accessed_at: '2026-10-22T07:32:34.888778Z'
  snapshot_sha256: e53c4514a68861a1c2b3a8f59e42465d9262dbf798fd65f3d1afeac117a77e91
- evidence_id: links
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000160/external-resource-verification.json
  locator: Three publication identities and bibliography/data distinction
  summary: Current PubMed links identify publications, not independent dataset accessions.
  support: supports
  accessed_at: '2026-10-22T07:32:34.888935Z'
  snapshot_sha256: 6eb724cf446cc7dedc956bda1d1f297969f0bc29fb60b94ca39fd0de86e7c795
- evidence_id: snippets
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000160/snippet-audit.json
  locator: All twelve canonical excerpt placements
  summary: All twelve strictly match fresh Abstracts and selected caches.
  support: supports
  accessed_at: '2026-10-22T07:32:34.889031Z'
  snapshot_sha256: 7403a706a9ea47e137bbd559550a246c00cb7cc673be6720140cfbb777958622
- evidence_id: provenance
  kind: prior_review
  reference: /private/tmp/cm-review-session/batch-16/000160/provenance-audit.json
  locator: Focal histories, exact batch 33 row, cohort and current issues
  summary: Historical graph repairs are independently tested; issue state and prior
    decisions are preserved.
  support: supports
  accessed_at: '2026-10-22T07:32:34.889181Z'
  snapshot_sha256: d8c43acf04f01f1ed0bddb67bcb7443fe888db46abc7aa5aa6c620642b14af73
- evidence_id: assets
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000160/lead-source-assets.json
  locator: Primary retrievals, actual file magic and source assets
  summary: All three main articles and eleven main figures recovered. Failed XML and
    2011 SI responses are classified separately from scientific content.
  support: supports
  accessed_at: '2026-10-22T07:32:34.889304Z'
  snapshot_sha256: f306d134bd327acac8078ad27e3fddccc032db61874323699f2e2818d0ce6a66
- evidence_id: read-scope
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000160/lead-primary-read-scope.json
  locator: Actual lead whole-main and bounded supplementary reading
  summary: All three complete main projections, eleven main figures, selected 2015
    SI and actual corrigendum were read.
  support: supports
  accessed_at: '2026-10-22T07:32:34.889355Z'
  snapshot_sha256: 016ab034a3b6107671622997eb1ece3a59998ba881ebe0822d389c98172a6fb4
- evidence_id: locators
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000160/source-locator-verification.json
  locator: Actual heading and paragraph inventory
  summary: Direct source locators and the two-word quote were checked against current
    HTML.
  support: supports
  accessed_at: '2026-10-22T07:32:34.889498Z'
  snapshot_sha256: ea406b90b6779d273effc6b0b521b699b7c19359809c795ea8260b641fe5ad4b
- evidence_id: source-audit
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000160/source-audit.json
  locator: Final lead scientific assessment
  summary: 'Completed scientific review: two P2 and three P3 findings, with all four
    node hashes and one arrow bound.'
  support: supports
  accessed_at: '2026-10-22T07:32:34.889720Z'
  snapshot_sha256: f2a6aae9ad2471fb5db282df390b40cbe007509f66e4c087248563ac9b08f1db
- evidence_id: root-source
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000160/root-independent-source-audit.json
  locator: Independent root source review
  summary: Independent source, figure, supplement, correction and authority review
    agrees with the final findings.
  support: supports
  accessed_at: '2026-10-22T07:32:34.889854Z'
  snapshot_sha256: b12cb3a049e8fcf09af48694dfc3f9cd8dcc908e9753496b34f3e3eb45e5cb2a
- evidence_id: support
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000160/support-final-audit.json
  locator: Final supporting reconciliation
  summary: Literal completeness 30; quality base 128.33333333333331 minus 26 gives
    102.33333333333331, capped at 100.
  support: supports
  accessed_at: '2026-10-22T07:32:34.889974Z'
  snapshot_sha256: 1fe3467da3cbf126f78792423471d39bd626b9f32c3683b9328d96e30d22c2aa
- evidence_id: support-manifest
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000160/support-frozen-manifest.json
  locator: Frozen supporting artifacts
  summary: Current provenance, source, resource and input hashes retained.
  support: supports
  accessed_at: '2026-10-22T07:32:34.890103Z'
  snapshot_sha256: 0dea920b76e58dde815bae35c4c758e633d796e3c7ef0ca86e3236e259eaa3af
- evidence_id: auxiliary
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000160/auxiliary-frozen-manifest.json
  locator: Frozen native and authority artifacts
  summary: All eight required native checks pass; no source failure is counted as
    a candidate failure.
  support: supports
  accessed_at: '2026-10-22T07:32:34.890228Z'
  snapshot_sha256: 50c5714c1287dd001c8a3c0d2fe608f58d6ce8398f8e62d820cff06245fa00b0
- evidence_id: native-summary
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000160/final-validator-summary.json
  locator: Actual eight native receipts
  summary: All required commands exited 0; reference validation and scientific support
    remain separate.
  support: supports
  accessed_at: '2026-10-22T07:32:34.890404Z'
  snapshot_sha256: 06a4d09b8c792a68cd8686f0acef0995dd8eb5cd35ae93a8cf4a749e669f9428
- evidence_id: corpus-context
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000160/child-corpus-context.json
  locator: Fresh batch 16 corpus baseline
  summary: Actual warning-only corpus exits are contextual, not target failures.
  support: supports
  accessed_at: '2026-10-22T07:32:34.890546Z'
  snapshot_sha256: fdffb2c83865adb54e4cb7bafe1abcbf0d61c5589cc823b3ba6ffbbe18aa5e61
- evidence_id: check-validate
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000160/validate.json
  locator: Actual command/stdout/stderr
  summary: Required native command exited 0.
  support: supports
  accessed_at: '2026-10-22T07:32:34.890946Z'
  snapshot_sha256: 1f9ba9920a1b4a783d3200192941e80b8ad148c78ffbf54baeae926780e43d55
- evidence_id: check-validate-strict
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000160/validate-strict.json
  locator: Actual command/stdout/stderr
  summary: Required native command exited 0.
  support: supports
  accessed_at: '2026-10-22T07:32:34.891130Z'
  snapshot_sha256: cbfa6992a5d552890c56324671109c5ffa11be6828294c00789e772bc5d771ca
- evidence_id: check-validate-terms
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000160/validate-terms.json
  locator: Actual command/stdout/stderr
  summary: Required native command exited 0.
  support: supports
  accessed_at: '2026-10-22T07:32:34.891300Z'
  snapshot_sha256: 3e529dec95760d301e01c1a7b344836ddd6cc8cd00b4ca493e61c0ad694f6d2c
- evidence_id: check-validate-references-explained
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000160/validate-references-explained.json
  locator: Actual command/stdout/stderr
  summary: Required native command exited 0.
  support: supports
  accessed_at: '2026-10-22T07:32:34.891449Z'
  snapshot_sha256: e6f3a2ad3d600cff9acc87b51cc9009746279691f4bc27ec15cd4b6fc3f52c7a
- evidence_id: check-validate-gtdb
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000160/validate-gtdb.json
  locator: Actual command/stdout/stderr
  summary: Required native command exited 0.
  support: supports
  accessed_at: '2026-10-22T07:32:34.891615Z'
  snapshot_sha256: 4a2dfbb76886f6f452bb56f4e5c974a9e2b7a386156c94289fb290624983fc75
- evidence_id: check-validate-gtdb-domain
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000160/validate-gtdb-domain.json
  locator: Actual command/stdout/stderr
  summary: Required native command exited 0.
  support: supports
  accessed_at: '2026-10-22T07:32:34.891772Z'
  snapshot_sha256: bef2946c19cc6281da9628e2c2e8cbc86b7d7a62ee917ee89b421aa69910ba8d
- evidence_id: check-validate-history
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000160/validate-history.json
  locator: Actual command/stdout/stderr
  summary: Required native command exited 0.
  support: supports
  accessed_at: '2026-10-22T07:32:34.891938Z'
  snapshot_sha256: 82d8e76b362056be6ce400af0de907624cd36ae2939df37150302368abca7492
- evidence_id: check-normalize-cache-names-check
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000160/normalize-cache-names-check.json
  locator: Actual command/stdout/stderr
  summary: Required native command exited 0.
  support: supports
  accessed_at: '2026-10-22T07:32:34.892106Z'
  snapshot_sha256: 88275114b39d6ab165233027e8d797256696c923aea1367292da3f29c033183f
- evidence_id: context-audit-network
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/audit-network.json
  locator: Fresh batch 16 corpus baseline
  summary: Warning-only actual corpus exit 1 retained.
  support: supports
  accessed_at: '2026-10-22T07:32:34.892314Z'
  snapshot_sha256: f4809c6a349f1496dbfe0243fb5ce661f469f7235f2aa00e6294ee3aa04f3123
- evidence_id: context-check-network-quality
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/check-network-quality.json
  locator: Fresh batch 16 corpus baseline
  summary: Warning-only actual corpus exit 1 retained.
  support: supports
  accessed_at: '2026-10-22T07:32:34.892487Z'
  snapshot_sha256: 759ba13f2cda067251275491bbafc401d0be8bddf7907c7f962eb4369f61688f
assessments:
- assessment_id: identity
  area: identity
  topic: Defined microbial membership and source stocks
  outcome: concern
  summary: The five-source-species identity is recoverable, but the host and historical
    genus aggregate need correction.
  target_ids:
  - CommunityMech:000160
  evidence_ids:
  - record
  - stocks
  - survey
  - species
  - schema-fields
  dimensions:
  - name: stable_id
    value: CommunityMech:000160; primary PMID:24242251 / PMC3911109 / DOI:10.1128/AEM.02742-13
    definition: One maintained record; the 2011 survey and 2015 host-genotype study
      have distinct evidence roles.
    evidence_ids:
    - record
    - inspection
    - links
  - name: source_strains
    value: A. pomorum DmelCS_004; A. tropicalis DmelCS_006; L. brevis DmelCS_003;
      L. fructivorans DmelCS_002; L. plantarum DmelCS_001
    definition: Exact source stock names are verified in 2015 Methods; no strain CURIE
      or genome is inferred from a species descriptor.
    evidence_ids:
    - stocks
    - species
  - name: community_scope
    value: Five bacterial isolates reintroduced into dechorionated fly hosts; mono-,
      dual- and five-member comparisons
    definition: The microbial membership excludes the host. Whole-fly measurements
      and the 2011 source survey are not interchangeable with persistent gut colonization
      or a complete ecological census.
    evidence_ids:
    - cultivation
    - stocks
    - survey
    - schema-fields
  details: Drosophila is the host, not a sixth microbial member. Current NCBITaxon:1578
    does not contain Levilactobacillus brevis, Fructilactobacillus fructivorans or
    Lactiplantibacillus plantarum. The two Acetobacter species remain in Acetobacter.
    Preserve historical source names as aliases, verified DmelCS designations and
    the host as an outside-community participant. Roster counts are not quantitative
    abundance.
- assessment_id: roles
  area: evidence
  topic: Metabolic role entailment
  outcome: concern
  summary: The four group-wide metabolic role tags exceed the demonstrated mechanism.
  target_ids:
  - CommunityMech:000160
  evidence_ids:
  - role-limits
  - schema
  - semantics
  details: CROSS_FEEDER means utilization of metabolites from other taxa; SECONDARY_FERMENTER
    means fermentation of products from primary degraders. The studies report host
    phenotypes and CFU responses, with provisioning as one hypothesis. Neither reciprocal
    CFU promotion nor supplied diet/MMRS establishes those roles for all members.
    This does not show that exchange is impossible, and no replacement role is invented.
- assessment_id: node-0
  area: graph
  topic: Joint host triglyceride outcome
  outcome: supported
  summary: Retain the qualified COMMUNITY_LEVEL outcome; mixed-pair effects differ
    and no exchange is established.
  target_ids:
  - CommunityMech:000160
  evidence_ids:
  - record
  - tag
  - snippets
  - ontology
  - semantics
  details: 'Exact selector ecological_interactions[0]. Current taxon/scope bindings:
    {"scope": "COMMUNITY_LEVEL", "participating_taxa": [{"preferred_term": "Drosophila
    gut Acetobacter isolates", "term": {"id": "NCBITaxon:434", "label": "Acetobacter"}},
    {"preferred_term": "Drosophila gut Lactobacillus isolates", "term": {"id": "NCBITaxon:1578",
    "label": "Lactobacillus"}}, {"preferred_term": "Drosophila melanogaster", "term":
    {"id": "NCBITaxon:7227", "label": "Drosophila melanogaster"}}]}. Exact canonical
    excerpt bindings: [{"selector": "ecological_interactions[0].evidence[0].snippet",
    "sha256": "9e61c0454017de30ba4e2634d196afdb92b8141e4208c28768c75900b31db789",
    "reference": "PMID:24242251", "supports": "SUPPORT", "evidence_source": "IN_VIVO"}].
    PMID:24242251, Results single- and dual-species comparisons and Figures 2–3 support
    host TAG effects. Host lipid-process and interspecies GO terms are context, not
    direct molecular flux. Species descriptors need the separately graded roster repair;
    no new interaction type is required.'
- assessment_id: node-1
  area: graph
  topic: Species-specific abundance promotion
  outcome: supported
  summary: Retain the observed PAIRWISE promotion in L. brevis/L. fructivorans contexts
    and the nonsignificant L. plantarum boundary.
  target_ids:
  - CommunityMech:000160
  evidence_ids:
  - record
  - abundance
  - snippets
  - ontology
  - semantics
  details: 'Exact selector ecological_interactions[1]. Current taxon/scope bindings:
    {"scope": "PAIRWISE", "source_taxon": {"preferred_term": "Drosophila gut Lactobacillus
    isolates", "term": {"id": "NCBITaxon:1578", "label": "Lactobacillus"}}, "target_taxon":
    {"preferred_term": "Drosophila gut Acetobacter isolates", "term": {"id": "NCBITaxon:434",
    "label": "Acetobacter"}}}. Exact canonical excerpt bindings: [{"selector": "ecological_interactions[1].evidence[0].snippet",
    "sha256": "ba4dd83d44e876d874912d34eb5255083267371033f1d8f7d18f03db907ce843",
    "reference": "PMID:24242251", "supports": "SUPPORT", "evidence_source": "IN_VIVO"}].
    PMID:24242251, Results abundance subsection paragraph 2 and Figure 5 support whole-fly
    CFU endpoints. CFU does not establish stable gut residence or growth rate. L.
    fructivorans is reduced in pairs and cannot be resolved in the mixed five-species
    CFU assay; do not infer biological absence.'
- assessment_id: node-2
  area: graph
  topic: Context-dependent host nutrition
  outcome: supported
  summary: Retain distinct 2014 and 2015 outcomes, including null and opposite-direction
    responses.
  target_ids:
  - CommunityMech:000160
  evidence_ids:
  - record
  - host-genotype
  - snippets
  - ontology
  - semantics
  - tag
  - correction
  details: 'Exact selector ecological_interactions[2]. Current taxon/scope bindings:
    {"scope": "COMMUNITY_LEVEL", "participating_taxa": [{"preferred_term": "Drosophila
    gut Acetobacter isolates", "term": {"id": "NCBITaxon:434", "label": "Acetobacter"}},
    {"preferred_term": "Drosophila gut Lactobacillus isolates", "term": {"id": "NCBITaxon:1578",
    "label": "Lactobacillus"}}, {"preferred_term": "Drosophila melanogaster", "term":
    {"id": "NCBITaxon:7227", "label": "Drosophila melanogaster"}}]}. Exact canonical
    excerpt bindings: [{"selector": "ecological_interactions[2].evidence[0].snippet",
    "sha256": "39772b5f4bea5a61f20ccb14cd8218c02842d635d96d71889bc54a2baa8052c6",
    "reference": "PMID:24242251", "supports": "SUPPORT", "evidence_source": "IN_VIVO"},
    {"selector": "ecological_interactions[2].evidence[1].snippet", "sha256": "247eccd82c5323a643ff4e2001e4ed7b8f8950dc5f7197ab97e3624d7345cea7",
    "reference": "PMID:25692519", "supports": "SUPPORT", "evidence_source": "IN_VIVO"}].
    PMID:24242251 Results and Figures 2–3 support glucose responses and the single/five-member
    null weight/protein/glycogen context. PMID:25692519 Figures 1–2 and Discussion
    paragraph 1 establish genotype-dependent responses. Growth/glucose GO terms and
    glucose/TAG CHEBI terms are host phenotype context, not exchange or universal
    benefit. The S5b correction is confined to its actual panels.'
- assessment_id: edge-1-0
  area: graph
  topic: Abundance promotion to host TAG outcome
  outcome: supported
  summary: Retain the explicitly PARTIAL proposed mediation.
  target_ids:
  - CommunityMech:000160
  evidence_ids:
  - mediation
  - abundance
  - tag
  - semantics
  details: 'Exact selector ecological_interactions[1].downstream[0]; target Acetobacter-Lactobacillus
    Nutrient Allocation Interaction. Exact description: PARTIAL - greater Acetobacter
    abundance could contribute to lower host triglycerides. Inoculum perturbations
    support this model but do not selectively establish abundance as the mediator.
    Description SHA256 8423b6c667b022baaf8d2fd052126648851e3eb6b6380af8b70dc1df4cceb97a.
    Figure 6 fixes A. tropicalis inoculum while varying L. brevis, with CFU/TAG associations;
    varying A. tropicalis alone did not establish the mediator. This supports a proposed
    direction without selective causal proof. When repairing species descriptors,
    attach this specific source evidence to the arrow; no additional arrow or grading
    penalty is warranted.'
- assessment_id: cultivation
  area: evidence
  topic: Source-specific microbial and host conditions
  outcome: concern
  summary: Recover the documented recipes and stages, with claim-local evidence.
  target_ids:
  - CommunityMech:000160
  evidence_ids:
  - medium
  - cultivation
  - stocks
  - schema-fields
  dimensions:
  - name: medium
    value: 2014 MMRS stocks and Y-G host diet; 2015 MRS stages and separately specified
      Y-G diet
    definition: '2014 Y-G: 100 g/L each yeast/glucose, 12 g/L agar, 0.04% phosphoric
      and 0.42% propionic acid. The 2015 preservative amounts double to 0.08% and
      0.84%; the 2011 survey uses 83 g/L yeast/glucose and 10 g/L agar.'
    evidence_ids:
    - medium
    - stocks
    - survey
  - name: experimental_setting
    value: 2014 50 µL inoculum at 10^8 cells/mL per vial; 2015 7.5 mL food in 50 mL
      Falcon tubes
    definition: Equal parts give one million cells per species in the five-member
      inoculum. Tube capacity and food volume are from 2015; no unstated 2014 vessel
      dimensions or shaking rate are inferred.
    evidence_ids:
    - cultivation
    - stocks
  - name: environment
    value: Stock maintenance at 30 °C; host rearing at 25 °C and 12:12 h light:dark;
      intestinal habitat
    definition: Lactobacillus plates are in CO2-gassed containers, with aerobic Acetobacter
      handling stated in 2015. Do not equate CO2 flushing with a specified anaerobic
      gas mixture or the broad facultative physiological requirement.
    evidence_ids:
    - medium
    - stocks
    - ontology
    - schema-fields
  details: The 2014 MMRS recipe is 1.25% vegetable peptone, 0.75% yeast extract, 2%
    glucose, 0.5% sodium acetate, 0.2% dipotassium hydrogen phosphate, 0.2% triammonium
    citrate, 0.02% magnesium sulfate heptahydrate, 0.005% manganese sulfate tetrahydrate
    and 1.2% agar. Retain reported units/forms. The current FACULTATIVE_ANAEROBIC
    category is not a substitute for source-specific aerobic/CO2 plate handling. The
    2015 MRS broths use overnight shaking for Acetobacter, overnight static L. brevis/L.
    plantarum and seven days static L. fructivorans; do not transfer these durations
    into the principal 2014 assay.
- assessment_id: grounding
  area: grounding
  topic: Current species scope and GTDB provenance
  outcome: concern
  summary: Valid labels and numeric genus mappings do not settle source isolate classification.
  target_ids:
  - CommunityMech:000160
  evidence_ids:
  - ontology
  - species
  - gtdb
  - semantics
  dimensions:
  - name: taxon_grounding
    value: 'Encoded: NCBITaxon:434 Acetobacter and NCBITaxon:1578 Lactobacillus; host
      NCBITaxon:7227. Proposed source species: NCBITaxon:65959, NCBITaxon:104102,
      NCBITaxon:1580, NCBITaxon:1614 and NCBITaxon:1590, with preserved DmelCS codes
      and separately grounded GTDB scope.'
    definition: Host NCBITaxon:7227 and NO_GTDB_EQUIVALENT are valid domain facts;
      removing host membership is required by community scope, not by an invalid host
      identifier.
    evidence_ids:
    - species
    - ontology
    - gtdb
    - schema-fields
  details: Encoded descriptors are NCBITaxon:434 Acetobacter, NCBITaxon:1578 Lactobacillus
    and host NCBITaxon:7227 Drosophila melanogaster. Proposed source species IDs are
    NCBITaxon:65959 Acetobacter pomorum, NCBITaxon:104102 Acetobacter tropicalis,
    NCBITaxon:1580 Levilactobacillus brevis, NCBITaxon:1614 Fructilactobacillus fructivorans
    and NCBITaxon:1590 Lactiplantibacillus plantarum; these are species descriptors,
    not exact DmelCS strain identifiers. Both Acetobacter species have ambiguous local
    name routes; the other species have verified local routes, each distinct from
    exact DmelCS strain classification. The existing genus totals 395/395 and 5369/5379
    reproduce, but latest/built 2026-07-25 is not validated release metadata.
- assessment_id: evidence-quality
  area: evidence
  topic: Claim-local evidence and phenotype interpretation
  outcome: supported
  summary: All twelve canonical snippets match; their scope still matters.
  target_ids:
  - CommunityMech:000160
  evidence_ids:
  - snippets
  - survey
  - role-limits
  - host-genotype
  - correction
  dimensions:
  - name: evidence_tier
    value: IN_VIVO host experiments, computational/16S survey identification, IN_VITRO
      stock preparation
    definition: Host GWAS associations and P-element perturbations are not bacterial
      expression or proof of microbial exchange; the source distinction survives literal
      snippet matching.
    evidence_ids:
    - survey
    - tag
    - host-genotype
    - medium
    - snippets
  details: The survey excerpts establish taxonomic OTUs, not exact stock genomes or
    cross-feeding. The graph correctly uses in-vivo host outcomes and keeps mediation
    partial. The corrected SI panel labels must accompany any later panel-specific
    host-gene interpretation.
- assessment_id: resources
  area: representation
  topic: Publication references versus actual datasets
  outcome: concern
  summary: Move bibliography-shaped dataset entries to publication links and scope
    genuine survey data separately.
  target_ids:
  - CommunityMech:000160
  evidence_ids:
  - resources
  - links
  - survey
  details: 'All three PMID/PubMed identifiers are correct publications. SRA023605.3
    resolves to SRP003313, SRX025956, SRR155572 and SAMN00109755: one pooled 454 16S
    survey run. HQ173707–HQ173711 are 270 bp uncultured clone markers. These are not
    exact cultured DmelCS isolate genomes, new phenotype datasets or strain-specific
    reference assemblies. No broad missing-archive search or raw-read reanalysis was
    performed.'
- assessment_id: source-scope
  area: scope
  topic: Full main evidence and bounded supplements
  outcome: supported
  summary: Current encoded claims were adjudicated from all three full articles, figures
    and relevant follow-up supplements.
  target_ids:
  - CommunityMech:000160
  evidence_ids:
  - assets
  - read-scope
  - locators
  - root-source
  - supplement
  - correction
  details: Lead read complete 2014, 2011 and 2015 main projections, including tables,
    captions and references, and all eleven main figures. The 2015 SI review covers
    all seven figures on nine pages, complete Tables S1/S2/S5/S6/S7 and Note 1. Bulk
    SNP/GO Tables S3/S4 were inventoried with headers/initial displayed rows only.
    Five 2011 supplements were not recovered; no claim depends on unseen supplementary
    details. Actual corrigendum text and corrected thumbnail were separately read.
    The optional structured adapter is unavailable in the owned runtime and host dataset
    coverage remains unknown.
- assessment_id: ownership
  area: ownership
  topic: Prior reviews and maintained-record ownership
  outcome: supported
  summary: The present audit preserves source history and existing graph qualifications.
  target_ids:
  - CommunityMech:000160
  evidence_ids:
  - inspection
  - provenance
  details: Support read the exact prior row, whole focal caches/history and bounded
    cohort/current issue context. Historical repair or issue status is not substituted
    for fresh source entailment. Any future curation belongs to the maintained record
    under separate authorization; this review changes no canonical YAML, cache, history
    or issue.
- assessment_id: native
  area: schema
  topic: Actual native validation
  outcome: supported
  summary: All eight required checks passed; the current network has no reported structural
    issues.
  target_ids:
  - CommunityMech:000160
  evidence_ids:
  - native-summary
  - auxiliary
  - schema
  - corpus-context
  details: Native COMPLETE does not establish correct community membership, metabolic
    exchange or complete source coverage. Retrieval and ad hoc display failures are
    distinct from native validation.
- assessment_id: metrics
  area: completeness
  topic: Literal rubric scores
  outcome: supported
  summary: Completeness 30; raw quality 102.33333333333331, capped at 100.
  target_ids:
  - CommunityMech:000160
  evidence_ids:
  - support
  metrics:
  - name: completeness
    value: 30
    unit: points
    minimum: 0
    maximum: 100
    definition: 0 required-fields-and-all-taxon-roles +5 environment +0 at least three
      factors +10 at least three nodes +0 external resources +10 growth medium +5
      associated datasets +0 node metabolites = 30. The combined 50-point role component
      is not granted; adding an invented host role is not a remedy.
  - name: validation_quality
    value: 100
    unit: points
    minimum: 0
    maximum: 100
    definition: 100 +20*min((4/3)/2,1) +15 COMPLETE -10*2 P2 -2*3 P3 = 102.33333333333331,
      capped at 100. Evidence and structural bonuses are not scientific truth.
  - name: P1
    value: 0
    unit: findings
    definition: Native severity count.
  - name: P2
    value: 2
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
- finding_id: membership
  issue_key: cm-000160-membership
  category: identity
  severity: major
  native_severity: P2
  normalization_reason: Membership or metabolic mechanism is materially misrepresented.
  rule_id: review-checklist.claim-specific-support-and-context
  status: open
  certainty: confirmed
  title: Resolve microbial members and preserve host context
  description: Host inclusion violates the membership slot, and the current Lactobacillus
    genus descriptor does not contain the three source species.
  target_ids:
  - CommunityMech:000160
  field_paths:
  - taxonomy
  - ecological_interactions[0].participating_taxa
  - ecological_interactions[1].source_taxon
  - ecological_interactions[1].target_taxon
  - ecological_interactions[2].participating_taxa
  evidence_ids:
  - stocks
  - species
  - schema-fields
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Drosophila_FiveSpecies_Gnotobiotic_Gut_Microbiota.yaml
    role: canonical_record
  ownership_note: Future maintained YAML curation only; preserve sources, caches,
    history and prior reviews.
- finding_id: roles
  issue_key: cm-000160-roles
  category: evidence
  severity: major
  native_severity: P2
  normalization_reason: Membership or metabolic mechanism is materially misrepresented.
  rule_id: review-checklist.claim-specific-support-and-context
  status: open
  certainty: confirmed
  title: Qualify unsupported metabolic roles
  description: CROSS_FEEDER and SECONDARY_FERMENTER are asserted for both groups without
    demonstrated partner-product utilization or fermentation.
  target_ids:
  - CommunityMech:000160
  field_paths:
  - taxonomy[0].functional_role
  - taxonomy[1].functional_role
  evidence_ids:
  - role-limits
  - schema
  - semantics
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Drosophila_FiveSpecies_Gnotobiotic_Gut_Microbiota.yaml
    role: canonical_record
  ownership_note: Future maintained YAML curation only; preserve sources, caches,
    history and prior reviews.
- finding_id: cultivation
  issue_key: cm-000160-cultivation
  category: representation
  severity: minor
  native_severity: P3
  normalization_reason: Bounded cultivation, provenance or resource representation
    repair; core phenotypes remain supported.
  rule_id: review-checklist.claim-specific-support-and-context
  status: open
  certainty: confirmed
  title: Separate source-specific media and preparation stages
  description: The maintained medium lacks source-local evidence and its physiological
    atmosphere category does not convey the distinct reported protocols. Recover the
    available recipe and study-specific stages.
  target_ids:
  - CommunityMech:000160
  field_paths:
  - growth_media
  - engineering_design
  evidence_ids:
  - medium
  - cultivation
  - stocks
  - schema-fields
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Drosophila_FiveSpecies_Gnotobiotic_Gut_Microbiota.yaml
    role: canonical_record
  ownership_note: Future maintained YAML curation only; preserve sources, caches,
    history and prior reviews.
- finding_id: gtdb-provenance
  issue_key: cm-000160-gtdb-provenance
  category: grounding
  severity: minor
  native_severity: P3
  normalization_reason: Bounded cultivation, provenance or resource representation
    repair; core phenotypes remain supported.
  rule_id: review-checklist.claim-specific-support-and-context
  status: open
  certainty: confirmed
  title: Replace unsupported GTDB release wording
  description: Both mapping_source strings assert latest release and a build date
    not established by the local crosswalk metadata.
  target_ids:
  - CommunityMech:000160
  field_paths:
  - taxonomy[0].taxon_term.gtdb_classification.mapping_source
  - taxonomy[1].taxon_term.gtdb_classification.mapping_source
  evidence_ids:
  - gtdb
  - species
  - semantics
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Drosophila_FiveSpecies_Gnotobiotic_Gut_Microbiota.yaml
    role: canonical_record
  ownership_note: Future maintained YAML curation only; preserve sources, caches,
    history and prior reviews.
- finding_id: datasets
  issue_key: cm-000160-datasets
  category: representation
  severity: minor
  native_severity: P3
  normalization_reason: Bounded cultivation, provenance or resource representation
    repair; core phenotypes remain supported.
  rule_id: review-checklist.claim-specific-support-and-context
  status: open
  certainty: confirmed
  title: Distinguish publications from data resources
  description: The three associated dataset accessions are publication PMIDs rather
    than genuine dataset identifiers.
  target_ids:
  - CommunityMech:000160
  field_paths:
  - associated_datasets
  evidence_ids:
  - resources
  - links
  - survey
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Drosophila_FiveSpecies_Gnotobiotic_Gut_Microbiota.yaml
    role: canonical_record
  ownership_note: Future maintained YAML curation only; preserve sources, caches,
    history and prior reviews.
actions:
- action_id: repair-membership
  description: Represent the five source bacteria and external host consistently.
  finding_ids:
  - membership
  target_ids:
  - CommunityMech:000160
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Drosophila_FiveSpecies_Gnotobiotic_Gut_Microbiota.yaml
    role: canonical_record
  acceptance_checks:
  - Use verified current species IDs and canonical labels with historical source names
    and exact DmelCS codes retained; do not invent strain CURIEs or attach clone markers
    as stock genomes.
  - Remove the fly from microbial taxonomy while keeping it in host/environment and
    appropriate ecological interaction participation. Preserve the named mono-, dual-
    and five-member experimental scopes.
  - Align node participants and pair descriptors with the measured species combinations.
    Preserve all three qualified observations and the PARTIAL 1→0 arrow, attaching
    the specific Figure 6 evidence to its mediation statement; do not universalize
    genus-level responses or add exchange arrows.
  - Move roster-count prose from deprecated abundance_value into appropriate notes
    without inventing quantitative abundance.
- action_id: repair-roles
  description: Remove unsupported unqualified metabolic role assertions.
  finding_ids:
  - roles
  target_ids:
  - CommunityMech:000160
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Drosophila_FiveSpecies_Gnotobiotic_Gut_Microbiota.yaml
    role: canonical_record
  acceptance_checks:
  - Retain only role tags supported by actual utilization/fermentation evidence; source-attributed
    provisioning hypotheses can remain explicitly hypothetical.
  - Preserve observed CFU/host traits and mechanistic alternatives. Do not substitute
    another speculative role or treat missing optional roles as a defect.
- action_id: repair-cultivation
  description: Document source-specific recipes, preparation and host assay context.
  finding_ids:
  - cultivation
  target_ids:
  - CommunityMech:000160
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Drosophila_FiveSpecies_Gnotobiotic_Gut_Microbiota.yaml
    role: canonical_record
  acceptance_checks:
  - Add the complete nine-component 2014 MMRS recipe with reported forms/units and
    direct Methods evidence. Preserve 30 °C stocks, CO2 plate handling, 25 °C host
    conditions and 12:12 h cycle.
  - Keep 2014 equal-part 50 µL inoculation separate from 2015 MRS broth durations,
    7.5 mL food/50 mL tubes and different preservatives. Do not import the 2011 survey
    diet into the defined assay.
  - Qualify or remove FACULTATIVE_ANAEROBIC if it lacks source-specific physiological
    support; report actual aerobic/CO2 stages without inferring exact oxygen concentration
    or anaerobic mixture.
- action_id: repair-gtdb
  description: Record reproducible mapping provenance at the correct taxon scope.
  finding_ids:
  - gtdb-provenance
  target_ids:
  - CommunityMech:000160
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Drosophila_FiveSpecies_Gnotobiotic_Gut_Microbiota.yaml
    role: canonical_record
  acceptance_checks:
  - Replace latest/build wording with verified local snapshot hash, retrieval context
    and mapping method. Filesystem mtime is not a GTDB release/build date.
  - Re-ground resolved species independently; preserve two Acetobacter ambiguities
    and distinguish other verified species routes from exact DmelCS genome classification.
    Do not transplant old genus confidence/counts to strains.
- action_id: repair-resources
  description: Keep publication citations and actual datasets distinct.
  finding_ids:
  - datasets
  target_ids:
  - CommunityMech:000160
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Drosophila_FiveSpecies_Gnotobiotic_Gut_Microbiota.yaml
    role: canonical_record
  acceptance_checks:
  - Retain all three verified articles as publication/external references with their
    study roles.
  - If adding source survey data, use verified SRA study/run metadata and explicitly
    pooled 454 16S scope; keep HQ173707–HQ173711 as clone markers, not isolate genomes
    or phenotype datasets.
  - Do not infer an absent deposit from unqueried archives or the unavailable 2011
    supplement details.
- action_id: validate-curation
  description: Validate any separately authorized future curation.
  finding_ids:
  - membership
  - roles
  - cultivation
  - gtdb-provenance
  - datasets
  target_ids:
  - CommunityMech:000160
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Drosophila_FiveSpecies_Gnotobiotic_Gut_Microbiota.yaml
    role: canonical_record
  acceptance_checks:
  - Run focused schema, strict, term-label, reference, GTDB/domain and history checks
    after changes.
  - Preserve all source/correction receipts and existing causal limitations; do not
    edit caches or histories to make validation pass.
limitations:
- The five 2011 supplementary objects were not recovered by the preserved public routes.
  Current claims were adjudicated from the complete main survey; no conclusion relies
  on unseen supplementary data.
- 2015 SI bulk SNP and GO Tables S3/S4 were only inventoried with headers and initial
  displayed rows. Selected Tables S1/S2/S5/S6/S7, Note 1 and all Figures S1–S7 were
  read; no GWAS or raw-sequence reanalysis was performed.
- The original S5b panels and actual corrigendum were kept separate. The corrected
  image was a thumbnail, used for panel arrangement rather than quantitative extraction.
  The main and SI table/cross-reference numbering differ in places.
- Whole-fly CFU does not establish persistent intestinal residence or growth rates;
  the PARTIAL mediation arrow is not a selective causal experiment. No microbial metabolite
  exchange is demonstrated by the reported host outcomes.
- Source species, historical names, DmelCS stock codes, survey OTUs and generic GTDB
  mappings have different scopes. Exact stock genomes and strain CURIEs were not established.
- The optional structured adapter could not run in the owned environment. Host GWAS/P-element
  relevance was considered explicitly, but organism/dataset coverage remains unknown.
- Completion concerns this record review at the stated scope; it does not authorize
  curation, issue changes or source-cache restoration.
notes:
- All 33 official input hashes remain unchanged. Eight evidence-linked dimensions,
  four exact graph snippet hashes and the single arrow binding are explicit.
- Required native checks passed. Access and ad hoc display failures are retained separately;
  candidate validation is recorded after this actual file is rendered.
- Lead read the whole canonical record and focal histories; supporting reviewers independently
  own the full cache, prior/cohort and current issue scopes recorded in their receipts.
- The direct source quote contains two words. Root alone saves the accepted review
  and runs post-save gates.
tags:
- record-review
- gnotobiotic
- host-microbiota
- batch-16
```
