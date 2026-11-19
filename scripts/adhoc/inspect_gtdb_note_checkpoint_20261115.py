"""Verify one applied note-only intermediate; #2869/#2874, 2026-11-15.

Inputs: explicit check config, actual stage/apply evidence and eight native gates.
Output: metadata-only JSON on stdout; no writes, network or completion promotion.
The later mapping transition and immutable partial assessment remain separate.
"""

import argparse
import json
from pathlib import Path

import check_gtdb_batch_unit_20261115 as checks
import curate_gtdb_source_notes_20261115 as notes

ROOT = Path(__file__).resolve().parents[2]


def inspect(config_name, config_sha, prefix, attempt):
    captured = {}

    def get(name, expected=None):
        return notes.capture(captured, name, expected)

    get(str(Path(__file__).relative_to(ROOT)))
    get(str(Path(checks.__file__).relative_to(ROOT)))
    get(str(Path(notes.__file__).relative_to(ROOT)))
    config = json.loads(get(config_name, config_sha))
    target = config["target"]
    current = get(target, config["after_sha256"])
    applied_name = config["application_receipt"]
    applied = json.loads(get(applied_name, config["application_receipt_sha256"]))
    original_name = str(Path(applied_name).with_name("before.yaml"))
    original = get(original_name, config["before_sha256"])
    if (
        applied["applied"] is not True
        or applied["target"] != target
        or applied["before_sha256"] != config["before_sha256"]
        or applied["after_sha256"] != config["after_sha256"]
        or applied["scope"] != "taxonomy-notes-only"
        or applied["scientific_review"] is not False
    ):
        raise ValueError("actual note-only application required")
    stage_info = applied["reviewed_receipt"]
    stage = json.loads(get(stage_info["path"], stage_info["sha256"]))
    plan_info = applied["source_plan"]
    plan = json.loads(get(plan_info["path"], plan_info["sha256"]))
    if any(
        stage[key] != applied[key]
        for key in (
            "target",
            "target_id",
            "execution_revision",
            "before_sha256",
            "source_plan",
            "inputs",
            "appended_native_inline_history",
        )
    ):
        raise ValueError("actual stage/application chain differs")
    if (
        stage["candidate_sha256"] != applied["after_sha256"]
        or stage["canonical_apply"] is not False
        or stage["source_inputs_unchanged"] is not True
    ):
        raise ValueError("validated stage candidate differs")
    _, event = notes.verify_candidate(original, current, plan)
    if event != applied["appended_native_inline_history"]:
        raise ValueError("actual native event differs")
    for name, expected in applied["inputs"].items():
        raw = original if name == target else get(name, expected)
        if notes.sha(raw) != expected:
            raise ValueError("actual application input differs")
    for anchor in plan["source_anchors"]:
        if anchor["text"] not in get(anchor["path"], plan["inputs"][anchor["path"]]).decode():
            raise ValueError("captured source anchor differs")
    rows = []
    new_sidecars = {}
    for gate, recipe in checks.RECIPES.items():
        directory = Path(prefix + "-" + gate + "-" + attempt)
        receipt_name = str(directory / "receipt.json")
        receipt_raw = get(receipt_name)
        receipt = json.loads(receipt_raw)
        log = get(str(directory / "native.log"), receipt["log_sha256"])
        exit_raw = get(str(directory / "native.exit"))
        if (
            receipt["revision"] != applied["execution_revision"]
            or receipt["plan"] is not False
            or receipt["exit_code"] != 0
            or int(exit_raw.strip()) != 0
            or not receipt.get("finished_at")
            or receipt["execution_inputs_unchanged"] is not True
            or not log
            or len(log) != receipt["log_bytes"]
            or receipt["command"][:6]
            != ["just", "--verbose", "--no-dotenv", "--color", "never", recipe]
        ):
            raise ValueError("completed native gate differs: " + gate)
        expected_target = "history/records/" + Path(target).stem if gate == "history" else target
        if gate != "new-history" and receipt["command"][6] != expected_target:
            raise ValueError("native gate target differs")
        for name, expected in receipt["inputs"].items():
            location = Path(name)
            if location.is_relative_to(ROOT):
                get(str(location.relative_to(ROOT)), expected)
        required = {
            str(ROOT / target): config["after_sha256"],
            str(ROOT / applied_name): config["application_receipt_sha256"],
            str(ROOT / config_name): config_sha,
        }
        if any(receipt["inputs"].get(name) != value for name, value in required.items()):
            raise ValueError("native gate lacks exact application inputs")
        if gate == "new-history":
            new_sidecars = receipt["new_history_sidecars"]
            if len(new_sidecars) != 1:
                raise ValueError("one native sidecar required")
            for name, expected in new_sidecars.items():
                raw = get(name, expected)
                if (
                    applied_name.encode() not in raw
                    or config["application_receipt_sha256"].encode() not in raw
                ):
                    raise ValueError("sidecar lacks actual application link")
        elif receipt["new_history_sidecars"]:
            raise ValueError("validation unexpectedly added history")
        rows.append(
            {
                "gate": gate,
                "recipe": recipe,
                "revision": receipt["revision"],
                "started_at": receipt["started_at"],
                "finished_at": receipt["finished_at"],
                "exit_code": 0,
                "receipt": receipt_name,
                "receipt_sha256": notes.sha(receipt_raw),
                "log_sha256": notes.sha(log),
                "log_bytes": len(log),
                "exit_sha256": notes.sha(exit_raw),
                "python": receipt["python"],
            }
        )
    if any(location.read_bytes() != raw for location, raw in captured.items()):
        raise ValueError("captured checkpoint bytes changed")
    return {
        "target": target,
        "target_id": applied["target_id"],
        "execution_revision": applied["execution_revision"],
        "before_sha256": notes.sha(original),
        "after_sha256": notes.sha(current),
        "stage": stage_info,
        "application": {"path": applied_name, "sha256": notes.sha(get(applied_name))},
        "source_plan": plan_info,
        "new_history_sidecars": new_sidecars,
        "checks": rows,
        "captured_local_inputs": len(captured),
        "captured_inputs_unchanged": True,
        "external_history_source_limit": "Native receipt binds external Claw source hashes; this local inspector does not reread that external checkout.",
        "scientific_review": False,
        "mapping_transition_complete": False,
        "limits": "Verified note-only intermediate. Existing candidate alternatives remain unchanged; final mapping, immutable assessment and composite successor admission are pending.",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", required=True)
    parser.add_argument("--config-sha256", required=True)
    parser.add_argument("--prefix", required=True)
    parser.add_argument("--attempt", required=True)
    args = parser.parse_args()
    print(json.dumps(inspect(args.config, args.config_sha256, args.prefix, args.attempt), indent=2))
