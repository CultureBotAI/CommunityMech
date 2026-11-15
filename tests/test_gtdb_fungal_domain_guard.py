"""Real native mixed staging with controlled authority, #2904, 2026-11-15.

Synthetic table/adapter tests are not a scientific or actual M5 measurement.
The unchanged resolver, classifier, CLI writer and validated apply all execute.
"""

import copy
import gzip
import importlib.util
import json
import sqlite3
import subprocess
from pathlib import Path

import pytest
import scoped_gtdb_fungal_successor as strict
import yaml

ROOT = Path(__file__).resolve().parents[1]
BASE = "68699871415fda3c9eebf20382a315f9f3c7b17a"
TARGET = "kb/communities/PPCP_Wastewater_Sphingopyxis_Ochrobactrum_Apiotrichum_SMC.yaml"


def load(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / f"scripts/adhoc/{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def table_row(number, genus, species, output_genus, count=1):
    cells = [""] * 19
    cells[0], cells[2], cells[3] = str(number), str(count), "1.0"
    cells[4:11] = [
        "Bacteria",
        "Pseudomonadota",
        "Alphaproteobacteria",
        "Testales",
        "Testaceae",
        genus,
        species,
    ]
    cells[12:19] = [
        "Bacteria",
        "Pseudomonadota",
        "Alphaproteobacteria",
        "Testales",
        "Testaceae",
        output_genus,
        species,
    ]
    return "\t".join(cells)


@pytest.fixture
def case(tmp_path, monkeypatch):
    monkeypatch.syspath_prepend(str(ROOT / "scripts/adhoc"))
    engine = load("gtdb_fungal_batch_curation_20261115")
    native = engine.native_module()
    root = tmp_path / "repo"
    state = root / ".temp/unit"
    state.mkdir(parents=True)
    for name in (*engine.REQUIRED_INPUTS, engine.domain_contract.ENGINE):
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes((ROOT / name).read_bytes())
    original = subprocess.check_output(["git", "show", f"{BASE}:{TARGET}"], cwd=ROOT)
    before = yaml.safe_load(original)
    target = root / TARGET
    target.parent.mkdir(parents=True)
    target.write_bytes(original)
    table = state / "kg-microbe/data/raw/NCBI2GTDB.tsv.gz"
    table.parent.mkdir(parents=True)
    lines = [
        "\t".join(f"column_{i}" for i in range(19)),
        table_row(500, "Sphingopyxis", "Sphingopyxis alba", "Sphingopyxis", 79),
    ]
    lines.extend(
        table_row(i, "Ochrobactrum", f"Ochrobactrum {species}", output)
        for i, species, output in [
            (501, "alba", "Ochrobactrum_A"),
            (502, "beta", "Ochrobactrum_B"),
            (503, "gamma", "Ochrobactrum"),
        ]
    )
    table.write_bytes(gzip.compress(("\n".join(lines) + "\n").encode()))
    rows = native.collect_rows(
        table,
        {"165697", "528", "105983"},
        {"sphingopyxis", "ochrobactrum", "apiotrichum"},
        {"sphingopyxis", "ochrobactrum", "apiotrichum"},
    )
    occurrences = []
    for index, member in enumerate(before["taxonomy"]):
        descriptor = member["taxon_term"]
        term = descriptor["term"]
        result = native.resolve_target(term["id"].split(":")[1], term["label"], *rows)
        status = (
            {"status": "NO_GTDB_EQUIVALENT", "candidates": []}
            if result is None
            else (
                {"status": "AMBIGUOUS", "candidates": result["gtdb_options"]}
                if result.get("ambiguous")
                else {"status": "NOT_ATTEMPTED", "candidates": []}
            )
        )
        occurrences.append(
            {
                "taxonomy_index": index,
                "term": copy.deepcopy(term),
                "strain_name": member["strain_designation"]["strain_name"],
                "existing_descriptor": copy.deepcopy(descriptor),
                "native_result": result,
                "classify_status": status,
                "manual_curated_reason": None,
                "manual_withheld_reason": None,
            }
        )
    row = {
        "record": TARGET,
        "record_id": before["id"],
        "before_sha256": engine.sha(original),
        "occurrences": occurrences,
    }
    identity_rows = [
        {
            "subject": "NCBITaxon:105983",
            "predicate": "ncbitaxon:has_rank",
            "value": None,
            "object": "NCBITaxon:genus",
        },
        {
            "subject": "NCBITaxon:105983",
            "predicate": "rdfs:label",
            "value": "Apiotrichum",
            "object": None,
        },
        {
            "subject": "NCBITaxon:105983",
            "predicate": "rdfs:subClassOf",
            "value": None,
            "object": "NCBITaxon:4751",
        },
    ]
    occurrences[2]["ncbi_identity_rows"] = identity_rows
    source = state / "source.json"
    source.write_text(
        json.dumps(
            {
                "records": [row],
                "inputs_unchanged": True,
                "canonical_writes": False,
                "inputs": {
                    TARGET: engine.sha(original),
                    str(table.relative_to(root)): engine.sha(table.read_bytes()),
                },
            }
        )
    )
    database = state / "oaklib/ncbitaxon.db"
    database.parent.mkdir()
    with sqlite3.connect(database) as connection:
        connection.execute("CREATE TABLE statements (subject,predicate,value,object)")
        connection.executemany(
            "INSERT INTO statements VALUES (:subject,:predicate,:value,:object)", identity_rows
        )

    class Adapter:
        ancestors_result = ["NCBITaxon:4751", "NCBITaxon:2759", "NCBITaxon:1"]

        def ancestors(self, curies, predicates):
            assert predicates == ["rdfs:subClassOf"]
            return self.ancestors_result if curies == ["NCBITaxon:105983"] else ["NCBITaxon:2"]

    adapter = Adapter()
    import oaklib

    def constructor(selector):
        assert selector == f"sqlite:{database}"
        return adapter

    monkeypatch.setattr(oaklib, "get_adapter", constructor)
    monkeypatch.setattr(engine, "ROOT", root)
    monkeypatch.setattr(engine, "STATE", root / ".temp")
    monkeypatch.setattr(engine, "DATABASE", database)
    monkeypatch.setattr(engine, "__file__", str(root / engine.domain_contract.ENGINE))
    monkeypatch.setattr(engine, "head", lambda: "f" * 40)
    monkeypatch.setattr(engine, "TABLE_SHA", engine.sha(table.read_bytes()))
    monkeypatch.setattr(strict, "TABLE_SHA", engine.sha(table.read_bytes()))
    return {
        "engine": engine,
        "native": native,
        "root": root,
        "state": state,
        "target": target,
        "before": before,
        "original": original,
        "source": source,
        "row": row,
        "database": database,
        "adapter": adapter,
        "table": table,
    }


def stage(case, name="stage"):
    engine, root = case["engine"], case["root"]
    return engine.stage(
        str(case["source"].relative_to(root)),
        engine.sha(case["source"].read_bytes()),
        case["row"]["record_id"],
        f".temp/unit/{name}",
        "f" * 40,
        "ground-and-status",
    )


def apply(case, pins, output="applied", plan=False):
    return case["engine"].apply(
        ".temp/unit/stage",
        f".temp/unit/{output}",
        pins["candidate_sha256"],
        pins["receipt_sha256"],
        "f" * 40,
        plan=plan,
    )


def projection(case):
    directory = case["state"] / "stage"
    after = yaml.safe_load((directory / case["target"].name).read_bytes())
    domain = json.loads((directory / "domain-observations.json").read_bytes())
    source = {**case["row"], "domain_observation": domain}
    return after, source


def test_actual_native_stage_apply_persistence_and_old_refusal(case):
    pins = stage(case)
    after, source = projection(case)
    strict.verify_projection(case["before"], after, source, [0, 1, 2])
    old = load("gtdb_batch_curation_20261115")
    with pytest.raises(ValueError, match="UNRESOLVED"):
        old.verify_operations(case["row"], ["--apply", "--apply-status"])
    assert apply(case, pins, plan=True)["planned"]
    assert case["target"].read_bytes() == case["original"]
    result = apply(case, pins)
    assert result["applied"] and result["contract"] == case["engine"].domain_contract.CONTRACT
    assert (
        case["target"].read_bytes() == (case["state"] / "stage" / case["target"].name).read_bytes()
    )
    receipt = case["state"] / "applied/receipt.json"
    assert json.loads(receipt.read_bytes()) == result
    assert after["taxonomy"][2]["taxon_term"]["gtdb_grounding_status"] == "NO_GTDB_EQUIVALENT"
    assert len(after["curation_history"]) == len(case["before"]["curation_history"]) + 2


@pytest.mark.parametrize(
    "ancestors",
    [
        [],
        ["NCBITaxon:2759"],
        ["NCBITaxon:4751"],
        ["NCBITaxon:2"],
        ["NCBITaxon:10239"],
        ["NCBITaxon:4751", "NCBITaxon:2759", "NCBITaxon:2"],
    ],
)
def test_null_or_unresolved_ancestry_never_proves_fungi(case, ancestors):
    stage(case, "positive-before")
    old = case["adapter"].ancestors_result
    case["adapter"].ancestors_result = ancestors
    with pytest.raises(ValueError, match="classifier|Fungi"):
        stage(case, "refused")
    assert not (case["state"] / "refused/receipt.json").exists()
    assert case["target"].read_bytes() == case["original"]
    case["adapter"].ancestors_result = old
    stage(case, "restored")


@pytest.mark.parametrize(
    "mutation", ["manual", "withheld", "block", "status", "candidates", "null_only", "status_only"]
)
def test_source_contract_refuses_then_restores(case, mutation):
    engine, row = case["engine"], copy.deepcopy(case["row"])
    flags = ["--apply", "--apply-status"]
    engine.verify_operations(row, flags)
    item = row["occurrences"][2]
    if mutation == "manual":
        item["manual_curated_reason"] = "preserve"
    elif mutation == "withheld":
        item["manual_withheld_reason"] = "preserve"
    elif mutation == "block":
        item["existing_descriptor"]["gtdb_classification"] = {}
    elif mutation == "status":
        item["classify_status"]["status"] = "UNRESOLVED"
    elif mutation == "candidates":
        item["classify_status"]["candidates"] = ["GTDB:s__invented"]
    elif mutation == "null_only":
        row["occurrences"] = [item]
    else:
        flags = ["--apply-status"]
    with pytest.raises(ValueError):
        engine.verify_operations(row, flags)
    engine.verify_operations(case["row"], ["--apply", "--apply-status"])


@pytest.mark.parametrize("mutation", ["stock", "biology", "history", "alternatives", "domain"])
def test_projection_rejects_changed_science_or_forged_domain_then_restores(case, mutation):
    stage(case)
    after, source = projection(case)
    strict.verify_projection(case["before"], after, source, [0, 1, 2])
    altered, forged = copy.deepcopy(after), copy.deepcopy(source)
    if mutation == "stock":
        altered["taxonomy"][2]["strain_designation"]["strain_name"] = "other"
    elif mutation == "biology":
        altered["description"] += " invented"
    elif mutation == "history":
        altered["curation_history"][0]["changes"] += " rewritten"
    elif mutation == "alternatives":
        altered["taxonomy"][1]["taxon_term"]["gtdb_candidates"].pop()
    else:
        forged["domain_observation"]["observations"][0]["ancestor_ids"].remove("NCBITaxon:4751")
    with pytest.raises((AssertionError, ValueError)):
        strict.verify_projection(case["before"], altered, forged, [0, 1, 2])
    strict.verify_projection(case["before"], after, source, [0, 1, 2])


@pytest.mark.parametrize("change", ["table", "source", "helper", "domain", "database"])
def test_post_validation_input_change_prevents_apply(case, monkeypatch, change):
    pins = stage(case)
    engine = case["engine"]
    original_writer = engine.write_validated_community
    apply(case, pins, plan=True)
    target = {
        "table": case["table"],
        "source": case["source"],
        "helper": case["root"] / engine.domain_contract.HELPER,
        "domain": case["state"] / "stage/domain-observations.json",
        "database": case["database"],
    }[change]
    saved = target.read_bytes()
    saved_stat = target.stat()

    def changed(doc, path):
        original_writer(doc, path)
        target.write_bytes(saved + b"\nchanged")

    monkeypatch.setattr(engine, "write_validated_community", changed)
    with pytest.raises(ValueError, match="changed"):
        apply(case, pins, output="refused")
    assert case["target"].read_bytes() == case["original"]
    assert not (case["state"] / "refused/receipt.json").exists()
    target.write_bytes(saved)
    engine.os.utime(target, ns=(saved_stat.st_atime_ns, saved_stat.st_mtime_ns))
    monkeypatch.setattr(engine, "write_validated_community", original_writer)
    assert apply(case, pins, output="restored")["applied"]


@pytest.mark.parametrize("failure", ["missing", "construction", "query", "identity"])
def test_authority_failure_after_success_cannot_borrow_cached_domain(case, monkeypatch, failure):
    import oaklib

    stage(case, "positive-before")
    original_constructor = oaklib.get_adapter
    original_ancestors = case["adapter"].ancestors
    if failure in {"missing", "construction"}:

        def unavailable(*args):
            if failure == "construction":
                raise RuntimeError("controlled authority construction failure")
            return None

        monkeypatch.setattr(oaklib, "get_adapter", unavailable)
    elif failure == "query":

        def unavailable(*args, **kwargs):
            raise RuntimeError("controlled ancestor query failure")

        monkeypatch.setattr(case["adapter"], "ancestors", unavailable)
    else:
        with sqlite3.connect(case["database"]) as connection:
            connection.execute(
                "UPDATE statements SET value='different' WHERE predicate='rdfs:label'"
            )
    with pytest.raises(ValueError, match="adapter|classifier|identity"):
        stage(case, "refused")
    assert not (case["state"] / "refused/receipt.json").exists()
    assert case["target"].read_bytes() == case["original"]
    monkeypatch.setattr(oaklib, "get_adapter", original_constructor)
    monkeypatch.setattr(case["adapter"], "ancestors", original_ancestors)
    if failure == "identity":
        with sqlite3.connect(case["database"]) as connection:
            connection.execute(
                "UPDATE statements SET value='Apiotrichum' WHERE predicate='rdfs:label'"
            )
    stage(case, "restored")


@pytest.mark.parametrize("rank", [None, "", "NCBITaxon:not_a_rank"])
def test_matching_malformed_rank_refuses_native_stage_then_restores(case, rank):
    """#2907: agreeing source/authority values still require a recognized rank."""
    stage(case, "positive-before")
    source_bytes = case["source"].read_bytes()
    source = json.loads(source_bytes)
    rank_row = source["records"][0]["occurrences"][2]["ncbi_identity_rows"][0]
    assert rank_row["predicate"] == "ncbitaxon:has_rank"
    assert rank_row["object"] == "NCBITaxon:genus"
    rank_row["object"] = rank
    case["source"].write_text(json.dumps(source))
    with sqlite3.connect(case["database"]) as connection:
        connection.execute(
            "UPDATE statements SET object=? WHERE predicate='ncbitaxon:has_rank'", (rank,)
        )
        assert connection.execute(
            "SELECT object FROM statements WHERE predicate='ncbitaxon:has_rank'"
        ).fetchall() == [(rank,)]
    refusal = None
    try:
        stage(case, "refused")
    except ValueError as error:
        refusal = str(error)
    finally:
        case["source"].write_bytes(source_bytes)
        with sqlite3.connect(case["database"]) as connection:
            connection.execute(
                "UPDATE statements SET object='NCBITaxon:genus' "
                "WHERE predicate='ncbitaxon:has_rank'"
            )
        restored = stage(case, "restored")
        assert (case["state"] / "restored/receipt.json").is_file()
        assert restored["candidate_sha256"]
    assert refusal is not None, "malformed matching rank was admitted by native stage"
    assert "recognized NCBI rank" in refusal
    assert not (case["state"] / "refused/receipt.json").exists()
    assert case["target"].read_bytes() == case["original"]


@pytest.mark.parametrize("mutation", ["contract", "operations", "domain", "inputs"])
def test_rehashed_stage_receipt_cannot_change_the_reviewed_contract(case, mutation):
    pins = stage(case)
    receipt_path = case["state"] / "stage/receipt.json"
    original = receipt_path.read_bytes()
    forged = json.loads(original)
    apply(case, pins, plan=True)
    if mutation == "contract":
        forged["contract"] = "other"
    elif mutation == "operations":
        forged["native_operations"] = ["--apply-status"]
        forged["exit_codes"] = [0]
    elif mutation == "domain":
        forged["domain_proof"]["sha256"] = "0" * 64
    else:
        forged["inputs"].pop(case["engine"].domain_contract.HELPER)
    raw = (json.dumps(forged) + "\n").encode()
    receipt_path.write_bytes(raw)
    altered = {**pins, "receipt_sha256": case["engine"].sha(raw)}
    with pytest.raises(ValueError):
        apply(case, altered, output="refused")
    assert not (case["state"] / "refused/receipt.json").exists()
    assert case["target"].read_bytes() == case["original"]
    receipt_path.write_bytes(original)
    assert apply(case, pins, output="restored")["applied"]


@pytest.mark.parametrize(
    "mutation", ["version", "operations", "raw_link", "identity", "ancestry", "helper"]
)
def test_builder_and_export_bind_actual_domain_bytes_then_restore(case, monkeypatch, mutation):
    pins = stage(case)
    applied = apply(case, pins)
    builder = load("build_gtdb_fungal_diagnostic_20261115")
    exporter = load("export_gtdb_fungal_evidence_20261115")
    monkeypatch.setattr(exporter.base, "ROOT", case["root"])
    monkeypatch.setattr(exporter.base.audit, "ROOT", case["root"])
    engine = case["engine"]
    receipt = json.loads((case["state"] / "stage/receipt.json").read_bytes())
    captured = {}

    def read(name, expected):
        return engine.capture(captured, name, expected)

    item, document = builder.verify_domain_chain(case["row"], receipt, applied, read)
    source = {
        **case["row"],
        "contract": engine.domain_contract.CONTRACT,
        "domain_proof": item,
        "domain_observation": document,
    }
    proof = {
        "before_sha256": engine.sha(case["original"]),
        "contract": engine.domain_contract.CONTRACT,
        "domain_observation": {**item, "raw_path": item["path"], "raw_sha256": item["sha256"]},
    }
    for name in (
        engine.domain_contract.ENGINE,
        engine.domain_contract.HELPER,
        engine.domain_contract.DOMAIN,
        engine.domain_contract.ADAPTER,
    ):
        engine.capture(captured, name)
    review = {
        "source": {
            "inputs": [
                {"path": str(path.relative_to(case["root"])), "sha256": engine.sha(raw)}
                for path, raw in captured.items()
            ]
        }
    }
    exporter.verify_domain_export(review, captured, proof, applied, source)
    strict.verify_domain_artifact(
        strict.Artifacts(case["root"]), review, proof, applied, source, proof["before_sha256"]
    )
    bad_applied, bad_receipt, bad_source = copy.deepcopy((applied, receipt, source))
    if mutation == "version":
        bad_applied["contract"] = "old-contract"
    elif mutation == "operations":
        bad_applied["native_operations"] = ["--apply-status"]
    elif mutation == "raw_link":
        bad_applied["domain_proof"]["sha256"] = "0" * 64
    elif mutation == "helper":
        bad_applied["inputs"][engine.domain_contract.HELPER] = "0" * 64
    else:
        # Mutate and rehash every transport link: semantic authority checks must
        # still refuse a consistently linked but invalid observation.
        bad_document = copy.deepcopy(document)
        observation = bad_document["observations"][0]
        if mutation == "identity":
            observation["term"]["id"] = "NCBITaxon:2"
        else:
            observation["ancestor_ids"].remove("NCBITaxon:4751")
        raw = (json.dumps(bad_document) + "\n").encode()
        location = case["root"] / item["path"]
        location.write_bytes(raw)
        captured[location] = raw
        for row in review["source"]["inputs"]:
            if row["path"] == item["path"]:
                row["sha256"] = engine.sha(raw)
        for value in (bad_applied, bad_receipt, bad_source):
            value["domain_proof"]["sha256"] = engine.sha(raw)
        bad_source["domain_observation"] = bad_document
    bad_proof = copy.deepcopy(proof)
    if mutation in {"identity", "ancestry"}:
        bad_proof["domain_observation"].update(sha256=engine.sha(raw), raw_sha256=engine.sha(raw))
    with pytest.raises(ValueError):
        builder.verify_domain_chain(case["row"], bad_receipt, bad_applied, read)
    with pytest.raises(ValueError):
        exporter.verify_domain_export(review, captured, proof, bad_applied, bad_source)
    with pytest.raises((ValueError, AssertionError)):
        strict.verify_domain_artifact(
            strict.Artifacts(case["root"]),
            review,
            bad_proof,
            bad_applied,
            bad_source,
            proof["before_sha256"],
        )
    location = case["root"] / item["path"]
    original_raw = (json.dumps(document, indent=2) + "\n").encode()
    location.write_bytes(original_raw)
    captured[location] = original_raw
    for row in review["source"]["inputs"]:
        if row["path"] == item["path"]:
            row["sha256"] = engine.sha(original_raw)
    builder.verify_domain_chain(case["row"], receipt, applied, read)
    exporter.verify_domain_export(review, captured, proof, applied, source)
    strict.verify_domain_artifact(
        strict.Artifacts(case["root"]), review, proof, applied, source, proof["before_sha256"]
    )
