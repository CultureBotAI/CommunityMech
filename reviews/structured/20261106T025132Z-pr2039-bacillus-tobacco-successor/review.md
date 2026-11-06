# Bacillus G12-Y4-X25 tobacco SynCom: current-main partial successor

- Review: 20261106T025132Z-pr2039-bacillus-tobacco-successor
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-11-06T02:41:16.309998Z
- Finished UTC: 2026-11-06T02:51:32.665033Z
- Reviewer: codex (unknown)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Current main removes two external tobacco target_taxon blocks while preserving host descriptions. Fresh main text and all 11 main figures verify all 18 snippets but expose a P2 field-yield comparator overstatement. Both original P3 findings remain open: local role evidence and cultivation context. A new P3 finding identifies incorrect October 21 history. Supplementary pixels remain unavailable, so completion is partial. Eight focused checks pass; corpus network commands retain 44 warnings across 16 of 503 records, with no target issues.

## Scope And Provenance

Entire current three-strain target, all five community-level nodes and no arrows, 18 evidence occurrences, three history sidecars, complete primary main HTML and main Figures 1–11. Supplementary captions S1–S5 were read, but the DOCX download returned HTML and its figure pixels were not inspected. No raw sequence or statistical reanalysis.

Selection: Refresh only stale CommunityMech:000373 in PR 2039. The parsed delta has five changed leaves: two tobacco target_taxon blocks removed, two descriptions given explicit tobacco names, and one embedded curation entry added. Every original finding was reassessed and retains its stable key and exact predecessor.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base d0e2089599f282254bae8a4c8c4c3be342c633be.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000373 | kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml | maintained | Bacillus G12-Y4-X25 Tobacco Biocontrol SynCom |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000373 | Target schema validation passed. |
| validate-strict | passed | True | CommunityMech:000373 | Target strict validation passed. |
| validate-terms | passed | True | CommunityMech:000373 | Target term validation passed. |
| validate-gtdb | passed | True | CommunityMech:000373 | Target GTDB syntax/status validation passed. |
| validate-gtdb-domain | passed | True | CommunityMech:000373 | Target GTDB domain validation passed. |
| validate-history | passed | True | CommunityMech:000373 | Target history validation passed. |
| normalize-cache-names-check | passed | True | CommunityMech:000373 | Read-only corpus cache-filename preflight passed. |
| validate-references-explained | passed | True | CommunityMech:000373 | Target reference validation passed against the pinned selected-passage cache. |
| audit-network | failed | True | CommunityMech:000373 | Fresh corpus check retains exit 1: 44 warnings across 16 of 503 records, with zero target-specific issues. |
| check-network-quality | failed | True | CommunityMech:000373 | Fresh corpus check retains exit 1: 44 warnings across 16 of 503 records, with zero target-specific issues. |
| Publication identity and accessible-source comparison | passed | True | CommunityMech:000373 | Fresh metadata, complete primary main HTML and all 18 snippets independently verify; all 11 main figures were visually reviewed. |
| Remaining supplementary figure assessment | unavailable | True | CommunityMech:000373 | Complete main Methods, Results, Discussion and Figures 1–11 are now inspected. Supplementary S1–S5 captions are accessible, but the DOCX route returns HTML and its figure pixels remain unavailable. |
| Encoded dataset accession and release boundary | not_applicable | False | CommunityMech:000373 | No accession is encoded; the public statement reports temporary sequencing restrictions and future deposition. |
| Encoded medium and ingredient-Mech links | not_applicable | False | CommunityMech:000373 | No CultureMech or MediaIngredientMech ID is encoded or uniquely inferred from the LB name. |
| Optional structured source adapter | unavailable | False | CommunityMech:000373 | Optional runner unavailable; fresh public catalog provides a bounded fallback without exact target dataset or strain-module coverage. |

## Scientific And Domain Assessments

### Three-strain inoculant and plant-pathogen assay scope

identity: supported. Targets: CommunityMech:000373.

The source resolves G12/Y4/X25 and separates inoculum composition, host/pathogen targets and experimental endpoints.

### All three member roles, source strains and prominence

grounding: concern. Targets: CommunityMech:000373.

Identities, habitats and antagonist roles are supported, but nearest taxonomy snippets establish only identity/source.

Attach the explicit pathogen-specific antagonism evidence locally. DOMINANT may describe co-equal formulation members; it is not a percentage defect and does not certify abundance or persistence in field soil.

### ecological_interactions[0]: Mild-Inhibition Three-Strain SynCom Compatibility

graph: supported. Targets: CommunityMech:000373.

Reciprocal directional inhibition supports the existing COMPETITION label at plate-assay scope.

Participants are G12, Y4 and X25, with each pair tested in both directions. Fresh Methods 2.2, Results 3.1 and Figure 1 corroborate mild reciprocal plate inhibition. This supports COMPETITION at assay scope, not resource depletion, reciprocal benefit or durable coexistence; supplementary plate photographs S1 remain uninspected.

### ecological_interactions[1]: SynCom Indole-3-Acetic Acid Enhancement

graph: supported. Targets: CommunityMech:000373.

The node preserves a per-volume colorimetric increase without claiming exchange or IAA-mediated plant protection.

Direction is three-strain co-culture versus constituent monocultures to measured supernatant output. The separate 25 C/48 h co-cultivation growth measurement is not assumed to define the IAA assay conditions. GO IAA biosynthesis and CHEBI identity are compatible subject annotations; no member-resolved flux or selective mediation is certified.

### ecological_interactions[2]: Tobacco FO/PN Glasshouse Disease Suppression

graph: supported. Targets: CommunityMech:000373.

Disease-index suppression is corroborated; the record does not convert it into a specific hormonal pathway.

The G12/Y4/X25 inoculant treats He Luo No. 1 tobacco challenged with F. oxysporum and P. nicotianae, under preventive and curative timing. Source defense-enzyme responses support broad protective-response context but do not distinguish every direct/host-mediated contribution.

### ecological_interactions[3]: Tobacco Root Activity Improvement

graph: supported. Targets: CommunityMech:000373.

The TTC-based endpoint is correctly limited to root metabolic activity.

Direction is SynCom treatment under FO/PN stress to tobacco root TTC activity versus single-strain treatments. Tobacco is now explicitly named in the description and absent from target_taxon. This preserves external host scope without treating it as a missing microbial member or turning TTC activity into biomass growth.

### ecological_interactions[4]: Two-Site Field Disease Suppression and Yield Increase

graph: concern. Targets: CommunityMech:000373.

Natural-disease and estimated-yield outcomes are supported, but the combined sentence overextends demonstrated yield comparators.

Results 3.6 gives numeric yield increases versus the control, and Figure 9D has no commercial-product yield arm. Figure 9E supports superior disease efficacy versus B. subtilis. Although the Discussion asserts broader yield superiority, the record should separate these endpoint/comparator scopes or explicitly attribute that unresolved assertion. Not every single-strain yield comparison is significant. Neither whole-plot harvested yield nor durable microbiome change is established.

### downstream inventory

graph: not_applicable. Targets: CommunityMech:000373.

No downstream arrows are encoded, so no additional mechanistic direction is certified.

### LB, glasshouse and field context

completeness: concern. Targets: CommunityMech:000373.

The correctly scoped 30 C preparation block omits separate co-cultivation growth, glasshouse and field conditions now independently verified in complete Methods.

Keep preparation, 25 C/48 h co-cultivation measurement, 21-day controlled plant experiment and repeated field root irrigation separate. The environmental factor duplicates assembly strategy. The source does not provide a unique LB formulation; supplement unavailability no longer prevents checking these main-text conditions.

### IAA output and biological scope

grounding: supported. Targets: CommunityMech:000373.

The IAA entry is a measured potential growth-promoting output rather than a verified mediator of disease protection.

No metal-processing phenotype or specific additional metabolite is established by the accessible evidence. Names alone do not justify additional pathways or genes.

### Source/cache/history and resource boundaries

evidence: concern. Targets: CommunityMech:000373.

Fresh complete main HTML supports every snippet, but the October 21 history narrative misidentifies the record and edit.

The committed cache is still selected text and is not overwritten. An append-only correction must reconcile the incorrect 000449/Ralstonia/counter_selection narrative with the actual 000373 tobacco-target cleanup. Closed issue 2049 also has unrelated record/source identities; its closure is not evidence of scientific correctness. Current public data restrictions remain explicit, with no invented study accession.

### Native checks and remaining supplementary scope

schema: concern. Targets: CommunityMech:000373.

Eight focused/native checks pass; all 10 current term pairs and all 18 snippets verify. The target audit is clean. The corpus commands retain their 44-warning exits, and unavailable supplementary pixels keep completion partial.

### Native completeness and quality within partial supplementary coverage

completeness: supported. Targets: CommunityMech:000373.

Completeness is 85 and capped validation quality is 100; source scope and open findings remain explicit.

### Current-main host cleanup and grouped-review boundary

provenance: supported. Targets: CommunityMech:000373.

Fresh inspection replaces the stale input and confirms only the bounded 000373 host-target cleanup.

Nodes 3 and 4 retain tobacco host context and source-backed outcomes without host membership. The Stage 5 grouped resolved finding is context; no same-key supersession or disposition is emitted for its other targets. Incorrect history/issue identities remain a separate provenance concern. Both original single-record findings remain open.

## Findings

### role-evidence-placement: Taxonomy role claims lack their narrow source evidence

minor / open / confirmed; issue key: cm-000373-role-evidence-placement.

Each PATHOGEN_ANTAGONIST entry cites taxonomic identity and isolation habitat, although the fresh abstract separately provides the relevant pathogen-specific prior-study attribution.

### cultivation-context: Preparation and outcome-assay contexts are incompletely represented

minor / open / confirmed; issue key: cm-000373-cultivation-context.

The LB block captures 30 C preparation but omits the separate 25 C/48 h co-cultivation growth assay and controlled glasshouse/field settings. Fresh complete Methods independently verify these contexts; environmental_factors[0] repeats assembly design.

### history-edit-misattribution: October 21 history misidentifies the record and the actual host-target edit

minor / open / confirmed; issue key: cm-000373-history-2049-edit-misattribution.

The 2026-10-21T190000Z-claude-2049 sidecar names CommunityMech:000449 and claims added Ralstonia/Phytophthora counter_selection entries. Current 000373 instead removes tobacco target_taxon from nodes 3 and 4 and retains host text. Issue 2049's body separately assigns 000373 to an unrelated Ralstonia-phage/Pseudomonas record and PMID. Neither historical narrative is reliable proof of this change.

### field-yield-comparator: Separate field disease-control and estimated-yield comparator scopes

major / open / confirmed; issue key: cm-000373-field-yield-comparator.

Node 4 says estimated yield increased relative to both single-strain and commercial microbial treatments. Figure 9D presents only G12/Y4/X25/SC/LB yield arms, while Figure 9E supports the commercial B. subtilis disease-efficacy comparison. Results 3.6 assigns the 41.33% and 37.54% dry-yield increases to the control. The Discussion does assert broader commercial-product yield superiority, but the presented yield evidence does not establish it; SC versus X25 fresh-yield comparisons are also nonsignificant. The record should preserve demonstrated comparators or explicitly qualify the broader author assertion.

## Recommended Actions And Acceptance Checks

### fix-role-evidence-placement

Attach source-attributed antagonism evidence to each corresponding taxon role.

- Keep G12 linked to F. oxysporum and Y4/X25 to P. nicotianae, preserving attribution to the prior studies summarized by this article.
- Retain current species/strain/habitat evidence; do not generalize every strain to every pathogen or invent direct mechanisms.
- If original prior-study protocols are later cited, inspect them before adding stronger strain-specific claims.
- Run references, schema and strict validation after separately authorized curation.

### fix-cultivation-context

Use freshly verified complete Methods to represent the distinct cultivation and plant-assay settings without conflating preparation and outcome protocols.

- Preserve the correctly scoped 30 C preparation block; the main-text numerical contexts have now been independently verified.
- Keep 30 C/180 rpm inoculum preparation separate from 25 C/180 rpm/48 h co-cultivation measurement.
- Represent glasshouse 25 +/- 2 C, 12 h:12 h light/dark, 70-80% RH and 21-day experiments separately from field cultivation.
- Preserve field 10 mL per-plant root irrigation and two events seven days apart without extrapolating glasshouse conditions to field sites.
- Move duplicated assembly prose to engineering_design and use environmental fields for actual setting conditions.
- Do not fabricate LB formulation, exact CultureMech ID, assay inoculum details or unavailable field protocol information.
- Attach exact main-article Methods evidence at each added context and run strict, term, reference and history checks plus regenerated-document checks after separately authorized curation.

### complete-source-assessment

Complete the remaining supplementary S1–S5 figure assessment when publicly accessible, then save a new immutable review; full main Methods, Results and Figures 1–11 are already assessed here.

- Inspect the actual supplementary plate photographs, disease/field images and pathway figure; captions alone are not the images. Retain this successor's bounded main-text and numeric verification.
- Do not convert transcriptomic associations, nonsignificant genus shifts or IAA output into hormone mediation or persistent colonization.
- Revisit sequencing-data release only when the source provides a real deposited accession.
- No purchase, author contact, canonical edit or status promotion is authorized by this review.

### append-history-correction

In separately authorized provenance curation, append a correction identifying the erroneous sidecar and actual 000373 edit; record the linked issue-body mismatch without rewriting old history.

