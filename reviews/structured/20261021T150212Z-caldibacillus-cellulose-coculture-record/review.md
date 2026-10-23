# Caldibacillus–Clostridium aerotolerant cellulose coculture review

- Review: 20261021T150212Z-caldibacillus-cellulose-coculture-record
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-21T14:54:00.884200Z
- Finished UTC: 2026-10-21T15:02:12.671358Z
- Reviewer: codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The full primary main, four tables and Figure 1 support the defined pair and its qualified three-node, one-arrow graph. Three minor findings concern cultivation/oxygen context, narrow functional/lactate qualification and exact strain/sequence provenance. Local oxygen depletion and donor-resolved transfer remain proposed.

## Scope And Provenance

Whole canonical record and every node/arrow assessed against direct main/table/figure evidence, authority, archive metadata, history and native checks.

Selection: Only released CommunityMech:000179 in the owned batch 09 checkout.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f491097e6f3cd52baf6c2e89b3e614756ebce558.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000179 | kb/communities/Caldibacillus_Clostridium_Aerotolerant_Cellulose_Coculture.yaml | maintained | Caldibacillus-Clostridium Aerotolerant Cellulose Coculture |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000179 | Schema validation passed. |
| validate-strict | passed | True | CommunityMech:000179 | Strict validation passed. |
| validate-terms | passed | True | CommunityMech:000179 | Term validation passed. |
| validate-gtdb | passed | True | CommunityMech:000179 | GTDB syntax/status validation passed. |
| validate-gtdb-domain | passed | True | CommunityMech:000179 | GTDB domain validation passed. |
| validate-history | passed | True | CommunityMech:000179 | History validation passed. |
| normalize-cache-names-check | passed | True | CommunityMech:000179 | Read-only cache-name preflight passed. |
| validate-references-explained | passed | True | CommunityMech:000179 | Reference validation passed against the pinned abstract caches. |
| audit-network | failed | True | CommunityMech:000179 | Fresh batch 09 corpus diagnostics report 57 warnings across 21 of 477 communities; the focal graph separately reports COMPLETE. |
| check-network-quality | failed | True | CommunityMech:000179 | Fresh batch 09 corpus diagnostics report 57 warnings across 21 of 477 communities; the focal graph separately reports COMPLETE. |
| Primary scientific review | passed | True | CommunityMech:000179 | Complete current-claim assessment of direct main, all four tables and Figure 1; no linked scientific supplement identified in the inspected HTML. |
| Strain and sequence resource identity | passed | True | CommunityMech:000179 | Direct bounded catalogue/nucleotide metadata separates focal strains, GB1 markers and reference/comparator genomes. |
| Source-linked scientific supplementary assets | not_applicable | False | CommunityMech:000179 | No scientific supplement identified in the inspected article text/anchors. EPMC’s non-OA endpoint response is not treated as a missing required asset. |
| Earlier modified1191 base recipe | skipped | False | CommunityMech:000179 | The cited precursor recipe was not fully reviewed. Only current-source modifications/conditions are certified; no exact external recipe mapping is proposed. |
| Optional expression-module adapter | unavailable | False | CommunityMech:000179 | No applicable expression-module source established; discovery is recorded without biological absence inference. |

## Scientific And Domain Assessments

### Defined pair and strain scope

identity: supported. Targets: CommunityMech:000179.

Retain the two species and source-defined GB1/DSM 1237 pair, separately from B4-1 and the type comparator.

### State, origin and category

scope: supported. Targets: CommunityMech:000179.

Retain ENGINEERED, SYNTHETIC and LIGNOCELLULOSE.

The defined laboratory pairing was deliberately assembled for cellulose conversion. Its origin differs from the antecedent natural enrichment. No claim of ecological equilibrium or replacement state is needed.

### taxonomy[0:2] functional roles

evidence: concern. Targets: CommunityMech:000179.

Retain the supported degradation/fermentation roles with narrow evidence and explicitly inferred GB1 recipient scope.

Current snippets identify members or their antecedent consortium, rather than establishing every role in the defined pair. Whole-source substrate assays and combined phenotype support a bounded cross-feeding inference; no direct transfer assay is invented and no extra requirement that the primary degrader be another species is imposed.

### ecological_interactions[0]

graph: supported. Targets: CommunityMech:000179.

Respiratory protection is supported while its local oxygen mechanism remains hypothesized.

Bulk oxygen persisted. The source does not establish an unaffected GB1 partner or measure local gradients; the record correctly omits a commensalism sign assignment.

### ecological_interactions[0].downstream[0]

graph: supported. Targets: CommunityMech:000179.

Retain the PARTIAL protection-to-aerotolerant-conversion edge.

The combined phenotype supports the enabling link. It does not demonstrate the exact microscopic oxygen-removal route or justify restoring the removed lactate-response edge.

### ecological_interactions[1]

graph: supported. Targets: CommunityMech:000179.

Retain the transient aerobic ethanol endpoint and explicitly partial substrate-transfer interpretation.

Table 3 verifies 5.5 mM ethanol at 72 h and below detection at 168 h for the defined pair. Pure-culture substrate use supports the authors’ proposal but does not assign coculture exchange flux. B4-1 results stay separate.

### ecological_interactions[2]

graph: supported. Targets: CommunityMech:000179.

Retain the time-bounded lactate response with proposed stress and partner attribution.

The existing node already reports the 72 h increase and subsequent decline without converting an endpoint into commensalism or a proven molecular response.

### related_ingredients[0:2]

evidence: concern. Targets: CommunityMech:000179.

Cellulose identity is sound; the lactate explanation needs the graph’s existing comparator/time boundaries.

The C. debilis type strain is a comparator, not GB1’s parent. Source experiments distinguish pure-strain physiology from the defined-pair response. Do not assert that the pair/type comparison established the lactate effect or that lactate remained elevated at 168 h.

### growth_media[0] and cultivation_setup

completeness: concern. Targets: CommunityMech:000179.

Recover the actual assay context and avoid an unmeasured aerobic-preference claim.

The brief abstract-based entry omits available medium modifications, temperature, pH, adaptation, inoculum and bottle/fill/agitation/timing. Use assay-specific air/anaerobic conditions and the appropriate enum/notes; do not infer uniformly oxic conditions at the strict anaerobe’s surface.

### Structured strains and archive resources

provenance: concern. Targets: CommunityMech:000179.

The source provides exact strain/marker identities not yet represented in the record.

Add optional traceability at its correct scope. A marker sequence is not a whole genome, and the DSM 16016 reference genome is not GB1. Current species identity is not false merely because an exact strain field is incomplete.

### Historical repair and source limitations

provenance: supported. Targets: CommunityMech:000179.

Preserve the qualified graph and the prior removed edge.

The prior decision’s bounded scope is preserved; current issue 1270 also concerns another record. No issue closure, curation/history event or scientific-status promotion is performed.

### Native and semantic checks

schema: supported. Targets: CommunityMech:000179.

All eight focused native checks pass; three source-specific minor findings remain.

### Native completeness and validation quality

completeness: supported. Targets: CommunityMech:000179.

Scores describe encoded fields and validation, not source truth.

## Findings

### cultivation-context: Recover assay-specific cultivation and oxygen context

minor / open / confirmed; issue key: cm-000179-cultivation-context.

The abstract-based medium entry omits directly available method details. FACULTATIVE_AEROBIC additionally asserts aerobic preference, which is not established for this pair; the study compares aerobic and anaerobic operation.

### claim-qualification: Carry source qualifiers into taxon roles and lactate explanation

minor / open / confirmed; issue key: cm-000179-claim-qualification.

Local taxonomy snippets mainly establish membership, including the antecedent enrichment, while the full source supports narrower defined-pair roles and proposed GB1 transfer. The ingredient wording conflates type-strain comparison with a time-bounded coculture lactate response and calls the comparator a parent.

### strain-resource-provenance: Add exact strain and sequence-resource traceability

minor / open / confirmed; issue key: cm-000179-strain-resource-provenance.

DSM 1237 and GB1’s DSM 29516 deposit, plus two GB1 marker sequences, are recoverable. The publication-only resource list lacks these scoped identities; reference/comparator genomes must remain distinct.

## Recommended Actions And Acceptance Checks

### recover-cultivation

Represent the defined-pair assay separately from pure-culture screens and physiological preferences.

- Record modified 1191 medium with yeast extract 0.76 g/L and initial pH 7.2, and 5 g/L cellulose for the Table 3 defined pair. Do not import the 2 g/L screen or pure-GB1 cellobiose as universal pair conditions; do not invent the unread base recipe or a CultureMech identifier.
- Record 60 °C, one adaptation passage, 10% inoculum and triplicate experiments; attach 110 mL serum bottles, 10 mL medium/100 mL headspace, 75 rpm and 72/168 h sampling to the appropriate defined-pair assays. Do not confuse these with 26 mL Balch tubes or static 48 h screens.
- Replace or qualify FACULTATIVE_AEROBIC so no aerobic preference is asserted. FACULTATIVE_ANAEROBIC is available for growth with or without oxygen; separate operational air/anaerobic conditions in notes or scoped entries, retaining air without added sodium sulfide for the aerobic preparation and the cited method boundary for anaerobic preparation.
- Keep bulk oxygen persistence distinct from a hypothesized reduced local microenvironment. Retain the current three nodes/one PARTIAL arrow; rerun schema, strict, terms, references, GTDB/domain and history validation after separately authorized curation.

### qualify-functional-evidence

