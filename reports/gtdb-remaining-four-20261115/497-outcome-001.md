# Acetate-butanol reference correspondence checkpoint

CommunityMech:000497 received one generic PCC 6803 reference block, one grounding
status and two native inline events on frozen M5 revision
`bfef6b2a7684bfc4bb4a22fb1b1234faf797536b` (Python 3.13.2). The exact NCBI 1148
route yields `GTDB:s__Synechocystis_sp000284455`, `total_genomes: 22` and
`majority_fraction: 1.0`, with no explicit support numerator. It does not
identify an experimental engineered-stock assembly or verify its inserted
sequences.

The experimental `WT_PKPa_RBS_BsPta_Δacs` designation and engineering, separate
BL21(DE3) Pem7_ButOH partner and its old E. coli block remain unchanged. The
generic reference population does not make this stock interchangeable with
PPHET's PPT1. P. taiwanensis is a separate experimental consortium, E. coli T7
is a subcloning host, and Pthl is a distinct tested version. None is added as a
member of this canonical pair.

The source review covered the whole canonical record and retained main-text
construction, cultivation and carbon-interpretation passages from PMID 42726284.
It did not newly audit supplementary Tables S1/S2, original figures, plasmid
sequences, experimental genomes or isotope-resolved flux. The two nodes, one
HYPOTHESIZED/PARTIAL arrow and OPEN carbon-specificity discussion are preserved.
Lower extracellular acetate and CFU recovery do not establish exclusive
acetate-to-butanol carbon transfer. Other photosynthetic carbon pools, proposed
ATP/NAD(P)H limitations, evaporation and product reuptake remain distinct
possibilities. OD ratios at different wavelengths are not cell ratios; 30 °C
cultivation, 37 °C colony recovery, adaptation assays, 42-day coculture and
medium/pH refreshes retain their separate contexts.

The exact crosswalk hash identifies bytes with an unestablished release.
The unchanged E. coli block's older provenance wording is not newly certified.
NCBI authority observations use file identity/stat, not a full database digest.

Independent review verified the actual candidate and all 29 stage inputs before
guarded plan/application, then the actual application and gate configuration.
All eight free gate plans preceded eight serial actual commands. Each actual
receipt records exit zero, unchanged inputs, frozen `bfef6b2a` and Python 3.13.2.
Strict validation scanned one file with zero errors; terms reported
`Validation passed`. Native history created one new sidecar while retaining both
old sidecars unchanged. No full binder was rerun after earlier canonical changes.

| Artifact | SHA256 |
| --- | --- |
| Original canonical | `6210d91810b668f546c1e2f17c7f2c01ed37bc250d6314f79696ee7e591b063c` |
| Actual candidate/current canonical | `f87fe83d224c5c2f334d11183618bb0aebe2d473b575e116d05e970fc0c1973f` |
| Actual stage receipt | `433d9c8650d502b3ef228d223b51c726b419251aacb98ad52ab6fe5bca4abda6` |
| Actual application receipt | `093d54e944cb6140103379df0b7a5ea8b54a0add6a7e181864727ef7399a30c1` |
| New sidecar | `95700cb25949504781384969e98eb274eae1b2ac28128bad2fca82add052be02` |
| Source metadata | `2e027d1b1f6de1067df5f695384e8d33356e7f592bbbb12cceede2cc0665d58a` |

The accepted native diagnostic was saved immutably as
[YAML](../../reviews/structured/20261115T230643Z-acetate-butanol-497-generic-phototroph-reference-diagnostic/review.yaml)
and derived
[Markdown](../../reviews/structured/20261115T230643Z-acetate-butanol-497-generic-phototroph-reference-diagnostic/review.md),
SHA256 `6d063d7e9cc2ec1f199459eef704beb93e079af8272127652d2b37eb4dfeac11`
and `18b8b96e233309034c4f071af69325104479df8e74b6b342b5e7d6dea3343c4f`.
Its three assessments and eight actual checks have partial coverage and
`scientific_review: false`.

