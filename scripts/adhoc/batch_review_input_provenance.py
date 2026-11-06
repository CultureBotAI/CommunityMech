"""Capture a configured batch's current inputs without superseding scientific work.

This one-off workflow accepts a frozen JSON configuration, inventories exact
current manifest members, and produces a JSON candidate after native inspection.
It writes only new JSON artifacts under the configured PR scratch directory.
The native record-review saver owns publication of the immutable review pair.
"""

import argparse
import hashlib
import json
import shlex
import subprocess
from datetime import datetime, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
SELF = str(Path(__file__).relative_to(ROOT))
REPOSITORY = "CultureBotAI/CommunityMech"
RULES = [
    "AGENTS.md",
    "docs/record-reviews.md",
    "docs/record-review-profile.md",
    "conf/record_review.yaml",
    "schema/record_review.yaml",
    "scripts/record_review.py",
    "src/communitymech/schema/communitymech.yaml",
    ".claude/skills/review-communities/SKILL.md",
    ".claude/skills/review-communities/reference/execution-protocol.md",
]


def now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def local(name):
    path = ROOT / name
    if Path(name).is_absolute() or path.is_symlink() or not path.resolve().is_relative_to(ROOT):
        raise ValueError(f"Unsafe checkout input: {name}")
    return path


def digest(name):
    return hashlib.sha256(local(name).read_bytes()).hexdigest()


def read_json(name):
    return json.loads(local(name).read_text())


def read_review(name):
    return yaml.safe_load(local(name).read_text())


def write_json(out, name, value):
    path = local(str(out / name))
    if not path.is_relative_to(local(str(out))) or path.exists():
        raise ValueError(f"Refusing unsafe or existing output: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n")
    return str(path.relative_to(ROOT))


def review_metadata(review, path):
    return {
        "path": path,
        "review_id": review["review_id"],
        "completion": review["completion"],
        "verdict": review["verdict"],
        "scientific_review": review["scientific_review"],
        "issue_keys": [f["issue_key"] for f in review["findings"]],
    }


def pin_pair(inputs, path):
    inputs.update([path, str(Path(path).with_name("review.md"))])


def continuing_occurrence(finding, previous, review):
    return any(
        p["repository"] == REPOSITORY
        and p["review_id"] == review["review_id"]
        and p["finding_id"] == previous["finding_id"]
        for p in finding.get("previous_occurrences", [])
    )


def retained_actions(review, keys):
    """Keep exact action objects selected by live heads and prerequisite closure."""
    if keys == {f["issue_key"] for f in review["findings"]}:
        return review["actions"]
    if any(not a["finding_ids"] for a in review["actions"]):
        raise ValueError("Partial succession needs explicit handling of unlinked actions")
    finding_ids = {f["finding_id"] for f in review["findings"] if f["issue_key"] in keys}
    by_id = {a["action_id"]: a for a in review["actions"]}
    pending = [a["action_id"] for a in review["actions"] if finding_ids & set(a["finding_ids"])]
    selected = set()
    while pending:
        action_id = pending.pop()
        if action_id not in selected:
            selected.add(action_id)
            pending.extend(by_id[action_id].get("depends_on", []))
    return [a for a in review["actions"] if a["action_id"] in selected]


def apply_partial_successors(active, names, target_id):
    """Advance only explicitly linked keys; retain every unaffected head."""
    for name in names:
        review = read_review(name)
        if target_id not in {t["target_id"] for t in review["targets"]}:
            raise ValueError(f"Partial observation omits target: {name}")
        all_keys = [key for _, _, keys in active for key in keys]
        if len(all_keys) != len(set(all_keys)):
            raise ValueError(f"Ambiguous predecessor heads: {target_id}")
        current = {
            f["issue_key"]: (r, f)
            for r, _, keys in active
            for f in r["findings"]
            if f["issue_key"] in keys
        }
        new_keys = {f["issue_key"] for f in review["findings"]}
        if not new_keys or not new_keys <= set(current):
            raise ValueError(f"Partial successor must update existing keys: {name}")
        for finding in review["findings"]:
            prior_review, prior = current[finding["issue_key"]]
            if not continuing_occurrence(finding, prior, prior_review):
                raise ValueError(f"Missing exact partial lineage: {finding['issue_key']}")
            if not set(prior["target_ids"]) <= set(finding["target_ids"]):
                raise ValueError(
                    f"Partial successor drops affected targets: {finding['issue_key']}"
                )
        active = [(r, p, keys - new_keys) for r, p, keys in active if keys - new_keys]
        active.append((review, name, new_keys))
    return active


