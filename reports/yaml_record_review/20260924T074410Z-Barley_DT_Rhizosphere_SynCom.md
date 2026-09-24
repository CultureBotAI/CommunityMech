# YAML Record Review: Barley DT Rhizosphere SynCom

- Repository: CultureBotAI/CommunityMech
- Record: kb/communities/Barley_DT_Rhizosphere_SynCom.yaml
- Started UTC: 2026-09-24T07:37:00Z
- Finished UTC: 2026-09-24T07:44:10Z
- Verdict: pass with minor issues

## Target

Reviewed maintained `MicrobialCommunity` record
`kb/communities/Barley_DT_Rhizosphere_SynCom.yaml`.

- ID: `CommunityMech:000428`
- Label: `Barley DT Rhizosphere SynCom`
- Primary source: `PMID:42453107`
- DOI: `10.3389/fmicb.2026.1818676`
- Maintained or generated: maintained YAML
- New history entry:
  `history/records/Barley_DT_Rhizosphere_SynCom/2026-09-24T073321Z-codex-428.yaml`

## Validation

| Check | Result |
|---|---|
| `just validate kb/communities/Barley_DT_Rhizosphere_SynCom.yaml` | Blocked before validation by `uv` rebuilding `llvmlite==0.46.0` under Python 3.13. |
| `.venv/bin/linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Barley_DT_Rhizosphere_SynCom.yaml` | Pass, no issues found. |
| `just validate-history history/records/Barley_DT_Rhizosphere_SynCom/2026-09-24T073321Z-codex-428.yaml` | Blocked before validation by the same `uv` / `llvmlite==0.46.0` rebuild failure. |
| `.venv/bin/linkml-validate --schema src/communitymech/schema/history.yaml --target-class HistoryRecord history/records/Barley_DT_Rhizosphere_SynCom/2026-09-24T073321Z-codex-428.yaml` | Pass, no issues found. |
| `PYTHONPATH=src .venv/bin/python scripts/validate_strict.py kb/communities/Barley_DT_Rhizosphere_SynCom.yaml` | Pass; 1 file scanned, 0 error rows. |
| `.venv/bin/linkml-term-validator validate-data kb/communities/Barley_DT_Rhizosphere_SynCom.yaml -s src/communitymech/schema/communitymech.yaml --labels` | Pass. |
| `.venv/bin/linkml-reference-validator validate data kb/communities/Barley_DT_Rhizosphere_SynCom.yaml -s src/communitymech/schema/communitymech.yaml --config conf/reference_validator.yaml` | Pass. |
| `PYTHONPATH=src .venv/bin/python scripts/evidence_snippet_audit.py kb/communities/Barley_DT_Rhizosphere_SynCom.yaml` | Pass as part of the two-record audit; all 58 snippets across the Barley and Wheat DT-SynCom records matched cached evidence exactly, with 0 weak, mismatched, or missing snippets. |
| `PYTHONPATH=src .venv/bin/python scripts/validate_yaml_scalars.py kb/communities/Barley_DT_Rhizosphere_SynCom.yaml history/records/Barley_DT_Rhizosphere_SynCom/2026-09-24T073321Z-codex-428.yaml` | Pass as part of the two-record scalar audit. |
| `PYTHONPATH=src .venv/bin/python scripts/validate_gtdb_coherence.py kb/communities/Barley_DT_Rhizosphere_SynCom.yaml` | Pass as part of the two-record GTDB coherence audit. |
| `PYTHONPATH=src .venv/bin/python scripts/validate_shared_taxon_ids.py kb/communities/Barley_DT_Rhizosphere_SynCom.yaml` | Pass as part of the two-record shared-id audit. |
| `PYTHONPATH=src .venv/bin/python scripts/validate_prokaryotic_lineage.py kb/communities/Barley_DT_Rhizosphere_SynCom.yaml` | Pass as part of the two-record lineage audit. |
| `PYTHONPATH=src .venv/bin/python scripts/validate_ncbitaxon_ids.py kb/communities/Barley_DT_Rhizosphere_SynCom.yaml` | Skipped after the external resolver hung. |

## Identity and Grounding

