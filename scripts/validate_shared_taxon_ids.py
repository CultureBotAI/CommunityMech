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
    for path in paths:
        try:
            document = yaml.safe_load(path.read_text()) or {}
        except yaml.YAMLError as error:
            print(f"{path}: unparseable: {error}", file=sys.stderr)
            problems += 1
            continue
        for message in check_record(document.get("taxonomy") or []):
            print(f"{path}: {message}")
            problems += 1
    print(f"\nfiles checked: {len(paths)}\nreused ids: {problems}")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
