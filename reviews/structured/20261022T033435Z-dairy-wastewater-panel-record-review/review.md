# Dairy wastewater algal-cyanobacterial panel record review

- Review: 20261022T033435Z-dairy-wastewater-panel-record-review
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-22T03:27:23.149764Z
- Finished UTC: 2026-10-22T03:34:35.436889Z
- Reviewer: codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The panel, cultivation details and empty graph are supported. One major finding requires qualification of the article-versus-archive sequencing discrepancy and unresolved run assignments; one minor finding completes two cyanobacterial GTDB mappings. Eight focused checks pass. Literal completeness 85 and raw quality 103(capped 100) are separate from the source judgment.

## Scope And Provenance

Whole maintained record and focal data article, all three figures, declared 19 CSV inventory and selected tables, current registry and taxonomic evidence. Companion-paper access is explicitly bounded.

Selection: Only released CommunityMech:000384 in owned batch14.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base e117e3d37c65bfad2e04af53ab34e1325d8d7f98.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000384 | kb/communities/Dairy_Wastewater_Algal_Cyanobacterial_Cultivation_Panel.yaml | maintained | Dairy Wastewater Algal-Cyanobacterial Cultivation Panel |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000384 | Actual native exit0. |
| validate-strict | passed | True | CommunityMech:000384 | Actual native exit0. |
| validate-terms | passed | True | CommunityMech:000384 | Actual native exit0. |
| validate-references-explained | passed | True | CommunityMech:000384 | Actual native exit0. |
| validate-gtdb | passed | True | CommunityMech:000384 | Actual native exit0. |
| validate-gtdb-domain | passed | True | CommunityMech:000384 | Actual native exit0. |
| validate-history | passed | True | CommunityMech:000384 | Actual native exit0. |
| normalize-cache-names-check | passed | True | CommunityMech:000384 | Actual native exit0. |
| audit-network corpus context | failed | False | CommunityMech:000384 | Actual corpus exit1 retained. |
| check-network-quality corpus context | failed | False | CommunityMech:000384 | Actual corpus exit1 retained. |
| Optional structured source adapter | unavailable | False | CommunityMech:000384 | Unavailable in owned runtime. |

## Scientific And Domain Assessments

### Twelve distinct cultivation arms

identity: supported. Targets: CommunityMech:000384.

Retain the panel and all four source-named phototrophs.

MC1–4 are monocultures; CC1–4 simultaneous pairs and SC1–4 sequential pairs. Table 3 supports the existing member placements. Indigenous nonsterile bacteria remain present without an invented exhaustive roster.

### No encoded causal interactions

graph: supported. Targets: CommunityMech:000384.

Retain ecological_interactions: [] with zero nodes and zero arrows.

There are no source/target participants, node snippets or downstream directions to bind. Co-culture membership, functional predictions and community associations do not independently justify directed mechanistic edges. Empty encoding does not assert that biological interactions are absent.

### Source-matched culture and sampling

evidence: supported. Targets: CommunityMech:000384.

The encoded wastewater, culture conditions and endpoint fractionation match the full data article.

Keep measured initial pH distinct from control, working volume distinct from bottle capacity, co-culture inoculum ratio distinct from sequential transfer, and sampling filters distinct from cultivation. Exact sequential switching times remain unresolved; no unsupported schedule is added.

### Two available GTDB completions

grounding: concern. Targets: CommunityMech:000384.

Both cyanobacterial UNRESOLVED statuses can be completed at their encoded ranks.

Retain genus Synechocystis and species Desertifilum tharense with actual snapshot/route provenance. Chlorella and Euglena are eukaryotic; their current GTDB exclusions remain valid.

### Article versus archive sequencing scope

provenance: concern. Targets: CommunityMech:000384.

The correct linked project has a material platform/layout discrepancy and unresolved run assignments.

Source MiSeq PE300 paired-end and registry NovaSeq X Plus/SINGLE must both remain attributed. Counts alone cannot map 26 runs onto 13 groups by 2 fractions; five sample IDs are reused across library names. Preserve processed-table aliases rather than decoding them by order.

### Maintained YAML and prior limitations

ownership: supported. Targets: CommunityMech:000384.

The focal maintained YAML owns the proposed repairs.

Keep all prior history/cache bytes, open mechanistic discussion and the dry-run research limitation. No source or issue mutation is part of this review.

### Native validity and separate science

schema: supported. Targets: CommunityMech:000384.

Eight required focused checks pass; two contextual corpus exits and unavailable optional adapter remain explicit.

### Literal completeness and quality

completeness: supported. Targets: CommunityMech:000384.

Completeness85 and raw quality 103, capped 100.

## Findings

### archive-provenance: Qualify the source-versus-archive sequencing discrepancy

major / open / confirmed; issue key: cm-000384-archive-provenance.

The dataset block presents MiSeq PE300 paired-end data and treatment/fraction coverage without the live archive conflict. All26 returned ENA libraries declare NovaSeq X Plus/SINGLE; exact NCBI experiment metadata agrees. The21 sample records and processed CSV labels do not establish a defensible run-to-arm/fraction key. This warrants qualification, not a unilateral platform correction or rejection of the project.

### gtdb-completion: Complete the two resolvable cyanobacterial mappings

minor / open / confirmed; issue key: cm-000384-gtdb-completion.

Current reference mapping resolves the genus and species left UNRESOLVED. This enriches taxon grounding without assigning an experimental stock or changing the valid eukaryotic exclusions.

## Recommended Actions And Acceptance Checks

### qualify-archive

Preserve project identity while making source and archive scope explicit.

- Retain PRJNA1265442/SRP587285, NCBI_BIOPROJECT and AMPLICON_16S. Attribute MiSeq PE300/paired-end to Specifications, Methods 4.4 and Data 3.1; separately report all 26 returned run metadata records as NovaSeq X Plus/SINGLE, including NCBI SRX28907617/SRR33681287 confirmation. Do not silently select one version as the experimental truth.
- Qualify description, platform, conditions, sample_types and evidence explanation to distinguish article-reported arm/fraction scope from independently mapped archive contents. Preserve the exact source excerpt; a true quotation does not resolve the discrepancy.
- Record 26 MCS libraries and 21 distinct BioSamples as registry counts, without inferring replicate semantics or assigning sample aliases to treatment/fraction by order. Preserve MN/MC and AS/AT/ACK supplementary labels; leave the crosswalk unresolved until an authenticated key is available. No raw-read reanalysis or contact is required for this review repair.

### complete-gtdb

Add current genus/species mappings with accurate provenance.

- Set taxonomy[0] GROUNDED with GTDB:g__Synechocystis, genus lineage, majority_fraction 1.0, support/total 8/8, via ncbi_rank_g and one total destination. Do not interpret 21 pre-filter rows as the denominator or as study isolates.
- Set taxonomy[1] GROUNDED with GTDB:s__Desertifilum_tharense, species lineage, majority_fraction 1.0 over one reference genome, via exact ncbi_id 1185873. Keep original NCBI labels and source strain uncertainty.
- Use actual snapshot SHA256 761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd and route; do not infer a release/build date from mtime. Retain NO_GTDB_EQUIVALENT for Chlorella sorokiniana and Euglena gracilis.

