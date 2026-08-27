"""KGX TSV emitter for CommunityMech communities.

Walks `kb/communities/*.yaml` and emits two TSVs:

- nodes.tsv: id, category, name, description, provided_by, ...
- edges.tsv: id, subject, predicate, object, category, publications,
             supporting_text, primary_knowledge_source, ...

Edge IDs are deterministic UUID5 (namespace-stable across runs) so
downstream consumers can rely on idempotent identifiers.

Evidence propagation: each `evidence[]` block (already populated in
~1,288 places across the 78 community YAMLs with PMIDs/DOIs/snippets)
contributes to its enclosing edge's `publications` and
`supporting_text` columns. This is the dismech `_format_evidence`
pattern from `src/dismech/export/kgx_export.py`.

Usage:
    python -m communitymech.export --output output/kgx
    python -m communitymech.export --output output/kgx --kb kb/communities
"""

from __future__ import annotations

import argparse
import csv
import dataclasses
import datetime as _dt
import sys
import uuid
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[3]
DEFAULT_KB = REPO_ROOT / "kb" / "communities"
DEFAULT_OUT = REPO_ROOT / "output" / "kgx"
KGX_NS = uuid.UUID("00000000-0000-0000-0000-000000000001")  # stable namespace
KNOWLEDGE_SOURCE = "infores:communitymech"

# ---------- biolink predicate / category constants ----------

# Categories
CAT_COMMUNITY = "biolink:OrganismalEntity"
CAT_TAXON = "biolink:OrganismTaxon"
CAT_ENVIRONMENT = "biolink:EnvironmentalFeature"
CAT_CHEMICAL = "biolink:ChemicalEntity"
CAT_MEDIUM = "biolink:NamedThing"

# Edge categories
ASSOC_TAXON = "biolink:OrganismToOrganismAssociation"
ASSOC_ENV = "biolink:OrganismToEnvironmentAssociation"
ASSOC_CHEM = "biolink:ChemicalEntityToOrganismalEntityAssociation"
ASSOC_GENERIC = "biolink:Association"

# Predicates
PRED_HAS_PART = "biolink:has_part"
PRED_LOCATED_IN = "biolink:located_in"
PRED_RELATED_TO = "biolink:related_to"
PRED_OCCURS_IN = "biolink:occurs_in"

# Bare-name → CHEBI lookup for the elements appearing in metals_present
# and rare_earth_elements_present. Verified against CHEBI sqlite via
# OAK at port time; expand as new elements appear in community YAMLs.
_ELEMENT_CHEBI: dict[str, tuple[str, str]] = {
    # (uppercase element name): (CHEBI ID, label)
    "TITANIUM": ("CHEBI:33341", "titanium atom"),
    "IRON": ("CHEBI:18248", "iron atom"),
    "COPPER": ("CHEBI:28694", "copper atom"),
    "GOLD": ("CHEBI:29287", "gold atom"),
    "NICKEL": ("CHEBI:28112", "nickel atom"),
    "ZINC": ("CHEBI:27363", "zinc atom"),
    "PALLADIUM": ("CHEBI:33363", "palladium"),
    "VANADIUM": ("CHEBI:27698", "vanadium atom"),
    "CHROMIUM": ("CHEBI:28073", "chromium atom"),
    "LEAD": ("CHEBI:25016", "lead atom"),
    "SILVER": ("CHEBI:30512", "silver atom"),
    "GALLIUM": ("CHEBI:49631", "gallium atom"),
    "COBALT": ("CHEBI:27638", "cobalt atom"),
    "URANIUM": ("CHEBI:27214", "uranium atom"),
    "LITHIUM": ("CHEBI:30145", "lithium atom"),
    "MERCURY": ("CHEBI:16793", "mercury(2+)"),
    # Rare earths
    "CERIUM": ("CHEBI:33369", "cerium"),
    "LANTHANUM": ("CHEBI:33336", "lanthanum atom"),
    "NEODYMIUM": ("CHEBI:33372", "neodymium atom"),
    "PRASEODYMIUM": ("CHEBI:49828", "praseodymium atom"),
    "SAMARIUM": ("CHEBI:33374", "samarium atom"),
    "EUROPIUM": ("CHEBI:49591", "europium(3+)"),
    "DYSPROSIUM": ("CHEBI:33377", "dysprosium atom"),
    "ERBIUM": ("CHEBI:33379", "erbium"),
    "GADOLINIUM": ("CHEBI:33375", "gadolinium atom"),
    "HOLMIUM": ("CHEBI:49650", "holmium(3+)"),
    "TERBIUM": ("CHEBI:33376", "terbium atom"),
    "THULIUM": ("CHEBI:33380", "thulium atom"),
    "YTTERBIUM": ("CHEBI:33381", "ytterbium"),
    "LUTETIUM": ("CHEBI:49746", "lutetium(3+)"),
    "YTTRIUM": ("CHEBI:33331", "yttrium atom"),
}


