"""Guard every schema enum ``meaning:`` grounding against its ontology.

Enum ``meaning:`` ids are **not** covered by ``validate-products`` (the id↔label
gate only checks record-level ``term.{id,label}`` pairs), so they drifted
silently: PALLADIUM was grounded to CHEBI:33373 *promethium* (PR #206) and 13
rare-earth/INDIUM ids were off-by-one within the CHEBI:333xx block or
digit-transposed — e.g. INDIUM → *aluminium trifluoride*, YTTRIUM → *zinc
dichloride* (PR #207).

This module is that missing gate, generalised from the two element enums to
**every** grounded enum in the schema. It **auto-discovers** each permissible
value that carries a ``meaning:`` and validates it, so a newly grounded enum (or a
newly grounded value) is covered automatically — or fails until registered in
``EXPECTED``. It runs in the ``validate-strict`` pytest step (already a blocking
gate) and needs no network:

* ``test_all_meanings_match_expected`` compares the full discovered
  ``{enum: {value: meaning}}`` against the frozen ``EXPECTED`` map. A changed id,
  a new/removed grounded value, or a whole new grounded enum all fail here,
  forcing a conscious update + re-verification.
* ``test_no_shared_meaning_within_enum`` enforces that no two values inside one
  enum share an ontology id — the invariant that directly catches the
  swap/duplication pattern (THULIUM and DYSPROSIUM both = CHEBI:33377, etc.).
* ``test_meanings_resolve_canonically`` additionally checks each id against its
  **canonical ontology label** — for element enums the element name must appear —
  but only for prefixes whose OAK sqlite is already cached locally, so it never
  forces a multi-GB download in CI.

The ``EXPECTED`` ids were verified against the local ontology builds (element
enums 2026-07-18, all enums re-confirmed 2026-07-19). Rare earths are grounded to
the ``(3+)`` cation to match each enum ``description:`` "X(3+) cation"; Dy/Er/Tm
have no ``(3+)`` term in ChEBI and are grounded to the atom (CHEBI:33377 / :33379
/ :33380).
"""

from pathlib import Path

import pytest
import yaml

SCHEMA = Path(__file__).parent.parent / "src" / "communitymech" / "schema" / "communitymech.yaml"

# Frozen, verified element -> ontology id for every grounded enum in the schema.
# Auto-discovery (below) fails if the schema grows a grounded value not listed
# here, so this map must stay complete.
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
    "CultivationSystemEnum": {
        "BIOREACTOR_UNSPECIFIED": "OBI:0001046",  # "bioreactor"
    },
}

# Enums whose permissible-value names are element names, so the canonical label
# must literally contain the value name (a stronger check than mere resolution).
ELEMENT_ENUMS = frozenset({"MetalElementEnum", "RareEarthElementEnum"})

# ontology prefix -> local OAK sqlite filename under ~/.data/oaklib/
_OAK_DB = {"CHEBI": "chebi.db", "OBI": "obi.db"}


def _discover_meanings():
    """{enum_name: {permissible_value: meaning_curie}} for EVERY grounded enum."""
    enums = yaml.safe_load(SCHEMA.read_text())["enums"]
    out = {}
    for name, body in enums.items():
        grounded = {
            pv: (b or {}).get("meaning")
            for pv, b in ((body or {}).get("permissible_values") or {}).items()
            if (b or {}).get("meaning")
        }
        if grounded:
            out[name] = grounded
    return out


def test_all_meanings_match_expected():
    """Every grounded enum value maps to its verified-correct ontology id.

    Auto-discovers grounded enums from the schema, so a new/changed/removed
    grounding fails here until EXPECTED is updated and re-verified.
    """
    assert _discover_meanings() == EXPECTED


def test_no_shared_meaning_within_enum():
    """No two values inside one enum share an ontology id (catches swaps/dupes)."""
    problems = []
    for enum_name, pvs in _discover_meanings().items():
        seen = {}
        for pv, meaning in pvs.items():
            if meaning in seen:
                problems.append(f"{enum_name}: {meaning} reused by {seen[meaning]} and {pv}")
            seen[meaning] = pv
    assert not problems, "Duplicate enum groundings:\n" + "\n".join(problems)


def test_meanings_resolve_canonically():
    """Each meaning resolves to a non-obsolete term whose label fits the value.

    Runs per ontology prefix only when that prefix's OAK sqlite is already cached
    locally, so it never triggers a multi-GB download in CI. For element enums the
    element name must appear in the label — the check that catches a wrong id at
    source (PALLADIUM→promethium, INDIUM→aluminium trifluoride, ...).
    """
    from oaklib import get_adapter

    adapters = {}
    checked_prefixes = set()
    problems = []
    for enum_name, pvs in _discover_meanings().items():
        for pv, meaning in pvs.items():
            prefix = meaning.split(":")[0]
            db = _OAK_DB.get(prefix)
            if db is None:
                problems.append(f"{enum_name}.{pv}: no OAK db registered for prefix {prefix}")
                continue
            db_path = Path.home() / ".data" / "oaklib" / db
            if not db_path.exists():
                continue  # ontology not cached locally; skip this prefix's checks
            checked_prefixes.add(prefix)
            adapter = adapters.setdefault(prefix, get_adapter(f"sqlite:{db_path}"))
            label = adapter.label(meaning)
            if label is None:
                problems.append(f"{enum_name}.{pv} {meaning}: id absent from {prefix}")
            elif label.lower().startswith("obsolete"):
                problems.append(f"{enum_name}.{pv} {meaning}: obsolete term '{label}'")
            elif enum_name in ELEMENT_ENUMS and pv.lower() not in label.lower():
                problems.append(f"{enum_name}.{pv} {meaning}: label '{label}' does not name '{pv}'")

    if not checked_prefixes:
        pytest.skip("no ontology sqlite cached locally; skipping canonical-label check")
    assert not problems, "Enum groundings disagree with the ontology:\n" + "\n".join(problems)
