"""Apply one independently reviewed JMP134 mapping candidate, #2848, 2026-11-15.

Inputs: external reviewed candidate/receipt hashes, exact execution revision,
unchanged source proof and native implementation. Outputs: native-validated
bounded replacement and exclusive private receipt; sidecar/gates follow.
"""

import argparse
import copy
import json
from datetime import datetime, timezone
from pathlib import Path

import stage_jmp134_grounding_20261115 as staging
import yaml

from communitymech.validation.write_validated import write_validated_community

ROOT, STATE, TARGET, BASELINE = staging.ROOT, staging.STATE, staging.TARGET, staging.BASELINE
digest = staging.evidence.digest


def checked_inputs(raw_receipt, original, candidate, candidate_sha):
    receipt = json.loads(raw_receipt)
    required = {
        TARGET,
        "scripts/gtdb_ground.py",
        "scripts/adhoc/stage_jmp134_grounding_20261115.py",
        "scripts/adhoc/inspect_jmp134_grounding_20261115.py",
        ".temp/gtdb-species-status-20261115/jmp134-source-001.json",
        ".temp/gtdb-species-status-20261115/kg-microbe/data/raw/NCBI2GTDB.tsv.gz",
        "src/communitymech/validation/write_validated.py",
        "src/communitymech/schema/communitymech.yaml",
        "src/communitymech/schema/mech_shared.yaml",
    }
    if (
        digest(original) != BASELINE
        or receipt.get("code_revision") != staging.REVISION
        or receipt.get("canonical_apply") is not False
        or receipt.get("source_inputs_unchanged") is not True
        or receipt.get("exit_codes") != [0, 0]
        or receipt.get("candidate_sha256") != candidate_sha
        or not required.issubset(receipt.get("inputs", {}))
    ):
        raise ValueError("exact native candidate/source provenance required")
    captured = {}
    for name, expected in receipt["inputs"].items():
        path = ROOT / name
        if Path(name).is_absolute() or path.is_symlink() or not path.resolve().is_relative_to(ROOT):
            raise ValueError("unsafe source input path")
        raw = path.read_bytes()
        if digest(raw) != expected:
            raise ValueError("reviewed source input changed")
        captured[path] = raw
    if captured[ROOT / TARGET] != original:
        raise ValueError("target changed while capturing")
    proof_path = ROOT / ".temp/gtdb-species-status-20261115/jmp134-source-001.json"
    if digest(captured[proof_path]) != staging.PROOF_SHA:
        raise ValueError("reviewed primary/stock/crosswalk source proof differs")
    proof = json.loads(captured[proof_path])
    if any(
        ROOT / name not in captured or digest(captured[ROOT / name]) != expected
        for name, expected in proof["inputs"].items()
    ):
        raise ValueError("source proof inputs must all be captured exactly")
    native = staging.native_module()
    block = receipt["native_block"]
    result = proof["native_result"]
    expected_block = native._block(result, block["mapping_source"])
    if (
        result.get("via") != "ncbi_id"
        or result.get("ncbi_source_id") != "NCBITaxon:264198"
        or result.get("gtdb_id") != "GTDB:s__Cupriavidus_pinatubonensis"
        or result.get("majority_fraction") != 1.0
        or result.get("total_genomes") != 1
        or result.get("is_reclassified") is not False
        or receipt.get("native_result") != result
        or block != expected_block
        or "sha256:761d5537a7edb4b0" not in block["mapping_source"]
    ):
        raise ValueError("exact one-genome native source correspondence differs")
    after = yaml.safe_load(candidate)
    before = yaml.safe_load(original)
    expected = copy.deepcopy(before)
    term = expected["taxonomy"][0]["taxon_term"]
    if (
        expected["id"] != "CommunityMech:000555"
        or len(expected["taxonomy"]) != 1
        or term["term"] != {"id": "NCBITaxon:264198", "label": "Cupriavidus pinatubonensis JMP134"}
        or term.get("gtdb_grounding_status") != "UNRESOLVED"
        or "gtdb_classification" in term
    ):
        raise ValueError("wrong exact-strain application baseline")
    term["gtdb_classification"] = block
    term["gtdb_grounding_status"] = "GROUNDED"
    events = after.get("curation_history", [])[len(before.get("curation_history", [])) :]
    if len(events) != 2:
        raise ValueError("two appended native events required")
    for event, action, changes in zip(
        events,
        ("GTDB_GROUND", "GTDB_SET_STATUS"),
        (
            "Added 1 gtdb_classification block(s) from NCBI2GTDB.tsv.gz (#395).",
            "Wrote gtdb_grounding_status on 1 taxonomy entries (#294, #395).",
        ),
        strict=True,
    ):
        if event != native.record_curation_event(
            expected,
            curator="gtdb_ground.py",
            action=action,
            changes=changes,
            timestamp=event.get("timestamp"),
        ):
            raise ValueError("native application event differs")
    if after != expected:
        raise ValueError("candidate exceeds one block/status/two-event scope")
    if events != receipt.get("appended_native_inline_history"):
        raise ValueError("appended native history differs from receipt")
    return receipt, captured, after


