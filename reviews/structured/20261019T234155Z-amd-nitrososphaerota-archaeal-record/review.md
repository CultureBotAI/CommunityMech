# AMD Nitrososphaerota archaeal record: whole-record scientific review

- Review: 20261019T234155Z-amd-nitrososphaerota-archaeal-record
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-19T23:34:06.330971Z
- Finished UTC: 2026-10-19T23:41:55.733353Z
- Reviewer: codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The four nodes and sole causal arrow preserve appropriate partial/hypothetical scope. Four major findings concern whole-community scope, organism mechanisms, environmental quantities and project genome attribution; one minor finding concerns metal classification/provenance. Approximately 54 Gb, three deposited genomes and Nitrososphaerota phylum membership are verified. All focused gates pass; corpus network warnings remain explicit.

## Scope And Provenance

Entire maintained community record, all four taxonomic entries, four nodes and one arrow, five factors, three ingredients, ontology meanings, source boundaries and public project provenance.

Selection: Sixth repository-relative target in the parent ordered corpus review. Exactly one resolved maintained record in this bundle; earlier reviews remain immutable.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base a4611c913c8da9619673df63a0c2cce3aa206a83.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000002 | kb/communities/AMD_Nitrososphaerota_Archaeal.yaml | maintained | AMD Nitrososphaerota Archaeal Community |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000002 | No issues found<br>uv run linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/AMD_Nitrososphaerota_Archaeal.yaml |
| validate-strict | passed | True | CommunityMech:000002 | uv run python scripts/validate_strict.py kb/communities/AMD_Nitrososphaerota_Archaeal.yaml --out /private/tmp/cm-review-session/000002/strict-report.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/communitymech-record-reviews-20261019/src/communitymech/schema/communitymech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cm-review-session/000002/strict-report.tsv |
| validate-terms | passed | True | CommunityMech:000002 | ✅ Validation passed<br>uv run linkml-term-validator validate-data kb/communities/AMD_Nitrososphaerota_Archaeal.yaml -s src/communitymech/schema/communitymech.yaml --labels |
| validate-gtdb | passed | True | CommunityMech:000002 | PYTHONPATH=src uv run python scripts/validate_gtdb_coherence.py kb/communities/AMD_Nitrososphaerota_Archaeal.yaml<br><br>files checked: 1<br>incoherent blocks: 0<br>malformed lineages: 0<br>lineage conflicts: 0 |
| validate-gtdb-domain | passed | True | CommunityMech:000002 | files checked: 1<br>contradictory lineages: 0<br>PYTHONPATH=src uv run python scripts/validate_prokaryotic_lineage.py kb/communities/AMD_Nitrososphaerota_Archaeal.yaml |
| validate-history | passed | True | CommunityMech:000002 | No issues found |
| normalize-cache-names | passed | False | CommunityMech:000002 | Actual command returned exit 0 with no issues or output. |
| validate-references-explained | passed | True | CommunityMech:000002 | Validating kb/communities/AMD_Nitrososphaerota_Archaeal.yaml against schema src/communitymech/schema/communitymech.yaml<br>Cache directory: references_cache<br><br>Validation Summary:<br>  Reported validation issues: 0<br>  All validations passed!<br><br>[annotate] This is not a count of checked excerpts (#1469). Native Discussion evidence coverage remains incomplete (#476). |
| audit-network | failed | True | CommunityMech:000002 | Actual full-corpus recipe exit 1: 462 records, 57 warnings in 21 records, zero errors. No AMD_Nitrososphaerota_Archaeal target findings. Reused same-session results against unchanged Git base and record bytes; other-record warnings are not assigned to this target. |
| check-network-quality | failed | True | CommunityMech:000002 | Actual full-corpus recipe exit 1: 462 records, 57 warnings in 21 records, zero errors. No AMD_Nitrososphaerota_Archaeal target findings. Reused same-session results against unchanged Git base and record bytes; other-record warnings are not assigned to this target. |
| Resolve iModulonDB structured adapter | unavailable | False | CommunityMech:000002 | No console runner on PATH or in the permitted own-checkout runtime; public source catalog fallback was inspected. |

## Scientific And Domain Assessments

### Canonical identity and community boundary

identity: concern. Targets: CommunityMech:000002.

The target is uniquely resolved as CommunityMech:000002. AMD nitrifier diversity is a supported ecological topic, but the record combines Colorado gene surveys, Indian archaeal amplicons, soil isolates and a separate biomining coculture into a fixed, stable community without same-system composition evidence. The graph recognizes this distinction; the description and taxon notes frequently do not.

### taxonomy[0]: Nitrosotalea identity, physiology, role and abundance

grounding: concern. Targets: CommunityMech:000002.

NCBITaxon:1078905 has canonical label Nitrosotalea devaniterrae; the preferred historical Ca. N. devanaterra wording and GTDB:s__Nitrosotalea devanaterra are retained separately and pass native coherence/domain checks. The soil isolate supports acidophilic autotrophy and AMO/Amt/potential homeostasis genes. It does not establish exact isolate presence, 30–45% abundance or the stated per-gram amoA counts in AMD. Urease attribution conflicts with its inspected genome; 0.6–2.8 nM Km and 100–120 h optimal doubling are not established by these citations. The 2014 Nd1 growth rate of 0.29/day implies about 57 h under that experiment, illustrating condition dependence rather than a replacement community doubling time.

### taxonomy[1]: Nitrososphaera-like archaeon

grounding: concern. Targets: CommunityMech:000002.

NCBITaxon:497726 and GTDB:g__Nitrososphaera are genus-level grounding. The AMD survey supports affiliated amoA sequences, not an identified strain or measured acid-growth optimum, cell size, urease/HAO expression, 50–200 mg N/L optimum, syntrophic partner, 15–25% abundance or per-gram gene count. PMID:24909965 studies two Nitrosotalea isolates and cannot establish the asserted Nitrososphaera acidophily.

### taxonomy[2]: Ferroplasma acidiphilum

grounding: concern. Targets: CommunityMech:000002.

NCBITaxon:74969 and the stored GTDB:s__Ferroplasma acidarmanus mapping pass native coherence/domain gates; the names are not independently rederived from genome mappings here. Malanjkhand V6 lineage evidence is broader than F. acidiphilum. BRL-115 chemomixotrophy is supported in a separate culture with Leptospirillum. This does not verify exact AMD abundance, AOA-directed detoxification, metal niche services, quantitative intracellular pH, iron-dominated cellular proteins, As/Cu/Zn resistance, or numeric pH/oxygen optima asserted for this guild. General cell-wall-free archaeal morphology does not supply these missing strain- and assay-specific measurements.

### taxonomy[3]: Nitrospira-like bacterium

grounding: concern. Targets: CommunityMech:000002.

NCBITaxon:1234 correctly denotes genus Nitrospira; GTDB is explicitly withheld rather than guessed. nxrB affiliations support nitrite-oxidation potential. The duplicated PMID:29209281 excerpts do not independently verify nitrite removal, partner rescue, comammox activity at 380 mg N/L, 30% relative abundance or 10^3–10^4 nxrB/g. The original assay units and generally higher nxrB counts differ.

### ecological_interactions[0]: Archaeal Ammonia Oxidation to Nitrite

graph: supported. Targets: CommunityMech:000002.

PARTIAL is appropriate. Source physiology shows soil Nitrosotalea converts ammonia to nitrite; AMD amoA genes support community potential. The participants are Nitrosotalea and Nitrospira as conceptual guild context, not a measured isolate pair. Direction is ammonia/ammonium acquisition to nitrite production with carbon fixation. CHEBI:16134/28938/16301 and GO:0019329/0015977 are chemically/process appropriate, while preferred nitrification wording is broader than ammonia oxidation. The node explicitly prevents transfer of soil-strain identity and activity to AMD.

### ecological_interactions[0].downstream[0]: ammonia oxidation → nitrite oxidation

graph: supported. Targets: CommunityMech:000002.

The sole arrow points from archaeal ammonia oxidation to Nitrospira nitrite oxidation and is explicitly HYPOTHESIZED. Potential producer Nitrosotalea-like AOA → potential consumer Nitrospira is a chemically coherent nitrite sequence. The AMD survey detects both functional groups but does not track nitrite transfer, rate coupling, rescue or reciprocal benefit. The exact target resolves and the uncertainty label should be preserved. Shared short quotations in soil-isolate and amd-survey supply the bounded source basis, not proof of the arrow.

### ecological_interactions[1]: Nitrite Oxidation to Nitrate by Nitrospira

graph: supported. Targets: CommunityMech:000002.

PARTIAL is appropriate for Nitrospira nxrB affiliation. Direction nitrite → nitrate and source genus Nitrospira fit the proposed pathway; CHEBI:16301/17632 and GO:0019332 match. The node expressly disclaims measured nitrate production and partner detoxification. The single source supports genetic potential, not activity.

### ecological_interactions[2]: Putative Ferroplasma Organic Matter Turnover

graph: supported. Targets: CommunityMech:000002.

HYPOTHESIZED is appropriate. Source participant F. acidiphilum is an extrapolation from a separately studied BRL-115 culture; broad Thermoplasmata co-occurrence does not identify that species in the AMD assemblage. CHEBI:50860 is a broad organic entity substrate, not an identified exchanged metabolite. No AOA recipient or downstream arrow is asserted. The description correctly distinguishes culture-supported chemomixotrophy from untested AOA detoxification.

### ecological_interactions[3]: Archaeal Ammonia-Oxidizer Diversity

graph: supported. Targets: CommunityMech:000002.

PARTIAL is appropriate for diversity. Nitrososphaera/Nitrosotalea affiliations come from AMD genes; the exact N. devaniterrae species descriptor is conceptual, not survey species identification. Ammonia/ammonium/nitrite and GO:0019329 describe shared nitrifier potential. The soil study compares two Nitrosotalea strains, so the node correctly rejects demonstrated complementary niches or reciprocal benefits between the named AMD participants. No causal arrow is asserted.

### environment_term.notes: environmental context and ranges

scope: concern. Targets: CommunityMech:000002.

Acid mine drainage and metal-rich acidic sediments are appropriate general habitat context. The specific ammonium ceiling, sulfate greater than 500 mg/L, temperature range, comparison with extreme AMD metal loads and implied taxon selection are not tied to same-system measurements in the inspected source text. Source-specific values and chemistry should be separated from general explanations, without extrapolating uninspected supplementary data.

### environmental_factors[0]: Acidic pH

quantity: concern. Targets: CommunityMech:000002.

The survey measured site pH 3.2–8.3 and detected AOB/nxrB genes at 3.2 and AOA genes at 3.5; this does not measure activity or establish a universal 2.5–4.5 operational range, AOB exclusion below 5.5, vertical zones or species transitions. The soil isolate optimum is 4–5, with a separately stated growth range 4–5.5. Using the record own pKa 9.25 and pH 4 yields NH4/NH3 = 10^5.25 ≈177,828, not 10,000; this is an explicit arithmetic check, not a new environmental measurement. The pyrite reaction is an unbalanced schematic and should not be presented as quantitative stoichiometry.

### environmental_factors[1]: Ammonium Concentration

quantity: concern. Targets: CommunityMech:000002.

The conversion 50–380 mg N/L to approximately 3.6–27 mM is dimensionally sound. The source excerpt about low pH/metals does not measure those ammonium concentrations. Neither inspected citation establishes the stated correlation r² 0.65–0.78, 50–200 mg/L optimum, inhibition above 300 mg/L, 5–20 microgram N/g/day consumption, or an AMD Km of 0.6–2.8 nM. The urea experiment is in soils. Amt-mediated acquisition is a proposed mechanism, not a measured active transport result for the AMD population.

### environmental_factors[2]: Temperature

quantity: concern. Targets: CommunityMech:000002.

The field survey reports 7.1–21.2 degrees C, not a universal 15–25 degree regime. The quoted cultivation excerpt concerns pH, not temperature. Seasonal amplitude, depth stratification, Q10, 50% activity reduction at 10 degrees, negligible activity below 5 and spring/fall rate maxima are not supported by these sources. Nd1 and Nd2 culture optima differ (25 versus 35 degrees), and should not be averaged into a community optimum. Acidithiobacillus caldus is mentioned as a comparison without a source for its claimed optimum and must not become an inferred member.

### environmental_factors[3]: Oxygen Availability

quantity: concern. Targets: CommunityMech:000002.

Aerobic ammonia/nitrite oxidation is reasonable pathway context. The survey measured 1.1–10 mg/L dissolved oxygen in field waters associated with 0–5 cm sediment composites; this is not a millimetre-resolved oxygen profile. Neither cited abstract establishes 5–15 mm penetration, defined taxon depth zones, O2 Km 2–10 micromolar, Ferroplasma optimum 1–3 mg/L, or 2–5 micromole O2/g/day consumption. The cited 0.18 nM ammonia growth concentration is not oxygen evidence. The AMO reaction is a schematic biochemical context, not a measured AMD rate.

### environmental_factors[4]: Genomic Data PRJNA1261802

provenance: concern. Targets: CommunityMech:000002.

The accession resolves, approximately 54 Gb and three assemblies are verified, and both deposited genera are Nitrososphaerota. The assemblies instead identify Thermosulfuris and Acidarchaeum in Conexivisphaeria. Their combined length is about 4.66 Mb, not the proposed 6–9 Mb. The claimed AOA/Ferroplasma identities, high-quality designation, 1000–6000x coverage, GC ranges and gene/pathway/lipid/glycosylation/HGT inventories are not established by generic database documentation or the unrelated Nitrosotalea isolate genome. No sequence annotation or read mapping was performed here.

### Natural field context versus cultivation conditions

scope: supported. Targets: CommunityMech:000002.

No growth_media block is present, which is not intrinsically defective for a natural field assemblage. The relevant sources provide distinct culture conditions: Nitrosotalea enrichment used mineral salts, 500 micromolar NH4Cl, pH 4.7, 1% soil inoculum, darkness and no shaking at 28/37 degrees; routine maintenance used 2% mid-exponential transfers at pH 5, with Nd1 at 25 and Nd2 at 37 degrees. BRL-115 yeast-extract growth belongs to the separate biomining pair. These conditions should not be inserted as the AMD community medium.

### related_ingredients[0..2]: ammonia, nitrite and urea

evidence: concern. Targets: CommunityMech:000002.

CHEBI:16134, 16301 and 16199 correctly identify ammonia, nitrite and urea. Ammonia as AOA substrate and nitrite as nitrification intermediate are supported. The ammonia relevance overstates universal AOB exclusion; nitrite relevance asserts a demonstrated handoff/syntrophic core despite the graph hypothesis; urea relevance transfers a group-level soil result to the AMD guild and named Nitrosotalea despite the genome limitation. Exact chemical grounding does not fix these biological scope errors.

### taxonomy[*].functional_role and community stability

representation: concern. Targets: CommunityMech:000002.

PRIMARY_PRODUCER is compatible with the AOA/Nitrospira autotrophic pathway context, but marker detection does not establish all field activity. CROSS_FEEDER for Ferroplasma has support in its separate Leptospirillum culture. SYNTROPHIC_PARTNER on all four taxa, the fixed abundance assignments, and STABLE ecological state lack same-system exchange or longitudinal stability evidence. These labels should follow the graph limited evidence rather than implying established mutual dependence.

### metals_present, metal_relevance and metal_notes

representation: concern. Targets: CommunityMech:000002.

Copper and iron are appropriate AMD context. PRIMARY metal relevance is not justified solely by a metal-rich habitat for a record centered on nitrogen cycling; Ferroplasma metal cycling remains an extrapolation here. metal_notes claims detection from graph CHEBI metabolites and environmental measurements, but this record graph contains only nitrogen species and organic entity, and its factors contain no quantified metal measurement. Keyword context exists; the stated detection pathways do not.

### Discussions, prior graph decisions and evidence placement

provenance: supported. Targets: CommunityMech:000002.

Both discussion attachments resolve to retained nodes and correctly state the unresolved nitrite-transfer, urease and archaeal partner questions. The append-only event matches the embedded curation history and records AI assistance. The prior graph review explicitly excluded the non-graph claims now audited; its qualifications should be propagated during future curation, not interpreted as full-record approval.

### Structured gene/trait source cross-check

evidence: not_applicable. Targets: CommunityMech:000002.

amoA/Amt/kdp/mgtA and acid-stress claims trigger structured-source consideration. The permitted local runner is unavailable. The public iModulonDB catalog provides no matching organism dataset, so no component search or summary is applicable. An unrelated archaeal dataset cannot substantiate these claims, and catalog absence is not negative biological evidence.

### Native gates and ontology ID/label correspondence

schema: supported. Targets: CommunityMech:000002.

Focused schema, strict, term, reference, GTDB coherence/domain and history gates all passed with exit 0 and no reported ontology skips. They cover the four taxonomic descriptors, ENVO:00001997, nitrogen/organic entity CHEBI terms and GO process terms. Their canonical meanings fit the intended entities/processes, but exact source occurrence and claimed roles require the scientific qualifications above. No target network issue was reported. Label matching and cache snippet matching do not certify claim support.

### Native completeness and validation quality

completeness: concern. Targets: CommunityMech:000002.

The complete presence rubric scores 80, while validation quality scores 93 with four P2 and one P3 findings. These are separate native metrics, not scientific approval. Eight node EvidenceItems across four interactions yield a mean of 2; duplicate and cross-system citations are not independent replication. Network COMPLETE is based on participant and reference integrity, not whether every causal node is connected.

## Findings

### community-scope: A multi-study guild is represented as a measured fixed community

major / open / confirmed; issue key: cm-000002-community-scope.

The description, taxon membership/abundances and syntrophic roles combine separate AMD surveys with soil isolates and a Ferroplasma–Leptospirillum culture. No cited source identifies the stated four-member stable assemblage, exact species abundances, per-gram gene counts, partner rescue or reciprocal niche benefits. PMID:29209281 uses counts per microgram DNA and usually greater nxrB abundance. The graph and open discussions already acknowledge these limits; related nitrite relevance and taxon notes contradict them.

### metabolic-attribution: Named organism mechanisms exceed or conflict with the source evidence

major / open / confirmed; issue key: cm-000002-metabolic-attribution.

Nitrosotalea urease-based adaptation conflicts with its cited closed-genome study. The stated 0.6–2.8 nM Km is not measured for this organism; growth at 0.18 nM is a different endpoint, and the genome paper discusses marine Nitrosopumilus kinetics. Predicted Amt transport/homeostasis and inferred glycosylation/lipid protection are presented as established mechanisms. Leptospirillum is incorrectly described as a nitrite oxidizer, and Nitrososphaera HAO/urease expression lacks a matching source. Soil urea-supported nitrification cannot establish that pathway in this AMD assemblage.

### environment-quantities: Environmental and physiological numbers lack source-matched measurements

major / open / confirmed; issue key: cm-000002-environment-quantities.

environment_term.notes and the pH, ammonium, temperature and oxygen fields contain unsupported operating ranges, correlations, rates, gradients, seasonal effects and species optima. Their snippets often address another variable or report genes rather than activity. The 50–380 mg N/L conversion is valid, but the underlying field concentration is unverified. The record own pKa gives an ammonium/ammonia ratio near 178,000 at pH 4, not 10,000. Soil pH optimum versus range and isolate doubling endpoints are also conflated. The field survey actual pH, temperature and oxygen ranges should retain site context, not be replaced by a universal protocol.

### project-provenance: Verified BioProject counts are followed by unsupported genome identities and functions

major / open / confirmed; issue key: cm-000002-project-provenance.

PRJNA1261802 does contain about 54 Gb and three assemblies, and its deposited species are Nitrososphaerota. Current records identify Thermosulfuris yongpingense and Acidarchaeum fankouense in Conexivisphaeria, not the proposed Nitrosotalea, Nitrososphaera and Ferroplasma/Acidiplasma genomes. Sizes also differ. Generic NCBI resources documentation and another isolate genome do not substantiate predicted gene inventories, GC, completeness, HGT, or 1000–6000x coverage. These fields conflate valid accession-level counts with unverified biological interpretation.

### metal-provenance: Metal relevance and detection notes exceed the represented evidence

minor / open / confirmed; issue key: cm-000002-metal-provenance.

Copper/iron habitat context is supported, but PRIMARY asserts primary metal extraction/cycling while the record focuses on nitrification. The automated-looking metal_notes claims CHEBI metal metabolites and measured environmental metal factors that are not present in this target. This is a bounded representation/provenance mismatch rather than denial of metal-rich AMD.

## Recommended Actions And Acceptance Checks

### fix-community-scope

Constrain this maintained record to an explicitly sourced conceptual guild or a defined sampled assemblage. Qualify species presence, abundances and partner roles to each source scope; preserve the graph uncertainty and unresolved discussions.

- Every retained member/abundance has a same-system source and original measurement unit; marker counts are not converted to organism percentages without justification.
- Taxonomic rank matches source resolution; soil isolate physiology does not establish species identity in AMD.
- STABLE and SYNTROPHIC_PARTNER are retained only with their required ecological evidence or changed to supported representations.
- just validate-strict kb/communities/AMD_Nitrososphaerota_Archaeal.yaml; just validate-terms kb/communities/AMD_Nitrososphaerota_Archaeal.yaml; just validate-gtdb kb/communities/AMD_Nitrososphaerota_Archaeal.yaml; just validate-references-explained kb/communities/AMD_Nitrososphaerota_Archaeal.yaml

### fix-metabolic-attribution

Remove or explicitly qualify unsupported organism-specific pathways and kinetic claims. Attach separate evidence to gene presence, expression, biochemical activity and ecological function; correct the Leptospirillum energy-metabolism attribution.

- Retained urease claims identify the actually tested taxon and habitat; the Nitrosotalea genome conflict is preserved.
- Km, growth substrate concentration and transport hypotheses remain separate endpoints with organism/assay conditions.
- Predicted acidophily mechanisms are not promoted to causal demonstration without functional experiments.
- just validate-strict kb/communities/AMD_Nitrososphaerota_Archaeal.yaml; just validate-references-explained kb/communities/AMD_Nitrososphaerota_Archaeal.yaml

### fix-environment-quantities

Audit each numeric assertion against its original measurement, units, sampled system and endpoint. Remove unsupported numerical specificity, correct the acid-base calculation, and distinguish observed field conditions from laboratory optima and proposed mechanisms.

- No rate, correlation, depth, oxygen affinity, ammonium optimum or seasonal statement is retained on a general-context quote alone.
- Growth ranges, optimum, doubling time, gene abundance and measured activity are separately labeled.
- Balanced chemistry or an explicitly schematic equation is used; conversions state N-mass versus compound-mass basis.
- just validate-strict kb/communities/AMD_Nitrososphaerota_Archaeal.yaml; just validate-references-explained kb/communities/AMD_Nitrososphaerota_Archaeal.yaml

### fix-project-provenance

Preserve the verified project accession and sequencing/assembly counts with direct provenance. Replace proposed genome identities with source-supported descriptions or remove the unsupported association to this guild; require accession-specific annotation before retaining gene, coverage or quality claims.

- Source access date, assembly accession/version, lineage and source-provided statistics are recorded distinctly.
- Approximately 54 Gb and three assemblies are not incorrectly rejected; Nitrososphaerota phylum identity is preserved.
- No function is inferred solely from phylum, generic database citation or total metagenomic read yield.
- just validate-strict kb/communities/AMD_Nitrososphaerota_Archaeal.yaml; just validate-references-explained kb/communities/AMD_Nitrososphaerota_Archaeal.yaml

### fix-metal-provenance

Choose metal relevance according to the schema meaning and the supported primary process. Replace detection notes with accurate traceable context rather than claiming nonexistent local measurement paths.

- The selected relevance level matches the actual documented function.
- Each detection/provenance statement points to a field and source that exists in the maintained record.
- just validate-strict kb/communities/AMD_Nitrososphaerota_Archaeal.yaml

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | kb/communities/AMD_Nitrososphaerota_Archaeal.yaml; Entire maintained record, including four taxonomy entries, four interaction nodes, one downstream arrow, five environmental factors, three related ingredients, two discussions and curation history | supports | The stable target is an AMD archaeal nitrifier guild synthesis. Its graph is explicitly partial or hypothetical, while surrounding prose makes stronger assertions about a fixed community, abundances and physiology. |
| pubmed-identities | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=21896746,26896134,29209281,24909965,33388792,27535541,22592820&amp;retmode=xml; PubmedArticle/PubmedData/ArticleIdList and Article/Abstract for the seven requested PMIDs; exact response body retained in primary-pubmed.body.xml | supports | Current primary NCBI metadata confirms the seven PMID/DOI pairs and the inspected abstracts. Article identities were read from each article own PubmedData, not from reference-list identifiers. |
| soil-isolate | https://doi.org/10.1073/pnas.1107196108; PMID:21896746; Abstract; live PubMed abstract and figure captions; PMC3179093 identifier; references_cache/PMID_21896746.md | partial | The soil isolate is chemolithotrophic and acidophilic, with optimum pH 4–5 and reported growth range 4–5.5. Its growth at 0.18 nM ammonia is not an experimentally measured enzyme Km. Soil growth and autotrophy do not identify this isolate in AMD. |
| acidophily-genome | https://doi.org/10.1128/AEM.04031-15; PMID:26896134; Full text: genome Results; Ammonia oxidation at low pH; Discussion and final limitations; cache lines 154–185; live PMC4836417; references_cache/PMID_26896134.md | partial | The closed soil-isolate genome lacks the proposed urease adaptation. AMO and Amt genes, candidate pH-homeostasis transcription and unusual lipid composition support mechanistic hypotheses. NH4 binding is predicted; transported species and causal necessity for acidophily were not experimentally established. The cited approximately 2 nM NH3 half-saturation value belongs to marine Nitrosopumilus maritimus, not this Nitrosotalea isolate. |
| amd-survey | https://doi.org/10.3389/fmicb.2017.02136; PMID:29209281; Full text: Methods Study site/sample collection, qPCR, Results Table 1 and gene abundance, Discussion and Conclusions; live Frontiers DOI page; references_cache/PMID_29209281.md | partial | Iron Springs, Colorado sediments were sampled during 2013–2014. AOA amoA and bacterial 16S/nxrB sequences establish gene abundance and affiliation. Counts are per microgram extracted DNA, not per gram sediment or organism percentages. The study does not measure nitrification rates, partner transfer or detoxification. It reports pH 3.2–8.3, temperature 7.1–21.2 degrees C and dissolved oxygen 1.1–10 mg/L. |
| soil-strains | https://doi.org/10.1111/1574-6941.12353; PMID:24909965; Full cached text: Methods enrichment/maintenance; Results physiology, Figures 1 and 4; cache lines 80–88 and 124–148; live PubMed abstract; references_cache/PMID_24909965.md | partial | The studied isolates are Nitrosotalea devanaterra Nd1 from Scottish agricultural soil and Nitrosotalea sp. Nd2 from Chinese paddy soil. Their temperature optima, growth rates and responses to organic acids differ. This does not demonstrate Nitrososphaera acid tolerance or complementary niches among AMD populations. |
| malanjkhand | https://doi.org/10.1007/s00203-020-02130-4; PMID:33388792; Abstract, V6 amplicon composition and inferred functional roles; live Springer article abstract; references_cache/PMID_33388792.md | partial | Malanjkhand copper-project sediment contains broad Thermoplasmata and Nitrososphaeria lineages. V6 amplicons and inferred functions do not identify the exact Ferroplasma acidiphilum–Nitrosotalea pair or prove exchange, metal detoxification or partner fitness. |
| ferroplasma-culture | https://doi.org/10.1002/btpr.2340; PMID:27535541; Complete abstract: strain BRL-115, yeast extract, reciprocal filtered-supernatant growth and cyclic batch/FBA; current NCBI abstract; references_cache/PMID_27535541.txt | partial | Ferroplasma acidiphilum BRL-115 was tested with Leptospirillum ferriphilum. Chemomixotrophic growth was maximized with 0.04% wt/vol yeast extract, and filtered partner media improved growth. This is evidence for that culture pair, not for an AOA-associated AMD consortium or the claimed oxygen optimum. |
| urea-soils | https://doi.org/10.1038/ismej.2012.45; PMID:22592820; Complete abstract: 15N-urea tracing, tea-orchard pH 3.75 and forest pH 5.4, group-level AOA; live NCBI abstract; references_cache/PMID_22592820.md | partial | Urea-supported archaeal nitrification was tested in two acidic soils, using isotope tracing and community markers. The result does not assign urease to Nitrosotalea devanaterra or demonstrate urea-supported nitrification in AMD. Absence of detected AOB applies to the tested soils. |
| ncbi-resources | https://doi.org/10.1093/nar/gkz899; NCBI resources 2020 abstract and primary Nucleic Acids Research PDF pages D9–D10; DOI metadata; references_cache/doi_10.1093_nar_gkz899.md | partial | The generic NCBI resources publication describes the database suite. It supplies no accession-specific evidence for PRJNA1261802, which was subsequently inspected directly. |
| amd-count-units | PMID:29209281; Abstract and Results gene abundances; references_cache/PMID_29209281.md | refutes | Reported ranges are AOA amoA 3.2e4–4.9e7, AOB 16S 1.5e3–5.3e5 and Nitrospira nxrB 1.3e6–7.7e7 per microgram DNA. nxrB was usually more abundant, and marker copy-number differences prevent direct cell-ratio conversion. |
| leptospirillum-primary | https://journals.asm.org/doi/10.1128/aem.02091-17; Christel et al. 2018; Abstract and Introduction paragraph 1; live primary text lines 86–100 inspected | refutes | Primary genome/transcriptome/proteome study treats L. ferriphilum as an iron oxidizer; the type strain gains energy from Fe(II) oxidation. It does not support classifying Leptospirillum as the nitrite-oxidizing partner asserted in this record. |
| ncbi-project | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=bioproject&amp;id=1261802&amp;retmode=xml; ProjectDescr/Title, Description, Organism and archive links; body retained at /private/tmp/cm-review-session/000002/project-source/ncbi-project.body | partial | PRJNA1261802 is an acid-mine-drainage metagenomic assembly project; its general description does not identify the proposed three AOA/supporting species or validate their functions. |
| ena-project | https://www.ebi.ac.uk/ena/browser/api/xml/PRJNA1261802; STUDY title, abstract and cross references; body retained at /private/tmp/cm-review-session/000002/project-source/ena-project.body | partial | ENA independently resolves PRJNA1261802 to the same general AMD metagenome project. |
| ena-runs | https://www.ebi.ac.uk/ena/portal/api/filereport?accession=PRJNA1261802&amp;result=read_run&amp;fields=run_accession,study_accession,sample_accession,scientific_name,instrument_platform,read_count,base_count&amp;format=tsv; Entire two-row read_run TSV, base_count column; body retained at /private/tmp/cm-review-session/000002/project-source/ena-runs.body | partial | The two runs contain 53,964,165,000 bases in total, consistent with approximately 54 Gb. This is total metagenomic sequencing yield, not per-genome coverage. |
| ncbi-assemblies | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=assembly&amp;term=PRJNA1261802%5BBioProject%5D&amp;retmode=json&amp;retmax=100; esearchresult.count and idlist; body retained at /private/tmp/cm-review-session/000002/project-source/ncbi-assemblies.body | partial | The project currently has three indexed assembly records. This verifies the count without verifying the record proposed organisms or gene functions. |
| project-assemblies | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=assembly&amp;id=30290111,30290101,30290091&amp;retmode=json; Three assembly esummary entries: accession, organism, taxid, BioSample, meta/Stats/total_length and release date; exact response body retained at /private/tmp/cm-review-session/000002/project-source/assembly-summaries.body | partial | GCA_053486515.1 is Thermosulfuris yongpingense (SeqCode), 1,569,763 bp; GCA_053486495.1 and GCA_053486475.1 are Acidarchaeum fankouense (SeqCode), 1,448,496 and 1,637,578 bp. Released November 2025, these do not match the proposed Nitrosotalea/Nitrososphaera/Ferroplasma genome identities or claimed 6–9 Mb combined genome size. |
| project-taxonomy | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=3693717,3693715&amp;retmode=xml; NCBITaxon:3693717 and 3693715: ScientificName, Rank and Lineage; exact response body retained at /private/tmp/cm-review-session/000002/project-source/assembly-taxonomy.body | partial | Both deposited species belong to Nitrososphaerota, class Conexivisphaeria, order Conexivisphaerales, family Thermosulfuridaceae. Their genera are Thermosulfuris and Acidarchaeum, not alternative spellings of Nitrosotalea or Nitrososphaera. Phylum membership alone does not establish ammonia oxidation. |
| schema | src/communitymech/schema/communitymech.yaml; MicrobialCommunity, FunctionalRoleEnum, MetalRelevanceEnum and EvidenceItem | supports | Natural community context, source experiment and claimed roles must remain distinct. PRIMARY_PRODUCER denotes carbon fixation; SYNTROPHIC_PARTNER denotes syntrophic metabolism. PRIMARY metal relevance requires metal extraction/cycling as the primary function. |
| history | history/records/AMD_Nitrososphaerota_Archaeal/2026-10-05T055158Z-codex-ce2f0a.yaml; Entire event; reports/causal_graph_review/decisions/20261005-seven-records.yaml target entry; discussions and embedded curation_history | supports | The prior graph curation explicitly removed unsupported urea and rescue claims, qualified the retained graph, and left non-graph taxa and environmental quantities for later audit. This history is preserved and does not certify the unreviewed fields. |
| snippet-inventory | /private/tmp/cm-review-session/000002/snippet-correspondence.json; Recursive inventory of all 30 record EvidenceItem snippets against the eight inspected cache files; exact and whitespace/case-normalized tests | supports | All 30 snippets match the cited cached source after whitespace/case normalization; line wrapping accounts for nonexact matches. The central problem is claim attribution and scope, not fabricated quotation text. Eight graph EvidenceItems cite six distinct publications; repeated excerpts are not independent replication. |
| adapter-resolution | kg-microbe-sources; PATH resolution and own isolated-checkout .venv/bin/kg-microbe-sources existence check; structured-adapter-resolution.json | context_only | No console runner was found on PATH or in this isolated checkout. Other checkouts were deliberately excluded from execution by user instruction. |
| imodulondb-catalog | https://imodulondb.org/api/datasets; Entire public catalog: 20 organism keys and 28 datasets; own-runtime read-only HTTP response retained in session 000273 scratch | context_only | The inspected catalog has no Nitrosotalea, Nitrososphaera, Nitrospira or Ferroplasma dataset. The record amoA, Amt, kdp and mgtA claims therefore have no matching iModulonDB organism/dataset/component to summarize. Absence from this catalog is not evidence against the genes or phenotype. |
| check-validate | UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true JUST_NO_DOTENV=true just --no-dotenv validate kb/communities/AMD_Nitrososphaerota_Archaeal.yaml; Actual output and exit_code=0; full JSON log /private/tmp/cm-review-session/000002/validate.json | context_only | No issues found<br>uv run linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/AMD_Nitrososphaerota_Archaeal.yaml |
| check-validate-strict | UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true JUST_NO_DOTENV=true just --no-dotenv validate-strict kb/communities/AMD_Nitrososphaerota_Archaeal.yaml --out /private/tmp/cm-review-session/000002/strict-report.tsv; Actual output and exit_code=0; full JSON log /private/tmp/cm-review-session/000002/validate-strict.json | context_only | uv run python scripts/validate_strict.py kb/communities/AMD_Nitrososphaerota_Archaeal.yaml --out /private/tmp/cm-review-session/000002/strict-report.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/communitymech-record-reviews-20261019/src/communitymech/schema/communitymech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cm-review-session/000002/strict-report.tsv |
| check-validate-terms | UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true JUST_NO_DOTENV=true just --no-dotenv validate-terms kb/communities/AMD_Nitrososphaerota_Archaeal.yaml; Actual output and exit_code=0; full JSON log /private/tmp/cm-review-session/000002/validate-terms.json | context_only | ✅ Validation passed<br>uv run linkml-term-validator validate-data kb/communities/AMD_Nitrososphaerota_Archaeal.yaml -s src/communitymech/schema/communitymech.yaml --labels |
| check-validate-gtdb | UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true JUST_NO_DOTENV=true just --no-dotenv validate-gtdb kb/communities/AMD_Nitrososphaerota_Archaeal.yaml; Actual output and exit_code=0; full JSON log /private/tmp/cm-review-session/000002/validate-gtdb.json | context_only | PYTHONPATH=src uv run python scripts/validate_gtdb_coherence.py kb/communities/AMD_Nitrososphaerota_Archaeal.yaml<br><br>files checked: 1<br>incoherent blocks: 0<br>malformed lineages: 0<br>lineage conflicts: 0 |
| check-validate-gtdb-domain | UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true JUST_NO_DOTENV=true just --no-dotenv validate-gtdb-domain kb/communities/AMD_Nitrososphaerota_Archaeal.yaml; Actual output and exit_code=0; full JSON log /private/tmp/cm-review-session/000002/validate-gtdb-domain.json | context_only | files checked: 1<br>contradictory lineages: 0<br>PYTHONPATH=src uv run python scripts/validate_prokaryotic_lineage.py kb/communities/AMD_Nitrososphaerota_Archaeal.yaml |
| check-validate-history | UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true JUST_NO_DOTENV=true just --no-dotenv validate-history history/records/AMD_Nitrososphaerota_Archaeal; Actual output and exit_code=0; full JSON log /private/tmp/cm-review-session/000002/validate-history.json | context_only | No issues found |
| check-normalize-cache-names | UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true JUST_NO_DOTENV=true uv run python scripts/normalize_cache_names.py --check; Actual output and exit_code=0; full JSON log /private/tmp/cm-review-session/000002/normalize-cache-names-check.json | context_only | Actual command returned exit 0 with no issues or output. |
| check-validate-references-explained | UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true JUST_NO_DOTENV=true just --no-dotenv validate-references-explained kb/communities/AMD_Nitrososphaerota_Archaeal.yaml; Actual output and exit_code=0; full JSON log /private/tmp/cm-review-session/000002/validate-references-explained.json | context_only | Validating kb/communities/AMD_Nitrososphaerota_Archaeal.yaml against schema src/communitymech/schema/communitymech.yaml<br>Cache directory: references_cache<br><br>Validation Summary:<br>  Reported validation issues: 0<br>  All validations passed!<br><br>[annotate] This is not a count of checked excerpts (#1469). Native Discussion evidence coverage remains incomplete (#476). |
| check-audit-network | just --no-dotenv audit-network; Complete corpus output from 2026-10-19T07:30:27.845593+00:00; /private/tmp/cm-review-session/000320/audit-network.json | context_only | Actual full-corpus recipe exit 1: 462 records, 57 warnings in 21 records, zero errors. No AMD_Nitrososphaerota_Archaeal target findings. Reused same-session results against unchanged Git base and record bytes; other-record warnings are not assigned to this target. |
| check-check-network-quality | just --no-dotenv check-network-quality; Complete corpus output from 2026-10-19T07:30:43.193891+00:00; /private/tmp/cm-review-session/000320/check-network-quality.json | context_only | Actual full-corpus recipe exit 1: 462 records, 57 warnings in 21 records, zero errors. No AMD_Nitrososphaerota_Archaeal target findings. Reused same-session results against unchanged Git base and record bytes; other-record warnings are not assigned to this target. |

## Limits And Additional Notes

- Full primary text was inspected for PMID:26896134 and 29209281; cached full text plus live primary metadata/abstract were used for 24909965. PMID:21896746 assessment uses abstract and available figure captions. PMID:33388792, 27535541 and 22592820 are limited to accessible abstracts; inaccessible full texts or supplements are not assumed to lack protocols.
- Primary NCBI and ENA project, read-run, assembly and lineage metadata were inspected. No metagenomic reads, annotations, completeness/contamination tools, coverage calculations or functional experiments were analyzed; unverified function claims are not declared biologically impossible.
- The existing GTDB coherence/domain gates passed, but historical genome support counts, mapping fractions and reclassification provenance were not independently regenerated.
- The optional structured adapter was unavailable in the permitted runtime. The inspected iModulonDB public catalog has no matching target organism dataset; this limits applicability, not biological plausibility.
- Required corpus network gates returned warning failures outside this target; those actual exit statuses remain in this report.
- The review was performed by an agent with delegated validators and primary metadata retrieval. No target was authored or edited this session; prior curation also used codex, so person-level independence is unknown.
- Search for related local sources/decisions used rg --no-ignore --hidden across references_cache, history, reports, research and kb/taxa for the record slug and PRJNA1261802, including ignored files; broad generated HTML/JSON/TSV/CSV/TTL outputs were excluded. Absence statements are bounded to that search and the fully inspected source responses.
- No record, source cache, append-only history, generated product or scientific-status field was changed. Proposed curation requires separate authorization.
- Shared short quotations are attached once and reused by node/arrow assessments; all cached article quotations are exact and total at most 25 words per publication.
- All 30 target EvidenceItems were examined. Lexical correspondence does not cure incorrect explanation, assay, taxon or habitat attribution.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261019T234155Z-amd-nitrososphaerota-archaeal-record
kind: record
repository: CultureBotAI/CommunityMech
title: 'AMD Nitrososphaerota archaeal record: whole-record scientific review'
started_at: '2026-10-19T23:34:06.330971Z'
finished_at: '2026-10-19T23:41:55.733353Z'
reviewer:
  identity: codex
  kind: agent
  independence: unknown
  independence_basis: The review was performed by an agent with delegated validators
    and primary metadata retrieval. No target was authored or edited this session;
    prior curation also used codex, so person-level independence is unknown.
skill: review-yaml-record
completion: completed
verdict: needs_curation
scientific_review: true
summary: The four nodes and sole causal arrow preserve appropriate partial/hypothetical
  scope. Four major findings concern whole-community scope, organism mechanisms, environmental
  quantities and project genome attribution; one minor finding concerns metal classification/provenance.
  Approximately 54 Gb, three deposited genomes and Nitrososphaerota phylum membership
  are verified. All focused gates pass; corpus network warnings remain explicit.
source:
  git_revision: a4611c913c8da9619673df63a0c2cce3aa206a83
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
  - path: history/records/AMD_Nitrososphaerota_Archaeal/2026-10-05T055158Z-codex-ce2f0a.yaml
    sha256: b664c9b1f3cf637d373cda78bf369c7622f67cb49bb64c1aafae1997aa1e1327
    role: context
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: kb/communities/AMD_Nitrososphaerota_Archaeal.yaml
    sha256: 4ec75078d1c9fcd32e5fbac218c3d4c48af25be5a0cb76887cc650c570c95e22
    role: target
  - path: references_cache/PMID_21896746.md
    sha256: 20f31dbad287d81a25f75a55d6ae64d192142c14df52cee1d582ebbe6618db44
    role: context
  - path: references_cache/PMID_22592820.md
    sha256: a6381e852c2627e9176c39ce6334d7009117c53754fd252400d274bde5eaf11f
    role: context
  - path: references_cache/PMID_24909965.md
    sha256: 125e3dfa3003d1ec74f8504934a5deda3d8428d2fdc16b47b7a78c0b42089118
    role: context
  - path: references_cache/PMID_26896134.md
    sha256: 539aead91aae585b580cddc2d7d634a58c7e475858272830c834979074074635
    role: context
  - path: references_cache/PMID_27535541.txt
    sha256: daf84c5d47a7e43c14d877dffdd3f915f959793d05b5e58bf5504dbd7c029376
    role: context
  - path: references_cache/PMID_29209281.md
    sha256: d0016a6b52115c87bb02cff3a48bc1b8acbdbd5410b5bdb688a4738b373a5c2c
    role: context
  - path: references_cache/PMID_33388792.md
    sha256: 6fcc5f7b1ed38b88556c77f0942b973ef674c64e0d8928faab204d3e002e91be
    role: context
  - path: references_cache/doi_10.1093_nar_gkz899.md
    sha256: a7a53d50cf3e1f74c79a3a598ae9c66efbb75e5821e75760f601d9ad3876c0fd
    role: context
  - path: reports/causal_graph_review/decisions/20261005-seven-records.yaml
    sha256: 064f7395bbb54d42023f3a0bceeb31a3dd990221e62094f6a51507fee81eea69
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: src/communitymech/network/auditor.py
    sha256: fe32aa2eddf9e09c153c47576f943bf08a6019f650bf2575e3ddc8e14675049b
    role: context
  - path: src/communitymech/schema/communitymech.yaml
    sha256: e5a87e5367609334ec0d6361f6ddafbe6bc4a1f7d93e5264c64688c28325910f
    role: context
  - path: src/communitymech/schema/history.yaml
    sha256: b01b06f1b9a37db205c26c31ec0fd910690848507c7e1bfb73b424ac0829c52d
    role: context
  - path: src/communitymech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
targets:
- target_id: CommunityMech:000002
  path: kb/communities/AMD_Nitrososphaerota_Archaeal.yaml
  label: AMD Nitrososphaerota Archaeal Community
  record_class: MicrobialCommunity
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/AMD_Nitrososphaerota_Archaeal.yaml
    role: canonical_record
scope:
  description: Entire maintained community record, all four taxonomic entries, four
    nodes and one arrow, five factors, three ingredients, ontology meanings, source
    boundaries and public project provenance.
  selection: Sixth repository-relative target in the parent ordered corpus review.
    Exactly one resolved maintained record in this bundle; earlier reviews remain
    immutable.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000002
checks:
- check_id: validate
  name: validate
  status: passed
  required: true
  summary: 'No issues found

    uv run linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/AMD_Nitrososphaerota_Archaeal.yaml'
  target_ids:
  - CommunityMech:000002
  command: UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true
    JUST_NO_DOTENV=true just --no-dotenv validate kb/communities/AMD_Nitrososphaerota_Archaeal.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate
  scope_note: Single maintained target; history uses its exact history directory.
    Cache-name preflight is a corpus check and does not write caches.
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: "uv run python scripts/validate_strict.py kb/communities/AMD_Nitrososphaerota_Archaeal.yaml\
    \ --out /private/tmp/cm-review-session/000002/strict-report.tsv\nValidating 1\
    \ files with 17 workers; schema=/private/tmp/communitymech-record-reviews-20261019/src/communitymech/schema/communitymech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cm-review-session/000002/strict-report.tsv"
  target_ids:
  - CommunityMech:000002
  command: UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true
    JUST_NO_DOTENV=true just --no-dotenv validate-strict kb/communities/AMD_Nitrososphaerota_Archaeal.yaml
    --out /private/tmp/cm-review-session/000002/strict-report.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-strict
  scope_note: Single maintained target; history uses its exact history directory.
    Cache-name preflight is a corpus check and does not write caches.
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: '✅ Validation passed

    uv run linkml-term-validator validate-data kb/communities/AMD_Nitrososphaerota_Archaeal.yaml
    -s src/communitymech/schema/communitymech.yaml --labels'
  target_ids:
  - CommunityMech:000002
  command: UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true
    JUST_NO_DOTENV=true just --no-dotenv validate-terms kb/communities/AMD_Nitrososphaerota_Archaeal.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-terms
  scope_note: Single maintained target; history uses its exact history directory.
    Cache-name preflight is a corpus check and does not write caches.
- check_id: validate-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: 'PYTHONPATH=src uv run python scripts/validate_gtdb_coherence.py kb/communities/AMD_Nitrososphaerota_Archaeal.yaml


    files checked: 1

    incoherent blocks: 0

    malformed lineages: 0

    lineage conflicts: 0'
  target_ids:
  - CommunityMech:000002
  command: UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true
    JUST_NO_DOTENV=true just --no-dotenv validate-gtdb kb/communities/AMD_Nitrososphaerota_Archaeal.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb
  scope_note: Single maintained target; history uses its exact history directory.
    Cache-name preflight is a corpus check and does not write caches.
- check_id: validate-gtdb-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: 'files checked: 1

    contradictory lineages: 0

    PYTHONPATH=src uv run python scripts/validate_prokaryotic_lineage.py kb/communities/AMD_Nitrososphaerota_Archaeal.yaml'
  target_ids:
  - CommunityMech:000002
  command: UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true
    JUST_NO_DOTENV=true just --no-dotenv validate-gtdb-domain kb/communities/AMD_Nitrososphaerota_Archaeal.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb-domain
  scope_note: Single maintained target; history uses its exact history directory.
    Cache-name preflight is a corpus check and does not write caches.
- check_id: validate-history
  name: validate-history
  status: passed
  required: true
  summary: No issues found
  target_ids:
  - CommunityMech:000002
  command: UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true
    JUST_NO_DOTENV=true just --no-dotenv validate-history history/records/AMD_Nitrososphaerota_Archaeal
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-history
  scope_note: Single maintained target; history uses its exact history directory.
    Cache-name preflight is a corpus check and does not write caches.
- check_id: normalize-cache-names
  name: normalize-cache-names
  status: passed
  required: false
  summary: Actual command returned exit 0 with no issues or output.
  target_ids:
  - CommunityMech:000002
  command: UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true
    JUST_NO_DOTENV=true uv run python scripts/normalize_cache_names.py --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-normalize-cache-names
  scope_note: Single maintained target; history uses its exact history directory.
    Cache-name preflight is a corpus check and does not write caches.
- check_id: validate-references-explained
  name: validate-references-explained
  status: passed
  required: true
  summary: "Validating kb/communities/AMD_Nitrososphaerota_Archaeal.yaml against schema\
    \ src/communitymech/schema/communitymech.yaml\nCache directory: references_cache\n\
    \nValidation Summary:\n  Reported validation issues: 0\n  All validations passed!\n\
    \n[annotate] This is not a count of checked excerpts (#1469). Native Discussion\
    \ evidence coverage remains incomplete (#476)."
  target_ids:
  - CommunityMech:000002
  command: UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true
    JUST_NO_DOTENV=true just --no-dotenv validate-references-explained kb/communities/AMD_Nitrososphaerota_Archaeal.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-references-explained
  scope_note: Single maintained target; history uses its exact history directory.
    Cache-name preflight is a corpus check and does not write caches.
- check_id: audit-network
  name: audit-network
  status: failed
  required: true
  summary: 'Actual full-corpus recipe exit 1: 462 records, 57 warnings in 21 records,
    zero errors. No AMD_Nitrososphaerota_Archaeal target findings. Reused same-session
    results against unchanged Git base and record bytes; other-record warnings are
    not assigned to this target.'
  target_ids:
  - CommunityMech:000002
  command: just --no-dotenv audit-network
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-audit-network
  scope_note: Corpus-wide gate includes declared community and isolate roots. Target-specific
    network integrity is COMPLETE; weak connectivity of every causal node is not required.
- check_id: check-network-quality
  name: check-network-quality
  status: failed
  required: true
  summary: 'Actual full-corpus recipe exit 1: 462 records, 57 warnings in 21 records,
    zero errors. No AMD_Nitrososphaerota_Archaeal target findings. Reused same-session
    results against unchanged Git base and record bytes; other-record warnings are
    not assigned to this target.'
  target_ids:
  - CommunityMech:000002
  command: just --no-dotenv check-network-quality
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-check-network-quality
  scope_note: Corpus-wide gate includes declared community and isolate roots. Target-specific
    network integrity is COMPLETE; weak connectivity of every causal node is not required.
- check_id: structured-source-runner
  name: Resolve iModulonDB structured adapter
  status: unavailable
  required: false
  summary: No console runner on PATH or in the permitted own-checkout runtime; public
    source catalog fallback was inspected.
  target_ids:
  - CommunityMech:000002
  evidence_ids:
  - adapter-resolution
  - imodulondb-catalog
  scope_note: Optional adapter unavailable; source assessment completed by permitted
    read-only fallback. No external-checkout runner or paid provider used.
evidence:
- evidence_id: record
  kind: record_content
  reference: kb/communities/AMD_Nitrososphaerota_Archaeal.yaml
  locator: Entire maintained record, including four taxonomy entries, four interaction
    nodes, one downstream arrow, five environmental factors, three related ingredients,
    two discussions and curation history
  accessed_at: '2026-10-19T23:34:06.330971Z'
  support: supports
  summary: The stable target is an AMD archaeal nitrifier guild synthesis. Its graph
    is explicitly partial or hypothetical, while surrounding prose makes stronger
    assertions about a fixed community, abundances and physiology.
- evidence_id: pubmed-identities
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=21896746,26896134,29209281,24909965,33388792,27535541,22592820&retmode=xml
  locator: PubmedArticle/PubmedData/ArticleIdList and Article/Abstract for the seven
    requested PMIDs; exact response body retained in primary-pubmed.body.xml
  accessed_at: '2026-10-19T23:35:27.852792Z'
  support: supports
  summary: Current primary NCBI metadata confirms the seven PMID/DOI pairs and the
    inspected abstracts. Article identities were read from each article own PubmedData,
    not from reference-list identifiers.
  snapshot_sha256: 37af14decb0417cf4b6e10a009946217540c538a6e3ec91a9c0e43ba218b3d77
- evidence_id: soil-isolate
  kind: primary_source
  reference: https://doi.org/10.1073/pnas.1107196108
  locator: PMID:21896746; Abstract; live PubMed abstract and figure captions; PMC3179093
    identifier; references_cache/PMID_21896746.md
  accessed_at: '2026-10-19T23:41:55.726743Z'
  support: partial
  summary: The soil isolate is chemolithotrophic and acidophilic, with optimum pH
    4–5 and reported growth range 4–5.5. Its growth at 0.18 nM ammonia is not an experimentally
    measured enzyme Km. Soil growth and autotrophy do not identify this isolate in
    AMD.
  quote: from an acidic agricultural soil
- evidence_id: acidophily-genome
  kind: primary_source
  reference: https://doi.org/10.1128/AEM.04031-15
  locator: 'PMID:26896134; Full text: genome Results; Ammonia oxidation at low pH;
    Discussion and final limitations; cache lines 154–185; live PMC4836417; references_cache/PMID_26896134.md'
  accessed_at: '2026-10-19T23:41:55.726848Z'
  support: partial
  summary: The closed soil-isolate genome lacks the proposed urease adaptation. AMO
    and Amt genes, candidate pH-homeostasis transcription and unusual lipid composition
    support mechanistic hypotheses. NH4 binding is predicted; transported species
    and causal necessity for acidophily were not experimentally established. The cited
    approximately 2 nM NH3 half-saturation value belongs to marine Nitrosopumilus
    maritimus, not this Nitrosotalea isolate.
  quote: (e.g., with urease)
- evidence_id: amd-survey
  kind: primary_source
  reference: https://doi.org/10.3389/fmicb.2017.02136
  locator: 'PMID:29209281; Full text: Methods Study site/sample collection, qPCR,
    Results Table 1 and gene abundance, Discussion and Conclusions; live Frontiers
    DOI page; references_cache/PMID_29209281.md'
  accessed_at: '2026-10-19T23:41:55.726853Z'
  support: partial
  summary: Iron Springs, Colorado sediments were sampled during 2013–2014. AOA amoA
    and bacterial 16S/nxrB sequences establish gene abundance and affiliation. Counts
    are per microgram extracted DNA, not per gram sediment or organism percentages.
    The study does not measure nitrification rates, partner transfer or detoxification.
    It reports pH 3.2–8.3, temperature 7.1–21.2 degrees C and dissolved oxygen 1.1–10
    mg/L.
  quote: NOB genes related to Nitrospira
- evidence_id: soil-strains
  kind: primary_source
  reference: https://doi.org/10.1111/1574-6941.12353
  locator: 'PMID:24909965; Full cached text: Methods enrichment/maintenance; Results
    physiology, Figures 1 and 4; cache lines 80–88 and 124–148; live PubMed abstract;
    references_cache/PMID_24909965.md'
  accessed_at: '2026-10-19T23:41:55.726856Z'
  support: partial
  summary: The studied isolates are Nitrosotalea devanaterra Nd1 from Scottish agricultural
    soil and Nitrosotalea sp. Nd2 from Chinese paddy soil. Their temperature optima,
    growth rates and responses to organic acids differ. This does not demonstrate
    Nitrososphaera acid tolerance or complementary niches among AMD populations.
  quote: two Nitrosotalea strains
- evidence_id: malanjkhand
  kind: primary_source
  reference: https://doi.org/10.1007/s00203-020-02130-4
  locator: PMID:33388792; Abstract, V6 amplicon composition and inferred functional
    roles; live Springer article abstract; references_cache/PMID_33388792.md
  accessed_at: '2026-10-19T23:41:55.726858Z'
  support: partial
  summary: Malanjkhand copper-project sediment contains broad Thermoplasmata and Nitrososphaeria
    lineages. V6 amplicons and inferred functions do not identify the exact Ferroplasma
    acidiphilum–Nitrosotalea pair or prove exchange, metal detoxification or partner
    fitness.
  quote: V6-16S rRNA gene amplicon data
- evidence_id: ferroplasma-culture
  kind: primary_source
  reference: https://doi.org/10.1002/btpr.2340
  locator: 'PMID:27535541; Complete abstract: strain BRL-115, yeast extract, reciprocal
    filtered-supernatant growth and cyclic batch/FBA; current NCBI abstract; references_cache/PMID_27535541.txt'
  accessed_at: '2026-10-19T23:41:55.726861Z'
  support: partial
  summary: Ferroplasma acidiphilum BRL-115 was tested with Leptospirillum ferriphilum.
    Chemomixotrophic growth was maximized with 0.04% wt/vol yeast extract, and filtered
    partner media improved growth. This is evidence for that culture pair, not for
    an AOA-associated AMD consortium or the claimed oxygen optimum.
  quote: strain BRL-115 is a chemomixotrophic
- evidence_id: urea-soils
  kind: primary_source
  reference: https://doi.org/10.1038/ismej.2012.45
  locator: 'PMID:22592820; Complete abstract: 15N-urea tracing, tea-orchard pH 3.75
    and forest pH 5.4, group-level AOA; live NCBI abstract; references_cache/PMID_22592820.md'
  accessed_at: '2026-10-19T23:41:55.726863Z'
  support: partial
  summary: Urea-supported archaeal nitrification was tested in two acidic soils, using
    isotope tracing and community markers. The result does not assign urease to Nitrosotalea
    devanaterra or demonstrate urea-supported nitrification in AMD. Absence of detected
    AOB applies to the tested soils.
  quote: two acidic soils tested
- evidence_id: ncbi-resources
  kind: primary_source
  reference: https://doi.org/10.1093/nar/gkz899
  locator: NCBI resources 2020 abstract and primary Nucleic Acids Research PDF pages
    D9–D10; DOI metadata; references_cache/doi_10.1093_nar_gkz899.md
  accessed_at: '2026-10-19T23:41:55.726865Z'
  support: partial
  summary: The generic NCBI resources publication describes the database suite. It
    supplies no accession-specific evidence for PRJNA1261802, which was subsequently
    inspected directly.
  quote: 35 distinct databases
- evidence_id: amd-count-units
  kind: primary_source
  reference: PMID:29209281
  locator: Abstract and Results gene abundances; references_cache/PMID_29209281.md
  accessed_at: '2026-10-19T23:35:27.852792Z'
  support: refutes
  summary: Reported ranges are AOA amoA 3.2e4–4.9e7, AOB 16S 1.5e3–5.3e5 and Nitrospira
    nxrB 1.3e6–7.7e7 per microgram DNA. nxrB was usually more abundant, and marker
    copy-number differences prevent direct cell-ratio conversion.
  quote: copies per μg DNA
- evidence_id: leptospirillum-primary
  kind: primary_source
  reference: https://journals.asm.org/doi/10.1128/aem.02091-17
  locator: Christel et al. 2018; Abstract and Introduction paragraph 1; live primary
    text lines 86–100 inspected
  accessed_at: '2026-10-19T23:38:33Z'
  support: refutes
  summary: Primary genome/transcriptome/proteome study treats L. ferriphilum as an
    iron oxidizer; the type strain gains energy from Fe(II) oxidation. It does not
    support classifying Leptospirillum as the nitrite-oxidizing partner asserted in
    this record.
  quote: gaining energy only via ferrous iron
- evidence_id: ncbi-project
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=bioproject&id=1261802&retmode=xml
  locator: ProjectDescr/Title, Description, Organism and archive links; body retained
    at /private/tmp/cm-review-session/000002/project-source/ncbi-project.body
  accessed_at: '2026-10-19T23:34:59.332711Z'
  support: partial
  summary: PRJNA1261802 is an acid-mine-drainage metagenomic assembly project; its
    general description does not identify the proposed three AOA/supporting species
    or validate their functions.
  snapshot_sha256: 60ede6b9dd2c12d390ce53cbee235850646ce4096c1b7c23dc6ddbcffa5ffc7d
- evidence_id: ena-project
  kind: database
  reference: https://www.ebi.ac.uk/ena/browser/api/xml/PRJNA1261802
  locator: STUDY title, abstract and cross references; body retained at /private/tmp/cm-review-session/000002/project-source/ena-project.body
  accessed_at: '2026-10-19T23:34:59.333066Z'
  support: partial
  summary: ENA independently resolves PRJNA1261802 to the same general AMD metagenome
    project.
  snapshot_sha256: 376a0dad4533f3e67f5c96a3447d951a923a8327d40c4bd704095b8cee21cdc5
- evidence_id: ena-runs
  kind: database
  reference: https://www.ebi.ac.uk/ena/portal/api/filereport?accession=PRJNA1261802&result=read_run&fields=run_accession,study_accession,sample_accession,scientific_name,instrument_platform,read_count,base_count&format=tsv
  locator: Entire two-row read_run TSV, base_count column; body retained at /private/tmp/cm-review-session/000002/project-source/ena-runs.body
  accessed_at: '2026-10-19T23:34:59.844150Z'
  support: partial
  summary: The two runs contain 53,964,165,000 bases in total, consistent with approximately
    54 Gb. This is total metagenomic sequencing yield, not per-genome coverage.
  snapshot_sha256: d723730de080f4fd300e432c8e3a470ba19dd2e2988c86a3134b7fd50752a15c
- evidence_id: ncbi-assemblies
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=assembly&term=PRJNA1261802%5BBioProject%5D&retmode=json&retmax=100
  locator: esearchresult.count and idlist; body retained at /private/tmp/cm-review-session/000002/project-source/ncbi-assemblies.body
  accessed_at: '2026-10-19T23:34:59.995818Z'
  support: partial
  summary: The project currently has three indexed assembly records. This verifies
    the count without verifying the record proposed organisms or gene functions.
  snapshot_sha256: fbf2f849c19c738415f9a6458ceac18a63ce25b38a306d087b44004d9ff2cf37
- evidence_id: project-assemblies
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=assembly&id=30290111,30290101,30290091&retmode=json
  locator: 'Three assembly esummary entries: accession, organism, taxid, BioSample,
    meta/Stats/total_length and release date; exact response body retained at /private/tmp/cm-review-session/000002/project-source/assembly-summaries.body'
  accessed_at: '2026-10-19T23:35:33.436658Z'
  support: partial
  summary: GCA_053486515.1 is Thermosulfuris yongpingense (SeqCode), 1,569,763 bp;
    GCA_053486495.1 and GCA_053486475.1 are Acidarchaeum fankouense (SeqCode), 1,448,496
    and 1,637,578 bp. Released November 2025, these do not match the proposed Nitrosotalea/Nitrososphaera/Ferroplasma
    genome identities or claimed 6–9 Mb combined genome size.
  snapshot_sha256: 37be8741ae08d8545f246b2847594b9a83ae5d0ad6e989242a0494e0400b78aa
- evidence_id: project-taxonomy
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=3693717,3693715&retmode=xml
  locator: 'NCBITaxon:3693717 and 3693715: ScientificName, Rank and Lineage; exact
    response body retained at /private/tmp/cm-review-session/000002/project-source/assembly-taxonomy.body'
  accessed_at: '2026-10-19T23:36:05.080006Z'
  support: partial
  summary: Both deposited species belong to Nitrososphaerota, class Conexivisphaeria,
    order Conexivisphaerales, family Thermosulfuridaceae. Their genera are Thermosulfuris
    and Acidarchaeum, not alternative spellings of Nitrosotalea or Nitrososphaera.
    Phylum membership alone does not establish ammonia oxidation.
  snapshot_sha256: a8cc56f8737e1f9b6d5dc13e41546af61d278827c83c3c413b0b0c60cbf7adb5
- evidence_id: schema
  kind: authority
  reference: src/communitymech/schema/communitymech.yaml
  locator: MicrobialCommunity, FunctionalRoleEnum, MetalRelevanceEnum and EvidenceItem
  accessed_at: '2026-10-19T23:41:55.729164Z'
  support: supports
  summary: Natural community context, source experiment and claimed roles must remain
    distinct. PRIMARY_PRODUCER denotes carbon fixation; SYNTROPHIC_PARTNER denotes
    syntrophic metabolism. PRIMARY metal relevance requires metal extraction/cycling
    as the primary function.
- evidence_id: history
  kind: record_content
  reference: history/records/AMD_Nitrososphaerota_Archaeal/2026-10-05T055158Z-codex-ce2f0a.yaml
  locator: Entire event; reports/causal_graph_review/decisions/20261005-seven-records.yaml
    target entry; discussions and embedded curation_history
  accessed_at: '2026-10-19T23:41:55.729170Z'
  support: supports
  summary: The prior graph curation explicitly removed unsupported urea and rescue
    claims, qualified the retained graph, and left non-graph taxa and environmental
    quantities for later audit. This history is preserved and does not certify the
    unreviewed fields.
- evidence_id: snippet-inventory
  kind: validation
  reference: /private/tmp/cm-review-session/000002/snippet-correspondence.json
  locator: Recursive inventory of all 30 record EvidenceItem snippets against the
    eight inspected cache files; exact and whitespace/case-normalized tests
  accessed_at: '2026-10-19T23:41:55.729532Z'
  support: supports
  summary: All 30 snippets match the cited cached source after whitespace/case normalization;
    line wrapping accounts for nonexact matches. The central problem is claim attribution
    and scope, not fabricated quotation text. Eight graph EvidenceItems cite six distinct
    publications; repeated excerpts are not independent replication.
  snapshot_sha256: cbbd2835f7df494550f6c66f3b95e056d49de9b0cc96a512aa35517ba8614c64
- evidence_id: adapter-resolution
  kind: search
  reference: kg-microbe-sources
  locator: PATH resolution and own isolated-checkout .venv/bin/kg-microbe-sources
    existence check; structured-adapter-resolution.json
  accessed_at: '2026-10-19T23:38:33.033241Z'
  support: context_only
  summary: No console runner was found on PATH or in this isolated checkout. Other
    checkouts were deliberately excluded from execution by user instruction.
  search_scope: PATH and own isolated checkout only; other checkouts excluded by user
    instruction.
- evidence_id: imodulondb-catalog
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: 'Entire public catalog: 20 organism keys and 28 datasets; own-runtime read-only
    HTTP response retained in session 000273 scratch'
  accessed_at: '2026-10-19T23:31:07.726770Z'
  support: context_only
  summary: The inspected catalog has no Nitrosotalea, Nitrososphaera, Nitrospira or
    Ferroplasma dataset. The record amoA, Amt, kdp and mgtA claims therefore have
    no matching iModulonDB organism/dataset/component to summarize. Absence from this
    catalog is not evidence against the genes or phenotype.
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
- evidence_id: check-validate
  kind: validation
  reference: UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true
    JUST_NO_DOTENV=true just --no-dotenv validate kb/communities/AMD_Nitrososphaerota_Archaeal.yaml
  locator: Actual output and exit_code=0; full JSON log /private/tmp/cm-review-session/000002/validate.json
  accessed_at: '2026-10-19T23:37:09.076268Z'
  support: context_only
  summary: 'No issues found

    uv run linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/AMD_Nitrososphaerota_Archaeal.yaml'
  snapshot_sha256: ad2af2792bd0384b8526d81e67e14d23033d19e7b1bc376890b3379c1c157c46
- evidence_id: check-validate-strict
  kind: validation
  reference: UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true
    JUST_NO_DOTENV=true just --no-dotenv validate-strict kb/communities/AMD_Nitrososphaerota_Archaeal.yaml
    --out /private/tmp/cm-review-session/000002/strict-report.tsv
  locator: Actual output and exit_code=0; full JSON log /private/tmp/cm-review-session/000002/validate-strict.json
  accessed_at: '2026-10-19T23:37:14.157762Z'
  support: context_only
  summary: "uv run python scripts/validate_strict.py kb/communities/AMD_Nitrososphaerota_Archaeal.yaml\
    \ --out /private/tmp/cm-review-session/000002/strict-report.tsv\nValidating 1\
    \ files with 17 workers; schema=/private/tmp/communitymech-record-reviews-20261019/src/communitymech/schema/communitymech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cm-review-session/000002/strict-report.tsv"
  snapshot_sha256: bf531c814a2cd2bf8a063288b59a54f348b35b66c86e19a263397bda97005e0d
- evidence_id: check-validate-terms
  kind: validation
  reference: UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true
    JUST_NO_DOTENV=true just --no-dotenv validate-terms kb/communities/AMD_Nitrososphaerota_Archaeal.yaml
  locator: Actual output and exit_code=0; full JSON log /private/tmp/cm-review-session/000002/validate-terms.json
  accessed_at: '2026-10-19T23:37:13.071674Z'
  support: context_only
  summary: '✅ Validation passed

    uv run linkml-term-validator validate-data kb/communities/AMD_Nitrososphaerota_Archaeal.yaml
    -s src/communitymech/schema/communitymech.yaml --labels'
  snapshot_sha256: 08fff0fa91bd5b433c0a8cbf8348cda4a64b94bc35ed1374d620789cc053b6df
- evidence_id: check-validate-gtdb
  kind: validation
  reference: UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true
    JUST_NO_DOTENV=true just --no-dotenv validate-gtdb kb/communities/AMD_Nitrososphaerota_Archaeal.yaml
  locator: Actual output and exit_code=0; full JSON log /private/tmp/cm-review-session/000002/validate-gtdb.json
  accessed_at: '2026-10-19T23:37:09.385840Z'
  support: context_only
  summary: 'PYTHONPATH=src uv run python scripts/validate_gtdb_coherence.py kb/communities/AMD_Nitrososphaerota_Archaeal.yaml


    files checked: 1

    incoherent blocks: 0

    malformed lineages: 0

    lineage conflicts: 0'
  snapshot_sha256: 5c54997fadb190cfcbadadc1c43df205fb39e57e2f17587fc84395a747ecce56
- evidence_id: check-validate-gtdb-domain
  kind: validation
  reference: UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true
    JUST_NO_DOTENV=true just --no-dotenv validate-gtdb-domain kb/communities/AMD_Nitrososphaerota_Archaeal.yaml
  locator: Actual output and exit_code=0; full JSON log /private/tmp/cm-review-session/000002/validate-gtdb-domain.json
  accessed_at: '2026-10-19T23:37:14.441093Z'
  support: context_only
  summary: 'files checked: 1

    contradictory lineages: 0

    PYTHONPATH=src uv run python scripts/validate_prokaryotic_lineage.py kb/communities/AMD_Nitrososphaerota_Archaeal.yaml'
  snapshot_sha256: 79b76522d91ce8c4843fe08242e1b18ffc5ed5f58f72908faf061639bb5fdee3
- evidence_id: check-validate-history
  kind: validation
  reference: UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true
    JUST_NO_DOTENV=true just --no-dotenv validate-history history/records/AMD_Nitrososphaerota_Archaeal
  locator: Actual output and exit_code=0; full JSON log /private/tmp/cm-review-session/000002/validate-history.json
  accessed_at: '2026-10-19T23:37:15.210142Z'
  support: context_only
  summary: No issues found
  snapshot_sha256: 3368b6b2fa8509076b064ed936919bf15e48abac2e1dacacd8c36873958e0b2d
- evidence_id: check-normalize-cache-names
  kind: validation
  reference: UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true
    JUST_NO_DOTENV=true uv run python scripts/normalize_cache_names.py --check
  locator: Actual output and exit_code=0; full JSON log /private/tmp/cm-review-session/000002/normalize-cache-names-check.json
  accessed_at: '2026-10-19T23:37:15.423423Z'
  support: context_only
  summary: Actual command returned exit 0 with no issues or output.
  snapshot_sha256: 704ee444be289adc0bbea29c97038c09eb71056c86aece51e9770cf2eae69ba8
- evidence_id: check-validate-references-explained
  kind: validation
  reference: UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true
    JUST_NO_DOTENV=true just --no-dotenv validate-references-explained kb/communities/AMD_Nitrososphaerota_Archaeal.yaml
  locator: Actual output and exit_code=0; full JSON log /private/tmp/cm-review-session/000002/validate-references-explained.json
  accessed_at: '2026-10-19T23:37:17.588959Z'
  support: context_only
  summary: "Validating kb/communities/AMD_Nitrososphaerota_Archaeal.yaml against schema\
    \ src/communitymech/schema/communitymech.yaml\nCache directory: references_cache\n\
    \nValidation Summary:\n  Reported validation issues: 0\n  All validations passed!\n\
    \n[annotate] This is not a count of checked excerpts (#1469). Native Discussion\
    \ evidence coverage remains incomplete (#476)."
  snapshot_sha256: 0a1ec6184465e93c92222c2ca0c658f7deaa539ad987c35f27a25f3b0ad9b200
- evidence_id: check-audit-network
  kind: validation
  reference: just --no-dotenv audit-network
  locator: Complete corpus output from 2026-10-19T07:30:27.845593+00:00; /private/tmp/cm-review-session/000320/audit-network.json
  accessed_at: '2026-10-19T07:30:27.845593Z'
  support: context_only
  summary: 'Actual full-corpus recipe exit 1: 462 records, 57 warnings in 21 records,
    zero errors. No AMD_Nitrososphaerota_Archaeal target findings. Reused same-session
    results against unchanged Git base and record bytes; other-record warnings are
    not assigned to this target.'
  snapshot_sha256: bedf3fd18a964bda429f7c6b5feb01b8918e1440b48a4329664501161c80e3f4
- evidence_id: check-check-network-quality
  kind: validation
  reference: just --no-dotenv check-network-quality
  locator: Complete corpus output from 2026-10-19T07:30:43.193891+00:00; /private/tmp/cm-review-session/000320/check-network-quality.json
  accessed_at: '2026-10-19T07:30:43.193891Z'
  support: context_only
  summary: 'Actual full-corpus recipe exit 1: 462 records, 57 warnings in 21 records,
    zero errors. No AMD_Nitrososphaerota_Archaeal target findings. Reused same-session
    results against unchanged Git base and record bytes; other-record warnings are
    not assigned to this target.'
  snapshot_sha256: 885e62e84ed8d3e69a6e5ef5be43f941ef64d756107c3b062846831f76e081aa
assessments:
- assessment_id: identity
  area: identity
  topic: Canonical identity and community boundary
  outcome: concern
  summary: The target is uniquely resolved as CommunityMech:000002. AMD nitrifier
    diversity is a supported ecological topic, but the record combines Colorado gene
    surveys, Indian archaeal amplicons, soil isolates and a separate biomining coculture
    into a fixed, stable community without same-system composition evidence. The graph
    recognizes this distinction; the description and taxon notes frequently do not.
  target_ids:
  - CommunityMech:000002
  evidence_ids:
  - record
  - amd-survey
  - malanjkhand
  - soil-isolate
  - ferroplasma-culture
  dimensions:
  - name: community_scope
    value: Natural AMD nitrifier guild synthesis
    definition: A conceptual synthesis of multiple studies, not a demonstrated four-member
      consortium.
    evidence_ids:
    - record
    - amd-survey
    - malanjkhand
  - name: experimental_setting
    value: AMD field surveys; distinct soil isolates and laboratory coculture
    definition: The measured endpoint and habitat of each source remain separate.
    evidence_ids:
    - amd-survey
    - soil-strains
    - ferroplasma-culture
  - name: source_strain
    value: Nitrosotalea Nd1/Nd2 and Ferroplasma BRL-115 in separate experiments
    definition: No same-system isolate pairing or AMD strain identity follows from
      these culture experiments.
    evidence_ids:
    - soil-strains
    - ferroplasma-culture
  - name: environment
    value: AMD-impacted sediments; ENVO:00001997 acid mine drainage
    definition: Environment term fits the surveyed habitat; it does not transfer soil
      physiology to the AMD community.
    evidence_ids:
    - amd-survey
    - malanjkhand
- assessment_id: taxon-0
  area: grounding
  topic: 'taxonomy[0]: Nitrosotalea identity, physiology, role and abundance'
  outcome: concern
  summary: NCBITaxon:1078905 has canonical label Nitrosotalea devaniterrae; the preferred
    historical Ca. N. devanaterra wording and GTDB:s__Nitrosotalea devanaterra are
    retained separately and pass native coherence/domain checks. The soil isolate
    supports acidophilic autotrophy and AMO/Amt/potential homeostasis genes. It does
    not establish exact isolate presence, 30–45% abundance or the stated per-gram
    amoA counts in AMD. Urease attribution conflicts with its inspected genome; 0.6–2.8
    nM Km and 100–120 h optimal doubling are not established by these citations. The
    2014 Nd1 growth rate of 0.29/day implies about 57 h under that experiment, illustrating
    condition dependence rather than a replacement community doubling time.
  target_ids:
  - CommunityMech:000002
  evidence_ids:
  - record
  - soil-isolate
  - acidophily-genome
  - soil-strains
  - amd-count-units
  dimensions:
  - name: ncbi_gtdb
    value: NCBITaxon:1078905; GTDB:s__Nitrosotalea devanaterra
    definition: Canonical NCBI label differs from source and GTDB naming; this is
      not proof of ecological species occurrence.
    evidence_ids:
    - record
    - soil-isolate
- assessment_id: taxon-1
  area: grounding
  topic: 'taxonomy[1]: Nitrososphaera-like archaeon'
  outcome: concern
  summary: NCBITaxon:497726 and GTDB:g__Nitrososphaera are genus-level grounding.
    The AMD survey supports affiliated amoA sequences, not an identified strain or
    measured acid-growth optimum, cell size, urease/HAO expression, 50–200 mg N/L
    optimum, syntrophic partner, 15–25% abundance or per-gram gene count. PMID:24909965
    studies two Nitrosotalea isolates and cannot establish the asserted Nitrososphaera
    acidophily.
  target_ids:
  - CommunityMech:000002
  evidence_ids:
  - record
  - amd-survey
  - soil-strains
  - amd-count-units
  dimensions:
  - name: ncbi_gtdb
    value: NCBITaxon:497726; GTDB:g__Nitrososphaera
    definition: Genus-level survey affiliation; no strain-resolved occurrence or physiology.
    evidence_ids:
    - record
    - amd-survey
- assessment_id: taxon-2
  area: grounding
  topic: 'taxonomy[2]: Ferroplasma acidiphilum'
  outcome: concern
  summary: NCBITaxon:74969 and the stored GTDB:s__Ferroplasma acidarmanus mapping
    pass native coherence/domain gates; the names are not independently rederived
    from genome mappings here. Malanjkhand V6 lineage evidence is broader than F.
    acidiphilum. BRL-115 chemomixotrophy is supported in a separate culture with Leptospirillum.
    This does not verify exact AMD abundance, AOA-directed detoxification, metal niche
    services, quantitative intracellular pH, iron-dominated cellular proteins, As/Cu/Zn
    resistance, or numeric pH/oxygen optima asserted for this guild. General cell-wall-free
    archaeal morphology does not supply these missing strain- and assay-specific measurements.
  target_ids:
  - CommunityMech:000002
  evidence_ids:
  - record
  - malanjkhand
  - ferroplasma-culture
  dimensions:
  - name: ncbi_gtdb
    value: NCBITaxon:74969; GTDB:s__Ferroplasma acidarmanus
    definition: Distinct stored taxonomic names pass coherence; neither supplies source-specific
      species identification.
    evidence_ids:
    - record
    - ferroplasma-culture
- assessment_id: taxon-3
  area: grounding
  topic: 'taxonomy[3]: Nitrospira-like bacterium'
  outcome: concern
  summary: NCBITaxon:1234 correctly denotes genus Nitrospira; GTDB is explicitly withheld
    rather than guessed. nxrB affiliations support nitrite-oxidation potential. The
    duplicated PMID:29209281 excerpts do not independently verify nitrite removal,
    partner rescue, comammox activity at 380 mg N/L, 30% relative abundance or 10^3–10^4
    nxrB/g. The original assay units and generally higher nxrB counts differ.
  target_ids:
  - CommunityMech:000002
  evidence_ids:
  - record
  - amd-survey
  - amd-count-units
  dimensions:
  - name: ncbi_gtdb
    value: NCBITaxon:1234; GTDB WITHHELD
    definition: Genus-level environmental affiliation; no precise GTDB species inferred.
    evidence_ids:
    - record
    - amd-survey
- assessment_id: node-0
  area: graph
  topic: 'ecological_interactions[0]: Archaeal Ammonia Oxidation to Nitrite'
  outcome: supported
  summary: PARTIAL is appropriate. Source physiology shows soil Nitrosotalea converts
    ammonia to nitrite; AMD amoA genes support community potential. The participants
    are Nitrosotalea and Nitrospira as conceptual guild context, not a measured isolate
    pair. Direction is ammonia/ammonium acquisition to nitrite production with carbon
    fixation. CHEBI:16134/28938/16301 and GO:0019329/0015977 are chemically/process
    appropriate, while preferred nitrification wording is broader than ammonia oxidation.
    The node explicitly prevents transfer of soil-strain identity and activity to
    AMD.
  target_ids:
  - CommunityMech:000002
  evidence_ids:
  - record
  - soil-isolate
  - acidophily-genome
  - amd-survey
- assessment_id: edge-0-1
  area: graph
  topic: 'ecological_interactions[0].downstream[0]: ammonia oxidation → nitrite oxidation'
  outcome: supported
  summary: The sole arrow points from archaeal ammonia oxidation to Nitrospira nitrite
    oxidation and is explicitly HYPOTHESIZED. Potential producer Nitrosotalea-like
    AOA → potential consumer Nitrospira is a chemically coherent nitrite sequence.
    The AMD survey detects both functional groups but does not track nitrite transfer,
    rate coupling, rescue or reciprocal benefit. The exact target resolves and the
    uncertainty label should be preserved. Shared short quotations in soil-isolate
    and amd-survey supply the bounded source basis, not proof of the arrow.
  target_ids:
  - CommunityMech:000002
  evidence_ids:
  - record
  - soil-isolate
  - amd-survey
  - history
- assessment_id: node-1
  area: graph
  topic: 'ecological_interactions[1]: Nitrite Oxidation to Nitrate by Nitrospira'
  outcome: supported
  summary: PARTIAL is appropriate for Nitrospira nxrB affiliation. Direction nitrite
    → nitrate and source genus Nitrospira fit the proposed pathway; CHEBI:16301/17632
    and GO:0019332 match. The node expressly disclaims measured nitrate production
    and partner detoxification. The single source supports genetic potential, not
    activity.
  target_ids:
  - CommunityMech:000002
  evidence_ids:
  - record
  - amd-survey
- assessment_id: node-2
  area: graph
  topic: 'ecological_interactions[2]: Putative Ferroplasma Organic Matter Turnover'
  outcome: supported
  summary: HYPOTHESIZED is appropriate. Source participant F. acidiphilum is an extrapolation
    from a separately studied BRL-115 culture; broad Thermoplasmata co-occurrence
    does not identify that species in the AMD assemblage. CHEBI:50860 is a broad organic
    entity substrate, not an identified exchanged metabolite. No AOA recipient or
    downstream arrow is asserted. The description correctly distinguishes culture-supported
    chemomixotrophy from untested AOA detoxification.
  target_ids:
  - CommunityMech:000002
  evidence_ids:
  - record
  - malanjkhand
  - ferroplasma-culture
- assessment_id: node-3
  area: graph
  topic: 'ecological_interactions[3]: Archaeal Ammonia-Oxidizer Diversity'
  outcome: supported
  summary: PARTIAL is appropriate for diversity. Nitrososphaera/Nitrosotalea affiliations
    come from AMD genes; the exact N. devaniterrae species descriptor is conceptual,
    not survey species identification. Ammonia/ammonium/nitrite and GO:0019329 describe
    shared nitrifier potential. The soil study compares two Nitrosotalea strains,
    so the node correctly rejects demonstrated complementary niches or reciprocal
    benefits between the named AMD participants. No causal arrow is asserted.
  target_ids:
  - CommunityMech:000002
  evidence_ids:
  - record
  - amd-survey
  - soil-strains
- assessment_id: environment-notes
  area: scope
  topic: 'environment_term.notes: environmental context and ranges'
  outcome: concern
  summary: Acid mine drainage and metal-rich acidic sediments are appropriate general
    habitat context. The specific ammonium ceiling, sulfate greater than 500 mg/L,
    temperature range, comparison with extreme AMD metal loads and implied taxon selection
    are not tied to same-system measurements in the inspected source text. Source-specific
    values and chemistry should be separated from general explanations, without extrapolating
    uninspected supplementary data.
  target_ids:
  - CommunityMech:000002
  evidence_ids:
  - record
  - amd-survey
  - malanjkhand
- assessment_id: environment-ph
  area: quantity
  topic: 'environmental_factors[0]: Acidic pH'
  outcome: concern
  summary: The survey measured site pH 3.2–8.3 and detected AOB/nxrB genes at 3.2
    and AOA genes at 3.5; this does not measure activity or establish a universal
    2.5–4.5 operational range, AOB exclusion below 5.5, vertical zones or species
    transitions. The soil isolate optimum is 4–5, with a separately stated growth
    range 4–5.5. Using the record own pKa 9.25 and pH 4 yields NH4/NH3 = 10^5.25 ≈177,828,
    not 10,000; this is an explicit arithmetic check, not a new environmental measurement.
    The pyrite reaction is an unbalanced schematic and should not be presented as
    quantitative stoichiometry.
  target_ids:
  - CommunityMech:000002
  evidence_ids:
  - record
  - amd-survey
  - soil-isolate
  - acidophily-genome
- assessment_id: environment-ammonium
  area: quantity
  topic: 'environmental_factors[1]: Ammonium Concentration'
  outcome: concern
  summary: The conversion 50–380 mg N/L to approximately 3.6–27 mM is dimensionally
    sound. The source excerpt about low pH/metals does not measure those ammonium
    concentrations. Neither inspected citation establishes the stated correlation
    r² 0.65–0.78, 50–200 mg/L optimum, inhibition above 300 mg/L, 5–20 microgram N/g/day
    consumption, or an AMD Km of 0.6–2.8 nM. The urea experiment is in soils. Amt-mediated
    acquisition is a proposed mechanism, not a measured active transport result for
    the AMD population.
  target_ids:
  - CommunityMech:000002
  evidence_ids:
  - record
  - amd-survey
  - urea-soils
  - acidophily-genome
- assessment_id: environment-temperature
  area: quantity
  topic: 'environmental_factors[2]: Temperature'
  outcome: concern
  summary: The field survey reports 7.1–21.2 degrees C, not a universal 15–25 degree
    regime. The quoted cultivation excerpt concerns pH, not temperature. Seasonal
    amplitude, depth stratification, Q10, 50% activity reduction at 10 degrees, negligible
    activity below 5 and spring/fall rate maxima are not supported by these sources.
    Nd1 and Nd2 culture optima differ (25 versus 35 degrees), and should not be averaged
    into a community optimum. Acidithiobacillus caldus is mentioned as a comparison
    without a source for its claimed optimum and must not become an inferred member.
  target_ids:
  - CommunityMech:000002
  evidence_ids:
  - record
  - amd-survey
  - soil-isolate
  - soil-strains
- assessment_id: environment-oxygen
  area: quantity
  topic: 'environmental_factors[3]: Oxygen Availability'
  outcome: concern
  summary: Aerobic ammonia/nitrite oxidation is reasonable pathway context. The survey
    measured 1.1–10 mg/L dissolved oxygen in field waters associated with 0–5 cm sediment
    composites; this is not a millimetre-resolved oxygen profile. Neither cited abstract
    establishes 5–15 mm penetration, defined taxon depth zones, O2 Km 2–10 micromolar,
    Ferroplasma optimum 1–3 mg/L, or 2–5 micromole O2/g/day consumption. The cited
    0.18 nM ammonia growth concentration is not oxygen evidence. The AMO reaction
    is a schematic biochemical context, not a measured AMD rate.
  target_ids:
  - CommunityMech:000002
  evidence_ids:
  - record
  - amd-survey
  - soil-isolate
  - ferroplasma-culture
- assessment_id: environment-genomes
  area: provenance
  topic: 'environmental_factors[4]: Genomic Data PRJNA1261802'
  outcome: concern
  summary: The accession resolves, approximately 54 Gb and three assemblies are verified,
    and both deposited genera are Nitrososphaerota. The assemblies instead identify
    Thermosulfuris and Acidarchaeum in Conexivisphaeria. Their combined length is
    about 4.66 Mb, not the proposed 6–9 Mb. The claimed AOA/Ferroplasma identities,
    high-quality designation, 1000–6000x coverage, GC ranges and gene/pathway/lipid/glycosylation/HGT
    inventories are not established by generic database documentation or the unrelated
    Nitrosotalea isolate genome. No sequence annotation or read mapping was performed
    here.
  target_ids:
  - CommunityMech:000002
  evidence_ids:
  - record
  - ncbi-project
  - ena-project
  - ena-runs
  - ncbi-assemblies
  - project-assemblies
  - project-taxonomy
  - ncbi-resources
  - acidophily-genome
- assessment_id: cultivation
  area: scope
  topic: Natural field context versus cultivation conditions
  outcome: supported
  summary: 'No growth_media block is present, which is not intrinsically defective
    for a natural field assemblage. The relevant sources provide distinct culture
    conditions: Nitrosotalea enrichment used mineral salts, 500 micromolar NH4Cl,
    pH 4.7, 1% soil inoculum, darkness and no shaking at 28/37 degrees; routine maintenance
    used 2% mid-exponential transfers at pH 5, with Nd1 at 25 and Nd2 at 37 degrees.
    BRL-115 yeast-extract growth belongs to the separate biomining pair. These conditions
    should not be inserted as the AMD community medium.'
  target_ids:
  - CommunityMech:000002
  evidence_ids:
  - record
  - soil-strains
  - ferroplasma-culture
  dimensions:
  - name: medium
    value: No same-community cultivation medium established
    definition: Separate isolate mineral-salts cultures and Ferroplasma yeast-extract
      cultures retain experiment-specific scope.
    evidence_ids:
    - soil-strains
    - ferroplasma-culture
  - name: conditions
    value: Field habitat measurements and isolate optima remain distinct
    definition: No unsupported unified temperature, oxygen, pH, vessel, atmosphere
      or incubation is supplied.
    evidence_ids:
    - amd-survey
    - soil-strains
- assessment_id: ingredients
  area: evidence
  topic: 'related_ingredients[0..2]: ammonia, nitrite and urea'
  outcome: concern
  summary: CHEBI:16134, 16301 and 16199 correctly identify ammonia, nitrite and urea.
    Ammonia as AOA substrate and nitrite as nitrification intermediate are supported.
    The ammonia relevance overstates universal AOB exclusion; nitrite relevance asserts
    a demonstrated handoff/syntrophic core despite the graph hypothesis; urea relevance
    transfers a group-level soil result to the AMD guild and named Nitrosotalea despite
    the genome limitation. Exact chemical grounding does not fix these biological
    scope errors.
  target_ids:
  - CommunityMech:000002
  evidence_ids:
  - record
  - soil-isolate
  - amd-survey
  - urea-soils
  - acidophily-genome
- assessment_id: functional-roles
  area: representation
  topic: taxonomy[*].functional_role and community stability
  outcome: concern
  summary: PRIMARY_PRODUCER is compatible with the AOA/Nitrospira autotrophic pathway
    context, but marker detection does not establish all field activity. CROSS_FEEDER
    for Ferroplasma has support in its separate Leptospirillum culture. SYNTROPHIC_PARTNER
    on all four taxa, the fixed abundance assignments, and STABLE ecological state
    lack same-system exchange or longitudinal stability evidence. These labels should
    follow the graph limited evidence rather than implying established mutual dependence.
  target_ids:
  - CommunityMech:000002
  evidence_ids:
  - record
  - schema
  - amd-survey
  - ferroplasma-culture
  - soil-isolate
- assessment_id: metal-classification
  area: representation
  topic: metals_present, metal_relevance and metal_notes
  outcome: concern
  summary: Copper and iron are appropriate AMD context. PRIMARY metal relevance is
    not justified solely by a metal-rich habitat for a record centered on nitrogen
    cycling; Ferroplasma metal cycling remains an extrapolation here. metal_notes
    claims detection from graph CHEBI metabolites and environmental measurements,
    but this record graph contains only nitrogen species and organic entity, and its
    factors contain no quantified metal measurement. Keyword context exists; the stated
    detection pathways do not.
  target_ids:
  - CommunityMech:000002
  evidence_ids:
  - record
  - schema
  - amd-survey
  - malanjkhand
- assessment_id: history-consistency
  area: provenance
  topic: Discussions, prior graph decisions and evidence placement
  outcome: supported
  summary: Both discussion attachments resolve to retained nodes and correctly state
    the unresolved nitrite-transfer, urease and archaeal partner questions. The append-only
    event matches the embedded curation history and records AI assistance. The prior
    graph review explicitly excluded the non-graph claims now audited; its qualifications
    should be propagated during future curation, not interpreted as full-record approval.
  target_ids:
  - CommunityMech:000002
  evidence_ids:
  - record
  - history
- assessment_id: imodulondb
  area: evidence
  topic: Structured gene/trait source cross-check
  outcome: not_applicable
  summary: amoA/Amt/kdp/mgtA and acid-stress claims trigger structured-source consideration.
    The permitted local runner is unavailable. The public iModulonDB catalog provides
    no matching organism dataset, so no component search or summary is applicable.
    An unrelated archaeal dataset cannot substantiate these claims, and catalog absence
    is not negative biological evidence.
  target_ids:
  - CommunityMech:000002
  evidence_ids:
  - record
  - adapter-resolution
  - imodulondb-catalog
- assessment_id: validation
  area: schema
  topic: Native gates and ontology ID/label correspondence
  outcome: supported
  summary: Focused schema, strict, term, reference, GTDB coherence/domain and history
    gates all passed with exit 0 and no reported ontology skips. They cover the four
    taxonomic descriptors, ENVO:00001997, nitrogen/organic entity CHEBI terms and
    GO process terms. Their canonical meanings fit the intended entities/processes,
    but exact source occurrence and claimed roles require the scientific qualifications
    above. No target network issue was reported. Label matching and cache snippet
    matching do not certify claim support.
  target_ids:
  - CommunityMech:000002
  evidence_ids:
  - record
  - schema
  - check-validate
  - check-validate-strict
  - check-validate-terms
  - check-validate-references-explained
  - check-validate-gtdb
  - check-validate-gtdb-domain
  - check-validate-history
  - snippet-inventory
- assessment_id: scores
  area: completeness
  topic: Native completeness and validation quality
  outcome: concern
  summary: The complete presence rubric scores 80, while validation quality scores
    93 with four P2 and one P3 findings. These are separate native metrics, not scientific
    approval. Eight node EvidenceItems across four interactions yield a mean of 2;
    duplicate and cross-system citations are not independent replication. Network
    COMPLETE is based on participant and reference integrity, not whether every causal
    node is connected.
  target_ids:
  - CommunityMech:000002
  evidence_ids:
  - record
  - check-audit-network
  - history
  metrics:
  - name: completeness
    value: 80
    unit: points
    minimum: 0
    maximum: 100
    definition: min(100, required metadata/taxonomy-with-roles 50 + environment 5
      + at least 3 environmental factors 10 + at least 3 interactions 10 + external
      resources 0 + growth_media 0 + associated_datasets 0 + any interaction metabolites
      5) = 80. Presence rubric only; unsupported content still counts as present.
  - name: validation_quality
    value: 93
    unit: points
    minimum: 0
    maximum: 100
    definition: clamp(100 - 50*P1 - 10*P2 - 2*P3 + 20*min(mean_interaction_evidence/2,1)
      + 15 for COMPLETE network,0,100). P1=0, P2=4, P3=1; evidence=8/4=2; COMPLETE
      target network. 100-40-2+20+15=93. Unrelated corpus warnings are retained separately.
  - name: P1
    value: 0
    unit: findings
    definition: Target-specific blockers.
  - name: P2
    value: 4
    unit: findings
    definition: Target-specific major findings.
  - name: P3
    value: 1
    unit: findings
    definition: Target-specific minor findings.
  - name: interaction_evidence
    value: 2
    unit: evidence items per interaction
    denominator: 4
    definition: Eight EvidenceItems directly attached to four nodes; repeated source
      excerpts are not independent corroboration.
findings:
- finding_id: community-scope
  issue_key: cm-000002-community-scope
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: A multi-study guild is represented as a measured fixed community
  description: The description, taxon membership/abundances and syntrophic roles combine
    separate AMD surveys with soil isolates and a Ferroplasma–Leptospirillum culture.
    No cited source identifies the stated four-member stable assemblage, exact species
    abundances, per-gram gene counts, partner rescue or reciprocal niche benefits.
    PMID:29209281 uses counts per microgram DNA and usually greater nxrB abundance.
    The graph and open discussions already acknowledge these limits; related nitrite
    relevance and taxon notes contradict them.
  target_ids:
  - CommunityMech:000002
  field_paths:
  - description
  - ecological_state
  - taxonomy[0].abundance_value
  - taxonomy[1].abundance_value
  - taxonomy[2].abundance_value
  - taxonomy[3].abundance_value
  - taxonomy[*].functional_role
  - taxonomy[1].evidence[1].explanation
  - taxonomy[2].taxon_term.notes
  - taxonomy[3].taxon_term.notes
  - related_ingredients[1].relevance
  evidence_ids:
  - record
  - amd-survey
  - amd-count-units
  - malanjkhand
  - soil-isolate
  - soil-strains
  - ferroplasma-culture
  - history
  rule_id: CLAUDE.claim-level-evidence; review-checklist.scope
  native_severity: P2
  normalization_reason: 'P2 major: unsupported attribution or quantitative scope materially
    changes the ecological or mechanistic interpretation.'
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/AMD_Nitrososphaerota_Archaeal.yaml
    role: canonical_record
- finding_id: metabolic-attribution
  issue_key: cm-000002-metabolic-attribution
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Named organism mechanisms exceed or conflict with the source evidence
  description: Nitrosotalea urease-based adaptation conflicts with its cited closed-genome
    study. The stated 0.6–2.8 nM Km is not measured for this organism; growth at 0.18
    nM is a different endpoint, and the genome paper discusses marine Nitrosopumilus
    kinetics. Predicted Amt transport/homeostasis and inferred glycosylation/lipid
    protection are presented as established mechanisms. Leptospirillum is incorrectly
    described as a nitrite oxidizer, and Nitrososphaera HAO/urease expression lacks
    a matching source. Soil urea-supported nitrification cannot establish that pathway
    in this AMD assemblage.
  target_ids:
  - CommunityMech:000002
  field_paths:
  - description
  - taxonomy[0].taxon_term.notes
  - taxonomy[1].taxon_term.notes
  - environmental_factors[1].description
  - related_ingredients[0].relevance
  - related_ingredients[2].relevance
  evidence_ids:
  - record
  - acidophily-genome
  - soil-isolate
  - soil-strains
  - urea-soils
  - leptospirillum-primary
  rule_id: CLAUDE.claim-level-evidence; review-checklist.evidence
  native_severity: P2
  normalization_reason: 'P2 major: unsupported attribution or quantitative scope materially
    changes the ecological or mechanistic interpretation.'
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/AMD_Nitrososphaerota_Archaeal.yaml
    role: canonical_record
- finding_id: environment-quantities
  issue_key: cm-000002-environment-quantities
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Environmental and physiological numbers lack source-matched measurements
  description: environment_term.notes and the pH, ammonium, temperature and oxygen
    fields contain unsupported operating ranges, correlations, rates, gradients, seasonal
    effects and species optima. Their snippets often address another variable or report
    genes rather than activity. The 50–380 mg N/L conversion is valid, but the underlying
    field concentration is unverified. The record own pKa gives an ammonium/ammonia
    ratio near 178,000 at pH 4, not 10,000. Soil pH optimum versus range and isolate
    doubling endpoints are also conflated. The field survey actual pH, temperature
    and oxygen ranges should retain site context, not be replaced by a universal protocol.
  target_ids:
  - CommunityMech:000002
  field_paths:
  - description
  - environment_term.notes
  - taxonomy[0].taxon_term.notes
  - taxonomy[1].taxon_term.notes
  - taxonomy[2].taxon_term.notes
  - environmental_factors[0]
  - environmental_factors[1]
  - environmental_factors[2]
  - environmental_factors[3]
  evidence_ids:
  - record
  - amd-survey
  - soil-isolate
  - soil-strains
  - acidophily-genome
  - ferroplasma-culture
  - urea-soils
  rule_id: CLAUDE.claim-level-evidence; review-checklist.quantity
  native_severity: P2
  normalization_reason: 'P2 major: unsupported attribution or quantitative scope materially
    changes the ecological or mechanistic interpretation.'
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/AMD_Nitrososphaerota_Archaeal.yaml
    role: canonical_record
- finding_id: project-provenance
  issue_key: cm-000002-project-provenance
  category: provenance
  severity: major
  status: open
  certainty: confirmed
  title: Verified BioProject counts are followed by unsupported genome identities
    and functions
  description: PRJNA1261802 does contain about 54 Gb and three assemblies, and its
    deposited species are Nitrososphaerota. Current records identify Thermosulfuris
    yongpingense and Acidarchaeum fankouense in Conexivisphaeria, not the proposed
    Nitrosotalea, Nitrososphaera and Ferroplasma/Acidiplasma genomes. Sizes also differ.
    Generic NCBI resources documentation and another isolate genome do not substantiate
    predicted gene inventories, GC, completeness, HGT, or 1000–6000x coverage. These
    fields conflate valid accession-level counts with unverified biological interpretation.
  target_ids:
  - CommunityMech:000002
  field_paths:
  - description
  - environmental_factors[4].description
  - environmental_factors[4].evidence
  evidence_ids:
  - record
  - ncbi-project
  - ena-project
  - ena-runs
  - ncbi-assemblies
  - project-assemblies
  - project-taxonomy
  - ncbi-resources
  - acidophily-genome
  rule_id: CLAUDE.claim-level-evidence; review-checklist.provenance
  native_severity: P2
  normalization_reason: 'P2 major: unsupported attribution or quantitative scope materially
    changes the ecological or mechanistic interpretation.'
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/AMD_Nitrososphaerota_Archaeal.yaml
    role: canonical_record
- finding_id: metal-provenance
  issue_key: cm-000002-metal-provenance
  category: representation
  severity: minor
  status: open
  certainty: confirmed
  title: Metal relevance and detection notes exceed the represented evidence
  description: Copper/iron habitat context is supported, but PRIMARY asserts primary
    metal extraction/cycling while the record focuses on nitrification. The automated-looking
    metal_notes claims CHEBI metal metabolites and measured environmental metal factors
    that are not present in this target. This is a bounded representation/provenance
    mismatch rather than denial of metal-rich AMD.
  target_ids:
  - CommunityMech:000002
  field_paths:
  - metal_relevance
  - metal_notes
  evidence_ids:
  - record
  - schema
  - amd-survey
  - malanjkhand
  rule_id: CLAUDE.claim-level-evidence; review-checklist.representation
  native_severity: P3
  normalization_reason: 'P3 minor: bounded classification/provenance mismatch, with
    metal-rich AMD context otherwise supported.'
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/AMD_Nitrososphaerota_Archaeal.yaml
    role: canonical_record
actions:
- action_id: fix-community-scope
  description: Constrain this maintained record to an explicitly sourced conceptual
    guild or a defined sampled assemblage. Qualify species presence, abundances and
    partner roles to each source scope; preserve the graph uncertainty and unresolved
    discussions.
  finding_ids:
  - community-scope
  target_ids:
  - CommunityMech:000002
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/AMD_Nitrososphaerota_Archaeal.yaml
    role: canonical_record
  acceptance_checks:
  - Every retained member/abundance has a same-system source and original measurement
    unit; marker counts are not converted to organism percentages without justification.
  - Taxonomic rank matches source resolution; soil isolate physiology does not establish
    species identity in AMD.
  - STABLE and SYNTROPHIC_PARTNER are retained only with their required ecological
    evidence or changed to supported representations.
  - just validate-strict kb/communities/AMD_Nitrososphaerota_Archaeal.yaml; just validate-terms
    kb/communities/AMD_Nitrososphaerota_Archaeal.yaml; just validate-gtdb kb/communities/AMD_Nitrososphaerota_Archaeal.yaml;
    just validate-references-explained kb/communities/AMD_Nitrososphaerota_Archaeal.yaml
- action_id: fix-metabolic-attribution
  description: Remove or explicitly qualify unsupported organism-specific pathways
    and kinetic claims. Attach separate evidence to gene presence, expression, biochemical
    activity and ecological function; correct the Leptospirillum energy-metabolism
    attribution.
  finding_ids:
  - metabolic-attribution
  target_ids:
  - CommunityMech:000002
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/AMD_Nitrososphaerota_Archaeal.yaml
    role: canonical_record
  acceptance_checks:
  - Retained urease claims identify the actually tested taxon and habitat; the Nitrosotalea
    genome conflict is preserved.
  - Km, growth substrate concentration and transport hypotheses remain separate endpoints
    with organism/assay conditions.
  - Predicted acidophily mechanisms are not promoted to causal demonstration without
    functional experiments.
  - just validate-strict kb/communities/AMD_Nitrososphaerota_Archaeal.yaml; just validate-references-explained
    kb/communities/AMD_Nitrososphaerota_Archaeal.yaml
- action_id: fix-environment-quantities
  description: Audit each numeric assertion against its original measurement, units,
    sampled system and endpoint. Remove unsupported numerical specificity, correct
    the acid-base calculation, and distinguish observed field conditions from laboratory
    optima and proposed mechanisms.
  finding_ids:
  - environment-quantities
  target_ids:
  - CommunityMech:000002
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/AMD_Nitrososphaerota_Archaeal.yaml
    role: canonical_record
  acceptance_checks:
  - No rate, correlation, depth, oxygen affinity, ammonium optimum or seasonal statement
    is retained on a general-context quote alone.
  - Growth ranges, optimum, doubling time, gene abundance and measured activity are
    separately labeled.
  - Balanced chemistry or an explicitly schematic equation is used; conversions state
    N-mass versus compound-mass basis.
  - just validate-strict kb/communities/AMD_Nitrososphaerota_Archaeal.yaml; just validate-references-explained
    kb/communities/AMD_Nitrososphaerota_Archaeal.yaml
- action_id: fix-project-provenance
  description: Preserve the verified project accession and sequencing/assembly counts
    with direct provenance. Replace proposed genome identities with source-supported
    descriptions or remove the unsupported association to this guild; require accession-specific
    annotation before retaining gene, coverage or quality claims.
  finding_ids:
  - project-provenance
  target_ids:
  - CommunityMech:000002
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/AMD_Nitrososphaerota_Archaeal.yaml
    role: canonical_record
  acceptance_checks:
  - Source access date, assembly accession/version, lineage and source-provided statistics
    are recorded distinctly.
  - Approximately 54 Gb and three assemblies are not incorrectly rejected; Nitrososphaerota
    phylum identity is preserved.
  - No function is inferred solely from phylum, generic database citation or total
    metagenomic read yield.
  - just validate-strict kb/communities/AMD_Nitrososphaerota_Archaeal.yaml; just validate-references-explained
    kb/communities/AMD_Nitrososphaerota_Archaeal.yaml
- action_id: fix-metal-provenance
  description: Choose metal relevance according to the schema meaning and the supported
    primary process. Replace detection notes with accurate traceable context rather
    than claiming nonexistent local measurement paths.
  finding_ids:
  - metal-provenance
  target_ids:
  - CommunityMech:000002
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/AMD_Nitrososphaerota_Archaeal.yaml
    role: canonical_record
  acceptance_checks:
  - The selected relevance level matches the actual documented function.
  - Each detection/provenance statement points to a field and source that exists in
    the maintained record.
  - just validate-strict kb/communities/AMD_Nitrososphaerota_Archaeal.yaml
limitations:
- Full primary text was inspected for PMID:26896134 and 29209281; cached full text
  plus live primary metadata/abstract were used for 24909965. PMID:21896746 assessment
  uses abstract and available figure captions. PMID:33388792, 27535541 and 22592820
  are limited to accessible abstracts; inaccessible full texts or supplements are
  not assumed to lack protocols.
- Primary NCBI and ENA project, read-run, assembly and lineage metadata were inspected.
  No metagenomic reads, annotations, completeness/contamination tools, coverage calculations
  or functional experiments were analyzed; unverified function claims are not declared
  biologically impossible.
- The existing GTDB coherence/domain gates passed, but historical genome support counts,
  mapping fractions and reclassification provenance were not independently regenerated.
- The optional structured adapter was unavailable in the permitted runtime. The inspected
  iModulonDB public catalog has no matching target organism dataset; this limits applicability,
  not biological plausibility.
- Required corpus network gates returned warning failures outside this target; those
  actual exit statuses remain in this report.
- The review was performed by an agent with delegated validators and primary metadata
  retrieval. No target was authored or edited this session; prior curation also used
  codex, so person-level independence is unknown.
- Search for related local sources/decisions used rg --no-ignore --hidden across references_cache,
  history, reports, research and kb/taxa for the record slug and PRJNA1261802, including
  ignored files; broad generated HTML/JSON/TSV/CSV/TTL outputs were excluded. Absence
  statements are bounded to that search and the fully inspected source responses.
notes:
- No record, source cache, append-only history, generated product or scientific-status
  field was changed. Proposed curation requires separate authorization.
- Shared short quotations are attached once and reused by node/arrow assessments;
  all cached article quotations are exact and total at most 25 words per publication.
- All 30 target EvidenceItems were examined. Lexical correspondence does not cure
  incorrect explanation, assay, taxon or habitat attribution.
tags:
- record-review
- natural-community
- amd
- batch-01
```
