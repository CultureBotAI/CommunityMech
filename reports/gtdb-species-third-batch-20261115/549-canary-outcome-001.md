# B8-1 species-reference canary

CommunityMech:000549 now records the native correspondence from its existing
NCBITaxon:2026194 species descriptor to GTDB:s__Bacillus_A_paramycoides. The
reference population has nine genomes and majority fraction 1.0. B8-1 remains
the study's single-isolate baseline: its 16S marker does not identify an assembly,
and the GTDB label suffix does not establish a formal species rename.

Only this descriptor's block/status and two native inline events changed.
Existing stock, source, biological, related-record and previous-history content
is preserved. The remaining nine records in the third batch have not been
applied. Their accepted preparation is described in [README.md](README.md).

The [native diagnostic](../../reviews/structured/20261115T094640Z-b81-species-reference-correspondence-diagnostic/review.yaml)
and its [derived Markdown](../../reviews/structured/20261115T094640Z-b81-species-reference-correspondence-diagnostic/review.md)
contain three scoped assessments with `scientific_review: false` and partial
coverage. The inspected primary evidence is the retained abstract and bounded
main-text passages for PMID:42587276. No new figure-pixel, archive-sequence or
complete-paper assessment is claimed. The B8-1 biofilm-naphthalene numeric
discussion and separate 000358 findings [2317](https://github.com/CultureBotAI/CommunityMech/issues/2317),
[2318](https://github.com/CultureBotAI/CommunityMech/issues/2318) and
[2319](https://github.com/CultureBotAI/CommunityMech/issues/2319) are not resolved.

## Actual persistence and native checks

Source preparation ran at `7ed0013eac35b2a3ff8f1986e30d596411209849`.
The isolated M5 stage, guarded application, history and eight native checks ran
at `dd97489f4475c6cc6127d1fdd375b4a80f3220b1`, using Python 3.13.2. Local
publication and pair auditing use the maintained Python 3.13 environment; they
do not relabel M5 execution.

| Evidence | Exact value |
|---|---|
| Before record | `cb226c9c70b14d042991de11ef4a7b3677790ffd8a93549332e213dc4946b04e` |
| Actual after record | `78d68bf71c78ed5c50d3e629d40283a41a5eb1b2e5393fa4475fac5b845be4d2` |
| Actual raw application receipt | `43d3196da095da062aeef485063d19fcf1248a654fcf8a2660b5c41b50d8400b` |
| New native sidecar | `0eee049ca7003e0a4fc7a69802ecfcd1d79c218f9dc34c6b35152079ac03adb8` |
| Saved review YAML | `92bdaa61230d24b0a6a87c601b366be33dad0c7a8c4edcca01a19f811ac85b37` |
| Derived Markdown | `0fbc2edfa38f717a8118f98c79d6fab1410f4d6f01ce01f38a56e005dae17248` |

All eight actual commands passed: native history creation, schema, strict,
GTDB coherence, prokaryotic domain, scalar, history and ontology-term checks.
Each receipt records a real invocation, exit 0, nonempty native output and
unchanged execution inputs. The ontology-term log explicitly reports validation
passed. These checks do not include source-snippet validation or aggregate QC.

The [public successor manifest](549-001-successor.json), SHA256
`e23162ae95ef3cf54651ccd8efe9fcc703de2cfde3004e1391a5e2ffadaffdff`,
links the byte-identical actual application receipt, source proof, sidecar,
saved review and all eight receipt/log/exit triplets. The unchanged exporter
audited the captured input map before publication; all 27 persisted public
artifacts matched the returned plan. No primary-source body was added to this
public proof.

## Retained inputs and limits

Both local and M5 pair audits verified all 79 declared inputs, totaling
5,206,785 bytes, and reproduced the exact native Markdown. Before changing any
captured caller, the complete namespace was preserved and verified on both
machines: 81 files including the pair, totaling 5,281,482 bytes. The immutable
private snapshot is `.temp/gtdb-species-third-batch-20261115/549-complete-inputs-001`;
its manifest SHA256 is
`423fccece8b40cea37bab5d4aea4fe3dd26f228750f5ab30c2032ee239c5eedf`.

The initial local staging invocation omitted the required operations argument
and refused before candidate output. The initial M5 offline installation also
requested optional extras and failed for an unavailable optional DuckDB wheel;
the corrected frozen dev-only installation passed. Those receipts remain
private under the `species-third-*` recorder names. Neither failure is counted
as a passing gate or discarded.

The crosswalk's full hash identifies the exact bytes; no release date or
upstream version is inferred from its file timestamp. The correction does not
identify a study-stock genome or a degradation pathway. Generated products,
strict historical successor admission and combined full QC are separate from
the saved native diagnostic.

## Strict admission and integration checks

The thin species registry admits only this exact 549 proof. Batch147 retains
its immutable rows, old scientific assertions, existing 552/553, 554 and 555
successor routes and refusal for unlisted changes. No biological predicate or
shared admission rule was weakened.

The initial combined run passed the 16 shared positive/mutation controls and
both batch147 tests, but the extra unknown-target test failed before exercising
its refusal because an isolate-only fixture lacked `kb/communities/`. This
fixture defect was filed as [2885](https://github.com/CultureBotAI/CommunityMech/issues/2885).
The log remains immutable (`d64610aa80836ef1c86701b112b678fe976c6534508898b48d67b5dbb0b61cc3`):
18 passed, 1 failed, 12 warnings. Creating the unrelated target's parent
directory is the only correction. The exact failed refusal/restoration case
then passed, with 12 existing warnings in 2.83 seconds; its log SHA256 is
`788bc10435f4523915fbc638421affdb9207dbde68c845c00a1b6747f5bd78a6`.
The already successful 16 controls and two historical tests were not repeated
solely to produce a combined count.

Full native `just lint` passed on the resulting working tree: Black checked
745 files, Ruff passed with its existing directive warning, and mypy reported
no issues in 52 source files. The retained log SHA256 is
`18bdb78f8c1d539974ab5509d755857848b6ac7edd228c84998e20324a7c0e40`.
These are focused integration checks, not a full corpus QC or scientific pass.