### validate-future-curation

Validate any separately authorized repair.

- Recheck exact source evidence, dataset attribution and the unchanged zero-node/zero-arrow graph. Run schema, strict, terms, explained references, GTDB/domain and history checks.
- After authorized changes run just gen-html and just check-docs-current. Preserve original source/cache/history bytes and append curation provenance; this review makes no canonical, generated-page, Git or issue changes.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | kb/communities/Dairy_Wastewater_Algal_Cyanobacterial_Cultivation_Panel.yaml; Whole maintained YAML | supports | A twelve-arm cultivation panel with four phototrophs, indigenous wastewater bacteria and no encoded causal graph. |
| design | PMID:41561919; DOI:10.1016/j.dib.2025.112407; Abstract; Methods 4.1 and 4.2, each sole direct paragraph; Table 3 | supports | Four monocultures, four pairwise co-cultures and four sequential cultures are distinct treatments. Nonsterile handling retains indigenous bacteria; the four named phototrophs are not an exhaustive bacterial census. |
| cultivation | PMID:41561919; DOI:10.1016/j.dib.2025.112407; Methods 4.2 Cultivation Systems, sole direct paragraph; Table 3 | supports | The source specifies 500 mL bottles, 250 mL working volume, initial biomass 0.25 ± 0.1 g/L, co-culture 1:1 dry weight, 12 days, controlled 25 ± 0.9°C, continuous 6000 ± 100 lux from four 36 W white LEDs, three daily shakes and no external CO2 supplement. |
| medium | PMID:41561919; DOI:10.1016/j.dib.2025.112407; Methods 4.1 Wastewater collection and pre-treatment, sole direct paragraph | supports | Six layers of sterile gauze remove coarse material; nonsterile filtrate is diluted to 50% v/v with deionized water. Initial chemistry includes COD 1960±220, NH4-N 220±2.7, TN 733.3±0.1 and TP 11.06±0.6 mg/L, with measured pH 8.4±0.1. This is not a controlled pH setpoint. |
| analysis | PMID:41561919; DOI:10.1016/j.dib.2025.112407; Methods 4.3 sole paragraph; Methods 4.4 paragraphs 1–3; Methods 4.5 sole paragraph; Figures 1–3 and Tables 1–2 | supports | Endpoint 3 µm and 0.2 µm fractionation supplies PS/FL DNA. The article reports V3–V4 341F/806R amplicons, MiSeq PE300, QIIME2/DADA2, taxonomic profiles, FAPROTAX predictions and CCA/RDA associations. These analyses do not identify measured partner-specific exchange or mediation. |
| source-deposit | PMID:41561919; DOI:10.1016/j.dib.2025.112407; Specifications Table, Data collection and Data accessibility rows; Data Description 3.1 Raw data files sole paragraph; Methods 4.4 third paragraph and 4.5 sole paragraph | supports | The article links PRJNA1265442 and calls its reads paired-end, with MiSeq PE300 sequencing. Preserve this source claim while documenting the contradictory live archive metadata. |
| supplement | PMID:41561919; DOI:10.1016/j.dib.2025.112407; Appendix A, mmc1.zip; all 19 CSV member headers and sample labels; Environmental Factor and both phylum/kingdom tables | supports | The small processed-data archive supplies relative abundance and environmental tables. MN/MC and AS/AT/ACK naming variants remain unharmonized; its inspected inventory and labels do not establish an MCS run-to-arm/fraction key. No numeric matrix reanalysis was performed. |
| related | PMID:40946759; DOI:10.1016/j.biortech.2025.133329; Fresh MED Abstract, complete; limited publisher-indexed focal preview | supports | The companion abstract reports treatment-level performance and strong functional interpretations. The record already treats these as source-attributed claims and keeps mechanism/transition gaps open. The full companion Methods and figures were not recovered. |
| ontology | /private/tmp/cm-review-session/batch-14/000384/ontology-authority.json; Five exact ID-label/rank checks | supports | All four taxon labels and laboratory environment agree with current authorities. |
| schema | /private/tmp/cm-review-session/batch-14/000384/child-schema-semantics.json; Literal role, cultivation and state definitions | supports | PRIMARY_PRODUCER describes carbon fixation capability; it is not a measured wastewater flux. The pH slot alone does not assert control. |
| gtdb | /private/tmp/cm-review-session/batch-14/000384/child-gtdb-crosswalk.json; Current rank-aware genus and exact species resolutions | supports | Synechocystis maps at genus rank through 8/8 named reference genomes; Desertifilum tharense maps through one exact species reference genome. Eukaryotic taxa retain NO_GTDB_EQUIVALENT. |
| semantics | /private/tmp/cm-review-session/batch-14/000384/ontology-semantic-notes.json; Final source and ontology reconciliation | supports | Preserve the panel, broad producer capability, measured initial pH and empty graph; no study-strain substitution follows from reference mapping. |
| resources | /private/tmp/cm-review-session/batch-14/000384/dataset-verification.json; Whole source contexts, 26 ENA run records, 21 sample metadata projections and exact NCBI experiment | supports | The project identity is verified, but all returned libraries declare NovaSeq X Plus/SINGLE. NCBI SRX28907617 independently agrees. MCS1–26 across 21 BioSamples have no authenticated treatment/fraction mapping; repeated samples do not establish replicate semantics. |
| resource-selector | /private/tmp/cm-review-session/batch-14/000384/dataset-selector-clarification.json; Exact affected-field clarification | supports | Repair belongs to platform, description, conditions, sample_types and evidence explanation; no nonexistent notes field is assumed. |
| snippets | /private/tmp/cm-review-session/batch-14/000384/snippet-audit.json; All 24 canonical evidence placements | supports | Eighteen match fresh inline text and six require explicit adjacent Table 3 cell rendering; all 24 match the selected cache. Entailment was checked separately. |
| provenance | /private/tmp/cm-review-session/batch-14/000384/provenance-audit.json; Both histories, batch59 focal decision/adversarial, cohort and current context | supports | Prior panel and open-gap repairs remain valid context. The local Edison artifact is a dry run, not a paid research report or new scientific evidence. |
| inspection | /private/tmp/cm-review-session/batch-14/000384/inspect.json; 32 immutable official inputs | supports | Ignored-inclusive discovery bound ten focal contexts plus 21 authorities and the maintained target. |
| assets | /private/tmp/cm-review-session/batch-14/000384/lead-source-assets.json; Fresh main, three figures, declared CSV ZIP and related-paper access routes | supports | Complete focal body and declared assets are available. Companion ordinary publisher routes returned403 and API supplied coredata only; access bounds remain explicit. |
| lead-read | /private/tmp/cm-review-session/batch-14/000384/lead-primary-read-scope.json; Actual whole and bounded reads | supports | Whole focal text, row-preserved main tables and all three figures; all CSV headers/labels and selected small tables, not all abundance cells. |
| locators | /private/tmp/cm-review-session/batch-14/000384/source-locator-verification.json; Direct JATS section and quotation checks | supports | All source section numbers, direct paragraph counts and the sole three-word quote were verified against fresh JATS. |
| source-scope | /private/tmp/cm-review-session/batch-14/000384/source-audit.json; Final lead scientific findings | supports | One major dataset provenance qualification and one minor GTDB completion; current-claim review completed with companion-paper limits. |
| root-source | /private/tmp/cm-review-session/batch-14/000384/root-independent-source-audit.json; Independent root scientific review | supports | Root independently agrees the scope and two findings after fresh source and registry checks. |
| metrics | /private/tmp/cm-review-session/batch-14/000384/support-final-audit.json; Final independent support and literal metrics | supports | Completeness85; base 115 minus 10 for one major and 2 for one minor gives 103 raw, capped 100. Empty-graph COMPLETE is a native diagnostic, not proof of ecological knowledge. |
| support-manifest | /private/tmp/cm-review-session/batch-14/000384/support-frozen-manifest.json; Frozen supporting inputs | supports | Source, provenance, registry and authority judgments reconciled before candidate rendering. |
| auxiliary | /private/tmp/cm-review-session/batch-14/000384/auxiliary-frozen-manifest.json; Frozen authority and native outputs | supports | Eight focused checks pass and all 32 inspected inputs remain unchanged. |
| final-native | /private/tmp/cm-review-session/batch-14/000384/final-validator-summary.json; Eight actual command/stdout/stderr outcomes | supports | No native error was returned; scientific entailment is assessed independently. |
| corpus-context | /private/tmp/cm-review-session/batch-14/000384/child-current-corpus-context.json; Actual batch14 corpus baseline | supports | Both contextual corpus commands exited1 with 44 warnings across 16/477 records and zero errors. |
| adapter | /private/tmp/cm-review-session/batch-14/000384/adapter-check.json; Optional adapter availability | supports | Unavailable in the owned runtime; no external-checkout adapter was executed. |
| check-validate | /private/tmp/cm-review-session/batch-14/000384/validate.json; Actual current command/stdout/stderr | supports | Native exit0; source entailment assessed separately. |
| check-validate-strict | /private/tmp/cm-review-session/batch-14/000384/validate-strict.json; Actual current command/stdout/stderr | supports | Native exit0; source entailment assessed separately. |
| check-validate-terms | /private/tmp/cm-review-session/batch-14/000384/validate-terms.json; Actual current command/stdout/stderr | supports | Native exit0; source entailment assessed separately. |
| check-validate-references-explained | /private/tmp/cm-review-session/batch-14/000384/validate-references-explained.json; Actual current command/stdout/stderr | supports | Native exit0; source entailment assessed separately. |
| check-validate-gtdb | /private/tmp/cm-review-session/batch-14/000384/validate-gtdb.json; Actual current command/stdout/stderr | supports | Native exit0; source entailment assessed separately. |
| check-validate-gtdb-domain | /private/tmp/cm-review-session/batch-14/000384/validate-gtdb-domain.json; Actual current command/stdout/stderr | supports | Native exit0; source entailment assessed separately. |
| check-validate-history | /private/tmp/cm-review-session/batch-14/000384/validate-history.json; Actual current command/stdout/stderr | supports | Native exit0; source entailment assessed separately. |
| check-normalize-cache-names-check | /private/tmp/cm-review-session/batch-14/000384/normalize-cache-names-check.json; Actual current command/stdout/stderr | supports | Native exit0; source entailment assessed separately. |
| context-audit-network | /private/tmp/cm-review-session/batch-14/audit-network.json; Actual batch14 corpus baseline | supports | Exit1,44warnings across16/477records and zero errors. |
| context-check-network-quality | /private/tmp/cm-review-session/batch-14/check-network-quality.json; Actual batch14 corpus baseline | supports | Exit1,44warnings across16/477records and zero errors. |