def _resolve_element(name: str) -> tuple[str, str]:
    """Map a bare element name to (CHEBI:N, label).
    Falls back to (uppercase-as-id, uppercase-as-label) when unknown
    so the export remains total — emit-everything semantics."""
    if not name:
        return "", ""
    key = name.strip().upper()
    if key in _ELEMENT_CHEBI:
        return _ELEMENT_CHEBI[key]
    return key, name


# ---------- evidence formatting (dismech pattern) ----------


def _format_evidence(evidence_items: list[dict] | None) -> tuple[str, str]:
    """Returns (publications, supporting_text). Both '|'-separated."""
    if not evidence_items:
        return "", ""
    pubs: list[str] = []
    snippets: list[str] = []
    for ev in evidence_items:
        ref = (ev.get("reference") or "").strip()
        if ref:
            # Normalize: doi:10.x → DOI:10.x; PMID:NNN → PMID:NNN; bare → no prefix
            if ":" in ref:
                prefix, rest = ref.split(":", 1)
                pubs.append(f"{prefix.upper()}:{rest}")
            else:
                pubs.append(ref)
        snippet = (ev.get("snippet") or "").replace("\t", " ").replace("\n", " ").strip()
        if snippet:
            snippets.append(snippet)
    return "|".join(pubs), "|".join(snippets)


# ---------- graph model ----------


@dataclasses.dataclass
class Node:
    id: str
    category: str
    name: str = ""
    description: str = ""
    provided_by: str = KNOWLEDGE_SOURCE


@dataclasses.dataclass
class Edge:
    id: str
    subject: str
    predicate: str
    object: str
    category: str
    publications: str = ""
    supporting_text: str = ""
    knowledge_level: str = "knowledge_assertion"
    agent_type: str = "manual_agent"
    primary_knowledge_source: str = KNOWLEDGE_SOURCE


def _edge_id(subject: str, predicate: str, obj: str, qualifier: str = "") -> str:
    """Stable UUID5 derived from (subject, predicate, object, qualifier)."""
    key = f"{subject}\t{predicate}\t{obj}\t{qualifier}"
    return f"uuid:{uuid.uuid5(KGX_NS, key)}"


# ---------- per-community extraction ----------


def _extract(community: dict, nodes: dict[str, Node], edges: list[Edge]) -> None:
    cid = community.get("id")
    if not cid:
        return
    name = community.get("name") or cid
    desc = (community.get("description") or "").strip()
    nodes[cid] = Node(cid, CAT_COMMUNITY, name, desc)

    # ---- Community → environment ----
    env = community.get("environment_term") or {}
    env_term = env.get("term") or {}
    env_id = env_term.get("id")
    if env_id:
        nodes.setdefault(
            env_id,
            Node(env_id, CAT_ENVIRONMENT, env_term.get("label") or "", env.get("notes") or ""),
        )
        # Environment-level evidence sometimes lives at the community
        # level via environmental_factors[]
        env_evidence: list[dict] = []
        for f in community.get("environmental_factors") or []:
            env_evidence.extend(f.get("evidence") or [])
        pubs, supp = _format_evidence(env_evidence)
        edges.append(
            Edge(
                id=_edge_id(cid, PRED_LOCATED_IN, env_id),
                subject=cid,
                predicate=PRED_LOCATED_IN,
                object=env_id,
                category=ASSOC_ENV,
                publications=pubs,
                supporting_text=supp,
            )
        )

    # ---- Community → member taxa ----
    for entry in community.get("taxonomy") or []:
        term = (entry.get("taxon_term") or {}).get("term") or {}
        tid = term.get("id")
        if not tid:
            continue
        nodes.setdefault(
            tid, Node(tid, CAT_TAXON, term.get("label") or "", entry.get("functional_role") or "")
        )
        pubs, supp = _format_evidence(entry.get("evidence"))
        qualifier = entry.get("functional_role") or ""
        edges.append(
            Edge(
                id=_edge_id(cid, PRED_HAS_PART, tid, qualifier),
                subject=cid,
                predicate=PRED_HAS_PART,
                object=tid,
                category=ASSOC_TAXON,
                publications=pubs,
                supporting_text=supp,
            )
        )

    # ---- Community → metals_present + rare_earth_elements_present ----
    metal_lists = (
        ("metal", community.get("metals_present") or []),
        ("rare_earth", community.get("rare_earth_elements_present") or []),
    )
    for qualifier, items in metal_lists:
        for metal in items:
            if isinstance(metal, dict):
                mterm = metal.get("term") or {}
                mid = mterm.get("id") or ""
                mlabel = mterm.get("label") or metal.get("preferred_term") or ""
                if not mid:
                    # Fall back to bare-name resolver
                    mid, fallback_label = _resolve_element(metal.get("preferred_term") or "")
                    mlabel = mlabel or fallback_label
                mevidence = metal.get("evidence") or []
            else:
                mid, mlabel = _resolve_element(str(metal))
                mevidence = []
            if not mid:
                continue
            nodes.setdefault(mid, Node(mid, CAT_CHEMICAL, mlabel, ""))
            pubs, supp = _format_evidence(mevidence)
            edges.append(
                Edge(
                    id=_edge_id(cid, PRED_RELATED_TO, mid, qualifier),
                    subject=cid,
                    predicate=PRED_RELATED_TO,
                    object=mid,
                    category=ASSOC_CHEM,
                    publications=pubs,
                    supporting_text=supp,
                )
            )

    # ---- Community → growth_media (CultureMech links if present) ----
    for gm in community.get("growth_media") or []:
        if isinstance(gm, dict):
            gid = gm.get("id") or gm.get("medium_id") or ""
            glabel = gm.get("name") or gm.get("preferred_term") or gid
            gev = gm.get("evidence") or []
        else:
            gid = str(gm)
            glabel = str(gm)
            gev = []
        if not gid:
            continue
        nodes.setdefault(gid, Node(gid, CAT_MEDIUM, glabel, ""))
        pubs, supp = _format_evidence(gev)
        edges.append(
            Edge(
                id=_edge_id(cid, PRED_OCCURS_IN, gid, "growth_medium"),
                subject=cid,
                predicate=PRED_OCCURS_IN,
                object=gid,
                category=ASSOC_GENERIC,
                publications=pubs,
                supporting_text=supp,
            )
        )


