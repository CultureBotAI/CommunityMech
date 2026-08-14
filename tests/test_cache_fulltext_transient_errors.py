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
