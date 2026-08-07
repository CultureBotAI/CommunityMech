"""Proof that `validate-references` checks something, and where it does not (#466).

#466 read the validator's output as a vacuous pass:

    Validation Summary:
      Total checks: 0
      All validations passed!

That reading is wrong, and the output invites it. `Total checks` is printed as
`len(all_results)` in the upstream CLI (`cli/validate.py`), and `all_results`
holds validation *issues* — so "Total checks: 0" means **no problems found**,
not "nothing was examined". A clean record prints 0 and always will.

Verified by planting: replacing a snippet in `taxonomy[0].evidence[0]` with
text that appears in no publication yields

    [ERROR] Text part not found as substring: 'ZZQQ ...'
    Location: taxonomy[0].evidence[0].snippet
    Total checks: 1 / Issues found: 1

So `EvidenceItem` snippets are genuinely validated against `references_cache/`.

Two real gaps remain, and this file pins the boundary between them so the next
reader does not have to re-derive it:

1. **A truncated snippet still passes**, because a quote cut mid-word is a
   substring of the source and substring matching is what the tool promises.
   That is why the eight snippets in #295/#465 survived — not vacuity.
   `tests/test_snippets_are_not_truncated.py` covers that class.

2. **`SupportingReference` is never checked at all.** It is the range of
   `Discussion.evidence`, and unlike `EvidenceItem` its `snippet` and
   `reference` carry no `implements:` annotation, so the plugin's field
   detection does not see them. 11 snippets across 8 records are unvalidated.
   Fixing it means editing `mech_shared.yaml`, which is vendored byte-identical
   and sha-pinned across the Mech repos, so it is filed rather than done here.

The tests below use the plugin directly rather than the CLI: no subprocess, no
network, and they read the same `references_cache/` the recipe does.
"""

from __future__ import annotations

import pathlib

import pytest
from linkml_runtime.utils.schemaview import SchemaView

REPO = pathlib.Path(__file__).parent.parent
SCHEMA = REPO / "src/communitymech/schema/communitymech.yaml"
CACHE = REPO / "references_cache"

# A reference with a cache entry, and a phrase genuinely in that entry.
CACHED_PMID = "PMID:28287150"
NONSENSE = "ZZQQ this sentence appears in no publication whatsoever XKCD"


@pytest.fixture(scope="module")
def plugin():
    from linkml_reference_validator.models import ReferenceValidationConfig
    from linkml_reference_validator.plugins.reference_validation_plugin import (
        ReferenceValidationPlugin,
    )

    instance = ReferenceValidationPlugin(config=ReferenceValidationConfig(cache_dir=CACHE))
    instance.schema_view = SchemaView(str(SCHEMA))
    return instance


def test_a_snippet_in_no_publication_is_rejected(plugin):
    """The canary. If this passes, `validate-references` proves nothing.

    Without it, a green run is indistinguishable from a broken tool — which is
    exactly the ambiguity #466 was filed on.
    """
    results = list(plugin._validate_excerpt(NONSENSE, CACHED_PMID, None, "probe"))
    assert results, (
        "the reference validator accepted text that appears in no publication, "
        f"so every green `just validate-references` run is vacuous (#466). "
        f"Checked {NONSENSE!r} against {CACHED_PMID}"
    )
    assert any("not found" in str(getattr(r, "message", r)).lower() for r in results)


def test_a_real_quote_from_the_cached_source_is_accepted(plugin):
    """The other half: it must not reject everything, which would be equally useless."""
    import yaml

    record = (
        REPO / "kb/communities/Geobacter_Clostridium_Interspecies_Electron_Transfer_Coculture.yaml"
    )
    document = yaml.safe_load(record.read_text())
    item = document["taxonomy"][0]["evidence"][0]

    results = list(plugin._validate_excerpt(item["snippet"], item["reference"], None, "probe"))
    assert results == [], (
        "a curated snippet that should match its cached source was rejected: "
        f"{[str(getattr(r, 'message', r)) for r in results]}"
    )


def test_evidence_item_exposes_the_slots_the_plugin_looks_for(plugin):
    """The annotations are what make the check reachable; without them it is silent.

    This is the difference between EvidenceItem and SupportingReference, and it
    is invisible in the validator's output — both simply produce no findings.
    """
    assert plugin._find_excerpt_fields("EvidenceItem") == ["snippet"]
    assert plugin._find_reference_fields("EvidenceItem") == ["reference"]


def test_the_supporting_reference_gap_is_still_open(plugin):
    """Pins a KNOWN GAP, and fails when it is closed — which is the point.

    `Discussion.evidence` has range `SupportingReference`, whose `snippet` and
    `reference` carry no `implements:`, so the plugin cannot see them and every
    discussion snippet is unchecked. The fix belongs in `mech_shared.yaml`,
    which is vendored byte-identical and sha-pinned across the Mech repos.

    Asserting the gap rather than ignoring it means whoever closes it gets a
    red test pointing at this docstring instead of a silent behaviour change.
    """
    schema_view = plugin.schema_view
    assert schema_view.get_class("SupportingReference"), "the class has been renamed"
    assert (
        schema_view.induced_slot("evidence", "Discussion").range == "SupportingReference"
    ), "Discussion.evidence no longer ranges on SupportingReference; update this test"

    assert plugin._find_excerpt_fields("SupportingReference") == [], (
        "SupportingReference now exposes an excerpt slot, so discussion snippets "
        "are validated and this known gap is closed. Delete this test, update "
        "the module docstring, and close the follow-up issue from #466."
    )


def test_the_gap_is_not_hypothetical(plugin):
    """Counts what is unchecked, so the follow-up issue has a real scope.

    A gap nobody can size gets deferred forever.
    """
    import yaml

    unchecked = 0
    for directory in ("kb/communities", "data/isolates", "kb/taxa"):
        for path in sorted((REPO / directory).glob("*.yaml")):
            document = yaml.safe_load(path.read_text()) or {}
            for discussion in document.get("discussions") or []:
                for item in (discussion or {}).get("evidence") or []:
                    if isinstance(item, dict) and item.get("snippet"):
                        unchecked += 1

    assert unchecked > 0, (
        "no discussion snippets remain, so the SupportingReference gap is moot "
        "and the tests above can be simplified"
    )
