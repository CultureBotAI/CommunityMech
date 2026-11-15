"""Real native measurements plus adversarial accounting/privacy export controls."""

import importlib.util
import json
import subprocess
from pathlib import Path

import pytest
import yaml
from test_reference_assertion_coverage import coverage, fixture_repo  # noqa: F401

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "phase2_reference_export",
    ROOT / "scripts/adhoc/export_phase2_reference_measurement_20261115.py",
)
exporter = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(exporter)


@pytest.fixture
def measured(
    fixture_repo,  # noqa: F811 - imported pytest fixture
    request,
):
    root = fixture_repo
    if getattr(request, "param", None) == "case-alias":
        source = root / "references_cache/PMID_1.md"
        lower = source.with_name("pmid_1.md")
        if not lower.exists() or not lower.samefile(source):
            pytest.skip("Native case-alias reproduction requires a case-insensitive filesystem")
        source.rename(lower)
    schema_path = root / coverage.SCHEMA
    schema = yaml.safe_load(schema_path.read_text())
    schema["classes"]["SupportingReference"]["attributes"] = {
        "snippet": {"implements": ["linkml:excerpt"]},
        "reference": {"implements": ["linkml:authoritative_reference"]},
    }
    schema_path.write_text(yaml.safe_dump(schema))
    records = root / "kb/communities"
    records.mkdir(parents=True)
    document = {
        "evidence": [
            {"snippet": "alpha", "reference": "PMID:1"},
            {"snippet": "alpha ... beta", "reference": "PMID:1"},
            {"snippet": "unsupported", "reference": "PMID:1"},
            {"snippet": "not compared", "reference": "BIOPROJECT:PRJ1"},
            {"snippet": "not cached", "reference": "PMID:2"},
            {"snippet": "no content", "reference": "PMID:3"},
            {"snippet": "   ", "reference": "PMID:1"},
            {"snippet": "missing reference"},
        ],
        "discussions": [{"snippet": "alpha", "reference": "PMID:1"}],
        "unknown": {"snippet": "not traversed", "reference": "PMID:1"},
        "titles": [{"title": "Source title", "reference": "PMID:1"}],
    }
    (records / "sample.yaml").write_text(yaml.safe_dump(document, sort_keys=False))
    (records / "empty.yaml").write_text("{}\n")
    (root / "uv.lock").write_text("retained lock fixture\n")
    (root / "pyproject.toml").write_text("[project]\nname='fixture'\n")
    (root / exporter.SCRIPT).parent.mkdir()
    (root / exporter.SCRIPT).write_bytes(Path(coverage.__file__).read_bytes())
    subprocess.run(["git", "init", "-q", str(root)], check=True)
    subprocess.run(["git", "-C", str(root), "add", "."], check=True)
    subprocess.run(
        [
            "git",
            "-C",
            str(root),
            "-c",
            "user.name=Offline fixture",
            "-c",
            "user.email=fixture@example.invalid",
            "commit",
            "-qm",
            "fixture",
        ],
        check=True,
    )
    run = root / ".temp/native-measurement"
    coverage.run(root, run, None)
    return root, run


def summarize(measured):
    return exporter.checked_summary(*measured, execution_host="local")


def change_case(run, mutate):
    receipt = json.loads((run / "receipt.json").read_text())
    case = receipt["cases"][0]
    mutate(case)
    (run / "measurement.json").write_text(json.dumps(case))
    (run / "receipt.json").write_text(json.dumps(receipt))


def test_actual_native_counts_ellipsis_omissions_classes_and_zero_assertion_record(measured):
    root, _ = measured
    before = {path: path.read_bytes() for path in root.rglob("*") if path.is_file()}
    report = summarize(measured)
    assert report["counts"]["snippet_occurrences_compared"] == 4
    assert report["counts"]["substring_parts_compared"] == 5
    assert report["counts"]["title_only_invocations"] == 1
    assert report["counts"]["native_issues"] == 4
    assert report["record_processing_complete"] and report["full_inventory_processed"]
    assert not report["assertion_coverage_complete"] and not report["native_validation_passed"]
    assert report["native_exit_code"] == report["wrapper_exit_code"] == 1
    assert report["records"][0]["record_kind"] == "no_snippet_surfaces"
    classes = report["records"][1]["native_classes"]
    assert classes["SupportingReference"] == {
        "surfaces": 1,
        "compared": 1,
        "status_counts": {"matched": 1},
    }
    assert classes["outside_native_traversal"]["compared"] == 0
    public = json.dumps(report) + exporter.markdown(report)
    assert all(value not in public for value in ("alpha", "PMID:1", "Source title", str(root)))
    assert report["execution_declaration"]["python_version"] is None
    assert not report["process_exit_independently_retained"]
    assert before == {path: path.read_bytes() for path in root.rglob("*") if path.is_file()}