## Limits And Additional Notes

- The companion research paper was read through its fresh Abstract and limited indexed preview; its full Methods, ordinary figures and supplementary inventory were not recovered. Current claims are reviewable from the complete data article; exact sequential transfer timing remains unresolved.
- The 19 CSV supplement was inventoried in full, with all headers/sample labels and selected environmental/phylum/kingdom tables read. Larger abundance matrices were not reanalysed. No raw sequence, quantitative causal reconstruction or new stock identity was inferred.
- Source processed labels, caption top 30 versus 35 displayed genera and broad companion biomolecule interpretations were not silently harmonized. Archive platform/layout and run-to-arm/fraction ambiguity remain explicit.
- FAPROTAX predictions and CCA/RDA associations do not measure transcription, exchange or selective mediation. An empty interaction graph and its native COMPLETE status do not prove absence of biological interactions.
- All32 official inputs remain unchanged. The graph contains zero nodes, zero arrows and no node snippets to bind.
- Sole quotation: three words from fresh Methods 4.2 sole paragraph. Candidate validation and root saving/post-save gates follow this review; no future pass is asserted.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T033435Z-dairy-wastewater-panel-record-review
kind: record
repository: CultureBotAI/CommunityMech
title: Dairy wastewater algal-cyanobacterial panel record review
started_at: '2026-10-22T03:27:23.149764Z'
finished_at: '2026-10-22T03:34:35.436889Z'
reviewer:
  identity: codex
  kind: agent
  independence: unknown
  independence_basis: Separate lead, root, support and auxiliary reviewers; no person-level
    independence claim.
skill: review-yaml-record
completion: completed
verdict: needs_curation
scientific_review: true
summary: The panel, cultivation details and empty graph are supported. One major finding
  requires qualification of the article-versus-archive sequencing discrepancy and
  unresolved run assignments; one minor finding completes two cyanobacterial GTDB
  mappings. Eight focused checks pass. Literal completeness 85 and raw quality 103(capped
  100) are separate from the source judgment.
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
  - path: history/records/Dairy_Wastewater_Algal_Cyanobacterial_Cultivation_Panel/2026-09-15T103307Z-codex-c7ce53.yaml
    sha256: c006f934e9c7513b3db2ba73e63b3934e0e48a26200f6a063d97708d0d328db9
    role: context
  - path: history/records/Dairy_Wastewater_Algal_Cyanobacterial_Cultivation_Panel/2026-10-06T195342Z-codex-bf5610.yaml
    sha256: 756bc94254624bb359bdee5473199c69c24cd0c94953c93f19ae198a7baf9694
    role: context
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: kb/communities/Dairy_Wastewater_Algal_Cyanobacterial_Cultivation_Panel.yaml
    sha256: 4fc81cfb17b74f44b121440c5375d5a8e2f42e76b60ee057fdc53deafa263831
    role: target
  - path: references_cache/PMID_41561919.txt
    sha256: 815ea25a152efcf13f2c82c6f96165671cfa5ab978ce71207cd6de6f51bf4f21
    role: context
  - path: reports/causal_graph_review/adversarial-review-20261006-batch59.yaml
    sha256: 9a18e460ee94a65aca27d6c8a5d17dfe188bb919ff7510977940dbd60fa74275
    role: context
  - path: reports/causal_graph_review/decisions/20261006-kefir-dairy-batch59.yaml
    sha256: 6eb7cba4bcbbfee3ba456be7cc886f59f3a032845a7c2ad252174cf2afb9f5f0
    role: context
  - path: research/communities/Dairy_Wastewater_Algal_Cyanobacterial_Cultivation_Panel-edison-literature-causal-meta.yaml
    sha256: 04042b5d68781891c536659bf65e140c24434038fdae8f27b497d2d0eae81487
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
- target_id: CommunityMech:000384
  path: kb/communities/Dairy_Wastewater_Algal_Cyanobacterial_Cultivation_Panel.yaml
  label: Dairy Wastewater Algal-Cyanobacterial Cultivation Panel
  kind: maintained
  record_class: MicrobialCommunity
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Dairy_Wastewater_Algal_Cyanobacterial_Cultivation_Panel.yaml
    role: canonical_record
