# Clostridial fusion coculture source and protocol review

- Review: 20261021T200731Z-clostridial-fusion-record-review
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-21T19:55:48.180220Z
- Finished UTC: 2026-10-21T20:07:31.209210Z
- Reviewer: codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Three open main papers and critical supplements support the defined WT pair, eight qualified interaction nodes and two hypothesized arrows. Two major findings correct WT-versus-engineered transfer claims and cultivation handling; two minor findings repair GTDB provenance and local role/population evidence. All eight focused native checks pass.

## Scope And Provenance

Whole maintained record assessed against current source science, declared supplementary/visual coverage, literal schema/ontology authority and bounded public provenance/resources.

Selection: Only released CommunityMech:000336 in owned batch 11.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 95812d3412d5aab41fd03422340cf736ac7b56f3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000336 | kb/communities/Clostridium_Acetobutylicum_Ljungdahlii_Fusion_Coculture.yaml | maintained | Clostridium acetobutylicum-Clostridium ljungdahlii Syntrophic Fusion Coculture |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000336 | validate passed on this record; scientific support is separately assessed. |
| validate-strict | passed | True | CommunityMech:000336 | validate-strict passed on this record; scientific support is separately assessed. |
| validate-terms | passed | True | CommunityMech:000336 | validate-terms passed on this record; scientific support is separately assessed. |
| validate-references-explained | passed | True | CommunityMech:000336 | validate-references-explained passed on this record; scientific support is separately assessed. |
| validate-gtdb | passed | True | CommunityMech:000336 | validate-gtdb passed on this record; scientific support is separately assessed. |
| validate-gtdb-domain | passed | True | CommunityMech:000336 | validate-gtdb-domain passed on this record; scientific support is separately assessed. |
| validate-history | passed | True | CommunityMech:000336 | validate-history passed on this record; scientific support is separately assessed. |
| normalize-cache-names-check | passed | True | CommunityMech:000336 | normalize-cache-names-check passed on this record; scientific support is separately assessed. |
| audit-network | failed | True | CommunityMech:000336 | Existing batch 11 corpus diagnostic retains its actual nonzero result; focal network separately reports COMPLETE. |
| check-network-quality | failed | True | CommunityMech:000336 | Existing batch 11 corpus diagnostic retains its actual nonzero result; focal network separately reports COMPLETE. |
| Current-claim source review | passed | True | CommunityMech:000336 | Three complete scientific mains, 20 main figures and declared critical SI assessed; founding abstract and unread supplementary regions remain explicit. |
| Reference-specific excerpt verification | passed | True | CommunityMech:000336 | All 41 strict reference-specific matches: 15 abstract, 25 body, one DATA AVAILABILITY back matter; all 41 cache matches. |
| Ontology, schema, GTDB and strain authority | passed | True | CommunityMech:000336 | Nineteen ID-label pairs/36 occurrences match; source scope, exact mapping routes and culture semantics assessed. |
| Optional structured expression-source adapter | unavailable | False | CommunityMech:000336 | Same-batch 403 discovery is explicitly reused with fresh runtime compatibility. The other-checkout executable was not used. |
| Experimental and raw-data reproduction | skipped | False | CommunityMech:000336 | No new culture, raw-read processing, external code execution or statistical recalculation. |

## Scientific And Domain Assessments

### WT pairing, reporter context and community scope

identity: concern. Targets: CommunityMech:000336.

Keep the two WT members and synthetic laboratory scope; narrow the description.

WT structural fusion and chemical protein-label transfer are supported. RNA uses a Halo reporter; DNA integration uses a plasmid-bearing donor and selected recipients. These engineered observations belong in scoped contextual bibliography, not an unconditional WT-summary claim. No extra member or WT DNA node is needed.

### Taxon, chemical, environment and GTDB authority

grounding: concern. Targets: CommunityMech:000336.

All 19 labels match; repair three mapping-provenance fields without changing valid species targets.

1488 exact-ID and 1538 name-fallback mappings reproduce the existing species classifications. Both strain-absence notes are false in the current crosswalk. Exact strain mappings use different denominators and are optional. Laboratory environment, encoded chemicals/processes and source aliases are appropriate at their qualified scopes.

### Local roles and population evidence

evidence: concern. Targets: CommunityMech:000336.

Attach utilization evidence for the C. acetobutylicum recipient role or omit that optional assignment.

H2/CO2 donation does not itself establish C. acetobutylicum CROSS_FEEDER. Do not declare reciprocal uptake impossible or impose a carbon/energy-growth test. PRIMARY_DEGRADER can refer to founding complex-carbohydrate potential rather than glucose complexity. Broad syntrophic roles and C. ljungdahlii primary production remain valid. Keep ordinal abundance, separating prior cell-population rationale, current aligned-mRNA ratio and OD-based inoculum.

### ecological_interactions[0]

graph: supported. Targets: CommunityMech:000336.

Retain gas exchange and the qualified feedback arrow.

C. acetobutylicum produces H2/CO2 used by the acetogen. The edge to proposed hydrogenase relief remains HYPOTHESIZED; neither net gas production nor transcription alone measures local turnover or causal enzyme relief.

### ecological_interactions[1]

graph: supported. Targets: CommunityMech:000336.

Retain the qualified arginine route.

Measured amino-acid profiles, gene expression and recipient supplementation support a proposed route. They do not trace donor arginine, directly measure ATP from deimination or establish transfer quantitatively.

### ecological_interactions[2]

graph: supported. Targets: CommunityMech:000336.

Retain the qualified histidine/Wood–Ljungdahl explanation.

Recipient monoculture histidine effects and transcript patterns support the hypothesis. Histidine-dependent acetate is not isotope-traced carbon fixation or direct donor-to-recipient flux.

### ecological_interactions[3]

graph: supported. Targets: CommunityMech:000336.

Retain the untyped proposed feedback mechanism.

Early glucose consumption is a measured proxy; local H2, hydrogenase activity and species-resolved reciprocal growth remain unmeasured. Keep the uncertainty and existing direction.

### ecological_interactions[4]

graph: supported. Targets: CommunityMech:000336.

Retain measured contact-associated transcription with proposed growth benefit.

Transwell separation supports contact association but does not identify fusion specifically or equate mRNA abundance with growth rate. Keep this community-level node and existing unset interaction type.

### ecological_interactions[5]

graph: supported. Targets: CommunityMech:000336.

Retain proposed competition/inhibition without promoting it to direct antagonism.

Amino-acid depletion and transcriptional responses are compatible with the authors’ explanation; specific competition or inhibitory mediator perturbation was not performed.

### ecological_interactions[6]

graph: supported. Targets: CommunityMech:000336.

Retain WT structural/protein evidence and reporter qualifications.

The node already distinguishes WT structure/protein transfer from reporter RNA and excludes unmodified-pair DNA claims. Contact separation is not fusion-specific. Keep the edge to product emergence HYPOTHESIZED.

### ecological_interactions[7]

graph: supported. Targets: CommunityMech:000336.

Retain product emergence within reported culture and control conditions.

Isopropanol and 2,3-butanediol are coculture outcomes under specified conditions. Avoid a universal claim that either species can never produce them, and do not certify fusion as the necessary cause.

### Type I, Type II, preculture and control protocols

completeness: concern. Targets: CommunityMech:000336.

Correct manual pH, species-specific heat shock, vessel class and experimental stage separation.

Retain supported 37°C, anaerobiosis, 60 mL Type I volume and 5 g/L yeast extract. Type I pH was adjusted at 11 h; ph_controlled:false based on absent apparatus is wrong. Loose-cap bottles are not sealed serum bottles. Keep 8 mL Type II and gas-fed/shaken C. ljungdahlii monocultures separate. The chamber atmosphere is not a measured sealed headspace. No complete founding recipe or unverified cross-Mech link is invented.

### Environmental factors and metal relevance

evidence: supported. Targets: CommunityMech:000336.

Keep laboratory/chamber/venting/separation context and current nonmetal scope.

The three environmental factors have direct support. The medium’s analytical or background components do not create a metal mechanism; NOT_APPLICABLE with empty metal lists is appropriate for this record. No plant, host or natural-community environment is added.

### Bibliographic resources and sequencing project

provenance: supported. Targets: CommunityMech:000336.

Retain four publications and verified PRJNA1167669 with assay-specific limits.

Fifty-four archive samples/runs/experiments support the recorded project identity, not a claim that every species-labeled library is a monoculture. Preserve the source/archive sequencer discrepancy without silently normalizing metadata. The DNA-transfer publication remains useful contextual bibliography. No new resource finding or raw-data reanalysis is required.

### Reference-specific evidence and source availability

evidence: supported. Targets: CommunityMech:000336.

All 41 excerpts strictly match their fresh sources; surrounding overclaims remain separately actionable.

The exact partition is 15 abstract, 25 body and one back-matter excerpt. Four founding excerpts rely on its fresh abstract. The complete three open scientific mains and critical SI cover the current claims, despite unavailable founding body/recipe/SI and bounded unread SI/data regions. The stale abstract_only cache headers do not erase their appended full texts and do not justify a new scientific finding.

### Historical repairs, current issue ownership and immutable scope

provenance: supported. Targets: CommunityMech:000336.

Preserve the qualified graph repairs and use current issue 1317 for overlapping non-graph work.

Issue 1316 is closed; 748 resolved ordinal semantics, while 749/752 retain upstream discussion. Current local definitions control. Sidecars were read in full; supporting cache reading was front matter plus all encoded contexts and full-byte lexical checks, not three whole appended article rereads. No historical event, cache or issue was rewritten.

### Focused checks and completed current-claim review

schema: supported. Targets: CommunityMech:000336.

Eight focused checks pass; corpus diagnostics retain their actual nonzero outcomes.

Only review artifacts are written. Canonical, cache, history and generated products remain unchanged. Parent persistence may save the new immutable review bundle after independent audit. Passing native checks do not certify the WT summary or protocol, and the optional adapter was unavailable.

### Native completeness and quality

completeness: supported. Targets: CommunityMech:000336.

Completeness 100; raw quality 111 caps at 100.

## Findings

### scope-wild-type-summary: Scope the WT summary to the demonstrated experimental pair

major / open / confirmed; issue key: cm-000336-scope-wild-type-summary.

The description unconditionally attributes RNA and DNA exchange to the WT pair. WT structural fusion and protein-label exchange are supported; RNA uses C. acetobutylicum-Halo, and DNA integration uses a plasmid-bearing C. ljungdahlii donor and selected recipients. The graph already preserves these distinctions.

### correct-cultivation-protocol: Correct culture conditions that change experimental handling

major / open / confirmed; issue key: cm-000336-correct-cultivation-protocol.

The record infers no pH control from absent apparatus, applies heat shock without member restriction, calls loosened screw-cap bottles sealed serum bottles and compresses distinct Type II/control conditions into the Type I setup. The source explicitly adjusts Type I pH at 11 h and heat-shocks only C. acetobutylicum.

### repair-gtdb-provenance: Repair GTDB mapping route and stale strain-absence notes

minor / open / confirmed; issue key: cm-000336-repair-gtdb-provenance.

The C. acetobutylicum species mapping is an exact-ID result, not a name fallback. Both claimed absent strain IDs have exact current rows. Existing species classifications and the C. ljungdahlii species fallback remain valid.

### attach-role-and-population-evidence: Attach local role evidence and distinguish population measures

minor / open / confirmed; issue key: cm-000336-attach-role-and-population-evidence.

Taxon-local gas-donor evidence does not establish C. acetobutylicum utilization of a partner metabolite. Attach provider/currency/utilization evidence or omit the optional recipient role. Contextualize PRIMARY_DEGRADER using the founding complex-carbohydrate description, and distinguish prior approximately 25% population rationale from aligned-mRNA and OD-based measures.

## Recommended Actions And Acceptance Checks

### scope-wt-description

Align the top-level description with WT, reporter and engineered evidence.

- State WT cell-wall/membrane fusion and protein-label exchange with 2020 Figures 1–2 and Figure S4 support. Identify RNA exchange as the C. acetobutylicum-Halo/WT C. ljungdahlii experiment and DNA acquisition as the 2024 plasmid-donor/selected-recipient experiment rather than unconditional WT properties.
- Retain the eight existing interaction nodes and both HYPOTHESIZED edges. Preserve the fusion node’s reporter qualifications, its exclusion of unmodified-pair DNA claims and the condition-specific product node. No extra WT DNA node, member or mechanistic arrow is required.
- Keep the 2024 publication as scoped contextual bibliography and the open knowledge-gap discussion. If updating the discussion’s historical unread-SI statement, add the current dated scope rather than erasing earlier review provenance.

### repair-cultivation

Represent the actual Type I and Type II protocols with member-specific preparation.

- Correct the Type I pH representation to record manual adjustment at 11 h to approximately 5.3. Remove the claim that absent automated apparatus proves ph_controlled:false. State the intervention and its experimental scope rather than implying continuous automated control.
- Restrict the 80°C heat-shock step to C. acetobutylicum spores. Separate its seed/exponential preculture and 17% inoculation from the C. ljungdahlii gas-fed precultures, centrifugation/resuspension and OD-based R=5 inoculum. Do not heat-shock the nonsporulating partner.
- Retain 100 mL loose screw-cap bottles, 60 mL working volume, static 37°C and venting for Type I. Replace the sealed-serum interpretation with a source-compatible system classification or leave the optional enum unset with explicit apparatus notes. Preserve 85% N2/10% CO2/5% H2 as chamber atmosphere, not a measured sealed headspace.
- Represent Type II separately: Corning 7910, 0.4 µm membrane, 4 mL per compartment/8 mL total, 34% C. acetobutylicum lower inoculum and OD-based R=5 upper inoculum. Keep the insert-removed mixed control, five separated wells pooled per plate, three plates allocated one each to 2/4/11 h sampling, and the separately reported three biological replicates and no imported Type I pH intervention.
- Distinguish C. ljungdahlii monoculture controls: 160 mL serum bottles, 90 mL glucose-free medium, 20 psig 80% H2/20% CO2 and 90 rpm. Do not imply matched shaking, vessel or gas conditions in Type I. Keep the 2020 100 nm/~1 mL reporter transwell and 2024 antibiotic selection separate.
- Retain the source-named Turbo CGM and measured 5 g/L yeast extract. Do not reconstruct the unavailable founding recipe, add catalogue conditions, transplant analytical reagents into growth medium or invent a CultureMech equivalence. Add exact source/section evidence for each changed claim.

