# Curating phage-bacteria communities

How to represent bacteriophages and the community dynamics they drive, and where
the schema currently stops. Read alongside `CLAUDE.md` and
`.claude/skills/curate-yaml-record/SKILL.md`.

## The complexity scale, and which part of it this KB holds

Phage biology is usefully organised by how many phages meet how many bacteria
(Selvakumar et al. 2026, `doi:10.1146/annurev-virology-100424-123645`):

| Scale | System | Fits a `MicrobialCommunity` record? |
|---|---|---|
| 1-1 | one phage, one clonal host | No — a pair is not a community |
| 1-N | one phage, a bacterial community | Yes — e.g. `CommunityMech:000467` |
| N-1 | a phage cocktail, one strain | Only if the record's subject is the community it is applied to |
| N-N | phage community, bacterial community | Yes — e.g. `CommunityMech:000468` |

The record root is a community, so 1-1 host-range data belongs in a record only
as evidence for an edge inside a community that actually has members. Do not
promote a strain pair to a community record; `CLAUDE.md` forbids generalising a
strain pair into a natural-community claim, and that applies here too.

The two curated exemplars are deliberately a matched pair. `CommunityMech:000467`
is a four-species assembly under experimental control where a single added phage
produces a measurable competitive release. `CommunityMech:000468` is an open
reactor community where a resident phage population drives rotating dominance.
Read them together before curating a third.

## Phages as members

A phage goes in `taxonomy` when it is part of the community — resident in the
sampled system, or added to it and replicating there. It does not when the
record's community is only its target, which is the same rule that keeps a
suppressed pathogen out of `taxonomy`.

- **Ground it in NCBITaxon.** Phages have NCBITaxon ids. Where only an
  uncultivated population is available (metagenomic pOTUs, vOTUs), ground at
  `NCBITaxon:10239` *Viruses* and say in `notes` what the population actually is.
- **Engineered derivatives.** NCBITaxon usually carries the parent phage species,
  not a lab derivative. Ground at the parent and name the derivative in
  `preferred_term` and `strain_designation.genetic_modification` — as
  `CommunityMech:000467` does for the lytic derivative DMS3vir of the temperate
  phage DMS3.
- **GTDB.** Always `NO_GTDB_EQUIVALENT`. GTDB covers Bacteria and Archaea; this
  is a final state, not an ungrounded gap.
- **Role.** `LYTIC_PHAGE` names the phage. A host is not given a functional role
  by being infected.

## Interaction types

| Value | Asserts | Needs |
|---|---|---|
| `LYTIC_INFECTION` | phage infects and lyses a host | the infection; host specificity if claimed |
| `LYSOGENIC_INFECTION` | temperate phage persists in a surviving host | the lysogenic state — integration, prophage carriage, induction — not just "the phage is temperate" |
| `COMPETITIVE_RELEASE` | suppressing one taxon lets a competitor expand | the competitor's expansion actually observed |
| `KILL_THE_WINNER` | predation falls on whoever is dominant, so dominance rotates | turnover over time, not one depletion |

Two traps worth naming:

**`PREDATION` is not a synonym for `LYTIC_INFECTION`.** A grazer removes biomass;
a lytic phage replicates within the host before lysis releases progeny viruses
and cellular contents. Host- or prey-density dependence alone does not
distinguish viral infection from grazing. Existing records that used
`PREDATION` for phage infection predate these values and have not been migrated.

**`COMPETITIVE_RELEASE` is weaker than `KILL_THE_WINNER`, and the gap is
evidential.** One release, observed once, is not a recurring feedback on
dominance. `CommunityMech:000467` records its kill-the-winner edge as `PARTIAL`
for exactly this reason: a 10-day experiment showed one such cycle.

## Where dynamics live, and where they do not

This is the live limitation, and curators hit it immediately.

`TaxonomicComposition` carries **one** abundance per member —
`abundance_level`, `relative_abundance`, `absolute_abundance` — with **no time
axis**. A record whose finding is a trajectory therefore cannot state that
trajectory in its composition.

The current convention, used by both exemplars:

1. Set `abundance_level` to a single defensible state and **say in the member's
   `evidence.explanation` which state it is**. `CommunityMech:000467` uses the
   phage-free baseline, so it reads `P. aeruginosa: DOMINANT` — the opposite of
   the record's point — and says so at the claim.
2. Put the trajectory in `ecological_interactions`, as a qualitative dynamic
   regime with its evidence. This is what `COMPETITIVE_RELEASE` and
   `KILL_THE_WINNER` are for.
3. Put per-timepoint numbers in `associated_datasets`, not in the record.

Both exemplars carry an open `CURATION_TODO` or `OPEN_QUESTION` discussion about
this, because the convention is a workaround and should be recognisable as one.
Whether CommunityMech should represent time-resolved composition at all is
undecided; it is a schema question, not a curation one, and should be settled
before the corpus accumulates more records that encode a baseline where a reader
expects an outcome.

A second gap, narrower: there is no slot for a **phage-resistance mechanism** or
its fitness cost. Receptor mutation versus defence system is the distinction that
governs whether a phage cocktail works, and it is currently prose inside an
interaction `description`.

## Modelling provenance

Phage-community papers lean on fitted models, and the type matters.

- `POPULATION_DYNAMIC_MODEL` — generalised Lotka-Volterra, ODE and chemostat
  formulations, predator-prey models, agent/individual-based simulations.
  Anything that integrates a dynamical law.
- `STATISTICAL_INFERENCE` — structural equation models, co-occurrence networks,
  correlation. Fits a structure; does not integrate a law. A SEM that the authors
  read causally is still this.
- `MACHINE_LEARNING` — protein language models over receptor-binding proteins,
  graph neural networks over infection networks.

**Record what the fit established, not what the framework assumes.** A fitted
model can fail informatively, and that failure is often the paper's result:
`CommunityMech:000467` curates a gLV parameterisation whose finding is that
pairwise coefficients do *not* predict the assembled community. Where a causal
direction rests on a fitted correlational model rather than a manipulation, mark
the evidence `PARTIAL` and say so in the `explanation`, as
`CommunityMech:000468` does for its SEM-inferred mechanism. Correlated turnover,
predicted defense genes, and AMG transcription are not themselves lytic
infections. Preserve these observations without an `interaction_type` when no
existing relation describes them, and retain computational provenance for the
prediction or statistical inference. Do not link a modeled mechanism to its
own supporting association as though two independent causal steps were measured.

## Evidence

The usual rules, with two phage-specific notes.

Both exemplars cite open-access papers whose full text is cached via
`just cache-fulltext PMID:<id>`, so Methods and Results snippets validate rather
than just abstracts. Cache the abstract first (the script requires it), then
append full text:

```bash
curl -sS "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=<pmid>&rettype=abstract&retmode=text" \
  -o references_cache/PMID_<pmid>.txt
just cache-fulltext PMID:<pmid>
```

Verify every snippet is an exact substring of the cache **before** writing it
into a record. `just validate-references` is the gate, but its clean output
reads "Total checks: 0", which is an issue count and not a check count — see the
justfile note. Checking substrings yourself first is cheaper than triaging that
output.

Finally: a review article is weak evidence for a specific community claim. The
Annual Review that motivates these values is cited in record `description` prose
for framing, and nowhere as an `EvidenceItem` reference. Primary sources carry
the claims.
