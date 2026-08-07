"""Unquoted YAML scalars that a mid-line `#` silently truncates (#398).

In YAML a `#` **preceded by whitespace** opens a comment, even mid-value. So

    curation_note: rather than by decision (#376, #384).

parses as `rather than by decision (#376,`. The file is valid YAML, the value is
non-empty, and every schema check passes — which is how that exact line shipped,
losing the pointer to the issue the field existed for.

Re-serializing cannot reveal it: PyYAML emits the *truncated* value as good YAML,
so a load/dump round-trip compares equal to itself. The check reads raw lines.

`#` is legitimate in three places — a whole-line comment, inside a quoted scalar,
and inside a block scalar (`>`/`|`) where it is literal. Flagging any of those
would make the rule unusable, so the false-positive cases below matter as much as
the true positives.
"""

from __future__ import annotations

import subprocess
from pathlib import Path

import pytest
import yaml

from communitymech.validators.yaml_scalars import find_truncated_scalars

REPO = Path(__file__).parent.parent


def _write(tmp_path: Path, text: str, name: str = "probe.yaml") -> Path:
    path = tmp_path / name
    path.write_text(text)
    return path


@pytest.mark.parametrize(
    ("name", "text", "lost"),
    [
        ("plain mapping", "key: some text #376 here\n", "#376 here"),
        ("sequence item", "items:\n- some text #376 here\n", "#376 here"),
        ("nested mapping", "a:\n  b:\n    c: text #1 x\n", "#1 x"),
        (
            "after a block scalar ends",
            "notes: >\n  fine #376 here\nkey: bad #384 here\n",
            "#384 here",
        ),
        # The value *begins* with the hash, so the whole thing parses as null.
        # The first version searched inside the captured value, where a leading
        # `#` has no whitespace before it, and missed total loss (#399 review).
        ("leading hash parses as null", "notes: #398 documents why\n", "#398 documents why"),
        # A plain scalar wraps across lines; the truncation lands on the last
        # one. The first version only ever inspected the line the key was on,
        # and 5333 of the KB's scalars span several lines.
        (
            "wrapped scalar, hash on the last line",
            "notes: a long note wrapped by\n  an editor. (see #398)\n",
            "#398)",
        ),
    ],
)
def test_a_truncating_scalar_is_reported(tmp_path, name, text, lost):
    """Each of these loses data on parse — verified against PyYAML itself."""
    path = _write(tmp_path, text)
    issues = find_truncated_scalars(path)

    assert len(issues) == 1, f"{name}: expected one issue, got {issues}"
    assert lost in issues[0].lost

    # The premise: YAML really does drop it. Without this the test could be
    # asserting a rule nobody needs.
    parsed = yaml.safe_load(text)
    assert lost not in str(parsed), f"{name}: YAML kept the tail, nothing to report"


@pytest.mark.parametrize(
    ("name", "text"),
    [
        ("whole-line comment", "# a comment\nkey: value\n"),
        ("hash with no space", "key: see (#376) for detail\n"),
        ("single-quoted", "key: 'text with #376 inside'\n"),
        ("double-quoted", 'key: "text with #376 inside"\n'),
        ("folded block scalar", "notes: >\n  a note mentioning #376\n  and more\nother: fine\n"),
        ("literal block scalar", "notes: |\n  literal #376 text\nother: fine\n"),
        ("block scalar with indicator", "notes: >-\n  a note with #376\nother: fine\n"),
        ("blank line inside a block", "notes: >\n  first #376\n\n  key: value #384\nother: x\n"),
        ("mapping-shaped block body", "notes: >\n  key: value #376 here\nother: fine\n"),
        ("sequence-shaped block body", "notes: |\n  - item #376 here\nother: fine\n"),
        ("no hash at all", "key: ordinary text\n"),
        # Every one of these was a false positive before the rewrite. A quoted or
        # block scalar delimits itself, so a `#` after it cannot have eaten
        # anything the author wrote (#399 review).
        ("deliberate comment after a quoted value", 'key: "value" # a real comment\n'),
        ("deliberate comment after a single-quoted value", "key: 'value' # a real comment\n"),
        ("hash inside a quoted scalar in a flow mapping", '- { a: "x", b: "PR #105 reverted" }\n'),
        ("comment on a block scalar header", "notes: > # folded\n  key: value #384\nother: x\n"),
        ("block scalar as a bare sequence item", "notes:\n  - >\n    key: value #376 here\n"),
        ("prose quoted at both ends", 'note: "syntrophic" became obligate\n'),
    ],
)
def test_legitimate_hashes_are_not_reported(tmp_path, name, text):
    """False positives would make this rule unusable, so they are pinned too."""
    assert find_truncated_scalars(_write(tmp_path, text)) == [], name


