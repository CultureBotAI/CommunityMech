# Chlorella–Rhizobium bioflocculation source and evidence review

- Review: 20261021T184646Z-chlorella-rhizobium-record
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-21T18:37:44.356968Z
- Finished UTC: 2026-10-21T18:46:46.791396Z
- Reviewer: codex (unknown)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Direct Abstract/Significance support the named pair, 45–50% harvesting and the qualified two-node/one-arrow graph. Two major findings address non-graph overclaims and unsupported complex-substrate degradation; two minor findings address experimental-context fields and iron significance. Critical focal main/SI remain inaccessible, so scientific verification is partial despite eight passing focused checks.

## Scope And Provenance

Whole canonical record, both members, both nodes and the arrow assessed against direct Abstract/Significance, current authorities, prior provenance and bounded access evidence; full scientific verification remains partial.

Selection: Only released CommunityMech:000016 in the owned batch 10 checkout.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 95812d3412d5aab41fd03422340cf736ac7b56f3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000016 | kb/communities/Chlorella_Rhizobium_Bioflocculation.yaml | maintained | Chlorella-Rhizobium Bioflocculation |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000016 | Schema validation passed. |
| validate-strict | passed | True | CommunityMech:000016 | Strict validation passed. |
| validate-terms | passed | True | CommunityMech:000016 | Encoded ID-label validation passed. |
| validate-gtdb | passed | True | CommunityMech:000016 | GTDB structure and ambiguity coherence passed. |
| validate-gtdb-domain | passed | True | CommunityMech:000016 | Taxon domain applicability passed. |
| validate-history | passed | True | CommunityMech:000016 | The sole append-only history record passed validation. |
| normalize-cache-names-check | passed | True | CommunityMech:000016 | Read-only cache filename normalization check passed. |
| validate-references-explained | passed | True | CommunityMech:000016 | Native references passed against the unchanged selected-excerpt cache; direct-source matching and biological support remain separate checks. |
| audit-network | failed | True | CommunityMech:000016 | Fresh batch 10 corpus diagnostic retains unrelated warnings; the focal two-node/one-arrow graph separately reports COMPLETE. |
| check-network-quality | failed | True | CommunityMech:000016 | Fresh batch 10 corpus diagnostic retains unrelated warnings; the focal two-node/one-arrow graph separately reports COMPLETE. |
| Full main and critical supplementary verification | unavailable | True | CommunityMech:000016 | Full focal Methods/Results, figures and actual S1–S4 contents remain inaccessible and unread. Direct Abstract/Significance support bounded findings; scientific review remains partial. |
| Fresh source-specific excerpt verification | passed | True | CommunityMech:000016 | All twelve occurrences match direct publisher Abstract/Significance and cache; ten also match EPMC, with exact publisher typography supplying the other two. |
| Critical supplementary source access | unavailable | True | CommunityMech:000016 | Exact DOCX listing and four table titles are verified, but linked/static responses are 403 HTML. No cells or supplementary statistical details were read. |
| Publication and bounded resource identity | passed | True | CommunityMech:000016 | Exact focal bibliographic identity and public SI listing verified; no global resource absence or recipe equivalence inferred. |
| Raw data and experimental reproduction | skipped | False | CommunityMech:000016 | No culture experiment, raw sequence analysis, RSM refitting or statistical reproduction was performed. |
| Optional structured source adapter | unavailable | False | CommunityMech:000016 | Explicit same-runtime discovery reuse preserves unavailable status and original scope. No paid or other-checkout executable was used. |

## Scientific And Domain Assessments

### Community identity and source strain

identity: supported. Targets: CommunityMech:000016.

Retain the constructed C. vulgaris–F2 pair and current broad taxon grounding.

Exact F2 authority supports parent NCBITaxon:358 despite the generic Rhizobium radiobacter name pointing elsewhere. Do not automatically substitute NCBITaxon:362, select one of the four species-scope GTDB candidates or promote the record to an exact strain node. This is authority reconciliation, not proof of a sequenced 2015 experimental stock. The paper name remains a source synonym.

### Origin, state, category and physical environment

identity: concern. Targets: CommunityMech:000016.

ENGINEERED origin/state and PHYTOPLANKTON category fit; physical treatment-plant context is not established.

The source describes a controlled synthetic-wastewater coculture and prospective treatment application. The encoded ENVO term denotes an actual wastewater treatment plant. Separate application from location. Laboratory environment is an authority-checked candidate only if source confidence supports that physical context; an unresolved field is preferable to an unsupported precise facility.

### taxonomy[0]: Chlorella vulgaris

evidence: concern. Targets: CommunityMech:000016.

Retain algal membership and broad PRIMARY_PRODUCER capability; narrow evidence explanations and relocate functional abundance prose.

Poor axenic flocculation directly supports the baseline, not a necessity for bacterial assistance in all conditions or measured photosynthetic production in this assay. The abundance_value string is a role statement, not a quantitative abundance observation. NO_GTDB_EQUIVALENT is appropriate for the eukaryotic alga. No new cell ratio, stable abundance or carbon-transfer role is inferred.

### taxonomy[1]: F2 role, product notes and abundance

evidence: concern. Targets: CommunityMech:000016.

Retain membership and bioflocculant association; PRIMARY_DEGRADER is unsupported by the attached source claim.

Producing a flocculant and using supplied glucose do not demonstrate degradation of complex substrates. Roles are optional, so removing the unsupported enum does not require inventing another role. EPS capability reported in earlier F2 literature is not disproven, but exact focal-coculture product identity and mediation remain unverified. The helper/optimized-ratio abundance string belongs in source-scoped notes, not quantitative abundance.

### description and non-graph source explanations

evidence: concern. Targets: CommunityMech:000016.

Correct over-90% harvesting and distinguish observed recovery from chemical and economic interpretation.

The range in the overview contradicts both the abstract and the current harvesting node. Retain 45–50% and the separate over-21% lipid content with optimized-condition context. Attribute environmental and cost prospects to the authors rather than present a measured comparative advantage. Restrict explanatory prose to the attached claim: a short harvesting or taxon-name excerpt does not prove photosynthetic mode, chemical mediation or general physiological necessity.

### engineering_design objective, assembly, endpoints and perturbation

evidence: concern. Targets: CommunityMech:000016.

Harvesting optimization is supported; generic mechanism/persistence endpoints and a tested light factor are not established.

Bottom-up coculture at defined inoculation ratios is consistent with the abstract, but exact axenic stock preparation is not verified in Methods. Replace backfilled endpoints with harvesting efficiency, lipid content and the reported RSM variables. Do not turn three named optimization variables into a new mechanistic characterization or member-persistence experiment. Light is not one of the three variables listed in the accessed abstract.

### ecological_interactions[0]: Bioflocculant Production and Cell Aggregation

evidence: supported. Targets: CommunityMech:000016.

Retain the source-directed, explicitly PARTIAL association node.

F2 is the bioflocculant-associated source partner and C. vulgaris the harvested target. GO:0098743 cell aggregation fits the readout. The node already excludes product identity, charge neutralization/bridging, algal-exudate transfer, biofilm formation and reciprocal fitness. No stronger mechanism or carbon-transfer arrow is warranted from the accessed material.

### ecological_interactions[1]: Algal Biomass Harvesting

evidence: supported. Targets: CommunityMech:000016.

Retain the community-level recovery endpoint and correct abstract range.

Both partners are appropriate participants in the measured coculture outcome. The node distinguishes 45–50% harvesting from the unsupported over-90% summary, and avoids mutualism or direct cost/energy conclusions. Its two evidence entries support the optimized range and axenic baseline. No improvement in lipid productivity, absolute biomass or comparative energy use is inferred from lipid content alone.

### ecological_interactions[0].downstream[0]

evidence: supported. Targets: CommunityMech:000016.

Retain the one qualified association-to-recovery arrow.

Direction from F2-associated aggregation to algal harvesting is the source’s applied interpretation, and the current PARTIAL description excludes a demonstrated specific mediator or bacterial fitness benefit. The arrow is not a selective-product intervention result. Its current qualification is sufficient for the accessible evidence; no graph expansion or reversal is required.

### environmental_factors[0:4]

evidence: concern. Targets: CommunityMech:000016.

Retain source-reported ratio, glucose and time; remove unverified protocol and process extrapolations.

The paper calls three process variables significant in its RSM framing, but the full individual-term analysis is unread. A photosynthetic species name supplies no tested photoperiod. Ratio basis is not established as cell counts, and contamination minimization is not an accessed endpoint. Nutrient depletion and instability with longer incubation are generic possibilities, not demonstrated results of this experiment. No absolute counts or substitute causal claims should be added.

### growth_media[0] and cultivation setup

completeness: concern. Targets: CommunityMech:000016.

Preserve the three abstract-supported ranges while separating composition ratio from inoculum density.

Synthetic wastewater, 9–14 days and glucose below 1.5 kg/m3 are supported. The 0.20–0.25 bacteria:alga composition ratio is not an initial density or transfer percentage and should move to appropriate setup or preparation notes with unknown basis. Do not infer CFU, cells, percent v/v or absolute inoculum. Complete formulation, temperature, pH, vessel, mixing, atmosphere and illumination remain unresolved, not confirmed absent from the full source. No CultureMech equivalence follows from the medium name.

### metals_present, metal_relevance and metal_notes

evidence: concern. Targets: CommunityMech:000016.

Remove or explicitly substantiate keyword-derived significant iron metabolism.

The current boilerplate does not cite an iron measurement or metal-metabolism mechanism. SIGNIFICANT is not justified merely because a growth medium might contain trace iron or a separate reference discusses chemical flocculants. The unknown complete recipe prevents any global claim that iron is absent; correcting this flag is a bounded evidence repair.

### Study resources, medium links and source access

completeness: unknown. Targets: CommunityMech:000016.

Publication and SI listing are verified; focal datasets and complete source protocols remain unresolved.

No external resource or associated dataset is currently encoded, and no dataset omission is graded. S1–S4 are known by title only. The earlier F2 genome accession and EPS paper are identity/background leads, not focal 2015 experimental datasets. Do not invent an archive, use publication landing pages as phenotype accessions or contact authors during this review.

### Reference cache, prior review, discussions and issue ownership

provenance: supported. Targets: CommunityMech:000016.

Retain the qualified graph repair and existing source-gap discussion with exact issue scopes.

The sole cache explicitly contains selected Abstract/Significance excerpts and is not falsely labeled a full paper. All twelve excerpts are matched to direct source text, but larger claims remain independently assessed. Open 561 owns the role/vocabulary question and open 1301 the non-graph follow-up. Closed 1299 records prior graph work. Neither a prior review nor a closed issue certifies all current prose. No issue is opened, closed or commented on here.

### Native checks and immutable workflow

schema: supported. Targets: CommunityMech:000016.

All eight focused checks pass; scientific verification remains partial.

Canonical, cache, history and generated products are unchanged. Any review persistence is restricted to a new immutable review bundle. Initial and final native summaries are separate. Optional grounder exit 1 records expected species ambiguity, not a failure of the eight focused checks or a reason to force a GTDB candidate.

### Native mechanical completeness and validation quality

completeness: supported. Targets: CommunityMech:000016.

Completeness is 75; raw quality 106 caps at 100 independently of the partial scientific status.

## Findings

### non-graph-source-overreach: Align the overview and explanations with the focal source

major / open / confirmed; issue key: cm-000016-issue1301-non-graph-source-overreach.

Replace over 90% with the source-reported 45–50% under optimized conditions and keep the 0.2% axenic baseline separate. Distinguish bioflocculant association from verified focal product chemistry/mediation and measured cost, energy or safety advantage. Earlier F2 EPS capability is not disproven. Restrict evidence explanations to the claims their excerpts support; general taxon capability is not a measured assay mechanism.

### unsupported-primary-degrader: Remove or independently support F2 complex-substrate degradation

