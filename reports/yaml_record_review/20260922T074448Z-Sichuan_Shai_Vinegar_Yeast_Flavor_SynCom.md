# YAML Record Review: Sichuan Shai Vinegar Yeast Flavor SynCom

- Repository: CultureBotAI/CommunityMech
- Record: `kb/communities/Sichuan_Shai_Vinegar_Yeast_Flavor_SynCom.yaml`
- Started UTC: 2026-09-22T07:44:48Z
- Finished UTC: 2026-09-22T07:45:20Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `kb/communities/Sichuan_Shai_Vinegar_Yeast_Flavor_SynCom.yaml` |
| Class | `MicrobialCommunity` |
| ID | `CommunityMech:000417` |
| Label | Sichuan Shai Vinegar Yeast Flavor SynCom |
| Maintained or generated | Maintained curated record |
| Category / state / origin | `BIOTECHNOLOGY` / `ENGINEERED` / `SYNTHETIC` |
| Primary source | `PMID:41344775`, `doi:10.1016/j.fm.2025.104983` |

The record denotes the Zhu et al. defined yeast-consortium comparison for early solid-state Sichuan Shai vinegar fermentation. The scope is a synthetic model of SSV yeast flavor formation, not the full natural vinegar microbiota.

## Validation

| Check | Result |
|---|---|
| `linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Sichuan_Shai_Vinegar_Yeast_Flavor_SynCom.yaml` | Pass, no issues found |
| `scripts/validate_strict.py kb/communities/Sichuan_Shai_Vinegar_Yeast_Flavor_SynCom.yaml` | Pass, 1 file scanned and 0 ERROR rows |
| `linkml-term-validator validate-data ... --labels` | Pass, all ontology labels resolved |
| `scripts/evidence_snippet_audit.py --list-mismatch --list-rendering --list-assembled ...` | Pass, 26 `MATCH`, 0 `MISMATCH`, 0 `WEAK`, 0 `RENDERING`, 0 `ASSEMBLED`, 0 `NOCONTENT` |
| `linkml-reference-validator validate data ... --config conf/reference_validator.yaml` | Pass, but the upstream tool printed `Total checks: 0`; the snippet audit above is the meaningful exact-snippet reconciliation |
| `linkml-validate --schema src/communitymech/schema/history.yaml --target-class HistoryRecord history/records/Sichuan_Shai_Vinegar_Yeast_Flavor_SynCom/2026-09-22T074121Z-codex-004abf.yaml` | Pass, no issues found |
| `scripts/validate_gtdb_coherence.py kb/communities/Sichuan_Shai_Vinegar_Yeast_Flavor_SynCom.yaml` | Pass, 0 incoherent blocks, 0 malformed lineages, 0 lineage conflicts |
| `scripts/validate_yaml_scalars.py kb/communities/Sichuan_Shai_Vinegar_Yeast_Flavor_SynCom.yaml` | Pass, 0 truncated scalars |
| `scripts/validate_shared_taxon_ids.py kb/communities/Sichuan_Shai_Vinegar_Yeast_Flavor_SynCom.yaml` | Pass, 0 reused IDs |
| `scripts/validate_prokaryotic_lineage.py kb/communities/Sichuan_Shai_Vinegar_Yeast_Flavor_SynCom.yaml` | Pass, 0 contradictory lineages |
| `git diff --check` | Pass |
| `python -m communitymech.network.auditor kb/communities/Sichuan_Shai_Vinegar_Yeast_Flavor_SynCom.yaml` | Not counted: module emitted only its `runpy` warning and no actionable diagnostics |

The generated HTML renderer also completed for the full corpus, rendering 407 community pages and regenerating `docs/browser.html` and `docs/index.html`.

## Identity and Grounding

The primary identity is sound. PubMed cache `references_cache/PMID_41344775.txt` identifies a 2026 Food Microbiology paper by Zhu et al. with DOI `10.1016/j.fm.2025.104983` and PMID `41344775`; its title matches the record scope.

A gitignore-independent duplicate search over `kb`, `data`, `history`, `reports`, `references_cache`, and `research/scouting` found this maintained record, its new history record, the new `PMID_41344775` cache, and prior scouting entries for the DOI/title. It did not find an older curated record for the same DOI or PMID.

The four curated yeast members are supported by the PubMed abstract and by ontology validation:

| Source name | Grounded term | Review |
|---|---|---|
| Saccharomyces cerevisiae | `NCBITaxon:4932` Saccharomyces cerevisiae | Sound |
| Pichia kudriavzevii | `NCBITaxon:4909` Pichia kudriavzevii | Sound |
| Kazachstania humilis | `NCBITaxon:51915` Maudiozyma humilis | Sound; record preserves the paper's older name in `preferred_term` and uses NCBI's current label |
| Brettanomyces bruxellensis | `NCBITaxon:5007` Brettanomyces bruxellensis | Sound |

The ENVO grounding to `ENVO:03600040` fermentation starter is reasonable for the starter-like synthetic community. The record correctly leaves GTDB lineages absent and marks all four fungal taxa as `NO_GTDB_EQUIVALENT`.

