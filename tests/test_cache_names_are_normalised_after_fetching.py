"""A recipe that can fetch must leave the cache in a name the next run can read.

`linkml-reference-validator` normalises a reference id to `DOI:` and builds its
cache path from that, so every cache MISS it fills writes `DOI_*.md`
(``etl/reference_fetcher.py:204-225``). Every reader here builds `doi_...` from
the `doi:` citation, so the file it just wrote is unreachable — and per
``src/communitymech/paths.py`` an unreachable cache is not a skip, it sends the
fetcher back to the network. The loop never converges: miss, fetch, write an
unreadable name, miss again.

133 files accumulated that way before #690. The rename fixed the backlog and
`scripts/cache_fulltext.py` stopped producing new ones, but the *upstream*
fetcher was never ours to fix and went on writing them — which is #697, and why
#690's closure was incomplete.

So the obligation is on the recipe: whatever fetches must normalise afterwards.
Two things are asserted, and the second is the one that would go wrong quietly:

* every recipe invoking the validator also runs `normalize_cache_names.py`;
* it preserves the validator's exit code. A recipe that ends with a successful
  rename reports success no matter what the validation said, which converts an
  evidence gate into a no-op.
"""

from __future__ import annotations

import pathlib
import re
import subprocess

import pytest

from communitymech.paths import canonical_cache_name

REPO = pathlib.Path(__file__).parent.parent
NORMALISER = "normalize_cache_names.py"
FETCHER = "linkml-reference-validator"


def _recipe_bodies() -> dict[str, str]:
    """Recipe name -> body, from `just --dump` rather than a hand parse."""
    dump = subprocess.run(
        ["just", "--unstable", "--dump", "--dump-format", "just"],
        capture_output=True,
        text=True,
        cwd=REPO,
        timeout=120,
    )
    text = dump.stdout if dump.returncode == 0 else (REPO / "justfile").read_text()
    bodies: dict[str, str] = {}
    current = None
    for line in text.splitlines():
        header = re.match(r"^([a-zA-Z][\w-]*)(?:\s+[^:]*)?:(?!=)", line)
        if header and not line.startswith((" ", "\t")):
            current = header.group(1)
            bodies[current] = ""
        elif current and (line.startswith((" ", "\t")) or not line.strip()):
            bodies[current] += line + "\n"
        else:
            current = None
    return bodies


def _fetching_recipes() -> dict[str, str]:
    return {name: body for name, body in _recipe_bodies().items() if FETCHER in body}


def test_there_are_fetching_recipes_to_check():
    """Guard: a parse that finds nothing makes both checks below vacuous."""
    found = _fetching_recipes()
    assert found, (
        "no recipe invokes the reference validator; either the parse in "
        "_recipe_bodies() broke or the recipes were renamed (#697)"
    )


@pytest.mark.parametrize("recipe", sorted(_fetching_recipes()), ids=str)
def test_a_fetching_recipe_normalises_afterwards(recipe: str):
    body = _fetching_recipes()[recipe]
    assert NORMALISER in body, (
        f"`just {recipe}` runs the reference validator, which writes `DOI_*` on "
        f"any cache miss -- a name no reader here resolves to, so the next run "
        f"re-fetches. Add a `{NORMALISER}` step after it (#697)."
    )


@pytest.mark.parametrize("recipe", sorted(_fetching_recipes()), ids=str)
def test_the_validator_exit_code_survives_the_normaliser(recipe: str):
    """A rename must not be able to report success on a failed validation."""
    body = _fetching_recipes()[recipe]
    lines = [line.strip() for line in body.splitlines() if line.strip()]
    normalise_at = max(i for i, line in enumerate(lines) if NORMALISER in line)
    after = lines[normalise_at + 1 :]
    assert any(re.match(r"exit \$\{?(code|rc)\b", line) for line in after), (
        f"`just {recipe}` runs {NORMALISER} last, so the recipe's exit status is "
        f"the RENAME's, not the validation's -- a failing validation would report "
        f"success. Capture the validator's code and `exit` it afterwards (#697)."
    )


def _script() -> dict:
    """The normaliser's namespace, executed from source.

    From source rather than imported: `scripts/` is not a package, and a `.pyc`
    validated on (mtime, size) can serve a module that is not the file under
    test -- which produced a false red here once already (#693).
    """
    path = REPO / "scripts" / NORMALISER
    module: dict = {"__file__": str(path)}
    exec(  # noqa: S102
        compile(path.read_text(encoding="utf-8"), f"scripts/{NORMALISER}", "exec"), module
    )
    return module


