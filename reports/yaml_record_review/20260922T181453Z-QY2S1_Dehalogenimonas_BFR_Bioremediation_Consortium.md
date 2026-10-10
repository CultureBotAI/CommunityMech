# YAML Record Review: QY2-S1 Dehalogenimonas-Rich Brominated-Flame-Retardant Consortium

- Repository: CultureBotAI/CommunityMech
- Record: `kb/communities/QY2S1_Dehalogenimonas_BFR_Bioremediation_Consortium.yaml`
- Started UTC: 2026-09-22T18:14:53Z
- Finished UTC: 2026-09-22T18:14:53Z
- Verdict: needs curation

## Target

`CommunityMech:000424` is a maintained `MicrobialCommunity` record for the QY2-S1 Dehalogenimonas-containing anaerobic enrichment from Zhang et al. 2026 (`PMID:42511722`, DOI `10.3390/ijms27146379`). The record models the culture as an engineered bioremediation enrichment assayed in anaerobic serum bottles with BDE 99, beta-TBCO, and combined BDE 99/beta-TBCO exposure arms.

An ignored-inclusive duplicate search covered `kb/`, `data/`, `docs/`, `history/`, `references_cache/`, `research/`, and `reports/` for `QY2S1`, `QY2-S1`, `42511722`, `10.3390/ijms27146379`, `SRP684405`, and the title phrase `Dehalogenimonas-Rich Brominated`. It found prior scouting leads in `research/scouting/`, the new record, the new cached reference files, the new generated page, and the new history record, but no pre-existing curated record in `kb/communities/` or `data/isolates/`.

## Validation

| Check | Result |
|---|---|
| `.venv/bin/linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/QY2S1_Dehalogenimonas_BFR_Bioremediation_Consortium.yaml` | Passed |
| `.venv/bin/linkml-term-validator validate-data kb/communities/QY2S1_Dehalogenimonas_BFR_Bioremediation_Consortium.yaml -s src/communitymech/schema/communitymech.yaml --labels` | Passed |
| `PYTHONPATH=src .venv/bin/python scripts/validate_strict.py kb/communities/QY2S1_Dehalogenimonas_BFR_Bioremediation_Consortium.yaml` | Passed |
| `.venv/bin/linkml-reference-validator validate data kb/communities/QY2S1_Dehalogenimonas_BFR_Bioremediation_Consortium.yaml -s src/communitymech/schema/communitymech.yaml --config conf/reference_validator.yaml` | Passed |
| `.venv/bin/linkml-validate -s src/communitymech/schema/history.yaml history/records/QY2S1_Dehalogenimonas_BFR_Bioremediation_Consortium/2026-09-22T181130Z-claude-code-b0c50c.yaml` | Passed |
| `PYTHONPATH=src .venv/bin/python scripts/validate_strict.py` | Passed over 418 files |
| `PYTHONPATH=src .venv/bin/python scripts/audit_writers.py` | Passed |
| `PYTHONPATH=src .venv/bin/pytest tests/test_id_uniqueness.py tests/test_reference_validator_actually_validates.py` | 27 passed; `test_isolates_pass_schema_validation` failed because the test shells out through `uv run`, which fails building `llvmlite==0.46.0` on Python 3.13 before LinkML runs |
| `.venv/bin/linkml-validate -s src/communitymech/schema/communitymech.yaml data/isolates/*.yaml`, expanded over the isolate records named by the failing test | Passed |

