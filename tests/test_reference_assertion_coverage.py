"""Real CLI controls for measured assertions; issue counters alone cannot pass."""

from __future__ import annotations

import importlib.util
import json
import socket
import subprocess
from copy import deepcopy
from io import BytesIO
from pathlib import Path
from unittest.mock import patch
from zipfile import ZipFile

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "reference_assertion_coverage", ROOT / "scripts/reference_assertion_coverage.py"
)
coverage = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(coverage)


@pytest.fixture
def fixture_repo(tmp_path):
    schema = {
        "id": "https://example.org/reference-coverage",
        "name": "reference_coverage",
        "prefixes": {"linkml": "https://w3id.org/linkml/"},
        "imports": ["linkml:types"],
        "default_range": "string",
        "classes": {
            "Root": {
                "tree_root": True,
                "attributes": {
                    "evidence": {"range": "EvidenceItem", "multivalued": True},
                    "discussions": {"range": "SupportingReference", "multivalued": True},
                    "titles": {"range": "TitleOnly", "multivalued": True},
                },
            },
            "EvidenceItem": {
                "attributes": {
                    "snippet": {"implements": ["linkml:excerpt"]},
                    "reference": {"implements": ["linkml:authoritative_reference"]},
                }
            },
            "SupportingReference": {"attributes": {"snippet": {}, "reference": {}}},
            "TitleOnly": {"attributes": {"title": {}, "reference": {}}},
        },
    }
    (tmp_path / coverage.SCHEMA).parent.mkdir(parents=True)
    (tmp_path / coverage.SCHEMA).write_text(yaml.safe_dump(schema))
    (tmp_path / coverage.CONFIG).parent.mkdir(parents=True)
    (tmp_path / coverage.CONFIG).write_text(
        yaml.safe_dump(
            {
                "skip_prefixes": ["BIOPROJECT"],
                "literal_bracket_patterns": [".*"],
            }
        )
    )
    cache = tmp_path / "references_cache"
    cache.mkdir()
    (cache / "PMID_1.md").write_text(
        "---\nreference_id: PMID:1\ntitle: Source title\ncontent_type: full_text\n---\n"
        "# Source title\n\n## Content\n\nalpha beta expression of [NiFe]-hydrogenases\n"
    )
    (cache / "PMID_3.md").write_text(
        "---\nreference_id: PMID:3\ntitle: Empty source\n---\n# Empty source\n\n## Content\n"
    )
    return tmp_path


def invoke(root, document, name="record"):
    path = root / f"{name}.json"
    path.write_text(json.dumps(document))
    return coverage.measure(root, [(path.name, document)], [path])


def test_native_counts_comparisons_and_unexamined_surfaces(fixture_repo):
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
        "discussions": [{"snippet": "unannotated", "reference": "PMID:1"}],
        "unknown": {"snippet": "not traversed", "reference": "PMID:1"},
        "titles": [{"title": "Source title", "reference": "PMID:1"}],
    }
    before = {p.name: p.read_bytes() for p in (fixture_repo / "references_cache").iterdir()}
    result, log = invoke(fixture_repo, document)
    assert result["measurement_valid"], result["errors"]
    assert result["record_processing_complete"]
    assert not result["assertion_coverage_complete"]
    assert not result["validation_passed"]
    assert result["counts"] == {
        "records_selected": 1,
        "records_completed": 1,
        "snippet_surfaces": 10,
        "snippet_occurrences_compared": 3,
        "excerpt_validator_invocations": 7,
        "matcher_calls": 4,
        "substring_calls": 3,
        "substring_parts_compared": 4,
        "title_only_invocations": 1,
        "native_issues": 4,
    }
    assert result["assertion_status_counts"] == {
        "matched": 2,
        "mismatched": 1,
        "skipped_prefix": 1,
        "missing_cache": 1,
        "no_content": 1,
        "empty_query": 1,
        "no_extractable_reference": 1,
        "unannotated_excerpt": 1,
        "not_visited_by_native_schema": 1,
    }
    assert "Total checks: 4" in log
    assert result["records"][0]["title_only"][0]["status"] == "title_match"
    assert before == {p.name: p.read_bytes() for p in (fixture_repo / "references_cache").iterdir()}


def test_positive_mutated_restored_native_cli_and_literal_brackets(fixture_repo):
    good = {"evidence": [{"snippet": "expression of [NiFe]-hydrogenases", "reference": "PMID:1"}]}
    bad = deepcopy(good)
    bad["evidence"][0]["snippet"] = "expression of [FeFe]-hydrogenases"
    results = [
        invoke(fixture_repo, doc, str(index))[0] for index, doc in enumerate([good, bad, good])
    ]
    assert [r["native_exit_code"] for r in results] == [0, 1, 0]
    assert [r["validation_passed"] for r in results] == [True, False, True]
    assert all(
        r["measurement_valid"] and r["counts"]["substring_parts_compared"] == 1 for r in results
    )
    assert results[0]["counts"] == results[2]["counts"]


