"""Report NCBITaxon ids standing in for more than one organism (#292).

Single-file form of the check `validate-strict` runs. See
`communitymech.validators.shared_taxon_ids` for why the id<->label gate cannot
see this class of error.
"""

from __future__ import annotations

import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from communitymech.validators.shared_taxon_ids import check_record  # noqa: E402


def main(argv: list[str] | None = None) -> int:
    paths = [Path(p) for p in (argv if argv is not None else sys.argv[1:])]
    if not paths:
        print("usage: validate_shared_taxon_ids.py FILE [FILE ...]", file=sys.stderr)
        return 2
    problems = 0
    unreadable = 0
    for path in paths:
        # An unreadable file is a usage error, not a finding. Counting it as one
        # would exit 1 and read as "this record reuses an id" (#434); the
        # sibling validators return 2 for the same reason.
        try:
            text = path.read_text()
        except OSError as error:
            print(f"[taxon-ids] cannot read {path}: {error}", file=sys.stderr)
            unreadable += 1
            continue
        try:
            document = yaml.safe_load(text)
        except yaml.YAMLError as error:
            print(f"[taxon-ids] unparseable {path}: {error}", file=sys.stderr)
            unreadable += 1
            continue
        taxonomy = document.get("taxonomy") if isinstance(document, dict) else None
        for message in check_record(taxonomy):
            print(f"{path}: {message}")
            problems += 1
    print(f"\nfiles checked: {len(paths)}\nreused ids: {problems}")
    if unreadable:
        print(f"unreadable: {unreadable}", file=sys.stderr)
        return 2
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
