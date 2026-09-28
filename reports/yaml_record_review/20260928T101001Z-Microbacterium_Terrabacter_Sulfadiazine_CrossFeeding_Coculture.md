# YAML Record Review: Microbacterium-Terrabacter Sulfadiazine Cross-Feeding Coculture

- Repository: CultureBotAI/CommunityMech
- Record: kb/communities/Microbacterium_Terrabacter_Sulfadiazine_CrossFeeding_Coculture.yaml
- Started UTC: 2026-09-28T10:10:01Z
- Finished UTC: 2026-09-28T10:10:01Z
- Verdict: pass

## Target

- Class: MicrobialCommunity
- ID: CommunityMech:000462
- Label: Microbacterium-Terrabacter Sulfadiazine Cross-Feeding Coculture
- Maintained path: kb/communities/Microbacterium_Terrabacter_Sulfadiazine_CrossFeeding_Coculture.yaml
- Generated page: docs/communities/Microbacterium_Terrabacter_Sulfadiazine_CrossFeeding_Coculture.html
- Primary source: PMID:42598292, DOI 10.1021/acs.estlett.6c00474

The record denotes the two-member in-vitro consortium in Xue et al. 2026: Microbacterium sp. BR1 releases 2-aminopyrimidine from sulfadiazine and Terrabacter DSMZ 28514 uses the released intermediate.

## Validation

| Check | Result |
|---|---|
| `just validate kb/communities/Microbacterium_Terrabacter_Sulfadiazine_CrossFeeding_Coculture.yaml` | Not available locally: `uv run` failed while building `llvmlite==0.46.0` through `umap-learn`. |
| `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python -m linkml.validator.cli -s src/communitymech/schema/communitymech.yaml kb/communities/Microbacterium_Terrabacter_Sulfadiazine_CrossFeeding_Coculture.yaml` | Passed. |
| `PYTHONPATH=src /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/validate_strict.py kb/communities/Microbacterium_Terrabacter_Sulfadiazine_CrossFeeding_Coculture.yaml` | Passed with 0 ERROR rows. |
| `uvx linkml-term-validator validate-data kb/communities/Microbacterium_Terrabacter_Sulfadiazine_CrossFeeding_Coculture.yaml -s src/communitymech/schema/communitymech.yaml --labels` | Passed. |
| `uvx --with 'linkml>=1.9.3' linkml-reference-validator validate data kb/communities/Microbacterium_Terrabacter_Sulfadiazine_CrossFeeding_Coculture.yaml -s src/communitymech/schema/communitymech.yaml --config conf/reference_validator.yaml` | Passed. |
| `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python -m linkml.validator.cli -s src/communitymech/schema/history.yaml -C HistoryRecord history/records/Microbacterium_Terrabacter_Sulfadiazine_CrossFeeding_Coculture/2026-09-28T100001Z-codex-425982.yaml` | Passed. |
| `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/validate_gtdb_coherence.py kb/communities/Microbacterium_Terrabacter_Sulfadiazine_CrossFeeding_Coculture.yaml` | Passed. |
| `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/validate_prokaryotic_lineage.py kb/communities/Microbacterium_Terrabacter_Sulfadiazine_CrossFeeding_Coculture.yaml` | Passed. |
| `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/validate_shared_taxon_ids.py kb/communities/Microbacterium_Terrabacter_Sulfadiazine_CrossFeeding_Coculture.yaml` | Passed. |
| `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/validate_yaml_scalars.py kb/communities/Microbacterium_Terrabacter_Sulfadiazine_CrossFeeding_Coculture.yaml` | Passed. |
| `PYTHONPATH=src /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python -m communitymech.render` | Passed; rendered 452 community pages plus `docs/browser.html` and `docs/index.html`. |
| docs orphan sweep from `just check-docs-current` | Passed. |
| `PYTHONPATH=src /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python -m pytest tests/test_participating_taxa.py::test_the_corpus_is_unchanged_by_this_feature tests/test_community_level_connectivity_credit.py tests/test_published_pages_name_real_records.py -q` | Passed. |
| `PYTHONPATH=src /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python -m pytest tests/test_id_uniqueness.py::test_every_communitymech_id_is_used_exactly_once tests/test_id_uniqueness.py::test_no_id_bearing_records_outside_known_dirs -q` | Passed. |
| `git diff --check` | Passed. |