major / open / confirmed; issue key: cm-000016-issue561-primary-degrader.

PRIMARY_DEGRADER is not established by producing a flocculant or by supplied glucose. Omit the optional role until claim-specific evidence is available, preserving source-supported bioflocculant function in prose. Existing issue 561 owns the role/shared vocabulary follow-up; a comment proposing another enum is not evidence that the current schema already contains it.

### experimental-context-placement: Separate measured optimization from generic context and misplaced fields

minor / open / confirmed; issue key: cm-000016-issue1301-experimental-context-placement.

Distinguish synthetic wastewater and treatment application from an actual plant. Replace unsupported backfilled endpoints and light perturbation with source-supported RSM scope. Relocate functional abundance prose and composition ratio from quantitative abundance/inoculum-density fields. Remove unverified illumination, contamination, depletion and stability extrapolations without inventing missing Methods.

### unsupported-metal-significance: Remove unsupported keyword-derived iron significance

minor / open / confirmed; issue key: cm-000016-issue1301-metal-significance.

IRON and SIGNIFICANT are supported only by keyword-detection boilerplate, with no identified claim-specific metal-metabolism evidence. Remove or substantiate these fields. Unknown medium composition is not evidence that iron was absent, and a reference to chemical flocculants would not establish significant biological iron cycling.

## Recommended Actions And Acceptance Checks

### repair-summary-and-explanations

Correct the quantitative overview and source-specific non-graph interpretations.

- Use 45–50% harvesting efficiency under the stated optimized conditions versus 0.2% axenic flocculation; preserve lipid content over 21% as a distinct content endpoint. Do not call it productivity, conversion yield or over-90% recovery.
- Describe F2 as a bioflocculant-producing partner. Keep the focal product identity and mediation unresolved unless exact focal Methods/Results or a specific intervention assay supports them. Earlier F2 EPS reports may be separately attributed background but cannot silently certify the focal mediator.
- Attribute cost-effectiveness and environmental promise as the authors’ significance framing unless an inspected comparison supports measured effects. Narrow the engineering/algal evidence explanations so a harvest or species-name excerpt does not prove photosynthetic mode or a universal need for bacterial assistance.
- Retain both qualified interaction nodes and their one PARTIAL arrow, including the limits on polymer identity, carbon transfer, biofilm formation and reciprocal fitness. Keep the existing discussion open and reference issue 1301 without creating a duplicate.

### repair-f2-role

Resolve the production-versus-degradation mismatch within existing issue 561.

- Remove F2 PRIMARY_DEGRADER unless a directly inspected, claim-specific source establishes complex-substrate degradation relevant to the stated role. Preserve membership and bioflocculant-production notes; do not invent PRIMARY_PRODUCER, CROSS_FEEDER or another replacement enum.
- Keep broader vocabulary discussion under the existing shared issue 561. Any separately authorized schema proposal must follow schema ownership and regeneration rules; no schema change is required merely to omit an unsupported optional role.
- Retain exact F2 source naming, parent NCBITaxon:358 and the four species-level GTDB candidates. Do not substitute generic radiobacter 362 or silently import the exact-strain GTDB classification.

### repair-experimental-context

Represent actual experimental scope and move nonquantitative content into suitable notes.

- Describe synthetic-wastewater experimental culture separately from wastewater-treatment application. Reconcile the treatment-plant environment term with direct physical-context evidence; use the authority-checked laboratory term only if supported, otherwise retain uncertainty rather than choose by lexical similarity.
- Use harvest efficiency, lipid content and the ratio/glucose/time RSM design as supported endpoints/variables. Remove generic mechanism-characterization and member-persistence tracking claims unless the full source demonstrates those assays; do not claim light was a tested factor from an algal name alone.
- Move both abundance_value role/design strings to source-qualified notes rather than invent quantitative abundance, counts or ranks. Preserve the 0.20–0.25 bacteria:microalgae composition ratio in suitable setup or preparation notes, removing it from inoculum_size/unit fields intended for initial density or transfer percentage. State that its cell, viable-count or volume basis is unverified; do not infer cells, CFU or percent v/v.
- Retain synthetic wastewater, glucose below 1.5 kg/m3 and 9–14 days. Remove unsupported required/continuous/cyclic illumination and contamination/depletion/instability claims unless direct Methods/results support them. Do not infer full recipe, temperature, pH, vessel, aeration or mixing, and do not map a generic medium name to CultureMech.

### repair-metal-metadata

Resolve the unsupported iron and significant-metal flags.

- Remove keyword-derived iron/significant-metal assertions or add exact source evidence for meaningful metal metabolism and the appropriate native category. Do not substitute an asserted absence category merely because the complete medium is unavailable.
- Keep medium trace ingredients, chemical-flocculant comparisons and biological metal-metabolism evidence distinct. Reference the existing issue 1301 scope; do not add a new mechanism, metal ingredient or issue based on a keyword.

### complete-source-followup

Complete the scientific assessment when authorized full main and supplementary evidence is available.

- Obtain the exact focal Methods/Results, figures and lam12403-sup-0001-TableS1-S4.docx through an authorized accessible or supplied copy. Preserve version, actual contents and section/table locators; the present named listing is metadata only.
- Independently inspect experimental setup, ratio definition, harvest/lipid denominators, controls, replicates, model specification and supplementary ANOVA before changing partial scientific status. A high native score or abstract model fit does not substitute for that source review.
- Assess exact product chemistry/mediation and F2 degradation claims against the focal assays. Preserve earlier strain-background versus focal-data boundaries; no raw genome or author-contact work is authorized by this review.
- If later authorized curation adds main or supplementary excerpts, preserve source-specific cache provenance and exact locators. Do not relabel the current selected-excerpt cache as full text or merge inaccessible supplements into a main-text cache to manufacture matching.

### validate-authorized-curation

Validate separately authorized curation and preserve historical evidence.

