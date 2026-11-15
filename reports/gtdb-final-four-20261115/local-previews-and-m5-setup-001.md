# Local previews and isolated M5 preparation

The thirteen reviewed preparation files were published at
`c9bb51a8b2a5591400dc8f170f043e59642116ce` in draft PR2927. This checkpoint
records subsequent private local previews and M5 setup. No canonical record,
source cache, historical caller, shared helper or scientific claim changed.
The remaining whole-record M5 canary is not complete.

Each local unit passed a free plan before the unchanged native stage helper
processed its original-basename private copy. Actual receipts record clean
c9bb51a8, Python 3.13.12, native exits 0/0, unchanged captured inputs and
unchanged local database stat observations. All input hashes and the complete
candidate diffs were checked.

| Record | Native delta | Verified inputs | Candidate SHA256 | Receipt SHA256 |
| --- | --- | --- | --- | --- |
| Transwell091 | Five reference blocks/statuses and two native events | 33 | `dcbc318e97a4be7478f3eb1afebdfb9d9911588ac53e75b0030ccf5bda1226cc` | `4ecbf029e7792fd928d9a452614d9e55776abdf373d74c6299b0a8892061000e` |
| Nasal395 | Nine reference blocks/statuses and two native events | 32 | `e161af858293a47472d973db39dc4d47d47406fef86548f70c9dabb64c18648c` | `ae21ec53b9fe869785bf2ed231c2a5891cda714d0a0942c60fe0a9393776fcce` |
| Rumen398 | Four reference blocks/statuses and two native events | 31 | `5913e5e9927c1e21dd06fe8163b3c34b55e316cf5ed9a8575a34d394423c0595` | `5f91fe468031ae9953af2c5fc4e5fe95e28e29505e97afc098a5a7549d0318af` |

Candidates and native receipts/logs/diffs remain under
`.temp/gtdb-final-four-20261115/{091,395,398}-local-candidate-001/`.
Transwell uses the corrected source binding002 while preserving the failed001
locator and historical October15 no-crosswalk notes. Those dated observations
do not describe the new preview's current reference mappings. The reporter
pair, separate three-member assay and SC11 designation conflict remain exact.
Nasal retains nine distinct included stocks, separate supplement support,
excluded challenge strains, empty biological graph and unresolved publication
status. Rumen preserves its three-option S. equinus ambiguity and all five
stocks: native stdout processes five taxa, while the appended event correctly
records four changed statuses. Rounded reference fractions do not acquire
invented support numerators or study-genome equivalence. Scientific findings
1467, 1640 and 1658 remain unresolved.

Local plan/stage recorder triplets are in `.temp/phase2-schema-20261115/`:

| Recorder | Exit | Raw log SHA256 |
| --- | --- | --- |
| `final-four-091-local-stage-plan-001` | 0 | `594aca782cad71660dd9a244c9719e840684b410df8dbbf2c3a7fc654ef138b8` |
| `final-four-091-local-stage-001` | 0 | `ce768c7489b78e60ecc625f3718cc1b992ff90f88524842e72b09967dc8f2270` |
| `final-four-395-local-stage-plan-001` | 0 | `83aa3f41ca5145b2c8aef061cb2b5be69920bd027869919ba8be3c7a13ae22a9` |
| `final-four-395-local-stage-001` | 0 | `667d08e9f6667d950ce636f0b65fa4d00358f190096278be47dc29a752411fd5` |
| `final-four-398-local-stage-plan-001` | 0 | `c4af22e14e3cf9802baa9cfc467c95ec45e4761ead903460ffae82341b38a6fb` |
| `final-four-398-local-stage-001` | 0 | `2d7d17e2423d0c88bdd6053e7c8fdbacddec8d2742da0b7557c1a5eefe77b1df` |

A new isolated M5 checkout at the same published c9bb51a8 revision was created
at `/Users/marcin/agent-work/CommunityMech/gtdb-final-four-20261115`.
The unchanged recorder ran explicit `uv sync --offline --frozen --extra dev`;
a separate actual invocation verified its installed Python 3.13.2. The
preserved anchor checkout was used only for Git object fetch and worktree
registration, without advancing its tracked state.

| Setup recorder, same local namespace | Verified observation | Raw log SHA256 |
| --- | --- | --- |
| `final-four-m5-fetch-001` | Published commit fetched | `c01f1ccc702ff0da806a87eacbfeb427632af43bedfc7a85995c3709c9e13c79` |
| `final-four-m5-worktree-001` | Isolated detached checkout created | `e884c110b0344a4d51055e456a538f99819a5d498eb576bbda054890e33fedb4` |
| `final-four-m5-install-launch-001` | Inner offline installation receipt reports exit0 | `a93f37ad7312df6d973a5f000d672469bb448684808fa4fe9c7f7ef0a88b6afe` |
| `final-four-m5-head-verify-001` | Actual remote HEAD equals c9bb51a8 | `d10dd2c6ec6361fd13d5f4c3c6fc51a142e81fadfb7b8227013a3f7a5e83ba20` |
| `final-four-m5-runtime-verify-001` | Installed interpreter reports Python3.13.2 | `37c71daf531d479b497f6e6eb964f6af1aef21097615012f1fb678a0263ec020` |
| `final-four-m5-source-transfer-canary-001` | One crosswalk file persisted | `23fe20abaaf84649158256a2b2f276a69edf800229d37107ad13075013ba3961` |
| `final-four-m5-source-canary-verify-001` | Actual remote crosswalk SHA256 equals761d5537 | `520580e154f578f65635e068badbff43e138d4d71c6ab599b2160ac2a5b92d01` |

The inner M5 `final-four-m5-install-001` log has SHA256
`5d3087e13d62758cb68a6388ebd08e0c6f5bc980003cce094d6f100914a1fd76`.
The one-file transfer used the existing recorder with
`rsync -avR --ignore-existing --files-from`; remote readback returned the full
crosswalk SHA256 `761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd`.
That proves only one file's exact persistence.

Automatic approval review rejected the subsequent six-file Sorghum source
transfer before process execution because exact private-payload/destination
permission was required. The list
`.temp/gtdb-final-four-20261115/348-private-inputs-001.txt`, SHA256
`c6c02f5becea4d9156d1c02f4918a42249dda115e35c332a249facc3287a4e2f`,
describes 7,129,166 bytes including the already copied crosswalk. Its destination
is the isolated checkout above on `marcins-MacBook-Pro-3.local`.
The refusal is retained in the same private directory as
`348-private-transfer-rejection-001.md`, SHA256
`a8a72ea3d21ccbb31a38b89332dbd805979e33e9ab1cc6151a3d2d7c3377d3b6`.
No success receipt exists for that rejected command; no retry or alternate
transfer occurred. Shrimp and other denied scopes remain separate.

Actual M5 staging and the full Sorghum348 application/check/history/saved-review
chain remain pending exact permission and complete input verification. No
remaining record may be applied before that complete canary. These local
previews and setup checks are not scientific approval, generated-product
validation, aggregate QC or merge authorization.
