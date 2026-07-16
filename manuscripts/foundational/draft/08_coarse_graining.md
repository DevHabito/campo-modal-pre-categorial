# 8. Observable-Relative Coarse-Graining

## 8.1 Coarse-graining as a preservation problem

Let \(X\) be a finite microscopic state space and let

\[
\mathcal P=\{B_1,\ldots,B_r\}
\]

be a partition into macrostates. A coarse-graining map is not determined by
the partition alone. It must specify which microscopic observables or
dynamical predictions are to be preserved.

For a scalar mark \(q\) with masses \(\mu\), different targets select different
messages:

- the weighted arithmetic mean preserves the first moment;
- the exponential effective score preserves an exponential partition sum;
- the minimum preserves an extremal value;
- a quantile preserves a rank-based location but generally not an additive
  message.

There is therefore no reason to expect one scalar summary to be exactly
sufficient for every observable.

## 8.2 Regular decomposable means

A weighted quasi-arithmetic mean has the form

\[
M_f(q;\mu)
=
f^{-1}\left(
\frac{\sum_i\mu_i f(q_i)}
{\sum_i\mu_i}
\right),
\]

where \(f\) is continuous and strictly monotone. Such means are hierarchically
decomposable when each block transmits its total mass and its block mean.

Classical characterization results associated with Kolmogorov, Nagumo, and
Aczél show how regularity, decomposability, and invariance assumptions restrict
the generator [@Kolmogorov1930; @Nagumo1930; @Aczel1966]. In the
translation-covariant class relevant here,

\[
M_f(q+c;\mu)=M_f(q;\mu)+c,
\]

the regular generators reduce, up to equivalent affine transformations, to
the affine family and the exponential family. These yield, respectively, the
weighted arithmetic mean and log-sum-exp means.

This characterization does not select one universal mean. It leaves at least
two distinct families because they preserve different structures.

## 8.3 Static messages depend on the observable

Section 6 proved that the pair

\[
(M_B,Q_\lambda(B))
\]

is an exact hierarchical message for the exponential weight
\(W_\lambda(B)\). By contrast, the weighted arithmetic mean is exact for the
first moment. Neither message is universally sufficient.

The distinction can be stated without repeating the aggregation proof. If two
blocks have the same first moment but different exponential weight, an
arithmetic-mean message preserves the first target and loses the second. If
they have the same \(Q_\lambda\) but different means or different
\(Q_\eta\) for \(\eta\ne\lambda\), the exponential message preserves only the
declared transform value.

Appendix D gives an exact example showing that total mass plus weighted median
is not a closed hierarchical message. Robustness, cardinality, and
decomposability are therefore separate properties.

## 8.4 Dynamic aggregation and source occupancy

Now let \(K\) be a row-stochastic microscopic transition kernel:

\[
K_{ij}\ge0,
\qquad
\sum_jK_{ij}=1.
\]

For source block \(A\) and destination block \(B\), the probability of moving
from \(A\) to \(B\) depends on which microscopic state inside \(A\) is
occupied. If

\[
\rho(i\mid A)
\]

is the conditional source occupancy, then

\[
K^{\mathrm{macro}}_{AB}
=
\sum_{i\in A}\rho(i\mid A)
\sum_{j\in B}K_{ij}.
\]

Two different occupancies on the same microscopic kernel and the same
partition can produce different macro rows. Therefore \(K\) and
\(\mathcal P\) alone do not generally determine a unique Markovian macro
kernel.

There is one important exception. If, for every pair of source states
\(i,i'\in A\),

\[
\sum_{j\in B}K_{ij}
=
\sum_{j\in B}K_{i'j}
\]

for every destination block \(B\), then the macro row is independent of
\(\rho\). This is the classical strong lumpability condition
[@KemenySnell1960]. In the absence of such a condition, occupancy is required.

The obstruction is informational, not metaphysical. A partition tells us
which states are grouped; it does not tell us how probability mass is
distributed among the grouped source states at the moment of transition.

## 8.5 Exact flow aggregation

Let a global occupancy distribution \(\pi\) be supplied, with

\[
\pi_i\ge0,
\qquad
\sum_i\pi_i=1.
\]

Define the joint one-step flow

\[
F_{ij}=\pi_iK_{ij}.
\]

For macro blocks \(A,B\), define

\[
\pi_A=\sum_{i\in A}\pi_i
\]

and

\[
F_{AB}
=
\sum_{i\in A}
\sum_{j\in B}
F_{ij}.
\]

When \(\pi_A>0\), set

\[
K^{\mathrm{macro}}_{AB}
=
\frac{F_{AB}}{\pi_A}.
\]

**Proposition 8.1 (exact occupancy-weighted aggregation).**  
The macro kernel above equals direct microscopic aggregation with the
conditional occupancy

\[
\rho(i\mid A)=\frac{\pi_i}{\pi_A}.
\]

**Proof.**

\[
\frac{F_{AB}}{\pi_A}
=
\frac1{\pi_A}
\sum_{i\in A}\sum_{j\in B}\pi_iK_{ij}
=
\sum_{i\in A}
\frac{\pi_i}{\pi_A}
\sum_{j\in B}K_{ij}.
\qquad\square
\]

Joint flow is additive under further regrouping, so it provides an exact
dynamic message. However, this positive construction requires \(\pi\).
The mathematics does not supply the initial occupancy, its evolution beyond
the declared kernel, or a physical interpretation.

## 8.6 Static and dynamic sufficiency are different

The static exponential message and the dynamic flow message solve different
problems.

For static aggregation, the relevant additive object is

\[
W_B=\sum_{i\in B}\mu_i e^{-\lambda q_i}.
\]

For dynamic aggregation, the relevant additive object is

\[
F_{AB}
=
\sum_{i\in A,j\in B}\pi_iK_{ij}.
\]

Neither can be substituted for the other without further assumptions. A
measure \(\mu\) used to encode refinement multiplicity need not equal a
time-dependent occupancy \(\pi\). A kernel \(K\) defines conditional
transitions but not the source distribution with which those transitions are
averaged.

This yields the organizing principle of the section:

\[
\boxed{
\text{a coarse-graining variable is exact only relative to a declared
observable or dynamics.}
}
\]

The principle does not rule out a richer common state representation capable
of preserving several observables simultaneously. It rules out calling one
scalar “the” coarse-grained value without specifying the preservation
contract.