- Append fresh curation history after authorized canonical changes and run focused schema, strict, term, reference, GTDB/domain and history checks, followed by just gen-html and just check-docs-current. No canonical, cache, history or generated artifact is changed by this review.
- Verify every new excerpt against its exact source and section. Preserve previous reviews, original source-access failures and immutable receipts. Only a new review bundle may be persisted here; neither native validation nor bundle persistence changes the explicit partial scientific status.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | kb/communities/Chlorella_Rhizobium_Bioflocculation.yaml; Entire maintained YAML, two taxa, two interaction nodes, one downstream arrow and discussion | supports | The record describes a constructed Chlorella vulgaris–F2 coculture for harvesting in synthetic wastewater. The graph already limits chemical mediation and corrects the harvesting range; several non-graph statements retain stronger or different claims. |
| identity | doi:10.1111/lam.12403; PMID:25693426; Significance and Impact of the Study: opening paragraph | supports | The directly inspected publisher identifies Chlorella vulgaris and bioflocculant-producing F2, named Rhizobium radiobacter, in synthetic wastewater. This supports the experimental pair and treatment application. It does not establish operation at an actual wastewater treatment plant, exact culture-stock continuity or a complete medium recipe. |
| harvesting | doi:10.1111/lam.12403; PMID:25693426; Abstract: opening axenic baseline and results paragraph | supports | The source reports 0.2% flocculation for axenic C. vulgaris and 45–50% harvesting efficiency under optimized coculture conditions. Lipid content over 21% is a separate content endpoint. The record’s overview exceeds 90%, whereas its harvesting node already gives the correct range. No full-text denominator, replicate, uncertainty or statistical comparison has been independently inspected. |
| optimization | doi:10.1111/lam.12403; PMID:25693426; Abstract: RSM design, model statistics and optimized conditions | supports | The authors vary bacteria:microalgae inoculation ratio, initial glucose and coculture time using response surface methodology. The reported operating ranges are ratio 0.20–0.25, glucose below 1.5 kg/m3 and 9–14 days. Abstract model F-values 3.98/8.46 and R-squared values 0.7817/0.8711 are author-reported summaries, not a reproduced model or proof of each mechanistic interpretation. The ratio basis is unspecified in the accessed text. |
| chemical-scope | doi:10.1111/lam.12403; PMID:25693426; Abstract and Significance and Impact of the Study: bioflocculant-producing partner and prospective benefits | supports | The focal source identifies a bioflocculant-producing partner and improved harvesting. The accessed text does not identify the product chemistry, isolate its causal mediation, trace algal carbon transfer or measure reciprocal fitness. Environmental and cost benefits are framed as significance and prospects; the accessible sections do not expose a comparative cost, energy or safety experiment. Earlier exact-F2 EPS leads do not establish the focal coculture mediator and are not disproven by this access limit. |
| protocol-scope | doi:10.1111/lam.12403; PMID:25693426; Abstract: three process variables; Significance and Impact of the Study: synthetic wastewater | supports | The source supports the named medium context and optimization variables. It does not report illumination intensity/photoperiod, a complete recipe, initial viable density, vessel, temperature, pH, strain-specific counts or member persistence in the accessed sections. Identifying an alga does not supply a tested illumination regime. Ratio and time optimization do not directly establish reduced bacterial contamination, nutrient depletion or culture instability. |
| supplement-listing | https://enviromicro-journals.onlinelibrary.wiley.com/doi/abs/10.1111/lam.12403; Supporting Information: lam12403-sup-0001-TableS1-S4.docx, advertised 23.9 KB | supports | The publisher lists S1 design matrix/results, S2 independent variables for the central composite design, and S3/S4 ANOVA for flocculation and lipid content. These are verified table titles only. Linked and ordinary static download routes returned 403 HTML, not a DOCX; no table cells or figures were inspected. |
| access | Public Wiley/OUP main and supplementary routes; OpenAlex and Europe PMC metadata; Frozen lead access receipts and body signatures | supports | Direct publisher Abstract and Significance are available. Main/full/PDF routes failed or resolved to the abstract; metadata indicates subscription access without an available PMC/repository copy. The correct OUP article identifier is 6699742. Public linked and static SI responses were access-denial HTML. These bounded attempts do not establish global absence of authorized copies. |
| schema | src/communitymech/schema/communitymech.yaml; FunctionalRoleEnum.PRIMARY_DEGRADER and PRIMARY_PRODUCER; MetalRelevanceEnum.SIGNIFICANT; environment_term, abundance_value and inoculum_size slots | supports | PRIMARY_DEGRADER concerns complex-substrate degradation, not flocculant production. Algal PRIMARY_PRODUCER can express broad carbon-fixing capability without proving exchange. SIGNIFICANT concerns significant metal/REE metabolism. Quantitative abundance and initial density/transfer fields are not containers for functional prose or an inoculation composition ratio. Actual environmental context is distinct from treatment application. |
| ontology | ontology-authority.json; Whole frozen receipt and declared scope | supports | All four distinct encoded ID-label pairs match across nine occurrences: the two taxon concepts, wastewater treatment plant and cell aggregation. Correct labels do not establish that a plant was the actual experimental setting or identify the flocculant mechanism. |
| strain-authority | child-F2-strain-authority.json; authority; local_OAK; generic_name_comparison; exact_strain_crosswalk.rows and scope; focal_source_scope | supports | Direct exact-strain NCBI node 1050720 explicitly lists Rhizobium radiobacter F2 and parent 358, supporting retention of the current species-parent grounding. Generic Rhizobium radiobacter maps to a different concept, 362, and is not an automatic replacement. Local OAK uses strain rank while the live page displays no rank; no raw laboratory-stock sequence identity is certified. The exact F2 taxid 1050720 crosswalk separately maps to Agrobacterium oryzihabitans in two genomes at fraction 1.0. This optional exact-strain context is not silently transferred into the species-level record. |
| taxonomy-scope | child-schema-taxonomy-scope.json; Whole frozen receipt and declared scope | supports | The four current species-level GTDB candidates are retained. Optional ENVO:01001405 laboratory environment is authority-checked as a possible actual-context term subject to source confidence. Scope and rank metadata are explicit; no canonical term is replaced during this review. |
| gtdb | child-gtdb-crosswalk.json; exact_id_rows; exact_species_name_row_count; name_group_gtdb_species; scope | supports | The current species-name group has fifteen rows across four GTDB species and remains ambiguous. Exact species ID 358 has no direct row. This receipt reproduces the current species-level mapping; it does not establish F2 identity or select a single candidate. |
| semantics | ontology-semantic-notes.json; Whole frozen receipt and declared scope | supports | Independent schema/authority assessment agrees with the two major and two minor groups, retained taxon/graph scope and partial source status. GO cell aggregation fits clustering without proving biofilm formation, EPS mediation or reciprocal fitness. |
| resources | dataset-verification.json; Whole frozen receipt and declared scope | supports | PMID/DOI/title and the exact supplement listing are verified. No usable focal supplement contents or source-linked independent dataset were recovered within the bounded access scope. This is not a dataset absence finding, a complete recipe claim or authorization to substitute an earlier F2 genome for focal coculture data. |
| source-metadata | source-metadata-audit.json; Whole frozen receipt and declared scope | supports | The exact 2015 publication is verified. Publisher online, PubMed electronic and issue dates have different metadata scopes; their differences are not graded as a record error. |
| snippets | snippet-audit.json; Whole frozen receipt and declared scope | supports | All twelve evidence occurrences match fresh publisher Abstract/Significance and the selected-excerpt cache: ten abstract and two Significance occurrences. Ten also match EPMC directly; two exact publisher range/unit forms differ from EPMC typography. No broad punctuation substitution or full-main match claim is used. |
| publisher-projection | publisher-abstract-projection.json; Whole frozen receipt and declared scope | supports | The direct publisher text supports the exact en-dash and superscript/unit forms in the record. Literal excerpt matching is separately evaluated from the larger explanatory claims attached to those excerpts. |
| history | provenance-audit.json; Whole frozen receipt and declared scope | supports | Whole sole history and exact prior batch 13 row were read. Open issue 561 owns F2 role/shared vocabulary follow-up; open 1301 owns non-graph summary, environment, process and metal follow-up. Closed/completed 1299 is explicitly reused with its original same-session retrieval and complete comment; historical keep-open wording does not override its current closed status. |
| inspect | inspect.json; Whole frozen receipt and declared scope | supports | The fresh official inspect establishes 25 input hashes, exact maintained target/class and batch 10 base. All inputs remain unchanged; prior-record inspection is not inherited. |
| metrics | support-audit.json; Whole frozen receipt and declared scope | supports | Two interaction nodes, one arrow and three node-evidence entries give mean 1.5 and native COMPLETE. Completeness is 75. Two major and two minor findings yield raw quality 106, capped at 100. These are mechanical scores, not scientific completion. |
| support-manifest | supporting-artifact-manifest.json; Whole frozen receipt and declared scope | supports | The frozen support manifest pins provenance, source-specific snippets, resources, score arithmetic, official input integrity and final root/lead source receipts. |
| lead-read | lead-primary-read-scope.json; Whole frozen receipt and declared scope | supports | Lead read the whole canonical, selected-excerpt cache, sole history and exact prior row, fresh direct Abstract/Significance, access metadata and frozen authorities. Full focal main, figures and SI remain unread; earlier F2 discovery is bounded identity context. |
| source-scope | source-audit.json; Whole frozen receipt and declared scope | supports | Lead assessment is partial with scientific_review false, two major and two minor findings, completeness 75 and raw quality 106. Findings separate demonstrable abstract-level correction from unresolved full-source questions. |
| root-source | root-independent-source-audit.json; Whole frozen receipt and declared scope | supports | Root independently read the whole canonical and fresh direct Abstract/Significance, checked all twelve excerpts, and assessed authority, provenance and access limits. The independent scientific review also remains partial. |
| root-read | root-primary-read.json; Whole frozen receipt and declared scope | supports | Exact independent root read scope and raw-source pins are preserved. Root did not inspect the focal main/SI, full earlier genome paper or full RSC manuscript; earlier EPS leads do not disprove or establish focal mediation. |
| auxiliary | auxiliary-frozen-manifest.json; Whole frozen receipt and declared scope | supports | All eight focused native checks pass; four ontology pairs match across nine occurrences. Initial native summary is immutable, and later metadata is a separate final summary. |
| final-native | final-validator-summary.json; Whole frozen receipt and declared scope | supports | The separate final native summary pins the original eight execution records without rewriting the initial validator summary. Optional GTDB grounder exit 1 is preserved as ambiguity, outside those eight passing gates. |
| adapter | adapter-check.json; Whole frozen receipt and declared scope | supports | Optional adapter unavailability is explicitly reused from the same verified batch 10 runtime, with its original retrieval timestamp and bounded ignored-inclusive discovery. No executable from another checkout or paid provider was invoked. |
| check-validate | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src just --no-dotenv validate kb/communities/Chlorella_Rhizobium_Bioflocculation.yaml; Actual execution 2026-10-21T18:38:07.919542+00:00 to 2026-10-21T18:38:09.311778+00:00 | supports | Schema validation passed. |
| check-validate-strict | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src just --no-dotenv validate-strict kb/communities/Chlorella_Rhizobium_Bioflocculation.yaml --out /private/tmp/cm-review-session/batch-10/000016/strict-report.tsv; Actual execution 2026-10-21T18:38:07.919813+00:00 to 2026-10-21T18:38:13.986022+00:00 | supports | Strict validation passed. |
| check-validate-terms | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src just --no-dotenv validate-terms kb/communities/Chlorella_Rhizobium_Bioflocculation.yaml; Actual execution 2026-10-21T18:38:07.919906+00:00 to 2026-10-21T18:38:12.728411+00:00 | supports | Encoded ID-label validation passed. |
| check-validate-gtdb | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src just --no-dotenv validate-gtdb kb/communities/Chlorella_Rhizobium_Bioflocculation.yaml; Actual execution 2026-10-21T18:38:09.312187+00:00 to 2026-10-21T18:38:09.449209+00:00 | supports | GTDB structure and ambiguity coherence passed. |
| check-validate-gtdb-domain | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src just --no-dotenv validate-gtdb-domain kb/communities/Chlorella_Rhizobium_Bioflocculation.yaml; Actual execution 2026-10-21T18:38:09.449494+00:00 to 2026-10-21T18:38:14.327610+00:00 | supports | Taxon domain applicability passed. |
| check-validate-history | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src just --no-dotenv validate-history history/records/Chlorella_Rhizobium_Bioflocculation; Actual execution 2026-10-21T18:38:12.728899+00:00 to 2026-10-21T18:38:14.409466+00:00 | supports | The sole append-only history record passed validation. |
| check-normalize-cache-names-check | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src uv run python scripts/normalize_cache_names.py --check; Actual execution 2026-10-21T18:38:14.410707+00:00 to 2026-10-21T18:38:14.494905+00:00 | supports | Read-only cache filename normalization check passed. |
| check-validate-references-explained | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src just --no-dotenv validate-references-explained kb/communities/Chlorella_Rhizobium_Bioflocculation.yaml; Actual execution 2026-10-21T18:38:14.495174+00:00 to 2026-10-21T18:38:16.219142+00:00 | supports | Native references passed against the unchanged selected-excerpt cache; direct-source matching and biological support remain separate checks. |
| check-audit-network | PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv audit-network; Actual execution 2026-10-21T17:04:17.819938+00:00 to 2026-10-21T17:04:25.370848+00:00 | supports | Fresh batch 10 corpus diagnostic retains unrelated warnings; the focal two-node/one-arrow graph separately reports COMPLETE. |
| check-check-network-quality | PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv check-network-quality; Actual execution 2026-10-21T17:04:17.819995+00:00 to 2026-10-21T17:04:26.163649+00:00 | supports | Fresh batch 10 corpus diagnostic retains unrelated warnings; the focal two-node/one-arrow graph separately reports COMPLETE. |

## Limits And Additional Notes

- The focal paper is PMID 25693426, DOI 10.1111/lam.12403. Full direct publisher Abstract and Significance were read, together with fresh metadata and the whole selected-excerpt cache. Full scientific main, figures and S1–S4 contents remain unavailable and unread; completion is partial and scientific_review is false.
- Public full/PDF routes failed or resolved to abstract-only content. Linked and static supplement responses were 403 HTML rather than DOCX. Europe PMC and OpenAlex access flags describe the inspected metadata scope, not proof that no authorized full copy exists. No paywall, authentication or human-verification control was bypassed.
- The supplementary filename, advertised 23.9 KB size and four table titles are known only from the publisher listing. No table cells, CCD matrix, complete ANOVA, harvest denominator, uncertainty or replication detail is certified. Abstract model statistics are attributed to the authors and were not recomputed.
- Exact F2 authority supports the current species-parent mapping while generic radiobacter nomenclature differs. Neither metadata nor the optional two-genome exact-strain crosswalk proves raw-sequence stock continuity for the 2015 assay. Species-level GTDB ambiguity remains; local rank and live no-rank labels are preserved as distinct authority presentations.
- Earlier genome-announcement and RSC EPS leads were consulted only within declared identity/discovery limits. Full earlier papers and a culture collection entry were not scientifically inspected. Do not deny F2 EPS capability or treat an earlier strain-associated product as the proven focal coculture mediator.
- The ratio 0.20–0.25 is source-stated bacteria:microalgae composition with unknown basis, not a demonstrated cell ratio, viable density or transfer percentage. Glucose and 9–14 days are optimization ranges; a complete formulation and actual light, temperature, pH, vessel and mixing remain unresolved.
- Algal PRIMARY_PRODUCER denotes broad capability without proving measured photosynthesis or carbon transfer here. Flocculant production is not complex-substrate degradation. No new role, polymer mechanism, mutualism, biofilm, cost comparison or causal edge is inferred from excerpt matching or ontology consistency.
- All twelve excerpts match direct publisher text and cache. Ten also match EPMC exactly; two publisher range/unit forms differ from EPMC typography. This is a source-presentation boundary, not fabricated text or a full-body match. Explanatory overreach is assessed separately.
- Current open issues 561 and 1301 are the relevant existing owners. Closed 1299 is historical graph provenance, explicitly reused at its original retrieval time. Publisher online, PubMed electronic and issue dates are distinct metadata and are not treated as a scientific error.
- No source-declared focal dataset or exact medium identifier was verified within the bounded access scope. That is not proof of absence or a graded resource omission. No arbitrary archive search, raw-data analysis, RSM execution, experimental reproduction, paid service, author contact or later-record assessment occurred.
- Eight focused native checks pass; corpus diagnostics retain their actual broader failure scope. The optional GTDB grounder exit 1 records ambiguity. Completeness 75 and capped quality 100/raw 106 do not override the scientific access limit or the four evidence-linked findings.
- All 25 official inspected inputs remain unchanged. No canonical, source-cache, history, generated or previously saved artifact was edited.
- Root and lead independently assessed fresh direct Abstract/Significance and bounded access evidence. Child owns native/ontology/strain checks; sibling owns provenance, snippets, resources and arithmetic. All source receipts are immutable.
- Two major and two minor findings yield completeness 75 and quality 100/raw 106. Partial completion and scientific_review false remain controlling; no later target was assessed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T184646Z-chlorella-rhizobium-record
kind: record
repository: CultureBotAI/CommunityMech
title: Chlorella–Rhizobium bioflocculation source and evidence review
started_at: '2026-10-21T18:37:44.356968Z'
finished_at: '2026-10-21T18:46:46.791396Z'
reviewer:
  identity: codex
  kind: agent
  independence: unknown
  independence_basis: Separate agents assessed primary evidence, auxiliary authorities
    and provenance; no person-level independence is asserted.
