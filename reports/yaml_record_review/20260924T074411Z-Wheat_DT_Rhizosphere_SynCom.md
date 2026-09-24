# YAML Record Review: Wheat DT Rhizosphere SynCom

- Repository: CultureBotAI/CommunityMech
- Record: kb/communities/Wheat_DT_Rhizosphere_SynCom.yaml
- Started UTC: 2026-09-24T07:37:00Z
- Finished UTC: 2026-09-24T07:44:11Z
- Verdict: needs curation

## Target

Reviewed maintained `MicrobialCommunity` record
`kb/communities/Wheat_DT_Rhizosphere_SynCom.yaml`.

- ID: `CommunityMech:000429`
- Label: `Wheat DT Rhizosphere SynCom`
- Primary source: `PMID:42453107`
- DOI: `10.3389/fmicb.2026.1818676`
- Maintained or generated: maintained YAML
- New history entry:
  `history/records/Wheat_DT_Rhizosphere_SynCom/2026-09-24T073322Z-codex-429.yaml`

## Validation

| Check | Result |
|---|---|
| `just validate kb/communities/Wheat_DT_Rhizosphere_SynCom.yaml` | Blocked before validation by `uv` rebuilding `llvmlite==0.46.0` under Python 3.13. |
| `.venv/bin/linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Wheat_DT_Rhizosphere_SynCom.yaml` | Pass, no issues found. |
| `just validate-history history/records/Wheat_DT_Rhizosphere_SynCom/2026-09-24T073322Z-codex-429.yaml` | Blocked before validation by the same `uv` / `llvmlite==0.46.0` rebuild failure. |
| `.venv/bin/linkml-validate --schema src/communitymech/schema/history.yaml --target-class HistoryRecord history/records/Wheat_DT_Rhizosphere_SynCom/2026-09-24T073322Z-codex-429.yaml` | Pass, no issues found. |
| `PYTHONPATH=src .venv/bin/python scripts/validate_strict.py kb/communities/Wheat_DT_Rhizosphere_SynCom.yaml` | Pass; 1 file scanned, 0 error rows. |
| `.venv/bin/linkml-term-validator validate-data kb/communities/Wheat_DT_Rhizosphere_SynCom.yaml -s src/communitymech/schema/communitymech.yaml --labels` | Pass. |
| `.venv/bin/linkml-reference-validator validate data kb/communities/Wheat_DT_Rhizosphere_SynCom.yaml -s src/communitymech/schema/communitymech.yaml --config conf/reference_validator.yaml` | Pass. |
| `PYTHONPATH=src .venv/bin/python scripts/evidence_snippet_audit.py kb/communities/Wheat_DT_Rhizosphere_SynCom.yaml` | Pass as part of the two-record audit; all 58 snippets across the Barley and Wheat DT-SynCom records matched cached evidence exactly, with 0 weak, mismatched, or missing snippets. |
| `PYTHONPATH=src .venv/bin/python scripts/validate_yaml_scalars.py kb/communities/Wheat_DT_Rhizosphere_SynCom.yaml history/records/Wheat_DT_Rhizosphere_SynCom/2026-09-24T073322Z-codex-429.yaml` | Pass as part of the two-record scalar audit. |
| `PYTHONPATH=src .venv/bin/python scripts/validate_gtdb_coherence.py kb/communities/Wheat_DT_Rhizosphere_SynCom.yaml` | Pass as part of the two-record GTDB coherence audit. |
| `PYTHONPATH=src .venv/bin/python scripts/validate_shared_taxon_ids.py kb/communities/Wheat_DT_Rhizosphere_SynCom.yaml` | Pass as part of the two-record shared-id audit. |
| `PYTHONPATH=src .venv/bin/python scripts/validate_prokaryotic_lineage.py kb/communities/Wheat_DT_Rhizosphere_SynCom.yaml` | Pass as part of the two-record lineage audit. |
| `PYTHONPATH=src .venv/bin/python scripts/validate_ncbitaxon_ids.py kb/communities/Wheat_DT_Rhizosphere_SynCom.yaml` | Skipped after the external resolver hung. |

## Identity and Grounding

The record denotes the sixteen-member wheat-origin Drought-Tolerant SynCom
assembled by Rigerte et al. from wheat rhizosphere isolates and assayed in the
barley rhizosphere. Its `ENGINEERED` state, `SYNTHETIC` origin, and
`RHIZOSPHERE` category match the defined bacterial inoculant; the
`environment_term` correctly follows the barley assay environment while
`modeled_environment` preserves the wheat isolation context.

