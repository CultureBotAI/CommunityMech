# YAML Record Review: Burkholderia-Pseudomonas YB2 PET Degradation Consortium

- Repository: CultureBotAI/CommunityMech
- Record: `kb/communities/Burkholderia_Pseudomonas_YB2_PET_Degradation_Consortium.yaml`
- Started UTC: 2026-09-22T21:37:32Z
- Finished UTC: 2026-09-22T21:37:32Z
- Verdict: pass

## Target

`CommunityMech:000426` is a maintained `MicrobialCommunity` record for the
defined two-strain YB2 consortium of `Burkholderia cepacia` ZY1 and
`Pseudomonas harudinis` G1B from Qiu et al. 2026 (`PMID:42664909`, DOI
`10.1016/j.jenvman.2026.130823`). The source abstract reports comparison of the
individual strains, YB2 construction at a 4:5 inoculation ratio, PET film mass
loss at pH 7.0 and 30 C, BHET/MHET conversion, near-complete TPA utilization,
EG release and decline, and PET surface erosion plus ester-related structural
changes.

An ignored/hidden-inclusive duplicate search covered `kb`, `data`, `history`,
`pages`, `docs`, `reports`, `references_cache`, `research`, and `tmp` for
`CommunityMech:000426`,
`Burkholderia_Pseudomonas_YB2_PET_Degradation_Consortium`,
`10.1016/j.jenvman.2026.130823`, and `42664909`. It found only the new curated
record, new history record, new PMID cache, the new rendered page, and the scout
reports that originally identified PMID:42664909 as a new candidate.

## Validation

| Check | Result |
|---|---|
| `.venv/bin/linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Burkholderia_Pseudomonas_YB2_PET_Degradation_Consortium.yaml` | Passed, `No issues found`. |
| `PYTHONPATH=src .venv/bin/python scripts/validate_strict.py kb/communities/Burkholderia_Pseudomonas_YB2_PET_Degradation_Consortium.yaml` | Passed, 1 file scanned, 0 files with `ERROR`. |
| `.venv/bin/linkml-term-validator validate-data kb/communities/Burkholderia_Pseudomonas_YB2_PET_Degradation_Consortium.yaml -s src/communitymech/schema/communitymech.yaml --labels` | Passed. |
| `PYTHONPATH=src .venv/bin/python scripts/validate_gtdb_coherence.py kb/communities/Burkholderia_Pseudomonas_YB2_PET_Degradation_Consortium.yaml` | Passed, 0 incoherent blocks, 0 malformed lineages, 0 lineage conflicts. |
| `PYTHONPATH=src .venv/bin/python scripts/validate_yaml_scalars.py kb/communities/Burkholderia_Pseudomonas_YB2_PET_Degradation_Consortium.yaml` | Passed, 1 file checked, 0 truncated scalars. |
| `.venv/bin/linkml-validate --schema src/communitymech/schema/history.yaml --target-class HistoryRecord history/records/Burkholderia_Pseudomonas_YB2_PET_Degradation_Consortium/2026-09-22T213202Z-codex-426.yaml` | Passed, `No issues found`. |
| `PYTHONPATH=src .venv/bin/python scripts/evidence_snippet_audit.py kb/communities/Burkholderia_Pseudomonas_YB2_PET_Degradation_Consortium.yaml` | Passed, 18 snippets scanned, 18 `MATCH`, 0 `RENDERING`, 0 `WEAK`, 0 `MISMATCH`, 0 `NOCONTENT`. |
| `.venv/bin/linkml-reference-validator validate data kb/communities/Burkholderia_Pseudomonas_YB2_PET_Degradation_Consortium.yaml -s src/communitymech/schema/communitymech.yaml --config conf/reference_validator.yaml` | Passed, but `Total checks: 0`; the snippet audit above did the effective evidence-text check. |
| `PYTHONPATH=src .venv/bin/python scripts/audit_writers.py` | Passed before this review. |
| `PYTHONPATH=src .venv/bin/python -m communitymech.render` | Passed, rendered 416 communities plus `docs/browser.html` and `docs/index.html`. |
| `git diff --check` | Passed. |

