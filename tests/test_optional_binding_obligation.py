"""Regression test for REQUIRED id↔label bindings on OPTIONAL slots.

Two optional slots in the schema carry an id↔label binding with
``obligation_level: REQUIRED``:

* ``RelatedMedia.shared_environment_term``
* ``RelatedIngredient.chebi_term``

Both slots are ``required: false``. The REQUIRED obligation is meant to enforce
the id↔label *correspondence* when the term IS present — it must NOT turn the
optional slot into a de-facto required slot. This test pins that contract:

1. An instance that OMITS both bound optional slots validates clean.
2. (positive control) An instance with a PRESENT-but-WRONG label still fails,
   proving the binding gate is actually engaged rather than silently inert.

The test shells out to ``linkml-term-validator validate-data --labels`` (the
same gate ``just validate`` uses) and is skipped when that CLI is unavailable.
"""
from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
SCHEMA = REPO_ROOT / "src" / "communitymech" / "schema" / "communitymech.yaml"
FIXTURE = REPO_ROOT / "tests" / "data" / "optional_binding" / "omits_bound_optionals.yaml"

pytestmark = pytest.mark.skipif(
    shutil.which("linkml-term-validator") is None,
    reason="linkml-term-validator CLI not installed",
)


def _validate(data_path: Path) -> subprocess.CompletedProcess:
    return subprocess.run(
        [
            "linkml-term-validator",
            "validate-data",
            str(data_path),
            "-s",
            str(SCHEMA),
            "--labels",
        ],
        capture_output=True,
        text=True,
    )


def test_absent_optional_bound_slot_does_not_trip_required_obligation():
    """Omitting the optional bound slots must validate clean (exit 0)."""
    result = _validate(FIXTURE)
    assert result.returncode == 0, (
        "Absent optional slot tripped the REQUIRED binding obligation.\n"
        "If this fails, downgrade the obligation_level on "
        "RelatedMedia.shared_environment_term and RelatedIngredient.chebi_term "
        "to a non-required level (e.g. RECOMMENDED).\n"
        f"stdout:\n{result.stdout}\nstderr:\n{result.stderr}"
    )


def test_present_wrong_label_is_caught(tmp_path: Path):
    """Positive control: a present term with a wrong label must fail (gate is live)."""
    bad = tmp_path / "wrong_label.yaml"
    bad.write_text(
        "id: CommunityMech:999998\n"
        "name: Wrong Label Control\n"
        "related_ingredients:\n"
        "- preferred_term: Test Ingredient\n"
        "  chebi_term:\n"
        "    id: CHEBI:15377\n"
        "    label: definitely not the right label for water\n"
    )
    result = _validate(bad)
    assert result.returncode != 0, (
        "Binding gate did not catch a present-but-wrong label; the absent-slot "
        "pass would then be meaningless.\n"
        f"stdout:\n{result.stdout}\nstderr:\n{result.stderr}"
    )
