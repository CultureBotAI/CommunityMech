"""Export configured scoped GTDB canary proofs, #2848/#2860, 2026-11-15.

Inputs: externally pinned config, immutable saved review and retained raw bytes.
Outputs: exclusive reports-only metadata/log/exit artifacts and manifests.
Every payload is derived from one captured map; no source or review mutation.
"""

import argparse
import copy
import json
import re
import shlex
from collections import Counter
from pathlib import Path

import export_m5_technical_evidence_20261114 as redactor
import scoped_gtdb_evidence_20261115 as audit
import yaml
from export_m5_technical_evidence_20261114 import sanitize

ROOT = audit.ROOT
RECIPES = {
    "schema": "validate",
    "strict": "validate-strict",
    "gtdb": "validate-gtdb",
    "domain": "validate-gtdb-domain",
    "scalars": "validate-scalars",
    "history": "validate-history",
    "new-history": "new-history",
    "terms": "validate-terms",
}


def safe_path(name):
    path = ROOT / name
    if Path(name).is_absolute() or path.is_symlink() or not path.resolve().is_relative_to(ROOT):
        raise ValueError("unsafe repository-relative path")
    return path.resolve()


def raw_metadata(review, source, destination, captured):
    item = audit.bound(review, source, captured)
    raw = captured[source]
    if sanitize(raw.decode(), Counter()).encode() != raw:
        raise ValueError("byte-identical public metadata contains private content")
    return raw, {
        "path": str(destination.relative_to(ROOT)),
        "sha256": audit.digest(raw),
        "raw_path": item["path"],
        "raw_sha256": item["sha256"],
    }


def capture_additional(captured, paths):
    for path in paths:
        if path not in captured:
            captured[path] = path.read_bytes()


def gate_payload(review, captured, row, gate, directory, check_id, revision):
    for name in ("receipt.json", "native.log", "native.exit"):
        audit.bound(review, directory / name, captured)
    raw = captured[directory / "receipt.json"]
    receipt = json.loads(raw)
    log, exit_raw = captured[directory / "native.log"], captured[directory / "native.exit"]
    matching = [item for item in review["checks"] if item["check_id"] == check_id]
    if len(matching) != 1:
        raise ValueError("exact saved native check required")
    check = matching[0]
    targets = [
        value for name, value in receipt["inputs"].items() if name.endswith("/" + row["target"])
    ]
    command = receipt["command"]
    if (
        receipt["revision"] != revision
        or receipt["plan"] is not False
        or targets != [row["after_sha256"]]
        or receipt["exit_code"] != 0
        or exit_raw.strip() != b"0"
        or not receipt.get("finished_at")
        or receipt.get("execution_inputs_unchanged") is not True
        or not log
        or audit.digest(log) != receipt["log_sha256"]
        or len(log) != receipt["log_bytes"]
        or check["required"] is not True
        or check["status"] != "passed"
        or check["exit_code"] != 0
        or row["target_id"] not in check["target_ids"]
        or shlex.split(check["command"]) != command
        or command[:6] != ["just", "--verbose", "--no-dotenv", "--color", "never", RECIPES[gate]]
    ):
        raise ValueError("actual native gate proof differs: " + gate)
    if gate != "new-history":
        wanted = row["history_directory"] if gate == "history" else row["target"]
        if command[6] != wanted or (gate != "strict" and len(command) != 7):
            raise ValueError("native gate has wrong target or arguments")
        if gate == "strict" and command[7:] != [
            "--out",
            str((directory / "strict.tsv").relative_to(ROOT)),
        ]:
            raise ValueError("strict result path differs")
    else:
        if receipt["new_history_sidecars"] != {
            row["history_sidecar"]: audit.digest(captured[safe_path(row["history_sidecar"])])
        }:
            raise ValueError("actual new-history sidecar differs")
    counts = Counter()
    public_log = sanitize(log.decode(), counts).encode()
    public = json.loads(sanitize(raw.decode(), counts))
    public["public_evidence"] = {
        "raw_receipt_sha256": audit.digest(raw),
        "raw_log_sha256": audit.digest(log),
        "raw_exit_sha256": audit.digest(exit_raw),
        "public_log_sha256": audit.digest(public_log),
        "redactions": dict(sorted(counts.items())),
        "raw_location": "Saved-review input paths and hashes identify retained raw artifacts; this export verifies the current checkout's captured bytes.",
        "scope": "Scoped record grounding diagnostic only; no corpus or whole-record scientific completion.",
    }
    return public_log, exit_raw, (json.dumps(public, indent=2) + "\n").encode()


