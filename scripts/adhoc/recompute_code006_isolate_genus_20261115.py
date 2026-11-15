"""Read-only native source recomputation for an applied genus canary, #2848.

2026-11-15. Inputs: exact current record/revision/native code and pinned761table.
JSON stdout only. No writer, network, source mixing or scientific assessment.
Stored staging mtime provenance is retained separately from current table mtime.
"""

import argparse
import hashlib
import importlib.util
import json
import socket
import subprocess
from pathlib import Path
from unittest.mock import patch

import yaml

ROOT = Path(__file__).resolve().parents[2]
TABLE = ".temp/gtdb-code006-20261115/kg-microbe/data/raw/NCBI2GTDB.tsv.gz"
TABLE_SHA = "761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd"
TARGETS = {
    "000552": "data/isolates/Pelagerythrobacter_N7_Halophilic_Pyrene_Oxidation_Isolate_Baseline.yaml",
    "000553": "data/isolates/Salinicola_A11_Halophilic_Bioemulsifier_Decarboxylase_Isolate_Baseline.yaml",
}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def head():
    return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()


def deny(*_args, **_kwargs):
    raise RuntimeError("network acquisition prohibited")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--record", choices=TARGETS, required=True)
    parser.add_argument("--expected-revision", required=True)
    parser.add_argument("--expected-record-sha256", required=True)
    args = parser.parse_args()
    target = ROOT / TARGETS[args.record]
    source, table = ROOT / "scripts/gtdb_ground.py", ROOT / TABLE
    inputs = {path: sha(path) for path in (target, source, table, Path(__file__))}
    if (
        head() != args.expected_revision
        or inputs[target] != args.expected_record_sha256
        or inputs[table] != TABLE_SHA
    ):
        raise ValueError("exact applied record, execution revision and table required")
    record = yaml.safe_load(target.read_bytes())
    if record["id"] != "CommunityMech:" + args.record or len(record["taxonomy"]) != 1:
        raise ValueError("exact selected isolate required")
    descriptor = record["taxonomy"][0]["taxon_term"]
    spec = importlib.util.spec_from_file_location("native_isolate_recompute", source)
    native = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(native)
    term = descriptor["term"]
    with patch.object(socket.socket, "connect", deny):
        groups = native.collect_rows(table, set(), set(), set(native.lookup_keys(term["label"])))
        result = native.resolve_target(term["id"].split(":")[1], term["label"], *groups)
        if not result or result.get("ambiguous"):
            raise ValueError("native same-genus correspondence unavailable")
        expected = native._block(result, native.describe_mapping(table))
    stored = descriptor["gtdb_classification"]

    def compared(block):
        return {key: value for key, value in block.items() if key != "mapping_source"}

    if descriptor["gtdb_grounding_status"] != "GROUNDED" or compared(stored) != compared(expected):
        raise ValueError("current classification differs from native source recomputation")
    if inputs != {path: sha(path) for path in inputs} or head() != args.expected_revision:
        raise ValueError("inputs changed during source recomputation")
    print(
        json.dumps(
            {
                "target": TARGETS[args.record],
                "record_sha256": inputs[target],
                "revision": args.expected_revision,
                "matches_corrected_block": True,
                "classifier_sha256": inputs[source],
                "crosswalk_path": TABLE,
                "crosswalk_sha256": inputs[table],
                "result": result,
                "block": stored,
                "native_current_mapping_source": expected.get("mapping_source"),
                "limits": "All mapping fields and GROUNDED status recomputed; stored staging mapping_source text is preserved. Current file mtime is not a release or proof of source vintage. No study-stock species/genome identity or scientific approval inferred.",
                "inputs": {str(path.relative_to(ROOT)): value for path, value in inputs.items()},
                "inputs_unchanged": True,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
