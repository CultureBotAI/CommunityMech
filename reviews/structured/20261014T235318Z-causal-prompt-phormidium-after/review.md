# Causal prompt repair and partial Phormidium extension research

- Review: 20261014T235318Z-causal-prompt-phormidium-after
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-14T23:53:18.314795Z
- Finished UTC: 2026-10-14T23:53:18.314795Z
- Reviewer: codex (self_review)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The shared prompt direction defect is resolved with failing-before/passing-after render tests. The four Phormidium nodes and one arrow remain unchanged; seven niche candidates and four source discrepancies are documented. Required extension research and participant reconciliation remain open under #1699; this is not corpus completion.

## Scope And Provenance

One maintained prompt plus the current Phormidium graph and source-backed extension handoff.

Selection: Next needs_research record and the shared prompt used for its dry run.
Coverage: partial; 2 reviewed / 462 in the declared population.
Source: git_commit at Git base 413abb97a13d7ae3c5af960afacb770dd1e216e9.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| causal-template | templates/community_causal_graph_research.md | maintained | Causal research prompt |
| CommunityMech:000054 | kb/communities/Phormidium_Alkaline_Consortium.yaml | maintained | Phormidium alkaline consortium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| final-focused-tests | passed | True | causal-template, CommunityMech:000054 | 25 focused tests pass, including the shared render path, capture/provenance tests and review contract tests; 12 dependency deprecation warnings remain. |
| lint-formatted | passed | True | causal-template | Black, Ruff and mypy pass after the retained first lint failure was corrected. |
| corrected-phormidium-dry-run | passed | True | causal-template, CommunityMech:000054 | The maintained one-community dry run succeeds with a 17518-character query. No authentication or Edison job was submitted; an SDK public model-cost lookup failed and used its fallback. |
| source-replay | passed | True | CommunityMech:000054 | Six source file hashes, selected table observations, all 462 canonical record hashes and unchanged 57 network warnings replay successfully. Discovery includes ignored files. |
| docs-current | passed | True | causal-template, CommunityMech:000054 | The native generated-docs currency check passes without generated changes. |
| before-bundle-check | passed | True | causal-template | The before bundle and 20 earlier structured bundles validate against the pre-change main base. |
| Native network zero-warning diagnostic | failed | False | CommunityMech:000054 | Actual exit 1 with 57 existing DISCONNECTED/UNKNOWN_TARGET warnings, identical to batch130. No error-severity findings; do not claim a zero-warning pass. |
| Required one-community extension research | unavailable | True | CommunityMech:000054 | Spending is authorized but no inherited Edison/FutureHouse credential is available. No credential values or dotenv file inspected. No provider submission occurred; explicit primary-only substitution authorization is pending. |

## Scientific And Domain Assessments

### Corrected causal direction and evidence boundaries

graph: supported. Targets: causal-template.

The corrected illustrative direction agrees with the primary study, while measured effects, predictions and hypotheses remain distinct from unverified record context. Render tests reject the original example and preserve both target contexts.

### Photosynthetic CO2 Fixation

graph: supported. Targets: CommunityMech:000054.

Figure 4 and the protein/SIP Results support cyanobacterial assimilation of supplied inorganic-carbon label. No inference that each proposed organic-carbon release route was measured.

### Carbon Transfer to Heterotrophs

graph: supported. Targets: CommunityMech:000054.

Figure 4 and Table S4 show the strongest heterotrophic peptide coverage for MAG34 and MAG57. Label incorporation is not a compound-specific transfer assay or proof of nutrient return.

### Proposed Cyanobacterial Polymer Use by Verrucomicrobiota

graph: supported. Targets: CommunityMech:000054.

Figure 3 and the Results assign hydrolase/sulfatase gene capacity to four MAGs. Capacity and weak isotope signals do not isolate sulfated polymers as the exchanged substrate.

### Alphaproteobacterial Heterotrophic Carbon Use

graph: supported. Targets: CommunityMech:000054.

Figure 4 and Table S4 retain a low-peptide MAG58 signal; Figure 3 separates predicted phototrophy. No class-wide reciprocal vitamin, siderophore, nitrogen or protection service is established.

### Photosynthetic carbon input to heterotrophic incorporation

graph: supported. Targets: CommunityMech:000054.

Retain the existing arrow from Photosynthetic CO2 Fixation to Carbon Transfer to Heterotrophs. In vitro bicarbonate protein/SIP supports this direction; it does not identify exchanged compounds, exact release routes, nutrient return or a precisely timed trophic cascade.

### Unfinished niche coverage and MAG-level source reconciliation