Both native audits verified all 78 inputs / 59,653,763 bytes, native validation,
exact Markdown and unchanged bytes. Complete snapshots on both hosts verified
80 files / 59,731,446 bytes under
`.temp/gtdb-remaining-four-20261115/497-input-checkpoint-001`. The independently
created manifests are local
`cc24dc7ae1c642bdd18ea235f7d1461f2672d3f74d4bfb3ce8ec6048c33e1770` and M5
`16d244e92c67f2970012215d27e07865157f92beaa79b41933bd25c2df37b83f`.
Root independently reran the local pair/checkpoint audits and read the matching
M5 outcomes before export or caller changes. The large complete route and
original caller remain private checkpoint inputs.

The unchanged captured-byte exporter passed planning and actual publication;
all 27 emitted artifact hashes match, and plan/actual stdout is byte-identical.
The [successor manifest](497-001-successor.json), SHA256
`47822a8cb7f752d8f71fe1423897d9a72c1a35974f9f61c63d8ee5ee8b1bc768`, binds
the actual application, source, pair, sidecar, inline events and eight raw/public
gate triplets. Labeled path-redacted derivatives retain separate raw hashes.
No private primary body or complete route body was exported.

After the complete snapshots, the existing actual-proof registry gained only
the explicit 497 allowance and case. Real Git revision `68699871415fda3c9eebf20382a315f9f3c7b17a`
contains the exact `6210` predecessor. Batch 137 dispatches this path before
its existing 498/499/500 routes; the original ledger, all current biological
and cache predicates, current parsed-history equality, and fabricated-snippet
mutation controls remain unchanged. No shared core or validator was modified.

The original caller correctly refused the changed record twice, with one test
passing. After independent code review, one actual positive proof canary passed,
then 67 composed tests passed: all three actual-proof cases plus batches 137,
81 and 135. Native lint passed Black (776 files), Ruff and mypy (52 sources).
Its initial invocation refused the inherited `JUST_NO_DOTENV=1` before lint;
the retained second invocation explicitly used the same boolean environment
and `--no-dotenv` command as the prior checkpoint. Checks recorded local start
revision `a149dda6` plus working changes, not a clean aggregate QC run.

Recorder triplets remain under `.temp/phase2-schema-20261115/`:

| Recorder prefix | Actual result | Log SHA256 |
| --- | --- | --- |
| `remaining-four-497-caller-before-001` | 2 expected unknown-change refusals, 1 passed, 12 warnings, 2.24 s | `46be9dec8f64d4ba89d83035c465574149cfa406930ba1dae658435c7d2fc991` |
| `remaining-four-497-proof-canary-001` | 1 passed, 12 warnings, 4.04 s | `6dd1316b0411b0f349487809b775a3e6bdc09c5406714aad9b38f0640715034e` |
| `remaining-four-497-proof-matrix-001` | 67 passed, 12 warnings, 63.83 s | `d26e0ab67794649f761ec96238c868fc916ff00876e0ea12718d6d4a4499a5d2` |
| `remaining-four-497-lint-001` | CLI environment-value refusal before lint, exit 2 | `3e6bdd695c4f518ccb8857917f42178c0601fc4cfad25b5023237d9101c6ff3e` |
| `remaining-four-497-lint-002` | Native lint exit 0 | `a091bb2c35178d612a93c603a6ef5be6450af2abf6c3565f57dec2cfea666aff` |
| `remaining-four-497-review-integrity-001` | Native review integrity exit 0; 348 valid reviews, declared scopes only | `57556c4c85729b12563565500edab845c305bbc38b72502e96ca3e1351c61e6f` |

The native all-review integrity check completed at 23:20:12 UTC with 348 valid
reviews and `coverage: declared_scopes_only`. Its recorded start revision is
`a149dda6` with the reported working changes; it is not a clean aggregate QC
or expanded scientific-coverage assessment.
The separately reviewed 454 application is outside this saved diagnostic and
requires its own gates, review, checkpoints and strict proof. Final integration,
current products, measured references, aggregate QC and scientific-finding
disposition remain separate. No full scientific completion or merge is claimed.
