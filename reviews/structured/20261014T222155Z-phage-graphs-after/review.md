# Final pending phage graphs: scoped post-repair scientific review

- Review: 20261014T222155Z-phage-graphs-after
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-14T22:21:55.727208Z
- Finished UTC: 2026-10-14T22:21:55.727208Z
- Reviewer: codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

All ten nodes and three existing arrows were assessed. The three Alseth findings are resolved by scoped typing, mediation and modeling repairs, plus an explicit phenotype-versus-sequenced-genotype qualification. PHA remains unchanged with five bounded nodes and no arrows. All 52 snippets match; 98 focused tests pass. This is self-review of two graphs, not independent approval or corpus completion.

## Scope And Provenance

Ten graph nodes and three arrows across the two inventory-pending records; related discussions and record description for consistency.

Selection: All two records pending in the freshly rebuilt full-corpus inventory.
Coverage: partial; 2 reviewed / 462 in the declared population.
Source: git_commit at Git base 4bfd8189823d06538423fdacc330cb443d05f66f.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000467 | kb/communities/Alseth_FourSpecies_Pathogen_Phage_Community.yaml | maintained | Alseth four-species phage community |
| CommunityMech:000468 | kb/communities/PHA_MixedCulture_Phage_Succession_Community.yaml | maintained | PHA mixed-culture phage succession community |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| final-alseth-schema | passed | True | CommunityMech:000467, CommunityMech:000468 | Actual command completed successfully on the final record hashes; see retained receipt. |
| final-alseth-strict | passed | True | CommunityMech:000467, CommunityMech:000468 | Actual command completed successfully on the final record hashes; see retained receipt. |
| final-alseth-terms | passed | True | CommunityMech:000467, CommunityMech:000468 | Actual command completed successfully on the final record hashes; see retained receipt. |
| final-alseth-references | passed | False | CommunityMech:000467, CommunityMech:000468 | CLI completed but reports Total checks: 0. It is not counted as excerpt validation; explicit plugin/full traversal and audit-snippets supply that coverage. |
| final-alseth-rank | passed | True | CommunityMech:000467, CommunityMech:000468 | Actual command completed successfully on the final record hashes; see retained receipt. |
| final-pha-schema | passed | True | CommunityMech:000467, CommunityMech:000468 | Actual command completed successfully on the final record hashes; see retained receipt. |
| final-pha-strict | passed | True | CommunityMech:000467, CommunityMech:000468 | Actual command completed successfully on the final record hashes; see retained receipt. |
| final-pha-terms | passed | True | CommunityMech:000467, CommunityMech:000468 | Actual command completed successfully on the final record hashes; see retained receipt. |
| final-pha-references | passed | False | CommunityMech:000467, CommunityMech:000468 | CLI completed but reports Total checks: 0. It is not counted as excerpt validation; explicit plugin/full traversal and audit-snippets supply that coverage. |
| final-pha-rank | passed | True | CommunityMech:000467, CommunityMech:000468 | Actual command completed successfully on the final record hashes; see retained receipt. |
| final-snippets-explicit | passed | True | CommunityMech:000467, CommunityMech:000468 | Explicit plugin checks 27 Alseth and 24 PHA fields; explicit traversal additionally checks the Alseth Discussion, totaling 28 and 24. Invented-quote mutation controls fail and immediate restorations pass; network access is forbidden. |
| final-history | passed | True | CommunityMech:000467, CommunityMech:000468 | Actual command completed successfully on the final record hashes; see retained receipt. |
| final-audit-snippets | passed | True | CommunityMech:000467, CommunityMech:000468 | Actual command completed successfully on the final record hashes; see retained receipt. |
| final-inventory | passed | True | CommunityMech:000467, CommunityMech:000468 | Ignored-inclusive inventory:462 records,1383 nodes,533 arrows;408 reviewed,54 needs_research,zero pending or stale; no structural defects or error-severity network findings. |
| final-network | failed | False | CommunityMech:000467, CommunityMech:000468 | Zero-warning command exits1 for 57 warnings (50 DISCONNECTED, 7 UNKNOWN_TARGET), byte-identical to baseline output. Required structural-error gate passes separately in final-inventory; no error-severity findings. |
| final-lint-corrected | passed | True | CommunityMech:000467, CommunityMech:000468 | Actual command completed successfully on the final record hashes; see retained receipt. |
| final-regression-complete | passed | True | CommunityMech:000467, CommunityMech:000468 | 98 tests passed, including mutation/control/restoration checks. Twelve dependency deprecation warnings remain. This is focused coverage, not the full CI suite. |
| final-preservation-replay | passed | True | CommunityMech:000467, CommunityMech:000468 | All 462 canonical records accounted for; only Alseth changed. Other461 records,927 tracked cache files and unrelated Alseth root blocks unchanged. |
| final-gen-html | passed | True | CommunityMech:000467, CommunityMech:000468 | Actual command completed successfully on the final record hashes; see retained receipt. |
| final-docs-current | passed | True | CommunityMech:000467, CommunityMech:000468 | Actual command completed successfully on the final record hashes; see retained receipt. |
| final-diff-check | passed | True | CommunityMech:000467, CommunityMech:000468 | Actual command completed successfully on the final record hashes; see retained receipt. |
| final-reviews-before | passed | True | CommunityMech:000467, CommunityMech:000468 | Actual command completed successfully on the final record hashes; see retained receipt. |

## Scientific And Domain Assessments

### Measured treatment effects versus mechanism and model claims

graph: supported. Targets: CommunityMech:000467.

Retained measured infection, competitive release, resistance and diversity observations with source-bounded types, PARTIAL mediation and computational model scope. Mutation terminology is explicitly phenotype-based, not sequenced genotype. Five nodes and three existing directions remain; no new topology.

### Observed turnover and explicitly modeled/predicted process context

graph: supported. Targets: CommunityMech:000468.

Retain the kill-the-winner hypothesis as partial, coupled turnover as association, SEM diversity/activity effects as modeled associations, AMG transcripts without a yield claim, and defense predictions without functional resistance claims. These qualified context nodes do not supply causal arrows; the graph remains arrow-free.

## Findings

### typing: Outcome and model nodes carry unsupported mechanistic types

major / resolved / confirmed; issue key: communitymech-2005-typing.

The diversity outcome is not another lytic infection; resistance-route observations and fitted-model failure do not establish reciprocal negative effects. Keep measured infection and competitive release, and omit inappropriate optional types.

Disposition: Unsupported optional COMPETITION and outcome LYTIC_INFECTION labels removed; genuine pairwise infection and competitive release retained. Regression mutations reject their reintroduction.

### mediation: Two arrows exceed their measured causal support

major / resolved / confirmed; issue key: communitymech-2005-mediation.

Receptor targeting is stated to cause the resistance route's fitness cost, and competitive release is stated to be the established diversity-maintaining mechanism. The source supports a partial cost explanation and joint treatment outcomes, not isolated necessary or sufficient mediation.

