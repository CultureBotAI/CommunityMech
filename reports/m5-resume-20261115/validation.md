# Coverage inventory validation and reproduction

The inventory was generated before its publication commit, while HEAD was
`68699871415fda3c9eebf20382a315f9f3c7b17a`. The helper's exact SHA-256 is in
`coverage.json`. Record files, retained reviews, native validator/schema and
lock inputs remained unchanged. Only new inventory code, tests and reports
were authored.

The dedicated environment was created offline with:

```sh
uv sync --frozen --extra dev --offline
```

The capture ran the native `.venv/bin/python scripts/record_review.py list`,
checked its actual exit, and bound the review/script/schema/config/lock hashes
before and after execution. The inventory then verified every emitted row
against the retained YAML and exact bundle set. It checked all 549 declared
record paths against both the Git tree and ignore-independent filesystem
enumeration, compared current bytes to Git, and rechecked inputs before output.

The new helper has no provider calls, canonical writes or review-save path.
Its only output is stdout. Preserve exclusive destinations when repeating a
capture or inventory; old observations should remain available.

```sh
set -o noclobber
.venv/bin/python scripts/adhoc/inventory_resume_review_coverage_20261115.py \
  --expected-revision 68699871415fda3c9eebf20382a315f9f3c7b17a \
  capture-native > .temp/m5-resume-20261115/native-review-capture-001.json
.venv/bin/python scripts/adhoc/inventory_resume_review_coverage_20261115.py \
  --expected-revision 68699871415fda3c9eebf20382a315f9f3c7b17a \
  inventory --capture .temp/m5-resume-20261115/native-review-capture-001.json \
  > reports/m5-resume-20261115/coverage.json
.venv/bin/python scripts/adhoc/inventory_resume_review_coverage_20261115.py \
  render-summary --ledger reports/m5-resume-20261115/coverage.json \
  > reports/m5-resume-20261115/README.md
```

These are the original prepublication commands, not instructions to overwrite
their outputs. For a new inventory, choose new exclusive paths and the exact
revision of the checkout being examined. `--expected-revision` must match HEAD;
after publication this will be a different commit, even if the record bytes
are unchanged. Compare the public record-inventory digest and native input
hashes to establish whether a later run used the same inputs.

Validation passed:

- [24 focused guard tests](validation-tests.log.txt): valid controls plus wrong
  revision, failed native capture, altered byte hash/context/metadata, omitted
  or duplicated reviews, ignored extra records, dirty records, partial/batch/
  selector/diagnostic scope, and stale-record cases.
- [Full native lint](validation-lint.log.txt): Black, Ruff and mypy.
- `git diff --check`.

The native inventory and helper were independently reviewed read-only before
publication. Scientific truth, source-cache freshness and resolution of old
findings are deliberately outside these checks. No whole-repository QC run
was repeated for this read-only inventory helper.
