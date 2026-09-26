# YAML Record Review: Nitrifying Wastewater Ammonia-Oxidizing Consortium

- Repository: CultureBotAI/CommunityMech
- Record: `kb/communities/Nitrifying_Wastewater_Ammonia_Oxidizing_Consortium.yaml`
- Started UTC: 2026-09-26T07:30:06Z
- Finished UTC: 2026-09-26T07:30:06Z
- Verdict: needs curation

## Target

`CommunityMech:000433` is a new `MicrobialCommunity` record for the
top-down, model aerobic ammonia-oxidizing consortium used by Smith et al. 2026
(`PMID:41457319`, DOI `10.1128/aem.01984-25`) to test wastewater-like aerobic
and anoxic synthetic-pond-water incubations by long-read metagenomics,
short-read metagenomics, metatranscriptomics, nitrogen chemistry, virulence
factor screening, and antibiotic-resistance-gene screening.

An ignored/hidden-inclusive duplicate search covered `kb`, `data`, `docs`,
`reports`, `references_cache`, and `research` for `41457319`,
`10.1128/aem.01984-25`, `PMC12838200`, `PRJNA1165788`, and
`10.5281/zenodo.14861210`. It found the newly added record, the new local
PMID:41457319 cache files, and ignored local scouting outputs, but no
pre-existing curated record in `kb` or `data`.

## Validation

| Check | Result |
|---|---|
| `.venv/bin/linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Nitrifying_Wastewater_Ammonia_Oxidizing_Consortium.yaml` | Passed, `No issues found`. |
| `PYTHONPATH=src .venv/bin/python scripts/validate_strict.py kb/communities/Nitrifying_Wastewater_Ammonia_Oxidizing_Consortium.yaml` | Passed, 1 file scanned, 0 files with `ERROR`. |
| `.venv/bin/linkml-term-validator validate-data kb/communities/Nitrifying_Wastewater_Ammonia_Oxidizing_Consortium.yaml -s src/communitymech/schema/communitymech.yaml --labels` | Passed. |
| `PYTHONPATH=src .venv/bin/linkml-reference-validator validate data kb/communities/Nitrifying_Wastewater_Ammonia_Oxidizing_Consortium.yaml -s src/communitymech/schema/communitymech.yaml --config conf/reference_validator.yaml` | Passed; `Total checks: 0`, so the snippet audit below did the effective evidence-text check. |
| `PYTHONPATH=src .venv/bin/python scripts/validate_shared_taxon_ids.py kb/communities/Nitrifying_Wastewater_Ammonia_Oxidizing_Consortium.yaml` | Passed, 0 reused IDs. |
| `PYTHONPATH=src .venv/bin/python scripts/validate_gtdb_coherence.py kb/communities/Nitrifying_Wastewater_Ammonia_Oxidizing_Consortium.yaml` | Passed, 0 incoherent blocks, 0 malformed lineages, 0 lineage conflicts. |
| `.venv/bin/linkml-validate --schema src/communitymech/schema/history.yaml --target-class HistoryRecord history/records/Nitrifying_Wastewater_Ammonia_Oxidizing_Consortium/2026-09-26T072714Z-codex-433.yaml` | Passed, `No issues found`. |
| `PYTHONPATH=src .venv/bin/python scripts/validate_yaml_scalars.py kb/communities/Nitrifying_Wastewater_Ammonia_Oxidizing_Consortium.yaml history/records/Nitrifying_Wastewater_Ammonia_Oxidizing_Consortium/2026-09-26T072714Z-codex-433.yaml` | Passed, 2 files checked, 0 truncated scalars. |
| `PYTHONPATH=src .venv/bin/python scripts/evidence_snippet_audit.py kb/communities/Nitrifying_Wastewater_Ammonia_Oxidizing_Consortium.yaml` | Passed, 14 snippets scanned, 14 `MATCH`, 0 `WEAK`, 0 `MISMATCH`, 0 `NOCONTENT`. |
| `PYTHONPATH=src .venv/bin/python -m communitymech.render` | Passed, rendered 423 communities plus `docs/browser.html` and `docs/index.html`. |
| `git diff --check` | Passed. |

## Identity and Grounding

The record identity is coherent. The source PMID, DOI, title, and
version-of-record open-access article cache all point to the same Applied and
Environmental Microbiology article, and the curated BioProject `PRJNA1165788`
and Zenodo DOI `10.5281/zenodo.14861210` are exact matches for the paper's data
availability statement.

