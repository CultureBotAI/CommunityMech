# Independent review handoff: records 389, 381 and 482

Independent reviewer: `pr_review`, 2026-11-16. The bounded source, candidate,
native-gate, diagnostic, persistence and export reviews ended **accepted, with
no new finding**. This checkpoint is ready for publication on the existing
draft branch. It does not include strict successor admission, affected caller
tests, integration into the maintained aggregate branch, or full scientific
approval. Those steps remain pending at the requested checkpoint boundary.

The actual M5 execution revision remains
`308081a8cf3f82472c542db87e135a5b96da61be`, with Python 3.13.2 and recorded
working-tree changes. Independent local persistence audits ran at
`4f46bb640e0a5ceec646df90527bdfa881a20e12` with recorded working changes.
These revisions describe different operations; neither is a claim of clean
aggregate QC.

## Accepted scope and exact current bytes

All three complete candidate diffs, application receipts and stage inputs
were independently read and rehashed before application. Only declared GTDB
fields and actual native events changed. The 31 selected descriptor
occurrences comprise 29 reference blocks and two complete ambiguity lists;
they do not describe 31 experimental stocks. The three sidecars and all 24
native gate logs and receipts were subsequently read and verified. Each gate
reports the actual expected command, exit 0, plan false, frozen M5 revision
and unchanged captured inputs. Terms validation supplies no assertion
denominator.

| Record | Current canonical SHA-256 | Actual application receipt SHA-256 | Public manifest SHA-256 |
| --- | --- | --- | --- |
| 389 | `f3d1070490b0d63e018b74be21d805e4f61da66dc423bb0fb059fa434825db3f` | `9a60d55787efc3047167f7a901741dbe3456403541c863bfc24adf7c5b97a5c0` | `c33fe6ab2fdad1cecf9c6d2a0f7377eb1970c1885168a18ef77274bae6fa874a` |
| 381 | `c5e1f0beaab510b6cc61f7f32b38d89935461378ba56e231e0eaed3887e7a2b7` | `f9112ed5819200db8899bb8217d5965d1259efa5dc1b29d4773169936545a964` | `234e7fe2da9f1a4184bb4973cc6d97ca46f91e76d125bdf8f53687046ed2ba57` |
| 482 | `d06607ee111c282355160fc88cc38c0431ed7580c901b73941d7a0fab1baf82c` | `6ede537a6413f86dae402140ca9f1a232c765fac0175944609c5b9604d5b5660` | `bb7a3a36f57ee59d76085649f579d235ea385d5c5e9f1ae7241ea02944c7d6e6` |

Public manifests are `{389,381,482}-001-successor.json` beside this handoff.
They bind the exact accepted source metadata, sidecars, native gate artifacts,
predecessors and selected indices. Their existence is not a production
registry admission.

For record 389, four substrate enrichments and separate SILVA amplicon bins
remain distinct from generic genus/family reference populations. The 278/482
and 47/54 majority relations do not rename source organisms or establish
member-resolved flux. For record 381, all fifteen bacterial stocks and the
algal member remain distinct, including the two Alteromonas stocks; name
fallbacks do not establish stock assemblies. Issue 1728 and B12 transfer
limits remain. For record 482, the Rhodanobacter 15/15 relation is term-only:
issues 2404–2406 concerning experiment attribution, the four-stock roster and
mechanisms remain unresolved. Preserving its current biological claims does
not endorse them. The pinned crosswalk's upstream release is unestablished.

## Native diagnostic and saved-input verification

The actual draft has three targets, nine assessments, 38 evidence items and
24 checks. All content was independently read against the already accepted
source and native evidence. Coverage remains `partial`,
`scientific_review: false`, and the scoped verdict is `pass_with_limitations`.

| Artifact | SHA-256 |
| --- | --- |
| Authored `remaining-three-review-config-001.json` | `94536696803bcde8a4f7ee0155d1f942f5e0bfb7f602053eea87a809c17761eb` |
| Actual private draft `remaining-three-review-draft-001/review.json` | `b5090c3f347b5b1e888609d2693ec29464776e40ef6699e8b668cea415f6776f` |
| Native inspection | `4a5b65420d2da87c2e526502a8a2ca8c4fffa47c3ddeecb3c600a8aa1c7ea08e` |
| Saved `review.yaml` | `b186628bcc4944dc16c077734212a73f0e70da546b92d27eecefc51fecd9a208` |
| Saved `review.md` | `35684b9575193db3707e90fe5df6f9ce911dc1948a315dcb4e36b296c96b8602` |
| Local complete checkpoint manifest | `dbe1a4fa16650ba3dff75379c2507a77bcbcb9260878473c642fa18f0b37e103` |
| M5 complete checkpoint manifest | `bca9957755c7ce99615cb59a3b6d73d48603cc7e4b9e571d11d3af0ace7c6ec4` |