Disposition: Both affected arrows are now explicitly PARTIAL. Source-backed Discussion records unresolved mediation, while existing directions and positive treatment observations remain intact. Mutation checks reject causal overclaims.

### model-scope: Model failure and improved prediction are overgeneralized

major / resolved / confirmed; issue key: communitymech-2005-model-scope.

The record omits the phage-free condition on improved quantitative four-species prediction and turns failure of tested pairwise-fitted models into general non-reconstructibility. Retain the published computational observation without treating it as proof of one higher-order mechanism or an impossibility theorem.

Disposition: Node and root description distinguish tested-model failure from general impossibility, phage-free quantitative improvement from phage-present failure, and qualitative release prediction. New exact excerpts and computational modality are verified; mutations reject lost conditions and fabricated evidence.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| alseth | PMID:38648198; Publisher Results: phage effects, resistance, competitive release and diversity; Figures 3-5 and 8-10 captions; modeling Results and Discussion | partial | Phage treatment altered dominance and diversity. The resistance-cost explanation is partial. Adding three-species data improved phage-free quantitative prediction; phage-present models retained quantitative failure despite qualitative release prediction. Caption text, not figure pixels, was inspected. |
| pha | PMID:40152616; Publisher Abstract; Results and Discussion: community overview, SEM/turnover, predicted host links/defenses and AMG expression; cached computational Methods | supports | The observational time series supports correlated turnover and modeled associations. Sequence-derived host links/defenses and AMG transcripts remain qualified predictions or observations, not experimentally established lysis, resistance or yield effects. |
| schema | src/communitymech/schema/communitymech.yaml; InteractionTypeEnum and EcologicalInteraction | supports | LYTIC_INFECTION requires virus-to-host infection; COMPETITION asserts reciprocal negative effects. The optional type need not be filled when neither applies. Community-level phenomena and explicitly bounded computational evidence can be represented without such a type. |
| records | reports/causal_graph_review/decisions/20261014-phage-graphs-batch130.yaml; All ten per-node decisions and three retained-arrow decisions; exact canonical hashes | supports | Each current node is covered exactly once with source locator, participants and modality. Alseth retains three directions with two PARTIAL mediation qualifications. PHA remains arrow-free and byte-identical. |
| methods-limit | PMID:38648198; Materials and methods: Evolution experiment, statement that receptor mutants were not sequenced | supports | The authors' receptor-mutant terminology is phenotype-based classification, not direct sequencing of the mutants in this study. The retained node and root summary now state this limit without changing the observed resistance outcome. |
| before | reviews/structured/20261014T215456Z-phage-graphs-before/review.yaml | supports | The immutable pre-repair review records the three original open findings. Exact input bytes are preserved in the before-provenance archive; the original report is not rewritten. |
| sources | reports/causal_graph_review/sources/20261014-phage-graphs-batch130.json | supports | Dated primary-source access scope and unchanged cache hashes. Relevant passages and captions, not figure pixels, all supplements or raw-data reanalysis. |
| gate-final-alseth-schema | reports/causal_graph_review/20261014-batch130/final-alseth-schema.json | supports | Actual command completed successfully on the final record hashes; see retained receipt. |
| gate-final-alseth-strict | reports/causal_graph_review/20261014-batch130/final-alseth-strict.json | supports | Actual command completed successfully on the final record hashes; see retained receipt. |
| gate-final-alseth-terms | reports/causal_graph_review/20261014-batch130/final-alseth-terms.json | supports | Actual command completed successfully on the final record hashes; see retained receipt. |
| gate-final-alseth-references | reports/causal_graph_review/20261014-batch130/final-alseth-references.json | context_only | CLI completed but reports Total checks: 0. It is not counted as excerpt validation; explicit plugin/full traversal and audit-snippets supply that coverage. |
| gate-final-alseth-rank | reports/causal_graph_review/20261014-batch130/final-alseth-rank.json | supports | Actual command completed successfully on the final record hashes; see retained receipt. |
| gate-final-pha-schema | reports/causal_graph_review/20261014-batch130/final-pha-schema.json | supports | Actual command completed successfully on the final record hashes; see retained receipt. |
| gate-final-pha-strict | reports/causal_graph_review/20261014-batch130/final-pha-strict.json | supports | Actual command completed successfully on the final record hashes; see retained receipt. |
| gate-final-pha-terms | reports/causal_graph_review/20261014-batch130/final-pha-terms.json | supports | Actual command completed successfully on the final record hashes; see retained receipt. |
| gate-final-pha-references | reports/causal_graph_review/20261014-batch130/final-pha-references.json | context_only | CLI completed but reports Total checks: 0. It is not counted as excerpt validation; explicit plugin/full traversal and audit-snippets supply that coverage. |
| gate-final-pha-rank | reports/causal_graph_review/20261014-batch130/final-pha-rank.json | supports | Actual command completed successfully on the final record hashes; see retained receipt. |
| gate-final-snippets-explicit | reports/causal_graph_review/20261014-batch130/final-snippets-explicit.json | supports | Explicit plugin checks 27 Alseth and 24 PHA fields; explicit traversal additionally checks the Alseth Discussion, totaling 28 and 24. Invented-quote mutation controls fail and immediate restorations pass; network access is forbidden. |
| gate-final-history | reports/causal_graph_review/20261014-batch130/final-history.json | supports | Actual command completed successfully on the final record hashes; see retained receipt. |
| gate-final-audit-snippets | reports/causal_graph_review/20261014-batch130/final-audit-snippets.json | supports | Actual command completed successfully on the final record hashes; see retained receipt. |
| gate-final-inventory | reports/causal_graph_review/20261014-batch130/final-inventory.json | supports | Ignored-inclusive inventory:462 records,1383 nodes,533 arrows;408 reviewed,54 needs_research,zero pending or stale; no structural defects or error-severity network findings. |
| gate-final-network | reports/causal_graph_review/20261014-batch130/final-network.json | context_only | Zero-warning command exits1 for 57 warnings (50 DISCONNECTED, 7 UNKNOWN_TARGET), byte-identical to baseline output. Required structural-error gate passes separately in final-inventory; no error-severity findings. |
| gate-final-lint-corrected | reports/causal_graph_review/20261014-batch130/final-lint-corrected.json | supports | Actual command completed successfully on the final record hashes; see retained receipt. |
| gate-final-regression-complete | reports/causal_graph_review/20261014-batch130/final-regression-complete.json | supports | 98 tests passed, including mutation/control/restoration checks. Twelve dependency deprecation warnings remain. This is focused coverage, not the full CI suite. |
| gate-final-preservation-replay | reports/causal_graph_review/20261014-batch130/final-preservation-replay.json | supports | All 462 canonical records accounted for; only Alseth changed. Other461 records,927 tracked cache files and unrelated Alseth root blocks unchanged. |
| gate-final-gen-html | reports/causal_graph_review/20261014-batch130/final-gen-html.json | supports | Actual command completed successfully on the final record hashes; see retained receipt. |
| gate-final-docs-current | reports/causal_graph_review/20261014-batch130/final-docs-current.json | supports | Actual command completed successfully on the final record hashes; see retained receipt. |
| gate-final-diff-check | reports/causal_graph_review/20261014-batch130/final-diff-check.json | supports | Actual command completed successfully on the final record hashes; see retained receipt. |
| gate-final-reviews-before | reports/causal_graph_review/20261014-batch130/final-reviews-before.json | supports | Actual command completed successfully on the final record hashes; see retained receipt. |

