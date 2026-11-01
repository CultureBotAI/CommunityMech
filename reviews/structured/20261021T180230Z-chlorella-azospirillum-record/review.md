# Chlorella–Azospirillum source and assay-scope review

- Review: 20261021T180230Z-chlorella-azospirillum-record
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-21T17:51:54.498793Z
- Finished UTC: 2026-10-21T18:02:30.813766Z
- Reviewer: codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Full-source review supports the two members and the qualified four-node/two-arrow graph. Two major findings address generic medium composition/protocol conflation and stronger non-graph local-exchange/chemical-form assertions; one minor corrects historical strain-name provenance. Current claims are scientifically assessed with unread starch SI and source contradictions explicitly bounded.

## Scope And Provenance

Entire maintained record, each taxon/node/arrow and non-graph metadata assessed against three full scientific mains, all main figures, nutrient Table S1, exact strain authorities and current provenance.

Selection: Only released CommunityMech:000191 in the owned batch 10 checkout.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 95812d3412d5aab41fd03422340cf736ac7b56f3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000191 | kb/communities/Chlorella_Azospirillum_Synthetic_Mutualism.yaml | maintained | Chlorella-Azospirillum Synthetic Mutualism |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000191 | Schema passed. |
| validate-strict | passed | True | CommunityMech:000191 | Strict validation passed. |
| validate-terms | passed | True | CommunityMech:000191 | Term validation passed. |
| validate-gtdb | passed | True | CommunityMech:000191 | GTDB structure/coherence passed. |
| validate-gtdb-domain | passed | True | CommunityMech:000191 | Algal and bacterial GTDB applicability passed. |
| validate-history | passed | True | CommunityMech:000191 | History validation passed. |
| normalize-cache-names-check | passed | True | CommunityMech:000191 | Read-only cache filename check passed. |
| validate-references-explained | passed | True | CommunityMech:000191 | Native references pass against unchanged source-specific caches; fresh scientific checks separately verify excerpt context. |
| audit-network | failed | True | CommunityMech:000191 | Fresh batch 10 corpus diagnostic retains unrelated warnings; this focal graph separately reports COMPLETE. |
| check-network-quality | failed | True | CommunityMech:000191 | Fresh batch 10 corpus diagnostic retains unrelated warnings; this focal graph separately reports COMPLETE. |
| Main and current-claim-critical source verification | passed | True | CommunityMech:000191 | All three scientific mains, all 17 main figures, both main tables and complete nutrient Table S1 were assessed. Unread starch SI does not carry an exact current numerical claim being certified. |
| Fresh reference-specific excerpt checks | passed | True | CommunityMech:000191 | All 32 excerpts are supported: 31 strict fresh matches and one documented FEMS unit projection; cache comparison has a separate sentence-initial capitalization projection. |
| Starch supplementary Table S1 and Figure S1 | unavailable | False | CommunityMech:000191 | The exact supplemental growth-rate table and bacterial growth panels remain unread after ordinary DOI/API/publisher discovery. Main text and figures support the bounded current claims; no precise SI-only bacterial growth value is certified. |
| Exact source-linked publication and strain context | passed | True | CommunityMech:000191 | Bibliography, actual nutrient supplement and predecessor/current-catalogue identity were checked with their precise scopes. No dedicated study archive or cross-Mech mapping is invented. |
| Raw data and experimental reproduction | skipped | False | CommunityMech:000191 | No raw data analysis, statistical retest, code execution, experimental reproduction or inferred source-error correction. |
| Optional structured source adapter | unavailable | False | CommunityMech:000191 | Availability is bounded by the frozen runtime-discovery receipt; inspected public primary sources and authorities supplied the necessary review evidence. |

## Scientific And Domain Assessments

### Community, member and strain identity

identity: supported. Targets: CommunityMech:000191.

Retain the synthetic laboratory pair and current focal species/strains.

UTEX 2714 and Cd/DSM 1843 are directly supported. The old C. vulgaris name refers to the same algal accession in the specifically inspected predecessor. Its bacterial DSM number is inconsistent with current catalogue identity and must remain attributed. Do not widen the roster to Sp6/SpM7918 comparators, invent natural coisolation or change the explicitly scoped species-name GTDB block.

### Both taxonomy functional_role lists and narrow evidence

evidence: supported. Targets: CommunityMech:000191.

Retain broad roles with source-specific evidence and physiological context.

Algal primary production is applicable to illuminated cultures, not a claim of photosynthesis in the dark glucose assay. The bacterial algal-resource use and source-described reciprocal metabolic/signaling interpretation support qualified roles. Attach actual exudate, supplementation and response evidence instead of expecting membership-only snippets to establish a mechanism. No exact local flux, algal IAA catabolism, obligate syntrophy or energetic product-removal requirement is introduced.

### ecological_interactions[0]: Nutrient-Modulated Synthetic Mutualism

evidence: supported. Targets: CommunityMech:000191.

Retain condition- and time-specific mutualism with its exceptions.

The 12-hour initial nutrient shift and later common SGM phase are explicit. Neither general population benefit nor starch accumulation is universal across treatments; the current node already preserves the later NB bacterial comparison.

### ecological_interactions[1]: Tryptophan, Thiamine, and IAA Exchange

evidence: supported. Targets: CommunityMech:000191.

Retain the PARTIAL exudate/supplement-based exchange interpretation.

The node already distinguishes thiamine diphosphate supplementation from an unmeasured extracellular chemical form, and bulk non-detection from proposed bead-local exchange. IPDC activity is not uniquely bacterial or specific to IAA. Do not upgrade to a directly measured flux or automatically replace the metabolite term with TPP as the secreted species.

### ecological_interactions[1].downstream[0]

evidence: supported. Targets: CommunityMech:000191.

Retain PARTIAL cross-study IAA mediation of starch/AGPase responses.

The dark glucose-fed assay and synthetic IAA comparator support mediation, while SpM7918 is derived from Sp6 rather than Cd. Exact-Cd necessity and local resource-transfer contribution remain unresolved. Do not equate starch yield with mutual growth or recast the comparator as a focal member.

### ecological_interactions[2]: Co-Immobilization and Cell Aggregation

evidence: supported. Targets: CommunityMech:000191.

Retain observed organization without a colonization-facilitation type.

Investigators create the beads; microscopy shows condition-dependent mixed aggregates. The current node separates that physical organization from a proven partner-caused colonization mechanism.

### ecological_interactions[2].downstream[0]

evidence: supported. Targets: CommunityMech:000191.

Retain HYPOTHESIZED aggregation-to-growth mediation.

No selective proximity intervention establishes necessity. Observed growth and aggregation can be described without upgrading their causal relationship or introducing additional arrows.

### ecological_interactions[3]: IAA-Linked Starch Accumulation Response

evidence: supported. Targets: CommunityMech:000191.

Retain the untyped physiological response with dark-assay and strain limits.

AGPase/starch/glucose uptake responses are measured, whereas direct AGPase regulation remains a proposed pathway. Most paired algal-growth comparisons decrease and the Cd N-starvation correlation is nonsignificant. Main figures and text suffice for current claims; exact unread bacterial SI growth trends are not certified.

### Engineering, ingredient and resource exchange wording

evidence: concern. Targets: CommunityMech:000191.

Carry the graph’s chemical-form and local-transfer qualifications into non-graph fields.

Measured algal exudates, bacterial utilization, TPP supplementation, bulk nondetection and inferred local transfer are different evidence classes. The current related_ingredients thiamine/IAA prose and general exchange-measurement descriptions collapse these distinctions. Preserve broad source conclusions as attributed interpretation rather than direct endogenous-form or flux identification.

### growth_media and cultivation-related environmental_factors

evidence: concern. Targets: CommunityMech:000191.

Replace the generic Trp/IAA composition with stage- and assay-specific source conditions.

Trp is added in bacterial controls and IAA in an algal comparator, rather than universally to the pair. The three papers distinguish preculture, bead recovery, initial nutrient treatments, later SGM and dark glucose-fed assays. Recover the available conditions without conflating 2/3/3–4 mm beads, 12/24-hour stages, contradictory flask fills, assay versus analytical pH, or nutrient-table gluconate versus starch-paper glycerol. Printed units must be visually verified when PDF extraction is unreliable.

### State, origin, category and environment

identity: supported. Targets: CommunityMech:000191.

Keep the synthetic engineered laboratory context and scope condition descriptions.

Laboratory environment and the broad algal community category fit the intended system. Bead construction is cultivation setup, and illumination/aerobic conditions require study-specific labels so dark starch assays do not inherit illuminated growth conditions. Empty metal/REE fields and NOT_APPLICABLE remain appropriate for the encoded biological scope.

### Publication and historical identity context

provenance: concern. Targets: CommunityMech:000191.

Correct the historical different-species explanation; retain verified publication resources.

The same UTEX accession is explicitly reported under the older name. Preserve the source DSM 7030 discrepancy and focal DSM 1843 authority without claiming a verified bacterial alias. No dataset-absence defect or invented CultureMech mapping follows from the empty datasets list.

### Current issue ownership and excerpt scope

provenance: supported. Targets: CommunityMech:000191.

Use existing issue 1297 and preserve the resolved FEMS cache-scope correction.

All 32 occurrences have source support, with explicit unit and capitalization projection boundaries rather than a false all-strict claim. Closed issue 1295 and the exact historical decision certify only their prior scope. The current cache label is already corrected; no duplicate issue or full restricted-body cache import is authorized.

### Native checks and immutable workflow

schema: supported. Targets: CommunityMech:000191.

Eight focused checks pass; scientific review confirms three non-graph findings.

Canonical, caches, history and generated products remain unchanged. Persistence is limited to a new immutable review bundle. Completed scientific review concerns the current encoded claims and does not imply full inspection of unavailable ancillary SI or raw data.

### Native mechanical scores

completeness: supported. Targets: CommunityMech:000191.

Completeness 95 and quality 100/raw 113 are mechanical metrics.

## Findings

### assay-specific-media: Separate measured metabolites and assay-specific supplements from basal medium

major / open / confirmed; issue key: cm-000191-assay-specific-media.

The generic composition lists Trp and IAA as common coculture ingredients although the studies use distinct precursor/cofactor bacterial controls and synthetic IAA algal comparators. The same generic block omits recoverable source-specific precursor culture, recovery, initial nutrient-shift and dark glucose-fed conditions. The attached abstract snippets cannot establish a unified recipe.

### nongraph-exchange-scope: Qualify local exchange and exact cofactor-form assertions outside the graph

major / open / confirmed; issue key: cm-000191-nongraph-exchange-scope.

Related-ingredient and general measurement/resource prose presents endogenous thiamine and local metabolite exchange as directly established. The sources distinguish exudate use and Trp plus TPP supplementation from bulk coculture non-detection and inferred bead-local transfer. Correct these claims and their evidence attachment without removing the supported broad roles or already qualified graph.

### historical-strain-provenance: Reconcile the predecessor’s historical algal name and culture-number conflict

minor / open / confirmed; issue key: cm-000191-historical-strain-provenance.

The predecessor explicitly reports UTEX 2714 under C. vulgaris, while focal sources call the same accession C. sorokiniana, formerly C. vulgaris. The different-Chlorella-species explanation is misleading. Its reported Cd/DSM 7030 conflicts with current catalogue identity and cannot be silently treated as DSM 1843 or as proof that an unrelated bacterium was studied.

## Recommended Actions And Acceptance Checks

### separate-cultivation-contexts

Recover exact study- and stage-specific culture representations.

