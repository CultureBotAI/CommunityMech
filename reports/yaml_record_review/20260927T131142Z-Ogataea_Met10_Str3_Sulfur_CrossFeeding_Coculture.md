# YAML Record Review: Ogataea Met10-Str3 Sulfur Cross-Feeding Coculture

- Repository: `CultureBotAI/CommunityMech`
- Record: `kb/communities/Ogataea_Met10_Str3_Sulfur_CrossFeeding_Coculture.yaml`
- Started UTC: `2026-09-27T13:11:42Z`
- Finished UTC: `2026-09-27T13:12:56Z`
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `MicrobialCommunity` |
| ID | `CommunityMech:000450` |
| Label | Ogataea Met10-Str3 Sulfur Cross-Feeding Coculture |
| Maintained path | `kb/communities/Ogataea_Met10_Str3_Sulfur_CrossFeeding_Coculture.yaml` |
| Generated products | `docs/communities/Ogataea_Met10_Str3_Sulfur_CrossFeeding_Coculture.html`, `docs/browser.html`, `docs/index.html` |
| History | `history/records/Ogataea_Met10_Str3_Sulfur_CrossFeeding_Coculture/2026-09-27T130550Z-claude-code-bb4f27.yaml` |
| Primary reference | `PMID:42318495`; DOI `10.1016/j.synbio.2026.05.008` |

The record is a maintained community YAML for a two-member engineered `Ogataea polymorpha` sulfur-auxotroph coculture: `FY34 met10Δ-mCherry` and `FY31 str3Δ-EGFP`.

## Validation

| Check | Result |
|---|---|
| `../../culturebotai-claw/.venv/bin/linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Ogataea_Met10_Str3_Sulfur_CrossFeeding_Coculture.yaml` | Passed; no issues found. |
| `PYTHONPATH=src ../../culturebotai-claw/.venv/bin/python scripts/validate_strict.py kb/communities/Ogataea_Met10_Str3_Sulfur_CrossFeeding_Coculture.yaml` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `uvx --from linkml-term-validator linkml-term-validator validate-data kb/communities/Ogataea_Met10_Str3_Sulfur_CrossFeeding_Coculture.yaml -s src/communitymech/schema/communitymech.yaml --labels` | Passed. |
| `uvx --from linkml-reference-validator --with linkml linkml-reference-validator validate data kb/communities/Ogataea_Met10_Str3_Sulfur_CrossFeeding_Coculture.yaml -s src/communitymech/schema/communitymech.yaml --config conf/reference_validator.yaml` | Passed; all evidence snippets matched the committed `PMID:42318495` cache. |
| `PYTHONPATH=src ../../culturebotai-claw/.venv/bin/python scripts/validate_yaml_scalars.py kb/communities/Ogataea_Met10_Str3_Sulfur_CrossFeeding_Coculture.yaml` | Passed; 0 truncated scalars. |
| `PYTHONPATH=src ../../culturebotai-claw/.venv/bin/python scripts/validate_gtdb_coherence.py kb/communities/Ogataea_Met10_Str3_Sulfur_CrossFeeding_Coculture.yaml` | Passed; 0 incoherent GTDB blocks and 0 malformed or conflicting lineages. |
| `../../culturebotai-claw/.venv/bin/linkml-validate --schema src/communitymech/schema/history.yaml --target-class HistoryRecord history/records/Ogataea_Met10_Str3_Sulfur_CrossFeeding_Coculture/2026-09-27T130550Z-claude-code-bb4f27.yaml` | Passed; no issues found. |
| `PYTHONPATH=src ../../culturebotai-claw/.venv/bin/python scripts/audit_writers.py` | Passed. |
| `PYTHONPATH=src ../../culturebotai-claw/.venv/bin/python -m communitymech.render` twice, with SHA-1 comparison across the Ogataea page, `docs/browser.html`, and `docs/index.html` | Passed; the second render was byte-stable. |

## Identity and Grounding

The record identity agrees across the file name, `CommunityMech:000450`, the human label, the `SYNTHETIC` origin, `ENGINEERED` state, and the `BIOTECHNOLOGY` category.

