# Shrimp, thermophilic reactor and Sahara source preparation

This branch prepares current-reference taxonomy corrections for records 436,
416 and 494. All three canonical records, historical ledgers, source caches,
shared curation helpers and scientific claims remain unchanged. No canonical
application, remote source transfer, native post-application gate or saved
diagnostic had occurred at the preparation checkpoint described below. Later
local previews, the isolated M5 setup and the pending private-transfer
permission are recorded in [local-preview-checkpoint-001.md](local-preview-checkpoint-001.md).

The isolated checkout starts at published integration revision
`2db92b640ae1300d0945f4d635ba899c74068249`. Its development environment was
installed with explicit local `uv sync --offline --frozen --extra dev`; native
reports identify Python 3.13.12. The unchanged reporter uses crosswalk SHA256
`761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd` at the
native writer's required private `kg-microbe/data/raw/NCBI2GTDB.tsv.gz` layout.
Local NCBI authority is bound by file identity/stat, not a database content hash
or ontology release. Neither source modification time nor correspondence
success establishes a GTDB release.

| Record | Assessed source and native scope | Retained limits |
| --- | --- | --- |
| Shrimp436 | Eight genus descriptors; six same-name results, Exiguobacterium to Exiguobacterium_A, and Tritonibacter to Epibacterium | Abstract-only eight-isolate/four-SynCom roster; unknown species, strain codes, genomes, mixing ratios and challenge timing. Exiguobacterium_A is the non-type majority at 49/83 versus 34 references in the type clade; Ruegeria 30/44 and Bacillus 4981/8737 are also non-unanimous. |
| Thermophilic416 | Three phyla, one class and two genera; six overlapping descriptors | Methanobacteriota 2815/5300 and non-type Bacillota_A 226306/451729 are narrow reference majorities. The paper's qPCR control species are not reactor stock identifications; total DNA does not establish viability or activity. |
| Sahara494 | One renamed species reference result and five genus results; existing Paenibacillus ambiguity remains unselected | H. trueperi's exact-ID route reports seven genomes and fraction 0.86 under H. aidingensis; no numerator is reconstructed. The source is a 336-isolate collection across five sites, not a seven-strain SynCom. All 33 existing Paenibacillus alternatives remain intact. |

The proposed mutable scope is 20 descriptors among 21 whole-record taxonomy
occurrences. Reference populations do not identify study-stock genomes,
measure community abundance or establish biological mechanisms. The authored
configurations retain exact native values and explicit per-occurrence source,
population and naming judgments. Expanded configurations are produced through
the unchanged committed composer; they do not infer scientific support.

One whole Shrimp436 route report ran and its persisted output and all captured
inputs were verified before the same launcher produced the three-record
report. The separate source binder then checked the first accepted Shrimp
configuration against exact source bytes, local identity/rank and the retained
native report. These canaries prove local read-only route/binder persistence;
they do not establish remote application or saved-review persistence.

| Recorder name | Verified observation | Raw log SHA256 |
| --- | --- | --- |
| `shrimp436-native-route-canary-001` | One whole record; 1,476,246 bytes; all 13 inputs verified | `4ad7792a8b9d550bb9b7793804190f1256d6e4c22392de98948a2882f31ca572` |
| `shrimp-thermophilic-sahara-native-routes-001` | Three whole records; 13,512,549 bytes; all 15 inputs verified | `0ded5f54dacbbb462b75677374d973f7a41914f1ebc1df5b9551c3afdda4528d` |
| `shrimp-thermophilic-sahara-native-inspection-001` | Native inspection-only capture of three maintained targets and nine source/guard inputs | `0cd6421f1321d5fc2f1495775b0ee03f5dced546a3e3697505792f9b9f4d8fc3` |
| `shrimp436-source-binding-canary-001` | Accepted first source unit; 246,282 bytes; all 25 inputs verified | `ad5c42d353b6cfea8bd65b18e397a3f0bcbe3f310c4b817631a7f89c10e1de31` |
| `thermophilic416-source-binding-001` | Accepted second source unit; 1,855,683 bytes; all 25 inputs verified | `542824ce02648384346aabc49e8c70aaf39f608270903c5b209902cb26412af4` |
| `sahara494-source-binding-001` | Accepted third source unit; 168,866 bytes; all 27 inputs verified | `bf2f16c15c82c111a2da8855345aad1d7b3df9c94e4daaea4f7e9e2aadea74cf` |
| `shrimp436-local-stage-plan-001` | Free native plan passed before the private preview | `29fea79cb7295c9c158dbc26df843995e4f1fbc479b8fa45c7258e19d4e0a9b3` |
| `shrimp436-local-stage-001` | Original-basename private preview; both native operations exit 0 | `f4507b0398784d7660ab629c787b9cdf0015d877e109cc21aebe3d99d3a17173` |
| `shrimp-thermophilic-sahara-preparation-lint-001` | Black 772 files, Ruff and mypy 52 source files pass | `021c6394515fa626c54ef5b9f8eb440bc8fb0188ffeeb9a395a2cfca064a3bab` |