completeness: concern. Targets: CommunityMech:000054.

The primary paper describes seven candidate niches beyond the sparse representation. New nodes require qualified gene-based versus experimental scope, participant reconciliation and source-conflict disposition. MAG58 almA, MAG57 alkB, late SIP times and the cyanobacterial peptide total disagree across source representations; they are constraints, not four new canonical defects.

## Findings

### hydrogen-direction: Shared prompt reverses hydrogen-mediated facilitation

major / resolved / confirmed; issue key: communitymech-2007-hydrogen-direction.

The old example assigned reduced hydrogen partial pressure to production and could bias research directions.

Disposition: Consumption-to-oxidation direction is corrected; illustration and target evidence are explicitly separate, and record context must be checked. New render tests failed against the original and pass against the repaired template.

### phormidium-coverage: Phormidium niche coverage remains incomplete

major / open / confirmed; issue key: communitymech-1699-coverage.

The bounded four-node graph does not yet represent the source's other proposed ecological niches. Source conflicts and MAG-level participant reconciliation must be assessed before adding supported structure; a connected graph is not itself the acceptance criterion.

## Recommended Actions And Acceptance Checks

### extend-phormidium

Complete authorized one-community research, reconcile MAG/source discrepancies and curate only supported graph structure.

- Obtain the one-community Edison research report required by the invoked skill, or explicit authorization to use direct-primary-source research in its place.
- Keep the corrected prompt and explicit warning about non-graph context claims tracked in issue 1701.
- Resolve MAG-level participant mapping against source taxonomy and canonical identifiers without transferring related-species phenotypes.
- Verify exact snippets and keep supplemental evidence separate from article caches.
- Apply only supported nodes/arrows with guarded writes, append-only history, validators, generated-doc checks and a successor review.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| hydrogen | PMID:16347751; https://pubmed.ncbi.nlm.nih.gov/16347751/ ; Abstract | supports | Primary experimental abstract reports hydrogen inhibition of syntrophic butyrate conversion and dependence on product removal. It supports the direction of the illustration, not Phormidium biology. |
| prompt | templates/community_causal_graph_research.md; Community context boundary and Causal edges example | supports | The maintained prompt now attributes lowered hydrogen partial pressure to consumption, labels the example illustrative, and requires checking record claims against primary evidence. |
| before | reviews/structured/20261014T234638Z-causal-prompt-before/review.yaml; finding hydrogen-direction | context_only | Immutable historical finding at the original main commit; lineage is explicitly retained. |
| phormidium | doi:10.3389/fmicb.2022.780346; reports/causal_graph_review/sources/20261014-phormidium-batch131/manifest.json ; Introduction, Methods, Results/Discussion, Figure 3 and 4 pixels, selected Table S3/S4 cells | partial | Main text, figure pixels and selected supplement cells support bounded carbon assimilation and predicted niches; four source discrepancies constrain new MAG-specific or precisely timed claims. Table S2 headers only, not all taxonomic rows, were inspected. |
| handoff | reports/causal_graph_review/sources/20261014-phormidium-batch131/assessment.yaml; current_graph, extension_candidates, source_discrepancies, verified_coverage | supports | Per-node and arrow retention reasons, seven candidate niches, exact source cells and four conflicts are preserved. This is a research handoff, not completed graph curation. |
| record | kb/communities/Phormidium_Alkaline_Consortium.yaml; ecological_interactions and related knowledge-gap Discussion | supports | All four current nodes and the single donor-to-heterotroph arrow were read. Source taxon is Ca. Phormidium alkaliphilum; the major recipients are MAG34 and MAG57, with broad canonical grounding explicitly bounded. Non-graph claims tracked by #1701 are not certified. |
| final-focused-tests | reports/causal_graph_review/20261014-batch131/final-focused-tests.json | supports | 25 focused tests pass, including the shared render path, capture/provenance tests and review contract tests; 12 dependency deprecation warnings remain. |
| lint-formatted | reports/causal_graph_review/20261014-batch131/lint-formatted.json | supports | Black, Ruff and mypy pass after the retained first lint failure was corrected. |
| corrected-phormidium-dry-run | reports/causal_graph_review/20261014-batch131/corrected-phormidium-dry-run.json | supports | The maintained one-community dry run succeeds with a 17518-character query. No authentication or Edison job was submitted; an SDK public model-cost lookup failed and used its fallback. |
| source-replay | reports/causal_graph_review/20261014-batch131/source-replay.json | supports | Six source file hashes, selected table observations, all 462 canonical record hashes and unchanged 57 network warnings replay successfully. Discovery includes ignored files. |
| docs-current | reports/causal_graph_review/20261014-batch131/docs-current.json | supports | The native generated-docs currency check passes without generated changes. |
| before-bundle-check | reports/causal_graph_review/20261014-batch131/before-bundle-check.json | supports | The before bundle and 20 earlier structured bundles validate against the pre-change main base. |

