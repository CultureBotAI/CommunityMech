# YAML Record Review: Wheat SynCom-SASW01 Drought-Resistance Inoculant

- Repository: CultureBotAI/CommunityMech
- Record: kb/communities/Wheat_SynCom_SASW01_Drought_Inoculant.yaml
- Started UTC: 2026-09-21T16:09:20Z
- Finished UTC: 2026-09-21T16:11:02Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `kb/communities/Wheat_SynCom_SASW01_Drought_Inoculant.yaml` |
| Class | `MicrobialCommunity` |
| ID | `CommunityMech:000409` |
| Label | `Wheat SynCom-SASW01 Drought-Resistance Inoculant` |
| Maintained status | Maintained curated YAML record, not generated |

The record denotes the five-strain SynCom-SASW01 wheat drought-resistance inoculant described in PMID:42513902. A pre-addition duplicate search for `PMID:42513902`, `10.3390/microorganisms14071396`, `SynCom-SASW01`, and the publication title covered `kb/communities`, `data/isolates`, `history`, and `references_cache` with `rg --no-ignore --hidden`; no existing CommunityMech record for this consortium was found.

## Validation

| Check | Result |
|---|---|
| `.venv/bin/linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Wheat_SynCom_SASW01_Drought_Inoculant.yaml` | Passed |
| `PYTHONPATH=src .venv/bin/python scripts/validate_strict.py kb/communities/Wheat_SynCom_SASW01_Drought_Inoculant.yaml` | Passed |
| `PYTHONPATH=src .venv/bin/python scripts/validate_gtdb_coherence.py kb/communities/Wheat_SynCom_SASW01_Drought_Inoculant.yaml` | Passed |
| `.venv/bin/linkml-term-validator validate-data kb/communities/Wheat_SynCom_SASW01_Drought_Inoculant.yaml -s src/communitymech/schema/communitymech.yaml --labels` | Passed |
| `.venv/bin/linkml-reference-validator validate data kb/communities/Wheat_SynCom_SASW01_Drought_Inoculant.yaml -s src/communitymech/schema/communitymech.yaml --config conf/reference_validator.yaml` | Passed, but the CLI reported `Total checks: 0`; a separate exact cache scan confirmed no PMID:42513902 snippets were missing from `references_cache/PMID_42513902.txt`. |
| `PYTHONPATH=src .venv/bin/python -m communitymech.network.validators --explain kb/communities/Wheat_SynCom_SASW01_Drought_Inoculant.yaml` | Passed; emitted only the package import-order runtime warning also seen in local direct module execution. |

`just` validation wrappers were not used because local `uv run` resolution attempted to build `llvmlite`/`numba` under Python 3.13 and failed before reaching the validators.

## Identity and Grounding

- The community identity is correctly bounded to SynCom-SASW01, not to the broader class of wheat PGP inoculants.
- The five asserted members are the exact strains named in the Methods: `Enterobacter hormaechei FN0603`, `Enterobacter cloacae FWP0601`, `Enterobacter ludwigii FWP1205`, `Pseudomonas putida FWP0405`, and `Stenotrophomonas maltophilia HLPD6`.
- The ENVO grounding to rhizosphere plus the modeled plant-associated environment are narrow enough for a wheat seed inoculant assayed in rhizosphere and endosphere compartments.
- The NCBITaxon IDs and labels pass the local term validator. GTDB ambiguity is explicitly marked for the species whose NCBI species bins map to multiple GTDB species.

## Evidence

Supported:

- Strain membership, R2A activation, 16S V5-V7 species confirmation, OD600 normalization, and 1:1:1:1:1 assembly are supported by the article's strain activation and identification methods.
- The greenhouse treatment arms, biological seed-coating matrix, 1:20 coating-to-seed ratio, moderate drought pot regime, and dual Inner Mongolia field sites are supported by the article's experimental methods.
- The article supports rhizosphere water retention and root-endosphere restructuring as author-level interpretations of the BCC SynCom-SASW01 treatment.
- The BCAA claim is supported as a functional prediction from amplicon profiles, but not as a curated ecological interaction.

Unsupported or over-scoped:

- The equal-ratio assembly statement is true but stored in `ecological_interactions` as `COLONIZATION_FACILITATION`; it is an inoculum assembly procedure, not an interaction between organisms or between the consortium and a host/environment.
- The BCAA/antioxidant statement is a root-associated predicted function and physiological association, not a demonstrated ecological interaction. It also uses `evidence_source: COMPUTATIONAL` without the recommended `computational_provenance`.

## Completeness

- The record is complete enough for exact consortium identity, strain membership, inoculant preparation, the drought pot assay, the field-trial context, and high-level rhizosphere/endosphere response.
- The source article says strain isolation sites and individual PGP traits are in Supplementary Tables S1 and S2. The record correctly leaves those strain-specific details unasserted and records the uninspected supplement as an open `KNOWLEDGE_GAP` discussion.
- No BioProject, SRA run table, or FigShare data DOI was required for the curated community identity because the record does not curate raw amplicon accessions or measurement tables.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Equal-ratio inoculum assembly is modeled as an ecological interaction. | The article's 1:1:1:1:1 sentence supports laboratory mixing of normalized suspensions; it does not describe `COLONIZATION_FACILITATION` or a community-level ecological interaction. | `kb/communities/Wheat_SynCom_SASW01_Drought_Inoculant.yaml` |
| Major | The BCAA/antioxidant row over-scopes a PICRUSt2 functional prediction into `ecological_interactions`. | The cached article states that functional-potential prediction used PICRUSt2 2.6.0 and MetaCyc Level 3 pathways, while the discussion links BCAA enrichment, root proline, and antioxidant enzymes as a hypothesized host response. That is not a direct microbial interaction edge. | `kb/communities/Wheat_SynCom_SASW01_Drought_Inoculant.yaml` |

No blockers or minor findings were found.

## Recommended Edits

1. Delete `ecological_interactions[].name == "Equal-ratio SynCom-SASW01 assembly"`.
2. Keep OD600 normalization and the equal-volume 1:1:1:1:1 mix in `engineering_design`, with a narrow evidence item that avoids the cache's `10^8` to `108` XML extraction artifact.
3. Delete `ecological_interactions[].name == "SynCom-SASW01-associated BCAA and antioxidant response"`.
4. Preserve BCAA functional prediction as the existing `Predicted root-associated MetaCyc pathway abundance` measurement endpoint unless a future curation pass adds a dedicated measured-feature slot or causal graph edge supported by stronger evidence.

## Follow-up Checks

- Rerun schema, strict, GTDB, term, reference, and network validators against the edited YAML.
- Re-run the exact PMID:42513902 snippet scan after editing evidence text.
- Regenerate committed HTML so the public community page matches the maintained YAML.

## Additional Notes

The source cache contains the PubMed abstract plus the Europe PMC PMC13414153 full text under a CC BY license marker. Supplementary Tables S1 and S2 remain intentionally uninspected; any future addition of isolation-site or strain-specific PGP trait claims should cite those tables or another primary source directly.
