# Internal Adversarial Review

## Status

`AUTHOR_SIDE_STRESS_TEST_NOT_INDEPENDENT_REVIEW`

This document records an adversarial editorial and mathematical pass performed
inside the manuscript-production workflow. It does **not** close the external
independent-review gate.

## Findings

### IR-1 — Order-law language

**Result:** no blocking defect found.

Proposition 2.2 is restricted to continuous strictly increasing marginals and
states that the finite order law depends *at most* on the copula. The text
explicitly avoids the converse claim that every distinct copula produces a
distinct finite order law.

### IR-2 — Added-mark criterion

**Result:** wording is appropriately necessary, not sufficient.

Proposition 3.1 says that \(q\) can break an order-only equivalence only when
its conditional marked law differs within that class. It does not claim that
every such difference is identifiable from finite data.

### IR-3 — Exponential selection

**Result:** no hidden use of IIA alone.

Section 4 explicitly states that normalized pointwise weights already satisfy
IIA and that the exponential requires the stronger difference-only odds
condition or a declared maximum-entropy problem.

**External-review target:** verify the domain assumptions used to convert the
multiplicative functional equation into continuous exponential solutions.

### IR-4 — Context–scale lemma

**Result:** proof is algebraically sound under its strong assumptions.

Extension stability removes context dependence; translation invariance reduces
the difference to \(h(x-y)\); full positive-scale numerical invariance makes
\(h\) constant on each sign class; continuity at zero makes both constants
zero.

**External-review target:** determine whether the domain and use of numerical
invariance should be stated more explicitly.

### IR-5 — Infinite refinement

**Correction applied.**

The F3 wording repeated “standard extension theorem” and left the measurable
domain implicit. F4 now specifies the countable cylinder algebra and the
standard path sigma-algebra for a finitely branching rooted tree.

**External-review target:** verify that the stated extension assumptions are
sufficient for the exact path-space claim.

### IR-6 — Static versus dynamic closure

**Result:** distinction remains valid.

Section 6 proves only static regrouping of \(W_\lambda\). Section 7 shows that
the centered update transports the required transform argument to
\(a\lambda\), so one fixed transform value need not determine its successor.

### IR-7 — Exact four-point witness

**Result:** independently recomputed exactly.

For the two rational probability vectors, both means equal \(3/2\), both
\(\lambda=\log2\) exponential moments equal \(15/32\), and the half-parameter
moments differ by

\[
\frac{5\sqrt2-7}{40}>0.
\]

The witness proves failure of closure for
\((\bar q_\mu,Q_\lambda)\) on the unrestricted finite class. It does not rule
out richer finite states or restricted invariant families.

### IR-8 — Occupancy and lumpability

**Result:** no contradiction found.

The manuscript distinguishes an occupancy-weighted macro kernel from strong
lumpability, under which block transition sums are independent of the
microstate inside each source block.

### IR-9 — Relative minimality

**Result:** scope is adequately qualified.

The tuple \((R,q,\mu,K,\pi)\) is called minimal only relative to the studied
operations and representation classes. Equivalent packaging, such as joint
flow replacing \((K,\pi)\), is explicitly allowed.

### IR-10 — Reference closure

**Correction applied.**

Four exact locations were closed. Aczél remains open because only the weighted
mean section range was verified, not the exact theorem page. Nagumo remains
the primary citation, so this is a bibliographic precision gate rather than a
missing mathematical dependency.

## Internal verdict

`NO_BLOCKING_ERROR_DETECTED_EXTERNAL_REVIEW_STILL_REQUIRED`

The absence of a detected internal blocking error is not evidence of
independent correctness. The external reviewer should focus on Targets 5–12 in
`MATH_AUDIT_TARGETS.md`.
