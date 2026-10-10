# YAML Record Review: DCPP DBS4-DCP-4-DCP-11d Degradation SynCom

- Repository: CultureBotAI/CommunityMech
- Record: kb/communities/DCPP_DBS4_DCP4_DCP11d_Degradation_SynCom.yaml
- Started UTC: 2026-09-21T17:22:00Z
- Finished UTC: 2026-09-21T17:31:12Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `kb/communities/DCPP_DBS4_DCP4_DCP11d_Degradation_SynCom.yaml` |
| Class | `MicrobialCommunity` |
| ID | `CommunityMech:000410` |
| Label | DCPP DBS4-DCP-4-DCP-11d Degradation SynCom |
| Maintained/generated | Maintained curated YAML with generated HTML at `docs/communities/DCPP_DBS4_DCP4_DCP11d_Degradation_SynCom.html` |
| Primary reference | `PMID:42613016`, DOI `10.1111/1462-2920.70404` |

The record resolves to a single YAML file under the curated community corpus. It describes the three-member SynCom `DBS4&DCP-4&DCP-11d` that Lin et al. selected from five DCPP-enrichment isolates by multi-strain metabolic modelling and then tested in mineral medium and soil. The record intentionally excludes the two non-member strains `Bosea` sp. DCP-2 and `Pigmentiphaga` sp. DCP-6d from `taxonomy`.

## Validation

| Check | Result |
|---|---|
| `.venv/bin/linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/DCPP_DBS4_DCP4_DCP11d_Degradation_SynCom.yaml` | Pass: `No issues found` |
| `PYTHONPATH=src .venv/bin/python scripts/validate_strict.py kb/communities/DCPP_DBS4_DCP4_DCP11d_Degradation_SynCom.yaml` | Pass: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows |
| `PYTHONPATH=src .venv/bin/python scripts/validate_gtdb_coherence.py kb/communities/DCPP_DBS4_DCP4_DCP11d_Degradation_SynCom.yaml` | Pass: 0 incoherent blocks, 0 malformed lineages, 0 lineage conflicts |
| `.venv/bin/linkml-term-validator validate-data kb/communities/DCPP_DBS4_DCP4_DCP11d_Degradation_SynCom.yaml -s src/communitymech/schema/communitymech.yaml --labels` | Pass |
| `.venv/bin/linkml-reference-validator validate data kb/communities/DCPP_DBS4_DCP4_DCP11d_Degradation_SynCom.yaml -s src/communitymech/schema/communitymech.yaml --config conf/reference_validator.yaml` | Pass, but the configured run reported `Total checks: 0`, so exact snippet presence still required a manual cache audit |
| `PYTHONPATH=src .venv/bin/python -m communitymech.network.validators --explain kb/communities/DCPP_DBS4_DCP4_DCP11d_Degradation_SynCom.yaml` | Pass; emitted only the known `runpy` warning |
| `.venv/bin/linkml-validate --schema src/communitymech/schema/history.yaml --target-class HistoryRecord history/records/DCPP_DBS4_DCP4_DCP11d_Degradation_SynCom/2026-09-21T172849Z-codex-f34c71.yaml` | Pass: `No issues found` |
| `git diff --check` | Pass |

## Identity and Grounding

The record identity is sound. `CommunityMech:000410` and the record name denote the `DBS4&DCP-4&DCP-11d` SynCom rather than the original five-strain enrichment or the larger four- and five-member comparator SynComs.

`Sphingopyxis` sp. DBS4 and `Sphingopyxis` sp. DCP-4 are represented as separate strain descriptors with the genus-level `NCBITaxon:165697` grounding used for both, plus unresolved GTDB grounding and strain-specific `preferred_term`/`strain_designation` values. That preserves the source paper's genus-level identity without asserting a species-level assignment.

`Achromobacter` sp. DCP-11d is grounded to `NCBITaxon:222` and `GTDB:g__Achromobacter`; the NCBI label and GTDB genus block are coherent.