@pytest.mark.parametrize(
    "damage",
    [
        "counter",
        "class",
        "reference",
        "comparison",
        "status",
        "coverage",
        "native_exit",
        "record_order",
    ],
)
def test_mutually_consistent_case_and_aggregate_cannot_forge_accounting(measured, damage):
    _, run = measured

    def mutate(case):
        assertion = case["records"][1]["assertions"][0]
        if damage == "counter":
            case["counts"]["snippet_occurrences_compared"] += 1
        elif damage == "class":
            assertion["native_class"] = "SupportingReference"
        elif damage == "reference":
            assertion["normalized_reference"] = "PMID:4"
        elif damage == "comparison":
            assertion["actually_compared"] = False
        elif damage == "status":
            assertion["status"] = "skipped_prefix"
        elif damage == "coverage":
            case["assertion_coverage_complete"] = True
        elif damage == "native_exit":
            case["native_exit_code"] = 0
        else:
            case["records"].reverse()

    change_case(run, mutate)
    with pytest.raises(ValueError):
        summarize(measured)


@pytest.mark.parametrize(
    "damage",
    ["start", "case", "inventory", "record", "added_cache", "removed_cache", "log", "wrapper_exit"],
)
def test_independent_inputs_start_log_and_exit_are_required(measured, damage):
    root, run = measured
    if damage == "start":
        data = json.loads((run / "started.json").read_text())
        data["scope"] = "different scope"
        (run / "started.json").write_text(json.dumps(data))
    elif damage == "case":
        (run / "measurement.json").write_text("{}")
    elif damage in {"inventory", "wrapper_exit"}:
        data = json.loads((run / "receipt.json").read_text())
        if damage == "inventory":
            data["declared_records"] = data["declared_records"][1:]
            start = json.loads((run / "started.json").read_text())
            start["declared_records"] = data["declared_records"]
            (run / "started.json").write_text(json.dumps(start))
        else:
            data["exit_code"] = 0
        (run / "receipt.json").write_text(json.dumps(data))
    elif damage == "record":
        (root / "kb/communities/sample.yaml").write_text("{}")
    elif damage == "added_cache":
        (root / "references_cache/new.md").write_text("unexpected")
    elif damage == "removed_cache":
        (root / "references_cache/PMID_1.md").unlink()
    else:
        log = run / "measurement.log"
        log.write_text(log.read_text().replace("Total checks: 4", "Total checks: 0"))
    with pytest.raises(ValueError):
        summarize(measured)


def test_retained_process_exit_and_runtime_are_explicit(measured):
    root, run = measured
    path = run / "launcher.exit"
    path.write_text("1\n")
    report = exporter.checked_summary(root, run, "M5", "3.13.2", path)
    assert report["process_exit_independently_retained"]
    assert report["execution_declaration"]["host"] == "M5"
    assert "Caller declaration" in report["execution_declaration"]["authority"]
    path.write_text("0\n")
    with pytest.raises(ValueError, match="Retained process exit"):
        exporter.checked_summary(root, run, "M5", "3.13.2", path)


@pytest.mark.parametrize("measured", ["case-alias"], indirect=True)
def test_native_case_alias_is_bound_to_one_physical_cache_file(measured):
    """The actual native fetcher requests uppercase; disk inventory has lowercase."""
    root, run = measured
    receipt = json.loads((run / "receipt.json").read_text())
    assert "references_cache/pmid_1.md" in receipt["input_sha256"]
    assert "references_cache/PMID_1.md" not in receipt["input_sha256"]
    event = receipt["cases"][0]["records"][1]["assertions"][0]
    assert event["cache"]["requested_path"] == "references_cache/PMID_1.md"
    assert (root / event["cache"]["requested_path"]).samefile(root / "references_cache/pmid_1.md")
    report = summarize(measured)
    assert report["counts"]["snippet_occurrences_compared"] == 4
    assert report["counts"]["native_issues"] == 4


def test_cache_alias_requires_unique_candidate_matching_bytes_and_physical_identity(
    tmp_path, monkeypatch
):
    """#2829: neither matching spelling nor a retained digest alone is sufficient."""
    cache = tmp_path / "references_cache"
    cache.mkdir()
    path = cache / "source.md"
    path.write_text("retained source")
    digest = exporter.sha(path.read_bytes())
    item = {"requested_path": "references_cache/SOURCE.md", "sha256": digest}
    manifest = {"references_cache/source.md": digest}
    # Physical-identity branch is deterministic on case-sensitive CI too.
    monkeypatch.setattr(Path, "is_file", lambda self: True)
    monkeypatch.setattr(Path, "samefile", lambda self, other: False)
    with pytest.raises(ValueError, match="same physical file"):
        exporter.verify_cache_identity(tmp_path, manifest, item)
    monkeypatch.setattr(Path, "samefile", lambda self, other: True)
    exporter.verify_cache_identity(tmp_path, manifest, item)
    with pytest.raises(ValueError, match="absent or ambiguous"):
        exporter.verify_cache_identity(
            tmp_path, {**manifest, "references_cache/Source.md": digest}, item
        )
    with pytest.raises(ValueError, match="Loaded cache"):
        exporter.verify_cache_identity(tmp_path, manifest, {**item, "sha256": "0" * 64})
    path.write_text("changed source")
    with pytest.raises(ValueError, match="Current aliased cache"):
        exporter.verify_cache_identity(tmp_path, manifest, item)
    with pytest.raises(ValueError, match="absent or ambiguous"):
        exporter.verify_cache_identity(
            tmp_path, manifest, {**item, "requested_path": "references_cache/other.md"}
        )
