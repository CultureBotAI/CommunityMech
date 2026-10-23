# Cultivated-meat contaminant SynCom record review

- Review: 20261022T022739Z-cultivated-meat-contaminant-record-review
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-22T02:19:21.721665Z
- Finished UTC: 2026-10-22T02:27:39.102130Z
- Reviewer: codex (unknown)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: false

## Summary

The fresh abstract supports the six-contaminant model, computationally predicted complementarity and reported 1018-k6 intervention outcomes. Recovered supplements improve candidate-member traceability but do not resolve the final isolates or production protocol. Two minor findings concern that traceability and GTDB provenance; no major defect is established. Eight focused checks pass. Literal completeness is 20 and capped quality is 100; source coverage remains partial.

## Scope And Provenance

Whole maintained record, fresh abstract and publication metadata, whole recovered mmc1 text, selected mmc2 regions, exact local authorities and prior context. Full main experiments and final membership remain unavailable.

Selection: Only released CommunityMech:000366 in owned batch14.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base e117e3d37c65bfad2e04af53ab34e1325d8d7f98.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000366 | kb/communities/Cultivated_Meat_Contaminant_SynCom.yaml | maintained | Cultivated Meat Contaminant SynCom |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000366 | Actual native exit 0. |
| validate-strict | passed | True | CommunityMech:000366 | Actual native exit 0. |
| validate-terms | passed | True | CommunityMech:000366 | Actual native exit 0. |
| validate-references-explained | passed | True | CommunityMech:000366 | Actual native exit 0. |
| validate-gtdb | passed | True | CommunityMech:000366 | Actual native exit 0. |
| validate-gtdb-domain | passed | True | CommunityMech:000366 | Actual native exit 0. |
| validate-history | passed | True | CommunityMech:000366 | Actual native exit 0. |
| normalize-cache-names-check | passed | True | CommunityMech:000366 | Actual native exit 0. |
| audit-network corpus context | failed | False | CommunityMech:000366 | Actual corpus exit 1 retained. |
| check-network-quality corpus context | failed | False | CommunityMech:000366 | Actual corpus exit 1 retained. |
| Optional structured source adapter | unavailable | False | CommunityMech:000366 | Unavailable in the owned runtime. |

## Scientific And Domain Assessments

### Six-contaminant model and unresolved membership

identity: supported. Targets: CommunityMech:000366.

The broad bacterial aggregate honestly represents the abstract-defined model.

Retain synthetic origin, engineered state and biotechnology scope. The six-member identity remains unresolved at strain level; seven S1 classifications and six S2 profiles are candidate leads, not grounds for silently expanding or replacing the aggregate.

### Six-Contaminant Potential Metabolic Complementarity

graph: supported. Targets: CommunityMech:000366.

Retain computationally predicted potential complementarity without a measured exchange or robustness mechanism.

Exact selector ecological_interactions[0]; name Six-Contaminant Potential Metabolic Complementarity; scope COMMUNITY_LEVEL; interaction_type absent (untyped). Actual encoded taxa: {"source": null, "target": null, "participants": []}. Canonical evidence bindings: [{"selector": "ecological_interactions[0].evidence[0].snippet", "sha256": "cb334dfe4c9243a4d902f2722cdaf704a6807fa09bf18aedfc3729b647f68492", "reference": "PMID:42425643", "supports": "SUPPORT", "evidence_source": "COMPUTATIONAL"}]. Snippet audit SHA256 31e0b246ccd1315316aee0e9a237c4711a19736f62d63f2d4381149f69fc7535. PMID:42425643 locator: Fresh MED Abstract, second sentence beginning In this study, WGS-based functional mapping clause. Retain SUPPORT / COMPUTATIONAL. WGS potential is not measured metabolite transfer, an identified donor-recipient pair or proof that complementarity causes resistance to intervention.

### 1018-k6 SynCom Antimicrobial Suppression

graph: supported. Targets: CommunityMech:000366.

Retain the reported peptide screen and long-term suppression as community-level in vitro outcomes.

Exact selector ecological_interactions[1]; name 1018-k6 SynCom Antimicrobial Suppression; scope COMMUNITY_LEVEL; interaction_type absent (untyped). Actual encoded taxa: {"source": null, "target": null, "participants": []}. Canonical evidence bindings: [{"selector": "ecological_interactions[1].evidence[0].snippet", "sha256": "1b8f901213816602c2e79b15dc471ae1ea68a76089b5b056ee7542d018be0069", "reference": "PMID:42425643", "supports": "SUPPORT", "evidence_source": "IN_VITRO"}, {"selector": "ecological_interactions[1].evidence[1].snippet", "sha256": "0a65963b56e8e89a6c7cb7dcede3d7d1a2f7b3edea76a7f2de06661f0a5a9290", "reference": "PMID:42425643", "supports": "SUPPORT", "evidence_source": "IN_VITRO"}]. Snippet audit SHA256 31e0b246ccd1315316aee0e9a237c4711a19736f62d63f2d4381149f69fc7535. PMID:42425643 locator: Fresh MED Abstract, sentence beginning Within 11 tested and following sentence beginning The long-term suppression assay. Retain both SUPPORT / IN_VITRO excerpts. The MIC is 37.5 µg/mL; the separate 14-day challenge uses 10^6 CFU/mL, with an unspecified effective long-term peptide dose. The second excerpt uses the documented superscript display conversion. Do not infer broad safety or a missing pairwise interaction.

### Zero downstream arrows

graph: supported. Targets: CommunityMech:000366.

No causal arrow is required between WGS characterization and the intervention assay.

The former workflow edge remains removed. No source or target participant is encoded in either current community-level node; species candidates do not create pairwise topology.

### Intervention, cell readouts and culture limits

scope: supported. Targets: CommunityMech:000366.

The record keeps quantitative abstract results separate from unresolved cultivation details.

Keep 1018-k6 as an intervention. FBS peptide discovery does not define the contamination medium. The existing protocol discussion remains open; indexed C2C12 and sampling leads do not supply a complete cell line, vessel, medium or dosing regimen. Cell-growth/resazurin compatibility is restricted to the tested readouts and dose.

### Ontology identity and domain mapping

grounding: supported. Targets: CommunityMech:000366.

All four encoded ID-label pairs and the Bacteria domain aggregate reproduce.

GO:0044419 and GO:0040007 remain broad context, not proof of a particular exchange or cell-size mechanism. No absent optional role or abundance value is scored as a defect. NOT_APPLICABLE metal relevance describes study scope, not a metal-free medium.

### Recovered supplementary candidate identities

completeness: concern. Targets: CommunityMech:000366.

S1/S2 provide useful leads while leaving final membership unresolved.

Record the six S2 candidates and seven-row S1 comparison without certifying a final roster. The existing abstract-limited notes are accurate; this finding concerns newly recoverable traceability.

### Release and build claims

provenance: concern. Targets: CommunityMech:000366.

The mapping core is sound; latest-release and build-date wording lacks evidence.

Record actual snapshot identity and rank route. Filesystem modification time must not be relabeled as the upstream release or build date.

### Publication and background sequence identifiers

provenance: supported. Targets: CommunityMech:000366.

Existing publication links resolve; supplementary comparator accessions are not study deposits.

No concrete focal archive accession was found within the explicitly inspected source subset. This does not establish global absence and creates no additional finding.

### Maintained record and dated decisions

ownership: supported. Targets: CommunityMech:000366.

The record owns proposed repairs; historical aggregate, intervention and rendering fixes remain preserved.

The exact batch28 focal row and both histories are retained. Closed 858/859/860 and shared 746 are context, not automatic present dispositions; no issue, cache or history is changed.

### Partial source coverage

scope: unknown. Targets: CommunityMech:000366.

Recovered supplements do not replace the inaccessible whole manuscript.

Whole abstract, mmc1 and selected workbook regions are assessed. Main Methods/results/figures, complete SI inventory, final isolate mapping and production protocol remain critical limits. No whole KO matrix, sequence analysis or raw dataset reanalysis is claimed.

### Focused validation and excerpt support

schema: supported. Targets: CommunityMech:000366.

Eight focused checks pass; corpus failures and optional adapter limits remain explicit.

