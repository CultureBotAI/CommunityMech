# YAML Record Review: Wheat Crown-Rot Six-Strain Cross-Kingdom SMC

- Repository: CultureBotAI/CommunityMech
- Record: kb/communities/Wheat_CrownRot_SixStrain_CrossKingdom_SMC.yaml
- Started UTC: 2026-09-22T00:32:34Z
- Finished UTC: 2026-09-22T00:32:54Z
- Verdict: pass with minor issues

## Target

| Field | Value |
|---|---|
| Class | `MicrobialCommunity` |
| ID | `CommunityMech:000414` |
| Label | Wheat Crown-Rot Six-Strain Cross-Kingdom SMC |
| Maintained path | `kb/communities/Wheat_CrownRot_SixStrain_CrossKingdom_SMC.yaml` |
| Generated status | Maintained YAML with generated HTML at `docs/communities/Wheat_CrownRot_SixStrain_CrossKingdom_SMC.html` |
| Primary reference | `PMID:41504167`; DOI `10.1021/acs.jafc.5c11786`; PMCID `PMC12833866` |

The target is a six-member synthetic microbial community made from `Trichoderma harzianum` T19 plus five `Bacillus` strains. It is distinct from the existing two-member TB wheat crown-rot SynCom in `kb/communities/Wheat_CrownRot_TB_CrossKingdom_SynCom.yaml`, which is based on PMID:41821943 and contains only T19 plus `Bacillus rugosus` PM16.

## Validation

| Check | Result |
|---|---|
| `.venv/bin/linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Wheat_CrownRot_SixStrain_CrossKingdom_SMC.yaml` | Pass |
| `env PYTHONPATH=src .venv/bin/python scripts/validate_strict.py kb/communities/Wheat_CrownRot_SixStrain_CrossKingdom_SMC.yaml` | Pass: 1 file, 0 error rows |
| `.venv/bin/linkml-term-validator validate-data kb/communities/Wheat_CrownRot_SixStrain_CrossKingdom_SMC.yaml -s src/communitymech/schema/communitymech.yaml --labels` | Pass |
| `.venv/bin/linkml-reference-validator validate data kb/communities/Wheat_CrownRot_SixStrain_CrossKingdom_SMC.yaml -s src/communitymech/schema/communitymech.yaml --config conf/reference_validator.yaml` | Pass |
| `env PYTHONPATH=src .venv/bin/python scripts/evidence_snippet_audit.py kb/communities/Wheat_CrownRot_SixStrain_CrossKingdom_SMC.yaml` | Pass: 28 `MATCH`, 0 `RENDERING`, 0 `ASSEMBLED`, 0 `WEAK`, 0 `MISMATCH`, 0 `NOCONTENT` |
| `env PYTHONPATH=src .venv/bin/python scripts/validate_gtdb_coherence.py kb/communities/Wheat_CrownRot_SixStrain_CrossKingdom_SMC.yaml` | Pass |
| `env PYTHONPATH=src .venv/bin/python scripts/validate_prokaryotic_lineage.py kb/communities/Wheat_CrownRot_SixStrain_CrossKingdom_SMC.yaml` | Pass |
| `env PYTHONPATH=src .venv/bin/python scripts/validate_yaml_scalars.py kb/communities/Wheat_CrownRot_SixStrain_CrossKingdom_SMC.yaml` | Pass |
| `.venv/bin/linkml-validate --schema src/communitymech/schema/history.yaml --target-class HistoryRecord history/records/Wheat_CrownRot_SixStrain_CrossKingdom_SMC/2026-09-22T002234Z-claude-code-d64ca7.yaml` | Pass |
| `env PYTHONPATH=src .venv/bin/python scripts/validate_strict.py` | Pass: 408 files, 0 error rows |
| `env PYTHONPATH=src .venv/bin/python scripts/validate_gtdb_coherence.py kb/communities/*.yaml data/isolates/*.yaml` | Pass: 408 files |
| `env PYTHONPATH=src .venv/bin/python scripts/validate_prokaryotic_lineage.py kb/communities/*.yaml data/isolates/*.yaml` | Pass: 408 files |
| `env PYTHONPATH=src .venv/bin/python scripts/validate_yaml_scalars.py kb/communities/*.yaml data/isolates/*.yaml` | Pass: 408 files |
| `env PYTHONPATH=src .venv/bin/python scripts/validate_shared_taxon_ids.py kb/communities/*.yaml data/isolates/*.yaml` | Pass: 408 files, 0 reused IDs |
| `env PYTHONPATH=src:scripts .venv/bin/python -m pytest tests/test_participating_taxa.py -v` | Pass: 9 tests |
| `git diff --check` | Pass |

Unavailable or partially unavailable checks:

- `just new-history` and `just validate-history` could not run through their `uv run` wrappers because `uv` attempted to build `llvmlite==0.46.0` on the local Python 3.13 environment and failed before the repository commands started. The same shared history scaffolder and LinkML history validator were run directly through `.venv`.
- A full direct `pytest tests/ -v` collection could not run in the partial `.venv` because `communitymech` was not installed on `PYTHONPATH` and optional test dependencies such as `umap` and `dotenv` were absent.
- A focused 557-test pytest subset run with `PYTHONPATH=src:scripts` had 553 passes. Three failures were in tests that shell out to `uv run` and hit `/Users/marcin/.cache/uv/sdists-v9/.git: Operation not permitted`; one pre-existing isolate schema test also shells out to `uv`. The direct 408-file strict/schema gates above cover the new record and the isolate root without those local `uv` failures.
- `.venv` does not include `black` or `ruff`, so local lint could not be run without invoking `uv`.

