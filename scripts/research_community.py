#!/usr/bin/env python3
"""Run deep research for CommunityMech community records."""

from __future__ import annotations

import argparse
import os
import shlex
import subprocess
import sys
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
COMMUNITIES_DIR = REPO_ROOT / "kb" / "communities"
DEFAULT_TEMPLATE = REPO_ROOT / "templates" / "community_mechanism_research.md"
DEFAULT_RESEARCH_DIR = REPO_ROOT / "research"


def load_community(path: Path) -> dict[str, Any]:
    """Load a MicrobialCommunity YAML file."""
    if not path.exists():
        raise FileNotFoundError(f"Community file not found: {path}")
    doc = yaml.safe_load(path.read_text())
    if not isinstance(doc, dict):
        raise ValueError(f"Community file is not a YAML mapping: {path}")
    return doc


def resolve_community_file(target: str) -> Path:
    """Resolve a path, filename stem, filename, or CommunityMech id to a community YAML path."""
    candidate = Path(target)
    if candidate.exists():
        return candidate.resolve()

    if candidate.suffix in {".yaml", ".yml"}:
        repo_candidate = (REPO_ROOT / candidate).resolve()
        if repo_candidate.exists():
            return repo_candidate
        community_candidate = COMMUNITIES_DIR / candidate.name
        if community_candidate.exists():
            return community_candidate

    stem_candidate = COMMUNITIES_DIR / f"{target}.yaml"
    if stem_candidate.exists():
        return stem_candidate

    for path in sorted(COMMUNITIES_DIR.glob("*.yaml")):
        try:
            doc = load_community(path)
        except ValueError:
            continue
        if doc.get("id") == target:
            return path

    available = ", ".join(path.stem for path in sorted(COMMUNITIES_DIR.glob("*.yaml"))[:20])
    message = (
        f"Community target not found: {target}. "
        f"Available communities include: {available or 'none'}"
    )
    raise FileNotFoundError(message)


def _term_label(value: Any) -> str:
    if not isinstance(value, dict):
        return str(value or "")
    preferred = value.get("preferred_term")
    term = value.get("term")
    if isinstance(term, dict):
        label = term.get("label") or term.get("id")
        if preferred and label and preferred != label:
            return f"{preferred} ({label})"
        return str(preferred or label or "")
    return str(preferred or "")


def _join_values(values: Any) -> str:
    if values is None:
        return ""
    if isinstance(values, list):
        return ", ".join(str(value) for value in values)
    return str(values)


def summarize_environment(doc: dict[str, Any]) -> str:
    environment = doc.get("environment_term")
    if not isinstance(environment, dict):
        return ""
    term = environment.get("term")
    term_id = ""
    label = environment.get("preferred_term", "")
    if isinstance(term, dict):
        term_id = str(term.get("id", ""))
        label = str(term.get("label") or label)
    notes = environment.get("notes", "")
    parts = [part for part in [label, term_id, notes] if part]
    return " | ".join(parts)


def summarize_taxonomy(doc: dict[str, Any]) -> str:
    rows = []
    for item in doc.get("taxonomy", []) or []:
        if not isinstance(item, dict):
            continue
        taxon = _term_label(item.get("taxon_term"))
        roles = _join_values(item.get("functional_role"))
        abundance = item.get("abundance_value", "")
        rows.append(" - ".join(part for part in [taxon, roles, str(abundance)] if part))
    return " | ".join(rows)


def summarize_interactions(doc: dict[str, Any]) -> str:
    rows = []
    for item in doc.get("ecological_interactions", []) or []:
        if not isinstance(item, dict):
            continue
        name = str(item.get("name", ""))
        interaction_type = str(item.get("interaction_type", ""))
        description = str(item.get("description", ""))
        metabolites = ", ".join(_term_label(value) for value in item.get("metabolites", []) or [])
        rows.append(
            " - ".join(part for part in [name, interaction_type, metabolites, description] if part)
        )
    return " | ".join(rows)


def summarize_named_sections(doc: dict[str, Any], section: str) -> str:
    rows = []
    for item in doc.get(section, []) or []:
        if not isinstance(item, dict):
            continue
        name = str(item.get("name", ""))
        value = str(item.get("value", ""))
        description = str(item.get("description", item.get("preparation_notes", "")))
        rows.append(" - ".join(part for part in [name, value, description] if part))
    return " | ".join(rows)


def summarize_datasets(doc: dict[str, Any]) -> str:
    rows = []
    for section in ("associated_datasets", "external_resources"):
        for item in doc.get(section, []) or []:
            if not isinstance(item, dict):
                continue
            name = str(item.get("name", ""))
            accession = str(item.get("accession", item.get("resource_id", "")))
            url = str(item.get("url", ""))
            rows.append(" - ".join(part for part in [name, accession, url] if part))
    return " | ".join(rows)


