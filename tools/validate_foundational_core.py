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
    "03_quantitative_structure_q.md",
    "04_operational_kernels.md",
    "05_measure_and_refinement.md",
    "06_static_aggregation.md",
    "07_dynamic_nonclosure.md",
    "08_coarse_graining.md",
    "09_informational_architecture.md",
]

EXPECTED_CLAIMS = {
    "MF-R023","MF-R024","MF-R025","MF-R028","MF-R029",
    "MF-R031","MF-R032","MF-R033","MF-R034","MF-R035","MF-R036",
    "MF-R037","MF-R039","MF-R040","MF-R041","MF-R042","MF-R043",
    "MF-R044","MF-R045","MF-R046","MF-R047","MF-R048","MF-R049",
    "MF-R050","MF-R058","MF-R059","MF-R061","MF-R062","MF-R063",
    "MF-R067","MF-R068","MF-R069",
}

BANNED_PHRASES = [
    "new fundamental theory",
    "unique minimal ontology",
    "emergent spacetime",
    "derived gravity",
    "proves gravity",
    "universal constant",
    "first ever",
    "ii a selects the exponential",
]

def bib_keys(text: str) -> list[str]:
    return re.findall(r"@\w+\{([^,]+),", text)

def cited_keys(text: str) -> set[str]:
    keys: set[str] = set()
    for block in re.findall(r"\[([^\]]*@[^\]]+)\]", text):
        keys.update(re.findall(r"@([A-Za-z0-9_:-]+)", block))
    return keys

def main() -> int:
    errors: list[str] = []
    all_text = ""
    headings: list[str] = []

    for filename in SECTION_FILES:
        path = DRAFT / filename
        if not path.exists():
            errors.append(f"Missing section: {filename}")
            continue

        text = path.read_text(encoding="utf-8")
        all_text += "\n" + text
        headings.append(text.splitlines()[0])

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
    available_list = bib_keys(bib_text)
    available = set(available_list)
    if len(available_list) != len(available):
        errors.append("Duplicate keys in working bibliography.")

    cited = cited_keys(all_text)
    if cited - available:
        errors.append(f"Citation keys missing from bibliography: {sorted(cited - available)}")

    section4 = (DRAFT / "04_operational_kernels.md").read_text(encoding="utf-8")
    required_kernel_phrases = [
        "IIA by itself does not force",
        "difference-based exponential selection",
        "identifiable within the standardized model",
        "remaining underived",
    ]
    for phrase in required_kernel_phrases:
        if phrase not in section4:
            errors.append(f"Section 4 lacks required distinction: {phrase}")

    section6 = (DRAFT / "06_static_aggregation.md").read_text(encoding="utf-8")
    required_static = [
        r"W_\lambda(B)",
        r"Q_\lambda(aq+c,\mu)",
        "exact static aggregation does not imply autonomous dynamic closure",
    ]
    for token in required_static:
        if token not in section6:
            errors.append(f"Section 6 lacks required content: {token}")

    witness_file = (DRAFT / "07_dynamic_nonclosure.md").read_text(encoding="utf-8")
    witness_tokens = [
        r"\frac9{40}", r"\frac7{20}", r"\frac{11}{40}",
        r"\frac3{20}", r"\frac{15}{32}", r"\frac{5\sqrt2-7}{40}",
    ]
    for token in witness_tokens:
        if token not in witness_file:
            errors.append(f"Exact C2 witness token missing: {token}")

    integrated = (DRAFT / "TECHNICAL_BODY.md").read_text(encoding="utf-8")
    positions = []
    for heading in headings:
        pos = integrated.find(heading)
        if pos < 0:
            errors.append(f"Integrated body missing heading: {heading}")
        positions.append(pos)
    if any(a >= b for a, b in zip(positions, positions[1:]) if a >= 0 and b >= 0):
        errors.append("Integrated section order is incorrect.")

    core = (DRAFT / "CORE_DRAFT.md").read_text(encoding="utf-8")
    if core != integrated:
        errors.append("CORE_DRAFT.md and TECHNICAL_BODY.md differ.")

    status_text = (DRAFT / "DRAFT_STATUS.md").read_text(encoding="utf-8").lower()
    if "not a submission manuscript" not in status_text:
        errors.append("Draft status lacks explicit non-submission boundary.")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    total_words = len(re.findall(r"\b[\wÀ-ÿ'-]+\b", all_text))
    print(f"Validated {len(SECTION_FILES)} integrated technical sections.")
    print(f"Technical-body words: {total_words}")
    print(f"Traceable main claims: {len(ids)}")
    print(f"Citation keys used: {len(cited)}")
    print("F2 foundational technical-body validation passed.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
