# Manuscript F — Section Outline

## 1. Introduction

- Ask which informational structures are required before a relational model
  can support quantitative and dynamical operations.
- State the obstruction-driven method.
- Introduce the provisional architecture
  \[
  (R,q,\mu,K,\pi).
  \]
- Distinguish mathematical necessity within the studied operations from
  physical derivation.

## 2. Order-Only Identifiability

### 2.1 Relational observation

Define the order/relation object \(R\).

### 2.2 Monotone recalibration

Prove that strictly coordinatewise monotone transforms preserve the induced
product order.

### 2.3 Copula versus marginals

Attribute the copula result: continuous marginal recalibration does not change
the induced order law for fixed dependence structure.

### 2.4 Identifiability conclusion

State the conditional no-go: deterministic order-only observables cannot
recover quantities varying within the same order-equivalence class.

**Claims:** MF-R023–MF-R025.

## 3. Additional Quantitative Structure \(q\)

- Introduce \(q\) as additional cardinal information, not derived from \(R\).
- Define global offset gauge.
- Separate relative contrasts from calibrated physical scale.
- Exclude effective geometry from this manuscript.

**Claims:** MF-R028–MF-R029.

## 4. Operational Kernels and Parameter Status

### 4.1 Exponential candidate kernel

Introduce the softmax/logit form as a classical candidate operationalization.

### 4.2 Raw-scale degeneracy

Show the joint degeneracy between raw \(q\) scale and coupling strength.

### 4.3 Kernel underdetermination

Show that locality and affine standardization alone leave infinitely many
positive kernel functions.

### 4.4 Classical exponential selection

Attribute Luce/IIA/functional-equation selection of the exponential family.

### 4.5 Status of \(\lambda\)

Distinguish removable raw parameterization, standardized identifiability, and
physical underivation.

### 4.6 Context–scale lemma

Use MF-R036 only as a short measurement-invariance lemma.

**Claims:** MF-R031–MF-R036.

## 5. Measure, Multiplicity, and Refinement

### 5.1 Why relation plus \(q\) is insufficient

Use descriptive-clone versus ontic-copy indistinguishability to motivate a
separate mass/refinement semantics.

### 5.2 Finite additive measure

Attribute the finite-tree extension.

### 5.3 Infinite projective refinement

Attribute the extension theorem and separate atomicity from terminality.

### 5.4 Projective branch fractions

Derive conditional ratios once additive weights are supplied.

### 5.5 Remaining underdetermination

Consistency determines combination rules, not terminal weights or their
physical meaning.

**Claims:** MF-R037, MF-R039–MF-R045.  
**Appendix:** MF-R038.

## 6. Static Exponential Aggregation

Define

\[
Q_\lambda(q,\mu)
=
-\frac1\lambda\log\sum_i\mu_i e^{-\lambda q_i}.
\]

- Attribute log-sum-exp/quasi-arithmetic associativity.
- Prove exact static aggregation when mass and score are passed.
- State classical affine covariance.
- Do not use thermodynamic terminology as a physical identification.

**Claims:** MF-R044, MF-R046, MF-R047.

## 7. Dynamic Transport and Nonclosure

### 7.1 Centered contraction

Define
\[
q_i'=\bar q+a(q_i-\bar q).
\]

### 7.2 Transport identity

\[
Q_\lambda'
=
(1-a)\bar q+aQ_{a\lambda}.
\]

Describe this as a project-specific exact corollary of classical affine
covariance.

### 7.3 Exact scalar nonclosure witness

Use the C2 four-point distributions with equal mean and equal
\(Q_{\log2}\), but unequal \(Q_{\frac12\log2}\).

### 7.4 Closure hierarchy

- one fixed-\(\lambda\) score: not generally closed;
- mean plus full \(Q(\lambda)\) curve: sufficient for the declared deterministic
  contraction;
- invariant finite-dimensional family: possible conditional closure;
- finite cumulant truncation: approximation, not exact general closure.

**Claims:** MF-R048–MF-R050.  
**Appendix:** MF-R051.

## 8. Observable-Relative Coarse-Graining

### 8.1 No universal scalar summary

Different observables select different exact summaries.

### 8.2 Exponential-kernel sufficiency

Show that \(Q_\lambda\) preserves the declared kernel under static grouping.

### 8.3 Occupancy obstruction

Attribute the Markov aggregation fact that a micro kernel and a partition do
not determine a macro kernel without source occupancy or lumpability.

### 8.4 Exact flow aggregation

Define \(F_{ij}=\pi_iK_{ij}\) and aggregate flows exactly.

**Claims:** MF-R058, MF-R059, MF-R061–MF-R063.  
**Appendix:** MF-R060.

## 9. Provisional Informational Architecture

Present

\[
(R,q,\mu,K,\pi)
\]

as a dependency map:

- \(R\): relational/ordinal structure;
- \(q\): relative cardinal marks;
- \(\mu\): additive refinement mass;
- \(K\): transition law;
- \(\pi\): occupancy needed for dynamic aggregation.

State explicitly that this is minimal only relative to the obstructions and
operations studied.

**Claims:** MF-R067–MF-R068.

## 10. Scope and Physical Boundary

State what has not been derived:

- spacetime;
- calibrated time or distance;
- curvature or gravity;
- physical \(\lambda\);
- origin or empirical mapping of \(q,\mu,\pi\).

**Claim:** MF-R069.

## Appendices and Supplement

- Appendix A: equivariance and external calibration.
- Appendix B: refinement singular boundary.
- Appendix C: Gaussian restricted-family exception and exponential-moment
  domain warning.
- Appendix D: median nonclosure counterexample.
- Supplement: broader noise-law and universality audits.
