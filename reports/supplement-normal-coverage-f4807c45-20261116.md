# Switchgrass normal-reference checkpoint at f4807c45

Both hosts measured the committed Switchgrass record at revision
`f4807c459e0986ff9d2aa41365f393b1e9ba4d2d` through the native reference dispatcher
and normal repository configuration. Each run counted 37 snippet surfaces,
37 validator calls, 37 substring comparisons and 37 matches, with zero native
issues or measurement errors. All captured inputs remained unchanged. This
completes the normal-reference measurements that were pending in the earlier
[canonical adoption checkpoint](supplement-canonical-adoption-20261115.md).
It does not complete scientific review, corpus-wide references or full QC.

The measured record is
`kb/communities/LBNL_Switchgrass_Soil_SynCom16.yaml`, SHA256
`bcc2759c9da7c4059330726a1b154df600ec394d1106be2dcc1f4d247eed5eb9`.
Both measurements used configuration SHA256
`8d6620c22f3f0cfd02bdc129a3bdc3d9319ea9d63266756580868798cce6120a`
and lock SHA256
`1e1374a77207de170502a89ea7eebcb018d65daac8b0faecc39988d955f3df62`.
The installed validator is the reviewed revision
`6b71e7f4b353b5b36000fda03da78b61734e3fc8`, version
`0.2.1.post1.dev0+6b71e7f`. No article cache or quotation was changed.

| Actual measurement | Receipt SHA256 | Native recorder log SHA256 |
| --- | --- | --- |
| Local, `switchgrass-canonical-coverage-local-001` | `039d7557d41dc4a96bbc57453a57db22051919edd98c9685f4f14777713838c1` | `4fa4c33912e3c446ab8da880f0e35a070720ebb101d2a46c4ef0ab19c93aefb9` |
| M5, `normal-coverage-m5-001` | `f1d9a3d4165fe15c55f5794b477722ae85db4c331c9adfc6e95b33e3fab033eb` | `b6504f12331f5df58115b9f23da12dfcb65c1dce46aeb3115729f444a0bf11b3` |

Each directory is under `.temp/supplement-adoption-1996-20261115/` and contains
`receipt.json`, `measurement.json` and `measurement.log`. The receipts record
the exact selected record, all 549 declared community/isolate paths, and 1,502
input hashes. The 549 declared paths are an inventory, not a claim that all
549 records were validated. Root independently rehashed all 1,502 captured
inputs against the local files after mirroring M5's evidence. Native receipts
also report no input drift during their respective executions.

The two hosts' measurement JSON files are byte-identical, SHA256
`b7db232076e7d7d53e969011d53b5f0a770bbd553575b6e902a5b321f81dff66`;
their measurement logs are byte-identical, SHA256
`f2e4d3c3bee1b93b02c6426894dae5d33db4204fa627857f5b44ff0b39242921`.
The receipts preserve different execution times. The three selected identities
bind the unchanged OAE516, Bacillus and OAE603 quotations to table/row/cell
1/12/2, 1/18/1 and 1/18/2, respectively, under PMID:36472419.

| Selected source component | SHA256 |
| --- | --- |
| Public catalog | `d3e425adfb24a75f30d7e1dd9aac729388861e6b18da6782ac0d6099e87c11f1` |
| Local DOCX asset | `5bfa02fdb94538e9405fb0ec7d7b0dad338791a5ca0b4b651589f33148c8e0e7` |
| Replayed table-cell projection | `c322c14c7e754df924e3e3151fb3d8e18564537dd0448e43d9a856d4e3ef32a5` |

M5's actual provisioning receipt has SHA256
`52820ef523e667a2e6dc3ef9a5b8b9b976335b2d0f3b640800b0bd25a7ec90ee`,
mirrored locally as `normal-source-install-m5-001-receipt.json` in the same
private evidence directory. It records all three destination hashes and no
canonical-record or configuration edit by the provisioning helper. The
approved content was already present in M5's verified preparation; this step
did not acquire or upload new paper content. M5 retains its original config
beside the current one as
`conf/reference_validator.yaml.bak-before-normal-source-20261115`, SHA256
`297b1fbd8a77ba2f89ca7126339deabc0f61ee91013d054d0fa64caef59a630d`.
Restoring that backup removes the normal catalog selection and reintroduces
the need to configure selected sources before supplement assertions can pass.

M5's standalone `just validate-references` invocation on this one record also
passed at `f4807c45`, with three selected-source identities. Its native raw log
is `.temp/phase2-schema-20261115/supplement-normal-references-actual-m5-001.log`,
SHA256 `c3d77b5960428802b6946afb017e52230d34b30bd0208396711ef29cac854196`.
The separate outer SSH recorder has different bytes. The CLI's printed
`Total checks: 0` is an issue counter; the independent instrumented native
measurement supplies the comparison denominator. The earlier standalone local
reference pass retains its original `3b1c7426` plus working-changes execution
context in the preceding checkpoint.

The local post-commit `just check-docs-current` invocation passed at
`f4807c45`, native recorder `supplement-docs-switchgrass-current-002`, exit 0,
raw log SHA256
`fdd91098d245e6dec2ffb3baa152a0135a784c9fc77d77dd688eba86c7829502`.
The preceding exit-1 run remains preserved; committing the reviewed manual
coverage guide resolved its Git-status failure. No gate was weakened and no
generated page was manually edited.

This checkpoint retains the existing scientific blocker under issue1548.
The new full scientific assessment and its strict successor evidence are
still pending here. Earlier immutable reviews remain untouched. The two
source errors found before saving the new draft are recorded under issues2940
and2941; neither their correction nor these lexical results establish a
completed scientific review. Final combined `just qc` and the separate
corpus-reference work still require execution on their recorded revision.