- Name the exact October 21 sidecar and its incorrect 000449/Ralstonia/counter_selection claims; establish 000373 identity using target content and PMID 42388034.
- Document removal of tobacco target_taxon from nodes 3 and 4 plus retained host descriptions; do not fabricate absent counter_selection or pathogen changes.
- Preserve all original history bytes and verify the new corrective history with native validation.
- Link a correction to the erroneous issue-body identity without treating issue closure as scientific evidence or changing grouped findings for unrelated targets.

### bound-field-yield-comparators

Separate field disease-control comparators from middle-leaf estimated-yield comparisons in the node and its evidence explanation.

- Preserve two-site natural-disease scope and commercial-product disease-efficacy comparison supported by Figure 9E.
- State 41.33% and 37.54% dry-yield increases against the source control, preserving middle-leaf estimation and Figure 9D treatment arms.
- Do not assert significant superiority over every single-strain yield arm. Distinguish any broader Discussion assertion from demonstrated commercial-product yield data unless additional directly supporting primary evidence is verified.
- Attach endpoint-specific evidence, append history, and run reference, strict and generated-document checks after separately authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml; Entire current record: three members, five nodes, no arrows and 18 snippets | supports | The record separates microbial inoculant members from tobacco host/pathogens, source habitats and measured endpoints. |
| cache | PMID:42388034; references_cache/PMID_42388034.txt: complete cache, selected Methods/Results/Discussion | supports | The committed cache remains selected primary passages, not the complete article. All 18 snippets match both this cache and the independently retrieved complete PMC main HTML. |
| pubmed | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=42388034&amp;retmode=xml; https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=42388034&amp;retmode=xml | supports | Fresh article-level PubMed metadata verifies PMID 42388034, DOI 10.1002/ps.71069, PMC13569317 and the full abstract. |
| crossref | https://api.crossref.org/works/10.1002/ps.71069; https://api.crossref.org/works/10.1002/ps.71069 | supports | Fresh Crossref metadata verifies DOI/title and journal full-XML/PDF routes. |
| epmc | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:42388034&amp;format=json&amp;resultType=core; https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:42388034&amp;format=json&amp;resultType=core | supports | Fresh Europe PMC metadata links PMID 42388034, DOI 10.1002/ps.71069 and PMC13569317. Its XML route did not yield the body; the separately retrieved public PMC HTML did. |
| access | Public EPMC, PMC, BioC and Wiley routes; .temp/pr2039/373/sources.json and media-sources.json with per-request receipts | context_only | Fresh EPMC XML and publisher requests returned curl exit 56. PubMed, Crossref, EPMC metadata, PMC efetch, PMC HTML, BioC and catalog requests returned exit 0. Successful transport alone is not source sufficiency: the complete main HTML and 11 figure images were inspected, whereas the supplement response is a Preparing to download HTML page, not DOCX. No bypass or paid retrieval was used. |
| root-access | https://pmc.ncbi.nlm.nih.gov/articles/PMC13569317/; Fresh author retrieval: complete Methods 2.1–2.8, Results 3.1–3.7, Discussion, main Figures 1–11 and supplementary captions S1–S5 | context_only | The original main-text access limitation is overcome. Supplementary captions are available in HTML; their DOCX and underlying supplementary pixels remain unverified. The author's own retrieval and source assessment are used here, not another agent's approval. |
| members | PMID:42388034; Abstract and Methods 2.1 | supports | G12 is the rhizosphere B. amyloliquefaciens isolate; Y4 and X25 are tobacco endophytes assigned to B. pumilus and B. velezensis. The source attributes prior F. oxysporum antagonism to G12 and P. nicotianae inhibition to Y4/X25. Identity/habitat snippets alone do not directly support the local role annotations. |
| compatibility | PMID:42388034; Methods 2.2; Results 3.1; Figure 1 A–C; supplementary S1 caption | supports | All six directional plate-inhibition values are below 25%. Figure 1 confirms mild inhibition and aggregate co-culture growth without resolving each strain's survival or persistent coexistence. The record does not claim a specific resource-depletion mechanism. |
| iaa | PMID:42388034; Methods 2.2; Results 3.1; Figure 1 D–E; Discussion | supports | Per-volume Salkowski colorimetry reports 11.57 +/- 0.24 mg/L in the SynCom, above each monoculture. This supports the qualified IAA-output node; it does not establish member-resolved exchange or IAA-mediated plant protection. The separate co-cultivation growth protocol is not automatically an IAA incubation protocol. |
| glasshouse | PMID:42388034; Methods 2.4; Results 3.3; Figures 3–5; supplementary S2–S3 captions | supports | He Luo No. 1 tobacco receives preventive or curative treatment around a combined FO/PN challenge. Figure 4 shows disease indices 54.07 for pathogen control, 9.26 for preventive SynCom and 26.67 for curative SynCom. The record's preventive reduction and separate curative benefit are supported without assigning a specific hormonal mechanism. |
| root-activity | PMID:42388034; Methods 2.5; Results 3.4; Figure 6 | supports | The TTC/dehydrogenase assay and Figure 6 support higher root metabolic activity, with the text reporting 20.27–45.38% above preventive single-strain treatments. This is not direct biomass production or reciprocal microbial fitness. Root morphometry is a distinct endpoint. |
| field | PMID:42388034; Methods 2.7–2.8; Results 3.6–3.7; Figures 9–11; Discussion | supports | The two yellow-soil sites show natural-disease control and middle-leaf-based estimated yield. Results 3.6 gives yield increases against the control. Figure 9D shows only G12/Y4/X25/SC/LB yield arms, with SC versus X25 fresh-yield comparisons nonsignificant; commercial B. subtilis appears in disease-efficacy panel E. The Discussion makes a broader commercial-product yield claim, but the displayed yield evidence does not establish that comparator. Figure 11 genus shifts are nonsignificant and do not establish strain persistence. |
| cultivation | PMID:42388034; Methods 2.1, 2.2, 2.4 and 2.7 | supports | Fresh complete Methods verify 30 C/180 rpm preparation, distinct 25 C/180 rpm/48 h co-cultivation growth measurement, glasshouse 25 +/- 2 C with 12 h:12 h light/dark and 70–80% RH for 21 days, and 10 mL per-plant field irrigation twice seven days apart. These contexts must remain separate; a precise LB recipe is not specified. |
| limits | PMID:42388034; Methods 2.6, 2.8; Results 3.5, 3.7; Figures 7–8, 10–11; Discussion | supports | Pooled root/stem/leaf transcriptomic and co-expression associations do not prove tissue-specific hormonal mechanisms. A single-site endpoint and nonsignificant genus changes do not establish inoculant persistence, niche differentiation or resilience. Figure 10(F) depicts lower bacterial richness in SC than LB despite prose saying higher; no directional richness claim is adopted and the target encodes none. |
| ontology | Local OAK NCBITaxon, ENVO, CHEBI and GO snapshots; Ten unique current NCBITaxon, ENVO, CHEBI and GO pairs | supports | All 10 canonical labels match local OAK authority values. Species terms preserve isolate context; broad defense/growth terms are bounded to observed plant endpoints. The removed tobacco target objects are not current ontology placements. |
| schema | src/communitymech/schema/communitymech.yaml; InteractionTypeEnum.COMPETITION; FunctionalRoleEnum.PATHOGEN_ANTAGONIST; AbundanceEnum.DOMINANT; taxonomy host exclusion | supports | COMPETITION permits reciprocal negative effects without requiring resource depletion. DOMINANT is ordinal prominence of the co-equal formulation members, not a measured field population fraction. Tobacco remains external host context in descriptions; it is not a microbial member. |
| snippets | kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml; primary-html-replay.json and snippet-replay.json: all 18 evidence occurrences | supports | All 18 snippets match the fresh main HTML and the selected committed cache after NFKC and whitespace normalization. None is an exact match to the differently worded fresh PubMed abstract; main-text matching now independently verifies the lexical spans. |
| datasets | PMID:42388034; Fresh PMC main article Data Availability Statement and Methods 2.6/2.8 | supports | The current public article still states temporary sequencing-release restrictions and future deposition without a study accession. GCF_000715135.1 is a tobacco reference genome, not this study's deposited reads. No arbitrary accession or dataset-omission defect is inferred; no author contact or raw-data analysis was performed. |
| history | history/records/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom/2026-10-21T190000Z-claude-2049.yaml; All three sidecars; exact 000373 row in 20261005-eleven-records-batch5.yaml; fresh issues 1248, 880 and 2049 | supports | The historical graph decision's record hash matches the original review input and its non-graph exclusion remains explicit. Issues 1248 and 880 are CLOSED. The new October 21 sidecar is schema-valid but falsely describes 000449 and counter_selection/Ralstonia changes. The actual delta is tobacco-target removal. Closed issue 2049 also misidentifies the 000373 record/source and is context only, not scientific proof. |
| search | Owned community/isolate/reusable-taxon roots; Fresh rg --no-ignore --hidden exact record ID, PMID, G12, Y4 and X25 query | supports | The ignored-inclusive bounded search located this target's cache, three history sidecars and graph decision material. It produced no exact isolate-authenticating kb/taxa hit; shared Bacillus species do not establish equivalent isolates. The query also contains an irrelevant prior-target alternative, which does not narrow its exact current-target alternatives. |
| adapter | Optional kg-microbe-sources and public iModulonDB catalog; adapter-discovery.json and fresh imodulon-catalog.json | supports | No runner was found in PATH or either exact probed sibling checkout. The inspected public catalog includes B. subtilis but no exact G12/Y4/X25 target dataset; a different Bacillus species is not a substitute. No expression-module query was performed. |
| native-target | NetworkIntegrityAuditor().audit_community(target); Fresh NetworkIntegrityAuditor().audit_community(current target) | supports | The target audit returned an empty issue list after host-target removal. All five nodes use COMMUNITY_LEVEL scope for the three-member SynCom and contain one evidence item each; no explicit participating_taxa lists or downstream edges are encoded. Native structural completeness does not prove missing scientific mechanisms. |
| current-delta | kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml; semantic-diff.json; original frozen input versus current merged-main target | supports | Exactly five semantic leaves changed: curation_history[2] added, tobacco target_taxon removed from nodes 3 and 4, and explicit tobacco names added to those descriptions. The source scopes and two original finding surfaces remain unchanged. |
| host-lineage | reviews/structured/20261021T193000Z-stage5-remediation-verification/review.yaml; stage4-external-host-pathogen-targets and exact Stage 4 predecessor rows; lineage.json | context_only | The later grouped finding explicitly resolves the host-target outcome for 000347/000364/000373. This successor independently confirms only the 000373 tobacco-target cleanup. It neither reassesses the other targets nor supersedes the grouped disposition; the contradictory issue/history identity text is separately flagged. |
| check-validate | just --no-dotenv validate kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml; .temp/pr2039/373/validate.json; 2026-11-06T02:41:22.125920Z to 2026-11-06T02:41:22.630243Z | supports | Target schema validation passed. |
| check-validate-strict | just --no-dotenv validate-strict kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml --out /Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2039-batch05/.temp/pr2039/373/strict.tsv; .temp/pr2039/373/validate-strict.json; 2026-11-06T02:41:22.630432Z to 2026-11-06T02:41:24.531554Z | supports | Target strict validation passed. |
| check-validate-terms | just --no-dotenv validate-terms kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml; .temp/pr2039/373/validate-terms.json; 2026-11-06T02:41:24.531725Z to 2026-11-06T02:41:25.574661Z | supports | Target term validation passed. |
| check-validate-gtdb | just --no-dotenv validate-gtdb kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml; .temp/pr2039/373/validate-gtdb.json; 2026-11-06T02:41:25.574843Z to 2026-11-06T02:41:25.634574Z | supports | Target GTDB syntax/status validation passed. |
| check-validate-gtdb-domain | just --no-dotenv validate-gtdb-domain kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml; .temp/pr2039/373/validate-gtdb-domain.json; 2026-11-06T02:41:25.634749Z to 2026-11-06T02:41:26.571279Z | supports | Target GTDB domain validation passed. |
| check-validate-history | just --no-dotenv validate-history history/records/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom; .temp/pr2039/373/validate-history.json; 2026-11-06T02:41:26.571459Z to 2026-11-06T02:41:27.106257Z | supports | Target history validation passed. |
| check-normalize-cache-names-check | uv run python scripts/normalize_cache_names.py --check; .temp/pr2039/373/normalize-cache-names-check.json; 2026-11-06T02:41:27.106454Z to 2026-11-06T02:41:27.145533Z | supports | Read-only corpus cache-filename preflight passed. |
| check-validate-references-explained | just --no-dotenv validate-references-explained kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml; .temp/pr2039/373/validate-references-explained.json; 2026-11-06T02:41:27.145737Z to 2026-11-06T02:41:27.915383Z | supports | Target reference validation passed against the pinned selected-passage cache. |
| check-audit-network | just --no-dotenv audit-network; .temp/pr2039/373/audit-network.json; 2026-11-06T02:41:27.915565Z to 2026-11-06T02:41:32.146475Z | supports | Fresh corpus check retains exit 1: 44 warnings across 16 of 503 records, with zero target-specific issues. |
| check-check-network-quality | just --no-dotenv check-network-quality; .temp/pr2039/373/check-network-quality.json; 2026-11-06T02:41:32.146648Z to 2026-11-06T02:41:36.334206Z | supports | Fresh corpus check retains exit 1: 44 warnings across 16 of 503 records, with zero target-specific issues. |

