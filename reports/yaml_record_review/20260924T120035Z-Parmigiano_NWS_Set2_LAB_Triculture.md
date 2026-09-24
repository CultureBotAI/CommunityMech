# YAML Record Review: Parmigiano NWS Set 2 LAB Triculture

- Repository: CultureBotAI/CommunityMech
- Record: `kb/communities/Parmigiano_NWS_Set2_LAB_Triculture.yaml`
- Started UTC: 2026-09-24T11:57:45Z
- Finished UTC: 2026-09-24T12:00:35Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `MicrobialCommunity` |
| ID | `CommunityMech:000431` |
| Label | Parmigiano NWS Set 2 LAB Triculture |
| Path | `kb/communities/Parmigiano_NWS_Set2_LAB_Triculture.yaml` |
| Maintained/generated | Maintained curated YAML, with generated HTML at `docs/communities/Parmigiano_NWS_Set2_LAB_Triculture.html` |
| Source provenance | `PMID:41859451`, DOI `10.3389/fmicb.2026.1755652`, cache `references_cache/PMID_41859451.txt` |

The record denotes the exact set 2 laboratory milk triculture from Cristofolini et al. 2026:
`Lactobacillus helveticus` LBB04, `Streptococcus thermophilus` C001.27, and
`Lactobacillus delbrueckii subsp. lactis` C5I3.

## Validation

| Check | Result |
|---|---|
| `just validate kb/communities/Parmigiano_NWS_Set2_LAB_Triculture.yaml` | Not run: the `uv run` wrapper attempts to build `llvmlite==0.46.0` under Python 3.13 before repository validation code runs. |
| `PYTHONPATH=src .venv/bin/linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Parmigiano_NWS_Set2_LAB_Triculture.yaml` | Passed, no issues found. |
| `PYTHONPATH=src .venv/bin/python scripts/validate_strict.py kb/communities/Parmigiano_NWS_Set2_LAB_Triculture.yaml` | Passed: 1 file scanned, 0 files with errors, 0 total error rows. |
| `PYTHONPATH=src .venv/bin/python scripts/validate_gtdb_coherence.py kb/communities/Parmigiano_NWS_Set2_LAB_Triculture.yaml` | Passed: 0 incoherent blocks, 0 malformed lineages, 0 lineage conflicts. |
| `PYTHONPATH=src .venv/bin/linkml-term-validator validate-data kb/communities/Parmigiano_NWS_Set2_LAB_Triculture.yaml -s src/communitymech/schema/communitymech.yaml --labels` | Passed. |
| `PYTHONPATH=src .venv/bin/python scripts/validate_shared_taxon_ids.py kb/communities/Parmigiano_NWS_Set2_LAB_Triculture.yaml` | Passed: 1 file checked, 0 reused ids. |
| `PYTHONPATH=src .venv/bin/python scripts/validate_yaml_scalars.py kb/communities/Parmigiano_NWS_Set2_LAB_Triculture.yaml history/records/Parmigiano_NWS_Set2_LAB_Triculture/2026-09-24T115836Z-codex-1077-1079.yaml` | Passed: 2 files checked, 0 truncated scalars. |
| `PYTHONPATH=src .venv/bin/linkml-validate -s src/communitymech/schema/history.yaml history/records/Parmigiano_NWS_Set2_LAB_Triculture/2026-09-24T115836Z-codex-1077-1079.yaml` | Passed, no issues found. |
| `PYTHONPATH=src .venv/bin/linkml-reference-validator validate data kb/communities/Parmigiano_NWS_Set2_LAB_Triculture.yaml -s src/communitymech/schema/communitymech.yaml --config conf/reference_validator.yaml` | Passed. The tool's summary printed `Total checks: 0`, so an exact-snippet traversal also checked all `PMID:41859451` snippets. |
| Exact-snippet traversal over `PMID:41859451` evidence snippets | Passed: 17 snippets, 0 misses against `references_cache/PMID_41859451.txt`. |
| `PYTHONPATH=src .venv/bin/python -m communitymech.render` | Passed: rendered 421 communities, regenerated `docs/browser.html`, and regenerated `docs/index.html`. |

## Identity and Grounding

The ID, label, ecological state, origin, and category are aligned: `CommunityMech:000431`
is a maintained engineered biotechnology record for a defined three-strain milk
fermentation triculture, not a natural whole natural-whey-starter community.

| Member | NCBITaxon | GTDB state |
|---|---|---|
| `Lactobacillus helveticus` LBB04 | `NCBITaxon:1587` | `UNRESOLVED`; no GTDB classification asserted because the local NCBI2GTDB crosswalk was unavailable during initial curation. |
| `Streptococcus thermophilus` C001.27 | `NCBITaxon:1308` | Grounded to `GTDB:s__Streptococcus_thermophilus`. |
| `Lactobacillus delbrueckii subsp. lactis` C5I3 | `NCBITaxon:29397` | `UNRESOLVED`; no GTDB classification asserted because the local NCBI2GTDB crosswalk was unavailable during initial curation. |

