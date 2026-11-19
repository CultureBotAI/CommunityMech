"""Bind actual toy native routes to authored sources; mutations must refuse (#2848)."""

import ast
import copy
import importlib.util
import json
import sqlite3
from pathlib import Path

import pytest
import yaml
from test_gtdb_batch_route_report import case as route_case  # noqa: F401
from test_gtdb_batch_route_report import run as run_route

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "batch_source_binder", ROOT / "scripts/adhoc/bind_gtdb_batch_source_context_20261115.py"
)
binder = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(binder)


@pytest.fixture
def case(request, monkeypatch):
    case = request.getfixturevalue("route_case")
    root = case["root"]
    monkeypatch.setattr(binder, "ROOT", root)
    (root / binder.HELPER).write_bytes((ROOT / binder.HELPER).read_bytes())
    report = run_route(case)
    monkeypatch.setattr(binder, "TABLE_SHA", report["inputs"][case["mapping"]])
    raw = json.dumps(report, indent=2).encode()
    route_path = root / ".temp/routes.json"
    route_path.write_bytes(raw)
    receipt = {
        "command": [
            ".venv/bin/python",
            binder.REPORTER,
            "--plan",
            str(case["plan"].relative_to(root)),
            "--plan-sha256",
            report["plan_sha256"],
            "--expected-revision",
            case["revision"],
            "--mapping",
            case["mapping"],
        ],
        "head": case["revision"],
        "started_at": "2026-11-15T06:00:00+00:00",
        "finished_at": "2026-11-15T06:00:01+00:00",
        "exit_code": 0,
        "status": "PASSED",
        "log_bytes": len(raw),
        "log_sha256": binder.sha(raw),
    }
    receipt_path = root / ".temp/receipt.json"
    receipt_path.write_text(json.dumps(receipt))
    exit_path = root / ".temp/exit.txt"
    exit_path.write_bytes(b"0\n")
    source = root / ".temp/paper.txt"
    source.write_text(
        "PMID:1234. Example species stock X was assayed. Identity remains provisional."
    )
    case["database"].unlink()
    with sqlite3.connect(case["database"]) as connection:
        connection.execute(
            "CREATE TABLE statements(subject TEXT,predicate TEXT,value TEXT,object TEXT)"
        )
        for occurrence in report["records"][0]["occurrences"]:
            term = occurrence["term"]
            if occurrence["taxonomy_index"] == 3:
                continue
            connection.executemany(
                "INSERT INTO statements VALUES (?,?,?,?)",
                [
                    (term["id"], "rdfs:label", term["label"], None),
                    (term["id"], "rank", None, "NCBITaxon:species"),
                ],
            )

    def item(path):
        return {"path": str(path.relative_to(root)), "sha256": binder.sha(path.read_bytes())}

    observed = report["records"][0]["occurrences"][0]
    authored = {
        key: observed[key]
        for key in ("taxonomy_index", "term", "strain_name", "native_result", "classify_status")
    }
    authored.update(
        expected_ncbi_rank="NCBITaxon:species",
        source_assessment="Source names the descriptor; no stock genome assignment.",
        population_scope="All native alternatives retained; no strain denominator inferred.",
        name_scope="Species descriptor only; source naming unchanged.",
    )
    config = {
        "route_report": item(route_path),
        "route_receipt": item(receipt_path),
        "route_exit": item(exit_path),
        "records": [
            {
                **case["entry"],
                "additional_inputs": {},
                "occurrences": [authored],
                "primary_sources": [
                    {
                        **item(source),
                        "reference": "PMID:1234",
                        "locator": "Methods fixture",
                        "coverage": "One test paragraph",
                        "identity_tokens": ["PMID:1234"],
                        "anchors": ["Example species stock X was assayed."],
                    }
                ],
                "historical_guard_assessment": "Keep all historical biological assertions.",
            }
        ],
    }
    config_path = root / ".temp/context.json"
    config_path.write_text(json.dumps(config))
    case.update(
        config=config,
        config_path=config_path,
        route_path=route_path,
        receipt_path=receipt_path,
        source=source,
        route=report,
    )
    return case


def run(case):
    return binder.bind(
        str(case["config_path"].relative_to(case["root"])),
        binder.sha(case["config_path"].read_bytes()),
        case["revision"],
        case["database"],
    )


