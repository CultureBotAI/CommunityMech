# YAML Record Review: Hexamine Formaldehyde Consortium C6

- Repository: CultureBotAI/CommunityMech
- Record: `kb/communities/Hexamine_Formaldehyde_Consortium_C6.yaml`
- Started UTC: 2026-09-21T09:28:23Z
- Finished UTC: 2026-09-21T09:31:00Z
- Verdict: pass with minor issues

## Target

| Field | Value |
|---|---|
| Class | `MicrobialCommunity` |
| ID | `CommunityMech:000405` |
| Label | Hexamine Formaldehyde Consortium C6 |
| Maintained path | `kb/communities/Hexamine_Formaldehyde_Consortium_C6.yaml` |
| Generated | No |
| Primary source | `PMID:41743136`; DOI `10.3389/fmicb.2026.1753858`; cached full text in `references_cache/PMID_41743136.txt` |
| Scope | Six-isolate synthetic bacterial consortium for hexamine/formaldehyde/COD removal under suspended and immobilized biofilm conditions |

The target is a maintained community record for Consortium C6 from Ahmed and
Ray Chaudhuri 2026, not a natural wastewater-treatment-plant community, raw
environmental isolate set, or reusable taxon record.

Gitignore-independent `rg -uu` searches over `kb`, `data`, `history`,
`reports`, `references_cache`, `notes`, `docs`, and `.claude` for
`CommunityMech:000405`, `Hexamine_Formaldehyde_Consortium_C6`,
`PMID:41743136`, and `10.3389/fmicb.2026.1753858` found only the new curated
record, the new source cache, new generated docs, and this curation/review
trail. Ignored files were included.

## Validation

`just` wrappers were unavailable in this checkout because `uv run` currently
tries to build `llvmlite==0.46.0` / `numba==0.64.0` under Python 3.13 and fails
with `TypeError: Popen.__init__() got an unexpected keyword argument
'dry_run'`. Direct `.venv` equivalents were used where possible.

| Check | Result |
|---|---|
| `.venv/bin/linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Hexamine_Formaldehyde_Consortium_C6.yaml` | pass |
| `PYTHONPATH=src .venv/bin/python scripts/validate_strict.py kb/communities/Hexamine_Formaldehyde_Consortium_C6.yaml` | pass; 0 ERROR rows |
| `.venv/bin/linkml-term-validator validate-data kb/communities/Hexamine_Formaldehyde_Consortium_C6.yaml -s src/communitymech/schema/communitymech.yaml --labels` | pass |
| `PYTHONPATH=src .venv/bin/python scripts/evidence_snippet_audit.py kb/communities/Hexamine_Formaldehyde_Consortium_C6.yaml` | pass; 22 MATCH / 0 RENDERING / 0 ASSEMBLED / 0 WEAK / 0 MISMATCH / 0 NOCONTENT |
| `.venv/bin/linkml-validate --schema src/communitymech/schema/history.yaml --target-class HistoryRecord history/records/Hexamine_Formaldehyde_Consortium_C6/2026-09-21T091800Z-claude-code-8cb5e0.yaml history/records/Hexamine_Formaldehyde_Consortium_C6/2026-09-21T092303Z-claude-code-99ec4b.yaml` | pass |
| `PYTHONPATH=src .venv/bin/python scripts/audit_writers.py` | pass; audit table regenerated |
| `PYTHONPATH=src .venv/bin/python -m communitymech.render` | pass; rendered 395 community pages plus browser and landing pages |
| `PYTHONPATH=src .venv/bin/python -m pytest tests/test_snippets_are_not_truncated.py tests/test_no_new_bracketed_snippets.py -q` | pass; 10 tests |
| `PYTHONPATH=src .venv/bin/python -m pytest tests/test_id_uniqueness.py::test_every_communitymech_id_is_used_exactly_once tests/test_id_uniqueness.py::test_no_id_bearing_records_outside_known_dirs -q` | pass; 2 tests |
| `git diff --cached --check` | pass |

Not run through the `just validate-references-explained` wrapper for the same
`uv`/`llvmlite` reason. The direct `linkml-reference-validator` invocation was
not treated as substantive for this review because this repository documents
that a clean run reports `Total checks: 0`; `evidence_snippet_audit.py`
confirmed every curated snippet against the committed cache instead.

