"""Identity intermediate proof mutations preserve old biology and native scope."""

import copy
import importlib.util
import json
import subprocess
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture
def proof(monkeypatch):
    monkeypatch.syspath_prepend(str(ROOT / "scripts/adhoc"))
    spec = importlib.util.spec_from_file_location(
        "identity_diagnostic", ROOT / "scripts/adhoc/build_wetland_identity_diagnostic_20261115.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    original = subprocess.check_output(
        ["git", "show", "0126f074d97eb795e68bbe27bc15f21468c31634:" + module.identity.TARGET],
        cwd=ROOT,
    )
    plan = json.loads(
        (ROOT / "reports/gtdb-wetland-identity-20261115/471-identity-plan-001.json").read_bytes()
    )
    current, _, event = module.identity.render_candidate(original, plan, "2026-11-15T13:06:51Z")
    assert module.identity.sha(current) == module.AFTER
    common = {
        "target": module.identity.TARGET,
        "target_id": module.identity.TARGET_ID,
        "execution_revision": module.REVISION,
        "before_sha256": module.identity.BEFORE,
        "scope": module.identity.SCOPE,
        "scientific_review": False,
        "source_plan": {"pinned": True},
        "inputs": plan["inputs"],
        "appended_native_inline_history": event,
    }
    applied = dict(common, applied=True, after_sha256=module.AFTER)
    staged = dict(
        common, canonical_apply=False, source_inputs_unchanged=True, candidate_sha256=module.AFTER
    )
    return module, original, current, applied, staged, plan


def test_exact_actual_identity_transition(proof):
    module, *args = proof
    module.verify_chain(*args)


@pytest.mark.parametrize(
    "kind", ["graph", "taxon", "old_history", "snippet", "scope", "stage_inputs", "event"]
)
def test_chain_mutation_refuses_then_restores(proof, kind):
    module, original, current, applied, staged, plan = proof
    args = copy.deepcopy([original, current, applied, staged, plan])
    if kind in {"graph", "taxon", "old_history", "snippet"}:
        doc = yaml.safe_load(args[1])
        if kind == "graph":
            doc["ecological_interactions"][0]["downstream"][0][
                "description"
            ] += " Mechanism proven."
        elif kind == "taxon":
            doc["taxonomy"][0]["taxon_term"]["term"]["label"] = "different taxon"
        elif kind == "old_history":
            doc["curation_history"][0]["changes"] += " altered"
        else:
            doc["taxonomy"][0]["evidence"][0]["snippet"] += " fabricated"
        args[1] = yaml.safe_dump(doc).encode()
    elif kind == "scope":
        args[2]["scope"] = "taxonomy-notes-only"
    elif kind == "stage_inputs":
        args[3]["inputs"] = {"different": "0" * 64}
    else:
        args[3]["appended_native_inline_history"]["timestamp"] = "2026-11-15T00:00:00Z"
    with pytest.raises(ValueError, match="identity"):
        module.verify_chain(*args)
    module.verify_chain(original, current, applied, staged, plan)


@pytest.mark.parametrize("mutation", ["plan", "exit", "log", "command", "after", "input_changed"])
def test_gate_mutation_refuses_then_restores(proof, mutation):
    module = proof[0]
    config = {"application_receipt": ".temp/applied.json", "application_receipt_sha256": "a" * 64}
    log = b"actual native output\n"
    receipt = {
        "revision": module.REVISION,
        "plan": False,
        "exit_code": 0,
        "finished_at": "2026-11-15T13:13:00Z",
        "log_sha256": module.identity.sha(log),
        "log_bytes": len(log),
        "execution_inputs_unchanged": True,
        "inputs": {
            str(ROOT / module.identity.TARGET): module.AFTER,
            str(ROOT / ".temp/applied.json"): "a" * 64,
            str(ROOT / "config.json"): "c" * 64,
        },
        "command": [
            "just",
            "--verbose",
            "--no-dotenv",
            "--color",
            "never",
            "validate",
            module.identity.TARGET,
        ],
        "new_history_sidecars": {},
    }
    args = (log, b"0\n", "schema", ".temp/schema", config, "c" * 64)
    module.verify_gate(receipt, *args)
    altered = copy.deepcopy(receipt)
    if mutation == "plan":
        altered["plan"] = True
    elif mutation == "exit":
        altered["exit_code"] = 1
    elif mutation == "log":
        altered["log_sha256"] = "0" * 64
    elif mutation == "command":
        altered["command"][-1] = "other.yaml"
    elif mutation == "after":
        altered["inputs"][str(ROOT / module.identity.TARGET)] = "0" * 64
    else:
        altered["execution_inputs_unchanged"] = False
    with pytest.raises(ValueError):
        module.verify_gate(altered, *args)
    module.verify_gate(receipt, *args)


