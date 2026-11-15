"""Read-only accounting of the retained 20185647 native measurement, 2026-11-15.

Inputs: published aggregate metadata, exact private measurement, optional reviewed
issue-owner map. Output: metadata-only JSON/Markdown on stdout; caller chooses an
exclusive artifact. No validation, acquisition, source/cache writes or scientific
verdicts. Serves Phase2 blocker accounting under PR2804.
"""

import argparse
import hashlib
import json
import subprocess
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
SUMMARY = "reports/phase2-reference-measurements-20261115/m5-final-reference-corpus-001.json"
SUMMARY_SHA = "4dd2d4fcb8cad8ac95a0a645ba7a70fc4e21f267429f6fbd25d34530086ff147"
REVISION = "20185647ad327b686b37dcf3a0036cf298028779"
SCOPED = {
    "EcoFAB_Ring_Trial_SynCom17.yaml",
    "LBNL_Switchgrass_Soil_SynCom16.yaml",
    "LBNL_Brachypodium_Drought_SynCom15.yaml",
    "LBNL_Human_Gut_Interaction_SynCom.yaml",
    "Yolo_Silt_Loam_Soil_Dopamine_Amendment_Microcosm.yaml",
    "Brachypodium_Natural_Variation_Dopamine_SynCom16.yaml",
}


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def inventory(measurement_path):
    raw_summary = (ROOT / SUMMARY).read_bytes()
    assert digest(raw_summary) == SUMMARY_SHA
    summary = json.loads(raw_summary)
    raw_measurement = measurement_path.read_bytes()
    assert digest(raw_measurement) == summary["raw_artifact_sha256"]["measurement.json"]
    measurement = json.loads(raw_measurement)
    assert summary["measurement_revision"] == REVISION
    assert measurement["measurement_valid"] is True
    assert summary["counts"] == measurement["counts"]
    published = {row["record"]: row for row in summary["records"]}
    observed = {row["record"]: row for row in measurement["records"]}
    assert len(published) == len(observed) == len(measurement["records"]) == 549
    assert set(published) == set(observed)
    rows = []
    aggregate = Counter()
    for path, observed_row in observed.items():
        statuses = Counter(item["status"] for item in observed_row["assertions"])
        aggregate.update(statuses)
        assert dict(statuses) == published[path]["status_counts"]
        failures = [item for item in observed_row["assertions"] if item["status"] != "matched"]
        assert len(failures) == published[path]["native_issues"]
        if not failures and Path(path).name not in SCOPED:
            continue
        record_raw = subprocess.check_output(["git", "show", f"{REVISION}:{path}"], cwd=ROOT)
        assert digest(record_raw) == measurement["input_sha256"][path]
        record = yaml.safe_load(record_raw)
        row = {
            "record": path,
            "id": record["id"],
            "record_sha256": digest(record_raw),
            "phase2_scope": Path(path).name in SCOPED,
            "surfaces": published[path]["surfaces"],
            "compared": published[path]["compared"],
            "native_issues": len(failures),
            "status_counts": dict(statuses),
            "native_classes": published[path]["native_classes"],
            "failures": [],
        }
        for item in failures:
            assert item["status"] in {"mismatched", "no_content"}
            assert item["reference_binding_consistent"] is True
            cache = item.get("cache", {})
            row["failures"].append(
                {
                    "path": item["path"],
                    "reference": item["reference"],
                    "native_class": item["native_class"],
                    "status": item["status"],
                    "actually_compared": item["actually_compared"],
                    "cache_path": cache.get("requested_path"),
                    "cache_sha256": cache.get("sha256"),
                    "content_type": cache.get("content_type"),
                }
            )
        rows.append(row)
    assert dict(aggregate) == summary["status_counts"]
    assert sum(row["native_issues"] for row in rows) == 109
    assert sum(row["native_issues"] > 0 for row in rows) == 17
    assert sum(row["phase2_scope"] for row in rows) == 6
    return {
        "measurement_revision": REVISION,
        "published_metadata": {"path": SUMMARY, "sha256": SUMMARY_SHA},
        "raw_measurement_sha256": digest(raw_measurement),
        "counts": summary["counts"],
        "status_counts": summary["status_counts"],
        "record_processing_complete": summary["record_processing_complete"],
        "assertion_coverage_complete": summary["assertion_coverage_complete"],
        "validation_passed": summary["validation_passed"],
        "native_exit_code": summary["native_exit_code"],
        "rows": rows,
        "limit": "Historical lexical-validation accounting; no new matching, scientific verdict or final-current-revision measurement.",
    }