## Limits And Additional Notes

- Partial source-based self-review, not independent approval or whole-record certification. All 54 needs_research statuses remain unchanged.
- No Edison job was submitted. Spend authorization exists but inherited credentials do not; no dotenv or credential values were inspected. Primary-only substitution authorization is pending.
- Read spans are bounded in the source manifest. Full Table S2 classification reconciliation, supplementary PDF, raw data and proposed extension remain unreviewed.
- Blank annotation cells are not proof of gene absence; individual annotations do not automatically meet figure pathway-completeness criteria. Peptide counts are sampling coverage, not biomass or exchange flux.
- The source's functional-redundancy explanation is not an isolated causal perturbation. Source disagreements are preserved rather than silently reconciled.
- All 462 canonical records, reference caches and histories remain unchanged. Supplements are retained separately, not inserted into the canonical article cache.
- Native whole-record completeness and validation-quality metrics are not computed for this scoped prompt/research assessment. No canonical validation/status promotion is claimed.
- The network zero-warning diagnostic still exits 1 for 57 unchanged warnings. The replay checks preservation and structural error absence, not semantic completeness.
- The intentionally failing old-template regression and first lint failure remain preserved as historical receipts, not final passes.
- Remote CI and merge-queue checks have not yet completed at this snapshot; publication must respect required checks.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T235318Z-causal-prompt-phormidium-after
kind: repository
repository: CultureBotAI/CommunityMech
title: Causal prompt repair and partial Phormidium extension research
started_at: '2026-10-14T23:53:18.314795Z'
finished_at: '2026-10-14T23:53:18.314795Z'
reviewer:
  identity: codex
  kind: agent
  independence: self_review
  independence_basis: The implementing agent performed source-based adversarial checks;
    no independent approval is claimed.
skill: communitymech-causal-graphs
completion: partial
verdict: needs_curation
scientific_review: true
summary: 'The shared prompt direction defect is resolved with failing-before/passing-after
  render tests. The four Phormidium nodes and one arrow remain unchanged; seven niche
  candidates and four source discrepancies are documented. Required extension research
  and participant reconciliation remain open under #1699; this is not corpus completion.'
