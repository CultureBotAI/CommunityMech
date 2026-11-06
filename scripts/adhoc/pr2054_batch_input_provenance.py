"""Build a JSON-only, process-scoped PR2054 input-provenance observation.

Capture immutable manifests before native inspection; build the candidate only
after inspection. This helper never writes canonical data or saved review pairs.
"""

import argparse
import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / ".temp/pr2054/batch-provenance"
REPO = "CultureBotAI/CommunityMech"
SELF = "scripts/adhoc/pr2054_batch_input_provenance.py"
INVENTORY = ".temp/pr2054/review-inventory.json"
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
    ".temp/pr2054/issues/local-input-provenance.md",
    ".temp/pr2054/adversarial/original-input-scope-pattern.json",
    ".temp/pr2054/adversarial/historical-input-audit.json",
]


def now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def local(name):
    path = ROOT / name
    if path.is_symlink() or not path.resolve().is_relative_to(ROOT):
        raise ValueError(f"Unsafe input: {name}")
    return path


def digest(name):
    return hashlib.sha256(local(name).read_bytes()).hexdigest()


def read_json(name):
    return json.loads(local(name).read_text())


def read_review(name):
    return yaml.safe_load(local(name).read_text())


def write_json(name, value):
    path = OUT / name
    if path.exists():
        raise FileExistsError(f"Refusing to overwrite frozen artifact: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n")
    return str(path.relative_to(ROOT))


def prepare_manifests():
    """Freeze current source/check containers without interpreting their science."""
    groups = [
        (
            "independent-secondary",
            ["CommunityMech:000202", "CommunityMech:000196", "CommunityMech:000206"],
            "independent-secondary-inputs.json",
        ),
        ("root-resources", ["CommunityMech:000258"], "root-resource-inputs.json"),
    ]
    for directory, targets, output in groups:
        files = []
        for path in sorted((ROOT / ".temp/pr2054" / directory).rglob("*")):
            if not path.is_file() or path.name.startswith("proposed-owner-mapping"):
                continue
            name = str(path.relative_to(ROOT))
            files.append({"path": name, "sha256": digest(name), "bytes": path.stat().st_size})
        write_json(
            output,
            {
                "at": now(),
                "targets": targets,
                "scope": "Current source/check artifact byte inventory only. Actual scientific inspection and access limits remain in the originating receipts. Archive hashes do not imply manual inspection of every member; failed routes remain diagnostic context. No historical scratch was recovered, and no public contact fields are copied into review prose.",
                "inputs": files,
            },
        )


