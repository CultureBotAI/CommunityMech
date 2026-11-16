# Switchgrass canonical source-locator checkpoint

The three independently reviewed Table S1 locators were applied on M5 at
revision `3b1c7426fdb5447ae1fc34d10e463ee6b560fa40`. They identify the unchanged
OAE516, Bacillus and OAE603 quotations at table/row/cell 1/12/2, 1/18/1 and
1/18/2 under PMID:36472419. One truthful LLM-assisted inline event was appended.
All prior history, quotations, stock identities and biological claims remain
unchanged. The Methods/Table S1 correspondence finding under issue1548 remains
unresolved.

The host-specific [source plan](switchgrass-m5-locator-source-plan-20261115.json)
has SHA256 `8768d3d4727c2d1d78aa047b02355285174b9eb925cac90724ca5caf51b7cd2e`.
It binds the exact original record, preparation, runtime and five independently
read actual M5 controls. Selected and restored runs each matched 37 of 37
snippets with three verified source identities. Article-only matched 35/37;
wrong-cell matched 36/37; wrong-parent made 37 validator calls, 36 comparisons
and one hard source-selection refusal. Those are scratch-control results,
separate from validation of the subsequently applied canonical record.

| Actual M5 artifact | SHA256 |
| --- | --- |
| Before record and retained backup | `bb31b1df4a9be2241453528101fc5d55657c23eccf1d58ce1cc9639e5912b368` |
| Reviewed candidate and applied canonical record | `bcc2759c9da7c4059330726a1b154df600ec394d1106be2dcc1f4d247eed5eb9` |
| Stage receipt | `43d5e04aad76dad1fd8bef7f0b49d2fc7532f7a0fff37750d23ba9bb6e34ccc4` |
| Application receipt | `54eead0a6475128efde3a1afb2250b7ba75ff369b1c2253a53650caeed7f2983` |
| Native validated serialization | `6f2bd3a71d3a3a90045de347d0bdcac05365145436439fcf46c015d70af0b25f` |
| New native history sidecar | `199ecac05a60473ca084bbcda5c72675178ea7df4d2ab3592e9395d04a3896ea` |

Stage and application used free plans before actual operations. The guarded
writer verified all captured inputs, replayed the source extraction and checked
the exact candidate before replacement. The application receipt retains
`scientific_review: false`. Native application log SHA256 is
`ecee227d1bacefadbc965b1c7622797c6eb3198ca2138a837d02e3fb263a2d64`.
Execution was detached at the recorded revision. The named M5 branch
`fix/supplement-adoption-m5-1996-20261115` was created afterward without changing
HEAD. The local record was synchronized only after matching the original
backup and both independently rehashed copies of the actual M5 result.
The named-branch preflight gap is tracked in issue2939; the actual historical
sequence remains preserved. The reusable M5 launch guard is follow-up work.
The separately generated native sidecar is
`history/records/LBNL_Switchgrass_Soil_SynCom16/2026-11-16T003751Z-codex-245811.yaml`;
its exact metadata was independently read before local synchronization.
The [public application receipt](phase2-science-20261115/applied-chain-switchgrass-locators-003/switchgrass-locators-apply-001.json)
is byte-identical to the actual private receipt.

All eight actual M5 steps passed at the frozen revision. The native recorder
captures the command, Git revision/status, lock hash, raw log hash and exit;
separate before/after verification established the unchanged applied record,
original config and eleven older sidecars. These receipts are not being
represented as a different hash-capturing gate runner. Native terms reported
validation passed without an assertion denominator.

| M5 recorder under `.temp/phase2-schema-20261115/` | Raw log SHA256; each exit 0 |
| --- | --- |
| `supplement-locator-schema-actual-m5-001` | `da31c1cee34eed4547a5cd32f1f265870fd233b24d751fdef57f59e67d212ebc` |
| `supplement-locator-strict-actual-m5-001` | `73f74eb54d6459df153e6d88e1603564ad745b2b811d60cba3215c2902d98b71` |
| `supplement-locator-new-history-actual-m5-001` | `aa60c8ed48d0eef93441db4600fb92d87c80bf4a7c4026cb012c78e70d193e6f` |
| `supplement-locator-history-actual-m5-001` | `700b44227c4cf01270ac26f16b308622de0b26f48d71aec49cdfaaab87620f0a` |
| `supplement-locator-gtdb-actual-m5-001` | `cf1b678cc42f434b31ccd174fa36a9697689cbcebdbad0b0b7a8649c33156843` |
| `supplement-locator-domain-actual-m5-001` | `3af45fb355968724994a23ea1833dd6ca5b3fd28b6f622f5142432282341cba6` |
| `supplement-locator-scalars-actual-m5-001` | `66b37e84153f5ebb64c3fc1ccc7b217eacd23ff5f1ef55a4d32edd14b8fe271e` |
| `supplement-locator-terms-actual-m5-001` | `15e57591150b96e4168292f4fd0b978aeada541f8500973dfa6cac3608ed2f98` |