source:
  git_revision: 413abb97a13d7ae3c5af960afacb770dd1e216e9
  state: git_commit
  inputs:
  - path: conf/record_review.yaml
    sha256: 8cbd8f9d209f78de47a8c35091e43bf1dadbe41ee07492c7860b6d4be30112a8
    role: context
  - path: docs/record-review-profile.md
    sha256: 285f79747999f83edbe63e5efde349a5cc063e9e486ce1a748b47b76c6631f31
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: kb/communities/Phormidium_Alkaline_Consortium.yaml
    sha256: 5bd6ec7333293e123e4b68212ddd64a6db8a8efd69f446912d154b260d79f2f5
    role: target
  - path: references_cache/doi_10.3389_fmicb.2022.780346.md
    sha256: a3ba7f3dfd3bd6b6ae6338a05beead53f2cb15c89f70f0a89700cbfa0dc2b929
    role: context
  - path: reports/causal_graph_review/20261014-batch130/final-network.json
    sha256: d77f31682218889018b9e0fa2fef83608e4af9f127d2c6414a5e288e75beaec5
    role: context
  - path: reports/causal_graph_review/20261014-batch131/after-template-regression.json
    sha256: 8fa226cfb4f3b4f2cc7ffb0c4924eb5020570a4e47301cb6aadc8980b800f733
    role: context
  - path: reports/causal_graph_review/20261014-batch131/baseline-network.json
    sha256: 2d5bfe9faae3bc2ddf240f244053d0ef76acd4675d02e01315d7ad2c6dc019e0
    role: context
  - path: reports/causal_graph_review/20261014-batch131/baseline-rank.json
    sha256: fc5a46fb2abe7a7c6284d317f385fcd4381064628e1ffce273004385eb6e475d
    role: context
  - path: reports/causal_graph_review/20261014-batch131/before-bundle-check.json
    sha256: 0291f0d3dde039eb8fed270f763e7cf3e0e608e39336b0e54fff6154c7ccb87f
    role: context
  - path: reports/causal_graph_review/20261014-batch131/before-template-regression.json
    sha256: b5b831c9d63390ff6bdfa386505d002d901e613b9892912f154dcbd71e41ec88
    role: context
  - path: reports/causal_graph_review/20261014-batch131/corrected-phormidium-dry-run.json
    sha256: 1f67c8cd380119988835cd623f739843a24c1d4faec90fe112317bfc9213d222
    role: context
  - path: reports/causal_graph_review/20261014-batch131/docs-current.json
    sha256: 825ee33987cd691d4e4ec3ce15fd74d83d7f9322b2eaac7f99661c2026cb190a
    role: context
  - path: reports/causal_graph_review/20261014-batch131/final-focused-tests.json
    sha256: 44741ab66ee9c2d06f5523567b5160a6798caf0dc4914a70fff8e96fd353cf44
    role: context
  - path: reports/causal_graph_review/20261014-batch131/focused-research-tests.json
    sha256: 9e15d56edc3700042aba39f767a70812cd63c613d2ce9f856cc6a94c695f3cbc
    role: context
  - path: reports/causal_graph_review/20261014-batch131/lint-formatted.json
    sha256: e1baf5dfdfdf5aed27a693249422bd416fa7c168e9ab6c70581f7ff29b65ca6a
    role: context
  - path: reports/causal_graph_review/20261014-batch131/lint.json
    sha256: ca19a82ee7f3d05b284a42737946d30d9437aa3bdb8d1b98012eb4f90b927e1e
    role: context
  - path: reports/causal_graph_review/20261014-batch131/phormidium-corrected-dry-run.yaml
    sha256: f426f4da29518080c4429fa30376af1295ef6d2a97e2198584e47b32b6bb08d6
    role: context
  - path: reports/causal_graph_review/20261014-batch131/source-replay.json
    sha256: 0af177d1c9a49fd441d5ef4099f744f727a85735f1419e7c32101d961842fe26
    role: context
  - path: reports/causal_graph_review/20261014-batch131/verify_sources.py
    sha256: c09d2a804e69fe8370af08a0bcd5c7f38ff04049f398c29802a1d44eb88e5c39
    role: context
  - path: reports/causal_graph_review/inventory.tsv
    sha256: e826c14f14487a8feb7a4a54db7608881d112ff19d97c1df2332b81e70e43f7e
    role: context
  - path: reports/causal_graph_review/sources/20261014-phormidium-batch131/Table_2.XLSX
    sha256: 9b4837c57b8a05888e893b2adf3b8d89d525a20d8f2931e1cd04efd325919437
    role: context
  - path: reports/causal_graph_review/sources/20261014-phormidium-batch131/Table_3.XLSX
    sha256: 5c3ae85d677594e8e7b539ed4c442408f68f6623f03deefca7c20f0660928e39
    role: context
  - path: reports/causal_graph_review/sources/20261014-phormidium-batch131/Table_4.XLSX
    sha256: 69e74d4f46fe34baa6686121709f192cc01afb7eca3becff77affa88bde1d475
    role: context
  - path: reports/causal_graph_review/sources/20261014-phormidium-batch131/article.xml
    sha256: 3c62edb9012494e345827fe35d4a76c11a96f9c2decc36ffabfdfef43d0e14f5
    role: context
  - path: reports/causal_graph_review/sources/20261014-phormidium-batch131/assessment.yaml
    sha256: 2a60b9c521a35f667416739a3173a0875c22c060de1cc4edc1d3ea932addd5ac
    role: context
  - path: reports/causal_graph_review/sources/20261014-phormidium-batch131/figure3.webp
    sha256: f77c1718da6b886c6cc23f6e5f4e4e7808231b6e506309a193e2c6750465859a
    role: context
  - path: reports/causal_graph_review/sources/20261014-phormidium-batch131/figure4.webp
    sha256: 5790622cfe193f975a430371af77f6654e45f5420006b62c5b2869c872fcc22d
    role: context
  - path: reports/causal_graph_review/sources/20261014-phormidium-batch131/manifest.json
    sha256: aaf3062cb86b02f0952dd4bfdfab4a6cbe7ed88e6af2f5120e4e0912bd027553
    role: context
  - path: reports/causal_graph_review/summary.json
    sha256: d4e452ae6d6b3a8c12a77274e08723406b5c97fb702a4df58d15c1e547e92819
    role: context
  - path: reviews/structured/20261014T234638Z-causal-prompt-before/review.md
    sha256: 903d0433ad183c8e546489ff602d6e022c8016d3c3f681e1a51672fc173ffd14
    role: context
  - path: reviews/structured/20261014T234638Z-causal-prompt-before/review.yaml
    sha256: f104b34c86ce70c5f045eae8cb2d0739c6c690533779d66bb81fa33f399c212b
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/research_community.py
    sha256: 5ff871f8ad791eecd86a006a535d9239c9775cdc0c69fe15bf4272efb87a64ec
    role: context
  - path: scripts/research_community_edison.py
    sha256: e0e46c3f54db793b2275a69a2ccd790ebe79cda7548a4bcf08d114343dc4341b
    role: context
  - path: src/communitymech/schema/communitymech.yaml
    sha256: e5a87e5367609334ec0d6361f6ddafbe6bc4a1f7d93e5264c64688c28325910f
    role: context
  - path: templates/community_causal_graph_research.md
    sha256: a5fd1ac7eabee13b89774dbb40b77db9f878bc142a46622ae11ce643f6f50d03
    role: target
  - path: tests/test_research_community.py
    sha256: 2ee7dbb53aaaec8fbcc6f549b38d438ce9e0e0e69eb36082b373112e022f47c8
    role: context
  snapshot_id: review-provenance/20261014-batch131-inputs