## Limits And Additional Notes

- Source-based self-adversarial review, not independent approval or whole-record certification.
- Whole records and relevant primary Results/Discussion/Methods and captions inspected; figure pixels, all supplements, raw data and executable models not reanalyzed.
- Other 460 records receive structural census and preservation checks, not new semantic review; 54 needs_research records remain unresolved.
- Native reference CLI reports zero checks. Explicit plugin invocation checks 27 Alseth and 24 PHA fields; full excerpt traversal additionally checks the Alseth Discussion, totaling 28 and 24. Lexical matches do not prove causal support.
- Discussion traversal gap #476 is compensated locally, not fixed. No schema, validator or threshold is weakened.
- No new topology, provider submission, biological protocol or optimization instruction is introduced.
- Network zero-warning audit remains failed with its actual exit1 and unchanged57 warnings; required structural-error gate passes. No finding is hidden by changing gate thresholds.
- Native whole-record completeness and validation-quality scores are not computed for this graph-only assessment.
- The first lint run failed on test formatting; the retained corrected lint and regression receipts pass. Earlier failed/interim receipts remain historical, not counted as final success.
- Full remote CI and merge-queue checks are not yet complete at this scientific-review snapshot. Publication must wait for required checks; this verdict does not authorize bypass.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T222155Z-phage-graphs-after
kind: batch
repository: CultureBotAI/CommunityMech
title: 'Final pending phage graphs: scoped post-repair scientific review'
started_at: '2026-10-14T22:21:55.727208Z'
finished_at: '2026-10-14T22:21:55.727208Z'
reviewer:
  identity: codex
  kind: agent
  independence: self_review
  independence_basis: The same agent implemented and adversarially checked these repairs;
    no independent reviewer approval is claimed.
skill: communitymech-causal-graphs
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: All ten nodes and three existing arrows were assessed. The three Alseth findings
  are resolved by scoped typing, mediation and modeling repairs, plus an explicit
  phenotype-versus-sequenced-genotype qualification. PHA remains unchanged with five
  bounded nodes and no arrows. All 52 snippets match; 98 focused tests pass. This
  is self-review of two graphs, not independent approval or corpus completion.