scope:
  description: Whole maintained record and focal data article, all three figures,
    declared 19 CSV inventory and selected tables, current registry and taxonomic
    evidence. Companion-paper access is explicitly bounded.
  selection: Only released CommunityMech:000384 in owned batch14.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000384
checks:
- check_id: validate
  name: validate
  status: passed
  required: true
  summary: Actual native exit0.
  target_ids:
  - CommunityMech:000384
  command: just --no-dotenv validate kb/communities/Dairy_Wastewater_Algal_Cyanobacterial_Cultivation_Panel.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate
  scope_note: Focused target/history check; cache-name preflight is corpus-wide.
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Actual native exit0.
  target_ids:
  - CommunityMech:000384
  command: just --no-dotenv validate-strict kb/communities/Dairy_Wastewater_Algal_Cyanobacterial_Cultivation_Panel.yaml
    --out /private/tmp/cm-review-session/batch-14/000384/strict-report.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-strict
  scope_note: Focused target/history check; cache-name preflight is corpus-wide.
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Actual native exit0.
  target_ids:
  - CommunityMech:000384
  command: just --no-dotenv validate-terms kb/communities/Dairy_Wastewater_Algal_Cyanobacterial_Cultivation_Panel.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-terms
  scope_note: Focused target/history check; cache-name preflight is corpus-wide.
- check_id: validate-references-explained
  name: validate-references-explained
  status: passed
  required: true
  summary: Actual native exit0.
  target_ids:
  - CommunityMech:000384
  command: just --no-dotenv validate-references-explained kb/communities/Dairy_Wastewater_Algal_Cyanobacterial_Cultivation_Panel.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-references-explained
  scope_note: Focused target/history check; cache-name preflight is corpus-wide.
- check_id: validate-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: Actual native exit0.
  target_ids:
  - CommunityMech:000384
  command: just --no-dotenv validate-gtdb kb/communities/Dairy_Wastewater_Algal_Cyanobacterial_Cultivation_Panel.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb
  scope_note: Focused target/history check; cache-name preflight is corpus-wide.
- check_id: validate-gtdb-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: Actual native exit0.
  target_ids:
  - CommunityMech:000384
  command: just --no-dotenv validate-gtdb-domain kb/communities/Dairy_Wastewater_Algal_Cyanobacterial_Cultivation_Panel.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb-domain
  scope_note: Focused target/history check; cache-name preflight is corpus-wide.
- check_id: validate-history
  name: validate-history
  status: passed
  required: true
  summary: Actual native exit0.
  target_ids:
  - CommunityMech:000384
  command: just --no-dotenv validate-history history/records/Dairy_Wastewater_Algal_Cyanobacterial_Cultivation_Panel
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-history
  scope_note: Focused target/history check; cache-name preflight is corpus-wide.
- check_id: normalize-cache-names-check
  name: normalize-cache-names-check
  status: passed
  required: true
  summary: Actual native exit0.
  target_ids:
  - CommunityMech:000384
  command: uv run python scripts/normalize_cache_names.py --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-normalize-cache-names-check
  scope_note: Focused target/history check; cache-name preflight is corpus-wide.
- check_id: context-audit-network
  name: audit-network corpus context
  status: failed
  required: false
  summary: Actual corpus exit1 retained.
  target_ids:
  - CommunityMech:000384
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-14/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv audit-network
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - context-audit-network
  - corpus-context
  scope_note: Nonrequired corpus context, not wholly attributed to this target.
- check_id: context-check-network-quality
  name: check-network-quality corpus context
  status: failed
  required: false
  summary: Actual corpus exit1 retained.
  target_ids:
  - CommunityMech:000384
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-14/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv check-network-quality
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - context-check-network-quality
  - corpus-context
  scope_note: Nonrequired corpus context, not wholly attributed to this target.
- check_id: optional-structured-adapter
  name: Optional structured source adapter
  status: unavailable
  required: false
  summary: Unavailable in owned runtime.
  target_ids:
  - CommunityMech:000384
  evidence_ids:
  - adapter
  scope_note: No external-checkout adapter execution.
evidence:
- evidence_id: record
  kind: record_content
  reference: kb/communities/Dairy_Wastewater_Algal_Cyanobacterial_Cultivation_Panel.yaml
  locator: Whole maintained YAML
  summary: A twelve-arm cultivation panel with four phototrophs, indigenous wastewater
    bacteria and no encoded causal graph.
  support: supports
  accessed_at: '2026-10-22T03:34:35.430600Z'
- evidence_id: design
  kind: primary_source
  reference: PMID:41561919; DOI:10.1016/j.dib.2025.112407
  locator: Abstract; Methods 4.1 and 4.2, each sole direct paragraph; Table 3
  summary: Four monocultures, four pairwise co-cultures and four sequential cultures
    are distinct treatments. Nonsterile handling retains indigenous bacteria; the
    four named phototrophs are not an exhaustive bacterial census.
  support: supports
  accessed_at: '2026-10-22T03:34:35.430681Z'
  snapshot_sha256: d692bd7dd252ea8e075a6d936afc84ebd1f4795cf4178e7f8ea27ddfa8d7cde3
- evidence_id: cultivation
  kind: primary_source
  reference: PMID:41561919; DOI:10.1016/j.dib.2025.112407
  locator: Methods 4.2 Cultivation Systems, sole direct paragraph; Table 3
  summary: The source specifies 500 mL bottles, 250 mL working volume, initial biomass
    0.25 ± 0.1 g/L, co-culture 1:1 dry weight, 12 days, controlled 25 ± 0.9°C, continuous
    6000 ± 100 lux from four 36 W white LEDs, three daily shakes and no external CO2
    supplement.
  support: supports
  accessed_at: '2026-10-22T03:34:35.430925Z'
  snapshot_sha256: d692bd7dd252ea8e075a6d936afc84ebd1f4795cf4178e7f8ea27ddfa8d7cde3
  quote: three times daily
