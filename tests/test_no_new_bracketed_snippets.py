"""A snippet containing `[` can never be validated while #622 stands.

`validate-references` removes a bracket **and its contents** from the query
before matching (`_split_query`, supporting_text_validator.py:308) but not from
the reference text, whose normalisation strips only the bracket *characters*. So
`[NiFe]` becomes nothing on one side and `nife` on the other, and a verbatim
quote fails by construction:

    content normalised -> '... expression of genes for nife hydrogenases ...'
    query   normalised -> '... expression of genes for hydrogenases'

The consequence is not a noisy gate. It is that **a bracketed snippet is
unvalidatable**: nothing in the repo can confirm it against its source, so the
evidence it carries is unchecked in a KB whose premise is that every claim is
checked. Three separate snippets hit this during #183 curation, and two of the
three were ordinary citation markers — `Kester et al. [ 50 ]`, `(0 h [before
labeling/rewetting]` — which makes a large share of Methods prose unquotable.

This is a guard against a **tool limitation**, not a rule about good quoting.
The four existing snippets below are correct; they are pinned so their number
cannot grow silently. **Delete this file when #622 is fixed upstream** — at
which point the pin becomes the thing that is wrong.
"""

from __future__ import annotations

import pathlib

import yaml

REPO = pathlib.Path(__file__).parent.parent


def _record_dirs() -> list[str]:
    """Record directories, read from the id/label gate's config rather than listed.

    The repo already spells this set out in six separate places and they
    disagree — three GTDB tests omit `kb/taxa` (#656). A seventh hardcoded copy
    would mean a new record surface is silently unguarded here too, which is the
    "list that cannot notice a new member" failure this repo keeps hitting
    (#635, #471, #630).

    `conf/id_label_targets.yaml` enumerates the surfaces carrying curated
    (id, label) pairs and is loaded by a blocking gate, so it is the closest
    thing to a canonical list. Its non-YAML target (the KGX TSV export) is
    dropped: it holds no snippets.
    """
    config = yaml.safe_load((REPO / "conf/id_label_targets.yaml").read_text(encoding="utf-8"))
    globs = [t["glob"] for t in config["targets"] if t.get("glob", "").endswith(".yaml")]
    return sorted({glob.rsplit("/", 1)[0] for glob in globs})


# Snippets that already contain a bracket, with what is known about each. Keyed
# by (record, the bracketed fragment) so a DIFFERENT bracketed snippet in the
# same record still fails.
_KNOWN_BRACKETED = {
    ("Asgard_Wetland_Soil_Methanogenesis_Substrate_Community.yaml", "[NiFe]"): (
        "Verbatim in a 368 KB cached full text. The original #622 example."
    ),
    # Note the U+2010 HYPHEN in "poly(3‐hydroxybutyrate)" -- the fragment is kept
    # short and stops before it, so this pin does not depend on reproducing an
    # exotic dash correctly.
    ("Synechococcus_Pseudomonas_PhotoPHA_DNT_Coculture.yaml", "[e.g. poly(3"): (
        "Verbatim in a 156 KB cached full text."
    ),
    ("Syntrophomonas_Methanococcus_Butyrate_Growth_Coordination_Coculture.yaml", "[v/v]"): (
        "Verbatim in a 157 KB cached full text; the gas ratio N2:CO2 (80:20 [v/v])."
    ),
    ("Maize_Root_Simplified_Community.yaml", "[0.8% (wt/vol)]"): (
        "NOT confirmed either way: the cache for PMID:28275097 is 3.4 KB with no "
        "full-text marker, so it is abstract-only and absence is not reportable "
        "from it (the #605 rule). Recheck once its full text is cached."
    ),
}


def _snippets() -> list[tuple[str, str]]:
    """(record filename, snippet) for every snippet in the KB."""
    found = []
    for directory in _record_dirs():
        for path in sorted((REPO / directory).glob("*.yaml")):
            document = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
            stack = [document]
            while stack:
                node = stack.pop()
                if isinstance(node, dict):
                    if isinstance(node.get("snippet"), str):
                        found.append((path.name, node["snippet"]))
                    stack.extend(node.values())
                elif isinstance(node, list):
                    stack.extend(node)
    return found


def _known_for(record: str, snippet: str) -> str | None:
    for (known_record, fragment), reason in _KNOWN_BRACKETED.items():
        if record == known_record and fragment in snippet:
            return reason
    return None


def test_the_scan_finds_snippets_at_all():
    """A walker that found nothing would make the gate below vacuous."""
    snippets = _snippets()
    assert len(snippets) > 5000, f"only {len(snippets)} snippets found; the walk is broken"


def test_no_new_bracketed_snippet_is_added():
    """The gate. A bracketed snippet cannot be validated, so it must not be new."""
    offenders = [
        f"  {record}: {snippet[:90]!r}"
        for record, snippet in _snippets()
        if "[" in snippet and _known_for(record, snippet) is None
    ]
    assert not offenders, (
        "these snippets contain '[', which validate-references cannot match: it "
        "strips the bracket AND its contents from the query but not from the "
        "reference text, so a verbatim quote fails by construction (#622). The "
        "quote is not wrong -- it is unverifiable, which is worse in a KB where "
        "every claim is meant to be checked. Choose a span that avoids the "
        "bracket, or add it below with a reason if it must stay:\n" + "\n".join(offenders)
    )


def test_every_known_bracketed_snippet_still_exists():
    """A pin for a snippet that has been fixed or removed is dead weight.

    Without this, the allow-list keeps excusing records that no longer need it
    and quietly grows -- the failure mode that emptied the #529 waiver list.
    """
    present = {(record, snippet) for record, snippet in _snippets() if "[" in snippet}
    stale = [
        f"  {record} / {fragment!r}"
        for (record, fragment) in _KNOWN_BRACKETED
        if not any(r == record and fragment in s for r, s in present)
    ]
    assert not stale, (
        "these entries no longer match any bracketed snippet, so the pin is dead "
        "and should be removed (or #622 is fixed and this whole file should go):\n"
        + "\n".join(stale)
    )


def test_the_record_directories_come_from_config_and_are_real():
    """The derivation in #656 is now the untested part, so test it.

    Guards both ends: that the config still yields the surfaces this gate must
    walk, and that each one exists. A config edit that dropped a directory would
    otherwise shrink this gate's coverage silently.
    """
    directories = _record_dirs()
    assert set(directories) == {"kb/communities", "kb/taxa", "data/isolates"}, directories
    for directory in directories:
        path = REPO / directory
        assert path.is_dir(), f"{directory} is configured but does not exist"
        assert list(path.glob("*.yaml")), f"{directory} holds no YAML records"
