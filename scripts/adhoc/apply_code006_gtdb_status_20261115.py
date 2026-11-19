"""Apply exactly the separately reviewed one-record status candidate, #2848.

2026-11-15. Inputs: immutable staged candidate/receipt and externally supplied
dual hashes, exact current revision, unchanged canonical/source/review inputs.
Outputs: exclusive private validation/application receipt and bounded canonical
replacement. Native RecordHistory scaffolding and gates follow separately.
"""

import argparse
import copy
import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))
from communitymech.curate.curation_event import record_curation_event  # noqa: E402
from communitymech.validation.write_validated import write_validated_community  # noqa: E402

TARGET = "kb/communities/Acidic_Nitrification_Minimal_Consortium.yaml"
BASELINE = "13b8ee224941b8e8a9767f0543b9eea1768c6499e311d0cde2cca07ade2e708d"
STAGING_REVISION = "c9e151eb9f22afb5c531dd5a8b3346ce1d58b12a"
STATE = ROOT / ".temp/gtdb-code006-20261115"


def digest(value):
    return hashlib.sha256(value).hexdigest()


def current_head():
    return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()


def verify_inputs(receipt):
    inputs = receipt.get("inputs") or {}
    required = {TARGET, "scripts/gtdb_ground.py"}
    if not required.issubset(inputs):
        raise ValueError("missing reviewed inputs")
    for name, expected in inputs.items():
        path = ROOT / name
        if Path(name).is_absolute() or path.is_symlink() or not path.resolve().is_relative_to(ROOT):
            raise ValueError("unsafe reviewed input path")
        if digest(path.read_bytes()) != expected:
            raise ValueError("reviewed input changed")


def checked_candidate(original, stage, candidate_sha, receipt_sha):
    raw_candidate = (stage / Path(TARGET).name).read_bytes()
    raw_receipt = (stage / "receipt.json").read_bytes()
    if digest(raw_candidate) != candidate_sha or digest(raw_receipt) != receipt_sha:
        raise ValueError("externally reviewed candidate/receipt differs")
    receipt = json.loads(raw_receipt)
    if (
        digest(original) != BASELINE
        or receipt.get("code_revision") != STAGING_REVISION
        or receipt.get("canonical_apply") is not False
        or receipt.get("exit_code") != 0
        or receipt.get("candidate_sha256") != candidate_sha
        or receipt.get("inputs", {}).get(TARGET) != BASELINE
        or receipt.get("source_inputs_unchanged") is not True
    ):
        raise ValueError("reviewed candidate provenance differs")
    before = yaml.safe_load(original)
    after = yaml.safe_load(raw_candidate)
    if before.get("id") != "CommunityMech:000434":
        raise ValueError("wrong record identity")
    expected = copy.deepcopy(before)
    term = expected["taxonomy"][1]["taxon_term"]
    if (
        term["term"] != {"id": "NCBITaxon:1763", "label": "Mycobacterium"}
        or term.get("gtdb_grounding_status") != "UNRESOLVED"
        or "gtdb_classification" in term
    ):
        raise ValueError("wrong bounded status baseline")
    term["gtdb_grounding_status"] = "NOT_ATTEMPTED"
    event = receipt["appended_native_inline_history"]
    wanted_event = record_curation_event(
        expected,
        curator="gtdb_ground.py",
        action="GTDB_SET_STATUS",
        changes="Wrote gtdb_grounding_status on 1 taxonomy entries (#294, #395).",
        timestamp=event.get("timestamp"),
    )
    if wanted_event != event or after != expected:
        raise ValueError("candidate exceeds reviewed one-status/history scope")
    verify_inputs(receipt)
    return raw_candidate, raw_receipt, after, receipt


def apply(stage, output, candidate_sha, receipt_sha, expected_revision, *, plan=False):
    stage, output = Path(stage).resolve(), Path(output).resolve()
    if (
        not stage.is_relative_to(STATE.resolve())
        or not output.is_relative_to(STATE.resolve())
        or output.exists()
    ):
        raise ValueError("exclusive private stage/output required")
    if current_head() != expected_revision:
        raise ValueError("wrong execution revision")
    original = (ROOT / TARGET).read_bytes()
    candidate, raw_receipt, after, receipt = checked_candidate(
        original, stage, candidate_sha, receipt_sha
    )
    if plan:
        return {"planned": True, "target": TARGET, "candidate_sha256": candidate_sha}
    output.mkdir()
    (output / "before.yaml").write_bytes(original)
    write_validated_community(after, output / "validated.yaml")
    if yaml.safe_load((output / "validated.yaml").read_bytes()) != after:
        raise ValueError("native serialization differs")
    # Validation is not a concurrency lock. Recheck every reviewed byte and the
    # external stage bindings after it, immediately before canonical replacement.
    verify_inputs(receipt)
    if (
        current_head() != expected_revision
        or (ROOT / TARGET).read_bytes() != original
        or (stage / Path(TARGET).name).read_bytes() != candidate
        or (stage / "receipt.json").read_bytes() != raw_receipt
    ):
        raise ValueError("concurrent source/candidate modification")
    (output / "replacement.yaml").write_bytes(candidate)
    (output / "replacement.yaml").replace(ROOT / TARGET)
    if (ROOT / TARGET).read_bytes() != candidate:
        raise ValueError("persisted canonical bytes differ")
    result = {
        "applied": True,
        "target": TARGET,
        "execution_revision": expected_revision,
        "before_sha256": BASELINE,
        "after_sha256": candidate_sha,
        "reviewed_receipt_sha256": receipt_sha,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "helper_sha256": digest(Path(__file__).read_bytes()),
        "native_serialization_sha256": digest((output / "validated.yaml").read_bytes()),
        "scope": "Current crosswalk computability for existing genus only; no biological identity or historical scientific review change.",
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