def test_reference_routing_mutation_with_identical_source_text_fails(fixture_repo):
    """#2795: wrong-citation comparisons cannot establish assertion coverage."""
    document = {"evidence": [{"snippet": "alpha", "reference": {"id": "pmid:1"}}]}
    alternate = fixture_repo / "references_cache/PMID_4.md"
    alternate.write_bytes(
        (fixture_repo / "references_cache/PMID_1.md")
        .read_bytes()
        .replace(b"reference_id: PMID:1", b"reference_id: PMID:4")
    )
    control, _ = invoke(fixture_repo, document, "control")
    native = coverage.ReferenceValidationPlugin._validate_excerpt

    def misroute(plugin, text, reference, expected_title, path, **kwargs):
        yield from native(plugin, text, "PMID:4", expected_title, path, **kwargs)

    with patch.object(coverage.ReferenceValidationPlugin, "_validate_excerpt", misroute):
        mutated, _ = invoke(fixture_repo, document, "mutation")
    restored, _ = invoke(fixture_repo, document, "restoration")
    assert control["validation_passed"] and restored["validation_passed"]
    assert mutated["native_validation_passed"]  # Identical text, wrong source.
    assert mutated["records"][0]["assertions"][0]["cache"]["loaded_reference_id"] == "PMID:4"
    assert not mutated["measurement_valid"]
    assert not mutated["assertion_coverage_complete"]
    assert any("Reference identity mismatch" in error for error in mutated["errors"])


@pytest.mark.parametrize("reference", ["pmid:1", {"id": "PMID 1"}, {"reference_id": "PMID:1"}])
def test_raw_reference_supported_forms_use_native_normalization(fixture_repo, reference):
    result, _ = invoke(fixture_repo, {"evidence": [{"snippet": "alpha", "reference": reference}]})
    assert result["validation_passed"], result["errors"]
    item = result["records"][0]["assertions"][0]
    assert (
        item["normalized_expected_reference"] == item["normalized_validated_reference"] == "PMID:1"
    )
    assert item["cache"]["loaded_reference_id"] == "PMID:1"


def test_zero_comparison_cannot_pass_even_if_native_returns_success(fixture_repo):
    result, log = invoke(
        fixture_repo, {"evidence": [{"snippet": "ignored", "reference": "BIOPROJECT:PRJ1"}]}
    )
    assert "Total checks: 0" in log
    assert result["native_validation_passed"]
    assert not result["measurement_valid"]
    assert not result["validation_passed"]
    assert "Zero snippet occurrences actually compared" in result["errors"]


def test_legitimate_empty_record_is_typed_and_not_compared(fixture_repo):
    documents = [
        ("empty", {}),
        ("good", {"evidence": [{"snippet": "alpha", "reference": "PMID:1"}]}),
    ]
    paths = []
    for name, document in documents:
        path = fixture_repo / f"{name}.json"
        path.write_text(json.dumps(document))
        paths.append(path)
    result, _ = coverage.measure(fixture_repo, documents, paths)
    assert result["measurement_valid"], result["errors"]
    assert result["counts"]["records_completed"] == 2
    assert result["records"][0]["record_kind"] == "no_snippet_surfaces"
    assert result["counts"]["snippet_occurrences_compared"] == 1


@pytest.mark.parametrize(
    "operation", ["write", "mkdir", "network", "process", "save", "enrich", "source"]
)
def test_acquisition_and_writes_are_refused(tmp_path, operation):
    violations = []
    with coverage.no_side_effects(violations), pytest.raises(RuntimeError, match="attempted"):
        if operation == "write":
            (tmp_path / "forbidden").write_text("bad")
        elif operation == "mkdir":
            (tmp_path / "forbidden").mkdir()
        elif operation == "network":
            socket.create_connection(("example.org", 443))
        elif operation == "process":
            subprocess.run(["true"], check=True)
        elif operation == "save":
            coverage.ReferenceFetcher._save_to_disk(None, None)
        elif operation == "enrich":
            coverage.ReferenceFetcher._enrich_with_full_text(None, None)
        else:
            from linkml_reference_validator.etl.sources import ReferenceSourceRegistry

            ReferenceSourceRegistry.get_source("PMID:1")
    assert violations
    assert not (tmp_path / "forbidden").exists()


