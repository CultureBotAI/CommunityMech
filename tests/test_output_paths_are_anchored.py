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
_OUTPUT_PARAMS = (
    "output_dir",
    "output_path",
    "cache_dir",
    "out_dir",
    "out_path",
    "report_path",
    # Same relative-default-plus-mkdir shape as the literature cache, and worse
    # in consequence: a repair run rewrites tracked YAML while dropping its only
    # pre-edit backup in the caller's cwd, so a later restore cannot find it.
    "backup_dir",
)

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


# argparse/click flags whose value is a location the process writes.
_OUTPUT_FLAGS = ("--out", "--output", "--output-dir", "--output-path", "--cache-dir", "--report")


def _label(path: Path) -> str:
    """Repo-relative when it is a repo file, bare name for a tmp probe."""
    try:
        return str(path.relative_to(REPO))
    except ValueError:
        return path.name


def _offenders(files: list[Path]) -> list[str]:
    """Every relative output default in `files`, as `path:line description`."""
    found = []
    for path in files:
        if path.name in _EXEMPT:
            continue
        tree = ast.parse(path.read_text())
        for node in ast.walk(tree):
            # Function and method parameter defaults.
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                args = node.args
                defaults = list(args.defaults)
                positional = (args.posonlyargs + args.args)[
                    len(args.args) + len(args.posonlyargs) - len(defaults) :
                ]
                pairs = list(zip(positional, defaults, strict=False)) + list(
                    zip(args.kwonlyargs, args.kw_defaults, strict=False)
                )
                for arg, default in pairs:
                    if default is None or arg.arg not in _OUTPUT_PARAMS:
                        continue
                    literal = _relative_string_default(default)
                    if literal:
                        found.append(
                            f"{_label(path)}:{default.lineno} "
                            f"{node.name}({arg.arg}={literal!r})"
                        )
            # `add_argument("--out", default=...)`. This is the class that
            # started the whole thing — #391 was an argparse default, and the
            # first version of this guard could not see one, so six anchored
            # parameter defaults sat behind flags that still followed the cwd
            # (#409 review).
            elif isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
                if node.func.attr not in ("add_argument", "option", "argument"):
                    continue
                flags = [
                    a.value
                    for a in node.args
                    if isinstance(a, ast.Constant) and isinstance(a.value, str)
                ]
                if not any(flag in _OUTPUT_FLAGS for flag in flags):
                    continue
                for keyword in node.keywords:
                    if keyword.arg != "default":
                        continue
                    literal = _relative_string_default(keyword.value)
                    if literal:
                        found.append(
                            f"{_label(path)}:{keyword.value.lineno} "
                            f"{'/'.join(flags)} default={literal!r}"
                        )
    return found


def test_no_output_default_follows_the_working_directory():
    """A default that follows the cwd writes wherever the process happens to be."""
    assert not _offenders(_python_files()), (
        "output paths that follow the working directory — anchor them on "
        "`communitymech.paths` or `Path(__file__)` (#407):\n"
        + "\n".join(f"  {o}" for o in _offenders(_python_files()))
    )


def test_the_scan_actually_inspects_the_tree():
    """Guards the sweep above: an empty file list would pass vacuously."""
    files = _python_files()
    assert len(files) > 40, f"expected the source tree, found {len(files)} files"
    assert any(path.name == "literature.py" for path in files)


@pytest.mark.parametrize(
    ("name", "source", "needle"),
    [
        ("parameter default", "def f(output_dir='reports'):\n    pass\n", "output_dir="),
        (
            "Path() parameter default",
            "def f(output_dir=Path('reports')):\n    pass\n",
            "output_dir=",
        ),
        ("backup_dir", "def f(backup_dir=Path('.backups')):\n    pass\n", "backup_dir="),
        (
            "argparse default",
            "p.add_argument('--out', default=Path('reports/x.tsv'))\n",
            "--out default=",
        ),
        (
            "argparse output-dir",
            "p.add_argument('--output-dir', default='docs/x')\n",
            "--output-dir default=",
        ),
    ],
)
def test_the_scan_detects_each_shape_it_claims_to(tmp_path, name, source, needle):
    """Runs a synthetic offender through the *whole* scan, not just its helper.

    Emptying `_OUTPUT_PARAMS` left the suite green: the old vacuity guard only
    counted files, and the positive control called `_relative_string_default`
    directly, so nothing exercised the walk itself (#409 review).
    """
    probe = tmp_path / "probe.py"
    probe.write_text("from pathlib import Path\n" + source)

    found = _offenders([probe])

    assert found, f"the scan misses a {name}"
    assert any(needle in entry for entry in found), found


def test_the_scan_leaves_anchored_forms_alone(tmp_path):
    """A guard that fires on the fix would get switched off."""
    probe = tmp_path / "ok.py"
    probe.write_text(
        "from pathlib import Path\n"
        "from communitymech.paths import REPORTS\n"
        "def f(output_dir=REPORTS):\n    pass\n"
        "def g(output_dir=Path('/abs/reports')):\n    pass\n"
        "p.add_argument('--out', default=REPORTS / 'x.tsv')\n"
        "def h(name='report.txt'):\n    pass\n"
    )

    assert _offenders([probe]) == []


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


@pytest.mark.parametrize("attribute", ["REFERENCES_CACHE", "REPORTS", "DOCS", "KB_COMMUNITIES"])
def test_the_anchored_locations_are_under_the_repo(attribute):
    """`REPO in value.parents`, not "direct child of the repo".

    The first version asserted `value.parent == REPO or value == REPO / name` —
    two spellings of the same predicate, so the `or` was inert. The tell was that
    `KB_COMMUNITIES` was the one constant left out of the list: it would have
    failed, since its parent is `REPO/"kb"` (#409 review).
    """
    import importlib

    value = getattr(importlib.import_module("communitymech.paths"), attribute)

    assert value.is_absolute()
    assert REPO in value.parents, f"{attribute} is not under the repo"


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
