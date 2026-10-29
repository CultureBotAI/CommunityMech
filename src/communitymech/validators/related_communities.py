"""Cross-record and cross-field checks for `related_communities` and `host`.

LinkML can check that a `related_communities` entry has a well-formed
`CommunityMech:` id and an allowed `relation`, but not that the target exists,
nor that a membership relation is true. Both are facts about two records at
once, so they live here and run in `just validate-strict`.

**Membership relations are recomputed, not trusted.** SAME_MEMBERSHIP_AS,
MEMBER_SUBSET_OF, MEMBER_SUPERSET_OF and OVERLAPPING_MEMBERSHIP are decided by
comparing the two records' strain designations. When both records name a
strain for every member, the relation is computed and a stated relation that
disagrees is an error, whatever its `basis`: a source cannot make two rosters
equal that the records show to differ. When either roster is incomplete the
relation cannot be computed, so `basis: SHARED_STRAIN_DESIGNATIONS` is an
error and a SOURCE_STATEMENT relation must quote its source.

**A host is not a member (#319).** `host.term.id` appearing in `taxonomy` is
an error, and `host_participation` on an interaction needs a `host` to refer to.
"""

from __future__ import annotations

import functools
from collections.abc import Iterator
from pathlib import Path

import yaml

from communitymech.paths import record_files

MEMBERSHIP_RELATIONS = frozenset(
    {"SAME_MEMBERSHIP_AS", "MEMBER_SUBSET_OF", "MEMBER_SUPERSET_OF", "OVERLAPPING_MEMBERSHIP"}
)


def _strain_key(name: str) -> str:
    return "".join(name.split()).upper()


def strain_roster(instance: dict) -> frozenset[str] | None:
    """The record's strains, or None when any member lacks a strain name.

    A roster with a gap is not a roster: a member without a strain name could
    be any strain, so no set relation computed from the rest would be sound.
    """
    taxonomy = instance.get("taxonomy") or []
    if not taxonomy:
        return None
    names = []
    for entry in taxonomy:
        name = ((entry or {}).get("strain_designation") or {}).get("strain_name")
        if not name or not str(name).strip():
            return None
        names.append(_strain_key(str(name)))
    return frozenset(names)


def compute_relation(mine: frozenset[str], theirs: frozenset[str]) -> str | None:
    """The membership relation from `mine` to `theirs`, or None if disjoint."""
    if mine == theirs:
        return "SAME_MEMBERSHIP_AS"
    if mine < theirs:
        return "MEMBER_SUBSET_OF"
    if mine > theirs:
        return "MEMBER_SUPERSET_OF"
    if mine & theirs:
        return "OVERLAPPING_MEMBERSHIP"
    return None


@functools.lru_cache(maxsize=1)
def _corpus_index() -> dict[str, tuple[Path, frozenset[str] | None]]:
    index: dict[str, tuple[Path, frozenset[str] | None]] = {}
    for path in record_files():
        try:
            doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        except yaml.YAMLError:
            continue
        if isinstance(doc, dict) and doc.get("id"):
            index[str(doc["id"])] = (path, strain_roster(doc))
    return index


def check_record(
    instance: dict,
    index: dict[str, tuple[Path, frozenset[str] | None]] | None = None,
) -> Iterator[tuple[str, str]]:
    """Yield (category, message) for each problem in one record.

    `index` maps record id to (path, roster); it defaults to the whole corpus
    and is a parameter so tests can supply a small one.
    """
    if not isinstance(instance, dict):
        return
    if index is None:
        index = _corpus_index()
    own_id = str(instance.get("id", ""))
    own_roster = strain_roster(instance)

    seen: set[tuple[str, str]] = set()
    for link in instance.get("related_communities") or []:
        target = str(link.get("identifier", ""))
        relation = str(link.get("relation", ""))
        basis = str(link.get("basis", ""))
        label = f"{target} {relation}"
        if (target, relation) in seen:
            yield "related_community_duplicate", f"{label}: stated twice"
        seen.add((target, relation))
        if target == own_id:
            yield "related_community_self_link", f"{label}: a record cannot relate to itself"
            continue
        if target not in index:
            yield "related_community_unknown_target", f"{label}: no record has this id"
            continue
        if basis == "SOURCE_STATEMENT" and not link.get("evidence"):
            yield (
                "related_community_needs_evidence",
                f"{label}: basis SOURCE_STATEMENT needs evidence quoting the source",
            )
        if relation not in MEMBERSHIP_RELATIONS:
            if basis == "SHARED_STRAIN_DESIGNATIONS":
                yield (
                    "related_community_basis_mismatch",
                    f"{label}: {relation} is not a membership relation, so it cannot rest on "
                    "SHARED_STRAIN_DESIGNATIONS",
                )
            continue
        target_roster = index[target][1]
        if own_roster is None or target_roster is None:
            if basis == "SHARED_STRAIN_DESIGNATIONS":
                side = "this record" if own_roster is None else target
                yield (
                    "related_community_basis_mismatch",
                    f"{label}: {side} does not name a strain for every member, so the relation "
                    "cannot be computed; use basis SOURCE_STATEMENT with evidence",
                )
            continue
        computed = compute_relation(own_roster, target_roster)
        if computed != relation:
            yield (
                "related_community_membership_contradiction",
                f"{label}: the strain designations give {computed or 'no shared strains'}",
            )

    host = instance.get("host") or {}
    host_id = ((host.get("term") or {}).get("id")) if isinstance(host, dict) else None
    if host_id:
        for entry in instance.get("taxonomy") or []:
            member_id = (((entry or {}).get("taxon_term") or {}).get("term") or {}).get("id")
            if member_id == host_id:
                yield (
                    "host_listed_as_member",
                    f"{host_id}: the host is not a member (#319); remove it from taxonomy",
                )
    for interaction in instance.get("ecological_interactions") or []:
        if (interaction or {}).get("host_participation") and not host:
            yield (
                "host_participation_without_host",
                f"{interaction.get('name')}: host_participation is set but the record has no host",
            )
