# Count Guard Follow-Up Review

PR #2002; review issue #2004. This self-review supersedes the earlier publication
review's no-additional-defect observation for this test-contract finding only.
The saved scientific-scope review and all earlier reports remain unchanged.

## Confirmed Defect

On `80e9785b`, the aggregate `len(without) <= 4` assertion failed because five of
911 stored GTDB blocks lacked `total_genomes`. Local reproduction with
`pytest tests/test_gtdb_support_counts.py -q --no-cov -x` reported one failure,
seven passes, and one mapping-dependent skip. A failure marker in the cancelled
superseded CI run prompted this local reproduction; that cancelled run is not
claimed as completed verification.

The later completed pre-fix run confirms this was its only failure:
https://github.com/CultureBotAI/CommunityMech/actions/runs/38630622095
reported 1 failed, 4897 passed, 86 skipped and 8 deselected. All other required
PR checks passed for that pre-fix head; those results do not certify a new head.

The aggregate allowance both rejects valid source-only curation and can miss
lost computed denominators below its quota. The three source-only assignments
are the Rhodanobacter glycinis pin and the two spring assignments. None asserts
a voting fraction or numerator. Supplying invented counts would falsify their
provenance.

## Repair And Adversarial Checks

The test now evaluates each missing denominator. Source-only assignments need
an explicit curator flag, nonempty rationale and source/identity provenance,
and no fraction, numerator or denominator field. Other omissions fail. Existing
type, range and count-arithmetic checks remain unchanged.

Two pre-existing fractional pins remain bounded by exact semantic SHA-256
hashes and record/taxon identities, verified against main `8df89370`. This is
strictly narrower than the previous allowance for any four omissions. It does
not newly certify their old fractions, permit altered pins, or add exceptions
for the spring record. Future curation of those legacy blocks requires an
explicit reassessment of the frozen cases.

Ten control/mutation/immediate-restoration cases cover a lost computed count,
a curator-flagged vote without a count, missing curator/rationale/source fields,
fabricated fractions/numerators, explicit null counts, changed legacy fractions
and copied legacy identities. The small control contains only three blocks, so
the missing-denominator mutation is below the old aggregate cap.

The focused module passed 38 tests with nine external-mapping skips. The wider
regression command and exact result are retained in `count-guard-tests.json`;
`count-guard-lint.json` records Black, Ruff and mypy results. Their test-input
hashes bind the receipts to the reviewed file bytes, including when the command
ran before that edit was committed.

The wider run passed 149 tests with 19 skips, all explicitly caused by the
unavailable external NCBI2GTDB mapping. Black, Ruff and mypy passed. The native
coherence, schema/count gates and spring identity regressions are included in
that run; this remains proportional local coverage, not a full local suite.

## Limits

No canonical YAML, evidence caches, production schema or validator was changed
for this finding. This test checks representation and provenance metadata, not
the scientific truth of a curator's source claim. The two legacy pins remain
historical compatibility cases rather than new evidence-backed assignments.

An initial wider local attempt without `UV_NO_SYNC=1` failed in a subprocess
environment setup, before its schema control could pass. It is not counted as
a code regression or successful coverage; verification uses the documented
locked curation environment and reports unavailable external mappings as skips.
Final-head GitHub Actions and merge-queue results are separate release gates.

Self-review is not independent approval. Issues #1841 and #476 remain open;
neither this guard repair nor the provenance archive completes corpus curation.
