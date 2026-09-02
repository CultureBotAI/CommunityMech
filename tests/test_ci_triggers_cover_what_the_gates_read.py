"""A gate that cannot be triggered by its own input is not a gate (#471).

`label-correspondence.yaml` runs `just validate-terms-taxa`, whose entire input
is `kb/taxa/*.yaml`, and `just validate-products`, whose config carries a
`taxa_yaml` target. Neither could run on a change to a taxon record: `kb/taxa`
appeared in **no** workflow's `paths:` filter. Verified by opening a PR that
touched only `kb/taxa/` (#629, closed unmerged) — it drew exactly one check,
`vendored-sync`, the one workflow with no filter, which reads no YAML at all.

This is the #350/#471 defect a third time. Each previous instance was fixed by
adding one directory to one filter, which fixes the instance and not the class:
nothing connected *what a workflow runs* to *what can trigger it*, so the next
surface to be added was silently unguarded again. `data/isolates` took two PRs
(#350, #473) to be genuinely covered for the same reason.

These tests derive the inputs from the justfile recipes each workflow actually
invokes, so a new recipe, a new target in `conf/id_label_targets.yaml`, or a new
data directory fails here rather than in six months' worth of unvalidated
commits.

Pure parsing — no network, no OAK, no `just` execution — so it runs in the fast
suite alongside the gates it is about.
"""

from __future__ import annotations

import pathlib
import re

import pytest
import yaml

REPO = pathlib.Path(__file__).parent.parent
WORKFLOWS = REPO / ".github/workflows"
JUSTFILE = REPO / "justfile"

# The data surfaces a gate can read. Deliberately a prefix list and not "any
# path-looking token": a recipe mentions plenty of paths it does not treat as
# input (report destinations, `-s schema.yaml`), and asserting on those would
# make this test noisy enough to be disabled, which is how guards die.
DATA_ROOTS = ("kb/", "data/", "output/")

# A path rooted at one of the data surfaces, DERIVED from DATA_ROOTS rather than
# spelling the roots a second time. The two were separate literals, so adding a
# fourth surface to DATA_ROOTS left this regex blind to it: recipes reading the
# new root reported no inputs and the coverage assertion passed by having nothing
# to check (#635). That is the "list that cannot notice a new member" defect this
# module exists to gate — one source now, so it cannot recur here.
_ROOT_ALTERNATION = "|".join(re.escape(root.rstrip("/")) for root in DATA_ROOTS)
_INPUT_GLOB = re.compile(rf"(?<![\w/.-])((?:{_ROOT_ALTERNATION})/[\w*.-]+(?:/[\w*.-]+)*)")


def _workflow_paths(document: dict) -> list[str] | None:
    """The pull_request `paths:` filter, or None for "runs on everything".

    `on:` is the YAML 1.1 boolean `True` after parsing, which is the single
    most common way a workflow-reading test silently checks nothing.
    """
    triggers = document.get("on", document.get(True)) or {}
    if not isinstance(triggers, dict) or "pull_request" not in triggers:
        return None
    config = triggers["pull_request"] or {}
    return config.get("paths")


def _as_regex(pattern: str) -> re.Pattern[str]:
    """A GitHub `paths:` pattern as a regex.

    `**` crosses directory separators, `*` does not — the distinction that
    decides whether `kb/**` covers `kb/taxa/x.yaml` (it does) and whether
    `kb/*.yaml` does (it does not).
    """
    out, index = [], 0
    while index < len(pattern):
        char = pattern[index]
        if pattern.startswith("**", index):
            out.append(".*")
            index += 2
        elif char == "*":
            out.append("[^/]*")
            index += 1
        else:
            out.append(re.escape(char))
            index += 1
    return re.compile(f"^{''.join(out)}$")


def _probes(glob: str) -> list[str]:
    """Concrete paths inside `glob`, for asking whether a filter covers it.

    Probing beats globbing the real files: an empty or not-yet-built directory
    (`output/kgx/` on a fresh checkout) would expand to nothing and the check
    would pass by finding no files to be uncovered — vacuous in exactly the
    situation it is meant to catch.

    Two forms, because a recipe names its input both ways. `kb/communities/*.yaml`
    is a file glob, but `record="kb/communities/$(basename …)"` yields the bare
    directory `kb/communities`, and asking whether `kb/communities/**` covers the
    literal string `kb/communities` answers no — a false positive on a path that
    is plainly covered.
    """
    concrete = glob.replace("**", "probe").replace("*", "probe")
    return [concrete] if pathlib.PurePath(concrete).suffix else [concrete, f"{concrete}/probe.yaml"]