Attach narrow functional support and synchronize non-graph claims with existing graph limits.

- Use source passages about the defined DSM 1237/GB1 pair and substrate assays for roles, instead of treating an enrichment-membership excerpt as full functional support. Preserve primary-degrader/fermentation roles; do not require a different species as the primary degrader.
- Retain GB1 CROSS_FEEDER only with explicit source-inferred/proposed transfer scope at its evidence/notes. The combined phenotype and pure-substrate assays do not resolve donor-specific coculture flux; no obligacy or unsupported reciprocal-fitness claim is added.
- Describe DSM 16016 as a separate type-strain comparator, not GB1’s parent. Bound lactate increase to the 72 h oxidative condition and retain its decline by 168 h; separate pure-strain physiology from the pair response and keep partner/stress attribution proposed.
- Do not restore the removed protection-to-lactate edge or change supported cellulose/ethanol/lactate identities. Exact new snippets must come from the relevant source and remain compatible with the reference-cache workflow.

### resolve-strain-resources

Add verified strain and marker-sequence links with explicit reference/comparator scope.

- Add DSM 1237 to the C. thermocellum strain representation and DSM 29516 as a verified GB1 deposit alias, using the source/catalogue identities. Current species-level grounding is compatible; no automatic strain-level NCBI or GTDB replacement is required.
- Link KF652080.1 as GB1 partial 16S and KP259875.1 as GB1 complete GroEL/cpn60 coding sequence. Give the resource’s actual scope; neither is a GB1 whole-genome deposit.
- If NC_009012.1 is added, describe the member-reference chromosome and verified ATCC 27405/DSM 1237 identity. Keep NZ_ARVR00000000.1 as the DSM 16016 comparator WGS master, not GB1 or a third member. Do not treat master-record sequence length as a genome assembly length.
- Preserve the source purity-paragraph inconsistency explicitly: DSM 16016 there conflicts with GB1 throughout the defined-pair experiment. Do not silently resolve it by substituting the type strain, and do not copy catalogue maintenance conditions into the focal assay.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | kb/communities/Caldibacillus_Clostridium_Aerotolerant_Cellulose_Coculture.yaml; Entire canonical record; all three nodes and one arrow | supports | The target represents a defined thermophilic cellulose-converting pair. Its graph already distinguishes respiratory protection from a proposed oxygen microenvironment, inferred substrate exchange and transient ethanol accumulation. |
| pubmed | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=26048931&amp;retmode=xml; Article identity and available metadata | supports | Direct title, abstract and article IDs identify the focal 2015 paper. |
| epmc | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:26048931%20AND%20SRC:MED&amp;format=json&amp;resultType=core; Article identity and available metadata | supports | Article identity agrees; free PMC availability does not mean the separate full-text API provides XML. |
| crossref | https://api.crossref.org/works/10.1128/AEM.00735-15; Article identity and available metadata | supports | The DOI resolves to the same focal article; bibliographic identity does not establish a separate dataset. |
| pair-identity | PMID:26048931; Introduction aims; Methods: Culturing method; Results: Caldibacillus strain comparison | supports | The defined pair is C. thermocellum DSM 1237 plus C. debilis GB1, deposited as DSM 29516. B4-1 is the antecedent enrichment containing an uncharacterized C. thermocellum-like organism; DSM 16016 is a separate C. debilis type-strain comparator. |
| medium | PMID:26048931; Methods: Culturing method; Table 3 footnotes | supports | All experiments use modified 1191 medium with yeast extract 0.76 g/L and initial pH 7.2. Table 3 defined-pair experiments use cellulose 5 g/L; pure GB1 uses cellobiose 5 g/L. The 2 g/L substrate screen and full base formulation cited to an earlier paper are separate scopes. |
| cultivation | PMID:26048931; Methods: Cell growth; Tables 3–4 | supports | The cultures are adapted by one prior passage and inoculated at 10%, in triplicate. Defined-pair assays use 60 °C, 110 mL serum bottles with 10 mL medium/100 mL headspace, 75 rpm, and sampling at 72/168 h. Aerobic preparation uses air without added sodium sulfide; the anaerobic preparation follows a cited method. These are prescribed conditions, not GB1 physiological preference. |
| roles | PMID:26048931; Results: strain comparison and coculture; Discussion: coculture; Tables 1, 3, 4 | supports | C. thermocellum hydrolyses cellulose and ferments its breakdown products. GB1 uses cellobiose and can ferment under anaerobic conditions; pure-culture assays show aerobic ethanol/acetate consumption. The authors propose utilization of released cellobiose and fermentation products in the pair, without resolving donor-specific flux. |
| protection | PMID:26048931; Results and Discussion: C. debilis plus C. thermocellum coculture; Conclusion | supports | Aerobic cellulose conversion occurs in the pair while bulk oxygen and oxidized resazurin remain. Local oxygen depletion, oxygen-scavenging enzymes and a biofilm microenvironment are proposed explanations. Unaffected GB1 fitness is not established, so the record appropriately avoids COMMENSALISM typing. |
| products | PMID:26048931; Table 3 defined-pair rows and footnotes; Results: coculture; Figure 1 | supports | The defined pair has aerobic ethanol 5.5 mM at 72 h and below detection at 168 h, and lactate 6.6 then 1.3 mM. Anaerobic ethanol 6.3 mM at 72 h differs from monoculture 4.2 mM in the reported Welch test. The figure concerns 72 h endpoints; the separate B4-1 enrichment must not supply defined-pair outcomes. |
| lactate | PMID:26048931; Tables 1, 3, 4; Discussion: strain comparison and coculture | supports | The type strain DSM 16016 and GB1 have distinct pure-culture product profiles. The coculture lactate increase is a 72 h oxidative response followed by lower 168 h concentration; stress and partner attribution remain proposed. Calling DSM 16016 the GB1 parent or treating that comparator as the basis of the pair’s lactate effect conflates the experiments. |
| source-conflict | PMID:26048931; Methods: Culture purity confirmation; Introduction/Results/Discussion focal-pair identity | supports | The purity paragraph names DSM 16016 for the coculture, conflicting with the remainder of the paper’s GB1-defined pair. Preserve this source discrepancy rather than replacing GB1 with the type strain or certifying the inconsistent sentence as exact strain evidence. |
| source-archives | PMID:26048931; Methods: Bioinformatic analyses and Nucleotide sequence accession numbers; Results: strain comparison | supports | The paper deposits GB1 partial 16S and cpn60 sequences as KF652080/KP259875. NC_009012 is the C. thermocellum member-reference genome, while NZ_ARVR01000000 is the different DSM 16016 type-strain genome used for comparisons, not a GB1 genome. |
| figure | PMID:26048931; Figure 1 pixels and caption | supports | Figure 1 separates pure cultures, the defined pair and B4-1 across oxygen conditions. It compares reported 72 h ethanol and glucose-equivalent summaries; no numeric extraction from bars or independent carbon-balance calculation was performed. |
| schema | src/communitymech/schema/communitymech.yaml; MicrobialCommunity; FunctionalRoleEnum; AtmosphereEnum; GrowthMedia; CultivationSetup | supports | CROSS_FEEDER denotes use of another taxon’s metabolites. SECONDARY_FERMENTER does not explicitly require another species as the primary degrader. FACULTATIVE_AEROBIC asserts aerobic preference, while FACULTATIVE_ANAEROBIC permits growth with or without oxygen. Optional cultivation/state fields are not mandatory merely because they improve completeness. |
| ontology | ontology-authority.json; Whole bounded frozen receipt | supports | All encoded ontology labels were freshly checked against local authority; no taxonomy or chemical-ID correction is required. |
| semantics | ontology-semantic-notes.json; Whole bounded frozen receipt | supports | Species-level taxonomy/GTDB mapping remains compatible. Functional roles must retain source inference and atmosphere must not assert an unmeasured preference. |
| catalogues | child-strain-authority.json; Whole bounded frozen receipt | supports | Direct DSMZ catalogue verifies DSM 1237 aliases. GB1/DSM 29516 is verified from the source and directly opened DSMZ BacDive identity, while its catalogue result is indexed-only and direct catalogue attempts failed. Maintenance conditions are excluded from the focal assay. |
| resources | dataset-verification.json; Whole bounded frozen receipt | supports | Bounded nucleotide metadata verifies GB1 markers and separates member/reference and comparator genomes; no raw sequences or new GB1 genome are certified. |
| snippets | snippet-audit.json; Whole bounded frozen receipt | supports | All sixteen existing snippets match the direct abstract and the full article including that abstract, as well as both pinned abstract caches. No body-excluding-abstract literal match is claimed; lexical agreement does not establish every nearby explanation. |
| history | provenance-audit.json; Whole bounded frozen receipt | supports | Both histories and the exact prior decision were read. Current issue 1270 preserves qualified exchange and the removed protection-to-lactate edge; broader issue scope is retained. |
| native-target | support-audit.json; Whole bounded frozen receipt | supports | Native graph COMPLETE: three nodes, one arrow, five node-evidence entries. Completeness 85 and capped quality 100 are mechanical diagnostics, not scientific certification. |
| source-scope | source-audit.json; Whole bounded frozen receipt | supports | The entire current record was assessed using the full scientific main, all four tables, Figure 1 and bounded authority/archive checks; source discrepancies remain explicit. |
| target-metadata | lead-target-metadata-normalization.json; Whole bounded frozen receipt | supports | Candidate target kind is normalized to the schema’s maintained value, adding explicit MicrobialCommunity class; original inspect/source bytes remain unchanged. |
| lead-read | lead-primary-read-scope.json; Whole bounded frozen receipt | supports | Pins actual root-retrieved PMC HTML reused by lead, complete text/table reading and Figure 1 viewing. No linked scientific SI was identified in the inspected article scope. |
| independent-source | root-independent-source-audit.json; Whole bounded frozen receipt | supports | Root independently read the full scientific main/tables and Figure 1 and agrees with the three minor findings and completion boundary. |
| access-fulltext | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4510191/fullTextXML; Preserved actual access request | supports | EPMC returned an error rather than main XML. |
| access-pmc-html | https://pmc.ncbi.nlm.nih.gov/articles/PMC4510191/; Preserved actual access request | supports | The lead initial PMC response was a CAPTCHA page, distinct from the later successful root article. |
| access-publisher | https://journals.asm.org/doi/10.1128/AEM.00735-15; Preserved actual access request | supports | The direct ASM route returned 403. |
| access-supplement-zip | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4510191/supplementaryFiles; Preserved actual access request | supports | The endpoint returned a non-open-access error, not a ZIP or evidence that scientific SI exists. |
| access-epmc-html | https://europepmc.org/articles/PMC4510191; Preserved actual access request | supports | The ordinary EuropePMC HTML route returned 403. |
| access-epmc-pdf | https://europepmc.org/articles/PMC4510191?pdf=render; Preserved actual access request | supports | The ordinary EuropePMC PDF route returned 403. |
| adapter | adapter-check.json; Fresh optional structured-adapter discovery | supports | No applicable structured expression-module evidence was established; optional discovery is not negative biological evidence. |
| check-validate | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src just --no-dotenv validate kb/communities/Caldibacillus_Clostridium_Aerotolerant_Cellulose_Coculture.yaml; Actual execution 2026-10-21T14:55:00.679115+00:00 to 2026-10-21T14:55:02.409499+00:00 | supports | Schema validation passed. |
| check-validate-strict | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src just --no-dotenv validate-strict kb/communities/Caldibacillus_Clostridium_Aerotolerant_Cellulose_Coculture.yaml --out /private/tmp/cm-review-session/batch-09/000179/strict-report.tsv; Actual execution 2026-10-21T14:55:00.679450+00:00 to 2026-10-21T14:55:05.366302+00:00 | supports | Strict validation passed. |
| check-validate-terms | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src just --no-dotenv validate-terms kb/communities/Caldibacillus_Clostridium_Aerotolerant_Cellulose_Coculture.yaml; Actual execution 2026-10-21T14:55:00.679657+00:00 to 2026-10-21T14:55:04.269249+00:00 | supports | Term validation passed. |
| check-validate-gtdb | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src just --no-dotenv validate-gtdb kb/communities/Caldibacillus_Clostridium_Aerotolerant_Cellulose_Coculture.yaml; Actual execution 2026-10-21T14:55:02.410337+00:00 to 2026-10-21T14:55:02.606984+00:00 | supports | GTDB syntax/status validation passed. |
| check-validate-gtdb-domain | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src just --no-dotenv validate-gtdb-domain kb/communities/Caldibacillus_Clostridium_Aerotolerant_Cellulose_Coculture.yaml; Actual execution 2026-10-21T14:55:02.607345+00:00 to 2026-10-21T14:55:05.416771+00:00 | supports | GTDB domain validation passed. |
| check-validate-history | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src just --no-dotenv validate-history history/records/Caldibacillus_Clostridium_Aerotolerant_Cellulose_Coculture; Actual execution 2026-10-21T14:55:04.269631+00:00 to 2026-10-21T14:55:05.520628+00:00 | supports | History validation passed. |
| check-normalize-cache-names-check | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src uv run python scripts/normalize_cache_names.py --check; Actual execution 2026-10-21T14:55:05.521512+00:00 to 2026-10-21T14:55:05.607003+00:00 | supports | Read-only cache-name preflight passed. |
| check-validate-references-explained | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src just --no-dotenv validate-references-explained kb/communities/Caldibacillus_Clostridium_Aerotolerant_Cellulose_Coculture.yaml; Actual execution 2026-10-21T14:55:05.607335+00:00 to 2026-10-21T14:55:06.976204+00:00 | supports | Reference validation passed against the pinned abstract caches. |
| check-audit-network | PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv audit-network; Actual execution 2026-10-21T14:53:06.814378+00:00 to 2026-10-21T14:53:14.616064+00:00 | supports | Fresh batch 09 corpus diagnostics report 57 warnings across 21 of 477 communities; the focal graph separately reports COMPLETE. |
| check-check-network-quality | PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv check-network-quality; Actual execution 2026-10-21T14:53:06.817734+00:00 to 2026-10-21T14:53:14.704428+00:00 | supports | Fresh batch 09 corpus diagnostics report 57 warnings across 21 of 477 communities; the focal graph separately reports COMPLETE. |

