"""Reject duplicate mapping keys in community YAML.

`linkml-validate` cannot catch this. It parses through PyYAML, which keeps the
**last** of two duplicate keys and reports nothing — so a record that silently
discards one of two curated values passes every other gate we have. Issue #289
documents two records where that is happening, and in one of them the value that
survives is a claim a previous PR deliberately retracted.

The same defect was briefly introduced mechanically: `scripts/gtdb_ground.py`
keyed its insertions by NCBITaxon id, and records that list one id many times
(28 *Variovorax* isolates in `GLBRC_Populus_Variovorax_SynCom28`) got a second
`gtdb_classification` written onto an already-grounded entry. Every affected file
still passed `linkml-validate`, which is what makes this worth a gate rather than
care.

`KNOWN_DUPLICATES` is pinned rather than merely skipped: fixing one of the two
records fails this test until it is removed from the list, so the waiver cannot
outlive the bug. Same pattern as ``EXPECTED`` in tests/test_enum_groundings.py.
"""

from __future__ import annotations

import collections
from pathlib import Path

import pytest
import yaml

from communitymech.paths import record_files

# Both record roots, not kb/communities alone. `data/isolates` holds the same
# root class -- 4 records with 66 snippets, 3 ecological_interactions and 3
# gtdb_classification blocks -- and this module could not see any of it (#689).
COMMUNITIES = Path(__file__).parent.parent / "kb/communities"

# Empty since #289 was fixed: both records that needed a curator decision have
# had one. Add an entry here only with an issue reference, and only when the
# choice of which value survives genuinely cannot be made in the same change.
KNOWN_DUPLICATES: dict[str, list[str]] = {}


class _DuplicateDetectingLoader(yaml.SafeLoader):
    """A SafeLoader that records duplicate keys instead of silently dropping them."""


def _find_duplicates(text: str) -> list[tuple[str, int]]:
    """Return (key, 1-based line) for every duplicated mapping key in ``text``."""
    found: list[tuple[str, int]] = []

    def construct_mapping(loader, node, deep=False):
        seen: collections.Counter = collections.Counter()
        for key_node, _ in node.value:
            key = loader.construct_object(key_node, deep=True)
            seen[key] += 1
            if seen[key] == 2:
                found.append((str(key), key_node.start_mark.line + 1))
        return yaml.SafeLoader.construct_mapping(loader, node, deep)

    loader = type("_Loader", (_DuplicateDetectingLoader,), {})
    loader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, construct_mapping)
    yaml.load(text, loader)  # noqa: S506 — subclass of SafeLoader
    return found


def _community_files() -> list[Path]:
    return record_files()


def test_there_are_community_files_to_check():
    """Guard against the glob silently matching nothing and the suite passing."""
    assert len(_community_files()) > 100


@pytest.mark.parametrize("path", _community_files(), ids=lambda p: p.name)
def test_no_unexpected_duplicate_keys(path: Path):
    """No community record may carry an unrecorded duplicate mapping key."""
    duplicates = _find_duplicates(path.read_text())
    keys = sorted({key for key, _ in duplicates})
    expected = sorted(KNOWN_DUPLICATES.get(path.name, []))

    if not expected:
        assert not duplicates, (
            f"{path.name} has duplicate mapping key(s) "
            f"{[f'{k} (line {ln})' for k, ln in duplicates]}. PyYAML keeps the last "
            f"of each pair and reports nothing, so one curated value is being "
            f"discarded at parse time while every other gate still passes. Fix the "
            f"record, or record it in KNOWN_DUPLICATES with an issue reference."
        )
        return

    assert keys == expected, (
        f"{path.name} is in KNOWN_DUPLICATES for {expected} but now has {keys}. "
        f"If the record was fixed, remove it from KNOWN_DUPLICATES (see #289); "
        f"if a new duplicate appeared, fix that one."
    )


def test_known_duplicates_are_all_real():
    """Every pinned record must still exist and still be duplicated.

    Stops the waiver list outliving the bug — a stale entry here would silently
    excuse a file that no longer needs excusing.
    """
    for name in KNOWN_DUPLICATES:
        path = COMMUNITIES / name
        assert path.exists(), f"{name} is in KNOWN_DUPLICATES but no longer exists"
        assert _find_duplicates(
            path.read_text()
        ), f"{name} no longer has duplicate keys — remove it from KNOWN_DUPLICATES."