Fourteen excerpt placements resolve as nine strict abstract matches, three exact display renderings and two identity fields. Native checks do not certify inaccessible experimental details.

### Two literal native scores

completeness: supported. Targets: CommunityMech:000366.

Completeness 20; raw quality 126, capped at 100.

## Findings

### member-traceability: Record supplementary member candidates without certifying the roster

minor / open / confirmed; issue key: cm-000366-member-traceability.

The honest abstract-level identity gap can now include recovered S1/S2 leads. Seven ANI rows and six functional-profile labels remain unreconciled, so this is bounded source enrichment rather than a confirmed complete roster.

### gtdb-provenance: Replace unsupported release/build wording with snapshot provenance

minor / open / confirmed; issue key: cm-000366-gtdb-provenance.

The current Bacteria aggregate matches, but latest release and built date are inferred from local filesystem metadata. Those claims need accurate provenance without changing the valid domain classification.

## Recommended Actions And Acceptance Checks

### trace-members

Enrich the open membership discussion from bounded supplementary evidence.

- Cite mmc2 S1 A1:M8 and S2 A1:A7. Preserve the six S2 labels: Ferdinandcohnia onubensis, Rossellomorea marisflavi, Pantoea soli, Staphylococcus aureus, source-spelled Staphylococcus epidermidids, and Brevibacterium casei. Compare the seven S1 rows, including extra Dermacoccus nishinomiyaensis and the two _A suffixes; do not silently reconcile them.
- Treat NCBITaxon 33889, 3098669, 189381, 1571209, 1280 and 1282 as verified source-name candidates only. Preserve current Candidatus Pantoea soli/exact synonym, local Fredinandcohnia onubensis/related synonym, and the S1 epidermidis spelling. Do not invent a study-strain mapping or automatically expand the aggregate.
- Keep the final six-isolate selection and strain designations unresolved until direct experimental mapping is available. The S1 closest-reference GCFs are not isolated study genomes; no genome_accession or study-deposit promotion is justified.
- Retain the protocol gap. FBS extraction and peptide selection belong to discovery; indexed sampling/C2C12 leads are not full production Methods. Do not assign 37.5 µg/mL as the unspecified long-term dose or restore a characterization-to-treatment causal arrow.

### repair-gtdb

Keep the valid domain core and document its actual provenance.

- Retain GTDB:d__Bacteria, lineage d__Bacteria, NCBITaxon:2, majority_fraction 1.0, support/total 1603049/1603049 and one total destination, using ncbi_rank_d rather than claiming an exact strain row.
- Record mapping snapshot SHA256 761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd. Distinguish observed filesystem mtime from an upstream release/build date; leave unknown release/build metadata unknown.

### validate-future-curation

Validate any separately authorized repair.

