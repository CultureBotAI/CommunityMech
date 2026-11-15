# GENIA, HAMBI and MWF001 reference correspondence

The [MWF001 checkpoint](mwf443-outcome-001.md) records the actual isolated M5
application, eight native checks, saved partial diagnostic, complete input
checkpoints and strict successor proof for CommunityMech:000443. GENIA352 and
HAMBI423 remain preparation with private local previews; neither is applied.
These are scoped reference correspondences, not new full scientific reviews.

The preparation below describes the earlier published revision
`9b770f6603aa2714fc4f7f317768d8857fbb8d1e`, when all three canonical records,
source caches and historical assessments were unchanged.

The isolated checkout starts at published integration revision
`f18ca5b7f83eae0a9c8f537bdde6703760fee90e`. Its development environment was
installed with the explicit local `uv sync --offline --frozen --extra dev`
command. Actual route reports identify Python 3.13.12. The installation started
with clean Git status; route receipts list the new, untracked report directory.

The unchanged native route reporter used crosswalk SHA-256
`761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd`.
The local NCBI authority was bound by file identity/stat, not a database content
hash or claimed ontology release. Source modification times do not establish
a GTDB release.

| Recorder name | Persisted observation | Raw log SHA-256 |
| --- | --- | --- |
| `genia-hambi-mwf-443-route-canary-001` | One whole record; 28,824 bytes; all 13 captured input hashes verified | `7443cc16d1d8a2a27a6d89b7c10f7888c7d3b1ce4d492e24a03272da07335675` |
| `genia-hambi-mwf-three-routes-001` | Three whole records after the verified canary; 155,237 bytes; all 15 captured input hashes verified | `642b65eedd34f22993e8c085e73c53087cbed4cfb0b966a49d0a10eaa32f844d` |
| `genia-hambi-mwf-443-route-canary-002` | One whole record using the native writer's required table layout; 28,831 bytes; all 13 captured input hashes verified | `80870131ddf241501bc3a9ca56877cac55bb9bf2220cab98f53a2ed69c67bd8b` |
| `genia-hambi-mwf-three-routes-002` | Three whole records after the repeated canary; 155,244 bytes; all 15 captured input hashes verified | `2ec58f9651808455646ff8cc0d5f35b93642ba386b58b8f90b0a42fdab1d51c5` |
| `genia-hambi-mwf-443-primary-capture-001` | One anonymous primary XML request through the existing capture helper; HTTP 200 and exact article identity inspected | `657572afa216a9c45cbf2046b76b77d9b4b0d34beb7ec6758fe2e46ce92360ac` |
| `genia-hambi-mwf-443-primary-methods-001` | Native `xmllint --nonet` Methods text projection, 25,410 bytes | `889aae444080a3a5a003a2b31887dbe006651479738494fc608433fdc4e54ae6` |
| `genia-hambi-mwf-443-source-bind-002` | First source binder canary; 31,204 bytes; all 35 captured inputs verified | `eade95876fa7f5b4b1161c943dc057799da33efb629424a486d9da948e5151db` |
| `genia-hambi-mwf-352-source-bind-002` | GENIA binding after the verified canary; 43,486 bytes; all 25 captured inputs verified | `f71d63af12668735003794ad6f808dc3c5b5bd56b30ac63b652d5ad67e786a71` |
| `genia-hambi-mwf-423-source-bind-002` | HAMBI binding after the verified canary; 79,600 bytes; all 25 captured inputs verified | `6de51ae4896e7db6397a4c5f21296f5d79d85c0ea66fa7479a417500ca43116b` |
| `genia-hambi-mwf-443-stage-plan-001` | Free native stage plan passed | `ee0d9045f76158326bb4c3ecbc838da7bf5be78891cc6c958a5bc5ad15dc49a7` |
| `genia-hambi-mwf-443-local-stage-001` | Private original-basename preview, both native operations exit 0 | `d38e383b60d0ba154f25b3de9b47ee65b927a3e98177aa37f21f66cbdbabdd40` |
| `genia-hambi-mwf-preparation-lint-001` | Black 772 files, Ruff and mypy 52 source files passed; one non-fatal warning retained | `021c6394515fa626c54ef5b9f8eb440bc8fb0188ffeeb9a395a2cfca064a3bab` |

The native recorder triplets remain in `.temp/phase2-schema-20261115/`.
The canary verified the reporter's actual persistence and unchanged captured
inputs through the same launcher subsequently used for the three-record run.
It did not exercise canonical application, remote execution, native validation
gates, saved diagnostic persistence or aggregate QC.

