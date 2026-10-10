# YAML Record Review: Delta nrfA Shewanella-Anammox Nitrite Coupled Consortium

- Repository: CultureBotAI/CommunityMech
- Record: `kb/communities/Shewanella_Anammox_Delta_nrfA_Nitrite_Coupled_Consortium.yaml`
- Started UTC: 20260921T041134Z
- Finished UTC: 20260921T041253Z
- Verdict: pass with minor issues

## Target

| Field | Value |
|---|---|
| Class | `MicrobialCommunity` |
| ID | `CommunityMech:000402` |
| Label | Delta nrfA Shewanella-Anammox Nitrite Coupled Consortium |
| Maintained path | `kb/communities/Shewanella_Anammox_Delta_nrfA_Nitrite_Coupled_Consortium.yaml` |
| Evidence cache | `references_cache/PMID_42655905.txt` |
| Generated products | `docs/communities/Shewanella_Anammox_Delta_nrfA_Nitrite_Coupled_Consortium.html`, `docs/browser.html`, `docs/index.html` |
| Repository history | `history/records/Shewanella_Anammox_Delta_nrfA_Nitrite_Coupled_Consortium/2026-09-21T041028Z-claude-code-f07416.yaml` |

This is a maintained curated community record, not a generated import. It denotes the optimized engineered Delta-B1 anaerobic batch culture from Yi et al. 2026: activated anammox sludge plus an nrfA-deficient `S. oneidensis` MR-1 mutant in nitrate/ammonium/lactate mixed medium.

The same source was not already curated when searched by PMID, DOI, PMCID, title phrase, and slug with `rg -n -uu --hidden` over the repository, including ignored and hidden files while excluding generated/cache-heavy directories (`references_cache/files/**`, `docs/**`, `pages/**`, `output/**`, `.venv/**`, `.pytest_cache/**`). The only pre-curation hits were scout/report leads, not a canonical YAML record or committed PMID cache.

## Validation

| Check | Result |
|---|---|
| `env PYTHONPATH=src .venv/bin/linkml-validate --schema src/communitymech/schema/communitymech.yaml --target-class MicrobialCommunity kb/communities/Shewanella_Anammox_Delta_nrfA_Nitrite_Coupled_Consortium.yaml` | Pass: no issues found |
| `env PYTHONPATH=src .venv/bin/python scripts/validate_strict.py kb/communities/Shewanella_Anammox_Delta_nrfA_Nitrite_Coupled_Consortium.yaml` | Pass: 1 file scanned, 0 ERROR rows |
| `env PYTHONPATH=src .venv/bin/linkml-term-validator validate-data kb/communities/Shewanella_Anammox_Delta_nrfA_Nitrite_Coupled_Consortium.yaml -s src/communitymech/schema/communitymech.yaml --labels` | Pass |
| `.venv/bin/linkml-reference-validator validate data kb/communities/Shewanella_Anammox_Delta_nrfA_Nitrite_Coupled_Consortium.yaml -s src/communitymech/schema/communitymech.yaml --config conf/reference_validator.yaml` | Pass |
| `env PYTHONPATH=src .venv/bin/python scripts/evidence_snippet_audit.py kb/communities/Shewanella_Anammox_Delta_nrfA_Nitrite_Coupled_Consortium.yaml` | Pass: 37 MATCH, 0 RENDERING, 0 WEAK, 0 MISMATCH, 0 NOCONTENT |
| `env PYTHONPATH=src .venv/bin/python scripts/validate_gtdb_coherence.py kb/communities/Shewanella_Anammox_Delta_nrfA_Nitrite_Coupled_Consortium.yaml` | Pass: 1 file, 0 incoherent blocks, 0 malformed lineages, 0 lineage conflicts |
| `env PYTHONPATH=src .venv/bin/python scripts/validate_yaml_scalars.py kb/communities/Shewanella_Anammox_Delta_nrfA_Nitrite_Coupled_Consortium.yaml` | Pass: 1 file, 0 truncated scalars |
| `env PYTHONPATH=src .venv/bin/python scripts/validate_shared_taxon_ids.py kb/communities/Shewanella_Anammox_Delta_nrfA_Nitrite_Coupled_Consortium.yaml` | Pass: 1 file, 0 reused ids |
| `env PYTHONPATH=src .venv/bin/python scripts/validate_prokaryotic_lineage.py kb/communities/Shewanella_Anammox_Delta_nrfA_Nitrite_Coupled_Consortium.yaml` | Pass: 1 file, 0 contradictory lineages |
| `env PYTHONPATH=src .venv/bin/python scripts/validate_cross_repo_ids.py kb/communities/Shewanella_Anammox_Delta_nrfA_Nitrite_Coupled_Consortium.yaml` | Pass |
| `env PYTHONPATH=src .venv/bin/linkml-validate --schema src/communitymech/schema/history.yaml --target-class HistoryRecord history/records/Shewanella_Anammox_Delta_nrfA_Nitrite_Coupled_Consortium/2026-09-21T041028Z-claude-code-f07416.yaml` | Pass |
| `env PYTHONPATH=src .venv/bin/python scripts/audit_writers.py` | Pass |
| `env PYTHONPATH=src .venv/bin/python scripts/validate_strict.py kb/communities data/isolates` | Pass: 396 files scanned, 0 ERROR rows |
| `env PYTHONPATH=src .venv/bin/python scripts/validate_gtdb_coherence.py kb/communities/*.yaml data/isolates/*.yaml` | Pass: 396 files, 0 incoherent blocks, 0 malformed lineages, 0 lineage conflicts |
| `env PYTHONPATH=src .venv/bin/python scripts/validate_yaml_scalars.py kb/communities data/isolates kb/taxa` | Pass: 398 files, 0 truncated scalars |
| `env PYTHONPATH=src .venv/bin/python scripts/validate_yaml_scalars.py --idiomatic` | Pass: 157 files, 0 truncated scalars |
| `env PYTHONPATH=src .venv/bin/python -m communitymech.render` | Pass: rendered 392 communities and regenerated browser/landing pages |
| `git diff --check` | Pass |
| `.venv/bin/pytest tests/ -v` | Not checked to completion: local test collection is missing optional dependencies `umap` and `dotenv` |
| `.venv/bin/black --check src/ tests/ scripts/`; `.venv/bin/ruff check src/ tests/ scripts/`; `.venv/bin/mypy src/` | Not checked: the local `.venv` does not contain `black`, `ruff`, or `mypy` |
| `uv run black --check src/ tests/ scripts/`; `uv run ruff check src/ tests/ scripts/` | Not checked to completion: `uv` tries to build `llvmlite==0.46.0` through `umap-learn` and fails under Python 3.13 before running the tool |