def _covered(path: str, patterns: list[str]) -> bool:
    """Anchored deliberately: a GitHub `paths:` pattern is rooted at the repo.

    `kb/taxa/**` does not match `vendor/kb/taxa/x.yaml`. This used to pick
    `.search` for `/**` patterns and `.match` otherwise, which chose between two
    identical behaviours — `_as_regex` anchors both ends, so the branch was dead
    and implied an unanchored semantics the code never had (#633).
    """
    return any(_as_regex(pattern).match(path) for pattern in patterns)


def _glob_covered(glob: str, patterns: list[str]) -> bool:
    return any(_covered(probe, patterns) for probe in _probes(glob))


def _recipe_bodies() -> dict[str, tuple[list[str], str]]:
    """recipe name -> (dependency names, body text) from the justfile."""
    recipes: dict[str, tuple[list[str], str]] = {}
    name, deps, body = None, [], []
    for line in JUSTFILE.read_text(encoding="utf-8").splitlines():
        # Parameters are not all `FILE`-shaped: `validate-strict *args:` takes a
        # variadic lowercase one, and requiring uppercase silently dropped that
        # recipe — the single most load-bearing gate in the repo — from the
        # parse. The self-check below exists because this test found that itself.
        header = re.match(
            r"^([a-zA-Z][\w-]*)"
            r"(?:\s+[+*]?[A-Za-z_][\w-]*(?:=(?:\"[^\"]*\"|'[^']*'|\S+))?)*"
            r"\s*:(?!=)(.*)$",
            line,
        )
        if header:
            if name:
                recipes[name] = (deps, "\n".join(body))
            name = header.group(1)
            deps = [d for d in header.group(2).split() if re.fullmatch(r"[a-zA-Z][\w-]*", d)]
            body = []
        elif name and (line.startswith((" ", "\t")) or not line.strip()):
            body.append(line)
        elif line.strip() and not line.startswith("#"):
            if name:
                recipes[name] = (deps, "\n".join(body))
            name, deps, body = None, [], []
    if name:
        recipes[name] = (deps, "\n".join(body))
    return recipes


def _inputs_of(recipe: str, recipes: dict, seen: set[str] | None = None) -> set[str]:
    """Data-surface globs a recipe reads, through dependencies AND `just` calls.

    Both edges, because a recipe delegates either way. `check-docs-current` runs
    `just gen-html` from its body rather than declaring it, and following only
    declared dependencies means a recipe that delegates *entirely* reports no
    inputs — so the coverage assertion would pass by finding nothing to check,
    which is the vacuous pass this whole module exists to close (#634).
    """
    seen = seen if seen is not None else set()
    if recipe in seen or recipe not in recipes:
        return set()
    seen.add(recipe)
    deps, body = recipes[recipe]
    # Comment lines are prose about the recipe, not input to it. `check-docs-current`
    # explains at length why it does NOT run `just gen-umap` — naming
    # data/embeddings/*.tsv.gz in the course of saying so (#602). Reading that as an
    # input reports a gap in the one place the justfile documents there is none.
    code = "\n".join(line for line in body.splitlines() if not line.lstrip().startswith("#"))
    found = {m.group(1) for m in _INPUT_GLOB.finditer(code)}
    for dep in [*deps, *re.findall(r"\bjust\s+([a-zA-Z][\w-]*)", code)]:
        found |= _inputs_of(dep, recipes, seen)
    return found


def _workflow_files() -> list[pathlib.Path]:
    return sorted(p for p in WORKFLOWS.glob("*.y*ml"))


def _steps(document: dict) -> list[str]:
    """Every recipe a workflow causes to run, however it says so.

    Two forms now, because the id/label gate moved to a reusable workflow in
    claw (#731). A job that is `uses:` plus `with:` carries no `steps:` at all,
    so reading only `run:` blocks reported that nothing runs Engine B -- and
    three tests went red on main saying exactly that.

    The recipe names in `with:` are read as commands, which is what they become:
    the reusable workflow runs `just <input>`. The local workflow names them
    explicitly rather than relying on claw's defaults, so this stays answerable
    from this repository.
    """
    commands = []
    for job in (document.get("jobs") or {}).values():
        if not isinstance(job, dict):
            continue
        for step in job.get("steps") or []:
            if isinstance(step, dict) and isinstance(step.get("run"), str):
                commands.append(step["run"])
        for key, value in (job.get("with") or {}).items():
            if key.endswith("recipe") or key.endswith("recipes"):
                commands.extend(str(value).split())
    return commands


