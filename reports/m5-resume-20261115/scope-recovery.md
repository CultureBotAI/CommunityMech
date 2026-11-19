# Original M5 goals and ordered resumption

The current instruction is to resume **both scopes, Phase 2 first and the
all-record campaign afterward**. This inventory begins on
`68699871415fda3c9eebf20382a315f9f3c7b17a`. It neither resumes old deleted
batches nor creates new scientific reviews.

## Original corpus campaign

The preserved M5 session defined the population as the record skill's two
globs: `kb/communities/*.yaml` and `data/isolates/*.yaml`. A record counted as
reviewed when a validated bundle under `reviews/structured/` listed that
target, as determined by `scripts/record_review.py list`. That historical
criterion did not itself require current input bytes or full scientific
coverage.

The operational sequence was path order, one record per newly saved native
bundle, validation of every save, and publication in batches of ten through
fresh branches and PRs. The stop condition was every declared record reviewed,
or three consecutive review-validation failures. This original review request
did not grant canonical curation or merging authority.

The [coverage ledger](coverage.json) preserves that original presence criterion
and reports stronger assessed/scientific/full-record/current-byte subsets
separately. It does not silently reinterpret a completed historical campaign
as current scientific approval. Any renewed scientific campaign must select
work using the reviewed scope and retained findings, not merely the existence
of a YAML/Markdown pair.

## Later replacement and retained Phase 2 requirements

The later session explicitly superseded the original campaign, skipped
batches 17–46, and told the agent not to recreate deleted scratch or resume
the earlier goal. Other sessions had already published later review cycles.
The replacement first completed the old review-publication phase, beginning
with canary PR #2034 and ending with batch-16 PR #2062. This publication work
does not define an unfinished ten-record scientific batch.

Phase 2A covered the already merged PR #2102: its schema, four records, terms,
rendered documentation and products. The retained handoff stopped after a
reference failure and an incomplete audit recorded #2700–#2710. Phase 2B
required these additional capabilities:

- Named treatment arms that abundance and ecological-interaction assertions
  can reference explicitly.
- An ontology-term slot on `EnvironmentalFactor` (owner #2429).
- KGX export for `host`, `soils` and `related_communities` (owner #2430).
- Reconciliation or explicit documentation of the LBNL strain-roster and
  protocol problem (owner #1548).

The four PR #2102 records are `CommunityMech:000025` (EcoFAB), `000087`
(LBNL switchgrass), `000515` (Yolo soil microcosm) and `000516` (Brachypodium
dopamine SynCom). The original schema/render/validation findings #2700–#2707
need their own current-code acceptance checks. Membership and host-boundary
semantics constrain subsequent record changes; treatment-arm references must
use the final schema rather than an invented local convention. Named treatment
arms require explicit issue ownership before implementation; the retained
scope reconstruction did not establish one.

## Durable progress that remains usable

The [completion report](../m5-completion-20261114/README.md) preserves four
primary-source scientific assessments, an LBNL environment addendum, and a
three-record post-curation delta. They are immutable observations with exact
claim scopes and unresolved findings. This was deliberately narrower than
Phase 2 implementation or a whole-corpus scientific campaign.

That report records full native `qc` completion on
`e9ae9dee132ab210c87f76460c5d6247af9ea99c`, plus a separate completed reference
sweep with 549 targets and 103 errors across 14 records. The
[final reference inventory](../m5-completion-20261114/reference-sweep-final.json)
and [ownership triage](../m5-completion-20261114/reference-failure-triage-20261114.md)
retain each failure and its existing owner. A substring mismatch is a native
source-matching result, not a scientific verdict. The native `Total checks`
counter counts retained issues; zero is not an evidence-assertion coverage
measurement. The SupportingReference traversal gap is separately owned by #476.

Retained scientific findings include EcoFAB causal/protocol scope (#1427),
mapping provenance (#2674), genome identifiers (#2675), LBNL roster/protocol
scope (#1548) and study-setting distinction (#2776), and dopamine-community
grounding provenance (#2774). Each must be reassessed against the actual
source and current maintained input; an issue's state or a technical gate
alone cannot settle the scientific claim. Related LBNL records must be
reconciled when the source roster spans their ownership boundaries.

No earlier bundle is rewritten, and no issue is closed by this inventory.
Current PR/issue reconciliation and merge decisions are coordinated separately.

## Provenance and limits

The private preserved M5 session and retained scope snapshot supplied the
historical task sequence. Public reconstruction and input hashes are retained
in [the earlier scope report](../m5-completion-20261114/scope.md) and its
[machine-readable counterpart](../m5-completion-20261114/scope.json). The
instruction excerpt has SHA-256
`b670d34c6cdcec544ec409ad79e4e70d273541f5a14fb2342bbff548429f6934`; the stopped
handoff excerpt has SHA-256
`ac8d16aea620dfcb01b688500eded839fe29b86889d1dd6f8d6f51f8f0b92974`.
These identify the later replacement scope, not a newly constructed transcript
of the earlier goal. Raw session text, machine identities and personal paths
are not republished.

The earlier reconstruction recorded an ignored/hidden-inclusive inspection of
the original scratch directory and unavailable handoffs. Missing scratch is
not recreated or treated as evidence. This new inventory reads retained
native bundles and exact current Git paths, without providers, validators of
scientific claims, source/cache edits, or new scientific judgments.
