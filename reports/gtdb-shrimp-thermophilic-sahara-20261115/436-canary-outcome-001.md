# Shrimp 436 genus reference canary

Record 436 now contains eight native genus reference blocks and statuses, two
appended native events and one new history sidecar. Source genera, absent
species/strain identifiers, historical notes, four SynCom memberships, the
single community-level protection node and all other biology remain exact.
This is a partial taxonomy diagnostic, not full scientific review or corpus QC.
Records 416 and 494 have not been applied by this workflow.

The earlier private-transfer refusal remains preserved. After the human
explicitly approved the seven listed inputs, root copied them to the existing
isolated M5 checkout and verified all seven hashes. The retained transfer is
`shrimp436-m5-source-transfer-approved-001`; its remote hash listing is
`shrimp436-approved-inputs-m5-hashes-001.log`, SHA256
`07b148f91d0a393e4802fb3e9e4e75d705e75b0285e7cbf859959d5efe39229b`.
This authorization and transfer did not alter other lanes' permission holds.

All actual staging, application and eight native commands ran at frozen M5
revision `261941db9aa5c359dc7599f28e4648a6c9723396`, Python 3.13.2. Local
integration checks record revision `5ad73bc9764b9fadd4a686718450ae16845aa236`
and their actual working changes. They are not a fresh clean-tree aggregate QC.
The shared writer, gate checker, diagnostic builder, provenance wrapper,
exporter, strict admission core and mutation factory are unchanged.

The accepted local preview was retained. Actual M5 staging changed only the
two event timestamps relative to that preview; root independently read the
actual diff, native output and all 29 input bindings before application.
The exact transition is:

| Artifact | SHA256 |
| --- | --- |
| Before record | `f23b26c7b39205a716e77e5149c06e2c4e4c618dec523a3e5245c65370ec7c0e` |
| Actual applied record | `4152f796b81669cb2ebb9a2229ce35e8364e5f49c67f2ba454f1aafa0f1a9301` |
| Actual stage receipt | `598128e4353f750d0a539258289709c5a9988548c4d15cb0d7e9238bf26a807f` |
| Actual application receipt | `7ace8f2a47468e00800ee6d0478f3551b78b16f63d0717630a4ff7b597ae3b7b` |
| New history sidecar | `fbdc5c19d40c8c9be43ba16e1a79f6ecb0b9d6278500366e13c4846679c020d2` |
| Public strict manifest | `f08c08480c9af4b71c844d0daf9299f43c703111064f9f73062f7c50f16647fb` |

The native events are both timestamped `2026-11-15T23:50:10Z`. Eight free
plans preceded eight serial actual commands: schema, strict, GTDB coherence,
domain, scalars, native new-history, history and terms. Every actual receipt
records exit 0, `plan:false`, frozen execution revision and unchanged inputs.
Strict validation reports one file and zero errors; terms reports its literal
pass. Exactly one new sidecar was created and the old sidecar remains unchanged.

The reference populations remain carefully bounded:

| Source descriptor | Native reference result | Filtered support/total |
| --- | --- | --- |
| Ruegeria | Ruegeria | 30/44 |
| Microbacterium | Microbacterium | 591/591 |
| Tenacibaculum | Tenacibaculum | 264/270 |
| Demequina | Demequina | 88/88 |
| Exiguobacterium | Exiguobacterium_A | 49/83 |
| Bacillus | Bacillus | 4981/8737 |
| Paracoccus | Paracoccus | 486/486 |
| Tritonibacter | Epibacterium | 134/134 |

Exiguobacterium_A is a non-type majority, with 34 references in the type-bearing
alternative; Bacillus spans 44 native clades. Rounded native fractions are
preserved. None of these counts measures shrimp abundance, experimental
isolates, protective effect or independent study-stock placement. The source
Tritonibacter name remains preferred; the separate GTDB result is reference
nomenclature. Crosswalk SHA256 `761d5537...` establishes bytes, not a release;
NCBI authority is bound by file identity/stat, not a whole-database digest.

The complete retained abstract supports eight corresponding isolates and four
SynCom variants but does not resolve species/strain codes, assemblies, mixing
ratios, complete media or challenge timing. Its greater-than-68-percent
survival statement concerns enriched consortia, not a blanket SynCom estimate.
The current OPEN stock/protocol discussion stays open. CLOSED issues 1105 and
1106 document historical wording/timing repairs, not current scientific
clearance. Their exact snapshots were captured as two additional review inputs
through the unchanged provenance wrapper. Raw route and issue captures remain
private; the retained abstract is existing repository evidence.