def test_the_justfile_parser_finds_the_recipes_this_test_relies_on():
    """A parser that silently found nothing would make every test below pass."""
    recipes = _recipe_bodies()
    for expected in ("validate-terms-taxa", "validate-products", "validate-strict", "qc"):
        assert expected in recipes, f"justfile parser missed {expected!r}"
    assert "kb/taxa/*.yaml" in _inputs_of("validate-terms-taxa", recipes), (
        "the parser does not see kb/taxa/*.yaml in validate-terms-taxa, so the "
        "coverage assertions below cannot fail for the reason they exist"
    )


@pytest.mark.parametrize("root", DATA_ROOTS)
def test_the_input_scanner_covers_every_declared_data_root(root: str):
    """The derivation in #635 is now the untested part, so test it.

    Parametrised over DATA_ROOTS itself, not over a written-out list of roots —
    a second literal is precisely what caused #635.
    """
    body = f"    uv run thing {root}records/*.yaml\n"
    found = {m.group(1) for m in _INPUT_GLOB.finditer(body)}
    assert found == {f"{root}records/*.yaml"}, (
        f"the input scanner does not see paths under the declared root {root!r}, so "
        f"recipes reading it report no inputs and the coverage checks pass by having "
        f"nothing to check (#635). Found: {found}"
    )


def test_inputs_are_followed_through_a_recipe_that_only_delegates():
    """A recipe whose body is `just other` must still report other's inputs.

    Synthetic, not read off the justfile: every real delegation today happens to
    name its input directly too, so a regression here would change no verdict and
    no assertion over real data could notice. That is exactly why it needs pinning
    — a recipe added later that only delegates would report no inputs, and the
    coverage check would pass by having nothing to check (#634).
    """
    recipes = {
        "gate": ([], "    just inner\n"),
        "inner": ([], "    uv run thing kb/taxa/*.yaml\n"),
        "declared": (["inner"], "    echo hi\n"),
        "loop": ([], "    just loop\n"),  # a cycle must terminate, not recurse forever
    }
    assert _inputs_of("gate", recipes) == {"kb/taxa/*.yaml"}, "body `just` call not followed"
    assert _inputs_of("declared", recipes) == {"kb/taxa/*.yaml"}, "dependency not followed"
    assert _inputs_of("loop", recipes) == set()


# Roots whose contents a build produces rather than the checkout providing. A
# `paths:` filter cannot usefully name one: the directory is gitignored, so no
# file under it ever appears in a pull request, and listing it advertises a
# trigger that can never fire. `output/kgx/**` sat in label-correspondence's
# filter for exactly that reason and was inert (#686).
#
# The obligation for a generated input is different in kind, not absent: the
# workflow must BUILD it before the step that reads it. That is
# `tests/test_generated_gate_inputs_are_built_in_ci.py`, and it is why these
# globs are exempted here rather than simply ignored.
_GENERATED_ROOTS = ("output/",)


def _is_generated(glob: str) -> bool:
    return glob.startswith(_GENERATED_ROOTS)


