"""Point the id/label config at ontology builds that are already downloaded (#716).

`conf/id_label_targets.yaml` names its adapters as `sqlite:obo:<name>`. That
selector does not ask whether the database is usable — it asks pystow to ensure
the **`.db.gz`** is present and re-downloads when it is not. So a machine
holding a perfectly good `<name>.db` and no `.gz` re-downloads anyway, and while
`s3.amazonaws.com/bbop-sqlite` answers 403 that turns a working ontology into
"unavailable" (#707).

The effect is not small. CI restores 20.29 GB of `.db` files — `ncbitaxon.db`
alone is 13.52 GB — and not one `.gz`, so Engine B checked **nothing**. Handed a
config whose selectors name those files directly, it checks **6288 pairs and
exits 0**.

**Why a rewritten config rather than a fixed selector.** OAK expands neither
`~` nor `$HOME`; only an absolute path resolves. An absolute path cannot be
committed, because it differs per machine. So the path is resolved at run time
and written to a scratch config, and `validate_id_label_correspondence.py` --
which is a governed vendored artifact and must not drift -- is pointed at it
with the `-c` it already accepts. Nothing vendored changes.

Only the `sqlite:obo:` selectors are rewritten, and only when the local build
exists; everything else in the config is copied through byte for byte. A
selector with no local build keeps `sqlite:obo:`, so the download path (and its
failure) is unchanged for anything genuinely missing.

Usage:
    python scripts/resolve_ontology_config.py --out <path>
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG = REPO_ROOT / "conf" / "id_label_targets.yaml"

_OBO_SELECTOR = re.compile(r"sqlite:obo:([a-z0-9_]+)")


def oaklib_directory() -> Path:
    """Where OAK keeps its downloaded SQLite builds.

    pystow roots at ``$PYSTOW_HOME`` when set and ``~/.data`` otherwise; OAK's
    sqlite builds live in the ``oaklib`` module beneath it. Resolved rather than
    hardcoded so the tests' empty-``PYSTOW_HOME`` simulation is honoured.
    """
    home = os.environ.get("PYSTOW_HOME")
    root = Path(home) if home else Path.home() / ".data"
    return root / "oaklib"


def resolve(text: str, directory: Path | None = None) -> tuple[str, list[str]]:
    """Rewrite `sqlite:obo:<name>` to the local build, where one exists.

    Returns the new text and the names that were rewritten, so a caller can say
    what it did rather than claiming more than happened.
    """
    directory = directory or oaklib_directory()
    rewritten: list[str] = []

    def replace(match: re.Match[str]) -> str:
        name = match.group(1)
        database = directory / f"{name}.db"
        if not database.is_file() or database.stat().st_size == 0:
            return match.group(0)
        rewritten.append(name)
        return f"sqlite:{database}"

    return _OBO_SELECTOR.sub(replace, text), rewritten


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Resolve ontology selectors (#716).")
    parser.add_argument("-c", "--config", type=Path, default=DEFAULT_CONFIG)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args(argv)

    if not args.config.is_file():
        print(f"config not found: {args.config}", file=sys.stderr)
        return 2

    text, rewritten = resolve(args.config.read_text(encoding="utf-8"))
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(text, encoding="utf-8")

    if rewritten:
        print(
            f"resolved {len(rewritten)} ontolog(y/ies) to already-downloaded builds: "
            + ", ".join(sorted(rewritten)),
            file=sys.stderr,
        )
    else:
        print(
            "no already-downloaded builds found; every selector still says "
            "sqlite:obo: and will be fetched",
            file=sys.stderr,
        )
    print(args.out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
