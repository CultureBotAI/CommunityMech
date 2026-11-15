"""Cache-only controls for native excerpt validation and reachable slots (#476).

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

The governed shared-schema repair now exposes SupportingReference snippets and
references, including Discussion.evidence. The real CLI regression controls in
test_reference_cli_coverage.py compare every snippet in three actual records and
reject a planted discussion snippet. Historical gap probes/reports are retained.

A truncated snippet can still pass, because a quote cut mid-word is a substring
of the source. tests/test_snippets_are_not_truncated.py covers that distinct
class. Neither a match nor complete comparison coverage proves scientific support.

The tests below use the plugin directly rather than the CLI: no subprocess, no
network, and they read the same `references_cache/` the recipe does.
"""

from __future__ import annotations

import pathlib
from unittest.mock import patch

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
    from linkml_reference_validator.etl.reference_fetcher import ReferenceFetcher
    from linkml_reference_validator.models import ReferenceValidationConfig
    from linkml_reference_validator.plugins.reference_validation_plugin import (
        ReferenceValidationPlugin,
    )

    instance = ReferenceValidationPlugin(config=ReferenceValidationConfig(cache_dir=CACHE))
    instance.schema_view = SchemaView(str(SCHEMA))

    # The direct matcher tests also use only committed cache bytes. Do not let
    # an unsupported canary trigger acquisition or full-text enrichment.
    def cache_only(fetcher, reference_id, force_refresh=False):
        assert not force_refresh
        return fetcher._load_from_disk(fetcher.normalize_reference_id(reference_id))

    with patch.object(ReferenceFetcher, "fetch", cache_only):
        yield instance


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

    Issue counters alone cannot show that a particular slot was traversed.
    """
    assert plugin._find_excerpt_fields("EvidenceItem") == ["snippet"]
    assert plugin._find_reference_fields("EvidenceItem") == ["reference"]


def test_supporting_reference_exposes_excerpt_and_reference_slots(plugin):
    """Keep the governed shared-schema repair reachable to native traversal."""
    schema_view = plugin.schema_view
    assert schema_view.get_class("SupportingReference"), "the class has been renamed"
    assert (
        schema_view.induced_slot("evidence", "Discussion").range == "SupportingReference"
    ), "Discussion.evidence no longer ranges on SupportingReference; update this test"

    assert plugin._find_excerpt_fields("SupportingReference") == ["snippet"]
    assert plugin._find_reference_fields("SupportingReference") == ["reference"]


def test_discussion_snippet_surfaces_exist_in_actual_records():
    """Presence makes the slot regression meaningful; it is not a coverage count."""
    import yaml

    present = 0
    for directory in ("kb/communities", "data/isolates", "kb/taxa"):
        for path in sorted((REPO / directory).glob("*.yaml")):
            document = yaml.safe_load(path.read_text()) or {}
            for discussion in document.get("discussions") or []:
                for item in (discussion or {}).get("evidence") or []:
                    if isinstance(item, dict) and item.get("snippet"):
                        present += 1

    assert present > 0, "No discussion snippets remain; reassess the actual-record controls"
