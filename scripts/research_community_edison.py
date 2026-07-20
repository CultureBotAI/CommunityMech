#!/usr/bin/env python3
"""Run Edison Scientific deep research against CommunityMech community records.

Uses the `edison-client` SDK directly. The companion `research_community.py`
wraps `deep-research-client`, but as of DRC 0.2.4 only `cyberian` and
`openai` are registered providers — Edison/PaperQA is not exposed there,
so we drive the SDK directly. This is the CommunityMech port of
CultureMech's `research_media_edison.py`; the response-capture plumbing
(`_edison_capture.py`) is vendored verbatim and shared by both.

The default job is LITERATURE (== `job-futurehouse-paperqa3`), the
PaperQA agent — the best fit for "what is this community's composition,
what are its ecological interactions and mechanisms, what environment
and conditions support it"-type questions. Use ``--job literature-high``
for the deeper variant (more reads, higher cost), ``--job precedent``
for first-mention search, ``--job phoenix`` for synthesis.

Auth: reads ``EDISON_PLATFORM_API_KEY`` (SDK-native) or ``EDISON_API_KEY``
(the key already in this repo's ``.env``) from environment. A repo-root
``.env`` is auto-loaded via python-dotenv.

Outputs land under ``research/communities/{slug}-edison-{job}.md``
(``slug`` = community YAML stem, ``job`` = lowercase-hyphenated job
name, e.g. ``literature-high``). A sibling ``{slug}-edison-{job}-meta.yaml``
captures the rendered query text, task_id, total_cost, status,
template_path, and template_vars — sufficient for audit and re-runs.

Usage::

    # single record (filename stem, id, or path)
    python scripts/research_community_edison.py --target Yogurt_TwoSpecies_Starter_Culture

    # by CommunityMech id
    python scripts/research_community_edison.py --target CommunityMech:000164

    # batch from a JSON list of stems / ids / paths
    python scripts/research_community_edison.py --batch queue.json --limit 5

    # dry-run skips the API call but still writes the meta yaml (including
    # the full rendered query) so you can inspect the prompt that would
    # have been sent without spending credits.
    python scripts/research_community_edison.py --target <target> --dry-run
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml
from dotenv import load_dotenv

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))
import _edison_capture as ec  # noqa: E402  -- response/citation/agent capture
import research_community as rc  # noqa: E402  -- reuse template_vars + loaders

DEFAULT_TEMPLATE = REPO_ROOT / "templates" / "community_mechanism_research.md"
DEFAULT_OUT_DIR = REPO_ROOT / "research" / "communities"


_JOB_ALIASES: dict[str, str] = {
    "literature": "LITERATURE",
    "paperqa": "LITERATURE",
    "literature-high": "LITERATURE_HIGH",
    "literature_high": "LITERATURE_HIGH",
    "paperqa-high": "LITERATURE_HIGH",
    "precedent": "PRECEDENT",
    "phoenix": "PHOENIX",
}


def resolve_job(name: str):
    """Map a user-friendly --job alias to the edison_client JobNames enum."""
    from edison_client import JobNames

    key = _JOB_ALIASES.get(name.lower())
    if key is None:
        raise SystemExit(
            f"Unknown --job '{name}'. Choose one of: " + ", ".join(sorted(_JOB_ALIASES))
        )
    return getattr(JobNames, key)


def load_api_key() -> str:
    """Pick up the Edison key from env (with the legacy alias).

    The SDK natively reads ``EDISON_PLATFORM_API_KEY``; this repo's
    ``.env`` sets ``EDISON_API_KEY``. Honor both.
    """
    load_dotenv(REPO_ROOT / ".env")
    key = os.environ.get("EDISON_PLATFORM_API_KEY") or os.environ.get("EDISON_API_KEY")
    if not key:
        raise SystemExit(
            "EDISON_PLATFORM_API_KEY (or EDISON_API_KEY) is not set. "
            "Add it to .env at the repo root, or `export EDISON_PLATFORM_API_KEY=...` "
            "in your shell."
        )
    return key


def render_query(
    community_path: Path, template_path: Path, doc: dict[str, Any] | None = None
) -> tuple[str, dict[str, str]]:
    """Render the deep-research template for a single community.

    Returns ``(query_text, template_vars)`` so callers can stamp the
    variables into the meta file alongside the rendered query. ``doc``
    may be passed in to reuse an already-parsed YAML and avoid a second
    read.
    """
    if doc is None:
        doc = rc.load_community(community_path)
    variables = rc.template_vars(doc, community_path)
    template = template_path.read_text()
    return template.format_map(_DefaultEmpty(variables)), variables


class _DefaultEmpty(dict):
    """``str.format_map`` helper: leave unknown placeholders blank instead of KeyError."""

    def __missing__(self, key):  # noqa: ANN001
        return ""


def slug_for(community_path: Path) -> str:
    """Stable filename slug for output naming (the YAML file stem)."""
    return community_path.stem


def _short_job(job) -> str:
    """CLI-friendly filename suffix: ``JobNames.LITERATURE_HIGH`` -> ``literature-high``."""
    return job.name.lower().replace("_", "-")


def _display_path(path: Path) -> str:
    """Show ``path`` relative to the repo when possible; else absolute."""
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def run_one(
    client,
    community_path: Path,
    job,
    template_path: Path,
    out_dir: Path,
    dry_run: bool,
    label: str = "",
) -> dict[str, Any]:
    """Submit one task; write results to out_dir; return a stats dict.

    On a successful API call, ``_edison_capture.capture_full_response``
    writes a primary answer .md plus four sibling files
    (-response.json, -citations.md, -agent-state.json, -files.json)
    for full provenance. See scripts/_edison_capture.py for details.
    """
    from edison_client import TaskRequest

    doc = rc.load_community(community_path)
    query, variables = render_query(community_path, template_path, doc)
    slug = slug_for(community_path)
    job_short = _short_job(job)
    # An optional --label keeps parallel runs of the same (community, job) from
    # clobbering each other, e.g. `-causal` for the causal-graph template vs the
    # default mechanism template.
    label_suffix = f"-{label}" if label else ""
    stem = f"{slug}-edison-{job_short}{label_suffix}"
    meta_path = out_dir / f"{stem}-meta.yaml"

    def _safe_rel(p: Path) -> str:
        try:
            return str(p.resolve().relative_to(REPO_ROOT))
        except ValueError:
            return str(p)

    base_meta: dict[str, Any] = {
        "slug": slug,
        "community_path": _safe_rel(community_path),
        "community_id": str(doc.get("id") or ""),
        "job": job.name,
        "job_id": job.value,
        "label": label,
        "template_path": _safe_rel(template_path),
        "template_vars": variables,
        "query_chars": len(query),
        "query": query,
        "submitted_at": datetime.now(timezone.utc).isoformat(),
    }

    if dry_run:
        # Render the meta yaml even in dry-run so callers can audit
        # exactly what would be sent (and compare query_sha256 to detect
        # identical re-runs). No .md is written; only meta.
        meta = ec.capture_dry_run(out_dir=out_dir, stem=stem, query=query, base_meta=base_meta)
        out_dir.mkdir(parents=True, exist_ok=True)
        meta_path.write_text(yaml.safe_dump(meta, sort_keys=False, allow_unicode=True, width=100))
        md_path = out_dir / f"{stem}.md"
        print(f"[DRY RUN] {_display_path(community_path)} -> {_display_path(md_path)}")
        print(f"          job={job.name} query_chars={len(query)} meta={_display_path(meta_path)}")
        return {"slug": slug, "status": "dry-run", "cost": 0.0}

    out_dir.mkdir(parents=True, exist_ok=True)
    task = TaskRequest(name=job, query=query)
    print(f"  + submitting {slug} ({job.name})...", flush=True)
    [response] = client.run_tasks_until_done(task, progress_bar=False)

    meta = ec.capture_full_response(
        response=response,
        client=client,
        out_dir=out_dir,
        stem=stem,
        query=query,
        base_meta=base_meta,
    )
    meta_path.write_text(yaml.safe_dump(meta, sort_keys=False, allow_unicode=True, width=100))
    md_path = out_dir / f"{stem}.md"
    total_cost = meta.get("total_cost")
    print(
        f"    -> {_display_path(md_path)}  cost={total_cost}  "
        f"citations={meta.get('citations_parsed')}  "
        f"agent_state={meta.get('sidecar_files', {}).get('agent_state_json', False)}"
    )
    return {"slug": slug, "status": meta["status"], "cost": total_cost or 0.0}


def load_batch_targets(batch_path: Path) -> list[str]:
    """Return a list of target strings from a JSON batch file.

    Accepts either a JSON list of strings (stems/ids/paths) or a list of
    objects carrying one of ``target`` / ``slug`` / ``id`` / ``file_path``.
    Entries that yield no usable target are skipped.
    """
    data = json.loads(batch_path.read_text())
    if not isinstance(data, list):
        raise SystemExit(f"--batch expects a JSON list: {batch_path}")
    out: list[str] = []
    for entry in data:
        if isinstance(entry, str):
            out.append(entry)
        elif isinstance(entry, dict):
            for key in ("target", "slug", "id", "file_path"):
                if entry.get(key):
                    out.append(str(entry[key]))
                    break
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument("--target", help="Community path, filename stem, or CommunityMech id.")
    src.add_argument("--batch", type=Path, help="Path to a JSON list of stems/ids/paths.")
    ap.add_argument(
        "--job",
        default="literature",
        help="literature (paperqa3, default) | literature-high | precedent | phoenix",
    )
    ap.add_argument("--template", type=Path, default=DEFAULT_TEMPLATE)
    ap.add_argument(
        "--label",
        default="",
        help="Optional suffix on output filenames (e.g. 'causal') so a non-default "
        "template's run doesn't overwrite the default one for the same community+job.",
    )
    ap.add_argument("--out-dir", type=Path, default=DEFAULT_OUT_DIR)
    ap.add_argument(
        "--limit", type=int, default=None, help="When using --batch, cap the number researched."
    )
    ap.add_argument(
        "--start", type=int, default=0, help="When using --batch, skip this many entries first."
    )
    ap.add_argument(
        "--dry-run", action="store_true", help="Render queries + print plan; do NOT call the API."
    )
    args = ap.parse_args(argv)

    job = resolve_job(args.job)

    targets: list[Path]
    if args.target:
        targets = [rc.resolve_community_file(args.target)]
    else:
        names = load_batch_targets(args.batch)[args.start :]
        if args.limit is not None:
            names = names[: args.limit]
        targets = []
        unresolved: list[str] = []
        for name in names:
            try:
                targets.append(rc.resolve_community_file(name))
            except FileNotFoundError:
                unresolved.append(name)
        if unresolved:
            print(f"Note: skipped {len(unresolved)} unresolvable batch entries:", file=sys.stderr)
            for u in unresolved[:5]:
                print(f"  - {u}", file=sys.stderr)
            if len(unresolved) > 5:
                print(f"  - ... {len(unresolved) - 5} more", file=sys.stderr)

    if not targets:
        print("No targets to research.", file=sys.stderr)
        return 2

    print(f"Edison job:    {job.name} ({job.value})")
    print(f"Template:      {_display_path(args.template.resolve())}")
    print(f"Output dir:    {_display_path(args.out_dir.resolve())}")
    print(f"Communities:   {len(targets)}")
    if args.dry_run:
        print("Mode:          DRY RUN (no API calls, no credits spent)")
    print()

    client = None
    if not args.dry_run:
        api_key = load_api_key()
        from edison_client import EdisonClient

        client = EdisonClient(api_key=api_key)

    results: list[dict[str, Any]] = []
    try:
        for community_path in targets:
            results.append(
                run_one(
                    client,
                    community_path,
                    job,
                    args.template,
                    args.out_dir,
                    args.dry_run,
                    args.label,
                )
            )
    finally:
        if client is not None:
            client.close()

    if not args.dry_run:
        total_cost = sum(r["cost"] or 0.0 for r in results)
        print()
        print(f"Done. {len(results)} communities researched. Total reported cost: {total_cost:.4f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
