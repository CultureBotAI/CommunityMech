# M5 CommunityMech completion evidence

The recovered scope is four records, not the entire corpus. The original M5
checkout and stalled session were preserved. Work uses a separate full clone
on branch `review/m5-completion-20261114`, starting from current main
`76aa644cd6803ea2c9545d4c704276ede219d354`.

This checkpoint preserves completed primary-source assessments and bounded
post-curation acceptance. **Full `qc` and reference validation for all four
scoped records passed. The full-corpus reference gate remains blocked.** The first
corrected-revision run at `76686e5b03335baec13885196d0f736511b6a04a` failed its
test stage. The full M5 retry at
`e9ae9dee132ab210c87f76460c5d6247af9ea99c`, with independently reviewed repairs,
a clean tracked checkout, frozen dependencies and generated KGX prerequisites,
completed every native `qc` stage before starting separate reference validation.
The reference sweep completed all 549 expected records: 535 passed and 14 had
103 native errors (102 excerpt mismatches and one unavailable source). There were
no missing, extra, duplicate or unfinished targets. The `qc-references` invocation
exited 1; its final success-summary recipe remained `NOT RUN` after the failed
reference dependency. The [complete reference inventory](reference-sweep-final.json)
binds these results to the exact Git tree, native command, receipt and log hash.
The records are not collectively scientifically approved: retained findings
below continue to block that claim. No PR has been merged.

## Scope and assessments

[Recovered scope](scope.md) records the Git/session reconstruction, unavailable
old handoffs, prior PRs, exact record hashes and separate infrastructure backlog.
The first EcoFAB review was saved and independently checked before distributing
the other three records. Assessments inspect primary text, figures and applicable
supplements; focused validators are recorded separately from scientific judgments.

