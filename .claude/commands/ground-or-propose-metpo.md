---
description: Deep-research the ungrounded ecological-interaction predicates/nodes and environmental-factor terms in the community KB; ground to METPO first (else RO/GO/ENVO/PATO/CHEBI), and where no good term exists, draft a METPO proposal. METPO-maximizing, not METPO-forcing.
argument-hint: "[interactions|factors|roles] [min-freq N | category C | label \"...\"]  (default: interactions+factors, min-freq 2)"
---

# Ground-or-propose residual community terms (METPO-first)

Goal: shrink the ungrounded residual in the community knowledge base. CommunityMech's
interaction graph (`ecological_interactions[].downstream[]`) is the direct analog of
TraitMech's causal graph: free-text interaction nodes linked by implicit edges, plus
free-text `environmental_factors[].name`. For **each recurring residual term**, either
(a) ground it to an existing ontology term — **METPO first**, then RO/GO/ENVO/PATO/CHEBI —
or (b) draft a **METPO proposal** when nothing fits. Maximize METPO coverage; mint only
when no good existing term exists anywhere.

`$ARGUMENTS` selects scope (default: both `interactions` and `factors`, only labels with
count ≥ 2; skip the freq-1 long tail). Examples:
`/ground-or-propose-metpo interactions min-freq 3` ·
`/ground-or-propose-metpo factors label "hydrogen partial pressure"`.

