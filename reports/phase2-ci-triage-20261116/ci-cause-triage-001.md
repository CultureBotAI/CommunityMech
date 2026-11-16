# PR2927 CI causes at the integration checkpoint

The nine hosted strict-test failures remain relevant to the current integration,
but they are not nine independent scientific defects. They include unsupported
test assumptions about current mapping populations, one exact ignore-rule gap,
and source differences that still require adjudication. This report does not
change a record, test, schema, historical ledger, or generated page.

The [strict run 43780166175](https://github.com/CultureBotAI/CommunityMech/actions/runs/43780166175/job/133015307523)
finished with **9 failed, 8,367 passed, 90 skipped, 8 deselected, and 18 warnings**
in 3,255.82 seconds. No test suite was rerun for this inventory.

## Exact execution and observation scopes

GitHub reports PR head `f3ecf5dba91f50c7b3c30daa4953c9cc7425f762`, but the actual
checkout step used synthetic merge **`de9b5a7c705ab5c9ce722df211f5bced96b2a94d`**:
that PR head merged into `7d680adbd870311914781157c99923dd4e6ecb88`. The full
strict-job log records this at lines 232–235. Its counters must not be attributed
to the PR head alone. The docs job used the same synthetic merge.

The isolated triage branch is based on maintained integration
**`fb9be6d99daffd8ecf9c2cb7443d5b0022128d9e`**. All nine failing test files are
byte-identical across the PR head, actual CI checkout, and this integration
revision. The records differ. The [immutable inventory](immutable-ci-inventory-002.json)
reads exact Git archives, never a mutable working-tree record:

| Observation | PR head f3ec | Hosted merge de9b | Integration fb9 |
| --- | ---: | ---: | ---: |
| YAML records across three descriptor roots | 551 | 551 | 551 |
| Stored GTDB blocks, including non-taxonomy descriptors | 1,312 | 1,338 | 1,346 |
| Taxonomy entries marked UNRESOLVED | 281 | 255 | 247 |
| Blocks with `is_reclassified: true` | 194 | 206 | 208 |
| Classified outside the `different_name` bucket | 86 | 95 | 96 |
| Fraction outside that bucket | 44.33% | 46.12% | 46.15% |

The hosted merge reproduces the log's **95/206** and **255** exactly. These are
read-only calculations using the captured maintained pure name classifier,
not new pytest results or scientific judgments about why a name changed.

## Nine failed tests and bounded next actions

| Failed test | Evidence and present relevance | Owner and repair boundary |
| --- | --- | --- |
| `test_gtdb_grounding_freshness.py::test_grounding_is_not_stale_against_its_taxon_id` | The sole mismatch is Terrabacter stock 1472881 versus verified genus 53355. The current curated block intentionally records the genus route; the source proof says the exact stock route is null. | [2946](https://github.com/CultureBotAI/CommunityMech/issues/2946), related issue 2849. Authenticate this exact approved route through the existing source/application/review proof; retain ordinary equality and unknown-route refusals. Do not change stock or source IDs to make them equal. |
| `test_gtdb_lineage_tree.py::test_the_committed_kb_is_a_consistent_hierarchy` | Four parent-path conflicts derive from `Verrucomicrobiae` versus `Verrucomicrobiia`. Amsterdam record 382 uses the pinned 761 crosswalk; MUC2 and MDSC declare manual R232. The same conflict remains in fb9. | [2948](https://github.com/CultureBotAI/CommunityMech/issues/2948). Verify the actual source/version lineages before correcting a spelling or changing comparison scope. No source-independent alias or blanket curated exemption. |
| `test_gtdb_near_tie_marker.py::test_the_known_near_ties_are_still_there` | Its universal Bacillota-only assertion rejects the stored native Leptolyngbya reference at 0.542. The current inventory contains eight near-tie blocks, including the explicitly curated Syntrophotalea 0.5 case. | [2947](https://github.com/CultureBotAI/CommunityMech/issues/2947), related issue 396. Keep the historical known-block proof and current majority/curation and advisory-marker invariants; separately admit source-bound additions. |
| `test_gtdb_support_counts.py::test_every_kb_taxon_reports_one_denominator` | NCBITaxon 239935 is grouped into one legacy population despite total 4983/fraction 1.0 from the 761 crosswalk and total 1806/fraction 0.731 in two manual R232 blocks. The existing authenticated exception covers Blautia 53443 only. | [2833 evidence update](https://github.com/CultureBotAI/CommunityMech/issues/2833#issuecomment-6904882763). Verify exact source populations before partitioning comparisons. The manual 1806 tally is not recertified here. |
| `test_is_reclassified_semantics.py::test_the_majority_of_true_values_are_not_reclassifications` | Hosted 95/206 and current 96/208 exceed the 0.45 cap. The schema still calls 143 blocks and its historical breakdown current. Current zero plain-strain-drop semantics remain satisfied in the captured classifier census. | [2947](https://github.com/CultureBotAI/CommunityMech/issues/2947), related issues 480/2063. Preserve the actual migration's historical evidence and current semantic zero cases; make descriptive counts explicitly dated or generated. Do not arbitrarily widen the ratio band. |
| `test_label_drift_report_is_ignored.py::test_no_tracked_report_is_ignored` | Exactly one tracked public Wetland measurement log still matches committed `.gitignore:97` (`*.log`). The bytes are present and intact; forcing them into Git did not remove the ignore match. | [2922 evidence update](https://github.com/CultureBotAI/CommunityMech/issues/2922#issuecomment-6904881261). Root owns the exact path exception alongside the separate adoption exceptions under issue 2945. The immutable log and general private-log rule remain protected. |
| `test_phage_review_regressions.py::test_phage_corpus_addition_explains_the_grounding_baseline_delta` | Alseth has zero UNRESOLVED entries, so the old expectation of four fails. Its accepted successor contains three reference groundings and one complete ambiguity; PHA's five bacterial descriptors are now grounded. Both viral exclusions remain. | [2947](https://github.com/CultureBotAI/CommunityMech/issues/2947). Admit exact current proofs before evaluating the old 4/5-UNRESOLVED claim on authenticated predecessors. Keep current biological and source mutation controls. |
| `test_stage6_infrastructure.py::test_infra_0004_corpus_count_decoupling_preserves_invariants` | This calls the same reclassification ratio check after adding a synthetic different-name tuple. It fails the same 95/206 band; it is not a second source defect. | [2947](https://github.com/CultureBotAI/CommunityMech/issues/2947). Update the composed infrastructure control alongside the parent contract, retaining its positive/mutation/restoration meaning. |
| `test_transwell_participants.py::test_only_transwell_accounts_for_gtdb_distribution_change` | Hosted 255 and current 247 UNRESOLVED are below the historical 494 floor after reviewed mappings. | Community's separate 091 lane owns this. Its frozen code was independently accepted: exact current admission plus immutable Git 686 census, original floors, and exact −5/+1 predecessor substitution/restoration. Integration remains pending; no duplicate repair here. |

## What the retained proofs establish

Terrabacter's current SHA256 is
`068a38e5be07ab6756b1fe32683c166d8562e8405fae7bc4429575a33e2578ec`.
The [published source route](../gtdb-source-routes-2849-20261115/TERRABACTER.md)
and `tests/batch144_mapping_successor.py` already bind its precise stock,
genus result, source proof, actual application, saved partial review and history.
A future freshness exception must reuse that evidence with exact pins; a bare
`curated` flag or prose in `mapping_source` is insufficient.

The two phage manifests were read and every nested artifact path/hash was
independently verified, including their saved pairs, raw applications, native
results, eight gate triplets, and sidecars. Their real Git686 predecessors were
also rehashed:

| Record | Manifest SHA256 | Git686 predecessor | Current SHA256 |
| --- | --- | --- | --- |
| 467 Alseth | `6e46a3c754bf766546669c4abfb28bad36cc00fbd19f89dc634ebd2887ab1c76` | `cef1f3c47035ef336cb809456b25a185e0397bb9f0a16c492becdb5b371529f5` | `00bd07edc28d86c0133ed565ee28c81fe6a21aaa49a0ac2edd68639e70c21a08` |
| 468 PHA | `55b3a3c004f09cf2820303e14c8fb8b3419502d38d770e6e17ab4e868c2c8973` | `aebd6497b6d5a6f49e9e9ef956d4ec0847960acc0fd2413dce5e0960ed748488` | `ee9ebca7eb46d11d4182e89de6046f0b16bc43ae1cd711d6b402382a9d12d85b` |

This supports a bounded historical-test repair; it does not confer full
scientific approval on either record. No new strict admission was executed in
this read-only triage.

The Akkermansia discrepancy remains a scientific-source dependency. The
Amsterdam result is a species-name route with no exact species-ID rows, not a
study-stock genome assignment. The R232 1806 assertions and their lineage
spelling need their own primary-source audit. The pinned crosswalk's release is unknown;
no older/newer ordering or equivalence is inferred. Source-reported ATCC BAA-83
versus type-material BAA-835 must not be silently normalized.

## Generated products

[Docs run 43780166164](https://github.com/CultureBotAI/CommunityMech/actions/runs/43780166164)
rendered 512 communities but failed `check-docs-current` on exactly the Wetland 471
page plus `docs/browser.html`, `docs/communities.json`, and `docs/communities.tsv`.
Those four committed files are identical between f3ec and fb9. A fresh fb9
render was not run here. [2949](https://github.com/CultureBotAI/CommunityMech/issues/2949)
assigns native regeneration and actual final-gate verification to root/integration
after accepted leaves are composed. Generated HTML must not be hand-edited.

## Provenance and verification

The helper [inventory_phase2_ci_causes_20261116.py](../../scripts/adhoc/inventory_phase2_ci_causes_20261116.py)
reads immutable Git archives, captures per-file hashes, and executes only the
captured pure classifier definitions. It invokes no test, native grounder,
provider, or curation writer. Its exclusive JSON output contains public record
metadata and hashes, not private article bodies. Black check and Ruff pass.

| Retained evidence | SHA256 |
| --- | --- |
| Helper | `6d14e991c6562fa4c5af46a8cd8f825bf4fb5a3a1e1fe522c0b89e05d5031828` |
| Immutable inventory 002 | `45efbd22e90214aa4e1078f6b405a3ce3e35e188450eb59a6e1adf473245c0cc` |
| Actual inventory recorder 002 log | `c6c23181ac75386cf2265f017622b72214177d486eb9145b077d042627ffd57d` |
| Original strict failed-step log | `5d9f00b967a67c24791d253b3637c14813466cc4ac390b80a540ac8da1b89398` |
| Full strict-job log with checkout identity | `009a15f3a6448561f78ccdb9d252deccc3bb1bb726445edafeab3dde9cbc7dcc` |
| Original docs failed-step log | `c3679d514f0b7cb0a09f5329ee2348c00c0d88e964b0b5dd6f6ff48e07bc1420` |

Original failed-step logs remain in the final-four lane's
`.temp/phase2-schema-20261115/final-four-pr2927-*-failure-readback-001.log`.
Full job logs, exact issue bodies/readbacks, and bounded live issue searches are
retained under this lane's `.temp/phase2-ci-triage-20261116/`. The native inventory
receipt/log/exit are under `.temp/phase2-schema-20261115/phase2-ci-source-inventory-002.*`.
The earlier head-only inventory 001 and its exact executed helper are preserved
privately; inventory 002 adds the actual synthetic merge after the counter discrepancy was
identified. Initial helper lint found import ordering and an unannotated use of
the captured AST executor; both were corrected before 002, with no test or
scientific logic change. All six newly created issue/comment bodies were read
back byte-for-byte; the four new issues are open.

Root owns the exact ignore exceptions and final combined rendering. This lane
will prepare narrowly authenticated freshness and historical contracts.
The mixed Akkermansia populations still require source adjudication.
There is no aggregate QC pass, test repair, canonical change, issue closure, or
merge in this checkpoint.