## Identity and Grounding

The record identity is coherent. The primary PMID cache matches the Journal of
Environmental Management record for "Enhanced degradation of polyethylene
terephthalate by a two-strain microbial consortium" and carries DOI
`10.1016/j.jenvman.2026.130823`.

Both curated members are the exact strain labels reported in the abstract:
`Burkholderia cepacia` ZY1 and `Pseudomonas harudinis` G1B. Exact NCBI
Taxonomy scientific-name searches resolved these species to `NCBITaxon:292` and
`NCBITaxon:2833596`, and `linkml-term-validator` confirmed the local
id-to-label bindings. Both taxa are correctly left `UNRESOLVED` for GTDB:
`scripts/gtdb_ground.py --community ... --emit-yaml` could not find the local
`NCBI2GTDB.tsv.gz` crosswalk, so no deterministic genome-based grounding was
available in this checkout.

The `laboratory environment` grounding is scoped to the controlled PET/BHET/MHET
in-vitro assays, not to an inferred isolation source. The `BIOREMEDIATION`
category fits the pollutant-degradation objective.

## Evidence

Supported:

- The cached PubMed abstract explicitly names the two strains and says that a
  YB2 two-strain consortium was constructed at a 4:5 optimal inoculation ratio.
- The abstract supports the role split at the level curated here: ZY1 showed
  stronger PET depolymerization-related activity, while G1B grew better in
  BHET- and MHET-containing media and trended toward faster BHET conversion.
- The pH 7.0, 30 C PET-film phenotype is exact: YB2 reached 4.30% +/- 0.11%
  PET film mass loss after 3 days and exceeded the individual strains.
- BHET, MHET, TPA, and EG are all source-supported PET hydrolysis products or
  assay substrates: the abstract reports BHET/MHET/TPA detection during PET
  depolymerization, 96.4% BHET plus 97.3% MHET conversion within 2 days, nearly
  complete TPA use within 5 days, and initial EG accumulation followed by
  decline.
- Surface erosion, ester-related structural changes, and increased residual PET
  crystallinity are supported as PET-film modification readouts.

Not supported:

- Directional cross-feeding from ZY1 to G1B is not shown in the accessible
  abstract. The record therefore uses a community-level, non-directional
  `NICHE_PARTITIONING` interaction instead of a pairwise metabolite-transfer
  edge.
- Full medium composition, vessel geometry, aeration, and strain-specific
  hydrolase identities are not in the cached abstract. The growth-media block
  records only pH, temperature, inoculation ratio, abstract-level timing, and an
  explicit limitation note.

## Completeness

The record is complete enough for the accessible primary abstract. It captures
the exact two-strain membership, optimized inoculation ratio, pH/temperature
reported for the PET film assay, PET film mass-loss phenotype, BHET/MHET/TPA/EG
endpoints, non-directional complementarity claim, publication URL, PET-related
ChEBI ingredients with available terms, and explicit non-relevance to metal or
rare-earth processing.

No full text or supplementary files were cached. Europe PMC reports no
open-access full text for PMID:42664909 (`pmcid=None`, `oa=False`), and the
article is an Elsevier version-of-record publication, so this review did not
attempt publisher-bypassing retrieval.

## Findings

### Major

None found.

### Minor

None found.

### Blockers

None found.

## Pre-review Fixes

- Removed an over-specific `growth_media.incubation_time: 3` value. The medium
  block summarizes PET film, BHET, MHET, and TPA assays that have different
  reported durations, so the exact 3-day, 2-day, and 5-day timings now live in
  endpoint-specific factors and preparation notes only.

## Follow-up Checks

- Re-run full-corpus `PYTHONPATH=src .venv/bin/python scripts/validate_strict.py`
  after the review report is added.
- Stage only `references_cache/PMID_42664909.txt` from `references_cache/`; leave
  the unrelated untracked PMID 42385706 cache and PDF downloads unstaged.
- Run `git diff --check` after staging.

## Additional Notes

This review used the cached PubMed abstract only. It did not contact authors,
spend provider credits, or resolve the unavailable local NCBI-to-GTDB crosswalk.
