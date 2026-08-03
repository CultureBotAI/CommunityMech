Work the CommunityMech backlog to completion, one issue at a time.

## Loop

1. **Reconcile, then prioritize.** Never relay `NEXT_TASKS.md` verbatim — check every
   claim against `gh pr list --state merged`, `gh issue list`, and the code. Classify
   each: DONE / actionable / in-flight / upstream-blocked. Rank the open issues by
   value and pick the top actionable one. Update `NEXT_TASKS.md` every pass.

2. **Respect dependencies before starting.** Ask what this fix touches and whether an
   open PR already touches it. If issue B is only correct after PR A, do A first or
   branch B off A and say so in the PR body. Never run two PRs editing the same
   detector, slot, or workflow in parallel. State the chain when you report.

3. **Branch before the first edit.** Never commit to `main`.

4. **Measure; do not inherit the premise.** Repeatedly earned here: issue text is often
   wrong. #273 called four auditor false positives "genuine dangling references" and
   scheduled curation around it; #276's premise was wrong too. Quantify over the whole
   KB before proposing a fix, and report what you measured, not what you assumed.

5. **Verify side effects, not exit codes.** Run `just qc`. For anything that gates CI,
   prove *both* branches live: a temporary canary commit that breaks one record,
   confirm the job reddens at the intended step, then revert. For new detectors,
   mutation-test — substitute plausible wrong implementations and confirm a test
   fails. Check both sides of any two-sided check (source *and* target). A test using
   a relative path can pass while auditing nothing; assert the sweep was non-empty.

6. **Commit, push, open a PR.** The body states what you measured, what changed, and
   what you deliberately did not do.

7. **Review adversarially**, as a separate read-only pass — not a restatement of what
   you just wrote. Spawn a subagent for independent eyes. Re-review commits that
   landed *after* the previous review: review fixes are themselves unreviewed code,
   and that is where the last three real defects came from.

8. **File every finding as a GitHub issue**, including "won't fix". Then triage: fix
   what belongs in this PR, leave the rest filed, and say which is which and why.

9. **Merge** (squash) once CI is green and findings are addressed, **delete the branch**
   local and remote, sync `main`, re-reconcile, and go again.

## Pause and ask when

- A curation or schema decision has no obvious default ("should hosts be taxonomy
  members?").
- The work would delete or rewrite curated content.
- Two readings of an issue lead to materially different work.
- A change would redden `main`, or an @-mention seems needed — never @-mention anyone
  without explicit per-mention permission.

Ask one concrete question with a recommendation, then proceed on the answer.

## Gotchas

- `gh pr edit --body` is broken here. Use
  `gh api repos/OWNER/REPO/pulls/N -X PATCH -F body=@file`.
- "Not fixed: #N" in a commit **closes** #N — GitHub parses the substring `fixed: #N`.
  Write "Deferred: #N".
- Use explicit paths with `git add`; never `git add -A` (it has swept unrelated work
  into a PR).
- `just install` is broken; use `uv sync --extra dev`.
- `linkml-validate` is blind to duplicate YAML keys and duplicate `preferred_term`s.
- Report honestly. If a test fails, show it. If you skipped a step, say so.
