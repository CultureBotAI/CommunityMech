"""An ontology id that resolves to nothing must not pass silently (#471).

`linkml-term-validator` documents `--lenient` as "don't fail when term IDs are
not found in ontology [default: no-lenient]", but the strict default does not
enforce it for bound `term.id` slots: it silently skips ids it cannot resolve.
#471 demonstrated it directly —

    ENVO:00002121  label -> "totally bogus label xyz"   =>  exit 1  Label mismatch
    ENVO:00002121  -> ENVO:99999999 (label unchanged)   =>  exit 0  Validation passed

— so a typo'd CURIE passes the binding gate, and the three curator-accepted
residuals below pass it by blindness rather than by being fixed. Confirmed today:
`CHEBI:75315`, `GO:0070812` and `NCBITaxon:1807132` all still resolve to None.

Engine B (`validate_id_label_correspondence.py`) does report ID_NOT_FOUND, and is
the only thing that does — but it takes `sqlite:obo:` selectors, which
re-download whenever a `.db.gz` is missing, so during the bbop-sqlite outage it
skips wholesale (#708, #716). This check is deliberately independent of it: it
opens the already-downloaded builds by path, which touches no network, and so
keeps working when the selector route does not (#707).

**Exceptions are read from `conf/id_label_targets.yaml`, never re-listed here.**
That file is where a curator records an accepted residual with its reason, and a
second copy would be one more thing to get out of step — the failure #690 and
#697 are both about.

Scope is the id SLOTS, not a regex over the file. An earlier version of this
measurement scanned the text and reported `CHEBI:49782` as unresolvable; it
appears only inside a note explaining that it was replaced, so the scan was
reading prose as data.
"""

from __future__ import annotations

import pathlib

import pytest
import yaml

from communitymech.ontology_adapters import OBO_DATABASES, ontology_adapter
from communitymech.paths import default_record_roots, taxon_descriptor_roots

REPO = pathlib.Path(__file__).parent.parent
CONFIG = REPO / "conf" / "id_label_targets.yaml"


def _record_files() -> list[pathlib.Path]:
    roots = {*default_record_roots(), *taxon_descriptor_roots()}
    return sorted(path for root in roots for path in root.glob("*.yaml"))


def _ids_in_slots(node: object, found: set[str]) -> None:
    """Every CURIE sitting in an id SLOT, ignoring prose."""
    if isinstance(node, dict):
        value = node.get("id")
        if isinstance(value, str) and ":" in value:
            found.add(value)
        for key, item in node.items():
            if key.endswith("_id") and isinstance(item, str) and ":" in item:
                found.add(item)
            _ids_in_slots(item, found)
    elif isinstance(node, list):
        for item in node:
            _ids_in_slots(item, found)


def _curies_by_prefix() -> dict[str, set[str]]:
    found: set[str] = set()
    for path in _record_files():
        _ids_in_slots(yaml.safe_load(path.read_text(encoding="utf-8")) or {}, found)
    by_prefix: dict[str, set[str]] = {}
    for curie in found:
        prefix = curie.split(":", 1)[0]
        if prefix in OBO_DATABASES:
            by_prefix.setdefault(prefix, set()).add(curie)
    return by_prefix


def _accepted() -> set[str]:
    """Curator-accepted residuals, from the config that already records them."""
    accepted: set[str] = set()

    def walk(node: object) -> None:
        if isinstance(node, dict):
            for key, value in node.items():
                if key == "exceptions" and isinstance(value, list):
                    for entry in value:
                        if isinstance(entry, dict) and isinstance(entry.get("id"), str):
                            accepted.add(entry["id"])
                else:
                    walk(value)
        elif isinstance(node, list):
            for item in node:
                walk(item)

    walk(yaml.safe_load(CONFIG.read_text(encoding="utf-8")))
    return accepted


def test_the_scan_finds_ids_and_exceptions():
    """Guard on the guard: an empty scan would make the check below vacuous."""
    by_prefix = _curies_by_prefix()
    total = sum(len(v) for v in by_prefix.values())
    assert total > 900, f"only {total} ontology ids found in id slots; the walk is broken"
    assert len(_accepted()) > 20, "no exceptions parsed from conf/id_label_targets.yaml"


@pytest.mark.parametrize("prefix", sorted(OBO_DATABASES))
def test_every_id_resolves_or_is_an_accepted_residual(prefix: str):
    """A CURIE that resolves to nothing is a typo unless a curator said otherwise."""
    curies = _curies_by_prefix().get(prefix)
    if not curies:
        pytest.skip(f"no {prefix} ids in the corpus")

    adapter = ontology_adapter(prefix)
    if adapter is None:
        pytest.skip(
            f"{prefix} is unavailable, so its ids were SKIPPED, NOT PASSED — "
            f"this run says nothing about them (#708)"
        )

    accepted = _accepted()
    unresolved = []
    for curie in sorted(curies):
        try:
            label = adapter.label(curie)
        except Exception:
            label = None
        if label is None and curie not in accepted:
            unresolved.append(curie)

    assert unresolved == [], (
        f"these {prefix} ids resolve to nothing and are not accepted residuals "
        f"in conf/id_label_targets.yaml. The LinkML binding gate cannot see this "
        f"— it silently skips ids it cannot resolve (#471) — so either the id is "
        f"a typo, or it needs an exception entry with a reason:\n  " + "\n  ".join(unresolved)
    )