- evidence_id: medium
  kind: primary_source
  reference: PMID:41561919; DOI:10.1016/j.dib.2025.112407
  locator: Methods 4.1 Wastewater collection and pre-treatment, sole direct paragraph
  summary: Six layers of sterile gauze remove coarse material; nonsterile filtrate
    is diluted to 50% v/v with deionized water. Initial chemistry includes COD 1960±220,
    NH4-N 220±2.7, TN 733.3±0.1 and TP 11.06±0.6 mg/L, with measured pH 8.4±0.1. This
    is not a controlled pH setpoint.
  support: supports
  accessed_at: '2026-10-22T03:34:35.431310Z'
  snapshot_sha256: d692bd7dd252ea8e075a6d936afc84ebd1f4795cf4178e7f8ea27ddfa8d7cde3
- evidence_id: analysis
  kind: primary_source
  reference: PMID:41561919; DOI:10.1016/j.dib.2025.112407
  locator: Methods 4.3 sole paragraph; Methods 4.4 paragraphs 1–3; Methods 4.5 sole
    paragraph; Figures 1–3 and Tables 1–2
  summary: Endpoint 3 µm and 0.2 µm fractionation supplies PS/FL DNA. The article
    reports V3–V4 341F/806R amplicons, MiSeq PE300, QIIME2/DADA2, taxonomic profiles,
    FAPROTAX predictions and CCA/RDA associations. These analyses do not identify
    measured partner-specific exchange or mediation.
  support: supports
  accessed_at: '2026-10-22T03:34:35.431357Z'
  snapshot_sha256: d692bd7dd252ea8e075a6d936afc84ebd1f4795cf4178e7f8ea27ddfa8d7cde3
- evidence_id: source-deposit
  kind: primary_source
  reference: PMID:41561919; DOI:10.1016/j.dib.2025.112407
  locator: Specifications Table, Data collection and Data accessibility rows; Data
    Description 3.1 Raw data files sole paragraph; Methods 4.4 third paragraph and
    4.5 sole paragraph
  summary: The article links PRJNA1265442 and calls its reads paired-end, with MiSeq
    PE300 sequencing. Preserve this source claim while documenting the contradictory
    live archive metadata.
  support: supports
  accessed_at: '2026-10-22T03:34:35.431402Z'
  snapshot_sha256: d692bd7dd252ea8e075a6d936afc84ebd1f4795cf4178e7f8ea27ddfa8d7cde3
- evidence_id: supplement
  kind: primary_source
  reference: PMID:41561919; DOI:10.1016/j.dib.2025.112407
  locator: Appendix A, mmc1.zip; all 19 CSV member headers and sample labels; Environmental
    Factor and both phylum/kingdom tables
  summary: The small processed-data archive supplies relative abundance and environmental
    tables. MN/MC and AS/AT/ACK naming variants remain unharmonized; its inspected
    inventory and labels do not establish an MCS run-to-arm/fraction key. No numeric
    matrix reanalysis was performed.
  support: supports
  accessed_at: '2026-10-22T03:34:35.431441Z'
  snapshot_sha256: cb0e4b766fbb2c8fedaee2f38021d799d6d9d16e7ab58b4be81fbf005440ab13
- evidence_id: related
  kind: primary_source
  reference: PMID:40946759; DOI:10.1016/j.biortech.2025.133329
  locator: Fresh MED Abstract, complete; limited publisher-indexed focal preview
  summary: The companion abstract reports treatment-level performance and strong functional
    interpretations. The record already treats these as source-attributed claims and
    keeps mechanism/transition gaps open. The full companion Methods and figures were
    not recovered.
  support: supports
  accessed_at: '2026-10-22T03:34:35.431811Z'
  snapshot_sha256: 95c57ec5ff4c428d3649d859c1582fa4356dd3c38b152f91c88d920726bd86d0
- evidence_id: ontology
  kind: authority
  reference: /private/tmp/cm-review-session/batch-14/000384/ontology-authority.json
  locator: Five exact ID-label/rank checks
  summary: All four taxon labels and laboratory environment agree with current authorities.
  support: supports
  accessed_at: '2026-10-22T03:34:35.431977Z'
  snapshot_sha256: 37e6b06dacde398fff7329b0a19dfef18ff5eccf8e1940231f9813e48b2131a6
- evidence_id: schema
  kind: authority
  reference: /private/tmp/cm-review-session/batch-14/000384/child-schema-semantics.json
  locator: Literal role, cultivation and state definitions
  summary: PRIMARY_PRODUCER describes carbon fixation capability; it is not a measured
    wastewater flux. The pH slot alone does not assert control.
  support: supports
  accessed_at: '2026-10-22T03:34:35.432142Z'
  snapshot_sha256: 0da2b074c840a2b185fb7cd199fb919976d9e4852eb8abc1ba087f5a1bb94a19
- evidence_id: gtdb
  kind: authority
  reference: /private/tmp/cm-review-session/batch-14/000384/child-gtdb-crosswalk.json
  locator: Current rank-aware genus and exact species resolutions
  summary: Synechocystis maps at genus rank through 8/8 named reference genomes; Desertifilum
    tharense maps through one exact species reference genome. Eukaryotic taxa retain
    NO_GTDB_EQUIVALENT.
  support: supports
  accessed_at: '2026-10-22T03:34:35.432308Z'
  snapshot_sha256: b17dfe3ffda1cfd05b5c703597d0dc20cd38a49561823f43f2c13c4adabaca3a
- evidence_id: semantics
  kind: authority
  reference: /private/tmp/cm-review-session/batch-14/000384/ontology-semantic-notes.json
  locator: Final source and ontology reconciliation
  summary: Preserve the panel, broad producer capability, measured initial pH and
    empty graph; no study-strain substitution follows from reference mapping.
  support: supports
  accessed_at: '2026-10-22T03:34:35.432397Z'
  snapshot_sha256: c2cffb1f76a113ff89823db557a59686d6afc88c3ae11b41eb247874de3b8b62
- evidence_id: resources
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000384/dataset-verification.json
  locator: Whole source contexts, 26 ENA run records, 21 sample metadata projections
    and exact NCBI experiment
  summary: The project identity is verified, but all returned libraries declare NovaSeq
    X Plus/SINGLE. NCBI SRX28907617 independently agrees. MCS1–26 across 21 BioSamples
    have no authenticated treatment/fraction mapping; repeated samples do not establish
    replicate semantics.
  support: supports
  accessed_at: '2026-10-22T03:34:35.432565Z'
  snapshot_sha256: 385ad02aff04f4ef497072529512393a4647f9570637881bea0d2f523ae39ec8
  search_scope: Bounded source-declared project and its26 returned runs,21 sample
    metadata records, one exact NCBI experiment, and all 19 supplementary CSV headers/labels.
    No raw reads or broad archive absence claim.
- evidence_id: resource-selector
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000384/dataset-selector-clarification.json
  locator: Exact affected-field clarification
  summary: Repair belongs to platform, description, conditions, sample_types and evidence
    explanation; no nonexistent notes field is assumed.
  support: supports
  accessed_at: '2026-10-22T03:34:35.432766Z'
  snapshot_sha256: 5370ed01527b1fe5aa1c668d33d21bebf4e1c74bfb730a6148350ccbdb3e7411