The pre-curation duplicate search used `rg --no-ignore --hidden` over `kb`,
`data`, `history`, `references_cache`, `docs`, and `reports` for the
`PMID:42453107`, `10.3389/fmicb.2026.1818676`, `PMC13365038`, `1818676`,
`PRJNA1405459`, and title strings and found no older maintained record or
local cache for this article.

All sixteen Wheat SynCom members from Table 1 are present exactly once at the
genus plus strain-code resolution supported by the article. The NCBITaxon ids
and labels pass the id/label gate, and W16 correctly leaves the local GTDB
genus grounding `AMBIGUOUS` between `Ensifer` and `Sinorhizobium`.

## Evidence

The article supports most record claims exactly:

- The design evidence cites the PEG-tolerant strain selection, separate
  barley/wheat SynCom assembly, equal-volume culture mixing, and barley
  seedling inoculation.
- Each `taxonomy` member cites the exact Table 1 W-code, genus-level label,
  and NCBI accession.
- The powdery-mildew interaction quotes the reported DAF fluorescence
  reduction for barley and wheat SynCom treatments and the paper's own ISR
  interpretation.
- Pikovskaya isolation, YME preparation, and powdery-mildew challenge
  evidence are attached to their narrow environmental or growth-media claims.
- The BioProject association quotes the data-availability accession and keeps
  a discussion open because NCBI reported `PRJNA1405459` as not public during
  curation.

The only evidence-placement defect is in the rhizosphere metatranscriptome
interaction. Its current evidence snippet supports downregulation of `PF02868`,
`PF01614`, and `K05516` after Wheat SynCom inoculation, but it does not support
the final clause saying those were selective changes rather than a broad shift.
The article does support that broader clause elsewhere; the record needs the
second source sentence on selective, function-specific shifts attached to the
same assertion.

## Completeness

The record captures the consequential primary-source facts available from the
open article: all sixteen strain codes, Table 1 genus labels and accessions,
GCEF cultivar source, PEG-tolerant selection, inoculum assembly, barley
powdery-mildew protection, Wheat SynCom metatranscriptomic feature shifts,
sequencing BioProject metadata, and metal non-relevance.

Species-level taxonomy is correctly left unasserted for the Wheat SynCom
because Table 1 identifies every W-code member as `sp.` within its genus.
Species-level GTDB grounding is deliberately unresolved because the local
`NCBI2GTDB.tsv.gz` kg-microbe crosswalk was not available.

## Findings

| Severity | Finding | Maintained owner |
|---|---|---|
| Major | `Wheat DT-SynCom selective rhizosphere functional shifts` claims Wheat SynCom changes happened `rather than a broad shift in rhizosphere functional profiles`, but its only evidence item quotes only the wheat-specific downregulation of `PF02868`, `PF01614`, and `K05516`. The article supports the broad/non-broad distinction; the record needs a second snippet at this assertion. | `kb/communities/Wheat_DT_Rhizosphere_SynCom.yaml` |

## Recommended Edits

- Add a second evidence item under
  `Wheat DT-SynCom selective rhizosphere functional shifts` quoting the
  article's summary that bioinoculants induced selective,
  function-specific microbial gene-expression shifts, not broad community
  changes.
- Append a `curation_history` event and a new append-only history record for
  the review fix.
- Regenerate `docs/communities/Wheat_DT_Rhizosphere_SynCom.html` after the
  YAML change.

## Follow-up Checks

- Re-run the focused schema, strict, term, reference, snippet-audit,
  scalar, GTDB-coherence, shared-taxon-id, prokaryotic-lineage, and history
  validators for the edited Wheat record.
- Re-run `PYTHONPATH=src .venv/bin/python -m communitymech.render` and compare
  the generated docs diff.
- Re-run the standard `just` validator wrappers after the Python 3.13
  `llvmlite` rebuild issue is resolved, to confirm the direct `.venv/bin`
  invocations still match the declared recipes.

## Additional Notes

`scripts/gtdb_ground.py --community kb/communities/Wheat_DT_Rhizosphere_SynCom.yaml --emit-yaml`
stopped before producing grounding edits because `NCBI2GTDB.tsv.gz` was not
found in any configured local kg-microbe path. That is not a record defect:
the GTDB coherence and prokaryotic lineage validators both passed with most
new bacterial taxa left `UNRESOLVED` and W16 left `AMBIGUOUS`.