source:
  git_revision: 4bfd8189823d06538423fdacc330cb443d05f66f
  state: git_commit
  inputs:
  - path: docs/browser.html
    sha256: d87a5e0cd5eefc7bd4f3487b2eb23ddbaff4d7e4edf38ecf8cf93a4a30f678c7
    role: context
  - path: docs/communities/Alseth_FourSpecies_Pathogen_Phage_Community.html
    sha256: fec8974bcf8eaca5fcb69c18b3fff268cfa6eabb019b80c89ef655795b618908
    role: context
  - path: history/records/Alseth_FourSpecies_Pathogen_Phage_Community/2026-10-14T215856Z-codex-b473e9.yaml
    sha256: cbace6e1715cae5ccaf1963ddb7df5a6414b1f45dd246261d7b8512eccaac690
    role: context
  - path: history/records/Alseth_FourSpecies_Pathogen_Phage_Community/2026-10-14T220730Z-codex-dda3a4.yaml
    sha256: 234c0eba26f62435864b88f95a798dd02f7c158ac364f332f66302e8508827c2
    role: context
  - path: kb/communities/Alseth_FourSpecies_Pathogen_Phage_Community.yaml
    sha256: cef1f3c47035ef336cb809456b25a185e0397bb9f0a16c492becdb5b371529f5
    role: target
  - path: kb/communities/PHA_MixedCulture_Phage_Succession_Community.yaml
    sha256: aebd6497b6d5a6f49e9e9ef956d4ec0847960acc0fd2413dce5e0960ed748488
    role: target
  - path: references_cache/PMID_38648198.txt
    sha256: babc54ddb60c3ed882e817d1970ff9c7ba24069b0b06d67730e12eb974b58df3
    role: context
  - path: references_cache/PMID_40152616.txt
    sha256: 65e30e4f8aed4b1c7cde1fb173376207bbf90d92306c7f59997fd41bfeddbe8b
    role: context
  - path: reports/causal_graph_review/20261014-batch130/baseline-inventory.json
    sha256: 8473701ff2c1eeff60c3133290cb5af80ea53d1b3e74866cca531d2e2a8b3034
    role: context
  - path: reports/causal_graph_review/20261014-batch130/baseline-network.json
    sha256: bf6a0d75f159686d9116c33ce7b45c565c527f494994e936889f200d052d401d
    role: context
  - path: reports/causal_graph_review/20261014-batch130/before-provenance.json
    sha256: e529d336b5b009c4cb767fd5951f218a0370dac700c06379ccfe431fd8427976
    role: context
  - path: reports/causal_graph_review/20261014-batch130/check_preservation.py
    sha256: 1536b1b5aa8b9d1d9dc52b7e99082c68b127e045cfd763fe1bf69a74bee205ce
    role: context
  - path: reports/causal_graph_review/20261014-batch130/check_snippets.py
    sha256: 3e317b1f90cab3c6e97bf4a3127b1b232414b6ff70c09a377f3dcbf0afecff5f
    role: context
  - path: reports/causal_graph_review/20261014-batch130/final-alseth-rank.json
    sha256: 296703bb9fc31886b6d57a7aebe797b43de0587d6d1f984eea55bc0540d86392
    role: context
  - path: reports/causal_graph_review/20261014-batch130/final-alseth-references.json
    sha256: 1ca55e3e7cbee9d533bf05d14c2b2d0e2904ba62899434b6852de39b767cd8df
    role: context
  - path: reports/causal_graph_review/20261014-batch130/final-alseth-schema.json
    sha256: 691502f969c40c13d87d9e15271c999185f465cde44a662d88b5c00c1765f858
    role: context
  - path: reports/causal_graph_review/20261014-batch130/final-alseth-strict.json
    sha256: 52ae782a77c8d8513d540ba6ca123db3f8b8448a24cde6caa25ae4f2b741a574
    role: context
  - path: reports/causal_graph_review/20261014-batch130/final-alseth-terms.json
    sha256: 835fbe735408bb8ed88a0bdef45a4ab026bc8a4134bb48e5d480343265af5619
    role: context
  - path: reports/causal_graph_review/20261014-batch130/final-audit-snippets.json
    sha256: 6e37a425d9c571ee999b7066d1eef5d4b0226f9cd0d79096f0f5f4d50db2fcc6
    role: context
  - path: reports/causal_graph_review/20261014-batch130/final-diff-check.json
    sha256: ac2e7a8601a8cfd71759413653fa1fd2e6e8ff1217e67d305f6d34a403792f3b
    role: context
  - path: reports/causal_graph_review/20261014-batch130/final-docs-current.json
    sha256: 824a9d8391a7f64421b67ccc59a63796f2191eeb8f14c92d1ac747cadea9c2c8
    role: context
  - path: reports/causal_graph_review/20261014-batch130/final-gen-html.json
    sha256: 71d397ffae330a3e84c2c54d65b69b91d5459e4b582d571e025debed0ad580a6
    role: context
  - path: reports/causal_graph_review/20261014-batch130/final-history.json
    sha256: d573b5a7fbb1296a2334d89ba40ed01e120048565ea0157663970c5fff0d7363
    role: context
  - path: reports/causal_graph_review/20261014-batch130/final-inventory.json
    sha256: bfa6d6686bb16da489f5ce7cb9b5411f82edb00419590d90cf597e706c66584f
    role: context
  - path: reports/causal_graph_review/20261014-batch130/final-lint-corrected.json
    sha256: 25bc3b440997f36cdac0d60f39563a0c9a749c868c86b5edaab254fd53a8432d
    role: context
  - path: reports/causal_graph_review/20261014-batch130/final-network.json
    sha256: d77f31682218889018b9e0fa2fef83608e4af9f127d2c6414a5e288e75beaec5
    role: context
  - path: reports/causal_graph_review/20261014-batch130/final-pha-rank.json
    sha256: fdf14dfd2255edbb3cb16f7d4163cc7065601708affe1a844bf2445c37211795
    role: context
  - path: reports/causal_graph_review/20261014-batch130/final-pha-references.json
    sha256: ab9871dfbfc771a3c99dbca2782e43e40359b2d63e309b09e23f8abec21b1555
    role: context
  - path: reports/causal_graph_review/20261014-batch130/final-pha-schema.json
    sha256: 7df8c17ec521aeca53db9ac3d847846cc31ea79131e96a71873a9e20f56ea7ab
    role: context
  - path: reports/causal_graph_review/20261014-batch130/final-pha-strict.json
    sha256: ec88fdb7260e2d7b111548f38938b89f51ee7856b0ac863fc1ef7435e949b5eb
    role: context
  - path: reports/causal_graph_review/20261014-batch130/final-pha-terms.json
    sha256: 1bdafe0b6bc26c59409da5b5416f97579d7d8dcc77dd4904d14255ce7c87344d
    role: context
  - path: reports/causal_graph_review/20261014-batch130/final-preservation-replay.json
    sha256: 67489cf48e2f7343b48bdfd43ccf708593ca50fbce3be1bc337d46544a00e7a7
    role: context
  - path: reports/causal_graph_review/20261014-batch130/final-regression-complete.json
    sha256: dffcbdfcdd5ce6d87db62fd9b6ac15b23f85a41ae4e1c7fa8b81e2852de7644b
    role: context
  - path: reports/causal_graph_review/20261014-batch130/final-reviews-before.json
    sha256: d16e29e633c367034708a19cfa030efa2cdb59ff3e51c48a4ffea55d7296c6dc
    role: context
  - path: reports/causal_graph_review/20261014-batch130/final-snippets-explicit.json
    sha256: 60474ea0b5409b572c2a1610e44719a4742f62f4ba2cc6b18e31c65033ef37a9
    role: context
  - path: reports/causal_graph_review/build_inventory.py
    sha256: 5cb9aeb35b34b67077dddf434715d1ee9314f71130f9e165f5c41967180a9483
    role: context
  - path: reports/causal_graph_review/decisions/20261014-phage-graphs-batch130.yaml
    sha256: 88a433392f6b1ad7214280eb4d71f3fb55768f2803359afb0ee5490330bea785
    role: context
  - path: reports/causal_graph_review/inventory.tsv
    sha256: e826c14f14487a8feb7a4a54db7608881d112ff19d97c1df2332b81e70e43f7e
    role: context
  - path: reports/causal_graph_review/sources/20261014-phage-graphs-batch130.json
    sha256: 54714d5b8127649ca2a5cbcf969c789349de9136fc26e1857d63c67b98cbf55b
    role: context
  - path: reports/causal_graph_review/summary.json
    sha256: d4e452ae6d6b3a8c12a77274e08723406b5c97fb702a4df58d15c1e547e92819
    role: context
  - path: reviews/structured/20261014T215456Z-phage-graphs-before/review.md
    sha256: cc0f393e867950ec7af1c86289dc5d7d92df656559126b30a9a769d7c11289fc
    role: context
  - path: reviews/structured/20261014T215456Z-phage-graphs-before/review.yaml
    sha256: bfce598b4aa04606845c6068a618cf95f468d39cbe595f69942f1a02e619d013
    role: context
  - path: src/communitymech/schema/communitymech.yaml
    sha256: e5a87e5367609334ec0d6361f6ddafbe6bc4a1f7d93e5264c64688c28325910f
    role: context
  - path: src/communitymech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
  - path: tests/test_causal_review_batch130.py
    sha256: fc51ae1f93310f1317f78fbd11b7468b4ab6043bff4c577e8c52c1d96ac2c07b
    role: context
  - path: tests/test_phage_review_regressions.py
    sha256: 6b682e06de18099caa5142ed266b8c3c250ff8437c9caf2b2221225cbd80a9d6
    role: context
  snapshot_id: review-provenance/20261014-batch130-inputs
targets:
- target_id: CommunityMech:000467
  path: kb/communities/Alseth_FourSpecies_Pathogen_Phage_Community.yaml
  label: Alseth four-species phage community
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Alseth_FourSpecies_Pathogen_Phage_Community.yaml
    role: canonical_record
- target_id: CommunityMech:000468
  path: kb/communities/PHA_MixedCulture_Phage_Succession_Community.yaml
  label: PHA mixed-culture phage succession community
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/PHA_MixedCulture_Phage_Succession_Community.yaml
    role: canonical_record
scope:
  description: Ten graph nodes and three arrows across the two inventory-pending records;
    related discussions and record description for consistency.
  selection: All two records pending in the freshly rebuilt full-corpus inventory.
  coverage: partial
  population_size: 462
  reviewed_target_ids:
  - CommunityMech:000467
  - CommunityMech:000468
  exclusions:
  - target: Other 460 corpus records
    reason: Structural census only, not a new semantic review.
  - target: Non-graph assertions, raw data, model code, supplements and figure pixels
    reason: Read for context where available, not globally recertified or independently
      reanalyzed.
