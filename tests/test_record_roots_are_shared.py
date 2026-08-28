"""Every gate looks at the same record directories (#350).

`data/isolates/**` was added to the network-quality workflow's trigger paths,
and separately to `validate_strict`, `validate-all`, `validate-terms-all` and
`validate-references-all`. The network auditor was not: it kept
`communities_dir: Path = Path("kb/communities")`. So editing an isolate re-ran a
suite whose only isolate coverage was schema validation, and the interactions in
`data/isolates` — 12 of them across 3 records — were never audited at all.

Nothing was wrong with any of them, which is the point. The gap was invisible
because it produced no findings either way, and would have stayed invisible
until an isolate gained a dangling reference.

`default_record_roots()` is now the single source, in `communitymech.paths`, and
this file checks the places that must agree with it. Two of those checks are
about *shape* rather than content, because the failure mode was never a wrong
list — it was a second list nobody remembered existed:

* the CLI's `--communities-dir` must default to `None`. It defaulted to the
  string `"kb/communities"`, which silently overrode the auditor's own default:
  after the auditor was fixed, `audit-network` still reported 312 records. The
  fix looked wired and was not, and only running it and reading the count found
  that.
* the workflow's trigger paths must mention every root. A gate that covers a
  directory but never fires on changes to it is covered only by accident.
"""

from __future__ import annotations

import ast
import pathlib
import re

import pytest
import yaml

from communitymech.paths import default_record_roots, taxon_descriptor_roots

REPO = pathlib.Path(__file__).parent.parent
WORKFLOW = REPO / ".github/workflows/network-quality.yml"


@pytest.fixture(scope="module")
def roots() -> list[pathlib.Path]:
    return default_record_roots()


def test_the_roots_exist_and_hold_records(roots):
    """Guard: a root that does not exist makes every sweep below vacuous."""
    assert len(roots) >= 2
    for root in roots:
        assert root.is_dir(), f"{root} is not a directory"
        assert list(root.glob("*.yaml")), f"{root} holds no records"


def test_the_auditor_defaults_to_all_of_them(roots):
    """The defect itself: the audit saw one root while the validators saw two."""
    from communitymech.network.auditor import NetworkIntegrityAuditor

    assert NetworkIntegrityAuditor().record_dirs == roots


def test_a_single_directory_is_still_accepted():
    """`NetworkIntegrityAuditor(tmp_path)` must keep meaning what it did.

    Widening the default would be a poor trade if it broke every caller and
    test that audits one directory deliberately.
    """
    from communitymech.network.auditor import NetworkIntegrityAuditor

    only = REPO / "kb/communities"
    assert NetworkIntegrityAuditor(only).record_dirs == [only]
    assert NetworkIntegrityAuditor([only]).record_dirs == [only]


def test_validate_strict_uses_the_shared_list():
    """Parsed, not imported: importing the script pulls in linkml and forks.

    Asserted positively — that `DEFAULT_ROOTS` is assigned from a call to
    `default_record_roots` — rather than by checking the old literals are
    absent, which would also pass on a file that stopped defining roots.
    """
    tree = ast.parse((REPO / "scripts/validate_strict.py").read_text(encoding="utf-8"))
    assignments = [
        node
        for node in ast.walk(tree)
        if isinstance(node, ast.Assign)
        and any(isinstance(t, ast.Name) and t.id == "DEFAULT_ROOTS" for t in node.targets)
    ]
    assert len(assignments) == 1, "DEFAULT_ROOTS is gone or defined more than once"
    value = assignments[0].value
    assert isinstance(value, ast.Call), "DEFAULT_ROOTS is a literal again, not the shared list"
    assert getattr(value.func, "id", None) == "default_record_roots"


def test_the_cli_does_not_override_the_default():
    """A literal default here silently defeats the auditor's own (#350).

    This is the check that would have caught the half-fix: the auditor was
    already correct while `audit-network` still reported 312 records, because
    click passed `"kb/communities"` explicitly on every invocation.
    """
    tree = ast.parse((REPO / "src/communitymech/cli.py").read_text(encoding="utf-8"))
    # Scoped to `audit_network`'s own decorators. A module-wide sweep also flags
    # `generate-umap`, which takes the same option name but is a visualisation
    # rather than a gate — whether isolates belong in the UMAP is a separate
    # question (#519), not something to settle by widening this test.
    command = next(
        node
        for node in ast.walk(tree)
        if isinstance(node, ast.FunctionDef) and node.name == "audit_network"
    )
    offenders = []
    for node in command.decorator_list:
        if not isinstance(node, ast.Call):
            continue
        if getattr(node.func, "attr", None) != "option":
            continue
        names = [a.value for a in node.args if isinstance(a, ast.Constant)]
        if "--communities-dir" not in names:
            continue
        for keyword in node.keywords:
            if keyword.arg == "default" and not (
                isinstance(keyword.value, ast.Constant) and keyword.value.value is None
            ):
                offenders.append(ast.unparse(keyword.value))
    assert offenders == [], (
        "`--communities-dir` has a non-None default "
        f"({offenders}), which overrides `default_record_roots()` and drops "
        "`data/isolates` from the audit without changing anything visible (#350)"
    )