skill: review-yaml-record
completion: partial
verdict: needs_curation
scientific_review: false
summary: Direct Abstract/Significance support the named pair, 45–50% harvesting and
  the qualified two-node/one-arrow graph. Two major findings address non-graph overclaims
  and unsupported complex-substrate degradation; two minor findings address experimental-context
  fields and iron significance. Critical focal main/SI remain inaccessible, so scientific
  verification is partial despite eight passing focused checks.
source:
  git_revision: 95812d3412d5aab41fd03422340cf736ac7b56f3
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
  - path: history/records/Chlorella_Rhizobium_Bioflocculation/2026-10-05T204706Z-codex-3ffe65.yaml
    sha256: 5a47521e6edd71ac1b3343457c6dfc6bbf3eb88cf4830c891926dd26acc108bd
    role: context
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: kb/communities/Chlorella_Rhizobium_Bioflocculation.yaml
    sha256: 57d52ecbebc7d66ea87c15c949cb532b9cbad5e8c1211871a13f0647563dfbf9
    role: target
  - path: references_cache/doi_10.1111_lam.12403.md
    sha256: 2bfd35487a9a9ab63d5aaa0458604e6a37a88ca72851f10a6772cd020630ade0
    role: context
  - path: reports/causal_graph_review/decisions/20261005-two-records-batch13.yaml
    sha256: 3a67653fd9c38b7df2fb08988dee48c4b0166cd1fab67d65cf7441e34d6e2739
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
- target_id: CommunityMech:000016
  path: kb/communities/Chlorella_Rhizobium_Bioflocculation.yaml
  label: Chlorella-Rhizobium Bioflocculation
  kind: maintained
  record_class: MicrobialCommunity
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Chlorella_Rhizobium_Bioflocculation.yaml
    role: canonical_record
scope:
  description: Whole canonical record, both members, both nodes and the arrow assessed
    against direct Abstract/Significance, current authorities, prior provenance and
    bounded access evidence; full scientific verification remains partial.
  selection: Only released CommunityMech:000016 in the owned batch 10 checkout.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000016
checks:
- check_id: validate
  name: validate
  status: passed
  required: true
  summary: Schema validation passed.
  target_ids:
  - CommunityMech:000016
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src
    just --no-dotenv validate kb/communities/Chlorella_Rhizobium_Bioflocculation.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate
  scope_note: Fresh focused execution in the owned batch 10 checkout. Native/schema/lexical
    success does not certify inaccessible scientific methods or unsupported explanatory
    claims.
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Strict validation passed.
  target_ids:
  - CommunityMech:000016
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src
    just --no-dotenv validate-strict kb/communities/Chlorella_Rhizobium_Bioflocculation.yaml
    --out /private/tmp/cm-review-session/batch-10/000016/strict-report.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-strict
  scope_note: Fresh focused execution in the owned batch 10 checkout. Native/schema/lexical
    success does not certify inaccessible scientific methods or unsupported explanatory
    claims.
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Encoded ID-label validation passed.
  target_ids:
  - CommunityMech:000016
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src
    just --no-dotenv validate-terms kb/communities/Chlorella_Rhizobium_Bioflocculation.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-terms
  scope_note: Fresh focused execution in the owned batch 10 checkout. Native/schema/lexical
    success does not certify inaccessible scientific methods or unsupported explanatory
    claims.
- check_id: validate-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: GTDB structure and ambiguity coherence passed.
  target_ids:
  - CommunityMech:000016
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src
    just --no-dotenv validate-gtdb kb/communities/Chlorella_Rhizobium_Bioflocculation.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb
  scope_note: Fresh focused execution in the owned batch 10 checkout. Native/schema/lexical
    success does not certify inaccessible scientific methods or unsupported explanatory
    claims.
- check_id: validate-gtdb-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: Taxon domain applicability passed.
  target_ids:
  - CommunityMech:000016
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src
    just --no-dotenv validate-gtdb-domain kb/communities/Chlorella_Rhizobium_Bioflocculation.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb-domain
  scope_note: Fresh focused execution in the owned batch 10 checkout. Native/schema/lexical
    success does not certify inaccessible scientific methods or unsupported explanatory
    claims.
- check_id: validate-history
  name: validate-history
  status: passed
  required: true
  summary: The sole append-only history record passed validation.
  target_ids:
  - CommunityMech:000016
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src
    just --no-dotenv validate-history history/records/Chlorella_Rhizobium_Bioflocculation
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-history
  scope_note: Fresh focused execution in the owned batch 10 checkout. Native/schema/lexical
    success does not certify inaccessible scientific methods or unsupported explanatory
    claims.
- check_id: normalize-cache-names-check
  name: normalize-cache-names-check
  status: passed
  required: true
  summary: Read-only cache filename normalization check passed.
  target_ids:
  - CommunityMech:000016
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src
    uv run python scripts/normalize_cache_names.py --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-normalize-cache-names-check
  scope_note: Fresh focused execution in the owned batch 10 checkout. Native/schema/lexical
    success does not certify inaccessible scientific methods or unsupported explanatory
    claims.
- check_id: validate-references-explained
  name: validate-references-explained
  status: passed
  required: true
  summary: Native references passed against the unchanged selected-excerpt cache;
    direct-source matching and biological support remain separate checks.
  target_ids:
  - CommunityMech:000016
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src
    just --no-dotenv validate-references-explained kb/communities/Chlorella_Rhizobium_Bioflocculation.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-references-explained
  scope_note: Fresh focused execution in the owned batch 10 checkout. Native/schema/lexical
    success does not certify inaccessible scientific methods or unsupported explanatory
    claims.
- check_id: audit-network
  name: audit-network
  status: failed
  required: true
  summary: Fresh batch 10 corpus diagnostic retains unrelated warnings; the focal
    two-node/one-arrow graph separately reports COMPLETE.
  target_ids:
  - CommunityMech:000016
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv audit-network
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-audit-network
  - metrics
  scope_note: Explicit same-batch corpus reuse. The actual nonzero corpus status is
    not attributed as a new defect of this target.
- check_id: check-network-quality
  name: check-network-quality
  status: failed
  required: true
  summary: Fresh batch 10 corpus diagnostic retains unrelated warnings; the focal
    two-node/one-arrow graph separately reports COMPLETE.
  target_ids:
  - CommunityMech:000016
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv check-network-quality
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-check-network-quality
  - metrics
  scope_note: Explicit same-batch corpus reuse. The actual nonzero corpus status is
    not attributed as a new defect of this target.
- check_id: scientific-source
  name: Full main and critical supplementary verification
  status: unavailable
  required: true
  summary: Full focal Methods/Results, figures and actual S1–S4 contents remain inaccessible
    and unread. Direct Abstract/Significance support bounded findings; scientific
    review remains partial.
  target_ids:
  - CommunityMech:000016
  evidence_ids:
  - access
  - lead-read
  - root-source
  - source-scope
- check_id: direct-snippets
  name: Fresh source-specific excerpt verification
  status: passed
  required: true
  summary: All twelve occurrences match direct publisher Abstract/Significance and
    cache; ten also match EPMC, with exact publisher typography supplying the other
    two.
  target_ids:
  - CommunityMech:000016
  evidence_ids:
  - snippets
  - publisher-projection
- check_id: supplements
  name: Critical supplementary source access
  status: unavailable
  required: true
  summary: Exact DOCX listing and four table titles are verified, but linked/static
    responses are 403 HTML. No cells or supplementary statistical details were read.
  target_ids:
  - CommunityMech:000016
  evidence_ids:
  - supplement-listing
  - resources
  - access
- check_id: resources
  name: Publication and bounded resource identity
  status: passed
  required: true
  summary: Exact focal bibliographic identity and public SI listing verified; no global
    resource absence or recipe equivalence inferred.
  target_ids:
  - CommunityMech:000016
  evidence_ids:
  - resources
  - source-metadata
- check_id: reanalysis
  name: Raw data and experimental reproduction
  status: skipped
  required: false
  summary: No culture experiment, raw sequence analysis, RSM refitting or statistical
    reproduction was performed.
  target_ids:
  - CommunityMech:000016
  evidence_ids:
  - lead-read
  - root-read
- check_id: adapter
  name: Optional structured source adapter
  status: unavailable
  required: false
  summary: Explicit same-runtime discovery reuse preserves unavailable status and
    original scope. No paid or other-checkout executable was used.
  target_ids:
  - CommunityMech:000016
  evidence_ids:
  - adapter
evidence:
- evidence_id: record
  kind: record_content
  reference: kb/communities/Chlorella_Rhizobium_Bioflocculation.yaml
  locator: Entire maintained YAML, two taxa, two interaction nodes, one downstream
    arrow and discussion
  summary: The record describes a constructed Chlorella vulgaris–F2 coculture for
    harvesting in synthetic wastewater. The graph already limits chemical mediation
    and corrects the harvesting range; several non-graph statements retain stronger
    or different claims.
  support: supports
  accessed_at: '2026-10-21T18:46:46.786121Z'
- evidence_id: identity
  kind: primary_source
  reference: doi:10.1111/lam.12403; PMID:25693426
  locator: 'Significance and Impact of the Study: opening paragraph'
  summary: The directly inspected publisher identifies Chlorella vulgaris and bioflocculant-producing
    F2, named Rhizobium radiobacter, in synthetic wastewater. This supports the experimental
    pair and treatment application. It does not establish operation at an actual wastewater
    treatment plant, exact culture-stock continuity or a complete medium recipe.
  support: supports
  accessed_at: '2026-10-21T18:46:46.786197Z'
  snapshot_sha256: 5ea993fe3ce6c94f3cd5d0016d701306be2c3196d825f45ec54e073e9a2398d2
- evidence_id: harvesting
  kind: primary_source
  reference: doi:10.1111/lam.12403; PMID:25693426
  locator: 'Abstract: opening axenic baseline and results paragraph'
  summary: The source reports 0.2% flocculation for axenic C. vulgaris and 45–50%
    harvesting efficiency under optimized coculture conditions. Lipid content over
    21% is a separate content endpoint. The record’s overview exceeds 90%, whereas
    its harvesting node already gives the correct range. No full-text denominator,
    replicate, uncertainty or statistical comparison has been independently inspected.
  support: supports
  accessed_at: '2026-10-21T18:46:46.786459Z'
  snapshot_sha256: 5ea993fe3ce6c94f3cd5d0016d701306be2c3196d825f45ec54e073e9a2398d2
  quote: harvesting efficiency reached 45·0–50·0%
- evidence_id: optimization
  kind: primary_source
  reference: doi:10.1111/lam.12403; PMID:25693426
  locator: 'Abstract: RSM design, model statistics and optimized conditions'
  summary: The authors vary bacteria:microalgae inoculation ratio, initial glucose
    and coculture time using response surface methodology. The reported operating
    ranges are ratio 0.20–0.25, glucose below 1.5 kg/m3 and 9–14 days. Abstract model
    F-values 3.98/8.46 and R-squared values 0.7817/0.8711 are author-reported summaries,
    not a reproduced model or proof of each mechanistic interpretation. The ratio
    basis is unspecified in the accessed text.
  support: supports
  accessed_at: '2026-10-21T18:46:46.786509Z'
  snapshot_sha256: 5ea993fe3ce6c94f3cd5d0016d701306be2c3196d825f45ec54e073e9a2398d2
- evidence_id: chemical-scope
  kind: primary_source
  reference: doi:10.1111/lam.12403; PMID:25693426
  locator: 'Abstract and Significance and Impact of the Study: bioflocculant-producing
    partner and prospective benefits'
  summary: The focal source identifies a bioflocculant-producing partner and improved
    harvesting. The accessed text does not identify the product chemistry, isolate
    its causal mediation, trace algal carbon transfer or measure reciprocal fitness.
    Environmental and cost benefits are framed as significance and prospects; the
    accessible sections do not expose a comparative cost, energy or safety experiment.
    Earlier exact-F2 EPS leads do not establish the focal coculture mediator and are
    not disproven by this access limit.
  support: supports
  accessed_at: '2026-10-21T18:46:46.786545Z'
  snapshot_sha256: 5ea993fe3ce6c94f3cd5d0016d701306be2c3196d825f45ec54e073e9a2398d2