## Limits And Additional Notes

- No raw sequences, genome reannotation, statistical reanalysis or model execution. Primary gas/HPLC and derived glucose-equivalent measures are assessed as reported.
- The source culture-purity paragraph names DSM 16016 while the remainder of the defined-pair experiment identifies GB1; retain this internal discrepancy and do not substitute the comparator into the community.
- The modified 1191 base recipe is cited to an earlier method that was not fully reviewed; only source-reported modifications and current assay conditions are verified. No unique CultureMech formulation is asserted.
- Static Balch-tube substrate screens and shaken serum-bottle defined-pair experiments differ. Table 3 cultures use 5 g/L cellulose, except pure GB1 cellobiose; the 2 g/L screen is not a universal coculture concentration.
- No quantitative partner abundance, spatial oxygen profile or donor-resolved transfer is measured here. Inferred roles and local protection must not become unqualified mechanism claims.
- No linked scientific SI was identified within the full primary HTML, its article anchors or source text. EPMC supplementaryFiles returned a non-OA error rather than a supplement; no generic absence outside this inspected scope is claimed.
- Catalogue identities and archived sequence metadata do not make catalogue maintenance conditions the focal protocol or make the DSM 16016 genome a GB1 genome.
- Only the released record was assessed; prior decisions and issue 1270 have their original multi-target scopes and are not closed or superseded by this review.
- No canonical, cache, history, generated or saved-review file changed; all 25 inspected inputs remain pinned.
- Sixteen existing snippets match direct primary sources and both abstract-only caches. Complete main text was inspected without changing cache bytes.
- Completeness 85 and quality 100/raw 125.6666666667 are mechanical scores, not scientific certification.
- No raw sequence/statistical reanalysis, model execution, paid provider, author contact or later-target review.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T150212Z-caldibacillus-cellulose-coculture-record
kind: record
repository: CultureBotAI/CommunityMech
title: Caldibacillus–Clostridium aerotolerant cellulose coculture review
started_at: '2026-10-21T14:54:00.884200Z'
finished_at: '2026-10-21T15:02:12.671358Z'
reviewer:
  identity: codex
  kind: agent
  independence: unknown
  independence_basis: Separate agents reviewed primary science, native/ontology checks
    and supporting provenance; no person-level independence asserted.
skill: review-yaml-record
completion: completed
verdict: needs_curation
scientific_review: true
summary: The full primary main, four tables and Figure 1 support the defined pair
  and its qualified three-node, one-arrow graph. Three minor findings concern cultivation/oxygen
  context, narrow functional/lactate qualification and exact strain/sequence provenance.
  Local oxygen depletion and donor-resolved transfer remain proposed.
source:
  git_revision: f491097e6f3cd52baf6c2e89b3e614756ebce558
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
  - path: history/records/Caldibacillus_Clostridium_Aerotolerant_Cellulose_Coculture/2026-10-02T053712Z-codex-c8a4f0.yaml
    sha256: 075000e83fc564c6730c0c5cb2d24fc047781d8248ec8a664730e5a90c74caff
    role: context
  - path: history/records/Caldibacillus_Clostridium_Aerotolerant_Cellulose_Coculture/2026-10-05T155420Z-codex-85e288.yaml
    sha256: 28163a21ce80cd144266333db5352ea2624a9d318c85df4ead98ed87cec24e02
    role: context
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: kb/communities/Caldibacillus_Clostridium_Aerotolerant_Cellulose_Coculture.yaml
    sha256: 0d0ed40c05ec1cf70a99a4f012b65726cbdffa775db503b905e6cbf932ea6b24
    role: target
  - path: references_cache/PMID_26048931.txt
    sha256: f799ae2a2486f86e8e102aaf132a339a4e9491101a952efa2d65a41d8dc770ac
    role: context
  - path: references_cache/doi_10.1128_AEM.00735-15.md
    sha256: 117ac360c70d6219537953d9f059267269cbb81f6539f1e312db2c478cec325d
    role: context
  - path: reports/causal_graph_review/decisions/20261005-thermophile-pair-batch9.yaml
    sha256: 2e3b83e265ad0016f87051af9e80d4f825f78eeeebf9b29192e27e9c3675424f
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
- target_id: CommunityMech:000179
  path: kb/communities/Caldibacillus_Clostridium_Aerotolerant_Cellulose_Coculture.yaml
  label: Caldibacillus-Clostridium Aerotolerant Cellulose Coculture
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Caldibacillus_Clostridium_Aerotolerant_Cellulose_Coculture.yaml
    role: canonical_record
  record_class: MicrobialCommunity