Recorder triplets remain under `.temp/phase2-schema-20261115/`; raw native
source outputs remain private. Initial install status was clean; subsequent
receipts explicitly record the new untracked preparation files. No clean-tree
QC claim is made. The lint warning about quoted `noqa` text in unchanged
`scripts/gtdb_ground.py` is the existing issue2915, not a changed classifier or
an observed route failure.

The independently accepted Shrimp local preview is retained under
`.temp/gtdb-shrimp-thermophilic-sahara-20261115/436-local-candidate-001/`.
Candidate SHA256
`c61f66bc661dfe2823723d8db8176db221ea9e25299e7523ca6cdda9f9b75414`
and receipt SHA256
`a7d602cac5729e0bbc6a3b261b8a629df611906f9a40f2492c8c390060aa3421`
bind eight native reference blocks, eight statuses and two inline events. All
29 stage input hashes verify. Existing notes, variant memberships, single
community-level protection node, biological claims and old history are exact.
The non-type-clade warning is retained in the bound source context; the native
block does not identify the unnamed experimental isolate.

Separate read-only passes accepted all three authored/expanded scientific
scopes before their binders ran. The small new route-summary jq helper only
projects exact native outcome fields for inspection; it changes no classifier,
source result or canonical record.

Historical limits remain explicit. Closed issues1105/1106 record the Shrimp
missing-crosswalk and unsupported-timing corrections. Closed1932 records the
thermophilic graph correction; [open1935](https://github.com/CultureBotAI/CommunityMech/issues/1935)
still owns non-graph viability, group roles and abundance wording. New
[2924](https://github.com/CultureBotAI/CommunityMech/issues/2924) records the
Sahara causal-geography and isolate-collection concern after all-state issue
deduplication; its bounded source finding is preserved in
[sahara494-source-scope-finding-001.md](sahara494-source-scope-finding-001.md).
No issue is closed by a taxonomy correspondence.

Live issue reads were retained through the same recorder after a verified
single-issue snapshot canary. Exact source snapshots, available for the later
saved assessment's input bindings, are:

| Private log under `.temp/phase2-schema-20261115/` | State at capture | SHA256 |
| --- | --- | --- |
| `shrimp436-issue1105-snapshot-001.log` | CLOSED | `39176919ca270a8de596a3937c94af1e7b37f09ca3b02c4ff805b0e822084804` |
| `source-issue1106-snapshot-001.log` | CLOSED | `c4811ab4adffcc7152a951ca9fd6156bb8625d56bf902b8f5db6c0ddf3d2d7e0` |
| `source-issue1932-snapshot-001.log` | CLOSED | `522792413616396d02a84ad7be4b57ab7df0be2b594fc369d802551745518005` |
| `source-issue1935-snapshot-001.log` | OPEN | `7fb1d6ee9d66733a1fb6fa47bcce5191c915ba5c02dc269c70a9a4cedb92a967` |
| `source-issue2924-snapshot-001.log` | OPEN | `81ba949503c2c60b35c495d8c310603f752ecae36bf4a4b58e9fffadccc8c800` |

Sahara's authored source configuration already binds its issue snapshot.
Shrimp and thermophilic configurations retain their earlier accepted bytes;
their captured issue snapshots must enter the eventual saved assessment as
additional inputs. Historical callers101/120/135 must retain all current
biology and immutable ledger facts. Future strict admission may project only
the exact affected old digest/history predicates, preserving the other records
and their existing successor chains, including the separate492 work in135.

The first actual whole-record canary still requires a published preparation
revision, isolated M5 staging, independent actual-candidate read, guarded apply,
native history and eight checks, immutable partial diagnostic, complete input
checkpoint and strict successor proof. Remaining applications cannot precede
that verified chain. This preparation is not full scientific review, current
product validation, aggregate QC, campaign resumption or merge approval. The
previously denied private transfers for unrelated lanes remain untouched.