- Recheck exact source/field scope, ontology names and graph references. Run focused schema, strict, terms, explained-reference, GTDB/domain and history gates, then just gen-html and just check-docs-current after authorized record changes.
- Preserve all original sources, failed routes, native receipts and historical decisions. This review changes only its proposed review bundle and does not authorize canonical/cache/history edits, paid research, contact, Git mutation or issue closure.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | kb/communities/Cultivated_Meat_Contaminant_SynCom.yaml; Whole maintained YAML | supports | An explicitly unresolved bacterial aggregate represents six cultivated-meat contaminants. Two untyped community-level nodes describe predicted complementarity and peptide suppression; there are no arrows. |
| abstract-claims | PMID:42425643; DOI:10.1016/j.fm.2026.105164; Fresh MED Abstract, second sentence beginning In this study; subsequent assembly, screen, long-term suppression and cell-compatibility sentences | supports | The abstract supports six-contaminant assembly and predicted WGS functional complementarity. It reports an 11-agent screen, 1018-k6 MIC of 37.5 µg/mL, and complete inhibition for 14 days at a 10^6 CFU/mL challenge. Cell-growth and resazurin results concern the tested effective dose; that long-term dose is not specified as the MIC. |
| publication | PMID:42425643; DOI:10.1016/j.fm.2026.105164; Fresh MED identity fields; publisher coredata and Crossref identity | supports | PMID, DOI, title and PII agree. Fresh MED supplies no PMCID and reports no PMC/EPMC full text. The retrieved publisher API response contains coredata, not manuscript Methods. |
| supplement-methods | PMID:42425643; DOI:10.1016/j.fm.2026.105164; Recovered mmc1 DOCX, Supplementary methods S1.1–S1.4, entire text | supports | This supplement describes FBS peptide extraction, mass spectrometry, sequence identification and prediction-based selection of eight peptides from 478 candidates. This discovery stage does not identify the SynCom culture medium or contradict the separately described animal-component-free application. |
| supplement-members | PMID:42425643; DOI:10.1016/j.fm.2026.105164; Recovered mmc2 XLSX, S1 A1:M8; S2 A1:A7 and B1:F1 | supports | S1 contains seven ANI classifications and closest-reference genomes. S2 has six functional-profile row labels, omitting Dermacoccus nishinomiyaensis. S1 also uses two GTDB _A suffixes, and S2 misspells epidermidis as epidermidids. These tables improve candidate traceability but do not resolve the final six isolates or study strain designations. |
| supplement-proteins | PMID:42425643; DOI:10.1016/j.fm.2026.105164; Recovered mmc2 XLSX, entire S4 A1:C9; S3 header and dimensions only | supports | S4 links eight selected FBS peptides to parent protein accessions. These are background protein identities, not microbial interaction genes or study deposits. Only the S3 header and inventory were inspected; its full 478-row peptide table and the S2 KO matrix were not reanalysed. |
| indexed-preview | https://www.sciencedirect.com/science/article/abs/pii/S0740002026001280; Focal indexed publisher result only; direct publisher requests returned challenge responses | supports | Sampling, ANI and C2C12 mentions are limited discovery leads. Truncated sections do not establish a complete final roster, medium or production protocol. |
| selected-scope | /private/tmp/cm-review-session/batch-14/000366/supplement-selected-scope.json; Exact bounded workbook selection | supports | Whole S1 and S4, six S2 row labels and five feature headers, and S3 inventory are preserved. The generated full workbook projection is not claimed as a whole human read. |
| candidates | /private/tmp/cm-review-session/batch-14/000366/child-supplementary-taxonomy-candidates.json; Six S2 names against current local NCBI authority | supports | Candidate names resolve with explicit synonym and spelling boundaries. Candidatus Pantoea soli is an exact synonym match; local Fredinandcohnia onubensis is linked by a related synonym. These are source-name candidates, not confirmed study strains. |
| ontology | /private/tmp/cm-review-session/batch-14/000366/ontology-authority.json; Four ID-label pairs, definitions and four placements | supports | Bacteria, laboratory environment and both GO labels match. Broad process annotations provide context, not proof of pairwise exchange or a particular cell-growth mechanism. |
| schema | /private/tmp/cm-review-session/batch-14/000366/child-schema-semantics.json; Literal roles, scope, origin, state and evidence definitions | supports | Synthetic origin and engineered state fit the model. Absent optional roles and member-level abundance do not require fabrication. Computational potential remains distinct from measured interspecies transfer. |
| gtdb | /private/tmp/cm-review-session/batch-14/000366/child-gtdb-crosswalk.json; Bacteria rank-aware aggregation and snapshot provenance | supports | The ncbi_rank_d route reproduces GTDB:d__Bacteria with 1,603,049 of 1,603,049 reference genomes and one destination. Snapshot mtime does not establish a latest release or build date. |
| semantics | /private/tmp/cm-review-session/batch-14/000366/ontology-semantic-notes.json; Final child semantic assessment | supports | The aggregate, intervention and two untyped nodes remain appropriate. The supplement candidate roster and GTDB provenance warrant bounded enrichment, without mandatory member expansion. |
| resources | /private/tmp/cm-review-session/batch-14/000366/dataset-verification.json; Publication identities and bounded source-resource review | supports | Existing PubMed/DOI resources match. S1 GCF identifiers are closest-reference genomes, and S4 protein IDs are background FBS-parent identities. No concrete focal archive is identified in the inspected material; no global absence or missing-deposit finding follows. |
| snippets | /private/tmp/cm-review-session/batch-14/000366/snippet-audit.json; All 14 canonical excerpt placements | supports | Nine placements match the fresh abstract strictly, three match its explicitly documented superscript rendering, and two match PMID/DOI identity fields. All 14 match the committed cache. Matching does not broaden scientific scope. |
| rendering | /private/tmp/cm-review-session/batch-14/000366/snippet-rendering-projection.json; Single 10-superscript-6 to caret rendering and its three affected placements | supports | The exact display transformation is documented without changing the source or cache. It is not an unsupported biological statement or a native reference failure. |
| provenance | /private/tmp/cm-review-session/batch-14/000366/provenance-audit.json; Both histories, exact batch28 records[0], cohort context and current issues | supports | The prior abstract-only review and closed 858/859/860 fixes remain dated context. They explain the aggregate, intervention and rendering choices; this review does not close shared issues or rewrite history. |
| inspection | /private/tmp/cm-review-session/batch-14/000366/inspect.json; 31 immutable official inputs | supports | The target, 21 authorities and nine focal contexts are pinned. Ignored-inclusive discovery found the source cache, two histories, exact prior decision/adversarial pair and four cohort files. |
| assets | /private/tmp/cm-review-session/batch-14/000366/lead-source-assets.json; Bounded public routes and recovered assets | supports | Fresh abstract, publisher coredata, indexed preview and two coherent public supplements were recovered. Main Methods/results/figures and a complete supplement inventory remain unavailable in these routes. All failed routes are preserved. |
| lead-read | /private/tmp/cm-review-session/batch-14/000366/lead-primary-read-scope.json; Actual lead reading boundaries | supports | Whole target, abstract, cache, mmc1 text and selected workbook regions were read. No full main, full KO matrix, raw genome or statistical reanalysis is claimed. |
| source-scope | /private/tmp/cm-review-session/batch-14/000366/source-audit.json; Final partial scientific assessment | supports | Available evidence positively supports current claims. Two minor findings address bounded member traceability and GTDB provenance; critical whole-source gaps keep scientific completion false. |
| root-source | /private/tmp/cm-review-session/batch-14/000366/root-independent-source-audit.json; Independent root source and selected-workbook assessment | supports | Root independently agrees with partial access, two minor findings and the preserved abstract-level claims. Its exact reading boundaries are explicit. |
| metrics | /private/tmp/cm-review-session/batch-14/000366/support-final-audit.json; Distinct final support and literal metrics | supports | Completeness is 20. Quality base 130 minus four points for two P3 findings gives raw 126, capped at 100. Neither score certifies full source review. |
| support-manifest | /private/tmp/cm-review-session/batch-14/000366/supporting-artifact-manifest.json; Frozen final supporting receipts | supports | Final support follows source and authority reconciliation. Preliminary receipts and failed retrievals remain unchanged. |
| auxiliary | /private/tmp/cm-review-session/batch-14/000366/auxiliary-frozen-manifest.json; Final native and authority manifest | supports | Eight focused native checks pass; all four ontology pairs match, and all 31 inspected inputs remain unchanged. |
| final-native | /private/tmp/cm-review-session/batch-14/000366/final-validator-summary.json; Eight actual command/stdout/stderr receipts | supports | Focused checks pass with zero reported reference issues. Independent excerpt checks and source entailment remain separate. |
| corpus-context | /private/tmp/cm-review-session/batch-14/000366/child-current-corpus-context.json; Actual fresh batch14 corpus baseline | supports | Both corpus commands exited 1 with 44 warnings across 16 of 477 records and zero errors. These contextual results are not attributed entirely to this record. |
| adapter | /private/tmp/cm-review-session/batch-14/000366/adapter-check.json; Owned-runtime optional adapter availability | supports | The optional adapter is unavailable in the owned runtime. Its earlier filename-search boundary is explicitly dated; no external-checkout adapter was executed. |
| check-validate | /private/tmp/cm-review-session/batch-14/000366/validate.json; Actual command/stdout/stderr | supports | The native command passed; biological entailment is assessed separately. |
| check-validate-strict | /private/tmp/cm-review-session/batch-14/000366/validate-strict.json; Actual command/stdout/stderr | supports | The native command passed; biological entailment is assessed separately. |
| check-validate-terms | /private/tmp/cm-review-session/batch-14/000366/validate-terms.json; Actual command/stdout/stderr | supports | The native command passed; biological entailment is assessed separately. |
| check-validate-references-explained | /private/tmp/cm-review-session/batch-14/000366/validate-references-explained.json; Actual command/stdout/stderr | supports | The native command passed; biological entailment is assessed separately. |
| check-validate-gtdb | /private/tmp/cm-review-session/batch-14/000366/validate-gtdb.json; Actual command/stdout/stderr | supports | The native command passed; biological entailment is assessed separately. |
| check-validate-gtdb-domain | /private/tmp/cm-review-session/batch-14/000366/validate-gtdb-domain.json; Actual command/stdout/stderr | supports | The native command passed; biological entailment is assessed separately. |
| check-validate-history | /private/tmp/cm-review-session/batch-14/000366/validate-history.json; Actual command/stdout/stderr | supports | The native command passed; biological entailment is assessed separately. |
| check-normalize-cache-names-check | /private/tmp/cm-review-session/batch-14/000366/normalize-cache-names-check.json; Actual command/stdout/stderr | supports | The native command passed; biological entailment is assessed separately. |
| context-audit-network | /private/tmp/cm-review-session/batch-14/audit-network.json; Fresh batch14 corpus baseline | supports | Actual exit 1; 44 warnings across 16 of 477 records and zero errors. |
| context-check-network-quality | /private/tmp/cm-review-session/batch-14/check-network-quality.json; Fresh batch14 corpus baseline | supports | Actual exit 1; 44 warnings across 16 of 477 records and zero errors. |

## Limits And Additional Notes

- Bounded ordinary public routes did not recover the whole main Methods/results/figures or a complete supplement inventory. This is not a global claim that no full text exists.
- Indexed publisher sections remain discovery leads. Exact final isolate/strain mapping, culture medium, vessel, inoculation, dosing and host-cell experimental details are not established by those truncated sections.
- S1 seven classifications and S2 six labels remain distinct. Only S1/S4 were read wholly; S2 row labels/five feature headers and S3 inventory were inspected, without whole-matrix, sequence or statistical reanalysis.
- Fresh excerpt support includes three explicit superscript renderings and two identity-field projections; these are distinguished from strict abstract and cache matches.
- Two node assessments bind all three canonical excerpt SHA256 values, their exact selectors and retained tiers. Both nodes have no encoded source/target/participants and no downstream arrows.
- The sole quotation is two words from the fresh MED Abstract second sentence. Other source text is paraphrased or referenced by exact canonical selector/hash.
- All 31 inspected inputs remain unchanged. Candidate validation and parent-owned saving/post-save gates occur after this scientific and support assessment; none is asserted in advance.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T022739Z-cultivated-meat-contaminant-record-review
kind: record
repository: CultureBotAI/CommunityMech
title: Cultivated-meat contaminant SynCom record review
started_at: '2026-10-22T02:19:21.721665Z'
finished_at: '2026-10-22T02:27:39.102130Z'
reviewer:
  identity: codex
  kind: agent
  independence: unknown
  independence_basis: Separate lead, root, auxiliary authority and supporting reviewers;
    no person-level independence claim.
skill: review-yaml-record
completion: partial
verdict: pass_with_limitations
scientific_review: false
summary: The fresh abstract supports the six-contaminant model, computationally predicted
  complementarity and reported 1018-k6 intervention outcomes. Recovered supplements
  improve candidate-member traceability but do not resolve the final isolates or production
  protocol. Two minor findings concern that traceability and GTDB provenance; no major
  defect is established. Eight focused checks pass. Literal completeness is 20 and
  capped quality is 100; source coverage remains partial.