scope:
  description: Whole canonical record and every node/arrow assessed against direct
    main/table/figure evidence, authority, archive metadata, history and native checks.
  selection: Only released CommunityMech:000179 in the owned batch 09 checkout.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000179
checks:
- check_id: validate
  name: validate
  status: passed
  required: true
  summary: Schema validation passed.
  target_ids:
  - CommunityMech:000179
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src
    just --no-dotenv validate kb/communities/Caldibacillus_Clostridium_Aerotolerant_Cellulose_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate
  scope_note: Fresh focused native check; mechanical validity does not prove claim-specific
    support, physiological preference or resolved exchange flux.
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Strict validation passed.
  target_ids:
  - CommunityMech:000179
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src
    just --no-dotenv validate-strict kb/communities/Caldibacillus_Clostridium_Aerotolerant_Cellulose_Coculture.yaml
    --out /private/tmp/cm-review-session/batch-09/000179/strict-report.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-strict
  scope_note: Fresh focused native check; mechanical validity does not prove claim-specific
    support, physiological preference or resolved exchange flux.
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Term validation passed.
  target_ids:
  - CommunityMech:000179
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src
    just --no-dotenv validate-terms kb/communities/Caldibacillus_Clostridium_Aerotolerant_Cellulose_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-terms
  scope_note: Fresh focused native check; mechanical validity does not prove claim-specific
    support, physiological preference or resolved exchange flux.
- check_id: validate-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: GTDB syntax/status validation passed.
  target_ids:
  - CommunityMech:000179
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src
    just --no-dotenv validate-gtdb kb/communities/Caldibacillus_Clostridium_Aerotolerant_Cellulose_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb
  scope_note: Fresh focused native check; mechanical validity does not prove claim-specific
    support, physiological preference or resolved exchange flux.
- check_id: validate-gtdb-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: GTDB domain validation passed.
  target_ids:
  - CommunityMech:000179
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src
    just --no-dotenv validate-gtdb-domain kb/communities/Caldibacillus_Clostridium_Aerotolerant_Cellulose_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb-domain
  scope_note: Fresh focused native check; mechanical validity does not prove claim-specific
    support, physiological preference or resolved exchange flux.
- check_id: validate-history
  name: validate-history
  status: passed
  required: true
  summary: History validation passed.
  target_ids:
  - CommunityMech:000179
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src
    just --no-dotenv validate-history history/records/Caldibacillus_Clostridium_Aerotolerant_Cellulose_Coculture
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-history
  scope_note: Fresh focused native check; mechanical validity does not prove claim-specific
    support, physiological preference or resolved exchange flux.
- check_id: normalize-cache-names-check
  name: normalize-cache-names-check
  status: passed
  required: true
  summary: Read-only cache-name preflight passed.
  target_ids:
  - CommunityMech:000179
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src
    uv run python scripts/normalize_cache_names.py --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-normalize-cache-names-check
  scope_note: Fresh focused native check; mechanical validity does not prove claim-specific
    support, physiological preference or resolved exchange flux.
- check_id: validate-references-explained
  name: validate-references-explained
  status: passed
  required: true
  summary: Reference validation passed against the pinned abstract caches.
  target_ids:
  - CommunityMech:000179
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src
    just --no-dotenv validate-references-explained kb/communities/Caldibacillus_Clostridium_Aerotolerant_Cellulose_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-references-explained
  scope_note: Fresh focused native check; mechanical validity does not prove claim-specific
    support, physiological preference or resolved exchange flux.
- check_id: audit-network
  name: audit-network
  status: failed
  required: true
  summary: Fresh batch 09 corpus diagnostics report 57 warnings across 21 of 477 communities;
    the focal graph separately reports COMPLETE.
  target_ids:
  - CommunityMech:000179
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv audit-network
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-audit-network
  - native-target
  scope_note: Explicit same-batch corpus receipt reuse. Existing corpus warnings are
    neither concealed nor attributed to this focal record.
- check_id: check-network-quality
  name: check-network-quality
  status: failed
  required: true
  summary: Fresh batch 09 corpus diagnostics report 57 warnings across 21 of 477 communities;
    the focal graph separately reports COMPLETE.
  target_ids:
  - CommunityMech:000179
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv check-network-quality
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-check-network-quality
  - native-target
  scope_note: Explicit same-batch corpus receipt reuse. Existing corpus warnings are
    neither concealed nor attributed to this focal record.
- check_id: scientific-source
  name: Primary scientific review
  status: passed
  required: true
  summary: Complete current-claim assessment of direct main, all four tables and Figure
    1; no linked scientific supplement identified in the inspected HTML.
  target_ids:
  - CommunityMech:000179
  evidence_ids:
  - source-scope
  - independent-source
  - lead-read
- check_id: archive-identity
  name: Strain and sequence resource identity
  status: passed
  required: true
  summary: Direct bounded catalogue/nucleotide metadata separates focal strains, GB1
    markers and reference/comparator genomes.
  target_ids:
  - CommunityMech:000179
  evidence_ids:
  - catalogues
  - resources
- check_id: supplements
  name: Source-linked scientific supplementary assets
  status: not_applicable
  required: false
  summary: No scientific supplement identified in the inspected article text/anchors.
    EPMC’s non-OA endpoint response is not treated as a missing required asset.
  target_ids:
  - CommunityMech:000179
  evidence_ids:
  - lead-read
  - access-supplement-zip
- check_id: full-base-recipe
  name: Earlier modified1191 base recipe
  status: skipped
  required: false
  summary: The cited precursor recipe was not fully reviewed. Only current-source
    modifications/conditions are certified; no exact external recipe mapping is proposed.
  target_ids:
  - CommunityMech:000179
  evidence_ids:
  - medium
  - source-scope
- check_id: structured-adapter
  name: Optional expression-module adapter
  status: unavailable
  required: false
  summary: No applicable expression-module source established; discovery is recorded
    without biological absence inference.
  target_ids:
  - CommunityMech:000179
  evidence_ids:
  - adapter
evidence:
- evidence_id: record
  kind: record_content
  reference: kb/communities/Caldibacillus_Clostridium_Aerotolerant_Cellulose_Coculture.yaml
  locator: Entire canonical record; all three nodes and one arrow
  summary: The target represents a defined thermophilic cellulose-converting pair.
    Its graph already distinguishes respiratory protection from a proposed oxygen
    microenvironment, inferred substrate exchange and transient ethanol accumulation.
  support: supports
  accessed_at: '2026-10-21T15:02:12.658310Z'
- evidence_id: pubmed
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=26048931&retmode=xml
  locator: Article identity and available metadata
  summary: Direct title, abstract and article IDs identify the focal 2015 paper.
  support: supports
  accessed_at: '2026-10-21T14:54:37.698118Z'
  snapshot_sha256: ac8b1c43706b04717934db1828a4f28ee2d17f96e3e3b0b4a6a2996628e2fca9
- evidence_id: epmc
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:26048931%20AND%20SRC:MED&format=json&resultType=core
  locator: Article identity and available metadata
  summary: Article identity agrees; free PMC availability does not mean the separate
    full-text API provides XML.
  support: supports
  accessed_at: '2026-10-21T14:54:38.031636Z'
  snapshot_sha256: f83cb71cbf3f15448487ea4dcd60358ba57bcef574bea33368389fc162f86f02
- evidence_id: crossref
  kind: database
  reference: https://api.crossref.org/works/10.1128/AEM.00735-15
  locator: Article identity and available metadata
  summary: The DOI resolves to the same focal article; bibliographic identity does
    not establish a separate dataset.
  support: supports
  accessed_at: '2026-10-21T14:54:37.655831Z'
  snapshot_sha256: 8b04294f9d98e0d8f0ca4a9295b131c4a0ca2a11bdaf987725fb0b56e3b560d6
- evidence_id: pair-identity
  kind: primary_source
  reference: PMID:26048931
  locator: 'Introduction aims; Methods: Culturing method; Results: Caldibacillus strain
    comparison'
  summary: The defined pair is C. thermocellum DSM 1237 plus C. debilis GB1, deposited
    as DSM 29516. B4-1 is the antecedent enrichment containing an uncharacterized
    C. thermocellum-like organism; DSM 16016 is a separate C. debilis type-strain
    comparator.
  support: supports
  accessed_at: '2026-10-21T15:02:12.661402Z'
  snapshot_sha256: 2f65c1981455a8c7e9c38a5bcd4267cc90d5ccf8f64f2393fe7f04f996711ba9
- evidence_id: medium
  kind: primary_source
  reference: PMID:26048931
  locator: 'Methods: Culturing method; Table 3 footnotes'
  summary: All experiments use modified 1191 medium with yeast extract 0.76 g/L and
    initial pH 7.2. Table 3 defined-pair experiments use cellulose 5 g/L; pure GB1
    uses cellobiose 5 g/L. The 2 g/L substrate screen and full base formulation cited
    to an earlier paper are separate scopes.
  support: supports
  accessed_at: '2026-10-21T15:02:12.661578Z'
  snapshot_sha256: 2f65c1981455a8c7e9c38a5bcd4267cc90d5ccf8f64f2393fe7f04f996711ba9
- evidence_id: cultivation
  kind: primary_source
  reference: PMID:26048931
  locator: 'Methods: Cell growth; Tables 3–4'
  summary: The cultures are adapted by one prior passage and inoculated at 10%, in
    triplicate. Defined-pair assays use 60 °C, 110 mL serum bottles with 10 mL medium/100
    mL headspace, 75 rpm, and sampling at 72/168 h. Aerobic preparation uses air without
    added sodium sulfide; the anaerobic preparation follows a cited method. These
    are prescribed conditions, not GB1 physiological preference.
  support: supports
  accessed_at: '2026-10-21T15:02:12.661749Z'
  snapshot_sha256: 2f65c1981455a8c7e9c38a5bcd4267cc90d5ccf8f64f2393fe7f04f996711ba9
  quote: All experiments were carried out in triplicate