## Limits And Additional Notes

- Supplementary S1–S5 captions are inspected, but the DOCX download returned an HTML preparation/verification page; supplementary images remain unavailable. Main article and all 11 main figures were retrieved and assessed. No access-control bypass or paid retrieval was used.
- The selected committed cache remains incomplete despite its full-text separator. All 18 current snippets now independently match the complete primary HTML; no cache content was changed.
- No raw RNA-seq, amplicon data, figure digitization or statistical reanalysis was performed. Sequencing release restrictions and future deposition remain in the current article; the tobacco reference genome is not a study accession.
- Equal formulation membership is not persistent field dominance. Salkowski output, pooled-tissue expression associations and nonsignificant genus shifts do not establish metabolite mediation, member fitness, persistence or resilience. The existing colonization/mechanism discussion remains an evidence boundary, not a request to conduct experiments.
- The source's Figure 10(F) richness direction conflicts with its prose. This refresh does not adopt a directional richness claim, and none is encoded in the target; no correction to source raw data is inferred.
- Historical GTDB mapping counts/release were not recomputed. Optional adapter discovery is bounded to PATH and two exact sibling locations; the public catalog has no exact target dataset and no strain-module query was performed.
- The corpus network commands retain 44 warnings across 16 of 503 records, recorded as failed checks. The current target has no native network issues; grouped dispositions for other records were not reassessed.
- This is an author refresh, not independent approval. No canonical record, cache, history, schema or generated product was edited.
- Both original P3 issue keys and exact previous_occurrences remain open; the new history concern requires append-only follow-up outside this review-bundle PR.
- Direct excerpts retained from the original review total 15 words. Source snapshots and actual command receipts are pinned, and the initial repository input hashes were rechecked before final inspection.
- The original complete-source-assessment action is narrowed to still-uninspected supplementary material. The bounded host-target repair does not supersede the three-target Stage 4/5 finding lineage.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261106T025132Z-pr2039-bacillus-tobacco-successor
kind: record
repository: CultureBotAI/CommunityMech
title: 'Bacillus G12-Y4-X25 tobacco SynCom: current-main partial successor'
started_at: '2026-11-06T02:41:16.309998Z'
finished_at: '2026-11-06T02:51:32.665033Z'
reviewer:
  identity: codex
  kind: agent
  independence: unknown
  independence_basis: Author refresh of a stale PR 2039 review; prior Codex record
    creation and graph curation exist. This pass does not claim independent adversarial
    approval.
skill: review-yaml-record
completion: partial
verdict: needs_curation
scientific_review: false
summary: 'Current main removes two external tobacco target_taxon blocks while preserving
  host descriptions. Fresh main text and all 11 main figures verify all 18 snippets
  but expose a P2 field-yield comparator overstatement. Both original P3 findings
  remain open: local role evidence and cultivation context. A new P3 finding identifies
  incorrect October 21 history. Supplementary pixels remain unavailable, so completion
  is partial. Eight focused checks pass; corpus network commands retain 44 warnings
  across 16 of 503 records, with no target issues.'