def capture(args, config, out):
    inputs = set(RULES + [SELF, args.config, config["inventory"]] + config["extra_inputs"])
    manifest_targets = {}
    for spec in config["manifests"]:
        name = spec if isinstance(spec, str) else spec["path"]
        manifest = read_json(name)
        inputs.add(name)
        member_key = "inputs" if isinstance(spec, str) else spec.get("member_key", "inputs")
        for item in manifest[member_key]:
            if digest(item["path"]) != item["sha256"]:
                raise ValueError(f"Changed manifest input: {item['path']}")
            inputs.add(item["path"])
        declared_targets = manifest.get("targets", []) if isinstance(spec, str) else spec["targets"]
        for target in declared_targets:
            manifest_targets.setdefault(target, []).append(name)

    records, targets = [], []
    seen_targets = set()
    for entry in read_json(config["inventory"]):
        target_id, path = entry["target_id"], entry["path"]
        if target_id in seen_targets:
            raise ValueError(f"Duplicate target: {target_id}")
        seen_targets.add(target_id)
        original = read_review(entry["review"])
        target = next(t for t in original["targets"] if t["target_id"] == target_id)
        if target["path"] != path:
            raise ValueError(f"Conflicting target path: {target_id}")
        targets.append(target)
        pin_pair(inputs, entry["review"])
        inputs.add(path)
        original_pin = next(i for i in original["source"]["inputs"] if i["path"] == path)
        original_keys = {f["issue_key"] for f in original["findings"]}
        original_by_key = {f["issue_key"]: f for f in original["findings"]}
        active = [(original, entry["review"], original_keys)]
        replacement = config["replacements"].get(target_id)
        if digest(path) != original_pin["sha256"] and not replacement:
            raise ValueError(f"Changed target lacks an explicit successor: {target_id}")
        if replacement:
            review = read_review(replacement)
            replacement_keys = {f["issue_key"] for f in review["findings"]}
            if not original_keys <= replacement_keys:
                raise ValueError(f"Replacement does not preserve original keys: {target_id}")
            for finding in review["findings"]:
                if finding["issue_key"] not in original_keys:
                    continue
                previous = original_by_key[finding["issue_key"]]
                if not continuing_occurrence(finding, previous, original):
                    raise ValueError(f"Missing exact replacement lineage: {finding['issue_key']}")
                if not set(previous["target_ids"]) <= set(finding["target_ids"]):
                    raise ValueError(f"Replacement drops affected targets: {finding['issue_key']}")
            active = [(review, replacement, replacement_keys)]
        for name in config["supplements"].get(target_id, []):
            review = read_review(name)
            active.append((review, name, {f["issue_key"] for f in review["findings"]}))
        active = apply_partial_successors(
            active, config.get("partial_successors", {}).get(target_id, []), target_id
        )
        active_keys, actions = set(), []
        for review, name, keys in active:
            if target_id not in {t["target_id"] for t in review["targets"]}:
                raise ValueError(f"Current observation omits target: {name}")
            if any(f["status"] != "open" for f in review["findings"]):
                raise ValueError(f"Unexpected disposition in current observation: {name}")
            if active_keys & keys:
                raise ValueError(f"Ambiguous active finding heads: {target_id}")
            active_keys.update(keys)
            actions.extend(retained_actions(review, keys))
            pin_pair(inputs, name)
            if name != entry["review"]:
                for item in review["source"]["inputs"]:
                    if digest(item["path"]) != item["sha256"]:
                        raise ValueError(f"Changed current-observation input: {item['path']}")
                    inputs.add(item["path"])
        if not original_keys <= active_keys:
            raise ValueError(f"Original scientific key lost: {target_id}")
        if active_keys - original_keys != set(config["additional_keys"].get(target_id, [])):
            raise ValueError(f"Unaccounted additional finding: {target_id}")
        if not manifest_targets.get(target_id):
            raise ValueError(f"No concrete current-artifact manifest: {target_id}")
        row = {
            "target_id": target_id,
            "path": path,
            "current_sha256": digest(path),
            "original_target_sha256": original_pin["sha256"],
            "changed_since_original": digest(path) != original_pin["sha256"],
            "original": review_metadata(original, entry["review"]),
            "original_input_count": len(original["source"]["inputs"]),
            "original_scratch_input_count": sum(
                i["path"].startswith((".temp/", "/private/tmp/"))
                or Path(i["path"]).parts[:2] == ("/", "tmp")
                for i in original["source"]["inputs"]
            ),
            "original_actions": original["actions"],
            "current_observations": [
                {**review_metadata(r, p), "effective_issue_keys": sorted(keys)}
                for r, p, keys in active
            ],
            "current_issue_keys": sorted(active_keys),
            "current_actions": actions,
            "current_action_sources": [
                {"review_id": r["review_id"], "action_id": a["action_id"]}
                for r, _, keys in active
                for a in retained_actions(r, keys)
            ],
            "current_manifest_paths": manifest_targets[target_id],
            "limitation": "Historical scratch is unavailable; current artifacts do not reconstruct old bytes. This process observation changes no scientific occurrence or action.",
        }
        name = write_json(out, f"records/{target_id.split(':')[1]}.json", row)
        inputs.add(name)
        records.append({**row, "manifest": name})
    unknown = (
        set(config["replacements"])
        | set(config["supplements"])
        | set(config.get("partial_successors", {}))
        | set(config["additional_keys"])
    ) - seen_targets
    if unknown:
        raise ValueError(f"Unknown configured targets: {sorted(unknown)}")
    counts = {
        "records": len(records),
        "original_inputs": sum(r["original_input_count"] for r in records),
        "original_findings": sum(len(r["original"]["issue_keys"]) for r in records),
        "current_findings": sum(len(r["current_issue_keys"]) for r in records),
        "original_actions": sum(len(r["original_actions"]) for r in records),
        "current_actions": sum(len(r["current_actions"]) for r in records),
        "original_acceptance_checks": sum(
            len(a["acceptance_checks"]) for r in records for a in r["original_actions"]
        ),
        "current_acceptance_checks": sum(
            len(a["acceptance_checks"]) for r in records for a in r["current_actions"]
        ),
    }
    if counts != config["expected_counts"]:
        raise ValueError(f"Unexpected accounting: {counts}")
    audit = {
        "started_at": now(),
        "capture_head": subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip(),
        "counts": counts,
        "records": records,
        "command": shlex.join(["python", SELF, "--config", args.config, "capture"]),
        "scope": "Byte provenance and preservation of existing scientific work only; no literature reassessment, historical scratch reconstruction or new scientific disposition.",
    }
    inputs.add(write_json(out, "audit.json", audit))
    inputs.add(write_json(out, "targets.json", {"targets": targets}))
    write_json(
        out, "inputs.json", {"inputs": [{"path": p, "sha256": digest(p)} for p in sorted(inputs)]}
    )
    print(json.dumps(counts))