`DCPP` is grounded to `CHEBI:75375` and `2,4-DCP` to `CHEBI:16738`; both match the curated chemical claims.

An ignored-file-inclusive search across `kb`, `data`, `history`, `docs`, `references_cache`, and `reports` for `42613016`, `10.1111/1462-2920.70404`, `DCPP_DBS4_DCP4_DCP11d`, and `CommunityMech:000410` found only this new target, its generated HTML/history/cache artifacts, and older review-report notes that happened to mention unrelated untracked cache files. It did not find a pre-existing curated duplicate for the PMID, DOI, slug, or internal ID.

## Evidence

Supported:

- The three member strains are all directly named in Lin et al.'s methods and are the exact three strains used in the selected SynCom.
- The model-selection and experimental-performance evidence correctly support `DBS4&DCP-4&DCP-11d` as the best three-strain SynCom and as comparable to the larger SynComs in validation experiments.
- DCP-11d's 2,4-DCP helper role is supported by direct source text and the `discussions` item correctly records that the authors did not quantitatively separate the relative contributions of nutrient cross-feeding versus intermediate detoxification.
- The soil DCPP spike and the DCPP LC-MS co-culture condition are supported by the article text.
- DOI and PubMed identifiers agree with the cached PubMed record.

Unsupported or too weakly supported in the current maintained files:

- The `DBS4 to DCP-11d 2,4-DCP detoxification` interaction cites an abstract-level cross-feeding snippet about glucosamine, amino acids, and organic acids for a more specific model-derived 2,4-DCP-flow claim. The paper has direct wording for the 2,4-DCP model prediction in the Discussion, so the curated evidence should use that narrower source text.
- The YAML contains two snippets that do not occur verbatim in `references_cache/PMID_42613016.txt` as committed: the abstract cross-feeding snippet is broken across lines in the cached PubMed abstract and the primary-publication title is likewise wrapped across two lines.
- The `engineering_design.inoculation_strategy` asserts a 1:1 inoculation ratio in simulations and wet-lab validation, but the two `engineering_design.evidence` entries only support selection of the optimal three-strain combination and experimental comparability.
- `growth_media.ph` and `growth_media.incubation_time` are correct, but the local evidence snippets stop before the pH and 15 h values.

## Completeness

The record is complete enough on core composition, modeled and wet-lab evidence, metabolite detections, mineral-medium/soil validation settings, external resources, curation history, and the known unresolved mechanistic quantification gap.

Optional metal slots are correctly left as `NOT_APPLICABLE`; the primary article concerns DCPP degradation and does not report a metal-processing role.

The main curation gap is not a missing biological claim but a cache/evidence granularity gap: the committed cache needs exact selected excerpts for each curated direct quote, and a few evidence items need to be retargeted to those excerpts.

## Findings

### Major: the record has exact-snippet misses against the committed cache

`kb/communities/DCPP_DBS4_DCP4_DCP11d_Degradation_SynCom.yaml` contains two `EvidenceItem.snippet` values that are source-supported but are not contiguous substrings of `references_cache/PMID_42613016.txt`: the abstract-level cross-feeding snippet under the 2,4-DCP interaction and the primary-publication title snippet under `external_resources`.

Maintained owner: `kb/communities/DCPP_DBS4_DCP4_DCP11d_Degradation_SynCom.yaml` plus `references_cache/PMID_42613016.txt`.

### Major: the pairwise 2,4-DCP interaction should cite the direct 2,4-DCP model-prediction text

The record's pairwise `DBS4 to DCP-11d 2,4-DCP detoxification` edge says the community model predicted 2,4-DCP flow from DBS4 to DCP-11d. Its computational evidence currently cites a broad abstract sentence about cross-feeding of glucosamine, amino acids, and organic acids between degrader and helper strains. That snippet is true background, but it is not the nearest support for the source taxon, target taxon, and `CHEBI:16738` edge.

