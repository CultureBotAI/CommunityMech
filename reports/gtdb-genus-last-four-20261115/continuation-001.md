# Resume the three-record checkpoint

This lane is paused at the user's requested durable boundary for a separate
Intel handoff. No new records are assigned here. The completed 441 canary was
published at `4f46bb640e0a5ceec646df90527bdfa881a20e12` on draft PR 2905.
The later checkpoint preserves the accepted 389/381/482 applications and
evidence but deliberately leaves strict admission and integration unfinished.

Local worktree: `/Users/marcin/agent-work/CommunityMech/gtdb-genus-last-four-20261115`.
Local branch: `review/gtdb-genus-last-four-20261115`. Obtain the exact published
checkpoint head from this branch and PR 2905; do not infer it from M5 HEAD.
The M5 host is `marcins-MacBook-Pro-3.local`, with the same checkout path and
branch name, frozen at `308081a8cf3f82472c542db87e135a5b96da61be`.
Do not pull the later public leaf into this execution checkout or change its
Claw provider `23899092a4a2aedf53ff4435c0bdc03ebd79e6be`.

All 24 native gates are finished; no gate process remains. Both saved-pair
audits and standalone 181-file checkpoint verifiers passed. The saved bundle,
full hashes, byte counts, raw recorder names and 81 public artifact manifest
pins are in [the checkpoint outcome](remaining-three-checkpoint-outcome-001.md).
Private stage/apply/check/draft directories and both complete immutable
snapshots remain under `.temp/gtdb-genus-last-four-20261115/`. Preserve them,
including failed tooling attempts. They are not disposable scratch space.

Current accepted canonical hashes are:

| Record | Current SHA256 |
|---|---|
| 389 | `f3d1070490b0d63e018b74be21d805e4f61da66dc423bb0fb059fa434825db3f` |
| 381 | `c5e1f0beaab510b6cc61f7f32b38d89935461378ba56e231e0eaed3887e7a2b7` |
| 482 | `d06607ee111c282355160fc88cc38c0431ed7580c901b73941d7a0fab1baf82c` |

On resumption, verify the published branch and preserved proof hashes first.
Then add only these three fixed manifests to
`tests/genus_last_four_gtdb_successors.py` and reuse the existing thin actual
fixture in `tests/test_genus_last_four_gtdb_actual_successors.py`. Preserve the
441 allowance and the unchanged shared core/factory. Verify the expected
predecessors against real Git baseline
`68699871415fda3c9eebf20382a315f9f3c7b17a`; do not substitute an execution SHA.

Adapt the three historical callers only after an independent frozen-diff
review. Batch 96 needs exact 389 admission for its old raw digest and last-LLM
predicate while current biology stays current. Batch 88 needs the analogous
381 admission, retaining the unrelated 461 c9s5 remediation chain and source
cache predicates. Batch 133 needs only 482's old digest/history admission,
retaining the current-document equality guard and all existing
472/474/475/476/477/481 branches. The maintained integration branch additionally
contains the accepted 471 identity/mapping composite; its owner must compose
482 with that branch rather than replace the integration caller wholesale.
Do not import unrelated canonical/proof closures into this captured leaf.

Before publishing completion, retain a meaningful baseline refusal if run,
execute one real production proof canary, then the remaining actual tamper and
restoration controls plus the affected caller/participant checks. Run the
appropriate native lint and declared-scope review integrity check, record
actual results, and obtain independent final factual review. None of those
new registry/caller tests has run at this checkpoint. Do not treat the current
unchanged callers as a passing integration or cherry-pick this checkpoint into
the maintained branch before those obligations are completed.

Scientific limits remain unchanged: 389 is mixed amplicon/enrichment evidence,
381 retains stock/assembly and B12 attribution/transfer uncertainty, and 482
remains term-only with issues 2404–2406 open. The shared saved diagnostic is
partial with `scientific_review:false`; full scientific and aggregate QC work
remain outside this stopping point. No merge is authorized.
