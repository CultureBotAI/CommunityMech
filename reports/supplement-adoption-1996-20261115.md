# CommunityMech supplementary-source adoption checkpoint

The isolated adoption branch adds optional structured source selection to both
`EvidenceItem` and the shared `SupportingReference`. It prepares a real
Switchgrass canary using unchanged consumer schema bytes and the retained
supplement. The canonical Switchgrass record and the installed reference
validator remain unchanged at this checkpoint. This is preparation for
[issue 1996](https://github.com/CultureBotAI/CommunityMech/issues/1996), not a
completed reference or scientific review.

The branch starts from integrated Phase 2 revision
`2e9b51802d35adc806e1bd98c435e3a5fd0eaf48`. Independent review accepted the
schema, generated model, comment correction and new consumer controls. The
schema/helper checkpoint is `2e27a749`; no changes were committed to main.

## Native schema synchronization

The first synchronization used the independently reviewed Claw schema revision
`75ce01bdd326ce74278bc2bbcde7f78f002eb803` through its native repository settings,
configuration validation, lock and transactional synchronizer. The helper as
executed is retained at CommunityMech commit `09254e5d`. Its exact three-file
plan changed the shared schema, governed checker and source pin.

Private receipts under `.temp/supplement-adoption-1996-20261115/` are immutable:

| Receipt | SHA256 |
| --- | --- |
| `schema-plan-001/receipt.json` | `4d9baba245fce7156fdfecc50c01cd1e2ac3234133edaf88ecaa175179ffa770` |
| `schema-apply-001/receipt.json` | `14cb3c0194d77bfd0f74db7321ff633757aedc0aa3606b64987da1a306fd7796` |

The shared schema has SHA256
`01d09b7d91a21235b97cc37d8482518a7b2c36ab63d8898796fede3877061ed9`;
the consumer schema has SHA256
`a8db0b22ee6fb930fa9e603d881fd4b67cd1f1433e8fd716db13ca7db116febb`.
`just gen-python` produced the model with SHA256
`70a420af2534049434e8e563b82bdb9cb954765681267ee273d0cca97be38a77`.
The first generation wrote the model but failed in formatting because the new
environment lacked development tools. Its unformatted output and failed log
remain retained. After frozen offline installation of development extras, the
complete native recipe passed; no generated model was edited by hand.

Claw's initial hosted run found stale template-baseline hashes, retained under
[Claw issue 1220](https://github.com/CultureBotAI/culturebotai-claw/issues/1220).
The reviewed baseline correction was published at
`846c4635c305ff1d837fcb4aa7e261a01c4258e3`. Its native consumer plan changed only
the governance pin. The independently reviewed follow-up helper at `18f11ec9`
planned and applied that one-file update from clean revision `4ea7f9e2`.
The first dry run failed on sandbox DNS before writing; its log remains
`9627d0861b2bd9fe772ba68fd22b2c4063444dcb0459aa159980ec77ec5ad201`.
The separately numbered retry verified the exact public manifest and artifacts.
The actual application rechecked the plan under the native lock, validated the
configuration and verified zero remaining drift.

| Final pin receipt | SHA256 |
| --- | --- |
| `final-pin-plan-002/receipt.json` | `a190b0fadc86b2f4a2a27cdbfa50ac4ecc3c134348423db5e9036837a0ce56cf` |
| `final-pin-apply-001/receipt.json` | `86f9eba719d1e4eb085e14655c7ba08d83ae7d5df38107d508b8a0cc48782891` |

The resulting pin bytes hash to
`9b947f02f224974c46a5766717675b205fd279af75c6dfbb0a6ea2c6a98f3952`.
This identifies the reviewed draft Claw head; it does not claim that PR has
merged or authorize a merge.

## Consumer checks and exact-runtime canary preparation

The new schema controls use CommunityMech's frozen LinkML 1.9.3 and
linkml-runtime 1.9.5. They test both evidence classes, all six required locator
fields, invalid kinds and coordinates, blank identifiers, unexpected fields and
preservation of existing citations. Generated Python-model tests check nested
locator construction and unchanged reference/snippet values. Model construction
does not replace strict JSON-schema or runtime source-selection checks.

The first actual `EvidenceItem` schema canary passed before the wider focused
run. Recorder triplets are under `.temp/phase2-schema-20261115/`:

| Recorder | Result | Raw log SHA256 |
| --- | --- | --- |
| `supplement-schema-gen-python-002` | Native generation and formatting passed | `80de99c824f0edbe0bfd83ec87085b43e792987c38e82546aef1b34135ce7ed1` |
| `supplement-consumer-schema-canary-001` | 1 passed, 12 warnings, 3.41 s | `8c321a2b4352f35b4267ead02c37d2c2b45493081cff100e9e05d66314710c7b` |
| `supplement-consumer-schema-controls-001` | 65 passed, 14 warnings, 29.93 s | `a51baac65594a59ec9962d249750fc96e516a7d0f0563bd808626fe7c47f6e7c` |
| `supplement-consumer-helper-controls-003` | 14 passed in the separate candidate environment, 1.62 s | `ececcbc6d9d746bb444123adae014c42949e3ec1440cbf12b6e4d537ee80b47e` |
| `supplement-consumer-helper-ruff-002` | Passed | `82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18` |
| `supplement-consumer-lint-001` | Black 799 files, Ruff and mypy 52 sources passed | `9c175381c65bd61d32b6af67e8789a61cf5fdae706662b3989f571c1f85dea88` |

The 65-test run includes existing datamodel, reference traversal, assertion
coverage and CLI coverage checks. The helper controls used the separate
installed candidate because CommunityMech still has validator 0.2.1. An initial
helper-test error matched the refusal message too narrowly; its failed log and
subsequent correction remain retained. It was not a source-selection failure.
Native lint retained the existing non-fatal GTDB comment warning tracked in
[issue 2915](https://github.com/CultureBotAI/CommunityMech/issues/2915); the
executed GTDB source was not changed.

The preparation helper copies the exact consumer schemas and adds only three
locators to a private scratch record. The runner requires a clean, explicitly
pinned validator checkout and a noneditable installed copy with identical
Python-module membership and bytes. It independently counts the 37 snippets,
observes native comparisons, checks complete source identities and rejects
network attempts. Article-only, wrong-cell, wrong-parent and restoration modes
retain their exact expected outcomes. The helpers reuse the previously reviewed
runtime canary with explicit source hashes; their consumer changes were
independently reviewed.

No consumer-runtime preparation or validation run is claimed here. The runtime
must first be published at an exact reviewed commit, installed with a retained
lock, and checked in this environment. The actual selected canary must pass and
persist before the controls or any canonical record change.

## Remaining completion work

Runtime publication and installation, actual
consumer controls, canonical locator curation with native history, current
generated products, complete QC and measured references remain required. The
stale reference-annotation comment is corrected under
[issue 2932](https://github.com/CultureBotAI/CommunityMech/issues/2932); no QC
recipe or matching threshold changed. Reference matching does not resolve the
record's scientific disagreements. No merge is authorized by this checkpoint.