targets:
- target_id: causal-template
  path: templates/community_causal_graph_research.md
  label: Causal research prompt
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: templates/community_causal_graph_research.md
    role: maintained research prompt
- target_id: CommunityMech:000054
  path: kb/communities/Phormidium_Alkaline_Consortium.yaml
  label: Phormidium alkaline consortium
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Phormidium_Alkaline_Consortium.yaml
    role: canonical record
scope:
  description: One maintained prompt plus the current Phormidium graph and source-backed
    extension handoff.
  selection: Next needs_research record and the shared prompt used for its dry run.
  coverage: partial
  population_size: 462
  reviewed_target_ids:
  - causal-template
  - CommunityMech:000054
  exclusions:
  - target: Other 461 corpus records
    reason: Preservation/structural census only; not a new scientific review.
  - target: Phormidium non-graph assertions and whole-record certification
    reason: 'Known broader scope is tracked by #1701 and is not resolved by this handoff.'
checks:
- check_id: final-focused-tests
  name: final-focused-tests
  status: passed
  required: true
  summary: 25 focused tests pass, including the shared render path, capture/provenance
    tests and review contract tests; 12 dependency deprecation warnings remain.
  command: .venv/bin/python -m pytest tests/test_research_community.py tests/test_edison_capture_sidecar_provenance.py
    tests/test_enrich_edison_response_provenance.py tests/test_record_review_contract.py
    --no-cov -q
  exit_code: 0
  target_ids:
  - causal-template
  - CommunityMech:000054
  evidence_ids:
  - final-focused-tests
- check_id: lint-formatted
  name: lint-formatted
  status: passed
  required: true
  summary: Black, Ruff and mypy pass after the retained first lint failure was corrected.
  command: just --no-dotenv lint
  exit_code: 0
  target_ids:
  - causal-template
  evidence_ids:
  - lint-formatted
- check_id: corrected-phormidium-dry-run
  name: corrected-phormidium-dry-run
  status: passed
  required: true
  summary: The maintained one-community dry run succeeds with a 17518-character query.
    No authentication or Edison job was submitted; an SDK public model-cost lookup
    failed and used its fallback.
  command: .venv/bin/python scripts/research_community_edison.py --target CommunityMech:000054
    --template templates/community_causal_graph_research.md --label causal --out-dir
    research/causal-batch131/phormidium-corrected --dry-run
  exit_code: 0
  target_ids:
  - causal-template
  - CommunityMech:000054
  evidence_ids:
  - corrected-phormidium-dry-run
- check_id: source-replay
  name: source-replay
  status: passed
  required: true
  summary: Six source file hashes, selected table observations, all 462 canonical
    record hashes and unchanged 57 network warnings replay successfully. Discovery
    includes ignored files.
  command: .venv/bin/python reports/causal_graph_review/20261014-batch131/verify_sources.py
  exit_code: 0
  target_ids:
  - CommunityMech:000054
  evidence_ids:
  - source-replay
- check_id: docs-current
  name: docs-current
  status: passed
  required: true
  summary: The native generated-docs currency check passes without generated changes.
  command: just --no-dotenv check-docs-current
  exit_code: 0
  target_ids:
  - causal-template
  - CommunityMech:000054
  evidence_ids:
  - docs-current
- check_id: before-bundle-check
  name: before-bundle-check
  status: passed
  required: true
  summary: The before bundle and 20 earlier structured bundles validate against the
    pre-change main base.
  command: .venv/bin/python scripts/record_review.py check --base ec5e6468b74e874f5474c52d1825fa91a0b595b7
  exit_code: 0
  target_ids:
  - causal-template
  evidence_ids:
  - before-bundle-check
