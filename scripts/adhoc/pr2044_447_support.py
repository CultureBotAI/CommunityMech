"""Read-only source qualification and exact local replay for PR 2044 record 447."""

from __future__ import annotations

import json
import re
import unicodedata

import yaml
from defusedxml import ElementTree
from pr2044_447_audit import ROOT, SCRATCH, TARGET, now, run, sha, write

from communitymech.network.auditor import NetworkIntegrityAuditor
from communitymech.ontology_adapters import ontology_adapter


def norm(text):
    return " ".join(unicodedata.normalize("NFKC", text).split())


def hyphens(text):
    return re.sub("[‐‑‒–—−]", "-", norm(text))


def walk(value, path=""):
    if isinstance(value, dict):
        yield path, value
        for key, child in value.items():
            yield from walk(child, f"{path}.{key}" if path else key)
    elif isinstance(value, list):
        for i, child in enumerate(value):
            yield from walk(child, f"{path}[{i}]")


def main():
    record = yaml.safe_load((ROOT / TARGET).read_text())
    pm = ElementTree.fromstring((SCRATCH / "pubmed.xml").read_bytes())
    abstract = " ".join("".join(x.itertext()) for x in pm.findall(".//AbstractText"))
    pmid = pm.findtext(".//MedlineCitation/PMID")
    dois = [x.text for x in pm.findall(".//ArticleId") if x.get("IdType") == "doi"]
    assert pmid == "42323145" and "10.1016/j.biortech.2026.135206" in dois
    snippets, terms = [], []
    for path, node in walk(record):
        if "snippet" in node:
            snippet = node["snippet"]
            if norm(snippet) in norm(abstract):
                category = "strict_nfkc_whitespace_abstract_match"
            elif hyphens(snippet) in hyphens(abstract):
                category = "hyphen_glyph_equivalent_only"
            elif snippet == f"PMID: {pmid}" or snippet in [f"DOI: {doi}" for doi in dois]:
                category = "bibliographic_metadata_identifier"
            else:
                category = "unmatched"
            snippets.append({"path": path + ".snippet", "category": category})
        if set(node) >= {"id", "label"} and ":" in node["id"]:
            adapter = ontology_adapter(node["id"].split(":", 1)[0])
            assert adapter is not None, node["id"]
            label = adapter.label(node["id"])
            terms.append(
                {
                    "path": path,
                    "id": node["id"],
                    "record_label": node["label"],
                    "authority_label": label,
                    "exact_label_match": label == node["label"],
                }
            )
    taxonomy = ElementTree.fromstring((SCRATCH / "ncbi-taxonomy.xml").read_bytes())
    ranks = [
        {
            "id": "NCBITaxon:" + x.findtext("TaxId"),
            "name": x.findtext("ScientificName"),
            "rank": x.findtext("Rank"),
        }
        for x in taxonomy.findall("Taxon")
    ]
    issues = NetworkIntegrityAuditor().audit_community(ROOT / TARGET)
    assert len(snippets) == 13
    assert not any(s["category"] == "unmatched" for s in snippets)
    assert all(t["exact_label_match"] for t in terms)
    assert not issues
    write(
        "support-final.json",
        {
            "observed_at": now(),
            "record_sha256": sha((ROOT / TARGET).read_bytes()),
            "pubmed_sha256": sha((SCRATCH / "pubmed.xml").read_bytes()),
            "snippet_categories": {
                k: sum(s["category"] == k for s in snippets)
                for k in sorted({s["category"] for s in snippets})
            },
            "snippets": snippets,
            "terms": terms,
            "fresh_ncbi_ranks": ranks,
            "native_target_network": {"issues": issues, "integrity": "COMPLETE"},
            "metrics": {
                "completeness": 70,
                "P1": 0,
                "P2": 1,
                "P3": 1,
                "P4": 0,
                "node_count": 1,
                "node_evidence_count": 2,
                "validation_quality_raw": 123,
                "validation_quality_capped": 100,
            },
            "interpretation": "Native connectivity is structural and does not validate Kuenenia cross-feeding participation. The new evidence supports temporal succession; model-inferred complementary auxotrophies are explicitly within the multispecies Brocadia assemblage.",
        },
    )
    epmc = json.loads((SCRATCH / "epmc.json").read_text())["resultList"]["result"][0]
    crossref = json.loads((SCRATCH / "crossref.json").read_text())["message"]
    oa = json.loads((SCRATCH / "openalex.json").read_text())
    catalog = json.loads((SCRATCH / "imodulon-catalog.json").read_text())
    article = ElementTree.fromstring((SCRATCH / "article-api.xml").read_bytes())
    write(
        "source-qualification-final.json",
        {
            "observed_at": now(),
            "pubmed_pmid": pmid,
            "pubmed_dois": dois,
            "pubmed_title": pm.findtext(".//ArticleTitle"),
            "crossref_doi": crossref.get("DOI"),
            "crossref_title": crossref.get("title"),
            "epmc_is_open_access": epmc.get("isOpenAccess"),
            "epmc_pmcid": epmc.get("pmcid"),
            "epmc_full_text_urls": epmc.get("fullTextUrlList"),
            "openalex_open_access": oa.get("open_access"),
            "openalex_locations": oa.get("locations"),
            "elsevier_top_level_tags": [x.tag for x in article],
            "elsevier_article_body_present": any(
                x.tag.split("}")[-1] == "originalText" for x in article.iter()
            ),
            "imodulon_catalog_organisms": [x["name"] for x in catalog],
            "imodulon_exact_target_match": any(
                re.search("Brocadia|Kuenenia", x["name"], re.I) for x in catalog
            ),
            "manual_access_classification": {
                "doi.html": "HTTP 200 redirect shell only; no full article inspected.",
                "publisher.html": "HTTP 403 access-error page; no full article inspected.",
                "article-api.xml": "HTTP 200 bibliographic coredata only; no main Methods/Results, figures or SI.",
                "search": "Exact DOI and title searched with web tool; publisher indexed Methods fragment is a follow-up lead only. Direct publisher web open returned HTTP 403. No indexed reactor values are accepted as inspected full-source facts. This is bounded discovery, not a global absence claim.",
            },
            "source_scope": "Complete primary abstract and bibliographic metadata inspected. Full main Methods/Results, figures, SI and model inputs remain unavailable through these inspected routes; partial review retained.",
        },
    )
    run(
        "legacy-finding-search-final",
        [
            "rg",
            "--no-ignore",
            "--hidden",
            "-n",
            "F-P2-000447-01|F-C-COHORT-14-01",
            "history",
            "reports",
            "reviews",
        ],
    )
    print(
        json.dumps(
            {
                "snippets": len(snippets),
                "term_occurrences": len(terms),
                "unique_terms": len({x["id"] for x in terms}),
                "network_issues": len(issues),
            }
        )
    )


if __name__ == "__main__":
    main()