def build(args, config, out):
    audit = read_json(str(out / "audit.json"))
    manifest = read_json(str(out / "inputs.json"))
    inspection = read_json(args.inspection)
    source = inspection.get("source", inspection)
    expected = {i["path"] for i in manifest["inputs"]} | {str(out / "inputs.json")}
    if {i["path"] for i in source["inputs"]} != expected:
        raise ValueError("Native inspection must pin the complete exact input set")
    for item in manifest["inputs"] + source["inputs"]:
        if digest(item["path"]) != item["sha256"]:
            raise ValueError(f"Changed captured or inspected input: {item['path']}")
    targets = read_json(str(out / "targets.json"))["targets"]
    ids = [t["target_id"] for t in targets]
    evidence, assessments, related = [], [], {}
    for row in audit["records"]:
        eid = "provenance-" + row["target_id"].split(":")[1]
        change = (
            "changed; the separate successor is retained"
            if row["changed_since_original"]
            else "unchanged"
        )
        current = "; ".join(
            f"{r['review_id']} ({r['completion']}/{r['verdict']}, "
            f"scientific_review={r['scientific_review']}; "
            f"{len(r['effective_issue_keys'])} retained finding heads)"
            for r in row["current_observations"]
        )
        evidence.append(
            {
                "evidence_id": eid,
                "kind": "validation",
                "reference": row["manifest"],
                "locator": "Entire per-record manifest: exact old/current target digests, original/current review statuses, open issue keys/actions, concrete current input manifests.",
                "accessed_at": now(),
                "support": "supports",
                "snapshot_sha256": digest(row["manifest"]),
                "summary": f"The target is {change}. {len(row['current_issue_keys'])} current open finding keys remain. This observation makes no scientific disposition.",
            }
        )
        assessments.append(
            {
                "assessment_id": eid,
                "area": "provenance",
                "topic": "Historical input-set limitation and present byte accounting",
                "outcome": "supported",
                "target_ids": [row["target_id"]],
                "evidence_ids": [eid],
                "summary": f"Original {row['original']['completion']}/{row['original']['verdict']} review {row['original']['review_id']} declared {row['original_input_count']} inputs, including {row['original_scratch_input_count']} scratch paths. Its target is now {change}; current digest {row['current_sha256']}. Current observations: {current}.",
                "details": "The historical input set omits local source/check bytes and remains incomplete; evidence-level historical hashes do not replace omitted source.inputs. Current manifest members are individually frozen here, not reconstructed historical files. This audits byte provenance rather than literature support. Archive pins identify containers, not manual inspection of every asset. Current scientific/authority observations retain their separate scopes, limits, findings and actions; none is superseded by this process-only batch.",
            }
        )
        for review in [row["original"], *row["current_observations"]]:
            related[review["review_id"]] = {
                "repository": REPOSITORY,
                "review_id": review["review_id"],
                "relationship": "Bounded append-only input provenance accounting; retain all findings/actions and original or separate corrective scope. No scientific occurrence supersession.",
            }
    counts = audit["counts"]
    accounting = (
        f"{counts['original_findings']} original finding keys and "
        f"{counts['original_actions']} original actions / {counts['original_acceptance_checks']} "
        f"acceptance checks are retained in historical accounting. Separate current observations "
        f"maintain {counts['current_findings']} open finding keys, {counts['current_actions']} actions "
        f"and {counts['current_acceptance_checks']} acceptance checks."
    )
    candidate = {
        "schema_version": "1.0.0",
        "review_id": args.review_id,
        "kind": "batch",
        "repository": REPOSITORY,
        "title": f"PR{config['pr']} bounded current-input provenance and historical scratch limitation",
        "started_at": audit["started_at"],
        "finished_at": now(),
        "reviewer": {
            "identity": "Codex /root/batch2035_434_refresh",
            "kind": "agent",
            "independence": "self_review",
            "independence_basis": "Author of this process-only observation. Earlier scientific reviewers retain their declared independent or author roles; this candidate requires a separate read-only review.",
        },
        "skill": "review-communities",
        "completion": "completed",
        "verdict": "not_assessed",
        "scientific_review": False,
        "summary": f"Completed only the bounded {counts['records']}-record provenance accounting. {accounting} Current source/check artifacts are frozen individually; omitted historical scratch remains unavailable and explicitly incomplete. No literature support, scientific status or prior action is newly certified here.",
        "source": source,
        "targets": targets,
        "scope": {
            "description": f"Exact PR{config['pr']} provenance cohort; current bytes, historical local-input omissions and preservation of existing work only.",
            "selection": "Every original target in the frozen inventory, with explicitly configured current successor/supplemental observations; no sampling.",
            "coverage": "full",
            "population_size": len(targets),
            "reviewed_target_ids": ids,
            "exclusions": [
                {
                    "target": "Scientific literature support and record curation",
                    "reason": "Not reassessed here; originating review scopes remain distinct and unchanged.",
                },
                {
                    "target": "Lost historical scratch",
                    "reason": "Not read, recovered, reconstructed or newly certified.",
                },
            ],
        },
        "checks": [
            {
                "check_id": "provenance-accounting",
                "name": "Current artifact identities and retained scientific-work accounting",
                "status": "passed",
                "required": True,
                "command": audit["command"],
                "exit_code": 0,
                "summary": accounting,
                "target_ids": ids,
                "evidence_ids": [e["evidence_id"] for e in evidence],
                "scope_note": "Provenance only, not a rerun or scientific certification of originating validators. Later native inspection/candidate/save/CI outputs are generated metadata, not recursive inputs.",
            }
        ],
        "evidence": evidence,
        "assessments": assessments,
        "findings": [],
        "actions": [],
        "related_reviews": list(related.values()),
        "limitations": [
            "The historical maintained/context pins do not establish complete local input coverage. Omitted historical scratch is unavailable; evidence hashes remain historical attestations, not fresh reconstruction.",
            "Current source/check bytes are distinct from old scratch. Archive and raw-data pins do not imply every member was manually inspected or any analysis rerun. Actual access, partial-review and metadata-only limits remain in the frozen originating receipts.",
            "No new scientific review is performed here. Completed applies only to this bounded process audit; not_assessed is not a scientific passing verdict. Separate source/authority corrections retain their own restricted scope.",
            "No original review, canonical record, cache, history, schema, product or scientific status is rewritten. There are no findings, terminal dispositions, previous_occurrences or actions in this provenance observation, so it cannot retire or replace scientific work.",
            "The final native inspection output, candidate, and subsequent validation/save/CI receipts are generated metadata rather than recursively hashed inputs. Fresh inspection cannot recover omitted historical bytes.",
        ],
        "links": [
            f"https://github.com/{REPOSITORY}/pull/{config['pr']}",
            f"https://github.com/{REPOSITORY}/issues/{config['issue']}",
        ],
        "tags": [f"pr{config['pr']}", "provenance-only", "historical-input-limit"],
    }
    write_json(out, "candidate.json", candidate)
    print(candidate["review_id"])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", required=True)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("capture")
    second = commands.add_parser("build")
    second.add_argument("--inspection", required=True)
    second.add_argument("--review-id", required=True)
    args = parser.parse_args()
    config = read_json(args.config)
    if not isinstance(config["pr"], int) or config["pr"] <= 0:
        raise ValueError("PR must be a positive integer")
    out = Path(f".temp/pr{config['pr']}/batch-provenance")
    if args.command == "capture":
        capture(args, config, out)
    else:
        build(args, config, out)


if __name__ == "__main__":
    main()
