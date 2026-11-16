# Installed CommunityMech supplement canary

The isolated CommunityMech environment now uses the exact reviewed validator
commit `6b71e7f4b353b5b36000fda03da78b61734e3fc8` from the
[owned draft](https://github.com/realmarcin/linkml-reference-validator/pull/1).
Its native CLI compared all 37 unchanged Switchgrass snippets and matched all
37, including three explicit supplement-cell selections. The original
article-only record still produces its two expected mismatches. No canonical
record, reference cache or source asset was changed by these trials.

This follows the reviewed
[schema and governance preparation](supplement-adoption-1996-20261115.md).
The runtime's inherited live-network test failure remains recorded in
[issue 2934](https://github.com/CultureBotAI/CommunityMech/issues/2934).
Its full native suite is incomplete. Claw PR 1283 also retains its failed
schema-test setup run while isolation is investigated. Neither draft is merged.

## Exact installation

The dependency is a full Git commit URL, not a floating branch or version-only
selection. Native `uv lock --dry-run` preceded offline locking; the actual diff
changes only this validator and its source metadata. The installed version is
`0.2.1.post1.dev0+6b71e7f`; LinkML remains 1.9.3 and linkml-runtime 1.9.5.
The local interpreter is Python 3.13.12. The lock SHA256 is
`1e1374a77207de170502a89ea7eebcb018d65daac8b0faecc39988d955f3df62`.

Frozen offline `uv sync --extra dev --reinstall-package linkml-reference-validator`
built from that Git source. Independent source/wheel/installation verification
confirmed exact membership and bytes for all 49 package Python files and
unchanged inputs. The separately built reviewed wheel has SHA256
`3257211bda8a22d95b4b517325db383de3243950c0110ec778523c65df8b0628`.
The check establishes Python-code identity with that wheel; it does not claim
that uv installed that same wheel archive or attest every dependency's bytes.

| Recorder in `.temp/phase2-schema-20261115/` | Raw log SHA256 |
| --- | --- |
| `supplement-runtime-lock-plan-001` | `35bd46db4f052309837e4b21b76a4f622437b05e57d48e4f0c3d9a39eb7f86b3` |
| `supplement-runtime-lock-001` | `8605a04f7b516c3e18276cceab38837be7a228e91ab7d869b7d2219b1541f7d2` |
| `supplement-runtime-install-001` | `b8f5c63b91750067753503e9c05926fcec1028d7eb2df4ca77b6a06bed78a718` |
| `supplement-runtime-installed-verify-001` | `08734b09209d6bd64e4cb72180718985894b076cd65433c2c518b9a39c76c807` |

## Actual consumer controls

Preparation copied the actual consumer schemas byte-for-byte and mechanically
replayed the retained DOCX. It added only three locators to a private record;
all original 37 snippets and references remain unchanged. The original record
SHA256 is `bb31b1df4a9be2241453528101fc5d55657c23eccf1d58ce1cc9639e5912b368`.
The retained asset and extraction identities are the same as the runtime trial.
No source was downloaded, and no provider or matcher was replaced.

The private preparation receipt is
`.temp/supplement-adoption-1996-20261115/switchgrass-prepared-001/preparation.json`,
SHA256 `32e59f36484643038eeb109c9f756e6fe83e788d251b15a05389b6a4ad561eca`.
Its plan passed before persistence. The selected execution plan then passed,
followed by one real positive canary whose actual log, exit and receipt were
verified. The four remaining plans passed before the controls ran serially
through the same runner, interpreter and private namespace pattern.

| Run | Calls | Comparisons | Matches | Mismatches | Selection errors | Source identities | Native exit |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Selected | 37 | 37 | 37 | 0 | 0 | 3 | 0 |
| Article-only | 37 | 37 | 35 | 2 | 0 | 0 | 1 |
| Wrong cell | 37 | 37 | 36 | 1 | 0 | 3 | 1 |
| Wrong parent | 37 | 36 | 36 | 0 | 1 | 2 | 1 |
| Restored | 37 | 37 | 37 | 0 | 0 | 3 | 0 |

Every run passed its declared control with no changed captured inputs or
network attempts. Wrong-cell selection failed for `Bacillus` even though that
word occurs in the article, proving that the explicit selection did not fall
back. Wrong-parent selection failed before comparison and is counted separately.
The observer verified exact paths, text/reference hashes and source identities.
The native `Total checks` label still counts issues; it is not the denominator.

Receipts under `.temp/supplement-adoption-1996-20261115/`:

| Directory | Receipt SHA256 |
| --- | --- |
| `switchgrass-selected-001` | `9b0e6b77cb53f7566913d1a27b2c26a71df45c6754aba7e3fed0d50284256b94` |
| `switchgrass-article-only-001` | `8b1efaa85f3209aad6246a41b6ebf23a5922cdb4a546e8a9f76332ca934384d2` |
| `switchgrass-wrong-cell-001` | `1fce118c9b0d5e26eb579a0fc43dc1ccccee6bdd29402b0830952c864cea3b39` |
| `switchgrass-wrong-parent-001` | `e92a247b3c8971b9cae56aa062d708fe9ec104980eef5002e11940232745a861` |
| `switchgrass-restored-001` | `e0399e9eede173fde5af7301255cd1baf3e235ccd4e72ae102663f33bdbd913d` |

The selected native log is
`1d09a0ed82f143f0f6ec234dda3befd1b3e9d0c1c22aa2b128ae9ec69c32236b`;
the restored log is
`b02619737cc258a86c3b60175347443c6227dea752dd87f898bfdbc95b57b595`.
Recorded CommunityMech start revision is `8224968e`, with the dependency/lock
changes and independent helper work visible in each recorder. This is not a
clean aggregate QC result or an M5 execution. M5 installation and its actual
canary, guarded canonical curation, native history, updated saved review,
generated products, measured references and full combined QC remain required.