def capture(args):
    inputs = set(RULES + [SELF, INVENTORY])
    manifest_targets = {}
    for name in args.manifest:
        manifest = read_json(name)
        inputs.add(name)
        for item in manifest["inputs"]:
            if digest(item["path"]) != item["sha256"]:
                raise ValueError(f"Changed manifest input: {item['path']}")
            inputs.add(item["path"])
        for target in manifest["targets"]:
            manifest_targets.setdefault(target, []).append(name)

    latest = read_review(args.latest_180)
    inputs.update([args.latest_180, str(Path(args.latest_180).with_name("review.md"))])
    for item in latest["source"]["inputs"]:
        if digest(item["path"]) != item["sha256"]:
            raise ValueError(f"Changed 180 successor input: {item['path']}")
        inputs.add(item["path"])

    records = []
    targets = []
    for entry in read_json(INVENTORY):
        original = read_review(entry["review"])
        path = entry["path"]
        target = next(t for t in original["targets"] if t["target_id"] == entry["target_id"])
        targets.append(target)
        inputs.update([path, entry["review"], str(Path(entry["review"]).with_name("review.md"))])
        pin = next(i for i in original["source"]["inputs"] if i["path"] == path)
        if digest(path) != pin["sha256"]:
            raise ValueError(f"Stale target: {path}")
        active = latest if entry["target_id"] == "CommunityMech:000180" else original
        original_keys = [f["issue_key"] for f in original["findings"]]
        if set(original_keys) != {f["issue_key"] for f in active["findings"]}:
            raise ValueError("Scientific finding lineage changed")
        if any(f["status"] != "open" for f in active["findings"]):
            raise ValueError("Unexpected terminal scientific finding")
        if not manifest_targets.get(entry["target_id"]):
            raise ValueError(f"No current artifact manifest for {entry['target_id']}")
        row = {
            "target_id": entry["target_id"],
            "path": path,
            "current_sha256": digest(path),
            "original_target_sha256": pin["sha256"],
            "original_review": entry["review"],
            "original_review_id": original["review_id"],
            "original_completion": original["completion"],
            "original_verdict": original["verdict"],
            "original_scientific_review": original["scientific_review"],
            "original_input_count": len(original["source"]["inputs"]),
            "original_scratch_input_count": sum(
                i["path"].startswith((".temp/", "/private/tmp/"))
                for i in original["source"]["inputs"]
            ),
            "retained_issue_keys": original_keys,
            "original_actions": original["actions"],
            "current_review_id": active["review_id"],
            "current_completion": active["completion"],
            "current_verdict": active["verdict"],
            "current_scientific_review": active["scientific_review"],
            "current_actions": active["actions"],
            "current_manifest_paths": manifest_targets[entry["target_id"]],
            "limitation": "Historical scratch was not recovered. Fresh artifacts are current provenance, not reconstructed historical bytes.",
        }
        name = write_json(f"records/{entry['target_id'].split(':')[1]}.json", row)
        inputs.add(name)
        row["manifest"] = name
        records.append(row)
    counts = {
        "records": len(records),
        "original_inputs": sum(r["original_input_count"] for r in records),
        "finding_keys": sum(len(r["retained_issue_keys"]) for r in records),
        "original_actions": sum(len(r["original_actions"]) for r in records),
        "original_acceptance_checks": sum(
            len(a["acceptance_checks"]) for r in records for a in r["original_actions"]
        ),
        "current_actions": sum(len(r["current_actions"]) for r in records),
        "current_acceptance_checks": sum(
            len(a["acceptance_checks"]) for r in records for a in r["current_actions"]
        ),
    }
    assert counts["records"] == 10 and counts["finding_keys"] == 37
    assert counts["original_actions"] == counts["current_actions"] == 47
    assert counts["original_acceptance_checks"] == counts["current_acceptance_checks"] == 145
    audit = {
        "started_at": now(),
        "capture_head": subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip(),
        "counts": counts,
        "records": records,
        "latest_180_path": args.latest_180,
        "latest_180_review_id": latest["review_id"],
        "command": "python " + SELF + " capture " + " ".join(args.capture_arguments),
        "scope": "Byte provenance and retained scientific-work accounting only; no literature reassessment, old scratch recovery, or scientific disposition.",
    }
    inputs.add(write_json("audit.json", audit))
    inputs.add(write_json("targets.json", {"targets": targets}))
    manifest = [{"path": name, "sha256": digest(name)} for name in sorted(inputs)]
    write_json("inputs.json", {"inputs": manifest})
    print(json.dumps(counts))