The `just validate`, `just validate-strict`, `just validate-terms`, and `just new-history` wrappers all fail locally before reaching their underlying commands because `uv run` tries to build `llvmlite==0.46.0` and exits with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`. Direct `.venv` invocations were used for the same validators and the shared `kg_microbe_history` scaffolder.

## Identity and Grounding

The record identity is correct: the primary paper studied QY2-S1, a Dehalogenimonas-containing mixed culture derived from QY-2, under single and co-exposure BDE 99/beta-TBCO assays. `community_category: BIOREMEDIATION`, `ecological_state: ENGINEERED`, and laboratory `environment_term` match an enriched anaerobic test culture rather than an in situ pond assemblage.

The genus NCBITaxon identifiers in `taxonomy` validate against current labels. `Clostridium` is correctly marked `AMBIGUOUS` for GTDB because NCBI genus `NCBITaxon:1485` is split. `Sedimentibacter` and `Methanoculleus` carry internally coherent GTDB genus groundings copied from existing local records. `Dehalogenimonas` is unresolved for GTDB with an explicit note rather than a guessed mapping.

## Evidence

The PMID and DOI resolve, and the cache contains the PubMed abstract, the open Europe PMC article text, and manually extracted PDF supplement text. Snippet validation passes for every recorded snippet.

Most narrow claims are supported: the source explicitly names QY2-S1, its source pond and serial enrichment, the 3 uM BDE 99/beta-TBCO exposure panel, the genus-level 16S composition, the co-exposure rate inhibition and BDE 99 pathway truncation, 30 C anaerobic dark incubation, the SRA accession, and the unknown strain/genome/RDase gap.

## Completeness

The record is complete enough at genus level. It deliberately avoids species names, strain names, exact genus abundances, and RDase identities that the source did not report in text. It also records the remaining species/RDase uncertainty as a concrete open discussion.

The medium block contains the main available anaerobic setup details from the PDF supplement. The exact inorganic salt formula remains delegated to He et al. 2003 in the source and was not chased into a secondary methods citation for this initial record.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | `ecological_interactions#Dehalogenimonas BFR Organohalide Respiration` is not an interspecies or syntrophic interaction. It records a Dehalogenimonas-centered terminal-electron-acceptor inference, has `source_taxon: Dehalogenimonas` but no target organism, and uses the generic interspecies GO term. The cited paper supports Dehalogenimonas as the sole detected OHRB and a likely BDE 99/beta-TBCO terminal electron acceptor user, not a second community interaction beyond the fermenter/methanogen support edge. | Record lines 221-247; source snippets `only the genus Dehalogenimonas was detected` and `Dehalogenimonas likely utilizes BDE 99 and β-TBCO as terminal electron acceptors`. | `kb/communities/QY2S1_Dehalogenimonas_BFR_Bioremediation_Consortium.yaml` |
| major | The growth medium asserts two reductants and PCE setup details without a nearest snippet that supports those exact claims. The source supports `sodium lactate (10 mM)`, pH, and inoculum size in the attached evidence; `L-cysteine 0.2 mM`, `sodium sulfide nonahydrate 0.2 mM`, and `6 uL PCE` currently rely on uncited neighboring supplement text. | Record lines 285-321; supplement lines 73-87 in `references_cache/PMID_42511722.supplement.md`. | `kb/communities/QY2S1_Dehalogenimonas_BFR_Bioremediation_Consortium.yaml` |

## Recommended Edits

Remove `Dehalogenimonas BFR Organohalide Respiration` from `ecological_interactions` or move its evidence onto a non-interaction field. The existing taxonomy role, environmental factors, and the fermenter/methanogen support interaction already preserve the supported Dehalogenimonas claims without presenting a single-genus metabolism as syntrophy.

Add a supplement-backed medium/preparation snippet that explicitly names `L-cysteine`, `Na2S·9H2O`, `0.2 mM`, `6 uL of PCE`, and the readiness criterion for PCE degradation before QY2-S1 use; then keep the lactate, pH, and inoculum snippets as narrower support.

## Follow-up Checks

- Re-run `.venv/bin/linkml-validate` on the record.
- Re-run `.venv/bin/linkml-term-validator` on the record.
- Re-run `PYTHONPATH=src .venv/bin/python scripts/validate_strict.py` on the record and full corpus.
- Re-run `.venv/bin/linkml-reference-validator` on the record.
- Regenerate HTML with `PYTHONPATH=src .venv/bin/python -m communitymech.render`.

## Additional Notes

The review did not contact authors, spend provider credits, or inspect uncited secondary references. It used the cached PubMed/Europe PMC main text and the extracted open supplementary PDF only.
