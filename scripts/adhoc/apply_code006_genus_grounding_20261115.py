"""Apply the independently reviewed one-genus candidate, #2848, 2026-11-15.

Inputs: external candidate/receipt hashes and exact prior status-canary chain.
Outputs: exclusive actual application evidence and one canonical replacement
through the native validated writer. Sidecar/gates/assessment follow separately.
"""

import argparse
import importlib.util
import json
from datetime import datetime, timezone
from pathlib import Path

import apply_code006_gtdb_status_20261115 as guarded
import stage_code006_genus_grounding_20261115 as staging
import yaml

ROOT, STATE, TARGET, BASELINE = staging.ROOT, staging.STATE, staging.TARGET, staging.BASELINE
GUARD_SOURCE_SHA = "e71236dda4b27c53f9bed88e57351a715e6126868e62ddba7a857f31868dbce6"


def check(original, stage, candidate_sha, receipt_sha):
    candidate = (stage / Path(TARGET).name).read_bytes()
    receipt_bytes = (stage / "receipt.json").read_bytes()
    if guarded.digest(candidate) != candidate_sha or guarded.digest(receipt_bytes) != receipt_sha:
        raise ValueError("external reviewed candidate/receipt hashes differ")
    receipt = json.loads(receipt_bytes)
    if (
        guarded.digest(original) != BASELINE
        or receipt.get("code_revision") != staging.REVISION
        or receipt.get("canonical_apply") is not False
        or receipt.get("exit_codes") != [0, 0]
        or receipt.get("candidate_sha256") != candidate_sha
        or receipt.get("source_inputs_unchanged") is not True
        or receipt.get("inputs", {}).get(TARGET) != BASELINE
    ):
        raise ValueError("exact reviewed source/application chain required")
    required = {
        TARGET,
        "scripts/gtdb_ground.py",
        str(Path(staging.__file__).relative_to(ROOT)),
        ".temp/gtdb-code006-20261115/applied-001/receipt.json",
    }
    if not required.issubset(receipt.get("inputs", {})):
        raise ValueError("imported stager/native/actual predecessor inputs required")
    guarded.verify_inputs(receipt)
    source = ROOT / "scripts/gtdb_ground.py"
    spec = importlib.util.spec_from_file_location("actual_genus_apply_native", source)
    native = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(native)
    block = receipt["native_block"]
    expected_fields = {
        "gtdb_id": "GTDB:g__Mycobacterium",
        "gtdb_taxon": "Mycobacterium",
        "ncbi_source_id": "NCBITaxon:1763",
        "majority_fraction": 1.0,
        "support_genomes": 18589,
        "total_genomes": 18589,
        "is_reclassified": False,
    }
    if any(block.get(key) != value for key, value in expected_fields.items()):
        raise ValueError("reviewed same-genus correspondence differs")
    after = yaml.safe_load(candidate)
    staging.verify_semantics(yaml.safe_load(original), after, native, block)
    return candidate, receipt_bytes, receipt, after


def apply(stage, output, candidate_sha, receipt_sha, expected_revision, *, plan=False):
    stage, output = Path(stage).resolve(), Path(output).resolve()
    if (
        not stage.is_relative_to(STATE.resolve())
        or not output.is_relative_to(STATE.resolve())
        or output.exists()
        or guarded.current_head() != expected_revision
    ):
        raise ValueError("exclusive private namespace and exact execution revision required")
    guard_source = Path(guarded.__file__).resolve()
    if staging.sha(guard_source) != GUARD_SOURCE_SHA:
        raise ValueError("previous reviewed imported guard implementation differs")
    implementation = {
        path: staging.sha(path)
        for path in (Path(__file__), guard_source, Path(staging.__file__).resolve())
    }
    original = (ROOT / TARGET).read_bytes()
    candidate, receipt_bytes, receipt, after = check(original, stage, candidate_sha, receipt_sha)
    if plan:
        return {"planned": True, "target": TARGET, "candidate_sha256": candidate_sha}
    output.mkdir()
    (output / "before.yaml").write_bytes(original)
    guarded.write_validated_community(after, output / "validated.yaml")
    if yaml.safe_load((output / "validated.yaml").read_bytes()) != after:
        raise ValueError("native serialization differs")
    guarded.verify_inputs(receipt)
    if (
        guarded.current_head() != expected_revision
        or (ROOT / TARGET).read_bytes() != original
        or (stage / Path(TARGET).name).read_bytes() != candidate
        or (stage / "receipt.json").read_bytes() != receipt_bytes
        or implementation != {path: staging.sha(path) for path in implementation}
    ):
        raise ValueError("source/candidate/implementation changed during validation")
    (output / "replacement.yaml").write_bytes(candidate)
    (output / "replacement.yaml").replace(ROOT / TARGET)
    if (ROOT / TARGET).read_bytes() != candidate:
        raise ValueError("actual persisted canonical bytes differ")
    result = {
        "applied": True,
        "target": TARGET,
        "execution_revision": expected_revision,
        "before_sha256": BASELINE,
        "after_sha256": candidate_sha,
        "reviewed_receipt_sha256": receipt_sha,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "implementation": {
            str(path.relative_to(ROOT)): value for path, value in implementation.items()
        },
        "native_serialization_sha256": staging.sha(output / "validated.yaml"),
        "inputs": receipt["inputs"],
        "scope": "One same-genus reference correspondence. Species/genome identity, primary scientific assertions and both prior reviews remain unchanged.",
        "sidecar_status": "PENDING separate native scaffold/validation",
    }
    (output / "receipt.json").write_text(json.dumps(result, indent=2) + "\n")
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--stage", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--reviewed-candidate-sha256", required=True)
    parser.add_argument("--reviewed-receipt-sha256", required=True)
    parser.add_argument("--expected-revision", required=True)
    parser.add_argument("--plan", action="store_true")
    args = parser.parse_args()
    print(
        json.dumps(
            apply(
                args.stage,
                args.output,
                args.reviewed_candidate_sha256,
                args.reviewed_receipt_sha256,
                args.expected_revision,
                plan=args.plan,
            ),
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
