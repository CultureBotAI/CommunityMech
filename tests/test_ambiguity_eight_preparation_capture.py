"""Actual transient file edits cannot replace accepted source judgments (#2879)."""

import importlib.util
import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
HELPERS = [
    "scripts/adhoc/prepare_ambiguity_eight_sources_20261115.py",
    "scripts/adhoc/prepare_ambiguity_eight_sources_v2_20261115.py",
]


@pytest.fixture(params=HELPERS)
def fixture(tmp_path, monkeypatch, request):
    helper = request.param
    spec = importlib.util.spec_from_file_location("eight_preparation", ROOT / helper)
    producer = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(producer)
    monkeypatch.setattr(producer, "ROOT", tmp_path)
    monkeypatch.setattr(producer, "__file__", str(tmp_path / helper))

    def write(name, raw):
        path = tmp_path / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(raw)
        return producer.sha(raw)

    write(helper, (ROOT / helper).read_bytes())
    if hasattr(producer, "PRESERVED_INPUTS"):
        for name, expected in producer.PRESERVED_INPUTS.items():
            assert write(name, (ROOT / name).read_bytes()) == expected
    before = write("kb/communities/example.yaml", b"id: CommunityMech:000505\n")
    source_sha = write("references_cache/example.txt", b"Exact source identity and boundary.\n")
    ledger_sha = write("reports/ledger.yaml", b"historical: true\n")
    guard_sha = write("tests/guard.py", b"assert True\n")
    assignment_sha = write("reports/assignments.json", b"[]\n")
    term = {"id": "NCBITaxon:528", "label": "Ochrobactrum"}
    native = {"ambiguous": True, "gtdb_options": ["GTDB:g__Ochrobactrum"]}
    row = {
        "id": "CommunityMech:000505",
        "path": "kb/communities/example.yaml",
        "before_sha256": before,
        "preservation": "Preserve the stock identity.",
        "proposed_occurrences": [
            {
                "selector": "taxonomy[0].taxon_term",
                "stock": "SRCHD06",
                "correspondence": {
                    "descriptor": term,
                    "expected_rank": "genus",
                    "historical_expected": native,
                    "boundary": "No stock genome inference.",
                },
            }
        ],
    }
    plan = {
        "records": [row] + [{"id": f"CommunityMech:000{i}"} for i in range(506, 510)],
        "primary_source": {
            "reference": "doi:10.example/source",
            "url": "https://doi.org/10.example/source",
            "retained_path": "references_cache/example.txt",
            "retained_sha256": source_sha,
            "locator": "Methods",
            "coverage": "Selected source text only.",
            "exact_short_quote": "Exact source identity",
            "judgment": "Accepted source judgment.",
        },
        "historical_guard": {
            "path": "tests/guard.py",
            "sha256": guard_sha,
            "ledger": "reports/ledger.yaml",
            "ledger_sha256": ledger_sha,
            "note": "Preserve the historical record.",
        },
        "historical_mapping_input": {
            "path": "reports/assignments.json",
            "sha256": assignment_sha,
        },
    }
    first = {"records": [{"id": f"CommunityMech:000{i}"} for i in (400, 499, 500)]}
    plans = {
        "reports/first-plan.json": write("reports/first-plan.json", json.dumps(first).encode()),
        "reports/plan.json": write("reports/plan.json", json.dumps(plan).encode()),
    }
    monkeypatch.setattr(producer, "PLANS", plans)
    route = {
        "records": [
            {
                "record_id": row["id"],
                "record": row["path"],
                "before_sha256": before,
                "occurrences": [
                    {
                        "taxonomy_index": 0,
                        "term": term,
                        "strain_name": "SRCHD06",
                        "native_result": native,
                        "classify_status": {
                            "status": "AMBIGUOUS",
                            "candidates": native["gtdb_options"],
                        },
                    }
                ],
            }
        ]
    }
    stem = ".temp/phase2-schema-20261115/fixture-route"
    route_sha = write(stem + ".log", json.dumps(route).encode())
    write(stem + ".json", json.dumps({"exit_code": 0, "log_sha256": route_sha}).encode())
    write(stem + ".exit", b"0\n")
    return tmp_path, {"plan": "reports/plan.json", "route": stem + ".log"}, producer


@pytest.mark.parametrize("kind", ["plan", "route"])
@pytest.mark.parametrize("restore_before_final_check", [True, False])
def test_full_producer_binds_captured_bytes_and_checks_persistence(
    fixture, monkeypatch, kind, restore_before_final_check
):
    root, names, producer = fixture
    baseline = producer.prepare("fixture-route", "CommunityMech:000505")
    path = root / names[kind]
    original = path.read_bytes()
    changed = json.loads(original)
    if kind == "plan":
        changed["primary_source"]["judgment"] = "Unreviewed transient scientific judgment."
    else:
        changed["records"][0]["occurrences"][0]["classify_status"]["status"] = "GROUNDED"
    changed_raw = json.dumps(changed).encode()
    assert changed_raw != original
    read, verify = producer.CapturedInputs.read, producer.CapturedInputs.verify
    mutated = []

    def transient_read(capture, name):
        raw = read(capture, name)
        if name == names[kind] and not mutated:
            path.write_bytes(changed_raw)
            assert path.read_bytes() == changed_raw
            mutated.append(True)
        return raw

    def final_check(capture):
        assert mutated and path.read_bytes() == changed_raw
        if restore_before_final_check:
            path.write_bytes(original)
            assert path.read_bytes() == original
        return verify(capture)

    with monkeypatch.context() as patch:
        patch.setattr(producer.CapturedInputs, "read", transient_read)
        patch.setattr(producer.CapturedInputs, "verify", final_check)
        if restore_before_final_check:
            assert producer.prepare("fixture-route", "CommunityMech:000505") == baseline
        else:
            with pytest.raises(ValueError, match="captured input changed"):
                producer.prepare("fixture-route", "CommunityMech:000505")
    assert mutated
    path.write_bytes(original)
    assert path.read_bytes() == original
    assert producer.prepare("fixture-route", "CommunityMech:000505") == baseline


def test_changed_accepted_plan_is_refused_before_judgment(fixture):
    root, names, producer = fixture
    baseline = producer.prepare("fixture-route", "CommunityMech:000505")
    path = root / names["plan"]
    original = path.read_bytes()
    changed = original.replace(b"Accepted source judgment.", b"Unsupported stock assignment.")
    path.write_bytes(changed)
    assert path.read_bytes() != original
    with pytest.raises(ValueError, match="accepted input differs"):
        producer.prepare("fixture-route", "CommunityMech:000505")
    path.write_bytes(original)
    assert path.read_bytes() == original
    assert producer.prepare("fixture-route", "CommunityMech:000505") == baseline
