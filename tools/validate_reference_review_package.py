#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import csv
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
DRAFT = ROOT / "manuscripts" / "foundational" / "draft"
REVIEW = ROOT / "manuscripts" / "foundational" / "review"

REQUIRED_REVIEW_FILES = [
    "README.md",
    "ANONYMIZED_REVIEW_COPY.md",
    "EXTERNAL_REVIEW_REQUEST.md",
    "MATH_AUDIT_TARGETS.md",
    "CRITICAL_CLAIM_CHECKLIST.csv",
    "REVIEW_FORM.md",
    "REVIEW_LOG_TEMPLATE.csv",
    "CONFLICT_AND_INDEPENDENCE_POLICY.md",
    "INTERNAL_ADVERSARIAL_REVIEW.md",
    "EXACT_WITNESS_CHECK.json",
]

def bib_keys(text: str) -> set[str]:
    return set(re.findall(r"@\w+\{([^,]+),", text))

def cited_keys(text: str) -> set[str]:
    found: set[str] = set()
    for block in re.findall(r"\[([^\]]*@[^\]]+)\]", text):
        found.update(re.findall(r"@([A-Za-z0-9_:-]+)", block))
    return found

def main() -> int:
    errors: list[str] = []

    for filename in REQUIRED_REVIEW_FILES:
        if not (REVIEW / filename).exists():
            errors.append(f"Missing review file: {filename}")

    with (DRAFT / "REFERENCE_LOCATIONS.csv").open(newline="", encoding="utf-8") as handle:
        locations = list(csv.DictReader(handle))

    if len(locations) != 5:
        errors.append(f"Expected 5 reference gates, found {len(locations)}.")
    closed = [row for row in locations if row["status"] == "CLOSED"]
    open_rows = [row for row in locations if row["status"] == "OPEN"]
    if len(closed) != 4 or len(open_rows) != 1:
        errors.append(f"Expected 4 CLOSED and 1 OPEN gate; found {len(closed)} and {len(open_rows)}.")
    if open_rows and open_rows[0]["citation_key"] != "Aczel1966":
        errors.append("The only open reference gate must be Aczel1966.")

    exact_tokens = {
        "LuceEtAl1990": ["Chapter 20", "108–119", "Chapter 22", "267–291"],
        "Luce1959": ["5–15", "20–28", "p. 23"],
        "Kolmogorov1933": ["Chapter III", "27–32"],
        "KemenySnell1960": ["Theorem 6.3.2", "p. 124"],
    }
    by_key = {row["citation_key"]: row for row in locations}
    for key, tokens in exact_tokens.items():
        if key not in by_key:
            errors.append(f"Missing closed gate: {key}")
            continue
        text = by_key[key]["exact_location"]
        for token in tokens:
            if token not in text:
                errors.append(f"{key} location lacks token: {token}")

    bib_text = (DRAFT / "REFERENCES_VERIFIED.bib").read_text(encoding="utf-8")
    available = bib_keys(bib_text)
    full = (DRAFT / "FULL_MANUSCRIPT.md").read_text(encoding="utf-8")
    cited = cited_keys(full)
    if cited - available:
        errors.append(f"Missing bibliography keys: {sorted(cited - available)}")
    if available - cited:
        errors.append(f"Unused bibliography keys: {sorted(available - cited)}")
    if "LuceEtAl1990" not in available:
        errors.append("Volume III measurement citation was not added.")

    for filename in ["PRE_SUBMISSION_MANUSCRIPT.md", "CORE_DRAFT.md"]:
        if (DRAFT / filename).read_text(encoding="utf-8") != full:
            errors.append(f"{filename} differs from FULL_MANUSCRIPT.md.")

    section5 = (DRAFT / "05_measure_and_refinement.md").read_text(encoding="utf-8")
    if "by the standard\nextension theorem by the standard" in section5:
        errors.append("Section 5 still contains duplicated extension wording.")
    for phrase in ["countable cylinder algebra", "cylinder sigma-algebra"]:
        if phrase not in section5:
            errors.append(f"Section 5 lacks F4 domain clarification: {phrase}")

    section4 = (DRAFT / "04_operational_kernels.md").read_text(encoding="utf-8")
    if "[@LuceEtAl1990]" not in section4:
        errors.append("Section 4 does not cite the exact Volume III source.")

    anonymous = (REVIEW / "ANONYMIZED_REVIEW_COPY.md").read_text(encoding="utf-8")
    for identifying_text in ["Felipe Gianini Romero", "DevHabito", "precategorical-modal-field-framework"]:
        if identifying_text in anonymous:
            errors.append(f"Anonymous copy contains identifying text: {identifying_text}")

    internal = (REVIEW / "INTERNAL_ADVERSARIAL_REVIEW.md").read_text(encoding="utf-8")
    if "NOT_INDEPENDENT_REVIEW" not in internal:
        errors.append("Internal review is not explicitly marked non-independent.")

    status = json.loads((DRAFT / "DRAFT_STATUS.json").read_text(encoding="utf-8"))
    if status.get("independent_external_review") != "NOT_COMPLETED":
        errors.append("External review must remain NOT_COMPLETED.")
    if status.get("exact_reference_gates_closed") != 4:
        errors.append("Status does not report four closed gates.")
    if status.get("exact_reference_gates_open") != 1:
        errors.append("Status does not report one open gate.")

    witness = json.loads((REVIEW / "EXACT_WITNESS_CHECK.json").read_text(encoding="utf-8"))
    if witness.get("verdict") != "PASS_EXACT_FOUR_POINT_NONCLOSURE_WITNESS":
        errors.append("Exact witness verification did not pass.")
    if not all(witness.get("checks", {}).values()):
        errors.append("One or more exact witness checks failed.")

    with (REVIEW / "CRITICAL_CLAIM_CHECKLIST.csv").open(newline="", encoding="utf-8") as handle:
        checklist = list(csv.DictReader(handle))
    if len(checklist) < 20:
        errors.append(f"Critical checklist too small: {len(checklist)} claims.")

    status_md = (DRAFT / "DRAFT_STATUS.md").read_text(encoding="utf-8")
    if "not submission-ready" not in status_md.lower():
        errors.append("Status lacks explicit not-submission-ready statement.")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    words = len(re.findall(r"\b[\wÀ-ÿ'-]+\b", full))
    print(f"Reference gates: {len(closed)}/5 closed; Aczel gate open.")
    print(f"Verified bibliography keys: {len(available)}")
    print(f"Review package files: {len(REQUIRED_REVIEW_FILES)}")
    print(f"Critical claims prepared: {len(checklist)}")
    print(f"Full manuscript words: {words}")
    print("F4 reference and review package validation passed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
