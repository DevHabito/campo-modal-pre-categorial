#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
GLOBAL_CSV = ROOT / "manuscripts" / "GLOBAL_CLAIM_FREEZE.csv"
GLOBAL_JSON = ROOT / "manuscripts" / "GLOBAL_CLAIM_FREEZE.json"
COMB_CSV = ROOT / "manuscripts" / "combinatorics" / "CLAIM_MAP.csv"
FOUND_CSV = ROOT / "manuscripts" / "foundational" / "CLAIM_MAP.csv"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def main() -> int:
    errors: list[str] = []

    global_rows = read_csv(GLOBAL_CSV)
    global_json = json.loads(GLOBAL_JSON.read_text(encoding="utf-8"))
    comb_rows = read_csv(COMB_CSV)
    found_rows = read_csv(FOUND_CSV)

    global_ids = [row["claim_id"] for row in global_rows]

    if len(global_rows) != 69:
        errors.append(f"Expected 69 global claims, found {len(global_rows)}.")
    if len(set(global_ids)) != 69:
        errors.append("Global claim IDs are not unique.")
    if global_json != global_rows:
        errors.append("GLOBAL_CLAIM_FREEZE.json does not match CSV content.")

    comb_main = {
        row["claim_id"] for row in comb_rows if row["role"] == "MAIN"
    }
    found_main = {
        row["claim_id"] for row in found_rows if row["role"] == "MAIN"
    }

    if comb_main & found_main:
        errors.append(
            "A claim appears as MAIN in both manuscripts: "
            + ", ".join(sorted(comb_main & found_main))
        )

    required_comb = {
        "MF-R005", "MF-R006", "MF-R007", "MF-R008",
        "MF-R009", "MF-R010", "MF-R011",
    }
    if comb_main != required_comb:
        errors.append("Combinatorics main claim set differs from the frozen set.")

    required_found = {
        "MF-R023", "MF-R024", "MF-R025", "MF-R028", "MF-R029",
        "MF-R031", "MF-R032", "MF-R033", "MF-R034", "MF-R035",
        "MF-R036", "MF-R037", "MF-R039", "MF-R040", "MF-R041",
        "MF-R042", "MF-R043", "MF-R044", "MF-R045", "MF-R046",
        "MF-R047", "MF-R048", "MF-R049", "MF-R050", "MF-R058",
        "MF-R059", "MF-R061", "MF-R062", "MF-R063", "MF-R067",
        "MF-R068", "MF-R069",
    }
    if found_main != required_found:
        errors.append("Foundational main claim set differs from the frozen set.")

    for row in comb_rows + found_rows:
        if not row["allowed_claim"].strip():
            errors.append(f"{row['claim_id']} lacks allowed claim wording.")
        if not row["forbidden_overclaim"].strip():
            errors.append(f"{row['claim_id']} lacks forbidden-overclaim wording.")
        if not row["section"].strip():
            errors.append(f"{row['claim_id']} lacks a section assignment.")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print(f"Validated {len(global_rows)} globally frozen claims.")
    print(f"Combinatorics MAIN claims: {len(comb_main)}")
    print(f"Foundational MAIN claims: {len(found_main)}")
    print(f"Foundational APPENDIX claims: {sum(r['role']=='APPENDIX' for r in found_rows)}")
    print(f"Foundational SUPPLEMENT claims: {sum(r['role']=='SUPPLEMENT' for r in found_rows)}")
    print("Manuscript split validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
