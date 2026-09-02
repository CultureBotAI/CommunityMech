"""Can the ontology checks run at all? Ask before running them (#708).

`s3.amazonaws.com/bbop-sqlite` answers **403 for every build** — ncbitaxon, go,
chebi, envo, uberon, cl — and the checks that consult OAK react to that in
incompatible ways:

* `linkml-term-validator` (Engine A) passes 328 files vacuously and dies on the
  329th with a raw `DownloadError` traceback, so its exit code stops meaning
  "label drift";
* `validate_id_label_correspondence.py` (Engine B) reports `ADAPTER_ERROR` for
  every term of every record — 6250+ rows — because a configured adapter that
  fails to LOAD is fatal there by design, and rightly so: it cannot tell a dead
  bucket from a broken config.

`label-correspondence` was red on `main` for two days as a result, on a
condition no PR caused and none could fix. That is how a real failure gets waved
through as "the flaky one".

**This is a POSITIVE reachability probe, not a reading of a checker's
wreckage.** Telling an outage apart from real drift by grepping a tool's stderr
for "DownloadError" would be deciding something is FINE from a substring, which
is exactly what CLAUDE.md's "a guard may narrow, never excuse" forbids (#700).
Asking first costs one adapter construction per ontology and answers an honest,
different question: *can this check run?*

**Why this lives here and not in the validator.**
`scripts/validate_id_label_correspondence.py` is a governed vendored artifact,
byte-identical across the Mech repos and pinned to a claw revision. Teaching it
a finer-grained `SKIPPED_UNREACHABLE_ADAPTER` verdict — so it still checks the
ontologies that ARE reachable instead of skipping wholesale — is the better fix,
and it belongs upstream in claw rather than as local drift.

Exit codes: 0 = every configured ontology is reachable; 3 = at least one pinned
ontology is unreachable; 2 = usage/config error.
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG = REPO_ROOT / "conf" / "id_label_targets.yaml"

# The ontology names this repository is allowed to ask OAK for.
#
# **This pin is what makes the whole thing safe, and it is not optional.** A
# typo'd ontology name raises the SAME `DownloadError` as a real outage —
# verified: `sqlite:obo:not_a_real_ontology_xyz` fails identically to
# `sqlite:obo:go`, and S3 answers 403 for a nonexistent key just as it does for
# a forbidden one, so neither the exception type nor the HTTP status separates
# them. Without this list, one typo in `conf/id_label_targets.yaml` would report
# an ontology "unreachable", skip its checks, and leave the gate reporting clean
# while checking nothing — #686's failure mode, reintroduced by the fix for #708.
#
# Two independent conditions, in this order: the exception type NARROWS the
# candidates, and this pin DECIDES.
PINNED_ONTOLOGY_NAMES: frozenset[str] = frozenset(
    {"chebi", "cl", "envo", "go", "ncbitaxon", "uberon"}
)

_OBO_SELECTOR_PREFIX = "sqlite:obo:"


def is_pinned_obo_selector(selector: str) -> bool:
    """True for ``sqlite:obo:<name>`` where <name> is pinned above.

    Anything else — a local path, another scheme, an unpinned name — is not
    eligible for the "unreachable" reading and stays a hard failure.
    """
    if not selector.startswith(_OBO_SELECTOR_PREFIX):
        return False
    return selector[len(_OBO_SELECTOR_PREFIX) :].strip().lower() in PINNED_ONTOLOGY_NAMES


def is_download_failure(exc: BaseException) -> bool:
    """Did this adapter load fail because the ontology could not be fetched?

    ``isinstance`` against pystow's real type rather than a name match: pystow is
    a hard dependency of oaklib, so the import is safe, and another library's
    class that happens to be called ``DownloadError`` must not count. This is
    only ever the NARROWING half — ``is_pinned_obo_selector`` authorises.
    """
    try:
        from pystow.utils import DownloadError
    except Exception:  # pragma: no cover - pystow is an oaklib dependency
        return False
    return isinstance(exc, DownloadError)


def configured_adapters(config_path: Path) -> dict[str, str]:
    """Every ``adapters:`` mapping in the id/label target config, flattened."""
    config: Any = yaml.safe_load(config_path.read_text(encoding="utf-8"))
    selectors: dict[str, str] = {}

    def walk(node: Any) -> None:
        if isinstance(node, dict):
            for key, value in node.items():
                if key == "adapters" and isinstance(value, dict):
                    selectors.update(value)
                else:
                    walk(value)
        elif isinstance(node, list):
            for item in node:
                walk(item)

    walk(config)
    return selectors


def prefixes_in_use(config_path: Path) -> set[str]:
    """CURIE prefixes that actually appear in the targets this config names.

    An ontology no record cites cannot change the answer: the validator builds
    an adapter lazily, per prefix encountered, so it never touches one nothing
    references. Blocking the whole check on it is pure loss -- and it happened.
    CI has no `cl.db`, the corpus has zero CL ids, and `validate-products`
    skipped 6288 checkable pairs because of it (#716).

    Reads the same `glob:` targets the validator does, and only id SLOTS: a
    CURIE quoted in a note is prose, not a claim (that mistake is recorded in
    `tests/test_every_ontology_id_resolves.py`).
    """
    config = yaml.safe_load(config_path.read_text(encoding="utf-8"))
    globs = [
        target["glob"]
        for target in (config.get("targets") or [])
        if isinstance(target, dict) and str(target.get("glob", "")).endswith(".yaml")
    ]

    found: set[str] = set()

    def walk(node: Any) -> None:
        if isinstance(node, dict):
            value = node.get("id")
            if isinstance(value, str) and ":" in value:
                found.add(value.split(":", 1)[0])
            for key, item in node.items():
                if key.endswith("_id") and isinstance(item, str) and ":" in item:
                    found.add(item.split(":", 1)[0])
                walk(item)
        elif isinstance(node, list):
            for item in node:
                walk(item)

    for pattern in globs:
        for path in sorted(REPO_ROOT.glob(pattern)):
            walk(yaml.safe_load(path.read_text(encoding="utf-8")) or {})
    return found


def unreachable_ontologies(config_path: Path) -> list[str]:
    """Configured prefixes IN USE whose pinned ontology cannot be reached now.

    "In use" is the load-bearing word -- see `prefixes_in_use`.
    """
    used = prefixes_in_use(config_path)
    unreachable = []
    for prefix, selector in sorted(configured_adapters(config_path).items()):
        if prefix not in used:
            continue
        try:
            from oaklib import get_adapter  # type: ignore[import-untyped]

            get_adapter(selector)
        except Exception as exc:
            if is_download_failure(exc) and is_pinned_obo_selector(selector):
                unreachable.append(prefix)
            # Anything else — a typo, a bad path, a corrupt db — is NOT reported
            # here. It is a real problem, and the checker this guards will fail
            # on it, which is the correct outcome.
    return unreachable


def oaklib_directory() -> Path:
    """Where OAK keeps its downloaded SQLite builds.

    `pystow` roots at ``$PYSTOW_HOME`` when set and ``~/.data`` otherwise, and
    OAK puts its sqlite builds in the ``oaklib`` module under that. Resolved the
    same way here rather than hardcoded, so the report below describes the
    directory actually in use — including under the empty-``PYSTOW_HOME``
    simulation the tests run.
    """
    home = os.environ.get("PYSTOW_HOME")
    root = Path(home) if home else Path.home() / ".data"
    return root / "oaklib"


def describe_cache(selectors: dict[str, str]) -> list[str]:
    """What is actually on disk where OAK looks, as report lines.

    Printed whenever something is unreachable, because "unreachable" on its own
    is not diagnosable. In CI it was actively misleading: the `oaklib-Linux-v1`
    cache restores 6.7 GB successfully — "Cache restored from key:
    oaklib-Linux-v1" — and every ontology was still reported unreachable, with
    nothing in the log to say whether the files were absent, misnamed, or
    somewhere else entirely (#707).
    """
    directory = oaklib_directory()
    lines = [f"  oaklib directory: {directory}"]
    if not directory.is_dir():
        lines.append("  it does not exist — nothing was ever downloaded or restored here")
        return lines

    entries = sorted(directory.iterdir())
    total = sum(entry.stat().st_size for entry in entries if entry.is_file())
    lines.append(f"  {len(entries)} entries, {total / 1e9:.2f} GB")
    for prefix, selector in sorted(selectors.items()):
        if not selector.startswith(_OBO_SELECTOR_PREFIX):
            continue
        name = selector[len(_OBO_SELECTOR_PREFIX) :]
        found = []
        for suffix in (".db", ".db.gz"):
            candidate = directory / f"{name}{suffix}"
            if candidate.exists():
                found.append(f"{candidate.name} {candidate.stat().st_size / 1e9:.2f} GB")
        lines.append(
            f"    {prefix:<12} {', '.join(found) if found else 'no .db or .db.gz present'}"
        )
    return lines


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Probe ontology reachability (#708).")
    parser.add_argument("-c", "--config", type=Path, default=DEFAULT_CONFIG)
    args = parser.parse_args(argv)

    if not args.config.is_file():
        print(f"config not found: {args.config}", file=sys.stderr)
        return 2

    unreachable = unreachable_ontologies(args.config)
    if unreachable:
        print("unreachable ontologies: " + ", ".join(unreachable), file=sys.stderr)
        for line in describe_cache(configured_adapters(args.config)):
            print(line, file=sys.stderr)
        return 3
    print("all configured ontologies are reachable")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
