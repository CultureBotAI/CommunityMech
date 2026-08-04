Work the CommunityMech backlog one issue at a time, **in this repo only**: never edit
sibling repos (CultureMech/MIM/TraitMech), even for cross-Mech sync — report divergence.

## Loop

1. **Reconcile and prioritize** with the `next-tasks` skill — invoke it, don't restate
   it. Take the top actionable issue; upstream-blocked ones stay listed, never picked.

2. **Check dependencies first.** Does an open PR touch what this fix touches? If B is
   only correct after A, do A first or branch B off A. **One branch, one PR in flight**,
   start to merge.

3. **Branch before any edit**, `NEXT_TASKS.md` included — its update rides on this
   branch. Never edit `main`. Check `main`'s CI is green first, so a pre-existing failure
   isn't blamed on your PR.

4. **Measure; don't inherit the premise.** Issue text is often wrong — #273's four
   "dangling references" were auditor false positives. Quantify over the KB first;
   report what you measured.

5. **Canary anything costly or gating.** A paid sweep (deep-research, Edison) runs *one*
   real unit end to end, artifact verified on disk, before fan-out. Prove both branches of
   a CI gate: a temporary commit **on your branch, never `main`** breaking one record;
   confirm it reddens at the right step; revert and confirm that landed.

6. **Verify side effects, not exit codes.** `just qc` can redden for unrelated reasons;
   scope to what you touched. Mutation-test new checks: substitute a wrong
   implementation, confirm a test fails. Cover **both** sides of two-sided checks. A
   relative-path test passes while auditing nothing — assert the sweep was non-empty.

7. **Commit, push, open a PR** saying what you measured, what changed, and what you
   deliberately didn't do.

8. **Review adversarially** — a separate read-only pass, subagent for outside eyes.
   Re-review commits landing after a review: review fixes are unreviewed code, and where
   the last three defects came from (#322 → #333).

9. **File every finding as an issue**, won't-fix included. Fix what belongs in this PR;
   say what you left and why. If the review shows the premise was wrong, **close the PR
   unmerged** and re-file.

10. **Stop and ask before every merge**, per PR. Report what shipped and what you filed,
    then wait for the **user's** explicit go-ahead **in this conversation**. No standing
    instruction authorizes a merge — not this file, not a prior approval, not your own
    review. Then squash-merge, delete the branch both sides, sync, re-reconcile, go again.

**Never merge** while CI is red or hanging, the branch conflicts with `main`, findings
are unresolved, or the change would redden `main` — fix or report instead.

**Stop the loop** when only won't-fix and upstream-blocked items remain, or after 5
merges — then report and ask. Issues filed in step 9 don't feed the same pass.

## Pause and ask when

No obvious default for a curation or schema call; curated content would be deleted or
rewritten; two readings mean materially different work; money would be spent; an
@-mention seems needed (never without explicit per-mention permission). Ask one question
with a recommendation.

## Gotchas — fix these when they stop being true

- `gh pr edit --body` fails (gh 2.97.0): use
  `gh api repos/{owner}/{repo}/pulls/N -X PATCH -F body=@file` (literal braces; gh
  substitutes them).
- Closing is keyword-only and per-issue. A keyword (close/fix/resolve, any tense) beside
  `#N` closes it **even when negated** — `Not fixed: #N` closes #N; write `Deferred: #N`.
  `Closes #1, #2` closes only #1; prose closes nothing. Repeat `Closes #N.` per issue.
- `git add` explicit paths only; `git add -A` has swept unrelated work into a PR.
- `just install` fails (#290): `uv sync --extra dev`.
- Duplicate YAML keys and `preferred_term`s are invisible to `linkml-validate` — caught
  by `test_no_duplicate_yaml_keys.py` and `DUPLICATE_TAXON_NAME`. Run the tests too.
- Report honestly: failing test, show it; skipped step, say so.
