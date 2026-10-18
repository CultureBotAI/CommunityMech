"""Every `TaxonDescriptor` in a record, whatever root class the record has (#656).

The GTDB slots — `gtdb_grounding_status`, `gtdb_candidates`,
`gtdb_classification` — live on `TaxonDescriptor`, and the schema hangs that
class off two different roots:

    MicrobialCommunity.taxonomy[].taxon_term                        -> TaxonDescriptor
    CommonTaxon.taxon_term                                          -> TaxonDescriptor
    EcologicalInteraction.source_taxon / target_taxon               -> TaxonDescriptor
    EcologicalInteraction.participating_taxa[]                      -> TaxonDescriptor
     EngineeringDesign.counter_selection[].excluded_taxon           -> TaxonDescriptor

`CommonTaxon` records live in `kb/taxa` and carry `taxon_term` at the **top
level**, with no `taxonomy` key at all.

That difference made a directory fix insufficient in a way worth recording.
Three GTDB gates each carried `RECORD_DIRS = ("kb/communities",
"data/isolates")`; adding `kb/taxa` to that list looked like the whole fix and
was not, because their walkers iterate `document["taxonomy"]` and a
`CommonTaxon` has none. Planting a `NOT_ATTEMPTED` grounding in `kb/taxa` still
produced a green run. A gate can be pointed at a directory and still be blind to
everything in it.

Interaction endpoints (`source_taxon`, `target_taxon`), multi-taxon
`participating_taxa`, and `engineering_design.counter_selection[].excluded_taxon`
are included because they share `taxon_term`'s `TaxonDescriptor` range, so the
schema permits a grounding there too — the same reasoning
`gtdb_lineage_tree._descriptors` documents. None exist today.
"""

from __future__ import annotations

from collections.abc import Iterator


def iter_taxon_descriptors(document: object) -> Iterator[dict]:
    """Yield each `TaxonDescriptor` block in a parsed record.

    Malformed nodes are skipped rather than raising: callers include gates that
    sweep the whole corpus, where one bad record must not discard every other
    record's findings (the #429 rule).
    """
    if not isinstance(document, dict):
        return

    # CommonTaxon: the descriptor is the record's own subject.
    top_level = document.get("taxon_term")
    if isinstance(top_level, dict):
        yield top_level

    # MicrobialCommunity: one descriptor per member.
    for entry in document.get("taxonomy") or []:
        if isinstance(entry, dict) and isinstance(entry.get("taxon_term"), dict):
            yield entry["taxon_term"]

    # Interaction endpoints and participants share TaxonDescriptor's range.
    for interaction in document.get("ecological_interactions") or []:
        if not isinstance(interaction, dict):
            continue
        for role in ("source_taxon", "target_taxon"):
            block = interaction.get(role)
            if isinstance(block, dict):
                yield block
        for participant in interaction.get("participating_taxa") or []:
            if isinstance(participant, dict):
                yield participant

    # Counter-selection excluded_taxon also has range TaxonDescriptor.
    eng = document.get("engineering_design")
    if isinstance(eng, dict):
        for cs in eng.get("counter_selection") or []:
            if isinstance(cs, dict) and isinstance(cs.get("excluded_taxon"), dict):
                yield cs["excluded_taxon"]