- Remove the generic implication that Trp and IAA are universal basal ingredients. Represent Trp 1.5 µg/mL with or without thiamine diphosphate 70 ng/mL only in the FEMS bacterial control/supplement conditions, and synthetic IAA only in its distinct algal comparator. Keep measured or proposed exchanged metabolites in their appropriate biological context.
- Separate 2018 C30 algal and BTB-2 bacterial precultures from the 12-hour NB/OAB/SGM comparison and subsequent common SGM phase through 83 hours. Record source-supported 27±2 C, 140 rpm and 60 µmol photons/m²/s for the illuminated assay. Scope 32±2 C, 120 rpm and 16 hours to bacterial preculture, and seven days to algal preculture.
- Represent 2018 3 mm beads and 20 g/150 mL Methods separately from its 100 mL/250 mL statistics statement; preserve NB 10% v/v versus figure 10% w/v as an unresolved source presentation difference. Do not silently choose one value or infer SGM is N-free: its Methods includes NH4Cl 191 mg/L.
- Represent the FEMS 2 mm bead, 24-hour recovery and 120-hour exudate/supplement experiments separately. Preserve its Methods 20 g/150 mL versus statistics 300 mL/500 mL and counting-section 250 mL flask references. Do not transfer the separate algal exudate assay’s 120 rpm to all 140 rpm experiments.
- Represent the starch assay as 3–4 mm beads, 24-hour NB or OAB recovery, 12 g/150 mL in 250 mL flasks, glucose 10 g/L and N-replete versus no-added-ammonium SGM arms, dark aerobic conditions at 27±2 C and 140 rpm. Preserve Methods 96 hours versus displayed 120-hour endpoints. Use printed 47.5 ng/µL in section 2.3 and 48 ng/µL in section 2.6 as attributed synthetic-IAA statements; do not reproduce the text-extraction ng/mL error.
- Read source medium rows and hydrate/unit strings before populating quantities. Nutrient Table S1 uses BTB-2 gluconate whereas the starch paper uses glycerol; their common name does not justify recipe merging. pH 8 is analytical bead dissolution and starch BTB-2 pH 7 is bacterial preculture, not a universal coculture setpoint. No numerical culture pH or salinity should be invented.
- Move bead setup information to an appropriate cultivation/experimental description and keep environmental light/aerobic statements explicitly scoped. Attach short, exact source evidence and precise section/figure/table locators to each recovered condition. Preserve rights-restricted source bodies outside the repository; do not merge three full texts into one cache or invent a cross-Mech medium ID.

### qualify-nongraph-exchange

Align ingredient, design, resource and role evidence with measured versus inferred processes.

- Distinguish measured algal Trp release, bacterial exudate use and Trp-plus-TPP supplementation from inferred local transfer in co-immobilized cultures. State bulk coculture Trp/IAA non-detection and its analytical limit where relevant; absence from bulk medium does not prove or disprove local transfer.
- Qualify related_ingredients thiamine/IAA relevance and explanations, engineering measurement language and the FEMS external-resource description. The supplemented chemical is thiamine diphosphate, but the endogenous extracellular form is not identified by that intervention; do not automatically substitute a TPP ontology ID as the secreted species.
- Attach narrow source evidence to the retained functional roles. Preserve primary production in illuminated context, bacterial use of algal resources and source-qualified reciprocal metabolic/signaling interpretation. Do not impose a new obligacy, thermodynamic-removal or carbon-assimilation definition, and do not infer algal IAA catabolism from a response assay.
- Preserve all four nodes and two downstream arrows, including PARTIAL IAA-to-starch support and HYPOTHESIZED aggregation-to-growth mediation. Keep IPDC specificity/taxon limits, Sp6-derived mutant versus focal Cd, dark glucose assay versus illuminated growth, nonsignificant Cd N-starvation correlation and starch-versus-fitness distinctions explicit.
- Use current open issue 1297 for this non-graph follow-up and preserve closed 1295 graph-repair history. The FEMS selected-excerpt cache label is already corrected; do not reopen it as an unresolved abstract-only defect or create a duplicate issue.

### correct-historical-resource-context

Correct the predecessor identity explanation while preserving unresolved source attribution.

- Replace the categorical different-Chlorella-species explanation with the directly verified same UTEX 2714 accession under historical C. vulgaris naming and focal C. sorokiniana designation. This applies to the inspected predecessor, not every historical paper using the old name.
- Preserve that the predecessor reports Cd as DSM 7030 and that the current catalogue for that number is unrelated to Cd. Do not silently correct the paper, claim an alias, infer its actual organism was Paenibacillus, or alter the focal verified Cd/DSM 1843 assignment.
- Keep predecessor bibliography and the exact identity paragraph as bounded context. Do not transfer its protocol, population effects or mechanisms into the three focal assays. No dedicated dataset accession or CultureMech mapping is invented from resource-name similarity.

### validate-authorized-curation

When a separate curation task is authorized, preserve provenance and run the native completion gates.

