#!/usr/bin/env python3
"""Compute sentence-transformer text embeddings for every CommunityMech record.

Walks ``kb/communities/*.yaml``, assembles a canonical natural-language
document per community record (name, category, ecological state, origin,
description, environmental factors, taxonomy + functional roles, and
ecological interactions + metabolites), encodes with a local sentence-transformer
model (default ``BAAI/bge-small-en-v1.5``, 384-d, L2-normalized), and writes a
compact ``data/embeddings/records.npz`` bundle.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import time
from pathlib import Path
from typing import Any

import numpy as np
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
RECORDS_DIR = REPO_ROOT / "kb" / "communities"
DEFAULT_OUT = REPO_ROOT / "data" / "embeddings" / "records.npz"
DEFAULT_MODEL = "BAAI/bge-small-en-v1.5"


def _clean(value: Any) -> str:
    if value is None:
        return ""
    return " ".join(str(value).split())


def record_to_text(path: Path, doc: dict[str, Any]) -> tuple[str, dict[str, Any]]:
    """Build the text passage to embed and lightweight display metadata."""
    stem = path.stem
    community_id = _clean(doc.get("id")) or stem
    name = _clean(doc.get("name")) or stem
    category = _clean(doc.get("community_category")) or "OTHER"
    eco_state = _clean(doc.get("ecological_state")) or "UNKNOWN"
    origin = _clean(doc.get("community_origin")) or "UNKNOWN"
    desc = _clean(doc.get("description"))

    lines: list[str] = [f"{name} ({community_id})"]
    header_bits = [
        f"Category: {category}",
        f"Ecological state: {eco_state}",
        f"Origin: {origin}",
    ]
    lines.append(" | ".join(header_bits))
    if desc:
        lines.append(desc)

    keywords: list[str] = [category, eco_state, origin]

    env = doc.get("environmental_factors")
    env_name = ""
    if isinstance(env, dict):
        env_name = _clean(env.get("name"))
        env_term = env.get("environment_term") or {}
        if isinstance(env_term, dict):
            term_obj = env_term.get("term") or {}
            term_label = _clean(
                env_term.get("preferred_term")
                or (term_obj.get("label") if isinstance(term_obj, dict) else "")
            )
            if term_label and term_label not in env_name:
                env_name = f"{env_name} ({term_label})" if env_name else term_label
        env_bits = [b for b in [
            env_name,
            _clean(env.get("habitat")),
            _clean(env.get("description")),
        ] if b]
        if env_bits:
            lines.append("Environment: " + "; ".join(env_bits))
            keywords.append(env_name or env_bits[0])

    metals = doc.get("metals_present") or []
    if isinstance(metals, list) and metals:
        metal_strs = [_clean(m) for m in metals if _clean(m)]
        if metal_strs:
            lines.append("Metals present: " + ", ".join(metal_strs))
            keywords.extend(metal_strs)

    taxa = doc.get("taxonomy") or []
    taxon_chunks: list[str] = []
    if isinstance(taxa, list):
        for entry in taxa:
            if not isinstance(entry, dict):
                continue
            tterm = entry.get("taxon_term") or {}
            tname = ""
            if isinstance(tterm, dict):
                term_obj = tterm.get("term") or {}
                tname = _clean(
                    tterm.get("preferred_term")
                    or (term_obj.get("label") if isinstance(term_obj, dict) else "")
                )
            roles = entry.get("functional_role") or []
            if isinstance(roles, str):
                roles = [roles]
            role_str = ", ".join(_clean(r) for r in roles if _clean(r))
            if tname:
                keywords.append(tname)
                taxon_chunks.append(f"{tname} [{role_str}]" if role_str else tname)
    if taxon_chunks:
        lines.append("Taxonomic members: " + "; ".join(taxon_chunks))

    interactions = doc.get("ecological_interactions") or []
    ix_chunks: list[str] = []
    if isinstance(interactions, list):
        for ix in interactions:
            if not isinstance(ix, dict):
                continue
            iname = _clean(ix.get("name"))
            itype = _clean(ix.get("interaction_type"))
            idesc = _clean(ix.get("description"))
            mets = ix.get("metabolites") or []
            met_names: list[str] = []
            if isinstance(mets, list):
                for m in mets:
                    if isinstance(m, dict):
                        term_obj = m.get("term") or {}
                        mlabel = _clean(
                            m.get("preferred_term")
                            or (term_obj.get("label") if isinstance(term_obj, dict) else "")
                        )
                        if mlabel:
                            met_names.append(mlabel)
                            keywords.append(mlabel)
            if iname:
                keywords.append(iname)
            chunk = " - ".join(
                b for b in [
                    f"{iname} ({itype})" if iname and itype else (iname or itype),
                    idesc,
                    ("Metabolites: " + ", ".join(met_names)) if met_names else "",
                ]
                if b
            )
            if chunk:
                ix_chunks.append(chunk)
    if ix_chunks:
        lines.append("Ecological interactions: " + " | ".join(ix_chunks))

    text = "\n".join(lines)
    meta = {
        "id": stem,
        "community_id": community_id,
        "file": str(path.relative_to(REPO_ROOT)),
        "title": name,
        "category": category,
        "ecological_state": eco_state,
        "community_origin": origin,
        "environment": env_name or "Unspecified",
        "n_taxa": len(taxa) if isinstance(taxa, list) else 0,
        "n_interactions": len(interactions) if isinstance(interactions, list) else 0,
        "n_metals": len(metals) if isinstance(metals, list) else 0,
        "summary": (desc[:360] + ("..." if len(desc) > 360 else "")),
        "keywords": sorted({k for k in keywords if k})[:40],
        "text_sha256": hashlib.sha256(text.encode("utf-8")).hexdigest()[:16],
    }
    return text, meta


def load_corpus(records_dir: Path = RECORDS_DIR) -> tuple[list[str], list[dict[str, Any]]]:
    paths = sorted(records_dir.glob("*.yaml"))
    texts: list[str] = []
    metas: list[dict[str, Any]] = []
    for p in paths:
        doc = yaml.safe_load(p.read_text(encoding="utf-8"))
        if not isinstance(doc, dict):
            continue
        text, meta = record_to_text(p, doc)
        texts.append(text)
        metas.append(meta)
    return texts, metas


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", default=DEFAULT_MODEL, help="SentenceTransformer model id")
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT, help="Output .npz path")
    parser.add_argument("--batch-size", type=int, default=32)
    parser.add_argument("--device", default=None, help="torch device override (cpu, mps, cuda)")
    args = parser.parse_args()

    from sentence_transformers import SentenceTransformer

    t0 = time.time()
    texts, metas = load_corpus()
    print(f"Loaded {len(texts)} community records from {RECORDS_DIR.relative_to(REPO_ROOT)}")

    model = SentenceTransformer(args.model, device=args.device)
    embeddings = model.encode(
        texts,
        batch_size=args.batch_size,
        show_progress_bar=True,
        normalize_embeddings=True,
        convert_to_numpy=True,
    ).astype(np.float32)

    args.out.parent.mkdir(parents=True, exist_ok=True)
    ids = np.array([m["id"] for m in metas])
    meta_json = json.dumps(metas, ensure_ascii=False)
    np.savez_compressed(
        args.out,
        ids=ids,
        embeddings=embeddings,
        model=np.array(args.model),
        metadata_json=np.array(meta_json),
    )
    dt = time.time() - t0
    print(
        f"Wrote {embeddings.shape[0]} x {embeddings.shape[1]} embeddings "
        f"to {args.out.relative_to(REPO_ROOT)} in {dt:.1f}s"
    )


if __name__ == "__main__":
    main()