## Identity and Grounding

The identity is sound: the record denotes the 2026 Journal of Agricultural and Food Chemistry cross-kingdom SMC containing `T. harzianum` T19 and five `Bacillus` strains, not the separate 2026 Frontiers two-member TB SynCom.

An ignored-file-inclusive duplicate search across `kb`, `data`, `history`, `docs`, `references_cache`, `reports`, and `research` for `41504167`, `10.1021/acs.jafc.5c11786`, `Wheat_CrownRot_SixStrain_CrossKingdom_SMC`, and `CommunityMech:000414` found only the new record, the new generated page/cache/history paths, and scouting rows for the same candidate. It did not find a pre-existing canonical record using the PMID, DOI, or internal ID.

NCBI identity checks resolved the member species as:

| Strain | NCBITaxon |
|---|---|
| `Trichoderma harzianum` T19 | `NCBITaxon:5544` |
| `Bacillus subtilis` BS-Z15 | `NCBITaxon:1423` |
| `Bacillus spizizenii` PM9 | `NCBITaxon:96241` |
| `Bacillus rugosus` PM16 | `NCBITaxon:2715209` |
| `Bacillus rugosus` S32 | `NCBITaxon:2715209` |
| `Bacillus halotolerans` S8 | `NCBITaxon:260554` |

The fungal T19 member is correctly marked `NO_GTDB_EQUIVALENT`. `Bacillus subtilis` reuses a corpus GTDB species grounding. The remaining `Bacillus` entries are explicitly `UNRESOLVED` because the local kg-microbe `NCBI2GTDB.tsv.gz` file was not present in any expected checkout location during curation.

## Evidence

The source snippets are exact, cache-backed substrings from `references_cache/PMID_41504167.txt`, which was created from the Europe PMC full-text XML for `PMC12833866`.

Supported claims:

- The methods section identifies the six exact SMC strains, their species-level molecular IDs, and CCTCC deposits.
- The methods section states that the five bacterial nutrient-broth suspensions and the T19 spore suspension were mixed in equal volumes to produce the SMC.
- The results section supports the design grouping of T19/BS-Z15 as antagonists, PM9/PM16 as growth-promoting strains, and S8/S32 as auxiliary strains.
- The pot-assay evidence supports nonsterile soil, 25 °C, 16 h light / 8 h dark, CK/Fp/SMC/SMC+Fp arms, and delayed SMC inoculation after the Fp challenge.
- The disease-suppression evidence supports a 70.01% disease-severity reduction relative to Fp alone.
- The rhizosphere-remodeling evidence supports fungal and bacterial community shifts but not a pairwise interaction among introduced strains.

Unsupported or over-scoped claims:

- None found.

## Completeness

The record covers the consequential membership, source identity, culture conditions, pot-assay setup, FCR suppression, and resident-rhizosphere remodeling claims. It deliberately leaves genome accessions, associated datasets, and exact GTDB blocks for four non-`B. subtilis` members empty rather than inferring data from outside the inspected source or from an unavailable GTDB map.

Empty optional slots correctly left empty:

- `associated_datasets`: the inspected text did not expose stable NCBI/MetaboLights accession IDs analogous to the two-member TB record.
- `environmental_factors`: the soil properties and enzyme activities are outcomes, not fixed conditions required to define the SMC.
- `discussions`: no source conflict or bounded curation uncertainty needed a record-level discussion beyond the explicit GTDB notes.

## Findings

| Severity | Finding | Maintained owner |
|---|---|---|
| Minor | `ecological_interactions[0].participating_taxa` lists all six community members on a `COMMUNITY_LEVEL` edge. That slot is useful when a community-level claim applies to only some members; an omitted slot already means every member participates, and the `Fusarium pseudograminearum` target is already named in the interaction text as an outside-community pathogen. | `kb/communities/Wheat_CrownRot_SixStrain_CrossKingdom_SMC.yaml` |

## Recommended Edits

- Remove `participating_taxa` from `Six-strain SMC suppression of Fusarium crown rot`; the edge genuinely applies to the whole six-member SMC, so the default all-member interpretation is clearer. Because this makes the new record stop using `participating_taxa`, also remove `Wheat_CrownRot_SixStrain_CrossKingdom_SMC.yaml` from `USERS` in `tests/test_participating_taxa.py`.

## Follow-up Checks

- Re-run `env PYTHONPATH=src .venv/bin/python scripts/validate_strict.py kb/communities/Wheat_CrownRot_SixStrain_CrossKingdom_SMC.yaml`.
- Re-run `env PYTHONPATH=src:scripts .venv/bin/python -m pytest tests/test_participating_taxa.py -v`.
- Re-run `env PYTHONPATH=src .venv/bin/python -m communitymech.render` and check for zero generated-page orphans.
- Re-run `git diff --check`.

## Additional Notes

- The ordinary `rg` result that first surfaced `Wheat_CrownRot_TB_CrossKingdom_SynCom.yaml` would have been an unsafe duplicate conclusion on its own. The later ignored-file-inclusive searches separated the new PMID/DOI from the Frontiers PMID:41821943 TB sibling.
- The ACS supplementary PDF was not accessible locally: direct ACS and PMC static PDF downloads returned HTML denial pages. The main full text was sufficient for all retained claims.
