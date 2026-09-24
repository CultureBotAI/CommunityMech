# YAML Record Review: Four-Species Aerobic Lung Microbiome Model

- Repository: CultureBotAI/CommunityMech
- Record: kb/communities/FourSpecies_Aerobic_Lung_Microbiome_Model.yaml
- Started UTC: 2026-09-24T13:27:28Z
- Finished UTC: 2026-09-24T13:33:38Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `kb/communities/FourSpecies_Aerobic_Lung_Microbiome_Model.yaml` |
| Class | `MicrobialCommunity` |
| ID | `CommunityMech:000432` |
| Label | `Four-Species Aerobic Lung Microbiome Model` |
| Maintained status | Maintained curated YAML with generated HTML products |

The record denotes the simplified artificial lung microbiome model reported in PMID:42545019 / DOI
10.1128/msystems.00491-26: an aerobic brain-heart-infusion co-culture of `Pseudomonas koreensis`,
`Rothia aeria`, `Neisseria cinerea`, and `Streptococcus downei`.

## Validation

| Check | Result |
|---|---|
| `PYTHONPATH=src .venv/bin/linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/FourSpecies_Aerobic_Lung_Microbiome_Model.yaml` | Passed: no issues found |
| `PYTHONPATH=src .venv/bin/python scripts/validate_strict.py kb/communities/FourSpecies_Aerobic_Lung_Microbiome_Model.yaml` | Passed: 1 file scanned, 0 ERROR rows |
| `PYTHONPATH=src .venv/bin/linkml-term-validator validate-data kb/communities/FourSpecies_Aerobic_Lung_Microbiome_Model.yaml -s src/communitymech/schema/communitymech.yaml --labels` | Passed |
| `PYTHONPATH=src .venv/bin/linkml-reference-validator validate data kb/communities/FourSpecies_Aerobic_Lung_Microbiome_Model.yaml -s src/communitymech/schema/communitymech.yaml --config conf/reference_validator.yaml` | Passed |
| `PYTHONPATH=src .venv/bin/python scripts/validate_shared_taxon_ids.py kb/communities/FourSpecies_Aerobic_Lung_Microbiome_Model.yaml` | Passed: 1 file checked, 0 reused ids |
| `PYTHONPATH=src .venv/bin/python scripts/validate_gtdb_coherence.py kb/communities/FourSpecies_Aerobic_Lung_Microbiome_Model.yaml` | Passed: 0 incoherent blocks, 0 malformed lineages, 0 lineage conflicts |
| `PYTHONPATH=src .venv/bin/linkml-validate --schema src/communitymech/schema/history.yaml --target-class HistoryRecord history/records/FourSpecies_Aerobic_Lung_Microbiome_Model/*.yaml` | Passed for both append-only history records |
| `PYTHONPATH=src .venv/bin/python scripts/validate_yaml_scalars.py kb/communities/FourSpecies_Aerobic_Lung_Microbiome_Model.yaml history/records/FourSpecies_Aerobic_Lung_Microbiome_Model/*.yaml` | Passed: 3 files checked, 0 truncated scalars |
| `PYTHONPATH=src .venv/bin/pytest -q tests/test_gtdb_coherence_validator.py::test_the_status_distribution_is_what_was_measured tests/test_participating_taxa.py::test_the_corpus_is_unchanged_by_this_feature` | Passed: 2 tests |
| `PYTHONPATH=src .venv/bin/python -m communitymech.render` | Passed: rendered 422 community pages and regenerated `docs/browser.html` and `docs/index.html` |
| `tmp/check_lung_snippets.py` | Passed: all 11 record snippets found in `references_cache/PMID_42545019.txt` after whitespace normalization |

Full `just` recipes were not used because `uv run` is blocked locally by the known `llvmlite==0.46.0`
build failure under Python 3.13. The underlying project-venv commands above ran directly.

## Identity and Grounding

The publication identity resolves:

- PubMed EFetch returned PMID `42545019`, DOI `10.1128/msystems.00491-26`, PMCID `PMC13595950`, and the
  matching title.
- The direct PMC HTML page for `PMC13595950` resolved and exposed citation metadata for the same title,
  DOI, and PMID. NCBI's OA utility returned 404 for this PMCID, so the committed record remains backed by
  the PubMed abstract cache rather than a generated PMC full-text cache.
- Direct `doi.org` resolution returned HTTP 403 during review, but the DOI itself is present in both the
  PubMed XML `ArticleIdList` and the committed PMID cache.

The taxon CURIEs agree with NCBI Taxonomy ESummary and all resolve as active species:

| Preferred term | CURIE | Live NCBI scientific name |
|---|---|---|
| `Pseudomonas koreensis` | `NCBITaxon:198620` | `Pseudomonas koreensis` |
| `Rothia aeria` | `NCBITaxon:172042` | `Rothia aeria` |
| `Neisseria cinerea` | `NCBITaxon:483` | `Neisseria cinerea` |
| `Streptococcus downei` | `NCBITaxon:1317` | `Streptococcus downei` |

