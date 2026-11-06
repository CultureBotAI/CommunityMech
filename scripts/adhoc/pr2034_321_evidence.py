"""Reproduce source projections and snippet/ontology checks for PR 2034 record 321.

Reads only the current canary checkout and existing ontology caches. Public
author/contact metadata is deliberately excluded from the projected evidence.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json
import re
import subprocess
from pathlib import Path

import yaml
from defusedxml import ElementTree

from communitymech.ontology_adapters import _local_build

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / ".temp/pr2034/321"
TARGET = "data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml"


def pin(p):
    data = p.read_bytes()
    return {
        "path": str(p.relative_to(ROOT)),
        "sha256": hashlib.sha256(data).hexdigest(),
        "bytes": len(data),
    }


def write(name, value):
    p = OUT / name
    with p.open("x") as f:
        json.dump(value, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(json.dumps(pin(p)))


def walk(x, path=""):
    if isinstance(x, dict):
        yield path, x
        for k, v in x.items():
            yield from walk(v, f"{path}.{k}" if path else k)
    elif isinstance(x, list):
        for i, v in enumerate(x):
            yield from walk(v, f"{path}[{i}]")


def main():
    record = yaml.safe_load((ROOT / TARGET).read_text())
    checked_at = dt.datetime.now(dt.timezone.utc).isoformat()
    sources = {
        k: ROOT / v
        for k, v in {
            "PMID:28963201": "references_cache/PMID_28963201.txt",
            "PMID:33398099": "references_cache/PMID_33398099.md",
        }.items()
    }
    # Replay uses the exact retained carrier, and separately reports whole-file
    # match status. It does not turn literal matches into claim support.
    rows = []
    for path, item in walk(record):
        if "snippet" not in item:
            continue
        text = sources[item["reference"]].read_text()
        snip = item["snippet"]

        def normalize(s):
            return re.sub(r"\s+", " ", s).strip()

        rows.append(
            {
                "path": path,
                "reference": item["reference"],
                "snippet": snip,
                "raw": snip in text,
                "strict_whitespace": normalize(snip) in normalize(text),
                "raw_offset": text.find(snip),
            }
        )
    write(
        "snippet-replay.json",
        {
            "checked_at": checked_at,
            "normalization": "whitespace only",
            "input": pin(ROOT / TARGET),
            "sources": [pin(p) for p in sources.values()],
            "rows": rows,
            "counts": {
                "total": len(rows),
                "raw": sum(r["raw"] for r in rows),
                "strict": sum(r["strict_whitespace"] for r in rows),
            },
        },
    )
    terms = {}
    for path, item in walk(record):
        if isinstance(item.get("id"), str) and item["id"].split(":")[0] in (
            "NCBITaxon",
            "ENVO",
            "GO",
            "CHEBI",
        ):
            terms.setdefault((item["id"], item.get("label")), []).append(path)
    authority = []
    adapters = {}
    for (curie, label), paths in terms.items():
        prefix = curie.split(":")[0]
        adapters.setdefault(prefix, _local_build(prefix.lower()))
        adapter = adapters[prefix]
        assert adapter is not None, prefix
        authority.append(
            {
                "id": curie,
                "canonical_label": label,
                "current_label": adapter.label(curie),
                "definition": adapter.definition(curie),
                "metadata": adapter.entity_metadata_map(curie),
                "paths": paths,
            }
        )
    write(
        "ontology-authority.json",
        {
            "checked_at": checked_at,
            "authority": authority,
            "method": "Existing local OAK SQLite builds only; no download or cache mutation requested.",
        },
    )
    p = OUT / "sources"
    meta = json.loads((p / "biomodels-metadata.json").read_text())
    model = {
        k: meta.get(k)
        for k in [
            "name",
            "description",
            "format",
            "files",
            "firstPublished",
            "submissionId",
            "modellingApproach",
            "curationStatus",
            "modelTags",
            "modelLevelAnnotations",
        ]
    }
    model["revisions"] = [
        {k: r.get(k) for k in ["version", "submitted", "comment"]}
        for r in meta["history"]["revisions"]
    ]
    models = []
    for name in ["authors-model.xml", "biomodels-model.xml"]:
        doc = ElementTree.parse(p / name).getroot()
        m = next(x for x in doc if x.tag.endswith("}model"))
        models.append(
            dict(
                **pin(p / name),
                attributes=m.attrib,
                counts={
                    tag: sum(x.tag.endswith("}" + tag) for x in m.iter())
                    for tag in ["species", "reaction", "geneProduct"]
                },
            )
        )
    assembly = json.loads((p / "assembly.json").read_text())["result"]["1163481"]
    biosample = ElementTree.parse(p / "biosample.xml").getroot()
    attributes = {
        x.get("attribute_name"): x.text
        for x in biosample.iter("Attribute")
        if x.get("attribute_name")
        in ["strain", "isolation_source", "sample_type", "collection_date", "geo_loc_name"]
    }
    sample_ids = [(x.attrib, x.text) for x in biosample.iter("Id")]
    write(
        "primary-artifact-projection.json",
        {
            "checked_at": checked_at,
            "biomodels": model,
            "models": models,
            "authors_mapping": [
                line
                for line in (p / "authors-species.tsv").read_text().splitlines()
                if "156_03182016" in line
            ],
            "assembly": {
                k: assembly.get(k)
                for k in [
                    "assemblyaccession",
                    "assemblyname",
                    "taxid",
                    "organism",
                    "wgs",
                    "biosampleaccn",
                    "biosource",
                    "asmupdatedate",
                    "anomalouslist",
                    "exclfromrefseq",
                    "propertylist",
                    "synonym",
                    "meta",
                ]
            },
            "biosample": {"ids": sample_ids, "attributes": attributes},
            "source_pins": [pin(x) for x in sorted(p.iterdir())],
        },
    )
    baseline = "a4611c913c8da9619673df63a0c2cce3aa206a83"
    old = yaml.safe_load(
        subprocess.check_output(["git", "show", f"{baseline}:{TARGET}"], cwd=ROOT, text=True)
    )
    changed = []

    def delta(a, b, path=""):
        if type(a) is not type(b):
            changed.append(path)
            return
        if isinstance(a, dict):
            for k in sorted(set(a) | set(b)):
                key = f"{path}.{k}" if path else k
                if k not in a or k not in b:
                    changed.append(key)
                else:
                    delta(a[k], b[k], key)
        elif isinstance(a, list):
            for i in range(max(len(a), len(b))):
                key = f"{path}[{i}]"
                if i >= len(a) or i >= len(b):
                    changed.append(key)
                else:
                    delta(a[i], b[i], key)
        elif a != b:
            changed.append(path)

    delta(old, record)
    write(
        "target-change-proof.json",
        {
            "baseline": baseline,
            "current": pin(ROOT / TARGET),
            "changed_field_paths": changed,
            "diff": subprocess.check_output(
                ["git", "diff", baseline, "HEAD", "--", TARGET], cwd=ROOT, text=True
            ),
        },
    )
    manifest = ROOT / ".temp/pr2034/273/network-corpus-inputs.json"
    write(
        "network-reuse.json",
        {
            "manifest": pin(manifest),
            "inventory": json.loads(manifest.read_text()),
            "results": [
                json.loads((ROOT / f".temp/pr2034/273/{n}.json").read_text())
                for n in ["audit-network", "check-network-quality"]
            ],
        },
    )


if __name__ == "__main__":
    assert Path.cwd() == ROOT
    main()
