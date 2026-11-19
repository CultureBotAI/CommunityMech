"""Native strict controls for the reproduced PR2102 defects (#2700–2704)."""

from __future__ import annotations

import copy
import importlib.util

import pytest
import yaml

from communitymech.paths import REPO_ROOT
from communitymech.validators import related_communities

SPEC = importlib.util.spec_from_file_location(
    "phase2_native_strict", REPO_ROOT / "scripts" / "validate_strict.py"
)
STRICT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(STRICT)

A = "CommunityMech:900001"
B = "CommunityMech:900002"
HOST = {
    "preferred_term": "plant",
    "term": {"id": "NCBITaxon:15368", "label": "Brachypodium distachyon"},
}


def member(name="X", taxon="NCBITaxon:562", label="Escherichia coli", accession="123"):
    return {
        "taxon_term": {"preferred_term": label, "term": {"id": taxon, "label": label}},
        "strain_designation": {
            "strain_name": name,
            "culture_collections": [{"collection": "DSM", "accession": accession}],
        },
    }


def record(rid=A, **extra):
    return {"id": rid, "name": "Native control", **extra}


def pair(first=None, second=None):
    return [
        record(
            A,
            taxonomy=first or [member()],
            related_communities=[
                {
                    "identifier": B,
                    "relation": "SAME_MEMBERSHIP_AS",
                    "basis": "SHARED_STRAIN_DESIGNATIONS",
                }
            ],
        ),
        record(
            B,
            taxonomy=second or [member()],
            related_communities=[
                {
                    "identifier": A,
                    "relation": "SAME_MEMBERSHIP_AS",
                    "basis": "SHARED_STRAIN_DESIGNATIONS",
                }
            ],
        ),
    ]


@pytest.fixture
def native(tmp_path, monkeypatch):
    """Run the maintained strict entry point; only the corpus input paths differ."""
    written = []
    monkeypatch.setattr(related_communities, "record_files", lambda: written)

    def check(*docs):
        written.clear()
        for index, doc in enumerate(docs):
            path = tmp_path / f"record-{index}.yaml"
            path.write_text(yaml.safe_dump(doc, sort_keys=False))
            written.append(path)
        related_communities._corpus_index_and_duplicates.cache_clear()
        return STRICT.validate_one(written[0])

    yield check
    related_communities._corpus_index_and_duplicates.cache_clear()


def test_compatible_stock_formatting_native_control(native):
    assert native(*pair([member("x ")], [member(" X")])) == []


@pytest.mark.parametrize(
    "changed",
    [
        member(taxon="NCBITaxon:1423", label="Bacillus subtilis"),
        member(accession="999"),
    ],
)
def test_same_local_name_cannot_hide_incompatible_stocks(native, changed):
    control = pair()
    assert native(*control) == []
    control[1]["taxonomy"] = [changed]
    assert native(*control), "same local name must not certify incompatible stock identity"


def test_two_distinct_same_name_members_cannot_collapse(native):
    docs = pair()
    assert native(*docs) == []
    docs[0]["taxonomy"].append(
        member(taxon="NCBITaxon:1423", label="Bacillus subtilis", accession="999")
    )
    assert len(docs[0]["taxonomy"]) == 2
    assert native(*docs), "a frozenset of names must not collapse two members to one"


def test_modification_prose_and_assembly_versions_are_not_stock_conflicts(native):
    docs = pair()
    left = docs[0]["taxonomy"][0]["strain_designation"]
    right = docs[1]["taxonomy"][0]["strain_designation"]
    left.update(genetic_modification="nifA* mutant", genome_accession="GCF_000001.1")
    right.update(
        genetic_modification="nifA* mutant excreting ammonium", genome_accession="GCF_000001.2"
    )
    assert native(*docs) == []
    roster = related_communities.strain_roster(docs[0])
    assert roster.members[0].genome == "GCF_000001.1"
    assert roster.members[0].modification == "nifa* mutant"


