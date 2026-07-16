#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import csv
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
DRAFT = ROOT / "manuscripts" / "foundational" / "draft"

SECTION_FILES = [
    "02_order_identifiability.md",
    "05_measure_and_refinement.md",
    "07_dynamic_nonclosure.md",
    "08_coarse_graining.md",
    "09_informational_architecture.md",
]

EXPECTED_CLAIMS = {
    "MF-R023","MF-R024","MF-R025","MF-R037","MF-R039","MF-R040",
    "MF-R041","MF-R042","MF-R043","MF-R044","MF-R045","MF-R048",
    "MF-R049","MF-R050","MF-R058","MF-R059","MF-R061","MF-R062",
    "MF-R063","MF-R067","MF-R068","MF-R069",
}

BANNED_PHRASES = [
    "new fundamental theory",
    "unique minimal ontology",
    "emergent spacetime",
    "derived gravity",
    "proves gravity",
    "universal constant",
    "first ever",
]

def bib_keys(text: str) -> set[str]:
    return set(re.findall(r"@\w+\{([^,]+),", text))

def cited_keys(text: str) -> set[str]:
    keys: set[str] = set()
    for block in re.findall(r"\[([^\]]*@[^\]]+)\]", text):
        for match in re.findall(r"@([A-Za-z0-9_:-]+)", block):
            keys.add(match)
    return keys

def main() -> int:
    errors: list[str] = []
    all_text = ""

    for filename in SECTION_FILES:
        path = DRAFT / filename
        if not path.exists():
            errors.append(f"Missing section: {filename}")
            continue

        text = path.read_text(encoding="utf-8")
        all_text += "\n" + text
        word_count = len(re.findall(r"\b[\wÀ-ÿ'-]+\b", text))

        if word_count < 850:
            errors.append(f"{filename} is too short: {word_count} words.")

        if re.search(r"\bA\d{1,2}(?:\.\d+)?\b", text):
            errors.append(f"{filename} contains an audit number.")

        lower = text.lower()
        for phrase in BANNED_PHRASES:
            if phrase in lower:
                errors.append(f"{filename} contains banned phrase: {phrase}")

        if "TODO" in text or "[REFERENCE CHECK]" in text:
            errors.append(f"{filename} contains unresolved placeholder text.")

    trace_path = DRAFT / "CLAIM_TRACEABILITY.csv"
    with trace_path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    ids = [row["claim_id"] for row in rows]

    if set(ids) != EXPECTED_CLAIMS:
        errors.append(
            "Traceability mismatch: "
            f"missing={sorted(EXPECTED_CLAIMS - set(ids))}, "
            f"extra={sorted(set(ids) - EXPECTED_CLAIMS)}"
        )
    if len(ids) != len(set(ids)):
        errors.append("Duplicate claim IDs in traceability.")

    bib_text = (DRAFT / "REFERENCES_WORKING.bib").read_text(encoding="utf-8")
    available = bib_keys(bib_text)
    cited = cited_keys(all_text)
    if cited - available:
        errors.append(f"Citation keys missing from bibliography: {sorted(cited - available)}")

    witness_file = (DRAFT / "07_dynamic_nonclosure.md").read_text(encoding="utf-8")
    witness_tokens = [
        r"\frac9{40}", r"\frac7{20}", r"\frac{11}{40}",
        r"\frac3{20}", r"\frac{15}{32}", r"\frac{5\sqrt2-7}{40}",
    ]
    for token in witness_tokens:
        if token not in witness_file:
            errors.append(f"Exact witness token missing: {token}")

    combined = (DRAFT / "CORE_DRAFT.md").read_text(encoding="utf-8")
    for filename in SECTION_FILES:
        heading = (DRAFT / filename).read_text(encoding="utf-8").splitlines()[0]
        if heading not in combined:
            errors.append(f"Combined draft missing heading: {heading}")

    status_text = (DRAFT / "DRAFT_STATUS.md").read_text(encoding="utf-8").lower()
    if "not a submission manuscript" not in status_text:
        errors.append("Draft status lacks explicit non-submission boundary.")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    total_words = len(re.findall(r"\b[\wÀ-ÿ'-]+\b", all_text))
    print(f"Validated {len(SECTION_FILES)} core sections.")
    print(f"Core prose words: {total_words}")
    print(f"Traceable claims: {len(ids)}")
    print(f"Citation keys used: {len(cited)}")
    print("F1 manuscript core validation passed.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
