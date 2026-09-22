# YAML Record Review: Chlorella vulgaris Whey Co-culture

- Repository: CultureBotAI/CommunityMech
- Record: kb/communities/Chlorella_Vulgaris_Whey_Coculture.yaml
- Started UTC: 2026-09-22T15:15:44Z
- Finished UTC: 2026-09-22T15:15:44Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `kb/communities/Chlorella_Vulgaris_Whey_Coculture.yaml` |
| Class | `MicrobialCommunity` |
| ID | `CommunityMech:000422` |
| Label | `Chlorella vulgaris Whey Co-culture` |
| Maintained/generated | Maintained YAML record; `docs/communities/Chlorella_Vulgaris_Whey_Coculture.html`, `docs/browser.html`, and `docs/index.html` are generated from it |
| Primary source | `PMID:42249951`, DOI `10.1007/s00284-026-05004-y` |

The file denotes a synthetic laboratory microalgal co-culture from the Kelarijani et al. 2026 casein whey cultivation panel. The record is intentionally scoped to the two `Chlorella vulgaris` cultures named in the abstract, because the accessible PubMed cache names those two cultures and says the `Chlorella vulgaris` co-culture showed synergistic growth.

## Validation

| Check | Result |
|---|---|
| `.venv/bin/linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Chlorella_Vulgaris_Whey_Coculture.yaml` | Pass, no issues found |
| `.venv/bin/linkml-validate -s src/communitymech/schema/history.yaml --target-class HistoryRecord history/records/Chlorella_Vulgaris_Whey_Coculture/2026-09-22T150933Z-codex-422.yaml` | Pass, no issues found |
| `.venv/bin/linkml-term-validator validate-data kb/communities/Chlorella_Vulgaris_Whey_Coculture.yaml -s src/communitymech/schema/communitymech.yaml --labels` | Pass |
| `.venv/bin/linkml-reference-validator validate data kb/communities/Chlorella_Vulgaris_Whey_Coculture.yaml -s src/communitymech/schema/communitymech.yaml --config conf/reference_validator.yaml` | Pass |
| `PYTHONPATH=src .venv/bin/python scripts/evidence_snippet_audit.py --list-mismatch --list-nocontent --list-rendering --list-assembled kb/communities/Chlorella_Vulgaris_Whey_Coculture.yaml` | Pass; 10 snippets scanned, 10 matched, no rendering/assembled/weak/mismatch/nocontent hits |
| `PYTHONPATH=src .venv/bin/python scripts/validate_strict.py kb/communities/Chlorella_Vulgaris_Whey_Coculture.yaml` | Pass; one file scanned, zero errors |
| `PYTHONPATH=src .venv/bin/python scripts/validate_gtdb_coherence.py kb/communities/Chlorella_Vulgaris_Whey_Coculture.yaml` | Pass; one file checked, zero incoherent blocks or lineage conflicts |
| `PYTHONPATH=src .venv/bin/python scripts/validate_prokaryotic_lineage.py kb/communities/Chlorella_Vulgaris_Whey_Coculture.yaml` | Pass; one file checked, zero contradictory lineages |
| `PYTHONPATH=src .venv/bin/python scripts/validate_shared_taxon_ids.py kb/communities/Chlorella_Vulgaris_Whey_Coculture.yaml` | Pass; one file checked, zero reused IDs |
| `PYTHONPATH=src .venv/bin/python scripts/validate_yaml_scalars.py kb/communities/Chlorella_Vulgaris_Whey_Coculture.yaml` | Pass; one file checked, zero truncated scalars |
| `PYTHONPATH=src .venv/bin/python scripts/audit_writers.py` | Pass for this record; report-only writer audit completed |
| `PYTHONPATH=src .venv/bin/python -m communitymech.cli audit-network --check-only` | Failed with 14 unrelated warning-severity findings elsewhere in the corpus; JSON output had no `Chlorella_Vulgaris_Whey_Coculture` entry |

## Identity and Grounding

- `PMID:42249951` names four microalgae in the cultivation panel: `Scenedesmus sp. (SC)`, `Tetradesmus obliquus (TO)`, `Chlorella vulgaris Beijerinck (CVB)`, and `Chlorella vulgaris CCAP 211/19 (CV)`.
- The record's two taxonomy entries both ground to `NCBITaxon:3077`, canonical label `Chlorella vulgaris`, and correctly use `NO_GTDB_EQUIVALENT` because GTDB does not classify eukaryotic algae.
- A hidden, gitignore-independent search of `kb`, `data`, `history`, `docs`, `references_cache`, `reports`, and `research` for `CommunityMech:000422`, `PMID:42249951`, DOI `10.1007/s00284-026-05004-y`, and the publication title found only this new record/history/cache/rendered output plus scout leads. The same style of exact search across `kb/taxa`, `kb/communities`, and `data/isolates` found no existing `CCAP 211/19`, `CVB`, or `Chlorella vulgaris Beijerinck` YAML outside this record.
- A hidden, gitignore-independent search of `kb/taxa` for `Chlorella vulgaris` and `NCBITaxon:3077` found no reusable taxon record to reference.

