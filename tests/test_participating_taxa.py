"""`participating_taxa` narrows the community-level connectivity credit (#312).

A `COMMUNITY_LEVEL` interaction was credited as connecting **every** member of
the record. Defensible — such an interaction asserts something holding across
the community rather than between a named pair — and unavoidably coarse, because
`EcologicalInteraction` had only `source_taxon` and `target_taxon` and no way to
say *which* members participate. In a record carrying both kinds of edge, a
taxon in no pairwise edge was credited by an unrelated community-level one:
**407 of 522 taxa** were credited solely that way.

`participating_taxa` is the refinement #312 proposed. Optional, and absent or
empty means "every member" — so the corpus behaves identically today (measured:
55 findings before, 55 after, same breakdown). Nothing changes until a curator
names participants, which is the property that makes this safe to land ahead of
any curation.

Two things here were found by running the code rather than reading it, and both
are pinned below:

* an entry naming a member by CURIE resolved to the id string, which is not a
  key of `taxonomy_by_term` — so naming participants by id credited *nobody*
  and disconnected the whole record. The name path returned the right count
  throughout, so a test of the happy path alone would have shipped it.
* once that was fixed, naming by CURIE in the worked example credits **all 28**
  members, because those 28 taxa share one NCBITaxon id. That is correct, and it
  is the trap in #524: the slot silently does nothing in exactly the strain-level
  records whose over-broad credit motivated it.
"""

from __future__ import annotations

import pathlib
import tempfile

import pytest
import yaml

from communitymech.network.auditor import IssueType, NetworkIntegrityAuditor

REPO = pathlib.Path(__file__).parent.parent
COMMUNITIES = REPO / "kb/communities"
# #312's illustration: 28 taxa, every interaction COMMUNITY_LEVEL.
EXAMPLE = COMMUNITIES / "GLBRC_Populus_Variovorax_SynCom28.yaml"


def _disconnected(document: dict) -> int:
    """DISCONNECTED findings for one record, audited in isolation."""
    with tempfile.TemporaryDirectory() as directory:
        path = pathlib.Path(directory) / "record.yaml"
        path.write_text(
            yaml.safe_dump(document, sort_keys=False, allow_unicode=True, width=4096),
            encoding="utf-8",
        )
        issues = NetworkIntegrityAuditor(pathlib.Path(directory)).audit_community(path) or []
        return sum(1 for issue in issues if issue["type"] == IssueType.DISCONNECTED)


@pytest.fixture
def example() -> dict:
    return yaml.safe_load(EXAMPLE.read_text(encoding="utf-8"))


def _members(document: dict) -> list[dict]:
    return [(entry.get("taxon_term") or {}) for entry in document.get("taxonomy") or []]


def test_the_example_still_has_the_shape_the_test_needs(example):
    """Guard: if the record changes, the numbers below stop meaning anything."""
    assert len(_members(example)) == 28
    interactions = example["ecological_interactions"]
    assert len(interactions) == 3
    assert all(i.get("scope") == "COMMUNITY_LEVEL" for i in interactions)


def test_absent_participating_taxa_still_credits_everyone(example):
    """The default, and why landing this changes no finding today."""
    assert _disconnected(example) == 0


def test_an_empty_list_means_every_member_not_none(example):
    """`[]` is "unspecified", not "nobody".

    The opposite reading would turn an interaction that omits the slot by
    accident into 28 spurious DISCONNECTED findings.
    """
    for interaction in example["ecological_interactions"]:
        interaction["participating_taxa"] = []
    assert _disconnected(example) == 0


def test_naming_participants_narrows_the_credit(example):
    """The point of #312: 2 named of 28 leaves 26 uncredited."""
    members = _members(example)
    named = [
        {"preferred_term": m.get("preferred_term"), "term": m.get("term")} for m in members[:2]
    ]
    for interaction in example["ecological_interactions"]:
        interaction["participating_taxa"] = named
    assert _disconnected(example) == 26