source:
  git_revision: e117e3d37c65bfad2e04af53ab34e1325d8d7f98
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
  - path: history/records/Cultivated_Meat_Contaminant_SynCom/2026-09-13T193351Z-codex-424256.yaml
    sha256: cb1fc9b4f14b2271ee59173558abab533f92d6081afa9fb8acd37b09b4ebe1a6
    role: context
  - path: history/records/Cultivated_Meat_Contaminant_SynCom/2026-10-02T054552Z-codex-c7c366.yaml
    sha256: 01e3ae4e7ef9ee7e639aab3641fc6cdd49ff9586eb8d360875c5fa1b6a699cce
    role: context
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: kb/communities/Cultivated_Meat_Contaminant_SynCom.yaml
    sha256: 432da24bbdadb8fb88ea3c7aec46d75743748ef94449b645a1a199bd651d047e
    role: target
  - path: references_cache/PMID_42425643.txt
    sha256: 1d3994fb0b3aa1aedcb2af4effbf3d512a8f810140fec73dddedf5c98383b26f
    role: context
  - path: reports/causal_graph_review/adversarial-review-20261006-batch28.yaml
    sha256: 73b5f403e73107baf98d379cdc613b947a72382fddd9faf765b784cb63b98913
    role: context
  - path: reports/causal_graph_review/decisions/20261006-four-records-batch28.yaml
    sha256: b6c1f9081c2d4a75c3db896187e3e20dffac6d339c7ad455c03e07719c17a29f
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
- target_id: CommunityMech:000366
  path: kb/communities/Cultivated_Meat_Contaminant_SynCom.yaml
  label: Cultivated Meat Contaminant SynCom
  kind: maintained
  record_class: MicrobialCommunity
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Cultivated_Meat_Contaminant_SynCom.yaml
    role: canonical_record
scope:
  description: Whole maintained record, fresh abstract and publication metadata, whole
    recovered mmc1 text, selected mmc2 regions, exact local authorities and prior
    context. Full main experiments and final membership remain unavailable.
  selection: Only released CommunityMech:000366 in owned batch14.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000366
checks:
- check_id: validate
  name: validate
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000366
  command: just --no-dotenv validate kb/communities/Cultivated_Meat_Contaminant_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate
  scope_note: Focused record/history command; cache-name preflight is corpus-wide.
    Inputs remain unchanged.
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000366
  command: just --no-dotenv validate-strict kb/communities/Cultivated_Meat_Contaminant_SynCom.yaml
    --out /private/tmp/cm-review-session/batch-14/000366/strict-report.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-strict
  scope_note: Focused record/history command; cache-name preflight is corpus-wide.
    Inputs remain unchanged.
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000366
  command: just --no-dotenv validate-terms kb/communities/Cultivated_Meat_Contaminant_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-terms
  scope_note: Focused record/history command; cache-name preflight is corpus-wide.
    Inputs remain unchanged.
- check_id: validate-references-explained
  name: validate-references-explained
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000366
  command: just --no-dotenv validate-references-explained kb/communities/Cultivated_Meat_Contaminant_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-references-explained
  scope_note: Focused record/history command; cache-name preflight is corpus-wide.
    Inputs remain unchanged.
- check_id: validate-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000366
  command: just --no-dotenv validate-gtdb kb/communities/Cultivated_Meat_Contaminant_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb
  scope_note: Focused record/history command; cache-name preflight is corpus-wide.
    Inputs remain unchanged.
- check_id: validate-gtdb-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000366
  command: just --no-dotenv validate-gtdb-domain kb/communities/Cultivated_Meat_Contaminant_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb-domain
  scope_note: Focused record/history command; cache-name preflight is corpus-wide.
    Inputs remain unchanged.
- check_id: validate-history
  name: validate-history
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000366
  command: just --no-dotenv validate-history history/records/Cultivated_Meat_Contaminant_SynCom
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-history
  scope_note: Focused record/history command; cache-name preflight is corpus-wide.
    Inputs remain unchanged.
- check_id: normalize-cache-names-check
  name: normalize-cache-names-check
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000366
  command: uv run python scripts/normalize_cache_names.py --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-normalize-cache-names-check
  scope_note: Focused record/history command; cache-name preflight is corpus-wide.
    Inputs remain unchanged.
- check_id: context-audit-network
  name: audit-network corpus context
  status: failed
  required: false
  summary: Actual corpus exit 1 retained.
  target_ids:
  - CommunityMech:000366
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-14/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv audit-network
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - context-audit-network
  - corpus-context
  scope_note: Nonrequired corpus context, separate from focused passes.
- check_id: context-check-network-quality
  name: check-network-quality corpus context
  status: failed
  required: false
  summary: Actual corpus exit 1 retained.
  target_ids:
  - CommunityMech:000366
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-14/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv check-network-quality
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - context-check-network-quality
  - corpus-context
  scope_note: Nonrequired corpus context, separate from focused passes.
- check_id: optional-structured-adapter
  name: Optional structured source adapter
  status: unavailable
  required: false
  summary: Unavailable in the owned runtime.
  target_ids:
  - CommunityMech:000366
  evidence_ids:
  - adapter
  scope_note: No external-checkout adapter executed.
evidence:
- evidence_id: record
  kind: record_content
  reference: kb/communities/Cultivated_Meat_Contaminant_SynCom.yaml
  locator: Whole maintained YAML
  summary: An explicitly unresolved bacterial aggregate represents six cultivated-meat
    contaminants. Two untyped community-level nodes describe predicted complementarity
    and peptide suppression; there are no arrows.
  support: supports
  accessed_at: '2026-10-22T02:27:39.096717Z'
- evidence_id: abstract-claims
  kind: primary_source
  reference: PMID:42425643; DOI:10.1016/j.fm.2026.105164
  locator: Fresh MED Abstract, second sentence beginning In this study; subsequent
    assembly, screen, long-term suppression and cell-compatibility sentences
  summary: The abstract supports six-contaminant assembly and predicted WGS functional
    complementarity. It reports an 11-agent screen, 1018-k6 MIC of 37.5 µg/mL, and
    complete inhibition for 14 days at a 10^6 CFU/mL challenge. Cell-growth and resazurin
    results concern the tested effective dose; that long-term dose is not specified
    as the MIC.
  support: supports
  accessed_at: '2026-10-22T02:27:39.096800Z'
  snapshot_sha256: 8e7aebfd2eae9e43efb9678398e0e9cffc1b6946f5403fe70756e9a74a6b9bb8
  quote: metabolic complementarity
- evidence_id: publication
  kind: database
  reference: PMID:42425643; DOI:10.1016/j.fm.2026.105164
  locator: Fresh MED identity fields; publisher coredata and Crossref identity
  summary: PMID, DOI, title and PII agree. Fresh MED supplies no PMCID and reports
    no PMC/EPMC full text. The retrieved publisher API response contains coredata,
    not manuscript Methods.
  support: supports
  accessed_at: '2026-10-22T02:27:39.096939Z'
  snapshot_sha256: 8e7aebfd2eae9e43efb9678398e0e9cffc1b6946f5403fe70756e9a74a6b9bb8
- evidence_id: supplement-methods
  kind: primary_source
  reference: PMID:42425643; DOI:10.1016/j.fm.2026.105164
  locator: Recovered mmc1 DOCX, Supplementary methods S1.1–S1.4, entire text
  summary: This supplement describes FBS peptide extraction, mass spectrometry, sequence
    identification and prediction-based selection of eight peptides from 478 candidates.
    This discovery stage does not identify the SynCom culture medium or contradict
    the separately described animal-component-free application.
  support: supports
  accessed_at: '2026-10-22T02:27:39.096975Z'
  snapshot_sha256: ff2364e1e95b75dab59da4d33200589b191c192b41c8cc5b3e29679df488c5a1
- evidence_id: supplement-members
  kind: primary_source
  reference: PMID:42425643; DOI:10.1016/j.fm.2026.105164
  locator: Recovered mmc2 XLSX, S1 A1:M8; S2 A1:A7 and B1:F1
  summary: S1 contains seven ANI classifications and closest-reference genomes. S2
    has six functional-profile row labels, omitting Dermacoccus nishinomiyaensis.
    S1 also uses two GTDB _A suffixes, and S2 misspells epidermidis as epidermidids.
    These tables improve candidate traceability but do not resolve the final six isolates
    or study strain designations.
  support: supports
  accessed_at: '2026-10-22T02:27:39.097123Z'
  snapshot_sha256: cb01a6dffc50e573e9ef6a38add433b4527d984cfd49f35dd7ceb2ff63dc27bd
