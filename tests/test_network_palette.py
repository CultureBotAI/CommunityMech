"""Gate the per-community network palette on enum coverage and CVD separation.

The interaction colours in ``templates/community.html`` were hand-picked and had
drifted into two failure modes that nothing caught (issues #269, #271):

* **Silent enum drift.** The palette is a literal list in the template. A tenth
  ``InteractionTypeEnum`` value would not fail any gate — it would just render as
  a grey "Other" swatch and a grey rectangle on every affected page, because the
  template falls back to ``unmapped_color`` for unknown keys. Generated output
  that still builds and still looks plausible is the hardest kind to notice.
* **Indistinguishable colours.** COMPETITION ``#ef4444`` and PREDATION
  ``#dc2626`` sat ΔE 10.7 apart in *normal* vision, and MUTUALISM/SYNTROPHY
  collapsed to ΔE 4.1 under deuteranopia — the two most common interaction types
  after cross-feeding. Ten of 55 swatch pairs were below ΔE 15.

Interaction type is carried by fill colour alone in that diagram (every
interaction is the same rounded rectangle), so separation is load-bearing until
issue #270 adds a redundant channel. These tests pin both properties. They are
pure arithmetic — no network, no ontology downloads — so they run in the
blocking ``validate-strict`` pytest step.

Colour-vision deficiency is simulated with the Viénot–Brettel–Mollon (1999)
LMS-plane projection, and distances are CIE76 ΔE in L*a*b*. Tritanopia is
excluded from the threshold: it affects ~0.01% of people, and no nine-colour set
survives all three deficiency types at once (see #270). Tritan collisions are
reported by ``test_tritan_collisions_are_documented`` rather than enforced.
"""

from __future__ import annotations

import ast
import colorsys
import itertools
import math
import re
from pathlib import Path

import pytest
import yaml

TEMPLATE = Path(__file__).parent.parent / "src/communitymech/templates/community.html"
SCHEMA = Path(__file__).parent.parent / "src/communitymech/schema/communitymech.yaml"

# Minimum CIE76 ΔE required between any two swatches under normal vision,
# protanopia and deuteranopia. The shipped palette measures 15.4; the palette it
# replaced measured 0.0 (taxon and MUTUALISM were the same hex).
MIN_SEPARATION = 15.0

# Enum whose permissible values the palette must cover exactly.
INTERACTION_ENUM = "InteractionTypeEnum"


# --------------------------------------------------------------------------
# Extracting the palette from the template
# --------------------------------------------------------------------------


def _jinja_set(name: str) -> str:
    """Return the raw value assigned by ``{%- set <name> = ... -%}``."""
    text = TEMPLATE.read_text()
    match = re.search(
        r"\{%-?\s*set\s+" + re.escape(name) + r"\s*=\s*(.*?)\s*-?%\}",
        text,
        re.DOTALL,
    )
    assert match, f"{name} not found in {TEMPLATE.name} — did the template move?"
    return match.group(1)


def _palette() -> dict[str, str]:
    """The interaction-type → colour map declared in the template."""
    entries = ast.literal_eval(_jinja_set("interaction_legend"))
    return {e["key"]: e["color"] for e in entries}


def _labels() -> dict[str, str]:
    entries = ast.literal_eval(_jinja_set("interaction_legend"))
    return {e["key"]: e["label"] for e in entries}


def _neutrals() -> dict[str, str]:
    """Swatches that are not interaction types but share the diagram."""
    return {
        "_taxon": ast.literal_eval(_jinja_set("taxon_color")),
        "_unmapped": ast.literal_eval(_jinja_set("unmapped_color")),
    }


def _enum_values() -> set[str]:
    schema = yaml.safe_load(SCHEMA.read_text())
    enum = schema["enums"][INTERACTION_ENUM]
    return set(enum["permissible_values"])


# --------------------------------------------------------------------------
# Colour science
# --------------------------------------------------------------------------