- evidence_id: protocol-scope
  kind: primary_source
  reference: doi:10.1111/lam.12403; PMID:25693426
  locator: 'Abstract: three process variables; Significance and Impact of the Study:
    synthetic wastewater'
  summary: The source supports the named medium context and optimization variables.
    It does not report illumination intensity/photoperiod, a complete recipe, initial
    viable density, vessel, temperature, pH, strain-specific counts or member persistence
    in the accessed sections. Identifying an alga does not supply a tested illumination
    regime. Ratio and time optimization do not directly establish reduced bacterial
    contamination, nutrient depletion or culture instability.
  support: supports
  accessed_at: '2026-10-21T18:46:46.786574Z'
  snapshot_sha256: 5ea993fe3ce6c94f3cd5d0016d701306be2c3196d825f45ec54e073e9a2398d2
- evidence_id: supplement-listing
  kind: primary_source
  reference: https://enviromicro-journals.onlinelibrary.wiley.com/doi/abs/10.1111/lam.12403
  locator: 'Supporting Information: lam12403-sup-0001-TableS1-S4.docx, advertised
    23.9 KB'
  summary: The publisher lists S1 design matrix/results, S2 independent variables
    for the central composite design, and S3/S4 ANOVA for flocculation and lipid content.
    These are verified table titles only. Linked and ordinary static download routes
    returned 403 HTML, not a DOCX; no table cells or figures were inspected.
  support: supports
  accessed_at: '2026-10-21T18:46:46.786601Z'
  snapshot_sha256: 2abe5b02e7979a1b345ba9f72783d4207405c105d4ce445145dc4306ab03fceb
- evidence_id: access
  kind: validation
  reference: Public Wiley/OUP main and supplementary routes; OpenAlex and Europe PMC
    metadata
  locator: Frozen lead access receipts and body signatures
  summary: Direct publisher Abstract and Significance are available. Main/full/PDF
    routes failed or resolved to the abstract; metadata indicates subscription access
    without an available PMC/repository copy. The correct OUP article identifier is
    6699742. Public linked and static SI responses were access-denial HTML. These
    bounded attempts do not establish global absence of authorized copies.
  support: supports
  accessed_at: '2026-10-21T18:46:46.786850Z'
  snapshot_sha256: 409c8133a9f98b837f4d0937b5bf2860c1b6bf37238ae36dd21c972973092ce9
- evidence_id: schema
  kind: authority
  reference: src/communitymech/schema/communitymech.yaml
  locator: FunctionalRoleEnum.PRIMARY_DEGRADER and PRIMARY_PRODUCER; MetalRelevanceEnum.SIGNIFICANT;
    environment_term, abundance_value and inoculum_size slots
  summary: PRIMARY_DEGRADER concerns complex-substrate degradation, not flocculant
    production. Algal PRIMARY_PRODUCER can express broad carbon-fixing capability
    without proving exchange. SIGNIFICANT concerns significant metal/REE metabolism.
    Quantitative abundance and initial density/transfer fields are not containers
    for functional prose or an inoculation composition ratio. Actual environmental
    context is distinct from treatment application.
  support: supports
  accessed_at: '2026-10-21T18:46:46.786977Z'
  snapshot_sha256: c41630d09def826256ddb6678c1ce31fa71e3b074219bb9d217d98035a5324ee
- evidence_id: ontology
  kind: authority
  reference: ontology-authority.json
  locator: Whole frozen receipt and declared scope
  summary: 'All four distinct encoded ID-label pairs match across nine occurrences:
    the two taxon concepts, wastewater treatment plant and cell aggregation. Correct
    labels do not establish that a plant was the actual experimental setting or identify
    the flocculant mechanism.'
  support: supports
  accessed_at: '2026-10-21T18:46:46.787043Z'
  snapshot_sha256: d128cb8fc84e90d45658119e3570be9d02467c831d82f1eb60a8dad15c3708ec
- evidence_id: strain-authority
  kind: authority
  reference: child-F2-strain-authority.json
  locator: authority; local_OAK; generic_name_comparison; exact_strain_crosswalk.rows
    and scope; focal_source_scope
  summary: Direct exact-strain NCBI node 1050720 explicitly lists Rhizobium radiobacter
    F2 and parent 358, supporting retention of the current species-parent grounding.
    Generic Rhizobium radiobacter maps to a different concept, 362, and is not an
    automatic replacement. Local OAK uses strain rank while the live page displays
    no rank; no raw laboratory-stock sequence identity is certified. The exact F2
    taxid 1050720 crosswalk separately maps to Agrobacterium oryzihabitans in two
    genomes at fraction 1.0. This optional exact-strain context is not silently transferred
    into the species-level record.
  support: supports
  accessed_at: '2026-10-21T18:46:46.787242Z'
  snapshot_sha256: 56589cf82d43fb971a2555a9fd602e11a17aee2b93e895ade9db651c68c1201c
- evidence_id: taxonomy-scope
  kind: authority
  reference: child-schema-taxonomy-scope.json
  locator: Whole frozen receipt and declared scope
  summary: The four current species-level GTDB candidates are retained. Optional ENVO:01001405
    laboratory environment is authority-checked as a possible actual-context term
    subject to source confidence. Scope and rank metadata are explicit; no canonical
    term is replaced during this review.
  support: supports
  accessed_at: '2026-10-21T18:46:46.787362Z'
  snapshot_sha256: 48076dcf15563e10f1be48151c951f9bfff06dc8738642bf067574f88c40f046
- evidence_id: gtdb
  kind: authority
  reference: child-gtdb-crosswalk.json
  locator: exact_id_rows; exact_species_name_row_count; name_group_gtdb_species; scope
  summary: The current species-name group has fifteen rows across four GTDB species
    and remains ambiguous. Exact species ID 358 has no direct row. This receipt reproduces
    the current species-level mapping; it does not establish F2 identity or select
    a single candidate.
  support: supports
  accessed_at: '2026-10-21T18:46:46.787492Z'
  snapshot_sha256: df59919b3fba4e487455ebce08b61d8867b765e4e632da17cc2a814f21ef51d5
- evidence_id: semantics
  kind: authority
  reference: ontology-semantic-notes.json
  locator: Whole frozen receipt and declared scope
  summary: Independent schema/authority assessment agrees with the two major and two
    minor groups, retained taxon/graph scope and partial source status. GO cell aggregation
    fits clustering without proving biofilm formation, EPS mediation or reciprocal
    fitness.
  support: supports
  accessed_at: '2026-10-21T18:46:46.787609Z'
  snapshot_sha256: 76cfe7b67b62c6a019a5597ce30be4ac773d05c9d1bbac68012eb2202eac7256
- evidence_id: resources
  kind: database
  reference: dataset-verification.json
  locator: Whole frozen receipt and declared scope
  summary: PMID/DOI/title and the exact supplement listing are verified. No usable
    focal supplement contents or source-linked independent dataset were recovered
    within the bounded access scope. This is not a dataset absence finding, a complete
    recipe claim or authorization to substitute an earlier F2 genome for focal coculture
    data.
  support: supports
  accessed_at: '2026-10-21T18:46:46.787736Z'
  snapshot_sha256: 30bcc2ec321221ba48c9d1ba2a03679c0ccddb4c5371a7254fd87d3db4669162
- evidence_id: source-metadata
  kind: database
  reference: source-metadata-audit.json
  locator: Whole frozen receipt and declared scope
  summary: The exact 2015 publication is verified. Publisher online, PubMed electronic
    and issue dates have different metadata scopes; their differences are not graded
    as a record error.
  support: supports
  accessed_at: '2026-10-21T18:46:46.787851Z'
  snapshot_sha256: 0824a3e60322f3bf1c1dde41c7b29c18fe516af19aca9d9a6bdb15eb70ba91b0
- evidence_id: snippets
  kind: validation
  reference: snippet-audit.json
  locator: Whole frozen receipt and declared scope
  summary: 'All twelve evidence occurrences match fresh publisher Abstract/Significance
    and the selected-excerpt cache: ten abstract and two Significance occurrences.
    Ten also match EPMC directly; two exact publisher range/unit forms differ from
    EPMC typography. No broad punctuation substitution or full-main match claim is
    used.'
  support: supports
  accessed_at: '2026-10-21T18:46:46.787970Z'
  snapshot_sha256: 033de44cfedcca9ab958d3b51b006ba39a41865db754c3a759b4a67a9ac2b9f7
- evidence_id: publisher-projection
  kind: validation
  reference: publisher-abstract-projection.json
  locator: Whole frozen receipt and declared scope
  summary: The direct publisher text supports the exact en-dash and superscript/unit
    forms in the record. Literal excerpt matching is separately evaluated from the
    larger explanatory claims attached to those excerpts.
  support: supports
  accessed_at: '2026-10-21T18:46:46.788074Z'
  snapshot_sha256: 37433c646aadeddd1e860284cd7efae9ed8022713a2ef5cdaeead6485ea834a2
- evidence_id: history
  kind: record_content
  reference: provenance-audit.json
  locator: Whole frozen receipt and declared scope
  summary: Whole sole history and exact prior batch 13 row were read. Open issue 561
    owns F2 role/shared vocabulary follow-up; open 1301 owns non-graph summary, environment,
    process and metal follow-up. Closed/completed 1299 is explicitly reused with its
    original same-session retrieval and complete comment; historical keep-open wording
    does not override its current closed status.
  support: supports
  accessed_at: '2026-10-21T18:46:46.788140Z'
  snapshot_sha256: 467beb822687f3d81bd87992d8e608cc5ee64ccc6f58cf0fc6cd9a619bf3c084
- evidence_id: inspect
  kind: validation
  reference: inspect.json
  locator: Whole frozen receipt and declared scope
  summary: The fresh official inspect establishes 25 input hashes, exact maintained
    target/class and batch 10 base. All inputs remain unchanged; prior-record inspection
    is not inherited.
  support: supports
  accessed_at: '2026-10-21T18:46:46.788277Z'
  snapshot_sha256: b1ecf8da4eb72fe0d588c632fc23f64ad0de097f74bcfaad560675796295ab09
- evidence_id: metrics
  kind: validation
  reference: support-audit.json
  locator: Whole frozen receipt and declared scope
  summary: Two interaction nodes, one arrow and three node-evidence entries give mean
    1.5 and native COMPLETE. Completeness is 75. Two major and two minor findings
    yield raw quality 106, capped at 100. These are mechanical scores, not scientific
    completion.
  support: supports
  accessed_at: '2026-10-21T18:46:46.788302Z'
  snapshot_sha256: 4233ad09586c8c2ffcae024e2eab00fd7c659f5aade0517691e3cea0fb06e0d1
- evidence_id: support-manifest
  kind: validation
  reference: supporting-artifact-manifest.json
  locator: Whole frozen receipt and declared scope
  summary: The frozen support manifest pins provenance, source-specific snippets,
    resources, score arithmetic, official input integrity and final root/lead source
    receipts.
  support: supports
  accessed_at: '2026-10-21T18:46:46.788322Z'
  snapshot_sha256: 5bba471e7e64bcf18a74d735d3a407331ac179f1ad919503d48c67da7096005d
- evidence_id: lead-read
  kind: validation
  reference: lead-primary-read-scope.json
  locator: Whole frozen receipt and declared scope
  summary: Lead read the whole canonical, selected-excerpt cache, sole history and
    exact prior row, fresh direct Abstract/Significance, access metadata and frozen
    authorities. Full focal main, figures and SI remain unread; earlier F2 discovery
    is bounded identity context.
  support: supports
  accessed_at: '2026-10-21T18:46:46.788535Z'
  snapshot_sha256: 409c8133a9f98b837f4d0937b5bf2860c1b6bf37238ae36dd21c972973092ce9
