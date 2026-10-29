"""`related_communities`, `host` and the checks the schema cannot express.

Membership relations between records are recomputed from strain designations by
`communitymech.validators.related_communities`, which `just validate-strict`
runs. These tests pin each rule on small synthetic records, run the check over
the whole corpus, and prove on a real record that a wrong relation is caught.
"""

from __future__ import annotations

import copy
from pathlib import Path

import pytest
import yaml

from communitymech.paths import REPO_ROOT, record_files, record_path
from communitymech.validators.related_communities import (
    check_record,
    compute_relation,
    strain_roster,
)

SCHEMA = REPO_ROOT / "src" / "communitymech" / "schema" / "communitymech.yaml"


def _member(strain: str | None) -> dict:
    entry: dict = {"taxon_term": {"preferred_term": f"sp. {strain}", "term": {"id": "NCBITaxon:2"}}}
    if strain:
        entry["strain_designation"] = {"strain_name": strain}
    return entry


def _record(rid: str, strains: list[str | None], links: list[dict] | None = None, **extra) -> dict:
    doc = {"id": rid, "taxonomy": [_member(s) for s in strains]}
    if links:
        doc["related_communities"] = links
    doc.update(extra)
    return doc


def _index(*docs: dict) -> dict:
    return {d["id"]: (Path(f"{d['id']}.yaml"), strain_roster(d)) for d in docs}


def _categories(doc: dict, index: dict) -> list[str]:
    return [category for category, _ in check_record(doc, index)]


EVIDENCE = [{"reference": "PMID:1", "snippet": "a quoted sentence"}]
A = "CommunityMech:900001"
B = "CommunityMech:900002"


@pytest.mark.parametrize(
    "mine, theirs, expected",
    [
        ({"X", "Y"}, {"X", "Y"}, "SAME_MEMBERSHIP_AS"),
        ({"X"}, {"X", "Y"}, "MEMBER_SUBSET_OF"),
        ({"X", "Y"}, {"X"}, "MEMBER_SUPERSET_OF"),
        ({"X", "Y"}, {"Y", "Z"}, "OVERLAPPING_MEMBERSHIP"),
        ({"X"}, {"Z"}, None),
    ],
)
def test_compute_relation(mine, theirs, expected):
    assert compute_relation(frozenset(mine), frozenset(theirs)) == expected


def test_strain_names_compare_without_case_or_spaces():
    assert strain_roster(_record(A, ["oas 925"])) == strain_roster(_record(B, ["OAS925"]))


def test_a_roster_with_a_gap_is_no_roster():
    assert strain_roster(_record(A, ["OAS925", None])) is None
    assert strain_roster({"id": A}) is None


def test_a_true_computed_relation_passes():
    target = _record(B, ["X", "Y"])
    doc = _record(
        A,
        ["X"],
        [{"identifier": B, "relation": "MEMBER_SUBSET_OF", "basis": "SHARED_STRAIN_DESIGNATIONS"}],
    )
    assert _categories(doc, _index(doc, target)) == []


def test_a_contradicted_relation_fails_whatever_its_basis():
    target = _record(B, ["X", "Y"])
    for basis, evidence in [("SHARED_STRAIN_DESIGNATIONS", None), ("SOURCE_STATEMENT", EVIDENCE)]:
        link = {"identifier": B, "relation": "SAME_MEMBERSHIP_AS", "basis": basis}
        if evidence:
            link["evidence"] = evidence
        doc = _record(A, ["X"], [link])
        assert _categories(doc, _index(doc, target)) == [
            "related_community_membership_contradiction"
        ]


def test_shared_strain_basis_needs_two_complete_rosters():
    target = _record(B, ["X", None])
    doc = _record(
        A,
        ["X"],
        [
            {
                "identifier": B,
                "relation": "OVERLAPPING_MEMBERSHIP",
                "basis": "SHARED_STRAIN_DESIGNATIONS",
            }
        ],
    )
    assert _categories(doc, _index(doc, target)) == ["related_community_basis_mismatch"]


