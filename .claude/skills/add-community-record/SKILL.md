---
name: add-community-record
description: Discover and add evidence-backed CommunityMech communities through local
  scouting, identifier allocation and validated record writing; do not promote scouting
  stubs as records.
---

# Add a CommunityMech record

Use [scout-communities](../scout-communities/SKILL.md) to build a bounded candidate
frontier; inspect primary papers and reuse previously acquired research.
[deep-research-community](../deep-research-community/SKILL.md) is a separate
provider workflow whose spending requires existing authorization.
Search community names, source identifiers, exact membership and prior decisions
across `kb/communities/`, `data/isolates/`, `kb/taxa/`, research and history with
ignored files included. A title overlap is only a lead, not identity proof.

Read [manage-identifiers](../manage-identifiers/SKILL.md) and
[the current schema](../../../src/communitymech/schema/communitymech.yaml).
Allocate `CommunityMech:` IDs across **both** communities and isolates; check
again immediately before creation to avoid another session's allocation.
Scouting stubs under `research/scouting/stubs/` contain placeholder IDs and `_scout`
metadata and are not valid `MicrobialCommunity` records. Build from the current
class and nearest appropriate validated record, not historical skill examples.

Establish exact community scope, verified membership/strains, source-backed
interactions, environmental/growth context and claim evidence. Write with
`communitymech.validation.write_validated.write_validated_community` using the
correct root class; the default is `MicrobialCommunity`, while reusable taxon
records use `CommonTaxon`. Preserve native key order and use the curation event
helper plus append-only `just new-history` for actual additions.
Run `just validate <record-path>`, `just validate-strict <record-path>`,
`just validate-terms <record-path>`, `just validate-references-explained <record-path>`,
`just validate-history`, `just audit-writers`, `just gen-html`,
`just check-docs-current` and `just qc`. Reuse
[review-communities](../review-communities/SKILL.md) for its native rubric.

For an open discovery goal, maintain added/already-present/rejected/blocked
candidate dispositions. Re-query the recorded frontier after curation and report
no further admissible candidates only within that bounded source/query scope;
never claim that no undiscovered microbial communities exist.
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
