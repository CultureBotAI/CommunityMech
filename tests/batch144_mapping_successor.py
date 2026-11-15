"""Admit source-bound GTDB successors without changing batch144 biology (#2849).

2026-11-15. The original Git records and ledger remain immutable. Two exact
records may change one GTDB block and append one native event; BR1 may also
replace its one obsolete GTDB token in the opening description. Actual apply,
saved scoped assessment, source proof and sidecar bindings remain mandatory.
"""

import copy
import subprocess

import yaml
from sulfobacillus_mapping_successor import artifact, digest, reviewed_input

from scripts.record_review import render_markdown, validate_review

BASELINE = "68699871415fda3c9eebf20382a315f9f3c7b17a"
MANIFEST = "reports/gtdb-source-routes-2849-20261115/batch144-successors-001.json"
BR1 = "data/isolates/Microbacterium_BR1_Sulfadiazine_Cleaving_Isolate_Baseline.yaml"
TERRABACTER = "data/isolates/Terrabacter_2APm3_Sulfadiazine_Isolate_Baseline.yaml"
TARGETS = {
    BR1: ("CommunityMech:000531", "NCBITaxon:1070896", "Microbacterium sp. BR1"),
    TERRABACTER: ("CommunityMech:000532", "NCBITaxon:1472881", "Terrabacter sp. 2APm3"),
}
SELECTOR = "taxonomy[0].taxon_term.gtdb_classification"


def unchanged_science(path, before, after):
    identity, taxon, label = TARGETS[path]
    assert before["id"] == after["id"] == identity
    old_history = before["curation_history"]
    assert after["curation_history"][:-1] == old_history
    assert after["curation_history"][-1]["llm_assisted"] is True
    assert after["taxonomy"][0]["taxon_term"]["term"] == {"id": taxon, "label": label}
    old, new = copy.deepcopy(before), copy.deepcopy(after)
    for document in (old, new):
        document.pop("curation_history")
        document["taxonomy"][0]["taxon_term"].pop("gtdb_classification")
    if path == BR1:
        obsolete = "GTDB:s__Microbacterium_lacus"
        replacement = "GTDB:s__Microbacterium_sp002812725"
        assert old["description"].count(obsolete) == 1
        assert new["description"] == old["description"].replace(obsolete, replacement, 1)
        old["description"] = new["description"]
    assert old == new, "all other biological claims, quotations and prior history must remain equal"


def verify_grounding(path, before_hash, after_hash, after, proof):
    block = after["taxonomy"][0]["taxon_term"]["gtdb_classification"]
    assert block["curated"] is True and block["curation_note"].strip()
    if path == TERRABACTER:
        assert proof["target"] == path and proof["record_sha256"] == after_hash
        assert proof["matches_corrected_block"] is True and proof["exact_stock_result"] is None
        result = proof["result"]
        assert result["ncbi_source_id"] == "NCBITaxon:53355"
        assert result["gtdb_id"] == "GTDB:g__Terrabacter"
        assert result["total_genomes"] == result["support_genomes"] == 12
        assert result["majority_fraction"] == 1.0
        assert result["gtdb_lineage"] == (
            "d__Bacteria;p__Actinomycetota;c__Actinomycetes;o__Actinomycetales;"
            "f__Dermatophilaceae;g__Terrabacter"
        )
        assert {key: block[key] for key in result if key not in {"via", "n_alt"}} == {
            key: value for key, value in result.items() if key not in {"via", "n_alt"}
        }
    else:
        assert proof["record"] == path and proof["record_sha256"] == before_hash
        assert proof["assembly"] == {
            "refseq": "GCF_002812725.1",
            "genbank": "GCA_002812725.1",
            "ncbi_taxon": 1070896,
            "strain": "BR1",
            "biosample": "SAMN07351343",
            "bioproject": "PRJNA394223",
        }
        release = [row for row in proof["gtdb_release_history"] if row["release"] == "R220"]
        assert len(release) == 1
        lineage = ";".join(release[0][rank] for rank in ("d", "p", "c", "o", "f", "g", "s"))
        assert block["gtdb_lineage"] == lineage
        assert block["gtdb_id"] == "GTDB:s__Microbacterium_sp002812725"
        assert block["gtdb_taxon"] == "Microbacterium sp002812725"
        assert block["ncbi_source_id"] == "NCBITaxon:1070896"
        assert block["is_reclassified"] is True
        assert not {"majority_fraction", "support_genomes", "total_genomes"}.intersection(block)