## Identity and Grounding

The record identity is sound. The YAML describes a single engineered lab consortium and keeps the experimental scope bounded to the Delta nrfA Shewanella/anammox-sludge batch assays instead of upgrading the result into a natural wastewater-plant community.

The main member groundings agree with the source and with existing reusable repository choices:

| Member | Grounding judgement |
|---|---|
| Delta nrfA `Shewanella oneidensis` MR-1 | Correctly represented as `NCBITaxon:211586` with the knockout genotype in `strain_designation`; the mutant itself does not need a fabricated NCBITaxon identifier |
| `Candidatus Brocadia` anammox bacteria | Conservatively grounded at `NCBITaxon:203682` Planctomycetota; the paper reports `Candidatus Brocadia` as the only detected anammox genus in these Delta controls and Delta-B groups, but does not provide a species-complete isolate inventory |
| Endogenous activated-sludge heterotrophic bacteria | Correctly kept as a broad bacterial guild because the study profiled a sludge-derived metagenome rather than isolate-resolving every non-anammox member |

`ENVO:01001405` laboratory environment is acceptable for the curated batch-culture state. `ENVO:00002043` wastewater treatment plant is acceptable as a modeled/source setting because the seed anammox sludge was collected from a municipal wastewater treatment process and the assay was explicitly motivated by nitrate-laden wastewater nitrogen removal.

## Evidence

Most evidence is placed at the narrow claim it supports: Shewanella mutant identity under the Shewanella member, Brocadia metagenomic enrichment under the Planctomycetota/Brocadia member and interaction, the Delta-B1 bottle ratio under the inoculation-ratio factor, medium composition under `growth_media`, and continuous-reactor/isotope limitations under the open discussion.

All 37 snippets in the new record match committed source text exactly. The full-text cache contains Methods, Results, Conclusion, and Perspective sections sufficient to support the curated cultivation setup, nitrate/ammonium/lactate medium, final-time-point metagenomics, Brocadia enrichment, and future-work gaps.

