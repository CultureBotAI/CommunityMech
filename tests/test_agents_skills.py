"""Verify .agents/skills exposes .claude/skills and AGENTS.md exists."""

from __future__ import annotations

import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLAUDE_SKILLS = ROOT / ".claude" / "skills"
AGENTS_SKILLS = ROOT / ".agents" / "skills"
AGENTS_MD = ROOT / "AGENTS.md"
MARKDOWN_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def test_agents_md_points_to_claude_md_and_skills() -> None:
    assert AGENTS_MD.is_file()
    text = AGENTS_MD.read_text(encoding="utf-8")
    assert "CLAUDE.md" in text
    assert ".agents/skills" in text
    for target in MARKDOWN_LINK_RE.findall(text):
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        path_part = target.split("#", 1)[0]
        if path_part:
            assert (ROOT / path_part).exists(), f"Broken link in AGENTS.md: {target}"


def test_agents_skills_symlink_exposes_claude_skills() -> None:
    assert AGENTS_SKILLS.is_symlink()
    assert os.readlink(AGENTS_SKILLS) == "../.claude/skills"
    assert AGENTS_SKILLS.resolve() == CLAUDE_SKILLS.resolve()

    claude_skill_names = {
        d.name for d in CLAUDE_SKILLS.iterdir() if d.is_dir() and (d / "SKILL.md").is_file()
    }
    agents_skill_names = {
        d.name for d in AGENTS_SKILLS.iterdir() if d.is_dir() and (d / "SKILL.md").is_file()
    }
    assert "review-open-issues" in claude_skill_names
    assert agents_skill_names == claude_skill_names

    review_skill = AGENTS_SKILLS / "review-open-issues" / "SKILL.md"
    claude_review_skill = CLAUDE_SKILLS / "review-open-issues" / "SKILL.md"
    assert review_skill.resolve() == claude_review_skill.resolve()
    review_text = review_skill.read_text(encoding="utf-8")
    assert "CommunityMech" in review_text
    assert "read-only" in review_text.lower()