source:
  git_revision: d0e2089599f282254bae8a4c8c4c3be342c633be
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
  - path: .temp/pr2039/373/adapter-discovery.json
    sha256: 0ea2a569e36cbd47d8101eb92f6efa24d72a7fba5f4daad45f6b9277fd6add98
    role: context
  - path: .temp/pr2039/373/audit-network.json
    sha256: d4b57de354bca760a5a6ece012be1226f85a431b66250c0efa35b3b90436015b
    role: context
  - path: .temp/pr2039/373/audit-network.stderr.txt
    sha256: a71fb29e950f3eaf0eb2b834a43c59d4a1b6aa85a2a89473ae99b0e408a27a36
    role: context
  - path: .temp/pr2039/373/audit-network.stdout.txt
    sha256: f5dc190f832300fc5a73fcf3e7e8e3cd53d560ba09b17179ce6c7fcc8aa022e8
    role: context
  - path: .temp/pr2039/373/bioc.json
    sha256: 478f38e0765ee9c406831bb2fc27e8019ac5227c20c6b28ca0de582d8449354a
    role: context
  - path: .temp/pr2039/373/check-network-quality.json
    sha256: 96fcfd01e0b767ca98c053f9b005609c85fb2117fa9c2830dba7ef6e4b4af9a6
    role: context
  - path: .temp/pr2039/373/check-network-quality.stderr.txt
    sha256: f9a8e9fb5a4e4ea545236a809393dbc1ce4325b14579c65a3130bcfe713e798a
    role: context
  - path: .temp/pr2039/373/check-network-quality.stdout.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2039/373/crossref.json
    sha256: d0f11341318b3382380050ecc03f8599dd17dc1f7ce2edf02fccf41ecd102810
    role: context
  - path: .temp/pr2039/373/epmc.json
    sha256: 1425929b2c90b3decc0e30e22cf3cd932bc71b74129a46aa93a636071cee8f72
    role: context
  - path: .temp/pr2039/373/fetch-bioc.json.json
    sha256: c61366630a033af5026e580a1b1d16404f75ac68d1ac47a94e2783cc47398b21
    role: context
  - path: .temp/pr2039/373/fetch-bioc.json.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2039/373/fetch-bioc.json.stdout.txt
    sha256: 478f38e0765ee9c406831bb2fc27e8019ac5227c20c6b28ca0de582d8449354a
    role: context
  - path: .temp/pr2039/373/fetch-crossref.json.json
    sha256: 848de6dba2967550a8052d31940f24749419acb0017a66342471c8c37452c217
    role: context
  - path: .temp/pr2039/373/fetch-crossref.json.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2039/373/fetch-crossref.json.stdout.txt
    sha256: d0f11341318b3382380050ecc03f8599dd17dc1f7ce2edf02fccf41ecd102810
    role: context
  - path: .temp/pr2039/373/fetch-epmc.json.json
    sha256: 7b7a5fd2daccf15abc889b132c8982b8e47366c4a7f9e6957f78632e05f489f1
    role: context
  - path: .temp/pr2039/373/fetch-epmc.json.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2039/373/fetch-epmc.json.stdout.txt
    sha256: 1425929b2c90b3decc0e30e22cf3cd932bc71b74129a46aa93a636071cee8f72
    role: context
  - path: .temp/pr2039/373/fetch-imodulon-catalog.json.json
    sha256: 03c5b33a44e4084bbf0ced761cf823e2dc035bf9e9116e13573a346866105a46
    role: context
  - path: .temp/pr2039/373/fetch-imodulon-catalog.json.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2039/373/fetch-imodulon-catalog.json.stdout.txt
    sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
    role: context
  - path: .temp/pr2039/373/fetch-issue-1248.json
    sha256: c35a43724f112922ff269820cc45b053aab04c45772a87ba10ef8272a0cda555
    role: context
  - path: .temp/pr2039/373/fetch-issue-1248.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2039/373/fetch-issue-1248.stdout.txt
    sha256: 784dbe48ab77cc402187ebb8dfea56d6026b8e61b533d6b0f89d3cf68fdff943
    role: context
  - path: .temp/pr2039/373/fetch-issue-2049.json
    sha256: 7a49f96c4d454e7d7c0a8dfbc5d8b9c9e4693c31bbb1503f78f3fc132eb08c4c
    role: context
  - path: .temp/pr2039/373/fetch-issue-2049.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2039/373/fetch-issue-2049.stdout.txt
    sha256: 8cc229bcf5f4f701365f7980271df3dc171ee0a131e5615d42bbef6b309e2338
    role: context
  - path: .temp/pr2039/373/fetch-issue-880.json
    sha256: f438234b361ea80fea456998d571d1af9a9b60586342b9374a2841efc4d2dd6d
    role: context
  - path: .temp/pr2039/373/fetch-issue-880.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2039/373/fetch-issue-880.stdout.txt
    sha256: 8ce7369cb88f8f898473fe530cdc48b3b61c7abf2267ee2344af265e7673a886
    role: context
  - path: .temp/pr2039/373/fetch-pmc-efetch.xml.json
    sha256: 1666bd05e0942b2b65681a23208057befc32eb2802673c1e887207b47749d85e
    role: context
  - path: .temp/pr2039/373/fetch-pmc-efetch.xml.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2039/373/fetch-pmc-efetch.xml.stdout.txt
    sha256: 3bcf1d05787af2f2ba0362d0517e3e2833ad6a77b6c0e568e157652c9cc3ad53
    role: context
  - path: .temp/pr2039/373/fetch-pmc.html.json
    sha256: 1acf76c9b40e3605da60fee682acf26ecd8bd7da0ea42b71df3ed351a27c5978
    role: context
  - path: .temp/pr2039/373/fetch-pmc.html.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2039/373/fetch-pmc.html.stdout.txt
    sha256: c807670a53d46d99811a666598e5203bb18acdabb608732d8becd4442342fa00
    role: context
  - path: .temp/pr2039/373/fetch-primary.xml.json
    sha256: 5e022b6cb0214f374f21b29fc8ebedc58b9cfccdf46f7d7fe5cf08f893869407
    role: context
  - path: .temp/pr2039/373/fetch-primary.xml.stderr.txt
    sha256: b781edb7b5d6b3d44080407ce23b2f74dc1fefd0172aa8bcec7f72b4a513a6e5
    role: context
  - path: .temp/pr2039/373/fetch-primary.xml.stdout.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2039/373/fetch-ps71069-fig-0001.webp.json
    sha256: abc7eed2b6be0016cc128bc3f46c89098c117901acab567b74d679524a8a1176
    role: context
  - path: .temp/pr2039/373/fetch-ps71069-fig-0001.webp.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2039/373/fetch-ps71069-fig-0001.webp.stdout.txt
    sha256: ade140610378545538f8c644a10b3092212a72ea2e4f84541b1f7273c3d70471
    role: context
  - path: .temp/pr2039/373/fetch-ps71069-fig-0002.webp.json
    sha256: 929a9463e85b216339b27228d31d97978fcbec208193bcd301a75e1e939a0efb
    role: context
  - path: .temp/pr2039/373/fetch-ps71069-fig-0002.webp.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2039/373/fetch-ps71069-fig-0002.webp.stdout.txt
    sha256: 082d51f44787e6f52d5426312d77b7f97709f467522c2fc882b29451431e2485
    role: context
  - path: .temp/pr2039/373/fetch-ps71069-fig-0003.webp.json
    sha256: 788f3b4bd0670e96e736422df30bdb74210fefd044ccf95c4198ff5ddc283a3f
    role: context
  - path: .temp/pr2039/373/fetch-ps71069-fig-0003.webp.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2039/373/fetch-ps71069-fig-0003.webp.stdout.txt
    sha256: 55bc49186a66b470af7008f9660a37b544b529558798ede6778b6a4cf1adbf8d
    role: context
  - path: .temp/pr2039/373/fetch-ps71069-fig-0004.webp.json
    sha256: ae017df506970cdfdce4820a1182c647d04b49406e60516c2345f285f627fffa
    role: context
  - path: .temp/pr2039/373/fetch-ps71069-fig-0004.webp.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2039/373/fetch-ps71069-fig-0004.webp.stdout.txt
    sha256: 4b2dcdb4dd507a89471a1330329ee60df8595f005fdaf9845db9523a247b3aa1
    role: context
  - path: .temp/pr2039/373/fetch-ps71069-fig-0005.webp.json
    sha256: 2c02200c509b6b621955cb9c9e4ecee137962740cd27bc3aa54cb59b10c7e846
    role: context
  - path: .temp/pr2039/373/fetch-ps71069-fig-0005.webp.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2039/373/fetch-ps71069-fig-0005.webp.stdout.txt
    sha256: de497cdc23619dcf68dc6b826e30f7f1213caba96c7c0418dd9954b4e17143b8
    role: context
  - path: .temp/pr2039/373/fetch-ps71069-fig-0006.webp.json
    sha256: 67754b0ce3c74ef0998c1f3e085163d0f5ddc1724221fc4b1b89aeb3cdae7cf3
    role: context
  - path: .temp/pr2039/373/fetch-ps71069-fig-0006.webp.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2039/373/fetch-ps71069-fig-0006.webp.stdout.txt
    sha256: c3d68e059552ae94ff33161078c04deddfb3216505f944cfec1f8bdab4925184
    role: context
  - path: .temp/pr2039/373/fetch-ps71069-fig-0007.webp.json
    sha256: a9f21404477385ee819909203a26af3873425f52f27d09cb17222b28abb22863
    role: context
  - path: .temp/pr2039/373/fetch-ps71069-fig-0007.webp.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2039/373/fetch-ps71069-fig-0007.webp.stdout.txt
    sha256: af57ebb18d962ec3cf97d01acda9c52d099562719cfdcc78a4105088194e7d0f
    role: context
  - path: .temp/pr2039/373/fetch-ps71069-fig-0008.webp.json
    sha256: 565de9e1437c36c2c27cc24414cbf5d560206854b535f5d485365e693386f152
    role: context
  - path: .temp/pr2039/373/fetch-ps71069-fig-0008.webp.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2039/373/fetch-ps71069-fig-0008.webp.stdout.txt
    sha256: 97f2fecf40e216df08bab3714083f1cb312a57161d45cef2ca8ca77da5c81dd0
    role: context
  - path: .temp/pr2039/373/fetch-ps71069-fig-0009.webp.json
    sha256: 46c48a95d4a9606d1e4c00616578675335b8ed722bc6ffb2b2b05d02395368e0
    role: context
  - path: .temp/pr2039/373/fetch-ps71069-fig-0009.webp.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2039/373/fetch-ps71069-fig-0009.webp.stdout.txt
    sha256: 9239db361f01b66ea3d9d40d6ff1926d322de90c5eb6c458e26019fb9f2b18bc
    role: context
  - path: .temp/pr2039/373/fetch-ps71069-fig-0010.webp.json
    sha256: a23abf6a9bda656507e6113d8cdeab947616f608c5e64f990dec64828a51c51c
    role: context
  - path: .temp/pr2039/373/fetch-ps71069-fig-0010.webp.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2039/373/fetch-ps71069-fig-0010.webp.stdout.txt
    sha256: 8a9311442c81fb5aa103c772e05e24542c8fda72638d604b796691993e974ea1
    role: context
  - path: .temp/pr2039/373/fetch-ps71069-fig-0011.webp.json
    sha256: 46e94516cd5dd2b331591517c2eae26a5b7f1b19fa8fd9dc2f88c4eadb4343a5
    role: context
  - path: .temp/pr2039/373/fetch-ps71069-fig-0011.webp.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2039/373/fetch-ps71069-fig-0011.webp.stdout.txt
    sha256: 53a6661f6dae3056d5d4eca181e5f9ddc6b93a5e92f40b1aaec29dbdd9bf40f5
    role: context
  - path: .temp/pr2039/373/fetch-publication.xml.json
    sha256: 89a54868eb489ba6c8fc975b4586321115d860c2e22f3d4b84f7873b58c13167
    role: context
  - path: .temp/pr2039/373/fetch-publication.xml.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2039/373/fetch-publication.xml.stdout.txt
    sha256: 103674cbfe03ac75435744f571fe47bf7eb86395ca6f9dc10afad731a6d1df26
    role: context
  - path: .temp/pr2039/373/fetch-publisher.html.json
    sha256: 4bad98509d927c6852b3dd9fc293f45983893a0f2bbdc60475e80c1e0d9ee180
    role: context
  - path: .temp/pr2039/373/fetch-publisher.html.stderr.txt
    sha256: dd11db406ba29c9af00e1a02accacebcf7c5a2654b4162ef12e709fec8e5688a
    role: context
  - path: .temp/pr2039/373/fetch-publisher.html.stdout.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2039/373/fetch-supplement.json
    sha256: 7cd2eccc73ae148aad420c276907e011f2e4fa538e3edc25f7512770d0dc20b8
    role: context
  - path: .temp/pr2039/373/fetch-supplement.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2039/373/fetch-supplement.stdout.txt
    sha256: 343f71ede97e4e4d91e0e66e3350202939331573a9c550d2099e7bf17bd92428
    role: context
  - path: .temp/pr2039/373/frozen-target.json
    sha256: 39d1e7f56195a10929ea42db1b5197ea7c88fe829f696ac5023e90355494a704
    role: context
  - path: .temp/pr2039/373/frozen-target.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2039/373/frozen-target.stdout.txt
    sha256: e0126b602878c9abada427f906334f6a059784e07b29c33b709c9a9549f0689f
    role: context
  - path: .temp/pr2039/373/imodulon-catalog.json
    sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
    role: context
  - path: .temp/pr2039/373/inspect.json
    sha256: 1855f5b08031eb68ccc41185298247521ee972a91050ee8bb1e363015250c837
    role: context
  - path: .temp/pr2039/373/inspect.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2039/373/inspect.stdout.txt
    sha256: d8f82cd45da1c7e63a7573c56e864b80fca4a06239ae054790a722caa18a204b
    role: context
  - path: .temp/pr2039/373/inspection.json
    sha256: d8f82cd45da1c7e63a7573c56e864b80fca4a06239ae054790a722caa18a204b
    role: context
  - path: .temp/pr2039/373/issue-1248.json
    sha256: 797faf215c151e414f05c6a3a676ec444ef085bab9cb96ec66bee610602851dd
    role: context
  - path: .temp/pr2039/373/issue-2049.json
    sha256: 60f4e77bb49d35ae460f5a6072b690a02195ef460512891370812f204b057edd
    role: context
  - path: .temp/pr2039/373/issue-880.json
    sha256: 1e91159b74bcf612e86637ee14a55852905df1de70b899c8f2f84c97c99ecccb
    role: context
  - path: .temp/pr2039/373/lineage.json
    sha256: 583b24c1ea1c5ac531728352055326202456c1b7992786b8630960e3ee76f678
    role: context
  - path: .temp/pr2039/373/local-search.json
    sha256: bf685b1a693e21182b98988e97dd1db3a906cb8bccb687d4e3feae7a90165729
    role: context
  - path: .temp/pr2039/373/local-search.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2039/373/local-search.stdout.txt
    sha256: 6671da8c245d3b43b626f9a91e5d6d4a404561b60b56f97f5c060fc6f417dbc1
    role: context
  - path: .temp/pr2039/373/media-sources.json
    sha256: 5ba0a8cf8f0afcb1eaaa6739e352cdaae10c13df888e95cdab5542d136f55894
    role: context
  - path: .temp/pr2039/373/normalize-cache-names-check.json
    sha256: 5ab1766c51629e83b60bf5619378ef7626b11a620e219a6dca0ba8ff35455623
    role: context
  - path: .temp/pr2039/373/normalize-cache-names-check.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2039/373/normalize-cache-names-check.stdout.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2039/373/ontology-authorities.json
    sha256: 92d7fdd856ea4de05a74c91a942b4cb11a4475d25f48e3d67378fb721a621de2
    role: context
  - path: .temp/pr2039/373/pmc-efetch.xml
    sha256: 3bcf1d05787af2f2ba0362d0517e3e2833ad6a77b6c0e568e157652c9cc3ad53
    role: context
  - path: .temp/pr2039/373/pmc-text.txt
    sha256: 4a4e64f8888c20c2a7644b56cce4d4f489f1821a99a57ab49737bb9fd67f09b8
    role: context
  - path: .temp/pr2039/373/pmc.html
    sha256: c807670a53d46d99811a666598e5203bb18acdabb608732d8becd4442342fa00
    role: context
  - path: .temp/pr2039/373/primary-html-replay.json
    sha256: 7a1dc23e11964758b4342a9360c767fc3449cd971869b4be8c0d33cded8f9a16
    role: context
  - path: .temp/pr2039/373/primary-sections.json
    sha256: 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
    role: context
  - path: .temp/pr2039/373/ps71069-fig-0001.webp
    sha256: ade140610378545538f8c644a10b3092212a72ea2e4f84541b1f7273c3d70471
    role: context
  - path: .temp/pr2039/373/ps71069-fig-0002.webp
    sha256: 082d51f44787e6f52d5426312d77b7f97709f467522c2fc882b29451431e2485
    role: context
  - path: .temp/pr2039/373/ps71069-fig-0003.webp
    sha256: 55bc49186a66b470af7008f9660a37b544b529558798ede6778b6a4cf1adbf8d
    role: context
  - path: .temp/pr2039/373/ps71069-fig-0004.webp
    sha256: 4b2dcdb4dd507a89471a1330329ee60df8595f005fdaf9845db9523a247b3aa1
    role: context
  - path: .temp/pr2039/373/ps71069-fig-0005.webp
    sha256: de497cdc23619dcf68dc6b826e30f7f1213caba96c7c0418dd9954b4e17143b8
    role: context
  - path: .temp/pr2039/373/ps71069-fig-0006.webp
    sha256: c3d68e059552ae94ff33161078c04deddfb3216505f944cfec1f8bdab4925184
    role: context
  - path: .temp/pr2039/373/ps71069-fig-0007.webp
    sha256: af57ebb18d962ec3cf97d01acda9c52d099562719cfdcc78a4105088194e7d0f
    role: context
  - path: .temp/pr2039/373/ps71069-fig-0008.webp
    sha256: 97f2fecf40e216df08bab3714083f1cb312a57161d45cef2ca8ca77da5c81dd0
    role: context
  - path: .temp/pr2039/373/ps71069-fig-0009.webp
    sha256: 9239db361f01b66ea3d9d40d6ff1926d322de90c5eb6c458e26019fb9f2b18bc
    role: context
  - path: .temp/pr2039/373/ps71069-fig-0010.webp
    sha256: 8a9311442c81fb5aa103c772e05e24542c8fda72638d604b796691993e974ea1
    role: context
  - path: .temp/pr2039/373/ps71069-fig-0011.webp
    sha256: 53a6661f6dae3056d5d4eca181e5f9ddc6b93a5e92f40b1aaec29dbdd9bf40f5
    role: context
  - path: .temp/pr2039/373/publication.xml
    sha256: 103674cbfe03ac75435744f571fe47bf7eb86395ca6f9dc10afad731a6d1df26
    role: context
  - path: .temp/pr2039/373/semantic-diff.json
    sha256: 75eedc34865164fe1fba3e77462bf14b98d3d196e200a8eacdbdecad7ed0683b
    role: context
  - path: .temp/pr2039/373/snippet-replay.json
    sha256: abeca839494d3695c3336338415d1214197ee4998576d221992151c592ab75c2
    role: context
  - path: .temp/pr2039/373/sources.json
    sha256: cc34060703659cd069a193ba1527d578e15ac5fc662612bda56d521ecc3f20b2
    role: context
  - path: .temp/pr2039/373/strict.tsv
    sha256: b184ed5450b968070bb6c75648407e388f41a1eaf7017890723cf560999fc3f7
    role: context
  - path: .temp/pr2039/373/supplement.docx
    sha256: 343f71ede97e4e4d91e0e66e3350202939331573a9c550d2099e7bf17bd92428
    role: context
  - path: .temp/pr2039/373/target-diff.json
    sha256: fa79a000b14d4812e99a6e5dbc464aadf2ccb1f24c8405951ad5dcd5ec9a6ffb
    role: context
  - path: .temp/pr2039/373/target-diff.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2039/373/target-diff.stdout.txt
    sha256: b880fd6fb7735abec15107b74fc875e301ae8b11ee0161c4e3f32e0a7e12f7c8
    role: context
  - path: .temp/pr2039/373/target-network.json
    sha256: 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
    role: context
  - path: .temp/pr2039/373/targets.json
    sha256: 35ddabd08464c8434d5015ba0356b85f546cd222c1eeb2bf9052c47f4688a77f
    role: context
  - path: .temp/pr2039/373/validate-gtdb-domain.json
    sha256: 91ecab573d1f36e1cf582d79eeb39caa7b0b3d5f3220c017755ee925c79c2ef7
    role: context
  - path: .temp/pr2039/373/validate-gtdb-domain.stderr.txt
    sha256: 5925babd20017eb547109bf90bd78e88a3986b03183b6383f6bb7de4f4a7d8e8
    role: context
  - path: .temp/pr2039/373/validate-gtdb-domain.stdout.txt
    sha256: ede937293c42cad366f434dce49a485a9a0c56fe86620b52ca243ad10e09ecae
    role: context
  - path: .temp/pr2039/373/validate-gtdb.json
    sha256: f8e83e5b3fe9d6d5cb8d029ecb5bf556af548bac02156baf52302485f6784fe9
    role: context
  - path: .temp/pr2039/373/validate-gtdb.stderr.txt
    sha256: 4ad46532316efb60a35d197a45a8dd936fa6dbb5d36463624a6aa52867f31120
    role: context
  - path: .temp/pr2039/373/validate-gtdb.stdout.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2039/373/validate-history.json
    sha256: c72d5a4ab18722f7e5fc75c700bef2c3a3ffe04bda56e5500e6d51fc0bc0bfec
    role: context
  - path: .temp/pr2039/373/validate-history.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2039/373/validate-history.stdout.txt
    sha256: de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
    role: context
  - path: .temp/pr2039/373/validate-references-explained.json
    sha256: aacfabaf3c87d0cf9cd04d3c77a5db9f9d51e1fc0dd7f9ddd9e61eae9c6b7b83
    role: context
  - path: .temp/pr2039/373/validate-references-explained.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2039/373/validate-references-explained.stdout.txt
    sha256: c8640855fd342e94bbc3b4794170566c1a75010b8e4cf5db66d97ba8fbc5a309
    role: context
  - path: .temp/pr2039/373/validate-strict.json
    sha256: f6424f7f26c1390d800b84081236ce4beabeb37a4353cc4860faf3a1c3b45a2e
    role: context
  - path: .temp/pr2039/373/validate-strict.stderr.txt
    sha256: 150b2f4046118dbf4e4fe4945678108d9401c535bb267a149bc93dd5f44f4aa8
    role: context
  - path: .temp/pr2039/373/validate-strict.stdout.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2039/373/validate-terms.json
    sha256: 301986627197f519db20eb438eb9eb7b2f2e1f48da8930febba0f058715594ef
    role: context
  - path: .temp/pr2039/373/validate-terms.stderr.txt
    sha256: 8bcc4b82272ac8b15ee1549013bf3291dcb98e760c72a2c4e85fb417ffcbf284
    role: context
  - path: .temp/pr2039/373/validate-terms.stdout.txt
    sha256: 23acda1c1d3194d12bc947d897d07de83f4a076a9d93c135148885108530e018
    role: context
  - path: .temp/pr2039/373/validate.json
    sha256: 830aada84fe8e5d9b76251bfa5f8ee1f22bb310c04ddea345b3856a4911b46a9
    role: context
  - path: .temp/pr2039/373/validate.stderr.txt
    sha256: e732bae059aad173b0dcfaa36e808f867123df032d019ac9477fd405a9173e37
    role: context
  - path: .temp/pr2039/373/validate.stdout.txt
    sha256: de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
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
  - path: history/records/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom/2026-09-14T042451Z-codex-bacillus-tobacco.yaml
    sha256: 5edbf58603e8088c5b05fabd4f028014cd0c76414cf477e622b1d5aba1d8d519
    role: context
  - path: history/records/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom/2026-10-05T101150Z-codex-7933b3.yaml
    sha256: 1ee592e291879f3df8b0aae5f529d6b66e701f6c1d0ba9d784d2364a8a269d98
    role: context
  - path: history/records/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom/2026-10-21T190000Z-claude-2049.yaml
    sha256: 6ded0417ac214168f8a1b3c7b50f0b92c3e54bcc75f50aea8c4738de20c1ff60
    role: context
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml
    sha256: c9f62a78e6ca7a6c6fc3f3886a77fb9d7e0583f3ce931dd474aeefa2217a1e9d
    role: target
  - path: references_cache/PMID_42388034.txt
    sha256: 7c411b8884969706099963aa4cf8b7f6b1cda8810a8b38ca1dc392420d3dd393
    role: context
  - path: reports/causal_graph_review/decisions/20261005-eleven-records-batch5.yaml
    sha256: 5076ec8295dacfaae0ae1d829836e4380a312a702c4a43df5f604c3b1b1e0ad3
    role: context
  - path: reviews/structured/20261021T085942Z-bacillus-tobacco-syncom-record/review.yaml
    sha256: 659923a2b4d441158d87a2e19b19f1ff9666ccff1e50773c4b18428bfa2cabe2
    role: context
  - path: reviews/structured/20261021T101000Z-stage4-record-deep-audit/review.yaml
    sha256: f32db16fda535e46adee4bd7d8d2de5c3f206dc7fdb892d137e1fe00e3346b59
    role: context
  - path: reviews/structured/20261021T101100Z-stage4-frozen-cohort-review/review.yaml
    sha256: 37d089fd55c077793dd20d868b50c47cb1cceab6dae6a82887cc938bee05fa6d
    role: context
  - path: reviews/structured/20261021T193000Z-stage5-remediation-verification/review.yaml
    sha256: 8f8f980813203a0336e27f0bc0a3c3b6e68bb68c2f2a7d71460183f4fe3bbc09
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/adhoc/pr2039_373_audit.py
    sha256: fd2310c8de6572e7c0e85d68a5b60e85f05a1ffa7f1df8ba0aa1f21976a14b7e
    role: context
  - path: scripts/adhoc/pr2039_373_html.py
    sha256: 7d52d05209384b9f739d73310517cb3d78e5f5010533bdbc75dbb93c027bbb80
    role: context
  - path: scripts/adhoc/pr2039_373_media.py
    sha256: 0daf3b7d3e8b8804d15e5c817431fb89dbf8cf9c0f068929ddbe9b64083c3508
    role: context
  - path: scripts/adhoc/pr2039_373_review.py
    sha256: 35af9e98184ed1b7d6566b3bf6898820847ea485358cbb4ae827888d4906680a
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
- target_id: CommunityMech:000373
  path: kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml
  label: Bacillus G12-Y4-X25 Tobacco Biocontrol SynCom
  kind: maintained
  record_class: MicrobialCommunity
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml
    role: canonical_record
