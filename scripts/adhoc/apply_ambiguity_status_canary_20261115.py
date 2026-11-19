"""Apply one exact reviewed native ambiguity candidate for #2848, 2026-11-15.

Inputs: explicit candidate/receipt hashes, unchanged sources and frozen revision.
Outputs: exclusive private validated artifact and actual apply receipt; --apply
replaces only the named canonical record after validation and final input checks.
No fetching, chosen species, ledger rewrite, or wider scientific approval.
"""

import argparse
import copy
import hashlib
import importlib.util
import json
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

import yaml

from communitymech.curate.curation_event import record_curation_event
from communitymech.validation.write_validated import write_validated_community

ROOT = Path(__file__).resolve().parents[2]
STATE = Path(".temp/gtdb-ambiguity-20261115")
STAGER = Path(__file__).with_name("stage_ambiguity_status_canary_20261115.py")
STAGER_SHA = "3971c367bc04db09aa378a15a227cb6ecf0aeb7139f5011de215eeca32b0524e"
SPEC = importlib.util.spec_from_file_location("reviewed_ambiguity_stage", STAGER)
stage = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(stage)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def head():
    return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()


def verify_candidate(before, after, proof):
    stage.verify_semantics(before, after)
    event = after["curation_history"][-1]
    if not re.fullmatch(r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ", event.get("timestamp", "")):
        raise ValueError("native UTC event timestamp required")
    rebuilt = copy.deepcopy(after)
    rebuilt["curation_history"] = copy.deepcopy(before["curation_history"])
    expected_event = record_curation_event(
        rebuilt,
        curator="gtdb_ground.py",
        action="GTDB_SET_STATUS",
        changes="Wrote gtdb_grounding_status on 1 taxonomy entries (#294, #395).",
        timestamp=event["timestamp"],
    )
    if rebuilt != after or expected_event != proof["appended_native_inline_history"]:
        raise ValueError("full native event does not reconstruct")


def execute(candidate, candidate_sha, receipt_sha, output, revision, *, apply=False):
    candidate, output = Path(candidate).resolve(), Path(output).resolve()
    private = (ROOT / STATE).resolve()
    if not candidate.is_relative_to(private) or not output.is_relative_to(private):
        raise ValueError("private canary paths required")
    if output.exists() or output.is_symlink() or candidate.name != Path(stage.RECORD).name:
        raise ValueError("new output and exact original candidate basename required")
    if not re.fullmatch(r"[0-9a-f]{40}", revision) or head() != revision:
        raise ValueError("exact execution revision required")
    canonical = ROOT / stage.RECORD
    original, staged = canonical.read_bytes(), candidate.read_bytes()
    proof_path = candidate.with_name("receipt.json")
    proof_raw = proof_path.read_bytes()
    if (
        sha(original) != stage.BEFORE
        or sha(staged) != candidate_sha
        or sha(proof_raw) != receipt_sha
    ):
        raise ValueError("reviewed original/candidate/receipt hashes required")
    proof = json.loads(proof_raw)
    if (
        proof["record"] != stage.RECORD
        or proof["record_id"] != "CommunityMech:000546"
        or proof["candidate_sha256"] != candidate_sha
        or proof["canonical_apply"] is not False
        or proof["native_exit_code"] != 0
        or proof["execution_revision"] != revision
        or proof["source_inputs_unchanged"] is not True
    ):
        raise ValueError("successful exact native staging receipt required")
    captures = {candidate: staged, proof_path: proof_raw, canonical: original}
    for relative, digest in proof["inputs"].items():
        path = (ROOT / relative).resolve()
        if not path.is_relative_to(ROOT):
            raise ValueError("source input outside checkout")
        raw = path.read_bytes()
        if sha(raw) != digest:
            raise ValueError("reviewed source changed: " + relative)
        captures[path] = raw
    if sha(captures[STAGER]) != STAGER_SHA:
        raise ValueError("accepted stager changed")
    for name in ("native.log", "native.exit", "candidate.diff"):
        path = candidate.with_name(name)
        if path not in captures:
            captures[path] = path.read_bytes()
        key = {
            "native.log": "native_log_sha256",
            "native.exit": "native_exit_sha256",
            "candidate.diff": "diff_sha256",
        }[name]
        if sha(captures[path]) != proof[key]:
            raise ValueError("native staging artifacts changed")
    if captures[candidate.with_name("native.exit")] != b"0\n":
        raise ValueError("native stage did not pass")
    for path in (
        Path(__file__),
        STAGER,
        ROOT / "src/communitymech/validation/write_validated.py",
        ROOT / "src/communitymech/schema/communitymech.yaml",
        ROOT / "src/communitymech/curate/curation_event.py",
    ):
        if path not in captures:
            captures[path] = path.read_bytes()
    before, after = yaml.safe_load(original), yaml.safe_load(staged)
    verify_candidate(before, after, proof)

    def unchanged():
        if head() != revision or any(path.read_bytes() != raw for path, raw in captures.items()):
            raise ValueError("reviewed input changed during native validation")

    unchanged()
    output.mkdir(parents=True)
    write_validated_community(after, output / "validated.yaml")
    if yaml.safe_load((output / "validated.yaml").read_bytes()) != after:
        raise ValueError("native validated artifact changed candidate semantics")
    unchanged()
    (output / "before.yaml").write_bytes(original)
    (output / "candidate.yaml").write_bytes(staged)
    if apply:
        unchanged()
        canonical.write_bytes(staged)
        if canonical.read_bytes() != staged:
            raise ValueError("canonical persistence mismatch")
    result = {
        "record": stage.RECORD,
        "record_id": "CommunityMech:000546",
        "execution_revision": revision,
        "applied": apply,
        "before_sha256": sha(original),
        "after_sha256": sha(staged),
        "candidate_path": str(candidate.relative_to(ROOT)),
        "staging_receipt_sha256": receipt_sha,
        "completed_at": datetime.now(timezone.utc).isoformat(),
        "inputs": {str(path.relative_to(ROOT)): sha(raw) for path, raw in captures.items()},
        "validated_sha256": sha((output / "validated.yaml").read_bytes()),
        "scope": "Complete species-descriptor candidate list only; no GTDB species assigned to A2-165/JCM31915. Historical scientific ledger unchanged. Separate native sidecar/gates/saved assessment required.",
    }
    with (output / "receipt.json").open("x") as stream:
        json.dump(result, stream, indent=2)
        stream.write("\n")
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--candidate", type=Path, required=True)
    parser.add_argument("--candidate-sha256", required=True)
    parser.add_argument("--receipt-sha256", required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--expected-revision", required=True)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    result = execute(
        args.candidate,
        args.candidate_sha256,
        args.receipt_sha256,
        args.output,
        args.expected_revision,
        apply=args.apply,
    )
    print(
        json.dumps(
            {key: result[key] for key in ("record", "applied", "before_sha256", "after_sha256")},
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
