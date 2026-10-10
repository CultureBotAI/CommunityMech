# YAML Record Review: Rice FSQN Rhizosphere Microbiome SynCom

- Repository: CultureBotAI/CommunityMech
- Record: `kb/communities/Rice_FSQN_Rhizosphere_Microbiome_SynCom.yaml`
- Started UTC: 2026-09-22T10:28:36Z
- Finished UTC: 2026-09-22T10:28:37Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `kb/communities/Rice_FSQN_Rhizosphere_Microbiome_SynCom.yaml` |
| Class | `MicrobialCommunity` |
| ID | `CommunityMech:000419` |
| Label | Rice FSQN Rhizosphere Microbiome SynCom |
| Maintained or generated | Maintained curated record |
| Category / state / origin | `RHIZOSPHERE` / `ENGINEERED` / `SYNTHETIC` |
| Primary source | `PMID:42596554`, `doi:10.1071/FP26125` |

The record denotes the Kossalbayev et al. four-strain FSQN rice inoculant composed of
`Bacillus amyloliquefaciens FH1`, `Ochrobactrum tritici S112`, `Gluconacetobacter
liquefaciens QZR14`, and `Brevundimonas diminuta NH1`. The scope is the PubMed
abstract-level community membership, high-throughput rhizosphere/root microbiome
sequencing result, predicted fungal-guild functional shift, and an explicit protocol
knowledge gap.

## Validation

| Check | Result |
|---|---|
| `linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Rice_FSQN_Rhizosphere_Microbiome_SynCom.yaml` | Pass, no issues found |
| `scripts/validate_strict.py kb/communities/Rice_FSQN_Rhizosphere_Microbiome_SynCom.yaml` | Pass, 1 file scanned and 0 ERROR rows |
| `linkml-term-validator validate-data ... --labels` | Pass, all ontology labels resolved |
| `scripts/evidence_snippet_audit.py --list-mismatch --list-rendering --list-assembled ...` | Pass, 11 `MATCH`, 0 `MISMATCH`, 0 `WEAK`, 0 `RENDERING`, 0 `ASSEMBLED`, 0 `NOCONTENT` |
| `scripts/validate_gtdb_coherence.py kb/communities/Rice_FSQN_Rhizosphere_Microbiome_SynCom.yaml` | Pass, 0 incoherent blocks, 0 malformed lineages, 0 lineage conflicts |
| `scripts/validate_yaml_scalars.py kb/communities/Rice_FSQN_Rhizosphere_Microbiome_SynCom.yaml` | Pass, 0 truncated scalars |
| `scripts/validate_shared_taxon_ids.py kb/communities/Rice_FSQN_Rhizosphere_Microbiome_SynCom.yaml` | Pass, 0 reused IDs |
| `scripts/validate_prokaryotic_lineage.py kb/communities/Rice_FSQN_Rhizosphere_Microbiome_SynCom.yaml` | Pass, 0 contradictory lineages |
| `communitymech.network.auditor.NetworkIntegrityAuditor().audit_community(...)` | Pass, `[]` |
| `linkml-validate -s src/communitymech/schema/history.yaml --target-class HistoryRecord history/records/Rice_FSQN_Rhizosphere_Microbiome_SynCom/2026-09-22T102525Z-codex-419.yaml` | Pass, no issues found |

The generated HTML renderer completed for the full corpus, rendering 409 community pages and
regenerating `docs/browser.html` and `docs/index.html`.

## Identity and Grounding

The primary identity is sound. The PubMed cache `references_cache/PMID_42596554.txt`
identifies a 2026 Functional Plant Biology paper by Kossalbayev et al. with DOI
`10.1071/FP26125` and PMID `42596554`; its title exactly matches the external-resource
snippet.