- Apply only separately authorized maintained-input corrections, append a fresh curation-history entry, and retain source/version/locator and existing issue ownership. Recheck every changed scientific claim against its exact source rather than merely matching its snippet.
- Run the documented focused schema, strict, term, GTDB/domain, reference, cache-name and history checks. Verify the four-node/two-arrow graph and preserve the existing evidence-support qualifiers; report any remaining unavailable source or unresolved source contradiction.
- After canonical curation, run just gen-html and just check-docs-current with the required project environment, inspecting generated changes for the intended record. This review performs no canonical, source-cache, history or generator mutation; persistence is limited to its new immutable review bundle.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | kb/communities/Chlorella_Azospirillum_Synthetic_Mutualism.yaml; Entire maintained YAML, both taxa, all four nodes and both downstream arrows | supports | The graph preserves study-specific nutrient, local-transfer, aggregation and starch-response limits. The generic medium, non-graph exchange language and historical-resource explanation retain distinct curation debt. |
| identity | PMID:30397795; doi:10.1007/s00248-018-1282-1; Materials and Methods: Microorganisms and Preparation of Initial Inoculum; Introduction | supports | The focal pair is C. sorokiniana UTEX 2714, formerly designated C. vulgaris, with A. brasilense Cd, DSM 1843. The authors deliberately assemble the two organisms in alginate beads and distinguish their individual habitats. Synthetic origin and engineered state are supported; no natural coisolation is implied. Sp6 and its derivative SpM7918 in the starch paper are comparator strains, not extra members of this Cd record. |
| nutrient-growth | PMID:30397795; doi:10.1007/s00248-018-1282-1; Results: Growth and Metabolite Production Using Rich Medium (Diluted Nutrient Broth) During the Initial Growth Phase; corresponding N-Free OAB and C-Free SGM subsections; Figures 1–4 | supports | The first 12 hours compare diluted NB, N-free OAB and C-free SGM, followed by SGM in every treatment. Population benefits depend on treatment and time. Following NB, later bacterial counts are not significantly different between single and paired immobilization. Continuous C-free SGM gives the highest early starch concentration in algae alone. The current conditional mutualism node correctly preserves these exceptions. |
| aggregation | PMID:30397795; doi:10.1007/s00248-018-1282-1; Results: Dynamics of Aggregation Between Cells of C. sorokiniana and A. brasilense During Different Initial Nutritional Conditions; Figures 5–7; Discussion | supports | Microscopy shows mixed-cell organization within investigator-made beads. Initial N-free attachment weakens later, whereas large C-free aggregates develop at 83 hours. The study does not selectively disrupt proximity to establish that aggregation causes the growth benefit. Retain the untyped organization node and its HYPOTHESIZED downstream link, rather than converting bead assembly into partner-mediated colonization. |
| cultivation-nutrients | PMID:30397795; doi:10.1007/s00248-018-1282-1; Materials and Methods: Microorganisms and Preparation of Initial Inoculum; Immobilization in Alginate of Microorganisms; Experimental Culture Conditions; Experimental Design and Statistical Analysis; Figure 1 | supports | Algal C30 preculture is 10 mL inoculum into 90 mL, seven days at 27±2 C, 140 rpm and 60 µmol photons/m²/s; bacterial BTB-2 preculture is 32±2 C, 120 rpm for 16 hours. Experimental beads are 3 mm, formed with 2% alginate. Methods specifies 20 g beads in 150 mL, first 12 hours in NB/OAB/SGM, three saline washes and transfer to SGM through 83 hours at 27±2 C, 140 rpm and the same illumination. The statistics subsection instead says 100 mL in 250 mL flasks; retain this source conflict. NB is 10% v/v in Methods but 10% w/v in Figure 2. SGM contains NH4Cl 191 mg/L, so C-free does not mean nitrogen-free. Citrate pH 8 is bead dissolution, not a culture setpoint. |
| nutrient-si | PMID:30397795, electronic supplementary Table S1; Complete DOCX table: Media used in this study for initial cultivation of microorganisms | supports | The publisher-linked table identifies C30 for UTEX 2714 and BTB-2 for Cd/DSM 1843. C30 prints KNO3 25, MgSO4·7H2O 10, KH2PO4 4, K2HPO4 1 and FeSO4·7H2O 1 g/L, with trace compounds in µg/L. BTB-2 contains gluconate, tryptone and yeast extract at 5 g/L each, plus its stated salts. These are preculture formulations. The starch-paper BTB-2 instead lists glycerol 8 mL; do not silently merge the recipes or normalize the printed units from another standard medium. |
| exudate-supplement | PMID:27090758; doi:10.1093/femsec/fiw077; Materials and Methods: Experimental culture conditions; Results: Tryptophan consumption and IAA production by A. brasilense; Figure 2; Discussion | supports | Bacterial cultures grown in algal exudates or SGM supplemented with tryptophan plus thiamine diphosphate produce IAA; tryptophan alone does not reproduce that response. The tested supplement is a phosphorylated cofactor, not direct identification of the secreted extracellular thiamine form. Algal Trp release and bacterial use are supported, while the chemical-form and local-coculture claims require qualification. |
| local-transfer | PMID:27090758; doi:10.1093/femsec/fiw077; Results: Tryptophan consumption and IAA production by A. brasilense; IPDC activity; Expression of the ipdC gene; Figures 2,4–5; Discussion | supports | In co-immobilized cultures neither Trp nor IAA is detected in bulk SGM. The authors infer local transfer from exudate/supplement effects, growth and enzyme/expression observations. They discuss non-specific IPDC substrates and an algal contribution. This supports the existing PARTIAL interpretation, not direct measurement of endogenous molecule-resolved flux or unique bacterial IPDC activity. The source also contains P-sign/relative-expression presentation inconsistencies; no quantitative expression recalculation is attempted. |
| cultivation-exchange | PMID:27090758; doi:10.1093/femsec/fiw077; Materials and Methods: Microorganisms and initial growth conditions in prior experiments; Immobilization of microorganisms; Experimental culture conditions; Experimental design and statistical analysis | supports | The illuminated FEMS study uses 2 mm beads, an initial 24-hour recovery, and a reported 20 g beads in 150 mL SGM assay at 27±2 C and 140 rpm for 120 hours. Bacterial controls receive Trp 1.5 µg/mL alone or with thiamine diphosphate 70 ng/mL, or filtered three-day algal exudates. These are separate conditions, not a mandatory Trp/IAA basal recipe. Statistics instead describes 300 mL in 500 mL flasks; the counting section refers to 250 mL flasks. Preserve attribution rather than invent a single vessel/fill. The separate algal exudate experiment uses 120 rpm, distinct from the main 140 rpm assay. |
| primer-context | PMID:27090758; doi:10.1093/femsec/fiw077; Materials and Methods: RNA isolation, cDNA synthesis and quantitative Real Time PCR; Table 1 | supports | The source-reported NC016617.1 is a primer-design reference sequence. Table 1 is a primer inventory. Neither is a new experimental archive deposition or independently verified exact Cd genome here. No gene-level community annotation, genome identity or missing-data finding is inferred from that identifier. |
| starch-mechanism | PMID:26924113; doi:10.1016/j.resmic.2016.02.005; Results 3.1–3.4; Figures 1–5 and Table 1; Discussion | supports | Wild-type Cd and Sp6 pairs show stronger starch/AGPase responses than the Sp6-derived IAA-attenuated SpM7918 comparator; synthetic IAA gives a transient response. This supports partial IAA mediation under dark glucose-fed conditions. It does not establish Cd-specific genetic necessity or direct regulation of AGPase instead of altered glucose uptake. The Cd Trp/IAA correlation under N starvation is nonsignificant, despite broader discussion language. Most paired algal population comparisons decrease, so starch accumulation is not reciprocal growth or fitness. |
| cultivation-starch | PMID:26924113; doi:10.1016/j.resmic.2016.02.005; Materials and methods 2.1 Microorganisms and initial growth conditions; 2.2 Immobilization of microorganisms; 2.3 Experimental culture conditions; 2.6 Experimental design and statistical analysis; printed pages 368–370 | supports | The starch experiment uses 3–4 mm beads with 24-hour NB or N-free OAB recovery, three saline washes, and 12 g beads in 150 mL SGM in 250 mL flasks. SGM contains glucose 10 g/L, with NH4Cl 191 mg/L for the N-replete arm and without added NH4Cl for the starved arm. The assay is dark, aerobic, 27±2 C and 140 rpm. Section 2.3 states 96 hours but Results/figures extend to 120 hours. The synthetic IAA comparator dose is printed 47.5 ng/µL in section 2.3 and 48 ng/µL in section 2.6; PDF text extraction corrupts µL to mL. The visual source governs. BTB-2 pH 7 applies to bacterial preculture, not every coculture. Analytical extraction pH/temperature is not cultivation. |
| starch-unit-visual | PMID:26924113, author PDF; Printed page 369, section 2.3; independent visual check against pages 368 and 370 | supports | The rendered page explicitly prints the 47.5 ng/µL synthetic IAA supplement. The text extractor substitutes m for the micro-prefix in several units. Page 370 prints 48 ng/µL, and figure axes use their separately printed µg/mL. Do not copy the corrupted extraction or silently reconcile source concentrations. |
| predecessor | PMID:10742237; doi:10.1128/AEM.66.4.1527-1531.2000; MATERIALS AND METHODS: organism-identity paragraph, bounded historical context | supports | The predecessor explicitly reports C. vulgaris UTEX 2714. The focal papers identify that same algal accession as formerly C. vulgaris, so the record should not claim a different Chlorella species solely from the historical name. The old source calls Cd DSM 7030; direct current catalogue identity is unrelated to Cd, so retain this unresolved source-number conflict. Focal Cd/DSM 1843 remains independently supported. Only predecessor bibliography/abstract and this identity paragraph were assessed, not its whole experimental science. |
| schema | src/communitymech/schema/communitymech.yaml; FunctionalRoleEnum; growth_media/composition; CommunityOriginEnum and EcologicalStateEnum | supports | The role enum permits broad source-qualified metabolic cooperation; do not impose a new obligacy, energetic-removal or strict carbon-assimilation criterion. A structured medium composition denotes ingredients of the scoped medium, not merely metabolites detected in an experiment. Synthetic assembly and engineered state fit this laboratory pair; quantitative cultivation details require stage-specific evidence. |
| ontology | ontology-authority.json; Whole frozen receipt and its declared scope | supports | All 12 distinct encoded ontology pairs match across 31 occurrences. CHEBI:18385 identifies thiamine(1+), distinct from thiamine diphosphate; correct label matching does not determine which extracellular form was present. |
| semantics | ontology-semantic-notes.json; Whole frozen receipt and its declared scope | supports | Exact schema and ontology definitions support retaining the broad roles and qualified graph. The medium/composition and non-graph chemical-form assertions need source-specific repair; no narrower functional-role requirement or new taxon is imposed. |
| gtdb | child-gtdb-crosswalk.json; Whole frozen receipt and its declared scope | supports | The bacterial block matches its explicitly disclosed exact species-name fallback: no NCBI 192 row, one species-name row keyed to FP2/1262469, two genomes and fraction 1.0. This does not classify Cd genomically. Algal NO_GTDB_EQUIVALENT is appropriate. |
| catalogues | child-strain-catalogue-authority.json; Whole frozen receipt and its declared scope | supports | DSM 1843 directly confirms Cd and ATCC 29710. UTEX 2714 retains an old C. vulgaris heading but explicitly notes that this identification is incorrect and links a reidentification paper. The focal source naming is preserved; catalogue maintenance conditions are not assay conditions. |
| historical-number | child-predecessor-catalogue-discrepancy.json; Whole frozen receipt and its declared scope | supports | Current DSM 7030 identifies Paenibacillus larvae type strain 846, not a verified Cd alias. Do not infer that the predecessor used this unrelated organism or replace the focal DSM 1843 identifier. |
| historical-context | predecessor-strain-context.json; Whole frozen receipt and its declared scope | supports | The exact predecessor and focal identity paragraphs establish the historical UTEX name correspondence while preserving the unresolved bacterial culture-number conflict. No whole predecessor source review or protocol transfer is claimed. |
| resources | dataset-verification.json; Whole frozen receipt and its declared scope | supports | The four publications and two taxonomy links are correctly external resources. Nutrient Table S1 is a verified source medium table. Starch SI remains unread; no distinct new deposition or cross-Mech mapping is established by bounded source-resource checks. This does not imply global data absence. |
| snippets | snippet-audit.json; Whole frozen receipt and its declared scope | supports | All 32 excerpt occurrences are source-supported: 31 strict fresh matches plus one explicit FEMS unit typography projection. Cache comparison separately has 31 strict matches plus one sentence-initial capitalization projection. Excerpt validity does not make surrounding claims correct. |
| history | provenance-audit.json; Whole frozen receipt and its declared scope | supports | The sole history and exact prior decision preserve graph-repair context, not full certification. Current issue 1295 is closed/completed with one comment; issue 1297 is open with no comments and owns the non-graph protocol/exchange/historical-name follow-up. FEMS cache scope has already been corrected to selected abstract and Methods excerpts. |
| metrics | support-audit.json; Whole frozen receipt and its declared scope | supports | Native COMPLETE covers four nodes, two arrows and eight node-evidence entries. Completeness is 95. Two major and one minor findings give raw quality 113, capped at 100; no role or dataset is invented for score credit. |
| lead-read | lead-primary-read-scope.json; Whole frozen receipt and its declared scope | supports | Lead read all three scientific mains, all 17 main figures, both main Table 1 inventories and every nutrient Table S1 cell. Starch SI Table S1/Figure S1 remain unread; exact bacterial SI curves/rates are not certified. Predecessor read scope is bounded identity context. |
| source-scope | source-audit.json; Whole frozen receipt and its declared scope | supports | Frozen current-claim source assessment records two major and one minor findings, retained broad roles/four nodes/two arrows, detailed assay distinctions and exact source limitations. |
| root-source | root-independent-source-audit.json; Whole frozen receipt and its declared scope | supports | Root independently read the three scientific mains, all 17 main figures, both main tables, nutrient Table S1 and historical identity/catalogue context. It agrees with completed current-claim review and the three findings; starch SI limitations remain explicit. |
| auxiliary | auxiliary-frozen-manifest.json; Whole frozen receipt and its declared scope | supports | All eight focused native checks pass, all 27 official inputs remain unchanged, and the initial and final validator summaries are separate immutable files. Native and authority success do not certify biological mechanisms. |
| adapter | adapter-check.json; Whole frozen receipt and its declared scope | supports | Optional structured-adapter discovery is bounded to the recorded runtime. No paid provider, credentials or unapproved external execution was used. |
| check-validate | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src just --no-dotenv validate kb/communities/Chlorella_Azospirillum_Synthetic_Mutualism.yaml; Actual execution 2026-10-21T17:52:36.127155+00:00 to 2026-10-21T17:52:37.843903+00:00 | supports | Schema passed. |
| check-validate-strict | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src just --no-dotenv validate-strict kb/communities/Chlorella_Azospirillum_Synthetic_Mutualism.yaml --out /private/tmp/cm-review-session/batch-10/000191/strict-report.tsv; Actual execution 2026-10-21T17:52:36.146204+00:00 to 2026-10-21T17:52:41.021681+00:00 | supports | Strict validation passed. |
| check-validate-terms | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src just --no-dotenv validate-terms kb/communities/Chlorella_Azospirillum_Synthetic_Mutualism.yaml; Actual execution 2026-10-21T17:52:36.151417+00:00 to 2026-10-21T17:52:40.131241+00:00 | supports | Term validation passed. |
| check-validate-gtdb | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src just --no-dotenv validate-gtdb kb/communities/Chlorella_Azospirillum_Synthetic_Mutualism.yaml; Actual execution 2026-10-21T17:52:37.844488+00:00 to 2026-10-21T17:52:38.028489+00:00 | supports | GTDB structure/coherence passed. |
| check-validate-gtdb-domain | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src just --no-dotenv validate-gtdb-domain kb/communities/Chlorella_Azospirillum_Synthetic_Mutualism.yaml; Actual execution 2026-10-21T17:52:38.028825+00:00 to 2026-10-21T17:52:41.473755+00:00 | supports | Algal and bacterial GTDB applicability passed. |
| check-validate-history | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src just --no-dotenv validate-history history/records/Chlorella_Azospirillum_Synthetic_Mutualism; Actual execution 2026-10-21T17:52:40.131655+00:00 to 2026-10-21T17:52:41.717310+00:00 | supports | History validation passed. |
| check-normalize-cache-names-check | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src uv run python scripts/normalize_cache_names.py --check; Actual execution 2026-10-21T17:52:41.720248+00:00 to 2026-10-21T17:52:41.808206+00:00 | supports | Read-only cache filename check passed. |
| check-validate-references-explained | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src just --no-dotenv validate-references-explained kb/communities/Chlorella_Azospirillum_Synthetic_Mutualism.yaml; Actual execution 2026-10-21T17:52:41.808706+00:00 to 2026-10-21T17:52:43.552878+00:00 | supports | Native references pass against unchanged source-specific caches; fresh scientific checks separately verify excerpt context. |
| check-audit-network | PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv audit-network; Actual execution 2026-10-21T17:04:17.819938+00:00 to 2026-10-21T17:04:25.370848+00:00 | supports | Fresh batch 10 corpus diagnostic retains unrelated warnings; this focal graph separately reports COMPLETE. |
| check-check-network-quality | PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv check-network-quality; Actual execution 2026-10-21T17:04:17.819995+00:00 to 2026-10-21T17:04:26.163649+00:00 | supports | Fresh batch 10 corpus diagnostic retains unrelated warnings; this focal graph separately reports COMPLETE. |

## Limits And Additional Notes

- Completed scientific review is bounded to current encoded claims. All three scientific main texts, all 17 main figures, both main Table 1 inventories and every nutrient Table S1 cell were inspected. Starch supplementary Table S1 and Figure S1 remain unread after ordinary source discovery; no exact SI-only bacterial growth curve/rate is certified.
- The predecessor source was assessed only for title/abstract and the complete organism-identity Methods paragraph. The same UTEX 2714 historical name is established, but the reported Cd/DSM 7030 number remains inconsistent with current catalogue identity. Focal DSM 1843 is independently verified. No older protocol is imported.
- Exudate use and cofactor supplementation are experiments; precise bead-local transfer and the extracellular thiamine species are inferences or unresolved. IPDC has other substrates and an algal contribution. Broad retained roles do not imply direct local flux, a strict trophic-assimilation test, obligatory syntrophy or algal IAA catabolism.
- The illuminated nutrient study has source conflicts in 150 versus 100 mL fill and NB dilution basis. FEMS has 150 versus 300 mL assay descriptions and different flask references. Starch Methods specifies 96 hours while Results/figures extend to 120 hours. These are reported with source attribution, not merged into a fabricated common protocol.
- Starch printed Methods IAA dose is 47.5 ng/µL, with 48 ng/µL in statistics. PDF extraction incorrectly renders the micro-prefix as m; the page images were inspected directly. Figure axes have independently printed µg/mL. Source C30 macro/trace units and nutrient BTB-2 gluconate versus starch BTB-2 glycerol are preserved rather than normalized using external standard recipes.
- Analytical bead-dissolution pH 8, extraction buffers and enzyme assay temperatures are not culture setpoints. Precursor cultivation and bead recovery differ from the final experiments. Initial N-free OAB, later ammonium-containing SGM and no-added-ammonium dark assays must remain distinct.
- The source FEMS significance prose includes P&gt;0.05 alongside significance statements, while captions specify P&lt;0.05; its transformed-expression axis includes negative values. The starch narrative overgeneralizes the Cd N-starvation correlation and compares a Sp6-derived mutant. These source presentation/mechanism limits are retained without new statistical or causal reanalysis.
- All 32 snippets are source-supported, with 31 strict fresh matches and one documented FEMS unit typography projection. Cache matching separately has one sentence-initial capitalization projection. The FEMS cache is correctly labeled selected abstract and Methods excerpts; it is not a full main cache. The other caches remain their actual bounded contents.
- The GTDB species-name fallback is correctly disclosed and matches the local authority, but does not classify the focal Cd genome. UTEX catalogue heading and explicit reidentification note must be read together. No new exact-strain taxonomy, chemical-form identity or cross-Mech recipe equivalence is inferred.
- Resource discovery is bounded to the cited source statements and exact publisher assets. No dedicated new study-deposition accession was established, which is not proof that data do not exist. The reported primer reference is not certified as a Cd genome or new community dataset. No raw payloads, experimental replication or code analysis was performed.
- All eight focused native checks pass and all 27 official inputs remain unchanged. Corpus-wide nonzero diagnostics retain their wider warning scope. Completeness 95 and quality 100/raw 113 do not erase the two major and one minor findings. No canonical, cache, history, generated or previously saved artifact was changed; no paid provider or author contact was used.
- All 27 official inspected inputs remain unchanged; no canonical, cache, history, generated or previously saved artifact was edited.
- Lead and root independently assessed all three scientific mains and all 17 main figures with exact supplemental/historical scopes. Child owns immutable native/ontology receipts; sibling owns provenance/resources/snippets and score arithmetic.
- Two major and one minor findings give raw quality 113/capped 100; completeness is 95. Current open issue 1297 owns the follow-up. The existing graph and broad source-qualified roles are retained.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T180230Z-chlorella-azospirillum-record
kind: record
repository: CultureBotAI/CommunityMech
title: Chlorella–Azospirillum source and assay-scope review
started_at: '2026-10-21T17:51:54.498793Z'
finished_at: '2026-10-21T18:02:30.813766Z'
reviewer:
  identity: codex
  kind: agent
  independence: unknown
  independence_basis: Separate agents assessed primary science, auxiliary authorities
    and provenance; no person-level independence is asserted.
