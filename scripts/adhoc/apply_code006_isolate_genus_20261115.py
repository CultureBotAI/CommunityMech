"""Apply one externally reviewed batch147 genus candidate, #2848, 2026-11-15.

Inputs: exact candidate/receipt hashes, selected original baseline and all
staged source inputs. Outputs: private actual receipt plus one native-validated
canonical replacement. Default is plan; --apply is required. No bulk writes.
"""

import argparse
import copy
import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

import yaml

from communitymech.curate.curation_event import record_curation_event
from communitymech.validation.write_validated import write_validated_community

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / ".temp/gtdb-code006-20261115"
STAGER = "scripts/adhoc/stage_code006_isolate_genus_20261115.py"
STAGER_SHA = "15574e36f3b0bd6f2c6b6b6293fb856ab863d7ef3297b7f649e62d1166b9a5e0"
PLAN = ".temp/gtdb-code006-20261115/genus-subset-plan-001.json"
PLAN_SHA = "1501b8ec1b52aaf7936c9da2a48f4ee208b9e22f4b7bac135dcf5856a4363ae2"
TABLE = ".temp/gtdb-code006-20261115/kg-microbe/data/raw/NCBI2GTDB.tsv.gz"
TABLE_SHA = "761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd"
STAGING_REVISION = "fe18c5d2e1d2d151440137270402d895e9f8418d"
TARGETS = {
    "data/isolates/Pelagerythrobacter_N7_Halophilic_Pyrene_Oxidation_Isolate_Baseline.yaml": (
        "CommunityMech:000552",
        "NCBITaxon:2800685",
        "Pelagerythrobacter",
        16,
        "16d14ed3792a286afedaa4f17ba1c1773ebb04c6a7e8fc622cb7d946ce4c9610",
    ),
    "data/isolates/Salinicola_A11_Halophilic_Bioemulsifier_Decarboxylase_Isolate_Baseline.yaml": (
        "CommunityMech:000553",
        "NCBITaxon:404432",
        "Salinicola",
        46,
        "82b65eee0a1216e8a26c875a17206c3060b2304223a3eac2fcb1171de79aee4b",
    ),
}


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def sha(path):
    return digest(path.read_bytes())


def head():
    return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()


def verify_inputs(receipt):
    required = {
        receipt["target"],
        STAGER,
        PLAN,
        TABLE,
        "scripts/gtdb_ground.py",
        "src/communitymech/curate/curation_event.py",
        "references_cache/PMID_42666409.txt",
    }
    if not required.issubset(receipt.get("inputs", {})):
        raise ValueError("all reviewed native/source inputs required")
    if (
        receipt["inputs"][STAGER] != STAGER_SHA
        or receipt["inputs"][PLAN] != PLAN_SHA
        or receipt["inputs"][TABLE] != TABLE_SHA
    ):
        raise ValueError("reviewed staging implementation or plan differs")
    for name, expected in receipt["inputs"].items():
        path = ROOT / name
        if Path(name).is_absolute() or path.is_symlink() or not path.resolve().is_relative_to(ROOT):
            raise ValueError("unsafe source input path")
        if sha(path) != expected:
            raise ValueError("reviewed input changed")


