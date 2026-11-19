# Explicit supplementary sources

`catalog.json` binds PMID:36472419, published asset
`msystems.00951-22-s0006.docx`, and its deterministic Table S1 projection by
SHA256. The normal reference configuration selects this catalog. Only assertions
with an explicit `source_locator` use it; all other assertions retain the
article route. The validator verifies the parent, asset, version, file hashes,
replayed projection and table/row/cell before comparing the quotation. Missing
or invalid selected sources fail without article fallback.

The catalog is public metadata. The DOCX under `assets/` and projection under
`extractions/` are local, gitignored scientific inputs. They must be provisioned
before validating the three Switchgrass supplement assertions. This directory
does not mix supplementary content into the committed article cache. The
catalog's presence alone does not prove those inputs are available.

The accepted consumer preparations retain the exact source bytes:

| Host | Preparation directory under `.temp/supplement-adoption-1996-20261115/` | `preparation.json` SHA256 |
| --- | --- | --- |
| Local | `switchgrass-prepared-001` | `32e59f36484643038eeb109c9f756e6fe83e788d251b15a05389b6a4ad561eca` |
| M5 | `switchgrass-prepared-m5-001` | `54ffaa776d7687063c762357197f0e59add341fd8c86e6967e60398f13d18da4` |

From the checkout root, use the installed pinned environment and a new private
receipt directory. This M5 example first checks the complete plan:

```bash
.venv/bin/python scripts/adhoc/provision_switchgrass_reference_source_20261115.py \
  --prepared .temp/supplement-adoption-1996-20261115/switchgrass-prepared-m5-001 \
  --preparation-sha256 54ffaa776d7687063c762357197f0e59add341fd8c86e6967e60398f13d18da4 \
  --output .temp/supplement-adoption-1996-20261115/normal-source-install-m5-001 \
  --plan
```

Run the same command without `--plan` to provision. Verify the saved receipt
and all three destination hashes. The helper accepts an existing destination
only if its bytes already match, and refuses to overwrite differing content.
It performs no download and changes neither the reference configuration nor
the canonical record. It copies only the three fixed artifacts after replaying
the projection from the exact DOCX. If the retained preparation is unavailable,
recover and verify the original inputs before proceeding; a similarly named
file is not a substitute.

Native reference validation and
[`reference-assertion-coverage`](../../docs/REFERENCE_ASSERTION_COVERAGE.md)
serve different purposes. The latter verifies actual comparison counts and
selected-source identities on committed record bytes. Successful lexical
matching does not resolve the Methods/Table S1 panel disagreement or certify
the scientific claims.