@pytest.mark.parametrize("workflow", [p.name for p in _workflow_files()])
def test_every_data_surface_a_workflow_reads_can_also_trigger_it(workflow: str):
    """The gate. A step reading kb/taxa in a workflow kb/taxa cannot trigger.

    Covers two ways a step names its input: through a `just` recipe, and as a
    literal path in the `run:` block. Several workflows invoke a gate without
    `just` at all — `xargs -0 uv run linkml-validate`, `uv run communitymech
    audit-network`, `python -m communitymech.export` — and following only recipes
    left those steps unexamined (#636).

    What this still cannot see: a tool whose input paths live in Python rather
    than on the command line. `communitymech audit-network` reads kb/communities
    and data/isolates from inside the package, and no workflow/justfile parsing
    reveals that. `test_a_data_directory_is_not_invisible_to_every_workflow` is
    the weaker backstop for that case; #636 holds the decision.
    """
    document = yaml.safe_load((WORKFLOWS / workflow).read_text(encoding="utf-8"))
    patterns = _workflow_paths(document)
    if patterns is None:
        return  # no filter: everything triggers it, nothing to check

    recipes = _recipe_bodies()
    uncovered = {}
    for command in _steps(document):
        code = "\n".join(line for line in command.splitlines() if not line.strip().startswith("#"))
        for invoked in re.findall(r"\bjust\s+([a-zA-Z][\w-]*)", code):
            for glob in _inputs_of(invoked, recipes):
                if not _is_generated(glob) and not _glob_covered(glob, patterns):
                    uncovered.setdefault(glob, set()).add(f"just {invoked}")
        # Literal paths in the step itself, for the gates that skip `just`.
        for glob in {m.group(1) for m in _INPUT_GLOB.finditer(code)}:
            if not _is_generated(glob) and not _glob_covered(glob, patterns):
                uncovered.setdefault(glob, set()).add("a run: step directly")

    assert not uncovered, (
        f"{workflow} runs steps that read data this workflow's paths filter does "
        f"not match, so a PR changing only that data does not run them (#471). "
        + "; ".join(f"{g} (read by {', '.join(sorted(r))})" for g, r in sorted(uncovered.items()))
        + f". Filter is: {patterns}"
    )


def test_every_engine_b_target_can_trigger_the_workflow_that_runs_it():
    """`conf/id_label_targets.yaml` is a list that must not gain a member silently.

    The globs live in config rather than in the recipe, so the test above cannot
    see them: `just validate-products` names only the config file. A target
    added here without a matching trigger path is checked locally and never in
    CI — which is what `taxa_yaml` was.
    """
    targets = yaml.safe_load((REPO / "conf/id_label_targets.yaml").read_text())["targets"]
    globs = [t["glob"] for t in targets if t.get("glob") and not _is_generated(t["glob"])]
    assert globs, "no glob targets parsed; this test would pass vacuously"

    running = [
        path
        for path in _workflow_files()
        if any("validate-products" in c for c in _steps(yaml.safe_load(path.read_text())))
    ]
    assert running, "no workflow runs `just validate-products`; Engine B is not a gate"

    for path in running:
        patterns = _workflow_paths(yaml.safe_load(path.read_text()))
        if patterns is None:
            continue
        missing = [g for g in globs if not _glob_covered(g, patterns)]
        assert not missing, (
            f"{path.name} runs Engine B but its paths filter does not match "
            f"{missing} — those targets are validated locally and never in CI (#471)"
        )


def test_a_data_directory_is_not_invisible_to_every_workflow():
    """The whole-repo view: no data surface may be outside every filter.

    kb/taxa passed each per-workflow check for years by being absent from all of
    them at once. Enumerating the directories that exist, rather than the ones a
    filter mentions, is what makes a newly added surface fail here.

    A backstop, not the real check: being matched by *some* filter is weaker than
    being matched by the filter of a workflow that validates it. The per-workflow
    test above is what establishes that. This one only catches a surface no
    workflow can see at all.
    """
    # Existence filtered BEFORE iterating, not in the comprehension's `if`: that
    # clause is evaluated after `iterdir()`, so it never guarded the call it was
    # written to guard. `output/` is gitignored with no tracked files, so it is
    # absent on a fresh clone — i.e. on every CI runner — and this raised
    # FileNotFoundError there while passing locally, where output/ has been built
    # (#632). The #602 shape, inside the test meant to prevent it.
    roots = [REPO / root.rstrip("/") for root in DATA_ROOTS]
    surfaces = sorted(
        f"{directory.parent.name}/{directory.name}"
        for root in roots
        if root.is_dir()
        for directory in root.iterdir()
        if directory.is_dir() and any(directory.glob("*.yaml"))
    )
    assert surfaces, "found no data directories; this test would pass vacuously"

    filters = []
    for path in _workflow_files():
        patterns = _workflow_paths(yaml.safe_load(path.read_text()))
        if patterns:
            filters.extend(patterns)

    orphans = [s for s in surfaces if not _covered(f"{s}/probe.yaml", filters)]
    assert not orphans, (
        f"these data directories hold YAML records but match no workflow's paths "
        f"filter, so changing one of them runs no validation at all (#471): {orphans}"
    )
