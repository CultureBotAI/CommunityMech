"""Admit only reviewed genus/status successors while retaining batch147 science.

#2848: unchanged records still require their exact old hashes. A changed selected
record needs an actual application, saved technical assessment and native proof;
all original biological content and old history remain protected.
"""

import copy
import hashlib
import subprocess
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from scripts.record_review import render_markdown, validate_review  # noqa: E402

BASELINE = "68699871415fda3c9eebf20382a315f9f3c7b17a"
PREFIX = "data/isolates/"
TARGETS = {
    PREFIX
    + "Pelagerythrobacter_N7_Halophilic_Pyrene_Oxidation_Isolate_Baseline.yaml": (
        "CommunityMech:000552",
        "NCBITaxon:2800685",
        "Pelagerythrobacter",
        16,
    ),
    PREFIX
    + "Salinicola_A11_Halophilic_Bioemulsifier_Decarboxylase_Isolate_Baseline.yaml": (
        "CommunityMech:000553",
        "NCBITaxon:404432",
        "Salinicola",
        46,
    ),
}
MANIFEST = "reports/gtdb-code006-20261115/batch147-genus-successors-001.json"
MANIFESTS = {
    path: (
        MANIFEST
        if values[0] == "CommunityMech:000552"
        else "reports/gtdb-code006-20261115/batch147-genus-successors-002.json"
    )
    for path, values in TARGETS.items()
}


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def artifact(root, item):
    path = Path(item["path"])
    assert not path.is_absolute() and ".." not in path.parts
    resolved = (root / path).resolve()
    assert resolved.is_relative_to(root.resolve())
    raw = resolved.read_bytes()
    assert digest(raw) == item["sha256"]
    return raw


def reviewed_input(review, path, expected):
    matches = [row for row in review["source"]["inputs"] if row["path"] == path]
    assert len(matches) == 1 and matches[0]["sha256"] == expected, path


def historical_bytes(root, path):
    if path in TARGETS:
        return subprocess.check_output(["git", "show", f"{BASELINE}:{path}"], cwd=root)
    return (root / path).read_bytes()


def unchanged_science(before, after, path):
    identity, ncbi, label, count = TARGETS[path]
    assert before["id"] == after["id"] == identity
    assert len(before["taxonomy"]) == len(after["taxonomy"]) == 1
    old_term, new_term = before["taxonomy"][0]["taxon_term"], after["taxonomy"][0]["taxon_term"]
    assert old_term["term"] == new_term["term"] == {"id": ncbi, "label": label}
    assert old_term["gtdb_grounding_status"] == "UNRESOLVED"
    assert "gtdb_classification" not in old_term
    assert new_term["gtdb_grounding_status"] == "GROUNDED"
    block = new_term["gtdb_classification"]
    assert block["gtdb_id"] == "GTDB:g__" + label
    assert block["gtdb_taxon"] == label and block["ncbi_source_id"] == ncbi
    assert block["total_genomes"] == block["support_genomes"] == count
    assert block["majority_fraction"] == 1.0 and block["is_reclassified"] is False
    assert not block.get("curated")
    previous = before.get("curation_history", [])
    assert after["curation_history"][: len(previous)] == previous
    events = after["curation_history"][len(previous) :]
    assert len(events) == 2
    assert [event["action"] for event in events] == ["GTDB_GROUND", "GTDB_SET_STATUS"]
    assert all(event["curator"] == "gtdb_ground.py" for event in events)
    old, new = copy.deepcopy(before), copy.deepcopy(after)
    for doc in (old, new):
        doc.pop("curation_history", None)
        term = doc["taxonomy"][0]["taxon_term"]
        term.pop("gtdb_classification", None)
        term.pop("gtdb_grounding_status")
    assert (
        old == new
    ), "all source, study strain/genome, graph and biological content must be unchanged"


