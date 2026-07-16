#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import csv
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
DRAFT = ROOT / "manuscripts" / "foundational" / "draft"

MAIN_SECTIONS = [
    "01_introduction.md",
    "02_order_identifiability.md",
    "03_quantitative_structure_q.md",
    "04_operational_kernels.md",
    "05_measure_and_refinement.md",
    "06_static_aggregation.md",
    "07_dynamic_nonclosure.md",
    "08_coarse_graining.md",
    "09_informational_architecture.md",
    "10_scope_and_conclusion.md",
]

APPENDICES = [
    "APPENDIX_A_equivariance_and_calibration.md",
    "APPENDIX_B_refinement_boundary.md",
    "APPENDIX_C_restricted_closure_and_domain.md",
    "APPENDIX_D_median_nonclosure.md",
]

EXPECTED_MAIN = {
    "MF-R023","MF-R024","MF-R025","MF-R028","MF-R029",
    "MF-R031","MF-R032","MF-R033","MF-R034","MF-R035","MF-R036",
    "MF-R037","MF-R039","MF-R040","MF-R041","MF-R042","MF-R043",
    "MF-R044","MF-R045","MF-R046","MF-R047","MF-R048","MF-R049",
    "MF-R050","MF-R058","MF-R059","MF-R061","MF-R062","MF-R063",
    "MF-R067","MF-R068","MF-R069",
}

EXPECTED_APPENDIX = {
    "MF-R026","MF-R027","MF-R038","MF-R051","MF-R056","MF-R060",
}

BANNED_PHRASES = [
    "new fundamental theory",
    "unique minimal ontology",
    "emergent spacetime",
    "derived gravity",
    "proves gravity",
    "first ever",
    "universal constant",
]

def words(text: str) -> int:
    return len(re.findall(r"\b[\wÀ-ÿ'-]+\b", text))

def bib_keys(text: str) -> list[str]:
    return re.findall(r"@\w+\{([^,]+),", text)

def cited_keys(text: str) -> set[str]:
    found: set[str] = set()
    for block in re.findall(r"\[([^\]]*@[^\]]+)\]", text):
        found.update(re.findall(r"@([A-Za-z0-9_:-]+)", block))
    return found

