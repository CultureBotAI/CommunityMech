"""Exercise native route reporting and input refusal with isolated Git fixtures (#2848)."""

import gzip
import importlib.util
import json
import subprocess
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "batch_route_report", ROOT / "scripts/adhoc/report_gtdb_batch_routes_20261115.py"
)
reporter = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(reporter)


def row(number, species, genus, gtdb_species, gtdb_genus, total=1):
    cells = [""] * 19
    cells[0], cells[2], cells[3] = str(number), str(total), "1.0"
    cells[4:11] = ["Bacteria", "Bacillota", "Bacilli", "Testales", "Testaceae", genus, species]
    cells[12:19] = [
        "Bacteria",
        "Bacillota",
        "Bacilli",
        "Testales",
        "Testaceae",
        gtdb_genus,
        gtdb_species,
    ]
    return "\t".join(cells)


@pytest.fixture
def case(tmp_path, monkeypatch):
    root = tmp_path / "repository"
    root.mkdir()
    for relative in (*reporter.MODULES.values(), reporter.HELPER, "pyproject.toml", "uv.lock"):
        path = root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes((ROOT / relative).read_bytes())
    subprocess.run(["git", "init", "--quiet", "--initial-branch=fixture"], cwd=root, check=True)
    subprocess.run(["git", "add", "."], cwd=root, check=True)
    subprocess.run(
        [
            "git",
            "-c",
            "user.name=Codex",
            "-c",
            "user.email=codex@users.noreply.github.com",
            "-c",
            "commit.gpgsign=false",
            "-c",
            "core.hooksPath=/dev/null",
            "commit",
            "--quiet",
            "-m",
            "Native fixture sources",
        ],
        cwd=root,
        check=True,
    )
    monkeypatch.setattr(reporter, "ROOT", root)
    mapping = ".temp/NCBI2GTDB.tsv.gz"
    table = root / mapping
    table.parent.mkdir()
    lines = ["\t".join(f"column_{i}" for i in range(19))]
    lines += [
        row(i, "Example species", "Example", f"Example option{i}", "Example") for i in range(11)
    ]
    lines += [
        row(500, "Rankus alba", "Rankus", "Rankus alba", "Rankus", 8),
        row(501, "Rankus sp. X", "Rankus", "Altus spX", "Altus", 100),
    ]
    table.write_bytes(gzip.compress(("\n".join(lines) + "\n").encode()))
    monkeypatch.setattr(reporter, "TABLE_SHA", reporter.digest(table.read_bytes()))
    database = root / ".temp/oaklib/ncbitaxon.db"
    database.parent.mkdir()
    database.write_bytes(b"toy adapter stand-in; only the OAK constructor is doubled")
    import oaklib

    class LocalAdapter:
        def ancestors(self, _curies, predicates):
            assert predicates == ["rdfs:subClassOf"]
            return ["NCBITaxon:2"]

    selectors = []

    def local_adapter(selector):
        selectors.append(selector)
        assert selector == f"sqlite:{database}"
        return LocalAdapter()

    monkeypatch.setattr(oaklib, "get_adapter", local_adapter)
    record = "kb/communities/Fixture_Routes.yaml"
    target = root / record
    target.parent.mkdir(parents=True)
    doc = {
        "id": "CommunityMech:999991",
        "taxonomy": [
            {"taxon_term": {"term": {"id": "NCBITaxon:9991", "label": "Example species"}}},
            {"taxon_term": {"term": {"id": "NCBITaxon:9992", "label": "Rankus"}}},
            {"taxon_term": {"term": {"id": "NCBITaxon:9993", "label": "Unknownus"}}},
            {
                "taxon_term": {
                    "term": {"id": "NCBITaxon:9991", "label": "Example species"},
                    "gtdb_classification": {"curated": True, "gtdb_id": "GTDB:s__held"},
                },
                "strain_designation": {"strain_name": "held-stock"},
            },
        ],
    }
    target.write_text(yaml.safe_dump(doc))
    plan = root / ".temp/plan.json"
    entry = {
        "record": record,
        "record_id": doc["id"],
        "before_sha256": reporter.digest(target.read_bytes()),
    }
    plan.write_text(json.dumps({"records": [entry]}))
    return {
        "root": root,
        "plan": plan,
        "mapping": mapping,
        "database": database,
        "target": target,
        "entry": entry,
        "revision": reporter.revision(),
        "selectors": selectors,
    }


