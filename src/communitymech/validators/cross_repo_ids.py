"""Cross-repository ID validation for related_media and related_ingredients.

When a community YAML references a `culturemech_id` or `mediaingredientmech_id`
under `related_media` / `related_ingredients`, two things should hold:

1. The ID matches its CURIE pattern (`CultureMech:NNNNNN` /
   `MediaIngredientMech:NNNNNN`). LinkML's schema-level pattern check
   covers this, but mirroring it here surfaces issues without booting
   the full validator and lets callers act on individual offenders.

2. The ID actually exists in the sibling repository. This requires a
   path to the sibling repo and is therefore opt-in — if no sibling-repo
   path is supplied, existence checks are skipped (and the validator
   says so explicitly rather than silently passing).

Usage:

    from pathlib import Path
    from communitymech.validators.cross_repo_ids import validate_cross_repo_ids

    issues = validate_cross_repo_ids(
        Path("kb/communities/SPRUCE_Peatland_Methane_Cycling_Community.yaml"),
        sibling_repos={
            "CultureMech": Path("../CultureMech/kb/media"),
            "MediaIngredientMech": Path("../MediaIngredientMech/kb/ingredients"),
        },
    )
    for i in issues:
        print(i.severity, i.message)
"""

from __future__ import annotations

import re
from collections.abc import Iterable
from dataclasses import dataclass, field
from pathlib import Path

import yaml

CULTUREMECH_ID_RE = re.compile(r"^CultureMech:\d{6}$")
MEDIAINGREDIENTMECH_ID_RE = re.compile(r"^MediaIngredientMech:\d{6}$")


@dataclass
class CrossRepoIssue:
    """A single cross-repo ID validation finding."""

    severity: str  # "error" | "warning" | "info"
    field_path: str
    message: str

    def __str__(self) -> str:
        return f"[{self.severity}] {self.field_path}: {self.message}"


@dataclass
class SiblingRepoIndex:
    """Lazy index of IDs present in a sibling repo's kb/ directory.

    Treats every `*.yaml` file in `path` as a record and uses its top-level
    `id:` field as the canonical ID. Returns an empty index if `path` is
    None or does not exist, which lets callers configure repos optionally.
    """

    path: Path | None
    _ids: set[str] = field(default_factory=set)
    _loaded: bool = False

    def __contains__(self, candidate: str) -> bool:
        self._ensure_loaded()
        return candidate in self._ids

    @property
    def available(self) -> bool:
        return self.path is not None and self.path.exists()

    def _ensure_loaded(self) -> None:
        if self._loaded:
            return
        self._loaded = True
        if not self.available:
            return
        assert self.path is not None
        for yaml_file in self.path.glob("*.yaml"):
            try:
                data = yaml.safe_load(yaml_file.read_text())
            except yaml.YAMLError:
                continue
            if isinstance(data, dict) and isinstance(data.get("id"), str):
                self._ids.add(data["id"])


def _iter_entries(data: dict, slot: str) -> Iterable[tuple[int, dict]]:
    for idx, entry in enumerate(data.get(slot, []) or []):
        if isinstance(entry, dict):
            yield idx, entry


def validate_cross_repo_ids(
    yaml_path: Path,
    sibling_repos: dict[str, Path] | None = None,
) -> list[CrossRepoIssue]:
    """Validate cross-repo IDs in a single community YAML.

    Args:
        yaml_path: Path to the community YAML.
        sibling_repos: Optional dict mapping repo name to the directory
            holding the sibling repo's record YAMLs. Recognized keys:
            ``CultureMech``, ``MediaIngredientMech``. If a key is missing
            or its path doesn't exist, the existence check for that repo
            is skipped (with an info-level note in the issue list).

    Returns:
        List of CrossRepoIssue. Empty if everything checks out (or if
        there are no cross-repo IDs to check and sibling repos are
        configured).
    """
    sibling_repos = sibling_repos or {}
    culturemech = SiblingRepoIndex(path=sibling_repos.get("CultureMech"))
    mim = SiblingRepoIndex(path=sibling_repos.get("MediaIngredientMech"))

    data = yaml.safe_load(yaml_path.read_text()) or {}
    issues: list[CrossRepoIssue] = []

    for idx, entry in _iter_entries(data, "related_media"):
        cid = entry.get("culturemech_id")
        if cid is None:
            continue
        field_path = f"related_media[{idx}].culturemech_id"
        if not CULTUREMECH_ID_RE.match(cid):
            issues.append(
                CrossRepoIssue(
                    severity="error",
                    field_path=field_path,
                    message=f"'{cid}' does not match pattern CultureMech:NNNNNN",
                )
            )
            continue
        if culturemech.available:
            if cid not in culturemech:
                issues.append(
                    CrossRepoIssue(
                        severity="error",
                        field_path=field_path,
                        message=f"'{cid}' not found in CultureMech repo at {culturemech.path}",
                    )
                )
        else:
            issues.append(
                CrossRepoIssue(
                    severity="info",
                    field_path=field_path,
                    message=(
                        f"existence check for '{cid}' skipped: no CultureMech "
                        "sibling-repo path configured"
                    ),
                )
            )

    for idx, entry in _iter_entries(data, "related_ingredients"):
        mid = entry.get("mediaingredientmech_id")
        if mid is None:
            continue
        field_path = f"related_ingredients[{idx}].mediaingredientmech_id"
        if not MEDIAINGREDIENTMECH_ID_RE.match(mid):
            issues.append(
                CrossRepoIssue(
                    severity="error",
                    field_path=field_path,
                    message=f"'{mid}' does not match pattern MediaIngredientMech:NNNNNN",
                )
            )
            continue
        if mim.available:
            if mid not in mim:
                issues.append(
                    CrossRepoIssue(
                        severity="error",
                        field_path=field_path,
                        message=f"'{mid}' not found in MediaIngredientMech repo at {mim.path}",
                    )
                )
        else:
            issues.append(
                CrossRepoIssue(
                    severity="info",
                    field_path=field_path,
                    message=(
                        f"existence check for '{mid}' skipped: no "
                        "MediaIngredientMech sibling-repo path configured"
                    ),
                )
            )

    return issues