def checked(stage, candidate_sha, receipt_sha):
    receipt_bytes = (stage / "receipt.json").read_bytes()
    if digest(receipt_bytes) != receipt_sha:
        raise ValueError("external reviewed receipt hash differs")
    receipt = json.loads(receipt_bytes)
    target = receipt.get("target")
    if target not in TARGETS:
        raise ValueError("unreviewed target")
    identity, ncbi, label, count, baseline = TARGETS[target]
    original = (ROOT / target).read_bytes()
    candidate = (stage / Path(target).name).read_bytes()
    if (
        digest(candidate) != candidate_sha
        or digest(original) != baseline
        or receipt.get("candidate_sha256") != candidate_sha
        or receipt.get("record_id") != identity
        or receipt.get("code_revision") != STAGING_REVISION
        or receipt.get("canonical_apply") is not False
        or receipt.get("exit_codes") != [0, 0]
        or receipt.get("source_inputs_unchanged") is not True
        or receipt.get("inputs", {}).get(target) != baseline
    ):
        raise ValueError("exact reviewed candidate/baseline/receipt required")
    verify_inputs(receipt)
    before, after = yaml.safe_load(original), yaml.safe_load(candidate)
    expected = copy.deepcopy(before)
    if before["id"] != identity or len(before["taxonomy"]) != 1:
        raise ValueError("exact selected isolate required")
    term = expected["taxonomy"][0]["taxon_term"]
    if (
        term["term"] != {"id": ncbi, "label": label}
        or term["gtdb_grounding_status"] != "UNRESOLVED"
        or "gtdb_classification" in term
    ):
        raise ValueError("exact unchanged genus baseline required")
    block = receipt["native_block"]
    values = {
        "gtdb_id": "GTDB:g__" + label,
        "gtdb_taxon": label,
        "ncbi_source_id": ncbi,
        "support_genomes": count,
        "total_genomes": count,
        "majority_fraction": 1.0,
        "is_reclassified": False,
    }
    if any(block.get(name) != value for name, value in values.items()) or block.get("curated"):
        raise ValueError("exact same-genus source correspondence required")
    term["gtdb_classification"], term["gtdb_grounding_status"] = block, "GROUNDED"
    events = after.get("curation_history", [])[len(before.get("curation_history", [])) :]
    if len(events) != 2:
        raise ValueError("exactly two native events required")
    for event, action, changes in zip(
        events,
        ("GTDB_GROUND", "GTDB_SET_STATUS"),
        (
            "Added 1 gtdb_classification block(s) from NCBI2GTDB.tsv.gz (#395).",
            "Wrote gtdb_grounding_status on 1 taxonomy entries (#294, #395).",
        ),
        strict=True,
    ):
        actual = record_curation_event(
            expected,
            curator="gtdb_ground.py",
            action=action,
            changes=changes,
            timestamp=event.get("timestamp"),
        )
        if actual != event:
            raise ValueError("native inline event differs")
    if after != expected:
        raise ValueError("candidate exceeds exact mapping/status/native-history scope")
    return original, candidate, receipt_bytes, receipt, after


def apply(stage, output, candidate_sha, receipt_sha, expected_revision, *, do_apply=False):
    stage, output = Path(stage).resolve(), Path(output).resolve()
    if (
        not stage.is_relative_to(STATE.resolve())
        or not output.is_relative_to(STATE.resolve())
        or output.exists()
        or head() != expected_revision
    ):
        raise ValueError("exclusive private namespace and exact execution revision required")
    implementation = {
        path: sha(path)
        for path in (
            Path(__file__),
            ROOT / "src/communitymech/curate/curation_event.py",
            ROOT / "src/communitymech/validation/write_validated.py",
        )
    }
    original, candidate, receipt_bytes, receipt, after = checked(stage, candidate_sha, receipt_sha)
    if not do_apply:
        return {"planned": True, "target": receipt["target"], "candidate_sha256": candidate_sha}
    output.mkdir()
    (output / "before.yaml").write_bytes(original)
    write_validated_community(after, output / "validated.yaml")
    if yaml.safe_load((output / "validated.yaml").read_bytes()) != after:
        raise ValueError("native serialization differs")
    verify_inputs(receipt)
    target = ROOT / receipt["target"]
    if (
        head() != expected_revision
        or target.read_bytes() != original
        or (stage / target.name).read_bytes() != candidate
        or (stage / "receipt.json").read_bytes() != receipt_bytes
        or implementation != {path: sha(path) for path in implementation}
    ):
        raise ValueError("source/candidate/implementation changed during validation")
    (output / "replacement.yaml").write_bytes(candidate)
    (output / "replacement.yaml").replace(target)
    if target.read_bytes() != candidate:
        raise ValueError("actual persisted canonical bytes differ")
    result = {
        "applied": True,
        "target": receipt["target"],
        "record_id": receipt["record_id"],
        "execution_revision": expected_revision,
        "before_sha256": digest(original),
        "after_sha256": candidate_sha,
        "reviewed_receipt_sha256": receipt_sha,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "inputs": receipt["inputs"],
        "implementation": {
            str(path.relative_to(ROOT)): value for path, value in implementation.items()
        },
        "scope": receipt["scope"],
        "sidecar_status": "PENDING native scaffold and validation",
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
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    print(
        json.dumps(
            apply(
                args.stage,
                args.output,
                args.reviewed_candidate_sha256,
                args.reviewed_receipt_sha256,
                args.expected_revision,
                do_apply=args.apply,
            ),
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