def current_record_sha256(root, path, predecessor_hash, *, manifest=None, current=None):
    current = (root / path).read_bytes() if current is None else current
    actual = digest(current)
    if actual == predecessor_hash:
        return actual
    assert path in TARGETS, "no successor allowance for other batch147 records"
    manifest = (
        yaml.safe_load((root / MANIFESTS[path]).read_bytes()) if manifest is None else manifest
    )
    rows = [row for row in manifest["records"] if row["target"] == path]
    assert len(rows) == 1
    proof = rows[0]
    identity = TARGETS[path][0]
    assert proof["source_baseline"] == BASELINE and proof["target_id"] == identity
    assert proof["scientific_review"] is False
    original = historical_bytes(root, path)
    assert digest(original) == predecessor_hash == proof["before_sha256"]
    assert actual == proof["after_sha256"]
    unchanged_science(yaml.safe_load(original), yaml.safe_load(current), path)
    review = yaml.safe_load(artifact(root, proof["diagnostic_review"]))
    validate_review(review)
    assert review["repository"] == "CultureBotAI/CommunityMech"
    assert review["completion"] == "completed" and review["scientific_review"] is False
    assert review["verdict"] == "pass_with_limitations" and review["scope"]["coverage"] == "partial"
    assert review["scope"]["reviewed_target_ids"] == [identity] and len(review["targets"]) == 1
    target = review["targets"][0]
    assert (target["path"], target["target_id"], target["selector"]) == (
        path,
        identity,
        "taxonomy[0].taxon_term",
    )
    reviewed_input(review, path, actual)
    evidence = {row["evidence_id"]: row for row in review["evidence"]}
    assert any(
        row["area"] == "grounding"
        and row["outcome"] == "supported"
        and row["target_ids"] == [identity]
        and any(evidence[key]["kind"] == "database" for key in row["evidence_ids"])
        for row in review["assessments"]
    )
    required = [row for row in review["checks"] if row["required"]]
    assert {row["check_id"] for row in required} == {
        "schema",
        "strict",
        "gtdb",
        "domain",
        "scalars",
        "history",
        "completion",
        "terms",
    }
    assert all(row["status"] == "passed" and row["exit_code"] == 0 for row in required)
    application = proof["application_receipt"]
    assert application["sha256"] == application["raw_sha256"]
    reviewed_input(review, application["raw_path"], application["raw_sha256"])
    receipt = yaml.safe_load(artifact(root, application))
    assert receipt["target"] == path and receipt["applied"] is True
    assert receipt["before_sha256"] == predecessor_hash and receipt["after_sha256"] == actual
    assert receipt["execution_revision"] == review["source"]["git_revision"]
    for name, expected in receipt["inputs"].items():
        if name == path:
            # The actual receipt binds the pre-write canonical bytes; the saved
            # assessment binds the current target and its retained before copy.
            assert expected == predecessor_hash
            reviewed_input(review, proof["before_copy_path"], predecessor_hash)
        else:
            reviewed_input(review, name, expected)
    sidecar = proof["history_sidecar"]
    reviewed_input(review, sidecar["path"], sidecar["sha256"])
    history = yaml.safe_load(artifact(root, sidecar))
    assert history["target"]["kind"] == "record" and history["target"]["path"] == path
    assert history["events"]
    route = proof["native_recomputation"]
    reviewed_input(review, route["raw_path"], route["sha256"])
    result = yaml.safe_load(artifact(root, route))
    assert result["target"] == path and result["record_sha256"] == actual
    assert (
        result["revision"] == receipt["execution_revision"]
        and result["matches_corrected_block"] is True
    )
    block = yaml.safe_load(current)["taxonomy"][0]["taxon_term"]["gtdb_classification"]
    assert result["block"] == block
    reviewed_input(review, "scripts/gtdb_ground.py", result["classifier_sha256"])
    reviewed_input(review, result["crosswalk_path"], result["crosswalk_sha256"])
    assert (
        result["crosswalk_sha256"]
        == "761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd"
    )
    assert artifact(root, proof["review_markdown"]).decode() == render_markdown(review)
    return actual
