"""Regression and mutation-proof gate tests for Cycle 11/12/13 Stage 3 (protein_examples)."""

from __future__ import annotations

import copy
import hashlib
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parents[1]
SHEW_PATH = REPO / "kb/taxa/Shewanella_oneidensis_MR1.yaml"
GEO_PATH = REPO / "kb/taxa/Geobacter_sulfurreducens.yaml"
C11_REPORT_PATH = REPO / "reports/c11s3_uniprot_protein_corpus_review_20261108.md"
C12_REPORT_PATH = REPO / "reports/c12s3_uniprot_protein_corpus_review_20261108.md"
REPORT_PATH = REPO / "reports/c13s3_uniprot_protein_corpus_review_20261109.md"


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _snippet_matches(snippet: str, cache_text: str) -> bool:
    return " ".join(snippet.split()) in " ".join(cache_text.split())


def verify_c11s3_protein_contract(
    taxa_docs: dict[str, dict],
    taxa_hashes: dict[str, str],
    ref_caches: dict[str, str],
    report_text: str,
    community_common_taxon_ids: dict[str, set[str]],
) -> None:
    """Validate Stage 3 CommonTaxon UniProtKB evidence, SHA-256 ledger, and links."""
    expected_taxa_hashes = {
        "CommunityMech:taxon:000001": (
            "5994b4b237f3d87d16dcbb47edfd6a9fa88fc3898100457ce39036e712cccdf6"
        ),
        "CommunityMech:taxon:000002": (
            "413329d881e1bcfcf692ffcd76a3839d183e9abd64952703233f6e786b918d7e"
        ),
    }
    for tid, exp_sha in expected_taxa_hashes.items():
        actual_sha = taxa_hashes.get(tid)
        if actual_sha != exp_sha:
            raise AssertionError(f"{tid} SHA-256 mismatch: expected {exp_sha}, got {actual_sha}")
        if exp_sha not in report_text:
            raise AssertionError(f"{tid} SHA-256 {exp_sha} missing from c13s3 report")

    expected_gene_counts = {
        "CommunityMech:taxon:000001": {
            "mtrC": ("UniProtKB:Q8EG33", "SO_1778", 11),
            "mtrB": ("UniProtKB:Q8EG34", "SO_1776", 5),
            "mtrA": ("UniProtKB:Q8EG35", "SO_1777", 6),
            "omcA": ("UniProtKB:Q8EG32", "SO_1779", 11),
            "cymA": ("UniProtKB:Q8E945", "SO_4591", 6),
        },
        "CommunityMech:taxon:000002": {
            "pilA": ("UniProtKB:Q74BW5", "GSU1496", 8),
            "omcS": ("UniProtKB:Q749X9", "GSU2504", 10),
            "omcZ": ("UniProtKB:Q74A90", "GSU2076", 6),
            "omcB": ("UniProtKB:Q74A86", "GSU2737", 7),
        },
    }

    total_evs = 0
    for tid, exp_genes in expected_gene_counts.items():
        doc = taxa_docs[tid]
        genes = {g["gene_symbol"]: g for g in (doc.get("genes") or [])}
        if set(genes) != set(exp_genes):
            raise AssertionError(f"{tid} gene set mismatch: {set(genes)} != {set(exp_genes)}")
        for sym, (exp_uniprot, exp_locus, exp_ev_count) in exp_genes.items():
            gene = genes[sym]
            if gene.get("gene_id") != exp_uniprot:
                raise AssertionError(f"{tid} {sym} gene_id {gene.get('gene_id')} != {exp_uniprot}")
            if gene.get("locus_tag") != exp_locus:
                raise AssertionError(
                    f"{tid} {sym} locus_tag {gene.get('locus_tag')} != {exp_locus}"
                )
            evs = gene.get("evidence") or []
            if len(evs) != exp_ev_count:
                raise AssertionError(
                    f"{tid} {sym} evidence count {len(evs)} != expected {exp_ev_count}"
                )
            norm_snippets: list[tuple[str, str]] = []
            for ev in evs:
                snip = ev.get("snippet", "")
                if "[" in snip or "]" in snip:
                    raise AssertionError(f"Bracketed text in {tid} {sym} snippet: {snip}")
                ref = ev.get("reference", "")
                cache_text = ref_caches.get(ref, "")
                if not cache_text or not _snippet_matches(snip, cache_text):
                    raise AssertionError(
                        f"Snippet not verbatim in cached reference {ref} for {tid} {sym}: {snip}"
                    )
                norm = " ".join(snip.split())
                for prev_ref, prev_norm in norm_snippets:
                    if prev_ref == ref and (norm in prev_norm or prev_norm in norm):
                        raise AssertionError(
                            f"Overlapping snippets for {ref} on {tid} {sym}: {snip}"
                        )
                norm_snippets.append((ref, norm))
                total_evs += 1

        hist = doc.get("curation_history") or []
        if not hist or hist[-1].get("action") != "ADD_UNIPROT_PROTEIN_EXAMPLES":
            raise AssertionError(
                f"{tid} latest curation_history action must be ADD_UNIPROT_PROTEIN_EXAMPLES"
            )

    if total_evs != 70:
        raise AssertionError(f"Expected 70 total CommonTaxon EvidenceItems, got {total_evs}")

    expected_mr1_ids = {
        "CommunityMech:000177",
        "CommunityMech:000203",
        "CommunityMech:000211",
        "CommunityMech:000279",
        "CommunityMech:000288",
        "CommunityMech:000294",
        "CommunityMech:000298",
        "CommunityMech:000385",
        "CommunityMech:000402",
        "CommunityMech:000519",
        "CommunityMech:000520",
        "CommunityMech:000523",
        "CommunityMech:000524",
        "CommunityMech:000526",
        "CommunityMech:000527",
        "CommunityMech:000528",
    }
    expected_geo_ids = {
        "CommunityMech:000031",
        "CommunityMech:000175",
        "CommunityMech:000176",
        "CommunityMech:000177",
        "CommunityMech:000201",
        "CommunityMech:000268",
    }
    if community_common_taxon_ids.get("CommunityMech:taxon:000001") != expected_mr1_ids:
        raise AssertionError(
            f"CommonTaxon 000001 linked IDs mismatch: "
            f"{community_common_taxon_ids.get('CommunityMech:taxon:000001')} != {expected_mr1_ids}"
        )
    if community_common_taxon_ids.get("CommunityMech:taxon:000002") != expected_geo_ids:
        raise AssertionError(
            f"CommonTaxon 000002 linked IDs mismatch: "
            f"{community_common_taxon_ids.get('CommunityMech:taxon:000002')} != {expected_geo_ids}"
        )