Each taxon is intentionally curated at species rank: the inspected PubMed abstract names these four
species but does not expose strain designations. The `gtdb_grounding_status: UNRESOLVED` values are
internally coherent. `scripts/gtdb_ground.py --community ... --emit-yaml` could not run because no local
`NCBI2GTDB.tsv.gz` was present in its three default KG-Microbe sibling paths.

The record's scope is internally consistent: `ecological_state: ENGINEERED` and
`community_origin: SYNTHETIC` match an in vitro artificial co-culture, and `community_category: OTHER`
is the available enum fallback because `CommunityCategoryEnum` has no host- or lung-microbiome value.
The `ENVO:01001405` laboratory-environment term is deliberately broad, with a note preserving that the
model is a laboratory BHI co-culture rather than a sampled airway community.

## Evidence

All current evidence snippets are exact excerpts from the committed PubMed cache after whitespace
normalization. Evidence is attached to narrow claims:

| Claim area | Nearest support |
|---|---|
| Model objective and four-species artificial lung model scope | Abstract sentence that the authors developed a simplified artificial lung microbiome model composed of four representative species |
| Member taxa | Abstract species list naming `Pseudomonas koreensis`, `Rothia aeria`, `Neisseria cinerea`, and `Streptococcus downei` |
| BHI medium, 34 C incubation, 10-day stability | Abstract sentence naming the stable 10-day co-culture at 34 C in brain heart infusion medium |
| qPCR, viability PCR, conventional microbiology, and metaproteomics endpoints | Abstract sentences naming those validation and mass-spectrometry approaches |
| DOI and PubMed resources | PMID cache lines containing the DOI and PubMed identifier |

The record correctly avoids asserting individual pairwise ecological interactions: the only inspected
source text available in the committed cache says bioinformatic analyses revealed potential
microbe-microbe interactions supported by metaproteomic analysis, but does not expose exact source/target
pairs.

## Completeness

No consequential missing field was found.

The absent slots are defensible:

- No strain designations: none are visible in the inspected PubMed abstract.
- No `ecological_interactions`: the committed cache does not name directional pairwise edges.
- No `modeled_environment`: no exact host-lung ENVO term was identified during curation, and the record
  preserves the in vitro scope in `environment_term.notes`.
- No datasets: the PubMed abstract does not name an accession.

Duplicate detection used an ignored-file-independent search across `kb`, `data`, `docs`,
`references_cache`, `reports`, and `research` for PMID `42545019`, DOI `10.1128/msystems.00491-26`,
the full title, and the four member species. Matches were limited to this new record, its generated page,
the new PMID cache, the new scout queue/report, the new history records, or pre-existing records sharing
single taxa such as `Pseudomonas koreensis` or `Streptococcus downei`; no duplicate lung-model record was
found in the searched corpus.

## Findings

No current blocker, major, or minor findings remain.

One minor issue was found and fixed during review:

| Severity | Finding | Maintained owner | Status |
|---|---|---|---|
| Minor | The DOI external resource originally cited the article title as its snippet, which supported the article identity but not the DOI identifier itself. | `kb/communities/FourSpecies_Aerobic_Lung_Microbiome_Model.yaml` | Fixed for issue https://github.com/CultureBotAI/CommunityMech/issues/1080 by replacing the snippet with the exact `DOI: 10.1128/msystems.00491-26` cache line, appending `FIX_EXTERNAL_RESOURCE_EVIDENCE`, adding an EDIT history record, and rerendering docs. |

## Recommended Edits

None found for the current record.

## Follow-up Checks

If a local KG-Microbe checkout with `data/raw/NCBI2GTDB.tsv.gz` becomes available, run:

```bash
PYTHONPATH=src .venv/bin/python scripts/gtdb_ground.py \
  --community kb/communities/FourSpecies_Aerobic_Lung_Microbiome_Model.yaml \
  --emit-yaml
```

If it emits exact GTDB classifications, apply them with the guarded GTDB workflow and rerun:

```bash
PYTHONPATH=src .venv/bin/python scripts/validate_gtdb_coherence.py \
  kb/communities/FourSpecies_Aerobic_Lung_Microbiome_Model.yaml
```

## Additional Notes

- `just new-history` was unavailable for the same `uv` / Python 3.13 `llvmlite` build failure that blocks
  other `uv run` recipes locally, so both history records were written by schema-conformant local patches
  and validated against `src/communitymech/schema/history.yaml`.
- The direct PMC article HTML resolved even though NCBI's OA utility returned 404 for the same PMCID.
  Because `scripts/cache_fulltext.py` keys off stale Europe PMC metadata for this new paper, it skipped
  caching PMC full text; the record intentionally uses only abstract-supported claims.