### repair-gtdb-provenance

Correct mapping method and exact-row availability without changing species classifications.

- Update taxonomy[0].taxon_term.gtdb_classification.mapping_source to the verified exact NCBITaxon:1488 route, preserving its existing GTDB target, lineage, majority fraction 1.0 and 44-genome denominator.
- Correct taxonomy[0].taxon_term.notes and taxonomy[1].taxon_term.notes: exact strain IDs 272562 and 748727 are present with 1.0/2 and 1.0/4 mappings. Keep species-level 1538 name fallback at 1.0/4; do not falsely relabel it an exact species-ID match.
- Record the verified crosswalk snapshot/hash and method with file mtime explicitly labeled as such, not an invented release. Optional strain grounding requires a deliberate rank choice; do not silently substitute strain counts for species counts or infer experimental genome sequencing.

### attach-role-evidence

Use claim-local utilization and population evidence while preserving broad role semantics.

- For C. acetobutylicum CROSS_FEEDER, attach a source-supported partner, metabolite and utilization statement with the proper experimental uncertainty, or omit the optional assignment if unsupported. Gas production/donation alone does not support recipient status. Do not assert uptake impossible or require nutrient-growth benefit or reciprocation.
- If PRIMARY_DEGRADER is retained, link the founding abstract’s simple/complex carbohydrate potential and distinguish it from the glucose assay. Keep broad SYNTROPHIC_PARTNER roles and C. ljungdahlii PRIMARY_PRODUCER with their existing source scope; no obligacy or thermodynamic proof requirement is added.
- Keep DOMINANT/ABUNDANT when their contextual ordinal rationale is explicit. Separate the prior approximately 25% C. ljungdahlii estimate used for sequencing design, current aligned-mRNA proportions and OD-based R=5 inoculum. Do not manufacture a current fixed 75:25 cell fraction or demand arbitrary percentage thresholds.
- Preserve measured amino-acid profiles, recipient monoculture supplementation and early glucose-consumption evidence. Keep donor-resolved flux, ATP/Wood–Ljungdahl mediation, local hydrogenase relief and fusion-specific product causality qualified as proposals.

### validate-authorized-curation

Validate separately authorized curation and preserve immutable source/review history.

- Future new snippets must be verbatim and reference-specific, with exact main/SI locator and experimental scope. Extend only the relevant source cache when necessary; preserve original excerpts and actual body/header boundaries. Do not label unavailable founding text as read.
- After separately authorized canonical changes, append fresh history, run focused schema/strict/term/reference/GTDB/domain/history checks, then just gen-html and just check-docs-current. Preserve actual failed or unavailable outcomes.
- This review makes no canonical, cache, history or generated-product mutation. Only a new immutable review bundle may be saved after independent audits. Preserve initial/final native summaries, preliminary/final support, source failures and all prior provenance.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | kb/communities/Clostridium_Acetobutylicum_Ljungdahlii_Fusion_Coculture.yaml; Whole maintained YAML | supports | The WT C. acetobutylicum ATCC 824 and C. ljungdahlii DSM 13528 pair has eight interaction nodes, two hypothesized arrows, one cultivation entry, one medium, three environmental factors, four bibliographic resources and one sequencing project. The top-level summary and protocol require corrections beyond the already qualified graph. |
| founder | PMID:30391511; Fresh abstract, complete | supports | The founding study describes a deliberate coculture of a solventogen able to convert simple and complex carbohydrates and an acetogen using H2 and CO2, with emergent product formation. This supports pairing and broad substrate potential. The founding full body, original recipe and supplements were not recovered and are not treated as read. |
| identity | PMID:40298437; Abstract; RESULTS AND DISCUSSION: Experimental design: bottle and transwell experiments for Type I and II RNAseq comparisons and global summary of differential gene expression from the two comparisons; MATERIALS AND METHODS: Microorganisms and culture media | supports | The focal transcription study uses C. acetobutylicum ATCC 824 and C. ljungdahlii DSM 13528. Type I compares a mixed bottle culture with monocultures; Type II compares direct contact with membrane separation. These are distinct experimental conditions of the defined pair. SYNTHETIC origin and laboratory environment are appropriate; reporter and plasmid-bearing strains belong to separately scoped evidence. |
| type-one | PMID:40298437; RESULTS AND DISCUSSION: Experimental design: bottle and transwell experiments for Type I and II RNAseq comparisons and global summary of differential gene expression from the two comparisons; Figure 1; MATERIALS AND METHODS: Microorganisms and culture media | supports | C. acetobutylicum monocultures and cocultures use 100 mL screw-cap bottles at 60 mL working volume, static 37°C, inside an 85% N2/10% CO2/5% H2 chamber with caps loosened. Type I pH below 5 was manually adjusted at 11 h to approximately 5.3. The C. ljungdahlii monoculture instead uses 160 mL serum bottles with 90 mL glucose-free medium, 20 psig 80% H2/20% CO2 and 90 rpm. These controls are not identical vessel/gas/substrate conditions. |
| preparation | PMID:40298437; MATERIALS AND METHODS: Microorganisms and culture media | supports | The 80°C heat shock applies to C. acetobutylicum spores, not to both members. Its seed and exponential preculture precede a 17% inoculum into 60 mL. C. ljungdahlii grows through gas-fed primary/secondary precultures; an OD-based R=5 preparation is centrifuged, resuspended in 1 mL and added to the coculture. The medium is source-named complex Turbo CGM with 5 g/L yeast extract. No complete founding recipe or catalogue-medium equivalence is inferred. |
| type-two | PMID:40298437; MATERIALS AND METHODS: Transwell cultures; RESULTS AND DISCUSSION: Experimental design: bottle and transwell experiments for Type I and II RNAseq comparisons and global summary of differential gene expression from the two comparisons; Figure 1H–M | supports | Type II uses six-well Corning 7910 inserts with 0.4 µm membranes and 8 mL total, 4 mL per compartment. C. acetobutylicum is inoculated at 34% in the lower compartment and the OD-based C. ljungdahlii R=5 inoculum in the upper compartment. One insert is removed for the mixed control. Five separated wells are pooled as described for RNA preparation. Methods assigns three plates to the 2, 4 and 11 h timepoints, one per timepoint; Results and Figure 1 separately report three biological replicates. The plate/timepoint allocation is not the replicate count. Sampling at 2, 4 and 11 h differs from Type I 4, 11 and 22 h. Do not transfer the Type I 11 h pH intervention or 60 mL volume to this arm. |
| population | PMID:40298437; MATERIALS AND METHODS: RNAseq library preparation, sequencing, and data analysis; RESULTS AND DISCUSSION: Experimental design: bottle and transwell experiments for Type I and II RNAseq comparisons and global summary of differential gene expression from the two comparisons; Figure 1D and K | supports | The approximately 25% C. ljungdahlii estimate is cited from prior work as the rationale for deeper sequencing. Figure 1D/K proportions use species-aligned mRNA; the R=5 inoculum uses OD, not direct counts. These are different measures. Neither invalidates the existing ordinal designations by a fabricated numerical threshold, nor establishes a fixed current 75:25 cell ratio. |
| amino-acids | PMID:40298437; RESULTS AND DISCUSSION: Arginine, histidine, and tryptophan biosynthesis genes and metabolism; Figures 3 and 6 | supports | Supernatant amino-acid profiles and differential transcription support the proposed arginine/histidine routes. Figure 6 tests C. ljungdahlii monocultures under H2/CO2 without glucose/fructose, supplemented with arginine or histidine or both; it measures growth, acetate and ammonia with two biological replicates. Histidine raises acetate; arginine has a different net acetate outcome despite growth. The 5 g/L yeast-extract medium already contains amino acids. These are not donor-resolved transfer, isotope-traced carbon fixation, direct ATP assays or measured coculture flux. |
| hydrogen-feedback | PMID:40298437; RESULTS AND DISCUSSION: Does the differential expression of ribosomal proteins support the notion that the coculture benefits the growth of C. acetobutylicum?; Figure S3 | supports | Early glucose consumption and ribosomal transcription are measured proxies. The authors propose relief of local hydrogen inhibition, while stating that C. acetobutylicum does not receive growth substrates directly from C. ljungdahlii in this account. No local hydrogen turnover, hydrogenase activity or species-resolved reciprocal growth rate was measured. Gas donation alone does not establish the donor as a metabolite recipient; other source-supported utilization remains possible. |
| transcription | PMID:40298437; RESULTS AND DISCUSSION: Overview of genes strongly upregulated by direct interspecies contact (Type II comparisons); Cell motility genes in C. ljungdahlii and C. acetobutylicum; Key Wood-Ljungdahl pathway and autotrophic energy metabolism genes are either downregulated or unaffected in C. ljungdahlii in coculture compared to C. ljungdahlii monocultures under an H2/CO2 atmosphere | supports | Contact-associated ribosomal, pyrimidine and other transcription changes are measured. They do not directly measure growth rate, chemotaxis, inhibition or pathway flux. Type I includes a shaken-versus-static comparison; Type II reduces that confounding. Wood–Ljungdahl/Rnf/ATP-related expression is not universally upregulated; proposed alternative energy and amino-acid competition explanations remain hypotheses. |
| fusion-wt | PMID:32873766; RESULTS: Unanticipated cell fusion events between C. acetobutylicum and C. ljungdahlii.; Large-scale exchange of proteins between the two organisms.; Figures 1–3 and Figure S4 | supports | Electron microscopy and tomography support WT cell-wall/membrane fusion. Figure S4 specifically uses chemically labeled WT C. acetobutylicum and WT C. ljungdahlii to demonstrate protein-label exchange. Reporter assays provide additional evidence but should not replace this exact WT evidence. Contact separation does not selectively perturb fusion itself. |
| rna-context | PMID:32873766; RESULTS: Cell fusion leads to exchange of RNA in the syntrophic coculture.; Figures 7–8 and Figure S8 | supports | The RNA-transfer assay uses C. acetobutylicum-Halo and RNASelect-labeled WT C. ljungdahlii. Stable detected RNA is largely discussed as rRNA/tRNA, not demonstrated mRNA-specific transfer. The record’s fusion node already distinguishes this reporter context; its WT description should do the same. Figure S9 concerns dye/RNA stability rather than a new WT RNA-transfer experiment. |
| products | PMID:32873766; INTRODUCTION; RESULTS: Dynamics of coculture interactions using flow cytometry.; DISCUSSION; MATERIALS AND METHODS: Cocultures.; Cocultures in transwell plates. | supports | The founding product phenotype is described in the full 2020 source with glucose/fructose conditions and contact-separation controls. C. ljungdahlii has potential 2,3-butanediol capacity, so lack in the reported monocultures is condition-specific, not a universal species inability. The reporter transwell uses 100 nm pores and approximately 1 mL total; it is not the 2025 0.4 µm/8 mL transcriptome arm. Product emergence does not itself prove that fusion is the necessary mediator. |
| dna-context | PMID:38214507; Abstract; RESULTS: Coculture-mediated transfer of plasmid DNA from C. ljungdahlii-ptaHalo strain to WT C. acetobutylicum; Table 1; DISCUSSION | supports | DNA acquisition/integration uses an engineered p100ptaHalo-bearing C. ljungdahlii donor, WT C. acetobutylicum recipient and selected lineages. Table 1 distinguishes heat resistance and growth under selection. These findings do not establish DNA exchange in the unmodified pair. PCR/PacBio results and mixed or mosaic lineage interpretations retain their specific selection and clonality limits; fusion is the proposed route, not a selectively demonstrated DNA-transfer mechanism. |
| data-statement | PMID:40298437; DATA AVAILABILITY; MATERIALS AND METHODS: RNAseq library preparation, sequencing, and data analysis | supports | PRJNA1167669 and SAMN44010615–SAMN44010668 are directly reported for 54 RNA-seq samples. The study differentiates Type I NextSeq550 2×76 and Type II NextSeq2000 2×100 sequencing. The archive’s generic platform fields and species labels must be interpreted separately from those experimental assignments. |
| si-scope | lead-primary-read-scope.json; Supplementary reading and visual scope by source | supports | 2025: complete supporting text and three figures, with all workbook sheet names/dimensions and first four rows only. 2020: all nine captions and composites. 2024: all ten text projections, Text S1 and every Table S1/S2 cell; S2/S4/S6 pixels viewed, four other EMF figures acquired but not visually read. No full expression-table analysis or raw-data reproduction is claimed. |
| ontology | ontology-authority.json; Nineteen distinct ID-label pairs, 36 occurrences; exact definitions and locations | supports | Local OAK confirms all encoded taxon, environment, chemical and process labels. Semantic scope is separately checked: arginine/histidine and their pathway contexts are distinct from measured flux; carbon fixation and transcription terms do not prove ATP generation or growth. No forced new chemical stereochemistry or gene/UniProt annotations are required. |
| schema | child-schema-semantics.json; Literal role, interaction, ordinal abundance and experimental evidence definitions | supports | CROSS_FEEDER utilizes metabolites from other taxa; being a donor alone is insufficient, but neither reciprocal fitness nor a nutrient-growth-only test is required. Broad syntrophic roles remain compatible with source-described cooperation. Optional interaction types remain unset where the local schema does not fit fusion/material transfer. Ordinal abundance has no imposed percentage threshold. |
| culture-schema | child-schema-cultivation-slots.json; Cultivation setup, pH control, system type and gas scope | supports | Manual pH intervention cannot be represented as absent merely because no automated controller is described. Vessel/system classification must fit loose screw-cap bottles; chamber gas composition is different from measured vessel headspace. Distinct volume/control regimes must not be compressed into one inaccurate setup. |
| strain | child-strain-authority.json; Source strain aliases and direct culture-collection identity | supports | ATCC 824 and DSM 13528 aliases match the cited WT strains. Exact strain taxon candidates are available but do not compel a rank change. Catalogue medium or incubation details were not imported into the community protocol; engineered reporters/plasmid donors are separately scoped. |
| gtdb | child-gtdb-crosswalk.json; Exact species/strain rows and current fallback route | supports | NCBITaxon:1488 maps by exact ID to the existing C. acetobutylicum target at 1.0/44; 1538 uses a valid species-name fallback at 1.0/4. Exact strain rows exist for 272562 at 1.0/2 and 748727 at 1.0/4, contradicting both absence notes. Preserve species mappings/counts and distinguish optional strain denominators. |
| semantics | ontology-semantic-notes.json; Final auxiliary semantic review | supports | Nineteen pairs/36 occurrences and all eight native checks pass. Correct WT-versus-engineered scope, manual pH, heat-shock selectivity, cultivation stages and mapping provenance. Narrow role follow-up concerns local utilization evidence; no forced obligacy, nutrient-only role test or ordinal threshold is added. |
| resources | dataset-verification.json; PRJNA1167669 and all 54 public sample/run/experiment identities | supports | The encoded project is valid and supports the stated 54 BioSamples. All 54 runs are paired RNA-seq; 18 carry coculture labels and 18 each species labels, which do not alone identify all as monocultures. Archive NextSeq550 fields differ from the source’s Type II NextSeq2000 statement. No raw-read analysis or additional dataset finding is warranted. |
| snippets | snippet-source-audit.json; All 41 reference-specific excerpt occurrences | supports | All 41 strictly match fresh sources and their respective caches: 31 from the 2025 study, four founding-abstract occurrences, five from 2020 and one from 2024. This verifies text, not the biological support of surrounding explanations. The four cached metadata headers say abstract_only, while three contain appended open main text. |
| snippet-partition | snippet-partition-clarification.json; Mutually exclusive abstract, body and back-matter classification | supports | The exact partition is 15 abstract, 25 body and one DATA AVAILABILITY back-matter occurrence. The data statement is not called body evidence. The founding source contributes abstract support only. |
| history | provenance-audit.json; Four sidecars, exact focal batch 17 row, current issues 1316/1317/748/749/752 and all comments | supports | Current target and cache hashes match the prior graph review. Issue 1316 is closed after graph repair; open 1317 owns the WT-summary, manual-pH, heat-shock and control/population follow-up. Issue 748 resolved ordinal semantics; 749/752 retain upstream discussion and do not override current definitions. No new issue or comment was posted. |
| inspect | inspect.json; Fresh official inspect in owned batch 11; all 31 inputs | supports | The maintained MicrobialCommunity target, current base and exact local inputs were inspected before assessment and remain unchanged. Discovery included ignored files within the declared source/history/report scope. |
| metrics | support-final-audit.json; Final native arithmetic and accurate support read-scope erratum | supports | Completeness 100; eight nodes, two arrows and 20 node-evidence occurrences yield mean 2.5 and network COMPLETE. Two major/two minor findings give raw 111, capped 100. Support manually read whole sidecars, cache front matter and all encoded excerpt contexts, plus full-byte lexical checks; it did not independently reread the three appended full articles. This clarifies shorthand in the immutable lead read-scope. |
| support-manifest | supporting-artifact-manifest.json; Finalized distinct support and immutable supporting receipts | supports | Final support is separate from the unchanged preliminary receipt. Scientific/source, provenance, archive, snippet, native and authority receipts are pinned. Exact historical source-path resolution is separately documented without rewriting old provenance. |
| lead-read | lead-primary-read-scope.json; Lead main, figure, supplementary and authority scope | supports | Lead read the three complete scientific main texts, all 20 main figures and the declared critical SI scope. The 2020 reference list was also read; 2025/2024 reference tails are not claimed. Founding abstract/metadata were read; full founding body/recipe/SI were inaccessible. The sibling-cache shorthand is narrowed by final support. |
| source-scope | source-audit.json; Frozen four-group current-claim scientific assessment | supports | Completed current-claim review with two major and two minor findings. Keep eight nodes and two hypothesized arrows. Major corrections address the WT summary and actionable culture protocol; minor repairs address GTDB provenance and local role/population evidence. |
| root-source | root-independent-source-audit.json; Independent main-source and authority review | supports | Root read the three main texts including references and nine specifically listed visuals. Its initial completion condition depended on lead critical SI assessment, now completed and explicitly confirmed by the separate root-final-source-scope receipt. It does not claim all lead SI pixels. |
| root-final-scope | root-final-source-scope.json; Final independent acceptance after whole lead source/read-scope review | supports | Root accepted the completed critical SI assessment and final two-major/two-minor grading, 100/raw111/cap100. The original conditional receipt remains unchanged. The exact division of visual and supplementary reading is preserved. |
| auxiliary | auxiliary-frozen-manifest.json; Frozen child authority/native/semantic artifacts | supports | The child completed 19 ID-label pairs across 36 occurrences, exact GTDB and catalogue checks, schema scope and eight focused native checks. Source scientific reading remains independently owned by lead/root. |
| final-native | final-validator-summary.json; Separate final native metadata and input verification | supports | All eight focused checks pass and 31 inputs remain unchanged. Initial validator-summary bytes are preserved; final metadata is a separate receipt. |
| adapter | adapter-check.json; Same-batch 403 discovery timestamp and fresh runtime compatibility | supports | The discovery at 2026-10-21T19:20:45.556660+00:00 is explicitly reused. Fresh runtime checks still find no installed optional module/console script. No other-checkout executable was run; no unavailable adapter result is used as negative expression evidence. |
| historical-pins | historical-primary-pin-resolution.json; Three exact historical source paths resolved to byte-identical current XMLs | supports | Only the three explicitly listed historical XML pins are matched to fresh local XML bytes by SHA256. This preserves old paths and reading scopes; it is not a blanket redirect or certification of historically unread content. |
| check-validate | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-11/src just --no-dotenv validate kb/communities/Clostridium_Acetobutylicum_Ljungdahlii_Fusion_Coculture.yaml; Actual execution 2026-10-21T19:56:48.395650+00:00 to 2026-10-21T19:56:49.270187+00:00 | supports | validate passed on this record; scientific support is separately assessed. |
| check-validate-strict | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-11/src just --no-dotenv validate-strict kb/communities/Clostridium_Acetobutylicum_Ljungdahlii_Fusion_Coculture.yaml --out /private/tmp/cm-review-session/batch-11/000336/strict-report.tsv; Actual execution 2026-10-21T19:56:48.395936+00:00 to 2026-10-21T19:56:50.794746+00:00 | supports | validate-strict passed on this record; scientific support is separately assessed. |
| check-validate-terms | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-11/src just --no-dotenv validate-terms kb/communities/Clostridium_Acetobutylicum_Ljungdahlii_Fusion_Coculture.yaml; Actual execution 2026-10-21T19:56:48.396049+00:00 to 2026-10-21T19:56:50.334878+00:00 | supports | validate-terms passed on this record; scientific support is separately assessed. |
| check-validate-references-explained | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-11/src just --no-dotenv validate-references-explained kb/communities/Clostridium_Acetobutylicum_Ljungdahlii_Fusion_Coculture.yaml; Actual execution 2026-10-21T19:56:51.189377+00:00 to 2026-10-21T19:56:52.346173+00:00 | supports | validate-references-explained passed on this record; scientific support is separately assessed. |
| check-validate-gtdb | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-11/src just --no-dotenv validate-gtdb kb/communities/Clostridium_Acetobutylicum_Ljungdahlii_Fusion_Coculture.yaml; Actual execution 2026-10-21T19:56:49.270464+00:00 to 2026-10-21T19:56:49.378247+00:00 | supports | validate-gtdb passed on this record; scientific support is separately assessed. |
| check-validate-gtdb-domain | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-11/src just --no-dotenv validate-gtdb-domain kb/communities/Clostridium_Acetobutylicum_Ljungdahlii_Fusion_Coculture.yaml; Actual execution 2026-10-21T19:56:49.378492+00:00 to 2026-10-21T19:56:50.890111+00:00 | supports | validate-gtdb-domain passed on this record; scientific support is separately assessed. |
| check-validate-history | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-11/src just --no-dotenv validate-history history/records/Clostridium_Acetobutylicum_Ljungdahlii_Fusion_Coculture; Actual execution 2026-10-21T19:56:50.335229+00:00 to 2026-10-21T19:56:51.120024+00:00 | supports | validate-history passed on this record; scientific support is separately assessed. |
| check-normalize-cache-names-check | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-11/src uv run python scripts/normalize_cache_names.py --check; Actual execution 2026-10-21T19:56:51.121407+00:00 to 2026-10-21T19:56:51.189047+00:00 | supports | normalize-cache-names-check passed on this record; scientific support is separately assessed. |
| check-audit-network | PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-11/src JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv audit-network; Actual execution 2026-10-21T19:18:40.531566+00:00 to 2026-10-21T19:18:48.865608+00:00 | supports | Existing batch 11 corpus diagnostic retains its actual nonzero result; focal network separately reports COMPLETE. |
| check-check-network-quality | PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-11/src JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv check-network-quality; Actual execution 2026-10-21T19:18:40.534157+00:00 to 2026-10-21T19:18:48.224265+00:00 | supports | Existing batch 11 corpus diagnostic retains its actual nonzero result; focal network separately reports COMPLETE. |