## The residual surfaces (re-scan each run — there is no standing report yet)
Scan all `kb/communities/*.yaml` and rank by frequency (highest first). The four surfaces:
- **Interaction predicates / nodes** — `ecological_interactions[].name` and
  `ecological_interactions[].downstream[].target` are free-text (e.g. "Interspecies
  Electron Transfer and Methanogenesis", "Acetate Utilization by Methanogens"). ~800–1300
  edges across 265 communities; this is the head — work it first.
- **Environmental factors** — `environmental_factors[].name` (e.g. "Low partial pressure
  of hydrogen", "pH 2–4", "Temperature range 15–40°C"); no PATO/ENVO binding today.
- **Interaction-type / functional-role enums** — `InteractionTypeEnum`,
  `FunctionalRoleEnum`, etc. Most are already lifted in the v1 cohort (see Inputs); only
  *new or unlifted* enum values belong here.
- **Biological processes** — `ecological_interactions[].biological_processes[]` whose GO id
  is missing/placeholder.

Emit the worklist as `reports/ungrounded_community_terms.tsv`
(cols: `surface, label, count, example_community, node_type, routing_hint`) so the run is
reproducible and the coverage delta is measurable.

## Inputs (read these)
- **Community KB:** `kb/communities/*.yaml` (the source of every residual term).
- **Schema:** `src/communitymech/schema/communitymech.yaml` — the enums and the
  `EcologicalInteraction` / `EnvironmentalFactor` / `TaxonomicComposition` classes.
- **METPO term inventory (search FIRST):**
  - In-repo cohorts already proposed — reuse their placeholder CURIEs, never re-mint them:
    `proposals/metpo_communitymech_v1/` (interaction-type, functional-role, abundance,
    atmosphere, media-relationship, metal-context, …; classes `METPO:1007100`–`1007315`
    plus `METPO:1008000`–`1008013`, predicates `METPO:2007100`–`2007201` and
    `METPO:2008000`–`2008002`) and
    `proposals/metpo_communitymech_cultivation_v1/` (cultivation enums; classes
    `METPO:1008100`–`1008132`, predicates `METPO:2008100`–`2008102`).
  - Staged vocab awaiting proposal: `vocab/cultivation_terms.yaml`.
  - Full ontology: the latest release `https://w3id.org/metpo/metpo.owl`
    (BioPortal "METPO") for terms not yet seeded into a cohort.
- **Where groundings/proposals go:** new groundings → `mappings/community_term_grounding.tsv`
  (create if absent); new proposal cohort under `proposals/`.
- **Conventions:** the `metpo-proposal` and `manage-identifiers` skills (METPO-first policy,
  ID reservation, ROBOT-template format, `definition_source` vs `xref` rule).

## Procedure

### 1. Build + cluster the worklist
Load the residual for the requested scope, apply min-freq/category/label filters, and
**deduplicate by meaning, casing, and format** — "Interspecies electron transfer" /
"Interspecies Electron Transfer (IET)" / "interspecies_electron_transfer" are one concept;
ground once and let it apply to every surface form. Cluster near-synonyms so one decision
(and at most one research query) covers the whole cluster.

Drop terms that are narrative artifacts, not reusable concepts (one-community paraphrases,
vague verbs like "supports", "involves") — record as `skipped: non-ontological`.

### 2. Tier-0 bulk grounding — no research needed (do this first)
A large share of the head is mechanical. Ground these directly; **do not** spend a
`/deep-research-community` call on them:

- **Interaction-type predicates → the v1 METPO cohort.** Map each `InteractionTypeEnum`
  surface form to its already-proposed `METPO:1007NNN` class / `METPO:2007NNN` predicate
  (`MUTUALISM`, `SYNTROPHY`, `CROSS_FEEDING`, `COMPETITION`, …). Record `skos:exactMatch`,
  `source: METPO`. These are settled — reuse, never re-propose.
- **Nodes / factors route by type** to a target ontology branch — search *that branch first*:
  | surface / node_type | search first | then |
  |---|---|---|
  | interaction-type predicate | **METPO** (v1 cohort) | RO |
  | ecological / metabolic process (downstream target) | GO:BP | METPO, MetaCyc xref |
  | metabolite named in an interaction | CHEBI | — |
  | functional role | **METPO** (v1 FunctionalRoleEnum) | — |
  | environmental factor — chemical (O₂, H₂, sulfide) | CHEBI | ENVO |
  | environmental factor — condition/quality (pH, temp, salinity, redox) | PATO | METPO, ENVO |
  | environmental factor — habitat/material | ENVO | — |
  | numeric value + unit | UO (unit) + PATO (quality) | — |
  | organism | NCBITaxon | — |
  Concrete chemicals/processes (methane, acetate, methanogenesis) live in CHEBI/GO, **not**
  METPO. METPO is the trait/phenotype/interaction-capability layer; don't force concrete
  molecules or GO processes into it.

After Tier-0, what remains is the ambiguous middle: interaction *capabilities* and
condition *qualities* where the right term (or whether one exists) is unclear.

### 3. Deep-research the ambiguous remainder — use `/deep-research-community`
For each *cluster* that survives Tier-0 (batch related terms into one question), invoke the
`deep-research-community` skill with a tightly-scoped query. Pass the node_type and routing
hint so the search starts in the right branch:

> Deep-research the microbial-community concept **"<term>"** (used as <an ecological
> interaction predicate | a downstream interaction node | an environmental factor>;
> context: <one line from the community YAML>).
> 1. Does **METPO** (https://w3id.org/metpo/metpo.owl, BioPortal "METPO") contain a
>    class/relation for this concept? Give the exact `METPO:` CURIE + label and the match
>    strength (exact / broad / narrow / close).
> 2. If METPO has none, is there a standard term in the expected branch
>    (<RO/GO for interactions and processes; CHEBI/ENVO/PATO/UO for factors>)? Give the
>    CURIE + match strength.
> 3. If neither has a good match, state that explicitly and propose a one-line Aristotelian
>    definition + the most likely METPO parent class for a new term.
> Prefer authoritative ontology sources; cite OLS/BioPortal/OBO. Be decisive about match
> strength; flag if the concept is too vague/idiosyncratic to be an ontology term.

### 4. Decide per concept (priority order)
1. **Strong METPO match** (exact/close, same concept) → ground to the `METPO:` CURIE. *Maximize this — it is the whole point.*
2. **No METPO, strong RO/GO/ENVO/PATO/CHEBI match** → ground to that CURIE. Reuse a real term before minting.
3. **No good existing term anywhere**, but the concept is **generic + recurring + reusable** → **METPO proposal** (new term).
4. **Vague / idiosyncratic / one-off** → leave residual; do not force a match or mint a term.

Verify every chosen CURIE actually resolves to that label (catch typos / obsolete terms);
the `id-label-correspondence` gate re-checks OAK-resolvable prefixes, but don't rely on it
for METPO.

### 5. Apply
- **Groundings** → append rows to `mappings/community_term_grounding.tsv` (create with header
  if absent): `surface, label, target_curie, target_label, predicate_id(skos:*Match), source,
  confidence, notes`. Where the schema has a binding slot (`metabolites[].term`,
  `biological_processes[].term`, `environment_term`), also write the id/label into the
  community YAML; for free-text `downstream[].target` and `environmental_factors[].name`
  there is no slot yet — record the grounding in the mapping TSV and note "needs schema slot"
  as a follow-up (do not invent a slot in this run).
- **Proposals** → follow the `metpo-proposal` skill: a fresh cohort
  `proposals/metpo_communitymech_v2/` (or `..._<topic>_v1/`), ROBOT-template rows
  (`metpo_proposal_classes_robot.tsv` 11 cols, `metpo_proposal_properties_robot.tsv` 12 cols)
  with Aristotelian definitions, parents, `definition_source` =
  `CommunityMech:communitymech.yaml#<…>` or `CommunityMech:kb/communities/<…>` (citations only
  — equivalents go to `xrefs`/SSSOM), placeholder IDs in the **next free block above every
  minted ID** (classes `1008140+` — `1007300`–`1007315`, `1008000`–`1008013`, and
  `1008100`–`1008132` are already used by the v1 cohorts; predicates `2007300+`), verified
  collision-free against the latest release. Then ground the motivating edges/factors to the proposed placeholder CURIEs
  (the documented round-trip swaps them for real IDs once METPO mints).

### 6. Verify + report
Run the gates and fix anything they flag:
`just validate-all` · `just validate-strict` · `just validate-products` (id↔label gate clean) ·
`just audit-network` (interaction directionality/partners) · `just check-network-quality`.
For a new proposal cohort, run the `metpo-proposal` checks
(`awk -F'\t' 'NF != 11'` column-count guard, enum-coverage, parent-integrity, ROBOT/ELK).

Report, against the prior coverage:
- new % of interaction predicates/nodes and environmental factors grounded, and the delta;
- counts: grounded-to-METPO vs grounded-to-RO/GO/ENVO/PATO/CHEBI vs proposed vs skipped-non-ontological;
- the Tier-0 bulk share vs the deep-researched share;
- the new proposal cohort summary (if any).

## Guardrails
- **METPO-maximizing, not METPO-forcing:** never ground a term to a METPO CURIE whose
  meaning doesn't actually match just to raise METPO %. A wrong grounding is worse than a residual.
- **Right layer:** concrete metabolites/processes belong in CHEBI/GO, environmental materials
  in ENVO, condition qualities in PATO; push interaction-capability and trait/phenotype concepts
  toward METPO.
- **Reuse the v1 cohorts:** interaction-type, functional-role, abundance, and cultivation enums
  are already proposed — ground to their placeholder CURIEs; never re-mint them.
- **Conservative proposals:** propose only genuinely reusable concepts (recurring across
  communities or a clear mechanistic primitive); one-offs are not ontology terms.
- **Don't over-research:** Tier-0 the mechanical head; spend `/deep-research-community` only on
  the ambiguous middle. Batch clusters into one query. Work in batches, commit per scope, keep
  the diff reviewable.
