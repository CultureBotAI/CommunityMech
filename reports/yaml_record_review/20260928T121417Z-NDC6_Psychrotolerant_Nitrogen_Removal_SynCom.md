# YAML Record Review: NDC-6 Psychrotolerant Nitrogen Removal SynCom

- Repository: CultureBotAI/CommunityMech
- Record: kb/communities/NDC6_Psychrotolerant_Nitrogen_Removal_SynCom.yaml
- Started UTC: 2026-09-28T11:57:52Z
- Finished UTC: 2026-09-28T12:14:17Z
- Verdict: pass

## Target

- Class: MicrobialCommunity
- ID: CommunityMech:000463
- Label: NDC-6 Psychrotolerant Nitrogen Removal SynCom
- Maintained path: kb/communities/NDC6_Psychrotolerant_Nitrogen_Removal_SynCom.yaml
- Generated page: docs/communities/NDC6_Psychrotolerant_Nitrogen_Removal_SynCom.html
- Primary source: PMID:41504900, DOI 10.1007/s00449-025-03276-5

The record denotes the six-strain, low-temperature NDC-6 composite microbial agent in
Dong et al. 2026, assembled by coculturing psychrotolerant nitrifying consortium NC1 with
aerobic-denitrifying consortium DC1 at a 1:1 inoculation ratio.

## Validation

| Check | Result |
|---|---|
| `just validate`, `just validate-strict`, `just validate-references-explained`, `just check-docs-current` | Not available locally: the normal `uv run` path failed while trying to build `llvmlite==0.46.0` before repository code loaded. |
| `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/NDC6_Psychrotolerant_Nitrogen_Removal_SynCom.yaml` | Passed. |
| `PYTHONPATH=src /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/validate_strict.py kb/communities/NDC6_Psychrotolerant_Nitrogen_Removal_SynCom.yaml` | Passed with 0 ERROR rows. |
| `uvx --from linkml-reference-validator --with linkml --with linkml-runtime linkml-reference-validator validate data kb/communities/NDC6_Psychrotolerant_Nitrogen_Removal_SynCom.yaml -s src/communitymech/schema/communitymech.yaml --config conf/reference_validator.yaml` | Passed. |
| `uvx --from linkml-term-validator --with linkml --with oaklib linkml-term-validator validate-data kb/communities/NDC6_Psychrotolerant_Nitrogen_Removal_SynCom.yaml -s src/communitymech/schema/communitymech.yaml --labels` | Passed. |
| `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/linkml-validate --schema src/communitymech/schema/history.yaml --target-class HistoryRecord history/records/NDC6_Psychrotolerant_Nitrogen_Removal_SynCom/2026-09-28T115752Z-claude-code-798764.yaml history/records/NDC6_Psychrotolerant_Nitrogen_Removal_SynCom/2026-09-28T120834Z-codex-e36987.yaml` | Passed. |
| `PYTHONPATH=src /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/validate_gtdb_coherence.py kb/communities/NDC6_Psychrotolerant_Nitrogen_Removal_SynCom.yaml` | Passed. |
| `PYTHONPATH=src /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/validate_prokaryotic_lineage.py kb/communities/NDC6_Psychrotolerant_Nitrogen_Removal_SynCom.yaml` | Passed. |
| `PYTHONPATH=src /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/validate_yaml_scalars.py kb/communities/NDC6_Psychrotolerant_Nitrogen_Removal_SynCom.yaml` | Passed. |
| `PYTHONPATH=src /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/validate_shared_taxon_ids.py kb/communities/NDC6_Psychrotolerant_Nitrogen_Removal_SynCom.yaml` | Passed. |
| `PYTHONPATH=src /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/audit_writers.py` | Passed and rewrote `reports/pipeline_writers_audit.tsv` without changing it. |
| `PYTHONPATH=src /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python -m communitymech.render` | Passed; rendered 453 community pages plus `docs/browser.html` and `docs/index.html`. |
| docs orphan sweep equivalent to `just check-docs-current` | Passed with `pages=453 records=453 orphan_pages=0 missing_pages=0`. |
| `PYTHONPATH=src /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python -m pytest tests/test_published_pages_name_real_records.py tests/test_docs_do_not_contradict_the_kb.py -q` | Passed, 914 assertions. |
| Larger focused pytest shard over ID uniqueness, YAML-key, docs, scalar, lineage, and shared-taxon tests | Partially passed: 1,570 assertions passed and 6 failed only where tests shell out to `uv run`, which hit the same sandboxed uv cache / environment problem. |
| `git diff --check` | Passed. |

## Identity and Grounding

The record identity, category, origin, and state agree with PMID:41504900: this is a defined
six-strain synthetic consortium assembled for low-temperature nitrogen removal.

Ontology labels were checked by `linkml-term-validator` and agree with their CURIEs:

- NCBITaxon:76761, Pseudomonas veronii
- NCBITaxon:200451, Pseudomonas poae
- NCBITaxon:592361, Pseudomonas peli
- NCBITaxon:642, Aeromonas
- NCBITaxon:359110, Pseudomonas extremaustralis
- NCBITaxon:614, Serratia liquefaciens
- ENVO:01001405, laboratory environment
- ENVO:00002001, waste water
- CHEBI:28938, ammonium
- CHEBI:17632, nitrate
- GO:0019329, ammonia oxidation
- GO:0019333, denitrification pathway

The five species-level members and one `Aeromonas sp.` genus-level member preserve the names
available in the PubMed abstract. GTDB grounding remains `UNRESOLVED` because no local
NCBI-to-GTDB crosswalk was available during first-pass curation; the record carries explicit
notes on each member and the GTDB/domain validators accept the unresolved status.

## Evidence

Every curated evidence snippet in the record matched committed source text from
`references_cache/PMID_41504900.txt`.

The abstract supports the main claims:

- NDC-6 combines NC1, containing P. veronii HN1, P. poae HN2, and P. peli HN3, with DC1, containing Aeromonas sp. AD1, P. extremaustralis AD2, and S. liquefaciens AD3, at a 1:1 inoculation ratio.
- NDC-6 achieved 89.3% NH4+-N, 88.1% NO3--N, 85.5% total nitrogen, and 95.3% chemical oxygen demand removal after three days at 10 C.
- Sodium succinate was the optimal carbon source in the tested setup.
- Response-surface methodology found an optimum C/N ratio of 6, temperature of 10.2 C, pH of 7.2, and shaking speed of 156 rpm.
- Functional-gene expression of hao, napA, nirS, nirK, cnorB, and nosZ supports aerobic, low-temperature nitrogen removal through assimilation and dissimilation, with NC1/DC1 synergy and functional complementation.

## Completeness

The record intentionally leaves detailed methods as a bounded knowledge gap. The PubMed abstract
names the six strains, the NC1/DC1 module design, the 1:1 inoculation ratio, sodium succinate,
and the response-surface optimum, but not the full salts formulation, nitrogen concentrations,
strain isolation histories, optimized-assay duration, vessel geometry, or compatibility protocol.

iModulonDB cross-checks were not applicable: the record names functional genes but no
iModulon-covered organism, strain, or transcriptomics dataset keys.

Before creation, a gitignore-independent duplicate search with `rg --hidden --no-ignore` over
`kb`, `data`, `history`, `docs`, `references_cache`, and `research` found PMID:41504900 only in
`research/scouting/stubs/development-of-a-psychrotolerant-composi.stub.yaml`, not in the
maintained KB, reference cache, docs, or history.

## Findings

None open.

### Resolved During Review

- major: The draft set the NC1/DC1 community-level functional-complementation entry to `interaction_type: MUTUALISM`, but PMID:41504900 supports synergistic metabolism between the modules rather than a six-strain +/+ ecological interaction. Tracked as CommunityMech#1197 and fixed in `kb/communities/NDC6_Psychrotolerant_Nitrogen_Removal_SynCom.yaml` by removing the over-specific enum and preserving the source-supported `COMMUNITY_LEVEL` interaction.
- major: The draft combined the three-day 10 C performance assay with the response-surface optimum in one `growth_media` entry and made `incubation_time: 3 days` look like part of the 10.2 C optimized condition. Tracked as CommunityMech#1198 and fixed in `kb/communities/NDC6_Psychrotolerant_Nitrogen_Removal_SynCom.yaml` by removing the optimized-assay duration and expanding the open methods gap.
- minor: The draft duplicated sodium succinate under `related_ingredients` even though that slot complements `growth_media.composition` for environmentally or metabolically relevant compounds outside actual media. Tracked as CommunityMech#1198 and fixed in `kb/communities/NDC6_Psychrotolerant_Nitrogen_Removal_SynCom.yaml` by keeping sodium succinate only as a curated medium component.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate`, `just validate-strict`, `just validate-references-explained`, and `just check-docs-current` once the normal local `uv` environment can build or avoid the current `llvmlite==0.46.0` failure; direct equivalent gates pass now.
- Resolve the exact optimized medium salts, nitrogen concentrations, assay duration, and vessel geometry if the Springer version of record or supplementary materials become accessible.
- Re-run GTDB grounding when a local NCBI-to-GTDB crosswalk or equivalent mapping source is available for the six NDC-6 strains.

## Additional Notes

`runoak` was not installed on this checkout's PATH, so sodium-succinate CHEBI lookup through OLS
was not available. The final record does not require that lookup because sodium succinate is
represented as an ungrounded `GrowthMediaComponent`, while the nitrogen analytes are grounded as
`RelatedIngredient` entries.