## Limits And Additional Notes

- Completed scientific review applies to current encoded claims. The three open scientific mains and critical SI were assessed; the founding 2019 full body, original recipe and supplements remain inaccessible. Its four excerpts are independently supported by the fresh abstract, with fuller product context supplied by the 2020 source.
- Lead viewed all 20 main figures. Supplement scope: 2025 all supporting text/three figures and workbook schemas/first four rows only; 2020 all nine captions/composites; 2024 all ten text projections, Text S1 and Tables S1/S2, with S2/S4/S6 pixels. Four 2024 EMF figures and full expression data were not visually or analytically reviewed. No claim depends on unseen SI numerical results.
- Root independently read all three mains including references and nine named visuals; its final scope addendum accepts lead SI completion without claiming those additional pixels. Support read whole sidecars, cache front matter and all excerpt contexts with full-byte lexical checks, not three entire appended article bodies. Final support explicitly corrects the frozen lead shorthand.
- All 41 excerpt occurrences strictly match fresh reference-specific sources and caches: 15 abstract, 25 body and one DATA AVAILABILITY back matter. Three caches have full open text appended despite abstract_only metadata. Lexical matching alone does not validate surrounding interpretation.
- WT structural fusion and protein exchange are distinct from reporter RNA and engineered plasmid-DNA transfer. Contact dependence is not a selective fusion perturbation; no new unmodified-pair DNA or stable hybrid claim is made.
- Amino-acid concentrations, recipient supplementation, transcription and glucose consumption are measured at their stated scopes. Donor transfer, ATP production, local hydrogenase relief and species-resolved growth remain proposed. Figure 6 has two biological replicates, unlike the three-replicate transcriptome design; yeast extract supplies initial amino acids.
- Type I, Type II, 2020 reporter and 2024 selection protocols differ. Preserve manual Type I pH intervention, heat shock only for C. acetobutylicum and separately pressurized/shaken C. ljungdahlii controls. Source gas-mixture and supplementary caption inconsistencies are not silently resolved into a new protocol.
- Prior population estimates, current aligned-mRNA ratios and OD-based inocula have different denominators. GTDB genome counts are mapping support, not study population fractions. Species and optional strain mappings must not be silently interchanged.
- PRJNA1167669 is verified at metadata level without raw-read analysis. Species-labeled libraries are not automatically monocultures. The source reports different Type I/II sequencing platforms while archive fields list NextSeq550 throughout; both attributions remain explicit.
- Eight focused native checks pass; same-batch corpus diagnostics retain nonzero results. Optional adapter discovery is reused from 403 with fresh compatibility. No raw/statistical reproduction, other-checkout tool execution, paid service, author contact, issue mutation or later-record assessment occurred.
- All 31 inspected inputs remain unchanged. Initial native and preliminary support receipts are immutable; finalized summaries are separate.
- Open issue 1317 already owns the overlapping non-graph repair. Closed graph and ordinal repairs remain intact; no issue or comment was created.
- Two major and two minor findings; completeness 100, quality 100/raw111. Parent and sibling whole-candidate audits precede any save.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T200731Z-clostridial-fusion-record-review
kind: record
repository: CultureBotAI/CommunityMech
title: Clostridial fusion coculture source and protocol review
started_at: '2026-10-21T19:55:48.180220Z'
finished_at: '2026-10-21T20:07:31.209210Z'
reviewer:
  identity: codex
  kind: agent
  independence: unknown
  independence_basis: Separate agents assessed source science, native/authority checks
    and support; no person-level independence asserted.
