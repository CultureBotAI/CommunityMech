"""Measure exact working Wetland471 references; #2898/#476, 2026-11-15.

Inputs: fixed applied record, source/cache/schema/code bytes at frozen af80.
Outputs: exclusive private native measurement/log/receipt. Reuses the unchanged
collector/matcher; does not relax the maintained corpus Git-inventory contract.
"""

import argparse
import importlib.util
import inspect
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location(
    "wetland_reference_measurement", ROOT / "scripts/reference_assertion_coverage.py"
)
native = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(native)
TARGET = "kb/communities/Wetland_Lindane_Degrading_Organochlorine_Consortium.yaml"
AFTER = "b3234d5f041636195f4c9867aaccd0df802d22ff5f2fbc28b904868ee02b901a"
REVISION = "af80bc0970b2b495b16c2c5c237cdfbbaa771ce8"


def run(output_name, *, plan=False):
    output = (ROOT / output_name).resolve()
    if (
        not output.is_relative_to(ROOT / ".temp")
        or output == ROOT / ".temp"
        or output.exists()
        or native.git(ROOT, "rev-parse", "HEAD") != REVISION
        or native.version("linkml-reference-validator") != native.SUPPORTED_VERSION
    ):
        raise ValueError("exclusive private output and exact frozen native environment required")
    manifest = native.input_manifest(ROOT, [TARGET])
    if manifest[TARGET] != AFTER:
        raise ValueError("fixed approved working AFTER required")
    implementations = {
        Path(__file__),
        ROOT / "scripts/reference_assertion_coverage.py",
        *(
            Path(inspect.getfile(obj))
            for obj in (
                native.ReferenceFetcher,
                native.ReferenceValidationPlugin,
                native.SupportingTextValidator,
                native.Validator,
            )
        ),
    }
    captured = {path: path.read_bytes() for path in implementations}
    target_bytes = (ROOT / TARGET).read_bytes()
    if native.digest(target_bytes) != AFTER:
        raise ValueError("captured target differs from approved working AFTER")
    document = native.YAML(typ="safe").load(target_bytes)

    def unchanged():
        if (
            native.git(ROOT, "rev-parse", "HEAD") != REVISION
            or native.input_manifest(ROOT, [TARGET]) != manifest
            or any(path.read_bytes() != raw for path, raw in captured.items())
        ):
            raise ValueError("working source/cache/schema/implementation changed")

    unchanged()
    receipt = {
        "revision": REVISION,
        "source_state": "Frozen working tree with applied AFTER; target differs from HEAD.",
        "target": TARGET,
        "after_sha256": AFTER,
        "input_sha256": manifest,
        "implementation_sha256": {str(p): native.digest(raw) for p, raw in captured.items()},
        "python": sys.version,
        "python_executable": sys.executable,
        "plan": plan,
        "interpretation": "One-record lexical comparisons only; no scientific approval or corpus QC.",
    }
    if plan:
        return receipt
    output.mkdir(parents=True)
    receipt["started_at"] = datetime.now(timezone.utc).isoformat()
    native.write_json(output / "started.json", receipt)
    result, log = native.measure(ROOT, [(TARGET, document)], [ROOT / TARGET])
    unchanged()
    if not log:
        raise ValueError("native log must be nonempty")
    native.write_json(output / "measurement.json", result)
    with (output / "measurement.log").open("x") as stream:
        stream.write(log)
    code = 2 if not result["measurement_valid"] else (0 if result["validation_passed"] else 1)
    receipt.update(
        finished_at=datetime.now(timezone.utc).isoformat(),
        inputs_unchanged=True,
        measurement_sha256=native.digest((output / "measurement.json").read_bytes()),
        log_sha256=native.digest(log.encode()),
        exit_code=code,
        counts=result["counts"],
    )
    unchanged()
    native.write_json(output / "receipt.json", receipt)
    return receipt


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True)
    parser.add_argument("--plan", action="store_true")
    args = parser.parse_args()
    result = run(args.output, plan=args.plan)
    print(json.dumps(result, indent=2))
    raise SystemExit(result.get("exit_code", 0))