The three strain designations match the paper's set 2 cross-feeding panel.

## Evidence

Every evidence snippet in the YAML was verified as an exact substring of
`references_cache/PMID_41859451.txt`.

Supported exact claims include:

- The cross-feeding strains were natural-whey-starter isolates.
- Set 2 combined `L. helveticus` LBB04, `S. thermophilus` C001.27, and
  `L. delbrueckii subsp. lactis` C5I3.
- The milk fermentation design compared monocultures, 1:1 pairwise co-cultures,
  and 1:1:1 tricultures at a constant total final concentration.
- Cells were inoculated into 40 mL of partially skimmed UHT milk in 100 mL
  screw-cap Erlenmeyer flasks and incubated at 42 degrees C for 160 h.
- Across all inoculation sets, tricultures had the highest maximum acidification
  rates and total lactic acid production.
- In set 2, the C001.27/C5I3 pair produced maximum acidification rates
  comparable with tricultures, while the LBB04/C5I3 pair was weaker.
- Sets 1 and 2 had higher triculture D-lactate than the corresponding
  `L. delbrueckii` monocultures, supporting mixed-culture enhancement of the
  `L. delbrueckii` member without measuring the exact molecule-level exchange.
- The PubMed and DOI external resources identify the primary Frontiers in
  Microbiology article.

Unsupported or over-scoped claims: None found in the final reviewed record.

## Completeness

The record is complete enough for the source scope. It captures the exact
three-strain membership, engineered lab milk setting, NWS origin, cross-feeding
inoculation design, acidification and D-/L-lactate readouts, growth medium,
PubMed and DOI resources, and a knowledge gap that keeps the formate, folate,
urease, NADH oxidase, and antimicrobial-molecule explanations scoped as
hypotheses rather than exact set 2 measurements.

Optional slots correctly left empty:

- `functional_role`: the available enum lacks a generic milk-fermenter value,
  and the source does not prove the optional taxon-level cross-feeder role for
  every exact set 2 member.
- `related_media`: no CultureMech medium was asserted without running a
  CultureMech join.
- `datasets`: the record does not rely on a reusable sequencing dataset for
  this defined triculture.

Bounded duplicate search:

- `rg --no-ignore --hidden -n "CommunityMech:000431|Parmigiano_NWS_Set2_LAB_Triculture|41859451|10\\.3389/fmicb\\.2026\\.1755652" kb data history reports references_cache`
- The search included hidden and ignored files under those roots. Hits were the
  new community YAML, its new history entries, the `PMID_41859451` cache, and no
  pre-existing canonical record or exact-system duplicate.

## Findings

None found in the final reviewed record.

The adversarial pass on PR #1076 found and fixed three major findings:

- CommunityMech#1077: two acidification readouts used `interaction_type:
  MUTUALISM`, but the exact set 2 readouts proved improved acidification
  phenotypes rather than reciprocal benefit for all participating strains.
- CommunityMech#1078: the D-lactate interaction assigned the triculture
  D-lactate pool too specifically to C5I3, even though `L. helveticus` can also
  contribute D-lactate.
- CommunityMech#1079: every taxon carried `SECONDARY_FERMENTER` and
  `CROSS_FEEDER`, but the cited set 2 membership evidence did not support those
  optional role assignments.

## Recommended Edits

None remaining.

The issues above were addressed by removing the two unsupported `MUTUALISM`
values, removing the three unsupported `functional_role` lists, rewording the
C5I3 D-lactate interaction as a mixed-culture measurement, appending a
curation-history event, adding a new append-only history record, and
regenerating the Parmigiano HTML page.

## Follow-up Checks

- Re-run schema validation and strict validation after any YAML edit.
- Re-run `scripts/validate_gtdb_coherence.py` after any GTDB edit.
- Re-run the term validator after any ontology CURIE or label edit.
- Re-run exact-snippet traversal against `references_cache/PMID_41859451.txt`
  after any evidence edit.
- Regenerate `docs/` with `PYTHONPATH=src .venv/bin/python -m communitymech.render`
  after any community YAML edit.

## Additional Notes

The `just` wrappers around validators and renderers currently fail before
executing repository code because `uv run` attempts to build `llvmlite==0.46.0`
under Python 3.13. Direct `.venv` entry points were used for equivalent checks.

`references_cache/PMID_42385706.txt`, `references_cache/PMID_42602126.supplement.md`,
untracked files under `references_cache/files/`, and `reports/label_drift.tsv`
were already present before this review pass and are unrelated to the reviewed
YAML.
