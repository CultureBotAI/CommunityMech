# Named treatment arms and abundance observations

Treatment arms are optional, source-scoped experimental contexts. They let an
interaction or repeated abundance observation refer to a named assay arm without
copying the community's taxonomy. Existing records remain valid; their scalar
abundance values and interactions remain unscoped until a curator reviews and
assigns them explicitly. The schema work is tracked in [#2796](https://github.com/CultureBotAI/CommunityMech/issues/2796).

Give each referenced canonical taxonomy entry a stable `member_id` such as
`ecoli`. It is local to the record and identifies a member, not a taxonomic
CURIE: two strains may share the same taxon. Do not reuse an identifier for a
different stock. An arm's `id` and each arm-local timepoint's `id` are also stable
lowercase slugs. The [synthetic structural fixture](../tests/fixtures/treatment_arms.yaml)
shows the full field contract; its measurements are illustrative, not scientific
evidence.

Each `treatment_arms` entry requires `id`, `name`, `context`, and
`membership_status`. `context` names the assay/stage. `comparator_arm_ids` must
reference different arms with the identical context; a valid reference does not
by itself establish that two experiments are scientifically comparable.

| Membership status | Meaning | `participant_member_ids` |
|---|---|---|
| `DEFINED_MEMBERS` | The arm's complete microbial roster is stated | Nonempty, unique references to `taxonomy.member_id` |
| `NO_MICROBES` | The source explicitly describes a microbe-free arm | Omit |
| `NOT_REPORTED` | The source does not report that arm's microbial roster | Omit; empty does not mean none |

Hosts remain in `host`, not taxonomy. An earlier/larger source-study roster is
not the canonical membership of a later community. For example, initial 18- or
17-member assays must not become complete arms of a final 16-member record by
adding excluded stocks to its taxonomy. Retain such results as explicitly
separated source context/evidence or curate a distinct related community record.
Do not use `NOT_REPORTED` when the earlier roster is actually known.

Arm `conditions` use `EnvironmentalFactor` objects and retain source doses,
host-line descriptions and other context. `timepoints` are local to their arm;
two arms may both use `day-one`. A timepoint can have an `elapsed` duration,
whose `TimeQuantity` unit must descend from UO time unit (`UO:0000003`). An elapsed
duration requires an explicit `reference_event`, such as inoculation; never infer
that event from a number alone.

Store repeated `abundance_observations` under the existing taxonomy member. Each
observation requires `treatment_arm_id` and `measurement_basis`, plus at least
one abundance value. `timepoint_id`, `replicate`, description and evidence preserve
the source context. Repeated observations in the same arm/timepoint are allowed.

| Measurement | Required companion | Numerical boundary |
|---|---|---|
| `absolute_abundance` | `absolute_abundance_unit`, preserving the source unit | Finite and nonnegative |
| `relative_abundance` | `relative_abundance_unit`: `FRACTION` or `PERCENT` | Finite, 0–1 or 0–100 respectively |

An absolute count, CFU/mL and a read fraction are different measurements.
`measurement_basis` says what was measured; the model does not convert between
them. An observation cannot name a member excluded by the arm's complete roster
or assign a microbial measurement to a `NO_MICROBES` arm. Existing scalar
`relative_abundance_unit` remains free text for compatibility; the new enum
applies only to the new observations.

Interactions use `treatment_arm_ids`. Omission leaves a claim unscoped, rather
than making it true in every arm. Reference validity does not establish biological
participation, an effect direction, or a causal mechanism; these still need
source-based scientific review.

## Environmental-factor ontology grounding

[#2429](https://github.com/CultureBotAI/CommunityMech/issues/2429) adds optional
`EnvironmentalFactor.term: {id, label}`. The dynamic enum covers specific
descendants of chemical entity (`CHEBI:24431`), quality (`PATO:0000001`) or
environmental condition (`ENVO:01000203`). The roots were checked against the
retained OAK ontologies. They are excluded because a generic root is not useful
grounding for a specific factor; leave the optional term absent when a supported
specific term is unavailable. PATO is included in the normal ontology adapter
configurations, with no prefix exemption.

The term identifies the agent, quality or condition. Dose, timing and exposure
context remain in value/unit, arm context and evidence; the term alone does not
state an exposure event or a causal effect. Original name/value/unit fields stay
available without a term.

## Validation boundaries

Run `just validate-strict FILE` and `just validate-terms FILE` together with the
normal schema checks. The strict gate checks cross-field references, ambiguity,
membership and finite numerical values. The ontology gate checks the declared
dynamic ranges and labels. Schema-only success does not validate those cross-field
relations or scientifically approve a claim.

The current ontology binding engine accepts reflexive roots despite
`include_self: false` ([#2802](https://github.com/CultureBotAI/CommunityMech/issues/2802)).
The strict gate therefore explicitly rejects the three new environmental-factor
roots and the new elapsed-time unit root. This narrow guard does not replace
ontology descendant or label checks and does not claim to repair other bindings.

Explicit list declarations repair the generated loader's taxonomy and culture-
collection key failures while preserving canonical YAML lists. Whole-record
generated YAML reload remains a separate [#1703](https://github.com/CultureBotAI/CommunityMech/issues/1703)
limitation: the upstream generator serializes the existing interaction-scope enum
default as an object. The PAIRWISE schema default is retained; source dictionaries
and native schema/strict validation are unaffected. Generated-model component
checks are not a claim that every full record can be losslessly round-tripped.

Related-community `SHARED_STRAIN_DESIGNATIONS` remains an explicit curator stock
assertion. Strict validation now preserves every roster entry, rejects repeated
normalized local names and flags incompatible recorded taxon/deposit identifiers.
It retains assembly and modification metadata but does not treat a different
assembly version or different wording of a genotype description as proof of a
different stock. Matching local names and taxon IDs alone are not global stock
identity evidence; scientific review must verify the assertion.