def test_a_source_statement_needs_evidence():
    target = _record(B, [None])
    doc = _record(
        A, ["X"], [{"identifier": B, "relation": "DERIVED_FROM", "basis": "SOURCE_STATEMENT"}]
    )
    assert _categories(doc, _index(doc, target)) == ["related_community_needs_evidence"]


def test_a_non_membership_relation_cannot_rest_on_strains():
    target = _record(B, ["X"])
    doc = _record(
        A,
        ["X"],
        [{"identifier": B, "relation": "SAME_STUDY_AS", "basis": "SHARED_STRAIN_DESIGNATIONS"}],
    )
    assert _categories(doc, _index(doc, target)) == ["related_community_basis_mismatch"]


def test_unknown_self_and_duplicate_links():
    link = {
        "identifier": B,
        "relation": "SAME_STUDY_AS",
        "basis": "SOURCE_STATEMENT",
        "evidence": EVIDENCE,
    }
    doc = _record(A, ["X"], [link, dict(link)])
    assert _categories(doc, _index(doc)) == [
        "related_community_unknown_target",
        "related_community_duplicate",
        "related_community_unknown_target",
    ]
    doc = _record(A, ["X"], [dict(link, identifier=A)])
    assert _categories(doc, _index(doc)) == ["related_community_self_link"]


def test_the_host_is_not_a_member():
    host = {"preferred_term": "plant", "term": {"id": "NCBITaxon:15368"}}
    doc = _record(A, ["X"], host=host)
    doc["taxonomy"].append(
        {"taxon_term": {"preferred_term": "plant", "term": {"id": "NCBITaxon:15368"}}}
    )
    assert _categories(doc, _index(doc)) == ["host_listed_as_member"]


def test_host_participation_needs_a_host():
    doc = _record(
        A, ["X"], ecological_interactions=[{"name": "e", "host_participation": "HOST_IS_SOURCE"}]
    )
    assert _categories(doc, _index(doc)) == ["host_participation_without_host"]
    doc["host"] = {"preferred_term": "plant", "term": {"id": "NCBITaxon:15368"}}
    assert _categories(doc, _index(doc)) == []


def test_every_record_passes():
    failures = []
    for path in record_files():
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        failures += [f"{path.name}: {cat}: {msg}" for cat, msg in check_record(doc)]
    assert failures == [], "\n".join(failures)


def test_the_check_can_actually_fail():
    """Mutate a real computed relation and see it caught; the unmutated record,
    through the identical call, is the control arm (CLAUDE.md rule 5)."""
    path = record_path("Brachypodium_Natural_Variation_Dopamine_SynCom16.yaml")
    assert path is not None
    original = yaml.safe_load(path.read_text(encoding="utf-8"))
    assert list(check_record(original)) == []  # control arm

    mutated = copy.deepcopy(original)
    links = [
        link
        for link in mutated["related_communities"]
        if link["identifier"] == "CommunityMech:000025"
    ]
    assert [link["relation"] for link in links] == ["MEMBER_SUBSET_OF"]  # the mutation will apply
    links[0]["relation"] = "MEMBER_SUPERSET_OF"
    assert [c for c, _ in check_record(mutated)] == ["related_community_membership_contradiction"]


def test_new_dynamic_enums_keep_their_checked_roots():
    """The roots were checked against the ontologies when added (mechmaker
    design §5); changing one is a decision, not an edit."""
    enums = yaml.safe_load(SCHEMA.read_text())["enums"]
    roots = {
        name: enums[name]["reachable_from"]["source_nodes"]
        for name in [
            "HostTaxonTerm",
            "HostAnatomyTerm",
            "HostDevelopmentalStageTerm",
            "SoilTerm",
            "UnitTerm",
        ]
    }
    assert roots == {
        "HostTaxonTerm": ["NCBITaxon:2759"],
        "HostAnatomyTerm": ["PO:0025131", "UBERON:0001062"],
        "HostDevelopmentalStageTerm": ["PO:0009012", "UBERON:0000105"],
        "SoilTerm": ["ENVO:00001998"],
        "UnitTerm": ["UO:0000000"],
    }