- evidence_id: roles
  kind: primary_source
  reference: PMID:26048931
  locator: 'Results: strain comparison and coculture; Discussion: coculture; Tables
    1, 3, 4'
  summary: C. thermocellum hydrolyses cellulose and ferments its breakdown products.
    GB1 uses cellobiose and can ferment under anaerobic conditions; pure-culture assays
    show aerobic ethanol/acetate consumption. The authors propose utilization of released
    cellobiose and fermentation products in the pair, without resolving donor-specific
    flux.
  support: supports
  accessed_at: '2026-10-21T15:02:12.661855Z'
  snapshot_sha256: 2f65c1981455a8c7e9c38a5bcd4267cc90d5ccf8f64f2393fe7f04f996711ba9
- evidence_id: protection
  kind: primary_source
  reference: PMID:26048931
  locator: 'Results and Discussion: C. debilis plus C. thermocellum coculture; Conclusion'
  summary: Aerobic cellulose conversion occurs in the pair while bulk oxygen and oxidized
    resazurin remain. Local oxygen depletion, oxygen-scavenging enzymes and a biofilm
    microenvironment are proposed explanations. Unaffected GB1 fitness is not established,
    so the record appropriately avoids COMMENSALISM typing.
  support: supports
  accessed_at: '2026-10-21T15:02:12.661951Z'
  snapshot_sha256: 2f65c1981455a8c7e9c38a5bcd4267cc90d5ccf8f64f2393fe7f04f996711ba9
- evidence_id: products
  kind: primary_source
  reference: PMID:26048931
  locator: 'Table 3 defined-pair rows and footnotes; Results: coculture; Figure 1'
  summary: The defined pair has aerobic ethanol 5.5 mM at 72 h and below detection
    at 168 h, and lactate 6.6 then 1.3 mM. Anaerobic ethanol 6.3 mM at 72 h differs
    from monoculture 4.2 mM in the reported Welch test. The figure concerns 72 h endpoints;
    the separate B4-1 enrichment must not supply defined-pair outcomes.
  support: supports
  accessed_at: '2026-10-21T15:02:12.662042Z'
  snapshot_sha256: 2f65c1981455a8c7e9c38a5bcd4267cc90d5ccf8f64f2393fe7f04f996711ba9
- evidence_id: lactate
  kind: primary_source
  reference: PMID:26048931
  locator: 'Tables 1, 3, 4; Discussion: strain comparison and coculture'
  summary: The type strain DSM 16016 and GB1 have distinct pure-culture product profiles.
    The coculture lactate increase is a 72 h oxidative response followed by lower
    168 h concentration; stress and partner attribution remain proposed. Calling DSM
    16016 the GB1 parent or treating that comparator as the basis of the pair’s lactate
    effect conflates the experiments.
  support: supports
  accessed_at: '2026-10-21T15:02:12.662138Z'
  snapshot_sha256: 2f65c1981455a8c7e9c38a5bcd4267cc90d5ccf8f64f2393fe7f04f996711ba9
- evidence_id: source-conflict
  kind: primary_source
  reference: PMID:26048931
  locator: 'Methods: Culture purity confirmation; Introduction/Results/Discussion
    focal-pair identity'
  summary: The purity paragraph names DSM 16016 for the coculture, conflicting with
    the remainder of the paper’s GB1-defined pair. Preserve this source discrepancy
    rather than replacing GB1 with the type strain or certifying the inconsistent
    sentence as exact strain evidence.
  support: supports
  accessed_at: '2026-10-21T15:02:12.662235Z'
  snapshot_sha256: 2f65c1981455a8c7e9c38a5bcd4267cc90d5ccf8f64f2393fe7f04f996711ba9
- evidence_id: source-archives
  kind: primary_source
  reference: PMID:26048931
  locator: 'Methods: Bioinformatic analyses and Nucleotide sequence accession numbers;
    Results: strain comparison'
  summary: The paper deposits GB1 partial 16S and cpn60 sequences as KF652080/KP259875.
    NC_009012 is the C. thermocellum member-reference genome, while NZ_ARVR01000000
    is the different DSM 16016 type-strain genome used for comparisons, not a GB1
    genome.
  support: supports
  accessed_at: '2026-10-21T15:02:12.662333Z'
  snapshot_sha256: 2f65c1981455a8c7e9c38a5bcd4267cc90d5ccf8f64f2393fe7f04f996711ba9
- evidence_id: figure
  kind: primary_source
  reference: PMID:26048931
  locator: Figure 1 pixels and caption
  summary: Figure 1 separates pure cultures, the defined pair and B4-1 across oxygen
    conditions. It compares reported 72 h ethanol and glucose-equivalent summaries;
    no numeric extraction from bars or independent carbon-balance calculation was
    performed.
  support: supports
  accessed_at: '2026-10-21T15:02:12.662756Z'
  snapshot_sha256: fbdb7c1b705fc285d9fed8c87fabc33f8805e5508149267909b38a08215e0c0d
- evidence_id: schema
  kind: authority
  reference: src/communitymech/schema/communitymech.yaml
  locator: MicrobialCommunity; FunctionalRoleEnum; AtmosphereEnum; GrowthMedia; CultivationSetup
  summary: CROSS_FEEDER denotes use of another taxon’s metabolites. SECONDARY_FERMENTER
    does not explicitly require another species as the primary degrader. FACULTATIVE_AEROBIC
    asserts aerobic preference, while FACULTATIVE_ANAEROBIC permits growth with or
    without oxygen. Optional cultivation/state fields are not mandatory merely because
    they improve completeness.
  support: supports
  accessed_at: '2026-10-21T15:02:12.662856Z'
  snapshot_sha256: c41630d09def826256ddb6678c1ce31fa71e3b074219bb9d217d98035a5324ee
- evidence_id: ontology
  kind: authority
  reference: ontology-authority.json
  locator: Whole bounded frozen receipt
  summary: All encoded ontology labels were freshly checked against local authority;
    no taxonomy or chemical-ID correction is required.
  support: supports
  accessed_at: '2026-10-21T15:02:12.663101Z'
  snapshot_sha256: ce890325fbb3d6a5efcdc3edfc21c65b174a864bea3c5a4e3e3444eaadc92114
- evidence_id: semantics
  kind: authority
  reference: ontology-semantic-notes.json
  locator: Whole bounded frozen receipt
  summary: Species-level taxonomy/GTDB mapping remains compatible. Functional roles
    must retain source inference and atmosphere must not assert an unmeasured preference.
  support: supports
  accessed_at: '2026-10-21T15:02:12.663303Z'
  snapshot_sha256: 9713ecba9a44562899262dd9a06f9175bde9c215b21d0fb0da29e245a18ec10a
- evidence_id: catalogues
  kind: authority
  reference: child-strain-authority.json
  locator: Whole bounded frozen receipt
  summary: Direct DSMZ catalogue verifies DSM 1237 aliases. GB1/DSM 29516 is verified
    from the source and directly opened DSMZ BacDive identity, while its catalogue
    result is indexed-only and direct catalogue attempts failed. Maintenance conditions
    are excluded from the focal assay.
  support: supports
  accessed_at: '2026-10-21T15:02:12.663583Z'
  snapshot_sha256: fa021e18547b09ee259a21d8dd9d237c162d5afb0c6317aaefa9fcc6ed860038
- evidence_id: resources
  kind: database
  reference: dataset-verification.json
  locator: Whole bounded frozen receipt
  summary: Bounded nucleotide metadata verifies GB1 markers and separates member/reference
    and comparator genomes; no raw sequences or new GB1 genome are certified.
  support: supports
  accessed_at: '2026-10-21T15:02:12.663723Z'
  snapshot_sha256: a55a52e0d142c972ffc50dc980e3928a182c459b098dfd4cf54416101bd99d52
- evidence_id: snippets
  kind: validation
  reference: snippet-audit.json
  locator: Whole bounded frozen receipt
  summary: All sixteen existing snippets match the direct abstract and the full article
    including that abstract, as well as both pinned abstract caches. No body-excluding-abstract
    literal match is claimed; lexical agreement does not establish every nearby explanation.
  support: supports
  accessed_at: '2026-10-21T15:02:12.663878Z'
  snapshot_sha256: c3f581805f4f7246d91759e3cd3dfdd1be35d638cf58bfcc98b95e99a05de9bc
- evidence_id: history
  kind: record_content
  reference: provenance-audit.json
  locator: Whole bounded frozen receipt
  summary: Both histories and the exact prior decision were read. Current issue 1270
    preserves qualified exchange and the removed protection-to-lactate edge; broader
    issue scope is retained.
  support: supports
  accessed_at: '2026-10-21T15:02:12.664021Z'
  snapshot_sha256: 2a3ab45026d3dd0128a4af4e126929fa0accee28b6e183231ff48d7e2bd3e35b
- evidence_id: native-target
  kind: validation
  reference: support-audit.json
  locator: Whole bounded frozen receipt
  summary: 'Native graph COMPLETE: three nodes, one arrow, five node-evidence entries.
    Completeness 85 and capped quality 100 are mechanical diagnostics, not scientific
    certification.'
  support: supports
  accessed_at: '2026-10-21T15:02:12.664068Z'
  snapshot_sha256: 8463b1beaecad2a29a2a2a6921c80fea2816ddcf7288aafbfb1df3f55f737ee8