skill: review-yaml-record
completion: completed
verdict: needs_curation
scientific_review: true
summary: Three open main papers and critical supplements support the defined WT pair,
  eight qualified interaction nodes and two hypothesized arrows. Two major findings
  correct WT-versus-engineered transfer claims and cultivation handling; two minor
  findings repair GTDB provenance and local role/population evidence. All eight focused
  native checks pass.
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
  - path: history/records/Clostridium_Acetobutylicum_Ljungdahlii_Fusion_Coculture/2026-09-08T024312Z-claude-code-e9f340.yaml
    sha256: acaa907237aa55b8d2aa5375349b9e2f6ec855a77ee363614a6711ca1d1ea585
    role: context
  - path: history/records/Clostridium_Acetobutylicum_Ljungdahlii_Fusion_Coculture/2026-09-08T031432Z-claude-code-939363.yaml
    sha256: 3f3831ecece595970e0eb764751fcde5a33f9632fd62cf0df17a53c8cd1e3257
    role: context
  - path: history/records/Clostridium_Acetobutylicum_Ljungdahlii_Fusion_Coculture/2026-09-08T070006Z-claude-code-077576.yaml
    sha256: 59f7238362f0001da263531e68ae012f574d548d147b51ece375a5aa746aa268
    role: context
  - path: history/records/Clostridium_Acetobutylicum_Ljungdahlii_Fusion_Coculture/2026-10-05T224753Z-codex-668b1f.yaml
    sha256: 9ec75a55b4f12ea4ab2b7ef387fb3b411183b30de0cbe9d51d8f971a26dffc00
    role: context
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: kb/communities/Clostridium_Acetobutylicum_Ljungdahlii_Fusion_Coculture.yaml
    sha256: 27e4e0784e4d50f0b619fb8754e1f6f3417d351e12344be9f5c8df293035b61c
    role: target
  - path: references_cache/PMID_30391511.md
    sha256: 9bba0282942015d00969122ee448139191b8c66eff65ea0adf8f23296d76313b
    role: context
  - path: references_cache/PMID_32873766.md
    sha256: 5230e98ef56284528e6348ab21fb0220b99815d73a0474c9eff7a174df9dfddf
    role: context
  - path: references_cache/PMID_38214507.md
    sha256: 00501fb2595c3df92d30b72982311d43e6ddacad5fab1fa1ae12b116fb81a0c3
    role: context
  - path: references_cache/PMID_40298437.md
    sha256: 96f235b46b00eceee141aef2615e2838aaecd09d1a26fad68bacf095da3a4882
    role: context
  - path: reports/causal_graph_review/decisions/20261005-one-record-batch17.yaml
    sha256: c611efcaf72c5f0dacab108b89401f8de23b54c354669f23e4321abaf48fdcc8
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
- target_id: CommunityMech:000336
  path: kb/communities/Clostridium_Acetobutylicum_Ljungdahlii_Fusion_Coculture.yaml
  label: Clostridium acetobutylicum-Clostridium ljungdahlii Syntrophic Fusion Coculture
  kind: maintained
  record_class: MicrobialCommunity
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Clostridium_Acetobutylicum_Ljungdahlii_Fusion_Coculture.yaml
    role: canonical_record
scope:
  description: Whole maintained record assessed against current source science, declared
    supplementary/visual coverage, literal schema/ontology authority and bounded public
    provenance/resources.
  selection: Only released CommunityMech:000336 in owned batch 11.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000336
checks:
- check_id: validate
  name: validate
  status: passed
  required: true
  summary: validate passed on this record; scientific support is separately assessed.
  target_ids:
  - CommunityMech:000336
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-11/src
    just --no-dotenv validate kb/communities/Clostridium_Acetobutylicum_Ljungdahlii_Fusion_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate
  scope_note: Focused batch 11 execution; cache matching is not biological certification.
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: validate-strict passed on this record; scientific support is separately
    assessed.
  target_ids:
  - CommunityMech:000336
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-11/src
    just --no-dotenv validate-strict kb/communities/Clostridium_Acetobutylicum_Ljungdahlii_Fusion_Coculture.yaml
    --out /private/tmp/cm-review-session/batch-11/000336/strict-report.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-strict
  scope_note: Focused batch 11 execution; cache matching is not biological certification.
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: validate-terms passed on this record; scientific support is separately
    assessed.
  target_ids:
  - CommunityMech:000336
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-11/src
    just --no-dotenv validate-terms kb/communities/Clostridium_Acetobutylicum_Ljungdahlii_Fusion_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-terms
  scope_note: Focused batch 11 execution; cache matching is not biological certification.
- check_id: validate-references-explained
  name: validate-references-explained
  status: passed
  required: true
  summary: validate-references-explained passed on this record; scientific support
    is separately assessed.
  target_ids:
  - CommunityMech:000336
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-11/src
    just --no-dotenv validate-references-explained kb/communities/Clostridium_Acetobutylicum_Ljungdahlii_Fusion_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-references-explained
  scope_note: Focused batch 11 execution; cache matching is not biological certification.
- check_id: validate-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: validate-gtdb passed on this record; scientific support is separately assessed.
  target_ids:
  - CommunityMech:000336
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-11/src
    just --no-dotenv validate-gtdb kb/communities/Clostridium_Acetobutylicum_Ljungdahlii_Fusion_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb
  scope_note: Focused batch 11 execution; cache matching is not biological certification.
- check_id: validate-gtdb-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: validate-gtdb-domain passed on this record; scientific support is separately
    assessed.
  target_ids:
  - CommunityMech:000336
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-11/src
    just --no-dotenv validate-gtdb-domain kb/communities/Clostridium_Acetobutylicum_Ljungdahlii_Fusion_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb-domain
  scope_note: Focused batch 11 execution; cache matching is not biological certification.
- check_id: validate-history
  name: validate-history
  status: passed
  required: true
  summary: validate-history passed on this record; scientific support is separately
    assessed.
  target_ids:
  - CommunityMech:000336
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-11/src
    just --no-dotenv validate-history history/records/Clostridium_Acetobutylicum_Ljungdahlii_Fusion_Coculture
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-history
  scope_note: Focused batch 11 execution; cache matching is not biological certification.
- check_id: normalize-cache-names-check
  name: normalize-cache-names-check
  status: passed
  required: true
  summary: normalize-cache-names-check passed on this record; scientific support is
    separately assessed.
  target_ids:
  - CommunityMech:000336
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-11/src
    uv run python scripts/normalize_cache_names.py --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-normalize-cache-names-check
  scope_note: Focused batch 11 execution; cache matching is not biological certification.
- check_id: audit-network
  name: audit-network
  status: failed
  required: true
  summary: Existing batch 11 corpus diagnostic retains its actual nonzero result;
    focal network separately reports COMPLETE.
  target_ids:
  - CommunityMech:000336
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-11/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv audit-network
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-audit-network
  - metrics
  scope_note: Explicit same-batch corpus reuse; unrelated records not newly assessed.
- check_id: check-network-quality
  name: check-network-quality
  status: failed
  required: true
  summary: Existing batch 11 corpus diagnostic retains its actual nonzero result;
    focal network separately reports COMPLETE.
  target_ids:
  - CommunityMech:000336
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-11/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv check-network-quality
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-check-network-quality
  - metrics
  scope_note: Explicit same-batch corpus reuse; unrelated records not newly assessed.
- check_id: scientific-source
  name: Current-claim source review
  status: passed
  required: true
  summary: Three complete scientific mains, 20 main figures and declared critical
    SI assessed; founding abstract and unread supplementary regions remain explicit.
  target_ids:
  - CommunityMech:000336
  evidence_ids:
  - lead-read
  - si-scope
  - source-scope
  - root-source
  - root-final-scope
- check_id: direct-excerpts
  name: Reference-specific excerpt verification
  status: passed
  required: true
  summary: 'All 41 strict reference-specific matches: 15 abstract, 25 body, one DATA
    AVAILABILITY back matter; all 41 cache matches.'
  target_ids:
  - CommunityMech:000336
  evidence_ids:
  - snippets
  - snippet-partition
- check_id: authority-review
  name: Ontology, schema, GTDB and strain authority
  status: passed
  required: true
  summary: Nineteen ID-label pairs/36 occurrences match; source scope, exact mapping
    routes and culture semantics assessed.
  target_ids:
  - CommunityMech:000336
  evidence_ids:
  - ontology
  - schema
  - culture-schema
  - gtdb
  - strain
- check_id: adapter
  name: Optional structured expression-source adapter
  status: unavailable
  required: false
  summary: Same-batch 403 discovery is explicitly reused with fresh runtime compatibility.
    The other-checkout executable was not used.
  target_ids:
  - CommunityMech:000336
  evidence_ids:
  - adapter
- check_id: raw-reproduction
  name: Experimental and raw-data reproduction
  status: skipped
  required: false
  summary: No new culture, raw-read processing, external code execution or statistical
    recalculation.
  target_ids:
  - CommunityMech:000336
  evidence_ids:
  - lead-read
  - resources
evidence:
- evidence_id: record
  kind: record_content
  reference: kb/communities/Clostridium_Acetobutylicum_Ljungdahlii_Fusion_Coculture.yaml
  locator: Whole maintained YAML
  summary: The WT C. acetobutylicum ATCC 824 and C. ljungdahlii DSM 13528 pair has
    eight interaction nodes, two hypothesized arrows, one cultivation entry, one medium,
    three environmental factors, four bibliographic resources and one sequencing project.
    The top-level summary and protocol require corrections beyond the already qualified
    graph.
  support: supports
  accessed_at: '2026-10-21T20:07:31.192210Z'
- evidence_id: founder
  kind: primary_source
  reference: PMID:30391511
  locator: Fresh abstract, complete
  summary: The founding study describes a deliberate coculture of a solventogen able
    to convert simple and complex carbohydrates and an acetogen using H2 and CO2,
    with emergent product formation. This supports pairing and broad substrate potential.
    The founding full body, original recipe and supplements were not recovered and
    are not treated as read.
  support: supports
  accessed_at: '2026-10-21T20:07:31.192444Z'
  snapshot_sha256: 7482124d3cc6c1b3a0580c5941013dcb4d0be1832bc1f7addcb142446b4eb4bd
- evidence_id: identity
  kind: primary_source
  reference: PMID:40298437
  locator: 'Abstract; RESULTS AND DISCUSSION: Experimental design: bottle and transwell
    experiments for Type I and II RNAseq comparisons and global summary of differential
    gene expression from the two comparisons; MATERIALS AND METHODS: Microorganisms
    and culture media'
  summary: The focal transcription study uses C. acetobutylicum ATCC 824 and C. ljungdahlii
    DSM 13528. Type I compares a mixed bottle culture with monocultures; Type II compares
    direct contact with membrane separation. These are distinct experimental conditions
    of the defined pair. SYNTHETIC origin and laboratory environment are appropriate;
    reporter and plasmid-bearing strains belong to separately scoped evidence.
  support: supports
  accessed_at: '2026-10-21T20:07:31.192774Z'
  snapshot_sha256: 673cfd527ec15c8194097ba339486d53396a8116b6b6ed87cc0f6c91b7d1ca01
- evidence_id: type-one
  kind: primary_source
  reference: PMID:40298437
  locator: 'RESULTS AND DISCUSSION: Experimental design: bottle and transwell experiments
    for Type I and II RNAseq comparisons and global summary of differential gene expression
    from the two comparisons; Figure 1; MATERIALS AND METHODS: Microorganisms and
    culture media'
  summary: C. acetobutylicum monocultures and cocultures use 100 mL screw-cap bottles
    at 60 mL working volume, static 37°C, inside an 85% N2/10% CO2/5% H2 chamber with
    caps loosened. Type I pH below 5 was manually adjusted at 11 h to approximately
    5.3. The C. ljungdahlii monoculture instead uses 160 mL serum bottles with 90
    mL glucose-free medium, 20 psig 80% H2/20% CO2 and 90 rpm. These controls are
    not identical vessel/gas/substrate conditions.
  support: supports
  accessed_at: '2026-10-21T20:07:31.193100Z'
  snapshot_sha256: 673cfd527ec15c8194097ba339486d53396a8116b6b6ed87cc0f6c91b7d1ca01
  quote: manually adjusted
- evidence_id: preparation
  kind: primary_source
  reference: PMID:40298437
  locator: 'MATERIALS AND METHODS: Microorganisms and culture media'
  summary: The 80°C heat shock applies to C. acetobutylicum spores, not to both members.
    Its seed and exponential preculture precede a 17% inoculum into 60 mL. C. ljungdahlii
    grows through gas-fed primary/secondary precultures; an OD-based R=5 preparation
    is centrifuged, resuspended in 1 mL and added to the coculture. The medium is
    source-named complex Turbo CGM with 5 g/L yeast extract. No complete founding
    recipe or catalogue-medium equivalence is inferred.
  support: supports
  accessed_at: '2026-10-21T20:07:31.193199Z'
  snapshot_sha256: 673cfd527ec15c8194097ba339486d53396a8116b6b6ed87cc0f6c91b7d1ca01
- evidence_id: type-two
  kind: primary_source
  reference: PMID:40298437
  locator: 'MATERIALS AND METHODS: Transwell cultures; RESULTS AND DISCUSSION: Experimental
    design: bottle and transwell experiments for Type I and II RNAseq comparisons
    and global summary of differential gene expression from the two comparisons; Figure
    1H–M'
  summary: Type II uses six-well Corning 7910 inserts with 0.4 µm membranes and 8
    mL total, 4 mL per compartment. C. acetobutylicum is inoculated at 34% in the
    lower compartment and the OD-based C. ljungdahlii R=5 inoculum in the upper compartment.
    One insert is removed for the mixed control. Five separated wells are pooled as
    described for RNA preparation. Methods assigns three plates to the 2, 4 and 11
    h timepoints, one per timepoint; Results and Figure 1 separately report three
    biological replicates. The plate/timepoint allocation is not the replicate count.
    Sampling at 2, 4 and 11 h differs from Type I 4, 11 and 22 h. Do not transfer
    the Type I 11 h pH intervention or 60 mL volume to this arm.
  support: supports
  accessed_at: '2026-10-21T20:07:31.193388Z'
  snapshot_sha256: 673cfd527ec15c8194097ba339486d53396a8116b6b6ed87cc0f6c91b7d1ca01
