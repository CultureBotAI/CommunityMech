# Fifteen-record integration at fcb237b9

Revision `fcb237b9ed57f7d0da49d8944228b3fe4eb4b162` integrates three reviewed M5
batches: fifteen records, twenty-two selected taxonomy occurrences and twenty-seven
native inline events, plus one native history sidecar per record. All 120 required
record-level commands passed on their respective recorded execution revisions.
Each immutable assessment is a bounded technical diagnostic with
`scientific_review: false`; none certifies a study-stock genome or a full scientific
record. Existing paper, experimental, ontology and mechanistic limitations remain.

| Batch and actual evidence | Records | Selected occurrences | Native commands | Saved input audit |
|---|---|---:|---:|---|
| [Genus batch](../gtdb-code006-20261115/genus-three-001-outcome.md) | 342, 390, 406 | 6 | 24 passed | 171 inputs / 7,199,804 bytes |
| [Ambiguity batch](../gtdb-ambiguity-20261115/status-three-outcome-001.md) | 373, 365, 003 | 4 | 24 passed | 168 inputs / 5,803,554 bytes |
| [Species batch](../gtdb-species-status-20261115/remaining-nine-outcome-001.md) | 053, 313, 362, 396, 397, 426, 431, 517, 522 | 12 | 72 passed | 454 inputs / 9,502,843 bytes |

The input counts are separate complete namespaces, not mutually exclusive file
sets. A root reviewer independently reproduced each native saved-pair audit:
schema validity, exact Markdown derivation, captured file hashes and unchanged
inputs. Complete checkpoints on M5 and the local machine preserve each namespace
and both saved files before historical callers changed:

| Batch | Complete checkpoint | Local manifest SHA-256 |
|---|---|---|
| Genus | 173 files / 7,364,198 bytes | `e2f145cbfa25bc123998d41591be931fcb2e916a6dbf77ff4271c4b206445a9d` |
| Ambiguity | 170 files / 5,964,464 bytes | `236d4a987be6aee6e32225e79b3c66dd4a7ef88009da4ca858ff5d6c7e4253fa` |
| Species | 456 files / 9,951,391 bytes | `c08471f8baf7aa799c5d884845aac5df9ba205501efaa387d40060132b163a19` |

The shared strict proof requires each exact historical baseline, current record,
source/native result, actual application receipt, saved review, history sidecar and
all eight command receipts/logs/exits. It verifies unchanged biological content and
prior history before historical assertions can inspect the admitted predecessor.
Unknown changed paths remain rejected. The species batch retains the earlier
396/397 remediation chains; all prior Phase 2 and other scoped successor paths
remain in the combined callers.

The source branches already completed their real proof controls: 51 genus cases,
51 ambiguity cases and 144 species cases, each after its actual canary. These
distinct branch outcomes remain bound to their original logs. The species branch's
first historical run failed an outdated FT92W mapping expectation under #2505;
the saved predecessor now retains that historical assertion while new assertions
check the current mapping. Its restored six-test module passes. The original failed
run is retained, not recast as a passing aggregate.

## Combined verification

The integration run selected all fifteen affected historical modules, the shared
actual-proof module with all four existing cases, the strict core and species
registry controls, and the positive actual-proof case for each of the fifteen new
records. It passed **225 tests**, with twelve existing LinkML/Pydantic deprecation
warnings, in 127.35 seconds. No test was skipped or deselected in this command.
The already completed new-batch mutation matrices were not repeated merely to
increase a count. Native lint passed Black on 733 files, Ruff and mypy on 52 source
files.

| Retained run | Result | Log bytes | Log SHA-256 |
|---|---|---:|---|
| `integrated-fifteen-fcb237b9-001` | Exit 0; 225 passed | 1,074 | `f0e8f962dfe9bd6f4f83583f2f5d64729169f2c83f5d1e1b98419f0d32cd8a1a` |
| `integrated-fifteen-lint-fcb237b9-001` | Exit 0; native lint passed | 219 | `1592c3756d0b2d61b57918b6e87ba70c1378621b0fcfb7bfe1bf1aad01682c5d` |

The unchanged [command recorder](../../scripts/adhoc/run_phase2_schema_checks_20261115.py)
retains exact commands, revision, lockfile hash, start/finish times and raw
`.json/.log/.exit` triplets under `.temp/phase2-schema-20261115/`. Both runs recorded
one untracked source-plan draft, `species-ht-light-source-context-001.yaml`; there
were no tracked changes, and that draft was not an input to the selected checks.
No files were edited during these runs.

There are now **27 integrated taxonomy corrections**, of which **23 belong to the
historical 126-record repair partition**. The four earlier source-route canaries
were outside that partition. This leaves 103 partition records uncompleted at
this checkpoint. Source plans and concurrent branch work are not counted as
completed. In particular, the next genus batch and the source-note transition
work remain separate until their complete proofs are integrated.

Full combined M5 `just qc`, final reference measurements and maintained product
regeneration remain outstanding. The last full QC failure at `c9e151eb` and its
later stages marked **NOT RUN** remain unchanged. The separate reference sweep
did make 10,836 actual comparisons and retained 109 issues; lexical matching is
not scientific approval. The all-record scientific campaign has not resumed.

Review follow-up [#2873](https://github.com/CultureBotAI/CommunityMech/issues/2873)
records malformed duplicate-ID acceptance in the old transfer-path helper. Its
executed bytes and reproducer remain preserved; actual batch IDs were unique and
the complete saved namespace passed verification. An additive fix is prepared for
future transfers, separately from this recorded revision. No merge of Phase 2 is
authorized by this report.