def _load_real_inputs() -> tuple[
    dict[str, dict],
    dict[str, str],
    dict[str, str],
    str,
    dict[str, set[str]],
]:
    shew_doc = yaml.safe_load(SHEW_PATH.read_text())
    geo_doc = yaml.safe_load(GEO_PATH.read_text())
    taxa_docs = {
        shew_doc["id"]: shew_doc,
        geo_doc["id"]: geo_doc,
    }
    taxa_hashes = {
        shew_doc["id"]: _sha256(SHEW_PATH),
        geo_doc["id"]: _sha256(GEO_PATH),
    }

    ref_caches: dict[str, str] = {}
    for doc in taxa_docs.values():
        for g in doc.get("genes") or []:
            for ev in g.get("evidence") or []:
                ref = ev["reference"]
                if ref not in ref_caches:
                    pmid = ref.split(":", 1)[1]
                    parts = [
                        p.read_text()
                        for p in (
                            REPO / f"references_cache/PMID_{pmid}.txt",
                            REPO / f"references_cache/PMID_{pmid}.md",
                        )
                        if p.exists()
                    ]
                    ref_caches[ref] = " ".join(parts)

    community_common_taxon_ids: dict[str, set[str]] = {
        "CommunityMech:taxon:000001": set(),
        "CommunityMech:taxon:000002": set(),
    }
    for root in ("kb/communities", "data/isolates"):
        for path in sorted((REPO / root).glob("*.yaml")):
            doc = yaml.safe_load(path.read_text())
            for t in doc.get("taxonomy") or []:
                ct = t.get("common_taxon")
                if ct in community_common_taxon_ids:
                    community_common_taxon_ids[ct].add(doc["id"])

    report_text = REPORT_PATH.read_text()
    return taxa_docs, taxa_hashes, ref_caches, report_text, community_common_taxon_ids