- evidence_id: population
  kind: primary_source
  reference: PMID:40298437
  locator: 'MATERIALS AND METHODS: RNAseq library preparation, sequencing, and data
    analysis; RESULTS AND DISCUSSION: Experimental design: bottle and transwell experiments
    for Type I and II RNAseq comparisons and global summary of differential gene expression
    from the two comparisons; Figure 1D and K'
  summary: The approximately 25% C. ljungdahlii estimate is cited from prior work
    as the rationale for deeper sequencing. Figure 1D/K proportions use species-aligned
    mRNA; the R=5 inoculum uses OD, not direct counts. These are different measures.
    Neither invalidates the existing ordinal designations by a fabricated numerical
    threshold, nor establishes a fixed current 75:25 cell ratio.
  support: supports
  accessed_at: '2026-10-21T20:07:31.193565Z'
  snapshot_sha256: 673cfd527ec15c8194097ba339486d53396a8116b6b6ed87cc0f6c91b7d1ca01
- evidence_id: amino-acids
  kind: primary_source
  reference: PMID:40298437
  locator: 'RESULTS AND DISCUSSION: Arginine, histidine, and tryptophan biosynthesis
    genes and metabolism; Figures 3 and 6'
  summary: Supernatant amino-acid profiles and differential transcription support
    the proposed arginine/histidine routes. Figure 6 tests C. ljungdahlii monocultures
    under H2/CO2 without glucose/fructose, supplemented with arginine or histidine
    or both; it measures growth, acetate and ammonia with two biological replicates.
    Histidine raises acetate; arginine has a different net acetate outcome despite
    growth. The 5 g/L yeast-extract medium already contains amino acids. These are
    not donor-resolved transfer, isotope-traced carbon fixation, direct ATP assays
    or measured coculture flux.
  support: supports
  accessed_at: '2026-10-21T20:07:31.193764Z'
  snapshot_sha256: 673cfd527ec15c8194097ba339486d53396a8116b6b6ed87cc0f6c91b7d1ca01
- evidence_id: hydrogen-feedback
  kind: primary_source
  reference: PMID:40298437
  locator: 'RESULTS AND DISCUSSION: Does the differential expression of ribosomal
    proteins support the notion that the coculture benefits the growth of C. acetobutylicum?;
    Figure S3'
  summary: Early glucose consumption and ribosomal transcription are measured proxies.
    The authors propose relief of local hydrogen inhibition, while stating that C.
    acetobutylicum does not receive growth substrates directly from C. ljungdahlii
    in this account. No local hydrogen turnover, hydrogenase activity or species-resolved
    reciprocal growth rate was measured. Gas donation alone does not establish the
    donor as a metabolite recipient; other source-supported utilization remains possible.
  support: supports
  accessed_at: '2026-10-21T20:07:31.193878Z'
  snapshot_sha256: 673cfd527ec15c8194097ba339486d53396a8116b6b6ed87cc0f6c91b7d1ca01
- evidence_id: transcription
  kind: primary_source
  reference: PMID:40298437
  locator: 'RESULTS AND DISCUSSION: Overview of genes strongly upregulated by direct
    interspecies contact (Type II comparisons); Cell motility genes in C. ljungdahlii
    and C. acetobutylicum; Key Wood-Ljungdahl pathway and autotrophic energy metabolism
    genes are either downregulated or unaffected in C. ljungdahlii in coculture compared
    to C. ljungdahlii monocultures under an H2/CO2 atmosphere'
  summary: Contact-associated ribosomal, pyrimidine and other transcription changes
    are measured. They do not directly measure growth rate, chemotaxis, inhibition
    or pathway flux. Type I includes a shaken-versus-static comparison; Type II reduces
    that confounding. Wood–Ljungdahl/Rnf/ATP-related expression is not universally
    upregulated; proposed alternative energy and amino-acid competition explanations
    remain hypotheses.
  support: supports
  accessed_at: '2026-10-21T20:07:31.194366Z'
  snapshot_sha256: 673cfd527ec15c8194097ba339486d53396a8116b6b6ed87cc0f6c91b7d1ca01
- evidence_id: fusion-wt
  kind: primary_source
  reference: PMID:32873766
  locator: 'RESULTS: Unanticipated cell fusion events between C. acetobutylicum and
    C. ljungdahlii.; Large-scale exchange of proteins between the two organisms.;
    Figures 1–3 and Figure S4'
  summary: Electron microscopy and tomography support WT cell-wall/membrane fusion.
    Figure S4 specifically uses chemically labeled WT C. acetobutylicum and WT C.
    ljungdahlii to demonstrate protein-label exchange. Reporter assays provide additional
    evidence but should not replace this exact WT evidence. Contact separation does
    not selectively perturb fusion itself.
  support: supports
  accessed_at: '2026-10-21T20:07:31.194542Z'
  snapshot_sha256: d7a2480f551f28dd40e766be8a53f3315def3c82da087d0a08bd74b4824caa6a
- evidence_id: rna-context
  kind: primary_source
  reference: PMID:32873766
  locator: 'RESULTS: Cell fusion leads to exchange of RNA in the syntrophic coculture.;
    Figures 7–8 and Figure S8'
  summary: The RNA-transfer assay uses C. acetobutylicum-Halo and RNASelect-labeled
    WT C. ljungdahlii. Stable detected RNA is largely discussed as rRNA/tRNA, not
    demonstrated mRNA-specific transfer. The record’s fusion node already distinguishes
    this reporter context; its WT description should do the same. Figure S9 concerns
    dye/RNA stability rather than a new WT RNA-transfer experiment.
  support: supports
  accessed_at: '2026-10-21T20:07:31.195058Z'
  snapshot_sha256: d7a2480f551f28dd40e766be8a53f3315def3c82da087d0a08bd74b4824caa6a
- evidence_id: products
  kind: primary_source
  reference: PMID:32873766
  locator: 'INTRODUCTION; RESULTS: Dynamics of coculture interactions using flow cytometry.;
    DISCUSSION; MATERIALS AND METHODS: Cocultures.; Cocultures in transwell plates.'
  summary: The founding product phenotype is described in the full 2020 source with
    glucose/fructose conditions and contact-separation controls. C. ljungdahlii has
    potential 2,3-butanediol capacity, so lack in the reported monocultures is condition-specific,
    not a universal species inability. The reporter transwell uses 100 nm pores and
    approximately 1 mL total; it is not the 2025 0.4 µm/8 mL transcriptome arm. Product
    emergence does not itself prove that fusion is the necessary mediator.
  support: supports
  accessed_at: '2026-10-21T20:07:31.195369Z'
  snapshot_sha256: d7a2480f551f28dd40e766be8a53f3315def3c82da087d0a08bd74b4824caa6a
- evidence_id: dna-context
  kind: primary_source
  reference: PMID:38214507
  locator: 'Abstract; RESULTS: Coculture-mediated transfer of plasmid DNA from C.
    ljungdahlii-ptaHalo strain to WT C. acetobutylicum; Table 1; DISCUSSION'
  summary: DNA acquisition/integration uses an engineered p100ptaHalo-bearing C. ljungdahlii
    donor, WT C. acetobutylicum recipient and selected lineages. Table 1 distinguishes
    heat resistance and growth under selection. These findings do not establish DNA
    exchange in the unmodified pair. PCR/PacBio results and mixed or mosaic lineage
    interpretations retain their specific selection and clonality limits; fusion is
    the proposed route, not a selectively demonstrated DNA-transfer mechanism.
  support: supports
  accessed_at: '2026-10-21T20:07:31.195501Z'
  snapshot_sha256: 68696172fa04c38aed633529884a2fad1c56822122912185774bf171e5b8b22b
- evidence_id: data-statement
  kind: primary_source
  reference: PMID:40298437
  locator: 'DATA AVAILABILITY; MATERIALS AND METHODS: RNAseq library preparation,
    sequencing, and data analysis'
  summary: PRJNA1167669 and SAMN44010615–SAMN44010668 are directly reported for 54
    RNA-seq samples. The study differentiates Type I NextSeq550 2×76 and Type II NextSeq2000
    2×100 sequencing. The archive’s generic platform fields and species labels must
    be interpreted separately from those experimental assignments.
  support: supports
  accessed_at: '2026-10-21T20:07:31.196065Z'
  snapshot_sha256: 673cfd527ec15c8194097ba339486d53396a8116b6b6ed87cc0f6c91b7d1ca01
- evidence_id: si-scope
  kind: validation
  reference: lead-primary-read-scope.json
  locator: Supplementary reading and visual scope by source
  summary: '2025: complete supporting text and three figures, with all workbook sheet
    names/dimensions and first four rows only. 2020: all nine captions and composites.
    2024: all ten text projections, Text S1 and every Table S1/S2 cell; S2/S4/S6 pixels
    viewed, four other EMF figures acquired but not visually read. No full expression-table
    analysis or raw-data reproduction is claimed.'
  support: supports
  accessed_at: '2026-10-21T20:07:31.196190Z'
  snapshot_sha256: 50123bfa84be6a6f26795d61fe10c5655ddaa33e5eef2382d0575a56ae543474
- evidence_id: ontology
  kind: authority
  reference: ontology-authority.json
  locator: Nineteen distinct ID-label pairs, 36 occurrences; exact definitions and
    locations
  summary: 'Local OAK confirms all encoded taxon, environment, chemical and process
    labels. Semantic scope is separately checked: arginine/histidine and their pathway
    contexts are distinct from measured flux; carbon fixation and transcription terms
    do not prove ATP generation or growth. No forced new chemical stereochemistry
    or gene/UniProt annotations are required.'
  support: supports
  accessed_at: '2026-10-21T20:07:31.196544Z'
  snapshot_sha256: f4a448e62d2ef95e917f7b2c50b364a8779c3f6fd5ca9ceb5bd082d12f157391
- evidence_id: schema
  kind: authority
  reference: child-schema-semantics.json
  locator: Literal role, interaction, ordinal abundance and experimental evidence
    definitions
  summary: CROSS_FEEDER utilizes metabolites from other taxa; being a donor alone
    is insufficient, but neither reciprocal fitness nor a nutrient-growth-only test
    is required. Broad syntrophic roles remain compatible with source-described cooperation.
    Optional interaction types remain unset where the local schema does not fit fusion/material
    transfer. Ordinal abundance has no imposed percentage threshold.
  support: supports
  accessed_at: '2026-10-21T20:07:31.196897Z'
  snapshot_sha256: 701271919a4cbd2d3a00f8ed5f6ccc62a1977bce5ddc613f2fe3860e596f2bf3
- evidence_id: culture-schema
  kind: authority
  reference: child-schema-cultivation-slots.json
  locator: Cultivation setup, pH control, system type and gas scope
  summary: Manual pH intervention cannot be represented as absent merely because no
    automated controller is described. Vessel/system classification must fit loose
    screw-cap bottles; chamber gas composition is different from measured vessel headspace.
    Distinct volume/control regimes must not be compressed into one inaccurate setup.
  support: supports
  accessed_at: '2026-10-21T20:07:31.197508Z'
  snapshot_sha256: ed5423beee77f2b9c40055183a168fe8004a42c300c1ae3456de95b9067a655d
- evidence_id: strain
  kind: authority
  reference: child-strain-authority.json
  locator: Source strain aliases and direct culture-collection identity
  summary: ATCC 824 and DSM 13528 aliases match the cited WT strains. Exact strain
    taxon candidates are available but do not compel a rank change. Catalogue medium
    or incubation details were not imported into the community protocol; engineered
    reporters/plasmid donors are separately scoped.
  support: supports
  accessed_at: '2026-10-21T20:07:31.197873Z'
  snapshot_sha256: 363df49edbcc76a930031071972d9719596c4b50a00b0cadfc7f6570d34fb5c9
- evidence_id: gtdb
  kind: authority
  reference: child-gtdb-crosswalk.json
  locator: Exact species/strain rows and current fallback route
  summary: NCBITaxon:1488 maps by exact ID to the existing C. acetobutylicum target
    at 1.0/44; 1538 uses a valid species-name fallback at 1.0/4. Exact strain rows
    exist for 272562 at 1.0/2 and 748727 at 1.0/4, contradicting both absence notes.
    Preserve species mappings/counts and distinguish optional strain denominators.
  support: supports
  accessed_at: '2026-10-21T20:07:31.198227Z'
  snapshot_sha256: ef9dfba5163be431b1a672a5cf6717955f1fdaa2919088d14424277dcc8d2b43
- evidence_id: semantics
  kind: authority
  reference: ontology-semantic-notes.json
  locator: Final auxiliary semantic review
  summary: Nineteen pairs/36 occurrences and all eight native checks pass. Correct
    WT-versus-engineered scope, manual pH, heat-shock selectivity, cultivation stages
    and mapping provenance. Narrow role follow-up concerns local utilization evidence;
    no forced obligacy, nutrient-only role test or ordinal threshold is added.
  support: supports
  accessed_at: '2026-10-21T20:07:31.198553Z'
  snapshot_sha256: 97b4696bc714e74fdbefe56e3cf97da6eed9d1584f031cf053861fc2b3336375
- evidence_id: resources
  kind: database
  reference: dataset-verification.json
  locator: PRJNA1167669 and all 54 public sample/run/experiment identities
  summary: The encoded project is valid and supports the stated 54 BioSamples. All
    54 runs are paired RNA-seq; 18 carry coculture labels and 18 each species labels,
    which do not alone identify all as monocultures. Archive NextSeq550 fields differ
    from the source’s Type II NextSeq2000 statement. No raw-read analysis or additional
    dataset finding is warranted.
  support: supports
  accessed_at: '2026-10-21T20:07:31.198894Z'
  snapshot_sha256: 8257d57ed180095d221d804fb5eeefd7552825f291c29811d6df361d428fdafb
