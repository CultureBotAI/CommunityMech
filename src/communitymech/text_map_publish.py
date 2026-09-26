"""Validate and stage the configured semantic map before Pages deployment."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from communitymech.text_map_site import prepare_text_map


def publish(root: Path) -> dict:
    with prepare_text_map(root) as ready:
        if ready is not None:
            ready.stage(root / "docs")
        return {"enabled": ready is not None}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    args = parser.parse_args(argv)
    print(json.dumps(publish(args.root.resolve()), sort_keys=True))
    return 0