def test_actual_route_context_and_exact_unit_inputs(case):
    result = run(case)
    row = result["records"][0]
    assert (
        row["occurrences"][0]["native_result"]
        == case["route"]["records"][0]["occurrences"][0]["native_result"]
    )
    assert len(row["occurrences"][0]["classify_status"]["candidates"]) == 11
    assert len(row["occurrences"][0]["ncbi_identity_rows"]) == 2
    assert row["record"] in row["input_paths"]
    assert case["config"]["route_report"]["path"] in row["input_paths"]
    assert ".temp/paper.txt" in row["input_paths"]
    assert set(row["input_paths"]) <= set(result["inputs"])
    assert result["scientific_review"] is False
    assert result["canonical_writes"] is False


def test_native_builder_retains_each_captured_primary_locator(case):
    """Exercise the frozen builder's actual projection, not a parallel implementation (#2868)."""
    raw = "PMID:1234.\nα Example species stock X was assayed.\nIdentity remains provisional."
    case["source"].write_text(raw)
    source = case["config"]["records"][0]["primary_sources"][0]
    source["sha256"] = binder.sha(raw.encode())
    source["anchors"].append("Identity remains provisional.")
    case["config_path"].write_text(json.dumps(case["config"]))
    row = run(case)["records"][0]
    builder_path = ROOT / "scripts/adhoc/build_gtdb_batch_diagnostic_20261115.py"
    tree = ast.parse(builder_path.read_bytes())
    projections = [
        value
        for node in ast.walk(tree)
        if isinstance(node, ast.Dict)
        for key, value in zip(node.keys, node.values, strict=True)
        if isinstance(key, ast.Constant) and key.value == "primary_locators"
    ]
    assert len(projections) == 1
    projection = compile(ast.Expression(projections[0]), str(builder_path), "eval")
    locators = eval(projection, {"row": row})  # noqa: S307 - exact repository consumer expression
    assert locators == [
        {
            "reference": "PMID:1234",
            "path": ".temp/paper.txt",
            "character_offset": 13,
            "line": 2,
        },
        {
            "reference": "PMID:1234",
            "path": ".temp/paper.txt",
            "character_offset": 50,
            "line": 3,
        },
    ]
    assert row["primary_sources"] == [source]
    assert [item["anchor"] for item in row["primary_contexts"]] == source["anchors"]


@pytest.mark.parametrize(
    "mutation", ["descriptor", "stock", "result", "status", "anchor", "empty_scope", "duplicate"]
)
def test_authored_context_mutations_are_refused_and_restoration_passes(case, mutation):
    assert run(case)["inputs_unchanged"]
    original = case["config_path"].read_bytes()
    doc = json.loads(original)
    selected = doc["records"][0]
    occurrence = selected["occurrences"][0]
    if mutation == "descriptor":
        occurrence["term"]["label"] = "Other species"
    elif mutation == "stock":
        occurrence["strain_name"] = "invented stock"
    elif mutation == "result":
        occurrence["native_result"]["gtdb_options"].pop()
    elif mutation == "status":
        occurrence["classify_status"]["status"] = "GROUNDED"
    elif mutation == "anchor":
        selected["primary_sources"][0]["anchors"] = ["absent source claim"]
    elif mutation == "empty_scope":
        occurrence["population_scope"] = ""
    else:
        selected["occurrences"].append(dict(occurrence))
    case["config_path"].write_text(json.dumps(doc))
    with pytest.raises(ValueError):
        run(case)
    case["config_path"].write_bytes(original)
    assert run(case)["inputs_unchanged"]


@pytest.mark.parametrize("mutation", ["unfinished", "failed", "wrong_log", "wrong_command"])
def test_rehashed_bad_receipt_is_not_native_completion(case, mutation):
    assert run(case)["inputs_unchanged"]
    receipt = json.loads(case["receipt_path"].read_bytes())
    if mutation == "unfinished":
        receipt["finished_at"] = "2026-11-15T05:59:59+00:00"
    elif mutation == "failed":
        receipt["exit_code"] = 1
    elif mutation == "wrong_log":
        receipt["log_sha256"] = "0" * 64
    else:
        receipt["command"][1] = "scripts/other.py"
    case["receipt_path"].write_text(json.dumps(receipt))
    config = case["config"]
    config["route_receipt"]["sha256"] = binder.sha(case["receipt_path"].read_bytes())
    case["config_path"].write_text(json.dumps(config))
    with pytest.raises(ValueError):
        run(case)


