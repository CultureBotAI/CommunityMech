"""Index ENVO environment terms across CommunityMech and its sibling repos.

Issue #30 asks for environment-based links between CommunityMech communities,
CultureMech media, and MediaIngredientMech (MIM) ingredients, all keyed on shared
ENVO grounding. This module is the shared substrate for that: it reads the ENVO
environment terms out of each repo's records and builds a per-ENVO coverage map
used by the coverage dashboard (Use Case 2) and the ENVO-based suggester (Use
Case 1).

Where each repo records its environment (all as ENVO CURIEs):

* CommunityMech community: ``environment_term.term.id``
* CultureMech media:       ``source_environment[].term.id``
* MIM ingredient:          ``environmental_context[].environment_term`` (bare CURIE)

Sibling repos are read from **local paths** (no network). Their record trees are
large (CultureMech's is ~16k YAMLs) but only a handful carry an environment
field, so files are **byte-prefiltered** on the field name before YAML parsing —
scanning a full sibling tree stays well under a second.
"""

from __future__ import annotations

import os
from collections.abc import Iterator
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

# Field-name bytes used to prefilter candidate files before YAML parsing.
_COMMUNITY_FIELD = b"environment_term"
_CULTUREMECH_FIELD = b"source_environment"
_MIM_FIELD = b"environmental_context"

# Over-generic ENVO environments that describe a *study/lab* setting rather than a
# meaningful natural/source environment. As a community's primary environment they
# carry little signal (they cannot be re-derived to a specific habitat), and as a
# cross-repo match key they only add noise. The suggester skips them; the
# grounding-quality report flags community records grounded to them for review.
GENERIC_ENVIRONMENT_TERMS = {
    "ENVO:01001405",  # laboratory environment (applied to ~110 communities)
}


def _iter_prefiltered(root: Path, needle: bytes) -> Iterator[tuple[Path, dict]]:
    """Yield ``(path, parsed_yaml)`` for every ``*.yaml`` under ``root`` whose raw
    bytes contain ``needle``. Files under a ``tests`` directory are skipped, as
    are unreadable / non-mapping / unparseable files.
    """
    if not root.exists():
        return
    for path in root.rglob("*.yaml"):
        if "tests" in path.parts:
            continue
        try:
            raw = path.read_bytes()
        except OSError:
            continue
        if needle not in raw:
            continue
        try:
            data = yaml.safe_load(raw)
        except yaml.YAMLError:
            continue
        if isinstance(data, dict):
            yield path, data


def _envo(curie: object) -> str | None:
    """Return ``curie`` if it is an ENVO CURIE string, else None."""
    return curie if isinstance(curie, str) and curie.startswith("ENVO:") else None


@dataclass
class EnvCoverage:
    """Per-ENVO coverage across the three repos.

    Each ``*_records`` maps an ENVO id to the sorted list of record identifiers
    (community name / CultureMech id / MIM identifier) grounded to that term.
    ``labels`` holds a human label for each ENVO id (harvested from whichever
    record first supplied one), so the dashboard needs no ontology lookup.
    """

    community_records: dict[str, list[str]] = field(default_factory=dict)
    media_records: dict[str, list[str]] = field(default_factory=dict)
    ingredient_records: dict[str, list[str]] = field(default_factory=dict)
    labels: dict[str, str] = field(default_factory=dict)

    def all_terms(self) -> set[str]:
        return set(self.community_records) | set(self.media_records) | set(self.ingredient_records)

    def label(self, envo_id: str) -> str:
        return self.labels.get(envo_id, "")


def _add(index: dict[str, list[str]], envo_id: str, record_id: str) -> None:
    index.setdefault(envo_id, [])
    if record_id not in index[envo_id]:
        index[envo_id].append(record_id)


def community_environments(community_dir: Path, coverage: EnvCoverage) -> None:
    """Populate ``coverage.community_records`` from CommunityMech community YAMLs."""
    for path in sorted(community_dir.glob("*.yaml")):
        try:
            data = yaml.safe_load(path.read_bytes())
        except (OSError, yaml.YAMLError):
            continue
        if not isinstance(data, dict):
            continue
        et = data.get("environment_term")
        term = (et or {}).get("term") if isinstance(et, dict) else None
        if not isinstance(term, dict):
            continue
        envo_id = _envo(term.get("id"))
        if envo_id is None:
            continue
        _add(coverage.community_records, envo_id, data.get("name") or path.stem)
        if term.get("label"):
            coverage.labels.setdefault(envo_id, term["label"])


