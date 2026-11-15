"""Require actual ambiguity canary proof while preserving batch146 science.

2026-11-15, #2848. Only the exact one-record status/candidate successor is
admitted. Historical Git bytes, biology, source quotations and ledger stay fixed.
"""

import copy
import subprocess

import yaml
from sulfobacillus_mapping_successor import artifact, digest, reviewed_input

from communitymech.curate.curation_event import record_curation_event
from scripts.record_review import render_markdown, validate_review

BASELINE = "68699871415fda3c9eebf20382a315f9f3c7b17a"
TARGET = "data/isolates/Faecalibacterium_Prausnitzii_A2_165_2FL_FOS_Monoculture_Baseline.yaml"
IDENTITY = "CommunityMech:000546"
MANIFEST = "reports/gtdb-ambiguity-20261115/ambiguity-successors-001.json"
LEDGER = "reports/causal_graph_review/decisions/20261110-stage2-seven-records-batch146.yaml"
SELECTOR = "taxonomy[0].taxon_term.gtdb_grounding_status; taxonomy[0].taxon_term.gtdb_candidates"
OPTIONS = [
    "GTDB:s__Faecalibacterium_longum",
    "GTDB:s__Faecalibacterium_prausnitzii",
    "GTDB:s__Faecalibacterium_prausnitzii_D",
]


def unchanged_science(before, after):
    assert before["id"] == after["id"] == IDENTITY
    assert len(before["taxonomy"]) == len(after["taxonomy"]) == 1
    assert before["taxonomy"][0]["taxon_term"]["gtdb_grounding_status"] == "UNRESOLVED"
    assert "gtdb_classification" not in after["taxonomy"][0]["taxon_term"]
    expected = copy.deepcopy(before)
    expected["taxonomy"][0]["taxon_term"]["gtdb_grounding_status"] = "AMBIGUOUS"
    expected["taxonomy"][0]["taxon_term"]["gtdb_candidates"] = OPTIONS
    assert len(after["curation_history"]) == len(before["curation_history"]) + 1
    event = after["curation_history"][-1]
    record_curation_event(
        expected,
        curator="gtdb_ground.py",
        action="GTDB_SET_STATUS",
        changes="Wrote gtdb_grounding_status on 1 taxonomy entries (#294, #395).",
        timestamp=event["timestamp"],
    )
    assert expected == after, "all biology and the complete native event must remain exact"


def current_record_sha256(root, path, predecessor_hash, *, manifest=None, current=None):
    current = (root / path).read_bytes() if current is None else current
    if digest(current) == predecessor_hash:
        return predecessor_hash
    assert path == TARGET, "only the reviewed status successor may differ"
    manifest = yaml.safe_load((root / MANIFEST).read_bytes()) if manifest is None else manifest
    assert manifest["source_baseline"] == BASELINE
    assert len(manifest["records"]) == 1
    entry = manifest["records"][0]
    assert entry["target"] == path and entry["target_id"] == IDENTITY
    assert entry["scientific_review"] is False
    before_raw = subprocess.check_output(["git", "show", f"{BASELINE}:{path}"], cwd=root)
    assert digest(before_raw) == predecessor_hash == entry["before_sha256"]
    assert digest(current) == entry["after_sha256"]
    old_ledger = subprocess.check_output(["git", "show", f"{BASELINE}:{LEDGER}"], cwd=root)
    assert (root / LEDGER).read_bytes() == old_ledger
    before, after = yaml.safe_load(before_raw), yaml.safe_load(current)
    unchanged_science(before, after)
    review = yaml.safe_load(artifact(root, entry["diagnostic_review"]))
    validate_review(review)
    assert review["repository"] == "CultureBotAI/CommunityMech"
    assert review["completion"] == "completed" and review["scientific_review"] is False
    assert review["verdict"] == "pass_with_limitations" and review["scope"]["coverage"] == "partial"
    assert review["scope"]["reviewed_target_ids"] == [IDENTITY]
    assert len(review["targets"]) == 1
    target = review["targets"][0]
    assert (target["path"], target["target_id"], target["selector"]) == (path, IDENTITY, SELECTOR)
    reviewed_input(review, path, entry["after_sha256"])
    reviewed_input(review, LEDGER, digest(old_ledger))
    evidence = {row["evidence_id"]: row for row in review["evidence"]}
    assert any(
        row["area"] == "grounding"
        and row["outcome"] == "supported"
        and row["target_ids"] == [IDENTITY]
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
        "terms",
        "history",
        "new-history",
    }
    assert len(required) == 8 and all(
        row["status"] == "passed" and row["exit_code"] == 0 for row in required
    )
    binding = entry["application_receipt"]
    assert binding["sha256"] == binding["raw_sha256"]
    reviewed_input(review, binding["raw_path"], binding["raw_sha256"])
    applied = yaml.safe_load(artifact(root, binding))
    assert (
        applied["record"] == path
        and applied["record_id"] == IDENTITY
        and applied["applied"] is True
    )
    assert (
        applied["before_sha256"] == predecessor_hash
        and applied["after_sha256"] == entry["after_sha256"]
    )
    assert applied["execution_revision"] == review["source"]["git_revision"]
    # This actual receipt captured the canonical predecessor before replacement.
    # Bind those bytes through immutable Git and the separately saved before file,
    # never pretend that old hash is the present canonical state.
    before_path = binding["raw_path"].rsplit("/", 1)[0] + "/before.yaml"
    reviewed_input(review, before_path, predecessor_hash)
    for name, expected_hash in applied["inputs"].items():
        if name == path:
            assert expected_hash == predecessor_hash
        else:
            reviewed_input(review, name, expected_hash)
    sidecar = entry["history_sidecar"]
    reviewed_input(review, sidecar["path"], sidecar["sha256"])
    history = yaml.safe_load(artifact(root, sidecar))
    assert history["target"]["path"] == path and history["target"]["kind"] == "record"
    assert history["events"]
    binding = entry["native_recomputation"]
    assert binding["sha256"] == binding["raw_sha256"]
    reviewed_input(review, binding["raw_path"], binding["sha256"])
    route = yaml.safe_load(artifact(root, binding))
    assert route["execution_revision"] == applied["execution_revision"]
    assert route["target"] == path and route["record_sha256"] == entry["after_sha256"]
    assert route["descriptor"] == {"id": "NCBITaxon:853", "label": "Faecalibacterium prausnitzii"}
    assert route["status"] == "AMBIGUOUS" and route["candidates"] == OPTIONS
    assert route["matches_stored_state"] is True
    assert route["result"]["ambiguous"] is True and route["result"]["gtdb_options"] == OPTIONS
    assert route["result"]["n_alt"] == 3
    assert route["classifier_sha256"] == digest((root / "scripts/gtdb_ground.py").read_bytes())
    assert (
        route["crosswalk_sha256"]
        == "761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd"
    )
    reviewed_input(review, "scripts/gtdb_ground.py", route["classifier_sha256"])
    reviewed_input(
        review,
        ".temp/gtdb-ambiguity-20261115/kg-microbe/data/raw/NCBI2GTDB.tsv.gz",
        route["crosswalk_sha256"],
    )
    assert artifact(root, entry["review_markdown"]).decode() == render_markdown(review)
    return entry["after_sha256"]