def test_broken_traversal_does_not_report_coverage(fixture_repo):
    with patch.object(
        coverage.ReferenceValidationPlugin, "_validate_instance", return_value=iter(())
    ):
        result, _ = invoke(
            fixture_repo, {"evidence": [{"snippet": "alpha", "reference": "PMID:1"}]}
        )
    assert not result["measurement_valid"]
    assert not result["assertion_coverage_complete"]


def test_inconsistent_actual_validator_calls_fail_closed(fixture_repo):
    native = coverage.SupportingTextValidator.validate

    def duplicate(validator, *args, **kwargs):
        native(validator, *args, **kwargs)
        return native(validator, *args, **kwargs)

    with patch.object(coverage.SupportingTextValidator, "validate", duplicate):
        result, _ = invoke(
            fixture_repo, {"evidence": [{"snippet": "alpha", "reference": "PMID:1"}]}
        )
    assert not result["measurement_valid"]
    assert any("Inconsistent matcher accounting" in error for error in result["errors"])


def test_git_inventory_rejects_modified_and_extra_records(tmp_path):
    for name in ["kb/communities/one.yaml", "data/isolates/two.yaml"]:
        path = tmp_path / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("name: original\n")
    subprocess.run(["git", "init", "-q", str(tmp_path)], check=True)
    subprocess.run(["git", "-C", str(tmp_path), "add", "."], check=True)
    subprocess.run(
        [
            "git",
            "-C",
            str(tmp_path),
            "-c",
            "user.name=Fixture",
            "-c",
            "user.email=fixture@example.invalid",
            "commit",
            "-qm",
            "fixture",
        ],
        check=True,
    )
    _, records = coverage.declared_records(tmp_path)
    assert len(records) == 2
    path.write_text("name: modified\n")
    with pytest.raises(ValueError, match="exact declared Git"):
        coverage.declared_records(tmp_path)
    path.write_text("name: original\n")
    (tmp_path / "kb/communities/extra.yaml").write_text("name: extra\n")
    with pytest.raises(ValueError, match="globs disagree"):
        coverage.declared_records(tmp_path)


def test_output_refuses_non_temp_and_existing_directory(tmp_path, monkeypatch):
    monkeypatch.setattr(coverage, "declared_records", lambda root: ("revision", ["one"]))
    with pytest.raises(ValueError, match="beneath this checkout"):
        coverage.run(tmp_path, tmp_path / "reports/new", ["one"])
    output = tmp_path / ".temp/existing"
    output.mkdir(parents=True)
    monkeypatch.setattr(coverage, "input_manifest", lambda root, records: {})
    with pytest.raises(FileExistsError):
        coverage.run(tmp_path, output, ["one"])


def test_record_inventory_uses_native_yaml_scalar_semantics(fixture_repo, monkeypatch):
    """#2799: YAML1.1 sexagesimal coercion must not abort native YAML1.2 dispatch."""
    path = fixture_repo / "record.yaml"
    path.write_text("ratio: 1:1:1\nevidence:\n- snippet: alpha\n  reference: PMID:1\n")
    monkeypatch.setattr(coverage, "declared_records", lambda root: ("revision", ["record.yaml"]))
    monkeypatch.setattr(coverage, "input_manifest", lambda root, records: {})
    result = coverage.run(fixture_repo, fixture_repo / ".temp/native-parser", ["record.yaml"])
    assert result["exit_code"] == 0, result["cases"][0]["errors"]
    assert result["cases"][0]["counts"]["snippet_occurrences_compared"] == 1