- evidence_id: source-scope
  kind: validation
  reference: source-audit.json
  locator: Whole bounded frozen receipt
  summary: The entire current record was assessed using the full scientific main,
    all four tables, Figure 1 and bounded authority/archive checks; source discrepancies
    remain explicit.
  support: supports
  accessed_at: '2026-10-21T15:02:12.664109Z'
  snapshot_sha256: b36442c10dbd01b141c80a890026f4c5726a54306d367c88f4d5db8fb97ce696
- evidence_id: target-metadata
  kind: validation
  reference: lead-target-metadata-normalization.json
  locator: Whole bounded frozen receipt
  summary: Candidate target kind is normalized to the schema’s maintained value, adding
    explicit MicrobialCommunity class; original inspect/source bytes remain unchanged.
  support: supports
  accessed_at: '2026-10-21T15:02:12.664246Z'
  snapshot_sha256: 1b5410bde5adb1f5d3980be7e8afe4653e3a25bc0e51f8f574b1c648dc3f2408
- evidence_id: lead-read
  kind: validation
  reference: lead-primary-read-scope.json
  locator: Whole bounded frozen receipt
  summary: Pins actual root-retrieved PMC HTML reused by lead, complete text/table
    reading and Figure 1 viewing. No linked scientific SI was identified in the inspected
    article scope.
  support: supports
  accessed_at: '2026-10-21T15:02:12.664392Z'
  snapshot_sha256: 5166379768aaa976ba5f77feb212d4924c8fe8f9c53739624eb94bb72e52a4a1
- evidence_id: independent-source
  kind: validation
  reference: root-independent-source-audit.json
  locator: Whole bounded frozen receipt
  summary: Root independently read the full scientific main/tables and Figure 1 and
    agrees with the three minor findings and completion boundary.
  support: supports
  accessed_at: '2026-10-21T15:02:12.664539Z'
  snapshot_sha256: 47cf27e7afdca7d386b70a397f71a6c90b169f97735ab94c0c757dbc0395d13a
- evidence_id: access-fulltext
  kind: validation
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4510191/fullTextXML
  locator: Preserved actual access request
  summary: EPMC returned an error rather than main XML.
  support: supports
  accessed_at: '2026-10-21T14:54:50.236075Z'
  snapshot_sha256: 5c8516817e1dcd2a24e37a8617c97e9f81cb70a8f14859f714d20297abfc80d2
- evidence_id: access-pmc-html
  kind: validation
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC4510191/
  locator: Preserved actual access request
  summary: The lead initial PMC response was a CAPTCHA page, distinct from the later
    successful root article.
  support: supports
  accessed_at: '2026-10-21T14:54:49.999848Z'
  snapshot_sha256: c0edacba37415a3d5874c7e0f8a1aceeda096ddbf549b82996b07a01b852e20d
- evidence_id: access-publisher
  kind: validation
  reference: https://journals.asm.org/doi/10.1128/AEM.00735-15
  locator: Preserved actual access request
  summary: The direct ASM route returned 403.
  support: supports
  accessed_at: '2026-10-21T14:54:37.465149Z'
  snapshot_sha256: dd8ee340611b79214a2f5ba4aeda523672e1d401a1a571113ac9b93e3e433a53
- evidence_id: access-supplement-zip
  kind: validation
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4510191/supplementaryFiles
  locator: Preserved actual access request
  summary: The endpoint returned a non-open-access error, not a ZIP or evidence that
    scientific SI exists.
  support: supports
  accessed_at: '2026-10-21T14:54:50.100567Z'
  snapshot_sha256: fdc1a135101e581a2ed273221269876290b2a8db6aab8d370cf018ae12ba58b3
- evidence_id: access-epmc-html
  kind: validation
  reference: https://europepmc.org/articles/PMC4510191
  locator: Preserved actual access request
  summary: The ordinary EuropePMC HTML route returned 403.
  support: supports
  accessed_at: '2026-10-21T14:55:11.306791Z'
  snapshot_sha256: 0d8d5708fa92e368a6bdbbdf50f1e1ca36890100658991dc8a577269c99ca042
- evidence_id: access-epmc-pdf
  kind: validation
  reference: https://europepmc.org/articles/PMC4510191?pdf=render
  locator: Preserved actual access request
  summary: The ordinary EuropePMC PDF route returned 403.
  support: supports
  accessed_at: '2026-10-21T14:55:11.305517Z'
  snapshot_sha256: c3db5e151f8048ad283f81bcf03ee008843f1205690b8f4e849b8dccd5307b57
- evidence_id: adapter
  kind: validation
  reference: adapter-check.json
  locator: Fresh optional structured-adapter discovery
  summary: No applicable structured expression-module evidence was established; optional
    discovery is not negative biological evidence.
  support: supports
  accessed_at: '2026-10-21T15:02:12.666015Z'
  snapshot_sha256: eac8e40311ba26e375de8c4e306249d8b93bba480a22bac469c193b48d521236
- evidence_id: check-validate
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src
    just --no-dotenv validate kb/communities/Caldibacillus_Clostridium_Aerotolerant_Cellulose_Coculture.yaml
  locator: Actual execution 2026-10-21T14:55:00.679115+00:00 to 2026-10-21T14:55:02.409499+00:00
  summary: Schema validation passed.
  support: supports
  accessed_at: '2026-10-21T14:55:02.409499Z'
  snapshot_sha256: 9b0a1ad4a7448a27e9223fb6035843f77d4ebf0456ad7c706bf1c8996e77890a
- evidence_id: check-validate-strict
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src
    just --no-dotenv validate-strict kb/communities/Caldibacillus_Clostridium_Aerotolerant_Cellulose_Coculture.yaml
    --out /private/tmp/cm-review-session/batch-09/000179/strict-report.tsv
  locator: Actual execution 2026-10-21T14:55:00.679450+00:00 to 2026-10-21T14:55:05.366302+00:00
  summary: Strict validation passed.
  support: supports
  accessed_at: '2026-10-21T14:55:05.366302Z'
  snapshot_sha256: 780f549eb089c0dbac7e6fb98ab472ca05f4521a5e06e4b488c1fb506e336139
- evidence_id: check-validate-terms
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src
    just --no-dotenv validate-terms kb/communities/Caldibacillus_Clostridium_Aerotolerant_Cellulose_Coculture.yaml
  locator: Actual execution 2026-10-21T14:55:00.679657+00:00 to 2026-10-21T14:55:04.269249+00:00
  summary: Term validation passed.
  support: supports
  accessed_at: '2026-10-21T14:55:04.269249Z'
  snapshot_sha256: a0d612b4109b33ce0bb16851814c8035938fa6a41e423bc832772fce1de75f5a
- evidence_id: check-validate-gtdb
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src
    just --no-dotenv validate-gtdb kb/communities/Caldibacillus_Clostridium_Aerotolerant_Cellulose_Coculture.yaml
  locator: Actual execution 2026-10-21T14:55:02.410337+00:00 to 2026-10-21T14:55:02.606984+00:00
  summary: GTDB syntax/status validation passed.
  support: supports
  accessed_at: '2026-10-21T14:55:02.606984Z'
  snapshot_sha256: 655211f706c5853c1279699e1bab006848474faebe91f1422d985c0089a85a7e
- evidence_id: check-validate-gtdb-domain
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src
    just --no-dotenv validate-gtdb-domain kb/communities/Caldibacillus_Clostridium_Aerotolerant_Cellulose_Coculture.yaml
  locator: Actual execution 2026-10-21T14:55:02.607345+00:00 to 2026-10-21T14:55:05.416771+00:00
  summary: GTDB domain validation passed.
  support: supports
  accessed_at: '2026-10-21T14:55:05.416771Z'
  snapshot_sha256: dc92a8245d5aaa67279218b17842f7e73dbafd64f9ddd37c0ce600cba530efed
- evidence_id: check-validate-history
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src
    just --no-dotenv validate-history history/records/Caldibacillus_Clostridium_Aerotolerant_Cellulose_Coculture
  locator: Actual execution 2026-10-21T14:55:04.269631+00:00 to 2026-10-21T14:55:05.520628+00:00
  summary: History validation passed.
  support: supports
  accessed_at: '2026-10-21T14:55:05.520628Z'
  snapshot_sha256: 0c39855a7b5d60107c372df0d9660921953e95c626ec26c5fe75582dbbf15977
- evidence_id: check-normalize-cache-names-check
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src
    uv run python scripts/normalize_cache_names.py --check
  locator: Actual execution 2026-10-21T14:55:05.521512+00:00 to 2026-10-21T14:55:05.607003+00:00
  summary: Read-only cache-name preflight passed.
  support: supports
  accessed_at: '2026-10-21T14:55:05.607003Z'
  snapshot_sha256: 762d6e4d7c31c6b1d370e161df9a098134fe70a11d93b3b6218e5159b30d7102
- evidence_id: check-validate-references-explained
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src
    just --no-dotenv validate-references-explained kb/communities/Caldibacillus_Clostridium_Aerotolerant_Cellulose_Coculture.yaml
  locator: Actual execution 2026-10-21T14:55:05.607335+00:00 to 2026-10-21T14:55:06.976204+00:00
  summary: Reference validation passed against the pinned abstract caches.
  support: supports
  accessed_at: '2026-10-21T14:55:06.976204Z'
  snapshot_sha256: 83499ca1e3eb9e06804a014c8d13438cd82d6826723270f04fbbb5f0021f1565
