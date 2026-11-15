"""Admit only the actual reviewed JMP134 species successor, #2848, 2026-11-15.

The shared caller remains genus-lane owned. Unknown changed records have no
allowance; original686 biology and every unaffected historical hash stay intact.
"""

import copy
import hashlib
import json
import subprocess
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from scripts.record_review import render_markdown, validate_review  # noqa: E402

BASELINE = "68699871415fda3c9eebf20382a315f9f3c7b17a"
TARGET = "data/isolates/Cupriavidus_Necator_JMP134_24DBP_Hydroxylase_Isolate_Baseline.yaml"
TARGETS = {TARGET}
IDENTITY = "CommunityMech:000555"
BEFORE = "429964cbf945c41b2e89b57a072718158cf674e03786ef34b1ef96fe9247995e"
AFTER = "fede5211f0911d1a0543f1e19f8c53bf4c6dfc4ee306a6a3b8ee5d184ed7e786"
REVISION = "f95ad0d731bc53634336ae7b794a7b23aa96a3c0"
REVIEW_SHA = "7355641ae0d308b57b533c877132a4f3953a03cab1b3c2aae3424076b6806d4f"
APPLY_SHA = "d6d0af2d04990111aca3e7dd6c7437c3243e1bdb6f33f5afcc91feb857e83010"
SOURCE_SHA = "97fea5d3d87de7879155a45b29e8f0a754821f27fd87f4b875653bfc70e18d7f"
SIDECAR_SHA = "4ce51b644bdab92f1ea7702ce4261045097c4a03280dc483d62aa8695637596a"
MANIFEST = "reports/gtdb-species-status-20261115/jmp134-001-successor.json"
BLOCK = {
    "gtdb_id": "GTDB:s__Cupriavidus_pinatubonensis",
    "gtdb_taxon": "Cupriavidus pinatubonensis",
    "gtdb_lineage": (
        "d__Bacteria;p__Pseudomonadota;c__Gammaproteobacteria;o__Burkholderiales;"
        "f__Burkholderiaceae;g__Cupriavidus;s__Cupriavidus pinatubonensis"
    ),
    "ncbi_source_id": "NCBITaxon:264198",
    "majority_fraction": 1.0,
    "total_genomes": 1,
    "is_reclassified": False,
    "mapping_source": "kg-microbe NCBI2GTDB.tsv.gz sha256:761d5537a7edb4b0 (file mtime 2026-11-15)",
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
    rows = [row for row in review["source"]["inputs"] if row["path"] == path]
    assert len(rows) == 1 and rows[0]["sha256"] == expected, path


def historical_bytes(root, path):
    if path == TARGET:
        return subprocess.check_output(["git", "show", f"{BASELINE}:{path}"], cwd=root)
    return (root / path).read_bytes()


def unchanged_science(before, after):
    assert before["id"] == after["id"] == IDENTITY
    assert len(before["taxonomy"]) == len(after["taxonomy"]) == 1
    old = before["taxonomy"][0]["taxon_term"]
    new = after["taxonomy"][0]["taxon_term"]
    assert (
        old["term"]
        == new["term"]
        == {"id": "NCBITaxon:264198", "label": "Cupriavidus pinatubonensis JMP134"}
    )
    assert old["gtdb_grounding_status"] == "UNRESOLVED" and "gtdb_classification" not in old
    assert new["gtdb_grounding_status"] == "GROUNDED" and new["gtdb_classification"] == BLOCK
    prior = before["curation_history"]
    assert after["curation_history"][: len(prior)] == prior
    expected_events = [
        {
            "timestamp": "2026-11-15T05:47:34Z",
            "curator": "gtdb_ground.py",
            "action": "GTDB_GROUND",
            "changes": "Added 1 gtdb_classification block(s) from NCBI2GTDB.tsv.gz (#395).",
        },
        {
            "timestamp": "2026-11-15T05:47:34Z",
            "curator": "gtdb_ground.py",
            "action": "GTDB_SET_STATUS",
            "changes": "Wrote gtdb_grounding_status on 1 taxonomy entries (#294, #395).",
        },
    ]
    assert after["curation_history"][len(prior) :] == expected_events
    old, new = copy.deepcopy(before), copy.deepcopy(after)
    for doc in (old, new):
        doc.pop("curation_history")
        term = doc["taxonomy"][0]["taxon_term"]
        term.pop("gtdb_classification", None)
        term.pop("gtdb_grounding_status")
    assert old == new, "all unchanged scientific content and stock identities must be preserved"


def current_record_sha256(root, path, predecessor_hash, *, manifest=None, current=None):
    current = (root / path).read_bytes() if current is None else current
    actual = digest(current)
    if actual == predecessor_hash:
        return actual
    assert path == TARGET, "no species successor allowance for other batch147 records"
    assert predecessor_hash == BEFORE and actual == AFTER
    original = historical_bytes(root, path)
    assert digest(original) == BEFORE
    before, after = yaml.safe_load(original), yaml.safe_load(current)
    unchanged_science(before, after)
    proof = json.loads((root / MANIFEST).read_bytes()) if manifest is None else manifest
    assert proof["target"] == TARGET and proof["target_id"] == IDENTITY
    assert proof["before_sha256"] == BEFORE and proof["after_sha256"] == AFTER
    assert proof["execution_revision"] == REVISION and proof["scientific_review"] is False
    assert proof["diagnostic_review"]["sha256"] == REVIEW_SHA
    review = yaml.safe_load(artifact(root, proof["diagnostic_review"]))
    validate_review(review)
    assert review["repository"] == "CultureBotAI/CommunityMech"
    assert review["source"]["git_revision"] == REVISION
    assert review["completion"] == "completed" and review["scientific_review"] is False
    assert review["verdict"] == "pass_with_limitations" and review["scope"]["coverage"] == "partial"
    assert review["scope"]["reviewed_target_ids"] == [IDENTITY] and len(review["targets"]) == 1
    target = review["targets"][0]
    assert (target["path"], target["target_id"], target["selector"]) == (
        TARGET,
        IDENTITY,
        "taxonomy[0].taxon_term.gtdb_classification; gtdb_grounding_status",
    )
    reviewed_input(review, TARGET, AFTER)
    evidence = {row["evidence_id"]: row for row in review["evidence"]}
    assert any(
        row["area"] == "grounding"
        and row["outcome"] == "supported"
        and row["target_ids"] == [IDENTITY]
        and any(evidence[key]["kind"] == "database" for key in row["evidence_ids"])
        for row in review["assessments"]
    )
    required = [row for row in review["checks"] if row["required"]]
    expected_checks = {
        "schema",
        "strict",
        "gtdb",
        "domain",
        "scalars",
        "history",
        "new-history",
        "terms",
    }
    assert {row["check_id"] for row in required} == expected_checks
    assert set(proof["required_checks"]) == expected_checks
    assert all(
        row["status"] == "passed" and row["exit_code"] == 0 and row["target_ids"] == [IDENTITY]
        for row in required
    )
    application = proof["application_receipt"]
    assert application["sha256"] == application["raw_sha256"] == APPLY_SHA
    reviewed_input(review, application["raw_path"], APPLY_SHA)
    receipt = json.loads(artifact(root, application))
    assert receipt["target"] == TARGET and receipt["applied"] is True
    assert receipt["before_sha256"] == BEFORE and receipt["after_sha256"] == AFTER
    assert receipt["execution_revision"] == REVISION
    reviewed_input(
        review, "scripts/adhoc/apply_jmp134_grounding_20261115.py", receipt["helper_sha256"]
    )
    for name, expected in receipt["inputs"].items():
        if name == TARGET:
            assert expected == BEFORE
            reviewed_input(
                review, str(Path(application["raw_path"]).with_name("before.yaml")), BEFORE
            )
        else:
            reviewed_input(review, name, expected)
    sidecar = proof["history_sidecar"]
    assert sidecar["sha256"] == SIDECAR_SHA
    reviewed_input(review, sidecar["path"], SIDECAR_SHA)
    history = yaml.safe_load(artifact(root, sidecar))
    assert history["target"]["kind"] == "record" and history["target"]["path"] == TARGET
    assert history["events"] and history["events"][0]["outcome"] == "changed"
    source_artifact = proof["grounding_evidence"]
    assert source_artifact["sha256"] == SOURCE_SHA
    reviewed_input(review, source_artifact["path"], SOURCE_SHA)
    source = json.loads(artifact(root, source_artifact))
    assert source["record"] == TARGET and source["record_id"] == IDENTITY
    native = source["native_result"]
    expected_native = {key: value for key, value in BLOCK.items() if key != "mapping_source"}
    expected_native["via"] = "ncbi_id"
    assert native == expected_native
    row = source["crosswalk_exact_rows"][0]
    assert len(source["crosswalk_exact_rows"]) == 1 and row["line"] == 71828
    assert row["cells"]["taxonID NCBI"] == "264198"
    assert row["cells"]["strain (NCBI)"] == "Cupriavidus pinatubonensis JMP134"
    assert row["cells"]["total genomes"] == "1" and row["cells"]["majority fraction"] == "1.0"
    assert row["cells"]["species (GTDB)"] == "Cupriavidus pinatubonensis"
    assert any(
        row["predicate"] == "oio:hasRelatedSynonym" and row["value"] == "Cupriavidus necator JMP134"
        for row in source["ncbi_identity_rows"]
    )
    for name, expected in source["source_inputs"].items():
        reviewed_input(review, name, AFTER if name == TARGET else expected)
    route = proof["native_recomputation"]
    assert route["sha256"] == route["raw_sha256"] == SOURCE_SHA
    reviewed_input(review, route["raw_path"], SOURCE_SHA)
    assert json.loads(artifact(root, route)) == source
    assert artifact(root, proof["review_markdown"]).decode() == render_markdown(review)
    return actual
