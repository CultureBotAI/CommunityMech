# Whole-corpus stored-mapping check

The unchanged native `tests/test_gtdb_uncurated_blocks_match_the_tool.py`
passed on M5 after the three source-supported corrections in issue 2849:
**3 passed in 8.37 seconds, with no skips**.

Execution used published revision
`f39c0fe400740a754f2d006d17ffa8c8e82fae63`, Python 3.13.2, and the retained
NCBI2GTDB crosswalk SHA256
`761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd`.
The test file remained SHA256
`102ee759b9cd43c34d65d1b169affe6f0823400d40fa4571cdf59fa462306df0`.
There were no test, classifier, skip or threshold changes for this run.

The same retained runner first collected the three tests, then executed the
whole module in a fresh isolated M5 worktree with its own frozen offline
environment. Both original record canary checkouts were preserved. All captured
record, classifier, test, path-helper, lockfile and runner hashes remained equal,
and the before/after record-file inventories matched. Enumeration included
ignored YAML files under the three native record roots.

| Stage | Result | Evidence |
| --- | --- | --- |
| Native collection plan | 3 tests collected, exit 0 | [log](corpus-plan-001.log.txt), [receipt](corpus-plan-001.receipt.json) |
| Native execution | 3 passed, exit 0, no skips | [log](corpus-run-001.log.txt), [receipt](corpus-run-001.receipt.json) |

The module checks that it actually read a nonempty corpus, that stored mappings
disagreeing with the native tool are explicitly curated, and that every curated
block has a reason. The separate Sulfobacillus, BR1 and Terrabacter source-backed
canaries establish the particular mapping decisions; this aggregate test alone
does not validate their scientific evidence.

This is one maintained whole-corpus module, not full QC or a complete scientific
review. The separate grounding-status backlog in issue 2848 remains. Raw evidence
is retained privately on M5 and in the verified local mirror; public derivatives
record the exact native command, source hashes, runtime and raw/public log hashes.