# ---------- driver ----------


def export_kgx(kb_dir: Path, output_dir: Path) -> tuple[int, int]:
    """Walk kb_dir/*.yaml; write nodes.tsv + edges.tsv to output_dir.
    Returns (node_count, edge_count)."""
    output_dir.mkdir(parents=True, exist_ok=True)
    nodes: dict[str, Node] = {}
    edges: list[Edge] = []
    n_records = 0
    for path in sorted(kb_dir.glob("*.yaml")):
        try:
            with open(path) as f:
                community = yaml.safe_load(f)
        except Exception as e:
            print(f"  ERROR reading {path.name}: {e}", file=sys.stderr)
            continue
        if not isinstance(community, dict):
            continue
        _extract(community, nodes, edges)
        n_records += 1

    # Write nodes.tsv
    node_cols = ["id", "category", "name", "description", "provided_by"]
    nodes_path = output_dir / "nodes.tsv"
    with open(nodes_path, "w", newline="") as f:
        w = csv.writer(f, delimiter="\t")
        w.writerow(node_cols)
        for n in sorted(nodes.values(), key=lambda x: x.id):
            w.writerow([n.id, n.category, n.name, n.description, n.provided_by])

    # Write edges.tsv
    edge_cols = [
        "id",
        "subject",
        "predicate",
        "object",
        "category",
        "publications",
        "supporting_text",
        "knowledge_level",
        "agent_type",
        "primary_knowledge_source",
    ]
    edges_path = output_dir / "edges.tsv"
    seen_ids: set[str] = set()
    with open(edges_path, "w", newline="") as f:
        w = csv.writer(f, delimiter="\t")
        w.writerow(edge_cols)
        for edge in sorted(edges, key=lambda x: (x.subject, x.predicate, x.object, x.id)):
            if edge.id in seen_ids:
                continue
            seen_ids.add(edge.id)
            w.writerow(
                [
                    edge.id,
                    edge.subject,
                    edge.predicate,
                    edge.object,
                    edge.category,
                    edge.publications,
                    edge.supporting_text,
                    edge.knowledge_level,
                    edge.agent_type,
                    edge.primary_knowledge_source,
                ]
            )

    # Provenance manifest
    manifest_path = output_dir / "manifest.json"
    import json

    manifest = {
        "generator": "communitymech.export.kgx_export",
        "generated_at": _dt.datetime.now(_dt.timezone.utc).isoformat(timespec="seconds"),
        "knowledge_source": KNOWLEDGE_SOURCE,
        "input_kb_dir": str(kb_dir.resolve()),
        "input_record_count": n_records,
        "node_count": len(nodes),
        "edge_count": len(seen_ids),
    }
    with open(manifest_path, "w") as f:
        json.dump(manifest, f, indent=2)

    return len(nodes), len(seen_ids)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--kb", type=Path, default=DEFAULT_KB)
    ap.add_argument("--output", type=Path, default=DEFAULT_OUT)
    args = ap.parse_args()
    if not args.kb.is_dir():
        print(f"kb dir not found: {args.kb}", file=sys.stderr)
        return 2
    n_nodes, n_edges = export_kgx(args.kb, args.output)
    print(f"Wrote {n_nodes} nodes / {n_edges} edges to {args.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