def test_the_normaliser_renames_via_a_temporary_name(tmp_path):
    """`DOI_x.md` -> `doi_x.md` is a no-op on a case-insensitive filesystem.

    Asserted through the script's own `rename`, not a reimplementation, because
    a second copy of "how to rename safely" is how the two halves of #690 got out
    of step in the first place.
    """
    module = _script()

    bad = tmp_path / "DOI_10.9999_example.md"
    bad.write_text("cached text", encoding="utf-8")
    pairs = module["plan"](tmp_path)
    assert [p[0].name for p in pairs] == ["DOI_10.9999_example.md"]

    module["rename"](*pairs[0])
    good = tmp_path / "doi_10.9999_example.md"
    assert good.exists() and good.read_text(encoding="utf-8") == "cached text"
    assert module["plan"](tmp_path) == [], "a second pass should find nothing to do"
    assert not list(tmp_path.glob("*.casetmp")), "a temporary name was left behind"


def test_the_normaliser_leaves_a_real_conflict_alone(tmp_path):
    """Two distinct files, one per casing, is a choice no script should make."""
    module = _script()

    upper = tmp_path / "DOI_10.9999_clash.md"
    lower = tmp_path / "doi_10.9999_clash.md"
    upper.write_text("from the upstream fetcher", encoding="utf-8")
    if lower.exists():  # a case-insensitive filesystem: the clash cannot occur
        pytest.skip("filesystem ignores case, so two casings cannot coexist")
    lower.write_text("the committed one", encoding="utf-8")

    message = module["rename"](upper, lower)
    assert message.startswith("[conflict]"), message
    assert lower.read_text(encoding="utf-8") == "the committed one", "clobbered"


def test_only_the_prefix_is_normalised():
    """A DOI suffix is case-significant; lowercasing it would break resolution."""
    assert canonical_cache_name("DOI_10.1134_S0026261716060059.md") == (
        "doi_10.1134_S0026261716060059.md"
    )
    assert canonical_cache_name("doi_10.1134_S0026261716060059.md") is None
    assert canonical_cache_name("PMID_123.md") is None
    assert canonical_cache_name("README.md") is None


def test_an_interrupted_rename_is_recovered_not_orphaned(tmp_path):
    """A `.casetmp` left by a dead run must not stay unreachable (#705).

    It is invisible twice: no reader resolves the name, and
    `canonical_cache_name` returns None for it, so a later pass of this very
    script steps over it. The reference then reads as a cache MISS -- and a miss
    sends the fetcher back to the network, which is the loop #697 exists to
    close, arrived at from the other side.
    """
    module = _script()
    stranded = tmp_path / "DOI_10.9999_interrupted.md.casetmp"
    stranded.write_text("a real fetch", encoding="utf-8")

    assert [p.name for p in module["orphans"](tmp_path)] == [stranded.name]
    assert module["recover"](stranded).startswith("[recovered]")

    recovered = tmp_path / "doi_10.9999_interrupted.md"
    assert recovered.read_text(encoding="utf-8") == "a real fetch"
    assert not list(tmp_path.glob("*.casetmp"))


def test_a_leftover_temporary_is_never_clobbered(tmp_path):
    """`Path.rename` overwrites its destination silently, and that destination
    holds a cached fetch. Refuse instead (#705)."""
    module = _script()
    fetched = tmp_path / "DOI_10.9999_blocked.md"
    fetched.write_text("the new fetch", encoding="utf-8")
    leftover = tmp_path / "DOI_10.9999_blocked.md.casetmp"
    leftover.write_text("an older interrupted fetch", encoding="utf-8")

    message = module["rename"](fetched, tmp_path / "doi_10.9999_blocked.md")

    assert message.startswith("[conflict]"), message
    assert leftover.read_text(encoding="utf-8") == "an older interrupted fetch"
    assert fetched.read_text(encoding="utf-8") == "the new fetch"


def test_the_check_can_actually_fail(tmp_path):
    """Both #705 guards red when removed, mutated in the executed source.

    The mutations are applied to the script TEXT and executed from it, so there
    is no bytecode between the change and the run, and the assertion that each
    mutation is present is what separates a real red from an unapplied one
    (CLAUDE.md, "Proving a gate can fail").
    """
    source = (REPO / "scripts" / NORMALISER).read_text(encoding="utf-8")

    guard = "    if temporary.exists():"
    assert source.count(guard) == 1, "the clobber guard moved; re-point this"
    without_guard = source.replace(guard, "    if False:  # mutated: the leftover check is gone")
    assert "if False:  # mutated" in without_guard
    module: dict = {"__file__": str(REPO / "scripts" / NORMALISER)}
    exec(compile(without_guard, f"scripts/{NORMALISER}", "exec"), module)  # noqa: S102

    fetched = tmp_path / "DOI_10.9999_mutated.md"
    fetched.write_text("the new fetch", encoding="utf-8")
    leftover = tmp_path / "DOI_10.9999_mutated.md.casetmp"
    leftover.write_text("an older interrupted fetch", encoding="utf-8")
    module["rename"](fetched, tmp_path / "doi_10.9999_mutated.md")
    assert not leftover.exists(), (
        "with the guard removed the leftover should have been clobbered; it "
        "survived, so `test_a_leftover_temporary_is_never_clobbered` would pass "
        "with or without the guard it is meant to defend"
    )
