# Causal Graph Review Records

Each batch retains a decision ledger, validation outputs and an explicitly
source-based self-adversarial review. These records are not independent approval
or proof that every graph is complete. The current inventory and summary distinguish
`reviewed`, `pending` and `needs_research`.

## Connectivity Census Correction (2026-10-06)

The historical test survey unioned names, labels and CURIEs for pairwise endpoints.
This could credit every strain sharing a genus ID even when an endpoint named only
one strain. Batch43 reuses the already strain-aware readiness resolver; production
auditor behavior is unchanged. Historical raw survey outputs remain unchanged, but
their `credited_solely_by_the_rule` counts must not be interpreted as exact
strain-resolved counts. [Batch43 validation](validation-20261006-batch43.json)
records both algorithms on both the pre-edit and post-edit corpus, separating this
measurement correction from the CF313 scope change. See [issue 1472](https://github.com/CultureBotAI/CommunityMech/issues/1472).

## Reference-Validator Correction (2026-10-06)

Some historical batch reports incorrectly interpret `Total checks: 0` as zero
executed checks or a no-op. **That interpretation is withdrawn.** In installed
`linkml-reference-validator` 0.1.7, this CLI counter is the number of reported
validation issues. A zero means no issues reported, not that no snippets were checked.

[Correction receipt](reference-validator-correction-20261006-batch42.json) preserves
the installed-code evidence, passing positive/negative canaries, baseline failure
comparison and an ignored/hidden-inclusive inventory of candidate historical
statements. Historical raw outputs remain unchanged. Candidate text matches include
correct negations and are not all errors. See [issue 1469](https://github.com/CultureBotAI/CommunityMech/issues/1469).

The validator still has coverage limits: `SupportingReference` discovery is tracked
in [issue 476](https://github.com/CultureBotAI/CommunityMech/issues/476). The installed
fetcher does not combine supplement sidecars with the article cache. Batch42's
Fucoidan record therefore has 14 unchanged taxonomy-snippet findings, reproduced at
the pre-edit head; those snippets match its separate supplement sidecar. This is
an actual reference-CLI failure, not a pass or independent verification of the
original spreadsheet. No supplemental text was copied into the article cache.
The separate snippet auditor reports 35 matches and 15 mismatches for Fucoidan:
the same 14 taxonomy excerpts plus one discussion excerpt. Its output also matches
the baseline exactly; its exit code of zero does not mean an all-match result.

Textual matching also does not establish scientific support or independent source
provenance. In particular, selected `.txt` excerpts have a separate trust limitation
tracked in [issue 1362](https://github.com/CultureBotAI/CommunityMech/issues/1362).