- evidence_id: snippets
  kind: validation
  reference: snippet-source-audit.json
  locator: All 41 reference-specific excerpt occurrences
  summary: 'All 41 strictly match fresh sources and their respective caches: 31 from
    the 2025 study, four founding-abstract occurrences, five from 2020 and one from
    2024. This verifies text, not the biological support of surrounding explanations.
    The four cached metadata headers say abstract_only, while three contain appended
    open main text.'
  support: supports
  accessed_at: '2026-10-21T20:07:31.199429Z'
  snapshot_sha256: 3f9e91abd964ad16a8ebaec729b83035a19866d236a29098b6e50f80136841f7
- evidence_id: snippet-partition
  kind: validation
  reference: snippet-partition-clarification.json
  locator: Mutually exclusive abstract, body and back-matter classification
  summary: The exact partition is 15 abstract, 25 body and one DATA AVAILABILITY back-matter
    occurrence. The data statement is not called body evidence. The founding source
    contributes abstract support only.
  support: supports
  accessed_at: '2026-10-21T20:07:31.199885Z'
  snapshot_sha256: 2acc967a05b51fbc40df03780a6cedeb72e5e07b1cf2c307960b62025e361f2b
- evidence_id: history
  kind: prior_review
  reference: provenance-audit.json
  locator: Four sidecars, exact focal batch 17 row, current issues 1316/1317/748/749/752
    and all comments
  summary: Current target and cache hashes match the prior graph review. Issue 1316
    is closed after graph repair; open 1317 owns the WT-summary, manual-pH, heat-shock
    and control/population follow-up. Issue 748 resolved ordinal semantics; 749/752
    retain upstream discussion and do not override current definitions. No new issue
    or comment was posted.
  support: supports
  accessed_at: '2026-10-21T20:07:31.200238Z'
  snapshot_sha256: 4356d2f3c3c8ce560714477dc91a7fec535628d37629702e3625e649e10384c6
- evidence_id: inspect
  kind: validation
  reference: inspect.json
  locator: Fresh official inspect in owned batch 11; all 31 inputs
  summary: The maintained MicrobialCommunity target, current base and exact local
    inputs were inspected before assessment and remain unchanged. Discovery included
    ignored files within the declared source/history/report scope.
  support: supports
  accessed_at: '2026-10-21T20:07:31.200554Z'
  snapshot_sha256: 40ba9854360692f4f6114ca227a9321cee3411626eaf7521dba4b319d9544eee
- evidence_id: metrics
  kind: validation
  reference: support-final-audit.json
  locator: Final native arithmetic and accurate support read-scope erratum
  summary: Completeness 100; eight nodes, two arrows and 20 node-evidence occurrences
    yield mean 2.5 and network COMPLETE. Two major/two minor findings give raw 111,
    capped 100. Support manually read whole sidecars, cache front matter and all encoded
    excerpt contexts, plus full-byte lexical checks; it did not independently reread
    the three appended full articles. This clarifies shorthand in the immutable lead
    read-scope.
  support: supports
  accessed_at: '2026-10-21T20:07:31.200696Z'
  snapshot_sha256: a16f1301cee4f930fbede0a812761613d21ad0159a9d8148db73e5b7383dfc07
- evidence_id: support-manifest
  kind: validation
  reference: supporting-artifact-manifest.json
  locator: Finalized distinct support and immutable supporting receipts
  summary: Final support is separate from the unchanged preliminary receipt. Scientific/source,
    provenance, archive, snippet, native and authority receipts are pinned. Exact
    historical source-path resolution is separately documented without rewriting old
    provenance.
  support: supports
  accessed_at: '2026-10-21T20:07:31.200760Z'
  snapshot_sha256: 569240523af6f131f4745e3eeb3411333ebcdd4a0545f2259832745b9e0dbeaf
- evidence_id: lead-read
  kind: validation
  reference: lead-primary-read-scope.json
  locator: Lead main, figure, supplementary and authority scope
  summary: Lead read the three complete scientific main texts, all 20 main figures
    and the declared critical SI scope. The 2020 reference list was also read; 2025/2024
    reference tails are not claimed. Founding abstract/metadata were read; full founding
    body/recipe/SI were inaccessible. The sibling-cache shorthand is narrowed by final
    support.
  support: supports
  accessed_at: '2026-10-21T20:07:31.201121Z'
  snapshot_sha256: 50123bfa84be6a6f26795d61fe10c5655ddaa33e5eef2382d0575a56ae543474
- evidence_id: source-scope
  kind: validation
  reference: source-audit.json
  locator: Frozen four-group current-claim scientific assessment
  summary: Completed current-claim review with two major and two minor findings. Keep
    eight nodes and two hypothesized arrows. Major corrections address the WT summary
    and actionable culture protocol; minor repairs address GTDB provenance and local
    role/population evidence.
  support: supports
  accessed_at: '2026-10-21T20:07:31.201165Z'
  snapshot_sha256: 8b0f55c35d85aecf94c2cfa33d7b802a6889178e4feb10ebbc425ad07aa336e6
- evidence_id: root-source
  kind: validation
  reference: root-independent-source-audit.json
  locator: Independent main-source and authority review
  summary: Root read the three main texts including references and nine specifically
    listed visuals. Its initial completion condition depended on lead critical SI
    assessment, now completed and explicitly confirmed by the separate root-final-source-scope
    receipt. It does not claim all lead SI pixels.
  support: supports
  accessed_at: '2026-10-21T20:07:31.201528Z'
  snapshot_sha256: 5a12282d0f5dd13af656a50d5dc38c0fae10e5f920e6499002dcb2b809b1ec5c
- evidence_id: root-final-scope
  kind: validation
  reference: root-final-source-scope.json
  locator: Final independent acceptance after whole lead source/read-scope review
  summary: Root accepted the completed critical SI assessment and final two-major/two-minor
    grading, 100/raw111/cap100. The original conditional receipt remains unchanged.
    The exact division of visual and supplementary reading is preserved.
  support: supports
  accessed_at: '2026-10-21T20:07:31.201886Z'
  snapshot_sha256: 99b31238ce1b59751cbb0fc21eb3ab7a57e1a3205796a55747cce6f349717146
- evidence_id: auxiliary
  kind: validation
  reference: auxiliary-frozen-manifest.json
  locator: Frozen child authority/native/semantic artifacts
  summary: The child completed 19 ID-label pairs across 36 occurrences, exact GTDB
    and catalogue checks, schema scope and eight focused native checks. Source scientific
    reading remains independently owned by lead/root.
  support: supports
  accessed_at: '2026-10-21T20:07:31.202192Z'
  snapshot_sha256: 5f2df450036bb33566791319067fd8207ad130186f75d8b7ffd8c6f3f9bbd9ff
- evidence_id: final-native
  kind: validation
  reference: final-validator-summary.json
  locator: Separate final native metadata and input verification
  summary: All eight focused checks pass and 31 inputs remain unchanged. Initial validator-summary
    bytes are preserved; final metadata is a separate receipt.
  support: supports
  accessed_at: '2026-10-21T20:07:31.202541Z'
  snapshot_sha256: 776efac1d0b4b7d7f5712fbbce5aecc3e0ab33438a6aa7b7aa6df16be1b13e37
- evidence_id: adapter
  kind: validation
  reference: adapter-check.json
  locator: Same-batch 403 discovery timestamp and fresh runtime compatibility
  summary: The discovery at 2026-10-21T19:20:45.556660+00:00 is explicitly reused.
    Fresh runtime checks still find no installed optional module/console script. No
    other-checkout executable was run; no unavailable adapter result is used as negative
    expression evidence.
  support: supports
  accessed_at: '2026-10-21T20:07:31.202880Z'
  snapshot_sha256: 3b38ccc3b3dffad1b4d62013e8d84844164a41493c06d45150ad0cf9aa229073
- evidence_id: historical-pins
  kind: validation
  reference: historical-primary-pin-resolution.json
  locator: Three exact historical source paths resolved to byte-identical current
    XMLs
  summary: Only the three explicitly listed historical XML pins are matched to fresh
    local XML bytes by SHA256. This preserves old paths and reading scopes; it is
    not a blanket redirect or certification of historically unread content.
  support: supports
  accessed_at: '2026-10-21T20:07:31.203163Z'
  snapshot_sha256: f2ff695c3fb309762ce0f33649c5e16ebead2494e7af97c24b6203f03dc3bd4c
- evidence_id: check-validate
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-11/src
    just --no-dotenv validate kb/communities/Clostridium_Acetobutylicum_Ljungdahlii_Fusion_Coculture.yaml
  locator: Actual execution 2026-10-21T19:56:48.395650+00:00 to 2026-10-21T19:56:49.270187+00:00
  summary: validate passed on this record; scientific support is separately assessed.
  support: supports
  accessed_at: '2026-10-21T19:56:49.270187Z'
  snapshot_sha256: c44e2b390b3b40c8d63564dc357e3b3d57d55966648105ac41930e333383ae38
- evidence_id: check-validate-strict
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-11/src
    just --no-dotenv validate-strict kb/communities/Clostridium_Acetobutylicum_Ljungdahlii_Fusion_Coculture.yaml
    --out /private/tmp/cm-review-session/batch-11/000336/strict-report.tsv
  locator: Actual execution 2026-10-21T19:56:48.395936+00:00 to 2026-10-21T19:56:50.794746+00:00
  summary: validate-strict passed on this record; scientific support is separately
    assessed.
  support: supports
  accessed_at: '2026-10-21T19:56:50.794746Z'
  snapshot_sha256: e812c32613aa5f8cd4a5b4cccd0dd2a108c209528cd5d62d3573c7d23a6c73a9
- evidence_id: check-validate-terms
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-11/src
    just --no-dotenv validate-terms kb/communities/Clostridium_Acetobutylicum_Ljungdahlii_Fusion_Coculture.yaml
  locator: Actual execution 2026-10-21T19:56:48.396049+00:00 to 2026-10-21T19:56:50.334878+00:00
  summary: validate-terms passed on this record; scientific support is separately
    assessed.
  support: supports
  accessed_at: '2026-10-21T19:56:50.334878Z'
  snapshot_sha256: a1c2a370062a70fdb80b405bdb1a03fa8245e534479b017c2af6908f5fcda782
- evidence_id: check-validate-references-explained
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-11/src
    just --no-dotenv validate-references-explained kb/communities/Clostridium_Acetobutylicum_Ljungdahlii_Fusion_Coculture.yaml
  locator: Actual execution 2026-10-21T19:56:51.189377+00:00 to 2026-10-21T19:56:52.346173+00:00
  summary: validate-references-explained passed on this record; scientific support
    is separately assessed.
  support: supports
  accessed_at: '2026-10-21T19:56:52.346173Z'
  snapshot_sha256: 499530d80650b66f6ee2c2ddc8984f1ec39c7ad28b13b5cca9ee796bdd66a1c3
- evidence_id: check-validate-gtdb
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-11/src
    just --no-dotenv validate-gtdb kb/communities/Clostridium_Acetobutylicum_Ljungdahlii_Fusion_Coculture.yaml
  locator: Actual execution 2026-10-21T19:56:49.270464+00:00 to 2026-10-21T19:56:49.378247+00:00
  summary: validate-gtdb passed on this record; scientific support is separately assessed.
  support: supports
  accessed_at: '2026-10-21T19:56:49.378247Z'
  snapshot_sha256: a7f5f484712b3702c2382ddd0c862596565e2c554eed5d44d0a856d0576c3323
- evidence_id: check-validate-gtdb-domain
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-11/src
    just --no-dotenv validate-gtdb-domain kb/communities/Clostridium_Acetobutylicum_Ljungdahlii_Fusion_Coculture.yaml
  locator: Actual execution 2026-10-21T19:56:49.378492+00:00 to 2026-10-21T19:56:50.890111+00:00
  summary: validate-gtdb-domain passed on this record; scientific support is separately
    assessed.
  support: supports
  accessed_at: '2026-10-21T19:56:50.890111Z'
  snapshot_sha256: 10a9d371df728716dc9f2cea6f070d8d07ff249444f550767f31a9a1710ad9e3
- evidence_id: check-validate-history
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-11/src
    just --no-dotenv validate-history history/records/Clostridium_Acetobutylicum_Ljungdahlii_Fusion_Coculture
  locator: Actual execution 2026-10-21T19:56:50.335229+00:00 to 2026-10-21T19:56:51.120024+00:00
  summary: validate-history passed on this record; scientific support is separately
    assessed.
  support: supports
  accessed_at: '2026-10-21T19:56:51.120024Z'
  snapshot_sha256: 624c2dd988655f45ed05e86a2f2bd217fadcce813807a498ae4522ac36b449ce
- evidence_id: check-normalize-cache-names-check
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-11/src
    uv run python scripts/normalize_cache_names.py --check
  locator: Actual execution 2026-10-21T19:56:51.121407+00:00 to 2026-10-21T19:56:51.189047+00:00
  summary: normalize-cache-names-check passed on this record; scientific support is
    separately assessed.
  support: supports
  accessed_at: '2026-10-21T19:56:51.189047Z'
  snapshot_sha256: ec430aa2cb15c9dfc981840b0d9c9a04bf5d35c27e0b635bce47a2ad0bc147fa
- evidence_id: check-audit-network
  kind: validation
  reference: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-11/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv audit-network
  locator: Actual execution 2026-10-21T19:18:40.531566+00:00 to 2026-10-21T19:18:48.865608+00:00
  summary: Existing batch 11 corpus diagnostic retains its actual nonzero result;
    focal network separately reports COMPLETE.
  support: supports
  accessed_at: '2026-10-21T19:18:48.865608Z'
  snapshot_sha256: 5c91360a50ff296c596ef7b3fa3ca70cfa3f0423923df3104fa1aafcfcd96b61
