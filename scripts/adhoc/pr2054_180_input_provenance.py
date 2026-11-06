"""Pin actual PR 2054 record 180 inputs and build an immutable JSON successor.

Only scratch JSON and a byte-identical scratch GTDB copy are written here. The
native record-review saver owns YAML/Markdown creation. Existing reviews and the
first correction helper are never modified.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path

import yaml

PREDECESSOR = Path("reviews/structured/20261106T135321Z-jn4-gd17-s1-proof-correction/review.yaml")
ORIGINAL = Path("reviews/structured/20261021T231001Z-jn4-gd17-record-review/review.yaml")
SCRATCH = Path(".temp/pr2054/independent-third")
EARLIER = Path(".temp/pr2054/180-correction")
OUT = Path(".temp/pr2054/180-input-provenance")
SELF = Path("scripts/adhoc/pr2054_180_input_provenance.py")
GTDB = Path(
    "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/NCBI2GTDB.tsv.gz"
)
GTDB_SHA = "761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_json(path: Path):
    return json.loads(path.read_text())


def shared_manifest() -> None:
    """Inventory the earlier four-record read-only session for the batch observer."""
    OUT.mkdir(parents=True, exist_ok=True)
    paths = sorted(p for p in SCRATCH.rglob("*") if p.is_file())
    manifest = {
        "at": datetime.now(timezone.utc).isoformat(),
        "targets": ["CommunityMech:" + n for n in ("000264", "000168", "000180", "000208")],
        "scope": "Current source/check artifacts from the earlier independent read-only "
        "session. Package/container hashes do not imply every archived asset was scientifically "
        "inspected; exact inspection and access limitations are in independent-science-final.json. "
        "The 180 defect and later author-role switch remain explicit. No historical scratch "
        "was recovered. All listed input bytes are frozen.",
        "inputs": [{"path": str(p), "sha256": sha(p), "bytes": p.stat().st_size} for p in paths],
    }
    output = OUT / "independent-source-manifest.json"
    output.write_text(json.dumps(manifest, indent=2) + "\n")
    print(json.dumps({"manifest": str(output), "inputs": len(paths), "sha256": sha(output)}))


def prepare() -> None:
    """Gather the bounded scientific source/check surface before native inspect."""
    OUT.mkdir(parents=True, exist_ok=True)
    local_gtdb = OUT / "NCBI2GTDB.tsv.gz"
    assert sha(GTDB) == GTDB_SHA
    if local_gtdb.exists():
        assert sha(local_gtdb) == GTDB_SHA
    else:
        shutil.copyfile(GTDB, local_gtdb)
    assert GTDB.read_bytes() == local_gtdb.read_bytes()
    copy_receipt = OUT / "gtdb-copy.json"
    if not copy_receipt.exists():
        copy_receipt.write_text(
            json.dumps(
                {
                    "observed_at": datetime.now(timezone.utc).isoformat(),
                    "source": str(GTDB),
                    "copy": str(local_gtdb),
                    "sha256": GTDB_SHA,
                    "byte_identical": True,
                    "scope": "Exact snapshot used by the prior current-target community-mode replay",
                },
                indent=2,
            )
            + "\n"
        )
    previous = yaml.safe_load(PREDECESSOR.read_text())
    paths = {Path(item["path"]) for item in previous["source"]["inputs"]}
    paths.update(
        {
            PREDECESSOR,
            PREDECESSOR.with_suffix(".md"),
            ORIGINAL.with_suffix(".md"),
            SELF,
            Path("justfile"),
            Path(".claude/skills/ground-taxa-gtdb/SKILL.md"),
            local_gtdb,
            copy_receipt,
            OUT / "input-paths.json",
            OUT / "full-lint.json",
            OUT / "full-lint.stdout",
            OUT / "full-lint.stderr",
        }
    )
    # All shared receipts were read as whole files. Their non-180 entries are
    # pinned provenance context, not a scientific reassessment of other records.
    paths.update(SCRATCH.glob("*.json"))
    paths.update((SCRATCH / "000180").iterdir())
    paths.update((SCRATCH / "supplement-180").iterdir())
    paths.update((SCRATCH / "assets").glob("frontiers180-*"))
    paths.update(SCRATCH.glob("PMC6746925*"))
    paths.update(EARLIER.iterdir())
    paths.update(
        SCRATCH / name
        for name in (
            "frontiers180.html",
            "taxonomy.xml",
            "springer180.read.txt",
            "doi-s00253-016-7776-1.html",
            "doi-j.ijhydene.2008.04.004.html",
            "elsevier-j.ijhydene.2008.04.004.xml",
        )
    )
    data = {
        "target": "CommunityMech:000180",
        "paths": sorted(str(p) for p in paths),
        "boundaries": [
            "Includes prior native inspection, candidate and post-save receipts as historical inputs.",
            "The new inspection manifest defines the hashes and cannot hash itself.",
            "The new candidate and later save/check logs are outputs, not prior judgment inputs.",
            "Shared source/check receipts include other records; only 000180 is reassessed here.",
            "The external GTDB source is represented by a verified byte-identical scratch copy.",
        ],
    }
    (OUT / "input-paths.json").write_text(json.dumps(data, indent=2) + "\n")
    print(json.dumps({"input_count": len(paths), "manifest": str(OUT / "input-paths.json")}))


def build(inspection_path: Path, output: Path, started_at: str) -> None:
    """Retain the science and add complete input provenance without superseding others."""
    previous = yaml.safe_load(PREDECESSOR.read_text())
    result = copy.deepcopy(previous)
    inspection = read_json(inspection_path)
    manifest = read_json(OUT / "input-paths.json")
    expected = set(manifest["paths"]) | {t["path"] for t in previous["targets"]}
    actual = {i["path"] for i in inspection["source"]["inputs"]}
    assert actual == expected, sorted(actual ^ expected)
    for item in inspection["source"]["inputs"]:
        assert sha(Path(item["path"])) == item["sha256"], item["path"]
    assert inspection["targets"] == previous["targets"]
    now = datetime.now(timezone.utc)
    result.update(
        {
            "review_id": now.strftime("%Y%m%dT%H%M%SZ") + "-jn4-gd17-complete-input-provenance",
            "title": "JN4/GD17 successor: preserve S1 correction with complete local input pins",
            "started_at": started_at,
            "finished_at": now.isoformat().replace("+00:00", "Z"),
            "source": inspection["source"],
            "summary": previous["summary"]
            + " This linked successor also corrects issue #2566 by pinning the actual "
            "local source/check/helper inputs omitted from the first correction's input set.",
        }
    )
    result["reviewer"]["independence_basis"] = (
        "Author of both correction successors; a different agent identified the input-pin "
        "defect and will independently re-review. No independent self-approval is claimed."
    )
    for item in result["findings"]:
        item["previous_occurrences"].append(
            {
                "repository": result["repository"],
                "review_id": previous["review_id"],
                "finding_id": item["finding_id"],
            }
        )
    result["related_reviews"].append(
        {
            "repository": result["repository"],
            "review_id": previous["review_id"],
            "relationship": "Retain identical science, three open findings and four actions; "
            "correct incomplete local input provenance without rewriting the saved predecessor.",
        }
    )
    result["evidence"].append(
        {
            "evidence_id": "complete-input-manifest",
            "kind": "validation",
            "reference": str(OUT / "input-paths.json"),
            "locator": "Exact files passed to native inspect; GTDB byte-copy receipt",
            "summary": "The complete bounded local input surface is now hashed in source.inputs. "
            "Fresh main/SI figures, XML/text, authority/source-access data, actual check logs, "
            "both helpers and immutable predecessors are included. Shared receipt entries "
            "outside 000180 remain context only. The copied GTDB bytes equal the source snapshot.",
            "snapshot_sha256": sha(OUT / "input-paths.json"),
            "accessed_at": now.isoformat().replace("+00:00", "Z"),
            "support": "supports",
        }
    )
    result["assessments"].append(
        {
            "assessment_id": "complete-local-input-provenance",
            "area": "provenance",
            "topic": "Complete input attestation for the current 000180 successor",
            "outcome": "supported",
            "summary": "Correct the incomplete input set of the 135321 predecessor (#2566).",
            "target_ids": ["CommunityMech:000180"],
            "evidence_ids": ["complete-input-manifest"],
            "details": "The earlier 19 hashes matched their files but omitted other actual "
            "local sources and check receipts. Those omissions are explicitly acknowledged. "
            "This review retains the accepted S1 lane/caption qualification, partial scientific "
            "status, all three open scientific findings and all four actions unchanged. "
            "Native inspection output cannot hash itself; the new candidate and subsequent "
            "post-save validation receipts are generated outputs, not prior judgment inputs. "
            "This correction does not reassess the other nine original batch records.",
        }
    )
    lint = read_json(OUT / "full-lint.json")
    assert lint["exit_code"] == 0
    result["checks"].append(
        {
            "check_id": "provenance-helper-full-lint",
            "name": "Full lint before second helper freeze",
            "status": "passed",
            "required": True,
            "summary": "Full Black, Ruff and mypy passed before the new helper was frozen.",
            "target_ids": ["CommunityMech:000180"],
            "command": lint["command"],
            "exit_code": lint["exit_code"],
            "expected_exit_code": 0,
            "evidence_ids": ["complete-input-manifest"],
        }
    )
    result["notes"].extend(manifest["boundaries"])
    result["notes"].append(
        "Pinned scratch inputs attest to inspected bytes; they are not claimed to be committed "
        "source caches or durable raw-source publication. Current native input checks verified "
        "them before saving; later absence must not be described as source access."
    )
    result["links"].append("https://github.com/CultureBotAI/CommunityMech/issues/2566")
    result["tags"].append("complete-local-input-provenance")
    assert result["actions"] == previous["actions"]
    assert result["completion"] == "partial" and result["scientific_review"] is False
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(result["review_id"])


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("prepare")
    sub.add_parser("shared-manifest")
    candidate = sub.add_parser("build")
    candidate.add_argument("--inspection", type=Path, required=True)
    candidate.add_argument("--output", type=Path, required=True)
    candidate.add_argument("--started-at", required=True)
    args = parser.parse_args()
    if args.command == "prepare":
        prepare()
    elif args.command == "shared-manifest":
        shared_manifest()
    else:
        build(args.inspection, args.output, args.started_at)


if __name__ == "__main__":
    main()