The saved pair is under
`reviews/structured/20261116T024711Z-rumen-prymnesium-black-soil-reference-diagnostic/`.
The private checkpoint is
`.temp/gtdb-genus-last-four-20261115/remaining-three-input-checkpoint-001`
on each host. Local and M5 manifests are distinct and must not be substituted.
Each complete namespace contains **181 files / 13,500,609 bytes**. The saved
review binds **179 unique inputs / 13,313,207 bytes**.

The independent reviewer ran the unchanged native pair/input audit and
complete-namespace verifier locally, recording these immutable triplets under
`.temp/phase2-schema-20261115/`:

| Independent audit prefix | Raw log SHA-256 | Result |
| --- | --- | --- |
| `genus-three-pr-peer-saved-audit-001` | `db7c10fcb8eac424a8107f095a17a93a2c7c9d7dc3272bfa65070ecb2cb551c9` | Native validation, exact Markdown, all 179 inputs and unchanged bytes pass |
| `genus-three-pr-peer-checkpoint-verify-001` | `3897e0372169799b9b8af0d00ae49c9b4686e91aa1e0ba6eb67bb38a9b8417d7` | Complete local namespace, all 181 files and bytes pass |

The separately executed M5 audit and verifier receipts and full outputs were
read and rehashed after mirroring. The M5 saved-audit raw output is byte-identical
to the independent local audit above. The M5 standalone checkpoint-verifier
raw output is `c2be6e0892d472942dee21562baa731b85054c47d154d9c1fcd4fdbded5bba53`
under `genus-last-four-three-checkpoint-verify-m5-001`; its receipt records
the frozen M5 revision and exit 0. The reviewer did not rerun the native gates
or claim a separately executed peer SSH audit.

## Export verification and continuation boundary

The exact export config
`remaining-three-export-config-001.json`, SHA-256
`7a97b9a179664268dcfc213f525681ff7947bb6e857ff8e9cc1e1ebb49a0872b`,
was independently read before actual export. The unchanged exporter is
`f537b7cc1fb1abbda64a8712f651410ec4795512a0de23c260b93705a61b2f36`.
Plan and actual stdout were independently compared byte-for-byte; both hash
to `ecdbbe97e915c85ad4d6225aee282e949b09e2ff03cbb5ee04855336cb76cec7`.
All **81 persisted public artifacts** independently rehash through the existing
`gtdb_export_stdout_hash_lines_20261115.jq` renderer and `shasum -a 256 -c`.
The producer's retained export-hash log is
`ca139e68602cbb9896d78a4afe116886cdbf83ba0ceedacbdaa11bc72b6ffd39`.

No new strict registry entries, actual-successor test cases, caller edits or
their tests were performed for these three records at this checkpoint. The
captured batch callers remain unchanged:

| Caller | SHA-256 |
| --- | --- |
| `tests/test_causal_review_batch96.py` | `0d44ab0734e36cddaee7d2034e0f72148cba578b5a2215383ee3916ee9bac4c9` |
| `tests/test_causal_review_batch88.py` | `907f97690929d35d97fe4f632a7fc4dc0e09f01f1b692126719558079351bc1f` |
| `tests/test_causal_review_batch133.py` | `60c10cf5de2737339efcd732818538e1cab80a44c939c84e46ef840dcbe2d40f` |

Resume with the explicit current-proof registry and shared mutation controls,
then narrow historical caller admission preserving direct current biology and
immutable ledgers. Preserve batch 88's 461 chain, batch 96's sibling records,
all six captured batch 133 admissions, and the separately maintained Wetland
471 composite during later integration. Run one actual proof canary before
the remaining controls. No complete scientific review, measured quotation
coverage, aggregate QC, generated-product currency, merge or maintained-branch
integration is claimed by this handoff.