@pytest.mark.parametrize("changed", ["source", "target", "receipt_path", "config_path"])
def test_mutation_during_authority_read_refuses_before_stdout(case, monkeypatch, changed):
    assert run(case)["inputs_unchanged"]
    actual = binder.identity
    path = case[changed]
    original = path.read_bytes()

    def mutate(*args):
        result = actual(*args)
        path.write_bytes(original + b"\nchanged\n")
        assert path.read_bytes() != original
        return result

    monkeypatch.setattr(binder, "identity", mutate)
    with pytest.raises(ValueError, match="changed"):
        run(case)
    path.write_bytes(original)
    monkeypatch.setattr(binder, "identity", actual)
    assert run(case)["inputs_unchanged"]


def test_null_route_stays_null_with_uncertain_classification(case):
    config = case["config"]
    observed = case["route"]["records"][0]["occurrences"][2]
    occurrence = config["records"][0]["occurrences"][0]
    for key in ("taxonomy_index", "term", "strain_name", "native_result", "classify_status"):
        occurrence[key] = observed[key]
    case["config_path"].write_text(json.dumps(config))
    result = run(case)["records"][0]["occurrences"][0]
    assert result["native_result"] is None
    assert result["classify_status"] == {"status": "UNRESOLVED", "candidates": []}


def test_local_authority_mismatch_is_not_substituted(case):
    assert run(case)["inputs_unchanged"]
    with sqlite3.connect(case["database"]) as connection:
        connection.execute(
            "UPDATE statements SET value='Wrong species' WHERE predicate='rdfs:label'"
        )
    with pytest.raises(ValueError, match="label/rank"):
        run(case)


def test_batch_unit_inputs_exclude_unrelated_records_but_keep_explicit_dependency(case):
    second = case["root"] / "data/isolates/Fixture_Second.yaml"
    second.parent.mkdir(parents=True)
    doc = yaml.safe_load(case["target"].read_bytes())
    doc["id"] = "CommunityMech:999995"
    second.write_text(yaml.safe_dump(doc))
    entry = {
        "record": str(second.relative_to(case["root"])),
        "record_id": doc["id"],
        "before_sha256": binder.sha(second.read_bytes()),
    }
    case["plan"].write_text(json.dumps({"records": [case["entry"], entry]}))
    route = run_route(case)
    raw = json.dumps(route, indent=2).encode()
    case["route_path"].write_bytes(raw)
    receipt = json.loads(case["receipt_path"].read_bytes())
    receipt.update(log_bytes=len(raw), log_sha256=binder.sha(raw))
    command = receipt["command"]
    command[command.index("--plan-sha256") + 1] = route["plan_sha256"]
    case["receipt_path"].write_text(json.dumps(receipt))
    config = case["config"]
    config["route_report"]["sha256"] = binder.sha(raw)
    config["route_receipt"]["sha256"] = binder.sha(case["receipt_path"].read_bytes())
    other = copy.deepcopy(config["records"][0])
    other.update(entry)
    other["additional_inputs"] = {case["entry"]["record"]: case["entry"]["before_sha256"]}
    config["records"].append(other)
    case["config_path"].write_text(json.dumps(config))
    result = run(case)
    first_inputs = result["records"][0]["input_paths"]
    second_inputs = result["records"][1]["input_paths"]
    assert entry["record"] not in first_inputs
    assert case["entry"]["record"] in second_inputs
    assert entry["record"] in second_inputs
    assert set(first_inputs) | set(second_inputs) <= set(result["inputs"])


def test_database_changed_during_read_refuses_result(case, monkeypatch):
    assert run(case)["inputs_unchanged"]
    actual = binder.identity

    def mutate(*args):
        result = actual(*args)
        with sqlite3.connect(case["database"]) as connection:
            connection.execute("UPDATE statements SET value='Changed' WHERE predicate='rdfs:label'")
        return result

    monkeypatch.setattr(binder, "identity", mutate)
    with pytest.raises(ValueError, match="database stat changed"):
        run(case)
