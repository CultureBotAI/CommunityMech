# ground-or-propose-metpo — run summary

## Worklist (reports/ungrounded_community_terms.tsv, freq>=2)
- interaction_name: 15 recurring (803 distinct incl. freq-1 tail, skipped)
- downstream_target: 13 recurring (76 distinct)
- env_factor: 32 recurring (537 distinct)
- bioprocess_no_go: 0 — all `biological_processes` already carry GO ids (prior id-label cleanup)

## Tier-0 grounded this run (mappings/community_term_grounding.tsv)
Environmental-factor condition qualities / referents (the clear mechanical head):
Temperature→PATO:0000146, pH & Extreme Acidity→PATO:0001842 acidity, Light→PATO:0015013,
Oxygen (availability/gradient/anaerobic)→CHEBI:15379 dioxygen, Hydrogen Partial
Pressure→CHEBI:18276 dihydrogen, Sulfate→CHEBI:16189, Iron→CHEBI:24875.
Skipped as non-ontological: "defined synthetic community design" (35×), "Source
environment", "Agricultural application" — narrative/design descriptors, not factors.

NB: `environmental_factors[].name` and `ecological_interactions[].downstream[].target`
have **no ontology binding slot** in the schema today, so these groundings are recorded
in the mapping TSV only. **Follow-up: add a `term` slot to EnvironmentalFactor** (and
optionally to InteractionDownstream) so the groundings can be written into the YAMLs and
enforced by the id↔label gate.

## Deferred (ambiguous middle — needs deep-research + possibly a METPO proposal cohort)
- Interaction `name` head (interspecies electron/hydrogen transfer, chain elongation,
  DIET+methanogenesis, plant growth promotion, …): mostly **compound narrative labels**;
  their primary semantics already live in `interaction_type` (grounded to the v1 METPO
  cohort). Reusable primitives worth a METPO/RO/GO decision: "interspecies electron
  transfer", "interspecies hydrogen transfer", "cross-feeding" (already METPO v1),
  "plant growth promotion".
- downstream_target mineral-dissolution/redox nodes (pyrite/chalcopyrite/bastnaesite
  dissolution, iron oxidation): GO/CHEBI-adjacent, no slot.
These are a bounded next batch (≈10–15 `deep-research-community` cluster queries + one
`proposals/metpo_communitymech_v2/` cohort), not run here.
