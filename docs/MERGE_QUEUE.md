# Merging through the queue

When `main` requires GitHub's native merge queue, a reviewed PR enters the queue
and its required checks run again against the candidate containing current
`main` and preceding queued changes. A green PR check run alone does not show
that this combined candidate passed.

After required PR checks pass, enqueue the reviewed revision with:

```sh
gh pr merge PR_NUMBER --repo CultureBotAI/CommunityMech --match-head-commit HEAD_SHA
```

Enqueueing is asynchronous. Before deleting the branch or cleaning its worktree,
confirm `state` is `MERGED`, `headRefOid` equals the reviewed `HEAD_SHA`, and
`mergeCommit.oid` is present:

```sh
gh pr view PR_NUMBER --repo CultureBotAI/CommunityMech --json state,headRefOid,mergeCommit
```

The queue selects the configured merge method. Avoid `--admin`, which bypasses
the queue. On failure, inspect the PR timeline and the `merge_group` Actions
run, fix the cause, and enqueue the updated revision after its PR checks pass.

The network integrity audit runs on queue candidates. PR comments remain limited to PR events, and paid repair suggestions remain an explicit manual workflow option.

Required workflow triggers and stable job names are checked by
`tests/test_merge_queue_workflows.py`. Coordinate job renames with the `main`
ruleset so the queue continues receiving every expected result.

References: [GitHub merge queues](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue)
and [`gh pr merge`](https://cli.github.com/manual/gh_pr_merge).