The record denotes the sixteen-member barley-origin Drought-Tolerant SynCom
assembled by Rigerte et al. from barley rhizosphere isolates. Its
`ENGINEERED` state, `SYNTHETIC` origin, and `RHIZOSPHERE` category match the
Methods design in which selected isolates were cultivated, normalized, mixed
in equal proportions, and inoculated onto barley seeds.

The pre-curation duplicate search used `rg --no-ignore --hidden` over `kb`,
`data`, `history`, `references_cache`, `docs`, and `reports` for the
`PMID:42453107`, `10.3389/fmicb.2026.1818676`, `PMC13365038`, `1818676`,
`PRJNA1405459`, and title strings and found no older maintained record or
local cache for this article.

All sixteen Barley SynCom members from Table 1 are present exactly once. The
NCBITaxon ids and canonical labels pass the label validator; the
`Rhodococcus fascians` B12 preferred term intentionally preserves the article's
printed old name while the ontology term records the current
`Rhodococcoides fascians` label resolved from accession `NR_037021.1`.

## Evidence

The article supports the record's central claims:

- The design evidence cites the PEG-tolerant strain selection, separate
  barley/wheat SynCom assembly, equal-volume culture mixing, and barley
  seedling inoculation.
- Each `taxonomy` member cites the exact Table 1 row for its B-code, host,
  genus, species-level label when present, and NCBI accession.
- The powdery-mildew interaction quotes the reported DAF fluorescence
  reduction for barley and wheat SynCom treatments and the paper's own ISR
  interpretation.
- The persistence interaction is scoped to 16S OTU matches and explicitly
  avoids over-claiming strain-level persistence.
- Pikovskaya isolation, YME preparation, and powdery-mildew challenge
  evidence are attached to their narrow environmental or growth-media claims.
- The BioProject association quotes the data-availability accession and keeps
  a discussion open because NCBI reported `PRJNA1405459` as not public during
  curation.

No unsupported biological claim, wrong identifier, or citation mismatch was
found.

## Completeness

The record captures the consequential primary-source facts available from the
open article: all sixteen strain codes, Table 1 taxonomic labels and
accessions, GCEF cultivar source, PEG-tolerant selection, inoculum assembly,
barley powdery-mildew protection, post-inoculation 16S OTU detection,
sequencing BioProject metadata, and metal non-relevance.

The B7 `Priestia aryabhattai` accession is deliberately preserved as printed
and flagged with an open discussion because Table 1 repeats `NR_133818.1` for
B6 and B7. Species-level GTDB grounding is deliberately unresolved because the
local `NCBI2GTDB.tsv.gz` kg-microbe crosswalk was not available.

## Findings

| Severity | Finding | Maintained owner |
|---|---|---|
| Minor | The persistence interaction description says `at at least 99% identity and coverage`, duplicating `at`. This is non-biological wording drift in an otherwise correctly scoped claim. | `kb/communities/Barley_DT_Rhizosphere_SynCom.yaml` |

## Recommended Edits

- Fix the duplicate word in
  `kb/communities/Barley_DT_Rhizosphere_SynCom.yaml` so the persistence
  sentence reads `at least 99% identity and coverage`.
- Append a `curation_history` event and a new append-only history record for
  the review fix.
- Regenerate `docs/communities/Barley_DT_Rhizosphere_SynCom.html` after the
  YAML change.

## Follow-up Checks

- Re-run the focused schema, strict, term, reference, snippet-audit,
  scalar, GTDB-coherence, shared-taxon-id, prokaryotic-lineage, and history
  validators for the edited Barley record.
- Re-run `PYTHONPATH=src .venv/bin/python -m communitymech.render` and compare
  the generated docs diff.
- Re-run the standard `just` validator wrappers after the Python 3.13
  `llvmlite` rebuild issue is resolved, to confirm the direct `.venv/bin`
  invocations still match the declared recipes.

## Additional Notes

`scripts/gtdb_ground.py --community kb/communities/Barley_DT_Rhizosphere_SynCom.yaml --emit-yaml`
stopped before producing grounding edits because `NCBI2GTDB.tsv.gz` was not
found in any configured local kg-microbe path. That is not a record defect: the
GTDB coherence and prokaryotic lineage validators both passed with the new
members left `UNRESOLVED`.
