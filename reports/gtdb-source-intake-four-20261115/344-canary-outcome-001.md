# KZ344 complete genus-reference ambiguity canary

Record 344 now retains all 11 native alternatives for its existing Arthrobacter
genus descriptor. This is a database-correspondence correction with a saved
partial diagnostic (`scientific_review: false`), not a new scientific approval.
The existing Klebsiella block, both study stocks, all biological assertions,
source quotations and historical findings remain unchanged. The unread
corrigendum and Methods/cultivation limitations under
[1541](https://github.com/CultureBotAI/CommunityMech/issues/1541) remain unresolved.

The actual guarded application ran on the isolated M5 checkout at published
revision `8ad0caccd37c5903daa0cbcebd4f682bae63449a`, using its frozen Python 3.13.2
environment. The local preview and its timestamp remain preserved separately.
The accepted actual candidate changes only taxonomy index 1 from UNRESOLVED to
AMBIGUOUS, adds the complete ordered 11-option set, and appends one native
GTDB_SET_STATUS event. The native command processed two taxa but changed one.
No alternative was selected as the identity of study stock SZ-3.

| Actual artifact | SHA256 |
|---|---|
| Before record | `65275177a514ceb42276f4f416da7b727e5200b3a8f79fb1510cf6c49bbd083c` |
| Applied record | `4c0c1e99a85343e4efecb95d042e79c22e85c72d9cfad89195e2ceb0b385acf5` |
| Stage receipt | `d3b760b09999798842492641624b23237676eb4269d3c7362ea97c1e1446f5bd` |
| [Byte-identical actual apply receipt](344-001-apply.raw.json) | `c6a9d91a356d17efd1b4420a5893f80725462b573b962f8d1d8e8358d8e94b34` |
| New native history sidecar | `b04a373a637eac2404e5aa2c8c7af7b834aa2a86cc92153b1261c77165f7c7d9` |

All eight actual native commands passed: schema, strict, GTDB, domain, scalars,
history, terms and new-history. Strict reported one file and zero errors; terms
reported its literal pass result. Exactly one new nonempty sidecar was retained,
and the two existing sidecars were unchanged. Their completed command receipts,
logs and exits are linked by the [successor manifest](344-001-successor.json).
The manifest SHA256 is
`a2bffc7b22041ee8df2b0437f5a78443f09320d14cdaf4a80ffae299a8406486`.
All 27 public artifact hashes were checked after persistence. The strict log is
a labeled sanitized derivative; its original raw digest remains bound. Raw
source bodies and private command records remain in the private evidence tree.

The immutable native review is
[20261115T123209Z-kz344-complete-genus-reference-ambiguity-diagnostic](../../reviews/structured/20261115T123209Z-kz344-complete-genus-reference-ambiguity-diagnostic/review.md).
Its YAML SHA256 is
`5e7edb883cbf5a44874b7789063a7a8a9686e94b00eb4199ac9f4b750962ebc4`;
its Markdown SHA256 is
`c326e57c97a60ea1e5471cea5c438e79e4c586b872c44b62a6b85fb1963534b1`.
It contains three scoped assessments and eight actual check results. Native
validation, exact derived Markdown and all 80 input hashes (5,991,654 bytes)
passed on both hosts and in the independent parent audit.

Before changing the historical caller, the complete input namespace was
preserved and verified on both hosts: 82 files and 6,067,142 bytes, with manifest
SHA256 `4b78af5349784f7e6dfe093b8e21d8b845fa24d42a3a1acd0cf79a9d8ea0dedf`.
This includes the original caller and every reviewed helper/input alongside the
saved pair. The first local standalone verifier invocation omitted its required
manifest-hash argument and refused with exit 2; that receipt is retained. The
corrected invocation verified the exact manifest and every file. The frozen M5
inputs still match the saved review; the later local caller change is preserved
outside that immutable input snapshot.

The explicit successor registry binds the original record bytes at historical
revision `68699871415fda3c9eebf20382a315f9f3c7b17a` to this actual application,
source proof, native checks and saved review through the unchanged shared
admission core. Batch60 checks the admitted current record before its existing
biological predicates. Only the old KZ digest and last-LLM historical expectation
use the admitted predecessor; KMC, Komagataella, current graph/cache assertions
and the immutable ledger remain intact.

Local proportional checks started at revision `8ad0cacc` with the reviewed
working changes, using Python 3.13.12. These are not a clean aggregate QC run:

| Check | Actual result | Private raw log SHA256 |
|---|---|---|
| One actual-proof positive canary | 1 passed; 12 warnings; 2.34 s | `ee868d1daa61b845c6029ce3c0725c1cbcbd9550e0579b4c7aacc5008435ffbd` |
| Full scoped proof controls and batch60 | 25 passed; 12 warnings; 10.05 s | `ec39425326571a2f3aaa0ac8cf52cdd5930508ebfbf54cc9954b77bac19bb4cc` |
| Native lint | Black 759 files, Ruff and mypy 52 source files passed | `629b21f3652196eee977a104b5a4261bb002d3c5c5922b91661d44e64ee4c727` |
| Native check-record-reviews | Completed exit 0 | `e300e470c5c4af1534b0daa5518fe5830cbb1815fbd5823f4bd96134a8e6a5b6` |

The pytest warnings concern the installed LinkML/Pydantic deprecation; lint also
retains the existing malformed-noqa warning in gtdb_ground.py. Completed command
triplets are retained under `.temp/phase2-schema-20261115/kz344-*`.

The canary establishes the real stage/apply/history/check/save/checkpoint/export
and strict historical-admission path for one complete genus ambiguity set. It
does not establish strain genomes, resolve the crosswalk's unknown release,
validate unread primary material, perform full-corpus QC or complete records
498, 369 and 405. Those three remain at accepted source preparation and require
their own exact candidate review and preserved native execution.
