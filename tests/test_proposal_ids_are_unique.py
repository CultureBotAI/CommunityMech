"""Every METPO id proposed under `proposals/` is proposed exactly once (#759).

#755 proposed `METPO:1007200`, `1007201` and `1007210`-`1007215` for a new
interaction-semantics cohort. All eight were already taken by
`metpo_communitymech_v1` — `METPO:1007214` most awkwardly, since it already
denotes the DIET *community category* and was being reused for the DIET
*interaction*.

The check that missed it was `grep -oE "10071[0-9]{2}"`, which cannot match
1007200 or anything above, so it reported a maximum of 1007193 while the real
maximum across cohorts is 1008132. A pattern too narrow to see the answer
returns a confident wrong one, which is worse than returning nothing.

There was no test over `proposals/` at all before this.
"""

from __future__ import annotations

import collections
import csv

from communitymech.paths import REPO_ROOT

PROPOSALS = REPO_ROOT / "proposals"


def _rows():
    """(id, label, file) for every ROBOT-template row across every cohort."""
    for path in sorted(PROPOSALS.glob("*/metpo_proposal_*_robot.tsv")):
        with path.open() as fh:
            for n, row in enumerate(csv.reader(fh, delimiter="\t")):
                # row 0 is the human header, row 1 the ROBOT directive row
                if n < 2 or not row or not row[0].startswith("METPO:"):
                    continue
                yield row[0], (row[1] if len(row) > 1 else ""), path.name


def test_no_id_is_proposed_twice():
    where = collections.defaultdict(list)
    for curie, label, filename in _rows():
        where[curie].append(f"{filename}: {label!r}")
    clashes = [f"{curie} -> " + " | ".join(v) for curie, v in sorted(where.items()) if len(v) > 1]
    assert clashes == [], (
        "these METPO ids are proposed more than once across `proposals/` (#759). "
        "Allocate from the maximum across ALL cohorts, not the one being "
        "extended:\n" + "\n".join(clashes)
    )


def test_the_check_can_actually_fail():
    """The duplicate detector must react to a duplicate.

    Pins the mechanism, not the data: a `_rows()` that silently yielded nothing —
    a renamed file, a changed header depth — would make the test above pass over
    an empty corpus.
    """
    rows = list(_rows())
    assert (
        len(rows) > 100
    ), f"_rows() found only {len(rows)} proposal rows; it is not reading the cohorts"
    seeded = [c for c, _, _ in rows] + [rows[0][0]]
    counts = collections.Counter(seeded)
    assert counts[rows[0][0]] == 2, "the duplicate detector cannot see a duplicate"


def test_every_row_declares_a_parent():
    """A ROBOT class row with no `SC %` value imports as a floating class."""
    orphans = []
    for path in sorted(PROPOSALS.glob("*/metpo_proposal_classes_robot.tsv")):
        with path.open() as fh:
            for n, row in enumerate(csv.reader(fh, delimiter="\t")):
                if n < 2 or not row or not row[0].startswith("METPO:"):
                    continue
                if len(row) < 5 or not row[4].strip():
                    orphans.append(f"{path.name}: {row[0]} {row[1] if len(row) > 1 else ''!r}")
    assert orphans == [], "these proposed classes declare no parent:\n" + "\n".join(orphans)
