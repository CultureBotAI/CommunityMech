"""Guard against wrong CHEBI groundings in the element enums.

`MetalElementEnum` and `RareEarthElementEnum` each map an element name to a
CHEBI id via the permissible value's ``meaning:``. Those ids are **not** covered
by ``validate-products`` (the id↔label gate only checks record-level
``term.{id,label}`` pairs), so they drifted silently: PALLADIUM was grounded to
CHEBI:33373 *promethium* (PR #206) and 13 rare-earth/INDIUM ids were off-by-one
within the CHEBI:333xx lanthanide block or digit-transposed — e.g. INDIUM →
*aluminium trifluoride*, YTTRIUM → *zinc dichloride* (PR #207).

This module is that missing gate. It runs in the ``validate-strict`` pytest step
(which already blocks merges) and needs no network:

* ``test_meanings_match_expected`` freezes the verified-correct mapping so any
  future hand-edit that changes an id must consciously update ``EXPECTED``.
* ``test_no_shared_meaning`` enforces that no two element PVs share a CHEBI id —
  an ontology-free invariant that directly catches the swap/duplication pattern
  (THULIUM and DYSPROSIUM both = CHEBI:33377, etc.).
* ``test_meanings_resolve_to_element_label`` additionally checks each id against
  its **canonical ChEBI label** — but only when the ChEBI sqlite is already
  present locally, so it never forces a multi-GB download in CI.

The ``EXPECTED`` ids were verified on 2026-07-18 against the local ChEBI build:
rare earths are grounded to the ``(3+)`` cation to match each enum
``description:`` "X(3+) cation"; Dy/Er/Tm have no ``(3+)`` term in ChEBI and are
grounded to the atom (CHEBI:33377 / :33379 / :33380).
"""

from pathlib import Path

import pytest
import yaml

SCHEMA = Path(__file__).parent.parent / "src" / "communitymech" / "schema" / "communitymech.yaml"

# Verified-correct element -> CHEBI id (2026-07-18, against the local ChEBI build).
EXPECTED = {
    "MetalElementEnum": {
        "COPPER": "CHEBI:29036",
        "IRON": "CHEBI:29033",
        "ZINC": "CHEBI:27363",
        "NICKEL": "CHEBI:49786",
        "COBALT": "CHEBI:48828",
        "VANADIUM": "CHEBI:27698",
        "URANIUM": "CHEBI:27214",
        "CHROMIUM": "CHEBI:28073",
        "LEAD": "CHEBI:25016",
        "LITHIUM": "CHEBI:49713",
        "GOLD": "CHEBI:29287",
        "SILVER": "CHEBI:30512",
        "PALLADIUM": "CHEBI:33363",
        "GALLIUM": "CHEBI:49631",
        "INDIUM": "CHEBI:49664",
        "TITANIUM": "CHEBI:33341",
        "MERCURY": "CHEBI:16793",
    },
    "RareEarthElementEnum": {
        "LANTHANUM": "CHEBI:49701",
        "CERIUM": "CHEBI:48782",
        "PRASEODYMIUM": "CHEBI:229784",
        "NEODYMIUM": "CHEBI:229785",
        "SAMARIUM": "CHEBI:49890",
        "EUROPIUM": "CHEBI:49591",
        "GADOLINIUM": "CHEBI:49618",
        "TERBIUM": "CHEBI:49902",
        "DYSPROSIUM": "CHEBI:33377",  # atom; ChEBI has no dysprosium(3+) cation
        "HOLMIUM": "CHEBI:49650",
        "ERBIUM": "CHEBI:33379",  # atom; ChEBI has no erbium(3+) cation
        "THULIUM": "CHEBI:33380",  # atom; ChEBI has no thulium(3+) cation
        "YTTERBIUM": "CHEBI:49980",
        "LUTETIUM": "CHEBI:49746",
        "YTTRIUM": "CHEBI:49962",
        "SCANDIUM": "CHEBI:231857",
    },
}


def _actual_meanings():
    """{enum_name: {permissible_value: meaning_curie}} for the two element enums."""
    enums = yaml.safe_load(SCHEMA.read_text())["enums"]
    out = {}
    for name in EXPECTED:
        pvs = enums[name]["permissible_values"]
        out[name] = {pv: body.get("meaning") for pv, body in pvs.items()}
    return out


@pytest.mark.parametrize("enum_name", list(EXPECTED))
def test_meanings_match_expected(enum_name):
    """Every element PV is grounded to its verified-correct CHEBI id."""
    assert _actual_meanings()[enum_name] == EXPECTED[enum_name]


def test_no_shared_meaning():
    """No two element permissible values share a CHEBI id (catches swaps/dupes)."""
    seen = {}
    for enum_name, pvs in _actual_meanings().items():
        for pv, meaning in pvs.items():
            if meaning in seen:
                pytest.fail(f"CHEBI id {meaning} reused by {seen[meaning]} and {enum_name}.{pv}")
            seen[meaning] = f"{enum_name}.{pv}"


def test_meanings_resolve_to_element_label():
    """Each meaning's canonical ChEBI label names its element.

    Skipped unless the ChEBI sqlite is already cached locally, so it never
    triggers a multi-GB download in CI. When present, this is the check that
    would have caught PALLADIUM→promethium and the rare-earth swaps at source.
    """
    chebi_db = Path.home() / ".data" / "oaklib" / "chebi.db"
    if not chebi_db.exists():
        pytest.skip("ChEBI sqlite not cached locally; skipping canonical-label check")

    from oaklib import get_adapter

    adapter = get_adapter(f"sqlite:{chebi_db}")
    problems = []
    for enum_name, pvs in _actual_meanings().items():
        for pv, meaning in pvs.items():
            label = adapter.label(meaning)
            if label is None:
                problems.append(f"{enum_name}.{pv} {meaning}: id absent from ChEBI")
            elif pv.lower() not in label.lower():
                problems.append(f"{enum_name}.{pv} {meaning}: label '{label}' does not name '{pv}'")
    assert not problems, "Element enum groundings disagree with ChEBI:\n" + "\n".join(problems)