The first schema dry run failed before validator execution because the local
machine's `just` path was used on M5. Its native exit127/log
`96ed84ece2a30fd55f74fc91d50e6ae6256866f9cb35f2678c034130900f9764`
remain retained. Plan002 used M5's `/opt/homebrew/bin/just`, passed, and preceded
the actual schema invocation. No validator or acceptance condition changed.

The normal reference configuration adds only
`source_catalog: conf/reference_sources/catalog.json`. The public catalog has
SHA256 `d3e425adfb24a75f30d7e1dd9aac729388861e6b18da6782ac0d6099e87c11f1`.
The DOCX and projection stay local and ignored; the provisioning helper checks
their fixed hashes and replays the projection, without acquisition or overwrites.
The local actual provisioning receipt is
`.temp/supplement-adoption-1996-20261115/normal-source-install-001/receipt.json`,
SHA256 `7159ee7feb987dd7fb93bf9402358cbe54355bd16c91878d84fa7659d5e04331`.
All three destination hashes were independently verified after the real run.
The original config remains beside the edited file as
`conf/reference_validator.yaml.bak-source-catalog-20261115`, SHA256
`297b1fbd8a77ba2f89ca7126339deabc0f61ee91013d054d0fa64caef59a630d`.
Copying that backup over the config restores the previous configuration;
explicit supplement assertions then require catalog configuration again.

The following native local commands ran at `3b1c7426` with recorded working
changes. These are scoped checks, not full clean-revision QC.

| Recorder under `.temp/phase2-schema-20261115/` | Result | Raw log SHA256 |
| --- | --- | --- |
| `supplement-normal-source-plan-001` | Read-only provisioning plan passed | `ebfd056875612c70bdd6299b03c8e8b65074b0ebbba3fa9d49f4db99394b2324` |
| `supplement-normal-source-install-001` | Actual provisioning passed; three files persisted with exact hashes | `575264e9a1dbff446fc1d2028612f76fa0aeee0444ff8efe1985b937807313c7` |
| `supplement-normal-canonical-references-local-001` | Normal `just validate-references` passed and emitted three exact selected-source identities | `5ef3166799920129190e44b1c1d3c85eda5a8c4d91dbbb86e1245fc04199795a` |
| `supplement-normal-source-lint-001` | Black 802 files, Ruff and mypy 52 sources passed | `0c839f907cd4ee4e5fc06389f4b527a5714b8d7fae9969b12e194dd3c50a9dda` |
| `supplement-docs-switchgrass-canary-001` | One page rendered and verified before full generation | `e010f7d54f94b4c2c1a9d00bc2129b6cd33a2e7e5c2e95b2a05dac8b66ae110e` |
| `supplement-docs-switchgrass-all-001` | Full generation passed; generated files match the existing Git files | `7e13574cac6b543b735ceda71c55a012292921a2962c43d93b7f513b77207d60` |
| `supplement-docs-switchgrass-current-001` | Exit 1: the reviewed human-authored coverage guide was still uncommitted; all generated files matched | `00148918e6e4c3ecf70006472dc2d200c9cb648c7866ba1ad8bcc77b7163e7c6` |

The docs-current gate checks the entire `docs/` Git status. Its first run must
be repeated after committing the reviewed guide; no generated file or gate is
being changed to suppress this failure.

The normal validator's `Total checks: 0` remains an issue count. It is not the
comparison denominator. Committed-record coverage, M5 normal catalog/reference
validation, the post-commit docs-current gate and full QC are still pending
at this checkpoint. A new full scientific assessment will bind the applied
record and actual evidence, correct the earlier review descriptions under
issue2938, and retain unresolved scientific findings. The old immutable reviews
are unchanged. Neither these lexical controls nor the new routing complete
scientific review or authorize a merge.