def run(case, **kwargs):
    return reporter.report(
        str(case["plan"].relative_to(case["root"])),
        reporter.digest(case["plan"].read_bytes()),
        case["revision"],
        case["mapping"],
        case["database"],
        **kwargs,
    )


def test_native_full_options_null_rank_population_and_existing_hold(case):
    original = case["target"].read_bytes()
    result = run(case, record_id=case["entry"]["record_id"])
    rows = result["records"][0]["occurrences"]
    assert len(rows) == 4
    assert len(rows[0]["native_result"]["gtdb_options"]) == 11
    assert rows[0]["classify_status"]["candidates"] == rows[0]["native_result"]["gtdb_options"]
    assert rows[0]["classify_status"]["status"] == "AMBIGUOUS"
    assert rows[1]["native_result"]["via"] == "ncbi_rank_g"
    assert rows[1]["native_result"]["total_genomes"] == 8
    rank_hashes = rows[1]["lookup_indexes"]["ncbi_higher_name"]["rankus"]
    assert len(rank_hashes) == 2
    assert {result["crosswalk_rows"][key][2] for key in rank_hashes} == {"8", "100"}
    assert rows[2]["native_result"] is None
    assert rows[2]["classify_status"] == {"status": "UNRESOLVED", "candidates": []}
    assert rows[3]["classify_status"]["status"] == "GROUNDED"
    assert rows[3]["existing_descriptor"]["gtdb_classification"]["curated"] is True
    assert rows[3]["strain_name"] == "held-stock"
    assert result["inputs_unchanged"] is True
    assert result["scientific_review"] is False
    assert result["canonical_writes"] is False
    assert result["ncbi_database"]["content_sha256"] is None
    assert case["target"].read_bytes() == original
    assert case["selectors"] == [f"sqlite:{case['database']}"]


@pytest.mark.parametrize(
    "mutation", ["duplicate", "too_many", "unsafe_path", "wrong_id", "wrong_hash"]
)
def test_plan_refuses_ambiguous_population_or_changed_record(case, mutation):
    assert run(case)["selected_record_count"] == 1
    original = case["plan"].read_bytes()
    doc = json.loads(original)
    if mutation == "duplicate":
        doc["records"].append(dict(doc["records"][0]))
    elif mutation == "too_many":
        doc["records"] *= 11
    elif mutation == "unsafe_path":
        doc["records"][0]["record"] = "kb/communities/../../Fixture_Routes.yaml"
    elif mutation == "wrong_id":
        doc["records"][0]["record_id"] = "CommunityMech:999992"
    else:
        doc["records"][0]["before_sha256"] = "0" * 64
    case["plan"].write_text(json.dumps(doc))
    with pytest.raises(ValueError):
        run(case)
    case["plan"].write_bytes(original)
    assert run(case)["selected_record_count"] == 1


@pytest.mark.parametrize(
    "changed", ["target", "mapping", "native", "dependency", "database", "helper"]
)
def test_actual_input_change_during_computation_refuses_result(case, monkeypatch, changed):
    assert run(case)["inputs_unchanged"]
    paths = {
        "target": case["target"],
        "mapping": case["root"] / case["mapping"],
        "native": case["root"] / reporter.NATIVE,
        "dependency": case["root"] / "src/communitymech/validators/ncbi_domain.py",
        "database": case["database"],
        "helper": case["root"] / reporter.HELPER,
    }
    path = paths[changed]
    original = path.read_bytes()
    actual = reporter.compute

    def mutated(*args):
        result = actual(*args)
        path.write_bytes(original + b"\nchanged\n")
        assert path.read_bytes() != original
        return result

    monkeypatch.setattr(reporter, "compute", mutated)
    with pytest.raises(ValueError, match="changed"):
        run(case)
    path.write_bytes(original)
    assert path.read_bytes() == original
    monkeypatch.setattr(reporter, "compute", actual)
    assert run(case)["inputs_unchanged"]


def test_transient_table_and_record_edits_never_replace_captured_computation(case, monkeypatch):
    positive = run(case)
    actual = reporter.compute

    def transient(*args):
        paths = [case["target"], case["root"] / case["mapping"]]
        originals = {path: path.read_bytes() for path in paths}
        for path in paths:
            path.write_bytes(b"transient different bytes")
        try:
            return actual(*args)
        finally:
            for path, raw in originals.items():
                path.write_bytes(raw)

    monkeypatch.setattr(reporter, "compute", transient)
    observed = run(case)
    assert observed["records"] == positive["records"]
    assert observed["crosswalk_rows"] == positive["crosswalk_rows"]
    assert observed["inputs"] == positive["inputs"]