- evidence_id: supplement-proteins
  kind: primary_source
  reference: PMID:42425643; DOI:10.1016/j.fm.2026.105164
  locator: Recovered mmc2 XLSX, entire S4 A1:C9; S3 header and dimensions only
  summary: S4 links eight selected FBS peptides to parent protein accessions. These
    are background protein identities, not microbial interaction genes or study deposits.
    Only the S3 header and inventory were inspected; its full 478-row peptide table
    and the S2 KO matrix were not reanalysed.
  support: supports
  accessed_at: '2026-10-22T02:27:39.097363Z'
  snapshot_sha256: cb01a6dffc50e573e9ef6a38add433b4527d984cfd49f35dd7ceb2ff63dc27bd
- evidence_id: indexed-preview
  kind: search
  reference: https://www.sciencedirect.com/science/article/abs/pii/S0740002026001280
  locator: Focal indexed publisher result only; direct publisher requests returned
    challenge responses
  summary: Sampling, ANI and C2C12 mentions are limited discovery leads. Truncated
    sections do not establish a complete final roster, medium or production protocol.
  support: supports
  accessed_at: '2026-10-22T02:27:39.097445Z'
  snapshot_sha256: adeff56bb8531e1bb7d19e70573c1aae4e1469fb22814f17058120c1eecabd4c
  search_scope: Bounded exact PMID, DOI, title and PII searches; only the focal publisher
    result was read, excluding unrelated hits. Direct article/abstract/PDF and API
    routes, Crossref, OpenAlex and the author publication listing were checked. Search-returned
    prose is not direct full-text access; local source discovery separately included
    ignored files. No author contact, paid service or global absence assertion.
- evidence_id: selected-scope
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000366/supplement-selected-scope.json
  locator: Exact bounded workbook selection
  summary: Whole S1 and S4, six S2 row labels and five feature headers, and S3 inventory
    are preserved. The generated full workbook projection is not claimed as a whole
    human read.
  support: supports
  accessed_at: '2026-10-22T02:27:39.097595Z'
  snapshot_sha256: bad923349555caf75309bd6ed08ef29f55c33858dc0b912a652e86dc4588bc9f
- evidence_id: candidates
  kind: authority
  reference: /private/tmp/cm-review-session/batch-14/000366/child-supplementary-taxonomy-candidates.json
  locator: Six S2 names against current local NCBI authority
  summary: Candidate names resolve with explicit synonym and spelling boundaries.
    Candidatus Pantoea soli is an exact synonym match; local Fredinandcohnia onubensis
    is linked by a related synonym. These are source-name candidates, not confirmed
    study strains.
  support: supports
  accessed_at: '2026-10-22T02:27:39.097726Z'
  snapshot_sha256: 05a7b1242df8c1d25c656e872b174adeec10ea3c59975c01f743221c40c77561
- evidence_id: ontology
  kind: authority
  reference: /private/tmp/cm-review-session/batch-14/000366/ontology-authority.json
  locator: Four ID-label pairs, definitions and four placements
  summary: Bacteria, laboratory environment and both GO labels match. Broad process
    annotations provide context, not proof of pairwise exchange or a particular cell-growth
    mechanism.
  support: supports
  accessed_at: '2026-10-22T02:27:39.097879Z'
  snapshot_sha256: 72727eeeb307aeb5c172e2e687b790e0c12abe07b65776878846ac278832f244
- evidence_id: schema
  kind: authority
  reference: /private/tmp/cm-review-session/batch-14/000366/child-schema-semantics.json
  locator: Literal roles, scope, origin, state and evidence definitions
  summary: Synthetic origin and engineered state fit the model. Absent optional roles
    and member-level abundance do not require fabrication. Computational potential
    remains distinct from measured interspecies transfer.
  support: supports
  accessed_at: '2026-10-22T02:27:39.098020Z'
  snapshot_sha256: 739c8224a875bac7353415414b3c5921d5c6fdb9018be8dffc395e96afdaf5b4
- evidence_id: gtdb
  kind: authority
  reference: /private/tmp/cm-review-session/batch-14/000366/child-gtdb-crosswalk.json
  locator: Bacteria rank-aware aggregation and snapshot provenance
  summary: The ncbi_rank_d route reproduces GTDB:d__Bacteria with 1,603,049 of 1,603,049
    reference genomes and one destination. Snapshot mtime does not establish a latest
    release or build date.
  support: supports
  accessed_at: '2026-10-22T02:27:39.098155Z'
  snapshot_sha256: 985c7b5dc4dc544b72fe54694f994efa45359005cc8f5c3f17b41c73c9bb3fe1
- evidence_id: semantics
  kind: authority
  reference: /private/tmp/cm-review-session/batch-14/000366/ontology-semantic-notes.json
  locator: Final child semantic assessment
  summary: The aggregate, intervention and two untyped nodes remain appropriate. The
    supplement candidate roster and GTDB provenance warrant bounded enrichment, without
    mandatory member expansion.
  support: supports
  accessed_at: '2026-10-22T02:27:39.098281Z'
  snapshot_sha256: b917f43830d0ceebec19fef585d373294b07e39cec1bb3762268bd1d499cb367
- evidence_id: resources
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000366/dataset-verification.json
  locator: Publication identities and bounded source-resource review
  summary: Existing PubMed/DOI resources match. S1 GCF identifiers are closest-reference
    genomes, and S4 protein IDs are background FBS-parent identities. No concrete
    focal archive is identified in the inspected material; no global absence or missing-deposit
    finding follows.
  support: supports
  accessed_at: '2026-10-22T02:27:39.098427Z'
  snapshot_sha256: 5fa27390e723ec3335c0ea12844920856e99075c851a0da9727a1357e5077bf7
- evidence_id: snippets
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000366/snippet-audit.json
  locator: All 14 canonical excerpt placements
  summary: Nine placements match the fresh abstract strictly, three match its explicitly
    documented superscript rendering, and two match PMID/DOI identity fields. All
    14 match the committed cache. Matching does not broaden scientific scope.
  support: supports
  accessed_at: '2026-10-22T02:27:39.098568Z'
  snapshot_sha256: 31e0b246ccd1315316aee0e9a237c4711a19736f62d63f2d4381149f69fc7535
- evidence_id: rendering
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000366/snippet-rendering-projection.json
  locator: Single 10-superscript-6 to caret rendering and its three affected placements
  summary: The exact display transformation is documented without changing the source
    or cache. It is not an unsupported biological statement or a native reference
    failure.
  support: supports
  accessed_at: '2026-10-22T02:27:39.098706Z'
  snapshot_sha256: 0c4399071ee28ec518207a194f9beaacb03f8559f10da2ec9f532f80f7307d9a
- evidence_id: provenance
  kind: prior_review
  reference: /private/tmp/cm-review-session/batch-14/000366/provenance-audit.json
  locator: Both histories, exact batch28 records[0], cohort context and current issues
  summary: The prior abstract-only review and closed 858/859/860 fixes remain dated
    context. They explain the aggregate, intervention and rendering choices; this
    review does not close shared issues or rewrite history.
  support: supports
  accessed_at: '2026-10-22T02:27:39.098795Z'
  snapshot_sha256: 1d44a978b51f13a065b76d229595b75a117407479e0f2b3579f7514d7ad01c97
- evidence_id: inspection
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000366/inspect.json
  locator: 31 immutable official inputs
  summary: The target, 21 authorities and nine focal contexts are pinned. Ignored-inclusive
    discovery found the source cache, two histories, exact prior decision/adversarial
    pair and four cohort files.
  support: supports
  accessed_at: '2026-10-22T02:27:39.098925Z'
  snapshot_sha256: 7fbf95d906ac0adf330daed2c10a1ab8af5e863ad8445e9b40bd2d0b41635867
