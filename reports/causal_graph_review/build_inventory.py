"""Rebuild full-corpus graph checks and hash-bound semantic review coverage."""

from __future__ import annotations

import csv
import hashlib
import importlib.util
import json
import sys
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))
from communitymech.paths import default_record_roots, record_files  # noqa: E402


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    paths = sorted(record_files())
    discovered = sorted(p for root in default_record_roots() for p in root.rglob("*.yaml"))
    assert paths == discovered, "Record discovery omits YAML files (including ignored files)"
    ranker = load_module("rank_causal_graph_readiness", ROOT / "scripts/rank_causal_graph_readiness.py")
    auditor_module = load_module("network_auditor", ROOT / "src/communitymech/network/auditor.py")
    decisions = []
    for path in sorted((OUT / "decisions").glob("*.yaml")):
        decisions.extend(yaml.safe_load(path.read_text())["records"])
    by_path = {row["path"]: row for row in decisions}
    assert len(by_path) == len(decisions), "Duplicate record reviews"
    assert set(by_path) <= {str(p.relative_to(ROOT)) for p in paths}, "Review target is missing"
    rows, defects = [], []
    for path in paths:
        doc = yaml.load(path.read_text(), Loader=yaml.CSafeLoader)
        rel = str(path.relative_to(ROOT))
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        review = by_path.get(rel)
        status = "pending"
        if review:
            status = review["status"] if review["record_sha256"] == digest else "stale"
        score = ranker.score_document(doc)
        nodes = doc.get("ecological_interactions") or []
        names = [node["name"] for node in nodes]
        for name, count in Counter(names).items():
            if count > 1:
                defects.append({"path": rel, "type": "DUPLICATE_NODE", "node": name})
        for node in nodes:
            if node.get("downstream") == []:
                defects.append({"path": rel, "type": "EMPTY_DOWNSTREAM", "node": node["name"]})
            seen = set()
            for edge in node.get("downstream") or []:
                target = edge["target"]
                checks = {
                    "DANGLING_EDGE": target not in names,
                    "SELF_EDGE": target == node["name"],
                    "DUPLICATE_EDGE": target in seen,
                    "BLANK_EDGE_DESCRIPTION": not (edge.get("description") or "").strip(),
                    "SOURCE_WITHOUT_EVIDENCE": not node.get("evidence"),
                    "TARGET_WITHOUT_EVIDENCE": not any(n["name"] == target and n.get("evidence") for n in nodes),
                }
                defects.extend({"path": rel, "type": key, "node": node["name"], "target": target}
                               for key, failed in checks.items() if failed)
                seen.add(target)
        rows.append({"path": rel, "id": doc["id"], "record_sha256": digest,
                     "nodes": score["ecological_interactions"], "edges": score["downstream_edges"],
                     "readiness_score": score["score"],
                     "review_file": review.get("review_file", "") if review else "",
                     "review_status": status})
    findings = auditor_module.NetworkIntegrityAuditor().audit_all(quiet=True)
    network = [{"record": record, **issue, "severity": auditor_module.issue_severity(issue)}
               for record, issues in findings.items() for issue in issues]
    summary = {
        "scope": "Every YAML under kb/communities and data/isolates; filesystem discovery includes hidden/ignored files.",
        "semantic_review_rule": "Structural checks and readiness scores do not establish causal support. Completed reviews must match the current record SHA-256.",
        "records": len(rows), "nodes": sum(row["nodes"] for row in rows),
        "edges": sum(row["edges"] for row in rows),
        "records_without_nodes": sum(row["nodes"] == 0 for row in rows),
        "records_without_edges": sum(row["edges"] == 0 for row in rows),
        "review_status_counts": dict(sorted(Counter(row["review_status"] for row in rows).items())),
        "structural_defects": defects,
        "network_audit": network,
    }
    with (OUT / "inventory.tsv").open("w") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]), delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    (OUT / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps({key: value for key, value in summary.items() if key != "network_audit"}, indent=2))
    return 1 if defects or any(issue["severity"] == "error" for issue in network) else 0


if __name__ == "__main__":
    raise SystemExit(main())
