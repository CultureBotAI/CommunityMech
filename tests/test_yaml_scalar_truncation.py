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
        (
            "after a block scalar ends",
            "notes: >\n  fine #376 here\nkey: bad #384 here\n",
            "#384 here",
        ),
        ("nested mapping", "a:\n  b:\n    c: text #1 x\n", "#1 x"),
        # A tab before the hash is not this defect: YAML rejects the document
        # outright, which validate-strict already reports as a parse error.
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
    flat = str(parsed)
    assert lost not in flat, f"{name}: YAML kept the tail, so there is nothing to report"


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
        ("blank line inside a block", "notes: >\n  first #376\n\n  second #384\nother: fine\n"),
        # A block body line that *looks* like a mapping or a sequence item. This
        # is what makes skipping the block header load-bearing: without it the
        # body would be parsed as YAML structure and flagged.
        ("mapping-shaped block body", "notes: >\n  key: value #376 here\nother: fine\n"),
        ("sequence-shaped block body", "notes: |\n  - item #376 here\nother: fine\n"),
        ("comment line with a hash", "# see key: value #376\nkey: fine\n"),
        ("no hash at all", "key: ordinary text\n"),
    ],
)
def test_legitimate_hashes_are_not_reported(tmp_path, name, text):
    """False positives would make this rule unusable, so they are pinned too."""
    assert find_truncated_scalars(_write(tmp_path, text)) == [], name


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