| Record | Primary-source assessment | Bounded corrections in this PR | Retained scientific blockers |
|---|---|---|---|
| 000025 EcoFAB Ring Trial SynCom17 | [YAML](../../reviews/structured/20261114T212137Z-m5-ecofab-completion-canary/review.yaml) · [Markdown](../../reviews/structured/20261114T212137Z-m5-ecofab-completion-canary/review.md) | Correct the dopamine-community subset description; correct two article-cache content declarations | Causal-role and protocol scope (#1427); OAP107/mapping provenance (#2674); genome pseudo-range (#2675) |
| 000087 LBNL Switchgrass Soil SynCom16 | [YAML](../../reviews/structured/20261114T213343Z-m5-lbnl-switchgrass-completion/review.yaml) · [Markdown](../../reviews/structured/20261114T213343Z-m5-lbnl-switchgrass-completion/review.md) | No canonical edit; [reproduced mapping](lbnl-supplemental-assessment.md) supplements the saved assessment | Missing strain roster and assay scope (#1548); source habitat versus physical study setting (#2776) |
| 000515 Yolo Soil Dopamine Microcosm | [YAML](../../reviews/structured/20261114T213322Z-m5-yolo-scientific-completion/review.yaml) · [Markdown](../../reviews/structured/20261114T213322Z-m5-yolo-scientific-completion/review.md) | Replace copied amoA rationale with reproduced taxonomic-vote provenance; pin mapping hash/method; correct shared Ding cache metadata | Both assessed findings resolved in the bounded successor; no organism function was inferred from the crosswalk |
| 000516 Brachypodium Dopamine SynCom16 | [YAML](../../reviews/structured/20261114T213444Z-m5-dopamine-syncom-primary-review/review.yaml) · [Markdown](../../reviews/structured/20261114T213444Z-m5-dopamine-syncom-primary-review/review.md) | Remove unsupported causal tags from correlations and the extracellular endpoint; preserve measured effects/quotations; correct shared cache metadata and guide examples | Grounding/provenance ambiguity (#2774) |

The additive 000087 environment finding has its own immutable
[YAML](../../reviews/structured/20261114T213834Z-m5-lbnl-environment-addendum/review.yaml)
and [Markdown](../../reviews/structured/20261114T213834Z-m5-lbnl-environment-addendum/review.md).
Earlier reviews are historical observations and are never rewritten to appear green.

The completed [post-curation YAML](../../reviews/structured/20261114T221158Z-m5-postcuration-scientific-delta/review.yaml)
and [Markdown](../../reviews/structured/20261114T221158Z-m5-postcuration-scientific-delta/review.md)
resolve six stable finding keys and retain five across the three changed records.
Its 24 required gates passed on the corrected C1 revision: seven per record,
generated-page consistency, all-history validation and the four-module cache suite.
Both Ding-cache consumers are reconciled. Coverage is limited to changed fields;
the unchanged full-record claims and separate LBNL findings retain their earlier
assessments. Two failed broader diagnostics are included explicitly and do not
become passes through this scoped acceptance.

## Technical evidence and limits

[Technical checks](technical-checks.md) link exact exits, native stages and
[durable logs/receipts](technical-evidence/README.md). Failed and interrupted
attempts remain visible; a later individual check does not change an earlier
aggregate's `NOT RUN` stages. Receipts distinguish M5 runs from local checks
and record revision, source status and relevant hashes.

The final M5 run tested `e9ae9dee132ab210c87f76460c5d6247af9ea99c` from a clean
tracked checkout with frozen dependencies. Later reporting-only work does not
change that tested revision. The read-only
[reference-summary helper](../../scripts/adhoc/summarize_m5_native_references_20261114.py)
and its tests were added afterward to reconcile evidence; its
[27 regression checks](technical-evidence/local-native-reference-summary-guards.log.txt)
passed, and the exact-Git-inventory/command-binding fixes (#2791, #2792) passed
independent read-only review. They do not rerun or replace native validation.

| Final check | Result |
|---|---|
| Full native `qc` | **Passed**: 5,457 tests passed, 102 skipped, 8 deselected; all subsequent schema, strict, GTDB, scalar and ontology stages passed |
| Full corpus reference sweep | **Failed**, exit 1: all 549 targets completed; 103 errors across 14 records; all four scoped records passed |
| Three changed records: schema, strict, terms, references, GTDB, domain and history | **21/21 passed** |
| Generated pages (`check-docs-current`) | **Passed** |
| Unscoped `validate-history` | **Passed** |
| Product validation with generated KGX prerequisites | **Passed**: 11,245 canonical matches, 4 synonyms, 5 explicit exceptions and 1,065 intentional non-ontology/prefixless exclusions |

Product exclusions are outside ontology-lookup scope, not canonical-label passes.
No configured ontology outage was reported. The final `qc-references` success
summary remains `NOT RUN` because its reference dependency failed; later focused
checks are independent diagnostics and do not change that aggregate result.

The initial full QC exposed missing historical Git objects required by existing
tests. The exact CI-listed objects were fetched and the failed cases rerun.
Reference validation separately reproduced #622: the old dependency discarded
literal `[NiFe]` content. The minimal upstream fix retains that content; the
unchanged source passes and a mutated `[FeFe]` claim fails. Source quotations,
matching thresholds and scientific scope were preserved.

The C1 aggregate completed with exit 1: 7 failed, 5,392 passed, 102 skipped,
8 deselected. Lint passed; every later aggregate recipe was `NOT RUN`. The seven
failures identify historical-current hash assumptions (#2782), a PDF inventory
that included ignored source captures (#2786), a static scope-scanner variable
collision (#2787), and missing classifications for noncanonical review writers
(#2788). Each has a bounded independently reviewed fix. C2 verified them together:
5,457 tests passed, 102 skipped and 8 deselected, followed by all remaining native
`qc` stages. The [append-only successor provenance](successor-provenance.yaml)
retains the older observation and does not itself grant scientific approval.

Separate C1 diagnostics passed all 21 focused checks, generated pages, full
history and 60 cache tests. Product validation failed because the fresh clone
had not generated required `output/kgx/nodes.tsv`; it reported 10,254 canonical
matches, 5 exceptions and 553 adapter skips. C2 generated and strictly validated
the KGX prerequisites, then passed the product check as reported above. The 553 skips identify
non-ontology or prefixless identifiers deliberately outside ontology-lookup
scope; they are not canonical-label passes or unavailable configured adapters.
The saved summary does not provide a per-prefix breakdown. The duplicate C1 corpus-reference fallback was explicitly
left `NOT RUN` in favor of the frozen retry.

The broader schema/export/render findings #2429, #2430 and #2700–#2707 remain
outside these bounded corrections. Passing the existing gates cannot resolve
them. Missing mechanism evidence is retained as uncertainty, not replaced by
invented causal edges. No issue is automatically closed by this evidence bundle.

The legacy reference-error explanation is tracked separately in #2785: its
bracket-stripping diagnosis predates the literal-preserving configuration.
Native matching and exit codes determine validation status; that explanatory
heuristic is not accepted as scientific evidence or used to clear a failed gate.

During C2, native full-text enrichment exposed a separate source-identity defect
(#2790): an Anubis CAPTCHA page was appended to an unrelated cached source and
classified as article full text. The old cached text was preserved. Runtime
cache changes are retained privately and are not reviewed curation changes.
Matching against preserved passages remains informative; an automated pass
cannot certify the identity or completeness of newly fetched pages.

The [runtime-cache capture](runtime-cache-effects.md) preserves both the tested
baseline and the final cache tree in both completion clones. Native fetching
modified 136 tracked cache files and created 31 acquisition files; no tracked
changes occurred outside the cache. All five direct cache inputs used by the six
scientific reviews still match their C2 baseline hashes. The M5 runtime changes
remain uncommitted and are excluded from this PR; their private archives retain
the exact fetched bytes, including the known challenge-page defect.

The native `Total checks` summary counts retained validation issues, not compared
excerpts (the residual wording is documented in #257). Zero therefore means no
reported issues; it does not measure excerpt coverage. Actual matching and schema
annotation discovery were exercised by positive and fabricated-excerpt controls.
The separate SupportingReference traversal gap (#476) remains open.

The [reference-failure triage](reference-failure-triage-20261114.md) retains exact
native diagnostics, source/record hashes and existing issue ownership. Earlier
checkpoint counts remain explicitly partial; the complete inventory above is
the final corpus result. Source access and matching failures are not silently
converted to scientific verdicts.
The [parser-snapshot persistence proof](persistence-20261114/parser-snapshots-20261114.md)
records the missing-only copy and hash verification of its immutable inputs.

## Persistence and resumption

All new review bundles and append-only history are committed with their helper
scripts under `scripts/adhoc/`. Raw paper/supplement material and private recovery
evidence remain in `.temp/m5-completion-20261114/` in the completion clones;
public reviews retain source identifiers, locators, quotations and hashes.
Public technical logs redact private paths and credential-shaped text while
retaining original and derivative hashes. The original checkout is not a
resumption workspace.

The [dated persistence audit](persistence-20261114/README.md) corrects the
premature "both clones" location claim in two earlier immutable receipts
(#2789). Missing-only replication then established both copies: all six reviews'
268 retained-input checks, 33 native logs and 99 raw JSON/log/exit files matched.
The prior receipts remain unchanged, and one differing private PR-body draft was
preserved. That earlier audit excluded active C2 files. The later
[final reference persistence audit](persistence-20261114/final-reference-persistence-20261114.md)
verified all 25 immutable parser artifacts and all 105 local raw files (35
complete JSON/log/exit triplets) on M5 before final publication. The exporter's
unconditional location wording remains a follow-up.

The saved reviews' captured working inputs were rechecked without fetching or
rewriting them: [EcoFAB](retained-inputs/ecofab.json),
[Yolo](retained-inputs/yolo.json), [LBNL](retained-inputs/lbnl.json),
[dopamine SynCom](retained-inputs/dopamine.json), and
[LBNL environment addendum](retained-inputs/lbnl-environment.json), followed by
the [post-curation successor](retained-inputs/postcuration.json).
Every listed source/check input matches its saved SHA-256. These audits prove
retention of the assessed inputs; they do not constitute another scientific review.

The final native `check-record-reviews` run passed for all 286 saved reviews,
with `coverage: declared_scopes_only`. `RECORD_REVIEW_BASE` was explicitly set
to the initial current-main revision `76aa644cd6803ea2c9545d4c704276ede219d354`.
Its [log](technical-evidence/local-final-native-reviews.log.txt) and
[receipt](technical-evidence/local-final-native-reviews.receipt.json) preserve
the local working-tree check; all saved bundle bytes remained unchanged through
the subsequent commit. This validates the review contract, not all scientific
claims in the corpus.

Three builder/source helpers were formatted after their reviews were saved;
one XML parser was also changed to the hardened equivalent. No builder was
rerun and no saved review hash was changed. The immutable review inputs retain
the earlier working-tree helper hashes as historical attestations, rather than
claiming that later formatting reproduces those exact helper bytes. Subsequent
helper fixes are independently tested and reported separately from the frozen
M5 scientific/QC revision.

`git diff --check` passes for source and documentation changes when retained
native `*.log.txt` files are excluded. Those logs deliberately preserve native
trailing whitespace; an unrestricted whitespace check reports it.

PR: [CommunityMech #2775](https://github.com/CultureBotAI/CommunityMech/pull/2775).
The corpus-reference failure and retained scientific findings remain blockers;
green focused checks and bounded scientific acceptance do not clear them.