One claim needs to be moved for semantic fit rather than evidence support: the `Final-time-point metagenomic taxonomic assignment` object records a sequencing/annotation method in `environmental_factors`, whose schema definition is an environmental condition or parameter. That information belongs with the metagenomic measurement endpoint, not in the environmental-condition list.

One claim needs a narrower local citation: the broad endogenous-sludge bacterial member notes mention both Pseudomonadota and Bacteroidota in Delta treatments, but its only evidence item cites the Pseudomonadota abundance shift. The source also supports Bacteroidota as an additional non-anammox phylum, so this is fixable by adding an adjacent exact snippet.

## Completeness

The record is complete enough for a first PR:

- It captures the optimized Delta-B1 assembly, the 5:1 anammox-sludge-to-mutant ratio, 500 mL anaerobic bottle setup, medium formula, pH, nitrogen purge, final-time-point metagenomic endpoint, and source-derived uncertainty about direct flux attribution.
- It leaves `metals_present` and `rare_earth_elements_present` empty with `metal_relevance: NOT_APPLICABLE`, which is correct for a nitrate-removal study with no curated metal or rare-earth mechanism.
- It leaves `associated_datasets` empty. The inspected open-access body sections do not provide a public accession for the metagenomic reads, while `external_resources` records the stable PMID and DOI.
- It uses one open discussion for the real unresolved mechanism gap: isotope-resolved nitrate/nitrite/ammonium flux and long-term continuous-reactor stability.

The committed `references_cache/PMID_42655905.txt` has one provenance gap: it records the DOI and title but leaves the `PMCID:` header blank even though the full-text support was selected from `PMC13519132`.

## Findings

| Severity | Finding | Owner |
|---|---|---|
| blocker | None found | n/a |
| major | None found | n/a |
| minor | Move final-time-point metagenomic taxonomic assignment out of `environmental_factors`; it is a sequencing endpoint, not an environmental condition. | `kb/communities/Shewanella_Anammox_Delta_nrfA_Nitrite_Coupled_Consortium.yaml` |
| minor | Add evidence for the Bacteroidota part of the endogenous activated-sludge heterotroph note, or narrow the note to the cited Pseudomonadota result. | `kb/communities/Shewanella_Anammox_Delta_nrfA_Nitrite_Coupled_Consortium.yaml` |
| minor | Fill the blank `PMCID:` header in the committed PMID cache with `PMC13519132`. | `references_cache/PMID_42655905.txt` |

## Recommended Edits

1. In `kb/communities/Shewanella_Anammox_Delta_nrfA_Nitrite_Coupled_Consortium.yaml`, delete the `environmental_factors` item named `Final-time-point metagenomic taxonomic assignment`, preserve the useful DIAMOND/Micro_NR/final-time-point details in `engineering_design.measurement_endpoints` and `engineering_design.evidence`, and append a `FIX_ADVERSARIAL_REVIEW_FINDINGS` curation event.
2. In `kb/communities/Shewanella_Anammox_Delta_nrfA_Nitrite_Coupled_Consortium.yaml`, add exact source evidence for Bacteroidota as part of the broad endogenous activated-sludge bacteria member or narrow that member's notes.
3. In `references_cache/PMID_42655905.txt`, set `PMCID: PMC13519132`.
4. Regenerate `docs/` after the YAML change so the generated community page and browser card reflect the corrected record.
5. Add a second append-only history record for the review fixes.

## Follow-up Checks

Run the narrow record validators again:

- `linkml-validate` with `MicrobialCommunity`
- `scripts/validate_strict.py` on the new YAML
- `linkml-term-validator validate-data --labels`
- `linkml-reference-validator validate data`
- `scripts/evidence_snippet_audit.py`
- `scripts/validate_gtdb_coherence.py`
- `scripts/validate_shared_taxon_ids.py`
- `scripts/validate_prokaryotic_lineage.py`
- `scripts/validate_cross_repo_ids.py`
- history validation for the second append-only history YAML
- `scripts/validate_yaml_scalars.py` on the touched YAML and then the record trees
- `scripts/audit_writers.py`
- `python -m communitymech.render`
- `git diff --check`

## Additional Notes

`just`/`uv run` cannot currently run local lint in this checkout because `uv` tries to build `llvmlite==0.46.0` through the optional `umap-learn` dependency and dies with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'` under Python 3.13. The available `.venv` is still sufficient for the LinkML, reference, snippet, strict, scalar, GTDB, cross-repo, and render commands used above.