scope:
  description: Entire current three-strain target, all five community-level nodes
    and no arrows, 18 evidence occurrences, three history sidecars, complete primary
    main HTML and main Figures 1–11. Supplementary captions S1–S5 were read, but the
    DOCX download returned HTML and its figure pixels were not inspected. No raw sequence
    or statistical reanalysis.
  selection: 'Refresh only stale CommunityMech:000373 in PR 2039. The parsed delta
    has five changed leaves: two tobacco target_taxon blocks removed, two descriptions
    given explicit tobacco names, and one embedded curation entry added. Every original
    finding was reassessed and retains its stable key and exact predecessor.'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000373
checks:
- check_id: validate
  name: validate
  status: passed
  required: true
  summary: Target schema validation passed.
  target_ids:
  - CommunityMech:000373
  command: just --no-dotenv validate kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate
  scope_note: Fresh focused target/history check, except read-only corpus cache-name
    preflight. Exact environment is in the pinned receipt; history syntax does not
    validate narrative truth.
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Target strict validation passed.
  target_ids:
  - CommunityMech:000373
  command: just --no-dotenv validate-strict kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml
    --out /Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2039-batch05/.temp/pr2039/373/strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-strict
  scope_note: Fresh focused target/history check, except read-only corpus cache-name
    preflight. Exact environment is in the pinned receipt; history syntax does not
    validate narrative truth.
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Target term validation passed.
  target_ids:
  - CommunityMech:000373
  command: just --no-dotenv validate-terms kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-terms
  scope_note: Fresh focused target/history check, except read-only corpus cache-name
    preflight. Exact environment is in the pinned receipt; history syntax does not
    validate narrative truth.
- check_id: validate-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: Target GTDB syntax/status validation passed.
  target_ids:
  - CommunityMech:000373
  command: just --no-dotenv validate-gtdb kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb
  scope_note: Fresh focused target/history check, except read-only corpus cache-name
    preflight. Exact environment is in the pinned receipt; history syntax does not
    validate narrative truth.
- check_id: validate-gtdb-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: Target GTDB domain validation passed.
  target_ids:
  - CommunityMech:000373
  command: just --no-dotenv validate-gtdb-domain kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb-domain
  scope_note: Fresh focused target/history check, except read-only corpus cache-name
    preflight. Exact environment is in the pinned receipt; history syntax does not
    validate narrative truth.
- check_id: validate-history
  name: validate-history
  status: passed
  required: true
  summary: Target history validation passed.
  target_ids:
  - CommunityMech:000373
  command: just --no-dotenv validate-history history/records/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-history
  scope_note: Fresh focused target/history check, except read-only corpus cache-name
    preflight. Exact environment is in the pinned receipt; history syntax does not
    validate narrative truth.
- check_id: normalize-cache-names-check
  name: normalize-cache-names-check
  status: passed
  required: true
  summary: Read-only corpus cache-filename preflight passed.
  target_ids:
  - CommunityMech:000373
  command: uv run python scripts/normalize_cache_names.py --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-normalize-cache-names-check
  scope_note: Fresh focused target/history check, except read-only corpus cache-name
    preflight. Exact environment is in the pinned receipt; history syntax does not
    validate narrative truth.
- check_id: validate-references-explained
  name: validate-references-explained
  status: passed
  required: true
  summary: Target reference validation passed against the pinned selected-passage
    cache.
  target_ids:
  - CommunityMech:000373
  command: just --no-dotenv validate-references-explained kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-references-explained
  scope_note: Fresh focused target/history check, except read-only corpus cache-name
    preflight. Exact environment is in the pinned receipt; history syntax does not
    validate narrative truth.
- check_id: audit-network
  name: audit-network
  status: failed
  required: true
  summary: 'Fresh corpus check retains exit 1: 44 warnings across 16 of 503 records,
    with zero target-specific issues.'
  target_ids:
  - CommunityMech:000373
  command: just --no-dotenv audit-network
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-audit-network
  scope_note: Corpus warning exit preserved, not relabeled as passed.
- check_id: check-network-quality
  name: check-network-quality
  status: failed
  required: true
  summary: 'Fresh corpus check retains exit 1: 44 warnings across 16 of 503 records,
    with zero target-specific issues.'
  target_ids:
  - CommunityMech:000373
  command: just --no-dotenv check-network-quality
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-check-network-quality
  scope_note: Corpus warning exit preserved, not relabeled as passed.
- check_id: publication-identity
  name: Publication identity and accessible-source comparison
  status: passed
  required: true
  summary: Fresh metadata, complete primary main HTML and all 18 snippets independently
    verify; all 11 main figures were visually reviewed.
  target_ids:
  - CommunityMech:000373
  evidence_ids:
  - pubmed
  - crossref
  - epmc
  - cache
  - snippets
- check_id: full-primary-source
  name: Remaining supplementary figure assessment
  status: unavailable
  required: true
  summary: Complete main Methods, Results, Discussion and Figures 1–11 are now inspected.
    Supplementary S1–S5 captions are accessible, but the DOCX route returns HTML and
    its figure pixels remain unavailable.
  target_ids:
  - CommunityMech:000373
  evidence_ids:
  - access
  - root-access
  - cache
  scope_note: Required supplemental scope remains incomplete; main-text access is
    no longer the limitation.
- check_id: source-data
  name: Encoded dataset accession and release boundary
  status: not_applicable
  required: false
  summary: No accession is encoded; the public statement reports temporary sequencing
    restrictions and future deposition.
  target_ids:
  - CommunityMech:000373
  evidence_ids:
  - datasets
  - root-access
- check_id: cross-mech
  name: Encoded medium and ingredient-Mech links
  status: not_applicable
  required: false
  summary: No CultureMech or MediaIngredientMech ID is encoded or uniquely inferred
    from the LB name.
  target_ids:
  - CommunityMech:000373
  evidence_ids:
  - record
  - cultivation
- check_id: structured-adapter
  name: Optional structured source adapter
  status: unavailable
  required: false
  summary: Optional runner unavailable; fresh public catalog provides a bounded fallback
    without exact target dataset or strain-module coverage.
  target_ids:
  - CommunityMech:000373
  evidence_ids:
  - adapter
evidence:
- evidence_id: record
  kind: record_content
  reference: kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml
  locator: 'Entire current record: three members, five nodes, no arrows and 18 snippets'
  summary: The record separates microbial inoculant members from tobacco host/pathogens,
    source habitats and measured endpoints.
  support: supports
  accessed_at: '2026-11-06T02:51:32.665033Z'
  snapshot_sha256: c9f62a78e6ca7a6c6fc3f3886a77fb9d7e0583f3ce931dd474aeefa2217a1e9d
- evidence_id: cache
  kind: primary_source
  reference: PMID:42388034
  locator: 'references_cache/PMID_42388034.txt: complete cache, selected Methods/Results/Discussion'
  summary: The committed cache remains selected primary passages, not the complete
    article. All 18 snippets match both this cache and the independently retrieved
    complete PMC main HTML.
  support: supports
  accessed_at: '2026-11-06T02:51:32.665033Z'
  snapshot_sha256: 7c411b8884969706099963aa4cf8b7f6b1cda8810a8b38ca1dc392420d3dd393
- evidence_id: pubmed
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=42388034&retmode=xml
  locator: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=42388034&retmode=xml
  summary: Fresh article-level PubMed metadata verifies PMID 42388034, DOI 10.1002/ps.71069,
    PMC13569317 and the full abstract.
  support: supports
  accessed_at: '2026-11-06T02:41:27.013089Z'
  snapshot_sha256: 103674cbfe03ac75435744f571fe47bf7eb86395ca6f9dc10afad731a6d1df26
- evidence_id: crossref
  kind: database
  reference: https://api.crossref.org/works/10.1002/ps.71069
  locator: https://api.crossref.org/works/10.1002/ps.71069
  summary: Fresh Crossref metadata verifies DOI/title and journal full-XML/PDF routes.
  support: supports
  accessed_at: '2026-11-06T02:41:27.362009Z'
  snapshot_sha256: d0f11341318b3382380050ecc03f8599dd17dc1f7ce2edf02fccf41ecd102810
- evidence_id: epmc
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:42388034&format=json&resultType=core
  locator: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:42388034&format=json&resultType=core
  summary: Fresh Europe PMC metadata links PMID 42388034, DOI 10.1002/ps.71069 and
    PMC13569317. Its XML route did not yield the body; the separately retrieved public
    PMC HTML did.
  support: supports
  accessed_at: '2026-11-06T02:41:28.227800Z'
  snapshot_sha256: 1425929b2c90b3decc0e30e22cf3cd932bc71b74129a46aa93a636071cee8f72
- evidence_id: access
  kind: validation
  reference: Public EPMC, PMC, BioC and Wiley routes
  locator: .temp/pr2039/373/sources.json and media-sources.json with per-request receipts
  summary: 'Fresh EPMC XML and publisher requests returned curl exit 56. PubMed, Crossref,
    EPMC metadata, PMC efetch, PMC HTML, BioC and catalog requests returned exit 0.
    Successful transport alone is not source sufficiency: the complete main HTML and
    11 figure images were inspected, whereas the supplement response is a Preparing
    to download HTML page, not DOCX. No bypass or paid retrieval was used.'
  support: context_only
  accessed_at: '2026-11-06T02:51:32.665033Z'
  snapshot_sha256: 5ba0a8cf8f0afcb1eaaa6739e352cdaae10c13df888e95cdab5542d136f55894
- evidence_id: root-access
  kind: validation
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC13569317/
  locator: 'Fresh author retrieval: complete Methods 2.1–2.8, Results 3.1–3.7, Discussion,
    main Figures 1–11 and supplementary captions S1–S5'
  summary: The original main-text access limitation is overcome. Supplementary captions
    are available in HTML; their DOCX and underlying supplementary pixels remain unverified.
    The author's own retrieval and source assessment are used here, not another agent's
    approval.
  support: context_only
  accessed_at: '2026-11-06T02:51:32.665033Z'
  snapshot_sha256: c807670a53d46d99811a666598e5203bb18acdabb608732d8becd4442342fa00