skill: review-yaml-record
completion: completed
verdict: needs_curation
scientific_review: true
summary: Full-source review supports the two members and the qualified four-node/two-arrow
  graph. Two major findings address generic medium composition/protocol conflation
  and stronger non-graph local-exchange/chemical-form assertions; one minor corrects
  historical strain-name provenance. Current claims are scientifically assessed with
  unread starch SI and source contradictions explicitly bounded.
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
  - path: history/records/Chlorella_Azospirillum_Synthetic_Mutualism/2026-10-05T201241Z-codex-e557e4.yaml
    sha256: f5c7264c2d5b881762466a86be4a2881ac67717b2874d1587d35c2cb3b5a3f52
    role: context
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: kb/communities/Chlorella_Azospirillum_Synthetic_Mutualism.yaml
    sha256: 8debe22be0e21c034886b7e6e616bd3cc2a940a8bcdb7276c4235435c499e381
    role: target
  - path: references_cache/doi_10.1007_s00248-018-1282-1.md
    sha256: e5dd25e85b7833da8ee1a4c8df58f924c89ddcc98896b52c1c0f12691050b001
    role: context
  - path: references_cache/doi_10.1016_j.resmic.2016.02.005.md
    sha256: fe965f8411f7d365d8340afbd92e78d1fb92aff4c3b231c0c291311d66625236
    role: context
  - path: references_cache/doi_10.1093_femsec_fiw077.md
    sha256: 6db40ae92f46a1263a2fd3845639a63a2ac8a2c1bacea41eee7ea3dc0be1d6ac
    role: context
  - path: references_cache/doi_10.1128_AEM.66.4.1527-1531.2000.md
    sha256: 1f71c0f450e4eeb7280d481122d238bd513cc98ac7bedbc44fff101ca8a63fb4
    role: context
  - path: reports/causal_graph_review/decisions/20261005-two-records-batch12.yaml
    sha256: 7fd9cacc313e6f9db6e6836f0b4618db45ce8ac4fa58744bce36a4b7275d0a46
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
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
- target_id: CommunityMech:000191
  path: kb/communities/Chlorella_Azospirillum_Synthetic_Mutualism.yaml
  label: Chlorella-Azospirillum Synthetic Mutualism
  kind: maintained
  record_class: MicrobialCommunity
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Chlorella_Azospirillum_Synthetic_Mutualism.yaml
    role: canonical_record
scope:
  description: Entire maintained record, each taxon/node/arrow and non-graph metadata
    assessed against three full scientific mains, all main figures, nutrient Table
    S1, exact strain authorities and current provenance.
  selection: Only released CommunityMech:000191 in the owned batch 10 checkout.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000191
checks:
- check_id: validate
  name: validate
  status: passed
  required: true
  summary: Schema passed.
  target_ids:
  - CommunityMech:000191
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src
    just --no-dotenv validate kb/communities/Chlorella_Azospirillum_Synthetic_Mutualism.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate
  scope_note: Fresh execution in the owned batch 10 checkout. Mechanical success does
    not establish source-specific biological mechanisms or recipe equivalence.
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Strict validation passed.
  target_ids:
  - CommunityMech:000191
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src
    just --no-dotenv validate-strict kb/communities/Chlorella_Azospirillum_Synthetic_Mutualism.yaml
    --out /private/tmp/cm-review-session/batch-10/000191/strict-report.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-strict
  scope_note: Fresh execution in the owned batch 10 checkout. Mechanical success does
    not establish source-specific biological mechanisms or recipe equivalence.
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Term validation passed.
  target_ids:
  - CommunityMech:000191
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src
    just --no-dotenv validate-terms kb/communities/Chlorella_Azospirillum_Synthetic_Mutualism.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-terms
  scope_note: Fresh execution in the owned batch 10 checkout. Mechanical success does
    not establish source-specific biological mechanisms or recipe equivalence.
- check_id: validate-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: GTDB structure/coherence passed.
  target_ids:
  - CommunityMech:000191
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src
    just --no-dotenv validate-gtdb kb/communities/Chlorella_Azospirillum_Synthetic_Mutualism.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb
  scope_note: Fresh execution in the owned batch 10 checkout. Mechanical success does
    not establish source-specific biological mechanisms or recipe equivalence.
- check_id: validate-gtdb-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: Algal and bacterial GTDB applicability passed.
  target_ids:
  - CommunityMech:000191
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src
    just --no-dotenv validate-gtdb-domain kb/communities/Chlorella_Azospirillum_Synthetic_Mutualism.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb-domain
  scope_note: Fresh execution in the owned batch 10 checkout. Mechanical success does
    not establish source-specific biological mechanisms or recipe equivalence.
- check_id: validate-history
  name: validate-history
  status: passed
  required: true
  summary: History validation passed.
  target_ids:
  - CommunityMech:000191
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src
    just --no-dotenv validate-history history/records/Chlorella_Azospirillum_Synthetic_Mutualism
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-history
  scope_note: Fresh execution in the owned batch 10 checkout. Mechanical success does
    not establish source-specific biological mechanisms or recipe equivalence.
- check_id: normalize-cache-names-check
  name: normalize-cache-names-check
  status: passed
  required: true
  summary: Read-only cache filename check passed.
  target_ids:
  - CommunityMech:000191
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src
    uv run python scripts/normalize_cache_names.py --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-normalize-cache-names-check
  scope_note: Fresh execution in the owned batch 10 checkout. Mechanical success does
    not establish source-specific biological mechanisms or recipe equivalence.
- check_id: validate-references-explained
  name: validate-references-explained
  status: passed
  required: true
  summary: Native references pass against unchanged source-specific caches; fresh
    scientific checks separately verify excerpt context.
  target_ids:
  - CommunityMech:000191
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src
    just --no-dotenv validate-references-explained kb/communities/Chlorella_Azospirillum_Synthetic_Mutualism.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-references-explained
  scope_note: Fresh execution in the owned batch 10 checkout. Mechanical success does
    not establish source-specific biological mechanisms or recipe equivalence.
- check_id: audit-network
  name: audit-network
  status: failed
  required: true
  summary: Fresh batch 10 corpus diagnostic retains unrelated warnings; this focal
    graph separately reports COMPLETE.
  target_ids:
  - CommunityMech:000191
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv audit-network
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-audit-network
  - metrics
  scope_note: Explicit same-batch corpus reuse. Nonzero corpus status is not assigned
    as a new defect to this target.
- check_id: check-network-quality
  name: check-network-quality
  status: failed
  required: true
  summary: Fresh batch 10 corpus diagnostic retains unrelated warnings; this focal
    graph separately reports COMPLETE.
  target_ids:
  - CommunityMech:000191
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv check-network-quality
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-check-network-quality
  - metrics
  scope_note: Explicit same-batch corpus reuse. Nonzero corpus status is not assigned
    as a new defect to this target.
- check_id: scientific-source
  name: Main and current-claim-critical source verification
  status: passed
  required: true
  summary: All three scientific mains, all 17 main figures, both main tables and complete
    nutrient Table S1 were assessed. Unread starch SI does not carry an exact current
    numerical claim being certified.
  target_ids:
  - CommunityMech:000191
  evidence_ids:
  - lead-read
  - root-source
  - source-scope
- check_id: direct-snippets
  name: Fresh reference-specific excerpt checks
  status: passed
  required: true
  summary: 'All 32 excerpts are supported: 31 strict fresh matches and one documented
    FEMS unit projection; cache comparison has a separate sentence-initial capitalization
    projection.'
  target_ids:
  - CommunityMech:000191
  evidence_ids:
  - snippets
- check_id: starch-si
  name: Starch supplementary Table S1 and Figure S1
  status: unavailable
  required: false
  summary: The exact supplemental growth-rate table and bacterial growth panels remain
    unread after ordinary DOI/API/publisher discovery. Main text and figures support
    the bounded current claims; no precise SI-only bacterial growth value is certified.
  target_ids:
  - CommunityMech:000191
  evidence_ids:
  - resources
  - starch-mechanism
  - lead-read
- check_id: resources
  name: Exact source-linked publication and strain context
  status: passed
  required: true
  summary: Bibliography, actual nutrient supplement and predecessor/current-catalogue
    identity were checked with their precise scopes. No dedicated study archive or
    cross-Mech mapping is invented.
  target_ids:
  - CommunityMech:000191
  evidence_ids:
  - resources
  - catalogues
  - historical-context
- check_id: reanalysis
  name: Raw data and experimental reproduction
  status: skipped
  required: false
  summary: No raw data analysis, statistical retest, code execution, experimental
    reproduction or inferred source-error correction.
  target_ids:
  - CommunityMech:000191
  evidence_ids:
  - lead-read
  - resources
- check_id: adapter
  name: Optional structured source adapter
  status: unavailable
  required: false
  summary: Availability is bounded by the frozen runtime-discovery receipt; inspected
    public primary sources and authorities supplied the necessary review evidence.
  target_ids:
  - CommunityMech:000191
  evidence_ids:
  - adapter
evidence:
- evidence_id: record
  kind: record_content
  reference: kb/communities/Chlorella_Azospirillum_Synthetic_Mutualism.yaml
  locator: Entire maintained YAML, both taxa, all four nodes and both downstream arrows
  summary: The graph preserves study-specific nutrient, local-transfer, aggregation
    and starch-response limits. The generic medium, non-graph exchange language and
    historical-resource explanation retain distinct curation debt.
  support: supports
  accessed_at: '2026-10-21T18:02:30.804452Z'
- evidence_id: identity
  kind: primary_source
  reference: PMID:30397795; doi:10.1007/s00248-018-1282-1
  locator: 'Materials and Methods: Microorganisms and Preparation of Initial Inoculum;
    Introduction'
  summary: The focal pair is C. sorokiniana UTEX 2714, formerly designated C. vulgaris,
    with A. brasilense Cd, DSM 1843. The authors deliberately assemble the two organisms
    in alginate beads and distinguish their individual habitats. Synthetic origin
    and engineered state are supported; no natural coisolation is implied. Sp6 and
    its derivative SpM7918 in the starch paper are comparator strains, not extra members
    of this Cd record.
  support: supports
  accessed_at: '2026-10-21T18:02:30.804525Z'
  snapshot_sha256: 842f2157f5286bed5fc7a468fe8ad6e2a8767b41e08ce66805e5bf44ca11f1b8
- evidence_id: nutrient-growth
  kind: primary_source
  reference: PMID:30397795; doi:10.1007/s00248-018-1282-1
  locator: 'Results: Growth and Metabolite Production Using Rich Medium (Diluted Nutrient
    Broth) During the Initial Growth Phase; corresponding N-Free OAB and C-Free SGM
    subsections; Figures 1–4'
  summary: The first 12 hours compare diluted NB, N-free OAB and C-free SGM, followed
    by SGM in every treatment. Population benefits depend on treatment and time. Following
    NB, later bacterial counts are not significantly different between single and
    paired immobilization. Continuous C-free SGM gives the highest early starch concentration
    in algae alone. The current conditional mutualism node correctly preserves these
    exceptions.
  support: supports
  accessed_at: '2026-10-21T18:02:30.805449Z'
  snapshot_sha256: 842f2157f5286bed5fc7a468fe8ad6e2a8767b41e08ce66805e5bf44ca11f1b8
- evidence_id: aggregation
  kind: primary_source
  reference: PMID:30397795; doi:10.1007/s00248-018-1282-1
  locator: 'Results: Dynamics of Aggregation Between Cells of C. sorokiniana and A.
    brasilense During Different Initial Nutritional Conditions; Figures 5–7; Discussion'
  summary: Microscopy shows mixed-cell organization within investigator-made beads.
    Initial N-free attachment weakens later, whereas large C-free aggregates develop
    at 83 hours. The study does not selectively disrupt proximity to establish that
    aggregation causes the growth benefit. Retain the untyped organization node and
    its HYPOTHESIZED downstream link, rather than converting bead assembly into partner-mediated
    colonization.
  support: supports
  accessed_at: '2026-10-21T18:02:30.805943Z'
  snapshot_sha256: 842f2157f5286bed5fc7a468fe8ad6e2a8767b41e08ce66805e5bf44ca11f1b8
