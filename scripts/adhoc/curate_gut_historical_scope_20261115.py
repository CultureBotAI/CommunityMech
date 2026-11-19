"""Stage/apply the bounded gut discussion correction for #2831, 2026-11-15.

Inputs: exact accepted 000122 baseline, prior scientific review/application,
unchanged retained sources and current native schema. Outputs: exclusive private
candidate/diff/receipt; explicit reviewed dual hashes authorize native-validated
canonical replacement. Original saved reviews and history remain untouched.
"""

import argparse
import copy
import difflib
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts/adhoc"))
from curate_gut_record_20261115 import load, replace  # noqa: E402

from communitymech.curate.curation_event import record_curation_event  # noqa: E402
from communitymech.validation.write_validated import write_validated_community  # noqa: E402

STATE = ROOT / ".temp/phase2-gut-20261115"
TARGET = "kb/communities/LBNL_Human_Gut_Interaction_SynCom.yaml"
BASELINE = "d0beaaa1d74383d9b6c81fafe5a70cae23eae00ae706f38fa10d78f874504dce"
PREVIOUS = "reviews/structured/20261115T025440Z-phase2-gut-completion"
PRIMARY = "9148ad1c34d3e0527d86bbd7d70c83792306c502deadde5c353c525ece318e08"
OLD_SCOPE = (
    "Canonical NCBITaxon:2 is only an aggregate placeholder for the 12-species experimental roster; "
    "#1548 tracks its grounding and non-graph metadata. No original figure pixels, separate supplements, "
    "raw data or executable model reproduction was performed."
)
NEW_SCOPE = (
    "At the October 6, 2026 review checkpoint, the record still used one aggregate bacterial entry "
    "instead of the experimental twelve-stock roster; #1548 tracked that historical grounding and "
    "non-graph metadata gap. That review had not inspected original figure pixels or separate supplements, "
    "and had not reanalysed raw data or reproduced the executable model. The November 15 reassessment "
    "subsequently grounded the twelve Methods stocks and inspected the complete article text/captions, "
    "Figure 4B/C pixels, Appendix and EV1-EV4. Raw-data reanalysis, all supplemental figure pixels and "
    "executable model reproduction remain outside the reassessment's scope."
)
OLD_FOLLOWUP = (
    "The previous October discussion records its historical review scope and remains unchanged."
)
NEW_FOLLOWUP = (
    "The October discussion is now explicitly scoped to its historical checkpoint; its original wording "
    "is preserved in the prior Git and review artifacts."
)
SUMMARY = (
    "Clarified that the October discussion's aggregate roster and uninspected-figure/supplement limits "
    "describe its historical checkpoint, not the current twelve-stock record. Retained the model-bounded "
    "interaction, acetate and unresolved mechanism/stock-grounding limits; distinguished the November "
    "source inspection from unperformed raw-data/model reanalysis. No taxonomy, evidence quotation, "
    "protocol or graph assertion changed. Addresses #2831."
)


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def revised(before):
    after = copy.deepcopy(before)
    for index, identifier, old, new in (
        (0, "lbnl_gut_effective_interactions_and_molecular_mechanisms", OLD_SCOPE, NEW_SCOPE),
        (1, "gut_roster_protocol_reassessment_20261115", OLD_FOLLOWUP, NEW_FOLLOWUP),
    ):
        discussion = after["discussions"][index]
        if discussion["discussion_id"] != identifier or discussion["rationale"].count(old) != 1:
            raise ValueError("historical discussion baseline differs")
        discussion["rationale"] = discussion["rationale"].replace(old, new)
    return after


def verify_inputs(receipt):
    if not receipt.get("inputs"):
        raise ValueError("empty reviewed input manifest")
    for name, expected in receipt["inputs"].items():
        path = ROOT / name
        if Path(name).is_absolute() or path.is_symlink() or not path.resolve().is_relative_to(ROOT):
            raise ValueError("unsafe reviewed input")
        if digest(path.read_bytes()) != expected:
            raise ValueError("reviewed input changed")


