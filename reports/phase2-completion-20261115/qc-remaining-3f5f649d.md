# Remaining full-QC work at 3f5f649d

This bounded read-only audit concerns integration revision
`3f5f649d81ac685acbcef0e98de8b9976a8fa3a5` on
`fix/phase2-completion-20261115`. HEAD and the clean tracked working tree were
verified before the audit and again before writing this report. The audit read
retained evidence, current code and records, and issues
[2848](https://github.com/CultureBotAI/CommunityMech/issues/2848) and
[2849](https://github.com/CultureBotAI/CommunityMech/issues/2849). It did not run
pytest, a classifier sweep, validation recipes or full QC, or alter their inputs.
This report is the only new file authorized from that audit. No new network
queries were made while persisting it.

The original code006 aggregate remains failed. On M5, Python 3.13.2 at
`c9e151eb9f22afb5c531dd5a8b3346ce1d58b12a`, native `just qc-references` ran
with dependencies enabled from 04:15:59 to 04:34:03 UTC on 2026-11-15. Lint
passed, then pytest reported **2 failed, 5,861 passed, 30 skipped, 8 deselected
and 18 warnings in 1,080.02 seconds**. The failures were:

- `tests/test_gtdb_coherence_validator.py::test_the_stored_statuses_reproduce_from_the_classifier`
- `tests/test_gtdb_uncurated_blocks_match_the_tool.py::test_a_block_the_tool_would_not_produce_is_curated`

Every subsequent aggregate stage was **NOT RUN**: `validate-all`,
`validate-taxa`, `validate-strict`, `validate-gtdb-all`, `validate-scalars`,
`validate-scalars-idiomatic`, `validate-terms-all`, `validate-terms-taxa`,
`qc`, `validate-references-all` and `qc-references`. The original raw log
SHA256 is `9ea6742aa081136d3133d153d49103cb5ae696d35670edc3ed59e816afdae450`
(770,023 bytes); the sanitized public log has a different hash and size,
recorded below and in its receipt. The later standalone native validations
passed on that old revision, but do not revise the failed aggregate or establish
full QC on the current integration.

The three original issue2849 mapping causes have source-backed corrections in
the audited tree. BR1 has the independently supported, explicitly curated
`Microbacterium_sp002812725` correspondence. Terrabacter preserves the study
stock identity and uses the independently supported genus correspondence for
NCBITaxon:53355. The industrial consortium uses the supported species-name
fallback to `Sulfobacillus_A_acidophilus`. Their strict successor helpers and
historical protections are present. The unchanged whole-corpus
`test_gtdb_uncurated_blocks_match_the_tool.py` passed **3 tests, no skips, in
8.37 seconds** on M5 at `f39c0fe400740a754f2d006d17ffa8c8e82fae63` with the
retained crosswalk. This is evidence for that module and revision, not a current
aggregate pass or scientific approval of every record. It must run again after
the final changes are combined.

Issue2848 is not cleared by the current integration. The retained byte inventory
at `38c48a84187f86395d6e6b6fa8d8829d8e6c1ef4` reports **113 changed and 13
unchanged files** among the 126 historical assignments. The only change from
that revision to the audited HEAD is the Sorghum/Shrimp integration report.
The unchanged record IDs are **091, 363, 376, 381, 389, 395, 398, 416, 419,
441, 482, 494 and 501**. These are byte states, not a fresh count of classifier
discrepancies or completed reviews; pending worktrees are excluded. Existing
transfer refusals and approval boundaries are not changed by this report.

Record416 provides a concrete residual independent of that counting distinction.
Its current canonical taxonomy has six `UNRESOLVED` statuses and no corresponding
grounding blocks. Its accepted, retained native source configuration reports
six available phylum/class/genus routes and `classify_status: NOT_ATTEMPTED`
before those blocks exist. That evidence supports completing the reviewed
grounding, native history, saved diagnostic and strict caller path; it does not
authorize a blanket status rewrite. The near-tie Bacillota_A correspondence and
non-type warning remain scientific limitations. This audit did not recompute
those results or establish the complete current discrepancy population.

The native classifier `scripts/gtdb_ground.py` and the uncurated-block module
are unchanged from code006. The status-reproduction test's only intervening
change aligns its row-query collector with the maintained CLI, including
`lookup_keys` and the species heuristic for Candidatus names (#2854). Its
status/candidate equality assertions remain. Missing crosswalk data can skip
the mapping fixtures; the status-reproduction test also requires the real NCBI
adapter fixture. A skip is not evidence that either invariant passed.

The remaining execution order is:

1. Finish the reviewed record corrections and integrate their complete evidence
   and strict historical caller changes, retaining current biological predicates.
   The separate Switchgrass locator adoption also needs its new full current
   scientific assessment and scientific successor before final integration:
   `tests/phase2_review_successor.py` requires a completed scientific review
   bound to current bytes. A partial taxonomy diagnostic cannot replace it.
2. Freeze a clean named M5 branch at the exact final combined commit. Verify the
   frozen lock/environment, the retained crosswalk SHA256
   `761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd`,
   its native `data/raw/NCBI2GTDB.tsv.gz` layout and `KG_MICROBE_DIR`, the actual
   local NCBI adapter and required ontology sources, and every historical Git
   object required by the then-current workflow and successor fixtures. The
   old crosswalk prerequisite document records the actual code006 locations;
   future locations must be recorded rather than silently assumed.
3. Use the same native recorder/environment for free plans and the real-source
   canary
   `tests/test_gtdb_support_counts.py::test_the_species_path_reports_the_denominator_but_no_numerator`.
   Verify its actual persisted result and absence of a prerequisite skip. Run
   the QC driver's exact-revision `validate-strict` record canary and verify its
   retained artifacts before the aggregate. Rerun the two originally failing
   invariants, preferably their complete modules, with explicit skip reporting.
   Diagnose any residual from those new results; do not reuse historical counts
   as current measurements or weaken tests to admit unreviewed changes.
4. Run native **`just qc` with dependencies enabled** on that same final revision.
   Its current order is `lint` → `test` → `validate-all` → `validate-taxa` →
   `validate-strict` → `validate-gtdb-all` → `validate-scalars` →
   `validate-scalars-idiomatic` → `validate-terms-all` → `validate-terms-taxa`.
   Native `test` runs `uv run pytest tests/ -v`, using the repository's
   `not e2e` selection. Retain exclusive raw log/exit/receipt artifacts, exact
   source/runtime identities, skips, stage accounting and before/after state.
   On failure, later stages remain not run; standalone checks cannot be relabeled
   as execution of the failed aggregate.
5. Complete current generated-product checks and measured reference coverage
   separately. `just qc` does not include references; `qc-references` adds the
   reference sweep. Neither technical QC nor source matching grants scientific
   approval. Do not infer whole-corpus reference coverage from a one-record
   Switchgrass canary.

The maintained `run_phase2_qc_20261115.py` already enforces the expected revision,
clean tracked inputs, persisted strict canary and historical-object prerequisites.
Its underlying legacy recorder does not include `KG_MICROBE_DIR` or NCBI source
identity in `environment_overrides`; retain a separate prerequisite/environment
receipt, as code006 did. Do not rewrite the old receipt to add later information.
No final-revision whole-corpus GTDB result, full-QC pass, product freshness or
scientific completion is established by this audit.

The following SHA256 pins bind the retained evidence and current contracts read
for this report. Paths are relative to the audited checkout; `.temp` evidence is
retained privately rather than reproduced as new execution evidence.

```text
524997c84c7ea6185613ec5c6fd17ca2a6a477793974301cd6515e03812a5137  reports/phase2-completion-20261115/code006-outcome.md
2c8c5645f8115d2982d3c8e39545a4ec723cfb5bd616ee9436ac5c5fe0adcb2a  reports/phase2-completion-20261115/code006-crosswalk-prerequisite.md
aff0243950fba74ebea87fcf97f9ca94db0a8647c8eed4b12c26aea98e497ae1  reports/phase2-completion-20261115/code006-standalone-outcome.md
1e67b328abd24a82bcb3e91a5475d4dbce8d4b7eae7c5d689b38ab9310fc4713  reports/phase2-completion-20261115/technical-evidence/phase2-code006-qc-references.receipt.json
ef9424eff65437263a9c96a5ad9a27d1d010938cb5b46789bc0322e3535d73c7  reports/phase2-completion-20261115/technical-evidence/phase2-code006-qc-references.log.txt
4355a46b19d348dc2f57c046f8ef63d4538ebb936000f3c9ee954a27460dd865  reports/phase2-completion-20261115/technical-evidence/phase2-code006-qc-references.exit.txt
6965c9f0f73ebae32675828ed8f69ff4ab079f1695e6ecf92b48372a488ae66f  reports/gtdb-source-routes-2849-20261115/CORPUS-CHECK.md
76add2b275eb405cae0f71de6e3dc620bd6bc4703baafbe86209ed445a6c213e  reports/gtdb-source-routes-2849-20261115/corpus-run-001.receipt.json
638e1f568144ef8b9f9c190d21c8d003d0cade333cf76733ef5e975d30844a62  reports/gtdb-source-routes-2849-20261115/corpus-run-001.log.txt
9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa  reports/gtdb-source-routes-2849-20261115/corpus-run-001.exit.txt
34d92d4ceaf582e17cfa20580b16bac059c98c2c5662a866d47bd5a03faa466e  reports/phase2-completion-20261115/sorghum-shrimp-integration-38c48a84.md
1ccc66940fd45773a4184c52bc7b2376335ddfe273f6b90f525ca5f551f9621d  .temp/phase2-schema-20261115/assignment-progress-38c48a84-001.json
a76fa7cbc630b17c3c24e26994f5a08b665ab26d50187bee4bc08ea9f6f5e3b2  reports/gtdb-shrimp-thermophilic-sahara-20261115/thermophilic416-source-config-001.json
51357584e2099b2916e81f893f46fc0af8cede23e3b2616ca957adc5f7a4bf71  kb/communities/Thermophilic_ExSitu_Biomethanation_Mixed_Culture.yaml
acdadd88a7f7e81eced8c1d229709ba94023dde7e7f72f3238f483685b4c2236  data/isolates/Microbacterium_BR1_Sulfadiazine_Cleaving_Isolate_Baseline.yaml
068a38e5be07ab6756b1fe32683c166d8562e8405fae7bc4429575a33e2578ec  data/isolates/Terrabacter_2APm3_Sulfadiazine_Isolate_Baseline.yaml
24c55ff3c29b21fa5988c4859fdcccfacc52caf62a1902cb28887b68780f551e  kb/communities/Industrial_Bioreactor_Consortium.yaml
579a14cb2a2115897f492300157a7a931663ae0d7e56982450ae41ce4cd2d334  tests/batch144_mapping_successor.py
d14fe7fb3a26121d7b4e23c57a434bbf97b6e953c231bd3c8544c23a066bfc89  tests/sulfobacillus_mapping_successor.py
c6d22029a0431e5ad8578ab6b54aab096427c232c5a366d5071c6052a60f9b2f  tests/test_causal_review_batch144.py
477c1c4feb143be97affbc8fb4a65bc77429032e791bf822dbee64218ba26505  tests/test_gtdb_coherence_validator.py
102ee759b9cd43c34d65d1b169affe6f0823400d40fa4571cdf59fa462306df0  tests/test_gtdb_uncurated_blocks_match_the_tool.py
0fc1ba926a56e5be85cdf064db0cf56452aeeee93f15b0ced98e8f11b5296175  scripts/gtdb_ground.py
a0963a0082ed35efd2116439a995b154ce913d6bc2a3d3d3a898904f0bcf8511  scripts/adhoc/run_phase2_qc_20261115.py
2a73a3ab3d4ec955c797ff179ebc3e3be1423a5c37803a242241c1ccdfc86a04  scripts/adhoc/m5_completion_checks.py
40369611ad4531582e420df0e9ff22109e4b18adf03b34d86b54200b280f2d0f  justfile
ba3172b2c0604ea108ddebae37559062e83ab130d17f5746a02b5e66a5217bc8  .github/workflows/validate-strict.yaml
be952f0f137f85fed66bda0908f12014f1797a2dd229b44d832afc0c00471655  pyproject.toml
bb60838c24727c279c0c6219550a81b3373ff7b0b6ce90b912f89796a73e1c32  tests/conftest.py
b728c3ddef4f29667fa612b81d188751bfae6a303d712689b55443a25944d1d7  tests/phase2_review_successor.py
```