def prepare(config_path, expected_config_sha):
    config_path = config_path.resolve()
    raw_config = config_path.read_bytes()
    if audit.digest(raw_config) != expected_config_sha:
        raise ValueError("external config hash differs")
    config = json.loads(raw_config)
    review_path = safe_path(config["review"])
    review, captured = audit.validate_pair(review_path, config["review_sha256"])
    implementation_paths = (
        Path(__file__).resolve(),
        Path(audit.__file__).resolve(),
        Path(redactor.__file__).resolve(),
    )
    capture_additional(captured, (config_path, *implementation_paths))
    if captured[config_path] != raw_config:
        raise ValueError("config changed while capturing")
    if (
        review["scientific_review"] is not False
        or review["completion"] != "completed"
        or review["verdict"] != "pass_with_limitations"
        or review["scope"]["coverage"] != "partial"
        or review["source"]["git_revision"] != config["execution_revision"]
        or not 1 <= len(config["records"]) <= 10
        or {row["target_id"] for row in config["records"]}
        != {target["target_id"] for target in review["targets"]}
        or len({row["target_id"] for row in config["records"]}) != len(config["records"])
    ):
        raise ValueError("exact scoped review population/revision required")
    pending, manifests = {}, []
    for row in config["records"]:
        prefix = row["prefix"]
        if not re.fullmatch(r"[a-z0-9-]+", prefix):
            raise ValueError("safe exclusive artifact prefix required")
        out = safe_path(config["output_directory"])
        if not out.is_relative_to(ROOT / "reports"):
            raise ValueError("public reports output required")
        target, applied_path = safe_path(row["target"]), safe_path(row["application_receipt"])
        audit.bound(review, target, captured)
        audit.bound(review, applied_path, captured)
        applied = json.loads(captured[applied_path])
        before_path = applied_path.with_name("before.yaml")
        audit.bound(review, before_path, captured)
        if (
            applied["applied"] is not True
            or applied["execution_revision"] != config["execution_revision"]
            or applied["target"] != row["target"]
            or applied["before_sha256"] != row["before_sha256"]
            or applied["after_sha256"] != row["after_sha256"]
            or audit.digest(captured[target]) != row["after_sha256"]
            or audit.digest(captured[before_path]) != row["before_sha256"]
        ):
            raise ValueError("actual bounded application differs")
        before, after = yaml.safe_load(captured[before_path]), yaml.safe_load(captured[target])
        old, new = copy.deepcopy(before), copy.deepcopy(after)
        if old["id"] != row["target_id"] or new["id"] != row["target_id"]:
            raise ValueError("record identity differs")
        events = new.pop("curation_history")
        prior = old.pop("curation_history")
        if events[: len(prior)] != prior or events[len(prior) :] != row["appended_inline_events"]:
            raise ValueError("append-only reviewed history differs")
        for index in row["mutable_taxonomy_indices"]:
            for document in (old, new):
                term = document["taxonomy"][index]["taxon_term"]
                for key in ("gtdb_classification", "gtdb_grounding_status", "gtdb_candidates"):
                    term.pop(key, None)
        if old != new:
            raise ValueError("unrelated record semantics changed")
        source = safe_path(row["source_proof"])
        sidecar = safe_path(row["history_sidecar"])
        source_artifact = audit.bound(review, source, captured)
        sidecar_artifact = audit.bound(review, sidecar, captured)
        history = yaml.safe_load(captured[sidecar])
        if history["target"]["path"] != row["target"] or not history["events"]:
            raise ValueError("sidecar scope differs")
        applied_raw, applied_artifact = raw_metadata(
            review, applied_path, out / f"{prefix}-apply.raw.json", captured
        )
        route_raw, route_artifact = raw_metadata(
            review, source, out / f"{prefix}-native-proof.json", captured
        )
        payloads = {
            out / f"{prefix}-apply.raw.json": applied_raw,
            out / f"{prefix}-native-proof.json": route_raw,
        }
        gates = row["gates"]
        if not set(RECIPES).difference({"terms"}).issubset(gates) or not set(gates).issubset(
            RECIPES
        ):
            raise ValueError("required native gate set differs")
        for gate, item in gates.items():
            directory = safe_path(item["directory"])
            values = gate_payload(
                review,
                captured,
                row,
                gate,
                directory,
                item["check_id"],
                config["execution_revision"],
            )
            for suffix, raw in zip(("log.txt", "exit.txt", "receipt.json"), values, strict=True):
                payloads[out / f"{prefix}-{gate}.{suffix}"] = raw
        manifest = {
            "execution_revision": config["execution_revision"],
            "target": row["target"],
            "target_id": row["target_id"],
            "before_sha256": row["before_sha256"],
            "after_sha256": row["after_sha256"],
            "scientific_review": False,
            "diagnostic_review": audit.artifact(review_path, captured),
            "review_markdown": audit.artifact(review_path.with_name("review.md"), captured),
            "application_receipt": applied_artifact,
            "native_recomputation": route_artifact,
            "grounding_evidence": source_artifact,
            "history_sidecar": sidecar_artifact,
            "required_checks": list(gates),
            "review_inputs_verified": len(review["source"]["inputs"]),
            "native_markdown_verified": True,
            "mutable_taxonomy_indices": row["mutable_taxonomy_indices"],
            "scope": "Only configured GTDB block/status/candidates and exact appended native events may differ. Existing stock identities and biological claims remain unchanged; source-specific scientific support is assessed in the bound immutable review.",
        }
        manifest_path = out / f"{prefix}-successor.json"
        payloads[manifest_path] = (json.dumps(manifest, indent=2) + "\n").encode()
        if set(pending).intersection(payloads):
            raise ValueError("duplicate public artifact destinations")
        pending.update(payloads)
        manifests.append(str(manifest_path.relative_to(ROOT)))
    if any(path.exists() for path in pending):
        raise ValueError("public artifacts must be exclusive")
    audit.verify_captured(captured)
    result = {
        "review": config["review"],
        "review_inputs_verified": len(review["source"]["inputs"]),
        "native_markdown_verified": True,
        "implementation": {
            str(path.relative_to(ROOT)): audit.digest(captured[path])
            for path in implementation_paths
        },
        "config_sha256": expected_config_sha,
        "manifests": manifests,
        "artifacts": [
            {"path": str(path.relative_to(ROOT)), "sha256": audit.digest(raw)}
            for path, raw in sorted(pending.items())
        ],
    }
    return captured, pending, result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--expected-config-sha256", required=True)
    parser.add_argument("--plan", action="store_true")
    args = parser.parse_args()
    captured, pending, result = prepare(args.config, args.expected_config_sha256)
    if not args.plan:
        audit.publish(captured, pending)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
