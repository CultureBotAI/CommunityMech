# YAML Record Review: Fucoidan Seven-Degrader Combinatorial SynCom

- Repository: CultureBotAI/CommunityMech
- Record: `kb/communities/Fucoidan_Seven_Degrader_Combinatorial_SynCom.yaml`
- Started UTC: 2026-09-27T10:50:32Z
- Finished UTC: 2026-09-27T10:58:32Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `MicrobialCommunity` |
| ID | `CommunityMech:000449` |
| Label | Fucoidan Seven-Degrader Combinatorial SynCom |
| Maintained path | `kb/communities/Fucoidan_Seven_Degrader_Combinatorial_SynCom.yaml` |
| Generated products reviewed | `docs/communities/Fucoidan_Seven_Degrader_Combinatorial_SynCom.html`, `docs/browser.html`, `docs/index.html` |
| History reviewed | `history/records/Fucoidan_Seven_Degrader_Combinatorial_SynCom/2026-09-27T105032Z-codex-fucoidan.yaml` |

The target is a maintained CommunityMech YAML record, not a generated overlay. Its generated HTML page, the browser card, and the landing-page count were regenerated from the YAML.

## Validation

| Check | Result |
|---|---|
| LinkML community schema, `../../culturebotai-claw/.venv/bin/linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Fucoidan_Seven_Degrader_Combinatorial_SynCom.yaml` | Pass, no issues found |
| LinkML history schema, `../../culturebotai-claw/.venv/bin/linkml-validate -s src/communitymech/schema/history.yaml --target-class HistoryRecord history/records/Fucoidan_Seven_Degrader_Combinatorial_SynCom/2026-09-27T105032Z-codex-fucoidan.yaml` | Pass, no issues found |
| Strict instance validator, `PYTHONPATH=src ../../culturebotai-claw/.venv/bin/python scripts/validate_strict.py kb/communities/Fucoidan_Seven_Degrader_Combinatorial_SynCom.yaml` | Pass, 0 errors |
| YAML scalar audit, `PYTHONPATH=src ../../culturebotai-claw/.venv/bin/python scripts/validate_yaml_scalars.py kb/communities/Fucoidan_Seven_Degrader_Combinatorial_SynCom.yaml` | Pass, 0 truncated scalars |
| Shared taxon IDs, `PYTHONPATH=src ../../culturebotai-claw/.venv/bin/python scripts/validate_shared_taxon_ids.py kb/communities/Fucoidan_Seven_Degrader_Combinatorial_SynCom.yaml` | Pass, 0 reused IDs |
| GTDB coherence, `PYTHONPATH=src ../../culturebotai-claw/.venv/bin/python scripts/validate_gtdb_coherence.py kb/communities/Fucoidan_Seven_Degrader_Combinatorial_SynCom.yaml` | Pass, 0 incoherent blocks, 0 malformed lineages, 0 lineage conflicts |
| Prokaryotic lineage coherence, `PYTHONPATH=src ../../culturebotai-claw/.venv/bin/python scripts/validate_prokaryotic_lineage.py kb/communities/Fucoidan_Seven_Degrader_Combinatorial_SynCom.yaml` | Pass, 0 contradictory lineages |
| Term label validation, `uvx --with 'linkml>=1.9.3' linkml-term-validator validate-data kb/communities/Fucoidan_Seven_Degrader_Combinatorial_SynCom.yaml -s src/communitymech/schema/communitymech.yaml --labels` | Pass |
| Generated page render | Pass, rendered 439 communities and regenerated the browser and landing page |
| Git whitespace validation, `git diff --check` | Pass |
| Official reference validator, `just validate-references kb/communities/Fucoidan_Seven_Degrader_Combinatorial_SynCom.yaml` | Not checked: local `uv run` fails while building `llvmlite==0.46.0` under Python 3.13 with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'` |
| Supplemental exact-snippet audit | Pass, all 48 evidence snippets matched the combined article and `PMID_42649294.supplement.md` caches after whitespace normalization |

## Identity and Grounding

