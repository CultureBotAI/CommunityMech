#!/usr/bin/env python3
"""Can each recorded grounding be reproduced from the source it names? (#624)

Every `gtdb_classification` block records the `ncbi_source_id` it was resolved
from, plus a `majority_fraction` and `total_genomes`. Those numbers are what a
curator reads to decide whether to trust the grounding — #383 exists because the
fraction alone hid its own evidence, and `total_genomes` was added so the
denominator could be seen.

That only helps if the numbers can be checked against the id they claim to come
from. On `GLBRC_UFMP_Fermentation_Community` they cannot: the block records
`ncbi_source_id: NCBITaxon:133926`, `total_genomes: 29`, and that id has **zero**
rows in the crosswalk. *Olsenella uli* is there under NCBI 633147 with 27
genomes. So the grounding is not reproducible from what it says produced it.

This reports three states per block:

  OK          the id is in the crosswalk and total_genomes agrees
  DRIFTED     the id is present but total_genomes differs — most likely a
              grounding written against an older GTDB release, which nothing in
              the record identifies (that is the underlying gap)
  UNSOURCED   the id has no rows at all; the numbers cannot have come from here

A script, not a test: it reads a large external file from a local kg-microbe
checkout, so it cannot run in the blocking gate.

Usage:
    uv run python scripts/audit_grounding_provenance.py [--list] [--kg-microbe-dir DIR]
"""

from __future__ import annotations

import gzip
import importlib.util
import pathlib
import sys
from collections import Counter

import yaml

REPO = pathlib.Path(__file__).resolve().parent.parent
COMMUNITIES = REPO / "kb/communities"


def _ground_module():
    """Reuse gtdb_ground's column constants and directory resolution.

    Imported rather than copied: the column indices are load-bearing and a
    duplicate set would drift silently the first time the crosswalk changed
    shape. Same reason `audit_writers.py` is read rather than re-derived.
    """
    spec = importlib.util.spec_from_file_location(
        "gtdb_ground_for_audit", REPO / "scripts/gtdb_ground.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def crosswalk_totals(mapping: pathlib.Path, ground) -> dict[str, int]:
    """NCBI species NAME -> genome count, computed exactly as `gtdb_ground` does.

    Keyed by name because that is how groundings resolve: `COL_NCBI_ID` is a
    strain/genome-level taxid, so *Acetobacterium woodii* (species 33952) sits
    on a row keyed 931626 with the species in `COL_NCBI_SPECIES`.

    The count comes from `ground._species_denominator`, not from summing. That
    function exists precisely because a species-rank row and its strain rows
    describe overlapping genome sets, and its rule is "take the larger depth,
    never the sum". A naive sum here reported 160 blocks as drifted with the
    tell-tale signature of doubling — 2 against 4, 7 against 15 — which is what
    sent me to read it. Reusing it is also the point: a second copy of this
    arithmetic would disagree with the tool the moment either changed.
    """
    rows_by_name: dict[str, list] = {}
    with gzip.open(mapping, "rt") as handle:
        next(handle, None)  # header
        for line in handle:
            row = line.rstrip("\n").split("\t")
            if len(row) <= max(ground.COL_TOTAL_GENOMES, ground.COL_NCBI_STRAIN):
                continue
            name = row[ground.COL_NCBI_SPECIES].strip()
            if name:
                rows_by_name.setdefault(name, []).append(row)
    return {name: ground._species_denominator(rows)[0] for name, rows in rows_by_name.items()}


def blocks():
    """(file, preferred_term, gtdb_classification) for every grounding."""
    for path in sorted(COMMUNITIES.glob("*.yaml")):
        document = yaml.safe_load(path.read_text(encoding="utf-8")) or {}

        def walk(node, filename=path.name):
            if isinstance(node, dict):
                classification = node.get("gtdb_classification")
                if isinstance(classification, dict) and classification.get("ncbi_source_id"):
                    # The NCBI label is what the crosswalk is keyed by, so it is
                    # what a recorded total can be checked against.
                    label = ((node.get("term") or {}) or {}).get("label") or ""
                    yield filename, node.get("preferred_term") or "", classification, label
                for value in node.values():
                    yield from walk(value, filename)
            elif isinstance(node, list):
                for value in node:
                    yield from walk(value, filename)

        yield from walk(document)


def main() -> int:
    ground = _ground_module()
    kg_dir = ground.resolve_kg_microbe_dir(
        sys.argv[sys.argv.index("--kg-microbe-dir") + 1] if "--kg-microbe-dir" in sys.argv else None
    )
    mapping = kg_dir / ground.MAPPING_REL
    if not mapping.is_file():
        print(f"[audit] crosswalk not found at {mapping}", file=sys.stderr)
        return 2

    totals = crosswalk_totals(mapping, ground)
    verdicts: Counter[str] = Counter()
    detail = []

    skipped_higher = 0
    for filename, preferred, classification, ncbi_label in blocks():
        recorded = classification.get("total_genomes")

        # Only species-rank groundings are comparable: a higher rank sums a
        # different set of rows, and reproducing that means reimplementing
        # `resolve_higher` rather than auditing it.
        if not str(classification.get("gtdb_id", "")).startswith("GTDB:s__"):
            skipped_higher += 1
            continue
        if not ncbi_label or recorded is None:
            skipped_higher += 1
            continue

        actual = totals.get(ncbi_label)
        if actual is None:
            verdicts["UNSOURCED"] += 1
            detail.append(("UNSOURCED", filename, preferred, ncbi_label, recorded, None))
        elif int(recorded) != actual:
            verdicts["DRIFTED"] += 1
            detail.append(("DRIFTED", filename, preferred, ncbi_label, recorded, actual))
        else:
            verdicts["OK"] += 1

    total = sum(verdicts.values())
    print(f"# {total} SPECIES-level gtdb_classification blocks checked against {mapping.name}")
    print(f"  ({skipped_higher} higher-rank blocks skipped — resolved by name, not by taxid)")
    for state in ("OK", "DRIFTED", "UNSOURCED"):
        print(f"  {state:<10} {verdicts[state]}")

    if "--list" in sys.argv or verdicts["UNSOURCED"]:
        print("\n# Not reproducible from the ncbi_source_id they record")
        for state, filename, preferred, source, recorded, actual in detail:
            actual_text = "no rows" if actual is None else f"crosswalk says {actual}"
            print(
                f"  [{state}] {filename[:46]:46} {preferred[:30]:30} "
                f"{source!r} total_genomes={recorded} ({actual_text})"
            )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
