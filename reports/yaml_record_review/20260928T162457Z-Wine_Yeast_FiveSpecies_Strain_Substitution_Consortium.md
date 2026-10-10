# YAML Record Review: Wine Yeast Five-Species Strain-Substitution Consortium

- Repository: CultureBotAI/CommunityMech
- Record: `kb/communities/Wine_Yeast_FiveSpecies_Strain_Substitution_Consortium.yaml`
- Started UTC: 2026-09-28T16:18:00Z
- Finished UTC: 2026-09-28T16:24:57Z
- Verdict: pass with minor issues

## Target

| Field | Value |
|---|---|
| Path | `kb/communities/Wine_Yeast_FiveSpecies_Strain_Substitution_Consortium.yaml` |
| Class | `MicrobialCommunity` |
| ID | `CommunityMech:000465` |
| Label | `Wine Yeast Five-Species Strain-Substitution Consortium` |
| Maintained/generated | Maintained curated YAML |

The record denotes a defined five-species yeast consortium assembled to model
spontaneous wine alcoholic fermentation. It names *Saccharomyces cerevisiae*,
*Lachancea thermotolerans*, *Hanseniaspora uvarum*, *Starmerella bacillaris*,
and *Torulaspora delbrueckii* as members and intentionally keeps the ten exact
strain identities, fermentation medium, temperature, and timing in an open
knowledge-gap discussion because the cached PubMed abstract does not expose
those methods details.

## Validation

| Check | Result |
|---|---|
| `../TraitMech/.venv/bin/linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Wine_Yeast_FiveSpecies_Strain_Substitution_Consortium.yaml` | Pass |
| `PYTHONPATH=src ../TraitMech/.venv/bin/python scripts/validate_strict.py kb/communities/Wine_Yeast_FiveSpecies_Strain_Substitution_Consortium.yaml` | Pass; 1 file scanned, 0 files with ERROR |
| `uvx linkml-term-validator validate-data kb/communities/Wine_Yeast_FiveSpecies_Strain_Substitution_Consortium.yaml -s src/communitymech/schema/communitymech.yaml --labels` | Pass |
| `uvx --with linkml linkml-reference-validator validate data kb/communities/Wine_Yeast_FiveSpecies_Strain_Substitution_Consortium.yaml -s src/communitymech/schema/communitymech.yaml --config conf/reference_validator.yaml` | Pass |
| `PYTHONPATH=src ../TraitMech/.venv/bin/python scripts/evidence_snippet_audit.py kb/communities/Wine_Yeast_FiveSpecies_Strain_Substitution_Consortium.yaml --list-mismatch --list-nocontent --list-rendering` | Pass; 15 snippets scanned, all 15 MATCH |
| `../TraitMech/.venv/bin/linkml-validate --schema src/communitymech/schema/history.yaml --target-class HistoryRecord history/records/Wine_Yeast_FiveSpecies_Strain_Substitution_Consortium/2026-09-28T161413Z-codex-d68abd.yaml` | Pass |

`just validate-references-explained` and `just validate-terms` were run via
equivalent direct `uvx`/venv commands because project-level `uv run` is not
usable in this checkout with the current Python 3.13/llvmlite environment.

## Identity and Grounding

The ID, filename, name, `ENGINEERED` ecological state, `SYNTHETIC` origin, and
`BIOTECHNOLOGY` category agree with an in-vitro defined wine yeast consortium.
`ENVO:01001405` / `laboratory environment` is the physical study setting, with
free curator wording preserved in `preferred_term`.

Term validation confirmed the local ontology labels for the five NCBITaxon
members and the repeated `GO:0006113` fermentation process. The `NO_GTDB_EQUIVALENT`
status is appropriate because all five members are eukaryotic yeasts outside
GTDB's bacterial/archaeal scope.

iModulonDB was not applicable: the record names yeast species and consortium
outputs, not a bacterial gene, locus tag, regulator, pathway, or iModulonDB
covered expression component.

## Evidence

All 15 curated evidence snippets matched `references_cache/PMID_42784437.txt`.
The abstract directly supports the five species, two phenotypically diverging
strains per species, single-species drop-out and single-strain-substitution
perturbations, fermentation kinetics/sugar utilization/population/metabolite
endpoints, population/growth/metabolic output shifts, sugar-utilization
competition, and the broader non-*Saccharomyces* substitution effect.

The PubMed and DOI external resources are grounded by the cached PubMed record.
No DOI-only Methods details were lifted into the record; exact strain names,
medium, and incubation parameters remain unasserted.

## Completeness

The record is complete for the claims exposed by the cached PubMed abstract and
appropriately avoids fabricating strain, medium, temperature, or timepoint
details that would require Methods access.

An ignored-inclusive `rg --hidden --no-ignore` over `kb`, `data`, `history`,
`docs`, `references_cache`, `reports`, and the local 20260928 scout directory
found the expected new maintained YAML, generated pages/browser data, history
sidecar, PubMed cache, and scout hits for `PMID:42784437`,
`CommunityMech:000465`, and
`Wine_Yeast_FiveSpecies_Strain_Substitution_Consortium`; it found no
pre-existing duplicate curated record for the same PMID or title.

## Findings

| Severity | Finding | Maintained owner |
|---|---|---|
| Minor | The engineering-design note and knowledge-gap rationale both record that the publisher landing page blocked programmatic text retrieval during curation. That explains this session's evidence boundary, but it is transient access-state prose rather than durable source support and should be rewritten to say the cached PubMed abstract does not expose the ten exact strains or assay conditions while retaining the DOI as the stable Methods route. | `kb/communities/Wine_Yeast_FiveSpecies_Strain_Substitution_Consortium.yaml` |

## Recommended Edits

- Rewrite the two publisher-access sentences in `kb/communities/Wine_Yeast_FiveSpecies_Strain_Substitution_Consortium.yaml` so they focus on the stable abstract-backed uncertainty: exact strain designations, culture-collection accessions, fermentation medium, temperature, and timing are not present in the cached PubMed abstract.
- Regenerate the rendered HTML after editing the maintained YAML.

## Follow-up Checks

- Re-run schema, strict, term-label, reference, snippet-audit, and history validation for the edited record.
- Re-run `communitymech.render --all` and `communitymech.export.browser_export`, then check `git diff --check`.
- Re-read the edited YAML and rendered HTML section to make sure the curation-session access wording is gone.

## Additional Notes

None found.
