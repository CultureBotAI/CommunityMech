# CommunityMech record review checklist

Use this checklist for one `MicrobialCommunity` or `CommonTaxon`; it does not
require every optional field to be populated.

## Evidence standard

- An `EvidenceItem` needs a stable reference, `supports`, evidence source, and
  exact source snippet.
- Evidence belongs on the narrowest taxon, interaction, environment, or other
  assertion it supports.
- An association, co-occurrence, or enrichment does not establish ecological
  interaction direction or causality.
- A paper about a related strain or community is not evidence for the target
  without an explicit, justified scope relation.
- Record negative searches as bounded “not found” results.

## Field-by-field audit

| Area | Verify | Complete enough when |
|---|---|---|
| Identity/scope | ID, name, origin, category, ecological state, and experimental/natural scope agree. | The record denotes one clearly bounded community or reusable taxon. |
| Taxonomy | NCBITaxon/GTDB identity, canonical label, strain, lineage, and reusable-record link agree. | Every member is resolvable or explicitly uncertain without false precision. |
| Composition | Member inclusion, abundance/role wording, sampling state, and source scope match. | Composition does not combine incompatible time points, sites, or treatments. |
| Interactions | Source, target, interaction type, direction, scope, participants, and evidence agree. | Co-occurrence is not upgraded to interaction or causation. |
| Environment | ENVO term/label, modeled setting, parameters, units, and source context agree. | Natural, host-associated, and engineered contexts remain distinct. |
| Cultivation | Medium, ingredient, vessel, temperature, atmosphere, duration, and measured outcome match. | Conditions are attached to the experiment/community that actually used them. |
| Metals/metabolites | Identity, role, direction of exchange, and experimental support agree. | Presence is not treated as function and a measured analyte is not a causal actor without evidence. |
| Causal claims | Nodes exist, edges have the right direction/type, and every edge has evidence. | Mechanistic graphs preserve organism and experimental scope. |
| Datasets/resources | Identifier resolves and relevance is explicit. | The list is not a bibliography dump. |
| Discussions | Each item is a concrete unresolved question or conflict. | Checked sources and a resolution condition are named. |
| Audit | Per-record history and repository history reflect the exact change. | LLM assistance is explicit and prior history remains append-only. |
