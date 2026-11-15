# Code006 existing-source prerequisite and canaries

Code006 uses revision `c9e151eb9f22afb5c531dd5a8b3346ce1d58b12a` in the
dedicated M5 checkout. Code005 had finished and its failed result, unchanged
cache archives and verified local metadata mirror were preserved before this
checkout advanced. The frozen environment remained Python 3.13.2;
`uv.lock`, `pyproject.toml` and `.python-version` did not change.

The preserved completion checkout already contained
`.temp/m5-completion-20261114/yolo-sources/NCBI2GTDB.tsv.gz`:

- Size: 2,895,086 bytes.
- SHA-256: `761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd`.
- Native `gzip -t` passed.

An additive, exclusive private directory in the current M5 checkout now holds
the exact bytes at
`.temp/m5-completion-20261114/phase2-code006-kg-microbe/data/raw/NCBI2GTDB.tsv.gz`.
The copy did not overwrite an existing file. Source and destination hashes
matched before and after the actual-source canary. No acquisition or source
update was performed.

The native resolver in `scripts/gtdb_ground.py` supports `KG_MICROBE_DIR` and
requires `data/raw/NCBI2GTDB.tsv.gz` beneath it. Code006 launcher processes receive
that setting pointing to the new private directory. No profile or live
configuration file was edited. The stock driver receipts do not include this
variable in their `environment_overrides` field; the separate retained
`launcher-environment.txt` records the invocation assignment. No runtime field
was retroactively added to a receipt.

## Verified prerequisites

| Native operation | Observed result | Public evidence |
|---|---|---|
| Plan | Exit 0; every listed recipe remains DRY RUN | [Receipt](technical-evidence/phase2-code006-plan.receipt.json) |
| Historical Git prerequisites | Exit 0; nine exact commit/tree identities verified | [Receipt](technical-evidence/phase2-code006-history.receipt.json) |
| Actual-source GTDB canary | One test passed, no skip, in 0.12 seconds | [Receipt](technical-evidence/phase2-code006-gtdb-canary.receipt.json), [log](technical-evidence/phase2-code006-gtdb-canary.log.txt) |
| Strict record canary | One record scanned, zero errors; exit 0 | [Receipt](technical-evidence/phase2-code006-canary.receipt.json), [log](technical-evidence/phase2-code006-canary.log.txt) |

The GTDB canary was the existing
`tests/test_gtdb_support_counts.py::test_the_species_path_reports_the_denominator_but_no_numerator`.
It exercised the native mapping resolver and classifier against the supplied
source, including its expected species denominator and absent numerator. Its
98-byte native log has SHA-256
`3be6ffcaecf85b5bd3eef3693ab214b0e7c9eb4e36d117fcf1825652de5eb298`.
The strict canary used the same launcher environment and the current switchgrass
record. Its 520-byte native log has SHA-256
`1505e076747814a0c0f25d88dc184e118d0ea5b16baa90037cb1d7d60f1d65b9`.

The source-layout metadata remains private under
`.temp/m5-completion-20261114/phase2-code006-kg-microbe/` on M5 and in the local
metadata mirror. `mapping-hashes.sha256` has SHA-256
`7a61e2f9779cb2c53177a0558ba796f9d6b74f297128a456d45c74f9e81d1b85`;
`launcher-environment.txt` has SHA-256
`42308b352875907428085cb42114cc7603f698a1b581ee021a90db268c5f952b`.
The crosswalk body was not included in that metadata transfer or this public
report. All 17 prerequisite mirror hash checks passed.

The reference-cache before archive remained 47,403,520 bytes with SHA-256
`2284f07a11f0e6482ce2cee3d6dd5cb1f7bde4e065554203c6a83c8aa273162b`.
Full native `qc-references` started at `2026-11-15T04:15:59Z`, with dependencies
enabled and a clean tracked checkout. Its outcome is pending at this checkpoint.
These canaries establish their own bounded behavior and persistence; they do
not certify the full test suite, scientific claims or final reference coverage.