def test_the_workflow_fires_on_every_root(roots):
    """A gate that covers a directory but never triggers on it is luck."""
    workflow = yaml.safe_load(WORKFLOW.read_text(encoding="utf-8"))
    # `on` is parsed as the boolean True by YAML 1.1, which is why this reads
    # the key rather than the attribute.
    triggers = workflow.get("on") or workflow.get(True)
    patterns = triggers["pull_request"]["paths"]
    missing = [
        str(root.relative_to(REPO))
        for root in roots
        if not any(str(root.relative_to(REPO)) in pattern for pattern in patterns)
    ]
    assert missing == [], (
        "the network-quality workflow audits these directories but does not "
        f"trigger on changes to them: {missing}. Add them to `paths:` (#350)."
    )


def test_no_constructor_hardcodes_the_old_root():
    """The click default was one of two identical sites (#521).

    `BatchReporter.__init__` took `communities_dir: Path = Path("kb/communities")`
    and passed it to the auditor explicitly, so widening the auditor's default
    did nothing for it — the same half-fix, in the tool that repairs exactly
    what the audit reports. `cli.py` builds it as bare `BatchReporter()` in four
    places, so the literal is what ran every time.

    This walks the whole package rather than naming the two known offenders,
    because the point is the *shape*: any default that hardcodes a record
    directory reintroduces the drift `default_record_roots()` exists to remove.
    `BrowserExporter` is exempt — it is an export feeding the browser UI, and
    whether isolates belong in a visualisation is #519, not a coverage gap.
    """
    # Visualisation and export paths, not gates. Whether isolates belong in a
    # UMAP or the browser UI is a modelling question (#519), and answering it by
    # widening a coverage test would decide it silently.
    exempt = {"browser_export.py", "render.py", "umap_generator.py"}
    offenders = []
    for path in sorted((REPO / "src/communitymech").rglob("*.py")):
        if path.name in exempt:
            continue
        tree = ast.parse(path.read_text(encoding="utf-8"))
        for node in ast.walk(tree):
            if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                continue
            arguments = node.args
            names = [a.arg for a in arguments.posonlyargs + arguments.args + arguments.kwonlyargs]
            defaults = list(arguments.defaults) + list(arguments.kw_defaults)
            aligned = names[len(names) - len(defaults) :]
            for name, default in zip(aligned, defaults, strict=True):
                if name != "communities_dir" or default is None:
                    continue
                rendered = ast.unparse(default)
                if "kb/communities" in rendered or "data/isolates" in rendered:
                    offenders.append(f"{path.name}:{node.lineno} {name}={rendered}")
    assert offenders == [], (
        "these hardcode a record directory as a default, which overrides "
        "`default_record_roots()` at the call site and silently narrows what "
        "gets audited (#350, #521):\n" + "\n".join(offenders)
    )