The native saved review is
[`20261116T000401Z-shrimp-436-genus-reference-diagnostic`](../../reviews/structured/20261116T000401Z-shrimp-436-genus-reference-diagnostic/review.md),
with three assessments, eight checks, partial scope and
`scientific_review:false`. Its YAML SHA256 is
`814118a2de8d7dc84b6b0fed8a7100f4ce22cc68fc5ec92ad10cb965881b13db`;
Markdown SHA256 is
`9b9c3ea6aeb65a0c4142c18d5eb995db2922a14effc54f792b6d82b6e2a69cb5`.
Both hosts independently verified native validation, exact native Markdown and
all **82 inputs / 18,868,743 bytes**. Their shared audit output is byte-identical
at SHA256 `d24ce29d416ee8ad67d9e33081e195a6c9071349f651b450fd1bf3ea9de3d447`.

Complete private input namespaces preserve **84 files / 18,954,496 bytes**
before any caller edits, including the original batch 101 caller. Local
manifest `3509ee46ca6c8ed0caf88e449d38cc0e9a7ae1837e9415324d4f228e06f53e79`
and M5 manifest `eff10021368cb49918b91bd9a5a6b1d885b6ac1934b2e418275617965f0d435a`
each passed the unchanged independent checkpoint verifier. The namespaces are
`.temp/gtdb-shrimp-thermophilic-sahara-20261115/436-input-checkpoint-001`
on their respective hosts. Root independently audited the local saved pair and
complete namespace before public export.

All **27 public artifacts** match the exporter plan; plan and actual stdout are
byte-identical at `22bfad6bffa02fc1d982de572c05e96a962b9a8dece8e65cf025f5df4fd14710`.
The [strict manifest](436-001-successor.json) binds actual application, full
native source result, saved pair, sidecar and all eight gate triplets. The
initial hash-reader invocation omitted raw/slurp flags and correctly refused;
the corrected unchanged reader verified every output. No exporter changed.

The explicit lane registry admits only this exact proof from real Git baseline
`68699871415fda3c9eebf20382a315f9f3c7b17a`. Batch 101 still asserts the original
unchanged/zero-event ledger literally, retains all current biological tests,
source-cache checks and the 203/279/288 successor chains. Its expected current
digest is obtained only after strict admission. The actual-proof fixture uses
`historical_llm:false` because the original row genuinely added no event; full
old-history preservation remains enforced by the unchanged shared core.

The unmodified historical caller initially reported six passes and one expected
digest refusal, retained as `shrimp436-historical-caller-before-001`, raw
`f8fb33951006d3fb19b3118d94daaea2d32dae24ba1a52e58847b015d781cd91`.
One actual positive proof canary passed before the full affected controls.
The matrix includes the unchanged shared proof mutations/restorations, registry
unknown-change refusal and all seven batch 101 tests. Raw command/exit/log
triplets remain under `.temp/phase2-schema-20261115/`.

| Recorder prefix | Actual result | Raw log SHA256 |
| --- | --- | --- |
| `shrimp436-actual-proof-canary-001` | 1 passed, 12 warnings, 2.96 s | `79bf2387ad6a68a99d3364bbbc9527c08a5964eab0111cce71dec5cc0d81bc74` |
| `shrimp436-actual-proof-and-caller-001` | 24 passed, 12 warnings, 25.17 s | `eba86af5a353e73ef8e9500def3a47591bcf902ca3cb328bb95f53d8eaad8796` |
| `shrimp436-native-lint-001` | Black 774 files, Ruff, mypy 52 source files passed | `7cf92f80298d8a1896bf219efff0360145d0d41de114fc4eb823fab3e128b0ad` |
| `shrimp436-review-integrity-001` | 345 valid reviews, `declared_scopes_only`, exit 0 | `7eb1b3698b15fa7df4431e0fc240e0301321efe082fb316558b9e5609982a067` |

The unchanged native review-bundle integrity command completed at
`2026-11-16T00:21:17Z`. It validates 345 bundles within their declared scopes,
at the recorded local revision and working changes; it does not establish
full scientific coverage or a clean aggregate QC result.

Generated product reconciliation and broader integrated QC remain root-owned.
This canary neither resolves the scientific discussion nor authorizes issue
closure, other-lane transfers or merging.