- check_id: network-zero-warning
  name: Native network zero-warning diagnostic
  status: failed
  required: false
  summary: Actual exit 1 with 57 existing DISCONNECTED/UNKNOWN_TARGET warnings, identical
    to batch130. No error-severity findings; do not claim a zero-warning pass.
  command: just --no-dotenv audit-network-json
  exit_code: 1
  target_ids:
  - CommunityMech:000054
  evidence_ids:
  - source-replay
- check_id: extension-research
  name: Required one-community extension research
  status: unavailable
  required: true
  summary: Spending is authorized but no inherited Edison/FutureHouse credential is
    available. No credential values or dotenv file inspected. No provider submission
    occurred; explicit primary-only substitution authorization is pending.
  target_ids:
  - CommunityMech:000054
  evidence_ids:
  - handoff
  - corrected-phormidium-dry-run
evidence:
- evidence_id: hydrogen
  kind: primary_source
  reference: PMID:16347751
  locator: https://pubmed.ncbi.nlm.nih.gov/16347751/ ; Abstract
  accessed_at: '2026-10-14T23:53:18.314795Z'
  support: supports
  summary: Primary experimental abstract reports hydrogen inhibition of syntrophic
    butyrate conversion and dependence on product removal. It supports the direction
    of the illustration, not Phormidium biology.
- evidence_id: prompt
  kind: record_content
  reference: templates/community_causal_graph_research.md
  locator: Community context boundary and Causal edges example
  accessed_at: '2026-10-14T23:53:18.314795Z'
  support: supports
  summary: The maintained prompt now attributes lowered hydrogen partial pressure
    to consumption, labels the example illustrative, and requires checking record
    claims against primary evidence.
- evidence_id: before
  kind: prior_review
  reference: reviews/structured/20261014T234638Z-causal-prompt-before/review.yaml
  locator: finding hydrogen-direction
  accessed_at: '2026-10-14T23:53:18.314795Z'
  support: context_only
  summary: Immutable historical finding at the original main commit; lineage is explicitly
    retained.
- evidence_id: phormidium
  kind: primary_source
  reference: doi:10.3389/fmicb.2022.780346
  locator: reports/causal_graph_review/sources/20261014-phormidium-batch131/manifest.json
    ; Introduction, Methods, Results/Discussion, Figure 3 and 4 pixels, selected Table
    S3/S4 cells
  accessed_at: '2026-10-14T23:53:18.314795Z'
  support: partial
  summary: Main text, figure pixels and selected supplement cells support bounded
    carbon assimilation and predicted niches; four source discrepancies constrain
    new MAG-specific or precisely timed claims. Table S2 headers only, not all taxonomic
    rows, were inspected.
- evidence_id: handoff
  kind: record_content
  reference: reports/causal_graph_review/sources/20261014-phormidium-batch131/assessment.yaml
  locator: current_graph, extension_candidates, source_discrepancies, verified_coverage
  accessed_at: '2026-10-14T23:53:18.314795Z'
  support: supports
  summary: Per-node and arrow retention reasons, seven candidate niches, exact source
    cells and four conflicts are preserved. This is a research handoff, not completed
    graph curation.
- evidence_id: record
  kind: record_content
  reference: kb/communities/Phormidium_Alkaline_Consortium.yaml
  locator: ecological_interactions and related knowledge-gap Discussion
  accessed_at: '2026-10-14T23:53:18.314795Z'
  support: supports
  summary: 'All four current nodes and the single donor-to-heterotroph arrow were
    read. Source taxon is Ca. Phormidium alkaliphilum; the major recipients are MAG34
    and MAG57, with broad canonical grounding explicitly bounded. Non-graph claims
    tracked by #1701 are not certified.'
- evidence_id: final-focused-tests
  kind: validation
  reference: reports/causal_graph_review/20261014-batch131/final-focused-tests.json
  accessed_at: '2026-10-14T23:53:18.314795Z'
  support: supports
  summary: 25 focused tests pass, including the shared render path, capture/provenance
    tests and review contract tests; 12 dependency deprecation warnings remain.
- evidence_id: lint-formatted
  kind: validation
  reference: reports/causal_graph_review/20261014-batch131/lint-formatted.json
  accessed_at: '2026-10-14T23:53:18.314795Z'
  support: supports
  summary: Black, Ruff and mypy pass after the retained first lint failure was corrected.
