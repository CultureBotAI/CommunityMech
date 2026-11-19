# Backlog loop: select and deliver the right issue end to end

**Use:** A native agy/Codex/Claude goal prompt, not a project slash command.
Keep it below 4,000 ASCII characters, without YAML frontmatter. `$ARGUMENTS`
may name a repo, issue, theme or `report`; otherwise inspect the full backlog.

Finish the agreed batch through merge, resolved/filed findings, branch/worktree
cleanup and green tests. Follow `AGENTS.md`/`CLAUDE.md` and optional
`prompts/backlog-loop-local.md`. Provider credits and curated-data mutation
require explicit authorization.

## 1. Reconcile before choosing

- For an adopted freshness contract, run the packaged pre-goal gate before
  inventory, including no-change goals. Consume its immutable fetched-HEAD
  inventory; holds block entry. Report unadopted sessions; candidates are inert.
- Read `CLAUDE.md`, inspect Git status, and preserve unrelated work.
- Query all remote issues and PRs with explicit limits; print totals before
  ranking and verify pagination completeness.
- Read full bodies, state reasons and all comments of cited or selected items.
  Reproduce on current fetched default; titles and stale clones are not proof.
- Reconcile overlaps, dependencies and blockers; use three-dot PR diffs.
- Rank silently-wrong behavior first, then blast radius, blockers, missing
  regression gates, and cost. State what was not inspected.
- If no item was named, recommend one and await choice; also pause for
  decisions whose alternatives materially change the result.

## 2. Implement in isolation

- Fetch `origin/main`; branch before edits in a dedicated worktree under
  gitignored `<repo>/.temp/`, or `~/agent-work/<repo>/` for a separate clone.
  Never use `/tmp`, `/private/tmp` or `$TMPDIR` for campaigns, clones, helpers or handoffs;
  only disposable caches and pytest temp may. Never use a dirty shared checkout.
- Fix the cause; add a regression and prove it fails on the old behavior.
- Mutators default to dry-run and require explicit apply/write. Do not make
  network/provider calls merely to test integration.
- Run focused tests, native and relevant CI checks, and `git diff --check`.
  Inspect skips; a green command finding zero targets is not evidence.
- Review scope and stage explicit files; never sweep runtime artifacts.

## 3. Commit, push, and review

- Commit cause/issue. Push each branch the same day, even without a PR; verify
  its remote head. Unpublished commits block goal closure. Use explicit refspecs.
- Perform a separate read-only adversarial review. Check description versus
  diff, false factual claims, edge cases, whether the regression test kills the
  old behavior, CI path filters/skips, security-sensitive workflow changes,
  generated artifacts, and every vendored copy named by a manifest.
- Reproduce each finding. File every confirmed finding as an issue in the repo
  where it lives, even when it will be fixed immediately. Triage which findings
  belong in this PR, fix those, rerun checks, and report deferred ones.

## 4. Merge and finish

- Without prior merge authorization for this batch, pause with PR, checks,
  findings and merge order. Prior approval does not cover newly found work.
- Immediately before each merge, refresh the base and recheck mergeability and
  CI. Merge only green, non-draft PRs in dependency order.
- After actual merge, adopted freshness requires its post-merge gate before
  closure: fetch/inspect/safe-FF, fetched-HEAD equality and merge ancestry.
  Preserve frozen evidence; live claw requires reviewed deployment.
- Verify closing keywords closed the intended issues. Delete remote/local
  branches and remove worktrees only after merge; never touch another session's
  tree.
- Re-query open issues and PRs. Report merged URLs, exact tests, filed follow-ups,
  remaining blockers, cleanup, and whether the working tree is clean.

Completion means the selected scope is merged and verified, not merely coded.