def apply(stage, output, candidate_sha, receipt_sha, expected_revision, *, plan=False):
    stage, output = Path(stage).resolve(), Path(output).resolve()
    if (
        not stage.is_relative_to(STATE.resolve())
        or not output.is_relative_to(STATE.resolve())
        or output.exists()
        or staging.head() != expected_revision
    ):
        raise ValueError("exclusive private namespace and exact execution revision required")
    original = (ROOT / TARGET).read_bytes()
    candidate_path = stage / Path(TARGET).name
    receipt_path = stage / "receipt.json"
    candidate, raw_receipt = candidate_path.read_bytes(), receipt_path.read_bytes()
    if digest(candidate) != candidate_sha or digest(raw_receipt) != receipt_sha:
        raise ValueError("external reviewed candidate/receipt hashes differ")
    receipt, captured, after = checked_inputs(raw_receipt, original, candidate, candidate_sha)
    for path in (Path(__file__), candidate_path, receipt_path):
        captured[path] = path.read_bytes()
    if captured[candidate_path] != candidate or captured[receipt_path] != raw_receipt:
        raise ValueError("staged input changed while capturing")
    staging.unchanged(captured)
    if plan:
        return {"planned": True, "target": TARGET, "candidate_sha256": candidate_sha}
    output.mkdir()
    (output / "before.yaml").write_bytes(original)
    write_validated_community(after, output / "validated.yaml")
    if yaml.safe_load((output / "validated.yaml").read_bytes()) != after:
        raise ValueError("native validated serialization differs")
    staging.unchanged(captured)
    if staging.head() != expected_revision:
        raise ValueError("execution revision changed")
    # This is a bounded concurrent-change guard, not a lock against writers
    # that ignore cooperation. No force-recovery or automatic retry is allowed.
    (output / "replacement.yaml").write_bytes(candidate)
    (output / "replacement.yaml").replace(ROOT / TARGET)
    if (ROOT / TARGET).read_bytes() != candidate:
        raise ValueError("actual persisted record differs")
    result = {
        "applied": True,
        "target": TARGET,
        "execution_revision": expected_revision,
        "before_sha256": BASELINE,
        "after_sha256": candidate_sha,
        "reviewed_receipt_sha256": receipt_sha,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "inputs": receipt["inputs"],
        "helper_sha256": digest(captured[Path(__file__)]),
        "native_serialization_sha256": digest((output / "validated.yaml").read_bytes()),
        "scope": receipt["scope"],
        "sidecar_status": "PENDING separate native scaffold and validation",
        "scientific_review": False,
    }
    (output / "receipt.json").write_text(json.dumps(result, indent=2) + "\n")
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stage", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--reviewed-candidate-sha256", required=True)
    parser.add_argument("--reviewed-receipt-sha256", required=True)
    parser.add_argument("--expected-revision", required=True)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--plan", action="store_true")
    mode.add_argument("--apply", action="store_true")
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