def test_a_hash_inside_a_quoted_scalar_is_never_truncation(tmp_path):
    """The case that made the first version unusable outside the record trees.

    `conf/id_label_targets.yaml` carries `reason: "... (PR #105 reverted)"` inside
    a flow mapping. Judging quoting by whether the raw value starts and ends with
    a quote saw `{...}` and reported it; asking PyYAML for the scalar's style
    does not.
    """
    real = REPO / "conf/id_label_targets.yaml"
    reports = find_truncated_scalars(real)
    assert all(
        "#105" not in issue.lost for issue in reports
    ), "a hash inside a quoted scalar was reported as lost"


def test_the_record_trees_have_no_deliberate_trailing_comments(tmp_path):
    """Why the check is scoped to records rather than every YAML in the repo.

    A trailing comment on a *plain* scalar is genuinely ambiguous — nothing can
    tell "I meant a comment" from "I lost my tail". The record trees contain
    none, so the rule is unambiguous there. `conf/` and `.github/` use them
    deliberately, which is why they stay out of scope rather than being made to
    pass.
    """
    for directory in ("kb/communities", "data/isolates", "kb/taxa"):
        for path in sorted((REPO / directory).glob("*.yaml")):
            assert find_truncated_scalars(path) == [], f"{path.name} reports"


def test_the_line_number_and_key_are_usable(tmp_path):
    """A report that cannot be acted on is noise."""
    path = _write(tmp_path, "alpha: fine\nbeta: broken #1 here\n")
    issue = find_truncated_scalars(path)[0]

    assert issue.line == 2
    assert issue.key == "beta"
    assert issue.truncated_to == "broken"
    assert "Quote the value" in issue.message


def test_the_committed_kb_is_clean():
    """Every record, with a vacuity guard on the sweep."""
    scanned, issues = 0, []
    for directory in ("kb/communities", "data/isolates", "kb/taxa"):
        for path in sorted((REPO / directory).glob("*.yaml")):
            scanned += 1
            issues.extend(find_truncated_scalars(path))
    assert scanned > 300, f"expected the whole KB, scanned {scanned}"
    assert not issues, "truncated scalars:\n" + "\n".join(str(i) for i in issues)


def test_the_instance_that_shipped_is_caught(tmp_path):
    """The real defect, reconstructed by unquoting the line that now carries it.

    Reading it from git does not work: the note was added and fixed inside one
    PR, so the truncated form never reached `main`.
    """
    import re

    source = REPO / "kb/communities/Chlorochromatium_Aggregatum_Phototrophic_Consortium.yaml"
    text = source.read_text()
    assert 'curation_note: "' in text, "the note is no longer quoted; this test is stale"
    unquoted = re.sub(r'(curation_note: )"(.*)"', r"\1\2", text)

    issues = find_truncated_scalars(_write(tmp_path, unquoted))

    assert len(issues) == 1
    assert issues[0].key == "curation_note"
    assert "#384" in issues[0].lost, "the lost tail should name the dropped issue"


def test_validate_strict_reports_it(tmp_path):
    """It must fire through the CI gate, not only when called directly."""
    import re

    source = REPO / "kb/communities/Chlorochromatium_Aggregatum_Phototrophic_Consortium.yaml"
    unquoted = re.sub(r'(curation_note: )"(.*)"', r"\1\2", source.read_text())
    path = _write(tmp_path, unquoted, name="broken.yaml")

    result = subprocess.run(
        [
            "uv",
            "run",
            "python",
            "scripts/validate_strict.py",
            str(path),
            "--out",
            str(tmp_path / "report.tsv"),
        ],
        capture_output=True,
        text=True,
        cwd=REPO,
    )

    assert result.returncode == 1, "validate-strict passed a record it should fail"
    assert "yaml_truncated_scalar" in (result.stdout + result.stderr)


def test_linkml_validate_accepts_what_this_catches(tmp_path):
    """Why a raw-text check exists at all.

    If this ever starts failing, the schema layer gained the ability to see
    truncation and this validator can go.
    """
    import re

    source = REPO / "kb/communities/Chlorochromatium_Aggregatum_Phototrophic_Consortium.yaml"
    unquoted = re.sub(r'(curation_note: )"(.*)"', r"\1\2", source.read_text())
    path = _write(tmp_path, unquoted, name="accepted.yaml")

    result = subprocess.run(
        [
            "uv",
            "run",
            "linkml-validate",
            "-s",
            "src/communitymech/schema/communitymech.yaml",
            str(path),
        ],
        capture_output=True,
        text=True,
        cwd=REPO,
    )

    assert result.returncode == 0, "linkml-validate now rejects this — drop the raw-text check"


