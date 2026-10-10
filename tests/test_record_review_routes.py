"""Evidence review must use the maintained assessment and persistence route."""

from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def test_curate_audit_saves_review_without_changing_scientific_inputs():
    text = (ROOT / ".claude/skills/curate-yaml-record/SKILL.md").read_text()
    metadata = yaml.safe_load(text.split("---", 2)[1])
    assert metadata["metadata"]["version"] == "2.0.0"
    assert "preserves scientific inputs and saves a new structured review" in text


def test_evidence_review_delegates_without_stale_producers():
    profile = yaml.safe_load((ROOT / "conf/record_review.yaml").read_text())
    path = ".claude/skills/evidence-curation/SKILL.md"
    assert path in profile["skills"]
    assert ".claude/skills/review-communities/SKILL.md" in profile["skills"]
    text = (ROOT / path).read_text()
    for required in (
        "../review-communities/SKILL.md",
        "docs/record-reviews.md",
        "reviews/structured/<timestamp>-<slug>/",
        "scripts/record_review.py save --content",
        "scientific_review: false",
        "per-record P1-P4",
        "participants, direction, mechanism",
        "both native scores",
        "explicit authorization",
        "just validate-references-explained",
    ):
        assert required in text
    assert "scripts/quick_literature_review.py" not in text
    assert "scripts/review_literature.py" not in text
