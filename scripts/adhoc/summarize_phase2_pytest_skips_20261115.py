#!/usr/bin/env python3
"""Account for code005 native skips without rerunning tests (2026-11-15).

Inputs: completed immutable receipt/log/exit and exact recorded Git source.
Output: one exclusive JSON ledger, with native identifiers and source guard sites.
Serves Phase2 QC accounting and #2840/#2842; no provider or canonical writes.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
import re
import subprocess
from collections import Counter
from pathlib import Path

import tomllib

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / ".temp/m5-completion-20261114"
NAME = "phase2-code005-qc-references"
REVISION = "63b833d3f1752efbb5010f9ae1f5e6e3e1813962"
MODULE_CATEGORIES = {
    "test_cache_names_are_normalised_after_fetching": "case_insensitive_filesystem",
    "test_every_ontology_id_resolves": "no_prefix_ids_or_unavailable_adapter",
    "test_generated_gate_inputs_are_built_in_ci": "drift_report_not_generated",
    "test_justfile_triggers_the_gates_it_defines": "workflow_applicability_guard",
    "test_llm_client": "optional_anthropic_sdk_guard",
    "test_ncbitaxon_adapter_is_shared": "inconclusive_outage_negative_control",
    "test_scripts_import": "optional_import_guard",
}
CLI_MODULES = {
    "test_gtdb_candidate_curies",
    "test_gtdb_near_tie_marker",
    "test_gtdb_non_type_clade_flag",
}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def git_source(path):
    return subprocess.check_output(["git", "show", f"{REVISION}:{path}"], cwd=ROOT)


def source_guards(path):
    raw = git_source(path)
    source = raw.decode()
    guards = []
    for node in ast.walk(ast.parse(source)):
        if (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Attribute)
            and node.func.attr in {"skip", "skipif"}
            and ast.unparse(node.func).startswith("pytest.")
        ):
            guards.append({"line": node.lineno, "expression": ast.unparse(node)})
    if not guards:
        raise ValueError(f"No associated source skip guard found: {path}")
    return {"sha256": sha(raw), "guards": sorted(guards, key=lambda row: row["line"])}


def category(module, test):
    stem = Path(module).stem
    if stem.startswith("test_gtdb_"):
        if test.startswith(
            "test_the_curated_term_bears_the_clade_name_and_the_broad_one_does_not["
        ):
            return "explicitly_renamed_gtdb_clade"
        return "gtdb_cli_answer_guard" if stem in CLI_MODULES else "gtdb_mapping_fixture_guard"
    if stem not in MODULE_CATEGORIES:
        raise ValueError(f"Unclassified native skip: {module}::{test}")
    return MODULE_CATEGORIES[stem]


def build():
    paths = {suffix: STATE / f"{NAME}.{suffix}" for suffix in ("json", "log", "exit")}
    raw = {suffix: path.read_bytes() for suffix, path in paths.items()}
    receipt = json.loads(raw["json"])
    if (
        receipt.get("name") != NAME
        or receipt.get("head") != REVISION
        or receipt.get("status") != "FAILED"
        or not receipt.get("finished_at")
        or receipt.get("exit_code") != 1
        or raw["exit"].strip() != b"1"
        or receipt.get("log_bytes") != len(raw["log"])
        or receipt.get("log_sha256") != sha(raw["log"])
        or receipt.get("log") != str(paths["log"].relative_to(ROOT))
    ):
        raise ValueError("Native completion, revision or raw triplet does not reconcile")
    log = raw["log"].decode()
    summaries = re.findall(r"^=+ (.+?) in ([\d.]+)s(?: .*)? =+$", log, re.M)
    if len(summaries) != 1:
        raise ValueError("Expected exactly one native pytest summary")
    counts = {
        key: int(value)
        for value, key in re.findall(
            r"\b(\d+) (failed|passed|skipped|deselected|warnings)\b", summaries[0][0]
        )
    }
    collected = re.findall(r"collected (\d+) items / (\d+) deselected / (\d+) selected", log)
    if len(collected) != 1:
        raise ValueError("Expected one native collection census")
    total, deselected, selected = map(int, collected[0])
    if (
        total != selected + deselected
        or deselected != counts["deselected"]
        or selected != sum(counts[key] for key in ("passed", "failed", "skipped"))
    ):
        raise ValueError("Native collection and final counts disagree")
    pattern = r"^(tests/[^:]+\.py)::(.+?)\s+SKIPPED(?:\s+\((.*?)\))?\s+\[\s*\d+%\]$"
    rows = [
        {
            "identifier": f"{module}::{test}",
            "module": module,
            "category": category(module, test),
            "native_reason_fragment": reason or None,
        }
        for module, test, reason in re.findall(pattern, log, re.M)
    ]
    if len(rows) != counts["skipped"] or len({row["identifier"] for row in rows}) != len(rows):
        raise ValueError("Skipped identifiers are missing, duplicated or unreconciled")
    sources = {path: source_guards(path) for path in sorted({row["module"] for row in rows})}
    config = git_source("pyproject.toml")
    addopts = tomllib.loads(config.decode())["tool"]["pytest"]["ini_options"]["addopts"]
    if addopts != "-m 'not e2e'":
        raise ValueError("Native deselection policy changed")
    return {
        "run": NAME,
        "source_revision": REVISION,
        "finished_at": receipt["finished_at"],
        "native_exit_code": receipt["exit_code"],
        "native_stages": receipt["stages"],
        "native_recipe_skip_markers": receipt["skip_markers"],
        "raw_inputs": {
            suffix: {"path": str(path.relative_to(ROOT)), "sha256": sha(raw[suffix])}
            for suffix, path in paths.items()
        },
        "helper_sha256": sha(Path(__file__).read_bytes()),
        "pytest_counts": counts,
        "collected": total,
        "selected": selected,
        "duration_seconds": float(summaries[0][1]),
        "category_counts": dict(sorted(Counter(row["category"] for row in rows).items())),
        "skipped_identifiers": rows,
        "associated_source_guards": sources,
        "deselection": {"addopts": addopts, "config_sha256": sha(config), "count": deselected},
        "limits": [
            "No tests, validators or providers were rerun to produce this ledger.",
            "Categories describe associated pinned source guards, not independently observed runtime causes.",
            "The native verbose log generally omits full skip reasons; printed fragments may be truncated.",
            "CLI answer guards can also hide changed answers; their category does not prove global source absence.",
            "CL/PATO source guards permit either no cited identifiers or an unavailable adapter; this ledger does not choose a branch.",
            "Pytest skips and e2e deselections are distinct from required recipe skips and the eleven later NOT RUN recipe entries.",
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    output = args.output.resolve()
    allowed = [ROOT / "reports/phase2-completion-20261115", ROOT / ".temp"]
    if not any(
        output.is_relative_to(path.resolve()) and output != path.resolve() for path in allowed
    ):
        parser.error("Output must be exclusive within this checkout's report or private directory")
    result = build()
    with output.open("x") as handle:
        json.dump(result, handle, indent=2)
        handle.write("\n")
    print(
        json.dumps(
            {"pytest_counts": result["pytest_counts"], "categories": result["category_counts"]}
        )
    )


if __name__ == "__main__":
    main()