checks:
- check_id: final-alseth-schema
  name: final-alseth-schema
  status: passed
  required: true
  summary: Actual command completed successfully on the final record hashes; see retained
    receipt.
  command: just validate kb/communities/Alseth_FourSpecies_Pathogen_Phage_Community.yaml
  exit_code: 0
  target_ids:
  - CommunityMech:000467
  - CommunityMech:000468
  evidence_ids:
  - gate-final-alseth-schema
- check_id: final-alseth-strict
  name: final-alseth-strict
  status: passed
  required: true
  summary: Actual command completed successfully on the final record hashes; see retained
    receipt.
  command: just validate-strict kb/communities/Alseth_FourSpecies_Pathogen_Phage_Community.yaml
  exit_code: 0
  target_ids:
  - CommunityMech:000467
  - CommunityMech:000468
  evidence_ids:
  - gate-final-alseth-strict
- check_id: final-alseth-terms
  name: final-alseth-terms
  status: passed
  required: true
  summary: Actual command completed successfully on the final record hashes; see retained
    receipt.
  command: just validate-terms kb/communities/Alseth_FourSpecies_Pathogen_Phage_Community.yaml
  exit_code: 0
  target_ids:
  - CommunityMech:000467
  - CommunityMech:000468
  evidence_ids:
  - gate-final-alseth-terms
- check_id: final-alseth-references
  name: final-alseth-references
  status: passed
  required: false
  summary: 'CLI completed but reports Total checks: 0. It is not counted as excerpt
    validation; explicit plugin/full traversal and audit-snippets supply that coverage.'
  command: just validate-references-explained kb/communities/Alseth_FourSpecies_Pathogen_Phage_Community.yaml
  exit_code: 0
  target_ids:
  - CommunityMech:000467
  - CommunityMech:000468
  evidence_ids:
  - gate-final-alseth-references
- check_id: final-alseth-rank
  name: final-alseth-rank
  status: passed
  required: true
  summary: Actual command completed successfully on the final record hashes; see retained
    receipt.
  command: just rank-causal-graphs kb/communities/Alseth_FourSpecies_Pathogen_Phage_Community.yaml
  exit_code: 0
  target_ids:
  - CommunityMech:000467
  - CommunityMech:000468
  evidence_ids:
  - gate-final-alseth-rank
- check_id: final-pha-schema
  name: final-pha-schema
  status: passed
  required: true
  summary: Actual command completed successfully on the final record hashes; see retained
    receipt.
  command: just validate kb/communities/PHA_MixedCulture_Phage_Succession_Community.yaml
  exit_code: 0
  target_ids:
  - CommunityMech:000467
  - CommunityMech:000468
  evidence_ids:
  - gate-final-pha-schema
- check_id: final-pha-strict
  name: final-pha-strict
  status: passed
  required: true
  summary: Actual command completed successfully on the final record hashes; see retained
    receipt.
  command: just validate-strict kb/communities/PHA_MixedCulture_Phage_Succession_Community.yaml
  exit_code: 0
  target_ids:
  - CommunityMech:000467
  - CommunityMech:000468
  evidence_ids:
  - gate-final-pha-strict
- check_id: final-pha-terms
  name: final-pha-terms
  status: passed
  required: true
  summary: Actual command completed successfully on the final record hashes; see retained
    receipt.
  command: just validate-terms kb/communities/PHA_MixedCulture_Phage_Succession_Community.yaml
  exit_code: 0
  target_ids:
  - CommunityMech:000467
  - CommunityMech:000468
  evidence_ids:
  - gate-final-pha-terms
- check_id: final-pha-references
  name: final-pha-references
  status: passed
  required: false
  summary: 'CLI completed but reports Total checks: 0. It is not counted as excerpt
    validation; explicit plugin/full traversal and audit-snippets supply that coverage.'
  command: just validate-references-explained kb/communities/PHA_MixedCulture_Phage_Succession_Community.yaml
  exit_code: 0
  target_ids:
  - CommunityMech:000467
  - CommunityMech:000468
  evidence_ids:
  - gate-final-pha-references
- check_id: final-pha-rank
  name: final-pha-rank
  status: passed
  required: true
  summary: Actual command completed successfully on the final record hashes; see retained
    receipt.
  command: just rank-causal-graphs kb/communities/PHA_MixedCulture_Phage_Succession_Community.yaml
  exit_code: 0
  target_ids:
  - CommunityMech:000467
  - CommunityMech:000468
  evidence_ids:
  - gate-final-pha-rank
- check_id: final-snippets-explicit
  name: final-snippets-explicit
  status: passed
  required: true
  summary: Explicit plugin checks 27 Alseth and 24 PHA fields; explicit traversal
    additionally checks the Alseth Discussion, totaling 28 and 24. Invented-quote
    mutation controls fail and immediate restorations pass; network access is forbidden.
  command: .venv/bin/python reports/causal_graph_review/20261014-batch130/check_snippets.py
  exit_code: 0
  target_ids:
  - CommunityMech:000467
  - CommunityMech:000468
  evidence_ids:
  - gate-final-snippets-explicit
- check_id: final-history
  name: final-history
  status: passed
  required: true
  summary: Actual command completed successfully on the final record hashes; see retained
    receipt.
  command: just validate-history history/records/Alseth_FourSpecies_Pathogen_Phage_Community
  exit_code: 0
  target_ids:
  - CommunityMech:000467
  - CommunityMech:000468
  evidence_ids:
  - gate-final-history
- check_id: final-audit-snippets
  name: final-audit-snippets
  status: passed
  required: true
  summary: Actual command completed successfully on the final record hashes; see retained
    receipt.
  command: just audit-snippets kb/communities/Alseth_FourSpecies_Pathogen_Phage_Community.yaml
    kb/communities/PHA_MixedCulture_Phage_Succession_Community.yaml --list-mismatch
    --list-nocontent --list-rendering --list-assembled
  exit_code: 0
  target_ids:
  - CommunityMech:000467
  - CommunityMech:000468
  evidence_ids:
  - gate-final-audit-snippets
- check_id: final-inventory
  name: final-inventory
  status: passed
  required: true
  summary: Ignored-inclusive inventory:462 records,1383 nodes,533 arrows;408 reviewed,54
    needs_research,zero pending or stale; no structural defects or error-severity
    network findings.
  command: .venv/bin/python reports/causal_graph_review/build_inventory.py
  exit_code: 0
  target_ids:
  - CommunityMech:000467
  - CommunityMech:000468
  evidence_ids:
  - gate-final-inventory
- check_id: final-network
  name: final-network
  status: failed
  required: false
  summary: Zero-warning command exits1 for 57 warnings (50 DISCONNECTED, 7 UNKNOWN_TARGET),
    byte-identical to baseline output. Required structural-error gate passes separately
    in final-inventory; no error-severity findings.
  command: just audit-network-json
  exit_code: 1
  target_ids:
  - CommunityMech:000467
  - CommunityMech:000468
  evidence_ids:
  - gate-final-network
