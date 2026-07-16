# F3 Integrated Review Report

## Verdict

`COMPLETE_PRE_SUBMISSION_DRAFT_REFERENCE_AND_EXTERNAL_REVIEW_GATES_OPEN`

The manuscript now has a complete abstract, ten main sections, four
appendices, data/code availability, author declarations, a verified
bibliography, and claim-level traceability. The mathematical narrative is
integrated. It is not yet labeled submission-ready because exact
chapter/theorem locations remain open for four classical books and no external
specialist review has been recorded.

## Review gate results

| Gate | Requirement | Result | Notes |
|---|---|---|---|
| F3-G1 | Sections 1–10 complete | PASS | Introduction and conclusion added after technical review |
| F3-G2 | Main claim traceability | PASS | 32/32 main claims |
| F3-G3 | Appendix claim traceability | PASS | 6/6 appendix claims |
| F3-G4 | Mass normalization consistent | PASS | Arbitrary positive mass \(M=\sum_i\mu_i\); normalized weights used only inside means and transforms |
| F3-G5 | \(\beta\)/\(\lambda\) notation separated | PASS | \(\beta\) for transition strength; \(\lambda\) for aggregation transform unless explicitly identified |
| F3-G6 | Static aggregation proof has one primary home | PASS | Full proof in Section 6; Section 8 uses it without repetition |
| F3-G7 | Dynamic nonclosure witness exact | PASS | Rational four-point witness retained |
| F3-G8 | IIA wording corrected | PASS | IIA alone does not select the exponential |
| F3-G9 | Physical boundary explicit | PASS | Introduction, Section 9, conclusion, and abstract |
| F3-G10 | Bibliographic keys complete | PASS | 14 cited keys; no missing or unused entries |
| F3-G11 | Primary metadata checked | PASS | Metadata/DOIs checked for all 14 references |
| F3-G12 | Exact book theorem/page locations | PARTIAL | Five locations remain open |
| F3-G13 | External mathematical review | NOT RUN | Blocking before submission |
| F3-G14 | Journal-specific formatting | NOT STARTED | Deferred until venue selection |

## Major revisions from F2

### 1. Unified mass convention

Earlier sections alternated between arbitrary positive masses and normalized
probabilities. F3 defines

\[
M=\sum_i\mu_i
\]

and uses \(\mu_i/M\) whenever a mean, probability distribution, or effective
score requires normalization. Multiplying every mass by one common positive
factor therefore leaves \(Q_\lambda\) unchanged.

### 2. Separated kernel and transform parameters

The manuscript now reserves:

- \(\beta\) for the strength of a declared transition kernel;
- \(\lambda\) for the exponential aggregation transform.

The two can be identified by an additional model contract, but notation no
longer implies that identification.

### 3. Removed the duplicated static proof

Section 6 owns the proof that \((M_B,Q_\lambda(B))\) exactly preserves the
exponential weight. Section 8 now compares observable-specific messages and
moves directly to the dynamic occupancy obstruction.

### 4. Tightened extension-theorem attribution

The projective path-space extension is attributed directly to Kolmogorov.
Daniell is no longer listed as though his 1918 article were the exact source
of the theorem used.

### 5. Added boundary appendices

The appendices now isolate results that are important but would interrupt the
main narrative:

- equivariance and calibrated symmetry breaking;
- zero-variance standardization boundary;
- Gaussian restricted-family closure;
- exponential-moment domain;
- exact weighted-median nondecomposability.

### 6. Completed the article frame

F3 adds the introduction, conclusion, abstract, data/code availability, author
declarations, full manuscript assembly, and pre-submission status gates.

## Open reference-location gates

The following metadata are verified, but final journal formatting should add
exact theorem, chapter, or page locations:

1. `KrantzEtAl1971` — interval-scale and meaningfulness discussion;
2. `Luce1959` — exact choice-axiom location;
3. `Kolmogorov1933` — exact extension-theorem chapter/page;
4. `Aczel1966` — exact translation-covariant quasi-arithmetic
   characterization location;
5. `KemenySnell1960` — exact lumpability chapter/page.

These are bibliographic precision gates, not unresolved mathematical defects
in the manuscript's proofs.

## Remaining work before submission

1. obtain and record the four exact classical locations;
2. perform an independent specialist review of Sections 2, 4, 5, 7, and 8;
3. choose a target journal and apply its citation/formatting rules;
4. render equations and references in the selected manuscript system;
5. conduct a final proofreading pass after formatting.

No new scientific claim is required to complete the foundational manuscript.
The remaining gates concern verification, external review, and presentation.