- evidence_id: corrected-phormidium-dry-run
  kind: validation
  reference: reports/causal_graph_review/20261014-batch131/corrected-phormidium-dry-run.json
  accessed_at: '2026-10-14T23:53:18.314795Z'
  support: supports
  summary: The maintained one-community dry run succeeds with a 17518-character query.
    No authentication or Edison job was submitted; an SDK public model-cost lookup
    failed and used its fallback.
- evidence_id: source-replay
  kind: validation
  reference: reports/causal_graph_review/20261014-batch131/source-replay.json
  accessed_at: '2026-10-14T23:53:18.314795Z'
  support: supports
  summary: Six source file hashes, selected table observations, all 462 canonical
    record hashes and unchanged 57 network warnings replay successfully. Discovery
    includes ignored files.
- evidence_id: docs-current
  kind: validation
  reference: reports/causal_graph_review/20261014-batch131/docs-current.json
  accessed_at: '2026-10-14T23:53:18.314795Z'
  support: supports
  summary: The native generated-docs currency check passes without generated changes.
- evidence_id: before-bundle-check
  kind: validation
  reference: reports/causal_graph_review/20261014-batch131/before-bundle-check.json
  accessed_at: '2026-10-14T23:53:18.314795Z'
  support: supports
  summary: The before bundle and 20 earlier structured bundles validate against the
    pre-change main base.
assessments:
- assessment_id: prompt-fix
  area: graph
  topic: Corrected causal direction and evidence boundaries
  outcome: supported
  summary: The corrected illustrative direction agrees with the primary study, while
    measured effects, predictions and hypotheses remain distinct from unverified record
    context. Render tests reject the original example and preserve both target contexts.
  target_ids:
  - causal-template
  evidence_ids:
  - hydrogen
  - prompt
  - final-focused-tests
  - corrected-phormidium-dry-run
- assessment_id: node-0
  area: graph
  topic: Photosynthetic CO2 Fixation
  outcome: supported
  summary: Figure 4 and the protein/SIP Results support cyanobacterial assimilation
    of supplied inorganic-carbon label. No inference that each proposed organic-carbon
    release route was measured.
  target_ids:
  - CommunityMech:000054
  evidence_ids:
  - phormidium
  - handoff
  - record
- assessment_id: node-1
  area: graph
  topic: Carbon Transfer to Heterotrophs
  outcome: supported
  summary: Figure 4 and Table S4 show the strongest heterotrophic peptide coverage
    for MAG34 and MAG57. Label incorporation is not a compound-specific transfer assay
    or proof of nutrient return.
  target_ids:
  - CommunityMech:000054
  evidence_ids:
  - phormidium
  - handoff
  - record
- assessment_id: node-2
  area: graph
  topic: Proposed Cyanobacterial Polymer Use by Verrucomicrobiota
  outcome: supported
  summary: Figure 3 and the Results assign hydrolase/sulfatase gene capacity to four
    MAGs. Capacity and weak isotope signals do not isolate sulfated polymers as the
    exchanged substrate.
  target_ids:
  - CommunityMech:000054
  evidence_ids:
  - phormidium
  - handoff
  - record
- assessment_id: node-3
  area: graph
  topic: Alphaproteobacterial Heterotrophic Carbon Use
  outcome: supported
  summary: Figure 4 and Table S4 retain a low-peptide MAG58 signal; Figure 3 separates
    predicted phototrophy. No class-wide reciprocal vitamin, siderophore, nitrogen
    or protection service is established.
  target_ids:
  - CommunityMech:000054
  evidence_ids:
  - phormidium
  - handoff
  - record
- assessment_id: arrow
  area: graph
  topic: Photosynthetic carbon input to heterotrophic incorporation
  outcome: supported
  summary: Retain the existing arrow from Photosynthetic CO2 Fixation to Carbon Transfer
    to Heterotrophs. In vitro bicarbonate protein/SIP supports this direction; it
    does not identify exchanged compounds, exact release routes, nutrient return or
    a precisely timed trophic cascade.
  target_ids:
  - CommunityMech:000054
  evidence_ids:
  - phormidium
  - handoff
  - record
- assessment_id: extension-gap
  area: completeness
  topic: Unfinished niche coverage and MAG-level source reconciliation
  outcome: concern
  summary: The primary paper describes seven candidate niches beyond the sparse representation.
    New nodes require qualified gene-based versus experimental scope, participant
    reconciliation and source-conflict disposition. MAG58 almA, MAG57 alkB, late SIP
    times and the cyanobacterial peptide total disagree across source representations;
    they are constraints, not four new canonical defects.
  target_ids:
  - CommunityMech:000054
  evidence_ids:
  - phormidium
  - handoff
  - record
  - source-replay