def culturemech_environments(root: Path, coverage: EnvCoverage) -> None:
    """Populate ``coverage.media_records`` from CultureMech media YAMLs."""
    for path, data in _iter_prefiltered(root, _CULTUREMECH_FIELD):
        record_id = data.get("id") or data.get("name") or path.stem
        for entry in data.get("source_environment") or []:
            term = entry.get("term") if isinstance(entry, dict) else None
            if not isinstance(term, dict):
                continue
            envo_id = _envo(term.get("id"))
            if envo_id is None:
                continue
            _add(coverage.media_records, envo_id, str(record_id))
            if term.get("label"):
                coverage.labels.setdefault(envo_id, term["label"])


def mim_environments(root: Path, coverage: EnvCoverage) -> None:
    """Populate ``coverage.ingredient_records`` from MIM ingredient YAMLs."""
    for path, data in _iter_prefiltered(root, _MIM_FIELD):
        record_id = data.get("identifier") or data.get("name") or path.stem
        for entry in data.get("environmental_context") or []:
            if not isinstance(entry, dict):
                continue
            envo_id = _envo(entry.get("environment_term"))
            if envo_id is None:
                continue
            _add(coverage.ingredient_records, envo_id, str(record_id))
            if entry.get("environment_label"):
                coverage.labels.setdefault(envo_id, entry["environment_label"])


@dataclass(frozen=True)
class MediaHit:
    """A CultureMech medium grounded to a given ENVO environment."""

    culturemech_id: str
    name: str
    env_id: str
    env_label: str


def culturemech_media_by_environment(root: Path) -> dict[str, list[MediaHit]]:
    """Map ENVO id -> CultureMech media grounded to it, for the suggester.

    Unlike :func:`culturemech_environments` (which only counts record ids for the
    coverage table) this keeps each medium's name and the shared-environment
    label so a suggestion can be rendered without re-reading the record.
    """
    by_env: dict[str, list[MediaHit]] = {}
    for path, data in _iter_prefiltered(root, _CULTUREMECH_FIELD):
        cid = data.get("id")
        if not (isinstance(cid, str) and cid.startswith("CultureMech:")):
            continue
        name = data.get("name") or path.stem
        for entry in data.get("source_environment") or []:
            term = entry.get("term") if isinstance(entry, dict) else None
            if not isinstance(term, dict):
                continue
            envo_id = _envo(term.get("id"))
            if envo_id is None:
                continue
            hit = MediaHit(cid, str(name), envo_id, term.get("label") or "")
            bucket = by_env.setdefault(envo_id, [])
            if hit not in bucket:
                bucket.append(hit)
    return by_env


def build_coverage(
    community_dir: Path,
    sibling_repos: dict[str, Path] | None = None,
) -> EnvCoverage:
    """Build an :class:`EnvCoverage` from CommunityMech + configured sibling repos.

    ``sibling_repos`` maps repo name to a local path (repo root or any subtree
    holding its records). Recognized keys: ``CultureMech``,
    ``MediaIngredientMech``. Missing keys are simply not scanned.
    """
    sibling_repos = sibling_repos or {}
    coverage = EnvCoverage()
    community_environments(community_dir, coverage)
    cm = sibling_repos.get("CultureMech")
    if cm is not None:
        culturemech_environments(cm, coverage)
    mim = sibling_repos.get("MediaIngredientMech")
    if mim is not None:
        mim_environments(mim, coverage)
    return coverage


def envo_subtypes(envo_id: str, adapter: Any) -> set[str]:
    """ENVO ids that are ``is_a`` (rdfs:subClassOf) descendants of ``envo_id``.

    Used to widen environment matching: a medium grounded to a *subtype* of the
    community's environment (e.g. medium "marine sediment" for a "sediment"
    community) is a specific analog. Ancestors are intentionally NOT returned —
    broadening to super-generic parents ("environmental system", …) would
    over-match. ``adapter`` is an OAK adapter for ENVO.
    """
    try:
        descendants = adapter.descendants(envo_id, predicates=["rdfs:subClassOf"])
    except Exception:
        return set()
    return {d for d in descendants if d != envo_id}


def _cached_oak_adapter(db_name: str) -> Any | None:
    """OAK adapter for a locally-cached sqlite under ~/.data/oaklib/, or None."""
    db = Path.home() / ".data" / "oaklib" / db_name
    if not db.exists():
        return None
    from oaklib import get_adapter  # type: ignore[import-untyped]

    return get_adapter(f"sqlite:{db}")


