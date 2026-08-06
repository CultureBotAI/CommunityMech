"""One GTDB taxon under two different parent lineages (#454).

`gtdb_lineage` is a denormalised path — `d__Bacteria;p__Bacteroidota;c__Chlorobiia`
— and until #450 every one was written by `gtdb_ground.py` from the crosswalk,
so nothing needed to check the middle of it. The freshness checks compare
`gtdb_id`, `gtdb_taxon` and the lineage's *tail*; the prokaryote-only gate
(#365) reads its *head*. Corrupting a segment in between passed everything:

    d__Bacteria;p__Bacteroidota;c__Chlorobiia
    d__Archaea;p__Nonsense;c__Chlorobiia        <- still passes both

#450 made seven of those lineages **hand-written** curator pins, which is when
that stopped being theoretical.

The check needs no crosswalk, which is what makes it usable in CI — the
kg-microbe checkout is not there, so anything asking the mapping a question
would skip. GTDB is a strict hierarchy, so **a taxon has exactly one parent**.
Read every block's lineage as a set of (taxon, path-above-it) pairs and a
segment appearing under two different paths is a contradiction between two
records, whichever of them is wrong.

That is a weaker claim than "this lineage matches GTDB" and a much cheaper one.
It cannot catch a corruption that is internally consistent — a taxon named in
one record only, spelled wrongly throughout — but it catches the case that
matters here, where a hand-edited pin drifts from the 720 blocks the tool wrote.

Measured when added: 727 blocks, 740 distinct taxa, zero conflicts.
"""

from __future__ import annotations

RANK_ORDER = ["d__", "p__", "c__", "o__", "f__", "g__", "s__"]


def _segments(lineage) -> list[str]:
    """The non-empty segments of a lineage, or [] for anything unusable.

    Tolerates a non-string: `gtdb_lineage` carries no `range` in the schema, so
    a YAML list is schema-valid, and raising here would abort `validate-strict`
    and discard every other file's findings (#429, #438).
    """
    if not isinstance(lineage, str):
        return []
    return [part.strip() for part in lineage.split(";") if part.strip()]


def _blocks(document):
    """Every `gtdb_classification` with the taxon it belongs to."""
    if not isinstance(document, dict):
        return
    for entry in document.get("taxonomy") or []:
        if not isinstance(entry, dict):
            continue
        term_block = entry.get("taxon_term")
        if not isinstance(term_block, dict):
            continue
        block = term_block.get("gtdb_classification")
        if not isinstance(block, dict):
            continue
        term = term_block.get("term")
        name = (
            term_block.get("preferred_term")
            or (term.get("label") if isinstance(term, dict) else None)
            or "?"
        )
        yield name, block


def check_lineage_shape(document) -> list[str]:
    """Per-record: rank prefixes present, in order, and ending at `gtdb_id`."""
    problems: list[str] = []
    for name, block in _blocks(document):
        segments = _segments(block.get("gtdb_lineage"))
        if not segments:
            continue
        seen: list[str] = []
        for segment in segments:
            prefix = segment[:3]
            if prefix not in RANK_ORDER:
                problems.append(f"{name!r}: lineage segment {segment!r} has no rank prefix")
                break
            if seen and RANK_ORDER.index(prefix) <= RANK_ORDER.index(seen[-1]):
                problems.append(
                    f"{name!r}: lineage goes from {seen[-1]} to {prefix}, which is not "
                    f"finer — {block.get('gtdb_lineage')!r}"
                )
                break
            seen.append(prefix)
    return problems


def check_corpus(documents) -> list[str]:
    """Across records: every GTDB taxon must sit under one parent lineage.

    `documents` is an iterable of (label, parsed-document) pairs — a corpus
    check, unlike its neighbours, because a single record cannot disagree with
    itself about where a taxon sits.
    """
    parents: dict[str, dict[str, list[str]]] = {}
    for label, document in documents:
        for name, block in _blocks(document):
            segments = _segments(block.get("gtdb_lineage"))
            for index, segment in enumerate(segments):
                path = ";".join(segments[:index])
                parents.setdefault(segment, {}).setdefault(path, []).append(f"{label} ({name})")

    problems = []
    for segment, paths in sorted(parents.items()):
        if len(paths) < 2:
            continue
        detail = "; ".join(
            f"under {path or '(root)'!r} in {sources[0]}" for path, sources in sorted(paths.items())
        )
        problems.append(
            f"{segment} is placed under {len(paths)} different lineages — GTDB is a "
            f"hierarchy, so at most one can be right: {detail}"
        )
    return problems
