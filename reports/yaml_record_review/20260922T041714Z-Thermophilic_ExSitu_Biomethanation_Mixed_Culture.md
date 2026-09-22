# YAML Record Review: Thermophilic Ex-Situ Biomethanation Mixed Culture

- Repository: CommunityMech
- Record: `kb/communities/Thermophilic_ExSitu_Biomethanation_Mixed_Culture.yaml`
- Started UTC: 2026-09-22T04:10:00Z
- Finished UTC: 2026-09-22T04:17:14Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `kb/communities/Thermophilic_ExSitu_Biomethanation_Mixed_Culture.yaml` |
| Class | `MicrobialCommunity` |
| ID | `CommunityMech:000416` |
| Label | Thermophilic Ex-Situ Biomethanation Mixed Culture |
| Maintained/generated | Maintained canonical YAML under `kb/communities`; rendered HTML was regenerated under `docs/communities/` |
| Primary source | `PMID:42293522`, `doi:10.3389/fmicb.2026.1840981`, cached in `references_cache/PMID_42293522.txt` |

The target denotes one proof-of-concept, engineered, anaerobic-digestate-derived mixed microbial culture conditioned in a 0.4 L working-volume ex-situ H2/CO2 biomethanation CSTR, not the seed wastewater digestate in its native plant and not a later industrial continuous process.

## Validation

| Check | Result |
|---|---|
| `.venv/bin/linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Thermophilic_ExSitu_Biomethanation_Mixed_Culture.yaml` | Pass: no schema issues. |
| `PYTHONPATH=src .venv/bin/python scripts/validate_strict.py kb/communities/Thermophilic_ExSitu_Biomethanation_Mixed_Culture.yaml` | Pass: 1 file, 0 ERROR rows. |
| `.venv/bin/linkml-reference-validator validate data kb/communities/Thermophilic_ExSitu_Biomethanation_Mixed_Culture.yaml -s src/communitymech/schema/communitymech.yaml --config conf/reference_validator.yaml` | Pass: all `EvidenceItem` snippets matched the cached article/full-text cache. |
| `.venv/bin/linkml-term-validator validate-data kb/communities/Thermophilic_ExSitu_Biomethanation_Mixed_Culture.yaml -s src/communitymech/schema/communitymech.yaml --labels` | Pass: ontology CURIE/label pairs resolved. |
| `PYTHONPATH=src .venv/bin/python scripts/validate_gtdb_coherence.py kb/communities/Thermophilic_ExSitu_Biomethanation_Mixed_Culture.yaml` | Pass: all explicit GTDB states are internally coherent. |
| `PYTHONPATH=src .venv/bin/python scripts/validate_yaml_scalars.py kb/communities/Thermophilic_ExSitu_Biomethanation_Mixed_Culture.yaml` | Pass: no truncated scalars. |
| `PYTHONPATH=src .venv/bin/python scripts/validate_shared_taxon_ids.py kb/communities/Thermophilic_ExSitu_Biomethanation_Mixed_Culture.yaml` | Pass: no reused NCBITaxon IDs inside the new record. |
| `PYTHONPATH=src .venv/bin/python scripts/validate_prokaryotic_lineage.py kb/communities/Thermophilic_ExSitu_Biomethanation_Mixed_Culture.yaml` | Pass: no contradictory GTDB lineages. |
| `.venv/bin/linkml-validate --schema src/communitymech/schema/history.yaml --target-class HistoryRecord history/records/Thermophilic_ExSitu_Biomethanation_Mixed_Culture/2026-09-22T041407Z-claude-code-ec5722.yaml` | Pass: the append-only history record is valid. |
| `PYTHONPATH=src .venv/bin/python -m communitymech.cli audit-network --json` | Full-corpus command exited nonzero on pre-existing issues in other records. The JSON contained no `Thermophilic_ExSitu_Biomethanation_Mixed_Culture` entry, so the new record added no network issue. |
| `PYTHONPATH=src .venv/bin/python -m communitymech.render` | Pass: rendered 406 communities and produced `docs/communities/Thermophilic_ExSitu_Biomethanation_Mixed_Culture.html`, `docs/browser.html`, and `docs/index.html`. |

`just validate`, `just validate-strict`, `just validate-references-explained`, and `just new-history` were attempted but failed before reaching repository logic because `uv` tried to build `llvmlite==0.46.0` and hit the Python 3.13 `Popen(..., dry_run=...)` build error. The equivalent validators and renderer were rerun through the existing `.venv` executables.

`scripts/gtdb_ground.py --community ... --apply --apply-status` was attempted and reported that `NCBI2GTDB.tsv.gz` was absent from every default path it tried, including `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/NCBI2GTDB.tsv.gz`. The taxa are explicitly left `gtdb_grounding_status: UNRESOLVED`, which the GTDB-coherence validator accepts. Shallow `find` searches over the KG-Hub/KG-Microbe checkout area, including hidden names by default, located the candidate `kg-microbe` directories but not a usable `data/raw/NCBI2GTDB.tsv.gz`; broader archived project directories emitted permission-denied errors and were not treated as exhaustive.