- evidence_id: source-scope
  kind: validation
  reference: source-audit.json
  locator: Whole frozen receipt and declared scope
  summary: Lead assessment is partial with scientific_review false, two major and
    two minor findings, completeness 75 and raw quality 106. Findings separate demonstrable
    abstract-level correction from unresolved full-source questions.
  support: supports
  accessed_at: '2026-10-21T18:46:46.788556Z'
  snapshot_sha256: 3e019840d2095247a08a4be2742c40f480dee71fa5dc7aed58a07b7693535509
- evidence_id: root-source
  kind: validation
  reference: root-independent-source-audit.json
  locator: Whole frozen receipt and declared scope
  summary: Root independently read the whole canonical and fresh direct Abstract/Significance,
    checked all twelve excerpts, and assessed authority, provenance and access limits.
    The independent scientific review also remains partial.
  support: supports
  accessed_at: '2026-10-21T18:46:46.788782Z'
  snapshot_sha256: cbdd8f36f9ff08989e46bcd2cab903cc7e82f1b5dc7063b3539f76f2bf1a109e
- evidence_id: root-read
  kind: validation
  reference: root-primary-read.json
  locator: Whole frozen receipt and declared scope
  summary: Exact independent root read scope and raw-source pins are preserved. Root
    did not inspect the focal main/SI, full earlier genome paper or full RSC manuscript;
    earlier EPS leads do not disprove or establish focal mediation.
  support: supports
  accessed_at: '2026-10-21T18:46:46.788914Z'
  snapshot_sha256: ab3dfffaec0ba42d01e5dc2a71384711d76900445d0e29d3a600db1e9aac97af
- evidence_id: auxiliary
  kind: validation
  reference: auxiliary-frozen-manifest.json
  locator: Whole frozen receipt and declared scope
  summary: All eight focused native checks pass; four ontology pairs match across
    nine occurrences. Initial native summary is immutable, and later metadata is a
    separate final summary.
  support: supports
  accessed_at: '2026-10-21T18:46:46.789034Z'
  snapshot_sha256: 65e9e65e4e6660d4b756d0b157da070eb3338afd07532d7318300dafa566e5f0
- evidence_id: final-native
  kind: validation
  reference: final-validator-summary.json
  locator: Whole frozen receipt and declared scope
  summary: The separate final native summary pins the original eight execution records
    without rewriting the initial validator summary. Optional GTDB grounder exit 1
    is preserved as ambiguity, outside those eight passing gates.
  support: supports
  accessed_at: '2026-10-21T18:46:46.789141Z'
  snapshot_sha256: 74e0bd98ece399da4b244cb46d46ebe71886b18e8554272fe929f5f85f53b4cd
- evidence_id: adapter
  kind: validation
  reference: adapter-check.json
  locator: Whole frozen receipt and declared scope
  summary: Optional adapter unavailability is explicitly reused from the same verified
    batch 10 runtime, with its original retrieval timestamp and bounded ignored-inclusive
    discovery. No executable from another checkout or paid provider was invoked.
  support: supports
  accessed_at: '2026-10-21T18:46:46.789240Z'
  snapshot_sha256: adb1e1145b630b44802e9353a2896e9f521bea25c4c86b7c53252b2620a2a133
- evidence_id: check-validate
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src
    just --no-dotenv validate kb/communities/Chlorella_Rhizobium_Bioflocculation.yaml
  locator: Actual execution 2026-10-21T18:38:07.919542+00:00 to 2026-10-21T18:38:09.311778+00:00
  summary: Schema validation passed.
  support: supports
  accessed_at: '2026-10-21T18:38:09.311778Z'
  snapshot_sha256: 7cc4154059bde7c68cd1f9752fcd3551a6ed1658c1b996cacb47b735a970eff6
- evidence_id: check-validate-strict
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src
    just --no-dotenv validate-strict kb/communities/Chlorella_Rhizobium_Bioflocculation.yaml
    --out /private/tmp/cm-review-session/batch-10/000016/strict-report.tsv
  locator: Actual execution 2026-10-21T18:38:07.919813+00:00 to 2026-10-21T18:38:13.986022+00:00
  summary: Strict validation passed.
  support: supports
  accessed_at: '2026-10-21T18:38:13.986022Z'
  snapshot_sha256: 8eda21898feb1ca203ff50996ed27826f45e76662af4da0831d1afbb9ead0215
- evidence_id: check-validate-terms
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src
    just --no-dotenv validate-terms kb/communities/Chlorella_Rhizobium_Bioflocculation.yaml
  locator: Actual execution 2026-10-21T18:38:07.919906+00:00 to 2026-10-21T18:38:12.728411+00:00
  summary: Encoded ID-label validation passed.
  support: supports
  accessed_at: '2026-10-21T18:38:12.728411Z'
  snapshot_sha256: 2c04e053b5a9bd28310653cce5695353a7c15e70c35d603c3f955893949643de
- evidence_id: check-validate-gtdb
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src
    just --no-dotenv validate-gtdb kb/communities/Chlorella_Rhizobium_Bioflocculation.yaml
  locator: Actual execution 2026-10-21T18:38:09.312187+00:00 to 2026-10-21T18:38:09.449209+00:00
  summary: GTDB structure and ambiguity coherence passed.
  support: supports
  accessed_at: '2026-10-21T18:38:09.449209Z'
  snapshot_sha256: d72ce623307d7b1f97cc6b7daeb5211338accdfd9efedd795f7e04a57434b6d2
- evidence_id: check-validate-gtdb-domain
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src
    just --no-dotenv validate-gtdb-domain kb/communities/Chlorella_Rhizobium_Bioflocculation.yaml
  locator: Actual execution 2026-10-21T18:38:09.449494+00:00 to 2026-10-21T18:38:14.327610+00:00
  summary: Taxon domain applicability passed.
  support: supports
  accessed_at: '2026-10-21T18:38:14.327610Z'
  snapshot_sha256: 17da4f5c12df256f7c62a0edbf5ecbea51e02ddb578648265571cd8d43c8b93a
- evidence_id: check-validate-history
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src
    just --no-dotenv validate-history history/records/Chlorella_Rhizobium_Bioflocculation
  locator: Actual execution 2026-10-21T18:38:12.728899+00:00 to 2026-10-21T18:38:14.409466+00:00
  summary: The sole append-only history record passed validation.
  support: supports
  accessed_at: '2026-10-21T18:38:14.409466Z'
  snapshot_sha256: 517c6db3dcfa3acde9281430aa5f02d14b7a6ee5d51da2da64764b2b2a5d55be
- evidence_id: check-normalize-cache-names-check
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src
    uv run python scripts/normalize_cache_names.py --check
  locator: Actual execution 2026-10-21T18:38:14.410707+00:00 to 2026-10-21T18:38:14.494905+00:00
  summary: Read-only cache filename normalization check passed.
  support: supports
  accessed_at: '2026-10-21T18:38:14.494905Z'
  snapshot_sha256: 35fccdec29535357d22724ee299404d476a7ce44f02c288f695cdc921346fe45
- evidence_id: check-validate-references-explained
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src
    just --no-dotenv validate-references-explained kb/communities/Chlorella_Rhizobium_Bioflocculation.yaml
  locator: Actual execution 2026-10-21T18:38:14.495174+00:00 to 2026-10-21T18:38:16.219142+00:00
  summary: Native references passed against the unchanged selected-excerpt cache;
    direct-source matching and biological support remain separate checks.
  support: supports
  accessed_at: '2026-10-21T18:38:16.219142Z'
  snapshot_sha256: d9a98d96f6f5975e9692828c6102dd5dd54feb3ee4d26567af8df6ad07fd3996
- evidence_id: check-audit-network
  kind: validation
  reference: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv audit-network
  locator: Actual execution 2026-10-21T17:04:17.819938+00:00 to 2026-10-21T17:04:25.370848+00:00
  summary: Fresh batch 10 corpus diagnostic retains unrelated warnings; the focal
    two-node/one-arrow graph separately reports COMPLETE.
  support: supports
  accessed_at: '2026-10-21T17:04:25.370848Z'
  snapshot_sha256: 301cbda477198c0cff0f38601fdb49af8d805cafa7da106733150d64786d987d
- evidence_id: check-check-network-quality
  kind: validation
  reference: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv check-network-quality
  locator: Actual execution 2026-10-21T17:04:17.819995+00:00 to 2026-10-21T17:04:26.163649+00:00
  summary: Fresh batch 10 corpus diagnostic retains unrelated warnings; the focal
    two-node/one-arrow graph separately reports COMPLETE.
  support: supports
  accessed_at: '2026-10-21T17:04:26.163649Z'
  snapshot_sha256: f8dae0e292e8e2f8c221450aacc2bb120abe0e3f32c16ed59f8406e8b859a895
assessments:
- assessment_id: identity
  area: identity
  topic: Community identity and source strain
  outcome: supported
  summary: Retain the constructed C. vulgaris–F2 pair and current broad taxon grounding.
  target_ids:
  - CommunityMech:000016
  evidence_ids:
  - identity
  - strain-authority
  - ontology
  - gtdb
  details: Exact F2 authority supports parent NCBITaxon:358 despite the generic Rhizobium
    radiobacter name pointing elsewhere. Do not automatically substitute NCBITaxon:362,
    select one of the four species-scope GTDB candidates or promote the record to
    an exact strain node. This is authority reconciliation, not proof of a sequenced
    2015 experimental stock. The paper name remains a source synonym.
- assessment_id: state
  area: identity
  topic: Origin, state, category and physical environment
  outcome: concern
  summary: ENGINEERED origin/state and PHYTOPLANKTON category fit; physical treatment-plant
    context is not established.
  target_ids:
  - CommunityMech:000016
  evidence_ids:
  - identity
  - schema
  - ontology
  - taxonomy-scope
  details: The source describes a controlled synthetic-wastewater coculture and prospective
    treatment application. The encoded ENVO term denotes an actual wastewater treatment
    plant. Separate application from location. Laboratory environment is an authority-checked
    candidate only if source confidence supports that physical context; an unresolved
    field is preferable to an unsupported precise facility.
- assessment_id: taxon-alga
  area: evidence
  topic: 'taxonomy[0]: Chlorella vulgaris'
  outcome: concern
  summary: Retain algal membership and broad PRIMARY_PRODUCER capability; narrow evidence
    explanations and relocate functional abundance prose.
  target_ids:
  - CommunityMech:000016
  evidence_ids:
  - identity
  - harvesting
  - schema
  - semantics
  details: Poor axenic flocculation directly supports the baseline, not a necessity
    for bacterial assistance in all conditions or measured photosynthetic production
    in this assay. The abundance_value string is a role statement, not a quantitative
    abundance observation. NO_GTDB_EQUIVALENT is appropriate for the eukaryotic alga.
    No new cell ratio, stable abundance or carbon-transfer role is inferred.
- assessment_id: taxon-f2
  area: evidence
  topic: 'taxonomy[1]: F2 role, product notes and abundance'
  outcome: concern
  summary: Retain membership and bioflocculant association; PRIMARY_DEGRADER is unsupported
    by the attached source claim.
  target_ids:
  - CommunityMech:000016
  evidence_ids:
  - identity
  - chemical-scope
  - schema
  - strain-authority
  - semantics
  details: Producing a flocculant and using supplied glucose do not demonstrate degradation
    of complex substrates. Roles are optional, so removing the unsupported enum does
    not require inventing another role. EPS capability reported in earlier F2 literature
    is not disproven, but exact focal-coculture product identity and mediation remain
    unverified. The helper/optimized-ratio abundance string belongs in source-scoped
    notes, not quantitative abundance.