@pytest.mark.parametrize("side", [0, 1])
@pytest.mark.parametrize("basis", ["SHARED_STRAIN_DESIGNATIONS", "SOURCE_STATEMENT"])
def test_duplicate_names_never_collapse_even_with_evidence(native, side, basis):
    docs = pair()
    for doc in docs:
        doc["related_communities"][0].update(
            basis=basis,
            evidence=[
                {
                    "reference": "PMID:1",
                    "snippet": "The stocks were shared.",
                    "supports": "SUPPORT",
                    "evidence_source": "IN_VITRO",
                }
            ],
        )
    assert native(*docs) == []
    docs[side]["taxonomy"].append(copy.deepcopy(docs[side]["taxonomy"][0]))
    assert any(
        row["category"] == "related_community_ambiguous_stock_identity" for row in native(*docs)
    )


@pytest.mark.parametrize(
    "slot", ["sampling_depth", "sieve_size", "water_content", "organic_carbon"]
)
def test_all_typed_quantity_paths_require_finite_values(native, slot):
    quantity = {"value": 1.0, "unit": {"id": "UO:0000015", "label": "centimeter"}}
    doc = record(soils=[{"preferred_term": "soil", slot: quantity}])
    assert native(doc) == []
    quantity["value"] = float("inf")
    assert any(row["category"] == "quantity_nonfinite" for row in native(doc))


@pytest.mark.parametrize("role", ["HOST_IS_SOURCE", "HOST_IS_TARGET", "RECIPROCAL"])
def test_explicit_community_host_role_native_control(native, role):
    assert (
        native(
            record(
                host=HOST,
                ecological_interactions=[
                    {
                        "name": "host interaction",
                        "scope": "COMMUNITY_LEVEL",
                        "host_participation": role,
                    }
                ],
            )
        )
        == []
    )


@pytest.mark.parametrize("scope", ["PAIRWISE", None])
def test_host_participation_requires_explicit_community_scope(native, scope):
    interaction = {
        "name": "host interaction",
        "scope": "COMMUNITY_LEVEL",
        "host_participation": "HOST_IS_SOURCE",
    }
    doc = record(host=HOST, ecological_interactions=[interaction])
    assert native(doc) == []
    if scope is None:
        del interaction["scope"]
    else:
        interaction["scope"] = scope
    assert native(doc)


@pytest.mark.parametrize("slot", ["source_taxon", "target_taxon", "participating_taxa"])
def test_host_cannot_occupy_microbial_interaction_slots(native, slot):
    interaction = {"name": "interaction", "scope": "COMMUNITY_LEVEL"}
    doc = record(host=HOST, ecological_interactions=[interaction])
    microbial = member()["taxon_term"]
    interaction[slot] = [microbial] if slot == "participating_taxa" else microbial
    assert native(doc) == []
    interaction[slot] = [HOST] if slot == "participating_taxa" else HOST
    assert native(doc)


def soil_quantity(value=7.0, unit="UO:0000196", label="pH"):
    return record(
        soils=[
            {"preferred_term": "soil", "ph": {"value": value, "unit": {"id": unit, "label": label}}}
        ]
    )


def test_ph_unit_is_dimensional_not_merely_a_valid_uo_term(native):
    assert native(soil_quantity()) == []
    assert native(soil_quantity(unit="UO:0000009", label="kilogram"))


@pytest.mark.parametrize("value", [float("inf"), float("-inf"), float("nan")])
def test_quantity_values_must_be_finite(native, value):
    assert native(soil_quantity()) == []
    assert native(soil_quantity(value))


def test_other_finite_quantities_and_omitted_optional_properties_pass(native):
    assert native(record(soils=[{"preferred_term": "soil"}])) == []
    assert (
        native(
            record(
                soils=[
                    {
                        "preferred_term": "soil",
                        "sampling_depth": {
                            "value": 12.5,
                            "unit": {"id": "UO:0000015", "label": "centimeter"},
                        },
                    }
                ]
            )
        )
        == []
    )


@pytest.mark.parametrize("reverse", [False, True])
def test_focused_relation_rejects_duplicate_target_independent_of_order(native, reverse):
    docs = pair()
    assert native(*docs) == []
    duplicate = copy.deepcopy(docs[1])
    duplicate["taxonomy"] = [member("Y", accession="456")]
    targets = [docs[1], duplicate]
    if reverse:
        targets.reverse()
    errors = native(docs[0], *targets)
    assert any(row["category"] == "related_community_ambiguous_target" for row in errors)