def build(args):
    audit = read_json(".temp/pr2054/batch-provenance/audit.json")
    manifest = read_json(".temp/pr2054/batch-provenance/inputs.json")
    inspected = read_json(args.inspection)
    source = inspected.get("source", inspected)
    for item in manifest["inputs"]:
        if digest(item["path"]) != item["sha256"]:
            raise ValueError(f"Changed captured input: {item['path']}")
    expected = {i["path"] for i in manifest["inputs"]} | {
        ".temp/pr2054/batch-provenance/inputs.json"
    }
    if {i["path"] for i in source["inputs"]} != expected:
        raise ValueError("Native inspection must pin the complete exact input set")
    targets = read_json(".temp/pr2054/batch-provenance/targets.json")["targets"]
    ids = [t["target_id"] for t in targets]
    evidence = []
    assessments = []
    related = []
    for row in audit["records"]:
        rid = row["target_id"].split(":")[1]
        eid = "provenance-" + rid
        evidence.append(
            {
                "evidence_id": eid,
                "kind": "validation",
                "reference": row["manifest"],
                "locator": "Entire per-record provenance manifest; original/current record digests, retained review status, exact issue keys/actions and concrete current-input manifest paths.",
                "accessed_at": now(),
                "support": "supports",
                "snapshot_sha256": digest(row["manifest"]),
                "summary": f"The current target equals its original frozen target hash. {len(row['retained_issue_keys'])} unresolved scientific findings remain; this observation makes no scientific disposition.",
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
                "summary": f"Original {row['original_completion']}/{row['original_verdict']} review {row['original_review_id']} declared {row['original_input_count']} maintained/context input pins and no historical scratch inputs. Its current target digest is {row['current_sha256']}. Current scientific accounting remains {row['current_completion']}/{row['current_verdict']} in {row['current_review_id']}.",
                "details": "The historical input set is not exhaustive: evidence-level historical digests do not replace omitted native source.inputs. Current manifest-listed primary, supplementary, authority and check bytes are individually frozen here. This audits their provenance, not their scientific content. Archive pins identify containers, not manual review of every asset. Original findings/actions remain visible; the separate 180 successor retains the S1 correction. No omitted historical file is claimed recovered or reconstructed.",
            }
        )
        related.append(
            {
                "repository": REPO,
                "review_id": row["original_review_id"],
                "relationship": "Bounded append-only historical input-provenance limitation; no scientific finding or action supersession.",
            }
        )
    related.append(
        {
            "repository": REPO,
            "review_id": audit["latest_180_review_id"],
            "relationship": "Current 180 provenance/S1 correction retained unchanged; no scientific occurrence superseded by this batch.",
        }
    )
    candidate = {
        "schema_version": "1.0.0",
        "review_id": args.review_id,
        "kind": "batch",
        "repository": REPO,
        "title": "PR2054 bounded current-input provenance and historical scratch limitation",
        "started_at": audit["started_at"],
        "finished_at": now(),
        "reviewer": {
            "identity": "Codex /root/batch2035_434_refresh",
            "kind": "agent",
            "independence": "self_review",
            "independence_basis": "Author of this process observation; independently produced scientific receipts from other passes retain their stated authorship and limits. This candidate requires a separate read-only review.",
        },
        "skill": "review-communities",
        "completion": "completed",
        "verdict": "not_assessed",
        "scientific_review": False,
        "summary": "Completed only the bounded ten-record provenance accounting. All 37 unresolved finding keys, 47 actions and 145 original acceptance checks remain historical scientific work; the separate 180 successor retains its explicit S1 correction. Current fresh source/check files are frozen individually, while the ten October reviews' missing historical scratch input sets remain unavailable to this audit and explicitly incomplete. This observation neither certifies literature support nor promotes any scientific status.",
        "source": source,
        "targets": targets,
        "scope": {
            "description": "Exact PR2054 ten-record provenance cohort; current byte identities, historical local-input omissions and preservation of unresolved work only.",
            "selection": "All ten original review targets in the frozen PR2054 inventory; no sampling and no other PRs.",
            "coverage": "full",
            "population_size": 10,
            "reviewed_target_ids": ids,
            "exclusions": [
                {
                    "target": "Scientific literature support and record curation",
                    "reason": "Not reassessed in this process-only observation; original and separate successor scientific scopes persist.",
                },
                {
                    "target": "Lost historical scratch files",
                    "reason": "Not read, recovered, reconstructed or newly certified.",
                },
            ],
        },
        "checks": [
            {
                "check_id": "provenance-accounting",
                "name": "Current artifact identity and retained scientific-work accounting",
                "status": "passed",
                "required": True,
                "command": audit["command"],
                "exit_code": 0,
                "summary": "Capture completed with exact target matches and 37 continuing open keys; 47 original/current actions and 145 original acceptance checks are preserved in frozen manifests.",
                "target_ids": ids,
                "evidence_ids": [e["evidence_id"] for e in evidence],
                "scope_note": "A provenance check, not a rerun or certification of scientific validators. Subsequent native validation/save receipts are generated metadata, not recursive inputs.",
            }
        ],
        "evidence": evidence,
        "assessments": assessments,
        "findings": [],
        "actions": [],
        "related_reviews": related,
        "limitations": [
            "Historical maintained/context pins do not establish complete source.inputs coverage; the omitted historical scratch bytes are unavailable. Retained evidence hashes remain historical attestations, not fresh reconstruction.",
            "Fresh current sources/check outputs are distinct from historical scratch. Pinning a retrieved archive does not claim every member was manually inspected; source access, partial-review and metadata-only limits remain those of each frozen originating receipt.",
            "No new scientific review was performed here. Completed denotes only this bounded process audit; not_assessed is not a scientific passing verdict. All prior findings/actions and the separate 180 S1 correction remain unaffected.",
            "No original review, canonical record, cache, history, schema, product or scientific status is rewritten. No terminal finding or previous_occurrences is emitted; empty findings/actions applies only to this provenance observation.",
            "The final native inspection output, candidate and later validation/save/CI receipts are generated metadata and are not recursively hashed as their own inputs. Missing historical scratch cannot be repaired by a fresh inspection.",
        ],
        "links": [
            "https://github.com/CultureBotAI/CommunityMech/pull/2054",
            "https://github.com/CultureBotAI/CommunityMech/issues/2566",
        ],
        "tags": ["pr2054", "provenance-only", "historical-input-limit"],
    }
    write_json("candidate.json", candidate)
    print(candidate["review_id"])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("prepare-manifests")
    first = commands.add_parser("capture")
    first.add_argument("--manifest", action="append", required=True)
    first.add_argument("--latest-180", required=True)
    second = commands.add_parser("build")
    second.add_argument("--inspection", required=True)
    second.add_argument("--review-id", required=True)
    args = parser.parse_args()
    if args.command == "prepare-manifests":
        prepare_manifests()
    elif args.command == "capture":
        import sys

        args.capture_arguments = sys.argv[2:]
        capture(args)
    else:
        build(args)


if __name__ == "__main__":
    main()