A gitignore-independent duplicate search over `kb`, `data`, `history`, `docs`,
`reports`, `research`, and `references_cache` found this new maintained record, its
generated documentation, its new history artifact, prior scout queue hits, and the new
PubMed cache. It did not find an older maintained curated record for the same PMID, DOI,
title, FSQN slug, or `CommunityMech:000419` before this curation.

The four curated members are supported by the PubMed abstract and by ontology validation:

| Source name | Grounded term | Review |
|---|---|---|
| Bacillus amyloliquefaciens FH1 | `NCBITaxon:1390` Bacillus amyloliquefaciens | Sound species-level NCBI grounding with the strain preserved separately |
| Ochrobactrum tritici S112 | `NCBITaxon:94626` Brucella tritici | Sound current NCBI grounding for the Ochrobactrum tritici name reported in the abstract |
| Gluconacetobacter liquefaciens QZR14 | `NCBITaxon:89584` Gluconacetobacter liquefaciens | Sound species-level NCBI grounding |
| Brevundimonas diminuta NH1 | `NCBITaxon:293` Brevundimonas diminuta | Sound species-level NCBI grounding with the strain preserved separately |

The local `kg-microbe` NCBI2GTDB crosswalk was unavailable, so every bacterial member is
explicitly marked `gtdb_grounding_status: UNRESOLVED`.

## Evidence

Supported by exact snippets:

- The four-strain FSQN composition is abstract-backed.
- The rice rhizosphere/root high-throughput sequencing endpoints are abstract-backed.
- The FSQN-associated beta-diversity and enriched-taxon shifts are abstract-backed.
- The fungal functional shift is correctly stored as `COMPUTATIONAL` evidence because the
  abstract says it came from functional prediction.
- The record correctly leaves culture medium, isolate sources, inoculum ratios, and rice growth
  protocol details as an open knowledge gap because those protocol details are absent from the
  PubMed abstract.

Unsupported or over-scoped:

- The beta-diversity interaction is typed as `COLONIZATION_FACILITATION`, but the PubMed
  abstract does not report that FSQN facilitated colonization.
- A `downstream` edge from beta-diversity/composition shifts to predicted fungal functions
  implies a causal order that is stronger than the abstract's paired readout of composition and
  functional-prediction results.

## Findings

| ID | Severity | Finding | Maintained owner |
|---|---|---|---|
| CM-FSQN-001 | major | `FSQN-induced rice microbiome beta-diversity shift` uses `interaction_type: COLONIZATION_FACILITATION`, but the evidence only supports FSQN-associated beta-diversity and enriched-taxon shifts after inoculation. | `kb/communities/Rice_FSQN_Rhizosphere_Microbiome_SynCom.yaml` |
| CM-FSQN-002 | minor | The `downstream` edge from `FSQN-induced rice microbiome beta-diversity shift` to `FSQN-associated predicted fungal functional shift` asserts an order not shown by the abstract. | `kb/communities/Rice_FSQN_Rhizosphere_Microbiome_SynCom.yaml` |

## Recommended Edits

1. Remove `interaction_type: COLONIZATION_FACILITATION` from the beta-diversity interaction.
2. Remove the unsupported `downstream` edge between the two FSQN interactions.
3. Append a `FIX_ADVERSARIAL_REVIEW_FINDINGS` curation event, add an append-only history entry,
   regenerate `docs/`, and re-run validators.

## Follow-up Checks

- Re-run schema, strict, term, snippet, GTDB coherence, scalar, shared-taxon-ID, prokaryotic-lineage,
  and history validation on the edited files.
- Re-render `docs/communities/Rice_FSQN_Rhizosphere_Microbiome_SynCom.html`, `docs/browser.html`,
  and `docs/index.html`.
- Re-read the changed interaction, curation-history, repository-history, and rendered HTML sections
  after generation.

## Additional Notes

The current pass reviewed only the committed PubMed abstract cache plus local schema and validator
behavior. It did not fetch CSIRO full text, supplementary methods, publisher tables, or raw
sequencing accessions.