- evidence_id: assets
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000366/lead-source-assets.json
  locator: Bounded public routes and recovered assets
  summary: Fresh abstract, publisher coredata, indexed preview and two coherent public
    supplements were recovered. Main Methods/results/figures and a complete supplement
    inventory remain unavailable in these routes. All failed routes are preserved.
  support: supports
  accessed_at: '2026-10-22T02:27:39.098955Z'
  snapshot_sha256: b307b2fb092ef855e33a8868e520fae389a7f2745c9a3e7a0d08bdc580c0b095
- evidence_id: lead-read
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000366/lead-primary-read-scope.json
  locator: Actual lead reading boundaries
  summary: Whole target, abstract, cache, mmc1 text and selected workbook regions
    were read. No full main, full KO matrix, raw genome or statistical reanalysis
    is claimed.
  support: supports
  accessed_at: '2026-10-22T02:27:39.099101Z'
  snapshot_sha256: 4d72251c0bfc01a94b2288ec0c2470977585d0b069fc4d9083213b663955a9fd
- evidence_id: source-scope
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000366/source-audit.json
  locator: Final partial scientific assessment
  summary: Available evidence positively supports current claims. Two minor findings
    address bounded member traceability and GTDB provenance; critical whole-source
    gaps keep scientific completion false.
  support: supports
  accessed_at: '2026-10-22T02:27:39.099234Z'
  snapshot_sha256: f5a42286f89e93481550c511cee8110e79d72fdf72676cae5b311d2f70ee334c
- evidence_id: root-source
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000366/root-independent-source-audit.json
  locator: Independent root source and selected-workbook assessment
  summary: Root independently agrees with partial access, two minor findings and the
    preserved abstract-level claims. Its exact reading boundaries are explicit.
  support: supports
  accessed_at: '2026-10-22T02:27:39.099328Z'
  snapshot_sha256: 8460d6e33d1cdbf801d6162348fd326f761241d46d505198dee428c4f7af769d
- evidence_id: metrics
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000366/support-final-audit.json
  locator: Distinct final support and literal metrics
  summary: Completeness is 20. Quality base 130 minus four points for two P3 findings
    gives raw 126, capped at 100. Neither score certifies full source review.
  support: supports
  accessed_at: '2026-10-22T02:27:39.099467Z'
  snapshot_sha256: 8c2ae49d59dc97ff0dc98eec97d4b27757b10d99f25709fbb51fe45bf6c8a57f
- evidence_id: support-manifest
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000366/supporting-artifact-manifest.json
  locator: Frozen final supporting receipts
  summary: Final support follows source and authority reconciliation. Preliminary
    receipts and failed retrievals remain unchanged.
  support: supports
  accessed_at: '2026-10-22T02:27:39.099504Z'
  snapshot_sha256: 6cefc9c86f9c68bd80959382bb1addaa7d782cea1732a8f2304faf6f0ac56452
- evidence_id: auxiliary
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000366/auxiliary-frozen-manifest.json
  locator: Final native and authority manifest
  summary: Eight focused native checks pass; all four ontology pairs match, and all
    31 inspected inputs remain unchanged.
  support: supports
  accessed_at: '2026-10-22T02:27:39.099541Z'
  snapshot_sha256: ee3d3176fc620f6de5a17f0d76d4466543d0b6387f0b8c0e643fba1460df5437
- evidence_id: final-native
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000366/final-validator-summary.json
  locator: Eight actual command/stdout/stderr receipts
  summary: Focused checks pass with zero reported reference issues. Independent excerpt
    checks and source entailment remain separate.
  support: supports
  accessed_at: '2026-10-22T02:27:39.099688Z'
  snapshot_sha256: 2d3601331605d9ef5484448db80b3b64c3fe32da86339dbfd88bcd2a9dc41677
- evidence_id: corpus-context
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000366/child-current-corpus-context.json
  locator: Actual fresh batch14 corpus baseline
  summary: Both corpus commands exited 1 with 44 warnings across 16 of 477 records
    and zero errors. These contextual results are not attributed entirely to this
    record.
  support: supports
  accessed_at: '2026-10-22T02:27:39.099811Z'
  snapshot_sha256: bd59cb593b05640789b76f19f42fbeb1fc1afb54103539fa06bf924027c72cca
- evidence_id: adapter
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000366/adapter-check.json
  locator: Owned-runtime optional adapter availability
  summary: The optional adapter is unavailable in the owned runtime. Its earlier filename-search
    boundary is explicitly dated; no external-checkout adapter was executed.
  support: supports
  accessed_at: '2026-10-22T02:27:39.099942Z'
  snapshot_sha256: a7e3cdf7c543d163c62d5826759a7a1c1726aa5a32c233c64fd6dd1f60f9e4bf
- evidence_id: check-validate
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000366/validate.json
  locator: Actual command/stdout/stderr
  summary: The native command passed; biological entailment is assessed separately.
  support: supports
  accessed_at: '2026-10-22T02:27:39.100365Z'
  snapshot_sha256: 2598d1112b344421a096942eddb28d93fd98c1682528310298705f2f7ce064a1
- evidence_id: check-validate-strict
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000366/validate-strict.json
  locator: Actual command/stdout/stderr
  summary: The native command passed; biological entailment is assessed separately.
  support: supports
  accessed_at: '2026-10-22T02:27:39.100554Z'
  snapshot_sha256: 5c9647a321b412ee0c4f0a59c897a19f45d79d1ffdb711c85530e760b0aa7d1c
- evidence_id: check-validate-terms
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000366/validate-terms.json
  locator: Actual command/stdout/stderr
  summary: The native command passed; biological entailment is assessed separately.
  support: supports
  accessed_at: '2026-10-22T02:27:39.100750Z'
  snapshot_sha256: 5b913dc5dfc8e298d7320e71dab67d8ccc2b7be9016492c3ea5e2649d37f73f1
- evidence_id: check-validate-references-explained
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000366/validate-references-explained.json
  locator: Actual command/stdout/stderr
  summary: The native command passed; biological entailment is assessed separately.
  support: supports
  accessed_at: '2026-10-22T02:27:39.100919Z'
  snapshot_sha256: c6ce1b21595a30a5f7aba72867e7086012f4faf20b55d4357215d71a3e75c005
- evidence_id: check-validate-gtdb
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000366/validate-gtdb.json
  locator: Actual command/stdout/stderr
  summary: The native command passed; biological entailment is assessed separately.
  support: supports
  accessed_at: '2026-10-22T02:27:39.101049Z'
  snapshot_sha256: 8a3decc2f4366929ee173bc5de9a41aeb2bc1d5a33312d9185a29ab2c809dbc6
- evidence_id: check-validate-gtdb-domain
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000366/validate-gtdb-domain.json
  locator: Actual command/stdout/stderr
  summary: The native command passed; biological entailment is assessed separately.
  support: supports
  accessed_at: '2026-10-22T02:27:39.101221Z'
  snapshot_sha256: 2e33ce424abd8a1c94e8c432156741adefad41918a41e7c647227fd4c772680e
- evidence_id: check-validate-history
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000366/validate-history.json
  locator: Actual command/stdout/stderr
  summary: The native command passed; biological entailment is assessed separately.
  support: supports
  accessed_at: '2026-10-22T02:27:39.101384Z'
  snapshot_sha256: 2277b2af62ba30b2b1689b327fdc2aaf0aed4459700053f5f38ebc94f40b0fe1
- evidence_id: check-normalize-cache-names-check
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000366/normalize-cache-names-check.json
  locator: Actual command/stdout/stderr
  summary: The native command passed; biological entailment is assessed separately.
  support: supports
  accessed_at: '2026-10-22T02:27:39.101499Z'
  snapshot_sha256: bcc33a287503b01b35aaaba18d7be2c5133730059e1250e0a09a3f67ffcbfd84
- evidence_id: context-audit-network
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/audit-network.json
  locator: Fresh batch14 corpus baseline
  summary: Actual exit 1; 44 warnings across 16 of 477 records and zero errors.
  support: supports
  accessed_at: '2026-10-22T02:27:39.101927Z'
  snapshot_sha256: 3110e0bb1dbe3ea63b81aea82871ac4adb2915c8fce1d15249422d0f5db266c6
