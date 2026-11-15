# Mixed fungal-domain workflow support

This additive implementation addresses the workflow refusal recorded in
[issue 2904](https://github.com/CultureBotAI/CommunityMech/issues/2904). A record
containing a bacterial correspondence, bacterial ambiguity and a fungal
`NO_GTDB_EQUIVALENT` observation needs a different contract from the existing
native-null `UNRESOLVED` status-only path.

No canonical record has been changed by this implementation task. The real
CommunityMech:000420 application, eight native checks, saved diagnostic,
complete input checkpoint, public proof and actual strict-admission canary
remain required. The checks below use controlled synthetic authority/table
fixtures and existing published proofs; they do not establish a new scientific
assessment or an actual M5 application.

The new files use contract `gtdb-mixed-fungal-domain-v1`. Staging and application
both require the unchanged native resolver/classifier, exact source-bound NCBI
label/rank rows, affirmative Fungi and Eukaryota ancestry, the native domain and
exclusion results, no existing classification block and no manual hold. A null
lookup, missing adapter, query error, or missing ancestry refuses the unit.
The affirmative identity guard accepts exactly one of eight principal NCBI
ranks (superkingdom, kingdom, phylum, class, order, family, genus or species);
other ranks require a separately reviewed extension.
The selected unit must contain both a fungal null and a grounded route and use
the two native operations `--apply` and `--apply-status`.

The stage receipt binds an exclusive domain-observation artifact. Application
recomputes that observation through the same local adapter and requires the
database file identity/stat to match before and after validation. This is a
cooperative change guard using file identity/stat, not a whole-database content
hash, immutable database snapshot or release claim. The builder, exporter and
strict admission require the same observation bytes, implementation inputs,
actual application chain and saved-review bindings. Current biology, stock
identities, all old history and unselected taxonomy remain protected.

The diagnostic builder and strict core are explicit additive versions of the
executed implementations. The thin exporter reuses the existing captured-input
publication core and adds a byte-identical domain artifact. The existing
checker, native resolver/classifier and four original workflow files remain
unchanged:

| Original file | SHA256 |
| --- | --- |
| `scripts/adhoc/gtdb_batch_curation_20261115.py` | `bc488158440416db558133cfc0609111d96f46123b66c22efbafcfef1934d144` |
| `scripts/adhoc/build_gtdb_batch_diagnostic_20261115.py` | `c6bf0d09dc3d01797ab5d956a4f7458a9a153a8704508f50e656729e4ee1b860` |
| `scripts/adhoc/export_scoped_gtdb_evidence_20261115.py` | `f537b7cc1fb1abbda64a8712f651410ec4795512a0de23c260b93705a61b2f36` |
| `tests/scoped_gtdb_successor.py` | `6371b2eac029ff81c3fce7af6f0439c52eccacefbf172db7c1056df3ec03a007` |

Local working-tree verification used the frozen environment at base
`30cbf84d1d538011846447827a079edf71ee85c7`. The recorder explicitly retained the
untracked implementation files in its initial status; these are not clean-commit
test claims. Receipts and nonempty logs are retained under
`.temp/phase2-schema-20261115/` with the following stems:

| Receipt stem | Observed result | Log SHA256 |
| --- | --- | --- |
| `fungal-domain-focused-final-002` | 41 passed; 14 dependency warnings | `bbee1c466aac8963d6ee04473fcd2fb11d5f5d6925ca62f65c9bce17e35c022a` |
| `fungal-domain-original-guards-001` | 47 passed; 12 dependency warnings | `53123e5712cb80fba4c769741aaf540eb6fd0adde074ebd57e28405af842d005` |
| `fungal-domain-original-actual-proofs-001` | 64 passed; 12 dependency warnings | `d5e543bc9d91f3c67c731f52b6379e115259c5a17326f5983e194ece6c7f0168` |
| `fungal-domain-rank-before-001` | Three intended failures: malformed matching rank admitted | `d3827448014cb4631e842fc6c2ac7b12eed908f6cdc2e1dfb2c5af540371d8cf` |
| `fungal-domain-rank-after-001` | Three rank refusal/restoration controls passed | `4ea81fd70af775c194f0e6c0ad31f9e19b6407d92ca4a9f18acd2b9453d00931` |
| `fungal-domain-lint-003` | Black 770 files, Ruff, mypy 52 source files passed | `6dc2ee542c7284878b11c3e9214f94609312a47ea0cd58cb390d5a3a87ac37e7` |

The new controls execute the real native CLI writer and validated application
against a real historical record baseline with a synthetic crosswalk and local
authority fixture. They verify persisted candidate/application bytes, positive
controls before and after mutations, cached-success isolation after authority
loss, contradictory/missing ancestry, manual holds, changed science/history,
rehashed wrong contracts, post-validation input drift and consistently rehashed
but invalid domain evidence in builder/export/strict checks. The existing
four-record proof matrix continues to exercise its original core.

The first development attempt, `fungal-domain-initial-controls-001`, refused the
synthetic table at the strict crosswalk-provenance check. It remains retained.
The test fixture now supplies its explicit synthetic digest to the test-local
strict constant; the production crosswalk pin is unchanged. Earlier passing
subsets and the prior 38-control result remain separate from the final
41-control result. The first lint pass reported the pre-existing invalid `noqa`
warning in the unchanged native resolver. Lint attempt 002 failed because the
explicit launcher PATH omitted the installed `uv`; its raw log
`a3272201145adc9a2d847b40140becea0e8346c6c2b25903432908ccc81084a9`
and exit 127 remain retained. Attempt 003 restored the verified tool directory
in PATH and passed without a source, dependency or lockfile change.

Independent review found that agreeing source and SQLite rank rows could both
contain null, an empty string or an arbitrary non-rank value. This is recorded
in [issue 2907](https://github.com/CultureBotAI/CommunityMech/issues/2907).
The original six-file reviewed version and README remain byte-identical in
`.temp/gtdb-domain-mixed-2904-20261115/reviewed-code-001`.
All three native-stage regressions first failed after their unmodified and
restored positive controls succeeded. The corrected guard now refuses those
values without a successful stage receipt or canonical change. The actual 420
source has a valid genus rank; no real 420 execution preceded this correction.

The new commands retain the original CLI argument shapes under the explicit
filenames `gtdb_fungal_batch_curation_20261115.py`,
`build_gtdb_fungal_diagnostic_20261115.py` and
`export_gtdb_fungal_evidence_20261115.py`. Callers must explicitly use
`tests/scoped_gtdb_fungal_successor.py` for a separately reviewed, manifest-pinned
mixed-domain proof. No existing registry or historical caller is changed here.