The primary publication identity is consistent: the cached PubMed record and open-access full text both identify the article as "Engineering an asymmetric cross-feeding consortium in Ogataea polymorpha driven by sulfur metabolism" with `PMID:42318495`, `PMCID:PMC13273856`, and DOI `10.1016/j.synbio.2026.05.008`.

Both taxonomy entries are the tracked fluorescent strains described in the paper's methods. `FY31 (str3Δ-EGFP)` and `FY34 (met10Δ-mCherry)` are resolved to the species-level `NCBITaxon:460523` / `Ogataea polymorpha`, with the engineered strain designations preserved in `preferred_term` and `strain_designation`. `NO_GTDB_EQUIVALENT` is appropriate because this is a yeast and not a GTDB bacterial or archaeal genome.

An ignored- and hidden-file-inclusive search for `CommunityMech:000450` across `kb/communities`, `data/isolates`, `docs`, and `history`, excluding `.git`, `.env*`, and binary cached PDFs, found the identifier only in the new record, its new generated page, and its new history entry. A second ignored- and hidden-file-inclusive search for `42318495`, `10.1016/j.synbio.2026.05.008`, and the exact article title, excluding `.git`, `.env*`, cached PDFs, and the new Ogataea outputs, found only scout queues/reports under `research/scouting` and `tmp`.

## Evidence

The publication supports the record at the same scope the YAML claims:

- Engineering design: the source states that the study established auxotrophy-based cross-feeding in `O. polymorpha`, screened pairwise auxotrophic mutants, and selected `met10Δ-str3Δ` for robust reproducible complementation.
- Taxonomy and strain identity: the methods name `FY31 (str3Δ-EGFP)` and `FY34 (met10Δ-mCherry)`, describe construction in the `JQcr03L` background, and report PCR verification for gene deletions and fluorescent-marker integrations.
- Interaction support: the record separates broad growth complementation from the asymmetric sulfur-intermediate model and from initial-ratio-dependent composition shifts. That keeps direct flask/microplate growth observations distinct from the supplementation-based mechanistic inference.
- Methanol and glucose growth conditions: the glucose, methanol, initial OD600, ratio-series, temperature, shaking, vessel, and working-volume claims all have matching method snippets.
- Related sulfur intermediates: `L-cysteine`, `cystathionine`, and `homocysteine` are limited to the single-mutant supplementation result and are not claimed as directly measured coculture fluxes.
- External resources: the PMID and DOI entries are identifiers for the primary article, not a bibliography dump.

No unsupported, reversed, or over-scoped evidence claims were found. The record does not claim targeted metabolomics or isotopic proof of exchanged metabolites; it stays within the paper's supplementation assays and its proposed asymmetric exchange model.

## Completeness

The record is complete enough for the supported experimental scope:

- It records both community members, the engineered background, the two fluorescent reporters used for population tracking, and the `met10Δ:str3Δ` ratio series.
- It models both 20 g/L glucose and 10 or 20 g/L methanol Delft minimal media without inventing the full Delft salt recipe from the uncached supplement.
- It records shaken-flask batch cultivation and keeps plate-reader screening, flask validation, supplementation, and fluorescence-tracking endpoints out of a fictitious single protocol.
- It explicitly marks metal and rare-earth relevance as not applicable.
- It includes an append-only repository history record and an in-record `curation_history` item.

No causal graph is required for this record; the mechanism is already represented in `ecological_interactions`, and there is no direct metabolite-flux measurement to encode as a stronger causal edge.

## Findings

None found.

## Recommended Edits

None found.

## Follow-up Checks

Rerun these checks after any future edit to the maintained YAML:

- `linkml-validate` against `src/communitymech/schema/communitymech.yaml`
- `scripts/validate_strict.py`
- `linkml-term-validator validate-data --labels`
- `linkml-reference-validator validate data`
- `scripts/validate_yaml_scalars.py`
- `scripts/validate_gtdb_coherence.py`
- `linkml-validate --schema src/communitymech/schema/history.yaml --target-class HistoryRecord` for any new history entry
- `python -m communitymech.render`, followed by a docs idempotence or drift check

## Additional Notes

The documented `just` recipes dispatch through the same schema, reference config, validator scripts, and renderer targets used above. Direct command invocations were used for focused review because they allow the single-record checks to run without rebuilding the local `uv` environment.