def add_owners(result, directory):
    owner_path = ROOT / "reports/phase2-reference-blockers-20261115/ownership.json"
    owners = json.loads(owner_path.read_bytes())
    failures = [row for row in result["rows"] if row["native_issues"]]
    assert {row["id"].split(":")[1] for row in failures} == set(owners)
    issues = {}
    for row in result["rows"]:
        if not row["native_issues"]:
            row["ownership"] = {
                "issues": [],
                "note": "No issue in this historical run; no scientific approval or later-revision pass inferred.",
            }
            continue
        row["ownership"] = owners[row["id"].split(":")[1]]
        for number in row["ownership"]["issues"]:
            snapshot = directory / f"issue-{number}.json"
            raw = snapshot.read_bytes()
            issue = json.loads(raw)
            assert issue["number"] == number
            assert issue["url"] == f"https://github.com/CultureBotAI/CommunityMech/issues/{number}"
            issues[str(number)] = {
                key: issue[key] for key in ("number", "title", "state", "url", "updatedAt")
            }
            issues[str(number)].update(
                snapshot_sha256=digest(raw),
                retained_snapshot=f".temp/phase2-reference-blockers-20261115/issue-{number}.json",
                snapshot_saved_at=datetime.fromtimestamp(
                    snapshot.stat().st_mtime, timezone.utc
                ).isoformat(),
            )
    scoped = [row for row in result["rows"] if row["phase2_scope"]]
    outside = [row for row in result["rows"] if not row["phase2_scope"]]
    result["phase2"] = {
        "records": len(scoped),
        "surfaces": sum(row["surfaces"] for row in scoped),
        "compared": sum(row["compared"] for row in scoped),
        "matched": sum(row["status_counts"].get("matched", 0) for row in scoped),
        "native_issues": sum(row["native_issues"] for row in scoped),
        "affected_records": sum(row["native_issues"] > 0 for row in scoped),
    }
    result["outside_phase2"] = {
        "records": result["counts"]["records_selected"] - len(scoped),
        "affected_records": len(outside),
        "native_issues": sum(row["native_issues"] for row in outside),
    }
    assert result["phase2"]["native_issues"] == 2
    classes = Counter(item["native_class"] for row in failures for item in row["failures"])
    assert dict(classes) == {"EvidenceItem": 103, "SupportingReference": 6}
    result.update(
        failure_classes=dict(classes),
        issue_snapshots=issues,
        new_issue=2841,
        ownership_sha256=digest(owner_path.read_bytes()),
        helper_sha256=digest(Path(__file__).read_bytes()),
        triage_revision=subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
        ).strip(),
        checked_at=datetime.now(timezone.utc).isoformat(),
    )
    result["evidence_boundaries"] = [
        "No native validation or primary-source acquisition was rerun; current issue ownership is layered onto the immutable 20185647 measurement.",
        "The six SupportingReference failures are Bacteroides dataset1, Fucoidan discussion1, switchgrass discussion2, Panzhihua discussion1 and Synechococcus discussion1; each was actually compared.",
        "Exact TableS1 source support is retained in the three-record full scientific review; previous source-boundary recurrence evidence remains in the M5 reference-failure triage report.",
        "GitHub searches covered exact identifiers, record names and candidate issue bodies; comments and every external repository were not exhaustively searched. Bounded local report/review searches included ignored/hidden files.",
        "This ledger does not reorder the scientific campaign or close issues; the final-current M5 aggregate and later source revisions remain separate.",
    ]
    return result