- evidence_id: check-check-network-quality
  kind: validation
  reference: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-11/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv check-network-quality
  locator: Actual execution 2026-10-21T19:18:40.534157+00:00 to 2026-10-21T19:18:48.224265+00:00
  summary: Existing batch 11 corpus diagnostic retains its actual nonzero result;
    focal network separately reports COMPLETE.
  support: supports
  accessed_at: '2026-10-21T19:18:48.224265Z'
  snapshot_sha256: 5052a95a78eea50710110e7c8d5488631b3eb5df1705369d5ba42b9c3c0ee9f7
assessments:
- assessment_id: identity
  area: identity
  topic: WT pairing, reporter context and community scope
  outcome: concern
  summary: Keep the two WT members and synthetic laboratory scope; narrow the description.
  target_ids:
  - CommunityMech:000336
  evidence_ids:
  - identity
  - founder
  - fusion-wt
  - rna-context
  - dna-context
  - strain
  details: WT structural fusion and chemical protein-label transfer are supported.
    RNA uses a Halo reporter; DNA integration uses a plasmid-bearing donor and selected
    recipients. These engineered observations belong in scoped contextual bibliography,
    not an unconditional WT-summary claim. No extra member or WT DNA node is needed.
- assessment_id: grounding
  area: grounding
  topic: Taxon, chemical, environment and GTDB authority
  outcome: concern
  summary: All 19 labels match; repair three mapping-provenance fields without changing
    valid species targets.
  target_ids:
  - CommunityMech:000336
  evidence_ids:
  - ontology
  - gtdb
  - strain
  - schema
  details: 1488 exact-ID and 1538 name-fallback mappings reproduce the existing species
    classifications. Both strain-absence notes are false in the current crosswalk.
    Exact strain mappings use different denominators and are optional. Laboratory
    environment, encoded chemicals/processes and source aliases are appropriate at
    their qualified scopes.
- assessment_id: roles
  area: evidence
  topic: Local roles and population evidence
  outcome: concern
  summary: Attach utilization evidence for the C. acetobutylicum recipient role or
    omit that optional assignment.
  target_ids:
  - CommunityMech:000336
  evidence_ids:
  - founder
  - hydrogen-feedback
  - population
  - schema
  details: H2/CO2 donation does not itself establish C. acetobutylicum CROSS_FEEDER.
    Do not declare reciprocal uptake impossible or impose a carbon/energy-growth test.
    PRIMARY_DEGRADER can refer to founding complex-carbohydrate potential rather than
    glucose complexity. Broad syntrophic roles and C. ljungdahlii primary production
    remain valid. Keep ordinal abundance, separating prior cell-population rationale,
    current aligned-mRNA ratio and OD-based inoculum.
- assessment_id: gas-node
  area: graph
  topic: ecological_interactions[0]
  outcome: supported
  summary: Retain gas exchange and the qualified feedback arrow.
  target_ids:
  - CommunityMech:000336
  evidence_ids:
  - founder
  - identity
  - hydrogen-feedback
  details: C. acetobutylicum produces H2/CO2 used by the acetogen. The edge to proposed
    hydrogenase relief remains HYPOTHESIZED; neither net gas production nor transcription
    alone measures local turnover or causal enzyme relief.
- assessment_id: arginine-node
  area: graph
  topic: ecological_interactions[1]
  outcome: supported
  summary: Retain the qualified arginine route.
  target_ids:
  - CommunityMech:000336
  evidence_ids:
  - amino-acids
  - transcription
  details: Measured amino-acid profiles, gene expression and recipient supplementation
    support a proposed route. They do not trace donor arginine, directly measure ATP
    from deimination or establish transfer quantitatively.
- assessment_id: histidine-node
  area: graph
  topic: ecological_interactions[2]
  outcome: supported
  summary: Retain the qualified histidine/Wood–Ljungdahl explanation.
  target_ids:
  - CommunityMech:000336
  evidence_ids:
  - amino-acids
  - transcription
  details: Recipient monoculture histidine effects and transcript patterns support
    the hypothesis. Histidine-dependent acetate is not isotope-traced carbon fixation
    or direct donor-to-recipient flux.
- assessment_id: feedback-node
  area: graph
  topic: ecological_interactions[3]
  outcome: supported
  summary: Retain the untyped proposed feedback mechanism.
  target_ids:
  - CommunityMech:000336
  evidence_ids:
  - hydrogen-feedback
  - population
  details: Early glucose consumption is a measured proxy; local H2, hydrogenase activity
    and species-resolved reciprocal growth remain unmeasured. Keep the uncertainty
    and existing direction.
- assessment_id: transcription-node
  area: graph
  topic: ecological_interactions[4]
  outcome: supported
  summary: Retain measured contact-associated transcription with proposed growth benefit.
  target_ids:
  - CommunityMech:000336
  evidence_ids:
  - transcription
  - type-two
  details: Transwell separation supports contact association but does not identify
    fusion specifically or equate mRNA abundance with growth rate. Keep this community-level
    node and existing unset interaction type.
- assessment_id: competition-node
  area: graph
  topic: ecological_interactions[5]
  outcome: supported
  summary: Retain proposed competition/inhibition without promoting it to direct antagonism.
  target_ids:
  - CommunityMech:000336
  evidence_ids:
  - amino-acids
  - transcription
  details: Amino-acid depletion and transcriptional responses are compatible with
    the authors’ explanation; specific competition or inhibitory mediator perturbation
    was not performed.
- assessment_id: fusion-node
  area: graph
  topic: ecological_interactions[6]
  outcome: supported
  summary: Retain WT structural/protein evidence and reporter qualifications.
  target_ids:
  - CommunityMech:000336
  evidence_ids:
  - fusion-wt
  - rna-context
  - dna-context
  details: The node already distinguishes WT structure/protein transfer from reporter
    RNA and excludes unmodified-pair DNA claims. Contact separation is not fusion-specific.
    Keep the edge to product emergence HYPOTHESIZED.
- assessment_id: product-node
  area: graph
  topic: ecological_interactions[7]
  outcome: supported
  summary: Retain product emergence within reported culture and control conditions.
  target_ids:
  - CommunityMech:000336
  evidence_ids:
  - founder
  - products
  - identity
  details: Isopropanol and 2,3-butanediol are coculture outcomes under specified conditions.
    Avoid a universal claim that either species can never produce them, and do not
    certify fusion as the necessary cause.
- assessment_id: cultivation
  area: completeness
  topic: Type I, Type II, preculture and control protocols
  outcome: concern
  summary: Correct manual pH, species-specific heat shock, vessel class and experimental
    stage separation.
  target_ids:
  - CommunityMech:000336
  evidence_ids:
  - type-one
  - preparation
  - type-two
  - culture-schema
  details: Retain supported 37°C, anaerobiosis, 60 mL Type I volume and 5 g/L yeast
    extract. Type I pH was adjusted at 11 h; ph_controlled:false based on absent apparatus
    is wrong. Loose-cap bottles are not sealed serum bottles. Keep 8 mL Type II and
    gas-fed/shaken C. ljungdahlii monocultures separate. The chamber atmosphere is
    not a measured sealed headspace. No complete founding recipe or unverified cross-Mech
    link is invented.
- assessment_id: environment-metals
  area: evidence
  topic: Environmental factors and metal relevance
  outcome: supported
  summary: Keep laboratory/chamber/venting/separation context and current nonmetal
    scope.
  target_ids:
  - CommunityMech:000336
  evidence_ids:
  - identity
  - type-one
  - type-two
  - ontology
  details: The three environmental factors have direct support. The medium’s analytical
    or background components do not create a metal mechanism; NOT_APPLICABLE with
    empty metal lists is appropriate for this record. No plant, host or natural-community
    environment is added.
- assessment_id: resources
  area: provenance
  topic: Bibliographic resources and sequencing project
  outcome: supported
  summary: Retain four publications and verified PRJNA1167669 with assay-specific
    limits.
  target_ids:
  - CommunityMech:000336
  evidence_ids:
  - data-statement
  - resources
  - founder
  - dna-context
  details: Fifty-four archive samples/runs/experiments support the recorded project
    identity, not a claim that every species-labeled library is a monoculture. Preserve
    the source/archive sequencer discrepancy without silently normalizing metadata.
    The DNA-transfer publication remains useful contextual bibliography. No new resource
    finding or raw-data reanalysis is required.
- assessment_id: source-evidence
  area: evidence
  topic: Reference-specific evidence and source availability
  outcome: supported
  summary: All 41 excerpts strictly match their fresh sources; surrounding overclaims
    remain separately actionable.
  target_ids:
  - CommunityMech:000336
  evidence_ids:
  - snippets
  - snippet-partition
  - lead-read
  - si-scope
  - root-final-scope
  details: The exact partition is 15 abstract, 25 body and one back-matter excerpt.
    Four founding excerpts rely on its fresh abstract. The complete three open scientific
    mains and critical SI cover the current claims, despite unavailable founding body/recipe/SI
    and bounded unread SI/data regions. The stale abstract_only cache headers do not
    erase their appended full texts and do not justify a new scientific finding.
- assessment_id: provenance
  area: provenance
  topic: Historical repairs, current issue ownership and immutable scope
  outcome: supported
  summary: Preserve the qualified graph repairs and use current issue 1317 for overlapping
    non-graph work.
  target_ids:
  - CommunityMech:000336
  evidence_ids:
  - history
  - inspect
  - metrics
  - historical-pins
  details: Issue 1316 is closed; 748 resolved ordinal semantics, while 749/752 retain
    upstream discussion. Current local definitions control. Sidecars were read in
    full; supporting cache reading was front matter plus all encoded contexts and
    full-byte lexical checks, not three whole appended article rereads. No historical
    event, cache or issue was rewritten.
- assessment_id: validation
  area: schema
  topic: Focused checks and completed current-claim review
  outcome: supported
  summary: Eight focused checks pass; corpus diagnostics retain their actual nonzero
    outcomes.
  target_ids:
  - CommunityMech:000336
  evidence_ids:
  - auxiliary
  - final-native
  - inspect
  - root-final-scope
  details: Only review artifacts are written. Canonical, cache, history and generated
    products remain unchanged. Parent persistence may save the new immutable review
    bundle after independent audit. Passing native checks do not certify the WT summary
    or protocol, and the optional adapter was unavailable.
- assessment_id: metrics
  area: completeness
  topic: Native completeness and quality
  outcome: supported
  summary: Completeness 100; raw quality 111 caps at 100.
  target_ids:
  - CommunityMech:000336
  evidence_ids:
  - metrics
  metrics:
  - name: completeness
    value: 100
    unit: points
    minimum: 0
    maximum: 100
    definition: Required fields and taxon roles 50 + environment term 5 + at least
      three environmental factors 10 + at least three interaction nodes 10 + external
      resources 5 + growth media 10 + associated datasets 5 + node metabolites 5.
      These are presence bonuses, not support certification.
  - name: validation_quality
    value: 100
    unit: points
    minimum: 0
    maximum: 100
    definition: clamp(100 − 50P1 − 10P2 − 2P3 + 20min(mean node evidence/2,1) + 15
      if COMPLETE,0,100). P1=0, P2=2, P3=2, P4=0. Twenty evidence occurrences/eight
      nodes give mean 2.5 and evidence bonus 20; COMPLETE adds 15. Raw 111 caps at
      100.
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
- finding_id: scope-wild-type-summary
  issue_key: cm-000336-scope-wild-type-summary
  category: evidence
  severity: major
  native_severity: P2
  normalization_reason: This changes which biological system is claimed to show macromolecule
    transfer, a substantive source-support error in the main summary.
  rule_id: review-checklist.claim-specific-scope-and-evidence
  status: open
  certainty: confirmed
  title: Scope the WT summary to the demonstrated experimental pair
  description: The description unconditionally attributes RNA and DNA exchange to
    the WT pair. WT structural fusion and protein-label exchange are supported; RNA
    uses C. acetobutylicum-Halo, and DNA integration uses a plasmid-bearing C. ljungdahlii
    donor and selected recipients. The graph already preserves these distinctions.
  target_ids:
  - CommunityMech:000336
  field_paths:
  - description
  evidence_ids:
  - identity
  - fusion-wt
  - rna-context
  - dna-context
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Clostridium_Acetobutylicum_Ljungdahlii_Fusion_Coculture.yaml
    role: canonical_record
  ownership_note: Current open issue 1317 directly owns this non-graph scope repair.
    Preserve closed issue 1316 graph repairs; do not create a duplicate.
- finding_id: correct-cultivation-protocol
  issue_key: cm-000336-correct-cultivation-protocol
  category: evidence
  severity: major
  native_severity: P2
  normalization_reason: These errors can materially change preparation and culture
    behavior, beyond a missing optional condition.
  rule_id: review-checklist.claim-specific-scope-and-evidence
  status: open
  certainty: confirmed
  title: Correct culture conditions that change experimental handling
  description: The record infers no pH control from absent apparatus, applies heat
    shock without member restriction, calls loosened screw-cap bottles sealed serum
    bottles and compresses distinct Type II/control conditions into the Type I setup.
    The source explicitly adjusts Type I pH at 11 h and heat-shocks only C. acetobutylicum.
  target_ids:
  - CommunityMech:000336
  field_paths:
  - cultivation_setup[0].system_type
  - cultivation_setup[0].ph_controlled
  - cultivation_setup[0].controls_notes
  - cultivation_setup[0].notes
  - cultivation_setup[0].evidence
  - growth_media[0].headspace_gas
  - growth_media[0].preparation_notes
  - growth_media[0].evidence[1].explanation
  evidence_ids:
  - type-one
  - preparation
  - type-two
  - culture-schema
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Clostridium_Acetobutylicum_Ljungdahlii_Fusion_Coculture.yaml
    role: canonical_record
  ownership_note: Current issue 1317 owns pH, heat shock and control distinctions.
    Include the closely related vessel, gas and transwell staging correction in that
    follow-up.