- check_id: final-lint-corrected
  name: final-lint-corrected
  status: passed
  required: true
  summary: Actual command completed successfully on the final record hashes; see retained
    receipt.
  command: just lint
  exit_code: 0
  target_ids:
  - CommunityMech:000467
  - CommunityMech:000468
  evidence_ids:
  - gate-final-lint-corrected
- check_id: final-regression-complete
  name: final-regression-complete
  status: passed
  required: true
  summary: 98 tests passed, including mutation/control/restoration checks. Twelve
    dependency deprecation warnings remain. This is focused coverage, not the full
    CI suite.
  command: .venv/bin/pytest tests/test_causal_review_batch130.py tests/test_phage_review_regressions.py
    tests/test_causal_review_inventory.py tests/test_participating_taxa.py tests/test_network_palette.py
    tests/test_reference_validator_actually_validates.py -q --no-cov
  exit_code: 0
  target_ids:
  - CommunityMech:000467
  - CommunityMech:000468
  evidence_ids:
  - gate-final-regression-complete
- check_id: final-preservation-replay
  name: final-preservation-replay
  status: passed
  required: true
  summary: All 462 canonical records accounted for; only Alseth changed. Other461
    records,927 tracked cache files and unrelated Alseth root blocks unchanged.
  command: .venv/bin/python reports/causal_graph_review/20261014-batch130/check_preservation.py
  exit_code: 0
  target_ids:
  - CommunityMech:000467
  - CommunityMech:000468
  evidence_ids:
  - gate-final-preservation-replay
- check_id: final-gen-html
  name: final-gen-html
  status: passed
  required: true
  summary: Actual command completed successfully on the final record hashes; see retained
    receipt.
  command: just gen-html
  exit_code: 0
  target_ids:
  - CommunityMech:000467
  - CommunityMech:000468
  evidence_ids:
  - gate-final-gen-html
- check_id: final-docs-current
  name: final-docs-current
  status: passed
  required: true
  summary: Actual command completed successfully on the final record hashes; see retained
    receipt.
  command: just check-docs-current
  exit_code: 0
  target_ids:
  - CommunityMech:000467
  - CommunityMech:000468
  evidence_ids:
  - gate-final-docs-current
- check_id: final-diff-check
  name: final-diff-check
  status: passed
  required: true
  summary: Actual command completed successfully on the final record hashes; see retained
    receipt.
  command: git diff --check
  exit_code: 0
  target_ids:
  - CommunityMech:000467
  - CommunityMech:000468
  evidence_ids:
  - gate-final-diff-check
- check_id: final-reviews-before
  name: final-reviews-before
  status: passed
  required: true
  summary: Actual command completed successfully on the final record hashes; see retained
    receipt.
  command: .venv/bin/python scripts/record_review.py check --base b68d71e702200cd7ce9afdec001705dc8b0890fd
  exit_code: 0
  target_ids:
  - CommunityMech:000467
  - CommunityMech:000468
  evidence_ids:
  - gate-final-reviews-before
evidence:
- evidence_id: alseth
  kind: primary_source
  reference: PMID:38648198
  locator: 'Publisher Results: phage effects, resistance, competitive release and
    diversity; Figures 3-5 and 8-10 captions; modeling Results and Discussion'
  accessed_at: '2026-10-14T21:54:56.164161Z'
  support: partial
  summary: Phage treatment altered dominance and diversity. The resistance-cost explanation
    is partial. Adding three-species data improved phage-free quantitative prediction;
    phage-present models retained quantitative failure despite qualitative release
    prediction. Caption text, not figure pixels, was inspected.
- evidence_id: pha
  kind: primary_source
  reference: PMID:40152616
  locator: 'Publisher Abstract; Results and Discussion: community overview, SEM/turnover,
    predicted host links/defenses and AMG expression; cached computational Methods'
  accessed_at: '2026-10-14T21:54:56.164161Z'
  support: supports
  summary: The observational time series supports correlated turnover and modeled
    associations. Sequence-derived host links/defenses and AMG transcripts remain
    qualified predictions or observations, not experimentally established lysis, resistance
    or yield effects.
- evidence_id: schema
  kind: record_content
  reference: src/communitymech/schema/communitymech.yaml
  locator: InteractionTypeEnum and EcologicalInteraction
  accessed_at: '2026-10-14T21:54:56.164161Z'
  support: supports
  summary: LYTIC_INFECTION requires virus-to-host infection; COMPETITION asserts reciprocal
    negative effects. The optional type need not be filled when neither applies. Community-level
    phenomena and explicitly bounded computational evidence can be represented without
    such a type.
- evidence_id: records
  kind: record_content
  reference: reports/causal_graph_review/decisions/20261014-phage-graphs-batch130.yaml
  locator: All ten per-node decisions and three retained-arrow decisions; exact canonical
    hashes
  accessed_at: '2026-10-14T22:21:55.727208Z'
  support: supports
  summary: Each current node is covered exactly once with source locator, participants
    and modality. Alseth retains three directions with two PARTIAL mediation qualifications.
    PHA remains arrow-free and byte-identical.
- evidence_id: methods-limit
  kind: primary_source
  reference: PMID:38648198
  locator: 'Materials and methods: Evolution experiment, statement that receptor mutants
    were not sequenced'
  accessed_at: '2026-10-14T22:21:55.727208Z'
  support: supports
  summary: The authors' receptor-mutant terminology is phenotype-based classification,
    not direct sequencing of the mutants in this study. The retained node and root
    summary now state this limit without changing the observed resistance outcome.
- evidence_id: before
  kind: prior_review
  reference: reviews/structured/20261014T215456Z-phage-graphs-before/review.yaml
  accessed_at: '2026-10-14T22:21:55.727208Z'
  support: supports
  summary: The immutable pre-repair review records the three original open findings.
    Exact input bytes are preserved in the before-provenance archive; the original
    report is not rewritten.
- evidence_id: sources
  kind: record_content
  reference: reports/causal_graph_review/sources/20261014-phage-graphs-batch130.json
  accessed_at: '2026-10-14T22:21:55.727208Z'
  support: supports
  summary: Dated primary-source access scope and unchanged cache hashes. Relevant
    passages and captions, not figure pixels, all supplements or raw-data reanalysis.
- evidence_id: gate-final-alseth-schema
  kind: validation
  reference: reports/causal_graph_review/20261014-batch130/final-alseth-schema.json
  accessed_at: '2026-10-14T22:21:55.727208Z'
  support: supports
  summary: Actual command completed successfully on the final record hashes; see retained
    receipt.
