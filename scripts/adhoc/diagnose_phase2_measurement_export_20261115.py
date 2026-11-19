"""Diagnose refused Phase2 measurement exports without editing inputs, 2026-11-15.

Inputs: source checkout and retained native measurement directory (Phase2/#476).
Output: JSON on stdout, limited to exception type, static guard message, relative
record/assertion path and code frame names. No raw excerpt/reference values.
This calls only the metadata verifier, never native matching or acquisition.
"""

import argparse
import importlib.util
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path, required=True)
    parser.add_argument("--run", type=Path, required=True)
    args = parser.parse_args()
    path = Path(__file__).with_name("export_phase2_reference_measurement_20261115.py")
    spec = importlib.util.spec_from_file_location("phase2_measurement_export", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    try:
        summary = module.checked_summary(args.source_root, args.run, "M5")
    except Exception as error:
        report = {"exception_type": type(error).__name__, "frames": []}
        frame = error.__traceback__
        while frame:
            code = frame.tb_frame.f_code
            report["frames"].append(
                {
                    "file": Path(code.co_filename).name,
                    "function": code.co_name,
                    "line": frame.tb_lineno,
                }
            )
            if code.co_name == "require":
                report["static_guard_message"] = frame.tb_frame.f_locals.get("message")
            if code.co_name == "checked_summary":
                context = frame.tb_frame.f_locals
                report["record"] = context.get("row", {}).get("record")
                report["assertion_path"] = context.get("item", {}).get("path")
            frame = frame.tb_next
        print(json.dumps(report, indent=2))
        return 1
    print(json.dumps({"verified": True, "counts": summary["counts"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