findings:
- finding_id: hydrogen-direction
  issue_key: communitymech-2007-hydrogen-direction
  category: graph
  severity: major
  status: resolved
  certainty: confirmed
  title: Shared prompt reverses hydrogen-mediated facilitation
  description: The old example assigned reduced hydrogen partial pressure to production
    and could bias research directions.
  target_ids:
  - causal-template
  field_paths:
  - Causal edges / causal link example
  evidence_ids:
  - hydrogen
  - prompt
  - before
  - final-focused-tests
  rule_id: causal-research-direction
  native_severity: P2
  normalization_reason: Systematic scientific-direction error in a shared research
    prompt.
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: templates/community_causal_graph_research.md
    role: maintained research prompt
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/2007
  disposition_reason: Consumption-to-oxidation direction is corrected; illustration
    and target evidence are explicitly separate, and record context must be checked.
    New render tests failed against the original and pass against the repaired template.
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261014T234638Z-causal-prompt-before
    finding_id: hydrogen-direction
- finding_id: phormidium-coverage
  issue_key: communitymech-1699-coverage
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Phormidium niche coverage remains incomplete
  description: The bounded four-node graph does not yet represent the source's other
    proposed ecological niches. Source conflicts and MAG-level participant reconciliation
    must be assessed before adding supported structure; a connected graph is not itself
    the acceptance criterion.
  target_ids:
  - CommunityMech:000054
  field_paths:
  - ecological_interactions
  - discussions / graph extension knowledge gap
  evidence_ids:
  - phormidium
  - handoff
  - record
  rule_id: causal-graph-evidence-coverage
  native_severity: P2
  normalization_reason: Material missing evidence-backed graph coverage, already tracked
    as needs_research; no new unsupported edge is alleged.
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Phormidium_Alkaline_Consortium.yaml
    role: canonical record
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/1699
actions:
- action_id: extend-phormidium
  description: Complete authorized one-community research, reconcile MAG/source discrepancies
    and curate only supported graph structure.
  finding_ids:
  - phormidium-coverage
  target_ids:
  - CommunityMech:000054
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Phormidium_Alkaline_Consortium.yaml
    role: canonical record
  acceptance_checks:
  - Obtain the one-community Edison research report required by the invoked skill,
    or explicit authorization to use direct-primary-source research in its place.
  - Keep the corrected prompt and explicit warning about non-graph context claims
    tracked in issue 1701.
  - Resolve MAG-level participant mapping against source taxonomy and canonical identifiers
    without transferring related-species phenotypes.
  - Verify exact snippets and keep supplemental evidence separate from article caches.
  - Apply only supported nodes/arrows with guarded writes, append-only history, validators,
    generated-doc checks and a successor review.
limitations:
- Partial source-based self-review, not independent approval or whole-record certification.
  All 54 needs_research statuses remain unchanged.
- No Edison job was submitted. Spend authorization exists but inherited credentials
  do not; no dotenv or credential values were inspected. Primary-only substitution
  authorization is pending.
- Read spans are bounded in the source manifest. Full Table S2 classification reconciliation,
  supplementary PDF, raw data and proposed extension remain unreviewed.
- Blank annotation cells are not proof of gene absence; individual annotations do
  not automatically meet figure pathway-completeness criteria. Peptide counts are
  sampling coverage, not biomass or exchange flux.
- The source's functional-redundancy explanation is not an isolated causal perturbation.
  Source disagreements are preserved rather than silently reconciled.
- All 462 canonical records, reference caches and histories remain unchanged. Supplements
  are retained separately, not inserted into the canonical article cache.
- Native whole-record completeness and validation-quality metrics are not computed
  for this scoped prompt/research assessment. No canonical validation/status promotion
  is claimed.
- The network zero-warning diagnostic still exits 1 for 57 unchanged warnings. The
  replay checks preservation and structural error absence, not semantic completeness.
- The intentionally failing old-template regression and first lint failure remain
  preserved as historical receipts, not final passes.
- Remote CI and merge-queue checks have not yet completed at this snapshot; publication
  must respect required checks.
links:
- https://github.com/CultureBotAI/CommunityMech/issues/2007
- https://github.com/CultureBotAI/CommunityMech/issues/1699
- https://github.com/CultureBotAI/CommunityMech/issues/1701
- https://github.com/CultureBotAI/CommunityMech/tree/review-provenance/20261014-batch131-inputs
tags:
- causal-graphs
- batch131
- self-review
- partial-research
```
