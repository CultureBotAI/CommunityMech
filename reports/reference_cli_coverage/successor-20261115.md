# Current native reference controls after the shared annotation repair

The governed SupportingReference repair makes the former gap assertions fail as
intended. Existing issue [#476](https://github.com/CultureBotAI/CommunityMech/issues/476)
explicitly owns replacing that test and its stale explanation when the shared
annotations land. This checkpoint replaces those assertions with current native
controls; it does not change schemas, dependencies, records or cached sources.

The historical `reports/reference_cli_coverage/probe.py` and existing reports and
reviews remain byte-identical. An ignored/hidden-inclusive search confirmed that
three immutable review bundles and retained report artifacts bind that probe.
Its SHA256 remains `8e3782125ca5f5b022ec94527993bebca3e9a74fe93dc9d52037678dd4c127bd`.

The new `scripts/adhoc/probe_reference_cli_successor_20261115.py` uses the maintained
`scripts/reference_assertion_coverage.py` tracer without changing it. The native
CLI traverses each real record and its substring matcher compares unchanged cached
source bytes. Private copies retain native DOI filename casing for portability.
Acquisition, enrichment and writes during native dispatch are refused. Each run
also verifies unchanged canonical inputs and copied fixture inputs.

## Observed controls

All runs used Git base `78ae46cd7720e504f24366b509b5051a997ea999` with the reviewed
new helper and two modified tests in the working tree. These receipts identify
the actual base and hash the working helper; they do not imply that the base commit
already contained this test repair. Installed versions were LinkML 1.9.3 and
linkml-reference-validator 0.2.1.

| Actual record | Snippet occurrences compared in every case | Discussion occurrences | Native issue counts / exit codes, in order |
|---|---:|---:|---|
| Phormidium_Alkaline_Consortium | 23 / 23 | 2 | 0, 1, 0, 1, 0 |
| Alseth_FourSpecies_Pathogen_Phage_Community | 28 / 28 | 1 | 0, 1, 0, 1, 0 |
| PHA_MixedCulture_Phage_Succession_Community | 24 / 24 | 0 | 0, 1, 0 |

The first three cases are the original record, one planted interaction-evidence
mismatch, and restoration. Records with discussions additionally exercise one
planted discussion mismatch and restoration. Every mutation produced exactly the
intended mismatch path; every restoration matched. The CLI's `Total checks`
counter remains an issue count (0 or 1 here), separate from the independently
inventoried and actually compared snippet occurrences. These are lexical controls,
not a scientific support verdict or a whole-corpus reference pass.

Phormidium ran first end to end; its persisted receipt, all five native case logs,
counts and unchanged-input flags were verified before the other two actual probes.
The two original test modules first reproduced exactly three stale failures and
five passes. After the repair, the two modules, maintained measurement regressions
and writer audit passed: **35 passed**. Black, Ruff and diff whitespace checks also
passed. No new canonical-writer exception was needed.

## Reproduce and retained evidence

For one record, choose a new output directory beneath this checkout's `.temp`:

```bash
.venv/bin/python scripts/adhoc/probe_reference_cli_successor_20261115.py \
  --record Phormidium_Alkaline_Consortium \
  --output .temp/reference-coverage-successor-20261115/phormidium-new
.venv/bin/python -m pytest tests/test_reference_cli_coverage.py \
  tests/test_reference_validator_actually_validates.py \
  tests/test_reference_assertion_coverage.py tests/test_writers_leave_a_trace.py -q
```

Private receipts and logs are retained in the local successor checkout under
`.temp/reference-coverage-successor-20261115/`; they have not been copied to M5.
The receipts contain exact input hashes and per-occurrence native measurements.
No source text is added to this public report.

| Retained path relative to that private directory | SHA256 |
|---|---|
| `before.log` | `2f4f62bec1702a9b48e73198a1c7dae7e75c12669f0a78718b5d0113ec249121` |
| `after-001.log` | `c3ee762bce4a262eb92164c4b57a0f677e4d84e1639d552ba1148bf9ab36e5a6` |
| `phormidium-001/receipt.json` | `eb5d28d2bb7f0e606aa05ea356a571ec1bcea95faf8d2d51b4e3c105cfd126d4` |
| `alseth-001/receipt.json` | `980b4b7c524a3fa37fc1ab0e1cf88b5df277f38b982707c9802d7138a7c1b48b` |
| `pha-001/receipt.json` | `36d52eeb872718164a5fb681cc13d0bb2fa54847e6b76b0d95dc6efa485bb3b4` |

The successor helper SHA256 was
`08a3e5575a6d87a2707f6902bc8ccd2e540b5d1ee70ecde25fd1014aac67f335`;
the unchanged maintained tracer SHA256 was
`363cffb652bdd18733cd5c8c2d22abf663cb3314410ef237e531a8b2f3298908`.