- evidence_id: cultivation-nutrients
  kind: primary_source
  reference: PMID:30397795; doi:10.1007/s00248-018-1282-1
  locator: 'Materials and Methods: Microorganisms and Preparation of Initial Inoculum;
    Immobilization in Alginate of Microorganisms; Experimental Culture Conditions;
    Experimental Design and Statistical Analysis; Figure 1'
  summary: Algal C30 preculture is 10 mL inoculum into 90 mL, seven days at 27±2 C,
    140 rpm and 60 µmol photons/m²/s; bacterial BTB-2 preculture is 32±2 C, 120 rpm
    for 16 hours. Experimental beads are 3 mm, formed with 2% alginate. Methods specifies
    20 g beads in 150 mL, first 12 hours in NB/OAB/SGM, three saline washes and transfer
    to SGM through 83 hours at 27±2 C, 140 rpm and the same illumination. The statistics
    subsection instead says 100 mL in 250 mL flasks; retain this source conflict.
    NB is 10% v/v in Methods but 10% w/v in Figure 2. SGM contains NH4Cl 191 mg/L,
    so C-free does not mean nitrogen-free. Citrate pH 8 is bead dissolution, not a
    culture setpoint.
  support: supports
  accessed_at: '2026-10-21T18:02:30.806420Z'
  snapshot_sha256: 842f2157f5286bed5fc7a468fe8ad6e2a8767b41e08ce66805e5bf44ca11f1b8
- evidence_id: nutrient-si
  kind: primary_source
  reference: PMID:30397795, electronic supplementary Table S1
  locator: 'Complete DOCX table: Media used in this study for initial cultivation
    of microorganisms'
  summary: The publisher-linked table identifies C30 for UTEX 2714 and BTB-2 for Cd/DSM
    1843. C30 prints KNO3 25, MgSO4·7H2O 10, KH2PO4 4, K2HPO4 1 and FeSO4·7H2O 1 g/L,
    with trace compounds in µg/L. BTB-2 contains gluconate, tryptone and yeast extract
    at 5 g/L each, plus its stated salts. These are preculture formulations. The starch-paper
    BTB-2 instead lists glycerol 8 mL; do not silently merge the recipes or normalize
    the printed units from another standard medium.
  support: supports
  accessed_at: '2026-10-21T18:02:30.806895Z'
  snapshot_sha256: 1eee006f739d45427f7a451f182cc3ca529647ffd4cc76a22de3f1616a1b8cdf
- evidence_id: exudate-supplement
  kind: primary_source
  reference: PMID:27090758; doi:10.1093/femsec/fiw077
  locator: 'Materials and Methods: Experimental culture conditions; Results: Tryptophan
    consumption and IAA production by A. brasilense; Figure 2; Discussion'
  summary: Bacterial cultures grown in algal exudates or SGM supplemented with tryptophan
    plus thiamine diphosphate produce IAA; tryptophan alone does not reproduce that
    response. The tested supplement is a phosphorylated cofactor, not direct identification
    of the secreted extracellular thiamine form. Algal Trp release and bacterial use
    are supported, while the chemical-form and local-coculture claims require qualification.
  support: supports
  accessed_at: '2026-10-21T18:02:30.807175Z'
  snapshot_sha256: 01480ecde71b43cebead4cffda95a5089c24694ab10755d99653506705ad1532
- evidence_id: local-transfer
  kind: primary_source
  reference: PMID:27090758; doi:10.1093/femsec/fiw077
  locator: 'Results: Tryptophan consumption and IAA production by A. brasilense; IPDC
    activity; Expression of the ipdC gene; Figures 2,4–5; Discussion'
  summary: In co-immobilized cultures neither Trp nor IAA is detected in bulk SGM.
    The authors infer local transfer from exudate/supplement effects, growth and enzyme/expression
    observations. They discuss non-specific IPDC substrates and an algal contribution.
    This supports the existing PARTIAL interpretation, not direct measurement of endogenous
    molecule-resolved flux or unique bacterial IPDC activity. The source also contains
    P-sign/relative-expression presentation inconsistencies; no quantitative expression
    recalculation is attempted.
  support: supports
  accessed_at: '2026-10-21T18:02:30.807563Z'
  snapshot_sha256: 01480ecde71b43cebead4cffda95a5089c24694ab10755d99653506705ad1532
  quote: no tryptophan or IAA
- evidence_id: cultivation-exchange
  kind: primary_source
  reference: PMID:27090758; doi:10.1093/femsec/fiw077
  locator: 'Materials and Methods: Microorganisms and initial growth conditions in
    prior experiments; Immobilization of microorganisms; Experimental culture conditions;
    Experimental design and statistical analysis'
  summary: The illuminated FEMS study uses 2 mm beads, an initial 24-hour recovery,
    and a reported 20 g beads in 150 mL SGM assay at 27±2 C and 140 rpm for 120 hours.
    Bacterial controls receive Trp 1.5 µg/mL alone or with thiamine diphosphate 70
    ng/mL, or filtered three-day algal exudates. These are separate conditions, not
    a mandatory Trp/IAA basal recipe. Statistics instead describes 300 mL in 500 mL
    flasks; the counting section refers to 250 mL flasks. Preserve attribution rather
    than invent a single vessel/fill. The separate algal exudate experiment uses 120
    rpm, distinct from the main 140 rpm assay.
  support: supports
  accessed_at: '2026-10-21T18:02:30.807685Z'
  snapshot_sha256: 01480ecde71b43cebead4cffda95a5089c24694ab10755d99653506705ad1532
- evidence_id: primer-context
  kind: primary_source
  reference: PMID:27090758; doi:10.1093/femsec/fiw077
  locator: 'Materials and Methods: RNA isolation, cDNA synthesis and quantitative
    Real Time PCR; Table 1'
  summary: The source-reported NC016617.1 is a primer-design reference sequence. Table
    1 is a primer inventory. Neither is a new experimental archive deposition or independently
    verified exact Cd genome here. No gene-level community annotation, genome identity
    or missing-data finding is inferred from that identifier.
  support: supports
  accessed_at: '2026-10-21T18:02:30.807800Z'
  snapshot_sha256: 01480ecde71b43cebead4cffda95a5089c24694ab10755d99653506705ad1532
- evidence_id: starch-mechanism
  kind: primary_source
  reference: PMID:26924113; doi:10.1016/j.resmic.2016.02.005
  locator: Results 3.1–3.4; Figures 1–5 and Table 1; Discussion
  summary: Wild-type Cd and Sp6 pairs show stronger starch/AGPase responses than the
    Sp6-derived IAA-attenuated SpM7918 comparator; synthetic IAA gives a transient
    response. This supports partial IAA mediation under dark glucose-fed conditions.
    It does not establish Cd-specific genetic necessity or direct regulation of AGPase
    instead of altered glucose uptake. The Cd Trp/IAA correlation under N starvation
    is nonsignificant, despite broader discussion language. Most paired algal population
    comparisons decrease, so starch accumulation is not reciprocal growth or fitness.
  support: supports
  accessed_at: '2026-10-21T18:02:30.807915Z'
  snapshot_sha256: 1eed1c4dda89c0d3e9d7f091dd166b75e47558498683c37095082e8b006c71fb
  quote: co-immobilization reduced the population
- evidence_id: cultivation-starch
  kind: primary_source
  reference: PMID:26924113; doi:10.1016/j.resmic.2016.02.005
  locator: Materials and methods 2.1 Microorganisms and initial growth conditions;
    2.2 Immobilization of microorganisms; 2.3 Experimental culture conditions; 2.6
    Experimental design and statistical analysis; printed pages 368–370
  summary: The starch experiment uses 3–4 mm beads with 24-hour NB or N-free OAB recovery,
    three saline washes, and 12 g beads in 150 mL SGM in 250 mL flasks. SGM contains
    glucose 10 g/L, with NH4Cl 191 mg/L for the N-replete arm and without added NH4Cl
    for the starved arm. The assay is dark, aerobic, 27±2 C and 140 rpm. Section 2.3
    states 96 hours but Results/figures extend to 120 hours. The synthetic IAA comparator
    dose is printed 47.5 ng/µL in section 2.3 and 48 ng/µL in section 2.6; PDF text
    extraction corrupts µL to mL. The visual source governs. BTB-2 pH 7 applies to
    bacterial preculture, not every coculture. Analytical extraction pH/temperature
    is not cultivation.
  support: supports
  accessed_at: '2026-10-21T18:02:30.808325Z'
  snapshot_sha256: 1eed1c4dda89c0d3e9d7f091dd166b75e47558498683c37095082e8b006c71fb
- evidence_id: starch-unit-visual
  kind: primary_source
  reference: PMID:26924113, author PDF
  locator: Printed page 369, section 2.3; independent visual check against pages 368
    and 370
  summary: The rendered page explicitly prints the 47.5 ng/µL synthetic IAA supplement.
    The text extractor substitutes m for the micro-prefix in several units. Page 370
    prints 48 ng/µL, and figure axes use their separately printed µg/mL. Do not copy
    the corrupted extraction or silently reconcile source concentrations.
  support: supports
  accessed_at: '2026-10-21T18:02:30.808536Z'
  snapshot_sha256: 8ba84e2c3a6d0347398892e223fe81f466e039ecc9455f889ad5126cf32b99ba
- evidence_id: predecessor
  kind: primary_source
  reference: PMID:10742237; doi:10.1128/AEM.66.4.1527-1531.2000
  locator: 'MATERIALS AND METHODS: organism-identity paragraph, bounded historical
    context'
  summary: The predecessor explicitly reports C. vulgaris UTEX 2714. The focal papers
    identify that same algal accession as formerly C. vulgaris, so the record should
    not claim a different Chlorella species solely from the historical name. The old
    source calls Cd DSM 7030; direct current catalogue identity is unrelated to Cd,
    so retain this unresolved source-number conflict. Focal Cd/DSM 1843 remains independently
    supported. Only predecessor bibliography/abstract and this identity paragraph
    were assessed, not its whole experimental science.
  support: supports
  accessed_at: '2026-10-21T18:02:30.809169Z'
  snapshot_sha256: 12f320220e7e826ba53a7d701150e5f6eaa042bd5e54a252965f80facbb0ff07
- evidence_id: schema
  kind: authority
  reference: src/communitymech/schema/communitymech.yaml
  locator: FunctionalRoleEnum; growth_media/composition; CommunityOriginEnum and EcologicalStateEnum
  summary: The role enum permits broad source-qualified metabolic cooperation; do
    not impose a new obligacy, energetic-removal or strict carbon-assimilation criterion.
    A structured medium composition denotes ingredients of the scoped medium, not
    merely metabolites detected in an experiment. Synthetic assembly and engineered
    state fit this laboratory pair; quantitative cultivation details require stage-specific
    evidence.
  support: supports
  accessed_at: '2026-10-21T18:02:30.809467Z'
  snapshot_sha256: c41630d09def826256ddb6678c1ce31fa71e3b074219bb9d217d98035a5324ee
- evidence_id: ontology
  kind: authority
  reference: ontology-authority.json
  locator: Whole frozen receipt and its declared scope
  summary: All 12 distinct encoded ontology pairs match across 31 occurrences. CHEBI:18385
    identifies thiamine(1+), distinct from thiamine diphosphate; correct label matching
    does not determine which extracellular form was present.
  support: supports
  accessed_at: '2026-10-21T18:02:30.809541Z'
  snapshot_sha256: 6c9a2bd6d3c5f797641512705696ca8ec0cf0b378ca2e172b286ffe8f6db74d7
- evidence_id: semantics
  kind: authority
  reference: ontology-semantic-notes.json
  locator: Whole frozen receipt and its declared scope
  summary: Exact schema and ontology definitions support retaining the broad roles
    and qualified graph. The medium/composition and non-graph chemical-form assertions
    need source-specific repair; no narrower functional-role requirement or new taxon
    is imposed.
  support: supports
  accessed_at: '2026-10-21T18:02:30.809808Z'
  snapshot_sha256: 3a2a90a53e6baa00829ad8709b72606e43fa7acb7dd77e9f5d86490b6e872090
