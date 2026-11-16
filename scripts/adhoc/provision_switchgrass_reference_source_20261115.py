"""Copy verified local Table S1 inputs into the normal source catalog; #1996.

2026-11-15. Inputs: pinned consumer preparation and its three fixed artifacts.
Outputs: catalog metadata, ignored asset/projection and an exclusive receipt.
No acquisition, configuration edit, canonical record edit or existing-file overwrite.
"""

from __future__ import annotations

import argparse
import json
import subprocess
from hashlib import sha256
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DESTINATION = "conf/reference_sources"
PINS = {
    "catalog.json": "d3e425adfb24a75f30d7e1dd9aac729388861e6b18da6782ac0d6099e87c11f1",
    "assets/msystems.00951-22-s0006.docx": "5bfa02fdb94538e9405fb0ec7d7b0dad338791a5ca0b4b651589f33148c8e0e7",
    "extractions/table-s1.json": "c322c14c7e754df924e3e3151fb3d8e18564537dd0448e43d9a856d4e3ef32a5",
}


def local(name, *, private=False):
    relative = Path(name)
    path = ROOT / relative
    if (
        relative.is_absolute()
        or ".." in relative.parts
        or (private and relative.parts[:1] != (".temp",))
        or not path.resolve().is_relative_to(ROOT.resolve())
        or any(part.is_symlink() for part in (path, *path.parents))
    ):
        raise ValueError("safe repository-relative path required")
    return path


def digest(raw):
    return sha256(raw).hexdigest()


def provision(prepared, preparation_sha, output, *, plan=False):
    from linkml_reference_validator.etl.source_locator import extract_docx_tables

    directory = local(prepared, private=True)
    receipt_path = directory / "preparation.json"
    receipt_raw = receipt_path.read_bytes()
    if digest(receipt_raw) != preparation_sha:
        raise ValueError("pinned preparation differs")
    receipt = json.loads(receipt_raw)
    if receipt.get("plan") is not False or any(
        receipt.get("outputs", {}).get(name) != expected for name, expected in PINS.items()
    ):
        raise ValueError("completed fixed-source preparation required")
    inputs = {receipt_path: receipt_raw}
    for name, expected in PINS.items():
        path = local(str((directory / name).relative_to(ROOT)), private=True)
        raw = path.read_bytes()
        if digest(raw) != expected:
            raise ValueError("prepared artifact differs: " + name)
        inputs[path] = raw
    if extract_docx_tables(inputs[directory / "assets/msystems.00951-22-s0006.docx"]) != json.loads(
        inputs[directory / "extractions/table-s1.json"]
    ):
        raise ValueError("bound projection does not replay")
    output_path = local(output, private=True)
    if output_path.exists():
        raise ValueError("exclusive output directory required")
    destinations = {local(f"{DESTINATION}/{name}"): inputs[directory / name] for name in PINS}
    for path, raw in destinations.items():
        if path.exists() and (not path.is_file() or path.read_bytes() != raw):
            raise ValueError("existing destination differs: " + str(path.relative_to(ROOT)))
        if path.suffix != ".json" or path.name != "catalog.json":
            ignored = subprocess.run(
                ["git", "check-ignore", "--quiet", "--", str(path.relative_to(ROOT))], cwd=ROOT
            )
            if ignored.returncode != 0:
                raise ValueError("source content must be gitignored before provisioning")
    result = {
        "plan": plan,
        "revision": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
        ).strip(),
        "inputs": {str(path.relative_to(ROOT)): digest(raw) for path, raw in inputs.items()},
        "outputs": {str(path.relative_to(ROOT)): digest(raw) for path, raw in destinations.items()},
        "configuration_edited": False,
        "canonical_record_edited": False,
    }
    if any(path.read_bytes() != raw for path, raw in inputs.items()):
        raise ValueError("source input drift")
    if plan:
        return result
    for path, raw in destinations.items():
        if not path.exists():
            path.parent.mkdir(parents=True, exist_ok=True)
            with path.open("xb") as handle:
                handle.write(raw)
        if path.read_bytes() != raw:
            raise ValueError("persisted source differs")
    if any(path.read_bytes() != raw for path, raw in inputs.items()):
        raise ValueError("source input drift")
    output_path.mkdir(parents=True)
    raw = (json.dumps(result, indent=2, sort_keys=True) + "\n").encode()
    with (output_path / "receipt.json").open("xb") as handle:
        handle.write(raw)
    if (output_path / "receipt.json").read_bytes() != raw:
        raise ValueError("persisted receipt differs")
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--prepared", required=True)
    parser.add_argument("--preparation-sha256", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--plan", action="store_true")
    args = parser.parse_args()
    print(
        json.dumps(provision(args.prepared, args.preparation_sha256, args.output, plan=args.plan))
    )


if __name__ == "__main__":
    main()