- evidence_id: context-check-network-quality
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/check-network-quality.json
  locator: Fresh batch14 corpus baseline
  summary: Actual exit 1; 44 warnings across 16 of 477 records and zero errors.
  support: supports
  accessed_at: '2026-10-22T02:27:39.102096Z'
  snapshot_sha256: 18896ef4136601b37550cb5612abc06784abcbf982e4778cbf2b9c10368cb66a
assessments:
- assessment_id: identity
  area: identity
  topic: Six-contaminant model and unresolved membership
  outcome: supported
  summary: The broad bacterial aggregate honestly represents the abstract-defined
    model.
  target_ids:
  - CommunityMech:000366
  evidence_ids:
  - record
  - abstract-claims
  - schema
  - supplement-members
  dimensions:
  - name: taxon_scope
    value: NCBITaxon:2 / Bacteria aggregate
    definition: Six source-reported contaminants; exact final isolate mapping unresolved.
    evidence_ids:
    - record
    - abstract-claims
  - name: experimental_setting
    value: Laboratory cultivated-meat contamination model
    definition: Assembled SynCom and exogenous peptide intervention, not a natural
      community.
    evidence_ids:
    - record
    - abstract-claims
  details: Retain synthetic origin, engineered state and biotechnology scope. The
    six-member identity remains unresolved at strain level; seven S1 classifications
    and six S2 profiles are candidate leads, not grounds for silently expanding or
    replacing the aggregate.
- assessment_id: node-0
  area: graph
  topic: Six-Contaminant Potential Metabolic Complementarity
  outcome: supported
  summary: Retain computationally predicted potential complementarity without a measured
    exchange or robustness mechanism.
  target_ids:
  - CommunityMech:000366
  evidence_ids:
  - abstract-claims
  - snippets
  - rendering
  - schema
  details: 'Exact selector ecological_interactions[0]; name Six-Contaminant Potential
    Metabolic Complementarity; scope COMMUNITY_LEVEL; interaction_type absent (untyped).
    Actual encoded taxa: {"source": null, "target": null, "participants": []}. Canonical
    evidence bindings: [{"selector": "ecological_interactions[0].evidence[0].snippet",
    "sha256": "cb334dfe4c9243a4d902f2722cdaf704a6807fa09bf18aedfc3729b647f68492",
    "reference": "PMID:42425643", "supports": "SUPPORT", "evidence_source": "COMPUTATIONAL"}].
    Snippet audit SHA256 31e0b246ccd1315316aee0e9a237c4711a19736f62d63f2d4381149f69fc7535.
    PMID:42425643 locator: Fresh MED Abstract, second sentence beginning In this study,
    WGS-based functional mapping clause. Retain SUPPORT / COMPUTATIONAL. WGS potential
    is not measured metabolite transfer, an identified donor-recipient pair or proof
    that complementarity causes resistance to intervention.'
- assessment_id: node-1
  area: graph
  topic: 1018-k6 SynCom Antimicrobial Suppression
  outcome: supported
  summary: Retain the reported peptide screen and long-term suppression as community-level
    in vitro outcomes.
  target_ids:
  - CommunityMech:000366
  evidence_ids:
  - abstract-claims
  - snippets
  - rendering
  - schema
  details: 'Exact selector ecological_interactions[1]; name 1018-k6 SynCom Antimicrobial
    Suppression; scope COMMUNITY_LEVEL; interaction_type absent (untyped). Actual
    encoded taxa: {"source": null, "target": null, "participants": []}. Canonical
    evidence bindings: [{"selector": "ecological_interactions[1].evidence[0].snippet",
    "sha256": "1b8f901213816602c2e79b15dc471ae1ea68a76089b5b056ee7542d018be0069",
    "reference": "PMID:42425643", "supports": "SUPPORT", "evidence_source": "IN_VITRO"},
    {"selector": "ecological_interactions[1].evidence[1].snippet", "sha256": "0a65963b56e8e89a6c7cb7dcede3d7d1a2f7b3edea76a7f2de06661f0a5a9290",
    "reference": "PMID:42425643", "supports": "SUPPORT", "evidence_source": "IN_VITRO"}].
    Snippet audit SHA256 31e0b246ccd1315316aee0e9a237c4711a19736f62d63f2d4381149f69fc7535.
    PMID:42425643 locator: Fresh MED Abstract, sentence beginning Within 11 tested
    and following sentence beginning The long-term suppression assay. Retain both
    SUPPORT / IN_VITRO excerpts. The MIC is 37.5 µg/mL; the separate 14-day challenge
    uses 10^6 CFU/mL, with an unspecified effective long-term peptide dose. The second
    excerpt uses the documented superscript display conversion. Do not infer broad
    safety or a missing pairwise interaction.'
- assessment_id: graph-boundary
  area: graph
  topic: Zero downstream arrows
  outcome: supported
  summary: No causal arrow is required between WGS characterization and the intervention
    assay.
  target_ids:
  - CommunityMech:000366
  evidence_ids:
  - record
  - abstract-claims
  - provenance
  details: The former workflow edge remains removed. No source or target participant
    is encoded in either current community-level node; species candidates do not create
    pairwise topology.
- assessment_id: culture
  area: scope
  topic: Intervention, cell readouts and culture limits
  outcome: supported
  summary: The record keeps quantitative abstract results separate from unresolved
    cultivation details.
  target_ids:
  - CommunityMech:000366
  evidence_ids:
  - abstract-claims
  - supplement-methods
  - assets
  details: Keep 1018-k6 as an intervention. FBS peptide discovery does not define
    the contamination medium. The existing protocol discussion remains open; indexed
    C2C12 and sampling leads do not supply a complete cell line, vessel, medium or
    dosing regimen. Cell-growth/resazurin compatibility is restricted to the tested
    readouts and dose.
- assessment_id: grounding
  area: grounding
  topic: Ontology identity and domain mapping
  outcome: supported
  summary: All four encoded ID-label pairs and the Bacteria domain aggregate reproduce.
  target_ids:
  - CommunityMech:000366
  evidence_ids:
  - ontology
  - gtdb
  - schema
  details: GO:0044419 and GO:0040007 remain broad context, not proof of a particular
    exchange or cell-size mechanism. No absent optional role or abundance value is
    scored as a defect. NOT_APPLICABLE metal relevance describes study scope, not
    a metal-free medium.
- assessment_id: member-traceability
  area: completeness
  topic: Recovered supplementary candidate identities
  outcome: concern
  summary: S1/S2 provide useful leads while leaving final membership unresolved.
  target_ids:
  - CommunityMech:000366
  evidence_ids:
  - supplement-members
  - selected-scope
  - candidates
  details: Record the six S2 candidates and seven-row S1 comparison without certifying
    a final roster. The existing abstract-limited notes are accurate; this finding
    concerns newly recoverable traceability.
- assessment_id: gtdb-provenance
  area: provenance
  topic: Release and build claims
  outcome: concern
  summary: The mapping core is sound; latest-release and build-date wording lacks
    evidence.
  target_ids:
  - CommunityMech:000366
  evidence_ids:
  - gtdb
  - semantics
  details: Record actual snapshot identity and rank route. Filesystem modification
    time must not be relabeled as the upstream release or build date.
- assessment_id: resources
  area: provenance
  topic: Publication and background sequence identifiers
  outcome: supported
  summary: Existing publication links resolve; supplementary comparator accessions
    are not study deposits.
  target_ids:
  - CommunityMech:000366
  evidence_ids:
  - publication
  - resources
  - supplement-proteins
  details: No concrete focal archive accession was found within the explicitly inspected
    source subset. This does not establish global absence and creates no additional
    finding.
- assessment_id: prior
  area: ownership
  topic: Maintained record and dated decisions
  outcome: supported
  summary: The record owns proposed repairs; historical aggregate, intervention and
    rendering fixes remain preserved.
  target_ids:
  - CommunityMech:000366
  evidence_ids:
  - inspection
  - provenance
  details: The exact batch28 focal row and both histories are retained. Closed 858/859/860
    and shared 746 are context, not automatic present dispositions; no issue, cache
    or history is changed.