- evidence_id: check-audit-network
  kind: validation
  reference: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv audit-network
  locator: Actual execution 2026-10-21T14:53:06.814378+00:00 to 2026-10-21T14:53:14.616064+00:00
  summary: Fresh batch 09 corpus diagnostics report 57 warnings across 21 of 477 communities;
    the focal graph separately reports COMPLETE.
  support: supports
  accessed_at: '2026-10-21T14:53:14.616064Z'
  snapshot_sha256: af46c37677bdc80eb1866f799958882492e9f72ed8eff4c304f69cd667f99156
- evidence_id: check-check-network-quality
  kind: validation
  reference: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv check-network-quality
  locator: Actual execution 2026-10-21T14:53:06.817734+00:00 to 2026-10-21T14:53:14.704428+00:00
  summary: Fresh batch 09 corpus diagnostics report 57 warnings across 21 of 477 communities;
    the focal graph separately reports COMPLETE.
  support: supports
  accessed_at: '2026-10-21T14:53:14.704428Z'
  snapshot_sha256: 6bf7d1eaf4ddc02de94aaea33610660d4b12689dc78ff47a6e29148baeffdd4f
assessments:
- assessment_id: identity
  area: identity
  topic: Defined pair and strain scope
  outcome: supported
  summary: Retain the two species and source-defined GB1/DSM 1237 pair, separately
    from B4-1 and the type comparator.
  target_ids:
  - CommunityMech:000179
  evidence_ids:
  - pair-identity
  - source-conflict
  - ontology
  - catalogues
  dimensions:
  - name: community_scope
    value: Defined two-member laboratory coculture
    definition: Neither the B4-1 enrichment nor the DSM 16016 comparator is silently
      substituted.
    evidence_ids:
    - pair-identity
  - name: strain
    value: C. thermocellum DSM 1237; C. debilis GB1/DSM 29516
    definition: Recoverable identifiers improve traceability while current species
      grounding remains compatible.
    evidence_ids:
    - pair-identity
    - catalogues
  - name: taxon_rank
    value: Species-level encoded NCBITaxon:1515 and NCBITaxon:301148
    definition: Paper legacy names and current canonical labels remain distinguishable.
    evidence_ids:
    - ontology
  - name: grounding_status
    value: Both GTDB species mappings retained
    definition: Local crosswalk checks do not newly classify the exact assay isolates.
    evidence_ids:
    - semantics
  - name: environment
    value: Controlled thermophilic laboratory cellulose assay
    definition: Air-exposed bulk medium and proposed local anoxia are not the same
      scale.
    evidence_ids:
    - protection
    - cultivation
  - name: medium
    value: Modified 1191 with assay-specific reported modifications
    definition: Earlier full base recipe was not independently reviewed or assigned
      a unique CultureMech link.
    evidence_ids:
    - medium
  - name: evidence_tier
    value: Full main, four tables, one figure and bounded archive/authority metadata
    definition: No donor-resolved flux, spatial oxygen measurement or raw-data reanalysis.
    evidence_ids:
    - source-scope
- assessment_id: state
  area: scope
  topic: State, origin and category
  outcome: supported
  summary: Retain ENGINEERED, SYNTHETIC and LIGNOCELLULOSE.
  target_ids:
  - CommunityMech:000179
  evidence_ids:
  - pair-identity
  - schema
  details: The defined laboratory pairing was deliberately assembled for cellulose
    conversion. Its origin differs from the antecedent natural enrichment. No claim
    of ecological equilibrium or replacement state is needed.
- assessment_id: roles
  area: evidence
  topic: taxonomy[0:2] functional roles
  outcome: concern
  summary: Retain the supported degradation/fermentation roles with narrow evidence
    and explicitly inferred GB1 recipient scope.
  target_ids:
  - CommunityMech:000179
  evidence_ids:
  - roles
  - schema
  - record
  details: Current snippets identify members or their antecedent consortium, rather
    than establishing every role in the defined pair. Whole-source substrate assays
    and combined phenotype support a bounded cross-feeding inference; no direct transfer
    assay is invented and no extra requirement that the primary degrader be another
    species is imposed.
- assessment_id: node-0
  area: graph
  topic: ecological_interactions[0]
  outcome: supported
  summary: Respiratory protection is supported while its local oxygen mechanism remains
    hypothesized.
  target_ids:
  - CommunityMech:000179
  evidence_ids:
  - protection
  - products
  details: Bulk oxygen persisted. The source does not establish an unaffected GB1
    partner or measure local gradients; the record correctly omits a commensalism
    sign assignment.
- assessment_id: arrow-0-1
  area: graph
  topic: ecological_interactions[0].downstream[0]
  outcome: supported
  summary: Retain the PARTIAL protection-to-aerotolerant-conversion edge.
  target_ids:
  - CommunityMech:000179
  evidence_ids:
  - protection
  - products
  - history
  details: The combined phenotype supports the enabling link. It does not demonstrate
    the exact microscopic oxygen-removal route or justify restoring the removed lactate-response
    edge.
- assessment_id: node-1
  area: graph
  topic: ecological_interactions[1]
  outcome: supported
  summary: Retain the transient aerobic ethanol endpoint and explicitly partial substrate-transfer
    interpretation.
  target_ids:
  - CommunityMech:000179
  evidence_ids:
  - products
  - roles
  - figure
  details: Table 3 verifies 5.5 mM ethanol at 72 h and below detection at 168 h for
    the defined pair. Pure-culture substrate use supports the authors’ proposal but
    does not assign coculture exchange flux. B4-1 results stay separate.
- assessment_id: node-2
  area: graph
  topic: ecological_interactions[2]
  outcome: supported
  summary: Retain the time-bounded lactate response with proposed stress and partner
    attribution.
  target_ids:
  - CommunityMech:000179
  evidence_ids:
  - lactate
  - products
  details: The existing node already reports the 72 h increase and subsequent decline
    without converting an endpoint into commensalism or a proven molecular response.
- assessment_id: ingredients
  area: evidence
  topic: related_ingredients[0:2]
  outcome: concern
  summary: Cellulose identity is sound; the lactate explanation needs the graph’s
    existing comparator/time boundaries.
  target_ids:
  - CommunityMech:000179
  evidence_ids:
  - medium
  - lactate
  - ontology
  details: The C. debilis type strain is a comparator, not GB1’s parent. Source experiments
    distinguish pure-strain physiology from the defined-pair response. Do not assert
    that the pair/type comparison established the lactate effect or that lactate remained
    elevated at 168 h.
- assessment_id: cultivation
  area: completeness
  topic: growth_media[0] and cultivation_setup
  outcome: concern
  summary: Recover the actual assay context and avoid an unmeasured aerobic-preference
    claim.
  target_ids:
  - CommunityMech:000179
  evidence_ids:
  - medium
  - cultivation
  - schema
  details: The brief abstract-based entry omits available medium modifications, temperature,
    pH, adaptation, inoculum and bottle/fill/agitation/timing. Use assay-specific
    air/anaerobic conditions and the appropriate enum/notes; do not infer uniformly
    oxic conditions at the strict anaerobe’s surface.
- assessment_id: resources
  area: provenance
  topic: Structured strains and archive resources
  outcome: concern
  summary: The source provides exact strain/marker identities not yet represented
    in the record.
  target_ids:
  - CommunityMech:000179
  evidence_ids:
  - source-archives
  - resources
  - catalogues
  - source-conflict
  details: Add optional traceability at its correct scope. A marker sequence is not
    a whole genome, and the DSM 16016 reference genome is not GB1. Current species
    identity is not false merely because an exact strain field is incomplete.
- assessment_id: history
  area: provenance
  topic: Historical repair and source limitations
  outcome: supported
  summary: Preserve the qualified graph and the prior removed edge.
  target_ids:
  - CommunityMech:000179
  evidence_ids:
  - history
  - snippets
  - source-scope
  details: The prior decision’s bounded scope is preserved; current issue 1270 also
    concerns another record. No issue closure, curation/history event or scientific-status
    promotion is performed.
- assessment_id: validation
  area: schema
  topic: Native and semantic checks
  outcome: supported
  summary: All eight focused native checks pass; three source-specific minor findings
    remain.
  target_ids:
  - CommunityMech:000179
  evidence_ids:
  - ontology
  - check-validate
  - check-validate-references-explained
  - native-target