def summarize_evidence(doc: dict[str, Any]) -> str:
    rows: list[str] = []

    def collect(value: Any) -> None:
        if isinstance(value, dict):
            evidence = value.get("evidence")
            if isinstance(evidence, list):
                for item in evidence:
                    if isinstance(item, dict):
                        reference = item.get("reference", "")
                        snippet = item.get("snippet", "")
                        explanation = item.get("explanation", "")
                        rows.append(f"{reference}: {snippet} ({explanation})".strip())
            for nested in value.values():
                collect(nested)
        elif isinstance(value, list):
            for nested in value:
                collect(nested)

    collect(doc)
    return " | ".join(rows[:40])


def summarize_source_context(doc: dict[str, Any]) -> str:
    """Return discovery provenance carried by a review-only scout stub."""
    scout = doc.get("_scout")
    if not isinstance(scout, dict):
        return ""
    return " | ".join(
        str(scout.get(key, "")) for key in ("source_reference", "year", "journal") if scout.get(key)
    )


def template_vars(doc: dict[str, Any], community_file: Path) -> dict[str, str]:
    return {
        "community_name": str(doc.get("name", community_file.stem)),
        "community_id": str(doc.get("id", "")),
        "community_file": community_file.name,
        "community_slug": community_file.stem,
        "community_category": str(doc.get("community_category", "")),
        "ecological_state": str(doc.get("ecological_state", "")),
        "community_origin": str(doc.get("community_origin", "")),
        "description": str(doc.get("description", "")),
        "source_summary": summarize_source_context(doc),
        "environment_summary": summarize_environment(doc),
        "taxonomy_summary": summarize_taxonomy(doc),
        "interaction_summary": summarize_interactions(doc),
        "environmental_factor_summary": summarize_named_sections(doc, "environmental_factors"),
        "growth_media_summary": summarize_named_sections(doc, "growth_media"),
        "dataset_summary": summarize_datasets(doc),
        "evidence_summary": summarize_evidence(doc),
    }


def provider_args(provider: str) -> list[str]:
    """Mirror DisMech's cborg shortcut while allowing named providers such as falcon."""
    if provider == "cborg":
        return ["--use-cborg"]
    return ["--provider", provider]


def research_env(provider: str) -> dict[str, str]:
    """Build subprocess environment, including a FutureHouse Falcon key alias."""
    env = os.environ.copy()
    if provider == "falcon" and not env.get("EDISON_API_KEY") and env.get("FUTUREHOUSE_API_KEY"):
        env["EDISON_API_KEY"] = env["FUTUREHOUSE_API_KEY"]
    return env


def build_command(
    *,
    provider: str,
    template: Path,
    output_file: Path,
    variables: dict[str, str],
    passthrough_args: list[str],
    client_command: str = "deep-research-client",
) -> list[str]:
    command = [
        client_command,
        "research",
        "--template",
        str(template),
    ]
    for key, value in variables.items():
        command.extend(["--var", f"{key}={value}"])
    command.extend(provider_args(provider))
    command.extend(
        [
            # NO --separate-citations. The client builds that sidecar with a
            # regex over the report prose, and it is malformed: TraitMech's
            # #249 found 353 sidecars with 194 broken markdown-link tails,
            # 2,770 stray trailing commas, and 332 of 353 duplicating a
            # reference two or three times; CultureMech's own single sample
            # re-emitted the ~55-line rendered prompt as "Query" and listed
            # one DOI three times over. The report's own References section
            # is the trustworthy artifact — see CultureMech's
            # docs/RESEARCH_ARTIFACT_CONTRACT.md.
            "--output",
            str(output_file),
        ]
    )
    command.extend(passthrough_args)
    return command


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--provider", required=True, help="deep-research-client provider, e.g. falcon"
    )
    parser.add_argument(
        "--target", required=True, help="Community path, filename stem, or CommunityMech id"
    )
    parser.add_argument("--template", type=Path, default=DEFAULT_TEMPLATE)
    parser.add_argument("--research-dir", type=Path, default=DEFAULT_RESEARCH_DIR)
    parser.add_argument("--client-command", default="deep-research-client")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the deep-research-client command without running it.",
    )
    parser.add_argument("passthrough_args", nargs=argparse.REMAINDER)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    community_file = resolve_community_file(args.target)
    doc = load_community(community_file)

    output_dir = args.research_dir / "communities"
    output_file = output_dir / f"{community_file.stem}-deep-research-{args.provider}.md"
    variables = template_vars(doc, community_file)
    command = build_command(
        provider=args.provider,
        template=args.template,
        output_file=output_file,
        variables=variables,
        passthrough_args=args.passthrough_args,
        client_command=args.client_command,
    )

    print(  # noqa: T201
        f"Researching: {variables['community_name']} ({args.provider}) -> {output_file}"
    )
    if args.dry_run:
        print(shlex.join(command))  # noqa: T201
        return 0

    output_dir.mkdir(parents=True, exist_ok=True)
    subprocess.run(command, check=True, env=research_env(args.provider))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
