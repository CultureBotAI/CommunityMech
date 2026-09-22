# YAML Record Review: CICC Three-Strain Probiotic M-MV Luteolin Consortium

- Repository: CultureBotAI/CommunityMech
- Record: `kb/communities/Multispecies_Probiotic_MV_Luteolin_Consortium.yaml`
- Started UTC: 2026-09-22T19:54:21Z
- Finished UTC: 2026-09-22T19:54:21Z
- Verdict: needs curation

## Target

`CommunityMech:000425` is a maintained `MicrobialCommunity` record for the defined anaerobic co-culture of `Bifidobacterium longum` CICC25033, `Clostridium butyricum` CICC23847, and `Limosilactobacillus reuteri` CICC6131 from Hou et al. 2026 (`PMID:42604006`, DOI `10.1016/j.isci.2026.117105`). The source grew the three probiotic strains singly, pairwise, and as a 1:1:1 three-strain MRS co-culture, isolated mixed-species membrane vesicles from the three-strain co-culture supernatant, profiled vesicle proteins by LC-MS/MS, and tested luteolin-loaded M-MVs in vitro and in a DSS mouse-colitis model.

An ignored/hidden-inclusive duplicate search covered `kb`, `data`, `history`, `reports`, `references_cache`, and `research/scouting` for `CommunityMech:000425`, `Multispecies_Probiotic_MV_Luteolin_Consortium`, `10.1016/j.isci.2026.117105`, `42604006`, and `PMC13476518`. It found prior scouting queue/stub entries, the new record, the new history record, and the new PMID cache files, but no pre-existing curated record.

## Validation

| Check | Result |
|---|---|
| `.venv/bin/linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Multispecies_Probiotic_MV_Luteolin_Consortium.yaml` | Passed, `No issues found`. |
| `PYTHONPATH=src .venv/bin/python scripts/validate_strict.py kb/communities/Multispecies_Probiotic_MV_Luteolin_Consortium.yaml` | Passed, 1 file scanned, 0 files with `ERROR`. |
| `.venv/bin/linkml-term-validator validate-data kb/communities/Multispecies_Probiotic_MV_Luteolin_Consortium.yaml -s src/communitymech/schema/communitymech.yaml --labels` | Passed. |
| `PYTHONPATH=src .venv/bin/python scripts/validate_gtdb_coherence.py kb/communities/Multispecies_Probiotic_MV_Luteolin_Consortium.yaml` | Passed, 0 incoherent blocks, 0 malformed lineages, 0 lineage conflicts. |
| `PYTHONPATH=src .venv/bin/python scripts/validate_yaml_scalars.py kb/communities/Multispecies_Probiotic_MV_Luteolin_Consortium.yaml` | Passed, 1 file checked, 0 truncated scalars. |
| `.venv/bin/linkml-validate --schema src/communitymech/schema/history.yaml --target-class HistoryRecord history/records/Multispecies_Probiotic_MV_Luteolin_Consortium/2026-09-22T195007Z-codex-c24ab8.yaml` | Passed, `No issues found`. |
| `PYTHONPATH=src .venv/bin/python scripts/evidence_snippet_audit.py kb/communities/Multispecies_Probiotic_MV_Luteolin_Consortium.yaml` | Passed, 22 snippets scanned, 21 `MATCH`, 1 `RENDERING`, 0 `WEAK`, 0 `MISMATCH`, 0 `NOCONTENT`. |
| `.venv/bin/linkml-reference-validator validate data kb/communities/Multispecies_Probiotic_MV_Luteolin_Consortium.yaml -s src/communitymech/schema/communitymech.yaml --config conf/reference_validator.yaml` | Passed, but `Total checks: 0`; the snippet audit above did the effective evidence-text check. |
| `PYTHONPATH=src .venv/bin/python scripts/audit_writers.py` | Passed before this review. |
| `PYTHONPATH=src .venv/bin/python -m communitymech.render` | Passed, rendered 415 communities plus `docs/browser.html` and `docs/index.html`. |
| `git diff --check` | Passed. |

## Identity and Grounding

The record identity is coherent. The cached PubMed/Europe PMC article text matches the DOI, PMID, PMCID, title, and version-of-record article represented by the three `external_resources` entries.

All three curated member taxa are the exact CICC probiotic strains reported in the paper. `B. longum` is correctly left `AMBIGUOUS` for GTDB because the local crosswalk can split NCBI `Bifidobacterium longum` between `GTDB:s__Bifidobacterium_infantis` and `GTDB:s__Bifidobacterium_longum`. `C. butyricum` has an internally coherent species-level GTDB block, and `L. reuteri` is transparently marked `UNRESOLVED` rather than guessed.