`tests/test_id_uniqueness.py` as a whole is not available through the fallback environment because `test_isolates_pass_schema_validation` shells out to `uv run linkml-validate` and currently hits the same local `llvmlite` build failure as the `just validate` target.

## Identity and Grounding

The record identity, category, origin, and state agree with the source: this is a defined two-strain synthetic coculture used in isotope-tracing sulfadiazine biodegradation assays.

Ontology labels were checked by `linkml-term-validator` and agree with their CURIEs:

- NCBITaxon:1070896, Microbacterium sp. BR1
- NCBITaxon:1472881, Terrabacter sp. 2APm3
- CHEBI:9328, sulfadiazine
- CHEBI:38618, pyrimidin-2-amine
- ENVO:01001405, laboratory environment
- GO:0044419, biological process involved in interspecies interaction between organisms

The Microbacterium and Terrabacter NCBI taxa are exact strain-level nodes. Both remain `gtdb_grounding_status: UNRESOLVED` because local GTDB grounding could not resolve those informal `sp.` strain taxa to a GTDB species, and the GTDB/domain validators accept the unresolved status.

## Evidence

Every curated evidence snippet in the record matched committed source text from `references_cache/PMID_42598292.txt`.

The source supports the main claims:

- The community contains Microbacterium sp. strain BR1 and Terrabacter.
- 13C,15N-labeled sulfadiazine was used as the sulfadiazine carbon substrate in axenic and coculture assays.
- Microbacterium degraded sulfadiazine with accumulation of 2-aminopyrimidine.
- Terrabacter assimilated 2-aminopyrimidine-derived carbon and nitrogen.
- Coculture coupled the two metabolisms and prevented detectable 2-aminopyrimidine accumulation.

The article identifies the Terrabacter stock as DSMZ 28514. The NCBITaxon grounding uses the exact Terrabacter sp. 2APm3 taxon for that culture.

## Completeness

The record intentionally leaves detailed MVP salts, trace elements, vitamins, and buffer composition unresolved. The article body reports sulfadiazine concentration and points the remaining materials-and-methods details to supporting information, so the record captures sulfadiazine as the curated medium component and carries `exact-mvp-medium-composition` as an open knowledge gap.

iModulonDB cross-checks were not applicable: the record names no genes, locus tags, regulators, transcriptomics datasets, or iModulon-covered strains.

I used a gitignore-independent duplicate search with `rg --hidden --no-ignore` over `kb`, `data`, `history`, `docs`, and `tests` after excluding the new maintained record, its new history entry, and its new generated page. The only remaining matches for the new PMID, DOI, strain-pair, and sulfadiazine terms were the generated `docs/browser.html` entry and the new `tests/test_participating_taxa.py` allowlist row.

## Findings

None open.

### Resolved During Review

- major: `Terrabacter sp. 2APm3` was initially tagged with `PRIMARY_DEGRADER`, which overstated its role because the source reports that the Terrabacter axenic culture did not degrade sulfadiazine. Fixed in `kb/communities/Microbacterium_Terrabacter_Sulfadiazine_CrossFeeding_Coculture.yaml` by leaving Terrabacter as `CROSS_FEEDER` only, then rerunning schema, strict, term, reference, GTDB, lineage, scalar, docs, and focused pytest checks.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate`, `just validate-history`, and `just check-docs-current` once the local `uv` environment can build or avoid `llvmlite==0.46.0`; direct equivalent LinkML, history, render, and docs-orphan checks pass now.
- Cache the ACS supporting information for PMID:42598292 if future curation needs the exact MVP salts, trace elements, vitamins, or buffer composition.

## Additional Notes

`reports/instance_validation_failures.tsv` was rewritten by `scripts/validate_strict.py` during validation and was left at the clean zero-error state produced by the final strict run.