def test_the_gtdb_gates_sweep_every_root_a_grounding_can_live_in():
    """A GTDB gate that skips a root reports clean on what it never read (#656).

    Three gates carried their own `RECORD_DIRS = ("kb/communities",
    "data/isolates")`. The schema does not agree: `gtdb_classification` lives on
    `TaxonDescriptor`, which hangs off `CommonTaxon.taxon_term` as well as
    `MicrobialCommunity.taxonomy[].taxon_term`, and `CommonTaxon` records live in
    `kb/taxa`. The omission was invisible because `kb/taxa` holds no groundings
    yet — so the gates found nothing either way.

    Asserted positively, on the value each module computes, rather than by
    grepping for the old literal: a file that stopped defining `RECORD_DIRS`
    entirely would pass a negative check.
    """
    import importlib.util

    expected = tuple(str(p.relative_to(REPO)) for p in taxon_descriptor_roots())
    modules = (
        "test_gtdb_grounding_freshness",
        "test_gtdb_not_attempted",
        "test_gtdb_uncurated_blocks_match_the_tool",
    )
    wrong = {}
    for name in modules:
        spec = importlib.util.spec_from_file_location(name, REPO / f"tests/{name}.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        actual = tuple(getattr(module, "RECORD_DIRS", ()))
        if actual != expected:
            wrong[name] = actual

    assert not wrong, (
        f"these GTDB gates do not sweep every root a grounding can live in. "
        f"Expected {expected}, got {wrong}. Use `taxon_descriptor_roots()` (#656)."
    )


def test_the_two_root_lists_stay_distinct():
    """Widening `default_record_roots()` would be the wrong fix (#656).

    `kb/taxa` holds `CommonTaxon`, not `MicrobialCommunity`. Callers that mean
    community records — the network auditor, `validate_strict` — must not begin
    sweeping a different root class because a GTDB gate needed a wider list.
    """
    community = default_record_roots()
    descriptor = taxon_descriptor_roots()

    assert (REPO / "kb/taxa") not in community, (
        "`default_record_roots()` now includes kb/taxa, which holds CommonTaxon "
        "records; the network auditor and validate_strict would sweep a root "
        "class they do not model"
    )
    assert set(community) < set(descriptor), "the descriptor roots must be a strict superset"


# --- tests are gates too (#689) -------------------------------------------
#
# `test_no_constructor_hardcodes_the_old_root` scans `src/communitymech/**`. But
# many of this repository's gates ARE tests, and a test that globs
# `kb/communities` alone is invisible to that scan. That is how the #529
# discriminator swept one root for months, and it is why the check below
# exists: `tests/` is where the omission actually happens.
#
# Only modules that SWEEP the directory are classified. A test naming one record
# as a fixture is not making a scope decision, so asking it to justify itself
# would be noise that trains people to add entries without thinking.
#
# Two buckets, and the difference is evidence, not taste. `data/isolates` holds
# 4 records carrying 66 snippets, 3 `ecological_interactions`, 3
# `gtdb_classification` blocks, 0 `cultivation_setup` and 0 `go_terms`; none of
# the 4 is rendered into `docs/` (324 pages for 324 kb/communities records).
_COMMUNITY_ONLY: dict[str, str] = {
    "test_writers_leave_a_trace.py": (
        "scoped by its own argument to tools that edit kb/communities records; "
        "its _EXEMPT entries name research/ and data/ingredients explicitly"
    ),
    "test_docs_do_not_contradict_the_kb.py": (
        "docs/communities is rendered from kb/communities only -- 324 pages for "
        "324 records, and 0 of the 4 isolates has a page"
    ),
    "test_network_palette.py": (
        "the per-community palette is generated for those same rendered pages"
    ),
}

# Sweeps one root where the other holds the same kind of content. Each line is
# work, not a decision -- the measured consequence is stated so that "does this
# matter" is not re-litigated from scratch each time.
_OWED_BOTH_ROOTS: dict[str, str] = {}
# EMPTY as the result of the work, not for never having been used. All eleven
# were converted in #689: each now sweeps `record_files()` (or, for the two GTDB
# gates, `taxon_descriptor_roots()` with the shared `iter_taxon_descriptors`
# walker, because a CommonTaxon has no `taxonomy` key for a directory fix to
# reach).
#
# Nothing new was found, and that was checked before the conversion rather than
# hoped for afterwards: the truncation gate examined 66 isolate snippets and
# flagged 0, no isolate interaction participant sits outside its taxonomy, and
# the auditor reports 0 issues of any kind across the 4 records. The value is
# that a defect arriving in an isolate tomorrow is now visible to eleven gates
# that could not have seen it.
#
# `test_network_auditor` was the sharpest of the eleven: it passed
# `communities_dir=` explicitly, silently replacing the auditor's own
# `default_record_roots()` default -- the shape #350 fixed IN the auditor and
# left standing in its test. The override is gone, so the default is now under
# test as much as the corpus is.

_SWEEP_MARKERS = ("kb/communities", '"kb" / "communities"')

# `_SHARED_MARKERS` used to short-circuit the scan: a module mentioning
# `record_files` was assumed converted and skipped. Reviewing #689 showed that is
# not sound. `test_no_vacuous_go_annotations` imported `record_files`, never
# called it -- its sweep read `(corpus or COMMUNITIES).glob(...)`, which the
# conversion's pattern did not match -- and ruff then deleted the unused import,
# leaving a module that looked converted, was not, and passed this scan twice
# over. Presence of a name is not proof of its use.
#
# The detection below is now the whole test: a module that still globs a constant
# bound to `kb/communities` is flagged whatever else it says. A genuinely
# converted module cannot trip it, because it no longer has such a glob.


def _code_only(text: str) -> str:
    """Source with docstrings and comments removed.

    The scan reads for a `kb/communities` glob, and prose contains those too:
    `test_isolates_are_covered_by_id_checks.py` DISCUSSES reverting a loop to
    `Path("kb/communities").glob("*.yaml")` in a docstring, and was flagged for
    describing the defect it exists to prevent. A guard that cannot tell code
    from commentary teaches people to reword their explanations.
    """
    without_strings = re.sub(r'("""|\'\'\')(?:.|\n)*?\1', '""', text)
    return re.sub(r"#[^\n]*", "", without_strings)


def _sweeping_test_modules() -> dict[str, str]:
    """Test modules that glob kb/communities and never name the other root."""
    found = {}
    for path in sorted((REPO / "tests").glob("test_*.py")):
        text = _code_only(path.read_text(encoding="utf-8"))
        if not any(marker in text for marker in _SWEEP_MARKERS):
            continue
        constants = re.findall(r"^\s*(\w+)\s*=\s*[^\n]*kb[\"/ ]*communities", text, re.M)
        globs_a_constant = any(
            re.search(rf"\b{name}\b[^\n]*\.glob\(|\.glob\([^\n]*\b{name}\b", text)
            for name in constants
        )
        inline_glob = re.search(r'kb/communities"\)\.glob|"communities"\)\.glob', text)
        if globs_a_constant or inline_glob:
            found[path.name] = text
    return found


def test_the_sweep_scanner_finds_modules():
    """Guard: a scanner returning nothing makes both checks below vacuous.

    Calibrated against `_COMMUNITY_ONLY` rather than a written-out number. The
    count legitimately FELL when #689 converted eleven modules, so a fixed
    threshold would have had to be lowered -- and a threshold that gets lowered
    to match reality is not measuring anything. What must stay true is that the
    scanner still finds the modules that are classified as single-root, because
    those are the ones the checks below are about.
    """
    found = set(_sweeping_test_modules())
    missing = sorted(set(_COMMUNITY_ONLY) - found)
    assert missing == [], (
        f"the scanner no longer sees these classified single-root modules, so "
        f"the checks below are not enforcing anything for them: {missing}. "
        f"Either they were converted -- in which case take them out of "
        f"`_COMMUNITY_ONLY` -- or `_sweeping_test_modules()` has broken (#689)."
    )
    assert found, "the scanner found no sweeping modules at all; detection has broken"


def test_every_sweeping_test_declares_its_scope():
    """A new corpus sweep must say which roots it means, when it is written."""
    unclassified = sorted(
        name
        for name in _sweeping_test_modules()
        if name not in _COMMUNITY_ONLY and name not in _OWED_BOTH_ROOTS
    )
    assert unclassified == [], (
        "these test modules sweep kb/communities and never mention the other "
        "root, and are in neither list:\n"
        + "\n".join(f"  {name}" for name in unclassified)
        + "\n\nPrefer fixing it to recording it: sweep `default_record_roots()` "
        "(or `taxon_descriptor_roots()` for a GTDB check). If kb/communities "
        "alone is genuinely right, add it to `_COMMUNITY_ONLY` with the reason; "
        "if it should cover both and does not yet, add it to `_OWED_BOTH_ROOTS` "
        "with what is being missed (#689)."
    )


def test_neither_scope_list_has_rotted():
    """A module that started sweeping both roots must leave the lists."""
    sweeping = set(_sweeping_test_modules())
    gone = sorted((set(_COMMUNITY_ONLY) | set(_OWED_BOTH_ROOTS)) - sweeping)
    assert gone == [], (
        "these are classified but no longer sweep a single root -- either they "
        f"were fixed, renamed, or deleted; take them out: {gone}"
    )
    assert not (set(_COMMUNITY_ONLY) & set(_OWED_BOTH_ROOTS)), "a module cannot be both"
    blank = sorted(
        name
        for name, why in {**_COMMUNITY_ONLY, **_OWED_BOTH_ROOTS}.items()
        if not (why or "").strip()
    )
    assert blank == [], f"a scope decision needs a reason: {blank}"


def test_the_owed_backlog_stays_empty():
    """It reached zero in #689. Re-entering it is a decision, not a drift."""
    assert _OWED_BOTH_ROOTS == {}, (
        "a test module has been recorded as sweeping one root where both apply:\n"
        + "\n".join(f"  {name}: {why}" for name, why in sorted(_OWED_BOTH_ROOTS.items()))
        + "\n\nThe list was emptied in #689 by converting all eleven. Prefer "
        "calling `record_files()` in the new test to re-opening the backlog; if "
        "the sweep genuinely cannot cover both roots, say why here."
    )
