"""Replay fresh abstract excerpts, authority labels, and link scope for record 175."""

from __future__ import annotations

import json
import unicodedata

import yaml
from defusedxml import ElementTree
from pr2053_175_audit import COMMON, ROOT, SCRATCH, TARGET, now, sha, write

from communitymech.network.auditor import NetworkIntegrityAuditor
from communitymech.ontology_adapters import ontology_adapter


def norm(text):
    return " ".join(unicodedata.normalize("NFKC", text).split())


def walk(value, path=""):
    if isinstance(value, dict):
        yield path, value
        for key, child in value.items():
            yield from walk(child, f"{path}.{key}" if path else key)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from walk(child, f"{path}[{index}]")


def main():
    record = yaml.safe_load((ROOT / TARGET).read_text())
    common = yaml.safe_load((ROOT / COMMON).read_text())
    pubmed = ElementTree.fromstring((SCRATCH / "pubmed-175.xml").read_bytes())
    abstracts, bibliography = {}, []
    for article in pubmed.findall("PubmedArticle"):
        pmid = article.findtext(".//MedlineCitation/PMID")
        abstracts["PMID:" + pmid] = " ".join("".join(x.itertext()) for x in article.findall(".//AbstractText"))
        bibliography.append({"pmid": pmid,
            "title": "".join(article.find(".//ArticleTitle").itertext()),
            "dois": [x.text for x in article.findall(".//ArticleId") if x.get("IdType") == "doi"]})
    assert set(abstracts) == {"PMID:17695929", "PMID:18725730"}
    snippets, terms = [], []
    for path, node in walk(record):
        if "snippet" in node:
            snippets.append({"path": path + ".snippet", "reference": node["reference"],
                "nfkc_whitespace_match": norm(node["snippet"]) in norm(abstracts[node["reference"]])})
        if set(node) >= {"id", "label"} and ":" in node["id"]:
            adapter = ontology_adapter(node["id"].split(":", 1)[0])
            assert adapter is not None, node["id"]
            label = adapter.label(node["id"])
            terms.append({"path": path, "id": node["id"], "record_label": node["label"],
                "authority_label": label, "exact_label_match": label == node["label"]})
    issues = NetworkIntegrityAuditor().audit_community(ROOT / TARGET)
    assert len(snippets) == 28 and all(x["nfkc_whitespace_match"] for x in snippets)
    assert all(x["exact_label_match"] for x in terms) and not issues
    member = record["taxonomy"][1]
    assert member["common_taxon"] == common["id"] == "CommunityMech:taxon:000002"
    assert member["taxon_term"]["term"] == common["taxon_term"]["term"]
    tax = ElementTree.fromstring((SCRATCH / "taxonomy-175.xml").read_bytes())
    taxa = [{"id": t.findtext("TaxId"), "name": t.findtext("ScientificName"),
             "rank": t.findtext("Rank"), "parent": t.findtext("ParentTaxId"),
             "type_material": [n.findtext("DispName") for n in t.findall("OtherNames/Name")
                               if n.findtext("ClassCDE") == "type material"]} for t in tax.findall("Taxon")]
    catalog = json.loads((SCRATCH / "imodulon-catalog.json").read_text())
    write("support-final.json", {
        "observed_at": now(), "record_sha256": sha((ROOT / TARGET).read_bytes()),
        "common_taxon_sha256": sha((ROOT / COMMON).read_bytes()), "bibliography": bibliography,
        "snippets": snippets, "terms": terms, "taxonomy_authority": taxa,
        "native_target_network": {"issues": issues, "integrity": "COMPLETE"},
        "common_taxon_link": {"resolved": True, "same_species_term": True,
            "scope": "Identity link only. Reusable genes, other-community DIET experiments and genome examples are not focal cellulose-MFC mechanism evidence."},
        "imodulon_organisms": [x["name"] for x in catalog],
        "imodulon_focal_match": any("Geobacter" in x["name"] or "cellulolyticum" in x["name"] for x in catalog),
        "metrics": {"completeness": 85, "P1": 0, "P2": 2, "P3": 2, "P4": 0,
                    "nodes": 3, "arrows": 1, "node_evidence": 8,
                    "validation_quality_raw": 111, "validation_quality_capped": 100},
        "qualification": "Exact lexical matching and graph connectivity do not certify interpretation. The CMC derivative mismatch is semantic despite correct encoded ID-label correspondence.",
    })
    print(json.dumps({"snippets": len(snippets), "terms": len(terms), "common_link": "valid"}))


if __name__ == "__main__":
    main()