def current_record_sha256(root, path, predecessor_hash, *, manifest=None, current=None):
    current = (root / path).read_bytes() if current is None else current
    if path not in TARGETS:
        assert digest(current) == predecessor_hash
        return predecessor_hash
    manifest = yaml.safe_load((root / MANIFEST).read_bytes()) if manifest is None else manifest
    assert manifest["source_baseline"] == BASELINE
    rows = manifest["records"]
    assert len(rows) == len({row["target"] for row in rows})
    assert {row["target"] for row in rows} <= set(TARGETS)
    candidates = [row for row in rows if row["target"] == path]
    if not candidates:
        assert digest(current) == predecessor_hash
        return predecessor_hash
    entry = candidates[0]
    identity = TARGETS[path][0]
    assert entry["target_id"] == identity and entry["scientific_review"] is False
    before_raw = subprocess.check_output(["git", "show", f"{BASELINE}:{path}"], cwd=root)
    assert digest(before_raw) == predecessor_hash == entry["before_sha256"]
    assert digest(current) == entry["after_sha256"]
    before, after = yaml.safe_load(before_raw), yaml.safe_load(current)
    unchanged_science(path, before, after)
    review = yaml.safe_load(artifact(root, entry["diagnostic_review"]))
    validate_review(review)
    assert review["repository"] == "CultureBotAI/CommunityMech"
    assert review["completion"] == "completed" and review["scientific_review"] is False
    assert review["verdict"] == "pass_with_limitations" and review["scope"]["coverage"] == "partial"
    assert review["scope"]["reviewed_target_ids"] == [identity]
    assert len(review["targets"]) == 1
    target = review["targets"][0]
    selector = SELECTOR + "; description GTDB identifier" if path == BR1 else SELECTOR
    assert (target["path"], target["target_id"], target["selector"]) == (path, identity, selector)
    reviewed_input(review, path, entry["after_sha256"])
    evidence = {row["evidence_id"]: row for row in review["evidence"]}
    assert any(
        row["area"] == "grounding"
        and row["outcome"] == "supported"
        and row["target_ids"] == [identity]
        and any(evidence[key]["kind"] == "database" for key in row["evidence_ids"])
        for row in review["assessments"]
    )
    required = [row for row in review["checks"] if row["required"]]
    expected_checks = {
        "schema",
        "strict",
        "gtdb",
        "domain",
        "scalars",
        "history",
        "new-history",
    }
    if path == BR1:
        expected_checks.add("terms")
    assert {row["check_id"] for row in required} == expected_checks
    assert all(row["status"] == "passed" and row["exit_code"] == 0 for row in required)
    binding = entry["application_receipt"]
    assert binding["sha256"] == binding["raw_sha256"]
    reviewed_input(review, binding["raw_path"], binding["raw_sha256"])
    receipt = yaml.safe_load(artifact(root, binding))
    assert receipt["target"] == path and receipt["applied"] is True
    assert receipt["before_sha256"] == predecessor_hash
    assert receipt["after_sha256"] == entry["after_sha256"]
    assert receipt["execution_revision"] == review["source"]["git_revision"]
    for name, expected in receipt["inputs"].items():
        reviewed_input(review, name, expected)
    sidecar = entry["history_sidecar"]
    reviewed_input(review, sidecar["path"], sidecar["sha256"])
    history = yaml.safe_load(artifact(root, sidecar))
    assert history["target"]["path"] == path and history["target"]["kind"] == "record"
    assert history["events"]
    proof = entry["grounding_proof"]
    reviewed_input(review, proof["raw_path"], proof["sha256"])
    value = yaml.safe_load(artifact(root, proof))
    verify_grounding(path, predecessor_hash, entry["after_sha256"], after, value)
    if path == BR1:
        route = entry["native_recomputation"]
        assert route["sha256"] == route["raw_sha256"]
        reviewed_input(review, route["raw_path"], route["sha256"])
        measured = yaml.safe_load(artifact(root, route))
        assert measured["target"] == path and measured["record_sha256"] == entry["after_sha256"]
        assert measured["revision"] == receipt["execution_revision"]
        assert measured["native_result"] is None and measured["curated"] is True
        assert measured["majority_fraction_asserted"] is False
        assert measured["total_genomes_asserted"] is False
        reviewed_input(review, "scripts/gtdb_ground.py", measured["classifier_sha256"])
        reviewed_input(
            review,
            ".temp/br1-source-review-20261115/kg-microbe/data/raw/NCBI2GTDB.tsv.gz",
            measured["crosswalk_sha256"],
        )
    assert artifact(root, entry["review_markdown"]).decode() == render_markdown(review)
    return entry["after_sha256"]
