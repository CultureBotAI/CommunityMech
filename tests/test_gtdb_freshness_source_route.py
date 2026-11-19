"""Exercise the exact Terrabacter freshness admission and refusals (#2946).

2026-11-16. Reuse the existing actual published proof fixture. No canonical
source, proof artifact or historical ledger is changed by these controls.
"""

import copy
from pathlib import Path

import pytest
import test_gtdb_grounding_freshness as freshness
import yaml
from test_batch144_mapping_successor import evidence  # noqa: F401 - shared actual fixture

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture
def actual_route(evidence, monkeypatch):  # noqa: F811 - pytest injects imported actual fixture
    root, manifest, entry = evidence
    path = root / freshness.ANCESTOR_MANIFEST
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes((ROOT / freshness.ANCESTOR_MANIFEST).read_bytes())
    monkeypatch.setattr(freshness, "REPO", root)
    return root, manifest, entry


def rows(root):
    descriptor = yaml.safe_load((root / freshness.TERRABACTER).read_bytes())["taxonomy"][0][
        "taxon_term"
    ]
    return [
        (
            freshness.TERRABACTER,
            descriptor.get("preferred_term"),
            descriptor["term"]["id"],
            descriptor["gtdb_classification"],
        )
    ]


def check(root):
    freshness.test_grounding_is_not_stale_against_its_taxon_id(rows(root))


def test_actual_ancestor_route_passes_the_freshness_gate(actual_route):
    root, _, _ = actual_route
    check(root)
    row = rows(root)[0]
    assert row[2] == "NCBITaxon:1472881"
    assert row[3]["ncbi_source_id"] == "NCBITaxon:53355"


@pytest.mark.parametrize("mutation", ["stock", "source", "population", "name"])
def test_in_memory_inspection_cannot_borrow_another_proof(actual_route, mutation):
    root, _, _ = actual_route
    original = rows(root)
    freshness.test_grounding_is_not_stale_against_its_taxon_id(original)
    changed = list(copy.deepcopy(original[0]))
    if mutation == "stock":
        changed[2] = "NCBITaxon:53355"  # Equality must not bypass this exact route's proof.
    elif mutation == "source":
        changed[3]["ncbi_source_id"] = "NCBITaxon:1472881"
    elif mutation == "population":
        changed[3]["total_genomes"] = 999
    else:
        changed[1] = "Another stock"
    assert tuple(changed) != original[0]
    with pytest.raises(AssertionError, match="inspected row"):
        freshness.test_grounding_is_not_stale_against_its_taxon_id([tuple(changed)])
    freshness.test_grounding_is_not_stale_against_its_taxon_id(original)


@pytest.mark.parametrize(
    "artifact",
    ["current", "manifest", "grounding_proof", "application_receipt", "diagnostic_review"],
)
def test_current_bytes_and_provenance_are_required_and_restorable(actual_route, artifact):
    root, _, entry = actual_route
    check(root)
    if artifact == "current":
        path = root / freshness.TERRABACTER
    elif artifact == "manifest":
        path = root / freshness.ANCESTOR_MANIFEST
    else:
        path = root / entry[artifact]["path"]
    original = path.read_bytes()
    path.write_bytes(original + b"\n# changed proof input\n")
    assert path.read_bytes() != original
    try:
        with pytest.raises(AssertionError):
            check(root)
    finally:
        path.write_bytes(original)
    check(root)


def test_other_records_keep_exact_source_id_equality(actual_route):
    root, _, _ = actual_route
    original = rows(root)[0]
    unknown = ("kb/communities/unreviewed.yaml", *original[1:])
    assert unknown[3]["curated"] is True
    with pytest.raises(AssertionError, match="derived from a different id"):
        freshness.test_grounding_is_not_stale_against_its_taxon_id([unknown])
    equal = (unknown[0], unknown[1], unknown[2], {"ncbi_source_id": unknown[2]})
    freshness.test_grounding_is_not_stale_against_its_taxon_id([equal])
    with pytest.raises(AssertionError, match="derived from a different id"):
        freshness.test_grounding_is_not_stale_against_its_taxon_id([unknown])
    check(root)
