# YAML Record Review: Chinese Distillers Grains Dual Fungal Lignin Consortium

- Repository: CultureBotAI/CommunityMech
- Record: kb/communities/Chinese_Distillers_Grains_Dual_Fungal_Lignin_Consortium.yaml
- Started UTC: 2026-09-22T14:00:25Z
- Finished UTC: 2026-09-22T14:01:41Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MicrobialCommunity |
| ID | CommunityMech:000421 |
| Label | Chinese Distillers Grains Dual Fungal Lignin Consortium |
| Maintained path | kb/communities/Chinese_Distillers_Grains_Dual_Fungal_Lignin_Consortium.yaml |
| Generated page | docs/communities/Chinese_Distillers_Grains_Dual_Fungal_Lignin_Consortium.html |
| Primary source cache | references_cache/PMID_42660361.txt |
| Repository history | history/records/Chinese_Distillers_Grains_Dual_Fungal_Lignin_Consortium/2026-09-22T135255Z-codex-421.yaml |

The record is a maintained YAML community record, not a generated upstream transform.

## Validation

| Check | Result |
|---|---|
| `.venv/bin/linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Chinese_Distillers_Grains_Dual_Fungal_Lignin_Consortium.yaml` | Pass, no issues found. |
| `.venv/bin/linkml-validate -s src/communitymech/schema/history.yaml --target-class HistoryRecord history/records/Chinese_Distillers_Grains_Dual_Fungal_Lignin_Consortium/2026-09-22T135255Z-codex-421.yaml` | Pass, no issues found. |
| `.venv/bin/linkml-term-validator validate-data kb/communities/Chinese_Distillers_Grains_Dual_Fungal_Lignin_Consortium.yaml -s src/communitymech/schema/communitymech.yaml --labels` | Pass. |
| `PYTHONPATH=src .venv/bin/python scripts/validate_strict.py kb/communities/Chinese_Distillers_Grains_Dual_Fungal_Lignin_Consortium.yaml` | Pass, 0 files with errors. |
| `.venv/bin/linkml-reference-validator validate data kb/communities/Chinese_Distillers_Grains_Dual_Fungal_Lignin_Consortium.yaml -s src/communitymech/schema/communitymech.yaml --config conf/reference_validator.yaml` | Exit 0 but vacuous for this schema path: `Total checks: 0`. |
| `PYTHONPATH=src .venv/bin/python scripts/evidence_snippet_audit.py --list-mismatch --list-nocontent --list-rendering --list-assembled kb/communities/Chinese_Distillers_Grains_Dual_Fungal_Lignin_Consortium.yaml` | Pass, 16 snippets scanned: 16 `MATCH`, 0 `WEAK`, 0 `MISMATCH`, 0 `NOCONTENT`, 0 `RENDERING`, 0 `ASSEMBLED`. |
| `PYTHONPATH=src .venv/bin/python scripts/validate_yaml_scalars.py kb/communities/Chinese_Distillers_Grains_Dual_Fungal_Lignin_Consortium.yaml` | Pass. |
| `PYTHONPATH=src .venv/bin/python scripts/validate_gtdb_coherence.py kb/communities/Chinese_Distillers_Grains_Dual_Fungal_Lignin_Consortium.yaml` | Pass, 0 incoherent blocks, 0 malformed lineages, 0 lineage conflicts. |
| `PYTHONPATH=src .venv/bin/python scripts/validate_prokaryotic_lineage.py kb/communities/Chinese_Distillers_Grains_Dual_Fungal_Lignin_Consortium.yaml` | Pass, 0 contradictory lineages. |
| `PYTHONPATH=src .venv/bin/python scripts/validate_shared_taxon_ids.py kb/communities/Chinese_Distillers_Grains_Dual_Fungal_Lignin_Consortium.yaml` | Pass, 0 reused IDs. |

`just validate-history history/records/Chinese_Distillers_Grains_Dual_Fungal_Lignin_Consortium` and `just check-docs-current`
were attempted and failed before reaching repository logic because `uv run` attempted to build `llvmlite==0.46.0` under
Python 3.13 and hit `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`. The direct history
LinkML validation passed. The direct HTML renderer succeeded twice, and a `find`-based orphan check found no
`docs/communities/*.html` page lacking a matching `kb/communities/*.yaml` record.

## Identity and Grounding

The record identity is sound: it denotes the two-member Phanerochaete chrysosporium / Pleurotus eryngii solid-state
fermentation system constructed for lignin conversion in Chinese Distillers' grains in PMID:42660361, and the stable
DOI `10.1016/j.biortech.2026.135734` matches the PubMed metadata.

The fungal taxa are grounded at species rank to NCBI Taxonomy:

| Preferred term | Curie | Label | GTDB status | Verdict |
|---|---|---|---|---|
| Phanerochaete chrysosporium | NCBITaxon:2822231 | Phanerodontia chrysosporium | NO_GTDB_EQUIVALENT | Sound; the notes preserve the source's basionym versus NCBI's current scientific name. |
| Pleurotus eryngii | NCBITaxon:5323 | Pleurotus eryngii | NO_GTDB_EQUIVALENT | Sound; GTDB does not classify this eukaryotic fungus. |

The ENVO, CHEBI, and GO terms used in the record resolved with the expected labels.

## Evidence

Supported claims:

- PMID:42660361 directly names a dual-fungal solid-state fermentation system consisting of Phanerochaete chrysosporium and
  Pleurotus eryngii for lignin conversion in CDGs.
- The abstract directly reports 58.66% lignin degradation.
- The abstract directly reports day-10 laccase/manganese-peroxidase activity peaks and the day-15 lignin-peroxidase peak.
- The abstract directly reports a transcriptomic/metabolomic temporal division of labor in which P. chrysosporium dominates
  early AA2 peroxidase expression and P. eryngii dominates middle/late AA1 laccase and aromatic-catabolic pathways.
- The DOI and PubMed external resources match the inspected PubMed cache.

Unsupported or over-scoped claims:

- `engineering_design.assembly_strategy` says the two fungi were combined "to create a temporal division of labor." The
  abstract supports construction of the two-fungus system for lignin conversion and later discovery of a temporal division
  of labor, but it does not support temporal division as an intentional design strategy.

Misplaced claims:

- `environmental_factors` contains the 58.66% lignin degradation ratio and ligninolytic enzyme activity timing. Those values
  are measured outcomes of the fermentation, not environmental conditions or parameters.

## Completeness

The record correctly leaves strain designations, inoculation ratio, moisture, temperature, aeration, total fermentation
duration, and omics accessions unresolved. The open discussion names those missing method and accession details and points
at the full text as the source needed to resolve them.

An ignored-inclusive `rg --no-ignore --hidden` search across `kb/communities`, `data/isolates`, `references_cache`,
`history`, `reports`, `docs`, `research`, `src`, `scripts`, and `tests` for `42660361`,
`10.1016/j.biortech.2026.135734`, the exact article title, and the record slug found only the new record bundle plus
scouting leads under `research/scouting`; no separate full-text cache or older maintained record was present.

## Findings

| Severity | Finding | Maintained owner |
|---|---|---|
| Major | `engineering_design.assembly_strategy` converts an observed multi-omics result into a design intent by saying Phanerochaete chrysosporium and Pleurotus eryngii were combined "to create a temporal division of labor." The inspected abstract says the system was constructed for lignin conversion and that transcriptomics/metabolomics revealed a temporal division of labor; it does not say the consortium was assembled with temporal staging as an a priori strategy. | kb/communities/Chinese_Distillers_Grains_Dual_Fungal_Lignin_Consortium.yaml |
| Major | `environmental_factors` uses condition slots for two fermentation outcomes: `Lignin degradation ratio` and `Ligninolytic enzyme activity timing`. They should move to a result- or interaction-level representation so `environmental_factors` keeps describing CDG substrate/context rather than measured ligninolytic activity. | kb/communities/Chinese_Distillers_Grains_Dual_Fungal_Lignin_Consortium.yaml |

## Recommended Edits

1. Rewrite `engineering_design.assembly_strategy` to state only that the named fungi were paired in the constructed CDG
   solid-state fermentation system. Keep temporal division of labor as a measured outcome supported by the multi-omics
   evidence.
2. Remove the two outcome-valued `environmental_factors` entries. Preserve their quantitative evidence in a
   community-level lignin-conversion interaction, or another non-environmental slot, while leaving the CDG solid substrate
   as the sole environmental factor until full method conditions are available.
3. Add a `FIX_REVIEW_FINDINGS` curation event and a second append-only history YAML when the fixes are applied.
4. Regenerate `docs/` after editing the maintained YAML.

## Follow-up Checks

After the recommended edits:

- Rerun LinkML validation, term validation, strict validation, scalar validation, evidence snippet audit, GTDB coherence,
  prokaryotic-lineage, and duplicate taxon ID checks on
  `kb/communities/Chinese_Distillers_Grains_Dual_Fungal_Lignin_Consortium.yaml`.
- Rerun LinkML history validation on the new `history/records/Chinese_Distillers_Grains_Dual_Fungal_Lignin_Consortium/*.yaml`
  entry.
- Rerender `docs/` and verify no orphaned `docs/communities/*.html` pages exist.
- Run `git diff --check` before committing the review fixes.

## Additional Notes

No blocker findings were found. The review did not inspect the publisher full text or supplements, because the current
curated assertions were intentionally limited to the PubMed metadata/abstract cache.