- evidence_id: members
  kind: primary_source
  reference: PMID:42388034
  locator: Abstract and Methods 2.1
  summary: G12 is the rhizosphere B. amyloliquefaciens isolate; Y4 and X25 are tobacco
    endophytes assigned to B. pumilus and B. velezensis. The source attributes prior
    F. oxysporum antagonism to G12 and P. nicotianae inhibition to Y4/X25. Identity/habitat
    snippets alone do not directly support the local role annotations.
  support: supports
  accessed_at: '2026-11-06T02:51:32.665033Z'
  snapshot_sha256: c807670a53d46d99811a666598e5203bb18acdabb608732d8becd4442342fa00
- evidence_id: compatibility
  kind: primary_source
  reference: PMID:42388034
  locator: Methods 2.2; Results 3.1; Figure 1 A–C; supplementary S1 caption
  summary: All six directional plate-inhibition values are below 25%. Figure 1 confirms
    mild inhibition and aggregate co-culture growth without resolving each strain's
    survival or persistent coexistence. The record does not claim a specific resource-depletion
    mechanism.
  support: supports
  accessed_at: '2026-11-06T02:51:32.665033Z'
  quote: mild inhibition
  snapshot_sha256: c807670a53d46d99811a666598e5203bb18acdabb608732d8becd4442342fa00
- evidence_id: iaa
  kind: primary_source
  reference: PMID:42388034
  locator: Methods 2.2; Results 3.1; Figure 1 D–E; Discussion
  summary: Per-volume Salkowski colorimetry reports 11.57 +/- 0.24 mg/L in the SynCom,
    above each monoculture. This supports the qualified IAA-output node; it does not
    establish member-resolved exchange or IAA-mediated plant protection. The separate
    co-cultivation growth protocol is not automatically an IAA incubation protocol.
  support: supports
  accessed_at: '2026-11-06T02:51:32.665033Z'
  quote: higher indole-3-acetic acid production
  snapshot_sha256: c807670a53d46d99811a666598e5203bb18acdabb608732d8becd4442342fa00
- evidence_id: glasshouse
  kind: primary_source
  reference: PMID:42388034
  locator: Methods 2.4; Results 3.3; Figures 3–5; supplementary S2–S3 captions
  summary: He Luo No. 1 tobacco receives preventive or curative treatment around a
    combined FO/PN challenge. Figure 4 shows disease indices 54.07 for pathogen control,
    9.26 for preventive SynCom and 26.67 for curative SynCom. The record's preventive
    reduction and separate curative benefit are supported without assigning a specific
    hormonal mechanism.
  support: supports
  accessed_at: '2026-11-06T02:51:32.665033Z'
  quote: significant disease suppression
  snapshot_sha256: c807670a53d46d99811a666598e5203bb18acdabb608732d8becd4442342fa00
- evidence_id: root-activity
  kind: primary_source
  reference: PMID:42388034
  locator: Methods 2.5; Results 3.4; Figure 6
  summary: The TTC/dehydrogenase assay and Figure 6 support higher root metabolic
    activity, with the text reporting 20.27–45.38% above preventive single-strain
    treatments. This is not direct biomass production or reciprocal microbial fitness.
    Root morphometry is a distinct endpoint.
  support: supports
  accessed_at: '2026-11-06T02:51:32.665033Z'
  quote: Root activity increased
  snapshot_sha256: c807670a53d46d99811a666598e5203bb18acdabb608732d8becd4442342fa00
- evidence_id: field
  kind: primary_source
  reference: PMID:42388034
  locator: Methods 2.7–2.8; Results 3.6–3.7; Figures 9–11; Discussion
  summary: The two yellow-soil sites show natural-disease control and middle-leaf-based
    estimated yield. Results 3.6 gives yield increases against the control. Figure
    9D shows only G12/Y4/X25/SC/LB yield arms, with SC versus X25 fresh-yield comparisons
    nonsignificant; commercial B. subtilis appears in disease-efficacy panel E. The
    Discussion makes a broader commercial-product yield claim, but the displayed yield
    evidence does not establish that comparator. Figure 11 genus shifts are nonsignificant
    and do not establish strain persistence.
  support: supports
  accessed_at: '2026-11-06T02:51:32.665033Z'
  quote: middle-leaf-based estimated yield
  snapshot_sha256: c807670a53d46d99811a666598e5203bb18acdabb608732d8becd4442342fa00
- evidence_id: cultivation
  kind: primary_source
  reference: PMID:42388034
  locator: Methods 2.1, 2.2, 2.4 and 2.7
  summary: Fresh complete Methods verify 30 C/180 rpm preparation, distinct 25 C/180
    rpm/48 h co-cultivation growth measurement, glasshouse 25 +/- 2 C with 12 h:12
    h light/dark and 70–80% RH for 21 days, and 10 mL per-plant field irrigation twice
    seven days apart. These contexts must remain separate; a precise LB recipe is
    not specified.
  support: supports
  accessed_at: '2026-11-06T02:51:32.665033Z'
  snapshot_sha256: c807670a53d46d99811a666598e5203bb18acdabb608732d8becd4442342fa00
- evidence_id: limits
  kind: primary_source
  reference: PMID:42388034
  locator: Methods 2.6, 2.8; Results 3.5, 3.7; Figures 7–8, 10–11; Discussion
  summary: Pooled root/stem/leaf transcriptomic and co-expression associations do
    not prove tissue-specific hormonal mechanisms. A single-site endpoint and nonsignificant
    genus changes do not establish inoculant persistence, niche differentiation or
    resilience. Figure 10(F) depicts lower bacterial richness in SC than LB despite
    prose saying higher; no directional richness claim is adopted and the target encodes
    none.
  support: supports
  accessed_at: '2026-11-06T02:51:32.665033Z'
  snapshot_sha256: c807670a53d46d99811a666598e5203bb18acdabb608732d8becd4442342fa00
- evidence_id: ontology
  kind: authority
  reference: Local OAK NCBITaxon, ENVO, CHEBI and GO snapshots
  locator: Ten unique current NCBITaxon, ENVO, CHEBI and GO pairs
  summary: All 10 canonical labels match local OAK authority values. Species terms
    preserve isolate context; broad defense/growth terms are bounded to observed plant
    endpoints. The removed tobacco target objects are not current ontology placements.
  support: supports
  accessed_at: '2026-11-06T02:51:32.665033Z'
  snapshot_sha256: 92d7fdd856ea4de05a74c91a942b4cb11a4475d25f48e3d67378fb721a621de2
- evidence_id: schema
  kind: authority
  reference: src/communitymech/schema/communitymech.yaml
  locator: InteractionTypeEnum.COMPETITION; FunctionalRoleEnum.PATHOGEN_ANTAGONIST;
    AbundanceEnum.DOMINANT; taxonomy host exclusion
  summary: COMPETITION permits reciprocal negative effects without requiring resource
    depletion. DOMINANT is ordinal prominence of the co-equal formulation members,
    not a measured field population fraction. Tobacco remains external host context
    in descriptions; it is not a microbial member.
  support: supports
  accessed_at: '2026-11-06T02:51:32.665033Z'
- evidence_id: snippets
  kind: validation
  reference: kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml
  locator: 'primary-html-replay.json and snippet-replay.json: all 18 evidence occurrences'
  summary: All 18 snippets match the fresh main HTML and the selected committed cache
    after NFKC and whitespace normalization. None is an exact match to the differently
    worded fresh PubMed abstract; main-text matching now independently verifies the
    lexical spans.
  support: supports
  accessed_at: '2026-11-06T02:51:32.665033Z'
  snapshot_sha256: 7a1dc23e11964758b4342a9360c767fc3449cd971869b4be8c0d33cded8f9a16
- evidence_id: datasets
  kind: validation
  reference: PMID:42388034
  locator: Fresh PMC main article Data Availability Statement and Methods 2.6/2.8
  summary: The current public article still states temporary sequencing-release restrictions
    and future deposition without a study accession. GCF_000715135.1 is a tobacco
    reference genome, not this study's deposited reads. No arbitrary accession or
    dataset-omission defect is inferred; no author contact or raw-data analysis was
    performed.
  support: supports
  accessed_at: '2026-11-06T02:51:32.665033Z'
  snapshot_sha256: c807670a53d46d99811a666598e5203bb18acdabb608732d8becd4442342fa00
- evidence_id: history
  kind: record_content
  reference: history/records/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom/2026-10-21T190000Z-claude-2049.yaml
  locator: All three sidecars; exact 000373 row in 20261005-eleven-records-batch5.yaml;
    fresh issues 1248, 880 and 2049
  summary: The historical graph decision's record hash matches the original review
    input and its non-graph exclusion remains explicit. Issues 1248 and 880 are CLOSED.
    The new October 21 sidecar is schema-valid but falsely describes 000449 and counter_selection/Ralstonia
    changes. The actual delta is tobacco-target removal. Closed issue 2049 also misidentifies
    the 000373 record/source and is context only, not scientific proof.
  support: supports
  accessed_at: '2026-11-06T02:51:32.665033Z'
  snapshot_sha256: 6ded0417ac214168f8a1b3c7b50f0b92c3e54bcc75f50aea8c4738de20c1ff60
- evidence_id: search
  kind: search
  reference: Owned community/isolate/reusable-taxon roots
  locator: Fresh rg --no-ignore --hidden exact record ID, PMID, G12, Y4 and X25 query
  summary: The ignored-inclusive bounded search located this target's cache, three
    history sidecars and graph decision material. It produced no exact isolate-authenticating
    kb/taxa hit; shared Bacillus species do not establish equivalent isolates. The
    query also contains an irrelevant prior-target alternative, which does not narrow
    its exact current-target alternatives.
  support: supports
  accessed_at: '2026-11-06T02:51:32.665033Z'
  search_scope: references_cache, history, reports/causal_graph_review/decisions and
    kb/taxa, including hidden and ignored files; no machine-wide absence claim.
  snapshot_sha256: 6671da8c245d3b43b626f9a91e5d6d4a404561b60b56f97f5c060fc6f417dbc1
- evidence_id: adapter
  kind: search
  reference: Optional kg-microbe-sources and public iModulonDB catalog
  locator: adapter-discovery.json and fresh imodulon-catalog.json
  summary: No runner was found in PATH or either exact probed sibling checkout. The
    inspected public catalog includes B. subtilis but no exact G12/Y4/X25 target dataset;
    a different Bacillus species is not a substitute. No expression-module query was
    performed.
  support: supports
  accessed_at: '2026-11-06T02:51:32.665033Z'
  search_scope: PATH and two exact sibling paths including ignored files, then the
    public organism/dataset catalog; absence is not negative biological evidence.
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
- evidence_id: native-target
  kind: validation
  reference: NetworkIntegrityAuditor().audit_community(target)
  locator: Fresh NetworkIntegrityAuditor().audit_community(current target)
  summary: The target audit returned an empty issue list after host-target removal.
    All five nodes use COMMUNITY_LEVEL scope for the three-member SynCom and contain
    one evidence item each; no explicit participating_taxa lists or downstream edges
    are encoded. Native structural completeness does not prove missing scientific
    mechanisms.
  support: supports
  accessed_at: '2026-11-06T02:51:32.665033Z'
  snapshot_sha256: 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
- evidence_id: current-delta
  kind: record_content
  reference: kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml
  locator: semantic-diff.json; original frozen input versus current merged-main target
  summary: 'Exactly five semantic leaves changed: curation_history[2] added, tobacco
    target_taxon removed from nodes 3 and 4, and explicit tobacco names added to those
    descriptions. The source scopes and two original finding surfaces remain unchanged.'
  support: supports
  accessed_at: '2026-11-06T02:51:32.665033Z'
  snapshot_sha256: 75eedc34865164fe1fba3e77462bf14b98d3d196e200a8eacdbdecad7ed0683b
- evidence_id: host-lineage
  kind: record_content
  reference: reviews/structured/20261021T193000Z-stage5-remediation-verification/review.yaml
  locator: stage4-external-host-pathogen-targets and exact Stage 4 predecessor rows;
    lineage.json
  summary: The later grouped finding explicitly resolves the host-target outcome for
    000347/000364/000373. This successor independently confirms only the 000373 tobacco-target
    cleanup. It neither reassesses the other targets nor supersedes the grouped disposition;
    the contradictory issue/history identity text is separately flagged.
  support: context_only
  accessed_at: '2026-11-06T02:51:32.665033Z'
  snapshot_sha256: 583b24c1ea1c5ac531728352055326202456c1b7992786b8630960e3ee76f678
- evidence_id: check-validate
  kind: validation
  reference: just --no-dotenv validate kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml
  locator: .temp/pr2039/373/validate.json; 2026-11-06T02:41:22.125920Z to 2026-11-06T02:41:22.630243Z
  summary: Target schema validation passed.
  support: supports
  accessed_at: '2026-11-06T02:41:22.630243Z'
  snapshot_sha256: 830aada84fe8e5d9b76251bfa5f8ee1f22bb310c04ddea345b3856a4911b46a9
- evidence_id: check-validate-strict
  kind: validation
  reference: just --no-dotenv validate-strict kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml
    --out /Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2039-batch05/.temp/pr2039/373/strict.tsv
  locator: .temp/pr2039/373/validate-strict.json; 2026-11-06T02:41:22.630432Z to 2026-11-06T02:41:24.531554Z
  summary: Target strict validation passed.
  support: supports
  accessed_at: '2026-11-06T02:41:24.531554Z'
  snapshot_sha256: f6424f7f26c1390d800b84081236ce4beabeb37a4353cc4860faf3a1c3b45a2e