## Evidence

Supported claims:

- The PubMed abstract supports that the study cultivated combinations of the four-microalga panel in casein whey-based media.
- The PubMed abstract supports that one pair combined two `Chlorella vulgaris` cultures and that this pair exhibited synergistic growth relative to single cultures and the four-species `MIX`.
- The PubMed cache supports the DOI and PMID external-resource identifiers.

Unsupported or over-scoped claims:

- The nitrogen-removal interaction assigns a broad abstract-level result for algal co-cultures to the exact two-member Chlorella pair. The abstract says microalgal co-cultures enhanced nitrate and ammonia removal, but it does not say the two-`Chlorella vulgaris` co-culture was the pair with improved nitrate or ammonia removal.
- `interaction_type: MUTUALISM` says both cultures benefited. The abstract supports synergistic aggregate growth of the pair, not a taxon-resolved `+/+` interaction.
- The first member's `strain_designation.strain_name: Chlorella vulgaris Beijerinck` treats `Beijerinck` as though it were a formal strain. In the abstract it appears in the binomial authority-like source label `Chlorella vulgaris Beijerinck (CVB)`, and no strain or culture-collection accession is available in the cached text.

## Completeness

- Exact strain accessions for the CVB culture, inoculation ratios, casein whey dilution and supplementation, light, temperature, vessel, duration, and per-combination biomass/nitrogen outcome values are absent from the PubMed abstract and are correctly represented as an open knowledge gap.
- No associated omics dataset, host, metal/REE, reusable taxon record, or exact CultureMech medium link is supported by the inspected cache.
- The PubMed abstract reports measured protein and nitrate maxima, but the abstract does not tie those maxima to the Chlorella pair.

## Findings

| Severity | Finding | Maintained owner |
|---|---|---|
| major | `Whey Nitrogen Removal by Microalgal Co-cultures` is over-scoped. It is represented as a `COMMUNITY_LEVEL` interaction for the two Chlorella members, but the cited abstract only assigns improved nitrate/ammonia removal to algal co-cultures generically. | `kb/communities/Chlorella_Vulgaris_Whey_Coculture.yaml` |
| major | `Chlorella Whey Growth Synergy` is typed as `MUTUALISM`, whose enum meaning is `+/+`. The evidence supports aggregate synergistic co-culture growth, but not that each Chlorella culture individually benefited from the other. | `kb/communities/Chlorella_Vulgaris_Whey_Coculture.yaml` |
| major | The first member stores `Chlorella vulgaris Beijerinck` as a formal strain designation even though the cached abstract only exposes the paper's CVB label and no strain accession for that culture. | `kb/communities/Chlorella_Vulgaris_Whey_Coculture.yaml` |

## Recommended Edits

1. Remove the `Whey Nitrogen Removal by Microalgal Co-cultures` ecological interaction and make the absence of pair-specific nitrate/ammonia values part of the existing open discussion. Regenerate `docs/` afterward.
2. Remove `interaction_type: MUTUALISM` from `Chlorella Whey Growth Synergy` while keeping its `COMMUNITY_LEVEL` scope and both participating taxa.
3. Rename the first member to `Chlorella vulgaris CVB`, store `CVB` as its observed strain/culture label, and explain in notes that the PubMed abstract expands CVB as `Chlorella vulgaris Beijerinck` but does not expose a formal accession.
4. Append a curation-history event and an append-only `history/records/Chlorella_Vulgaris_Whey_Coculture/` record for the fix.

## Follow-up Checks

- Re-run schema, term, strict, reference, GTDB, prokaryotic-lineage, shared-ID, scalar, and history validation against the edited files.
- Re-run `scripts/evidence_snippet_audit.py` on the edited YAML and confirm every retained snippet still has a cache match.
- Re-run `communitymech.cli audit-network --check-only` or `--json` and confirm it still has no finding for `Chlorella_Vulgaris_Whey_Coculture`.
- Re-run the HTML renderer and `git diff --check`.

## Additional Notes

- The record is a maintained YAML file; the HTML card and per-record page are generated outputs and should not be edited by hand.
- The existing full-corpus network audit had warning-severity findings in other records but no finding in `Chlorella_Vulgaris_Whey_Coculture`.
