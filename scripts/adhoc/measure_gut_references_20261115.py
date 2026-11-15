"""Measure the exact staged/canonical 000122 reference assertions, 2026-11-15.

Input: one explicit record and maintained native-CLI coverage implementation.
Output: exclusive .temp receipt/native log. This is a focused content-hash binding,
not a claim of Git-declared corpus coverage. Native network/cache writes are refused
by the maintained measurement adapter. Serves #1548/#476.
"""

import argparse
import json
import sys
from pathlib import Path

from ruamel.yaml import YAML

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
import reference_assertion_coverage as native  # noqa: E402


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--record", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    path = args.record.resolve()
    output = args.output.resolve()
    if not path.is_relative_to(ROOT) or not output.is_relative_to(ROOT / ".temp"):
        raise ValueError("repository record and private output required")
    raw = path.read_bytes()
    document = YAML(typ="safe").load(raw)
    if document["id"] != "CommunityMech:000122":
        raise ValueError("wrong target")
    relative = str(path.relative_to(ROOT))
    output.mkdir()
    before = native.input_manifest(ROOT, [relative])
    result, log = native.measure(ROOT, [(relative, document)], [path])
    after = native.input_manifest(ROOT, [relative])
    result.update(
        record_sha256=native.digest(raw),
        inputs=before,
        inputs_unchanged=before == after,
        head=native.git(ROOT, "rev-parse", "HEAD"),
        measurement_helper_sha256=native.digest(Path(native.__file__).read_bytes()),
        scope="One exact staged/canonical record; no corpus inventory claim",
    )
    (output / "native.log").write_text(log)
    (output / "receipt.json").write_text(json.dumps(result, indent=2) + "\n")
    code = 2 if not result["measurement_valid"] or before != after else result["native_exit_code"]
    (output / "exit").write_text(str(code) + "\n")
    print(
        json.dumps(
            {
                key: result[key]
                for key in (
                    "counts",
                    "assertion_status_counts",
                    "measurement_valid",
                    "assertion_coverage_complete",
                    "inputs_unchanged",
                )
            },
            indent=2,
        )
    )
    raise SystemExit(code)


if __name__ == "__main__":
    main()