- evidence_id: gate-final-alseth-strict
  kind: validation
  reference: reports/causal_graph_review/20261014-batch130/final-alseth-strict.json
  accessed_at: '2026-10-14T22:21:55.727208Z'
  support: supports
  summary: Actual command completed successfully on the final record hashes; see retained
    receipt.
- evidence_id: gate-final-alseth-terms
  kind: validation
  reference: reports/causal_graph_review/20261014-batch130/final-alseth-terms.json
  accessed_at: '2026-10-14T22:21:55.727208Z'
  support: supports
  summary: Actual command completed successfully on the final record hashes; see retained
    receipt.
- evidence_id: gate-final-alseth-references
  kind: validation
  reference: reports/causal_graph_review/20261014-batch130/final-alseth-references.json
  accessed_at: '2026-10-14T22:21:55.727208Z'
  support: context_only
  summary: 'CLI completed but reports Total checks: 0. It is not counted as excerpt
    validation; explicit plugin/full traversal and audit-snippets supply that coverage.'
- evidence_id: gate-final-alseth-rank
  kind: validation
  reference: reports/causal_graph_review/20261014-batch130/final-alseth-rank.json
  accessed_at: '2026-10-14T22:21:55.727208Z'
  support: supports
  summary: Actual command completed successfully on the final record hashes; see retained
    receipt.
- evidence_id: gate-final-pha-schema
  kind: validation
  reference: reports/causal_graph_review/20261014-batch130/final-pha-schema.json
  accessed_at: '2026-10-14T22:21:55.727208Z'
  support: supports
  summary: Actual command completed successfully on the final record hashes; see retained
    receipt.
- evidence_id: gate-final-pha-strict
  kind: validation
  reference: reports/causal_graph_review/20261014-batch130/final-pha-strict.json
  accessed_at: '2026-10-14T22:21:55.727208Z'
  support: supports
  summary: Actual command completed successfully on the final record hashes; see retained
    receipt.
- evidence_id: gate-final-pha-terms
  kind: validation
  reference: reports/causal_graph_review/20261014-batch130/final-pha-terms.json
  accessed_at: '2026-10-14T22:21:55.727208Z'
  support: supports
  summary: Actual command completed successfully on the final record hashes; see retained
    receipt.
- evidence_id: gate-final-pha-references
  kind: validation
  reference: reports/causal_graph_review/20261014-batch130/final-pha-references.json
  accessed_at: '2026-10-14T22:21:55.727208Z'
  support: context_only
  summary: 'CLI completed but reports Total checks: 0. It is not counted as excerpt
    validation; explicit plugin/full traversal and audit-snippets supply that coverage.'
- evidence_id: gate-final-pha-rank
  kind: validation
  reference: reports/causal_graph_review/20261014-batch130/final-pha-rank.json
  accessed_at: '2026-10-14T22:21:55.727208Z'
  support: supports
  summary: Actual command completed successfully on the final record hashes; see retained
    receipt.
- evidence_id: gate-final-snippets-explicit
  kind: validation
  reference: reports/causal_graph_review/20261014-batch130/final-snippets-explicit.json
  accessed_at: '2026-10-14T22:21:55.727208Z'
  support: supports
  summary: Explicit plugin checks 27 Alseth and 24 PHA fields; explicit traversal
    additionally checks the Alseth Discussion, totaling 28 and 24. Invented-quote
    mutation controls fail and immediate restorations pass; network access is forbidden.
- evidence_id: gate-final-history
  kind: validation
  reference: reports/causal_graph_review/20261014-batch130/final-history.json
  accessed_at: '2026-10-14T22:21:55.727208Z'
  support: supports
  summary: Actual command completed successfully on the final record hashes; see retained
    receipt.
- evidence_id: gate-final-audit-snippets
  kind: validation
  reference: reports/causal_graph_review/20261014-batch130/final-audit-snippets.json
  accessed_at: '2026-10-14T22:21:55.727208Z'
  support: supports
  summary: Actual command completed successfully on the final record hashes; see retained
    receipt.
- evidence_id: gate-final-inventory
  kind: validation
  reference: reports/causal_graph_review/20261014-batch130/final-inventory.json
  accessed_at: '2026-10-14T22:21:55.727208Z'
  support: supports
  summary: Ignored-inclusive inventory:462 records,1383 nodes,533 arrows;408 reviewed,54
    needs_research,zero pending or stale; no structural defects or error-severity
    network findings.
- evidence_id: gate-final-network
  kind: validation
  reference: reports/causal_graph_review/20261014-batch130/final-network.json
  accessed_at: '2026-10-14T22:21:55.727208Z'
  support: context_only
  summary: Zero-warning command exits1 for 57 warnings (50 DISCONNECTED, 7 UNKNOWN_TARGET),
    byte-identical to baseline output. Required structural-error gate passes separately
    in final-inventory; no error-severity findings.
- evidence_id: gate-final-lint-corrected
  kind: validation
  reference: reports/causal_graph_review/20261014-batch130/final-lint-corrected.json
  accessed_at: '2026-10-14T22:21:55.727208Z'
  support: supports
  summary: Actual command completed successfully on the final record hashes; see retained
    receipt.
- evidence_id: gate-final-regression-complete
  kind: validation
  reference: reports/causal_graph_review/20261014-batch130/final-regression-complete.json
  accessed_at: '2026-10-14T22:21:55.727208Z'
  support: supports
  summary: 98 tests passed, including mutation/control/restoration checks. Twelve
    dependency deprecation warnings remain. This is focused coverage, not the full
    CI suite.
- evidence_id: gate-final-preservation-replay
  kind: validation
  reference: reports/causal_graph_review/20261014-batch130/final-preservation-replay.json
  accessed_at: '2026-10-14T22:21:55.727208Z'
  support: supports
  summary: All 462 canonical records accounted for; only Alseth changed. Other461
    records,927 tracked cache files and unrelated Alseth root blocks unchanged.
- evidence_id: gate-final-gen-html
  kind: validation
  reference: reports/causal_graph_review/20261014-batch130/final-gen-html.json
  accessed_at: '2026-10-14T22:21:55.727208Z'
  support: supports
  summary: Actual command completed successfully on the final record hashes; see retained
    receipt.
- evidence_id: gate-final-docs-current
  kind: validation
  reference: reports/causal_graph_review/20261014-batch130/final-docs-current.json
  accessed_at: '2026-10-14T22:21:55.727208Z'
  support: supports
  summary: Actual command completed successfully on the final record hashes; see retained
    receipt.
- evidence_id: gate-final-diff-check
  kind: validation
  reference: reports/causal_graph_review/20261014-batch130/final-diff-check.json
  accessed_at: '2026-10-14T22:21:55.727208Z'
  support: supports
  summary: Actual command completed successfully on the final record hashes; see retained
    receipt.
- evidence_id: gate-final-reviews-before
  kind: validation
  reference: reports/causal_graph_review/20261014-batch130/final-reviews-before.json
  accessed_at: '2026-10-14T22:21:55.727208Z'
  support: supports
  summary: Actual command completed successfully on the final record hashes; see retained
    receipt.
