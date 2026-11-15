# One-record ambiguity canary

CommunityMech:000546 now records `AMBIGUOUS` and all three native GTDB
alternatives for its existing NCBITaxon:853 descriptor. No alternative was
chosen as the identity of strain A2-165/JCM31915. The guarded application,
append-only history, eight native commands, immutable diagnostic and strict
historical-review successor have completed. This is the first canary in the
assigned 30-record lane; it does not establish completion of the other records.

The source remains
[Faecalibacterium A2-165 monoculture](../../data/isolates/Faecalibacterium_Prausnitzii_A2_165_2FL_FOS_Monoculture_Baseline.yaml).
The primary [Iguchi article](https://doi.org/10.3390/microorganisms14081812),
Methods 2.1, names “Faecalibacterium prausnitzii A2-165 (JCM31915)”. Its bibliography
also cites a 2024 paper naming A2-165 *Faecalibacterium duncaniae*. Resolving that
stock-level nomenclature or assigning a genome was outside this correction.
The retained anonymous Europe PMC XML has SHA256
`c5b4d94fcd98543be47d7eb623a69180ae15cc98dbe1a3b1ad772818f65d421e`.
Article text remains private. The pinned crosswalk is SHA256
`761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd`;
its file timestamp is not release/build evidence.

The actual M5 execution used published revision
`4a5999d5f9299a26e1aff0ffc1262bfff03a035f` and Python 3.13.2, with the
subsequently added gate wrapper and diagnostic builder individually hash-bound
in the review. The local development checks used Python 3.13.12. The same
published launcher performed plan, staging, validation and one guarded apply.
The canonical SHA256 changed from
`b6dc768bf6f705611933fc50882d91957225ef1e32c61330e1adb717fe175790` to
`d1843b01c495ca1a2c44820435e3a60b76e65089eff627590c26b5d0e003bcb6`.
Only the declared status/candidates and one complete native inline event changed.

The [actual apply receipt](ambiguity-apply-001.raw.json) and
[native recomputation](ambiguity-native-route-001.json) are byte-identical
metadata copies of the review-bound raw artifacts. The
[successor manifest](ambiguity-successors-001.json) binds those artifacts,
the exact current record, the immutable historical Git bytes and ledger, the
new sidecar, and the saved review pair. The original batch146 biological and
quotation assertions remain in force.

| Native command scope | Outcome | Retained public receipt |
| --- | --- | --- |
| Record schema | Passed, exit 0 | [schema](ambiguity-schema-001.receipt.json) |
| Record strict validation | Passed, exit 0 | [strict](ambiguity-strict-001.receipt.json) |
| Record GTDB | Passed, exit 0 | [GTDB](ambiguity-gtdb-001.receipt.json) |
| Record GTDB domain | Passed, exit 0 | [domain](ambiguity-domain-001.receipt.json) |
| Record scalar validation | Passed, exit 0 | [scalars](ambiguity-scalars-001.receipt.json) |
| Record ontology terms | Passed, exit 0 | [terms](ambiguity-terms-001.receipt.json) |
| Complete target history directory | Passed, exit 0 | [history](ambiguity-history-001.receipt.json) |
| Create exactly one native sidecar | Completed, exit 0 | [new history](ambiguity-new-history-001.receipt.json) |

These are seven scoped validation commands and one sidecar-creation command.
Each receipt has an adjacent sanitized `.log.txt` and exact `.exit.txt`, with
separate raw/derived hashes. Original logs remain in both the isolated M5
checkout and the verified local mirror. Existing sidecars were preserved.
References, full-corpus QC and regenerated pages were not run by this canary;
root integration owns those wider checks.

The immutable diagnostic is saved as
[native YAML](../../reviews/structured/20261115T061642Z-faecalibacterium-ambiguity-diagnostic/review.yaml)
and [derived Markdown](../../reviews/structured/20261115T061642Z-faecalibacterium-ambiguity-diagnostic/review.md).
It explicitly uses `scientific_review: false`, partial coverage and
`pass_with_limitations`. Both the [M5 audit](saved-review-audit-m5-002.json) and
[local audit](saved-review-audit-local-003.json) verified all 67 inputs
(5,226,886 bytes), native validation and exact Markdown. YAML SHA256 is
`7bddbfd88734b5657855f743ed55c0f01e31b42aa49603772d714fecfb68b383`;
Markdown SHA256 is
`a0543246a0d2432cfa10648c5b3a018d6fb73322efb286abd8b5000d9d5eb1ad`.

The later batch146 caller integration is deliberately a post-save code change:
the review inspected the original caller. Its exact bytes remain under the
private `batch146-inspected-original.py` archive and in the execution commit.
The local audit and public export completed before restoring the reviewed new
caller. No immutable review was rewritten to claim it inspected the successor
code, and the historical ledger remains unchanged.

The focused final suite passed **45 tests**, with 12 existing Pydantic warnings,
in 18.82 seconds. It covers the actual successor, rehashed proof/biology/stock/
candidate/event mutations, restoration, original batch146 assertions, staged
application guards, captured inspections, shared evidence capture and writer
inventory. The raw local log is retained privately with SHA256
`81f3a76095b316d159115ec4a61d155dc31b139f0b1685200795c8162c9d33b3`.
The native writer audit also completed with exit 0.

Earlier staging attempts, failed controls and the unsaved draft001 remain
preserved. [#2861](https://github.com/CultureBotAI/CommunityMech/issues/2861)
records the corrected historical-fixture dependency;
[#2865](https://github.com/CultureBotAI/CommunityMech/issues/2865) records the
captured-target gate binding; and
[#2864](https://github.com/CultureBotAI/CommunityMech/issues/2864) records the
inspection-versus-assessment binding. For #2864, all four transient/missing/
extra/duplicate-input controls failed before the repair and passed afterward.
Draft002 retains the same scientific judgments as draft001; its changes are the
binding repair, provenance paths/hashes, timestamps and issue link. No campaign
completion, scientific clearance or issue closure is inferred from these checks.
