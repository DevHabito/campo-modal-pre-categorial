# Novelty Audit C1 — Finite Preorder Counts and Edge-Toggle Sensitivity

**Project:** Pre-Categorical Modal Field Framework  
**Author:** Felipe Gianini Romero  
**Search date:** 2026-07-15  
**Scope:** MF-R007, MF-R008, MF-R011

## Executive verdict

| Claim | Final classification | Manuscript treatment |
|---|---|---|
| MF-R007 | Classical enumeration formula | Attribute; retain independent reproduction and corrective use |
| MF-R008 | Project-specific elementary proposition; no exact match found | Retain as a corrective named proposition, without claiming certified priority |
| MF-R011 | Apparently unreported exact finite statistic; novelty not certified | Retain as exact enumeration and open problem |

## MF-R007

\[
N_{\mathrm{full}}(n)
=
\sum_{k=1}^{n}S(n,k)p(k)
\]

is the classical labeled-preorder / finite-topology enumeration identity.
Fischer and Makowsky explicitly state the formula as known and attribute it to
a 1973 source. The value \(N_{\mathrm{full}}(5)=6942\) is historical, not new.

**What remains project-specific:** independent exhaustive reproduction,
formal resolution of the \(5234/6942\) ambiguity, and public corrective
provenance.

## MF-R008

\[
N_{\mathrm{rep}}(n)
=
\sum_{k=1}^{n}\binom{n-1}{k-1}p(k)
\]

counts the project's lossy minimum-representative quotient-poset code. No exact
prior formulation was found in the searched literature. However, the proof is
an immediate consequence of the definition, so this should be presented as a
project-specific elementary proposition rather than a major new theorem.

## MF-R011

Define

\[
P_n
=
\frac{1}{n(n-1)2^{n(n-1)}}
\sum_{G,e}
\mathbf 1[C(G)\neq C(G\triangle e)].
\]

Exact exhaustive values are

\[
P_2=1,\qquad
P_3=\frac34,\qquad
P_4=\frac12,\qquad
P_5=\frac{75}{256}.
\]

Related work studies dynamic SCC algorithms, network susceptibility, and
average sensitivity of graph algorithms. No inspected source reports this
exact statistic or \(75/256\). The correct wording is “apparently unreported
in the searched literature,” not a categorical priority claim.

## Consequences for the combinatorics paper

The paper should not be organized around \(6942\) as a new theorem. Its viable
core is instead:

1. precise comparison of complete and representative encodings;
2. exact fiber structure of the lossy code;
3. edge-toggle sensitivity \(P_n\);
4. a structural theorem, recurrence, bound, or asymptotic result for \(P_n\);
5. complete code and reproducibility contracts.

## Matrix updates

Apply `RESULT_CLASSIFICATION_PATCH.csv` to MF-R007, MF-R008, and MF-R011.
The patch changes novelty and literature-review wording only; it does not alter
the mathematical claims or archived computations.

## Limits of this audit

A literature search cannot prove novelty. This audit records the sources and
queries examined and supplies safe publication language. A journal submission
should still invite specialist review and avoid absolute “first-ever” claims.
