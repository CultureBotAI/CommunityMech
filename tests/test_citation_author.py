"""Tests for deterministic first-author / citation derivation.

These guard against the related_ingredients backfill regression where the
relevance prose cited the WRONG first author (a non-first or non-present
author) in "(Surname et al. Year)" citations.

The parametrized cases below use the REAL cached PubMed metadata for the
PMIDs that were mis-attributed in PRs #119/#122/#124/#127, asserting that the
parser recovers the paper's actual first author (not the wrong name that was
committed). When the cache file is not present the case is skipped so the
suite still runs in a checkout without references_cache/.
"""

from pathlib import Path

import pytest

from communitymech.literature import (
    LiteratureFetcher,
    format_citation,
    parse_first_author_from_author_string,
    parse_first_author_from_medline,
    parse_year_from_medline,
)

CACHE_DIR = Path(__file__).resolve().parents[1] / "references_cache"

# pmid -> (real first author surname, year, the WRONG name committed in a PR)
REAL_CASES = {
    "38520150": ("Luo", "2024", "Yu"),
    "40433987": ("Zhou", "2025", "Cui"),
    "36847519": ("Wang", "2023", "Liu"),
    "39858916": ("You", "2025", "Wei"),
    "37154752": ("Wu", "2023", "Zhang"),
    "38840214": ("Qiao", "2024", "Bai"),
    "37207729": ("Zhou", "2023", "Niu"),
}


@pytest.mark.parametrize("pmid,expected,year,wrong", [
    (p, e, y, w) for p, (e, y, w) in REAL_CASES.items()
])
def test_first_author_from_real_medline_cache(pmid, expected, year, wrong):
    cache_file = CACHE_DIR / f"PMID_{pmid}.txt"
    if not cache_file.exists():
        pytest.skip(f"cache file for PMID {pmid} not present")
    text = cache_file.read_text()
    parsed = parse_first_author_from_medline(text)
    assert parsed == expected, f"PMID {pmid}: parsed {parsed!r}, expected {expected!r}"
    # The parser must NOT reproduce the wrong name that the backfill committed.
    assert parsed != wrong
    assert parse_year_from_medline(text) == year
    assert format_citation(text) == f"({expected} et al. {year})"


def test_parse_first_author_medline_basic():
    text = (
        "1. J Appl Microbiol. 2024 Apr 1;135(4):lxae073. doi: 10.1093/jambio/lxae073.\n\n"
        "Seed-borne bacterial synthetic community resists seed pathogenic fungi.\n\n"
        "Luo DL(1), Huang SY(1), Dai CC(1).\n\n"
        "Author information:\n(1)Nanjing.\nPMID: 38520150"
    )
    assert parse_first_author_from_medline(text) == "Luo"
    assert format_citation(text) == "(Luo et al. 2024)"


def test_single_author_drops_et_al():
    text = (
        "1. Some J. 2021 Jan;1(1):1. doi: 10.1/x.\n\n"
        "A solo-authored title about microbes.\n\n"
        "Smith AB(1).\n\nAuthor information:\n(1)Place.\nPMID: 123"
    )
    assert format_citation(text) == "(Smith 2021)"


def test_multiword_surname():
    assert parse_first_author_from_author_string("Van Dyk JS, Other AB") == "Van Dyk"


def test_collective_author_preserved():
    name = "The Human Microbiome Consortium"
    assert parse_first_author_from_author_string(name) == name
    # No "et al." appended for a collective author.
    expected = f"({name} 2020)"
    assert format_citation("J. 2020 Feb;...", author_string=name) == expected


def test_author_string_path_multi_author():
    assert format_citation(
        "J. 2020 Feb;...", author_string="Luo DL, Huang SY, Dai CC"
    ) == "(Luo et al. 2020)"


def test_format_citation_no_year():
    assert format_citation("", author_string="Luo DL, Huang SY") == "(Luo et al.)"


def test_empty_inputs_return_none():
    assert parse_first_author_from_medline("") is None
    assert parse_first_author_from_author_string("") is None
    assert format_citation("") is None


def test_validate_citation_author_gate(tmp_path):
    fetcher = LiteratureFetcher(cache_dir=str(tmp_path))
    (tmp_path / "PMID_999.txt").write_text(
        "1. J. 2024 Apr;1(1):1. doi: 10.1/x.\n\nTitle.\n\n"
        "Luo DL(1), Huang SY(1).\n\nAuthor information:\n(1)X.\nPMID: 999"
    )
    assert fetcher.validate_citation_author("999", "Luo") is True
    assert fetcher.validate_citation_author("999", "luo") is True  # case-insensitive
    assert fetcher.validate_citation_author("999", "Yu") is False   # the bug
    # Unparseable / missing -> fail closed.
    assert fetcher.validate_citation_author("absent", "Anyone") is False


def test_citation_for_pmid_uses_cache(tmp_path):
    fetcher = LiteratureFetcher(cache_dir=str(tmp_path))
    (tmp_path / "PMID_42.txt").write_text(
        "1. J. 2023 Apr;1(1):1. doi: 10.1/y.\n\nTitle.\n\n"
        "Wang D(1), Hunt KA(2).\n\nAuthor information:\n(1)X.\nPMID: 42"
    )
    assert fetcher.citation_for_pmid("42") == "(Wang et al. 2023)"
    assert fetcher.first_author_for_pmid("42") == "Wang"