Before binding or staging, inspection found that the 001 report's explicit
crosswalk path did not use the downstream native writer's required
`kg-microbe/data/raw/NCBI2GTDB.tsv.gz` layout. This setup finding is retained in
[2913](https://github.com/CultureBotAI/CommunityMech/issues/2913). The 001 native
observations remain unchanged; no writer invocation or fallback lookup used that
layout. Byte-identical table data was placed at the required private path, then
the repeated 002 canary and three-record report passed. Their native outcome
summaries are identical to 001. No shared helper or classifier changed.

The three authored 002 configurations change only the retained route triplet
bindings. Their expanded successors are MWF 002, GENIA 002 and HAMBI 003. A local
HAMBI composer command initially mistyped the input directory's date and returned
exit 2 after shell redirection created an empty 002 file. That empty attempt and
its explanation remain privately preserved. The corrected command wrote the
exclusive 003 file through the unchanged composer; no binder or stage consumed
the failed output.

The authored plans propose 28 selected descriptors: 17 generic reference blocks
and 11 complete ambiguity sets. HAMBI's sixteenth member, Paraniabella
yanshanensis / source Niabella yanshanensis HAMBI 3031, retains native
null/UNRESOLVED and stays unselected. Missing correspondence is not taxon absence.
Reference populations and rounded majority fractions do not identify the
experimental stock genomes, measure community abundance or establish mechanism.

GENIA retains all nine source species without invented strain codes or assembly
links. Its mass-balance and non-graph mechanism limitations remain under
[1468](https://github.com/CultureBotAI/CommunityMech/issues/1468).
HAMBI retains all 16 distinct input stocks, eight-cycle design and the distinction
between controlled carbon responses and selectively demonstrated trait/pH
mediation. Its historical notes about unavailable crosswalk access remain
historical. MWF001 retains four distinct strains, both documented name changes,
finite coexistence and residual-substrate/model limitations; the protocol,
stock-level and causal-extension work under
[1574](https://github.com/CultureBotAI/CommunityMech/issues/1574) and
[1575](https://github.com/CultureBotAI/CommunityMech/issues/1575) remains open.
These three issue states and bodies were read live during this preparation.

An ignore-inclusive search of the local CommunityMech worktrees, original local
checkout and `/private/tmp` found the MWF001 excerpt cache and historical full-text
hash references, but no file under the recorded full-primary names. This bounded
search is not a claim about every possible source store. One anonymous request
then retained the current Europe PMC XML privately using the existing
`pr2062_resource_fetch.py` helper and its fixed private namespace. The response is
193,775 bytes, SHA-256
`d8937ac8a63e479f1dbb43ed2054ebf435c498ebd3ffc714d7c5424bee98509a`.
Its front matter identifies PMID 42752228, PMC13598246 and
DOI 10.1073/pnas.2607664123 with a CC BY license. The MWF001 authored source plan
binds the Methods projection, exact XML and extraction command receipt. Neither raw
XML nor extracted full Methods text is included in Git. Original figure pixels,
separate supplements and experimental assemblies were not inspected here.

Independent read-only reviews accepted all three frozen 001 scientific scopes
and the additive path-binding successors. The unchanged binder then checked
current local identity/rank, literal primary anchors and every captured source
input. It did not assign experimental stock genomes or clear earlier scientific
findings.

The independently accepted local MWF001 preview is retained under
`.temp/gtdb-genia-hambi-mwf-20261115/443-local-candidate-001/`. Candidate SHA-256
`8cc08a2e439aa434b50bbfd4bc1679f16102331e82d2ddbec1dda65584a5750d`
and raw receipt SHA-256
`1ea4969e8d418434394bd0ba4665282765a69b18f98c2cfc45bdfed4bb142032`
bind two reference blocks, complete four- and three-option ambiguity sets,
four statuses and two native events. All 39 stage inputs were rehashed. Its
22 reference genomes at fraction 1.0 and 100 reference genomes at fraction 0.94
preserve the source name bridges and do not identify the study stocks. All stock
notes, biological claims and old history are unchanged. The canonical file has
not been replaced.

The lint warning concerns quoted directive text in the unchanged native script,
not an observed classification failure; it is tracked separately in
[2915](https://github.com/CultureBotAI/CommunityMech/issues/2915). No executed
native source was edited to suppress it.

Actual M5 staging, independent candidate read, guarded canonical application,
eight native commands, immutable partial diagnostic and complete input
checkpoint remain necessary before the first whole-record canary is complete.
Existing denied private transfers for the unrelated genus and ambiguity lanes
have not been retried or replaced.