_RGB2LMS = ((0.31399, 0.63951, 0.04649), (0.15537, 0.75789, 0.08670), (0.01775, 0.10945, 0.87262))
_LMS2RGB = (
    (5.47221, -4.64196, 0.16963),
    (-1.12524, 2.29317, -0.16789),
    (0.02980, -0.19318, 1.16364),
)
_DEFICIENCY = {
    "protan": ((0, 1.05118294, -0.05116099), (0, 1, 0), (0, 0, 1)),
    "deutan": ((1, 0, 0), (0.9513092, 0, 0.04264942), (0, 0, 1)),
    "tritan": ((1, 0, 0), (0, 1, 0), (-0.86744736, 1.86727089, 0)),
}


def _hex_to_rgb(value: str) -> tuple[float, float, float]:
    value = value.lstrip("#")
    assert len(value) == 6, f"expected a 6-digit hex colour, got {value!r}"
    return tuple(int(value[i : i + 2], 16) / 255 for i in (0, 2, 4))  # type: ignore[return-value]


def _linearize(channel: float) -> float:
    return channel / 12.92 if channel <= 0.04045 else ((channel + 0.055) / 1.055) ** 2.4


def _apply(matrix, vector):
    return tuple(sum(matrix[i][j] * vector[j] for j in range(3)) for i in range(3))


def _simulate(rgb: tuple[float, float, float], kind: str) -> tuple[float, float, float]:
    """Project a colour onto the dichromat plane for ``kind``."""
    linear = tuple(_linearize(c) for c in rgb)
    projected = _apply(_LMS2RGB, _apply(_DEFICIENCY[kind], _apply(_RGB2LMS, linear)))
    return tuple(min(max(c, 0.0), 1.0) for c in projected)  # type: ignore[return-value]


def _lab(rgb: tuple[float, float, float]) -> tuple[float, float, float]:
    r, g, b = (_linearize(c) for c in rgb)
    x = 0.4124 * r + 0.3576 * g + 0.1805 * b
    y = 0.2126 * r + 0.7152 * g + 0.0722 * b
    z = 0.0193 * r + 0.1192 * g + 0.9505 * b

    def f(t: float) -> float:
        return t ** (1 / 3) if t > 0.008856 else 7.787 * t + 16 / 116

    fx, fy, fz = f(x / 0.95047), f(y / 1.0), f(z / 1.08883)
    return (116 * fy - 16, 500 * (fx - fy), 200 * (fy - fz))


def _delta_e(a: str, b: str, kind: str | None) -> float:
    ra, rb = _hex_to_rgb(a), _hex_to_rgb(b)
    if kind:
        ra, rb = _simulate(ra, kind), _simulate(rb, kind)
    return math.dist(_lab(ra), _lab(rb))


def _all_swatches() -> dict[str, str]:
    return {**_palette(), **_neutrals()}


# --------------------------------------------------------------------------
# Tests
# --------------------------------------------------------------------------


def test_palette_covers_the_interaction_enum_exactly():
    """Every InteractionTypeEnum value has a colour, and no colour is stale.

    Guards the silent-degradation path: an uncoloured type renders grey rather
    than failing, so only this comparison catches a newly added enum value.
    """
    palette, enum = set(_palette()), _enum_values()
    assert not (enum - palette), (
        f"{INTERACTION_ENUM} values with no colour in {TEMPLATE.name}: "
        f"{sorted(enum - palette)}. They would render as a grey 'Other' swatch "
        f"on every page instead of failing. Add them to `interaction_legend` "
        f"and rerun this module to confirm separation still holds."
    )
    assert not (palette - enum), (
        f"colours in {TEMPLATE.name} for values not in {INTERACTION_ENUM}: "
        f"{sorted(palette - enum)}. Remove them, or restore the enum value."
    )


def test_no_two_swatches_share_a_colour():
    """Distinct meanings must not share a hex — taxon and MUTUALISM once did."""
    swatches = _all_swatches()
    seen: dict[str, str] = {}
    for name, colour in swatches.items():
        assert colour not in seen, (
            f"{name} and {seen[colour]} are both {colour}; a taxon circle and an "
            f"interaction rectangle in the same colour cannot be told apart."
        )
        seen[colour] = name


