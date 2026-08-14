"""A failed fetch must not be mistaken for a paper that cannot be fetched (#586).

`scripts/cache_fulltext.py` decides which references the sweep can retrieve, and
that decision feeds #183's "needs access" set. So the difference between

* `[skip]` — Europe PMC answered, and the answer is *this paper is not OA*, and
* `[error]` — nobody answered

is not cosmetic. It is the difference between a fact about the paper and a fact
about the network. Conflating the two is the same defect corrected in #577/#578,
where a thin cache was read as a thin source.

Observed on one reference inside ninety seconds:

    attempt 1:  HTTPError 504: Gateway Time-out          <- traceback, batch dead
    attempt 2:  HTTPError 503: Service Temporarily Unavailable
    attempt 3:  [skip] 23306120: not open-access ...     <- the true answer

Two things were wrong. `_get` surfaced the transient statuses to the caller, and
`main` ran its refs in a bare `for` loop, so the first one to raise killed every
reference after it — which the output could not distinguish from those
references having been tried and found wanting.

Every test here drives the real functions. `_get` takes an injected `sleep` so
the backoff costs no wall-clock, and a fake opener stands in for the network.
"""

from __future__ import annotations

import importlib.util
import pathlib
import urllib.error

import pytest

REPO = pathlib.Path(__file__).parent.parent
SCRIPT = REPO / "scripts/cache_fulltext.py"


