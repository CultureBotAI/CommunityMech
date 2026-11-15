# Host, soil and related-community graph contexts

The exporter includes the `host`, `soils` and `related_communities` sections
introduced in PR #2102 (follow-up #2430). The first ten edge columns retain
their existing meaning. A new `communitymech_context` column contains JSON
with `field` and the exact enclosing `assertion`, including its evidence.
Consumers must retain this column to interpret these context edges precisely.

| Source section | Subject → object | Retained meaning |
| --- | --- | --- |
| `host` | Community → host NCBITaxon | Host association, with genotype, anatomy, stage, microbial status and qualifications from the descriptor. Never microbial membership. |
| Nested host terms | Community → ontology term | Descriptor-scoped term association; the JSON field identifies the qualified slot. |
| `soils` | Community → record-scoped soil descriptor | Distinct soil contexts with quantities, units, location, treatment, descriptions and evidence. |
| Nested soil terms | Soil descriptor → ontology term | The term's role within that descriptor, including units and texture. |
| `related_communities` | Containing community → named target | The original directed relation, basis, description and evidence, without conflating the six native relation kinds. |

All these edges use the broad `biolink:related_to` predicate and
`biolink:Association` category. This conservative mapping uses terms defined
in the [Biolink 4.3.6 model](https://github.com/biolink/biolink-model/blob/v4.3.6/biolink-model.yaml).
It does not assert a narrower biological predicate merely because two records
share members. In particular, `SAME_MEMBERSHIP_AS` is not entity identity,
`MEMBER_SUBSET_OF` is not ontological subclassing, and an inoculation host is
not necessarily a proven colonized habitat. The directed native assertion
remains in the JSON even though the broad Biolink predicate is symmetric.

NCBITaxon nodes use `biolink:OrganismTaxon`. Record-scoped soil descriptor nodes
and other contextual ontology nodes use `biolink:NamedThing`; the exporter
does not invent an accession for a physical sample. Ontology node names use
the saved canonical `term.label`; curator names remain in descriptor nodes
and the JSON assertion. Existing community nodes retain their previous
`biolink:OrganismalEntity` category.

Each edge receives evidence only from its enclosing descriptor or relation.
An unrelated community, environment or taxonomy citation is not borrowed.
Nested term edges carry the enclosing descriptor's evidence and full context;
they do not claim that the schema identifies a finer per-slot quotation.
Empty evidence stays empty, including computed membership relations whose
basis refers to the two curated strain rosters.

UUID5 identifiers are deterministic from the containing record, context kind
and canonical JSON assertion. Reordering input files, soils or relation entries
does not change graph bytes. Identical repeated soil entries remain separate
descriptor occurrences. Changing a context or its evidence creates a new
assertion identity; these identifiers are content identities, not permanent
accessions for real-world samples. Different relation kinds between the same
two records retain different edge identifiers and evidence.

The default export still emits claims from `kb/communities/*.yaml`. Its identity
catalog includes the shared community/isolate record roots so a linked isolate
gets its real name and a target node without importing all its claims. Custom
input directories are self-contained. Duplicate record IDs, malformed records
and unresolved related destinations fail before any graph product is written.
The export never silently creates an unnamed destination to conceal missing data.

The lightweight validator checks the extended column contract, context JSON
shape, duplicate graph IDs and endpoint closure. It does not certify full
Biolink semantic compliance or scientific truth. The existing id-label product
gate continues to inspect canonical labels in `nodes.tsv`.

Regression coverage lives in `tests/test_kgx_context_export.py`: distinct soil
measurements, host/member separation, canonical term labels, evidence isolation,
directed relation identity, deterministic order, duplicate/missing targets and
linked isolate resolution. Generated KGX artifacts remain under ignored
`output/kgx/` and are rebuilt for release and id-label checks.
