"""Verify participant-repair scope and retained provenance without network calls."""

import hashlib
import json
import subprocess
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[3]
BASE = "616a2806e363f01a3727ea57dcf3bcd019999943"
RECORD = "kb/communities/GLBRC_Exometabolite_Transwell_SynCom.yaml"
RECEIPTS = Path(__file__).resolve().parent


def verify():
    old_raw = subprocess.check_output(["git", "show", f"{BASE}:{RECORD}"], cwd=ROOT)
    old = yaml.safe_load(old_raw)
    doc = yaml.safe_load((ROOT / RECORD).read_text())
    row = yaml.safe_load(
        (ROOT / "reports/causal_graph_review/decisions/20261015-transwell.yaml").read_text()
    )["records"][0]
    assert row["original_sha256"] == hashlib.sha256(old_raw).hexdigest()
    assert row["record_sha256"] == hashlib.sha256((ROOT / RECORD).read_bytes()).hexdigest()
    assert {k for k in doc if doc[k] != old[k]} == set(row["allowed_changed_fields"])
    assert doc["curation_history"][:-1] == old["curation_history"]
    for before, after in zip(
        old["ecological_interactions"], doc["ecological_interactions"], strict=True
    ):
        assert before["name"] == after["name"]
        assert before["evidence"] == after["evidence"]
        assert before.get("downstream") == after.get("downstream")
    cache = "references_cache/PMID_29152587.txt"
    assert (ROOT / cache).read_bytes() == subprocess.check_output(
        ["git", "show", f"{BASE}:{cache}"], cwd=ROOT
    )
    manifest = json.loads(
        (ROOT / "reports/causal_graph_review/sources/20261015-transwell/manifest.json").read_text()
    )
    for source in manifest:
        assert hashlib.sha256((ROOT / source["path"]).read_bytes()).hexdigest() == source["sha256"]
    prior_network = json.loads(
        json.loads((RECEIPTS / "baseline-network.json").read_text())["stdout"]
    )
    after_network = json.loads(json.loads((RECEIPTS / "network.json").read_text())["stdout"])
    assert after_network == prior_network
    assert sum(map(len, after_network.values())) == 57
    assert not any(
        i["type"] in {"DANGLING_EDGE", "DANGLING_ANCHOR"}
        for issues in after_network.values()
        for i in issues
    )
    summary = json.loads((ROOT / "reports/causal_graph_review/summary.json").read_text())
    assert summary["records"] == 462 and summary["nodes"] == 1383 and summary["edges"] == 533
    assert summary["review_status_counts"] == {"needs_research": 54, "reviewed": 408}
    assert summary["structural_defects"] == []
    changed = []
    count = 0
    for folder in ["kb/communities", "data/isolates"]:
        # Filesystem discovery includes ignored/hidden records.
        for path in (ROOT / folder).rglob("*.yaml"):
            rel = str(path.relative_to(ROOT))
            raw = subprocess.check_output(["git", "show", f"{BASE}:{rel}"], cwd=ROOT)
            if raw != path.read_bytes():
                changed.append(rel)
            count += 1
    assert count == 462 and changed == [RECORD]
    print(
        json.dumps(
            {
                "records_checked": count,
                "changed": changed,
                "source_payloads": len(manifest),
                "native_network_warnings": 57,
                "warning_set_unchanged": True,
                "structural_errors": 0,
                "nodes": 1383,
                "edges": 533,
                "reviewed": 408,
                "needs_research": 54,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    verify()
