"""Phase 2 graph export preserves context, source boundaries and identities (#2430)."""

import csv
import json

import pytest
import yaml

from communitymech.export import kgx_export as kgx
from communitymech.export.validate_kgx import validate_edges, validate_nodes


def evidence(number, text):
    return [{"reference": f"PMID:{number}", "snippet": text}]


def records():
    return [
        {
            "id": "CommunityMech:999991",
            "name": "Community A",
            "host": {
                "preferred_term": "plant host",
                "term": {"id": "NCBITaxon:3702", "label": "Arabidopsis thaliana"},
                "developmental_stage": {
                    "preferred_term": "seedling",
                    "description": "Four days old",
                },
                "evidence": evidence(11, "host evidence"),
            },
            "soils": [
                {
                    "preferred_term": "soil in pot",
                    "term": {"id": "ENVO:00001998", "label": "soil"},
                    "ph": {"value": ph, "unit": {"id": "UO:0000196", "label": "pH"}},
                    "evidence": evidence(number, f"soil {ph} evidence"),
                }
                for ph, number in [(6, 12), (7, 13)]
            ],
            "related_communities": [
                {
                    "identifier": "CommunityMech:999992",
                    "relation": relation,
                    "basis": "SOURCE_STATEMENT",
                    "evidence": evidence(number, relation),
                }
                for relation, number in [("DERIVED_FROM", 14), ("SAME_STUDY_AS", 15)]
            ],
        },
        {"id": "CommunityMech:999992", "name": "Community B"},
    ]


def export(tmp_path, docs):
    kb = tmp_path / "kb"
    kb.mkdir(exist_ok=True)
    for index, doc in enumerate(docs):
        (kb / f"record{index}.yaml").write_text(yaml.safe_dump(doc))
    output = tmp_path / "graph"
    kgx.export_kgx(kb, output)
    with (output / "nodes.tsv").open() as handle:
        nodes = list(csv.DictReader(handle, delimiter="\t"))
    with (output / "edges.tsv").open() as handle:
        edges = list(csv.DictReader(handle, delimiter="\t"))
    return output, nodes, edges


def test_context_edges_preserve_roles_measurements_and_evidence(tmp_path):
    output, nodes, edges = export(tmp_path, records())
    contexts = [e for e in edges if e.get("communitymech_context")]
    host = next(e for e in contexts if json.loads(e["communitymech_context"])["field"] == "host")
    assert host["subject"] == "CommunityMech:999991"
    assert host["object"] == "NCBITaxon:3702"
    assert host["predicate"] == "biolink:related_to"
    assert host["publications"] == "PMID:11"
    assert host["supporting_text"] == "host evidence"
    assert (
        json.loads(host["communitymech_context"])["assertion"]["developmental_stage"]["description"]
        == "Four days old"
    )
    assert not any(
        e["predicate"] == "biolink:has_part" and e["object"] == host["object"] for e in edges
    )
    soils = [e for e in contexts if json.loads(e["communitymech_context"])["field"] == "soils"]
    assert len(soils) == 2 and len({e["object"] for e in soils}) == 2
    assert {e["publications"] for e in soils} == {"PMID:12", "PMID:13"}
    assert {json.loads(e["communitymech_context"])["assertion"]["ph"]["value"] for e in soils} == {
        6,
        7,
    }
    related = [
        e
        for e in contexts
        if json.loads(e["communitymech_context"])["field"] == "related_communities"
    ]
    assert len(related) == 2 and len({e["id"] for e in related}) == 2
    assert {json.loads(e["communitymech_context"])["assertion"]["relation"] for e in related} == {
        "DERIVED_FROM",
        "SAME_STUDY_AS",
    }
    assert {e["publications"] for e in related} == {"PMID:14", "PMID:15"}
    by_id = {n["id"]: n for n in nodes}
    assert by_id["NCBITaxon:3702"]["name"] == "Arabidopsis thaliana"
    assert by_id["ENVO:00001998"]["name"] == "soil"
    assert by_id["UO:0000196"]["name"] == "pH"
    assert by_id["CommunityMech:999992"]["name"] == "Community B"
    errors, warnings = [], []
    node_ids = validate_nodes(output / "nodes.tsv", errors)
    assert validate_edges(output / "edges.tsv", node_ids, errors, warnings) == len(edges)
    assert not errors and not warnings


def test_output_and_ids_are_deterministic_after_input_order_changes(tmp_path):
    docs = records()
    output, _, _ = export(tmp_path, docs)
    before = [(output / name).read_bytes() for name in ("nodes.tsv", "edges.tsv")]
    docs[0]["soils"].reverse()
    docs[0]["related_communities"].reverse()
    export(tmp_path, list(reversed(docs)))
    assert before == [(output / name).read_bytes() for name in ("nodes.tsv", "edges.tsv")]


@pytest.mark.parametrize("failure", ["duplicate_id", "missing_target"])
def test_ambiguous_or_missing_record_identity_fails_before_writing(tmp_path, failure):
    docs = records()
    if failure == "duplicate_id":
        docs[1]["id"] = docs[0]["id"]
    else:
        docs.pop()
    with pytest.raises(ValueError):
        export(tmp_path, docs)
    assert not (tmp_path / "graph/nodes.tsv").exists()


def test_related_isolate_identity_is_imported_without_fabricated_membership(tmp_path, monkeypatch):
    source = tmp_path / "communities"
    source.mkdir()
    doc, isolate = records()
    (source / "source.yaml").write_text(yaml.safe_dump(doc))
    isolate_path = tmp_path / "isolate.yaml"
    isolate_path.write_text(yaml.safe_dump(isolate))
    monkeypatch.setattr(kgx, "DEFAULT_KB", source)
    monkeypatch.setattr(kgx, "record_files", lambda: [source / "source.yaml", isolate_path])
    output = tmp_path / "graph"
    kgx.export_kgx(source, output)
    with (output / "nodes.tsv").open() as handle:
        nodes = {n["id"]: n for n in csv.DictReader(handle, delimiter="\t")}
    assert nodes[isolate["id"]]["name"] == isolate["name"]
    assert json.loads((output / "manifest.json").read_text())["input_record_count"] == 1


def test_relative_default_kb_uses_one_identity_per_source_file(tmp_path, monkeypatch):
    """The maintained just recipe passes --kb kb/communities explicitly."""
    kb = tmp_path / "kb/communities"
    kb.mkdir(parents=True)
    paths = []
    for index, doc in enumerate(records()):
        path = kb / f"record{index}.yaml"
        path.write_text(yaml.safe_dump(doc))
        paths.append(path)
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(kgx, "DEFAULT_KB", kb)
    monkeypatch.setattr(kgx, "record_files", lambda: paths)
    from pathlib import Path

    kgx.export_kgx(Path("kb/communities"), tmp_path / "relative", "record0.yaml")
    kgx.export_kgx(kb, tmp_path / "absolute", "record0.yaml")
    for name in ("nodes.tsv", "edges.tsv"):
        assert (tmp_path / "relative" / name).read_bytes() == (
            tmp_path / "absolute" / name
        ).read_bytes()