- evidence_id: check-validate-terms
  kind: validation
  reference: just --no-dotenv validate-terms kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml
  locator: .temp/pr2039/373/validate-terms.json; 2026-11-06T02:41:24.531725Z to 2026-11-06T02:41:25.574661Z
  summary: Target term validation passed.
  support: supports
  accessed_at: '2026-11-06T02:41:25.574661Z'
  snapshot_sha256: 301986627197f519db20eb438eb9eb7b2f2e1f48da8930febba0f058715594ef
- evidence_id: check-validate-gtdb
  kind: validation
  reference: just --no-dotenv validate-gtdb kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml
  locator: .temp/pr2039/373/validate-gtdb.json; 2026-11-06T02:41:25.574843Z to 2026-11-06T02:41:25.634574Z
  summary: Target GTDB syntax/status validation passed.
  support: supports
  accessed_at: '2026-11-06T02:41:25.634574Z'
  snapshot_sha256: f8e83e5b3fe9d6d5cb8d029ecb5bf556af548bac02156baf52302485f6784fe9
- evidence_id: check-validate-gtdb-domain
  kind: validation
  reference: just --no-dotenv validate-gtdb-domain kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml
  locator: .temp/pr2039/373/validate-gtdb-domain.json; 2026-11-06T02:41:25.634749Z
    to 2026-11-06T02:41:26.571279Z
  summary: Target GTDB domain validation passed.
  support: supports
  accessed_at: '2026-11-06T02:41:26.571279Z'
  snapshot_sha256: 91ecab573d1f36e1cf582d79eeb39caa7b0b3d5f3220c017755ee925c79c2ef7
- evidence_id: check-validate-history
  kind: validation
  reference: just --no-dotenv validate-history history/records/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom
  locator: .temp/pr2039/373/validate-history.json; 2026-11-06T02:41:26.571459Z to
    2026-11-06T02:41:27.106257Z
  summary: Target history validation passed.
  support: supports
  accessed_at: '2026-11-06T02:41:27.106257Z'
  snapshot_sha256: c72d5a4ab18722f7e5fc75c700bef2c3a3ffe04bda56e5500e6d51fc0bc0bfec
- evidence_id: check-normalize-cache-names-check
  kind: validation
  reference: uv run python scripts/normalize_cache_names.py --check
  locator: .temp/pr2039/373/normalize-cache-names-check.json; 2026-11-06T02:41:27.106454Z
    to 2026-11-06T02:41:27.145533Z
  summary: Read-only corpus cache-filename preflight passed.
  support: supports
  accessed_at: '2026-11-06T02:41:27.145533Z'
  snapshot_sha256: 5ab1766c51629e83b60bf5619378ef7626b11a620e219a6dca0ba8ff35455623
- evidence_id: check-validate-references-explained
  kind: validation
  reference: just --no-dotenv validate-references-explained kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml
  locator: .temp/pr2039/373/validate-references-explained.json; 2026-11-06T02:41:27.145737Z
    to 2026-11-06T02:41:27.915383Z
  summary: Target reference validation passed against the pinned selected-passage
    cache.
  support: supports
  accessed_at: '2026-11-06T02:41:27.915383Z'
  snapshot_sha256: aacfabaf3c87d0cf9cd04d3c77a5db9f9d51e1fc0dd7f9ddd9e61eae9c6b7b83
- evidence_id: check-audit-network
  kind: validation
  reference: just --no-dotenv audit-network
  locator: .temp/pr2039/373/audit-network.json; 2026-11-06T02:41:27.915565Z to 2026-11-06T02:41:32.146475Z
  summary: 'Fresh corpus check retains exit 1: 44 warnings across 16 of 503 records,
    with zero target-specific issues.'
  support: supports
  accessed_at: '2026-11-06T02:41:32.146475Z'
  snapshot_sha256: d4b57de354bca760a5a6ece012be1226f85a431b66250c0efa35b3b90436015b
- evidence_id: check-check-network-quality
  kind: validation
  reference: just --no-dotenv check-network-quality
  locator: .temp/pr2039/373/check-network-quality.json; 2026-11-06T02:41:32.146648Z
    to 2026-11-06T02:41:36.334206Z
  summary: 'Fresh corpus check retains exit 1: 44 warnings across 16 of 503 records,
    with zero target-specific issues.'
  support: supports
  accessed_at: '2026-11-06T02:41:36.334206Z'
  snapshot_sha256: 96fcfd01e0b767ca98c053f9b005609c85fb2117fa9c2830dba7ef6e4b4af9a6
assessments:
- assessment_id: identity
  area: identity
  topic: Three-strain inoculant and plant-pathogen assay scope
  outcome: supported
  summary: The source resolves G12/Y4/X25 and separates inoculum composition, host/pathogen
    targets and experimental endpoints.
  target_ids:
  - CommunityMech:000373
  evidence_ids:
  - record
  - members
  - cultivation
  - schema
  - ontology
  dimensions:
  - name: community_scope
    value: Three-strain Bacillus SynCom tested on tobacco
    definition: ENGINEERED/SYNTHETIC/RHIZOSPHERE fit the function-guided inoculant;
      plant and challenge pathogens are not added microbial members.
    evidence_ids:
    - record
    - members
    - schema
  - name: source_strain
    value: B. amyloliquefaciens G12, B. pumilus Y4 and B. velezensis X25
    definition: Source names/habitats are explicit; species ontology anchors do not
      establish deposited isolate genomes or physiological equivalence to other strains.
    evidence_ids:
    - members
    - ontology
  - name: environment
    value: Tobacco-associated and rhizosphere contexts
    definition: The rhizosphere and plant-associated ENVO terms preserve different
      isolate habitats and application/sampling contexts.
    evidence_ids:
    - members
    - field
    - ontology
  - name: medium
    value: LB preparation and separate co-cultivation measurement
    definition: The encoded 30 C preparation is supported; the separate 25 C/48 h
      assay context is omitted. No exact CultureMech recipe is inferred from the LB
      name.
    evidence_ids:
    - cultivation
  - name: experimental_setting
    value: Plate and liquid assays, two glasshouse trials and two field sites
    definition: Glasshouse challenge and preventive/curative timing differ from field
      natural disease and repeat root irrigation.
    evidence_ids:
    - compatibility
    - glasshouse
    - field
    - cultivation
  - name: evidence_tier
    value: Measured endpoints and associated host responses
    definition: IAA, TTC root activity, defense enzymes and estimated yield remain
      separate; hormonal mediation and persistent strain colonization are not established.
    evidence_ids:
    - iaa
    - root-activity
    - limits
  - name: grounding_status
    value: Ten canonical term pairs; historical GTDB blocks/statuses
    definition: G12/Y4 remain UNRESOLVED and X25 GROUNDED at species level; historical
      release/count provenance was not recomputed.
    evidence_ids:
    - ontology
    - adapter
- assessment_id: taxonomy
  area: grounding
  topic: All three member roles, source strains and prominence
  outcome: concern
  summary: Identities, habitats and antagonist roles are supported, but nearest taxonomy
    snippets establish only identity/source.
  target_ids:
  - CommunityMech:000373
  evidence_ids:
  - members
  - schema
  - ontology
  - limits
  details: Attach the explicit pathogen-specific antagonism evidence locally. DOMINANT
    may describe co-equal formulation members; it is not a percentage defect and does
    not certify abundance or persistence in field soil.
- assessment_id: node-0
  area: graph
  topic: 'ecological_interactions[0]: Mild-Inhibition Three-Strain SynCom Compatibility'
  outcome: supported
  summary: Reciprocal directional inhibition supports the existing COMPETITION label
    at plate-assay scope.
  target_ids:
  - CommunityMech:000373
  evidence_ids:
  - compatibility
  - members
  - schema
  - limits
  details: Participants are G12, Y4 and X25, with each pair tested in both directions.
    Fresh Methods 2.2, Results 3.1 and Figure 1 corroborate mild reciprocal plate
    inhibition. This supports COMPETITION at assay scope, not resource depletion,
    reciprocal benefit or durable coexistence; supplementary plate photographs S1
    remain uninspected.
- assessment_id: node-1
  area: graph
  topic: 'ecological_interactions[1]: SynCom Indole-3-Acetic Acid Enhancement'
  outcome: supported
  summary: The node preserves a per-volume colorimetric increase without claiming
    exchange or IAA-mediated plant protection.
  target_ids:
  - CommunityMech:000373
  evidence_ids:
  - iaa
  - cultivation
  - members
  - ontology
  details: Direction is three-strain co-culture versus constituent monocultures to
    measured supernatant output. The separate 25 C/48 h co-cultivation growth measurement
    is not assumed to define the IAA assay conditions. GO IAA biosynthesis and CHEBI
    identity are compatible subject annotations; no member-resolved flux or selective
    mediation is certified.
- assessment_id: node-2
  area: graph
  topic: 'ecological_interactions[2]: Tobacco FO/PN Glasshouse Disease Suppression'
  outcome: supported
  summary: Disease-index suppression is corroborated; the record does not convert
    it into a specific hormonal pathway.
  target_ids:
  - CommunityMech:000373
  evidence_ids:
  - glasshouse
  - members
  - ontology
  - limits
  details: The G12/Y4/X25 inoculant treats He Luo No. 1 tobacco challenged with F.
    oxysporum and P. nicotianae, under preventive and curative timing. Source defense-enzyme
    responses support broad protective-response context but do not distinguish every
    direct/host-mediated contribution.
- assessment_id: node-3
  area: graph
  topic: 'ecological_interactions[3]: Tobacco Root Activity Improvement'
  outcome: supported
  summary: The TTC-based endpoint is correctly limited to root metabolic activity.
  target_ids:
  - CommunityMech:000373
  evidence_ids:
  - root-activity
  - members
  - schema
  details: Direction is SynCom treatment under FO/PN stress to tobacco root TTC activity
    versus single-strain treatments. Tobacco is now explicitly named in the description
    and absent from target_taxon. This preserves external host scope without treating
    it as a missing microbial member or turning TTC activity into biomass growth.
- assessment_id: node-4
  area: graph
  topic: 'ecological_interactions[4]: Two-Site Field Disease Suppression and Yield
    Increase'
  outcome: concern
  summary: Natural-disease and estimated-yield outcomes are supported, but the combined
    sentence overextends demonstrated yield comparators.
  target_ids:
  - CommunityMech:000373
  evidence_ids:
  - field
  - cultivation
  - members
  - limits
  - ontology
  details: Results 3.6 gives numeric yield increases versus the control, and Figure
    9D has no commercial-product yield arm. Figure 9E supports superior disease efficacy
    versus B. subtilis. Although the Discussion asserts broader yield superiority,
    the record should separate these endpoint/comparator scopes or explicitly attribute
    that unresolved assertion. Not every single-strain yield comparison is significant.
    Neither whole-plot harvested yield nor durable microbiome change is established.
- assessment_id: edges
  area: graph
  topic: downstream inventory
  outcome: not_applicable
  summary: No downstream arrows are encoded, so no additional mechanistic direction
    is certified.
  target_ids:
  - CommunityMech:000373
  evidence_ids:
  - record
  - limits
- assessment_id: cultivation
  area: completeness
  topic: LB, glasshouse and field context
  outcome: concern
  summary: The correctly scoped 30 C preparation block omits separate co-cultivation
    growth, glasshouse and field conditions now independently verified in complete
    Methods.
  target_ids:
  - CommunityMech:000373
  evidence_ids:
  - cultivation
  - record
  details: Keep preparation, 25 C/48 h co-cultivation measurement, 21-day controlled
    plant experiment and repeated field root irrigation separate. The environmental
    factor duplicates assembly strategy. The source does not provide a unique LB formulation;
    supplement unavailability no longer prevents checking these main-text conditions.
- assessment_id: ingredients
  area: grounding
  topic: IAA output and biological scope
  outcome: supported
  summary: The IAA entry is a measured potential growth-promoting output rather than
    a verified mediator of disease protection.
  target_ids:
  - CommunityMech:000373
  evidence_ids:
  - iaa
  - ontology
  - limits
  details: No metal-processing phenotype or specific additional metabolite is established
    by the accessible evidence. Names alone do not justify additional pathways or
    genes.
- assessment_id: provenance
  area: evidence
  topic: Source/cache/history and resource boundaries
  outcome: concern
  summary: Fresh complete main HTML supports every snippet, but the October 21 history
    narrative misidentifies the record and edit.
  target_ids:
  - CommunityMech:000373
  evidence_ids:
  - pubmed
  - crossref
  - epmc
  - cache
  - snippets
  - history
  - datasets
  - root-access
  details: The committed cache is still selected text and is not overwritten. An append-only
    correction must reconcile the incorrect 000449/Ralstonia/counter_selection narrative
    with the actual 000373 tobacco-target cleanup. Closed issue 2049 also has unrelated
    record/source identities; its closure is not evidence of scientific correctness.
    Current public data restrictions remain explicit, with no invented study accession.
- assessment_id: validation
  area: schema
  topic: Native checks and remaining supplementary scope
  outcome: concern
  summary: Eight focused/native checks pass; all 10 current term pairs and all 18
    snippets verify. The target audit is clean. The corpus commands retain their 44-warning
    exits, and unavailable supplementary pixels keep completion partial.
  target_ids:
  - CommunityMech:000373
  evidence_ids:
  - ontology
  - snippets
  - check-validate
  - check-validate-strict
  - check-audit-network
  - native-target
  - schema
  - access