## Identity and Grounding

The record identity is sound. `ENGINEERED`, `SYNTHETIC`, and `BIOREMEDIATION`
match the source's defined culture-based consortium. The record correctly keeps
the measured setting as `ENVO:01001405` laboratory environment while using
`ENVO:00002043` only as a modeled wastewater-treatment-plant context for the
authors' proposed future STP/ETP application.

The six member strains match the paper's abstract and Table 1: SRCHD03 and
SRCHD04 are `Brevundimonas diminuta`; SRCHD05 and SRCHD07 are `Brucella
pseudintermedia`; SRCHD06 is `Ochrobactrum sp.` and is conservatively grounded
to genus `NCBITaxon:528`; SRCHD02 is `Micrococcus luteus`. NCBITaxon, CHEBI,
GO, and ENVO labels passed the term validator.

## Evidence

Supported claim groups:

- C6 is the SRCHD02:SRCHD03:SRCHD04:SRCHD05:SRCHD06:SRCHD07 consortium mixed
  at the Table 1 1:1:1:1:1:1 ratio.
- The six taxon entries preserve exactly the isolate IDs and organism names
  from the source abstract.
- Table 2 supports the 24 h, 48 h, and 72 h suspended-AS-broth readouts for
  C6 hexamine, formaldehyde, COD, and ammonia.
- The source's low-dose irradiation method supports the 3.75 Gy and 5.25 Gy
  cobalt-60 challenge and the suspended-culture vs polypropylene-Raschig-ring
  biofilm comparison.
- The post-irradiation medium record correctly uses Figure 4's 100 mg/L
  hexamine condition rather than the 50 mg/L C1-C6 development feed.
- The discussion-level knowledge gap correctly leaves pairwise molecular
  division of labor unresolved.

Unsupported or over-scoped claims:

- `growth_media[0].vessel_type` says `AS broth tube`, but the nearest cited
  source text only states that the consortia were cultured in AS broth at
  50 mg/L hexamine and sampled at 24 h, 48 h, and 72 h.

## Completeness

The record is complete enough for the source: it captures the defined
consortium identity, each strain member, the engineered C1-C6 assembly and C6
selection, suspended and immobilized pollutant-removal outcomes, low-dose
cobalt-60 perturbation, two distinct hexamine feed concentrations, the primary
DOI, and the unresolved molecular-mechanism gap.

Appropriately absent fields:

- `associated_datasets`: the article contains its contributions and does not
  report SRA, BioProject, or model-repository accessions.
- pairwise ecological edges: the source reports community-level C6 performance
  but does not identify isolate-resolved metabolite exchange steps.
- `metals_present`: the consortium targets hexamine, formaldehyde, ammonia,
  and COD, not metal or rare-earth processing.

## Findings

| Severity | Finding | Maintained owner |
|---|---|---|
| minor | The first growth-media entry has unsupported `vessel_type: AS broth tube`; the consortium-development method says the consortia were grown in AS broth but does not specify the vessel. | `kb/communities/Hexamine_Formaldehyde_Consortium_C6.yaml` |

No blocker or major findings.

## Recommended Edits

Remove `growth_media[0].vessel_type` from
`kb/communities/Hexamine_Formaldehyde_Consortium_C6.yaml`, append a focused
curation event and history record for the review fix, then regenerate
`docs/communities/Hexamine_Formaldehyde_Consortium_C6.html`.

## Follow-up Checks

After the recommended edit, rerun:

- `.venv/bin/linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Hexamine_Formaldehyde_Consortium_C6.yaml`
- `PYTHONPATH=src .venv/bin/python scripts/validate_strict.py kb/communities/Hexamine_Formaldehyde_Consortium_C6.yaml`
- `PYTHONPATH=src .venv/bin/python scripts/evidence_snippet_audit.py kb/communities/Hexamine_Formaldehyde_Consortium_C6.yaml`
- `PYTHONPATH=src .venv/bin/python -m communitymech.render`
- `git diff --check`
- `gh pr checks 1006`

## Additional Notes

The pre-review self-check had already split the 50 mg/L suspended-culture
record from the 100 mg/L Figure 4 post-irradiation record and added Table 1 as
direct evidence for the equal-ratio C6 assembly.
