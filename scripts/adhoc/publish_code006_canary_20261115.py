"""Publish immutable metadata/log derivatives for the000434 canary, #2848.

2026-11-15. Inputs: verified saved M5 assessments and actual raw application/
native log receipts. Output: exclusive reports/gtdb-code006-20261115/canary-000434-N.
No canonical, cache, historical-review or raw-evidence edits; no network.
"""

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path

import yaml
from export_m5_technical_evidence_20261114 import sanitize

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / ".temp/gtdb-code006-20261115"


def sha(data):
    return hashlib.sha256(data).hexdigest()


def checked_native_bytes(review, log, exit_path, expected_exit):
    raw, exit_raw = log.read_bytes(), exit_path.read_bytes()
    for path, data in ((log, raw), (exit_path, exit_raw)):
        relative = str(path.relative_to(ROOT))
        rows = [row for row in review["source"]["inputs"] if row.get("path") == relative]
        if len(rows) != 1 or rows[0].get("sha256") != sha(data):
            raise ValueError("native artifact differs from exact saved review input")
    if not raw or int(exit_raw.strip()) != expected_exit:
        raise ValueError("actual native log/exit differs")
    return raw, exit_raw


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--attempt", required=True)
    args = parser.parse_args()
    if not args.attempt.isdigit():
        raise ValueError("numeric exclusive attempt required")
    output = ROOT / f"reports/gtdb-code006-20261115/canary-000434-{args.attempt}"
    if output.exists():
        raise ValueError("exclusive public proof namespace required")
    payloads, audits, reviews = {}, [], []
    for name in ("assessment-saved-audit-004", "genus-assessment-saved-audit-001"):
        path = STATE / f"{name}.json"
        audit_bytes = path.read_bytes()
        audit = json.loads(audit_bytes)
        review = ROOT / "reviews/structured" / audit["review_id"] / "review.yaml"
        markdown = review.with_suffix(".md")
        review_bytes, markdown_bytes = review.read_bytes(), markdown.read_bytes()
        if (
            audit["all_inputs_match"] is not True
            or audit["markdown_matches_native_render"] is not True
            or sha(review_bytes) != audit["review_sha256"]
            or sha(markdown_bytes) != audit["markdown_sha256"]
        ):
            raise ValueError("saved native review/audit binding differs")
        payloads[f"{name}.json"] = audit_bytes
        reviews.append(yaml.safe_load(review_bytes))
        audits.append(
            {
                "review_id": audit["review_id"],
                "input_count": audit["input_count"],
                "review_sha256": audit["review_sha256"],
                "markdown_sha256": audit["markdown_sha256"],
                "audit_sha256": sha(audit_bytes),
                "audit_file": f"{name}.json",
            }
        )
    previous_after = None
    applications = []
    for name, expected in (
        ("applied-001", "39bac49ad4dc868eb2423d94ce1eaac64cef0bdd23595f233d81a75ac1fe853b"),
        ("genus-applied-001", "14a946e2082e7203b18b39d3c5862403c56eb47ee2844fb917b35b1b4d00123c"),
    ):
        raw = (STATE / name / "receipt.json").read_bytes()
        row = json.loads(raw)
        if sha(raw) != expected or row["applied"] is not True:
            raise ValueError("actual raw application receipt differs")
        if previous_after and previous_after != row["before_sha256"]:
            raise ValueError("application chain is not contiguous")
        previous_after = row["after_sha256"]
        counts = Counter()
        if sanitize(raw.decode(), counts).encode() != raw:
            raise ValueError("raw metadata requires redaction; refuse byte-identity publication")
        filename = name + ".raw-receipt.json"
        payloads[filename] = raw
        applications.append(
            {
                "file": filename,
                "sha256": expected,
                "before_sha256": row["before_sha256"],
                "after_sha256": previous_after,
            }
        )
    target = ROOT / "kb/communities/Acidic_Nitrification_Minimal_Consortium.yaml"
    if sha(target.read_bytes()) != previous_after:
        raise ValueError("current canonical differs from actual M5 final result")
    logs = []
    prefixes = [
        f"{phase}canary-run-{gate}-001"
        for phase in ("", "genus-")
        for gate in ("new-history", "schema", "strict", "gtdb", "domain", "scalars", "history")
    ]
    # The first review binds the resulting sidecar, but not its scaffold log.
    # Keep that original raw log private rather than invent a retrospective binding.
    prefixes.remove("canary-run-new-history-001")
    prefixes += ["canary-completion-001", "genus-completion-001"]
    for name in prefixes:
        log = STATE / f"{name}.log"
        exit_path = STATE / f"{name}.exit"
        expected_exit = 1 if name == "canary-completion-001" else 0
        review_index = int(name.startswith("genus-"))
        raw, exit_raw = checked_native_bytes(reviews[review_index], log, exit_path, expected_exit)
        counts = Counter()
        public = sanitize(raw.decode(), counts).encode()
        public_name = name + ".log.txt"
        payloads[public_name], payloads[name + ".exit.txt"] = public, exit_raw
        logs.append(
            {
                "name": name,
                "bound_review_id": audits[review_index]["review_id"],
                "exit_code": expected_exit,
                "raw_log_sha256": sha(raw),
                "public_log_sha256": sha(public),
                "raw_log": str(log.relative_to(ROOT)),
                "public_log": public_name,
                "exit_sha256": sha(exit_raw),
                "redactions": dict(counts),
            }
        )
    summary = {
        "record": str(target.relative_to(ROOT)),
        "record_id": "CommunityMech:000434",
        "source_revision": "c9e151eb9f22afb5c531dd5a8b3346ce1d58b12a",
        "execution_revision": "956d00c6143020810ef7a60a6298e67fb0ee0caf",
        "runtime": {"host_role": "isolated M5 checkout", "native_python": "3.13.2"},
        "final_record_sha256": previous_after,
        "applications": applications,
        "saved_assessments": audits,
        "logs": logs,
        "publisher_sha256": sha(Path(__file__).read_bytes()),
        "sanitizer_sha256": sha(
            Path(__file__).with_name("export_m5_technical_evidence_20261114.py").read_bytes()
        ),
        "scope": "One same-genus database correspondence. Both prior scientific/status-only assessments are retained; source species/genome and mechanism uncertainty is unchanged. No full-QC, scientific approval, issue closure or bulk application claim.",
        "raw_persistence": "Original M5 raw evidence is mirrored locally under the same private relative paths; public logs are explicit sanitized derivatives.",
    }
    payloads["summary.json"] = (json.dumps(summary, indent=2) + "\n").encode()
    lines = [
        "# One-record GTDB correspondence canary",
        "",
        "The native M5 path applied the reviewed Mycobacterium genus correspondence and passed six scoped gates plus both unchanged outstanding-grounding tests. This is a technical mapping assessment, not a full scientific review or corpus QC pass.",
        "",
        "The earlier status-only step remains recorded: six scoped gates passed, but both completion tests failed. Its immutable needs_curation assessment and actual receipt remain in the chain.",
        "",
        "| Phase | Canonical SHA prefix | Scoped gates | Completion tests |",
        "|---|---|---:|---:|",
        "| Status diagnostic | d58669e0 | 6 passed | 2 failed |",
        "| Genus correspondence | c2cf66bb | 6 passed | 2 passed |",
        "",
        "The mapping is NCBITaxon:1763 → GTDB:g__Mycobacterium, 18589/18589 named genomes, with no reclassification, using exact crosswalk SHA 761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd. The paper's exact species/genome and ecological mechanism remain unresolved; notes, evidence quotations and every other taxon/biological field are unchanged.",
        "",
        "Execution revision 956d00c6143020810ef7a60a6298e67fb0ee0caf used native Python 3.13.2 on the isolated M5 checkout plus explicitly hashed orchestration helpers. [Metadata and raw/public hashes](summary.json) bind both actual receipts, 15 retained native logs, both saved assessments and the original status failure. Each exported log and exit file matches its exact saved-review input hash. The earlier scaffold log remains private because that review bound its resulting sidecar rather than the scaffold log.",
        "",
    ]
    for audit in audits:
        lines += [
            f'- [{audit["review_id"]}](../../../reviews/structured/{audit["review_id"]}/review.yaml): {audit["input_count"]} input hashes and exact native Markdown verified on M5.'
        ]
    lines += [
        "",
        "Raw application receipts are byte-identical metadata copies. Native log derivatives replace private paths/addresses when present, retaining raw and public hashes. Original raw files remain private on both checkouts. Work tracked by #2848/#2849 and all older scientific limitations remains outstanding.",
        "",
    ]
    payloads["README.md"] = "\n".join(lines).encode()
    output.mkdir()
    for filename, raw in payloads.items():
        with (output / filename).open("xb") as stream:
            stream.write(raw)
    print(
        json.dumps(
            {
                "output": str(output.relative_to(ROOT)),
                "files": len(payloads),
                "summary_sha256": sha(payloads["summary.json"]),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