- assessment_id: overview
  area: evidence
  topic: description and non-graph source explanations
  outcome: concern
  summary: Correct over-90% harvesting and distinguish observed recovery from chemical
    and economic interpretation.
  target_ids:
  - CommunityMech:000016
  evidence_ids:
  - record
  - harvesting
  - chemical-scope
  - snippets
  details: 'The range in the overview contradicts both the abstract and the current
    harvesting node. Retain 45–50% and the separate over-21% lipid content with optimized-condition
    context. Attribute environmental and cost prospects to the authors rather than
    present a measured comparative advantage. Restrict explanatory prose to the attached
    claim: a short harvesting or taxon-name excerpt does not prove photosynthetic
    mode, chemical mediation or general physiological necessity.'
- assessment_id: design
  area: evidence
  topic: engineering_design objective, assembly, endpoints and perturbation
  outcome: concern
  summary: Harvesting optimization is supported; generic mechanism/persistence endpoints
    and a tested light factor are not established.
  target_ids:
  - CommunityMech:000016
  evidence_ids:
  - identity
  - optimization
  - protocol-scope
  - history
  details: Bottom-up coculture at defined inoculation ratios is consistent with the
    abstract, but exact axenic stock preparation is not verified in Methods. Replace
    backfilled endpoints with harvesting efficiency, lipid content and the reported
    RSM variables. Do not turn three named optimization variables into a new mechanistic
    characterization or member-persistence experiment. Light is not one of the three
    variables listed in the accessed abstract.
- assessment_id: node-flocculation
  area: evidence
  topic: 'ecological_interactions[0]: Bioflocculant Production and Cell Aggregation'
  outcome: supported
  summary: Retain the source-directed, explicitly PARTIAL association node.
  target_ids:
  - CommunityMech:000016
  evidence_ids:
  - identity
  - chemical-scope
  - ontology
  - semantics
  details: F2 is the bioflocculant-associated source partner and C. vulgaris the harvested
    target. GO:0098743 cell aggregation fits the readout. The node already excludes
    product identity, charge neutralization/bridging, algal-exudate transfer, biofilm
    formation and reciprocal fitness. No stronger mechanism or carbon-transfer arrow
    is warranted from the accessed material.
- assessment_id: node-harvesting
  area: evidence
  topic: 'ecological_interactions[1]: Algal Biomass Harvesting'
  outcome: supported
  summary: Retain the community-level recovery endpoint and correct abstract range.
  target_ids:
  - CommunityMech:000016
  evidence_ids:
  - harvesting
  - ontology
  details: Both partners are appropriate participants in the measured coculture outcome.
    The node distinguishes 45–50% harvesting from the unsupported over-90% summary,
    and avoids mutualism or direct cost/energy conclusions. Its two evidence entries
    support the optimized range and axenic baseline. No improvement in lipid productivity,
    absolute biomass or comparative energy use is inferred from lipid content alone.
- assessment_id: arrow
  area: evidence
  topic: ecological_interactions[0].downstream[0]
  outcome: supported
  summary: Retain the one qualified association-to-recovery arrow.
  target_ids:
  - CommunityMech:000016
  evidence_ids:
  - identity
  - harvesting
  - chemical-scope
  - semantics
  details: Direction from F2-associated aggregation to algal harvesting is the source’s
    applied interpretation, and the current PARTIAL description excludes a demonstrated
    specific mediator or bacterial fitness benefit. The arrow is not a selective-product
    intervention result. Its current qualification is sufficient for the accessible
    evidence; no graph expansion or reversal is required.
- assessment_id: environment-factors
  area: evidence
  topic: environmental_factors[0:4]
  outcome: concern
  summary: Retain source-reported ratio, glucose and time; remove unverified protocol
    and process extrapolations.
  target_ids:
  - CommunityMech:000016
  evidence_ids:
  - optimization
  - protocol-scope
  - schema
  details: The paper calls three process variables significant in its RSM framing,
    but the full individual-term analysis is unread. A photosynthetic species name
    supplies no tested photoperiod. Ratio basis is not established as cell counts,
    and contamination minimization is not an accessed endpoint. Nutrient depletion
    and instability with longer incubation are generic possibilities, not demonstrated
    results of this experiment. No absolute counts or substitute causal claims should
    be added.
- assessment_id: cultivation
  area: completeness
  topic: growth_media[0] and cultivation setup
  outcome: concern
  summary: Preserve the three abstract-supported ranges while separating composition
    ratio from inoculum density.
  target_ids:
  - CommunityMech:000016
  evidence_ids:
  - identity
  - optimization
  - protocol-scope
  - schema
  details: Synthetic wastewater, 9–14 days and glucose below 1.5 kg/m3 are supported.
    The 0.20–0.25 bacteria:alga composition ratio is not an initial density or transfer
    percentage and should move to appropriate setup or preparation notes with unknown
    basis. Do not infer CFU, cells, percent v/v or absolute inoculum. Complete formulation,
    temperature, pH, vessel, mixing, atmosphere and illumination remain unresolved,
    not confirmed absent from the full source. No CultureMech equivalence follows
    from the medium name.
- assessment_id: metals
  area: evidence
  topic: metals_present, metal_relevance and metal_notes
  outcome: concern
  summary: Remove or explicitly substantiate keyword-derived significant iron metabolism.
  target_ids:
  - CommunityMech:000016
  evidence_ids:
  - record
  - schema
  - semantics
  - protocol-scope
  details: The current boilerplate does not cite an iron measurement or metal-metabolism
    mechanism. SIGNIFICANT is not justified merely because a growth medium might contain
    trace iron or a separate reference discusses chemical flocculants. The unknown
    complete recipe prevents any global claim that iron is absent; correcting this
    flag is a bounded evidence repair.
- assessment_id: resources
  area: completeness
  topic: Study resources, medium links and source access
  outcome: unknown
  summary: Publication and SI listing are verified; focal datasets and complete source
    protocols remain unresolved.
  target_ids:
  - CommunityMech:000016
  evidence_ids:
  - supplement-listing
  - resources
  - source-metadata
  - access
  details: No external resource or associated dataset is currently encoded, and no
    dataset omission is graded. S1–S4 are known by title only. The earlier F2 genome
    accession and EPS paper are identity/background leads, not focal 2015 experimental
    datasets. Do not invent an archive, use publication landing pages as phenotype
    accessions or contact authors during this review.
- assessment_id: history
  area: provenance
  topic: Reference cache, prior review, discussions and issue ownership
  outcome: supported
  summary: Retain the qualified graph repair and existing source-gap discussion with
    exact issue scopes.
  target_ids:
  - CommunityMech:000016
  evidence_ids:
  - history
  - snippets
  - source-metadata
  - inspect
  details: The sole cache explicitly contains selected Abstract/Significance excerpts
    and is not falsely labeled a full paper. All twelve excerpts are matched to direct
    source text, but larger claims remain independently assessed. Open 561 owns the
    role/vocabulary question and open 1301 the non-graph follow-up. Closed 1299 records
    prior graph work. Neither a prior review nor a closed issue certifies all current
    prose. No issue is opened, closed or commented on here.
- assessment_id: validation
  area: schema
  topic: Native checks and immutable workflow
  outcome: supported
  summary: All eight focused checks pass; scientific verification remains partial.
  target_ids:
  - CommunityMech:000016
  evidence_ids:
  - auxiliary
  - final-native
  - snippets
  - inspect
  details: Canonical, cache, history and generated products are unchanged. Any review
    persistence is restricted to a new immutable review bundle. Initial and final
    native summaries are separate. Optional grounder exit 1 records expected species
    ambiguity, not a failure of the eight focused checks or a reason to force a GTDB
    candidate.
- assessment_id: metrics
  area: completeness
  topic: Native mechanical completeness and validation quality
  outcome: supported
  summary: Completeness is 75; raw quality 106 caps at 100 independently of the partial
    scientific status.
  target_ids:
  - CommunityMech:000016
  evidence_ids:
  - metrics
  metrics:
  - name: completeness
    value: 75
    unit: points
    minimum: 0
    maximum: 100
    definition: Required fields with taxon roles 50 + environment term 5 + at least
      three environmental factors 10 + growth media 10. Two interaction nodes earn
      no at-least-three-node bonus. No external resources, associated datasets or
      node-metabolite bonus applies. This counts field presence, not scientific correctness.
  - name: validation_quality
    value: 100
    unit: points
    minimum: 0
    maximum: 100
    definition: clamp(100 − 50P1 − 10P2 − 2P3 + 20min(mean node evidence/2,1) + 15
      if COMPLETE,0,100). P1=0, P2=2, P3=2, P4=0. Three node-evidence entries/two
      nodes give mean 1.5 and an evidence bonus of 15; COMPLETE adds 15. Raw 106 is
      capped at 100.
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
- finding_id: non-graph-source-overreach
  issue_key: cm-000016-issue1301-non-graph-source-overreach
  category: evidence
  severity: major
  native_severity: P2
  normalization_reason: 'P2: the quantitative overview contradicts the direct source
    and repaired graph, while unqualified chemical and comparative-benefit claims
    materially overstate the inspected evidence.'
  rule_id: review-checklist.claim-specific-scope-and-evidence
  status: open
  certainty: confirmed
  title: Align the overview and explanations with the focal source
  description: Replace over 90% with the source-reported 45–50% under optimized conditions
    and keep the 0.2% axenic baseline separate. Distinguish bioflocculant association
    from verified focal product chemistry/mediation and measured cost, energy or safety
    advantage. Earlier F2 EPS capability is not disproven. Restrict evidence explanations
    to the claims their excerpts support; general taxon capability is not a measured
    assay mechanism.
  target_ids:
  - CommunityMech:000016
  field_paths:
  - description
  - taxonomy[1].taxon_term.notes
  - engineering_design.evidence[0].explanation
  - taxonomy[0].evidence[0].explanation
  evidence_ids:
  - harvesting
  - chemical-scope
  - identity
  - schema
  - snippets
  - history
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Chlorella_Rhizobium_Bioflocculation.yaml
    role: canonical_record
- finding_id: unsupported-primary-degrader
  issue_key: cm-000016-issue561-primary-degrader
  category: evidence
  severity: major
  native_severity: P2
  normalization_reason: 'P2: an asserted functional role encodes degradation while
    the attached source establishes flocculant production; this is a substantive unsupported
    biological relation.'
  rule_id: review-checklist.claim-specific-scope-and-evidence
  status: open
  certainty: confirmed
  title: Remove or independently support F2 complex-substrate degradation
  description: PRIMARY_DEGRADER is not established by producing a flocculant or by
    supplied glucose. Omit the optional role until claim-specific evidence is available,
    preserving source-supported bioflocculant function in prose. Existing issue 561
    owns the role/shared vocabulary follow-up; a comment proposing another enum is
    not evidence that the current schema already contains it.
  target_ids:
  - CommunityMech:000016
  field_paths:
  - taxonomy[1].functional_role
  - taxonomy[1].evidence
  evidence_ids:
  - identity
  - chemical-scope
  - schema
  - semantics
  - history
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Chlorella_Rhizobium_Bioflocculation.yaml
    role: canonical_record
- finding_id: experimental-context-placement
  issue_key: cm-000016-issue1301-experimental-context-placement
  category: evidence
  severity: minor
  native_severity: P3
  normalization_reason: 'P3: bounded context/field-placement corrections preserve
    the supported pair, measured endpoints and optimization ranges; they do not require
    a new scientific mechanism.'
  rule_id: review-checklist.claim-specific-scope-and-evidence
  status: open
  certainty: confirmed
  title: Separate measured optimization from generic context and misplaced fields
  description: Distinguish synthetic wastewater and treatment application from an
    actual plant. Replace unsupported backfilled endpoints and light perturbation
    with source-supported RSM scope. Relocate functional abundance prose and composition
    ratio from quantitative abundance/inoculum-density fields. Remove unverified illumination,
    contamination, depletion and stability extrapolations without inventing missing
    Methods.
  target_ids:
  - CommunityMech:000016
  field_paths:
  - environment_term
  - engineering_design.measurement_endpoints
  - engineering_design.perturbation_design
  - engineering_design.notes
  - taxonomy[0].abundance_value
  - taxonomy[1].abundance_value
  - environmental_factors
  - growth_media[0].inoculum_size
  - growth_media[0].inoculum_unit
  - growth_media[0].preparation_notes
  evidence_ids:
  - identity
  - optimization
  - protocol-scope
  - schema
  - taxonomy-scope
  - history
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Chlorella_Rhizobium_Bioflocculation.yaml
    role: canonical_record
