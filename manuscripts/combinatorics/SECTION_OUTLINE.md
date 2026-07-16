# Manuscript C — Section Outline

## 1. Introduction

**Purpose:** identify the encoding ambiguity and define the new combinatorial
question.

- Introduce reachability preorders of labeled digraphs.
- State that the classical count \(6942\) and the project count \(5234\)
  refer to different objects.
- State the exact edge-toggle statistic \(P_n\).
- List contributions without physical language.

## 2. Definitions and Encoding Levels

### 2.1 Loopless labeled digraphs and reflexive reachability

Define \(G=(V,E)\), \(\preceq_G\), SCC equivalence, and condensation order.

### 2.2 Complete labeled reachability preorder

Define \(C_{\mathrm{full}}(G)\) and prove that it retains the SCC partition and
quotient order.

### 2.3 Minimum-representative quotient-poset code

Define the active minimum set and the quotient order stored by the earlier
implementation.

### 2.4 Three equivalence levels

Separate:

1. complete labeled preorders;
2. minimum-representative codes;
3. unlabeled preorder classes.

## 3. Classical Count and Independent Reproduction

- Attribute
  \[
  N_{\mathrm{full}}(n)=\sum_kS(n,k)p(k).
  \]
- Reproduce \(N_{\mathrm{full}}(5)=6942\).
- Explain why exhaustive digraph enumeration is an independent implementation
  check, not proof of novelty.

## 4. Representative Encoding and Exact Count

### Proposition

\[
N_{\mathrm{rep}}(n)
=
\sum_k\binom{n-1}{k-1}p(k).
\]

- Prove feasibility of every representative set containing vertex 0.
- Give the shifted-binomial generating-function observation.
- Prove non-injectivity by an explicit pair.
- Explain precisely which SCC membership information is lost.

## 5. Exact n=5 Fiber Structure

- Present the fiber-size distribution.
- Quantify the 1,708 collapsed distinctions.
- Identify possible combinatorial questions about maximal fibers and their
  structure.

## 6. Edge-Toggle Sensitivity

### 6.1 Definition

\[
P_n=
\frac{1}{n(n-1)2^{n(n-1)}}
\sum_{G,e}
\mathbf 1[C(G)\ne C(G\triangle e)].
\]

### 6.2 Exact small-n values

Present \(P_2,P_3,P_4,P_5\), ordered-pair counts, and reproducibility method.

### 6.3 Structural decomposition — blocking section

Separate toggles that:

1. create or destroy reachability without changing SCC membership;
2. fuse SCCs;
3. split SCCs;
4. alter quotient reachability with a fixed SCC partition.

This section must contain a theorem, recurrence, bound, or exact subclass
before submission.

## 7. Discussion and Open Problems

- Relation to dynamic reachability, strong bridges, and average sensitivity.
- No physical interpretation.
- Open problems for \(P_n\), fiber asymptotics, and encoding design.

## 8. Reproducibility

Point to A8.1, C1, contracts, hashes, and exact scripts without narrating the
audit chronology in the article body.
