"""Render CommunityMech community YAMLs to per-record HTML pages.

Walks `kb/communities/*.yaml`, applies the Jinja2 template at
`src/communitymech/templates/community.html.j2`, writes output to
`pages/community/<slug>.html`. Embeds a Mermaid membership graph via
the shared `kg_microbe_browser.graph` module in claw.

Phase 5 of the dismech-pattern port; see
../../culturebotai-claw/docs/proposals/phase5_mkdocs_material_and_browser_parity.md
"""

from __future__ import annotations

import argparse
import datetime as _dt
import re
import sys
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape
from markupsafe import Markup

# Make the shared kg_microbe_browser package importable. PYTHONPATH is
# set by the justfile recipe; this fallback covers `python -m` runs.
CLAW_SRC = Path(__file__).resolve().parents[3].parent / "culturebotai-claw" / "src"
if CLAW_SRC.is_dir():
    sys.path.insert(0, str(CLAW_SRC))

try:
    from kg_microbe_browser import build_community_membership_graph
except ImportError:

    def build_community_membership_graph(community: dict) -> str:  # type: ignore
        return ""


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_KB = REPO_ROOT / "kb" / "communities"
DEFAULT_OUT_DIR = REPO_ROOT / "pages" / "community"
DEFAULT_INDEX_DIR = REPO_ROOT / "pages"
TEMPLATES_DIR = Path(__file__).resolve().parent / "templates"


_CURIE_RESOLVERS = {
    "ENVO": "https://www.ebi.ac.uk/ols4/ontologies/envo/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_{}",
    "UBERON": "https://www.ebi.ac.uk/ols4/ontologies/uberon/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_{}",
    "NCBITaxon": "https://www.ebi.ac.uk/ols4/ontologies/ncbitaxon/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FNCBITaxon_{}",
    "CHEBI": "https://www.ebi.ac.uk/ols4/ontologies/chebi/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FCHEBI_{}",
    "GO": "https://www.ebi.ac.uk/ols4/ontologies/go/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FGO_{}",
}


def curie_to_url(curie: str | None) -> str:
    if not curie or ":" not in curie:
        return "#"
    prefix, local = curie.split(":", 1)
    template = _CURIE_RESOLVERS.get(prefix)
    if not template:
        return "#"
    return template.format(local)


_SLUG_RE = re.compile(r"[^A-Za-z0-9._-]+")


def slug_for(community: dict, source_path: Path) -> str:
    cid = community.get("id") or ""
    if ":" in cid:
        return cid.split(":", 1)[1]
    return _SLUG_RE.sub("_", source_path.stem)


def safe_mermaid(value: str) -> Markup:
    """The graph builder returns a fenced ```mermaid block; we strip
    the fence and emit a <pre class="mermaid"> for the JS init."""
    if not value:
        return Markup("")
    s = value.strip()
    if s.startswith("```mermaid"):
        s = s[len("```mermaid") :].lstrip()
    if s.endswith("```"):
        s = s[:-3].rstrip()
    # S704: input `s` is the Mermaid diagram body written by curators in
    # community YAML, not user-supplied at runtime; rendering it as-is is
    # required so Mermaid can render the diagram. Treat as trusted.
    return Markup(f'<pre class="mermaid">\n{s}\n</pre>')  # noqa: S704


def make_env() -> Environment:
    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES_DIR)),
        autoescape=select_autoescape(["html", "j2"]),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    env.globals["curie_to_url"] = curie_to_url
    env.filters["safe_mermaid"] = safe_mermaid
    return env


def render_one(
    env: Environment, source_path: Path, out_dir: Path, force: bool = False
) -> tuple[str, dict | None, str]:
    try:
        with open(source_path) as f:
            community = yaml.safe_load(f) or {}
    except Exception as e:
        return f"error:{type(e).__name__}", None, ""
    if not isinstance(community, dict) or not community.get("id"):
        return "error:no-id", None, ""
    slug = slug_for(community, source_path)
    out_path = out_dir / f"{slug}.html"
    if not force and out_path.exists() and out_path.stat().st_mtime >= source_path.stat().st_mtime:
        return "skipped", community, slug
    template = env.get_template("community.html.j2")
    html = template.render(
        community=community,
        membership_graph=build_community_membership_graph(community),
        source_path=str(source_path.relative_to(REPO_ROOT)),
        generated_at=_dt.datetime.now(_dt.timezone.utc).isoformat(timespec="seconds"),
    )
    out_path.write_text(html)
    return "rendered", community, slug


# ---------- index ----------

INDEX_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>CommunityMech — Community index</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
<header>
<h1>CommunityMech — Community index</h1>
<p class="muted">{count} communities, generated {generated_at}.</p>
</header>
{by_category}
</body>
</html>
"""


def _section(category: str, items: list[tuple[str, str, str]]) -> str:
    rows = "".join(
        f'<li><a href="community/{slug}.html">{name}</a> '
        f'<span class="muted">— <code>{cid}</code></span></li>'
        for (cid, slug, name) in sorted(items, key=lambda x: x[2].lower())
    )
    return (
        f"<section><h2>{category} "
        f'<small class="muted">({len(items)})</small></h2>'
        f'<ul class="medium-index">{rows}</ul></section>'
    )


def write_index(out_dir: Path, all_records: list[dict]) -> None:
    by_cat: dict[str, list[tuple[str, str, str]]] = {}
    for r in all_records:
        cat = r["community"].get("community_category") or "(uncategorized)"
        by_cat.setdefault(cat, []).append(
            (r["community"].get("id") or "", r["slug"], r["community"].get("name") or r["slug"])
        )
    sections = "\n".join(_section(c, items) for c, items in sorted(by_cat.items()))
    rows_total = sum(len(v) for v in by_cat.values())
    html = INDEX_TEMPLATE.format(
        count=rows_total,
        generated_at=_dt.datetime.now(_dt.timezone.utc).isoformat(timespec="seconds"),
        by_category=sections,
    )
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "index.html").write_text(html)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--kb", type=Path, default=DEFAULT_KB)
    ap.add_argument("--out-dir", type=Path, default=DEFAULT_OUT_DIR)
    ap.add_argument("--index-dir", type=Path, default=DEFAULT_INDEX_DIR)
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()

    if not args.kb.is_dir():
        print(f"kb dir not found: {args.kb}", file=sys.stderr)
        return 2
    args.out_dir.mkdir(parents=True, exist_ok=True)

    env = make_env()
    files = sorted(args.kb.glob("*.yaml"))
    if args.limit:
        files = files[: args.limit]
    print(f"Rendering up to {len(files)} community pages → {args.out_dir}")

    rendered = skipped = errors = 0
    successful: list[dict] = []
    for path in files:
        status, community, slug = render_one(env, path, args.out_dir, force=args.force)
        if status == "rendered":
            rendered += 1
        elif status == "skipped":
            skipped += 1
        else:
            errors += 1
            if errors <= 5:
                print(f"  {path.name}: {status}", file=sys.stderr)
        if community and slug:
            successful.append({"community": community, "slug": slug})

    print(f"  rendered: {rendered}")
    print(f"  skipped:  {skipped}")
    print(f"  errors:   {errors}")

    print("Writing index...")
    write_index(args.index_dir, successful)
    print(f"  → {args.index_dir / 'index.html'}")

    style_src = TEMPLATES_DIR / "style.css"
    if style_src.exists():
        (args.index_dir / "style.css").write_bytes(style_src.read_bytes())

    return 0 if errors == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
