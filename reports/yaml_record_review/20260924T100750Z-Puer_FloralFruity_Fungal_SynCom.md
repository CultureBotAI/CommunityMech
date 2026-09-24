# YAML Record Review: Pu'er Floral-Fruity Fungal SynCom

- Repository: CultureBotAI/CommunityMech
- Record: kb/communities/Puer_FloralFruity_Fungal_SynCom.yaml
- Started UTC: 2026-09-24T10:07:50Z
- Finished UTC: 2026-09-24T10:08:00Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `kb/communities/Puer_FloralFruity_Fungal_SynCom.yaml` |
| Class | `MicrobialCommunity` |
| ID | `CommunityMech:000430` |
| Label | Pu'er Floral-Fruity Fungal SynCom |
| Maintained/generated | Maintained curated YAML |

## Validation

| Check | Result |
|---|---|
| `.venv/bin/linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Puer_FloralFruity_Fungal_SynCom.yaml` | Pass |
| `PYTHONPATH=src .venv/bin/python scripts/validate_strict.py kb/communities/Puer_FloralFruity_Fungal_SynCom.yaml` | Pass |
| `PYTHONPATH=src .venv/bin/python scripts/validate_gtdb_coherence.py kb/communities/Puer_FloralFruity_Fungal_SynCom.yaml` | Pass |
| `PYTHONPATH=src .venv/bin/python scripts/validate_yaml_scalars.py kb/communities/Puer_FloralFruity_Fungal_SynCom.yaml` | Pass |
| `.venv/bin/linkml-term-validator validate-data kb/communities/Puer_FloralFruity_Fungal_SynCom.yaml -s src/communitymech/schema/communitymech.yaml --labels` | Pass |
| `.venv/bin/linkml-reference-validator validate data kb/communities/Puer_FloralFruity_Fungal_SynCom.yaml -s src/communitymech/schema/communitymech.yaml --config conf/reference_validator.yaml` | Pass |
| `.venv/bin/linkml-validate --schema src/communitymech/schema/history.yaml --target-class HistoryRecord history/records/Puer_FloralFruity_Fungal_SynCom/2026-09-24T100425Z-codex-5b4411.yaml` | Pass |
| `PYTHONPATH=src .venv/bin/python -m communitymech.render` | Pass; rendered 420 community pages and regenerated `docs/browser.html` and `docs/index.html` |
| `git diff --cached --check` | Pass after trimming trailing whitespace in `references_cache/PMID_42331835.txt` |
| `just qc` | Not checked: local `uv` currently attempts to build `llvmlite==0.46.0` under Python 3.13, so the focused `.venv` validators were used directly. |

## Identity and Grounding

The record identity is sound: it denotes the patented synthetic fungal starter that Yan et al. used to inoculate ripe Pu'er tea, not the whole spontaneous Pu'er pile community or the later metagenomic succession.

The three member taxa are present at the species level named by the article. `Saccharomyces cerevisiae` (`NCBITaxon:4932`) and `Aspergillus niger` (`NCBITaxon:5061`) reuse labels already accepted elsewhere in the corpus; `Rhizopus arrhizus` resolves to `NCBITaxon:64495` in NCBI Taxonomy. All three are fungi, so `NO_GTDB_EQUIVALENT` is the appropriate GTDB status.

The `ENVO:03600040` / `fermentation starter` grounding matches the neighboring fermented-food SynCom pattern and is semantically acceptable for the inoculum.

## Evidence

The PMID cache contains the PubMed abstract plus inspected open-access full text for DOI `10.1038/s41538-026-00945-x`.

Supported:

- Starter membership and 2:1:2 weight ratio are supported by the Introduction and Methods.
- Patent identifiers in taxon notes match the Methods text and are not over-modeled as culture-collection accessions.
- 0.1% starter inoculation, 30% water addition, 1 m covered piles, and ambient solid-state fermentation are supported by Methods.
- The floral-fruity aroma outcome and volatile/metagenomic readouts are supported by the abstract and Results.
- The PubMed and DOI resources point to the primary publication.

Unsupported or over-scoped:

- The `Fungal succession after Pu'er starter inoculation` interaction is a metagenomic readout from the inoculated pile community, not an ecological interaction among the three starter members.

## Completeness

The record intentionally leaves strain designations unresolved because the article reports patent identifiers rather than formal strain names or culture-collection accessions. The open discussion `puer_fungal_patented_starter_accessions` records this concrete gap.

A hidden and ignored duplicate search over maintained YAML, history, reports, docs, and the reference cache found no pre-existing canonical `CommunityMech:000430` record and no canonical record for PMID:42331835 before this branch.

No metal, rare-earth, dataset, or external protocol claim is needed for the inspected source.

## Findings

| Severity | Finding | Maintained owner |
|---|---|---|
| Major | `ecological_interactions#Fungal succession after Pu'er starter inoculation` turns a whole-pile metagenomic succession into a CommunityMech interaction. With no `participating_taxa`, a `COMMUNITY_LEVEL` edge is credited to all three starter members, but the cited text only says Aspergillus predominated on day 7 and Rasamsonia dominated on days 14-21. Rasamsonia is not one of the inoculated starter taxa. | `kb/communities/Puer_FloralFruity_Fungal_SynCom.yaml` |

No blockers found.

No minor issues found.

## Recommended Edits

1. Remove `ecological_interactions#Fungal succession after Pu'er starter inoculation` from `kb/communities/Puer_FloralFruity_Fungal_SynCom.yaml`.
2. Preserve the metagenomic succession as a measured endpoint and, if needed, prose in `engineering_design.notes` so the supported readout remains visible without entering the starter-member interaction graph.
3. Regenerate `docs/`, append curation history, rerun focused schema, term, reference, history, and docs-current checks.

## Follow-up Checks

- `.venv/bin/linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Puer_FloralFruity_Fungal_SynCom.yaml`
- `PYTHONPATH=src .venv/bin/python scripts/validate_strict.py kb/communities/Puer_FloralFruity_Fungal_SynCom.yaml`
- `.venv/bin/linkml-reference-validator validate data kb/communities/Puer_FloralFruity_Fungal_SynCom.yaml -s src/communitymech/schema/communitymech.yaml --config conf/reference_validator.yaml`
- `.venv/bin/linkml-validate --schema src/communitymech/schema/history.yaml --target-class HistoryRecord <new-history-record>`
- `PYTHONPATH=src .venv/bin/python -m communitymech.render`
- `git diff --check`

## Additional Notes

The generated page `docs/communities/Puer_FloralFruity_Fungal_SynCom.html` renders `CommunityMech:000430`, the three fungal taxa, and the over-scoped succession interaction, confirming the maintained YAML is the owner to edit before regenerating.
