---
name: add-uniprot-protein-examples
description: Review CommunityMech taxon gene annotations and add verified UniProt
  identifiers with evidence linking exact proteins to community roles or interactions.
---

# CommunityMech UniProt gene/protein annotations

Read [the schema](../../../src/communitymech/schema/communitymech.yaml),
[ground-causal-graph-taxa](../ground-causal-graph-taxa/SKILL.md) and the full
community plus linked reusable taxon. The native protein route is
`CommonTaxon.genes[]` (`GeneAnnotation`), not a new `protein_examples` field on
community interactions. `gene_id` accepts a UniProtKB CURIE, with gene symbol,
locus, genome, GO terms, supported role/interaction and claim evidence where
appropriate under the current schema.

Inventory communities/isolates and referenced `kb/taxa/` genes. Resolve the
protein in the exact parent taxon and experimental context. Confirm any versioned
genome matches the parent's declared genome and that the source establishes the
role/interaction claimed. A gene annotation must not assert a role merely because
the family is present or a neighbor carries it. If a community-specific protein
example lacks a suitable native owner or relationship, record the representation
gap instead of inserting unsupported fields.

Write through `communitymech.validation.write_validated.write_validated_community`
with `target_class="CommonTaxon"` for reusable taxa, and append truthful curation
and repository history. Run `just validate-taxa`, `just validate-terms-taxa`,
`just validate-history`, `just audit-writers` and `just qc`; run the appropriate
community/reference and page-current gates when linked community content changes.
## Protein identity and evidence

Inspect live UniProt entry metadata or a release-pinned, provenance-verifiable
native snapshot. Check primary accession and active/merged/deleted state,
organism and strain, sequence/isoform, gene/locus mapping and source identity.
Prefer an exact assayed protein over a convenient ortholog. A named gene alone
is not a unique protein match. Keep family, whole complex, individual subunit,
native protein and experimental construct distinct. UniProt identity metadata
supports identity; primary role evidence supports participation in the record's
mechanism. Retain the original accession and an explicit mapping rationale when
resolving a changed identifier. Do not silently substitute species or isoforms.
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
