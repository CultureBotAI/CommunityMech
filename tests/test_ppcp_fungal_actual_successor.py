"""Actual PPCP420 proof plus rehashed domain refusals, #2904/#2907, 2026-11-15.

Reuse the existing 15-mutation harness with a fixture-scoped fungal adapter.
Only isolated public-artifact copies mutate; executed originals remain frozen.
"""

import copy
import json
from pathlib import Path

import ppcp_fungal_gtdb_successor as registry
import pytest
import scoped_gtdb_fungal_successor as fungal
import test_scoped_gtdb_actual_successor as shared
import yaml
from test_scoped_gtdb_actual_successor import (
    test_actual_rehashed_tampering_refuses_and_restores,  # noqa: F401
    test_actual_shared_engine_successor_admits_and_retains_old_history,  # noqa: F401
)

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture
def actual(tmp_path, monkeypatch):
    # The immutable factory still reads real Git predecessor bytes. Scope its
    # adapter to this fixture so original generic proof cases remain unchanged.
    monkeypatch.setattr(shared, "successor", fungal)
    allowed = registry.ALLOWANCES[registry.TARGET]
    result = shared.build_actual(
        tmp_path,
        monkeypatch,
        proof_root=ROOT,
        manifest=allowed["manifest"]["path"],
        manifest_sha=allowed["manifest"]["sha256"],
        baseline_revision=allowed["baseline_revision"],
        historical_llm=True,
    )
    root, proof, _allowances, retained, _history = result
    name = proof["domain_observation"]["path"]
    raw = (ROOT / name).read_bytes()
    assert fungal.digest(raw) == proof["domain_observation"]["sha256"]
    (root / name).write_bytes(raw)
    retained[name] = raw
    return result


def test_registry_admits_actual_refuses_unknown_change_and_restores():
    result = registry.admit_ppcp_successor(ROOT, registry.TARGET, registry.BEFORE)
    assert result.changed and fungal.digest(result.historical_bytes) == registry.BEFORE
    with pytest.raises(AssertionError, match="unknown changed record"):
        registry.admit_ppcp_successor(
            ROOT, "kb/communities/Unreviewed.yaml", registry.BEFORE, current=b"changed"
        )
    assert registry.admit_ppcp_successor(ROOT, registry.TARGET, registry.BEFORE).changed


@pytest.mark.parametrize(
    "mutation", ["fungi", "eukaryota", "domain", "outside", "rank", "stock", "hold"]
)
def test_actual_rehashed_domain_mutation_refuses_and_restores(actual, mutation):
    root, proof, allowed, retained, _history = actual
    assert shared.check(actual).changed
    original = copy.deepcopy(proof)
    manifest = allowed[proof["target"]]["manifest"]
    manifest_sha = manifest["sha256"]
    review = yaml.safe_load((root / proof["diagnostic_review"]["path"]).read_bytes())
    domain_item = proof["domain_observation"]
    domain = json.loads((root / domain_item["path"]).read_bytes())
    source_item = proof["native_recomputation"]
    source = json.loads((root / source_item["path"]).read_bytes())
    applied_item = proof["application_receipt"]
    applied = json.loads((root / applied_item["path"]).read_bytes())
    observed = domain["observations"][0]
    if mutation in {"fungi", "eukaryota"}:
        observed["ancestor_ids"].remove(
            "NCBITaxon:4751" if mutation == "fungi" else "NCBITaxon:2759"
        )
    elif mutation == "domain":
        observed["domain"] = "NCBITaxon:2"
    elif mutation == "outside":
        observed["outside_gtdb_scope"] = False
    elif mutation == "rank":
        selected = next(row for row in source["occurrences"] if row["taxonomy_index"] == 2)
        for rows in (observed["ncbi_identity_rows"], selected["ncbi_identity_rows"]):
            rank = next(row for row in rows if row["predicate"].endswith("rank"))
            rank["object"] = None
    elif mutation == "stock":
        observed["strain_name"] = "Invented stock"
    else:
        observed["manual_withheld_reason"] = "Unreviewed hold"
    # Rehash every dependent public link and review input, so refusal exercises
    # domain semantics rather than just an intentionally stale artifact hash.
    domain_sha = shared.write(root, domain_item, domain)
    domain_item["raw_sha256"] = domain_sha
    shared.replace_review_hash(review, domain_item["raw_path"], domain_sha)
    applied["domain_proof"]["sha256"] = domain_sha
    source["domain_proof"]["sha256"] = domain_sha
    source["domain_observation"] = domain
    applied_sha = shared.write(root, applied_item, applied)
    applied_item["raw_sha256"] = applied_sha
    shared.replace_review_hash(review, applied_item["raw_path"], applied_sha)
    source_sha = shared.write(root, source_item, source)
    source_item["raw_sha256"] = source_sha
    proof["grounding_evidence"]["sha256"] = source_sha
    shared.replace_review_hash(review, source_item["raw_path"], source_sha)
    shared.reseal_review(root, proof, review)
    manifest["sha256"] = shared.write(root, manifest, proof)
    assert domain != json.loads(retained[domain_item["path"]])
    expected = "recognized NCBI rank" if mutation == "rank" else "affirmative matched"
    with pytest.raises(ValueError, match=expected):
        shared.check(actual)
    for name, raw in retained.items():
        (root / name).write_bytes(raw)
    proof.clear()
    proof.update(original)
    manifest["sha256"] = manifest_sha
    assert shared.check(actual).changed