- evidence_id: snippets
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000384/snippet-audit.json
  locator: All 24 canonical evidence placements
  summary: Eighteen match fresh inline text and six require explicit adjacent Table
    3 cell rendering; all 24 match the selected cache. Entailment was checked separately.
  support: supports
  accessed_at: '2026-10-22T03:34:35.432907Z'
  snapshot_sha256: 89c89dca9d2d24350e7bfd4ed8b862b009796307ac1b981ff2a0a8282c17c425
- evidence_id: provenance
  kind: prior_review
  reference: /private/tmp/cm-review-session/batch-14/000384/provenance-audit.json
  locator: Both histories, batch59 focal decision/adversarial, cohort and current
    context
  summary: Prior panel and open-gap repairs remain valid context. The local Edison
    artifact is a dry run, not a paid research report or new scientific evidence.
  support: supports
  accessed_at: '2026-10-22T03:34:35.433067Z'
  snapshot_sha256: 90c4aa9186c3efd30209ea87960d9c9f6c1748fb1f165928e15a96d667818122
- evidence_id: inspection
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000384/inspect.json
  locator: 32 immutable official inputs
  summary: Ignored-inclusive discovery bound ten focal contexts plus 21 authorities
    and the maintained target.
  support: supports
  accessed_at: '2026-10-22T03:34:35.433247Z'
  snapshot_sha256: 0d4fcef0c9c635adfcfe9be37b52abe4d18e7d53e910dc4955996014b4f51624
- evidence_id: assets
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000384/lead-source-assets.json
  locator: Fresh main, three figures, declared CSV ZIP and related-paper access routes
  summary: Complete focal body and declared assets are available. Companion ordinary
    publisher routes returned403 and API supplied coredata only; access bounds remain
    explicit.
  support: supports
  accessed_at: '2026-10-22T03:34:35.433295Z'
  snapshot_sha256: fc5034020cc4508263bf9c3c65a77eb89f57afe09b2fabc65921ff8317c852e4
- evidence_id: lead-read
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000384/lead-primary-read-scope.json
  locator: Actual whole and bounded reads
  summary: Whole focal text, row-preserved main tables and all three figures; all
    CSV headers/labels and selected small tables, not all abundance cells.
  support: supports
  accessed_at: '2026-10-22T03:34:35.433444Z'
  snapshot_sha256: 6b996c375a6bb7efbfe67e798d5b709db0fd6bade196404efaf485190a160a08
- evidence_id: locators
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000384/source-locator-verification.json
  locator: Direct JATS section and quotation checks
  summary: All source section numbers, direct paragraph counts and the sole three-word
    quote were verified against fresh JATS.
  support: supports
  accessed_at: '2026-10-22T03:34:35.433565Z'
  snapshot_sha256: 5ba402c49c432cec636afc4036b5c1003b41ea993f4b434c3cdf91cabec65b27
- evidence_id: source-scope
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000384/source-audit.json
  locator: Final lead scientific findings
  summary: One major dataset provenance qualification and one minor GTDB completion;
    current-claim review completed with companion-paper limits.
  support: supports
  accessed_at: '2026-10-22T03:34:35.433707Z'
  snapshot_sha256: 732b501dd16fb1aed4d63c55817706b6bf1db5ce83ef9c36d79af9b2b91a3c04
- evidence_id: root-source
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000384/root-independent-source-audit.json
  locator: Independent root scientific review
  summary: Root independently agrees the scope and two findings after fresh source
    and registry checks.
  support: supports
  accessed_at: '2026-10-22T03:34:35.433836Z'
  snapshot_sha256: d02edc953cf1526e191bf7d8677971e8bd1bb91a48d7ccef69161803772169a8
- evidence_id: metrics
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000384/support-final-audit.json
  locator: Final independent support and literal metrics
  summary: Completeness85; base 115 minus 10 for one major and 2 for one minor gives
    103 raw, capped 100. Empty-graph COMPLETE is a native diagnostic, not proof of
    ecological knowledge.
  support: supports
  accessed_at: '2026-10-22T03:34:35.434020Z'
  snapshot_sha256: 7f5acecd6d6ef16d7dca87e9b3af6038d1f212ff47fb61a7506a83a261ab82a1
- evidence_id: support-manifest
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000384/support-frozen-manifest.json
  locator: Frozen supporting inputs
  summary: Source, provenance, registry and authority judgments reconciled before
    candidate rendering.
  support: supports
  accessed_at: '2026-10-22T03:34:35.434072Z'
  snapshot_sha256: d48438565fc09d05dabb63883a0a3b4785c93ea50dc1546b9692cc3e938f93e9
- evidence_id: auxiliary
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000384/auxiliary-frozen-manifest.json
  locator: Frozen authority and native outputs
  summary: Eight focused checks pass and all 32 inspected inputs remain unchanged.
  support: supports
  accessed_at: '2026-10-22T03:34:35.434227Z'
  snapshot_sha256: 70dadebd2eb571a56a249f7b06dc68d50cbbef85ae83a7a2f5f6afbd02a12a7a
- evidence_id: final-native
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000384/final-validator-summary.json
  locator: Eight actual command/stdout/stderr outcomes
  summary: No native error was returned; scientific entailment is assessed independently.
  support: supports
  accessed_at: '2026-10-22T03:34:35.434281Z'
  snapshot_sha256: 1d1cb6b39ad0ed117af67b5390e2576b57fa3944ca74db228edeb471492f3986
- evidence_id: corpus-context
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000384/child-current-corpus-context.json
  locator: Actual batch14 corpus baseline
  summary: Both contextual corpus commands exited1 with 44 warnings across 16/477
    records and zero errors.
  support: supports
  accessed_at: '2026-10-22T03:34:35.434417Z'
  snapshot_sha256: 0186650be15a27e2a0c24d409771b93ee5bce2ed10a00f0789fbcfacc862b6c8
- evidence_id: adapter
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000384/adapter-check.json
  locator: Optional adapter availability
  summary: Unavailable in the owned runtime; no external-checkout adapter was executed.
  support: supports
  accessed_at: '2026-10-22T03:34:35.434545Z'
  snapshot_sha256: ec0f95042c7f7a1d1d48839f9da5c94395b37f0d106e5b3f2dbe6a9e2538ff97
- evidence_id: check-validate
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000384/validate.json
  locator: Actual current command/stdout/stderr
  summary: Native exit0; source entailment assessed separately.
  support: supports
  accessed_at: '2026-10-22T03:34:35.435267Z'
  snapshot_sha256: b66e2652067865a351185641c9bfd93ba9a2b58e85a35bc45ac6a4defe0f37b8
- evidence_id: check-validate-strict
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000384/validate-strict.json
  locator: Actual current command/stdout/stderr
  summary: Native exit0; source entailment assessed separately.
  support: supports
  accessed_at: '2026-10-22T03:34:35.435447Z'
  snapshot_sha256: b184fb6f17abf09606367df682ea62b916ed4cc83942883f15f0f191d7af8c54
- evidence_id: check-validate-terms
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000384/validate-terms.json
  locator: Actual current command/stdout/stderr
  summary: Native exit0; source entailment assessed separately.
  support: supports
  accessed_at: '2026-10-22T03:34:35.435611Z'
  snapshot_sha256: 279ebe4fc56f1970472e2f33b1842357c4710ca22e423c3171d9e9777a1d42ed
