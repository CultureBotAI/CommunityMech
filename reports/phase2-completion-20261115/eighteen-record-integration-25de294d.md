# Eighteen completed technical corrections integrated

At `25de294d4a2a6c4654cbf8b824e44e8222568925`, the draft integration branch
contains 51 completed taxonomy corrections, including 47 of the historical
126-record repair partition; 79 partition records remain. This adds eighteen
completed records to the preceding 33-record checkpoint. The separately
preserved Caragana 338 source-note intermediate is not a completed mapping
correction and is excluded from these counts.

| Integrated scope | Actual completion evidence |
|---|---|
| Species 481, 432, 411, 472, 341, 361, 378, 408 | [Eight-record outcome](../gtdb-species-status-20261115/second-eight-outcome-003.md): 64 native M5 commands, saved 404-input assessment and complete 406-file checkpoints verified on both machines |
| Genera 415, 477, 353, 440, 447, 433, 474, 403 | [Eight-record outcome](../gtdb-code006-20261115/genus-eight-outcome-001.md): 64 native M5 commands, saved 409-input assessment and complete 411-file checkpoints verified on both machines |
| Wheat 409 | [Final outcome](../gtdb-source-holds-20261115/wheat409-final-outcome-001.md): source-note and mapping transitions, eight final-byte M5 commands, saved 93-input assessment and complete 95-file checkpoint verified on both machines |
| Hexamine C1 505 | [Canary outcome](../gtdb-ambiguity-eight-20261115/505-canary-outcome-002.md): eight M5 commands, saved 82-input assessment and complete 84-file checkpoint verified on both machines |

Each outcome retains the actual execution revision, private command evidence,
public proof pins and source limitations. The eighteen mapping applications
passed 144 scoped native commands in total. These are distinct per-record
commands, not a corpus-wide QC run. Every saved mapping diagnostic remains
partial, with `scientific_review:false`; source-stock uncertainty, reference
populations and complete ordered ambiguity alternatives remain separate.

The exact integration revision passed **138 tests, with 12 existing warnings,
in 104.78 seconds**. The selection covers production admissions and the affected
historical modules, including shared batches 8, 92, 104, 122, 133 and 139.
Current biological predicates, prior events and immutable ledgers remain active.
Native lint passed Black's 747-file check, Ruff and mypy's 52 source files.
The earlier per-branch mutation controls remain linked through the outcomes;
their counts are not summed with this overlapping integration selection.

| Retained run under `.temp/phase2-schema-20261115/` | Result | Log SHA-256 |
|---|---|---|
| `integration-sixteen-wheat-hexamine-composition-001` | Exit 4: incorrect test filename; no tests ran | `d662bfa511fa50b39e979c563b9b598c8223c4dd75d940f082747f73accd8593` |
| `integration-sixteen-wheat-hexamine-composition-002` | Interrupted deliberately after 93 passes; exit 2, incomplete | `ca0d6eddf4560a094cc6a00664efdf4cbb9571aa898af864f0fa25cbf9e8a78c` |
| `integration-sixteen-wheat-hexamine-composition-003` | 138 passed at `25de294d`, exit 0 | `9d5c6af8b74825c3e8ce1f7b33a401c79a1f88ad5f3cfbe93cee5fc5f58002a7` |
| `integration-sixteen-wheat-hexamine-lint-001` | Native lint passed at `25de294d`, exit 0 | `3d1500a072150a6abda18b2a51e26e77a3abb8a1decfdabbb1cf8e67e88e673e` |

Run 002 repeated already-passing isolated mutation suites and was stopped in
favor of the integration-specific selection. It began at `2beb9d47`; the unrelated
338 note-only commit was added while that incomplete run was active. It is not
used as exact-revision completion evidence. Runs 003 and lint ran on the clean,
unchanged `25de294d` tree.

Review identified incorrect taxon names in the first species outcome draft
([#2883](https://github.com/CultureBotAI/CommunityMech/issues/2883)). The original
draft is preserved privately; additive outcome 003 is corrected and independently
verified. The C1 outcome separately retains its corrected unsaved-draft selector
finding [#2882](https://github.com/CultureBotAI/CommunityMech/issues/2882).

The [338 note checkpoint](../gtdb-source-holds-20261115/caragana338-note-intermediate-001.md)
is now preserved by the real maintained intermediate `25de294d`. Its actual M5
note execution remains `fa983c4b`; the independent inspector verified all 57
captured inputs and eight native commands. Final mapping, immutable diagnostic
and strict composite admission are pending. Other concurrent M5 applications
and source preparations are excluded from the completed counts above.

Current generated products, full combined M5 QC, reference-source blockers and
scientific review remain required. These results neither merge the CommunityMech
PR nor complete Phase 2 or the subsequent all-record campaign.