The laboratory `environment_term`, in-vitro MRS batch-culture setup, and intestine `modeled_environment` are appropriately scoped: the live co-culture was grown in MRS to produce M-MVs, and the intestinal model was a downstream DSS mouse-colitis test of M-MVs/Lut-MVs rather than live colonization by the three-strain consortium.

The one categorical identity error is `community_category: DIET`. In this schema `DIET` means direct interspecies electron transfer, while this record is about probiotic vesicle production for luteolin encapsulation and has no electrically conductive electron-transfer claim.

## Evidence

Supported:

- The primary PMID cache contains exact source text naming `B. longum CICC25033, C. butyricum CICC23847, and L. reuteri CICC6131`.
- The methods support mono-culture, pairwise 1:1, and 1:1:1 three-strain MRS arms, 1% inoculation, anaerobic 37 C 24 h incubation, and the 0.1 mg/mL L-cysteine hydrochloride amendment for groups containing `C. butyricum`.
- The results support higher viable cell counts in co-cultured strains, a putative cross-feeding interpretation, M-MV isolation from the co-cultured three-strain supernatant, LC-MS/MS profiling of mixed and single-strain MVs, and luteolin loading into M-MVs.
- The data-availability text supports ProteomeXchange `PXD071787`, iProX `IPX0014605000`, and BioProject `PRJNA1482721`.
- The discussion support for the open MsrA causality gap is exact: the authors state that they did not directly functionally validate causality by MsrA knockout, inhibition, or an equivalent add-back design.

Not supported:

- The `DIET` category is not an evidence issue in the article; it is a local enum misuse. The record does not cite, model, or otherwise discuss direct interspecies electron transfer.

## Completeness

The record is complete enough for the primary publication. It captures the three exact members, the CICC strain accessions, the MRS/L-cysteine anaerobic culture condition, the viable-count and cell-free-supernatant interaction assays, mixed-vesicle isolation and LC-MS/MS readouts, luteolin cargo, the in vivo DSS readouts at the level needed for this community, stable publication links, and the two public dataset accessions.

No major member, growth condition, stable reference, metal/REE declaration, or open mechanistic uncertainty is missing.

## Findings

### Major

| ID | Finding | Evidence | Maintained owner |
|---|---|---|---|
| F1 | `community_category: DIET` uses the wrong schema enum. In `src/communitymech/schema/communitymech.yaml`, `DIET` is defined as direct interspecies electron transfer; this record describes a probiotic biotechnology co-culture used to generate drug-delivery membrane vesicles and never asserts DIET. | `kb/communities/Multispecies_Probiotic_MV_Luteolin_Consortium.yaml:11`; `src/communitymech/schema/communitymech.yaml:213`; the maintained record text cites co-culture, M-MV, LC-MS/MS, and luteolin evidence only. | `tmp/write_multispecies_probiotic_vesicle_consortium.py`, then regenerate `kb/communities/Multispecies_Probiotic_MV_Luteolin_Consortium.yaml` and `docs/` |

### Minor

None found.

### Blockers

None found.

## Recommended Edits

1. In `tmp/write_multispecies_probiotic_vesicle_consortium.py`, change `community_category` from `DIET` to `BIOTECHNOLOGY`.
2. Regenerate `kb/communities/Multispecies_Probiotic_MV_Luteolin_Consortium.yaml` through `write_validated_community`.
3. Append a review-fix history record for the category correction.
4. Regenerate `docs/communities/Multispecies_Probiotic_MV_Luteolin_Consortium.html`, `docs/browser.html`, and `docs/index.html`.

## Follow-up Checks

- Re-run direct schema, strict, term-label, GTDB-coherence, YAML-scalar, history, and evidence-snippet validation after regeneration.
- Re-run `PYTHONPATH=src .venv/bin/python -m communitymech.render` after the YAML fix.
- Reinspect the generated YAML and browser card for `community_category: BIOTECHNOLOGY`.
- Run full-corpus `PYTHONPATH=src .venv/bin/python scripts/validate_strict.py`.
- Run `git diff --check` before staging.

## Additional Notes

This review used the cached PubMed abstract, Europe PMC open-access article text, and supplementary workbook text only. It did not contact authors, spend provider credits, or resolve the unavailable local NCBI-to-GTDB crosswalk for `L. reuteri`.

The category check is a schema-semantic review finding: LinkML validates `DIET`, but the enum description is direct interspecies electron transfer, not a diet/food/probiotic bucket.