- assessment_id: metrics
  area: completeness
  topic: Native completeness and validation quality
  outcome: supported
  summary: Scores describe encoded fields and validation, not source truth.
  target_ids:
  - CommunityMech:000179
  evidence_ids:
  - native-target
  metrics:
  - name: completeness
    value: 85
    unit: points
    minimum: 0
    maximum: 100
    definition: 50 required-field/taxon-role rubric points +5 environment +10 for
      at least three interaction nodes +5 external resources +10 growth medium +5
      metabolites. No three-factor or dataset bonus.
  - name: validation_quality
    value: 100
    unit: points
    minimum: 0
    maximum: 100
    definition: clamp(100−50P1−10P2−2P3+20 min(mean node evidence/2, 1)+15 if COMPLETE,
      0, 100). P1=0, P2=0, P3=3, P4=0; 5 evidence/3 nodes gives 16.6666666667; COMPLETE
      adds 15; raw 125.6666666667 capped 100.
  - name: P1
    value: 0
    unit: findings
    definition: Native severity count.
  - name: P2
    value: 0
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
- finding_id: cultivation-context
  issue_key: cm-000179-cultivation-context
  category: completeness
  severity: minor
  native_severity: P3
  normalization_reason: 'P3: bounded source-context, qualification or provenance repair;
    the community identity and qualified graph remain supported, and no optional field
    is treated as mandatory.'
  rule_id: review-checklist.claim-specific-scope-and-provenance
  status: open
  certainty: confirmed
  title: Recover assay-specific cultivation and oxygen context
  description: The abstract-based medium entry omits directly available method details.
    FACULTATIVE_AEROBIC additionally asserts aerobic preference, which is not established
    for this pair; the study compares aerobic and anaerobic operation.
  target_ids:
  - CommunityMech:000179
  field_paths:
  - growth_media[0]
  - cultivation_setup
  evidence_ids:
  - medium
  - cultivation
  - schema
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Caldibacillus_Clostridium_Aerotolerant_Cellulose_Coculture.yaml
    role: canonical_record
- finding_id: claim-qualification
  issue_key: cm-000179-claim-qualification
  category: evidence
  severity: minor
  native_severity: P3
  normalization_reason: 'P3: bounded source-context, qualification or provenance repair;
    the community identity and qualified graph remain supported, and no optional field
    is treated as mandatory.'
  rule_id: review-checklist.claim-specific-scope-and-provenance
  status: open
  certainty: confirmed
  title: Carry source qualifiers into taxon roles and lactate explanation
  description: Local taxonomy snippets mainly establish membership, including the
    antecedent enrichment, while the full source supports narrower defined-pair roles
    and proposed GB1 transfer. The ingredient wording conflates type-strain comparison
    with a time-bounded coculture lactate response and calls the comparator a parent.
  target_ids:
  - CommunityMech:000179
  field_paths:
  - taxonomy[0].evidence
  - taxonomy[1].evidence
  - taxonomy[1].taxon_term.notes
  - related_ingredients[1].relevance
  - related_ingredients[1].evidence[0].explanation
  evidence_ids:
  - roles
  - lactate
  - products
  - schema
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Caldibacillus_Clostridium_Aerotolerant_Cellulose_Coculture.yaml
    role: canonical_record
- finding_id: strain-resource-provenance
  issue_key: cm-000179-strain-resource-provenance
  category: provenance
  severity: minor
  native_severity: P3
  normalization_reason: 'P3: bounded source-context, qualification or provenance repair;
    the community identity and qualified graph remain supported, and no optional field
    is treated as mandatory.'
  rule_id: review-checklist.claim-specific-scope-and-provenance
  status: open
  certainty: confirmed
  title: Add exact strain and sequence-resource traceability
  description: DSM 1237 and GB1’s DSM 29516 deposit, plus two GB1 marker sequences,
    are recoverable. The publication-only resource list lacks these scoped identities;
    reference/comparator genomes must remain distinct.
  target_ids:
  - CommunityMech:000179
  field_paths:
  - taxonomy[0].strain_designation
  - taxonomy[1].strain_designation
  - associated_datasets
  - external_resources
  evidence_ids:
  - pair-identity
  - source-archives
  - resources
  - catalogues
  - source-conflict
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Caldibacillus_Clostridium_Aerotolerant_Cellulose_Coculture.yaml
    role: canonical_record
actions:
- action_id: recover-cultivation
  description: Represent the defined-pair assay separately from pure-culture screens
    and physiological preferences.
  finding_ids:
  - cultivation-context
  target_ids:
  - CommunityMech:000179
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Caldibacillus_Clostridium_Aerotolerant_Cellulose_Coculture.yaml
    role: canonical_record
  acceptance_checks:
  - Record modified 1191 medium with yeast extract 0.76 g/L and initial pH 7.2, and
    5 g/L cellulose for the Table 3 defined pair. Do not import the 2 g/L screen or
    pure-GB1 cellobiose as universal pair conditions; do not invent the unread base
    recipe or a CultureMech identifier.
  - Record 60 °C, one adaptation passage, 10% inoculum and triplicate experiments;
    attach 110 mL serum bottles, 10 mL medium/100 mL headspace, 75 rpm and 72/168
    h sampling to the appropriate defined-pair assays. Do not confuse these with 26
    mL Balch tubes or static 48 h screens.
  - Replace or qualify FACULTATIVE_AEROBIC so no aerobic preference is asserted. FACULTATIVE_ANAEROBIC
    is available for growth with or without oxygen; separate operational air/anaerobic
    conditions in notes or scoped entries, retaining air without added sodium sulfide
    for the aerobic preparation and the cited method boundary for anaerobic preparation.
  - Keep bulk oxygen persistence distinct from a hypothesized reduced local microenvironment.
    Retain the current three nodes/one PARTIAL arrow; rerun schema, strict, terms,
    references, GTDB/domain and history validation after separately authorized curation.
- action_id: qualify-functional-evidence
  description: Attach narrow functional support and synchronize non-graph claims with
    existing graph limits.
  finding_ids:
  - claim-qualification
  target_ids:
  - CommunityMech:000179
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Caldibacillus_Clostridium_Aerotolerant_Cellulose_Coculture.yaml
    role: canonical_record
  acceptance_checks:
  - Use source passages about the defined DSM 1237/GB1 pair and substrate assays for
    roles, instead of treating an enrichment-membership excerpt as full functional
    support. Preserve primary-degrader/fermentation roles; do not require a different
    species as the primary degrader.
  - Retain GB1 CROSS_FEEDER only with explicit source-inferred/proposed transfer scope
    at its evidence/notes. The combined phenotype and pure-substrate assays do not
    resolve donor-specific coculture flux; no obligacy or unsupported reciprocal-fitness
    claim is added.
  - Describe DSM 16016 as a separate type-strain comparator, not GB1’s parent. Bound
    lactate increase to the 72 h oxidative condition and retain its decline by 168
    h; separate pure-strain physiology from the pair response and keep partner/stress
    attribution proposed.
  - Do not restore the removed protection-to-lactate edge or change supported cellulose/ethanol/lactate
    identities. Exact new snippets must come from the relevant source and remain compatible
    with the reference-cache workflow.
- action_id: resolve-strain-resources
  description: Add verified strain and marker-sequence links with explicit reference/comparator
    scope.
  finding_ids:
  - strain-resource-provenance
  target_ids:
  - CommunityMech:000179
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Caldibacillus_Clostridium_Aerotolerant_Cellulose_Coculture.yaml
    role: canonical_record
  acceptance_checks:
  - Add DSM 1237 to the C. thermocellum strain representation and DSM 29516 as a verified
    GB1 deposit alias, using the source/catalogue identities. Current species-level
    grounding is compatible; no automatic strain-level NCBI or GTDB replacement is
    required.
  - Link KF652080.1 as GB1 partial 16S and KP259875.1 as GB1 complete GroEL/cpn60
    coding sequence. Give the resource’s actual scope; neither is a GB1 whole-genome
    deposit.
  - If NC_009012.1 is added, describe the member-reference chromosome and verified
    ATCC 27405/DSM 1237 identity. Keep NZ_ARVR00000000.1 as the DSM 16016 comparator
    WGS master, not GB1 or a third member. Do not treat master-record sequence length
    as a genome assembly length.
  - 'Preserve the source purity-paragraph inconsistency explicitly: DSM 16016 there
    conflicts with GB1 throughout the defined-pair experiment. Do not silently resolve
    it by substituting the type strain, and do not copy catalogue maintenance conditions
    into the focal assay.'
limitations:
- No raw sequences, genome reannotation, statistical reanalysis or model execution.
  Primary gas/HPLC and derived glucose-equivalent measures are assessed as reported.
- The source culture-purity paragraph names DSM 16016 while the remainder of the defined-pair
  experiment identifies GB1; retain this internal discrepancy and do not substitute
  the comparator into the community.
- The modified 1191 base recipe is cited to an earlier method that was not fully reviewed;
  only source-reported modifications and current assay conditions are verified. No
  unique CultureMech formulation is asserted.
- Static Balch-tube substrate screens and shaken serum-bottle defined-pair experiments
  differ. Table 3 cultures use 5 g/L cellulose, except pure GB1 cellobiose; the 2
  g/L screen is not a universal coculture concentration.
- No quantitative partner abundance, spatial oxygen profile or donor-resolved transfer
  is measured here. Inferred roles and local protection must not become unqualified
  mechanism claims.
- No linked scientific SI was identified within the full primary HTML, its article
  anchors or source text. EPMC supplementaryFiles returned a non-OA error rather than
  a supplement; no generic absence outside this inspected scope is claimed.
- Catalogue identities and archived sequence metadata do not make catalogue maintenance
  conditions the focal protocol or make the DSM 16016 genome a GB1 genome.
- Only the released record was assessed; prior decisions and issue 1270 have their
  original multi-target scopes and are not closed or superseded by this review.
notes:
- No canonical, cache, history, generated or saved-review file changed; all 25 inspected
  inputs remain pinned.
- Sixteen existing snippets match direct primary sources and both abstract-only caches.
  Complete main text was inspected without changing cache bytes.
- Completeness 85 and quality 100/raw 125.6666666667 are mechanical scores, not scientific
  certification.
- No raw sequence/statistical reanalysis, model execution, paid provider, author contact
  or later-target review.
tags:
- record-review
- cellulose
- thermophilic-coculture
- main-assessed
- batch-09
```
