---
name: curate-causal-graphs
description: Review and curate CommunityMech ecological interaction downstream graphs
  with evidence for each directed causal claim, preserving taxon and experimental
  scope.
---

# CommunityMech causal interaction graphs

Read [the schema](../../../src/communitymech/schema/communitymech.yaml),
[ground-causal-graph-taxa](../ground-causal-graph-taxa/SKILL.md) and
[evidence-curation](../evidence-curation/SKILL.md).
The native graph is `MicrobialCommunity.ecological_interactions` with
`EcologicalInteraction.downstream` (`InteractionDownstream`), not a copied
TraitMech nodes/edges list. Inventory `kb/communities/*.yaml` and
`data/isolates/*.yaml`; read reusable `kb/taxa/` records that support a claim.

Review each interaction and downstream target, direction, mechanism, participant
and organism/condition scope against inspected primary sources. Preserve stable
interaction names and their `downstream[].target` references. Taxon membership, co-occurrence
and a metabolite correlation do not prove a causal chain. If evidence supports
only an interaction but not the proposed downstream link, retain the narrower
supported claim and record the unresolved step. Do not fabricate native slots.
The causal-edge mode of
[deep-research-community](../deep-research-community/SKILL.md) may supply leads;
it does not itself curate the graph or satisfy scientific review.

Use `communitymech.curate.curation_event.record_curation_event` and
`communitymech.validation.write_validated.write_validated_community`; append
actual repository history. Run community validation/strict/term/reference gates,
`just validate-history`, `just audit-writers`, `just qc`, then `just gen-html` and
`just check-docs-current` for changed communities. Verify downstream references
and citations explicitly even if a structural validator accepts them.
## Scope and completion

For one target, read the whole maintained record and its generated projection or
components. For a corpus goal, first freeze an inventory of record IDs, paths,
input hashes and applicable graph/protein elements; resume that ledger after an
interruption. Include hidden and ignored inputs when establishing absence.
Classify each target as checked, changed, evidence-limited, excluded, not
applicable or blocked, with reasons and inspected sources. A sample, a provider
report and a validator pass do not establish whole-corpus scientific completion.

Use [curate-yaml-record](../curate-yaml-record/SKILL.md) for the local evidence,
write, history and status contract; this adapter does not replace its managed
method. Record actual agent identity. Preserve scientific status rules and
unrelated edits. Use inspected primary evidence for mechanistic claims and exact
active identifiers for instances; never infer causality from association or
coverage from an empty query. A quotation is source text; interpretation belongs
in the native notes/explanation field.

Save final scientific assessments through
[review-yaml-record](../review-yaml-record/SKILL.md),
[record reviews](../../../docs/record-reviews.md), and the
[local profile](../../../docs/record-review-profile.md), including their native
persistence exceptions. Keep coverage/checkpoint accounting even when a clean
review should not produce a bundle. Unavailable prerequisites remain blocked;
a skipped target is not a completed enrichment. This skill authorizes no paid
provider call by itself.

After a completed goal, follow the user's authorized commit, push/PR,
adversarial review, issue/fix, merge and branch-cleanup sequence under the current
repository guidance. Carry forward existing authorization without asking again.
Use fresh required checks and native merge-queue rules. Verify actual merge and
landed content before deleting that feature branch or starting the next goal.
Only genuine review findings become issues; a no-diff goal needs a documented
no-op receipt rather than an artificial commit.
