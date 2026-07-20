# Microbial Community Causal-Graph Research Template

## Target Community
- **Community name:** {community_name}
- **Community id:** {community_id}
- **Community file:** {community_file}
- **Community category:** {community_category}
- **Ecological state:** {ecological_state}
- **Community origin:** {community_origin}
- **Environment:** {environment_summary}
- **Description:** {description}

## Existing Record Context
- **Taxa:** {taxonomy_summary}
- **Known ecological interactions:** {interaction_summary}
- **Environmental factors:** {environmental_factor_summary}
- **Growth media / culture conditions:** {growth_media_summary}
- **Associated datasets / resources:** {dataset_summary}
- **Existing evidence:** {evidence_summary}

## Research Objective

Build a source-backed **causal interaction graph** for the microbial community
**{community_name}**, suitable for the `ecological_interactions` block of
`kb/communities/{community_file}`. The graph's **nodes are mechanistic
interactions** and its **directed edges are causal links** ("interaction A
enables / drives / suppresses interaction B"). Extract only relationships the
primary literature supports; do not infer edges that are not stated or directly
implied by an experiment.

## Required Findings

### 1. Interaction nodes (the vertices)

For each mechanistic interaction, report as a table row:

- **name** — a short, unique interaction name (used as the node id and as the
  `target` of any causal edge that points to it).
- **interaction_type** — one of: MUTUALISM, COMMENSALISM, CROSS_FEEDING,
  COMPETITION, PREDATION, SYNTROPHY, NICHE_PARTITIONING, STRAIN_COMPETITION,
  COLONIZATION_FACILITATION (or state "OTHER: <describe>" if none fit).
- **scope** — PAIRWISE (organism→organism) or COMMUNITY_LEVEL (emergent /
  abiotically driven, e.g. electrolysis-supplied H2). PAIRWISE **must** name a
  source taxon.
- **source_taxon → target_taxon** — the directed pair (who acts on whom). Give
  NCBITaxon CURIEs + labels where resolvable.
- **metabolites / biological_processes** — the exchanged compound(s) (CHEBI) and
  process(es) (GO) that mediate the interaction.
- **direction / sign** — does the source **increase (+)** or **decrease (−)** the
  target's growth/activity? State it explicitly.
- **evidence** — a short **verbatim** snippet + its reference (PMID/DOI).

### 2. Causal edges (the arcs)

This is the graph structure. For every ordered pair of nodes where the
literature supports a causal link, report a row:

- **from** — upstream interaction name (a node from §1).
- **to** — downstream interaction name (a node from §1).
- **causal link** — one sentence: *how* the upstream interaction causes /
  enables / is required for / suppresses the downstream one (e.g. "H2 produced
  by the syntrophic oxidation lowers pH2 enough for the acetogen to grow, which
  in turn supplies acetate to the methanogen").
- **evidence** — verbatim snippet + reference for the causal claim specifically
  (not just for the two endpoints existing).

Prefer chains that a paper demonstrates by perturbation (knockout, substrate
removal, inhibitor, co-culture vs mono-culture), and say which experiment shows
each edge. Flag any edge that is hypothesized rather than demonstrated.

### 3. Grounding

- CURIEs where available: NCBITaxon (taxa), CHEBI (metabolites), GO (processes),
  ENVO (environment), PMID / DOI (evidence).
- Do not invent taxa, ontology ids, snippets, accession ids, or citations. If a
  node or edge lacks a citable source, omit it or mark it UNVERIFIED.

## Output Format

Return a curation-focused report with:

1. **Scope summary** — the consortium and the top-level function the causal graph
   explains (1–3 sentences).
2. **Node table** — the interaction nodes (§1 columns).
3. **Edge table** — the directed causal edges (§2 columns: from, to, causal
   link, evidence).
4. **Adjacency / DOT sketch** — a compact `from -> to` edge list (or Graphviz DOT
   snippet) so the graph can be eyeballed; annotate edges with + / − sign.
5. **Gaps & controversies** — edges the literature disputes, or plausible edges
   with no direct evidence (candidates for a `Discussion`/knowledge-gap note).
6. **References** — every PMID/DOI cited, once.

Each biological claim (node and edge) must carry a verbatim snippet and a
reference. This report is reviewed by a curator before anything is written to
`kb/communities/`.