def reference_case(module):
    case = json.loads(
        (ROOT / "tests/data/wetland_identity_reference_measurement_20261115.json").read_bytes()
    )
    reference_log = (ROOT / "tests/data/wetland_identity_references_20261115.log.txt").read_bytes()
    assert module.identity.sha(reference_log) == case["references"]["log_sha256"]
    return case, reference_log


def verify_reference_case(module, current, case, reference_log):
    # Rehash dependent artifacts so negative cases exercise semantic guards.
    result_raw = (json.dumps(case["measurement"], indent=2) + "\n").encode()
    case["receipt"]["measurement_sha256"] = module.identity.sha(result_raw)
    outer_log = (json.dumps(case["receipt"], indent=2) + "\n").encode()
    case["shell"].update(log_sha256=module.identity.sha(outer_log), log_bytes=len(outer_log))
    commands = {
        "references": (case["references"], reference_log),
        "reference-measurement": (case["shell"], outer_log),
    }
    module.verify_references(
        current, case["directory"], case["started"], case["receipt"], case["measurement"], commands
    )


def test_actual_retained_measurement_projection(proof):
    module, _, current, *_ = proof
    case, log = reference_case(module)
    assert case["measurement"]["counts"]["snippet_occurrences_compared"] == 16
    verify_reference_case(module, current, case, log)


@pytest.mark.parametrize(
    "mutation",
    [
        "target",
        "coverage",
        "exit",
        "start",
        "command",
        "output",
        "population",
        "snippet",
        "outer_exit",
        "references_exit",
    ],
)
def test_rehashed_measurement_mutation_refuses_then_restores(proof, mutation):
    module, _, current, *_ = proof
    case, log = reference_case(module)
    altered = copy.deepcopy(case)
    if mutation == "target":
        altered["receipt"]["target"] = altered["started"]["target"] = "kb/communities/other.yaml"
        altered["measurement"]["records"][0]["record"] = "kb/communities/other.yaml"
    elif mutation == "coverage":
        altered["measurement"]["assertion_coverage_complete"] = False
    elif mutation == "exit":
        altered["measurement"]["native_exit_code"] = 1
        altered["measurement"]["validation_passed"] = False
        altered["measurement"]["native_validation_passed"] = False
        altered["receipt"]["exit_code"] = 1
    elif mutation == "start":
        altered["started"]["after_sha256"] = "0" * 64
    elif mutation == "command":
        altered["references"]["command"][-1] = "other.yaml"
    elif mutation == "output":
        altered["shell"]["command"][-1] = ".temp/different-measurement"
    elif mutation == "population":
        altered["measurement"]["records"] *= 2
    elif mutation == "snippet":
        altered["measurement"]["records"][0]["assertions"][0]["text_sha256"] = "0" * 64
    elif mutation == "outer_exit":
        altered["shell"]["exit_code"] = 1
    else:
        altered["references"]["exit_code"] = 1
    with pytest.raises(ValueError):
        verify_reference_case(module, current, altered, log)
    verify_reference_case(module, current, case, log)