@pytest.fixture
def selected_source(fixture_repo):
    """Real DOCX extraction, catalog and native matcher; no provider substitutes."""
    from linkml_reference_validator.etl.source_locator import extract_docx_tables

    root = fixture_repo
    schema_path = root / coverage.SCHEMA
    schema = yaml.safe_load(schema_path.read_text())
    schema["classes"]["EvidenceItem"]["attributes"]["source_locator"] = {
        "range": "SourceLocator",
        "inlined": True,
    }
    schema["classes"]["SourceLocator"] = {
        "attributes": {
            key: {"range": "integer" if key in {"table", "row", "cell"} else "string"}
            for key in ("kind", "asset_id", "version", "table", "row", "cell")
        }
    }
    schema_path.write_text(yaml.safe_dump(schema))
    folder = root / ".temp/sources"
    folder.mkdir(parents=True)
    buffer = BytesIO()
    with ZipFile(buffer, "w") as archive:
        archive.writestr(
            "word/document.xml",
            (
                '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
                "<w:body><w:tbl><w:tr>"
                + "".join(
                    f"<w:tc><w:p><w:r><w:t>{text}</w:t></w:r></w:p></w:tc>"
                    for text in ("alpha", "gamma", "alpha")
                )
                + "</w:tr></w:tbl></w:body></w:document>"
            ),
        )
    asset = buffer.getvalue()
    projection = json.dumps(extract_docx_tables(asset)).encode()
    (folder / "table.docx").write_bytes(asset)
    (folder / "cells.json").write_bytes(projection)
    catalog = {
        "version": 1,
        "sources": [
            {
                "reference": "PMID:1",
                "asset_id": "table.docx",
                "version": "published",
                "asset_path": "table.docx",
                "asset_sha256": coverage.digest(asset),
                "extraction_path": "cells.json",
                "extraction_sha256": coverage.digest(projection),
            }
        ],
    }
    (folder / "catalog.json").write_text(json.dumps(catalog))
    config = yaml.safe_load((root / coverage.CONFIG).read_text())
    config["source_catalog"] = str(folder / "catalog.json")
    (root / coverage.CONFIG).write_text(yaml.safe_dump(config))
    locator = {
        "kind": "supplement",
        "asset_id": "table.docx",
        "version": "published",
        "table": 1,
        "row": 1,
        "cell": 1,
    }
    return root, {
        "evidence": [
            {"snippet": "beta", "reference": "PMID:1"},
            {"snippet": "alpha", "reference": "PMID:1", "source_locator": locator},
        ]
    }


def test_selected_sources_keep_native_comparisons_and_failure_boundaries(selected_source):
    root, good = selected_source
    before = {p: p.read_bytes() for p in (root / ".temp/sources").iterdir()}
    cases = [deepcopy(good) for _ in range(5)]
    cases[1]["evidence"][1]["source_locator"]["cell"] = 2
    cases[2]["evidence"][1]["reference"] = "PMID:4"
    cases[3]["evidence"][1]["source_locator"] = None
    results = [invoke(root, doc, f"selected-{i}")[0] for i, doc in enumerate(cases)]
    assert all(r["measurement_valid"] for r in results), results
    assert [r["native_exit_code"] for r in results] == [0, 1, 1, 1, 0]
    assert [r["counts"]["snippet_occurrences_compared"] for r in results] == [2, 2, 1, 1, 2]
    assert [r["validation_passed"] for r in results] == [True, False, False, False, True]
    selected = [r["records"][0]["assertions"][1] for r in results]
    assert [a["status"] for a in selected] == [
        "matched",
        "mismatched",
        "source_selection_failed",
        "source_selection_failed",
        "matched",
    ]
    assert selected[0]["source_identity"]["locator"] == good["evidence"][1]["source_locator"]
    assert selected[0]["source_identity"] == selected[4]["source_identity"]
    assert all("cache" not in a for a in selected)  # No article fallback, even for alpha.
    assert before == {p: p.read_bytes() for p in (root / ".temp/sources").iterdir()}


def test_wrong_locator_with_identical_text_invalidates_coverage_then_restores(selected_source):
    root, good = selected_source
    original = coverage.ReferenceValidationPlugin._validate_excerpt

    def misroute(plugin, text, reference, title, path, *, source_locator=coverage.ABSENT):
        if source_locator is not coverage.ABSENT:
            source_locator = {**source_locator, "cell": 3}
        yield from original(plugin, text, reference, title, path, source_locator=source_locator)

    control, _ = invoke(root, good, "before")
    with patch.object(coverage.ReferenceValidationPlugin, "_validate_excerpt", misroute):
        mutated, _ = invoke(root, good, "misroute")
    restored, _ = invoke(root, good, "restored")
    assert control["validation_passed"] and restored["validation_passed"]
    assert mutated["native_validation_passed"]  # Same text in a different cell.
    assert not mutated["measurement_valid"] and not mutated["assertion_coverage_complete"]
    assert mutated["counts"]["snippet_occurrences_compared"] == 1
    assert any("Source locator identity mismatch" in e for e in mutated["errors"])


def test_manifest_binds_ignored_catalog_asset_and_projection(selected_source):
    root, _ = selected_source
    for name in ("uv.lock", "pyproject.toml"):
        (root / name).write_text("fixture\n")
    before = coverage.input_manifest(root, [])
    names = {f".temp/sources/{name}" for name in ("catalog.json", "table.docx", "cells.json")}
    assert names.issubset(before)
    asset = root / ".temp/sources/table.docx"
    original = asset.read_bytes()
    asset.write_bytes(original + b"changed")
    assert coverage.input_manifest(root, []) != before
    asset.write_bytes(original)
    assert coverage.input_manifest(root, []) == before