- evidence_id: check-validate-references-explained
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000384/validate-references-explained.json
  locator: Actual current command/stdout/stderr
  summary: Native exit0; source entailment assessed separately.
  support: supports
  accessed_at: '2026-10-22T03:34:35.435787Z'
  snapshot_sha256: 30e34a8d1c719f1ae5cf255e7e1b1665f74a0ae7b8113798294d5ebdffa52eae
- evidence_id: check-validate-gtdb
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000384/validate-gtdb.json
  locator: Actual current command/stdout/stderr
  summary: Native exit0; source entailment assessed separately.
  support: supports
  accessed_at: '2026-10-22T03:34:35.435989Z'
  snapshot_sha256: cefce7cde7dd5a59f3db45032dda89ce0bcb3f9803b81fde0193781f4ef0268e
- evidence_id: check-validate-gtdb-domain
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000384/validate-gtdb-domain.json
  locator: Actual current command/stdout/stderr
  summary: Native exit0; source entailment assessed separately.
  support: supports
  accessed_at: '2026-10-22T03:34:35.436154Z'
  snapshot_sha256: 6667cb2006ceea757342a457ab5adb006dc416175d376a6415ee451c38a990e8
- evidence_id: check-validate-history
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000384/validate-history.json
  locator: Actual current command/stdout/stderr
  summary: Native exit0; source entailment assessed separately.
  support: supports
  accessed_at: '2026-10-22T03:34:35.436301Z'
  snapshot_sha256: 872cf2715d21ee91b3bb2fc4fc68a8c05bc8844072a745d934f76b064abdda78
- evidence_id: check-normalize-cache-names-check
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000384/normalize-cache-names-check.json
  locator: Actual current command/stdout/stderr
  summary: Native exit0; source entailment assessed separately.
  support: supports
  accessed_at: '2026-10-22T03:34:35.436460Z'
  snapshot_sha256: b113d979052f8f0f5ba648781585667dc3dd774fac254f9138f77222f5a86728
- evidence_id: context-audit-network
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/audit-network.json
  locator: Actual batch14 corpus baseline
  summary: Exit1,44warnings across16/477records and zero errors.
  support: supports
  accessed_at: '2026-10-22T03:34:35.436669Z'
  snapshot_sha256: 3110e0bb1dbe3ea63b81aea82871ac4adb2915c8fce1d15249422d0f5db266c6
- evidence_id: context-check-network-quality
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/check-network-quality.json
  locator: Actual batch14 corpus baseline
  summary: Exit1,44warnings across16/477records and zero errors.
  support: supports
  accessed_at: '2026-10-22T03:34:35.436842Z'
  snapshot_sha256: 18896ef4136601b37550cb5612abc06784abcbf982e4778cbf2b9c10368cb66a
assessments:
- assessment_id: identity
  area: identity
  topic: Twelve distinct cultivation arms
  outcome: supported
  summary: Retain the panel and all four source-named phototrophs.
  target_ids:
  - CommunityMech:000384
  evidence_ids:
  - design
  - ontology
  - record
  dimensions:
  - name: experimental_scope
    value: Four MC, four CC and four SC treatments
    definition: A cultivation panel rather than one bottle containing all four phototrophs.
    evidence_ids:
    - design
  - name: strain_scope
    value: Genus/species names only
    definition: No verified collection identifier or study-strain genome assignment.
    evidence_ids:
    - design
    - ontology
  details: MC1–4 are monocultures; CC1–4 simultaneous pairs and SC1–4 sequential pairs.
    Table 3 supports the existing member placements. Indigenous nonsterile bacteria
    remain present without an invented exhaustive roster.
- assessment_id: graph-empty
  area: graph
  topic: No encoded causal interactions
  outcome: supported
  summary: 'Retain ecological_interactions: [] with zero nodes and zero arrows.'
  target_ids:
  - CommunityMech:000384
  evidence_ids:
  - analysis
  - related
  - semantics
  details: There are no source/target participants, node snippets or downstream directions
    to bind. Co-culture membership, functional predictions and community associations
    do not independently justify directed mechanistic edges. Empty encoding does not
    assert that biological interactions are absent.
- assessment_id: cultivation
  area: evidence
  topic: Source-matched culture and sampling
  outcome: supported
  summary: The encoded wastewater, culture conditions and endpoint fractionation match
    the full data article.
  target_ids:
  - CommunityMech:000384
  evidence_ids:
  - cultivation
  - medium
  - analysis
  details: Keep measured initial pH distinct from control, working volume distinct
    from bottle capacity, co-culture inoculum ratio distinct from sequential transfer,
    and sampling filters distinct from cultivation. Exact sequential switching times
    remain unresolved; no unsupported schedule is added.
- assessment_id: grounding
  area: grounding
  topic: Two available GTDB completions
  outcome: concern
  summary: Both cyanobacterial UNRESOLVED statuses can be completed at their encoded
    ranks.
  target_ids:
  - CommunityMech:000384
  evidence_ids:
  - gtdb
  - ontology
  - semantics
  details: Retain genus Synechocystis and species Desertifilum tharense with actual
    snapshot/route provenance. Chlorella and Euglena are eukaryotic; their current
    GTDB exclusions remain valid.
- assessment_id: archive
  area: provenance
  topic: Article versus archive sequencing scope
  outcome: concern
  summary: The correct linked project has a material platform/layout discrepancy and
    unresolved run assignments.
  target_ids:
  - CommunityMech:000384
  evidence_ids:
  - source-deposit
  - resources
  - supplement
  - resource-selector
  details: Source MiSeq PE300 paired-end and registry NovaSeq X Plus/SINGLE must both
    remain attributed. Counts alone cannot map 26 runs onto 13 groups by 2 fractions;
    five sample IDs are reused across library names. Preserve processed-table aliases
    rather than decoding them by order.
- assessment_id: ownership
  area: ownership
  topic: Maintained YAML and prior limitations
  outcome: supported
  summary: The focal maintained YAML owns the proposed repairs.
  target_ids:
  - CommunityMech:000384
  evidence_ids:
  - inspection
  - provenance
  details: Keep all prior history/cache bytes, open mechanistic discussion and the
    dry-run research limitation. No source or issue mutation is part of this review.
- assessment_id: native
  area: schema
  topic: Native validity and separate science
  outcome: supported
  summary: Eight required focused checks pass; two contextual corpus exits and unavailable
    optional adapter remain explicit.
  target_ids:
  - CommunityMech:000384
  evidence_ids:
  - final-native
  - auxiliary
  - corpus-context
  - adapter
  - snippets
