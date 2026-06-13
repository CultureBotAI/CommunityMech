"""Tests for the new abstract-source fallbacks added to LiteratureFetcher.

Covers:
- fetch_openalex_abstract (inverted-index reconstruction + cache)
- fetch_semantic_scholar_abstract
- fetch_europepmc_abstract
- fetch_publisher_meta_abstract (DOI page meta-tag scrape)
- fetch_pmcid_for_doi (ID Converter API success + not-found)

The tests mock requests.Session.get on the fetcher's session so no
network is required.
"""

from unittest.mock import MagicMock, patch

import pytest
import requests

from communitymech.literature import LiteratureFetcher


@pytest.fixture
def fetcher(tmp_path):
    """LiteratureFetcher pointing at a per-test cache_dir."""
    return LiteratureFetcher(cache_dir=str(tmp_path))


def _mock_json_response(payload):
    response = MagicMock()
    response.json.return_value = payload
    response.raise_for_status.return_value = None
    return response


def _mock_text_response(text):
    response = MagicMock()
    response.text = text
    response.raise_for_status.return_value = None
    return response


# ---------------------------------------------------------------------------
# fetch_openalex_abstract
# ---------------------------------------------------------------------------


def test_openalex_reconstructs_from_inverted_index(fetcher):
    """OpenAlex returns an inverted index; reconstruct in position order."""
    payload = {
        "abstract_inverted_index": {
            "Acetate": [0],
            "is": [1],
            "oxidized": [2],
            "by": [3],
            "Rhodoferax": [4],
        }
    }
    with patch.object(fetcher.session, "get", return_value=_mock_json_response(payload)):
        result = fetcher.fetch_openalex_abstract("10.1234/example")
    assert result == "Acetate is oxidized by Rhodoferax"


def test_openalex_cache_hit_skips_http(fetcher):
    """Second call reads from disk cache; no HTTP request is issued."""
    cache_file = fetcher._abstract_cache_path("openalex", "10.1234/cached")
    cache_file.write_text("cached abstract text")

    with patch.object(fetcher.session, "get") as mock_get:
        result = fetcher.fetch_openalex_abstract("10.1234/cached")
    mock_get.assert_not_called()
    assert result == "cached abstract text"


# ---------------------------------------------------------------------------
# fetch_pubmed_abstract cache naming (validator-visible PMID_<id>.txt)
# ---------------------------------------------------------------------------


def test_pubmed_abstract_reads_uppercase_cache_skips_http(fetcher):
    """A committed PMID_<id>.txt cache is read directly; no HTTP request."""
    (fetcher.cache_dir / "PMID_12345678.txt").write_text("cached abstract")
    with patch.object(fetcher.session, "get") as mock_get:
        result = fetcher.fetch_pubmed_abstract("PMID:12345678")
    mock_get.assert_not_called()
    assert result == "cached abstract"


def test_pubmed_abstract_writes_uppercase_cache(fetcher):
    """A network fetch caches under the validator-visible PMID_<id>.txt name.

    The external linkml-reference-validator resolves "PMID:<id>" to
    PMID_<id>.md (primary) with a legacy fallback to PMID_<id>.txt, so the
    abstract must be written uppercase to be discoverable on case-sensitive
    filesystems (Linux/CI).
    """
    with patch.object(fetcher.session, "get", return_value=_mock_text_response("fresh abstract")):
        result = fetcher.fetch_pubmed_abstract("87654321")
    assert result == "fresh abstract"
    # The abstract is cached under the uppercase, validator-visible name.
    # (We assert path existence rather than the directory-entry casing:
    # macOS dev disks are case-insensitive and report whichever casing the
    # entry was first created with, which is unreliable across machines.)
    assert (fetcher.cache_dir / "PMID_87654321.txt").read_text() == "fresh abstract"


