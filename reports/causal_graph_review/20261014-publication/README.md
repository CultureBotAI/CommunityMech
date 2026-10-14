# Batch129 Publication Review

PR: https://github.com/CultureBotAI/CommunityMech/pull/2002

Scope: adversarial self-review of the diff from `8df89370` to `bbf94e02` and
its publication provenance. This is not independent approval, a new scientific
certification, or completion of the full-corpus review.

The authoritative scoped record review remains unchanged:
`reviews/structured/20261014T200439Z-spring-parent-rank/review.yaml`
(with its derived `review.md`).

## Finding And Fix

Issue #2003 tracks the pre-merge risk that squash-and-delete would stop
advertising the saved review's source revision. The non-moving annotated tag
`review-provenance/20261014-batch129` retains snapshot
`bbf94e02b72dfc254f55e4fd08ee9e524c12ce35` and its source ancestor
`a7eaa4c339569107d60c25c409ba3599ce27a599`.

`archive-verification.json` records a fresh remote clone with no shared object
database. All 49 attested input hashes match the archived snapshot. Of these,
45 also match the earlier source base; four later verification receipts do not.
That distinction preserves the original working-tree attestation without
falsely converting it into committed-byte provenance at the earlier base.
The published annotated tag object is
`5b1f8e60773ebc096f4e7661f72f3448afad3d5b`.

Replay against a fresh clone of that tag:

```bash
.venv/bin/python reports/causal_graph_review/20261014-publication/verify_archive.py \
  /path/to/fresh-clone --output /path/to/new-receipt.json
```

The helper refuses to overwrite an existing receipt. Keep the archive tag after
topic-branch deletion. Remote tag availability after cleanup is a final release
check, not something this pre-merge receipt can prove in advance.

## Reassessment

The reviewed diff consistently replaces the unsupported genus in the roster and
existing graph participant, with an explicit parent-only identity boundary. It
preserves the three node names, zero-arrow topology, exact primary excerpts,
unresolved cell identity and metabolic-coupling limits. The earlier source
manifest and scoped review contain the inspected source passages and limitations.
No additional in-scope data defect was found in this pass.

Fresh command on `bbf94e02`:

```bash
.venv/bin/pytest tests/test_causal_review_batch107.py \
  tests/test_causal_review_batch127.py tests/test_causal_review_batch128.py \
  tests/test_causal_review_batch129.py tests/test_causal_review_inventory.py \
  -q --no-cov
```

Result: 64 passed in 4.50 seconds. Original validation receipts remain immutable.
Exact final-head CI and merge-queue results must be checked separately on the PR;
this report does not claim those future results or a full local test run.

Issue #1841 remains open for lower-rank and imaged-cell identity and coupling.
Issue #476 remains open for shared-schema Discussion evidence traversal; the
prior explicit 22-snippet check compensates only for this scoped record.
Neither issue is closed by retaining provenance. Full-corpus inventory still
has 54 records needing research and two pending reviews.