- assessment_id: metrics
  area: completeness
  topic: Literal completeness and quality
  outcome: supported
  summary: Completeness85 and raw quality 103, capped 100.
  target_ids:
  - CommunityMech:000384
  evidence_ids:
  - metrics
  metrics:
  - name: completeness
    value: 85
    unit: points
    minimum: 0
    maximum: 100
    definition: 50 required fields/taxon roles +5 environment +10 at least three factors
      +5 external resources +10 growth media +5 datasets; zero interaction-node/metabolite
      awards.
  - name: validation_quality
    value: 100
    unit: points
    minimum: 0
    maximum: 100
    definition: 100 -1major*10 -1minor*2 +0 evidence bonus +15 native COMPLETE =103
      raw, capped 100. Zero nodes, arrows and node evidence; the mathematical COMPLETE
      bonus does not certify ecological completeness.
  - name: P1
    value: 0
    unit: findings
    definition: Native severity count.
  - name: P2
    value: 1
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
- finding_id: archive-provenance
  issue_key: cm-000384-archive-provenance
  category: provenance
  severity: major
  native_severity: P2
  normalization_reason: Material conflict affects source and archive interpretation
    and reuse.
  rule_id: review-checklist.claim-specific-support-and-context
  status: open
  certainty: confirmed
  title: Qualify the source-versus-archive sequencing discrepancy
  description: The dataset block presents MiSeq PE300 paired-end data and treatment/fraction
    coverage without the live archive conflict. All26 returned ENA libraries declare
    NovaSeq X Plus/SINGLE; exact NCBI experiment metadata agrees. The21 sample records
    and processed CSV labels do not establish a defensible run-to-arm/fraction key.
    This warrants qualification, not a unilateral platform correction or rejection
    of the project.
  target_ids:
  - CommunityMech:000384
  field_paths:
  - associated_datasets[0].platform
  - associated_datasets[0].description
  - associated_datasets[0].conditions
  - associated_datasets[0].sample_types
  - associated_datasets[0].evidence[0].explanation
  evidence_ids:
  - source-deposit
  - resources
  - supplement
  - resource-selector
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Dairy_Wastewater_Algal_Cyanobacterial_Cultivation_Panel.yaml
    role: canonical_record
  ownership_note: The maintained focal YAML owns repair; source and archive assertions
    remain separately attributed.
- finding_id: gtdb-completion
  issue_key: cm-000384-gtdb-completion
  category: grounding
  severity: minor
  native_severity: P3
  normalization_reason: Recoverable taxonomic mapping at already encoded ranks.
  rule_id: review-checklist.claim-specific-support-and-context
  status: open
  certainty: confirmed
  title: Complete the two resolvable cyanobacterial mappings
  description: Current reference mapping resolves the genus and species left UNRESOLVED.
    This enriches taxon grounding without assigning an experimental stock or changing
    the valid eukaryotic exclusions.
  target_ids:
  - CommunityMech:000384
  field_paths:
  - taxonomy[0].taxon_term.gtdb_grounding_status
  - taxonomy[1].taxon_term.gtdb_grounding_status
  evidence_ids:
  - gtdb
  - ontology
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Dairy_Wastewater_Algal_Cyanobacterial_Cultivation_Panel.yaml
    role: canonical_record
  ownership_note: The maintained focal YAML owns repair; source and archive assertions
    remain separately attributed.
actions:
- action_id: qualify-archive
  description: Preserve project identity while making source and archive scope explicit.
  finding_ids:
  - archive-provenance
  target_ids:
  - CommunityMech:000384
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Dairy_Wastewater_Algal_Cyanobacterial_Cultivation_Panel.yaml
    role: canonical_record
  acceptance_checks:
  - Retain PRJNA1265442/SRP587285, NCBI_BIOPROJECT and AMPLICON_16S. Attribute MiSeq
    PE300/paired-end to Specifications, Methods 4.4 and Data 3.1; separately report
    all 26 returned run metadata records as NovaSeq X Plus/SINGLE, including NCBI
    SRX28907617/SRR33681287 confirmation. Do not silently select one version as the
    experimental truth.
  - Qualify description, platform, conditions, sample_types and evidence explanation
    to distinguish article-reported arm/fraction scope from independently mapped archive
    contents. Preserve the exact source excerpt; a true quotation does not resolve
    the discrepancy.
  - Record 26 MCS libraries and 21 distinct BioSamples as registry counts, without
    inferring replicate semantics or assigning sample aliases to treatment/fraction
    by order. Preserve MN/MC and AS/AT/ACK supplementary labels; leave the crosswalk
    unresolved until an authenticated key is available. No raw-read reanalysis or
    contact is required for this review repair.
- action_id: complete-gtdb
  description: Add current genus/species mappings with accurate provenance.
  finding_ids:
  - gtdb-completion
  target_ids:
  - CommunityMech:000384
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Dairy_Wastewater_Algal_Cyanobacterial_Cultivation_Panel.yaml
    role: canonical_record
  acceptance_checks:
  - Set taxonomy[0] GROUNDED with GTDB:g__Synechocystis, genus lineage, majority_fraction
    1.0, support/total 8/8, via ncbi_rank_g and one total destination. Do not interpret
    21 pre-filter rows as the denominator or as study isolates.
  - Set taxonomy[1] GROUNDED with GTDB:s__Desertifilum_tharense, species lineage,
    majority_fraction 1.0 over one reference genome, via exact ncbi_id 1185873. Keep
    original NCBI labels and source strain uncertainty.
  - Use actual snapshot SHA256 761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd
    and route; do not infer a release/build date from mtime. Retain NO_GTDB_EQUIVALENT
    for Chlorella sorokiniana and Euglena gracilis.
- action_id: validate-future-curation
  description: Validate any separately authorized repair.
  finding_ids:
  - archive-provenance
  - gtdb-completion
  target_ids:
  - CommunityMech:000384
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Dairy_Wastewater_Algal_Cyanobacterial_Cultivation_Panel.yaml
    role: canonical_record
  acceptance_checks:
  - Recheck exact source evidence, dataset attribution and the unchanged zero-node/zero-arrow
    graph. Run schema, strict, terms, explained references, GTDB/domain and history
    checks.
  - After authorized changes run just gen-html and just check-docs-current. Preserve
    original source/cache/history bytes and append curation provenance; this review
    makes no canonical, generated-page, Git or issue changes.
limitations:
- The companion research paper was read through its fresh Abstract and limited indexed
  preview; its full Methods, ordinary figures and supplementary inventory were not
  recovered. Current claims are reviewable from the complete data article; exact sequential
  transfer timing remains unresolved.
- The 19 CSV supplement was inventoried in full, with all headers/sample labels and
  selected environmental/phylum/kingdom tables read. Larger abundance matrices were
  not reanalysed. No raw sequence, quantitative causal reconstruction or new stock
  identity was inferred.
- Source processed labels, caption top 30 versus 35 displayed genera and broad companion
  biomolecule interpretations were not silently harmonized. Archive platform/layout
  and run-to-arm/fraction ambiguity remain explicit.
- FAPROTAX predictions and CCA/RDA associations do not measure transcription, exchange
  or selective mediation. An empty interaction graph and its native COMPLETE status
  do not prove absence of biological interactions.
notes:
- All32 official inputs remain unchanged. The graph contains zero nodes, zero arrows
  and no node snippets to bind.
- 'Sole quotation: three words from fresh Methods 4.2 sole paragraph. Candidate validation
  and root saving/post-save gates follow this review; no future pass is asserted.'
tags:
- record-review
- dairy-wastewater
- cultivation-panel
- batch-14
```
