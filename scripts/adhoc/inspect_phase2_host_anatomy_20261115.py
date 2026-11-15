"""Readonly PO-root evidence for the integrated term canary, 2026-11-15.

Inputs: explicit existing PO sqlite ontology and committed host enum.
Output: exclusive private JSON with canonical labels and subclass ancestry.
Serves the linked-runner adapter-completeness finding; no ontology/cache writes.
"""

import argparse
import hashlib
import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--po", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    output = args.output.resolve()
    if output.exists() or not output.is_relative_to(ROOT / ".temp/phase2-science-20261115"):
        raise ValueError("exclusive private output required")
    before = args.po.stat()
    with sqlite3.connect(args.po.resolve().as_uri() + "?mode=ro", uri=True) as database:
        database.execute("PRAGMA query_only=ON")
        database.execute("BEGIN")
        labels = database.execute(
            "SELECT subject,value FROM statements WHERE predicate='rdfs:label' AND subject IN ('PO:0009005','PO:0025131') ORDER BY subject"
        ).fetchall()
        ancestors = database.execute(
            "WITH RECURSIVE ancestors(id) AS (SELECT object FROM statements WHERE subject='PO:0009005' AND predicate='rdfs:subClassOf' UNION SELECT s.object FROM statements s JOIN ancestors a ON s.subject=a.id WHERE s.predicate='rdfs:subClassOf') SELECT id FROM ancestors ORDER BY id"
        ).fetchall()
    digest = sha(args.po)
    after = args.po.stat()
    if (before.st_size, before.st_mtime_ns) != (after.st_size, after.st_mtime_ns):
        raise ValueError("ontology changed during readonly query")
    result = {
        "created_at": datetime.now(timezone.utc).isoformat(),
        "ontology_filename": args.po.name,
        "ontology_sha256": digest,
        "labels": dict(labels),
        "subclass_ancestors": [row[0] for row in ancestors],
        "root_is_descendant_of_plant_anatomical_entity": ("PO:0025131",) in ancestors,
        "schema_sha256": sha(ROOT / "src/communitymech/schema/communitymech.yaml"),
        "helper_sha256": sha(Path(__file__)),
        "limitation": "Explicit readonly SQLite statements query; native validator execution is a separate receipt.",
    }
    with output.open("x") as stream:
        stream.write(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