def checked_stage(original, stage, candidate_sha, receipt_sha):
    candidate = (stage / "candidate.yaml").read_bytes()
    raw_receipt = (stage / "receipt.json").read_bytes()
    if (
        not candidate_sha
        or not receipt_sha
        or (digest(candidate) != candidate_sha or digest(raw_receipt) != receipt_sha)
    ):
        raise ValueError("externally reviewed candidate/receipt differs")
    receipt = json.loads(raw_receipt)
    if (
        receipt.get("applied") is not False
        or receipt.get("target") != TARGET
        or receipt.get("before_sha256") != BASELINE
        or digest(original) != BASELINE
        or receipt.get("after_sha256") != digest(candidate)
    ):
        raise ValueError("reviewed target/baseline differs")
    verify_inputs(receipt)
    before, after = load(original), load(candidate)
    expected = revised(before)
    event = receipt["event"]
    if (
        event.get("curator") != "codex"
        or event.get("action") != "EDIT"
        or event.get("changes") != SUMMARY
    ):
        raise ValueError("reviewed curation event differs")
    expected["curation_history"].append(event)
    if after != expected or after["id"] != "CommunityMech:000122":
        raise ValueError("change exceeds the reviewed discussion/history scope")
    return candidate, after, receipt


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--apply-staged", type=Path)
    parser.add_argument("--reviewed-candidate-sha256")
    parser.add_argument("--reviewed-receipt-sha256")
    args = parser.parse_args()
    output = args.output.resolve()
    if output.exists() or not output.is_relative_to(STATE):
        raise ValueError("exclusive private output required")
    original = (ROOT / TARGET).read_bytes()
    if digest(original) != BASELINE:
        raise ValueError("accepted canonical baseline changed")
    if args.apply_staged:
        stage = args.apply_staged.resolve()
        if args.apply_staged.is_symlink() or not stage.is_relative_to(STATE):
            raise ValueError("unsafe staged directory")
        candidate, after, receipt = checked_stage(
            original, stage, args.reviewed_candidate_sha256, args.reviewed_receipt_sha256
        )
    else:
        before = load(original)
        if before["id"] != "CommunityMech:000122":
            raise ValueError("wrong canonical identity")
        after = revised(before)
        text = replace(original.decode(), "discussions", after["discussions"])
        if load(text) != after:
            raise ValueError("bounded discussion serialization differs")
        event = record_curation_event(
            after, curator="codex", action="EDIT", changes=SUMMARY, llm_assisted=True
        )
        text = (
            text.rstrip()
            + "\n"
            + yaml.safe_dump([event], sort_keys=False, allow_unicode=True, width=108)
        )
        candidate = text.encode()
        if load(candidate) != after:
            raise ValueError("append-only history serialization differs")
        primary = STATE / "primary-001/article.xml"
        if digest(primary.read_bytes()) != PRIMARY:
            raise ValueError("retained primary source differs")
        paths = [
            primary,
            STATE / "primary-001/figure4.png",
            STATE / "applied-001/receipt.json",
            ROOT / PREVIOUS / "review.yaml",
            ROOT / PREVIOUS / "review.md",
            ROOT / "src/communitymech/schema/communitymech.yaml",
            ROOT / "src/communitymech/schema/mech_shared.yaml",
            ROOT / "uv.lock",
            Path(__file__),
            ROOT / "scripts/adhoc/curate_gut_record_20261115.py",
        ]
        paths.extend((ROOT / "history/records/LBNL_Human_Gut_Interaction_SynCom").glob("*.yaml"))
        paths.extend(
            path
            for path in STATE.glob("publisher-supplement-*/*")
            if path.suffix in {".pdf", ".xlsx", ".zip"}
        )
        receipt = {
            "target": TARGET,
            "before_sha256": BASELINE,
            "after_sha256": digest(candidate),
            "event": event,
            "inputs": {
                str(path.relative_to(ROOT)): digest(path.read_bytes()) for path in sorted(paths)
            },
        }
    output.mkdir()
    write_validated_community(after, output / "validated.yaml")
    if load((output / "validated.yaml").read_bytes()) != after:
        raise ValueError("native serialization differs")
    verify_inputs(receipt)
    if (ROOT / TARGET).read_bytes() != original:
        raise ValueError("concurrent canonical modification")
    (output / "before.yaml").write_bytes(original)
    (output / "candidate.yaml").write_bytes(candidate)
    (output / "diff.patch").write_text(
        "".join(
            difflib.unified_diff(
                original.decode().splitlines(True),
                candidate.decode().splitlines(True),
                fromfile=TARGET,
                tofile=TARGET,
            )
        )
    )
    if args.apply_staged:
        (output / "replacement.yaml").write_bytes(candidate)
        (output / "replacement.yaml").replace(ROOT / TARGET)
        if (ROOT / TARGET).read_bytes() != candidate:
            raise ValueError("persisted canonical bytes differ")
        receipt["reviewed_candidate_sha256"] = args.reviewed_candidate_sha256
        receipt["reviewed_receipt_sha256"] = args.reviewed_receipt_sha256
    receipt.update(
        created_at=datetime.now(timezone.utc).isoformat(), applied=bool(args.apply_staged)
    )
    (output / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps(receipt, indent=2))


if __name__ == "__main__":
    main()
