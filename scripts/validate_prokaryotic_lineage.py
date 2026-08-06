"""Report GTDB lineages whose domain contradicts their NCBITaxon id (#365).

Single-file form of the check `validate-strict` runs. See
`communitymech.validators.prokaryotic_lineage` for why GTDB being
prokaryote-only makes this a contradiction rather than a suspicion.
"""

from __future__ import annotations

import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from communitymech.validators.prokaryotic_lineage import check_record  # noqa: E402


def main(argv: list[str] | None = None) -> int:
    paths = [Path(p) for p in (argv if argv is not None else sys.argv[1:])]
    if not paths:
        print("usage: validate_prokaryotic_lineage.py FILE [FILE ...]", file=sys.stderr)
        return 2
    problems = 0
    unreadable = 0
    for path in paths:
        # An unreadable file is a usage error, not a finding — exiting 1 for it
        # would read as "this record has a contradictory lineage" (cf. #434).
        try:
            text = path.read_text()
        except OSError as error:
            print(f"[gtdb-domain] cannot read {path}: {error}", file=sys.stderr)
            unreadable += 1
            continue
        try:
            document = yaml.safe_load(text)
        except yaml.YAMLError as error:
            print(f"[gtdb-domain] unparseable {path}: {error}", file=sys.stderr)
            unreadable += 1
            continue
        taxonomy = document.get("taxonomy") if isinstance(document, dict) else None
        for message in check_record(taxonomy):
            print(f"{path}: {message}")
            problems += 1
    print(f"\nfiles checked: {len(paths)}\ncontradictory lineages: {problems}")
    if unreadable:
        print(f"unreadable: {unreadable}", file=sys.stderr)
        return 2
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
