Work the CommunityMech backlog, one issue at a time, **in this repo only** — never edit
sibling repos (CultureMech/MIM/TraitMech), even for cross-Mech sync; report divergence.

## Loop

1. **Reconcile and prioritize** with the `next-tasks` skill — invoke it, don't restate
   it. Pick the top actionable issue; upstream-blocked ones stay listed, never picked.

2. **Check dependencies first.** What does this fix touch, and does an open PR touch it?
   If B is only correct after A, do A first, or branch B off A and say so. **One branch
   and one PR in flight at a time** — no parallel PRs.

3. **Branch before any edit**, `NEXT_TASKS.md` included; its update rides on this
   issue's branch. Never edit `main`. Check `main`'s CI is green first, so a
   pre-existing failure isn't blamed on your PR.

4. **Measure; don't inherit the premise.** Issue text is often wrong: #273 called four
   auditor false positives "genuine dangling references" and scheduled curation around
   it. Quantify over the KB first; report what you measured.

5. **Canary anything costly or gating.** A paid sweep (deep-research, Edison) runs *one*
   real unit end to end, artifact verified on disk, before any fan-out. A CI gate gets
   both branches proved: a temporary commit **on your branch, never `main`**, breaking
   one record; confirm the job reddens at the right step; revert and confirm that landed.

6. **Verify side effects, not exit codes.** `just qc` reddens for unrelated reasons — if
   so, scope to what you touched. Mutation-test new checks: substitute wrong
   implementations, confirm a test fails. Cover **both** sides of two-sided checks. A
   relative-path test can pass while auditing nothing — assert the sweep was non-empty.

7. **Commit, push, open a PR** saying what you measured, what changed, and what you
   deliberately didn't do.

8. **Review adversarially** — a separate read-only pass, subagent for independent eyes.
   Re-review commits landing after a review: review fixes are unreviewed code, and are
   where the last three defects came from (#322 → #333).

9. **File every finding as an issue**, won't-fix included. Fix what belongs in this PR;
   say what you left and why. If the review shows the premise was wrong, **close the PR
   unmerged** and re-file — a success, not a failure (#315 did this to #273).

10. **Stop and ask before every merge**, per PR. Report what shipped and what you filed,
    then wait for explicit go-ahead. This prompt does not authorize merges and cannot: a
    prompt you wrote is not the user's consent. Approved → squash-merge, delete the
    branch both sides, sync, re-reconcile.

Don't even ask while CI is red or hanging, the branch conflicts, findings are unresolved,
or the change would redden `main` — fix or report instead.

**Stop the loop** when only won't-fix and upstream-blocked items remain, or after 5
merges. Issues filed in step 9 never feed the same pass.

## Pause and ask when

A curation or schema decision has no obvious default; work would delete or rewrite
curated content; two readings mean materially different work; money would be spent; or an
@-mention seems needed (never without explicit per-mention permission). Ask one question
with a recommendation.

## Gotchas — fix these here when they stop being true

- `gh pr edit --body` fails: use
  `gh api repos/{owner}/{repo}/pulls/N -X PATCH -F body=@file` — literal braces.
- **Any** `fixed: #N` substring closes #N, including `Not fixed: #N`. Write
  `Deferred: #N`.
- `Closes #N` added to a PR body *after* creation closes nothing — the squash commit
  uses the original body. Put it there at creation, or close by hand.
- `git add` explicit paths only; `git add -A` has swept unrelated work into a PR.
- `just install` fails (#290): `uv sync --extra dev`.
- Duplicate YAML keys and `preferred_term`s are invisible to `linkml-validate` — caught
  by the tests, not the validator. Run both.
- Report honestly: failing test, show it; skipped step, say so.
