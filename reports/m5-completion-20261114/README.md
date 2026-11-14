# M5 CommunityMech completion evidence

The recovered scope is four records, not the entire corpus. The original M5
checkout and stalled session were preserved. Work uses a separate full clone
on branch `review/m5-completion-20261114`, starting from current main
`76aa644cd6803ea2c9545d4c704276ede219d354`.

This checkpoint preserves completed primary-source assessments and bounded
corrections. **Final technical QC is running on M5 at
`76686e5b03335baec13885196d0f736511b6a04a`; post-curation acceptance is pending.**
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
| 000515 Yolo Soil Dopamine Microcosm | [YAML](../../reviews/structured/20261114T213322Z-m5-yolo-scientific-completion/review.yaml) · [Markdown](../../reviews/structured/20261114T213322Z-m5-yolo-scientific-completion/review.md) | Replace copied amoA rationale with reproduced taxonomic-vote provenance; pin mapping hash/method; correct shared Ding cache metadata | Correction acceptance awaits post-curation gates; no source-supported organism function was inferred from the crosswalk |
| 000516 Brachypodium Dopamine SynCom16 | [YAML](../../reviews/structured/20261114T213444Z-m5-dopamine-syncom-primary-review/review.yaml) · [Markdown](../../reviews/structured/20261114T213444Z-m5-dopamine-syncom-primary-review/review.md) | Remove unsupported causal tags from correlations and the extracellular endpoint; preserve measured effects/quotations; correct shared cache metadata and guide examples | Grounding/provenance ambiguity (#2774); correction acceptance awaits post-curation gates |

The additive 000087 environment finding has its own immutable
[YAML](../../reviews/structured/20261114T213834Z-m5-lbnl-environment-addendum/review.yaml)
and [Markdown](../../reviews/structured/20261114T213834Z-m5-lbnl-environment-addendum/review.md).
Earlier reviews are historical observations and are never rewritten to appear green.

## Technical evidence and limits

[Technical checks](technical-checks.md) link exact exits, native stages and
[durable logs/receipts](technical-evidence/README.md). Failed and interrupted
attempts remain visible; a later individual check does not change an earlier
aggregate's `NOT RUN` stages. Receipts distinguish M5 runs from local checks
and record revision, source status and relevant hashes.

The initial full QC exposed missing historical Git objects required by existing
tests. The exact CI-listed objects were fetched and the failed cases rerun.
Reference validation separately reproduced #622: the old dependency discarded
literal `[NiFe]` content. The minimal upstream fix retains that content; the
unchanged source passes and a mutated `[FeFe]` claim fails. Source quotations,
matching thresholds and scientific scope were preserved.

The broader schema/export/render findings #2429, #2430 and #2700–#2707 remain
outside these bounded corrections. Passing the existing gates cannot resolve
them. Missing mechanism evidence is retained as uncertainty, not replaced by
invented causal edges. No issue is automatically closed by this evidence bundle.

## Persistence and resumption

All new review bundles and append-only history are committed with their helper
scripts under `scripts/adhoc/`. Raw paper/supplement material and private recovery
evidence remain in `.temp/m5-completion-20261114/` in the completion clones;
public reviews retain source identifiers, locators, quotations and hashes.
Public technical logs redact private paths and credential-shaped text while
retaining original and derivative hashes. The original checkout is not a
resumption workspace.

The saved reviews' captured working inputs were rechecked without fetching or
rewriting them: [EcoFAB](retained-inputs/ecofab.json),
[Yolo](retained-inputs/yolo.json), [LBNL](retained-inputs/lbnl.json),
[dopamine SynCom](retained-inputs/dopamine.json), and
[LBNL environment addendum](retained-inputs/lbnl-environment.json).
Every listed source/check input matches its saved SHA-256. These audits prove
retention of the assessed inputs; they do not constitute another scientific review.

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
Only a completed final QC receipt and post-curation review can replace the
pending status above; green focused checks alone cannot do so.
