# Four-record source preparation

This branch prepares scoped GTDB correspondence corrections for Sorghum348,
Transwell091, Nasal395 and Rumen398. It starts at published integration
revision `acb0d4b95c4b4ec7e3b2837ee2bcb611a5de08d6`. Canonical records,
scientific claims, historical ledgers, source caches and shared curation code
remain unchanged. No M5 application or post-application review has occurred
in this lane at this preparation checkpoint.

The later local previews, isolated M5 setup and pending six-file source-transfer
permission are recorded in [local-previews-and-m5-setup-001.md](local-previews-and-m5-setup-001.md).

| Record | Proposed correspondence scope | Scientific limits retained |
| --- | --- | --- |
| Sorghum348 | Five missing blocks among 15 stocks; eight existing blocks and two unresolved native-null results preserved | The pinned roster extraction identifies PH2, SAI_226, SO6a, NA8 and TBS_030. No raw genome assignment, equivalence from nonsignificance, field efficacy or demonstrated flavonoid mediation. Issue1811 remains open. |
| Transwell091 | Five descriptors: three species anchors and two strain anchors, including DC3000's different GTDB species name | The Cv017/Cv026 reporter pair and separate three-member assay remain distinct. The SC11,368/SC11,378 discrepancy and cultivation metadata are unresolved under1467. |
| Nasal395 | Nine included LaCa stocks; seven ID routes and two species-name routes | Supplement TableS2 is separate from the article. SaA/SaC are excluded challenge strains. Inoculum inclusion does not establish all-nine persistence; the empty graph remains a research gap under1640. Latest publication status was not verified. |
| Rumen398 | Four missing species correspondences; existing S. equinus ambiguity preserved | Five optimized stocks differ from initial seven-member designs. Reference mapping does not establish study-genome identity, expressed function or cattle engraftment. Three animals per group and nested bags remain distinct;1655 is closed and1658 remains open. |

These are 23 selected descriptors among 34 whole-record taxonomy occurrences.
Reference denominators and rounded fractions are preserved exactly. Species
results without an explicit support numerator do not acquire one. Native-null
and ambiguous outcomes are not guessed into a match. GTDB names do not replace
source stock designations, experimental conditions or NCBI identities.

The fixed crosswalk SHA256 is
`761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd`.
Its file modification time is not a release identifier. Local NCBI authority
is checked by identity/rank rows and file stat; no full database digest or
ontology-release claim is made. All retained route inputs verified unchanged.

One whole Sorghum route canary completed and persisted before the same launcher
processed the four-record source plan. Raw logs and their exit-code/command
receipts are retained in `.temp/phase2-schema-20261115/`:

| Recorder | Observation | Raw log SHA256 |
| --- | --- | --- |
| `final-four-route-canary-001` | One whole record; 3,877,761 bytes; 13 captured inputs verified | `4e950b2b05f1dbd73b67c02931ef83722dac55ae3b893756df25f43ad11df089` |
| `final-four-routes-001` | Four whole records; 4,067,429 bytes; 16 captured inputs verified | `c7fa6442d249c780907b32b878e95a002d63862bc80ab06363a99be9781e8606` |
| `final-four-348-source-bind-001` | Accepted source context, 28 inputs verified | `06a22185d42c7fb036078d80f01de6f9f12cc2290ac83c91f835a75081045c03` |
| `final-four-091-source-bind-001` | Failed before staging: literal source anchor differed | `0c532d62701acfb8eef94e63515dd45b9ad8e772e8526c806d2c46e470b3ddb0` |
| `final-four-091-source-bind-002` | Corrected exact locator; 30 inputs verified | `f1ed9e7d452c0ef684dd47c7dd25c173b6ec7dfddc34bc341df27e5047396db7` |
| `final-four-395-source-bind-001` | Accepted source context, 29 inputs verified | `c0adb52854f0dffe61b515c0945335c52a47473d61ec00cd571e0df25fa4a2ee` |
| `final-four-398-source-bind-001` | Authored source context, 28 inputs verified | `e55cb713f26596e67a459884b8572c5322983dbc2de5fcd599f4c0955e5675d9` |
| `final-four-348-local-stage-plan-001` | Free plan passed before private preview | `2af609a00afda5d21205fda695e21ea3e64b5822533dc01462e53a3e3e8cd669` |
| `final-four-348-local-stage-001` | Both unchanged native operations passed on a private candidate | `4bbaf5ccda4cdfc03f18daf9645391c3c1fc12adf527729ab2591dc2d22b4395` |
| `final-four-preparation-lint-001` | Black 788 files, Ruff and mypy 52 source files passed | `3adaf5564b1ba0b311b31ae6bd954eb44553db9d8181930bce7da40d973fa1ac` |

These local preparation checks used Python3.13.12 and recorded the untracked
preparation files in their receipts. They are not clean-tree aggregate QC.
Lint retained the existing issue2915 warning about a quoted `noqa` directive
in unchanged native code; no classifier or warning suppression was edited.

The first Transwell authored/expanded configurations remain unchanged beside
version002. Only the faulty locator changed, preserving the source conflict
and the unchanged literal binder. The failed invocation and correction are
recorded in [the finding](091-source-anchor-finding-001.md) and
[issue2926](https://github.com/CultureBotAI/CommunityMech/issues/2926).

The local Sorghum preview is retained at
`.temp/gtdb-final-four-20261115/348-local-candidate-001/`:

- Candidate `3128f4031455748be842dbb93b65e8b87c66b3497c36017d5e29f37d6faec822`.
- Receipt `9ad6a5a879c81d545434ae4da34ecbc5d50db57e5de4fe2abdee6361eedfb709`.
- Diff `57c9215d546ca14c38f8b40195f41a9bbad650fe9267cd798723fd2184e4bd7d`.
- Native log `4cdb7c818b60d4ae618d0a10adea4d5a59eda06d1b5a8c2134d4e219e0e65168`.

All31 stage inputs verify. The full diff changes only five native blocks,
five statuses and two inline events. It preserves the other ten descriptors,
all stock metadata, biological assertions, quotations and old history. This
local preview is not an M5 application or the required end-to-end canary.

Before applying another record, Sorghum348 must complete actual M5 staging,
independent candidate review, guarded application, native history and scoped
checks, immutable partial review, complete verified input checkpoint and
strict historical admission. Other source inspections do not authorize early
application. Historical callers103/42/77/79 and the Transwell participant
guard must retain current biology and the literal old reviews; new evidence
may admit only the exact declared successor. Passing these scoped checks
will not complete full scientific review, reference validation, current
generated products or aggregate QC. No merge is authorized by this checkpoint.

The subsequent [Sorghum 348 canary outcome](348-canary-outcome-001.md) records
the approved six-file transfer, actual frozen-M5 application, eight native
checks, saved partial diagnostic, independently verified 80-input audit and
complete 82-file checkpoints, 27 verified public artifacts and strict
historical admission. Its actual proof/caller matrix passed 25 tests after the
separate positive canary; native lint passed. Native append-only review
integrity passed for 350 reviews with `declared_scopes_only` coverage. The original preparation and
failed-transfer observations above remain historical. Transwell 091, Nasal 395
and Rumen 398 remain unapplied in this lane. Full scientific review, generated
products and aggregate QC remain separate.
