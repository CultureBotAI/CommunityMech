#!/usr/bin/env python3
"""Current native CLI controls after the SupportingReference annotation repair.

Inputs: three real records and their unchanged committed cache/schema/config.
Outputs: exclusive private fixture copies, native logs and a hash-bound receipt.
Issue: #476. Date: 2026-11-15. Historical reports/probe.py stays immutable.
This reuses the maintained comparison tracer; issue counts are not coverage.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import subprocess
from copy import deepcopy
from datetime import datetime, timezone
from hashlib import sha256
from importlib.metadata import version
from pathlib import Path

from ruamel.yaml import YAML

ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location(
    "reference_assertion_coverage", ROOT / "scripts/reference_assertion_coverage.py"
)
coverage = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(coverage)
RECORDS = {
    "Phormidium_Alkaline_Consortium": "doi_10.3389_fmicb.2022.780346.md",
    "Alseth_FourSpecies_Pathogen_Phage_Community": "PMID_38648198.txt",
    "PHA_MixedCulture_Phage_Succession_Community": "PMID_40152616.txt",
}
SENTINEL = "ZZQQ_UNSUPPORTED_REFERENCE_CLI_COVERAGE_CANARY_XYZ"


def fingerprint(paths):
    return {str(p.relative_to(ROOT)): sha256(p.read_bytes()).hexdigest() for p in paths}


def run_probe(stem, output):
    """Run one record end to end; only the explicitly new .temp output is writable."""
    if version("linkml-reference-validator") != coverage.SUPPORTED_VERSION:
        raise ValueError("The maintained tracer requires reviewed validator 0.2.1")
    output = Path(output).resolve()
    private = (ROOT / ".temp").resolve()
    if output == private or not output.is_relative_to(private):
        raise ValueError("Output must be a new directory within this checkout's .temp")
    record = f"kb/communities/{stem}.yaml"
    cache = ROOT / "references_cache" / RECORDS[stem]
    schema_paths = sorted((ROOT / "src/communitymech/schema").glob("*.yaml"))
    paths = sorted(
        {
            ROOT / record,
            cache,
            *schema_paths,
            ROOT / coverage.CONFIG,
            ROOT / "uv.lock",
            ROOT / "pyproject.toml",
            ROOT / "scripts/reference_assertion_coverage.py",
            Path(__file__),
        }
    )
    before = fingerprint(paths)
    original = YAML(typ="safe").load((ROOT / record).read_text())
    surfaces = list(coverage.snippet_surfaces(original))
    discussion_paths = [p for p, *_ in surfaces if p.startswith("discussions[")]
    output.mkdir(parents=True, exist_ok=False)
    receipt = {
        "started_at": datetime.now(timezone.utc).isoformat(),
        "revision": subprocess.check_output(
            ["git", "-C", str(ROOT), "rev-parse", "HEAD"], text=True
        ).strip(),
        "record": record,
        "input_sha256": before,
        "dependencies": {p: version(p) for p in ("linkml", "linkml-reference-validator")},
        "discussion_fields": discussion_paths,
        "policy": "Copied input bytes; native traversal/matcher; no acquisition or source writes",
        "limit": "Lexical comparison coverage is not a scientific support verdict",
        "cases": [],
    }
    coverage.write_json(output / "started.json", receipt)
    fixture = output / "fixture"
    for source in [*schema_paths, ROOT / coverage.CONFIG]:
        target = fixture / source.relative_to(ROOT)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(source.read_bytes())
    # Native DOI casing in the isolated fixture only, as in the historical probe.
    target_cache = fixture / "references_cache" / cache.name.replace("doi_", "DOI_", 1)
    target_cache.parent.mkdir(parents=True)
    target_cache.write_bytes(cache.read_bytes())
    copied_inputs = sorted(p for p in fixture.rglob("*") if p.is_file())
    fixture_before = {p: sha256(p.read_bytes()).hexdigest() for p in copied_inputs}
    cases = ["control", "evidence_mutation", "restoration"]
    if discussion_paths:
        cases += ["discussion_mutation", "discussion_restoration"]
    for case in cases:
        document = deepcopy(original)
        mutation_path = None
        if case == "evidence_mutation":
            mutation_path = "ecological_interactions[0].evidence[0].snippet"
        elif case == "discussion_mutation":
            mutation_path = discussion_paths[0]
        if mutation_path:
            for path, _, _, field, owner in coverage.snippet_surfaces(document):
                if path == mutation_path:
                    owner[field] = SENTINEL
                    break
            else:
                raise ValueError(f"Mutation target is absent: {mutation_path}")
        target = output / f"{case}.json"
        coverage.write_json(target, document)  # JSON uses native YAML 1.2 scalar semantics.
        measured, log = coverage.measure(fixture, [(record, document)], [target])
        log = log.replace(str(output), "<probe-output>")
        (output / f"{case}.log").write_text(log)
        # Avoid publishing machine-specific paths in the reproducible metadata.
        measured["invocation"]["argv"] = [
            p.replace(str(output), "<probe-output>") for p in measured["invocation"]["argv"]
        ]
        expected = 1 if mutation_path else 0
        assertions = measured["records"][0]["assertions"] if measured["records"] else []
        mismatches = [a["path"] for a in assertions if a["status"] == "mismatched"]
        passed = (
            measured["measurement_valid"]
            and measured["assertion_coverage_complete"]
            and measured["native_exit_code"] == expected
            and measured["counts"]["native_issues"] == expected
            and mismatches == ([mutation_path] if mutation_path else [])
            and f"Total checks: {expected}" in log
            and (not mutation_path or f"Location: {mutation_path}" in log)
        )
        receipt["cases"].append(
            {"case": case, "expected_issues": expected, "control_passed": passed, **measured}
        )
    receipt["inputs_unchanged"] = fingerprint(paths) == before
    receipt["fixture_inputs_unchanged"] = fixture_before == {
        p: sha256(p.read_bytes()).hexdigest() for p in copied_inputs
    }
    receipt["controls_passed"] = (
        all(case["control_passed"] for case in receipt["cases"])
        and receipt["inputs_unchanged"]
        and receipt["fixture_inputs_unchanged"]
    )
    receipt["finished_at"] = datetime.now(timezone.utc).isoformat()
    coverage.write_json(output / "receipt.json", receipt)
    return receipt


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--record", choices=RECORDS, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    receipt = run_probe(args.record, args.output)
    print(json.dumps({"controls_passed": receipt["controls_passed"], "record": receipt["record"]}))
    return 0 if receipt["controls_passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
