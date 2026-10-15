"""Verify the integration repair leaves scientific graph/evidence unchanged."""

import hashlib
import json
import subprocess
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[3]
BASE = "1a274b20148ae84cd71e2b233f268c702b332b90"
RECORD = "kb/communities/GLBRC_Exometabolite_Transwell_SynCom.yaml"


def main():
    old_bytes = subprocess.check_output(["git", "show", f"{BASE}:{RECORD}"], cwd=ROOT)
    old = yaml.safe_load(old_bytes)
    doc = yaml.safe_load((ROOT / RECORD).read_text())
    row = yaml.safe_load(
        (ROOT / "reports/causal_graph_review/decisions/20261015-transwell-ci.yaml").read_text()
    )["records"][0]
    assert row["original_sha256"] == hashlib.sha256(old_bytes).hexdigest()
    assert row["record_sha256"] == hashlib.sha256((ROOT / RECORD).read_bytes()).hexdigest()
    assert {k for k in doc if doc[k] != old[k]} == {"taxonomy", "curation_history"}
    assert doc["curation_history"][:-1] == old["curation_history"]
    for before, after in zip(old["taxonomy"], doc["taxonomy"], strict=True):
        assert {k for k in before.keys() | after.keys() if before.get(k) != after.get(k)} == {
            "taxon_term"
        }
        assert before["evidence"] == after["evidence"]
        assert before["strain_designation"] == after["strain_designation"]
        a, b = before["taxon_term"], after["taxon_term"]
        assert {k for k in a.keys() | b.keys() if a.get(k) != b.get(k)} == {
            "notes",
            "gtdb_grounding_status",
        }
        assert a["term"] == b["term"] and a["preferred_term"] == b["preferred_term"]
        assert b["notes"].startswith(a["notes"])
        assert b["gtdb_grounding_status"] == "UNRESOLVED"
        assert "gtdb_classification" not in b
    summary = json.loads((ROOT / "reports/causal_graph_review/summary.json").read_text())
    assert summary["review_status_counts"] == {"needs_research": 54, "reviewed": 408}
    assert (summary["records"], summary["nodes"], summary["edges"]) == (462, 1383, 533)
    folder = ROOT / "reports/causal_graph_review/20261015-transwell-ci"
    network = json.loads(json.loads((folder / "ci-network.json").read_text())["stdout"])
    prior = json.loads(
        json.loads(
            (ROOT / "reports/causal_graph_review/20261015-transwell/network.json").read_text()
        )["stdout"]
    )
    assert network == prior and sum(map(len, network.values())) == 57
    print(
        "Only GTDB status/notes and append-only history changed; "
        "graph/evidence and 57 warnings preserved."
    )


if __name__ == "__main__":
    main()