@pytest.fixture
def runtime_inventory(proof, tmp_path, monkeypatch):
    module = proof[0]
    monkeypatch.setattr(module, "ROOT", tmp_path)
    monkeypatch.setattr(module.identity.capture_core, "ROOT", tmp_path)
    paths = {
        module.identity.TARGET: proof[2],
        module.identity.SOURCE: b"retained primary source\n",
        "references_cache/doi_DOI:10.1007_BF02106205.json": b"unrelated runtime cache\n",
        module.measured.native.CONFIG: b"skip_prefixes: []\n",
        "uv.lock": b"lock\n",
        "pyproject.toml": b"project\n",
        "src/communitymech/schema/communitymech.yaml": b"schema\n",
    }
    for name, raw in paths.items():
        path = tmp_path / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(raw)
    source_sha = module.identity.sha(paths[module.identity.SOURCE])
    monkeypatch.setattr(module.identity, "SOURCE_SHA", source_sha)
    receipt = {
        "input_sha256": module.measured.native.input_manifest(tmp_path, [module.identity.TARGET])
    }
    result = {
        "records": [
            {
                "assertions": [
                    {
                        "cache": {
                            "loaded": True,
                            "requested_path": module.identity.SOURCE,
                            "sha256": source_sha,
                        }
                    }
                    for _ in range(16)
                ]
            }
        ]
    }
    return module, tmp_path, paths, receipt, result


def test_unused_unsafe_cache_is_runtime_context_not_archived_input(runtime_inventory):
    module, root, paths, receipt, result = runtime_inventory
    captured = {}
    module.capture_measurement_inputs(captured, receipt, result)
    unrelated = root / "references_cache/doi_DOI:10.1007_BF02106205.json"
    assert str(unrelated.relative_to(root)) in receipt["input_sha256"]
    assert unrelated not in captured
    assert root / module.identity.SOURCE in captured
    assert len(captured) == len(paths) - 1
    module.verify_runtime_inventory(receipt)


@pytest.mark.parametrize("mutation", ["loaded", "cache", "hash", "missing_source"])
def test_loaded_cache_cannot_be_excluded_then_restores(runtime_inventory, mutation):
    module, _, _, receipt, result = runtime_inventory
    changed_receipt, changed_result = copy.deepcopy((receipt, result))
    cache = changed_result["records"][0]["assertions"][0]["cache"]
    if mutation == "loaded":
        cache["loaded"] = False
    elif mutation == "cache":
        cache["requested_path"] = "references_cache/doi_DOI:10.1007_BF02106205.json"
    elif mutation == "hash":
        cache["sha256"] = "0" * 64
    else:
        del changed_receipt["input_sha256"][module.identity.SOURCE]
    with pytest.raises(ValueError, match="exact loaded primary cache"):
        module.capture_measurement_inputs({}, changed_receipt, changed_result)
    module.capture_measurement_inputs({}, receipt, result)


@pytest.mark.parametrize("mutation", ["source", "unused", "schema", "added", "removed"])
def test_complete_runtime_namespace_mutation_refuses_then_restores(runtime_inventory, mutation):
    module, root, paths, receipt, result = runtime_inventory
    module.capture_measurement_inputs({}, receipt, result)
    names = {
        "source": module.identity.SOURCE,
        "unused": "references_cache/doi_DOI:10.1007_BF02106205.json",
        "schema": "src/communitymech/schema/communitymech.yaml",
        "added": "references_cache/new-unrelated-cache.txt",
        "removed": "references_cache/doi_DOI:10.1007_BF02106205.json",
    }
    name = names[mutation]
    path = root / name
    if mutation == "removed":
        path.unlink()
    else:
        path.write_bytes(b"changed input\n")
    with pytest.raises(ValueError, match="complete measurement runtime inventory changed"):
        module.verify_runtime_inventory(receipt)
    if mutation == "added":
        path.unlink()
    else:
        path.write_bytes(paths[name])
    module.verify_runtime_inventory(receipt)
    module.capture_measurement_inputs({}, receipt, result)