@pytest.mark.parametrize("kind", [None, "protan", "deutan"])
def test_swatches_stay_separated_under_colour_vision_deficiency(kind):
    """No pair may fall below MIN_SEPARATION in normal, protan or deutan vision."""
    swatches = _all_swatches()
    worst = min(
        (
            (_delta_e(swatches[a], swatches[b], kind), a, b)
            for a, b in itertools.combinations(swatches, 2)
        ),
        key=lambda row: row[0],
    )
    distance, first, second = worst
    assert distance >= MIN_SEPARATION, (
        f"{first} ({swatches[first]}) and {second} ({swatches[second]}) are only "
        f"ΔE {distance:.1f} apart under {kind or 'normal'} vision, below the "
        f"{MIN_SEPARATION} floor. Interaction type is carried by colour alone "
        f"(see issue #270), so retune one of them rather than lowering the floor."
    )


def test_swatches_are_visible_on_both_themes():
    """Every swatch keeps some contrast against the light and dark backgrounds.

    The page ships a dark theme, so a colour tuned only for white can vanish.
    The floor is deliberately low — these are filled shapes carrying a darker
    stroke, not text, so WCAG's 4.5:1 text ratio does not apply.
    """
    for name, colour in _all_swatches().items():
        for background in ("#ffffff", "#101420"):
            luminances = sorted(
                sum(
                    coefficient * _linearize(channel)
                    for coefficient, channel in zip(
                        (0.2126, 0.7152, 0.0722), _hex_to_rgb(value), strict=True
                    )
                )
                for value in (colour, background)
            )
            ratio = (luminances[1] + 0.05) / (luminances[0] + 0.05)
            assert ratio >= 1.9, (
                f"{name} ({colour}) has only {ratio:.2f}:1 contrast against "
                f"{background}; it would be near-invisible on that theme."
            )


def test_labels_are_present_and_human_readable():
    """Each swatch carries a label — the legend is the only key to the colours."""
    for key, label in _labels().items():
        assert label and not label.isupper(), f"{key} needs a prose label, got {label!r}"
        assert label[0].isupper(), f"{label!r} should be sentence-cased"


def test_tritan_collisions_are_documented():
    """Record, without enforcing, which pairs collide under tritanopia.

    No nine-colour set survives protan, deutan *and* tritan simultaneously, so
    this is tracked rather than gated (issue #270 is the real fix). The test
    fails only if tritan gets *worse* than the palette shipped with, which would
    mean a retune traded away separation nobody measured.
    """
    swatches = _all_swatches()
    collisions = sorted(
        (round(_delta_e(swatches[a], swatches[b], "tritan"), 1), a, b)
        for a, b in itertools.combinations(swatches, 2)
        if _delta_e(swatches[a], swatches[b], "tritan") < MIN_SEPARATION
    )
    assert len(collisions) <= 4, (
        f"tritanopia collisions grew to {len(collisions)} pairs: {collisions}. "
        f"The palette shipped with 4; a retune should not make this worse."
    )


def test_hues_are_spread_around_the_wheel():
    """Interaction hues should not cluster — clustering is what caused #269.

    Three near-identical reds (COMPETITION, PREDATION, STRAIN_COMPETITION) were
    the original defect, so assert the hue gaps stay wide enough that no future
    edit can quietly recreate a same-family cluster.
    """
    hues = sorted(colorsys.rgb_to_hls(*_hex_to_rgb(c))[0] * 360 for c in _palette().values())
    gaps = [(b - a) for a, b in itertools.pairwise(hues)] + [360 - hues[-1] + hues[0]]
    assert min(gaps) >= 5.0, (
        f"two interaction hues are only {min(gaps):.1f}° apart (hues: "
        f"{[round(h) for h in hues]}); colours this close read as one family."
    )
