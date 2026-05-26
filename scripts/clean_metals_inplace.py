#!/usr/bin/env python3
"""Surgical removal of false-positive entries from metals_present.

The original `metal_extraction.py` used plain substring matching against
2-character element symbols ('ti' for TITANIUM, 'au' for GOLD, 'pd' for
PALLADIUM). Those symbols matched inside unrelated words like
'characteristic', 'australia', 'phosphodiesterase' and salted
`metals_present` with elements the source paper never discusses.

This script removes those false positives **only**. Specifically: for
each metal currently listed in a community's `metals_present`, if its
keyword set contains a known-ambiguous short symbol (`ti`, `au`, `pd`)
and *none* of its unambiguous keywords (full word, ionic forms with
charge characters, +ous/+ic adjectival forms) appears anywhere in the
file as a word-bounded token, the entry is removed. Everything else is
left exactly as found.

Out of scope deliberately:

- `metal_notes` and `metal_relevance` are never touched. Curator-authored
  values in those fields would otherwise be silently clobbered.
- Adding new metal entries is also out of scope. The fixed extractor
  may find legitimate metals the old buggy run missed (e.g., via CHEBI
  tier-1 matching), but adding them here would surprise curators and
  conflate "fix bug" with "expand annotations." Run
  `scripts/backfill_metals.py --dry-run` to inspect missing additions.
- `rare_earth_elements_present` is left alone because no REE keyword is
  short enough to false-match the substring pattern that affects metals.

Usage:
    uv run python scripts/clean_metals_inplace.py            # dry-run (default)
    uv run python scripts/clean_metals_inplace.py --apply    # write changes

The script self-bootstraps `src/` onto `sys.path`, so PYTHONPATH does
not need to be set when invoking it directly.

History
-------
Originally this script mutated each YAML in place via regex/line edits
on the raw text and `path.write_text(string)`. That bypassed the
write-time validation gate and never recorded a CurationEvent — both
flagged by the writers audit (PR #85). This rewrite loads the document
through `yaml.safe_load`, mutates the in-memory dict, records a
`CLEAN_METAL_FIELDS` curation event, and writes back through
`write_validated_community` (with backup-restore on validation failure,
matching the apply_pmc_conversions / link_growth_media pattern).

The cleaning semantics are preserved verbatim: the same ambiguous-symbol
table is consulted, and the same word-bounded evidence search runs over
the document minus its `metals_present` block. The only externally
visible difference is that the file is now re-emitted as canonical YAML
(comments and incidental formatting are not preserved across the
roundtrip — this is the same cost paid by every other validated-writer
script in the repo).
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from communitymech.curate.curation_event import record_curation_event
from communitymech.metal_extraction import keyword_in_text
from communitymech.validation.write_validated import (
    ValidationFailedError,
    write_validated_community,
)

# Metals whose keyword list contains a short symbol that the old buggy
# substring matcher false-fired on. For each, the "unambiguous" tokens
# are the keywords that are safe to match with word boundaries because
# they cannot appear inside an unrelated English or scientific word.
AMBIGUOUS_METAL_KEYWORDS: dict[str, list[str]] = {
    "TITANIUM": ["titanium", "ti4+"],
    "GOLD": ["gold", "au3+"],
    "PALLADIUM": ["palladium", "pd2+"],
}


def _evidence_text(doc: dict) -> str:
    """Serialize ``doc`` minus ``metals_present`` for word-bounded keyword search.

    The original (text-based) implementation built the evidence string by
    concatenating every line of the source file *except* the
    ``metals_present:`` block, so that an ambiguous entry would never
    self-satisfy by matching its own listing. We mirror that exclusion
    here by stripping the key from a shallow copy before dumping.

    Caveat — this is a near-but-not-perfect equivalent of the raw-text
    view: ``yaml.safe_dump`` drops YAML comments and may reflow scalars
    (e.g. line widths on long descriptions). Practically, the keywords
    we search for (``zinc``, ``copper``, ``calcium``, …) live in
    ``description``, ``ecological_state``, evidence ``snippet`` values,
    and other YAML *content* — never in YAML comments. So the on-disk
    behavior is identical for the corpus today. If a future workflow
    starts encoding evidence in YAML comments, this assumption breaks
    and the function should switch to ``path.read_text()`` with a
    ``metals_present`` line-strip filter to preserve full fidelity.
    """
    scratch = {k: v for k, v in doc.items() if k != "metals_present"}
    return yaml.safe_dump(scratch, allow_unicode=True, sort_keys=False)


def clean_metal_fields_in_doc(doc: dict) -> tuple[list[str], list[str]]:
    """Remove false-positive ambiguous metals from ``doc['metals_present']``.

    Mutates ``doc`` in place. Returns ``(removed, kept)`` so callers can
    log what changed. When ``metals_present`` is missing, empty, or has
    no entries to drop, returns ``([], existing_list)`` and leaves the
    doc untouched.
    """
    entries = doc.get("metals_present")
    if not entries:
        return [], list(entries or [])

    evidence = _evidence_text(doc)

    kept: list[str] = []
    removed: list[str] = []
    for entry in entries:
        unambig = AMBIGUOUS_METAL_KEYWORDS.get(entry)
        if unambig is None:
            kept.append(entry)
            continue
        if any(keyword_in_text(kw, evidence) for kw in unambig):
            kept.append(entry)
        else:
            removed.append(entry)

    if removed:
        doc["metals_present"] = kept
    return removed, kept


def clean_file(path: Path, apply: bool) -> tuple[bool, str]:
    """Load, clean, and (if ``apply``) write a single community YAML.

    Returns ``(changed, summary)``. ``changed`` is True iff at least one
    false-positive metal was removed. ``summary`` is a human-readable
    one-liner suitable for printing alongside the file name.
    """
    with path.open() as f:
        doc = yaml.safe_load(f)
    if not isinstance(doc, dict):
        return False, ""

    removed, kept = clean_metal_fields_in_doc(doc)
    if not removed:
        return False, ""

    summary = f"  removed: {removed}; kept: {kept}"

    if not apply:
        return True, summary

    record_curation_event(
        doc,
        curator="clean_metals_inplace",
        action="CLEAN_METAL_FIELDS",
        changes=(
            f"Removed {len(removed)} false-positive metal(s) from metals_present: "
            f"{', '.join(removed)}"
        ),
    )

    # Restore-on-failure pattern (matches apply_pmc_conversions /
    # link_growth_media from PR #85): rename to .bak first so a failed
    # write doesn't leave the original missing on disk. Catch BOTH
    # ValidationFailedError (the expected-error case, surfaced with a
    # short summary) and *any other* exception (disk error, permission
    # denied, unexpected serializer fault) so the bak file always gets
    # rolled back rather than leaving the user with `.yaml.bak_metals`
    # and no `.yaml`.
    backup = path.with_suffix(".yaml.bak_metals")
    path.rename(backup)
    try:
        write_validated_community(doc, path)
    except ValidationFailedError as exc:
        backup.rename(path)
        print(
            f"  ✗ validation failed for {path.name}: {exc.summary()} "
            "(original restored from backup)",
            file=sys.stderr,
        )
        return False, summary
    except BaseException:
        # Restore the backup before re-raising so the corpus is never
        # left with a missing canonical file.
        if backup.exists() and not path.exists():
            backup.rename(path)
        raise
    backup.unlink()  # success — drop the backup
    return True, summary


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without writing (default).",
    )
    group.add_argument(
        "--apply",
        action="store_true",
        help="Actually write changes back to disk.",
    )
    args = parser.parse_args()

    apply = args.apply  # dry-run is the default; --apply is the explicit opt-in

    community_dir = Path("kb/communities")
    files = sorted(community_dir.glob("*.yaml"))
    changed = 0
    for f in files:
        did_change, summary = clean_file(f, apply=apply)
        if did_change:
            changed += 1
            print(f"{f.name}")
            print(summary)

    verb = "changed" if apply else "would change"
    print(f"\n{verb} {changed}/{len(files)} files")
    if not apply:
        print("(dry-run; re-run with --apply to write)")


if __name__ == "__main__":
    main()
