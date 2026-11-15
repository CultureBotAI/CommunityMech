"""Read original 000088 supplements for #1548, 2026-11-15.

Inputs: captured publisher ZIP and exact archive member, or an extracted XLSX/DOCX.
Outputs: exclusive private extraction and receipt, or tables/paragraphs on stdout.
Never extracts paths supplied by an archive and never overwrites retained files.
"""

import argparse
import hashlib
import json
import zipfile
from pathlib import Path

import openpyxl
from defusedxml import ElementTree


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path)
    parser.add_argument("--member")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.member:
        if not args.output or args.output.exists() or args.output.is_symlink():
            raise ValueError("extraction requires fresh explicit output path")
        receipt = args.output.with_name(args.output.name + ".extraction.json")
        if receipt.exists() or receipt.is_symlink():
            raise ValueError("existing extraction receipt")
        raw = args.path.read_bytes()
        with zipfile.ZipFile(args.path) as archive:
            entry = archive.getinfo(args.member)
            if entry.file_size > 50_000_000:
                raise ValueError("unexpectedly large source member")
            data = archive.read(entry)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with args.output.open("xb") as stream:
            stream.write(data)
        receipt.write_text(
            json.dumps(
                {
                    "archive_sha256": digest(raw),
                    "member": args.member,
                    "bytes": len(data),
                    "sha256": digest(data),
                },
                indent=2,
            )
            + "\n"
        )
        print(receipt.read_text())
    elif args.path.suffix == ".xlsx":
        workbook = openpyxl.load_workbook(args.path, data_only=True, read_only=True)
        for sheet in workbook:
            print("SHEET", sheet.title)
            for number, row in enumerate(sheet.iter_rows(values_only=True), 1):
                if any(cell is not None for cell in row):
                    print(number, json.dumps(row, ensure_ascii=False))
        workbook.close()
    elif args.path.suffix == ".docx":
        with zipfile.ZipFile(args.path) as archive:
            root = ElementTree.fromstring(archive.read("word/document.xml"))
            for number, paragraph in enumerate(
                root.iter("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p"), 1
            ):
                parts = [
                    node.text or ""
                    for node in paragraph.iter(
                        "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t"
                    )
                ]
                if parts:
                    print(number, "".join(parts))
            print("IMAGES", [name for name in archive.namelist() if name.startswith("word/media/")])
    else:
        raise ValueError("provide an exact member for extraction, or a supported source document")


if __name__ == "__main__":
    main()
