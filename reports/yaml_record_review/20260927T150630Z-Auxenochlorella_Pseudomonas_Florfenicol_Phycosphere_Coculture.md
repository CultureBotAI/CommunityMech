# YAML Record Review: Auxenochlorella-Pseudomonas Florfenicol Phycosphere Coculture

- Repository: `CultureBotAI/CommunityMech`
- Record: `kb/communities/Auxenochlorella_Pseudomonas_Florfenicol_Phycosphere_Coculture.yaml`
- Started UTC: 2026-09-27T15:02:00Z
- Finished UTC: 2026-09-27T15:06:30Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `MicrobialCommunity` |
| ID | `CommunityMech:000451` |
| Label | Auxenochlorella-Pseudomonas Florfenicol Phycosphere Coculture |
| Maintained path | `kb/communities/Auxenochlorella_Pseudomonas_Florfenicol_Phycosphere_Coculture.yaml` |
| Generated products | `docs/communities/Auxenochlorella_Pseudomonas_Florfenicol_Phycosphere_Coculture.html`, plus `docs/browser.html` and `docs/index.html` |
| Primary source | `PMID:41724996`; DOI `10.1186/s40168-026-02335-7` |
| Source cache | `references_cache/PMID_41724996.txt` |

The record represents the defined validation pair `Auxenochlorella pyrenoidosa` plus the locally named phycospheric isolate `Pseudomonas_sp1`, not the broader 60-day undefined South Lake bacterial pool.

## Validation

| Check | Result |
|---|---|
| `linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Auxenochlorella_Pseudomonas_Florfenicol_Phycosphere_Coculture.yaml` | passed, no issues |
| `scripts/validate_strict.py kb/communities/Auxenochlorella_Pseudomonas_Florfenicol_Phycosphere_Coculture.yaml` | passed, 0 ERROR rows |
| `scripts/validate_strict.py` | passed across 445 roots, 0 ERROR rows |
| `scripts/validate_gtdb_coherence.py kb/communities/Auxenochlorella_Pseudomonas_Florfenicol_Phycosphere_Coculture.yaml` | passed |
| `scripts/validate_prokaryotic_lineage.py kb/communities/Auxenochlorella_Pseudomonas_Florfenicol_Phycosphere_Coculture.yaml` | passed |
| `scripts/validate_shared_taxon_ids.py kb/communities/Auxenochlorella_Pseudomonas_Florfenicol_Phycosphere_Coculture.yaml` | passed |
| `scripts/validate_yaml_scalars.py kb/communities/Auxenochlorella_Pseudomonas_Florfenicol_Phycosphere_Coculture.yaml` | passed |
| `scripts/validate_cross_repo_ids.py kb/communities/Auxenochlorella_Pseudomonas_Florfenicol_Phycosphere_Coculture.yaml` | passed |
| `linkml-term-validator validate-data ... --labels` | passed |
| `linkml-reference-validator validate data ...` | passed against `references_cache/PMID_41724996.txt` |
| `linkml-validate -s src/communitymech/schema/history.yaml history/records/Auxenochlorella_Pseudomonas_Florfenicol_Phycosphere_Coculture/2026-09-27T150158Z-claude-code-3ccabb.yaml` | passed |
| `scripts/audit_writers.py` | passed |
| `communitymech.render` | rendered all 441 community pages, the browser, and the landing page |
| Manual orphan-page check | passed; every `docs/communities/*.html` stem has a matching `kb/communities/*.yaml` record |
| `git diff --check` | passed |
| `black --check src/ tests/ scripts/` | passed |
| `ruff check src/ tests/ scripts/` | passed via `uvx --from ruff` |

`mypy src/` could not complete in the sibling virtualenv because that environment lacks third-party stubs and optional embedding libraries: `types-PyYAML`, `types-requests`, `types-tqdm`, `sklearn`, `pandas-stubs`, and `pacmap`. Full `pytest tests/ -v` could not collect `tests/test_embedding/test_aggregator.py` because the same environment lacks `umap`. A retry with `tests/test_embedding` ignored exposed one unrelated `test_batch_snippet_fixer_validation.py` failure and was stopped after several minutes at roughly 5% of the suite.

## Identity and Grounding

The record identity is appropriately narrow:

- `Auxenochlorella pyrenoidosa` is grounded to `NCBITaxon:3078`, the same canonical NCBI identifier and label already used for this alga in the corpus.
- `Pseudomonas_sp1` is preserved as the source article's local isolate name and grounded conservatively to genus-level `NCBITaxon:306` / `Pseudomonas sp.`.
- `NO_GTDB_EQUIVALENT` is correct for the eukaryotic alga; `UNRESOLVED` is conservative for the unresolved Pseudomonas isolate.
- `community_origin: SYNTHETIC`, `ecological_state: ENGINEERED`, and `community_category: PHYTOPLANKTON` match a designed laboratory alga-bacterium pair.
- The environment uses `ENVO:01001405` / `laboratory environment` as the physical study setting and keeps the freshwater South Lake context in `modeled_environment`, avoiding a false natural-community claim.

Gitignore-independent duplicate checks covered `kb/`, `data/`, `docs/`, `history/`, `reports/`, `references_cache/`, `research/`, and `tmp/`, excluding `.git`, `.env*`, and the binary `references_cache/files/` tree. They found prior scout stubs and the fresh source cache, but no existing curated record for `PMID:41724996`, DOI `10.1186/s40168-026-02335-7`, or `Pseudomonas_sp1`.

## Evidence

Every asserted member, interaction, stress condition, dataset, DOI, and PMID in the final record has a narrow local evidence object whose snippet validates against `PMID_41724996.txt`.

- The `engineering_design` evidence supports isolation from the high-florfenicol plus PLA microplastic PFH group and selection of `Pseudomonas_sp1` for co-cultivation with axenic `A. pyrenoidosa`.
- The `taxonomy` evidence supports both the axenic algal member and the locally named Pseudomonas isolate, including the `PRJNA1171391` BioProject association for the isolate genome.
- The cross-feeding interaction evidence was deliberately left metabolite-causal but cautious: measured Pseudomonas-associated pyridoxal production and exogenous vitamin B6 growth support are marked `PARTIAL`, because the source supports a likely vitamin B6 mechanism rather than a traced pyridoxal flux from bacterium to alga.
- The stress-treatment environmental factor is backed by the paper's statement that FF and PLA MP treatments were set up in the isolate co-culture.
- The external DOI resource is backed by the article title, and the only associated dataset is the directly relevant `Pseudomonas_sp1` genome BioProject.

During adversarial review, two draft-scope issues were fixed before this report:

- Removed an `MTBLS11371` associated dataset entry because that MetaboLights accession describes the broader algal metabolomics experiment, not the defined Pseudomonas_sp1 validation pair.
- Tightened top-level prose that had mentioned MIC-confirmed florfenicol resistance plus chlorophyll, EPS, MDA, and SOD responses without carrying equally narrow evidence in the final YAML.

## Completeness

The final record intentionally leaves `growth_media` empty. The article body establishes the Pseudomonas_sp1/A. pyrenoidosa pair and reports the 13-day growth response, but points exact follow-up medium, inoculum, and grouping details to supplementary Text S12. The supplement listing process hung while reading the archive, so the record now carries `discussions#exact-pair-growth-medium` to name that concrete gap instead of borrowing the 60-day mixed-bacteria BG-11 conditions from the precursor experiment.

No metal, rare-earth, or cross-repository media/ingredient role was reported for this validation pair, and the record correctly leaves those optional domains empty or `NOT_APPLICABLE`.

## Findings

None found in the final maintained YAML.

The only adversarial findings were corrected before report emission, as noted in **Evidence**.

## Recommended Edits

None for the final maintained YAML.

## Follow-up Checks

For any future addition of pairwise growth-medium details, inspect Text S12 from the supplementary archive, add a guarded YAML curation event and append-only `history/records/Auxenochlorella_Pseudomonas_Florfenicol_Phycosphere_Coculture/` entry, then rerun:

- `linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Auxenochlorella_Pseudomonas_Florfenicol_Phycosphere_Coculture.yaml`
- `scripts/validate_strict.py kb/communities/Auxenochlorella_Pseudomonas_Florfenicol_Phycosphere_Coculture.yaml`
- `linkml-reference-validator validate data kb/communities/Auxenochlorella_Pseudomonas_Florfenicol_Phycosphere_Coculture.yaml -s src/communitymech/schema/communitymech.yaml --config conf/reference_validator.yaml`
- `communitymech.render`
- `git diff --check`

## Additional Notes

The supplementary archive fetch was deliberately terminated after it remained stuck. The open-access article body was sufficient for a supported pairwise record, and the only information known to be supplement-resident is now represented as a named discussion gap.
