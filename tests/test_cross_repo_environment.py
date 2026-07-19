"""Tests for the cross-repo ENVO coverage index (issue #30).

Uses tiny on-disk fixtures under ``tmp_path`` — no real sibling repos, no
network — mirroring the three repos' environment-field shapes:

* CommunityMech community: ``environment_term.term.id``
* CultureMech media:       ``source_environment[].term.id``
* MIM ingredient:          ``environmental_context[].environment_term`` (bare CURIE)
"""

import textwrap

from communitymech.cross_repo_environment import (
    build_coverage,
    culturemech_media_by_environment,
    sibling_repos_from_env,
)


def _write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(textwrap.dedent(text))


def _make_community(dir_, name, envo_id, label):
    _write(
        dir_ / f"{name}.yaml",
        f"""
        name: {name}
        environment_term:
          preferred_term: {label}
          term:
            id: {envo_id}
            label: {label}
        """,
    )


def _make_media(dir_, cid, envo_id, label):
    _write(
        dir_ / f"{cid.replace(':', '_')}.yaml",
        f"""
        id: {cid}
        name: {cid}
        source_environment:
        - preferred_term: {label}
          term:
            id: {envo_id}
            label: {label}
        """,
    )


def _make_ingredient(dir_, ident, envo_id, label):
    _write(
        dir_ / f"{ident.replace(':', '_')}.yaml",
        f"""
        identifier: {ident}
        environmental_context:
        - environment_term: {envo_id}
          environment_label: {label}
        """,
    )


def _fixture(tmp_path):
    comm = tmp_path / "communities"
    cm = tmp_path / "CultureMech"
    mim = tmp_path / "MIM"
    # peatland: community + media, no ingredient
    _make_community(comm, "PeatCommunity", "ENVO:00000044", "peatland")
    _make_media(cm / "data", "CultureMech:000001", "ENVO:00000044", "peatland")
    # soil: community + ingredient, no media
    _make_community(comm, "SoilCommunity", "ENVO:00001998", "soil")
    _make_ingredient(mim / "data", "kgmicrobe.ingredient:humic_acid", "ENVO:00001998", "soil")
    # vent: community only (full gap)
    _make_community(comm, "VentCommunity", "ENVO:01000030", "hydrothermal vent")
    return comm, cm, mim


def test_build_coverage_maps_all_three_repos(tmp_path):
    comm, cm, mim = _fixture(tmp_path)
    cov = build_coverage(comm, {"CultureMech": cm, "MediaIngredientMech": mim})

    assert cov.all_terms() == {"ENVO:00000044", "ENVO:00001998", "ENVO:01000030"}
    assert cov.community_records["ENVO:00000044"] == ["PeatCommunity"]
    assert cov.media_records["ENVO:00000044"] == ["CultureMech:000001"]
    assert cov.ingredient_records["ENVO:00001998"] == ["kgmicrobe.ingredient:humic_acid"]
    # labels harvested from records, no ontology lookup
    assert cov.label("ENVO:00000044") == "peatland"


def test_gap_terms_have_no_sibling_records(tmp_path):
    comm, cm, mim = _fixture(tmp_path)
    cov = build_coverage(comm, {"CultureMech": cm, "MediaIngredientMech": mim})

    # vent community has neither media nor ingredients
    assert "ENVO:01000030" in cov.community_records
    assert "ENVO:01000030" not in cov.media_records
    assert "ENVO:01000030" not in cov.ingredient_records
    # peatland lacks ingredients; soil lacks media
    assert "ENVO:00000044" not in cov.ingredient_records
    assert "ENVO:00001998" not in cov.media_records


def test_no_siblings_still_indexes_communities(tmp_path):
    comm, _, _ = _fixture(tmp_path)
    cov = build_coverage(comm, sibling_repos={})
    assert set(cov.community_records) == {"ENVO:00000044", "ENVO:00001998", "ENVO:01000030"}
    assert cov.media_records == {}
    assert cov.ingredient_records == {}


def test_non_envo_and_missing_terms_ignored(tmp_path):
    comm = tmp_path / "communities"
    _make_community(comm, "GoodCommunity", "ENVO:00000044", "peatland")
    # a community grounded to a non-ENVO term is ignored
    _write(
        comm / "OtherCommunity.yaml",
        """
        name: OtherCommunity
        environment_term:
          term:
            id: UBERON:0000955
            label: brain
        """,
    )
    # a community with no environment_term at all is ignored
    _write(comm / "BareCommunity.yaml", "name: BareCommunity\n")
    cov = build_coverage(comm, sibling_repos={})
    assert set(cov.community_records) == {"ENVO:00000044"}


def test_prefilter_skips_records_without_the_field(tmp_path):
    comm, cm, mim = _fixture(tmp_path)
    # add a CultureMech record with NO source_environment — must be skipped
    _write(
        cm / "data" / "no_env.yaml",
        """
        id: CultureMech:009999
        name: no_env
        ingredients: []
        """,
    )
    cov = build_coverage(comm, {"CultureMech": cm, "MediaIngredientMech": mim})
    media_ids = {rid for ids in cov.media_records.values() for rid in ids}
    assert "CultureMech:009999" not in media_ids


def test_culturemech_media_by_environment(tmp_path):
    cm = tmp_path / "CultureMech"
    _make_media(cm / "data", "CultureMech:000001", "ENVO:00000044", "peatland")
    _make_media(cm / "data", "CultureMech:000002", "ENVO:00000044", "peatland")
    _make_media(cm / "data", "CultureMech:000003", "ENVO:00001998", "soil")
    # a record with no source_environment must be prefiltered out
    _write(cm / "data" / "bare.yaml", "id: CultureMech:009999\nname: bare\n")

    by_env = culturemech_media_by_environment(cm)
    assert set(by_env) == {"ENVO:00000044", "ENVO:00001998"}
    peat = by_env["ENVO:00000044"]
    assert {h.culturemech_id for h in peat} == {"CultureMech:000001", "CultureMech:000002"}
    hit = peat[0]
    assert hit.name and hit.env_label == "peatland"
    assert "CultureMech:009999" not in {h.culturemech_id for v in by_env.values() for h in v}


def test_sibling_repos_from_env(monkeypatch):
    monkeypatch.setenv(
        "COMMUNITYMECH_SIBLING_REPOS",
        "CultureMech=/x/CultureMech, MediaIngredientMech=/y/MIM",
    )
    repos = sibling_repos_from_env()
    assert set(repos) == {"CultureMech", "MediaIngredientMech"}
    assert str(repos["CultureMech"]) == "/x/CultureMech"

    monkeypatch.delenv("COMMUNITYMECH_SIBLING_REPOS")
    assert sibling_repos_from_env() == {}