def markdown(result):
    phase2 = result["phase2"]
    lines = [
        "# Historical reference-validation blocker ledger",
        "",
        f"Measurement: `{REVISION}`; [published aggregate](../phase2-reference-measurements-20261115/m5-final-reference-corpus-001.json), SHA-256 `{SUMMARY_SHA}`.",
        "",
        "All **549 records** were processed. **109 native issues in 17 records** comprise 108 actual lexical mismatches and one no-content occurrence that was not compared. Native exit1 and incomplete assertion coverage remain unchanged. These outcomes do not establish scientific falsity.",
        "",
        f"The six Phase2 targets contain **{phase2['compared']}/{phase2['surfaces']} comparisons**, {phase2['matched']} matches and two mismatches, both in switchgrass. The other 543 records contain 107 issues across 16 records. This is the retained run, not a measurement of the final current revision.",
        "",
        "## Six Phase2 targets",
        "",
        "| Record | Compared/surfaces | Matched | Native issues | Disposition |",
        "|---|---:|---:|---:|---|",
    ]
    for row in result["rows"]:
        if row["phase2_scope"]:
            disposition = (
                "[#1996](https://github.com/CultureBotAI/CommunityMech/issues/1996): two TableS1 cells need source routing"
                if row["native_issues"]
                else "No issue in this run"
            )
            lines.append(
                f"| {row['id']} · {Path(row['record']).stem} | {row['compared']}/{row['surfaces']} | {row['status_counts'].get('matched', 0)} | {row['native_issues']} | {disposition} |"
            )
    lines.extend(
        [
            "",
            "## All affected records in measured inventory order",
            "",
            "| Record | Source | Issues | Boundary / owner |",
            "|---|---|---:|---|",
        ]
    )
    for row in result["rows"]:
        if not row["native_issues"]:
            continue
        refs = sorted({item["reference"] for item in row["failures"]})
        owners = ", ".join(
            f"[#{number}]({result['issue_snapshots'][str(number)]['url']})"
            for number in row["ownership"]["issues"]
        )
        lines.append(
            f"| {row['id']} · {Path(row['record']).stem} | {', '.join(refs)} | {row['native_issues']} | {row['ownership']['category']}; {owners} |"
        )
    lines.extend(["", "## Interpretation and retained limits", ""])
    for row in result["rows"]:
        if row["native_issues"] and (
            row["phase2_scope"]
            or row["id"]
            in {
                "CommunityMech:000142",
                "CommunityMech:000449",
                "CommunityMech:000051",
                "CommunityMech:000167",
            }
        ):
            lines.append(f"- **{row['id']}**: {row['ownership']['note']}")
    lines.extend(
        [
            "",
            "New bounded finding [#2841](https://github.com/CultureBotAI/CommunityMech/issues/2841) records the Panzhihua notation discrepancy after exact-phrase/record/PMID deduplication. All other rows map to existing owners. Current issue states and exact field/cache/hash identities are retained in [the JSON ledger](reference-blockers-20185647.json). No raw quotations, source bodies or absolute local paths are published.",
            "",
        ]
    )
    lines.extend("- " + item for item in result["evidence_boundaries"])
    lines.extend(
        [
            "",
            "Source-support context: [full three-record review](../../reviews/structured/20261115T031503Z-phase2-three-record-final-science/review.md); [previous reference triage](../m5-completion-20261114/reference-failure-triage-20261114.md). These are scope/ownership evidence, not a replacement for the measured artifact.",
            "",
        ]
    )
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--measurement", type=Path, required=True)
    parser.add_argument(
        "--record", help="One real canary row; validation still reconciles the aggregate"
    )
    parser.add_argument("--issue-snapshots", type=Path)
    parser.add_argument("--format", choices=["json", "markdown"], default="json")
    args = parser.parse_args()
    result = inventory(args.measurement)
    if args.issue_snapshots:
        result = add_owners(result, args.issue_snapshots)
    if args.record:
        result["rows"] = [row for row in result["rows"] if row["record"] == args.record]
        assert len(result["rows"]) == 1
        result["output_scope"] = "Single-row extraction canary; aggregate counts remain historical"
    if args.format == "markdown":
        assert args.issue_snapshots and not args.record
        print(markdown(result), end="")
    else:
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