Maintained owner: `kb/communities/DCPP_DBS4_DCP4_DCP11d_Degradation_SynCom.yaml`.

### Minor: the equal-inoculation strategy needs a local evidence item

The `engineering_design.inoculation_strategy` states that candidate SynComs used equal representation in simulations and experiments. The full text supports this, but the evidence currently attached to `engineering_design` supports model selection and wet-lab comparability, not the 1:1 simulation and validation ratio.

Maintained owner: `kb/communities/DCPP_DBS4_DCP4_DCP11d_Degradation_SynCom.yaml`.

### Minor: medium pH and LC-MS duration need nearer snippets

`growth_media.ph: 7.0` and `growth_media.incubation_time: 15` are supported by Lin et al.'s methods, but the selected snippets attached to `growth_media` stop at the salt formulation and at `30°C and 180 rpm`. Add exact excerpts that include `pH = 7.0` and `for 15 h`.

Maintained owner: `kb/communities/DCPP_DBS4_DCP4_DCP11d_Degradation_SynCom.yaml` plus `references_cache/PMID_42613016.txt`.

## Recommended Edits

- Add exact selected excerpts to `references_cache/PMID_42613016.txt` for the one-line title, the direct 2,4-DCP model-flow claim, the simulation/experimental 1:1 inoculation claim, the mineral-medium pH, and the LC-MS 15 h co-culture condition.
- Replace the broad computational snippet on the pairwise 2,4-DCP edge with the direct model-predicted 2,4-DCP-flow snippet.
- Add a targeted `engineering_design` evidence item for the 1:1 inoculation strategy.
- Add targeted `growth_media` evidence items or extend the existing explanations so the pH and 15 h fields have direct nearby source support.
- Append a `curation_history` event for the evidence-tightening pass and create an append-only per-record history file that references the GitHub issues opened for these findings.
- Regenerate `docs/communities/DCPP_DBS4_DCP4_DCP11d_Degradation_SynCom.html`, `docs/browser.html`, and `docs/index.html`.

## Follow-up Checks

After the recommended edit, rerun:

- `.venv/bin/linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/DCPP_DBS4_DCP4_DCP11d_Degradation_SynCom.yaml`
- `PYTHONPATH=src .venv/bin/python scripts/validate_strict.py kb/communities/DCPP_DBS4_DCP4_DCP11d_Degradation_SynCom.yaml`
- `PYTHONPATH=src .venv/bin/python scripts/validate_gtdb_coherence.py kb/communities/DCPP_DBS4_DCP4_DCP11d_Degradation_SynCom.yaml`
- `.venv/bin/linkml-term-validator validate-data kb/communities/DCPP_DBS4_DCP4_DCP11d_Degradation_SynCom.yaml -s src/communitymech/schema/communitymech.yaml --labels`
- `.venv/bin/linkml-reference-validator validate data kb/communities/DCPP_DBS4_DCP4_DCP11d_Degradation_SynCom.yaml -s src/communitymech/schema/communitymech.yaml --config conf/reference_validator.yaml`
- `PYTHONPATH=src .venv/bin/python -m communitymech.network.validators --explain kb/communities/DCPP_DBS4_DCP4_DCP11d_Degradation_SynCom.yaml`
- `.venv/bin/linkml-validate --schema src/communitymech/schema/history.yaml --target-class HistoryRecord history/records/DCPP_DBS4_DCP4_DCP11d_Degradation_SynCom/*.yaml`
- `PYTHONPATH=src .venv/bin/python -m communitymech.render`
- `git diff --check`
- `git diff --cached --check`

## Additional Notes

The configured reference-validator command succeeded but performed zero checks for this file, so a local snippet audit against `references_cache/PMID_42613016.txt` was necessary and found the two cache misses above.

`references_cache/PMID_42385706.txt` and the untracked files under `references_cache/files/` were already present in the worktree and are unrelated to this record.
