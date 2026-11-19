# Source adjudication holds for 000393 and 000409

These two whole records remain unresolved work under [#2848](https://github.com/CultureBotAI/CommunityMech/issues/2848). They are excluded from automatic mapping/status application. Holding them preserves evidence; it does not satisfy the corpus status gate or constitute scientific clearance. No canonical data, candidate list or validator is changed by this report.

The current records and retained source passages were inspected at local revision `aa727456df29a9af47e05ffff1f74b63c16f80fd`. The native results below are from the retained historical assignment/intake, **not a fresh native recomputation**. The private intake `intake-assigned-001.json`, produced at `301f35b8d9db679f3067297317356081fa305959`, has SHA-256 `f759d9159daab93df17c273bf01fb6a9a0292d484fc58d05995410264a267f98`; it is bound to the original residual partition. Fresh routes, explicit source judgments and independent review remain required before any candidate.

| Record | Current canonical SHA-256 | Retained primary-cache SHA-256 |
|---|---|---|
| [000393 Calcium-Tomato](../../kb/communities/Calcium_Tomato_Bacterial_Wilt_SynCom.yaml) | `2003158329c3f2113f6239f65b1e6a1b85bd3c19204f7aaf9d90be7f1f5c68f0` | PMID 41387930: `28088317360ce0a54f4245a898a662748ffce070f080cf47f96994f5eaa5588f` |
| [000409 Wheat SASW01](../../kb/communities/Wheat_SynCom_SASW01_Drought_Inoculant.yaml) | `613f8b97efa732c213fae320935a4f8cafa8cb899718e6c18a7c1f47f9ba0420` | PMID 42513902: `f36426f264438e022eeed4077aba924504d3192b25fac5b7d7a34ca5d8fd655e` |

## 000393: distinct source populations have not been reconciled

`taxonomy[2].taxon_term` (NCBITaxon:1406, Paenibacillus polymyxa) stores five alternatives: the unsuffixed species and `_B`, `_C`, `_D`, `_E`. Its note attributes that set to direct inspection of a GTDB bac120 taxonomy table. The adjacent Rhodanobacter block explicitly names an R226 bac120 source; this does **not** independently establish the exact release or checksum of the Paenibacillus source table. The original table bytes and the five-option derivation have not been reverified in this bounded intake.

The historical native result against crosswalk SHA-256 `761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd` returns only the unsuffixed species, `_B`, and `_C`, by `ncbi_name`. Replacing the five-option assertion with that three-option result would discard an explicitly different source claim without adjudicating it. Neither candidate set identifies the study stock's species cluster. The primary cache's Data availability section reports raw Paenibacillus genome reads as `SRR33221449`; raw reads alone are not an assembly-grounded GTDB assignment.

Next action: recover and hash the original bac120 evidence if retained, or acquire a precisely identified authoritative release through a single-file canary; reproduce its exact matching rows and population alongside a fresh pinned-crosswalk route. Decide whether the old candidate assertion is a supported distinct-source claim or needs a source-backed correction. Any source-aware native policy must bind the exact record, semantic block and independently verified source population, with mutation controls; it cannot be a generic curated/source-label exemption. Preserve the other three stocks and the scientific predicates in `tests/test_causal_review_batch8.py`.

## 000409: a new mapping would contradict an explicit scope note

`taxonomy[0]` names Enterobacter hormaechei FN0603 and `taxonomy[2]` names Enterobacter ludwigii FWP1205. Both current notes state that no species-level GTDB classification is asserted. The retained primary Methods 2.1 identifies these stocks through 16S rRNA V5–V7 sequencing. It names a five-stock consortium; this report does not infer whole-genome verification from that identification method.

The historical native results propose three alternatives for NCBITaxon:158836 (Enterobacter hoffmannii, E. hormaechei, E. hormaechei_B) and a unique NCBITaxon:299767 reference correspondence to E. ludwigii, fraction 0.95 across 296 reference genomes. Those numbers describe a database population, not FWP1205's strain placement. Installing the latter block while retaining the unqualified no-classification note would create a contradictory record.

Next action: obtain a fresh native route, then independently review a bounded wording change that distinguishes reference-species correspondence from unverified study-stock placement, if the evidence supports it. This requires an explicit additional semantic allowance and meaningful mutation controls; the current mapping-only engine must not silently edit the note or treat it as harmless. Preserve all five stock identities, three already ambiguous entries, experimental conditions, evidence and graph claims, and the immutable batch122 ledger plus its current scientific tests. If the wording cannot be honestly reconciled, retain this record as a concrete blocker instead of waiving it.

The next acceptance point for either record is a separately reviewed source/candidate canary, actual guarded M5 application, native history and checks, a saved partial diagnostic, strict historical successor admission and the unchanged combined corpus status test. No completion count is advanced here.
