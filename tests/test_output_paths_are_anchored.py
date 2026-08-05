"""Output locations must not follow the working directory (#407).

Several defaults were plain relative strings — `Path("reports")`,
`"references_cache"`, `"docs/communities"` — resolved against the *cwd*. Run from
anywhere but the repo root they wrote stray trees, and because the targets are
git-tracked a caller could also overwrite committed files.

The literature cache was the sharpest: `LiteratureFetcher` defaulted to
`references_cache` and `mkdir`-ed it, so running from another directory created a
second, empty cache and re-fetched from PubMed and CrossRef. That is a silent
cache miss and billed traffic, not an untidy tree, and it defeats the
reproducibility the committed cache exists for.

This file guards the class rather than the instances: a grep-style scan for
relative defaults on output-ish parameters, so the next one fails here instead of
being found by someone's stray directory.
"""

from __future__ import annotations

import ast
from pathlib import Path

import pytest

REPO = Path(__file__).parent.parent

# Parameters whose value is somewhere the process writes. `cache_dir` counts:
# a wrong cache is a re-fetch, which is the most expensive failure of the set.
_OUTPUT_PARAMS = ("output_dir", "output_path", "cache_dir", "out_dir", "out_path", "report_path")

# Files that legitimately take a relative default because they never write —
# none today; kept so an exemption has to be named rather than assumed.
_EXEMPT: set[str] = set()


def _python_files() -> list[Path]:
    return [
        path
        for directory in ("src/communitymech", "scripts")
        for path in sorted((REPO / directory).rglob("*.py"))
        if "__pycache__" not in path.parts
    ]


def _relative_string_default(node: ast.AST) -> str | None:
    """The literal if it is a bare relative path, else None."""
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        text = node.value
    elif (
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "Path"
        and node.args
        and isinstance(node.args[0], ast.Constant)
        and isinstance(node.args[0].value, str)
    ):
        text = node.args[0].value
    else:
        return None
    if not text or text.startswith("/") or text.startswith("~"):
        return None
    # Any relative string counts, with or without a separator. `Path("reports")`
    # has none and was one of the actual defects.
    return text


def test_no_output_parameter_defaults_to_a_relative_path():
    """A default that follows the cwd writes wherever the process happens to be."""
    offenders = []
    for path in _python_files():
        if path.name in _EXEMPT:
            continue
        tree = ast.parse(path.read_text())
        for node in ast.walk(tree):
            if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                continue
            args = node.args
            defaults = list(args.defaults)
            positional = (args.posonlyargs + args.args)[
                len(args.args) + len(args.posonlyargs) - len(defaults) :
            ]
            for arg, default in list(zip(positional, defaults, strict=False)) + list(
                zip(args.kwonlyargs, args.kw_defaults, strict=False)
            ):
                if default is None or arg.arg not in _OUTPUT_PARAMS:
                    continue
                literal = _relative_string_default(default)
                if literal:
                    offenders.append(
                        f"{path.relative_to(REPO)}:{default.lineno} "
                        f"{node.name}({arg.arg}={literal!r})"
                    )
    assert not offenders, (
        "output paths that follow the working directory — anchor them on "
        "`communitymech.paths` or `Path(__file__)` (#407):\n"
        + "\n".join(f"  {o}" for o in offenders)
    )


def test_the_scan_actually_inspects_the_tree():
    """Guards the test above: an empty or broken sweep would pass vacuously."""
    files = _python_files()
    assert len(files) > 40, f"expected the source tree, found {len(files)} files"
    assert any(path.name == "literature.py" for path in files)


def test_the_scan_would_catch_a_regression(tmp_path):
    """The rule detects the shape it is written for."""
    probe = tmp_path / "probe.py"
    probe.write_text(
        "from pathlib import Path\n"
        "def f(output_dir: Path = Path('reports')):\n"
        "    return output_dir\n"
    )
    tree = ast.parse(probe.read_text())
    function = next(n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef))

    assert _relative_string_default(function.args.defaults[0]) == "reports"
    assert _relative_string_default(ast.parse("f('a/b.html')").body[0].value.args[0]) == "a/b.html"
    # And it does not fire on the anchored forms actually used in the repo.
    anchored = ast.parse("def g(output_dir=REPORTS): pass")
    other = next(n for n in ast.walk(anchored) if isinstance(n, ast.FunctionDef))
    assert _relative_string_default(other.args.defaults[0]) is None


@pytest.mark.parametrize(
    ("module", "attribute"),
    [
        ("communitymech.paths", "REFERENCES_CACHE"),
        ("communitymech.paths", "REPORTS"),
        ("communitymech.paths", "DOCS"),
    ],
)
def test_the_anchored_locations_are_absolute_and_real(module, attribute):
    import importlib

    value = getattr(importlib.import_module(module), attribute)
    assert value.is_absolute()
    assert value.parent == REPO or value == REPO / value.name


def test_the_literature_cache_default_finds_the_committed_cache():
    """The failure this issue is really about: a cache miss, not a stray tree."""
    from communitymech.literature import LiteratureFetcher

    fetcher = LiteratureFetcher()

    assert fetcher.cache_dir.is_absolute()
    assert fetcher.cache_dir == REPO / "references_cache"
    assert len(list(fetcher.cache_dir.glob("*"))) > 100, "the default found an empty cache"


def test_an_explicit_cache_directory_still_wins(tmp_path):
    from communitymech.literature import LiteratureFetcher

    assert LiteratureFetcher(cache_dir=tmp_path).cache_dir == tmp_path