def test_c11s3_protein_grounding_contract_and_corpus_ledger() -> None:
    taxa_docs, taxa_hashes, ref_caches, report_text, community_common_taxon_ids = (
        _load_real_inputs()
    )
    verify_c11s3_protein_contract(
        taxa_docs, taxa_hashes, ref_caches, report_text, community_common_taxon_ids
    )

    c11_report = C11_REPORT_PATH.read_text()
    c12_report = C12_REPORT_PATH.read_text()
    for c11_sha in (
        "3bb69ddaa4d9064fe6340d04dff7bd9bac375fb08495580e369ba239b71bdd75",
        "ab3bcd9639241391f25a20b5bbdb3a40ee6e907d441f696355ce16745e3c4b92",
    ):
        assert c11_sha in c11_report and c11_sha in c12_report and c11_sha in report_text
    for c12_sha in (
        "5666e10e654de62d43df48c97be2215b1b24e7c94b471b3ece95bb248b7f41f5",
        "aeddfc60dfc34c721e1b2355aeddcd1b809da8196e449d360ce509f0af0c76dc",
    ):
        assert c12_sha in c12_report and c12_sha in report_text

    for hrel in (
        "history/records/Shewanella_oneidensis_MR1/2026-11-08T083200Z-antigravity-c11s301.yaml",
        "history/records/Geobacter_sulfurreducens/2026-11-08T083200Z-antigravity-c11s302.yaml",
        "history/records/Shewanella_oneidensis_MR1/2026-11-09T021000Z-antigravity-c12s301.yaml",
        "history/records/Geobacter_sulfurreducens/2026-11-09T021000Z-antigravity-c12s302.yaml",
        "history/records/Shewanella_oneidensis_MR1/2026-11-09T214500Z-antigravity-c13s301.yaml",
        "history/records/Geobacter_sulfurreducens/2026-11-09T214500Z-antigravity-c13s302.yaml",
    ):
        assert (REPO / hrel).is_file(), f"Missing Stage 3 history sidecar: {hrel}"


def test_the_check_can_actually_fail() -> None:
    taxa_docs, taxa_hashes, ref_caches, report_text, community_common_taxon_ids = (
        _load_real_inputs()
    )

    # 1. Control arm: unmutated copy passes
    verify_c11s3_protein_contract(
        copy.deepcopy(taxa_docs),
        copy.deepcopy(taxa_hashes),
        copy.deepcopy(ref_caches),
        report_text,
        copy.deepcopy(community_common_taxon_ids),
    )

    # 2. Mutated arm A: corrupted SHA-256 hash fails
    mut_hashes = copy.deepcopy(taxa_hashes)
    mut_hashes["CommunityMech:taxon:000001"] = "0" * 64
    with pytest.raises(AssertionError, match="SHA-256 mismatch"):
        verify_c11s3_protein_contract(
            taxa_docs, mut_hashes, ref_caches, report_text, community_common_taxon_ids
        )

    # 3. Mutated arm B: bracketed text in snippet fails
    mut_docs_b = copy.deepcopy(taxa_docs)
    mut_docs_b["CommunityMech:taxon:000001"]["genes"][0]["evidence"][-1]["snippet"] += " [...]"
    with pytest.raises(AssertionError, match="Bracketed text"):
        verify_c11s3_protein_contract(
            mut_docs_b, taxa_hashes, ref_caches, report_text, community_common_taxon_ids
        )

    # 4. Mutated arm C: overlapping duplicate snippet on same gene & reference fails
    mut_docs_c = copy.deepcopy(taxa_docs)
    mut_docs_c["CommunityMech:taxon:000001"]["genes"][0]["evidence"][-2] = copy.deepcopy(
        mut_docs_c["CommunityMech:taxon:000001"]["genes"][0]["evidence"][-1]
    )
    with pytest.raises(AssertionError, match="Overlapping snippets"):
        verify_c11s3_protein_contract(
            mut_docs_c, taxa_hashes, ref_caches, report_text, community_common_taxon_ids
        )

    # 5. Mutated arm D: missing CommunityMech:000526 common_taxon link fails
    mut_links = copy.deepcopy(community_common_taxon_ids)
    mut_links["CommunityMech:taxon:000001"].remove("CommunityMech:000526")
    with pytest.raises(AssertionError, match="CommonTaxon 000001 linked IDs mismatch"):
        verify_c11s3_protein_contract(taxa_docs, taxa_hashes, ref_caches, report_text, mut_links)