- finding_id: repair-gtdb-provenance
  issue_key: cm-000336-repair-gtdb-provenance
  category: provenance
  severity: minor
  native_severity: P3
  normalization_reason: The identities and species mappings are correct; this is bounded
    mapping-method and explanatory provenance repair.
  rule_id: review-checklist.claim-specific-scope-and-evidence
  status: open
  certainty: confirmed
  title: Repair GTDB mapping route and stale strain-absence notes
  description: The C. acetobutylicum species mapping is an exact-ID result, not a
    name fallback. Both claimed absent strain IDs have exact current rows. Existing
    species classifications and the C. ljungdahlii species fallback remain valid.
  target_ids:
  - CommunityMech:000336
  field_paths:
  - taxonomy[0].taxon_term.gtdb_classification.mapping_source
  - taxonomy[0].taxon_term.notes
  - taxonomy[1].taxon_term.notes
  evidence_ids:
  - gtdb
  - strain
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Clostridium_Acetobutylicum_Ljungdahlii_Fusion_Coculture.yaml
    role: canonical_record
  ownership_note: Maintained taxonomy descriptors own the correction. No forced strain-rank
    substitution or new issue is prescribed.
- finding_id: attach-role-and-population-evidence
  issue_key: cm-000336-attach-role-and-population-evidence
  category: evidence
  severity: minor
  native_severity: P3
  normalization_reason: The qualified graph and broad cooperation remain supported.
    This is local evidence/interpretation repair, not proof that reciprocal uptake
    is impossible or that the ordinals are wrong.
  rule_id: review-checklist.claim-specific-scope-and-evidence
  status: open
  certainty: confirmed
  title: Attach local role evidence and distinguish population measures
  description: Taxon-local gas-donor evidence does not establish C. acetobutylicum
    utilization of a partner metabolite. Attach provider/currency/utilization evidence
    or omit the optional recipient role. Contextualize PRIMARY_DEGRADER using the
    founding complex-carbohydrate description, and distinguish prior approximately
    25% population rationale from aligned-mRNA and OD-based measures.
  target_ids:
  - CommunityMech:000336
  field_paths:
  - taxonomy[0].functional_role
  - taxonomy[0].evidence
  - taxonomy[1].evidence
  evidence_ids:
  - founder
  - hydrogen-feedback
  - population
  - schema
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Clostridium_Acetobutylicum_Ljungdahlii_Fusion_Coculture.yaml
    role: canonical_record
  ownership_note: Current 1317 overlaps population/control qualification; role evidence
    belongs to maintained taxonomy. Resolved 748 and upstream 749/752 do not impose
    new thresholds or obligacy requirements.
actions:
- action_id: scope-wt-description
  description: Align the top-level description with WT, reporter and engineered evidence.
  finding_ids:
  - scope-wild-type-summary
  target_ids:
  - CommunityMech:000336
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Clostridium_Acetobutylicum_Ljungdahlii_Fusion_Coculture.yaml
    role: canonical_record
  acceptance_checks:
  - State WT cell-wall/membrane fusion and protein-label exchange with 2020 Figures
    1–2 and Figure S4 support. Identify RNA exchange as the C. acetobutylicum-Halo/WT
    C. ljungdahlii experiment and DNA acquisition as the 2024 plasmid-donor/selected-recipient
    experiment rather than unconditional WT properties.
  - Retain the eight existing interaction nodes and both HYPOTHESIZED edges. Preserve
    the fusion node’s reporter qualifications, its exclusion of unmodified-pair DNA
    claims and the condition-specific product node. No extra WT DNA node, member or
    mechanistic arrow is required.
  - Keep the 2024 publication as scoped contextual bibliography and the open knowledge-gap
    discussion. If updating the discussion’s historical unread-SI statement, add the
    current dated scope rather than erasing earlier review provenance.
- action_id: repair-cultivation
  description: Represent the actual Type I and Type II protocols with member-specific
    preparation.
  finding_ids:
  - correct-cultivation-protocol
  target_ids:
  - CommunityMech:000336
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Clostridium_Acetobutylicum_Ljungdahlii_Fusion_Coculture.yaml
    role: canonical_record
  acceptance_checks:
  - Correct the Type I pH representation to record manual adjustment at 11 h to approximately
    5.3. Remove the claim that absent automated apparatus proves ph_controlled:false.
    State the intervention and its experimental scope rather than implying continuous
    automated control.
  - Restrict the 80°C heat-shock step to C. acetobutylicum spores. Separate its seed/exponential
    preculture and 17% inoculation from the C. ljungdahlii gas-fed precultures, centrifugation/resuspension
    and OD-based R=5 inoculum. Do not heat-shock the nonsporulating partner.
  - Retain 100 mL loose screw-cap bottles, 60 mL working volume, static 37°C and venting
    for Type I. Replace the sealed-serum interpretation with a source-compatible system
    classification or leave the optional enum unset with explicit apparatus notes.
    Preserve 85% N2/10% CO2/5% H2 as chamber atmosphere, not a measured sealed headspace.
  - 'Represent Type II separately: Corning 7910, 0.4 µm membrane, 4 mL per compartment/8
    mL total, 34% C. acetobutylicum lower inoculum and OD-based R=5 upper inoculum.
    Keep the insert-removed mixed control, five separated wells pooled per plate,
    three plates allocated one each to 2/4/11 h sampling, and the separately reported
    three biological replicates and no imported Type I pH intervention.'
  - 'Distinguish C. ljungdahlii monoculture controls: 160 mL serum bottles, 90 mL
    glucose-free medium, 20 psig 80% H2/20% CO2 and 90 rpm. Do not imply matched shaking,
    vessel or gas conditions in Type I. Keep the 2020 100 nm/~1 mL reporter transwell
    and 2024 antibiotic selection separate.'
  - Retain the source-named Turbo CGM and measured 5 g/L yeast extract. Do not reconstruct
    the unavailable founding recipe, add catalogue conditions, transplant analytical
    reagents into growth medium or invent a CultureMech equivalence. Add exact source/section
    evidence for each changed claim.
- action_id: repair-gtdb-provenance
  description: Correct mapping method and exact-row availability without changing
    species classifications.
  finding_ids:
  - repair-gtdb-provenance
  target_ids:
  - CommunityMech:000336
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Clostridium_Acetobutylicum_Ljungdahlii_Fusion_Coculture.yaml
    role: canonical_record
  acceptance_checks:
  - Update taxonomy[0].taxon_term.gtdb_classification.mapping_source to the verified
    exact NCBITaxon:1488 route, preserving its existing GTDB target, lineage, majority
    fraction 1.0 and 44-genome denominator.
  - 'Correct taxonomy[0].taxon_term.notes and taxonomy[1].taxon_term.notes: exact
    strain IDs 272562 and 748727 are present with 1.0/2 and 1.0/4 mappings. Keep species-level
    1538 name fallback at 1.0/4; do not falsely relabel it an exact species-ID match.'
  - Record the verified crosswalk snapshot/hash and method with file mtime explicitly
    labeled as such, not an invented release. Optional strain grounding requires a
    deliberate rank choice; do not silently substitute strain counts for species counts
    or infer experimental genome sequencing.
- action_id: attach-role-evidence
  description: Use claim-local utilization and population evidence while preserving
    broad role semantics.
  finding_ids:
  - attach-role-and-population-evidence
  target_ids:
  - CommunityMech:000336
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Clostridium_Acetobutylicum_Ljungdahlii_Fusion_Coculture.yaml
    role: canonical_record
  acceptance_checks:
  - For C. acetobutylicum CROSS_FEEDER, attach a source-supported partner, metabolite
    and utilization statement with the proper experimental uncertainty, or omit the
    optional assignment if unsupported. Gas production/donation alone does not support
    recipient status. Do not assert uptake impossible or require nutrient-growth benefit
    or reciprocation.
  - If PRIMARY_DEGRADER is retained, link the founding abstract’s simple/complex carbohydrate
    potential and distinguish it from the glucose assay. Keep broad SYNTROPHIC_PARTNER
    roles and C. ljungdahlii PRIMARY_PRODUCER with their existing source scope; no
    obligacy or thermodynamic proof requirement is added.
  - Keep DOMINANT/ABUNDANT when their contextual ordinal rationale is explicit. Separate
    the prior approximately 25% C. ljungdahlii estimate used for sequencing design,
    current aligned-mRNA proportions and OD-based R=5 inoculum. Do not manufacture
    a current fixed 75:25 cell fraction or demand arbitrary percentage thresholds.
  - Preserve measured amino-acid profiles, recipient monoculture supplementation and
    early glucose-consumption evidence. Keep donor-resolved flux, ATP/Wood–Ljungdahl
    mediation, local hydrogenase relief and fusion-specific product causality qualified
    as proposals.
- action_id: validate-authorized-curation
  description: Validate separately authorized curation and preserve immutable source/review
    history.
  finding_ids:
  - scope-wild-type-summary
  - correct-cultivation-protocol
  - repair-gtdb-provenance
  - attach-role-and-population-evidence
  target_ids:
  - CommunityMech:000336
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Clostridium_Acetobutylicum_Ljungdahlii_Fusion_Coculture.yaml
    role: canonical_record
  - repository: CultureBotAI/CommunityMech
    path: references_cache/PMID_40298437.md
    role: source_cache
  - repository: CultureBotAI/CommunityMech
    path: references_cache/PMID_30391511.md
    role: source_cache
  - repository: CultureBotAI/CommunityMech
    path: references_cache/PMID_32873766.md
    role: source_cache
  - repository: CultureBotAI/CommunityMech
    path: references_cache/PMID_38214507.md
    role: source_cache
  acceptance_checks:
  - Future new snippets must be verbatim and reference-specific, with exact main/SI
    locator and experimental scope. Extend only the relevant source cache when necessary;
    preserve original excerpts and actual body/header boundaries. Do not label unavailable
    founding text as read.
  - After separately authorized canonical changes, append fresh history, run focused
    schema/strict/term/reference/GTDB/domain/history checks, then just gen-html and
    just check-docs-current. Preserve actual failed or unavailable outcomes.
  - This review makes no canonical, cache, history or generated-product mutation.
    Only a new immutable review bundle may be saved after independent audits. Preserve
    initial/final native summaries, preliminary/final support, source failures and
    all prior provenance.
limitations:
- Completed scientific review applies to current encoded claims. The three open scientific
  mains and critical SI were assessed; the founding 2019 full body, original recipe
  and supplements remain inaccessible. Its four excerpts are independently supported
  by the fresh abstract, with fuller product context supplied by the 2020 source.
- 'Lead viewed all 20 main figures. Supplement scope: 2025 all supporting text/three
  figures and workbook schemas/first four rows only; 2020 all nine captions/composites;
  2024 all ten text projections, Text S1 and Tables S1/S2, with S2/S4/S6 pixels. Four
  2024 EMF figures and full expression data were not visually or analytically reviewed.
  No claim depends on unseen SI numerical results.'
- Root independently read all three mains including references and nine named visuals;
  its final scope addendum accepts lead SI completion without claiming those additional
  pixels. Support read whole sidecars, cache front matter and all excerpt contexts
  with full-byte lexical checks, not three entire appended article bodies. Final support
  explicitly corrects the frozen lead shorthand.
- 'All 41 excerpt occurrences strictly match fresh reference-specific sources and
  caches: 15 abstract, 25 body and one DATA AVAILABILITY back matter. Three caches
  have full open text appended despite abstract_only metadata. Lexical matching alone
  does not validate surrounding interpretation.'
- WT structural fusion and protein exchange are distinct from reporter RNA and engineered
  plasmid-DNA transfer. Contact dependence is not a selective fusion perturbation;
  no new unmodified-pair DNA or stable hybrid claim is made.
- Amino-acid concentrations, recipient supplementation, transcription and glucose
  consumption are measured at their stated scopes. Donor transfer, ATP production,
  local hydrogenase relief and species-resolved growth remain proposed. Figure 6 has
  two biological replicates, unlike the three-replicate transcriptome design; yeast
  extract supplies initial amino acids.
- Type I, Type II, 2020 reporter and 2024 selection protocols differ. Preserve manual
  Type I pH intervention, heat shock only for C. acetobutylicum and separately pressurized/shaken
  C. ljungdahlii controls. Source gas-mixture and supplementary caption inconsistencies
  are not silently resolved into a new protocol.
- Prior population estimates, current aligned-mRNA ratios and OD-based inocula have
  different denominators. GTDB genome counts are mapping support, not study population
  fractions. Species and optional strain mappings must not be silently interchanged.
- PRJNA1167669 is verified at metadata level without raw-read analysis. Species-labeled
  libraries are not automatically monocultures. The source reports different Type
  I/II sequencing platforms while archive fields list NextSeq550 throughout; both
  attributions remain explicit.
- Eight focused native checks pass; same-batch corpus diagnostics retain nonzero results.
  Optional adapter discovery is reused from 403 with fresh compatibility. No raw/statistical
  reproduction, other-checkout tool execution, paid service, author contact, issue
  mutation or later-record assessment occurred.
notes:
- All 31 inspected inputs remain unchanged. Initial native and preliminary support
  receipts are immutable; finalized summaries are separate.
- Open issue 1317 already owns the overlapping non-graph repair. Closed graph and
  ordinal repairs remain intact; no issue or comment was created.
- Two major and two minor findings; completeness 100, quality 100/raw111. Parent and
  sibling whole-candidate audits precede any save.
tags:
- record-review
- clostridial-coculture
- fusion
- source-scope
- batch-11
```
