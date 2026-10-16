#!/usr/bin/env python3
"""Project CommunityMech text embeddings into 2D (PaCMAP + PCA) and write corpus_map.json.

Reads ``data/embeddings/records.npz`` produced by ``scripts/embed_records.py``,
computes a 2D PaCMAP layout, a 2D PCA layout, and top-k nearest neighbors by
cosine similarity, and writes ``data/embeddings/corpus_map.json``.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import numpy as np

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_NPZ = REPO_ROOT / "data" / "embeddings" / "records.npz"
DEFAULT_JSON = REPO_ROOT / "data" / "embeddings" / "corpus_map.json"


def _pca_2d(x: np.ndarray) -> tuple[np.ndarray, list[float]]:
    xc = x - x.mean(axis=0, keepdims=True)
    u, s, _ = np.linalg.svd(xc, full_matrices=False)
    coords = u[:, :2] * s[:2]
    var = (s**2) / max(len(x) - 1, 1)
    ratio = (var[:2] / var.sum()).tolist()
    return coords, [round(float(r), 4) for r in ratio]


def _normalize_coords(coords: np.ndarray) -> np.ndarray:
    c = coords.astype(np.float64)
    c = c - c.mean(axis=0, keepdims=True)
    scale = np.abs(c).max()
    if scale > 0:
        c = c / scale
    return np.round(c, 4)


def _top_k_neighbors(emb: np.ndarray, ids: list[str], k: int = 8) -> list[list[dict[str, Any]]]:
    sim = emb @ emb.T
    np.fill_diagonal(sim, -np.inf)
    n = emb.shape[0]
    k = min(k, max(n - 1, 0))
    out: list[list[dict[str, Any]]] = []
    for i in range(n):
        row = sim[i]
        idx = np.argpartition(-row, kth=k - 1)[:k] if k > 0 else np.array([], dtype=int)
        idx = idx[np.argsort(-row[idx])]
        out.append([{"id": ids[int(j)], "sim": round(float(row[int(j)]), 3)} for j in idx])
    return out


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--npz", type=Path, default=DEFAULT_NPZ)
    parser.add_argument("--out-json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--neighbors", type=int, default=8)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    import pacmap

    bundle = np.load(args.npz, allow_pickle=False)
    emb = bundle["embeddings"].astype(np.float32)
    model_name = str(bundle["model"].item())
    metas: list[dict[str, Any]] = json.loads(str(bundle["metadata_json"].item()))
    ids = [m["id"] for m in metas]

    n_neighbors = min(10, max(2, emb.shape[0] - 1))
    reducer = pacmap.PaCMAP(
        n_components=2,
        n_neighbors=n_neighbors,
        MN_ratio=0.5,
        FP_ratio=2.0,
        random_state=args.seed,
        verbose=False,
    )
    pac_coords = _normalize_coords(reducer.fit_transform(emb))
    pca_coords, pca_var = _pca_2d(emb)
    pca_coords = _normalize_coords(pca_coords)
    knn = _top_k_neighbors(emb, ids, k=args.neighbors)

    points: list[dict[str, Any]] = []
    for i, m in enumerate(metas):
        points.append(
            {
                **m,
                "x_pacmap": float(pac_coords[i, 0]),
                "y_pacmap": float(pac_coords[i, 1]),
                "x_pca": float(pca_coords[i, 0]),
                "y_pca": float(pca_coords[i, 1]),
                "neighbors": knn[i],
            }
        )

    payload = {
        "model": model_name,
        "dim": int(emb.shape[1]),
        "count": int(emb.shape[0]),
        "pca_variance_ratio": pca_var,
        "points": points,
    }

    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(f"Wrote {args.out_json.relative_to(REPO_ROOT)} ({len(points)} records)")


if __name__ == "__main__":
    main()