## Evidence

Supported by exact snippets:

- Engineering intent, source setting, co-culturing/metabolomics/simulated fermentation, and the optimized P. kudriavzevii / K. humilis / B. bruxellensis consortium are abstract-backed.
- Taxon membership is abstract-backed for all four yeasts.
- Division-of-labor roles are abstract-backed: P. kudriavzevii for ester synthesis, B. bruxellensis for acetaldehyde and 4-ethylguaiacol, K. humilis for acidification, and S. cerevisiae for ethanol provisioning.
- Ethanol, 4-ethylguaiacol, acetic-acid output, and pyruvate-mediated metabolic hubs are all named in the abstract.
- The PubMed and DOI external resources match the cached PMID record.

Unsupported or over-scoped:

- The Saccharomyces ethanol-provisioning edge uses `NCBITaxon:4751` Fungi for a `target_taxon` named "non-Saccharomyces yeast partners"; the cited sentence supports "other yeasts" in this four-member experiment, not all Fungi.
- The acetic-acid `RelatedIngredient` has an evidence snippet that stops at "achieving peak total acid" and therefore does not itself name acetic acid.
- `growth_media[].inoculum_source` currently holds the best-performing three-member output consortium rather than a source of inoculum. The abstract does not report strain accessions, inoculation ratios, inoculum density, or matrix setup.

## Completeness

The record includes the consequential abstract-level content: community identity, four yeast members, the three-member optimum, yeast role partitioning, principal flavor chemicals named in the abstract, PubMed/DOI resources, and an explicit knowledge gap for missing strain and solid-state-fermentation parameters.

The following optional slots are acceptably empty or absent:

- `modeled_environment`, because the physical environment and intended application are already represented by fermentation-starter grounding and SSV-specific prose.
- GTDB lineages, because all members are fungi.
- Metal and rare-earth arrays, because the paper's abstract is about yeast flavor formation rather than metal transformation or stress.
- Strain accessions, inoculation ratios, temperature, duration, vessel, and matrix composition, because those details are not present in the cached PubMed abstract.

No full text or supplementary cache was present for `PMID:41344775`; resolving the strain/protocol gap would require caching an open full text or a supplementary methods source if one is available.

## Findings

| ID | Severity | Finding | Maintained owner |
|---|---|---|---|
| CM-SICHUAN-001 | major | The `Saccharomyces ethanol provisioning for ester synthesis` interaction grounds its target as `NCBITaxon:4751` Fungi. That broad class is not a member of the curated record and scopes the edge far beyond the cited "other yeasts" in the four-yeast SSV experiment. | `kb/communities/Sichuan_Shai_Vinegar_Yeast_Flavor_SynCom.yaml` |
| CM-SICHUAN-002 | major | The acetic-acid related ingredient claims that acetic acid was a measured endpoint maximized by the triple consortium, but its nearest snippet says only "achieving peak total acid". The source sentence does support acetic acid, so the local evidence should quote the acetic-acid clause directly. | `kb/communities/Sichuan_Shai_Vinegar_Yeast_Flavor_SynCom.yaml` |
| CM-SICHUAN-003 | minor | The growth-media block puts the P. kudriavzevii / K. humilis / B. bruxellensis optimal consortium in `inoculum_source`. That slot should name the inoculum source when known; here the abstract only supports the optimal member set, and the record already says the inoculation details are absent. | `kb/communities/Sichuan_Shai_Vinegar_Yeast_Flavor_SynCom.yaml` |

## Recommended Edits

1. Replace the broad Fungi `target_taxon` in `Saccharomyces ethanol provisioning for ester synthesis` with `participating_taxa` entries for the curated yeast members involved in the four-species experiment, or otherwise remove the unsupported broad target while preserving the abstract-backed Saccharomyces-to-partner ethanol role.
2. Expand the acetic-acid related-ingredient snippet so it names acetic acid from the same sentence that reports peak total acid and acetic acid content.
3. Remove `growth_media[].inoculum_source`; keep the missing inoculation details in `preparation_notes` and the open discussion.
4. Append a new `curation_history` event for the review fixes, write the record through `write_validated_community`, add a new append-only `history/records/Sichuan_Shai_Vinegar_Yeast_Flavor_SynCom/*.yaml` entry, and regenerate `docs/`.

## Follow-up Checks

- Re-run schema, strict, term, snippet, reference, GTDB coherence, scalar, shared-taxon-ID, prokaryotic-lineage, and history validation on the edited files.
- Re-render `docs/communities/Sichuan_Shai_Vinegar_Yeast_Flavor_SynCom.html`, `docs/browser.html`, and `docs/index.html`.
- Re-read the changed interaction, ingredient, growth-media, curation-history, repository-history, and rendered HTML sections after generation.

## Additional Notes

The current pass reviewed only the committed PubMed abstract cache plus local schema and validator behavior. It did not fetch Elsevier full text, supplementary methods, or publisher tables.