- finding_id: unsupported-metal-significance
  issue_key: cm-000016-issue1301-metal-significance
  category: evidence
  severity: minor
  native_severity: P3
  normalization_reason: 'P3: unsupported optional metal metadata can be corrected
    locally without changing the community, harvesting endpoint or graph.'
  rule_id: review-checklist.claim-specific-scope-and-evidence
  status: open
  certainty: confirmed
  title: Remove unsupported keyword-derived iron significance
  description: IRON and SIGNIFICANT are supported only by keyword-detection boilerplate,
    with no identified claim-specific metal-metabolism evidence. Remove or substantiate
    these fields. Unknown medium composition is not evidence that iron was absent,
    and a reference to chemical flocculants would not establish significant biological
    iron cycling.
  target_ids:
  - CommunityMech:000016
  field_paths:
  - metals_present
  - metal_relevance
  - metal_notes
  evidence_ids:
  - schema
  - semantics
  - protocol-scope
  - history
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Chlorella_Rhizobium_Bioflocculation.yaml
    role: canonical_record
actions:
- action_id: repair-summary-and-explanations
  description: Correct the quantitative overview and source-specific non-graph interpretations.
  finding_ids:
  - non-graph-source-overreach
  target_ids:
  - CommunityMech:000016
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Chlorella_Rhizobium_Bioflocculation.yaml
    role: canonical_record
  acceptance_checks:
  - Use 45–50% harvesting efficiency under the stated optimized conditions versus
    0.2% axenic flocculation; preserve lipid content over 21% as a distinct content
    endpoint. Do not call it productivity, conversion yield or over-90% recovery.
  - Describe F2 as a bioflocculant-producing partner. Keep the focal product identity
    and mediation unresolved unless exact focal Methods/Results or a specific intervention
    assay supports them. Earlier F2 EPS reports may be separately attributed background
    but cannot silently certify the focal mediator.
  - Attribute cost-effectiveness and environmental promise as the authors’ significance
    framing unless an inspected comparison supports measured effects. Narrow the engineering/algal
    evidence explanations so a harvest or species-name excerpt does not prove photosynthetic
    mode or a universal need for bacterial assistance.
  - Retain both qualified interaction nodes and their one PARTIAL arrow, including
    the limits on polymer identity, carbon transfer, biofilm formation and reciprocal
    fitness. Keep the existing discussion open and reference issue 1301 without creating
    a duplicate.
- action_id: repair-f2-role
  description: Resolve the production-versus-degradation mismatch within existing
    issue 561.
  finding_ids:
  - unsupported-primary-degrader
  target_ids:
  - CommunityMech:000016
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Chlorella_Rhizobium_Bioflocculation.yaml
    role: canonical_record
  acceptance_checks:
  - Remove F2 PRIMARY_DEGRADER unless a directly inspected, claim-specific source
    establishes complex-substrate degradation relevant to the stated role. Preserve
    membership and bioflocculant-production notes; do not invent PRIMARY_PRODUCER,
    CROSS_FEEDER or another replacement enum.
  - Keep broader vocabulary discussion under the existing shared issue 561. Any separately
    authorized schema proposal must follow schema ownership and regeneration rules;
    no schema change is required merely to omit an unsupported optional role.
  - Retain exact F2 source naming, parent NCBITaxon:358 and the four species-level
    GTDB candidates. Do not substitute generic radiobacter 362 or silently import
    the exact-strain GTDB classification.
- action_id: repair-experimental-context
  description: Represent actual experimental scope and move nonquantitative content
    into suitable notes.
  finding_ids:
  - experimental-context-placement
  target_ids:
  - CommunityMech:000016
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Chlorella_Rhizobium_Bioflocculation.yaml
    role: canonical_record
  acceptance_checks:
  - Describe synthetic-wastewater experimental culture separately from wastewater-treatment
    application. Reconcile the treatment-plant environment term with direct physical-context
    evidence; use the authority-checked laboratory term only if supported, otherwise
    retain uncertainty rather than choose by lexical similarity.
  - Use harvest efficiency, lipid content and the ratio/glucose/time RSM design as
    supported endpoints/variables. Remove generic mechanism-characterization and member-persistence
    tracking claims unless the full source demonstrates those assays; do not claim
    light was a tested factor from an algal name alone.
  - Move both abundance_value role/design strings to source-qualified notes rather
    than invent quantitative abundance, counts or ranks. Preserve the 0.20–0.25 bacteria:microalgae
    composition ratio in suitable setup or preparation notes, removing it from inoculum_size/unit
    fields intended for initial density or transfer percentage. State that its cell,
    viable-count or volume basis is unverified; do not infer cells, CFU or percent
    v/v.
  - Retain synthetic wastewater, glucose below 1.5 kg/m3 and 9–14 days. Remove unsupported
    required/continuous/cyclic illumination and contamination/depletion/instability
    claims unless direct Methods/results support them. Do not infer full recipe, temperature,
    pH, vessel, aeration or mixing, and do not map a generic medium name to CultureMech.
- action_id: repair-metal-metadata
  description: Resolve the unsupported iron and significant-metal flags.
  finding_ids:
  - unsupported-metal-significance
  target_ids:
  - CommunityMech:000016
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Chlorella_Rhizobium_Bioflocculation.yaml
    role: canonical_record
  acceptance_checks:
  - Remove keyword-derived iron/significant-metal assertions or add exact source evidence
    for meaningful metal metabolism and the appropriate native category. Do not substitute
    an asserted absence category merely because the complete medium is unavailable.
  - Keep medium trace ingredients, chemical-flocculant comparisons and biological
    metal-metabolism evidence distinct. Reference the existing issue 1301 scope; do
    not add a new mechanism, metal ingredient or issue based on a keyword.
- action_id: complete-source-followup
  description: Complete the scientific assessment when authorized full main and supplementary
    evidence is available.
  finding_ids: []
  target_ids:
  - CommunityMech:000016
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Chlorella_Rhizobium_Bioflocculation.yaml
    role: canonical_record
  - repository: CultureBotAI/CommunityMech
    path: references_cache/doi_10.1111_lam.12403.md
    role: source_cache
  acceptance_checks:
  - Obtain the exact focal Methods/Results, figures and lam12403-sup-0001-TableS1-S4.docx
    through an authorized accessible or supplied copy. Preserve version, actual contents
    and section/table locators; the present named listing is metadata only.
  - Independently inspect experimental setup, ratio definition, harvest/lipid denominators,
    controls, replicates, model specification and supplementary ANOVA before changing
    partial scientific status. A high native score or abstract model fit does not
    substitute for that source review.
  - Assess exact product chemistry/mediation and F2 degradation claims against the
    focal assays. Preserve earlier strain-background versus focal-data boundaries;
    no raw genome or author-contact work is authorized by this review.
  - If later authorized curation adds main or supplementary excerpts, preserve source-specific
    cache provenance and exact locators. Do not relabel the current selected-excerpt
    cache as full text or merge inaccessible supplements into a main-text cache to
    manufacture matching.
- action_id: validate-authorized-curation
  description: Validate separately authorized curation and preserve historical evidence.
  finding_ids:
  - non-graph-source-overreach
  - unsupported-primary-degrader
  - experimental-context-placement
  - unsupported-metal-significance
  target_ids:
  - CommunityMech:000016
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Chlorella_Rhizobium_Bioflocculation.yaml
    role: canonical_record
  acceptance_checks:
  - Append fresh curation history after authorized canonical changes and run focused
    schema, strict, term, reference, GTDB/domain and history checks, followed by just
    gen-html and just check-docs-current. No canonical, cache, history or generated
    artifact is changed by this review.
  - Verify every new excerpt against its exact source and section. Preserve previous
    reviews, original source-access failures and immutable receipts. Only a new review
    bundle may be persisted here; neither native validation nor bundle persistence
    changes the explicit partial scientific status.
limitations:
- The focal paper is PMID 25693426, DOI 10.1111/lam.12403. Full direct publisher Abstract
  and Significance were read, together with fresh metadata and the whole selected-excerpt
  cache. Full scientific main, figures and S1–S4 contents remain unavailable and unread;
  completion is partial and scientific_review is false.
- Public full/PDF routes failed or resolved to abstract-only content. Linked and static
  supplement responses were 403 HTML rather than DOCX. Europe PMC and OpenAlex access
  flags describe the inspected metadata scope, not proof that no authorized full copy
  exists. No paywall, authentication or human-verification control was bypassed.
- The supplementary filename, advertised 23.9 KB size and four table titles are known
  only from the publisher listing. No table cells, CCD matrix, complete ANOVA, harvest
  denominator, uncertainty or replication detail is certified. Abstract model statistics
  are attributed to the authors and were not recomputed.
- Exact F2 authority supports the current species-parent mapping while generic radiobacter
  nomenclature differs. Neither metadata nor the optional two-genome exact-strain
  crosswalk proves raw-sequence stock continuity for the 2015 assay. Species-level
  GTDB ambiguity remains; local rank and live no-rank labels are preserved as distinct
  authority presentations.
- Earlier genome-announcement and RSC EPS leads were consulted only within declared
  identity/discovery limits. Full earlier papers and a culture collection entry were
  not scientifically inspected. Do not deny F2 EPS capability or treat an earlier
  strain-associated product as the proven focal coculture mediator.
- The ratio 0.20–0.25 is source-stated bacteria:microalgae composition with unknown
  basis, not a demonstrated cell ratio, viable density or transfer percentage. Glucose
  and 9–14 days are optimization ranges; a complete formulation and actual light,
  temperature, pH, vessel and mixing remain unresolved.
- Algal PRIMARY_PRODUCER denotes broad capability without proving measured photosynthesis
  or carbon transfer here. Flocculant production is not complex-substrate degradation.
  No new role, polymer mechanism, mutualism, biofilm, cost comparison or causal edge
  is inferred from excerpt matching or ontology consistency.
- All twelve excerpts match direct publisher text and cache. Ten also match EPMC exactly;
  two publisher range/unit forms differ from EPMC typography. This is a source-presentation
  boundary, not fabricated text or a full-body match. Explanatory overreach is assessed
  separately.
- Current open issues 561 and 1301 are the relevant existing owners. Closed 1299 is
  historical graph provenance, explicitly reused at its original retrieval time. Publisher
  online, PubMed electronic and issue dates are distinct metadata and are not treated
  as a scientific error.
- No source-declared focal dataset or exact medium identifier was verified within
  the bounded access scope. That is not proof of absence or a graded resource omission.
  No arbitrary archive search, raw-data analysis, RSM execution, experimental reproduction,
  paid service, author contact or later-record assessment occurred.
- Eight focused native checks pass; corpus diagnostics retain their actual broader
  failure scope. The optional GTDB grounder exit 1 records ambiguity. Completeness
  75 and capped quality 100/raw 106 do not override the scientific access limit or
  the four evidence-linked findings.
notes:
- All 25 official inspected inputs remain unchanged. No canonical, source-cache, history,
  generated or previously saved artifact was edited.
- Root and lead independently assessed fresh direct Abstract/Significance and bounded
  access evidence. Child owns native/ontology/strain checks; sibling owns provenance,
  snippets, resources and arithmetic. All source receipts are immutable.
- Two major and two minor findings yield completeness 75 and quality 100/raw 106.
  Partial completion and scientific_review false remain controlling; no later target
  was assessed.
tags:
- record-review
- bioflocculation
- abstract-assessed
- partial-source-access
- batch-10
```