def get_envo_adapter() -> Any | None:
    """OAK adapter for the locally-cached ENVO sqlite, or None if not cached."""
    return _cached_oak_adapter("envo.db")


def get_chebi_adapter() -> Any | None:
    """OAK adapter for the locally-cached ChEBI sqlite, or None if not cached."""
    return _cached_oak_adapter("chebi.db")


@dataclass(frozen=True)
class IngredientHit:
    """A MediaIngredientMech ingredient grounded to a given ENVO environment.

    ``chebi_id`` is the CHEBI term the MIM subject ``skos:exactMatch``-es (per MIM's
    SSSOM mappings) — the only equivalence-safe join per MediaIngredientMech#119 —
    or None when the MIM ingredient has no exactMatch CHEBI (e.g. an environment
    material grounded to ENVO/MICRO, or a close/narrowMatch). ``mim_subject`` is the
    provenance CURIE (``MIM:<name>``).
    """

    name: str
    chebi_id: str | None
    env_id: str
    env_label: str
    mim_subject: str


def mim_exactmatch_chebi(mim_root: Path) -> dict[str, str]:
    """Map ``MIM:<name>`` subject -> CHEBI id for ``skos:exactMatch`` rows only.

    Reads ``mappings/ingredient_mappings.sssom.tsv`` (skipping its ``#`` preamble).
    Per MediaIngredientMech#119, only ``skos:exactMatch`` is an equivalence-safe
    link — ``close``/``narrowMatch`` are excluded (a narrowMatch to CHEBI would
    silently generalise the ingredient). Returns {} if the SSSOM file is absent.
    """
    sssom = mim_root / "mappings" / "ingredient_mappings.sssom.tsv"
    if not sssom.exists():
        return {}
    import csv
    import io

    body = "".join(
        ln for ln in sssom.read_text().splitlines(keepends=True) if not ln.startswith("#")
    )
    out: dict[str, str] = {}
    for row in csv.DictReader(io.StringIO(body), delimiter="\t"):
        if row.get("predicate_id") == "skos:exactMatch" and str(
            row.get("object_id", "")
        ).startswith("CHEBI:"):
            out.setdefault(row["subject_id"], row["object_id"])
    return out


def mim_ingredients_by_environment(mim_root: Path) -> dict[str, list[IngredientHit]]:
    """Map ENVO id -> MIM ingredients grounded to it, with the exactMatch CHEBI.

    Joins each ``environmental_context`` record (``MIM:<file-stem>`` subject) to the
    SSSOM ``skos:exactMatch`` CHEBI map, so ``chebi_id`` follows MIM's authoritative
    mapping rather than the record's ``identifier`` field (which can differ from,
    or be a broken stand-in for, the real ontology mapping — see #119).
    """
    exact = mim_exactmatch_chebi(mim_root)
    by_env: dict[str, list[IngredientHit]] = {}
    # scan the per-ingredient record tree, not the whole repo: MIM keeps multi-MB
    # aggregate/backup dumps under data/curated/ that also mention the field and
    # would blow up YAML parsing.
    records_root = mim_root / "data" / "ingredients"
    if not records_root.exists():
        records_root = mim_root
    for path, data in _iter_prefiltered(records_root, _MIM_FIELD):
        subject = f"MIM:{path.stem}"
        chebi_id = exact.get(subject)
        name = data.get("preferred_term") or data.get("name") or path.stem
        for entry in data.get("environmental_context") or []:
            if not isinstance(entry, dict):
                continue
            envo_id = _envo(entry.get("environment_term"))
            if envo_id is None:
                continue
            hit = IngredientHit(
                str(name), chebi_id, envo_id, entry.get("environment_label") or "", subject
            )
            bucket = by_env.setdefault(envo_id, [])
            if hit not in bucket:
                bucket.append(hit)
    return by_env


def sibling_repos_from_env() -> dict[str, Path]:
    """Parse ``COMMUNITYMECH_SIBLING_REPOS`` (``Name=path,Name=path``) into paths.

    Mirrors ``scripts/validate_cross_repo_ids.py`` so both cross-repo tools share
    one configuration convention.
    """
    raw = os.environ.get("COMMUNITYMECH_SIBLING_REPOS", "").strip()
    out: dict[str, Path] = {}
    for pair in raw.split(","):
        if "=" not in pair:
            continue
        name, path = pair.split("=", 1)
        out[name.strip()] = Path(path.strip())
    return out
