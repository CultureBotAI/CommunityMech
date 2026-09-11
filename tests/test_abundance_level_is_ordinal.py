"""`abundance_level` ranks members within a record; it is not a percentage (#748).

The enum's values used to name bands — DOMINANT >1%, ABUNDANT 0.1-1%, COMMON
0.01-0.1%, RARE <0.01%. Nothing checked them, and the corpus never meant them.
Restricting to `community_origin: SYNTHETIC` records of at most four members,
where every member necessarily exceeds 1% of a closed community, **76 of 91
assignments claimed the member was below 1%** — off by up to three orders of
magnitude, and invisible to `validate`, `validate-strict`, `validate-terms` and
the network audit alike, because none of them can check a *pick* against
evidence.

The other half of the story is that the numeric slots already exist.
`relative_abundance` and `absolute_abundance` landed in #161 and are used by
**zero** taxa, so the enum was carrying a job it was never checked on while the
slot built for that job sat empty.

These tests pin the resolution: the descriptions must stay ordinal, and if
anyone starts populating the numeric slot the two must not contradict each
other.
"""

from __future__ import annotations

import yaml

from communitymech.paths import REPO_ROOT, record_files

SCHEMA = REPO_ROOT / "src" / "communitymech" / "schema" / "communitymech.yaml"
ORDER = ["RARE", "COMMON", "ABUNDANT", "DOMINANT"]

# 0 as of #748. Not a ceiling — a tripwire. The consistency check below is
# vacuous while this is 0, and saying so here is the honest form of a test that
# cannot yet exercise its own subject.
TAXA_WITH_A_NUMBER = 0


def _enum() -> dict:
    schema = yaml.safe_load(SCHEMA.read_text())
    return schema["enums"]["AbundanceEnum"]


def test_no_value_names_a_percentage_band():
    """The exact defect: a value description that reads as a measured share."""
    offenders = []
    for name, body in _enum()["permissible_values"].items():
        text = (body or {}).get("description", "")
        if "%" in text:
            offenders.append(f"{name}: {text.strip()[:80]}")
    assert offenders == [], (
        "these AbundanceEnum values describe a percentage band again. The corpus "
        "does not use them that way and nothing enforces it; put the number in "
        "`relative_abundance` instead (#748):\n" + "\n".join(offenders)
    )


def test_the_enum_says_the_scale_is_within_record():
    """Asserted positively — an absent phrase would pass on a description that
    simply dropped the reasoning."""
    text = _enum().get("description", "")
    assert "within" in text.lower() and "record" in text.lower(), (
        "AbundanceEnum's description no longer says the rank is within a record. "
        "That is the whole content of the #748 decision; without it the next "
        "reader re-derives percentages."
    )
    assert "relative_abundance" in text, (
        "AbundanceEnum's description should point at `relative_abundance` as the "
        "home for a measured share, or curators will keep encoding numbers here."
    )


def _taxa():
    for path in record_files():
        doc = yaml.safe_load(path.read_text()) or {}
        for taxon in doc.get("taxonomy") or []:
            yield path.name, taxon


def test_the_numeric_slot_is_still_unused():
    """When this changes, the consistency check below stops being vacuous."""
    with_number = [n for n, t in _taxa() if t.get("relative_abundance") is not None]
    assert len(with_number) == TAXA_WITH_A_NUMBER, (
        f"{len(with_number)} taxa now carry `relative_abundance`, expected "
        f"{TAXA_WITH_A_NUMBER}. That is good — but it means "
        f"test_level_and_number_do_not_contradict is no longer vacuous, so read "
        f"its result rather than its pass: {sorted(set(with_number))[:5]}"
    )


def test_level_and_number_do_not_contradict():
    """Within one record, a higher `abundance_level` may not sit on a smaller
    `relative_abundance` than a lower one.

    Vacuous while no taxon carries a number; the test above is what notices.
    """
    by_record: dict[str, list[tuple[str, float]]] = {}
    for name, taxon in _taxa():
        level, value = taxon.get("abundance_level"), taxon.get("relative_abundance")
        if level in ORDER and value is not None:
            by_record.setdefault(name, []).append((level, float(value)))

    conflicts = []
    for name, entries in by_record.items():
        for i, (level_a, value_a) in enumerate(entries):
            for level_b, value_b in entries[i + 1 :]:
                if ORDER.index(level_a) > ORDER.index(level_b) and value_a < value_b:
                    conflicts.append(f"{name}: {level_a}={value_a} but {level_b}={value_b}")
    assert conflicts == [], (
        "these records rank two members one way by `abundance_level` and the "
        "other way by `relative_abundance` (#748):\n" + "\n".join(conflicts)
    )