- evidence_id: gtdb
  kind: authority
  reference: child-gtdb-crosswalk.json
  locator: Whole frozen receipt and its declared scope
  summary: 'The bacterial block matches its explicitly disclosed exact species-name
    fallback: no NCBI 192 row, one species-name row keyed to FP2/1262469, two genomes
    and fraction 1.0. This does not classify Cd genomically. Algal NO_GTDB_EQUIVALENT
    is appropriate.'
  support: supports
  accessed_at: '2026-10-21T18:02:30.809969Z'
  snapshot_sha256: 678db1873a6d63157bc5cbb4a75b18e4e23dbbd8ff7e6c9b37bb972ee09483df
- evidence_id: catalogues
  kind: authority
  reference: child-strain-catalogue-authority.json
  locator: Whole frozen receipt and its declared scope
  summary: DSM 1843 directly confirms Cd and ATCC 29710. UTEX 2714 retains an old
    C. vulgaris heading but explicitly notes that this identification is incorrect
    and links a reidentification paper. The focal source naming is preserved; catalogue
    maintenance conditions are not assay conditions.
  support: supports
  accessed_at: '2026-10-21T18:02:30.810118Z'
  snapshot_sha256: 1f52491e1898550f2effafcd622a564cd7fe8a5f2160ebd5d0d296154b44d127
- evidence_id: historical-number
  kind: authority
  reference: child-predecessor-catalogue-discrepancy.json
  locator: Whole frozen receipt and its declared scope
  summary: Current DSM 7030 identifies Paenibacillus larvae type strain 846, not a
    verified Cd alias. Do not infer that the predecessor used this unrelated organism
    or replace the focal DSM 1843 identifier.
  support: supports
  accessed_at: '2026-10-21T18:02:30.810272Z'
  snapshot_sha256: 84a8c4855cf34f7e8625269420e576f85a447eca48c0a00a867d4a2a9e9fa478
- evidence_id: historical-context
  kind: record_content
  reference: predecessor-strain-context.json
  locator: Whole frozen receipt and its declared scope
  summary: The exact predecessor and focal identity paragraphs establish the historical
    UTEX name correspondence while preserving the unresolved bacterial culture-number
    conflict. No whole predecessor source review or protocol transfer is claimed.
  support: supports
  accessed_at: '2026-10-21T18:02:30.810389Z'
  snapshot_sha256: 166ac8fd0335193d6fbf59633a1c0a8685f2d0d52ba17cee9e6e99a34c1476ea
- evidence_id: resources
  kind: database
  reference: dataset-verification.json
  locator: Whole frozen receipt and its declared scope
  summary: The four publications and two taxonomy links are correctly external resources.
    Nutrient Table S1 is a verified source medium table. Starch SI remains unread;
    no distinct new deposition or cross-Mech mapping is established by bounded source-resource
    checks. This does not imply global data absence.
  support: supports
  accessed_at: '2026-10-21T18:02:30.810586Z'
  snapshot_sha256: 6e7c2bae960447a6253e895f0bb311ffe8c9877459bff06a5cb48eb4d267dc18
- evidence_id: snippets
  kind: validation
  reference: snippet-audit.json
  locator: Whole frozen receipt and its declared scope
  summary: 'All 32 excerpt occurrences are source-supported: 31 strict fresh matches
    plus one explicit FEMS unit typography projection. Cache comparison separately
    has 31 strict matches plus one sentence-initial capitalization projection. Excerpt
    validity does not make surrounding claims correct.'
  support: supports
  accessed_at: '2026-10-21T18:02:30.810732Z'
  snapshot_sha256: 0851b68fdef65fc4ac5f1a6c1e804de8927ca4aabffc6454690efcbe1d5736c8
- evidence_id: history
  kind: record_content
  reference: provenance-audit.json
  locator: Whole frozen receipt and its declared scope
  summary: The sole history and exact prior decision preserve graph-repair context,
    not full certification. Current issue 1295 is closed/completed with one comment;
    issue 1297 is open with no comments and owns the non-graph protocol/exchange/historical-name
    follow-up. FEMS cache scope has already been corrected to selected abstract and
    Methods excerpts.
  support: supports
  accessed_at: '2026-10-21T18:02:30.810967Z'
  snapshot_sha256: 34f2fa8e5ee1c426e537860ae5637ed4d48df01514946dc8d521a11c64a636d2
- evidence_id: metrics
  kind: validation
  reference: support-audit.json
  locator: Whole frozen receipt and its declared scope
  summary: Native COMPLETE covers four nodes, two arrows and eight node-evidence entries.
    Completeness is 95. Two major and one minor findings give raw quality 113, capped
    at 100; no role or dataset is invented for score credit.
  support: supports
  accessed_at: '2026-10-21T18:02:30.811121Z'
  snapshot_sha256: 344689501aa50b6f8d3bea0415852fc621ce29f36286464a562c5a201c59764e
- evidence_id: lead-read
  kind: validation
  reference: lead-primary-read-scope.json
  locator: Whole frozen receipt and its declared scope
  summary: Lead read all three scientific mains, all 17 main figures, both main Table
    1 inventories and every nutrient Table S1 cell. Starch SI Table S1/Figure S1 remain
    unread; exact bacterial SI curves/rates are not certified. Predecessor read scope
    is bounded identity context.
  support: supports
  accessed_at: '2026-10-21T18:02:30.811168Z'
  snapshot_sha256: f88a4faf199e9dc3cd0e31454a1b67cb5ccf6de41e0cc5919d9215b91b1d5087
- evidence_id: source-scope
  kind: validation
  reference: source-audit.json
  locator: Whole frozen receipt and its declared scope
  summary: Frozen current-claim source assessment records two major and one minor
    findings, retained broad roles/four nodes/two arrows, detailed assay distinctions
    and exact source limitations.
  support: supports
  accessed_at: '2026-10-21T18:02:30.811306Z'
  snapshot_sha256: 1a14efbcf7f2846df1ebcd08e0232f3ce19ae55070b2ff7cf33cae0d86f3d62a
- evidence_id: root-source
  kind: validation
  reference: root-independent-source-audit.json
  locator: Whole frozen receipt and its declared scope
  summary: Root independently read the three scientific mains, all 17 main figures,
    both main tables, nutrient Table S1 and historical identity/catalogue context.
    It agrees with completed current-claim review and the three findings; starch SI
    limitations remain explicit.
  support: supports
  accessed_at: '2026-10-21T18:02:30.811435Z'
  snapshot_sha256: 6031d9b1a091a90aac2630c6cb9c0438664e4d4975cdfd84cb8141f6f8bfc076
- evidence_id: auxiliary
  kind: validation
  reference: auxiliary-frozen-manifest.json
  locator: Whole frozen receipt and its declared scope
  summary: All eight focused native checks pass, all 27 official inputs remain unchanged,
    and the initial and final validator summaries are separate immutable files. Native
    and authority success do not certify biological mechanisms.
  support: supports
  accessed_at: '2026-10-21T18:02:30.811561Z'
  snapshot_sha256: 3936ea0f82a575c19bc92c8c2fc59f784bbd7b3e6f57f7bbdab2cb0b12c5aed0
- evidence_id: adapter
  kind: validation
  reference: adapter-check.json
  locator: Whole frozen receipt and its declared scope
  summary: Optional structured-adapter discovery is bounded to the recorded runtime.
    No paid provider, credentials or unapproved external execution was used.
  support: supports
  accessed_at: '2026-10-21T18:02:30.811705Z'
  snapshot_sha256: 2a65d039e5f99c048b8ed887451260a742e8567bab31507c571b756d503299ce
- evidence_id: check-validate
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src
    just --no-dotenv validate kb/communities/Chlorella_Azospirillum_Synthetic_Mutualism.yaml
  locator: Actual execution 2026-10-21T17:52:36.127155+00:00 to 2026-10-21T17:52:37.843903+00:00
  summary: Schema passed.
  support: supports
  accessed_at: '2026-10-21T17:52:37.843903Z'
  snapshot_sha256: cca488994f691f7025d23d70b13c3f7eef234335b4c58122292e434cf2ac8cd0
- evidence_id: check-validate-strict
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src
    just --no-dotenv validate-strict kb/communities/Chlorella_Azospirillum_Synthetic_Mutualism.yaml
    --out /private/tmp/cm-review-session/batch-10/000191/strict-report.tsv
  locator: Actual execution 2026-10-21T17:52:36.146204+00:00 to 2026-10-21T17:52:41.021681+00:00
  summary: Strict validation passed.
  support: supports
  accessed_at: '2026-10-21T17:52:41.021681Z'
  snapshot_sha256: 939e2e98fba7d64a6302c83a94c7bdaf3c9c95b2f9c74cd74604ecb043f02c71
- evidence_id: check-validate-terms
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src
    just --no-dotenv validate-terms kb/communities/Chlorella_Azospirillum_Synthetic_Mutualism.yaml
  locator: Actual execution 2026-10-21T17:52:36.151417+00:00 to 2026-10-21T17:52:40.131241+00:00
  summary: Term validation passed.
  support: supports
  accessed_at: '2026-10-21T17:52:40.131241Z'
  snapshot_sha256: 65353661bcfaadbb10e7f0a6ef594b75729451226a52beaed4bf92564d387d5d
- evidence_id: check-validate-gtdb
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src
    just --no-dotenv validate-gtdb kb/communities/Chlorella_Azospirillum_Synthetic_Mutualism.yaml
  locator: Actual execution 2026-10-21T17:52:37.844488+00:00 to 2026-10-21T17:52:38.028489+00:00
  summary: GTDB structure/coherence passed.
  support: supports
  accessed_at: '2026-10-21T17:52:38.028489Z'
  snapshot_sha256: 98d84251bd5d12028a5a946ec70986a3ab15fc19c1eef5a6112b2e94a8055483
- evidence_id: check-validate-gtdb-domain
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src
    just --no-dotenv validate-gtdb-domain kb/communities/Chlorella_Azospirillum_Synthetic_Mutualism.yaml
  locator: Actual execution 2026-10-21T17:52:38.028825+00:00 to 2026-10-21T17:52:41.473755+00:00
  summary: Algal and bacterial GTDB applicability passed.
  support: supports
  accessed_at: '2026-10-21T17:52:41.473755Z'
  snapshot_sha256: 6615399867590e9fafb5f71549244452d1746db31c6cabc92a4e0b05f6f1a0d6
- evidence_id: check-validate-history
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src
    just --no-dotenv validate-history history/records/Chlorella_Azospirillum_Synthetic_Mutualism
  locator: Actual execution 2026-10-21T17:52:40.131655+00:00 to 2026-10-21T17:52:41.717310+00:00
  summary: History validation passed.
  support: supports
  accessed_at: '2026-10-21T17:52:41.717310Z'
  snapshot_sha256: 934e993932df6bebd17f387a722d64d3e108747b9b3dad7e79b38d69e4e4447e
- evidence_id: check-normalize-cache-names-check
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src
    uv run python scripts/normalize_cache_names.py --check
  locator: Actual execution 2026-10-21T17:52:41.720248+00:00 to 2026-10-21T17:52:41.808206+00:00
  summary: Read-only cache filename check passed.
  support: supports
  accessed_at: '2026-10-21T17:52:41.808206Z'
  snapshot_sha256: 18746d076c9b5fa4a319ef43cfa6031d54742d854740612e7d631da79437c143
- evidence_id: check-validate-references-explained
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src
    just --no-dotenv validate-references-explained kb/communities/Chlorella_Azospirillum_Synthetic_Mutualism.yaml
  locator: Actual execution 2026-10-21T17:52:41.808706+00:00 to 2026-10-21T17:52:43.552878+00:00
  summary: Native references pass against unchanged source-specific caches; fresh
    scientific checks separately verify excerpt context.
  support: supports
  accessed_at: '2026-10-21T17:52:43.552878Z'
  snapshot_sha256: ca5b51958e536f2c6b8ce04d1a4d45a91a07b658c7b9c102f3dc4b63bc2f0363
- evidence_id: check-audit-network
  kind: validation
  reference: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv audit-network
  locator: Actual execution 2026-10-21T17:04:17.819938+00:00 to 2026-10-21T17:04:25.370848+00:00
  summary: Fresh batch 10 corpus diagnostic retains unrelated warnings; this focal
    graph separately reports COMPLETE.
  support: supports
  accessed_at: '2026-10-21T17:04:25.370848Z'
  snapshot_sha256: 301cbda477198c0cff0f38601fdb49af8d805cafa7da106733150d64786d987d