The record denotes the full seven-member fucoidan-degrader combinatorial SynCom from PMID:42649294, assembled from F12, F40, F56, F94, V25, V69, and V4. The ID is newly minted as `CommunityMech:000449`; an ignored- and hidden-file-inclusive scan of `kb/communities` and `data/isolates` found the prior maximum `CommunityMech:000448` and no duplicate `CommunityMech:000449`.

The record preserves the source paper's boundary between the seven consistent degraders used for all 127 non-empty combinations and the context-dependent Pseudocolwellia degrader G88/AS88 that was excluded from that panel. The record also captures the Lentimonas CC4 alias edge case: Supplementary Table 2 and the full-combinatorial Methods name the member as V4, while one prose paragraph in the article says V43.

The grounding terms are appropriate for a defined, engineered laboratory SynCom:

| Field | Grounding | Review |
|---|---|---|
| `environment_term` | `ENVO:01001405` laboratory environment | Exact for the curated culture system |
| `modeled_environment` | `ENVO:01000320` marine environment | Appropriate for macroalgae-associated marine fucoidan degraders |
| Interaction process | `GO:0016052` carbohydrate catabolic process | Appropriate for community-level fucoidan catabolism |
| Member taxa | Seven NCBITaxon CURIEs plus strain designations and assembly accessions | Internally coherent and supported by Supplementary Table 2 rows |

## Evidence

All YAML evidence objects cite the stable primary PMID `PMID:42649294`. The cached Nature article supports the main-text and Methods snippets, and `references_cache/PMID_42649294.supplement.md` supports the Supplementary Table 2 genome, strain-code, and role snippets.

The nearest-evidence placement is sound:

- The full seven-member panel and equal-OD, MBL plus 0.2% Fucus vesiculosus fucoidan assembly are attached to `engineering_design`.
- Each member taxon carries evidence for its degrader identity, its assembly accession, the Supplementary Table 2 name/code mapping, and its fucose, rare-sugar, or generalist role.
- Community-level interaction claims are limited to complementary monomer degradation and the full-combinatorial synergism landscape.
- The five-day, 1.8 mL, triplicate, batch assay is attached to `growth_media` and `cultivation_setup`.
- External resources are limited to the DOI, PRJNA996876, Panorama, Zenodo, and two GitHub repositories named in Data or Code Availability.
- The two open discussions cite the exact source passages that motivate G88 exclusion and the V4/V43 alias.

No unsupported or over-scoped claims were found.

## Completeness

Consequentially complete. The record includes all seven members in the 127-community panel, keeps G88 out of the taxon list, records the source medium, volume, inoculum, duration, endpoint measurements, genome accessions, LC-MS/data/code resources, metal irrelevance, and curation history.

The intentionally empty metal fields are appropriate because PMID:42649294 studies enzymatic breakdown of brown-algal fucoidan rather than metal cycling. No temperature is asserted because the accessible article text did not state a temperature for the full-combinatorial endpoint cultures.

Duplicate checks used gitignore-independent searches:

- Searched `kb/communities` and `data/isolates` with ignored and hidden files included before minting `CommunityMech:000449`.
- Searched `kb`, `data`, `docs`, `references_cache`, `history`, and `reports` with ignored and hidden files included for `CommunityMech:000449`, `Fucoidan_Seven_Degrader_Combinatorial_SynCom`, `PMID:42649294`, `10.1038/s41586-026-10980-z`, `PRJNA996876`, and the seven assembly accessions.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Run the official `just validate-references kb/communities/Fucoidan_Seven_Degrader_Combinatorial_SynCom.yaml` once the local `uv run` dependency build is fixed.
- Re-run the focused LinkML, strict, term, history, GTDB, lineage, scalar, shared-taxon, render, and whitespace checks after any future edit to the record.

## Additional Notes

The local GTDB mapping bundle required by `scripts/gtdb_ground.py` was not present, so explicit GTDB status assignment was not applied. The new record passes the local GTDB coherence check because its `taxon_term` values are NCBITaxon-grounded and its GTDB notes do not assert `gtdb_status` blocks.
