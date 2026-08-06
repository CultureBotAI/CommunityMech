"""A GTDB classification sitting on a taxon GTDB cannot classify (#365).

`NCBITaxon:169215` is the **plant** genus *Bosea* (Viridiplantae, Amaranthaceae).
Two records used it for the alphaproteobacterium of the same name and carried a
GTDB block derived from it, reading
`d__Bacteria;p__Pseudomonadota;...;g__Bosea`. The KB therefore asserted that a
plant genus is a bacterium, in a field that looked independently sourced.

The block came from a **name collision**, not a typo: `gtdb_ground.py`'s
higher-rank path matches on the cleaned label string rather than the id, so
"Bosea" resolved to the bacterial genus while the id pointed at the plant. The
bacterium is `NCBITaxon:85413`, which NCBI now labels *Allobosea* and aliases
"Bosea Das et al. 1996" — the two genera are homonyms, and the bacterial one was
renamed.

**No existing gate could see it.** `ncbi_source_id == term.id`, so the freshness
check from #364 passes. "Bosea" genuinely *is* `NCBITaxon:169215`'s label, so
id<->label correspondence passes. `linkml-validate` has nothing to say. And the
#292 shared-id gate cannot help either: the id appears once per record, so there
is no second organism to disagree with.

The signal needs no curation judgement: **GTDB classifies prokaryotes only.** A
taxon that is provably a eukaryote or a virus can therefore carry no GTDB
classification at all, whatever the block says. That makes this a contradiction
rather than a suspicion, and it would have caught the defect at write time.

**Only that one direction is checked**, deliberately. An earlier draft also
flagged an NCBI archaeon under `d__Bacteria` and the reverse, on the reasoning
that the two databases never disagree about domain. They do: 8 rows of the
repo's own `NCBI2GTDB.tsv.gz` disagree, and the gate fired on every block
`gtdb_ground.py` would build from them (#437). A gate that rejects its own
grounding tool's output is worse than no gate, so that arm is gone and only the
prokaryote-only rule — which has no counterexamples, because GTDB models no
other domain — remains.

Both taxonomy entries and interaction participants are walked: `source_taxon`
and `target_taxon` have the same range as `taxon_term`, so the schema permits a
GTDB block there too (#439), and both defective records named the plant id as an
interaction participant.

An id whose domain cannot be resolved is never judged — that covers a missing
NCBITaxon database, a taxid newer than the local snapshot, and any taxon above
the domain ranks such as `cellular organisms`.
"""

from __future__ import annotations

from communitymech.validators.ncbi_domain import (
    BACTERIA,
    EUKARYOTA,
    VIRUSES,
    domain_of,
    outside_gtdb_scope,
)

# Reusing `ncbi_domain` rather than re-deriving the lookup: an earlier draft of
# this module carried its own copy of the adapter, the four domain roots and the
# ancestor query, which is how two gates come to disagree about one taxon (#438).
#
# Only the two out-of-scope domains need naming here: `outside_gtdb_scope` is
# true for exactly these, so nothing else reaches the message.
OUT_OF_SCOPE_LABELS = {EUKARYOTA: "a eukaryote", VIRUSES: "a virus"}

_warned_no_adapter = False


def _warn_once_if_unavailable() -> None:
    """Say so when the check is being skipped rather than passed (cf. #426).

    Probes through the public `domain_of` rather than reaching for the adapter,
    so it cannot disagree with what the gate itself can resolve.
    """
    global _warned_no_adapter
    if not _warned_no_adapter and domain_of(BACTERIA) is None:
        _warned_no_adapter = True
        import sys

        print(
            "[gtdb-domain] NCBITaxon is unavailable, so the prokaryote-only check "
            "(#365) was skipped, not passed.",
            file=sys.stderr,
        )


def lineage_domain(lineage) -> str | None:
    """The domain a GTDB lineage string declares, or None if it declares none.

    Tolerates a non-string: `gtdb_lineage` has no `range` in the schema, so a
    YAML list or mapping is schema-valid and would otherwise raise here and
    abort the whole `validate-strict` run (#438, and #429 before it).
    """
    if not isinstance(lineage, str):
        return None
    head = lineage.split(";", 1)[0].strip()
    if head == "d__Bacteria":
        return "Bacteria"
    if head == "d__Archaea":
        return "Archaea"
    return None


def _descriptors(document):
    """Every taxon descriptor in a record, with where it was found.

    Yields `(where, block)`. Skips anything malformed rather than raising: this
    runs inside `validate_strict`, where an exception aborts the run and
    discards every other file's findings, and where the schema validator in the
    same pass diagnoses a malformed record properly (#429).
    """
    if not isinstance(document, dict):
        return
    for entry in document.get("taxonomy") or []:
        if isinstance(entry, dict) and isinstance(entry.get("taxon_term"), dict):
            yield "taxonomy", entry["taxon_term"]
    for interaction in document.get("ecological_interactions") or []:
        if not isinstance(interaction, dict):
            continue
        name = interaction.get("name") or "unnamed interaction"
        for role in ("source_taxon", "target_taxon"):
            block = interaction.get(role)
            if isinstance(block, dict):
                yield f"{role} of {name!r}", block


def check_record(document) -> list[str]:
    """Messages for each GTDB block on a taxon GTDB cannot classify."""
    _warn_once_if_unavailable()
    problems = []
    for where, block_owner in _descriptors(document):
        block = block_owner.get("gtdb_classification")
        if not isinstance(block, dict):
            continue
        term = block_owner.get("term")
        curie = term.get("id") if isinstance(term, dict) else None
        if not isinstance(curie, str) or not curie:
            continue
        if not outside_gtdb_scope(curie):
            continue
        actual = OUT_OF_SCOPE_LABELS.get(domain_of(curie) or "", "outside GTDB's scope")
        name = block_owner.get("preferred_term") or term.get("label") or curie
        declared = lineage_domain(block.get("gtdb_lineage"))
        says = f"a d__{declared} lineage" if declared else "a GTDB classification"
        problems.append(
            f"{curie} ({name!r}, in {where}) carries {says}, but the id is {actual} "
            f"— GTDB classifies prokaryotes only, so this id can carry no GTDB block at all."
        )
    return problems