- assessment_id: access
  area: scope
  topic: Partial source coverage
  outcome: unknown
  summary: Recovered supplements do not replace the inaccessible whole manuscript.
  target_ids:
  - CommunityMech:000366
  evidence_ids:
  - assets
  - lead-read
  - source-scope
  - root-source
  - indexed-preview
  details: Whole abstract, mmc1 and selected workbook regions are assessed. Main Methods/results/figures,
    complete SI inventory, final isolate mapping and production protocol remain critical
    limits. No whole KO matrix, sequence analysis or raw dataset reanalysis is claimed.
- assessment_id: native
  area: schema
  topic: Focused validation and excerpt support
  outcome: supported
  summary: Eight focused checks pass; corpus failures and optional adapter limits
    remain explicit.
  target_ids:
  - CommunityMech:000366
  evidence_ids:
  - final-native
  - auxiliary
  - snippets
  - rendering
  - corpus-context
  - adapter
  details: Fourteen excerpt placements resolve as nine strict abstract matches, three
    exact display renderings and two identity fields. Native checks do not certify
    inaccessible experimental details.
- assessment_id: metrics
  area: completeness
  topic: Two literal native scores
  outcome: supported
  summary: Completeness 20; raw quality 126, capped at 100.
  target_ids:
  - CommunityMech:000366
  evidence_ids:
  - metrics
  metrics:
  - name: completeness
    value: 20
    unit: points
    minimum: 0
    maximum: 100
    definition: Required fields/roles block 0 + environment 5 + three environmental
      factors 10 + external resources 5. Two nodes fall below the three-node threshold;
      absent medium/datasets/metabolites score 0. Optional absent roles are not a
      biological defect.
  - name: validation_quality
    value: 100
    unit: points
    minimum: 0
    maximum: 100
    definition: 100 - 0 major*10 - 2 minor*2 + 20*min((3 evidence/2 nodes)/2,1) +
      15 COMPLETE = 126 raw, capped 100. Two untyped nodes, zero arrows; capped quality
      is not scientific completion.
  - name: P1
    value: 0
    unit: findings
    definition: Native severity count.
  - name: P2
    value: 0
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
- finding_id: member-traceability
  issue_key: cm-000366-member-traceability
  category: completeness
  severity: minor
  native_severity: P3
  normalization_reason: Bounded provenance or traceability enrichment; existing abstract-level
    claims and community identity remain supported.
  rule_id: review-checklist.claim-specific-support-and-context
  status: open
  certainty: confirmed
  title: Record supplementary member candidates without certifying the roster
  description: The honest abstract-level identity gap can now include recovered S1/S2
    leads. Seven ANI rows and six functional-profile labels remain unreconciled, so
    this is bounded source enrichment rather than a confirmed complete roster.
  target_ids:
  - CommunityMech:000366
  field_paths:
  - taxonomy[0].taxon_term.notes
  - discussions[0]
  evidence_ids:
  - supplement-members
  - selected-scope
  - candidates
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Cultivated_Meat_Contaminant_SynCom.yaml
    role: canonical_record
  ownership_note: The maintained focal record owns future curation. No historical/shared
    issue is closed or superseded by this bounded finding.
- finding_id: gtdb-provenance
  issue_key: cm-000366-gtdb-provenance
  category: provenance
  severity: minor
  native_severity: P3
  normalization_reason: Bounded provenance or traceability enrichment; existing abstract-level
    claims and community identity remain supported.
  rule_id: review-checklist.claim-specific-support-and-context
  status: open
  certainty: confirmed
  title: Replace unsupported release/build wording with snapshot provenance
  description: The current Bacteria aggregate matches, but latest release and built
    date are inferred from local filesystem metadata. Those claims need accurate provenance
    without changing the valid domain classification.
  target_ids:
  - CommunityMech:000366
  field_paths:
  - taxonomy[0].taxon_term.gtdb_classification.mapping_source
  evidence_ids:
  - gtdb
  - semantics
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Cultivated_Meat_Contaminant_SynCom.yaml
    role: canonical_record
  ownership_note: The maintained focal record owns future curation. No historical/shared
    issue is closed or superseded by this bounded finding.
actions:
- action_id: trace-members
  description: Enrich the open membership discussion from bounded supplementary evidence.
  finding_ids:
  - member-traceability
  target_ids:
  - CommunityMech:000366
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Cultivated_Meat_Contaminant_SynCom.yaml
    role: canonical_record
  acceptance_checks:
  - 'Cite mmc2 S1 A1:M8 and S2 A1:A7. Preserve the six S2 labels: Ferdinandcohnia
    onubensis, Rossellomorea marisflavi, Pantoea soli, Staphylococcus aureus, source-spelled
    Staphylococcus epidermidids, and Brevibacterium casei. Compare the seven S1 rows,
    including extra Dermacoccus nishinomiyaensis and the two _A suffixes; do not silently
    reconcile them.'
  - Treat NCBITaxon 33889, 3098669, 189381, 1571209, 1280 and 1282 as verified source-name
    candidates only. Preserve current Candidatus Pantoea soli/exact synonym, local
    Fredinandcohnia onubensis/related synonym, and the S1 epidermidis spelling. Do
    not invent a study-strain mapping or automatically expand the aggregate.
  - Keep the final six-isolate selection and strain designations unresolved until
    direct experimental mapping is available. The S1 closest-reference GCFs are not
    isolated study genomes; no genome_accession or study-deposit promotion is justified.
  - Retain the protocol gap. FBS extraction and peptide selection belong to discovery;
    indexed sampling/C2C12 leads are not full production Methods. Do not assign 37.5
    µg/mL as the unspecified long-term dose or restore a characterization-to-treatment
    causal arrow.
- action_id: repair-gtdb
  description: Keep the valid domain core and document its actual provenance.
  finding_ids:
  - gtdb-provenance
  target_ids:
  - CommunityMech:000366
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Cultivated_Meat_Contaminant_SynCom.yaml
    role: canonical_record
  acceptance_checks:
  - Retain GTDB:d__Bacteria, lineage d__Bacteria, NCBITaxon:2, majority_fraction 1.0,
    support/total 1603049/1603049 and one total destination, using ncbi_rank_d rather
    than claiming an exact strain row.
  - Record mapping snapshot SHA256 761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd.
    Distinguish observed filesystem mtime from an upstream release/build date; leave
    unknown release/build metadata unknown.
- action_id: validate-future-curation
  description: Validate any separately authorized repair.
  finding_ids:
  - member-traceability
  - gtdb-provenance
  target_ids:
  - CommunityMech:000366
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Cultivated_Meat_Contaminant_SynCom.yaml
    role: canonical_record
  acceptance_checks:
  - Recheck exact source/field scope, ontology names and graph references. Run focused
    schema, strict, terms, explained-reference, GTDB/domain and history gates, then
    just gen-html and just check-docs-current after authorized record changes.
  - Preserve all original sources, failed routes, native receipts and historical decisions.
    This review changes only its proposed review bundle and does not authorize canonical/cache/history
    edits, paid research, contact, Git mutation or issue closure.
limitations:
- Bounded ordinary public routes did not recover the whole main Methods/results/figures
  or a complete supplement inventory. This is not a global claim that no full text
  exists.
- Indexed publisher sections remain discovery leads. Exact final isolate/strain mapping,
  culture medium, vessel, inoculation, dosing and host-cell experimental details are
  not established by those truncated sections.
- S1 seven classifications and S2 six labels remain distinct. Only S1/S4 were read
  wholly; S2 row labels/five feature headers and S3 inventory were inspected, without
  whole-matrix, sequence or statistical reanalysis.
- Fresh excerpt support includes three explicit superscript renderings and two identity-field
  projections; these are distinguished from strict abstract and cache matches.
notes:
- Two node assessments bind all three canonical excerpt SHA256 values, their exact
  selectors and retained tiers. Both nodes have no encoded source/target/participants
  and no downstream arrows.
- The sole quotation is two words from the fresh MED Abstract second sentence. Other
  source text is paraphrased or referenced by exact canonical selector/hash.
- All 31 inspected inputs remain unchanged. Candidate validation and parent-owned
  saving/post-save gates occur after this scientific and support assessment; none
  is asserted in advance.
tags:
- record-review
- cultivated-meat
- syncom
- partial-source
- batch-14
```
