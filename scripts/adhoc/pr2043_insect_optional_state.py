"""Append-only correction of the required-state premise in three PR 2043 reviews."""

from __future__ import annotations

import argparse
import copy
import json

import yaml
from pr2043_insect_audit import RECORDS, ROOT, SCRATCH, now, run, sha, write

PREDECESSORS = {
    "000006": "20261106T061435Z-pr2043-spittlebug-successor",
    "000007": "20261106T061437Z-pr2043-sharpshooter-successor",
    "000008": "20261106T061438Z-pr2043-cicada-successor",
}


def inspect(key):
    previous = ROOT / "reviews/structured" / PREDECESSORS[key] / "review.yaml"
    doc = yaml.safe_load(previous.read_text())
    folder = SCRATCH / key / "optional-state-correction"
    for entry in doc["source"]["inputs"]:
        assert sha((ROOT / entry["path"]).read_bytes()) == entry["sha256"], entry["path"]
    manifest = write(folder / "targets.json", {"targets": doc["targets"]})
    paths = {x["path"] for x in doc["source"]["inputs"] if x["role"] != "target"}
    paths.update(
        [
            str(previous.relative_to(ROOT)),
            str(previous.with_name("review.md").relative_to(ROOT)),
            "scripts/adhoc/pr2043_insect_optional_state.py",
            ".temp/pr2043/staleness.json",
        ]
    )
    args = [
        "uv",
        "run",
        "python",
        "scripts/record_review.py",
        "inspect",
        "--targets",
        str(manifest),
    ]
    for path in sorted(paths):
        args += ["--input", path]
    result = run(folder, "inspect", args)
    assert result.returncode == 0, result.stderr.decode()
    write(folder / "inspection.json", json.loads(result.stdout))


def build(key):
    folder = SCRATCH / key / "optional-state-correction"
    old = yaml.safe_load(
        (ROOT / "reviews/structured" / PREDECESSORS[key] / "review.yaml").read_text()
    )
    inspected = json.loads((folder / "inspection.json").read_text())
    for entry in inspected["source"]["inputs"]:
        assert sha((ROOT / entry["path"]).read_bytes()) == entry["sha256"], entry["path"]
    schema = yaml.safe_load((ROOT / "src/communitymech/schema/communitymech.yaml").read_text())
    state = schema["classes"]["MicrobialCommunity"]["attributes"]["ecological_state"]
    assert state.get("required") is not True
    assert state["range"] == "EcologicalStateEnum"
    doc = copy.deepcopy(old)
    stamp = now()
    insect = {"000006": "spittlebug", "000007": "sharpshooter", "000008": "cicada"}[key]
    doc.update(
        review_id=stamp[:19].replace("-", "").replace(":", "")
        + f"Z-pr2043-{insect}-optional-state-correction",
        title=f"{insect.capitalize()} review correction: optional ecological state",
        started_at=json.loads((folder / "inspect.json").read_text())["started_at"],
        finished_at=stamp,
        source=inspected["source"],
        targets=inspected["targets"],
    )
    doc[
        "summary"
    ] += " This linked observation corrects an inherited review-action premise: ecological_state is optional, so separately authorized curation may omit unsupported STABLE without a schema change. All five open scientific/provenance findings remain."
    doc["reviewer"][
        "independence_basis"
    ] = "Author correction after a separate independent reviewer identified an incorrect required-field premise in the saved remediation action. This observation preserves the author's freshly inspected scientific evidence; it does not claim independent approval."
    doc["scope"][
        "selection"
    ] += " This immediate append-only correction rechecks current schema optionality and preserved source pins; source access times remain those of the original fresh retrievals."
    evidence_id = "optional-state-contract"
    doc["evidence"].append(
        {
            "evidence_id": evidence_id,
            "kind": "authority",
            "reference": "src/communitymech/schema/communitymech.yaml",
            "locator": "classes.MicrobialCommunity.attributes.ecological_state and enums.EcologicalStateEnum",
            "summary": "The ecological_state attribute declares a range and no required constraint; unsupported STABLE can be omitted. This corrects repair-ecological-equilibrium.acceptance_checks[2] in the immediately preceding PR 2043 observation and the original October review, which incorrectly called it required.",
            "support": "refutes",
            "accessed_at": stamp,
            "snapshot_sha256": sha(
                (ROOT / "src/communitymech/schema/communitymech.yaml").read_bytes()
            ),
        }
    )
    doc["assessments"].append(
        {
            "assessment_id": "optional-state-remediation",
            "area": "schema",
            "topic": "Correction of the review's required-state premise",
            "outcome": "supported",
            "summary": "Omission is a schema-valid curation option for unsupported ecological STABLE; no schema follow-up is needed merely to express this absence.",
            "details": "The prior action's required-enum premise is retracted. Retain NATURAL biological origin and the qualified model graph; do not substitute ENGINEERED or TRANSIENT without evidence. All five findings were reassessed in the immediately preceding fresh source review and remain open with full lineage. This observation changes only remediation guidance, not canonical content or earlier review bytes.",
            "target_ids": [RECORDS[key]["target_id"]],
            "evidence_ids": [evidence_id, "schema", "methods", "record"],
        }
    )
    for a in doc["actions"]:
        if a["action_id"] == "repair-ecological-equilibrium":
            a["acceptance_checks"] = [
                "During separately authorized curation, omit ecological_state if no ecological evidence supports a specific state, or retain STABLE only with direct evidence of ecological equilibrium; metabolic steady-state optimization alone is insufficient.",
                "Retain community_origin NATURAL for the modeled biological association. Do not automatically substitute ENGINEERED or TRANSIENT merely because a computational model was constructed.",
                "The current schema makes ecological_state optional. Validate the record after omission; no schema change is needed merely to remove an unsupported value.",
                "Preserve the qualified interaction graph and append ordinary curation history without rewriting existing provenance.",
            ]
    for f in doc["findings"]:
        f["previous_occurrences"] = [
            {
                "repository": doc["repository"],
                "review_id": old["review_id"],
                "finding_id": f["finding_id"],
            }
        ]
    doc["notes"].append(
        "Explicit append-only correction: the original October review and the immediately preceding successor incorrectly called ecological_state required in repair-ecological-equilibrium.acceptance_checks[2]. This successor replaces that instruction with omission or evidence-supported state, preserves NATURAL, and retains all five finding heads with exact lineage."
    )
    doc["tags"].append("optional-state-correction")
    candidate = write(folder / "candidate.json", doc)
    result = run(
        folder,
        "native-validate",
        ["uv", "run", "python", "scripts/record_review.py", "validate", str(candidate)],
    )
    assert result.returncode == 0, result.stdout.decode() + result.stderr.decode()
    print(json.dumps({"review_id": doc["review_id"], "candidate": str(candidate)}))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=["inspect", "build"])
    parser.add_argument("record", choices=list(PREDECESSORS))
    args = parser.parse_args()
    (inspect if args.mode == "inspect" else build)(args.record)