`community_origin: NATURAL` and `ecological_state: ENGINEERED` are appropriate
for a top-down consortium grown from an environmental source under conditions
selected for wastewater ammonia removal. `community_category: BIOTECHNOLOGY`
also matches a wastewater-treatment microbial product; the record does not
misuse a narrower enum such as `DIET`.

The three curated taxa are genus-level MAG anchors, not exact cultured strains.
That is the right granularity here because the authors report poor
species-level resolution in GTDB for this consortium and the local
NCBI-to-GTDB crosswalk is unavailable. Marking all three as `UNRESOLVED` is
more faithful than guessing GTDB species mappings for anonymous MAGs.

The laboratory `environment_term`, wastewater-bioreactor `modeled_environment`,
aerobic and anoxic synthetic-pond-water growth media, and BioProject and Zenodo
dataset records are all in scope for the publication.

## Evidence

Supported:

- The abstract and main text support this as a model aerobic
  ammonia-oxidizing consortium for wastewater-treatment risk and performance
  assessment.
- The starting-material results identify 64 high-quality bacterial MAGs and
  classify the dominant MAG as `Nitrosospira`, a lower-abundance MAG as
  `Nitrobacter`, and Legionella-affiliated bins as part of the pathogen and
  virulence-gene screen.
- The methods support the 150 mL serum-bottle setup, synthetic pond water,
  10% live-consortium inoculation, aerobic sterile-air purging, and
  N2-bubbled anoxic treatments dispensed in a 97% N2/3% H2 glovebox.
- The introduction and results support a community-level AOB-to-NOB
  metabolic handoff between `Nitrosospira` and `Nitrobacter` genera without
  overclaiming a purified binary isolate experiment.
- The data availability statement supports both stable dataset records.

Needs curation:

- The current `Nitrosospira` evidence snippet supports dominance and
  ammonia-oxidation potential, but not the exact `45.96%` value in the
  curated `abundance_value`.

## Completeness

The record is complete enough for the primary publication. It captures the
dominant ammonia-oxidizing MAG, a representative nitrite-oxidizing MAG, the
Legionella biosafety-assessment axis, aerobic and anoxic growth media, the
multi-omics and nitrogen-chemistry endpoints, stable DOI/PubMed links, the
BioProject, and the Zenodo archive.

No major stable identifier, growth condition, metal/REE declaration, or
publication-level uncertainty is missing.

## Findings

### Major

| ID | Finding | Evidence | Maintained owner |
|---|---|---|---|
| F1 | The `Nitrosospira MAG` evidence snippet does not support the curated `45.96%` abundance value. The number is correct, but the current snippet only says the consortium showed dominance by an unclassified `Nitrosospira` species with ammonia-oxidation capabilities. | `kb/communities/Nitrifying_Wastewater_Ammonia_Oxidizing_Consortium.yaml:75`; `references_cache/PMID_41457319.txt` contains a later results sentence stating that MAG `MBSoxNitrifying4mlFreshRep3_metaMDBG_complete.48` was classified to `Nitrosospira` and maintained a high sequence abundance of `45.96%`. | `kb/communities/Nitrifying_Wastewater_Ammonia_Oxidizing_Consortium.yaml` |

### Minor

None found.

### Blockers

None found.

## Recommended Edits

1. Replace the abstract-level `Nitrosospira` evidence snippet with the exact
   starting-material results span that names
   `MBSoxNitrifying4mlFreshRep3_metaMDBG_complete.48`, classifies it to
   `Nitrosospira`, and reports `45.96%`.
2. Append a review-fix history record.
3. Regenerate `docs/communities/Nitrifying_Wastewater_Ammonia_Oxidizing_Consortium.html`,
   `docs/browser.html`, and `docs/index.html`.

## Follow-up Checks

- Re-run direct LinkML, strict, term-label, reference, shared-taxon, GTDB,
  evidence-snippet, YAML-scalar, and history validation.
- Re-run `PYTHONPATH=src .venv/bin/python -m communitymech.render`.
- Run `git diff --check` before staging.

## Additional Notes

This review used the cached PubMed abstract and Europe PMC open-access article
text. It did not contact the anonymous industry partner or resolve the
unavailable local NCBI-to-GTDB crosswalk.