- evidence_id: check-check-network-quality
  kind: validation
  reference: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv check-network-quality
  locator: Actual execution 2026-10-21T17:04:17.819995+00:00 to 2026-10-21T17:04:26.163649+00:00
  summary: Fresh batch 10 corpus diagnostic retains unrelated warnings; this focal
    graph separately reports COMPLETE.
  support: supports
  accessed_at: '2026-10-21T17:04:26.163649Z'
  snapshot_sha256: f8dae0e292e8e2f8c221450aacc2bb120abe0e3f32c16ed59f8406e8b859a895
assessments:
- assessment_id: identity
  area: identity
  topic: Community, member and strain identity
  outcome: supported
  summary: Retain the synthetic laboratory pair and current focal species/strains.
  target_ids:
  - CommunityMech:000191
  evidence_ids:
  - identity
  - catalogues
  - gtdb
  - predecessor
  details: UTEX 2714 and Cd/DSM 1843 are directly supported. The old C. vulgaris name
    refers to the same algal accession in the specifically inspected predecessor.
    Its bacterial DSM number is inconsistent with current catalogue identity and must
    remain attributed. Do not widen the roster to Sp6/SpM7918 comparators, invent
    natural coisolation or change the explicitly scoped species-name GTDB block.
- assessment_id: roles
  area: evidence
  topic: Both taxonomy functional_role lists and narrow evidence
  outcome: supported
  summary: Retain broad roles with source-specific evidence and physiological context.
  target_ids:
  - CommunityMech:000191
  evidence_ids:
  - identity
  - exudate-supplement
  - local-transfer
  - starch-mechanism
  - semantics
  details: Algal primary production is applicable to illuminated cultures, not a claim
    of photosynthesis in the dark glucose assay. The bacterial algal-resource use
    and source-described reciprocal metabolic/signaling interpretation support qualified
    roles. Attach actual exudate, supplementation and response evidence instead of
    expecting membership-only snippets to establish a mechanism. No exact local flux,
    algal IAA catabolism, obligate syntrophy or energetic product-removal requirement
    is introduced.
- assessment_id: node-nutrients
  area: evidence
  topic: 'ecological_interactions[0]: Nutrient-Modulated Synthetic Mutualism'
  outcome: supported
  summary: Retain condition- and time-specific mutualism with its exceptions.
  target_ids:
  - CommunityMech:000191
  evidence_ids:
  - nutrient-growth
  - cultivation-nutrients
  details: The 12-hour initial nutrient shift and later common SGM phase are explicit.
    Neither general population benefit nor starch accumulation is universal across
    treatments; the current node already preserves the later NB bacterial comparison.
- assessment_id: node-exchange
  area: evidence
  topic: 'ecological_interactions[1]: Tryptophan, Thiamine, and IAA Exchange'
  outcome: supported
  summary: Retain the PARTIAL exudate/supplement-based exchange interpretation.
  target_ids:
  - CommunityMech:000191
  evidence_ids:
  - exudate-supplement
  - local-transfer
  - ontology
  details: The node already distinguishes thiamine diphosphate supplementation from
    an unmeasured extracellular chemical form, and bulk non-detection from proposed
    bead-local exchange. IPDC activity is not uniquely bacterial or specific to IAA.
    Do not upgrade to a directly measured flux or automatically replace the metabolite
    term with TPP as the secreted species.
- assessment_id: edge-starch
  area: evidence
  topic: ecological_interactions[1].downstream[0]
  outcome: supported
  summary: Retain PARTIAL cross-study IAA mediation of starch/AGPase responses.
  target_ids:
  - CommunityMech:000191
  evidence_ids:
  - starch-mechanism
  - local-transfer
  details: The dark glucose-fed assay and synthetic IAA comparator support mediation,
    while SpM7918 is derived from Sp6 rather than Cd. Exact-Cd necessity and local
    resource-transfer contribution remain unresolved. Do not equate starch yield with
    mutual growth or recast the comparator as a focal member.
- assessment_id: node-aggregation
  area: evidence
  topic: 'ecological_interactions[2]: Co-Immobilization and Cell Aggregation'
  outcome: supported
  summary: Retain observed organization without a colonization-facilitation type.
  target_ids:
  - CommunityMech:000191
  evidence_ids:
  - aggregation
  - cultivation-nutrients
  details: Investigators create the beads; microscopy shows condition-dependent mixed
    aggregates. The current node separates that physical organization from a proven
    partner-caused colonization mechanism.
- assessment_id: edge-growth
  area: evidence
  topic: ecological_interactions[2].downstream[0]
  outcome: supported
  summary: Retain HYPOTHESIZED aggregation-to-growth mediation.
  target_ids:
  - CommunityMech:000191
  evidence_ids:
  - aggregation
  - nutrient-growth
  details: No selective proximity intervention establishes necessity. Observed growth
    and aggregation can be described without upgrading their causal relationship or
    introducing additional arrows.
- assessment_id: node-starch
  area: evidence
  topic: 'ecological_interactions[3]: IAA-Linked Starch Accumulation Response'
  outcome: supported
  summary: Retain the untyped physiological response with dark-assay and strain limits.
  target_ids:
  - CommunityMech:000191
  evidence_ids:
  - starch-mechanism
  - cultivation-starch
  details: AGPase/starch/glucose uptake responses are measured, whereas direct AGPase
    regulation remains a proposed pathway. Most paired algal-growth comparisons decrease
    and the Cd N-starvation correlation is nonsignificant. Main figures and text suffice
    for current claims; exact unread bacterial SI growth trends are not certified.
- assessment_id: nongraph
  area: evidence
  topic: Engineering, ingredient and resource exchange wording
  outcome: concern
  summary: Carry the graph’s chemical-form and local-transfer qualifications into
    non-graph fields.
  target_ids:
  - CommunityMech:000191
  evidence_ids:
  - exudate-supplement
  - local-transfer
  - starch-mechanism
  - semantics
  details: Measured algal exudates, bacterial utilization, TPP supplementation, bulk
    nondetection and inferred local transfer are different evidence classes. The current
    related_ingredients thiamine/IAA prose and general exchange-measurement descriptions
    collapse these distinctions. Preserve broad source conclusions as attributed interpretation
    rather than direct endogenous-form or flux identification.
- assessment_id: cultivation
  area: evidence
  topic: growth_media and cultivation-related environmental_factors
  outcome: concern
  summary: Replace the generic Trp/IAA composition with stage- and assay-specific
    source conditions.
  target_ids:
  - CommunityMech:000191
  evidence_ids:
  - cultivation-nutrients
  - nutrient-si
  - cultivation-exchange
  - cultivation-starch
  - starch-unit-visual
  details: Trp is added in bacterial controls and IAA in an algal comparator, rather
    than universally to the pair. The three papers distinguish preculture, bead recovery,
    initial nutrient treatments, later SGM and dark glucose-fed assays. Recover the
    available conditions without conflating 2/3/3–4 mm beads, 12/24-hour stages, contradictory
    flask fills, assay versus analytical pH, or nutrient-table gluconate versus starch-paper
    glycerol. Printed units must be visually verified when PDF extraction is unreliable.
- assessment_id: environment
  area: identity
  topic: State, origin, category and environment
  outcome: supported
  summary: Keep the synthetic engineered laboratory context and scope condition descriptions.
  target_ids:
  - CommunityMech:000191
  evidence_ids:
  - identity
  - schema
  - cultivation-nutrients
  - cultivation-starch
  details: Laboratory environment and the broad algal community category fit the intended
    system. Bead construction is cultivation setup, and illumination/aerobic conditions
    require study-specific labels so dark starch assays do not inherit illuminated
    growth conditions. Empty metal/REE fields and NOT_APPLICABLE remain appropriate
    for the encoded biological scope.
- assessment_id: resources
  area: provenance
  topic: Publication and historical identity context
  outcome: concern
  summary: Correct the historical different-species explanation; retain verified publication
    resources.
  target_ids:
  - CommunityMech:000191
  evidence_ids:
  - predecessor
  - historical-context
  - historical-number
  - resources
  details: The same UTEX accession is explicitly reported under the older name. Preserve
    the source DSM 7030 discrepancy and focal DSM 1843 authority without claiming
    a verified bacterial alias. No dataset-absence defect or invented CultureMech
    mapping follows from the empty datasets list.
- assessment_id: provenance
  area: provenance
  topic: Current issue ownership and excerpt scope
  outcome: supported
  summary: Use existing issue 1297 and preserve the resolved FEMS cache-scope correction.
  target_ids:
  - CommunityMech:000191
  evidence_ids:
  - history
  - snippets
  - lead-read
  details: All 32 occurrences have source support, with explicit unit and capitalization
    projection boundaries rather than a false all-strict claim. Closed issue 1295
    and the exact historical decision certify only their prior scope. The current
    cache label is already corrected; no duplicate issue or full restricted-body cache
    import is authorized.
- assessment_id: validation
  area: schema
  topic: Native checks and immutable workflow
  outcome: supported
  summary: Eight focused checks pass; scientific review confirms three non-graph findings.
  target_ids:
  - CommunityMech:000191
  evidence_ids:
  - auxiliary
  - ontology
  - snippets
  details: Canonical, caches, history and generated products remain unchanged. Persistence
    is limited to a new immutable review bundle. Completed scientific review concerns
    the current encoded claims and does not imply full inspection of unavailable ancillary
    SI or raw data.
- assessment_id: metrics
  area: completeness
  topic: Native mechanical scores
  outcome: supported
  summary: Completeness 95 and quality 100/raw 113 are mechanical metrics.
  target_ids:
  - CommunityMech:000191
  evidence_ids:
  - metrics
  metrics:
  - name: completeness
    value: 95
    unit: points
    minimum: 0
    maximum: 100
    definition: 'Native rubric: required fields with roles 50 + environment 5 + at
      least three environmental factors 10 + at least three interaction nodes 10 +
      external resources 5 + growth media 10 + any node metabolites 5. No associated-dataset
      bonus. Four nodes qualify even though only two are typed; no role or dataset
      is invented for points.'
  - name: validation_quality
    value: 100
    unit: points
    minimum: 0
    maximum: 100
    definition: clamp(100−50P1−10P2−2P3+20min(mean node evidence/2,1)+15 if COMPLETE,0,100).
      P1=0, P2=2, P3=1, P4=0. Eight node-evidence entries over four nodes give 20
      points; COMPLETE adds 15. Raw 113 is capped at 100.
  - name: P1
    value: 0
    unit: findings
    definition: Native severity count.
  - name: P2
    value: 2
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
- finding_id: assay-specific-media
  issue_key: cm-000191-assay-specific-media
  category: evidence
  severity: major
  native_severity: P2
  normalization_reason: 'P2: substantive scope inflation or unsupported experimental
    representation changes the biological meaning of a maintained claim.'
  rule_id: review-checklist.claim-specific-scope-and-evidence
  status: open
  certainty: confirmed
  title: Separate measured metabolites and assay-specific supplements from basal medium
  description: The generic composition lists Trp and IAA as common coculture ingredients
    although the studies use distinct precursor/cofactor bacterial controls and synthetic
    IAA algal comparators. The same generic block omits recoverable source-specific
    precursor culture, recovery, initial nutrient-shift and dark glucose-fed conditions.
    The attached abstract snippets cannot establish a unified recipe.
  target_ids:
  - CommunityMech:000191
  field_paths:
  - growth_media[0]
  - environmental_factors[1]
  - environmental_factors[2]
  evidence_ids:
  - cultivation-nutrients
  - nutrient-si
  - cultivation-exchange
  - cultivation-starch
  - starch-unit-visual
  - history
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Chlorella_Azospirillum_Synthetic_Mutualism.yaml
    role: canonical_record
- finding_id: nongraph-exchange-scope
  issue_key: cm-000191-nongraph-exchange-scope
  category: evidence
  severity: major
  native_severity: P2
  normalization_reason: 'P2: substantive scope inflation or unsupported experimental
    representation changes the biological meaning of a maintained claim.'
  rule_id: review-checklist.claim-specific-scope-and-evidence
  status: open
  certainty: confirmed
  title: Qualify local exchange and exact cofactor-form assertions outside the graph
  description: Related-ingredient and general measurement/resource prose presents
    endogenous thiamine and local metabolite exchange as directly established. The
    sources distinguish exudate use and Trp plus TPP supplementation from bulk coculture
    non-detection and inferred bead-local transfer. Correct these claims and their
    evidence attachment without removing the supported broad roles or already qualified
    graph.
  target_ids:
  - CommunityMech:000191
  field_paths:
  - engineering_design.perturbation_design
  - engineering_design.measurement_endpoints
  - engineering_design.evidence
  - related_ingredients[0]
  - related_ingredients[1]
  - related_ingredients[2]
  - external_resources[1].description
  - taxonomy[0].evidence
  - taxonomy[1].evidence
  evidence_ids:
  - exudate-supplement
  - local-transfer
  - starch-mechanism
  - ontology
  - semantics
  - history
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Chlorella_Azospirillum_Synthetic_Mutualism.yaml
    role: canonical_record
