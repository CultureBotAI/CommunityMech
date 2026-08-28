"""How much of the corpus `DISCONNECTED` cannot reach, and why (#312).

`audit_community` credits a `COMMUNITY_LEVEL` interaction as connecting **every**
member of the record. Defensible — such an interaction asserts something holding
across the community rather than between a named pair — and unavoidably coarse,
because `EcologicalInteraction` has only `source_taxon` and `target_taxon` and no
way to say *which* members participate.

So the credit is all-or-nothing, and in a record carrying both kinds of edge a
taxon in no pairwise edge is credited by an unrelated community-level one. In
`GLBRC_Populus_Variovorax_SynCom28` a single community-level interaction makes
`DISCONNECTED` unreachable for all 28 taxa.

#312 records this rather than fixing it, and was right to: not crediting was
measured and is worse in both directions — community-level-only crediting leaves
1 finding across the corpus (vacuous), dropping the exemption without the credit
reports 390 (noise). Together they land at a usable number.

What this file adds is that the coarseness is now **counted**, so it cannot grow
unnoticed. It already has: #312 measured 412 of 518 taxa credited solely by the
rule, and it is 407 of 522 today — the shape is stable, the corpus moved.

The refinement #312 proposes — an optional `participating_taxa` on
`EcologicalInteraction`, crediting only named members when present and falling
back to all members when absent — is a schema change that overlaps #307's
question of how to express which taxa a community-level statement is *about*.
Deliberately not done here. These bounds are loose because the point is to catch
a step change, not to freeze a number that legitimate curation moves.
"""

from __future__ import annotations

import pathlib

import pytest
import yaml

from communitymech.paths import record_files

REPO = pathlib.Path(__file__).parent.parent

# Both record roots, not kb/communities alone. `data/isolates` holds the same
# root class -- 4 records with 66 snippets, 3 ecological_interactions and 3
# gtdb_classification blocks -- and this module could not see any of it (#689).
COMMUNITIES = REPO / "kb/communities"


def _names(block: dict) -> set[str]:
    """Every string a pairwise edge could use to name this member."""
    found = set()
    if block.get("preferred_term"):
        found.add(block["preferred_term"])
    term = block.get("term") or {}
    for key in ("label", "id"):
        if term.get(key):
            found.add(term[key])
    return found


def _survey() -> dict[str, int]:
    records = with_cl = mixed = cl_only = 0
    taxa = solely = 0
    for path in record_files():
        document = yaml.safe_load(path.read_text()) or {}
        records += 1
        interactions = [
            i for i in (document.get("ecological_interactions") or []) if isinstance(i, dict)
        ]
        community_level = [i for i in interactions if i.get("scope") == "COMMUNITY_LEVEL"]
        if not community_level:
            continue
        with_cl += 1
        if len(community_level) < len(interactions):
            mixed += 1
        else:
            cl_only += 1

        members = [(t or {}).get("taxon_term") or {} for t in (document.get("taxonomy") or [])]
        pairwise: set[str] = set()
        for interaction in interactions:
            if interaction.get("scope") == "COMMUNITY_LEVEL":
                continue
            for role in ("source_taxon", "target_taxon"):
                node = interaction.get(role)
                if isinstance(node, dict):
                    pairwise |= _names(node)
                elif isinstance(node, str):
                    pairwise.add(node)
        taxa += len(members)
        solely += sum(1 for m in members if not (_names(m) & pairwise))
    return {
        "records": records,
        "with_community_level": with_cl,
        "mixed": mixed,
        "community_level_only": cl_only,
        "taxa": taxa,
        "credited_solely_by_the_rule": solely,
    }


@pytest.fixture(scope="module")
def survey() -> dict[str, int]:
    return _survey()


def test_the_survey_sees_the_corpus(survey):
    """Guard: a broken walk would make every bound below pass on zeros."""
    assert survey["records"] > 300
    assert survey["with_community_level"] > 100


def test_most_records_carry_a_community_level_interaction(survey):
    """The rule's reach. #312 measured 156; loose bounds, since curation adds records."""
    assert 130 <= survey["with_community_level"] <= 200, survey


def test_the_mixed_records_are_where_the_coarseness_bites(survey):
    """A record with both kinds is where an unrelated edge credits a lone taxon.

    #312 measured 46. In the community-level-only records the credit is not
    coarse — there is no pairwise edge it could be masking.
    """
    assert 35 <= survey["mixed"] <= 80, survey
    assert survey["mixed"] + survey["community_level_only"] == survey["with_community_level"]


def test_the_share_credited_solely_by_the_rule_has_not_stepped_up(survey):
    """The headline number, and the one worth watching.

    #312: 412 of 518. Today: 407 of 522. Bounded as a *share* rather than a
    count, so adding records does not trip it but a change in the rule's reach
    does.
    """
    share = survey["credited_solely_by_the_rule"] / survey["taxa"]
    assert 0.65 <= share <= 0.90, (
        f"{survey['credited_solely_by_the_rule']} of {survey['taxa']} taxa "
        f"({share:.0%}) are credited only by the community-level rule. #312 "
        f"measured 412 of 518 (80%). A step change means either the rule's "
        f"reach moved or curation added many pairwise edges — both worth "
        f"looking at before adjusting this bound."
    )


def test_the_worked_example_still_shows_the_limit():
    """`GLBRC_Populus_Variovorax_SynCom28` is #312's illustration.

    28 taxa, and one community-level interaction makes DISCONNECTED unreachable
    for every one. If this record ever gains pairwise edges the example should
    move rather than be quietly dropped.
    """
    path = COMMUNITIES / "GLBRC_Populus_Variovorax_SynCom28.yaml"
    assert path.exists(), "the worked example record is gone; pick another and update #312"
    document = yaml.safe_load(path.read_text()) or {}
    members = document.get("taxonomy") or []
    interactions = [
        i for i in (document.get("ecological_interactions") or []) if isinstance(i, dict)
    ]
    assert len(members) >= 20
    assert any(i.get("scope") == "COMMUNITY_LEVEL" for i in interactions)


def test_the_schema_can_now_name_participants():
    """#312's refinement landed; this file records what it did not change.

    `participating_taxa` is on `EcologicalInteraction` and the auditor narrows
    the community-level credit to the members it names. The numbers above are
    unaffected because no record uses it yet — absent or empty still means
    "every member", which is what makes the slot safe to land ahead of curation.

    When records do start naming participants, `credited_solely_by_the_rule`
    should fall and the bound in
    `test_the_share_credited_solely_by_the_rule_has_not_stepped_up` will need
    re-measuring downward rather than widening. See tests/test_participating_taxa.py.
    """
    schema = yaml.safe_load(
        (REPO / "src/communitymech/schema/communitymech.yaml").read_text(encoding="utf-8")
    )
    attributes = schema["classes"]["EcologicalInteraction"]["attributes"]
    assert "participating_taxa" in attributes, (
        "the slot #312 asked for is gone again; the all-or-nothing credit in "
        "audit_community has nothing to narrow against"
    )
    assert attributes["participating_taxa"].get("multivalued") is True
