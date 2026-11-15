"""Cross-record and cross-field checks for `related_communities` and `host`.

LinkML can check that a `related_communities` entry has a well-formed
`CommunityMech:` id and an allowed `relation`, but not that the target exists,
nor that a membership relation is true. Both are facts about two records at
once, so they live here and run in `just validate-strict`.

**Membership relations are checked, not globally resolved.** SAME_MEMBERSHIP_AS,
MEMBER_SUBSET_OF, MEMBER_SUPERSET_OF and OVERLAPPING_MEMBERSHIP are decided by
comparing curator-asserted corresponding strain designations. Local names (even
with matching taxonomy) do not independently prove stock identity across studies:
scientific review must verify that assertion. Roster multiplicity and available
taxon, deposit, assembly and modification metadata are retained; ambiguous names
or conflicting metadata block comparison rather than silently merging stocks.
When both records name an unambiguous strain for every member, the relation is
computed and a stated relation that
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
from dataclasses import dataclass
from pathlib import Path

import yaml

from communitymech.paths import record_files

MEMBERSHIP_RELATIONS = frozenset(
    {"SAME_MEMBERSHIP_AS", "MEMBER_SUBSET_OF", "MEMBER_SUPERSET_OF", "OVERLAPPING_MEMBERSHIP"}
)

INVERSE_RELATIONS = {
    "SAME_MEMBERSHIP_AS": "SAME_MEMBERSHIP_AS",
    "MEMBER_SUBSET_OF": "MEMBER_SUPERSET_OF",
    "MEMBER_SUPERSET_OF": "MEMBER_SUBSET_OF",
    "OVERLAPPING_MEMBERSHIP": "OVERLAPPING_MEMBERSHIP",
    "SAME_STUDY_AS": "SAME_STUDY_AS",
}


def _strain_key(name: str) -> str:
    return "".join(name.split()).upper()


def record_links(instance: dict) -> frozenset[tuple[str, str]]:
    """The (identifier, relation) pairs stated in `related_communities`."""
    return frozenset(
        (str(link.get("identifier", "")), str(link.get("relation", "")))
        for link in (instance.get("related_communities") or [])
        if isinstance(link, dict)
    )


@dataclass(frozen=True)
class StockIdentity:
    """Recorded identity metadata, not an inferred globally unique stock key."""

    name: str
    taxon: str
    collections: frozenset[tuple[str, str]]
    genome: str
    modification: str


@dataclass(frozen=True)
class StrainRoster:
    members: tuple[StockIdentity, ...]

    @property
    def names(self) -> frozenset[str]:
        return frozenset(member.name for member in self.members)


def strain_roster(instance: dict) -> StrainRoster | None:
    """The record's strains, or None when any member lacks a strain name.

    A roster with a gap is not a roster: a member without a strain name could
    be any strain, so no set relation computed from the rest would be sound.
    """
    taxonomy = instance.get("taxonomy") or []
    if not taxonomy:
        return None
    members = []
    for entry in taxonomy:
        if not isinstance(entry, dict):
            return None
        name = ((entry or {}).get("strain_designation") or {}).get("strain_name")
        if not name or not str(name).strip():
            return None
        designation = entry.get("strain_designation") or {}
        members.append(
            StockIdentity(
                name=_strain_key(str(name)),
                taxon=str(((entry.get("taxon_term") or {}).get("term") or {}).get("id") or ""),
                collections=frozenset(
                    (
                        str(item.get("collection") or ""),
                        _strain_key(str(item.get("accession") or "")),
                    )
                    for item in designation.get("culture_collections") or []
                    if isinstance(item, dict)
                ),
                genome=str(designation.get("genome_accession") or "").strip(),
                modification=" ".join(
                    str(designation.get("genetic_modification") or "").split()
                ).casefold(),
            )
        )
    return StrainRoster(tuple(members))


def _identity_ambiguities(mine: StrainRoster, theirs: StrainRoster) -> Iterator[str]:
    """Reject loss of members or unresolved recorded identity conflicts."""
    ambiguous = False
    for side, roster in (("this record", mine), ("target", theirs)):
        seen = set()
        for member in roster.members:
            if member.name in seen:
                ambiguous = True
                yield (
                    f"{side} repeats normalized strain name {member.name}; "
                    "members cannot be collapsed"
                )
            seen.add(member.name)
    if ambiguous:
        return
    by_name = {member.name: member for member in theirs.members}
    for member in mine.members:
        other = by_name.get(member.name)
        if other is None:
            continue
        # Assembly accessions can change for the same isolate, and differing
        # modification prose can describe the same genotype. Keep both in the
        # roster for scientific review, but do not infer incompatibility from
        # their string inequality.
        for field in ("taxon",):
            left, right = getattr(member, field), getattr(other, field)
            if left and right and left != right:
                yield f"{member.name}: conflicting {field} metadata ({left!r} versus {right!r})"
        collections = {collection for collection, _ in member.collections} & {
            collection for collection, _ in other.collections
        }
        for collection in sorted(collections):
            left = {accession for source, accession in member.collections if source == collection}
            right = {accession for source, accession in other.collections if source == collection}
            if left.isdisjoint(right):
                yield (
                    f"{member.name}: conflicting {collection} accessions "
                    f"({sorted(left)} versus {sorted(right)})"
                )


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
def _corpus_index_and_duplicates() -> tuple[
    dict[str, tuple[Path, StrainRoster | None, frozenset[tuple[str, str]]]],
    dict[str, tuple[Path, ...]],
]:
    index: dict[str, tuple[Path, StrainRoster | None, frozenset[tuple[str, str]]]] = {}
    paths_by_id: dict[str, list[Path]] = {}
    for path in record_files():
        try:
            doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        except yaml.YAMLError:
            continue
        if isinstance(doc, dict) and doc.get("id"):
            rid = str(doc["id"])
            paths_by_id.setdefault(rid, []).append(path)
            index[rid] = (path, strain_roster(doc), record_links(doc))
    duplicates = {rid: tuple(paths) for rid, paths in paths_by_id.items() if len(paths) > 1}
    return index, duplicates


def _corpus_index() -> dict[str, tuple[Path, StrainRoster | None, frozenset[tuple[str, str]]]]:
    return _corpus_index_and_duplicates()[0]


def _duplicate_ids() -> dict[str, tuple[Path, ...]]:
    return _corpus_index_and_duplicates()[1]


def check_record(
    instance: dict,
    index: dict[str, tuple] | None = None,
    duplicate_ids: dict[str, tuple[Path, ...]] | None = None,
) -> Iterator[tuple[str, str]]:
    """Yield (category, message) for each problem in one record.

    `index` maps record id to (path, roster[, links]); it defaults to the whole
    corpus and is a parameter so tests can supply a small one.
    """
    if not isinstance(instance, dict):
        return
    if index is None:
        index, default_duplicates = _corpus_index_and_duplicates()
        if duplicate_ids is None:
            duplicate_ids = default_duplicates
    own_id = str(instance.get("id", ""))
    if duplicate_ids and own_id in duplicate_ids:
        names = ", ".join(p.name for p in duplicate_ids[own_id])
        yield "duplicate_record_id", f"{own_id}: shared by multiple records ({names})"
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
        if duplicate_ids and target in duplicate_ids:
            names = ", ".join(p.name for p in duplicate_ids[target])
            yield (
                "related_community_ambiguous_target",
                f"{label}: multiple records have this id ({names}); no target can be selected",
            )
            continue
        if target not in index:
            yield "related_community_unknown_target", f"{label}: no record has this id"
            continue
        needs_evidence = basis == "SOURCE_STATEMENT" and not link.get("evidence")
        if needs_evidence:
            yield (
                "related_community_needs_evidence",
                f"{label}: basis SOURCE_STATEMENT needs evidence quoting the source",
            )
        target_entry = index[target]
        target_roster = target_entry[1]
        target_links = target_entry[2] if len(target_entry) >= 3 else None
        expected_inverse = INVERSE_RELATIONS.get(relation)
        if relation not in MEMBERSHIP_RELATIONS:
            if basis == "SHARED_STRAIN_DESIGNATIONS":
                yield (
                    "related_community_basis_mismatch",
                    f"{label}: {relation} is not a membership relation, so it cannot rest on "
                    "SHARED_STRAIN_DESIGNATIONS",
                )
                continue
            if (
                not needs_evidence
                and expected_inverse
                and target_links is not None
                and (own_id, expected_inverse) not in target_links
            ):
                yield (
                    "related_community_missing_inverse",
                    f"{label}: {target} does not state inverse link {own_id} {expected_inverse}",
                )
            continue
        if own_roster is None or target_roster is None:
            if basis == "SHARED_STRAIN_DESIGNATIONS":
                side = "this record" if own_roster is None else target
                yield (
                    "related_community_basis_mismatch",
                    f"{label}: {side} does not name a strain for every member, so the relation "
                    "cannot be computed; use basis SOURCE_STATEMENT with evidence",
                )
                continue
            if (
                not needs_evidence
                and expected_inverse
                and target_links is not None
                and (own_id, expected_inverse) not in target_links
            ):
                yield (
                    "related_community_missing_inverse",
                    f"{label}: {target} does not state inverse link {own_id} {expected_inverse}",
                )
            continue
        ambiguities = list(_identity_ambiguities(own_roster, target_roster))
        if ambiguities:
            for ambiguity in ambiguities:
                yield "related_community_ambiguous_stock_identity", f"{label}: {ambiguity}"
            continue
        computed = compute_relation(own_roster.names, target_roster.names)
        if computed != relation:
            yield (
                "related_community_membership_contradiction",
                f"{label}: the strain designations give {computed or 'no shared strains'}",
            )
            continue
        if (
            not needs_evidence
            and expected_inverse
            and target_links is not None
            and (own_id, expected_inverse) not in target_links
        ):
            yield (
                "related_community_missing_inverse",
                f"{label}: {target} does not state inverse link {own_id} {expected_inverse}",
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
        if not isinstance(interaction, dict):
            continue
        name = interaction.get("name")
        if interaction.get("host_participation"):
            if not host:
                yield (
                    "host_participation_without_host",
                    f"{name}: host_participation is set but the record has no host",
                )
            if interaction.get("scope") != "COMMUNITY_LEVEL":
                yield (
                    "host_participation_scope",
                    f"{name}: host_participation requires explicit COMMUNITY_LEVEL scope",
                )
        if host_id:
            for slot in ("source_taxon", "target_taxon", "participating_taxa"):
                values = interaction.get(slot) or []
                if isinstance(values, dict):
                    values = [values]
                for value in values:
                    if isinstance(value, dict) and (value.get("term") or {}).get("id") == host_id:
                        yield (
                            "host_in_microbial_interaction_slot",
                            f"{name}.{slot}: {host_id} is the host; use host_participation",
                        )
