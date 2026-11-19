# Supplement adoption: curation guards, current pages and assertion coverage

This checkpoint extends draft PR #2935. Canonical Switchgrass curation and its
normal reference configuration remain pending. These results do not complete
Phase 2, full QC or scientific review.

## Bounded curation helper

`curate_switchgrass_source_locators_20261115.py` admits only the original
Switchgrass record `bb31b1df4a9be2241453528101fc5d55657c23eccf1d58ce1cc9639e5912b368`,
three explicit source locators and one truthful native curation event. It requires
five distinct, externally pinned actual consumer controls, rechecks their full
inputs and source identities, replays the DOCX extraction, validates the private
candidate with the native writer and guards the final replacement with a backup.
The native sidecar is a separate required step. The helper has SHA256
`cfd6e405c4e2aad5fc48d780b094ca803ac31293b2703abdb070d2e24ae8d56b`.

Independent review found that its test fixture incorrectly depended on the
current canonical record. [Issue 2936](https://github.com/CultureBotAI/CommunityMech/issues/2936)
records the repair: tests load and hash-check the immutable predecessor from
Git, then prove that it remains usable after changing a private current record.
The corrected test has SHA256
`076206a08cd35f9b0a5d82c0bb80ef844238f6e86774dcc1b53d70b76fd8b8d9`.
The actual fixture canary and mutation/writer controls use explicitly synthetic
receipt fixtures; they are not substitutes for M5 consumer runs. The final
focused run passed 32 tests, with 12 warnings, in 114.18 seconds; raw log SHA256
`4a433a974fce65c1d8a16d80c3474580e9b182b6d7ddce674e29d4c0a34d9af5`.
The initial 31-test run and earlier attempts remain retained.

## Generated output

The hosted docs check at `b5cb827f` rendered 512 pages but detected five stale
outputs. The failure is recorded under
[issue 1996](https://github.com/CultureBotAI/CommunityMech/issues/1996#issuecomment-6903642970),
with raw log SHA256 `937badc161d03f2221a4d5a3e2c742efe816d312b3998f0b47c620a8684e3674`.
A native single-page canary persisted the corrected Wetland page before the
full native renderer ran. Independent review accepted all five resulting files:
the Wetland page and its browser/bulk descriptions match the existing canonical
record, and the schema page documents the new EvidenceItem locator slot.
No record or renderer was changed by this regeneration.

The five files and accepted curation guards were committed at
`964db448d32c3c8c3f22fa4d2557c1f5e6a530f1`.
The unmodified native `check-docs-current` subsequently passed at
`58158f33a6bc928c57f913d8a504a0899814dba5`, with the tracer repair recorded as
working changes. Raw log SHA256:
`fdd91098d245e6dec2ffb3baa152a0135a784c9fc77d77dd688eba86c7829502`.

## Maintained assertion counter

The adopted runtime exposed 14 failures in the old tracer/probe tests:
the observer rejected the new locator keyword and required version 0.2.1.
[Issue 2937](https://github.com/CultureBotAI/CommunityMech/issues/2937) retains
that finding and failed run; the separate schema-isolation report preserves
its exact boundary.

The maintained counter now requires the exact reviewed development version,
forwards explicit and absent source locators through the native plugin and
validator, records source-selection failures separately, and reconciles actual
locator identities against the independent record census. A different cell with
identical text cannot establish coverage. Selected-source failures do not count
as comparisons, and source catalog, asset and projection files are included in
the input manifest even beneath ignored directories. Article cache semantics,
native matching, acquisition refusal and the zero-comparison failure remain.

One real native CLI test using a synthetic DOCX exercised correct selection,
wrong cell, wrong parent, explicit null and restoration before the broader run.
It passed with raw log SHA256
`04a04b908a289fec97eee01f72fe37363cb16d255956fd2ac700056cb19e0558`.
All 46 coverage, CLI and reference-export tests then passed, with 14 warnings,
in 90.88 seconds; raw log SHA256
`d1f77802e5f6055c1f4b97fa6654ae8e031198cab8a66844827c46f7db1eb27c`.

The native `just reference-assertion-coverage` Asgard canary used the actual
Git-bound record and retained caches. All three cases compared 11/11 snippets:
the control and restoration matched all 11; the deliberate bracket mutation
matched 10 and failed exactly one, with native exits 0/1/0. Inputs stayed
unchanged. Receipt SHA256
`9a49974965f37f99c43726b2806e414605a8c1a701e259384bad8b0605001311`;
recorder log SHA256
`fb47f6600dbd188144118acaf16485d4ac14694a0e9e84dabaf61d89d1358c4d`.
Native lint passed Black over 801 files, Ruff and mypy over 52 source files;
raw log SHA256 `13f5f729c52f76a5ed241a28093067199a8a73e08dc0a16275b782b874342b57`.

All command triplets remain under `.temp/phase2-schema-20261115/`. The tracer
tests ran at `964db448` plus recorded working changes; the actual Asgard canary
and lint ran at `58158f33` plus the same tracer changes. These are bounded
checks, not a clean-revision aggregate QC pass. M5's separate frozen scratch
consumer canary and subsequent canonical/configuration adoption require their
own receipts and review.
