"""Force-directed 2D layout of a symmetric union-kNN graph over embeddings, via Graphviz sfdp.

Self-contained: scikit-learn (kNN) + the `sfdp` binary (Graphviz). No pygraphviz/
pydot needed. Deterministic-ish via -Gstart=<seed>. Rows are L2-normalized so the
Euclidean kNN mirrors the cosine metric used elsewhere. Output row order == input.
"""

import hashlib
import subprocess

import numpy as np
from sklearn.neighbors import kneighbors_graph  # type: ignore[import-untyped]
from sklearn.preprocessing import normalize  # type: ignore[import-untyped]

from communitymech.graph_embedding_receipts import matrix_receipt


def sfdp_layout(matrix, k=15, seed=42, sfdp_bin="sfdp", *, return_receipt=False, record_ids=None):
    """Return an (n, 2) float32 array of 2D coordinates for the rows of `matrix`."""
    matrix = normalize(np.asarray(matrix, dtype="float32"))
    n = matrix.shape[0]
    if n == 0:
        return np.zeros((0, 2), dtype="float32")
    requested_k = k
    k = min(k, max(1, n - 1))
    adj = kneighbors_graph(matrix, n_neighbors=k, mode="connectivity")
    adj = adj.maximum(adj.T)  # symmetric union-kNN graph
    coo = adj.tocoo()
    edges = {
        (min(i, j), max(i, j))
        for i, j in zip(coo.row.tolist(), coo.col.tolist(), strict=True)
        if i != j
    }
    dot = "\n".join(
        ["graph G {"]
        + [f"{i};" for i in range(n)]
        + [f"{i}--{j};" for i, j in sorted(edges)]
        + ["}"]
    )
    out = subprocess.run(
        [sfdp_bin, "-Tplain", f"-Gstart={seed}", "-Goverlap=prism", "-Gsmoothing=triangle"],
        input=dot,
        capture_output=True,
        text=True,
        timeout=900,
    )
    if out.returncode != 0:
        raise RuntimeError(f"sfdp failed (is graphviz installed?): {out.stderr[:300]}")
    xy = np.zeros((n, 2), dtype="float32")
    seen = set()
    for ln in out.stdout.splitlines():
        if ln.startswith("node "):
            p = ln.split()
            idx = int(p[1])
            if idx in seen or not 0 <= idx < n:
                raise ValueError("sfdp returned an invalid or repeated node")
            seen.add(idx)
            xy[idx, 0] = float(p[2])
            xy[idx, 1] = float(p[3])
    if len(seen) != n or not np.isfinite(xy).all():
        raise ValueError("sfdp did not return finite coordinates for every node")
    if return_receipt:
        version = subprocess.run(
            [sfdp_bin, "-V"], capture_output=True, text=True, check=True
        ).stderr.strip()
        if not version:
            raise ValueError("sfdp did not identify its Graphviz version")
        graph = {
            "construction": "symmetric_union_knn",
            "metric": "euclidean",
            "requested_k": requested_k,
            "effective_k": k,
            "edges": len(edges),
            "dot_sha256": hashlib.sha256(dot.encode()).hexdigest(),
            "graphviz_version": version,
            "arguments": ["-Tplain", f"-Gstart={seed}", "-Goverlap=prism", "-Gsmoothing=triangle"],
            "matrix": matrix_receipt(
                matrix, record_ids if record_ids is not None else [str(i) for i in range(n)]
            ),
        }
        return xy, graph
    return xy