def main() -> int:
    errors: list[str] = []

    for filename in MAIN_SECTIONS + APPENDICES:
        if not (DRAFT / filename).exists():
            errors.append(f"Missing manuscript component: {filename}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    main_text = "\n".join(
        (DRAFT / filename).read_text(encoding="utf-8")
        for filename in MAIN_SECTIONS
    )
    appendix_text = "\n".join(
        (DRAFT / filename).read_text(encoding="utf-8")
        for filename in APPENDICES
    )

    for filename in MAIN_SECTIONS:
        text = (DRAFT / filename).read_text(encoding="utf-8")
        if words(text) < 500:
            errors.append(f"{filename} is too short: {words(text)} words.")
        if re.search(r"\bA\d{2}(?:\.\d+)?\b", text):
            errors.append(f"{filename} contains an audit identifier.")
        lower = text.lower()
        for phrase in BANNED_PHRASES:
            if phrase in lower:
                errors.append(f"{filename} contains banned phrase: {phrase}")
        if "TODO" in text or "[REFERENCE CHECK]" in text:
            errors.append(f"{filename} contains an unresolved placeholder.")

    abstract = (DRAFT / "ABSTRACT.md").read_text(encoding="utf-8")
    abstract_words = words(abstract)
    if not 200 <= abstract_words <= 250:
        errors.append(f"Abstract length is {abstract_words}; expected 200-250.")

    trace_path = DRAFT / "CLAIM_TRACEABILITY.csv"
    with trace_path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    ids = [row["claim_id"] for row in rows]
    main_ids = {row["claim_id"] for row in rows if row["role"] == "MAIN"}
    appendix_ids = {row["claim_id"] for row in rows if row["role"] == "APPENDIX"}

    if len(ids) != len(set(ids)):
        errors.append("Duplicate claim IDs in traceability.")
    if main_ids != EXPECTED_MAIN:
        errors.append(
            f"Main-claim mismatch: missing={sorted(EXPECTED_MAIN-main_ids)}, "
            f"extra={sorted(main_ids-EXPECTED_MAIN)}"
        )
    if appendix_ids != EXPECTED_APPENDIX:
        errors.append(
            f"Appendix-claim mismatch: missing={sorted(EXPECTED_APPENDIX-appendix_ids)}, "
            f"extra={sorted(appendix_ids-EXPECTED_APPENDIX)}"
        )

    bib_text = (DRAFT / "REFERENCES_VERIFIED.bib").read_text(encoding="utf-8")
    available_list = bib_keys(bib_text)
    available = set(available_list)
    if len(available_list) != len(available):
        errors.append("Duplicate bibliography keys.")

    cited = cited_keys(main_text + "\n" + appendix_text)
    if cited - available:
        errors.append(f"Missing bibliography keys: {sorted(cited-available)}")
    if available - cited:
        errors.append(f"Unused bibliography keys: {sorted(available-cited)}")

    with (DRAFT / "REFERENCE_AUDIT.csv").open(newline="", encoding="utf-8") as handle:
        ref_rows = list(csv.DictReader(handle))
    if {row["citation_key"] for row in ref_rows} != available:
        errors.append("Reference audit and verified bibliography differ.")
    open_locations = sum(
        row["remaining_status"] in {
            "THEOREM_LOCATION_PENDING",
            "CHAPTER_PAGE_PENDING",
        }
        for row in ref_rows
    )
    if open_locations != 5:
        errors.append(f"Expected five open book-location gates, found {open_locations}.")

    section4 = (DRAFT / "04_operational_kernels.md").read_text(encoding="utf-8")
    for phrase in [
        "IIA by itself does not force",
        r"\(\beta\) denotes the strength",
        r"\(\lambda\) denotes the parameter",
        "remaining underived",
    ]:
        if phrase not in section4:
            errors.append(f"Section 4 lacks required distinction: {phrase}")

    section6 = (DRAFT / "06_static_aggregation.md").read_text(encoding="utf-8")
    if "**Proposition 6.1 (exact static aggregation).**" not in section6:
        errors.append("Section 6 lacks the primary static-aggregation proposition.")

    section8 = (DRAFT / "08_coarse_graining.md").read_text(encoding="utf-8")
    if "exponential-observable sufficiency" in section8:
        errors.append("Section 8 still duplicates the Section 6 static proposition.")
    if "**Proposition 8.1 (exact occupancy-weighted aggregation).**" not in section8:
        errors.append("Section 8 lacks the flow-aggregation proposition.")

    section7 = (DRAFT / "07_dynamic_nonclosure.md").read_text(encoding="utf-8")
    for token in [
        r"M=\sum_i\mu_i",
        r"\bar q_\mu=\frac1M\sum_i\mu_i q_i",
        r"\frac9{40}", r"\frac7{20}", r"\frac{11}{40}",
        r"\frac3{20}", r"\frac{15}{32}",
        r"\frac{5\sqrt2-7}{40}",
    ]:
        if token not in section7:
            errors.append(f"Section 7 lacks required exact content: {token}")

    appendix_d = (DRAFT / "APPENDIX_D_median_nonclosure.md").read_text(encoding="utf-8")
    median_tokens = [
        r"\frac35",
        r"\frac25",
        r"\frac12",
        r"combined median is \(50\)",
        "combined median\nis \\(1\\)",
    ]
    for token in median_tokens:
        if token not in appendix_d:
            errors.append(f"Appendix D lacks exact counterexample content: {token}")

    full = (DRAFT / "FULL_MANUSCRIPT.md").read_text(encoding="utf-8")
    pre = (DRAFT / "PRE_SUBMISSION_MANUSCRIPT.md").read_text(encoding="utf-8")
    core = (DRAFT / "CORE_DRAFT.md").read_text(encoding="utf-8")
    if not (full == pre == core):
        errors.append("Full, pre-submission, and core manuscript files differ.")

    order_markers = [
        "# Abstract",
        "# 1. Introduction",
        "# 2. Order-Only Identifiability",
        "# 3. Additional Quantitative Structure",
        "# 4. Operational Kernels",
        "# 5. Measure, Multiplicity, and Refinement",
        "# 6. Static Exponential Aggregation",
        "# 7. Dynamic Transport and Nonclosure",
        "# 8. Observable-Relative Coarse-Graining",
        "# 9. Provisional Informational Architecture",
        "# 10. Scope, Contribution, and Conclusion",
        "# Appendix A.",
        "# Appendix B.",
        "# Appendix C.",
        "# Appendix D.",
        "# Data and Code Availability",
        "# Author Declarations",
        "# References",
    ]
    positions = [full.find(marker) for marker in order_markers]
    if any(pos < 0 for pos in positions):
        errors.append("Full manuscript is missing one or more ordered components.")
    elif any(a >= b for a, b in zip(positions, positions[1:])):
        errors.append("Full manuscript component order is incorrect.")

    status_text = (DRAFT / "DRAFT_STATUS.md").read_text(encoding="utf-8")
    if "not a submission manuscript" in status_text.lower():
        errors.append("F3 status still describes the artifact as an incomplete core.")
    if "complete pre-submission" not in status_text.lower():
        errors.append("F3 status lacks complete pre-submission wording.")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print(f"Validated {len(MAIN_SECTIONS)} main sections and {len(APPENDICES)} appendices.")
    print(f"Abstract words: {abstract_words}")
    print(f"Full manuscript words: {words(full)}")
    print(f"Traceable claims: {len(ids)} ({len(main_ids)} main, {len(appendix_ids)} appendix)")
    print(f"Verified citation keys: {len(available)}")
    print(f"Open exact-location gates: {open_locations}")
    print("F3 foundational manuscript validation passed.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
