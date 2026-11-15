# Mapping-correction integration checkpoint

The combined Phase 2 tree at
`301f35b8d9db679f3067297317356081fa305959` contains the actual M5 applications,
append-only history, saved partial assessments and source proofs for the
Sulfobacillus, Mycobacterium, BR1 and Terrabacter corrections. This checkpoint
records local integration checks, separately from each M5 canary and the failed
code006 aggregate. It does not declare full QC or scientific review complete.

BR1 uses the exact study-strain assembly and its GTDB R220 history. Its native
crosswalk lookup remains unavailable; the curated mapping does not invent a
genome count. Terrabacter uses the independently verified genus route: the
study stock remains distinct from the twelve-genome genus population. Both
retain their earlier scientific limitations. The batch144 successor check
requires the saved actual applications and source evidence while preserving
the immutable historical scientific ledger and unchanged biological claims.

| Check | Actual result | Raw log SHA-256 |
|---|---|---|
| Eight focused integration modules | 63 passed, 12 deprecation warnings, 31.70 seconds; exit 0 | `64266afc7a071dfe70cd067247de002e402f42186090eb259c2be2ef95c8001f` |
| `just --no-dotenv lint` | Passed; exit 0 | `63e0dbecd51f9a1714dbe5e18bfcd19d48fb982a72c9935ecee41feb13d33d79` |
| One BR1 native render canary | Nonempty page persisted; exit 0 | `5913155a2485a44e619704f8805bc77d3a6fd9cda7b36d8fede94d5ffed19c6e` |
| Native community render batch | 512 community pages plus indexes/exports; exit 0; no tracked `docs/` changes | `577f0a6bece144dc8be76b1f865c465176f46cabf0814021694aeacd14c20249` |

The focused command ran `test_causal_review_batch144`,
`test_batch144_mapping_successor`, `test_terrabacter_mapping_guard`,
`test_terrabacter_evidence_snapshot`, `test_br1_grounding_guard`,
`test_br1_evidence_snapshot`, `test_writers_leave_a_trace` and
`test_writer_delegated_trace`. It exercised the actual integrated successors,
source/log/review mutation refusals and delegated-writer trace controls.

All commands used the existing
`scripts/adhoc/run_phase2_schema_checks_20261115.py` launcher. Its immutable
JSON, log and exit triplets are retained under `.temp/phase2-schema-20261115/`
with prefixes `integrated-mapping-301f35b8-001`,
`integrated-mapping-lint-301f35b8-001`,
`mapping-render-canary-301f35b8-001` and
`mapping-render-batch-301f35b8-001`. Execution used local Python 3.13.12 and
the frozen offline environment.

The render canary was inspected before the batch. Its page SHA-256 is
`11f7fca0fe39f027b0a8a59e2455a7ff472660354fcf879cc2fff349bd48a66d`.
That isolate page is outside the maintained community-render population; the
untracked probe was preserved, without changing its bytes, under
`.temp/phase2-schema-20261115/mapping-render-canary-301f35b8-001-output/`.
No additional published page is introduced by this check. The batch used the
same launcher/environment and native module, with its normal community scope.

The native stored-status reproducibility backlog remains #2848. These local
controls do not replace a full native M5 QC run on the final combined revision,
the separate measured reference run, or the subsequent all-record scientific
review campaign.