def test_explicit_plan_hash_revision_and_record_filter(case):
    args = [
        str(case["plan"].relative_to(case["root"])),
        reporter.digest(case["plan"].read_bytes()),
        case["revision"],
        case["mapping"],
        case["database"],
    ]
    for index, value in ((1, "0" * 64), (2, "0" * 40)):
        changed = list(args)
        changed[index] = value
        with pytest.raises(ValueError):
            reporter.report(*changed)
    with pytest.raises(ValueError, match="absent"):
        run(case, record_id="CommunityMech:999999")
    assert run(case)["selected_record_count"] == 1


def test_missing_adapter_never_falls_back_to_network(case, monkeypatch):
    import oaklib

    original = oaklib.get_adapter
    assert run(case)["inputs_unchanged"]
    selectors = []

    def missing(selector):
        selectors.append(selector)
        return None

    monkeypatch.setattr(oaklib, "get_adapter", missing)
    with pytest.raises(ValueError, match="no fallback"):
        run(case)
    assert selectors == [f"sqlite:{case['database']}"]
    monkeypatch.setattr(oaklib, "get_adapter", original)
    assert run(case)["inputs_unchanged"]


def test_no_network_path_during_native_adapter_construction(case, monkeypatch):
    import socket

    import oaklib

    called = []

    def attempt_network(_selector):
        with pytest.raises(RuntimeError, match="network is prohibited"):
            socket.create_connection(("example.invalid", 443))
        called.append(True)
        return None

    monkeypatch.setattr(oaklib, "get_adapter", attempt_network)
    with pytest.raises(ValueError, match="no fallback"):
        run(case)
    assert called == [True]


def test_exact_native_manual_hold_is_not_overridden_by_ambiguous_route(case):
    relative = "kb/communities/Dehalococcoides_Pelobacter_Acetylene_TCE_Coculture.yaml"
    path = case["root"] / relative
    doc = {
        "id": "CommunityMech:999993",
        "taxonomy": [{"taxon_term": {"term": {"id": "NCBITaxon:18", "label": "Example species"}}}],
    }
    path.write_text(yaml.safe_dump(doc))
    case["plan"].write_text(
        json.dumps(
            {
                "records": [
                    {
                        "record": relative,
                        "record_id": doc["id"],
                        "before_sha256": reporter.digest(path.read_bytes()),
                    }
                ]
            }
        )
    )
    result = run(case)["records"][0]["occurrences"][0]
    assert result["native_result"]["ambiguous"] is True
    assert result["classify_status"] == {"status": "WITHHELD", "candidates": []}
    assert result["manual_curated_reason"]


def test_same_plan_single_record_then_batch_preserves_each_native_result(case):
    second = case["root"] / "data/isolates/Fixture_Second.yaml"
    second.parent.mkdir(parents=True)
    doc = yaml.safe_load(case["target"].read_bytes())
    doc["id"] = "CommunityMech:999994"
    second.write_text(yaml.safe_dump(doc))
    case["plan"].write_text(
        json.dumps(
            {
                "records": [
                    case["entry"],
                    {
                        "record": str(second.relative_to(case["root"])),
                        "record_id": doc["id"],
                        "before_sha256": reporter.digest(second.read_bytes()),
                    },
                ]
            }
        )
    )
    canary = run(case, record_id=case["entry"]["record_id"])
    assert canary["planned_record_count"] == 2
    assert canary["selected_record_count"] == 1
    batch = run(case)
    assert batch["selected_record_count"] == 2
    assert batch["records"][0] == canary["records"][0]
    assert batch["records"][1]["occurrences"] == canary["records"][0]["occurrences"]
    assert batch["crosswalk_rows"] == canary["crosswalk_rows"]


def test_cli_refusal_emits_no_success_json(case, monkeypatch, capsys):
    monkeypatch.setattr(
        reporter.sys,
        "argv",
        [
            reporter.HELPER,
            "--plan",
            str(case["plan"].relative_to(case["root"])),
            "--plan-sha256",
            "0" * 64,
            "--expected-revision",
            case["revision"],
            "--mapping",
            case["mapping"],
            "--ncbi-db",
            str(case["database"]),
        ],
    )
    with pytest.raises(ValueError, match="plan hash"):
        reporter.main()
    assert capsys.readouterr().out == ""
