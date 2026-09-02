"""An ontology cache that can never be re-saved is a cache that goes stale (#707).

GitHub Actions cache entries are immutable per key, and a hit on the primary key
skips the save entirely. With `key: oaklib-${{ runner.os }}-v1` the post-step
said so verbatim, in every run:

    Cache hit occurred on the primary key oaklib-Linux-v1, not saving cache.

So whatever was first stored is frozen for good. Nothing downloaded afterwards
can ever reach the cache, and the only way to pick up a newer ontology release
is for a human to notice and bump `-v1` by hand -- which nothing prompts anyone
to do. The failure is quiet: a gate keeps passing against a taxonomy that is a
year stale.

The fix is a rotating primary key plus a prefix `restore-keys`, so each period
restores the previous entry as its base (keeping the hit rate) and then saves a
fresh one including anything newly fetched.

This is asserted structurally rather than by reading the key string for a
particular shape: what matters is that the key VARIES and that a restore-key
exists, not which stamp is used.
"""

from __future__ import annotations

import pathlib
import re

import pytest
import yaml

_EXPRESSION = re.compile(r"\$\{\{(.*?)\}\}")

REPO = pathlib.Path(__file__).parent.parent
WORKFLOWS = REPO / ".github" / "workflows"


def _oak_cache_steps() -> list[tuple[str, str, dict]]:
    """(workflow, job, step) for every step caching the OAK download directory.

    Found by what the step DOES -- caching `~/.data/oaklib` -- not by its name,
    so renaming it cannot drop it out of the check.
    """
    found = []
    for path in sorted(WORKFLOWS.glob("*.y*ml")):
        document = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        for job, spec in (document.get("jobs") or {}).items():
            for step in spec.get("steps") or []:
                with_ = step.get("with") or {}
                if "oaklib" in str(with_.get("path", "")):
                    found.append((path.name, job, step))
    return found


def test_there_are_oak_cache_steps_to_check():
    """A finder that found nothing would make the gate below vacuous.

    Two, not three: `label-correspondence` moved to a reusable workflow in claw
    (#731), so its cache step is no longer in this repository. That is fine --
    the rotation went upstream with it, and claw's copy carries the same month
    stamp and the same reason ("not saving cache" in every run) plus an
    `oak-cache-key` input as a manual bust. What is left here are
    `validate-strict`'s two jobs, and this still has to hold for them.
    """
    steps = _oak_cache_steps()
    assert len(steps) >= 2, f"expected several OAK cache steps, found {len(steps)}"


@pytest.mark.parametrize(
    "workflow,job,step",
    _oak_cache_steps(),
    ids=lambda v: v if isinstance(v, str) else "step",
)
def test_the_ontology_cache_key_can_rotate(workflow: str, job: str, step: dict):
    """The primary key varies, and a prefix restore-key keeps the hit rate."""
    with_ = step.get("with") or {}
    key = str(with_.get("key", ""))
    restore = str(with_.get("restore-keys", "")).strip()

    assert key, f"{workflow}::{job} caches oaklib with no key at all"
    # A key built ONLY from `runner.os` and literals cannot change, so the entry
    # is written once and frozen. Requiring a VARYING expression beyond
    # `runner.os` is what makes rotation structural rather than a promise in a
    # comment.
    #
    # Counted with a regex, not `key.split("${{")`. That split returns the
    # literal prefix as an element too, so `oaklib-${{ runner.os }}-v1` came
    # back as two and the fixed key this test exists to reject passed it. Found
    # by mutation: reverting a key to the old form left the test green.
    expressions = _EXPRESSION.findall(key)
    varying = [e for e in expressions if "runner.os" not in e]
    assert varying, (
        f"{workflow}::{job} has a fixed ontology cache key {key!r}. Actions "
        f"caches are immutable per key and a primary hit skips the save, so "
        f"this entry can never be updated (#707)."
    )
    assert restore, (
        f"{workflow}::{job} rotates its key but has no restore-keys, so every "
        f"rotation would start from an empty cache and re-download everything"
    )