assessments:
- assessment_id: alseth-graph
  area: graph
  topic: Measured treatment effects versus mechanism and model claims
  outcome: supported
  summary: Retained measured infection, competitive release, resistance and diversity
    observations with source-bounded types, PARTIAL mediation and computational model
    scope. Mutation terminology is explicitly phenotype-based, not sequenced genotype.
    Five nodes and three existing directions remain; no new topology.
  target_ids:
  - CommunityMech:000467
  evidence_ids:
  - alseth
  - schema
  - records
  - methods-limit
  - gate-final-regression-complete
  - gate-final-snippets-explicit
- assessment_id: pha-graph
  area: graph
  topic: Observed turnover and explicitly modeled/predicted process context
  outcome: supported
  summary: Retain the kill-the-winner hypothesis as partial, coupled turnover as association,
    SEM diversity/activity effects as modeled associations, AMG transcripts without
    a yield claim, and defense predictions without functional resistance claims. These
    qualified context nodes do not supply causal arrows; the graph remains arrow-free.
  target_ids:
  - CommunityMech:000468
  evidence_ids:
  - pha
  - records
  - sources
  - gate-final-preservation-replay
  - gate-final-snippets-explicit
findings:
- finding_id: typing
  issue_key: communitymech-2005-typing
  category: graph
  severity: major
  status: resolved
  certainty: confirmed
  title: Outcome and model nodes carry unsupported mechanistic types
  description: The diversity outcome is not another lytic infection; resistance-route
    observations and fitted-model failure do not establish reciprocal negative effects.
    Keep measured infection and competitive release, and omit inappropriate optional
    types.
  target_ids:
  - CommunityMech:000467
  field_paths:
  - ecological_interactions[2].interaction_type
  - ecological_interactions[3].interaction_type
  - ecological_interactions[4].interaction_type
  evidence_ids:
  - alseth
  - schema
  - records
  - before
  - gate-final-regression-complete
  - gate-final-snippets-explicit
  rule_id: graph-interaction-type-scope
  native_severity: P2
  normalization_reason: Material causal or mechanistic scope inflation in a graph
    consumed as structured scientific claims.
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Alseth_FourSpecies_Pathogen_Phage_Community.yaml
    role: canonical_record
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/2005
  disposition_reason: Unsupported optional COMPETITION and outcome LYTIC_INFECTION
    labels removed; genuine pairwise infection and competitive release retained. Regression
    mutations reject their reintroduction.
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261014T215456Z-phage-graphs-before
    finding_id: typing
- finding_id: mediation
  issue_key: communitymech-2005-mediation
  category: graph
  severity: major
  status: resolved
  certainty: confirmed
  title: Two arrows exceed their measured causal support
  description: Receptor targeting is stated to cause the resistance route's fitness
    cost, and competitive release is stated to be the established diversity-maintaining
    mechanism. The source supports a partial cost explanation and joint treatment
    outcomes, not isolated necessary or sufficient mediation.
  target_ids:
  - CommunityMech:000467
  field_paths:
  - ecological_interactions[0].downstream[1].description
  - ecological_interactions[1].downstream[0].description
  evidence_ids:
  - alseth
  - schema
  - records
  - before
  - gate-final-regression-complete
  - gate-final-snippets-explicit
  rule_id: graph-causal-mediation
  native_severity: P2
  normalization_reason: Material causal or mechanistic scope inflation in a graph
    consumed as structured scientific claims.
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Alseth_FourSpecies_Pathogen_Phage_Community.yaml
    role: canonical_record
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/2005
  disposition_reason: Both affected arrows are now explicitly PARTIAL. Source-backed
    Discussion records unresolved mediation, while existing directions and positive
    treatment observations remain intact. Mutation checks reject causal overclaims.
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261014T215456Z-phage-graphs-before
    finding_id: mediation
- finding_id: model-scope
  issue_key: communitymech-2005-model-scope
  category: graph
  severity: major
  status: resolved
  certainty: confirmed
  title: Model failure and improved prediction are overgeneralized
  description: The record omits the phage-free condition on improved quantitative
    four-species prediction and turns failure of tested pairwise-fitted models into
    general non-reconstructibility. Retain the published computational observation
    without treating it as proof of one higher-order mechanism or an impossibility
    theorem.
  target_ids:
  - CommunityMech:000467
  field_paths:
  - description
  - ecological_interactions[4]
  evidence_ids:
  - alseth
  - schema
  - records
  - before
  - gate-final-regression-complete
  - gate-final-snippets-explicit
  rule_id: graph-model-context-boundary
  native_severity: P2
  normalization_reason: Material causal or mechanistic scope inflation in a graph
    consumed as structured scientific claims.
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Alseth_FourSpecies_Pathogen_Phage_Community.yaml
    role: canonical_record
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/2005
  disposition_reason: Node and root description distinguish tested-model failure from
    general impossibility, phage-free quantitative improvement from phage-present
    failure, and qualitative release prediction. New exact excerpts and computational
    modality are verified; mutations reject lost conditions and fabricated evidence.
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261014T215456Z-phage-graphs-before
    finding_id: model-scope
actions: []
limitations:
- Source-based self-adversarial review, not independent approval or whole-record certification.
- Whole records and relevant primary Results/Discussion/Methods and captions inspected;
  figure pixels, all supplements, raw data and executable models not reanalyzed.
- Other 460 records receive structural census and preservation checks, not new semantic
  review; 54 needs_research records remain unresolved.
- Native reference CLI reports zero checks. Explicit plugin invocation checks 27 Alseth
  and 24 PHA fields; full excerpt traversal additionally checks the Alseth Discussion,
  totaling 28 and 24. Lexical matches do not prove causal support.
- 'Discussion traversal gap #476 is compensated locally, not fixed. No schema, validator
  or threshold is weakened.'
- No new topology, provider submission, biological protocol or optimization instruction
  is introduced.
- Network zero-warning audit remains failed with its actual exit1 and unchanged57
  warnings; required structural-error gate passes. No finding is hidden by changing
  gate thresholds.
- Native whole-record completeness and validation-quality scores are not computed
  for this graph-only assessment.
- The first lint run failed on test formatting; the retained corrected lint and regression
  receipts pass. Earlier failed/interim receipts remain historical, not counted as
  final success.
- Full remote CI and merge-queue checks are not yet complete at this scientific-review
  snapshot. Publication must wait for required checks; this verdict does not authorize
  bypass.
links:
- https://github.com/CultureBotAI/CommunityMech/issues/2005
- https://github.com/CultureBotAI/CommunityMech/tree/review-provenance/20261014-batch130-before
- https://github.com/CultureBotAI/CommunityMech/tree/review-provenance/20261014-batch130-inputs
tags:
- causal-graphs
- batch130
- self-review
```