def test_narrowing_one_of_three_interactions_is_not_enough(example):
    """Credit is a union across interactions, so the others still cover everyone.

    Worth pinning because it is how the first run of this check fooled me: I
    narrowed only the first interaction, saw 0, and briefly took the feature
    for broken rather than the probe.
    """
    members = _members(example)
    example["ecological_interactions"][0]["participating_taxa"] = [
        {"preferred_term": members[0].get("preferred_term"), "term": members[0].get("term")}
    ]
    assert _disconnected(example) == 0


def test_a_curie_only_entry_resolves_rather_than_crediting_nobody(example):
    """The bug the canary caught: ids are not keys of `taxonomy_by_term`.

    Before the fix this returned 28 — every member disconnected — because the
    id string matched no member key and the interaction credited nothing.
    """
    members = _members(example)
    by_id = [{"term": {"id": m["term"]["id"]}} for m in members[:2] if m.get("term", {}).get("id")]
    assert by_id, "the example lost its term ids"
    for interaction in example["ecological_interactions"]:
        interaction["participating_taxa"] = by_id
    assert _disconnected(example) != 28, (
        "a CURIE-named participant credited nobody, which disconnects the whole "
        "record — ids resolve through `taxonomy_keys_by_id`, not `taxonomy_by_term`"
    )


def test_a_curie_is_ambiguous_where_members_share_an_id(example):
    """#524, pinned as a property rather than left as a surprise.

    All 28 taxa carry `NCBITaxon:34072`. Naming two by CURIE credits all 28,
    which is the only sound reading of an ambiguous reference — and means the
    slot appears to do nothing in exactly the strain-level records that
    motivated it. The guidance ("name by preferred_term") is on the slot.
    """
    members = _members(example)
    ids = {m.get("term", {}).get("id") for m in members}
    assert len(ids) == 1, "the example no longer shares one id across its members"

    by_id = [{"term": {"id": next(iter(ids))}}]
    for interaction in example["ecological_interactions"]:
        interaction["participating_taxa"] = by_id
    assert _disconnected(example) == 0


def test_the_corpus_is_unchanged_by_this_feature():
    """Nothing uses the slot yet, so no finding may move.

    Asserted on the corpus rather than trusted from the schema: an
    `ifabsent` or a default that quietly populated the slot would change 312
    records' connectivity without anyone editing a record.
    """
    users = [
        path.name
        for path in sorted(COMMUNITIES.glob("*.yaml"))
        for interaction in (yaml.safe_load(path.read_text()) or {}).get("ecological_interactions")
        or []
        if isinstance(interaction, dict) and interaction.get("participating_taxa")
    ]
    assert users == [], (
        f"{len(users)} records now use participating_taxa. That is fine and "
        f"expected eventually — but the connectivity numbers in "
        f"tests/test_community_level_connectivity_credit.py were measured "
        f"without it, so check them: {sorted(set(users))[:5]}"
    )


def test_a_name_beats_an_id_on_the_same_entry(example):
    """Precedence, not union — and the flaw that nearly shipped this useless.

    Curators copy the whole `taxon_term` block into a participant, so an entry
    normally carries `preferred_term` *and* `term.id`. Resolving both and
    unioning them meant the id credited all 28 members sharing it, so an entry
    naming one strain credited every strain and the narrowing did nothing.

    The name path alone gave the right answer at every step, and the id path
    alone gave the right answer; only an entry carrying both was wrong. That is
    why this case is pinned separately from the two above.
    """
    members = _members(example)
    both = [{"preferred_term": m.get("preferred_term"), "term": m.get("term")} for m in members[:2]]
    assert all(entry["term"].get("id") for entry in both), "the fixture lost its ids"
    for interaction in example["ecological_interactions"]:
        interaction["participating_taxa"] = both
    assert _disconnected(example) == 26, (
        "an entry carrying both a preferred_term and a shared term.id credited "
        "every member sharing that id, defeating the narrowing (#312/#524)"
    )