@pytest.mark.parametrize(
    ("name", "text"),
    [
        ("extra spaces before the hash", "key:   #398 documents why\n"),
        ("hash immediately after a wrapped line", "notes: text wrapping to\n  more #398 x\n"),
        # A *tab* before the hash is not this defect: YAML rejects the document
        # outright, which validate-strict already reports as a parse error.
    ],
)
def test_the_gap_before_the_hash_may_be_any_whitespace(tmp_path, name, text):
    """`lstrip()`, not a literal `" #"`.

    The remainder handed to this check starts wherever the scalar stopped, which
    is not always exactly one space before the hash.
    """
    assert find_truncated_scalars(_write(tmp_path, text)), name


@pytest.mark.parametrize(
    ("name", "text", "key"),
    [
        ("mapping", "alpha: fine\nbeta: broken #1 here\n", "beta"),
        ("sequence at the key's indent", "items:\n- broken #1 here\n", "items"),
        ("indented sequence", "items:\n  - broken #1 here\n", "items"),
        ("nested mapping", "a:\n  b:\n    c: broken #1 here\n", "c"),
    ],
)
def test_the_report_names_the_right_field(tmp_path, name, text, key):
    """A report naming the wrong field sends the reader to the wrong line.

    A block sequence may sit at the *same* indent as its key, so an entry has to
    accept an equal indent when walking out to the enclosing name. Requiring a
    strictly smaller one attributed eleven list items in
    `conf/id_label_targets.yaml` to whichever key happened to precede them.
    """
    issue = find_truncated_scalars(_write(tmp_path, text))[0]
    assert issue.key == key, name


# ---------------------------------------------------------------------------
# `require_gap`: extending the check to trees where a deliberate trailing
# comment is an idiom (#400). The strict rule reports 13 of those as
# truncation, which is why conf/ and .github/ were left unchecked entirely.
# ---------------------------------------------------------------------------

_IDIOMATIC_DIRS = ("conf", ".github/workflows", "vocab", "src/communitymech/schema")


def _idiomatic_files() -> list[Path]:
    repo = Path(__file__).parent.parent
    return [
        path
        for directory in _IDIOMATIC_DIRS
        for suffix in ("*.yaml", "*.yml")
        for path in sorted((repo / directory).rglob(suffix))
    ]


def test_the_idiomatic_trees_have_files_to_check():
    """Guard: an empty sweep would make the two tests below vacuous."""
    assert len(_idiomatic_files()) >= 15, _idiomatic_files()


def test_require_gap_silences_every_deliberate_trailing_comment():
    """The whole reason those trees were unchecked.

    Without `require_gap` these files produce 13 reports, all of them comments
    somebody wrote on purpose — a gate that cries wolf 13 times is one nobody
    runs.
    """
    strict = sum(len(find_truncated_scalars(p)) for p in _idiomatic_files())
    gapped = sum(len(find_truncated_scalars(p, require_gap=True)) for p in _idiomatic_files())
    assert strict > 0, (
        "the strict rule no longer reports anything in these trees, so the "
        "trailing-comment idiom may be gone and require_gap may be unnecessary"
    )
    assert gapped == 0, (
        f"require_gap still reports {gapped} deliberate comment(s); the "
        f"two-space convention no longer holds across these trees (#400)"
    )


@pytest.mark.parametrize(
    ("label", "text", "expected"),
    [
        ("one space is prose the author lost", "key: some text #400 lost here\n", 1),
        ("no space at all", "key: some text#400 lost here\n", 0),
        ("two spaces is a deliberate comment", "key: value  # on purpose\n", 0),
        ("three spaces, as the repo actually writes them", "key: value   # on purpose\n", 0),
        ("a quoted value is never reported", 'key: "text # inside"  # comment\n', 0),
    ],
)
def test_the_gap_rule_case_by_case(tmp_path, label, text, expected):
    """`#` with no preceding space does not open a comment in YAML at all.

    So `some text#400` keeps its tail and is correctly not reported — the rule
    only has to separate one space from two.
    """
    assert len(find_truncated_scalars(_write(tmp_path, text), require_gap=True)) == expected, label


def test_require_gap_still_catches_a_real_truncation_in_a_conf_shaped_file(tmp_path):
    """The check must discriminate, or silencing 13 would be all it did."""
    text = (
        "targets:\n"
        "  - name: probe\n"
        "    reason: no clean CHEBI term #398 needs minting\n"
        "    policy: canonical   # deliberate comment\n"
    )
    issues = find_truncated_scalars(_write(tmp_path, text), require_gap=True)
    assert len(issues) == 1, issues
    assert issues[0].truncated_to == "no clean CHEBI term"
    assert "needs minting" in issues[0].lost