def test_pubmed_abstract_reads_legacy_lowercase_cache(fetcher):
    """Pre-rename lowercase pmid_<id>.txt caches are still read (fallback)."""
    (fetcher.cache_dir / "pmid_55555555.txt").write_text("legacy abstract")
    with patch.object(fetcher.session, "get") as mock_get:
        result = fetcher.fetch_pubmed_abstract("55555555")
    mock_get.assert_not_called()
    assert result == "legacy abstract"


def test_openalex_no_abstract_returns_none(fetcher):
    """Records without abstract_inverted_index return None without caching."""
    payload = {"title": "Paper without abstract"}
    with patch.object(fetcher.session, "get", return_value=_mock_json_response(payload)):
        result = fetcher.fetch_openalex_abstract("10.1234/no-abstract")
    assert result is None
    assert not fetcher._abstract_cache_path("openalex", "10.1234/no-abstract").exists()


def test_openalex_handles_request_exception(fetcher):
    """Network errors return None rather than raising."""
    with patch.object(
        fetcher.session, "get", side_effect=requests.exceptions.ConnectionError("boom")
    ):
        result = fetcher.fetch_openalex_abstract("10.1234/network-error")
    assert result is None


def test_openalex_strips_doi_prefix_case_insensitively(fetcher):
    """Both "doi:" and "DOI:" prefixes are stripped before hitting the API."""
    payload = {"abstract_inverted_index": {"abstract": [0]}}
    with patch.object(
        fetcher.session, "get", return_value=_mock_json_response(payload)
    ) as mock_get:
        fetcher.fetch_openalex_abstract("DOI:10.1234/example")
    called_url = mock_get.call_args[0][0]
    assert called_url == "https://api.openalex.org/works/doi:10.1234/example"


# ---------------------------------------------------------------------------
# fetch_semantic_scholar_abstract
# ---------------------------------------------------------------------------


def test_semantic_scholar_returns_abstract_field(fetcher):
    payload = {"abstract": "The coculture detoxifies furfural."}
    with patch.object(fetcher.session, "get", return_value=_mock_json_response(payload)):
        result = fetcher.fetch_semantic_scholar_abstract("10.1234/example")
    assert result == "The coculture detoxifies furfural."


def test_semantic_scholar_cache_hit_skips_http(fetcher):
    cache_file = fetcher._abstract_cache_path("semanticscholar", "10.1234/cached")
    cache_file.write_text("cached")

    with patch.object(fetcher.session, "get") as mock_get:
        result = fetcher.fetch_semantic_scholar_abstract("10.1234/cached")
    mock_get.assert_not_called()
    assert result == "cached"


def test_semantic_scholar_missing_abstract_returns_none(fetcher):
    payload = {"abstract": None}
    with patch.object(fetcher.session, "get", return_value=_mock_json_response(payload)):
        result = fetcher.fetch_semantic_scholar_abstract("10.1234/no-abstract")
    assert result is None


# ---------------------------------------------------------------------------
# fetch_europepmc_abstract
# ---------------------------------------------------------------------------


def test_europepmc_returns_abstract_from_first_result(fetcher):
    payload = {"resultList": {"result": [{"abstractText": "Wet sedge tundra Fe(III) reduction."}]}}
    with patch.object(fetcher.session, "get", return_value=_mock_json_response(payload)):
        result = fetcher.fetch_europepmc_abstract("10.1234/example")
    assert result == "Wet sedge tundra Fe(III) reduction."


def test_europepmc_empty_result_list_returns_none(fetcher):
    payload = {"resultList": {"result": []}}
    with patch.object(fetcher.session, "get", return_value=_mock_json_response(payload)):
        result = fetcher.fetch_europepmc_abstract("10.1234/missing")
    assert result is None


def test_europepmc_passes_doi_query_param(fetcher):
    """The DOI lookup is encoded as a DOI: query, format=json."""
    payload = {"resultList": {"result": []}}
    with patch.object(
        fetcher.session, "get", return_value=_mock_json_response(payload)
    ) as mock_get:
        fetcher.fetch_europepmc_abstract("10.1234/example")
    params = mock_get.call_args.kwargs["params"]
    assert params["query"] == "DOI:10.1234/example"
    assert params["format"] == "json"