- assessment_id: metrics
  area: completeness
  topic: Native completeness and quality within partial supplementary coverage
  outcome: supported
  summary: Completeness is 85 and capped validation quality is 100; source scope and
    open findings remain explicit.
  target_ids:
  - CommunityMech:000373
  evidence_ids:
  - record
  - native-target
  metrics:
  - name: completeness
    value: 85
    unit: points
    minimum: 0
    maximum: 100
    definition: min(100, 50 required metadata including all taxon roles + 5 environment
      + 10 at least 3 factors + 10 at least 3 nodes + 5 resources + 10 media + 5 datasets
      + 5 node metabolites). 50 + 5 + 0 + 10 + 5 + 10 + 0 + 5 = 85.
  - name: validation_quality
    value: 100
    unit: points
    minimum: 0
    maximum: 100
    definition: clamp(100 - 50P1 - 10P2 - 2P3 + 20 min(mean node evidence / 2, 1)
      + 15 if native COMPLETE, 0, 100). P1 = 0, P2 = 1, P3 = 3, P4 = 0; 5 items /
      5 nodes = 1; native target audit is empty. 100 - 10 - 6 + 10 + 15 = 109 before
      capping. A clean structural score does not complete supplementary source assessment.
  - name: P1
    value: 0
    unit: findings
    definition: Observed native severity count within this partial record review.
  - name: P2
    value: 1
    unit: findings
    definition: Observed native severity count within this partial record review.
  - name: P3
    value: 3
    unit: findings
    definition: Observed native severity count within this partial record review.
  - name: P4
    value: 0
    unit: findings
    definition: Observed native severity count within this partial record review.
- assessment_id: staleness-and-host-lineage
  area: provenance
  topic: Current-main host cleanup and grouped-review boundary
  outcome: supported
  summary: Fresh inspection replaces the stale input and confirms only the bounded
    000373 host-target cleanup.
  details: Nodes 3 and 4 retain tobacco host context and source-backed outcomes without
    host membership. The Stage 5 grouped resolved finding is context; no same-key
    supersession or disposition is emitted for its other targets. Incorrect history/issue
    identities remain a separate provenance concern. Both original single-record findings
    remain open.
  target_ids:
  - CommunityMech:000373
  evidence_ids:
  - current-delta
  - host-lineage
  - native-target
  - history
  - root-activity
  - field
findings:
- finding_id: role-evidence-placement
  issue_key: cm-000373-role-evidence-placement
  category: evidence
  severity: minor
  native_severity: P3
  normalization_reason: 'P3 minor: source-supported roles or experimental context
    lack precise local evidence/representation; the three-strain identity and qualified
    graph remain intact.'
  rule_id: review-checklist.claim_evidence
  status: open
  certainty: confirmed
  title: Taxonomy role claims lack their narrow source evidence
  description: Each PATHOGEN_ANTAGONIST entry cites taxonomic identity and isolation
    habitat, although the fresh abstract separately provides the relevant pathogen-specific
    prior-study attribution.
  target_ids:
  - CommunityMech:000373
  field_paths:
  - taxonomy[0].evidence
  - taxonomy[1].evidence
  - taxonomy[2].evidence
  evidence_ids:
  - members
  - schema
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml
    role: canonical_record
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261021T085942Z-bacillus-tobacco-syncom-record
    finding_id: role-evidence-placement
- finding_id: cultivation-context
  issue_key: cm-000373-cultivation-context
  category: completeness
  severity: minor
  native_severity: P3
  normalization_reason: 'P3 minor: source-supported roles or experimental context
    lack precise local evidence/representation; the three-strain identity and qualified
    graph remain intact.'
  rule_id: review-checklist.cultivation
  status: open
  certainty: confirmed
  title: Preparation and outcome-assay contexts are incompletely represented
  description: The LB block captures 30 C preparation but omits the separate 25 C/48
    h co-cultivation growth assay and controlled glasshouse/field settings. Fresh
    complete Methods independently verify these contexts; environmental_factors[0]
    repeats assembly design.
  target_ids:
  - CommunityMech:000373
  field_paths:
  - growth_media
  - cultivation_setup
  - environmental_factors[0]
  evidence_ids:
  - cultivation
  - record
  - cache
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml
    role: canonical_record
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261021T085942Z-bacillus-tobacco-syncom-record
    finding_id: cultivation-context
- finding_id: history-edit-misattribution
  issue_key: cm-000373-history-2049-edit-misattribution
  category: provenance
  severity: minor
  native_severity: P3
  normalization_reason: 'P3 minor: a non-blocking history narrative falsely attributes
    identity and edits; current scientific record identity remains correct.'
  rule_id: review-checklist.provenance
  status: open
  certainty: confirmed
  title: October 21 history misidentifies the record and the actual host-target edit
  description: The 2026-10-21T190000Z-claude-2049 sidecar names CommunityMech:000449
    and claims added Ralstonia/Phytophthora counter_selection entries. Current 000373
    instead removes tobacco target_taxon from nodes 3 and 4 and retains host text.
    Issue 2049's body separately assigns 000373 to an unrelated Ralstonia-phage/Pseudomonas
    record and PMID. Neither historical narrative is reliable proof of this change.
  target_ids:
  - CommunityMech:000373
  field_paths:
  - history/records/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom/2026-10-21T190000Z-claude-2049.yaml#events[0].summary
  - history/records/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom/2026-10-21T190000Z-claude-2049.yaml#events[0].details
  evidence_ids:
  - history
  - current-delta
  - host-lineage
  - members
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: history/records/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom/2026-10-21T190000Z-claude-2049.yaml
    role: append_only_history
- finding_id: field-yield-comparator
  issue_key: cm-000373-field-yield-comparator
  category: scope
  severity: major
  native_severity: P2
  normalization_reason: 'P2 major: a combined endpoint sentence presents commercial-product
    estimated-yield superiority beyond displayed comparator evidence, conflating disease
    and yield scopes.'
  rule_id: review-checklist.claim_evidence
  status: open
  certainty: confirmed
  title: Separate field disease-control and estimated-yield comparator scopes
  description: Node 4 says estimated yield increased relative to both single-strain
    and commercial microbial treatments. Figure 9D presents only G12/Y4/X25/SC/LB
    yield arms, while Figure 9E supports the commercial B. subtilis disease-efficacy
    comparison. Results 3.6 assigns the 41.33% and 37.54% dry-yield increases to the
    control. The Discussion does assert broader commercial-product yield superiority,
    but the presented yield evidence does not establish it; SC versus X25 fresh-yield
    comparisons are also nonsignificant. The record should preserve demonstrated comparators
    or explicitly qualify the broader author assertion.
  target_ids:
  - CommunityMech:000373
  field_paths:
  - ecological_interactions[4].description
  - ecological_interactions[4].evidence[0].explanation
  evidence_ids:
  - field
  - record
  - root-access
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml
    role: canonical_record
actions:
- action_id: fix-role-evidence-placement
  description: Attach source-attributed antagonism evidence to each corresponding
    taxon role.
  finding_ids:
  - role-evidence-placement
  target_ids:
  - CommunityMech:000373
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml
    role: canonical_record
  acceptance_checks:
  - Keep G12 linked to F. oxysporum and Y4/X25 to P. nicotianae, preserving attribution
    to the prior studies summarized by this article.
  - Retain current species/strain/habitat evidence; do not generalize every strain
    to every pathogen or invent direct mechanisms.
  - If original prior-study protocols are later cited, inspect them before adding
    stronger strain-specific claims.
  - Run references, schema and strict validation after separately authorized curation.
- action_id: fix-cultivation-context
  description: Use freshly verified complete Methods to represent the distinct cultivation
    and plant-assay settings without conflating preparation and outcome protocols.
  finding_ids:
  - cultivation-context
  target_ids:
  - CommunityMech:000373
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml
    role: canonical_record
  acceptance_checks:
  - Preserve the correctly scoped 30 C preparation block; the main-text numerical
    contexts have now been independently verified.
  - Keep 30 C/180 rpm inoculum preparation separate from 25 C/180 rpm/48 h co-cultivation
    measurement.
  - Represent glasshouse 25 +/- 2 C, 12 h:12 h light/dark, 70-80% RH and 21-day experiments
    separately from field cultivation.
  - Preserve field 10 mL per-plant root irrigation and two events seven days apart
    without extrapolating glasshouse conditions to field sites.
  - Move duplicated assembly prose to engineering_design and use environmental fields
    for actual setting conditions.
  - Do not fabricate LB formulation, exact CultureMech ID, assay inoculum details
    or unavailable field protocol information.
  - Attach exact main-article Methods evidence at each added context and run strict,
    term, reference and history checks plus regenerated-document checks after separately
    authorized curation.
- action_id: complete-source-assessment
  description: Complete the remaining supplementary S1–S5 figure assessment when publicly
    accessible, then save a new immutable review; full main Methods, Results and Figures
    1–11 are already assessed here.
  finding_ids:
  - role-evidence-placement
  - cultivation-context
  target_ids:
  - CommunityMech:000373
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml
    role: canonical_record
  acceptance_checks:
  - Inspect the actual supplementary plate photographs, disease/field images and pathway
    figure; captions alone are not the images. Retain this successor's bounded main-text
    and numeric verification.
  - Do not convert transcriptomic associations, nonsignificant genus shifts or IAA
    output into hormone mediation or persistent colonization.
  - Revisit sequencing-data release only when the source provides a real deposited
    accession.
  - No purchase, author contact, canonical edit or status promotion is authorized
    by this review.
- action_id: append-history-correction
  description: In separately authorized provenance curation, append a correction identifying
    the erroneous sidecar and actual 000373 edit; record the linked issue-body mismatch
    without rewriting old history.
  finding_ids:
  - history-edit-misattribution
  target_ids:
  - CommunityMech:000373
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: history/records/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom
    role: append_only_history
  acceptance_checks:
  - Name the exact October 21 sidecar and its incorrect 000449/Ralstonia/counter_selection
    claims; establish 000373 identity using target content and PMID 42388034.
  - Document removal of tobacco target_taxon from nodes 3 and 4 plus retained host
    descriptions; do not fabricate absent counter_selection or pathogen changes.
  - Preserve all original history bytes and verify the new corrective history with
    native validation.
  - Link a correction to the erroneous issue-body identity without treating issue
    closure as scientific evidence or changing grouped findings for unrelated targets.
- action_id: bound-field-yield-comparators
  description: Separate field disease-control comparators from middle-leaf estimated-yield
    comparisons in the node and its evidence explanation.
  finding_ids:
  - field-yield-comparator
  target_ids:
  - CommunityMech:000373
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml
    role: canonical_record
  acceptance_checks:
  - Preserve two-site natural-disease scope and commercial-product disease-efficacy
    comparison supported by Figure 9E.
  - State 41.33% and 37.54% dry-yield increases against the source control, preserving
    middle-leaf estimation and Figure 9D treatment arms.
  - Do not assert significant superiority over every single-strain yield arm. Distinguish
    any broader Discussion assertion from demonstrated commercial-product yield data
    unless additional directly supporting primary evidence is verified.
  - Attach endpoint-specific evidence, append history, and run reference, strict and
    generated-document checks after separately authorized curation.
limitations:
- Supplementary S1–S5 captions are inspected, but the DOCX download returned an HTML
  preparation/verification page; supplementary images remain unavailable. Main article
  and all 11 main figures were retrieved and assessed. No access-control bypass or
  paid retrieval was used.
- The selected committed cache remains incomplete despite its full-text separator.
  All 18 current snippets now independently match the complete primary HTML; no cache
  content was changed.
- No raw RNA-seq, amplicon data, figure digitization or statistical reanalysis was
  performed. Sequencing release restrictions and future deposition remain in the current
  article; the tobacco reference genome is not a study accession.
- Equal formulation membership is not persistent field dominance. Salkowski output,
  pooled-tissue expression associations and nonsignificant genus shifts do not establish
  metabolite mediation, member fitness, persistence or resilience. The existing colonization/mechanism
  discussion remains an evidence boundary, not a request to conduct experiments.
- The source's Figure 10(F) richness direction conflicts with its prose. This refresh
  does not adopt a directional richness claim, and none is encoded in the target;
  no correction to source raw data is inferred.
- Historical GTDB mapping counts/release were not recomputed. Optional adapter discovery
  is bounded to PATH and two exact sibling locations; the public catalog has no exact
  target dataset and no strain-module query was performed.
- The corpus network commands retain 44 warnings across 16 of 503 records, recorded
  as failed checks. The current target has no native network issues; grouped dispositions
  for other records were not reassessed.
notes:
- This is an author refresh, not independent approval. No canonical record, cache,
  history, schema or generated product was edited.
- Both original P3 issue keys and exact previous_occurrences remain open; the new
  history concern requires append-only follow-up outside this review-bundle PR.
- Direct excerpts retained from the original review total 15 words. Source snapshots
  and actual command receipts are pinned, and the initial repository input hashes
  were rechecked before final inspection.
- The original complete-source-assessment action is narrowed to still-uninspected
  supplementary material. The bounded host-target repair does not supersede the three-target
  Stage 4/5 finding lineage.
tags:
- record-review
- partial
- synthetic-community
- biocontrol
- batch-05
- pr-2039-refresh
```