- finding_id: historical-strain-provenance
  issue_key: cm-000191-historical-strain-provenance
  category: provenance
  severity: minor
  native_severity: P3
  normalization_reason: 'P3: bounded historical resource-provenance correction preserves
    current membership and graph.'
  rule_id: review-checklist.claim-specific-scope-and-evidence
  status: open
  certainty: confirmed
  title: Reconcile the predecessor’s historical algal name and culture-number conflict
  description: The predecessor explicitly reports UTEX 2714 under C. vulgaris, while
    focal sources call the same accession C. sorokiniana, formerly C. vulgaris. The
    different-Chlorella-species explanation is misleading. Its reported Cd/DSM 7030
    conflicts with current catalogue identity and cannot be silently treated as DSM
    1843 or as proof that an unrelated bacterium was studied.
  target_ids:
  - CommunityMech:000191
  field_paths:
  - external_resources[3].description
  - external_resources[3].evidence[0].explanation
  evidence_ids:
  - identity
  - predecessor
  - catalogues
  - historical-number
  - historical-context
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Chlorella_Azospirillum_Synthetic_Mutualism.yaml
    role: canonical_record
actions:
- action_id: separate-cultivation-contexts
  description: Recover exact study- and stage-specific culture representations.
  finding_ids:
  - assay-specific-media
  target_ids:
  - CommunityMech:000191
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Chlorella_Azospirillum_Synthetic_Mutualism.yaml
    role: canonical_record
  acceptance_checks:
  - Remove the generic implication that Trp and IAA are universal basal ingredients.
    Represent Trp 1.5 µg/mL with or without thiamine diphosphate 70 ng/mL only in
    the FEMS bacterial control/supplement conditions, and synthetic IAA only in its
    distinct algal comparator. Keep measured or proposed exchanged metabolites in
    their appropriate biological context.
  - Separate 2018 C30 algal and BTB-2 bacterial precultures from the 12-hour NB/OAB/SGM
    comparison and subsequent common SGM phase through 83 hours. Record source-supported
    27±2 C, 140 rpm and 60 µmol photons/m²/s for the illuminated assay. Scope 32±2
    C, 120 rpm and 16 hours to bacterial preculture, and seven days to algal preculture.
  - 'Represent 2018 3 mm beads and 20 g/150 mL Methods separately from its 100 mL/250
    mL statistics statement; preserve NB 10% v/v versus figure 10% w/v as an unresolved
    source presentation difference. Do not silently choose one value or infer SGM
    is N-free: its Methods includes NH4Cl 191 mg/L.'
  - Represent the FEMS 2 mm bead, 24-hour recovery and 120-hour exudate/supplement
    experiments separately. Preserve its Methods 20 g/150 mL versus statistics 300
    mL/500 mL and counting-section 250 mL flask references. Do not transfer the separate
    algal exudate assay’s 120 rpm to all 140 rpm experiments.
  - Represent the starch assay as 3–4 mm beads, 24-hour NB or OAB recovery, 12 g/150
    mL in 250 mL flasks, glucose 10 g/L and N-replete versus no-added-ammonium SGM
    arms, dark aerobic conditions at 27±2 C and 140 rpm. Preserve Methods 96 hours
    versus displayed 120-hour endpoints. Use printed 47.5 ng/µL in section 2.3 and
    48 ng/µL in section 2.6 as attributed synthetic-IAA statements; do not reproduce
    the text-extraction ng/mL error.
  - Read source medium rows and hydrate/unit strings before populating quantities.
    Nutrient Table S1 uses BTB-2 gluconate whereas the starch paper uses glycerol;
    their common name does not justify recipe merging. pH 8 is analytical bead dissolution
    and starch BTB-2 pH 7 is bacterial preculture, not a universal coculture setpoint.
    No numerical culture pH or salinity should be invented.
  - Move bead setup information to an appropriate cultivation/experimental description
    and keep environmental light/aerobic statements explicitly scoped. Attach short,
    exact source evidence and precise section/figure/table locators to each recovered
    condition. Preserve rights-restricted source bodies outside the repository; do
    not merge three full texts into one cache or invent a cross-Mech medium ID.
- action_id: qualify-nongraph-exchange
  description: Align ingredient, design, resource and role evidence with measured
    versus inferred processes.
  finding_ids:
  - nongraph-exchange-scope
  target_ids:
  - CommunityMech:000191
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Chlorella_Azospirillum_Synthetic_Mutualism.yaml
    role: canonical_record
  acceptance_checks:
  - Distinguish measured algal Trp release, bacterial exudate use and Trp-plus-TPP
    supplementation from inferred local transfer in co-immobilized cultures. State
    bulk coculture Trp/IAA non-detection and its analytical limit where relevant;
    absence from bulk medium does not prove or disprove local transfer.
  - Qualify related_ingredients thiamine/IAA relevance and explanations, engineering
    measurement language and the FEMS external-resource description. The supplemented
    chemical is thiamine diphosphate, but the endogenous extracellular form is not
    identified by that intervention; do not automatically substitute a TPP ontology
    ID as the secreted species.
  - Attach narrow source evidence to the retained functional roles. Preserve primary
    production in illuminated context, bacterial use of algal resources and source-qualified
    reciprocal metabolic/signaling interpretation. Do not impose a new obligacy, thermodynamic-removal
    or carbon-assimilation definition, and do not infer algal IAA catabolism from
    a response assay.
  - Preserve all four nodes and two downstream arrows, including PARTIAL IAA-to-starch
    support and HYPOTHESIZED aggregation-to-growth mediation. Keep IPDC specificity/taxon
    limits, Sp6-derived mutant versus focal Cd, dark glucose assay versus illuminated
    growth, nonsignificant Cd N-starvation correlation and starch-versus-fitness distinctions
    explicit.
  - Use current open issue 1297 for this non-graph follow-up and preserve closed 1295
    graph-repair history. The FEMS selected-excerpt cache label is already corrected;
    do not reopen it as an unresolved abstract-only defect or create a duplicate issue.
- action_id: correct-historical-resource-context
  description: Correct the predecessor identity explanation while preserving unresolved
    source attribution.
  finding_ids:
  - historical-strain-provenance
  target_ids:
  - CommunityMech:000191
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Chlorella_Azospirillum_Synthetic_Mutualism.yaml
    role: canonical_record
  acceptance_checks:
  - Replace the categorical different-Chlorella-species explanation with the directly
    verified same UTEX 2714 accession under historical C. vulgaris naming and focal
    C. sorokiniana designation. This applies to the inspected predecessor, not every
    historical paper using the old name.
  - Preserve that the predecessor reports Cd as DSM 7030 and that the current catalogue
    for that number is unrelated to Cd. Do not silently correct the paper, claim an
    alias, infer its actual organism was Paenibacillus, or alter the focal verified
    Cd/DSM 1843 assignment.
  - Keep predecessor bibliography and the exact identity paragraph as bounded context.
    Do not transfer its protocol, population effects or mechanisms into the three
    focal assays. No dedicated dataset accession or CultureMech mapping is invented
    from resource-name similarity.
- action_id: validate-authorized-curation
  description: When a separate curation task is authorized, preserve provenance and
    run the native completion gates.
  finding_ids:
  - assay-specific-media
  - nongraph-exchange-scope
  - historical-strain-provenance
  target_ids:
  - CommunityMech:000191
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Chlorella_Azospirillum_Synthetic_Mutualism.yaml
    role: canonical_record
  acceptance_checks:
  - Apply only separately authorized maintained-input corrections, append a fresh
    curation-history entry, and retain source/version/locator and existing issue ownership.
    Recheck every changed scientific claim against its exact source rather than merely
    matching its snippet.
  - Run the documented focused schema, strict, term, GTDB/domain, reference, cache-name
    and history checks. Verify the four-node/two-arrow graph and preserve the existing
    evidence-support qualifiers; report any remaining unavailable source or unresolved
    source contradiction.
  - After canonical curation, run just gen-html and just check-docs-current with the
    required project environment, inspecting generated changes for the intended record.
    This review performs no canonical, source-cache, history or generator mutation;
    persistence is limited to its new immutable review bundle.
limitations:
- Completed scientific review is bounded to current encoded claims. All three scientific
  main texts, all 17 main figures, both main Table 1 inventories and every nutrient
  Table S1 cell were inspected. Starch supplementary Table S1 and Figure S1 remain
  unread after ordinary source discovery; no exact SI-only bacterial growth curve/rate
  is certified.
- The predecessor source was assessed only for title/abstract and the complete organism-identity
  Methods paragraph. The same UTEX 2714 historical name is established, but the reported
  Cd/DSM 7030 number remains inconsistent with current catalogue identity. Focal DSM
  1843 is independently verified. No older protocol is imported.
- Exudate use and cofactor supplementation are experiments; precise bead-local transfer
  and the extracellular thiamine species are inferences or unresolved. IPDC has other
  substrates and an algal contribution. Broad retained roles do not imply direct local
  flux, a strict trophic-assimilation test, obligatory syntrophy or algal IAA catabolism.
- The illuminated nutrient study has source conflicts in 150 versus 100 mL fill and
  NB dilution basis. FEMS has 150 versus 300 mL assay descriptions and different flask
  references. Starch Methods specifies 96 hours while Results/figures extend to 120
  hours. These are reported with source attribution, not merged into a fabricated
  common protocol.
- Starch printed Methods IAA dose is 47.5 ng/µL, with 48 ng/µL in statistics. PDF
  extraction incorrectly renders the micro-prefix as m; the page images were inspected
  directly. Figure axes have independently printed µg/mL. Source C30 macro/trace units
  and nutrient BTB-2 gluconate versus starch BTB-2 glycerol are preserved rather than
  normalized using external standard recipes.
- Analytical bead-dissolution pH 8, extraction buffers and enzyme assay temperatures
  are not culture setpoints. Precursor cultivation and bead recovery differ from the
  final experiments. Initial N-free OAB, later ammonium-containing SGM and no-added-ammonium
  dark assays must remain distinct.
- The source FEMS significance prose includes P>0.05 alongside significance statements,
  while captions specify P<0.05; its transformed-expression axis includes negative
  values. The starch narrative overgeneralizes the Cd N-starvation correlation and
  compares a Sp6-derived mutant. These source presentation/mechanism limits are retained
  without new statistical or causal reanalysis.
- All 32 snippets are source-supported, with 31 strict fresh matches and one documented
  FEMS unit typography projection. Cache matching separately has one sentence-initial
  capitalization projection. The FEMS cache is correctly labeled selected abstract
  and Methods excerpts; it is not a full main cache. The other caches remain their
  actual bounded contents.
- The GTDB species-name fallback is correctly disclosed and matches the local authority,
  but does not classify the focal Cd genome. UTEX catalogue heading and explicit reidentification
  note must be read together. No new exact-strain taxonomy, chemical-form identity
  or cross-Mech recipe equivalence is inferred.
- Resource discovery is bounded to the cited source statements and exact publisher
  assets. No dedicated new study-deposition accession was established, which is not
  proof that data do not exist. The reported primer reference is not certified as
  a Cd genome or new community dataset. No raw payloads, experimental replication
  or code analysis was performed.
- All eight focused native checks pass and all 27 official inputs remain unchanged.
  Corpus-wide nonzero diagnostics retain their wider warning scope. Completeness 95
  and quality 100/raw 113 do not erase the two major and one minor findings. No canonical,
  cache, history, generated or previously saved artifact was changed; no paid provider
  or author contact was used.
notes:
- All 27 official inspected inputs remain unchanged; no canonical, cache, history,
  generated or previously saved artifact was edited.
- Lead and root independently assessed all three scientific mains and all 17 main
  figures with exact supplemental/historical scopes. Child owns immutable native/ontology
  receipts; sibling owns provenance/resources/snippets and score arithmetic.
- Two major and one minor findings give raw quality 113/capped 100; completeness is
  95. Current open issue 1297 owns the follow-up. The existing graph and broad source-qualified
  roles are retained.
tags:
- record-review
- algal-bacterial-mutualism
- main-and-critical-si-assessed
- batch-10
```