# ---------------------------------------------------------------------------
# fetch_publisher_meta_abstract (DOI page scrape)
# ---------------------------------------------------------------------------


def test_publisher_meta_extracts_twitter_description(fetcher):
    """Springer style: twitter:description carries 'Journal - Abstract text...'."""
    html = (
        "<html><head>"
        '<meta name="twitter:description" content="Current Microbiology - '
        "Acidobacterium is proposed as a new genus for the acidophilic, "
        'chemoorganotrophic bacteria containing menaquinone.">'
        "</head></html>"
    )
    with patch.object(fetcher.session, "get", return_value=_mock_text_response(html)):
        result = fetcher.fetch_publisher_meta_abstract("10.1234/springer")
    assert result is not None
    # The "Journal Name - " prefix is stripped
    assert result.startswith("Acidobacterium is proposed as a new genus")


def test_publisher_meta_falls_back_to_description(fetcher):
    """If twitter:description is missing, fall back to description / og:description."""
    long_desc = "A long meaningful description " * 5
    html = f'<html><head><meta name="description" content="{long_desc}"></head></html>'
    with patch.object(fetcher.session, "get", return_value=_mock_text_response(html)):
        result = fetcher.fetch_publisher_meta_abstract("10.1234/fallback")
    assert result is not None
    assert "long meaningful description" in result


def test_publisher_meta_skips_short_descriptions(fetcher):
    """Navigation-text descriptions under 80 chars are rejected as abstracts."""
    html = '<html><head><meta name="description" content="Short."></head></html>'
    with patch.object(fetcher.session, "get", return_value=_mock_text_response(html)):
        result = fetcher.fetch_publisher_meta_abstract("10.1234/nav-text")
    assert result is None


def test_publisher_meta_handles_request_exception(fetcher):
    with patch.object(fetcher.session, "get", side_effect=requests.exceptions.HTTPError("403")):
        result = fetcher.fetch_publisher_meta_abstract("10.1234/blocked")
    assert result is None


# ---------------------------------------------------------------------------
# fetch_pmcid_for_doi
# ---------------------------------------------------------------------------


def test_pmcid_for_doi_returns_numeric_id(fetcher):
    """Successful ID Converter records strip the PMC prefix."""
    payload = {"records": [{"doi": "10.1234/x", "pmcid": "PMC123456", "pmid": 99999}]}
    with patch.object(fetcher.session, "get", return_value=_mock_json_response(payload)):
        result = fetcher.fetch_pmcid_for_doi("10.1234/x")
    assert result == "123456"


def test_pmcid_for_doi_returns_none_when_not_in_pmc(fetcher):
    """Records with status: error mean the DOI isn't in PMC."""
    payload = {
        "records": [
            {"doi": "10.1234/x", "status": "error", "errmsg": "Identifier not found in PMC"}
        ]
    }
    with patch.object(fetcher.session, "get", return_value=_mock_json_response(payload)):
        result = fetcher.fetch_pmcid_for_doi("10.1234/x")
    assert result is None


def test_pmcid_for_doi_returns_none_for_empty_records(fetcher):
    """Defensive: API returning no records also yields None."""
    payload = {"records": []}
    with patch.object(fetcher.session, "get", return_value=_mock_json_response(payload)):
        result = fetcher.fetch_pmcid_for_doi("10.1234/x")
    assert result is None


# ---------------------------------------------------------------------------
# _abstract_cache_path helper
# ---------------------------------------------------------------------------


def test_abstract_cache_path_encodes_doi_safely(fetcher):
    """Forward slashes in the DOI are replaced with underscores in the filename."""
    path = fetcher._abstract_cache_path("openalex", "10.1234/some/path")
    assert path.name == "openalex_10.1234_some_path.txt"
    assert path.parent == fetcher.cache_dir