## Identity and Grounding

The identifier is unique in the current corpus: the new `CommunityMech:000416` was minted after confirming first-line IDs in both `kb/communities/` and `data/isolates/` topped out at `CommunityMech:000415`.

The `ENGINEERED` state/origin and `METHANOGENESIS` category agree with the article. The source reports an operational strategy for autoclave pretreatment, thermophilic conditioning, and intermittent washouts in an H2/CO2-fed ex-situ biomethanation CSTR, so the record is scoped to the engineered culture rather than its source sludge alone.

The ENVO groundings are correct: the study system physically existed in a `bioreactor` (`ENVO:00002123`), while the modeled input material is `anaerobic digester sludge` (`ENVO:00003965`). The growth-medium and cultivation blocks preserve the distinction between filtered/autoclaved digestate as the cultivation matrix and the custom CSTR as the hardware.

NCBITaxon labels validated for all six taxonomic entries. The record intentionally distinguishes the 16S phylum-level final composition (`Euryarchaeota`, `Firmicutes`, `Coprothermobacterota`) from qPCR target groups (`Methanobacteria`, `Methanosarcina`, `Methanosaeta` resolved through the current NCBI genus label `Methanothrix`), avoiding unsupported strain or MAG assignments.

## Evidence

Every curated `EvidenceItem` cites `PMID:42293522`; the DOI and PMCID in the cache agree with PubMed metadata in `references_cache/PMID_42293522.txt`. The article cache includes an open-access full-text block from PMCID `PMC13256089`, which is necessary because the reactor configuration, phase-4 results, VFA composition, qPCR values, and industrial-robustness caveat sit outside the PubMed abstract.

The narrow evidence placement is sound:

| Claim area | Review |
|---|---|
| Engineering design | Autoclave pretreatment, H2/CO2 conditioning, intermittent washouts, and local mesophilic digestate source are directly supported by the article text. |
| Taxonomy | The phylum relative abundances are supported by the phase-4/day-69 16S text. The Methanobacteria/Methanosarcina/Methanosaeta absolute abundances are supported by the day-69 qPCR sentence plus the Figure 4 `gene copies/mL` axis text. |
| Interactions | The record uses `COMMUNITY_LEVEL` interactions for H2/CO2 methanation and VFA syntrophic turnover; the source interprets Firmicutes, Coprothermobacterota, Methanosaeta, Methanobacteria, and Methanosarcina roles at this group level, so the curation does not overstate a pairwise edge. |
| Environment and cultivation | The 50 C, 500 L/L/d, 4:1 H2:CO2, 25% phase-4 washout, atmospheric pressure, 0.4 L working volume, Rushton impeller, and heating claims all have exact snippets on the relevant factor/setup/media objects. |
| Discussions | Both knowledge-gap discussions are supported by article passages: one names phylum-level community resolution, and the other quotes the authors' non-sterile industrial-operation caveat. `linkml-reference-validator` does not inspect `SupportingReference` snippets, so these two discussion snippets were manually checked against the cache. |

## Completeness

The record carries the consequential source-supported material for this paper: engineered assembly, source inoculum, high-throughput thermophilic operating conditions, 16S/qPCR composition at the final reactor state, VFA and methane outcomes, community-level methanogenic/VFA-turnover interactions, cultivation hardware, and source-grounded open questions.

No species-level taxonomy, MAG accession, or pairwise bacterial-archaeal edge is asserted because the article does not resolve the final culture at that level. The inline `taxonomy_resolution` discussion correctly records that absence as a knowledge gap rather than filling optional fields with unsupported organisms.

The article's supplementary payload held no extractable prose when `scripts/cache_supplements.py PMID:42293522` was run, so no supplemental claims were curated. The article itself states that original contributions are included in the article/supplement and does not expose a public BioProject/SRA accession; omitting `associated_datasets` is therefore appropriate.

Duplicate checking before creation used `rg --no-ignore --hidden` over `kb data history docs references_cache reports research tmp` for `PMID:42293522`, the DOI, title fragments, and `1840981`; existing hits were scouting artifacts plus the newly cached source, with no pre-existing canonical YAML, docs page, history, or review report for this community.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Rerun `scripts/gtdb_ground.py --community kb/communities/Thermophilic_ExSitu_Biomethanation_Mixed_Culture.yaml --apply --apply-status` if `kg-microbe/data/raw/NCBI2GTDB.tsv.gz` becomes available locally.
- Rerun `just check-docs-current` after staging in an environment where `uv` no longer attempts to rebuild `llvmlite`; the direct renderer has already regenerated the affected docs.

## Additional Notes

The record deliberately uses ASCII in prose for `H2`, `CO2`, and `CH4`, while exact snippets retain source Unicode such as `H₂`, `CO₂`, and `×` where the cache requires it.
