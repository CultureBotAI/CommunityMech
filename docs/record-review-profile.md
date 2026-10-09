# CommunityMech Record Review Profile

Passing verdicts require positive evidence-linked assessments of the reviewed
targets. Terminal finding dispositions require those targets to have actually
been reviewed and assessed, with completion other than failed. Every
supersession must preserve all affected targets from the cited prior finding,
including multi-record findings; a narrower observation cannot silently drop
unassessed members or close their issues. Keep their remaining scope explicit.

Use [Structured Record Reviews](record-reviews.md) and the route/rubric inventory
in `conf/record_review.yaml`.

## Routes And Domain Evidence

- `review-yaml-record`: one resolved community, isolate or reusable taxon.
- `review-yaml-category`: coherent ecological/taxonomic/experimental cohorts
  with explicit membership, sampling and lump/split/retain/defer decisions.
- `review-communities`: per-record or explicit batch P1-P4 review.
- `curate-yaml-record`: the audit-only route uses the same saved output.
- `evidence-curation`: delegate final assessed evidence review to registered
  `review-communities`, saved with that route as `skill`. Extraction, repair
  suggestions and network diagnostics are not completed scientific review.
  Preserve per-record P1-P4, both scores and edge-level source/participant/
  direction/context evidence. No stale literature producer is recreated;
  paid/LLM calls need explicit authorization, and review-only work runs no
  repair/apply commands or status/history transitions.

Preserve the native validation rules, execution protocol, metrics and curation
checklist. Each reviewed record needs its own assessment and affected findings.
Record stable IDs, NCBITaxon/GTDB grounding, source strain, community scope,
experimental setting, medium and environmental context in evidence-linked
dimensions. A strain pair, enrichment or synthetic consortium does not establish
the same claim for a natural community.

For each ecological interaction and downstream causal edge, retain source and
target participants, direction, mechanism, context, exact field path, PMID/DOI,
source locator and inspected verbatim snippet. Network integrity and lexical
snippet similarity do not prove causal support. Evidence belongs at the specific
assertion. Keep abstract, full-text and supplementary evidence boundaries.

Retain `rule_id` and P1-P4 `native_severity` with explicit impact-based
`normalization_reason` (normally P1 blocker, P2 major, P3 minor, P4 informational).
Preserve the two distinct 0-100 native metrics from
`reference/metrics-and-reports.md`: completeness and validation quality.
Store each under assessment metrics with its formula/definition and scale;
record constituent issue counts and evidence-per-interaction denominator.
Neither score substitutes for scientific evidence or a release verdict.

## Ownership

Maintained records are `kb/communities/`, `data/isolates/` (MicrobialCommunity)
and `kb/taxa/` (CommonTaxon). Identify exact record paths and claim selectors.
The LinkML source schema owns data shape; generated Python, HTML and KGX are
derived. Trace generated defects to the record, template or exporter owner.
Hash all local schema/source/cache inputs actually used with `inspect --input`.
Do not patch generated Pages or append history during review-only work.

## Real Commands And Persistence

```bash
uv run python scripts/record_review.py inspect --targets /tmp/review-targets.yaml
just validate <record-path>
just validate-strict <record-path>
just validate-terms <record-path>
just validate-references-explained <record-path>
just audit-network
just check-network-quality
uv run python scripts/record_review.py validate /tmp/completed-review.yaml
uv run python scripts/record_review.py save --content /tmp/completed-review.yaml
just check-record-reviews
just test-record-reviews
```

For reusable taxa use `just validate-taxa` and `just validate-terms-taxa`.
Report their corpus scope honestly. Select GTDB/domain gates when relevant.
`just qc` retains lint/tests, schema/cross-field, GTDB, scalar and ontology
checks. Reference checking is separate: `just qc-references` may need network
access and is not silently counted as part of `qc`.

Use session-unique temporary inputs. New final reviews persist as authoritative
YAML and derived Markdown under `reviews/structured/<timestamp>-<slug>/`.
A sampled batch states selection, population, reviewed IDs, exclusions and limits.
Link both saved files. Missing required checks mean partial/blocked review.

`audit-network-json`, `audit-network-report`, linkage reports and validator
output are deterministic diagnostics. They may be evidence for an assessment,
but are not completed scientific review. A saved diagnostic-only assessment
uses `scientific_review: false`. Raw research output requires actual source and
edge-level assessment before saving a scientific review; no provider is invoked
by this contract.

## Retained Gates

There is no record-level REVIEWED flag. Keep guarded writes, claim evidence,
native schemas, network thresholds, reference checks and append-only history.
Saving a bundle neither authorizes curation nor records a status transition.
Native generated-docs checks remain required for changes to records/templates.
No historical reports or history entries are migrated. The shared schema,
helper, documentation and contract test remain byte-identical CLAW payloads;
local profiles, rubrics and scientific judgments are maintained here.