def _module():
    """Load the script by path — `scripts/` is not an importable package."""
    spec = importlib.util.spec_from_file_location("cache_fulltext_under_test", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture()
def mod():
    return _module()


def _http_error(code: int) -> urllib.error.HTTPError:
    return urllib.error.HTTPError("https://example.invalid", code, "boom", {}, None)


class _Response:
    """The context-manager shape `urlopen` returns, with a fixed body."""

    def __init__(self, body: bytes):
        self._body = body

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False

    def read(self) -> bytes:
        return self._body


class _Opener:
    """Replays a scripted sequence of outcomes, counting calls."""

    def __init__(self, outcomes):
        self.outcomes = list(outcomes)
        self.calls = 0

    def __call__(self, req, timeout=None):
        self.calls += 1
        outcome = self.outcomes.pop(0)
        if isinstance(outcome, Exception):
            raise outcome
        return _Response(outcome)


def test_get_retries_a_503_and_returns_the_eventual_answer(mod, monkeypatch):
    """The exact observed sequence: two transient failures, then the real answer."""
    opener = _Opener([_http_error(504), _http_error(503), b"the real body"])
    monkeypatch.setattr(mod.urllib.request, "urlopen", opener)

    body = mod._get("https://example.invalid/x", sleep=lambda _s: None)

    assert body == b"the real body"
    assert opener.calls == 3, "did not retry through both transient failures"


@pytest.mark.parametrize("code", [500, 502, 503, 504, 429])
def test_every_transient_status_is_retried(mod, monkeypatch, code):
    opener = _Opener([_http_error(code), b"ok"])
    monkeypatch.setattr(mod.urllib.request, "urlopen", opener)
    assert mod._get("https://example.invalid/x", sleep=lambda _s: None) == b"ok"
    assert opener.calls == 2


def test_a_404_is_an_answer_and_is_not_retried(mod, monkeypatch):
    """Retrying a real verdict only slows the sweep to reach the same place."""
    opener = _Opener([_http_error(404), b"unreachable"])
    monkeypatch.setattr(mod.urllib.request, "urlopen", opener)

    with pytest.raises(urllib.error.HTTPError) as caught:
        mod._get("https://example.invalid/x", sleep=lambda _s: None)

    assert caught.value.code == 404
    assert opener.calls == 1, "a 404 was retried; it is a verdict, not an outage"


def test_get_eventually_gives_up_rather_than_looping(mod, monkeypatch):
    """A persistent outage must terminate — and still raise, not return None."""
    opener = _Opener([_http_error(503)] * 4)
    monkeypatch.setattr(mod.urllib.request, "urlopen", opener)

    with pytest.raises(urllib.error.HTTPError):
        mod._get("https://example.invalid/x", attempts=4, sleep=lambda _s: None)

    assert opener.calls == 4


def test_one_dead_reference_does_not_cost_the_others_their_attempt(mod, monkeypatch, capsys):
    """The batch defect: item 2 raising must not strand items 3 and 4.

    This is the regression that matters most. Before the fix the loop was a bare
    `for` with no `try`, so the sweep stopped at the first raise and its output
    gave no way to tell "not attempted" from "attempted and unavailable".
    """
    attempted = []

    def fake_cache_one(ref):
        attempted.append(ref)
        if ref == "2":
            raise urllib.error.HTTPError("https://example.invalid", 503, "boom", {}, None)
        return f"[cached] {ref}: fine"

    monkeypatch.setattr(mod, "cache_one", fake_cache_one)
    monkeypatch.setattr(mod.sys, "argv", ["cache_fulltext.py", "1", "2", "3", "4"])

    code = mod.main()
    out = capsys.readouterr().out

    assert attempted == ["1", "2", "3", "4"], (
        "the sweep abandoned references after the failing one; they were never "
        f"attempted (reached: {attempted})"
    )
    assert code == 1, "a batch that lost a reference reported success"
    assert "[error] 2:" in out, "the failing reference was not reported as an error"
    assert "[cached] 3: fine" in out and "[cached] 4: fine" in out


def test_an_outage_is_reported_as_error_never_as_skip(mod, monkeypatch, capsys):
    """`[skip]` is a verdict about the paper; `[error]` is the absence of one.

    Anything downstream that builds a "needs access" list reads these strings.
    If an outage printed `[skip]`, a transient failure would be filed as a
    paywall — exactly the #577/#578 confusion this whole file exists to prevent.
    """
    monkeypatch.setattr(
        mod,
        "cache_one",
        lambda ref: (_ for _ in ()).throw(
            urllib.error.HTTPError("https://example.invalid", 503, "boom", {}, None)
        ),
    )
    monkeypatch.setattr(mod.sys, "argv", ["cache_fulltext.py", "99"])

    assert mod.main() == 1
    out = capsys.readouterr().out
    assert "[error]" in out
    assert "[skip]" not in out, "an outage was reported with the vocabulary of a verdict"


def test_a_clean_batch_still_returns_zero(mod, monkeypatch, capsys):
    """Guard against the fix turning every run red."""
    monkeypatch.setattr(mod, "cache_one", lambda ref: f"[ok] {ref}: already cached")
    monkeypatch.setattr(mod.sys, "argv", ["cache_fulltext.py", "1", "2"])

    assert mod.main() == 0
    assert "[error]" not in capsys.readouterr().out


# --- the two review findings on #587 ---------------------------------------


def test_from_file_gets_the_same_guard_as_the_network_path(mod, monkeypatch, capsys, tmp_path):
    """#588 — the `--from-file` branch kept the bare loop for the whole fix.

    Both branches now go through `_sweep`, so this asserts the property rather
    than the plumbing: a raise on one ref must not strand the ones after it.
    """
    source = tmp_path / "paper.txt"
    source.write_text("full text")
    attempted = []

    def fake_from_file(ref, path):
        attempted.append(ref)
        if ref == "b":
            raise OSError("corrupt PDF")
        return f"[cached] {ref}: ok"

    monkeypatch.setattr(mod, "cache_from_file", fake_from_file)
    monkeypatch.setattr(
        mod.sys, "argv", ["cache_fulltext.py", "a", "b", "c", "--from-file", str(source)]
    )

    code = mod.main()

    assert attempted == ["a", "b", "c"], f"refs after the failure were stranded: {attempted}"
    assert code == 1
    assert "[error] b:" in capsys.readouterr().out


def test_an_unpaywall_outage_is_not_reported_as_no_oa_copy(mod, monkeypatch, tmp_path):
    """#589 — a failed lookup must not read as a fact about the paper."""
    cache = tmp_path / "DOI_10.1_x.md"
    cache.write_text("abstract")
    monkeypatch.setattr(mod, "_doi_cache_path", lambda doi: cache)
    monkeypatch.setattr(mod, "_pmcid_for_doi", lambda doi: (None, False))
    monkeypatch.setattr(mod, "_unpaywall_location", lambda doi: mod._LookupFailed("URLError: down"))

    message = mod.cache_one_doi("10.1/x")

    assert message.startswith("[error]"), f"an outage was reported as a verdict: {message}"
    assert "unknown" in message and "retry" in message
    assert "set UNPAYWALL_EMAIL" not in message, "told the curator to set a var they may have set"


def test_a_real_absence_is_still_a_skip(mod, monkeypatch, tmp_path):
    """The other side of #589: a confirmed 'no OA copy' must stay a verdict."""
    cache = tmp_path / "DOI_10.1_x.md"
    cache.write_text("abstract")
    monkeypatch.setattr(mod, "_doi_cache_path", lambda doi: cache)
    monkeypatch.setattr(mod, "_pmcid_for_doi", lambda doi: (None, False))
    monkeypatch.setattr(mod, "_unpaywall_location", lambda doi: None)

    message = mod.cache_one_doi("10.1/x")

    assert message.startswith("[skip]")
    assert "knows of no OA copy" in message


def test_unpaywall_distinguishes_outage_from_absence(mod, monkeypatch):
    """`_unpaywall_location` itself must return three distinguishable things."""
    monkeypatch.setenv("UNPAYWALL_EMAIL", "someone@example.org")

    monkeypatch.setattr(
        mod,
        "_get",
        lambda url, **kw: (_ for _ in ()).throw(urllib.error.URLError("down")),
    )
    outage = mod._unpaywall_location("10.1/x")
    assert isinstance(outage, mod._LookupFailed), "an outage collapsed back into None"

    monkeypatch.setattr(mod, "_get", lambda url, **kw: b'{"is_oa": false}')
    assert mod._unpaywall_location("10.1/x") is None, "a real absence must stay None"

    monkeypatch.setattr(
        mod, "_get", lambda url, **kw: b'{"is_oa": true, "best_oa_location": {"url": "u"}}'
    )
    found = mod._unpaywall_location("10.1/x")
    assert found == "u" and not isinstance(found, mod._LookupFailed)


def test_oa_but_no_xml_is_a_skip_not_an_error(mod, monkeypatch, tmp_path):
    """#590 — the mirror of #586: a stable fact reported as an outage.

    Europe PMC answers `isOpenAccess: Y` and then 404s on `fullTextXML` for the
    same PMCID (observed on PMID:25692519 / PMC4333721, identical on retry).
    There is nothing to retry, so it is a verdict and must not inflate the
    no-verdict count that #587 added.
    """
    cache = tmp_path / "PMID_1.md"
    cache.write_text("abstract only")
    monkeypatch.setattr(mod, "_cache_path", lambda pmid: cache)
    monkeypatch.setattr(mod, "_pmcid", lambda pmid: ("PMC4333721", True))
    monkeypatch.setattr(
        mod,
        "_fulltext_xml",
        lambda pmcid: (_ for _ in ()).throw(
            urllib.error.HTTPError("https://example.invalid", 404, "nf", {}, None)
        ),
    )

    message = mod.cache_one("1")

    assert message.startswith("[skip]"), f"a stable verdict was filed as an outage: {message}"
    assert "serves no full-text XML" in message
    assert "not open-access" not in message, "conflated with the genuinely-closed case"
    assert cache.read_text() == "abstract only", "wrote to the cache despite retrieving nothing"


def test_oa_but_no_xml_is_a_skip_on_the_doi_path_too(mod, monkeypatch, tmp_path):
    """The DOI path needs its own test, not its sibling's (#590).

    Found by mutation: reverting the guard reddened nothing, because the only
    test covered `cache_one` and the DOI branch sits earlier in the file. The
    mutation was valid and the suite was blind to it — a check that reports
    clean because it never ran.
    """
    cache = tmp_path / "DOI_10.1_x.md"
    cache.write_text("abstract only")
    monkeypatch.setattr(mod, "_doi_cache_path", lambda doi: cache)
    monkeypatch.setattr(mod, "_pmcid_for_doi", lambda doi: ("PMC4333721", True))
    monkeypatch.setattr(
        mod,
        "_fulltext_xml",
        lambda pmcid: (_ for _ in ()).throw(
            urllib.error.HTTPError("https://example.invalid", 404, "nf", {}, None)
        ),
    )

    message = mod.cache_one_doi("10.1/x")

    assert message.startswith("[skip]"), f"a stable verdict was filed as an outage: {message}"
    assert "serves no full-text XML" in message
    assert cache.read_text() == "abstract only", "wrote to the cache despite retrieving nothing"


def test_a_non_404_from_fulltext_still_propagates(mod, monkeypatch, tmp_path):
    """Only 404 is the verdict. A 503 here is still an outage and must raise."""
    cache = tmp_path / "PMID_1.md"
    cache.write_text("abstract only")
    monkeypatch.setattr(mod, "_cache_path", lambda pmid: cache)
    monkeypatch.setattr(mod, "_pmcid", lambda pmid: ("PMC1", True))
    monkeypatch.setattr(
        mod,
        "_fulltext_xml",
        lambda pmcid: (_ for _ in ()).throw(
            urllib.error.HTTPError("https://example.invalid", 503, "down", {}, None)
        ),
    )

    with pytest.raises(urllib.error.HTTPError):
        mod.cache_one("1")


def test_a_returned_error_reaches_the_exit_code(mod, monkeypatch, capsys):
    """A handler that *returns* `[error]` must fail the sweep, not just print.

    Found while fixing #589: `cache_one_doi` reports a failed Unpaywall lookup
    by return value rather than by raising, so the exception path alone would
    have printed `[error]` and still exited 0.
    """
    monkeypatch.setattr(mod, "cache_one", lambda ref: f"[error] {ref}: lookup did not complete")
    monkeypatch.setattr(mod.sys, "argv", ["cache_fulltext.py", "7"])

    assert mod.main() == 1, "a printed [error] did not reach the exit code"
