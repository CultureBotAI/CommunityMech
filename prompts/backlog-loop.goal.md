Work the CommunityMech backlog, one issue at a time, **in this repo only** — never edit
sibling repos (CultureMech/MIM/TraitMech), even for cross-Mech sync; report divergence.

## Loop

1. **Reconcile and prioritize** with the `next-tasks` skill — invoke it, don't restate
   it. Pick the top actionable issue; upstream-blocked items stay listed, never picked.

2. **Check dependencies before starting.** What does this fix touch, and does an open
   PR touch it? If B is only correct after A, do A first, or branch B off A and say so.
   **One branch and one PR in flight at a time**, start to merge — no parallel PRs.

3. **Branch before any edit**, `NEXT_TASKS.md` included; its update rides on this
   issue's branch. Never edit `main`. Check `main`'s CI is green first, so a
   pre-existing failure isn't blamed on your PR.

4. **Measure; don't inherit the premise.** Issue text is often wrong: #273 called four
   auditor false positives "genuine dangling references" and scheduled curation around
   it. Quantify over the KB first, and report what you measured.

5. **Canary anything costly or gating.** A paid sweep (deep-research, Edison) runs
   *one* real unit end to end and verifies the artifact on disk before any fan-out. A
   CI gate gets both branches proved: a temporary commit **on your branch, never
   `main`**, breaking one record; confirm the job reddens at the intended step; revert,
   and confirm the revert landed before merging.

6. **Verify side effects, not exit codes.** `just qc` is seven recipes over 311
   records and can redden for unrelated reasons — if so, scope to what you touched.
   Mutation-test new checks: substitute wrong implementations, confirm a test fails.
   Cover **both** sides of two-sided checks. A test on a relative path can pass while
   auditing nothing — assert the sweep was non-empty.

7. **Commit, push, open a PR** saying what you measured, what changed, and what you
   deliberately did not do.

8. **Review adversarially** — a separate read-only pass, subagent for independent eyes.
   Re-review commits that landed after the previous review: review fixes are themselves
   unreviewed code, and that is where the last three defects came from (#322 → #333).

9. **File every finding as an issue**, won't-fix included. Fix what belongs in this PR;
   say what you left and why. If the review shows the premise was wrong, **close the PR
   unmerged** and re-file — that is a success (#315 did this to #273).

10. **Squash-merge, delete the branch both sides**, sync, re-reconcile, go again.
    Running this prompt authorizes merges *inside* this loop only.

**Do not merge — stop and report — if** CI is red or never finishes, the branch
conflicts with `main`, review findings are unresolved, or the change would redden
`main`.

**Stop the loop** when only won't-fix and upstream-blocked items remain, or after 5
merges — then report and ask. Issues you filed in step 9 never feed the same pass.

## Pause and ask when

A curation or schema decision has no obvious default; work would delete or rewrite
curated content; two readings mean materially different work; money would be spent; or
an @-mention seems needed (never without explicit per-mention permission). Ask one
question with a recommendation.

## Gotchas — fix these here when they stop being true

- `gh pr edit --body` fails (gh 2.97.0): use
  `gh api repos/{owner}/{repo}/pulls/N -X PATCH -F body=@file` — literal braces; gh
  substitutes them.
- `Not fixed: #N` in a commit **closes** #N — GitHub parses `fixed: #N`. Write
  `Deferred: #N`.
- `git add` explicit paths only; `git add -A` has swept unrelated work into a PR.
- `just install` fails (#290): `uv sync --extra dev`.
- Duplicate YAML keys and duplicate `preferred_term`s are invisible to
  `linkml-validate`; they are caught by `test_no_duplicate_yaml_keys.py` and
  `DUPLICATE_TAXON_NAME`, so run the tests, not just the validator.
- Report honestly: failing test, show it; skipped step, say so.
