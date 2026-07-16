# 1. Introduction

Relational models often begin with a sparse primitive: a set of entities and a
relation among them. From that starting point, one may wish to define cardinal
comparisons, assign multiplicities, specify transition probabilities, or
construct macroscopic descriptions. These operations are not interchangeable.
Each requires information that may or may not be present in the original
relation.

This article studies that dependency problem. The question is not whether one
particular relational model is physically correct. It is:

> Which informational structures must be supplied before a relational
> description can support the quantitative and dynamical operations assigned
> to it?

The method is obstruction-driven. A new component is introduced only after an
invariance argument, identifiability result, underdetermination construction,
or closure counterexample shows that the previous representation is
insufficient for a declared operation. The resulting inventory is

\[
\mathcal M=(R,q,\mu,K,\pi),
\]

where \(R\) is relational or ordinal structure, \(q\) is an additional
cardinal mark, \(\mu\) is additive mass, \(K\) is a conditional transition
kernel, and \(\pi\) is source occupancy for dynamic aggregation. This tuple is
a provisional informational architecture. It is not asserted to be a unique
ontology or a derivation of physical spacetime.

The first obstruction concerns order-only identifiability. Strict
coordinatewise monotone transformations can preserve an induced finite order
while changing latent marginal scales and densities. Under continuous
marginals, the law of a coordinatewise order depends at most on the copula,
not on the marginal calibrations. Consequently, a deterministic order-only
estimator cannot recover targets that vary inside the same
order-equivalence class.

A separate mark \(q\) can add cardinal information only when its marked law is
not itself determined by \(R\). Operational meaning additionally requires a
declared observation kernel sensitive to gauge-invariant \(q\)-contrasts.
Locality, relabeling equivariance, and positive-affine standardization do not
select a unique kernel: an infinite family remains. Classical
difference-based odds and maximum-entropy arguments can select an exponential
family under stronger assumptions, but they do not determine a unique
physical coupling strength.

Multiplicity creates a second obstruction. Relation plus marks cannot
distinguish a descriptive refinement from the addition of ontically distinct
copies when both generate the same marked representation. An additive mass
\(\mu\) supplies the missing refinement semantics. Once masses are supplied,
conservative cloning, finite regrouping, and projective branch fractions can
be handled exactly; consistency constrains how weights combine but not which
weights should be used.

For a fixed parameter \(\lambda\), the additive exponential weight

\[
W_\lambda(B)=\sum_{i\in B}\mu_i e^{-\lambda q_i}
\]

admits the exact block message

\[
(M_B,Q_\lambda(B)),
\qquad
M_B=\sum_{i\in B}\mu_i,
\]

where

\[
Q_\lambda(B)
=
-\lambda^{-1}
\log\left(
\frac{W_\lambda(B)}{M_B}
\right).
\]

This is classical log-sum-exp algebra applied to the present architecture.
Its exact static associativity does not imply autonomous macrodynamics. Under
the centered contraction

\[
q_i'=\bar q_\mu+a(q_i-\bar q_\mu),
\]

affine covariance gives

\[
Q_\lambda'
=
(1-a)\bar q_\mu+aQ_{a\lambda}.
\]

The article provides an exact four-point counterexample showing that two
finite distributions can have the same mass-normalized mean and the same
\(Q_\lambda\), yet different \(Q_{a\lambda}\) and therefore different next
\(Q_\lambda\). Thus one fixed-\(\lambda\) score is not a generally closed
dynamic state.

A third distinction appears in coarse-graining. The exact message depends on
the observable to be preserved. Arithmetic means preserve first moments;
exponential scores preserve exponential weights; other targets require other
messages. For Markov dynamics, a microscopic kernel and a partition do not
generally determine a unique macro kernel without source occupancy or a
lumpability condition. Carrying the joint flow
\(F_{ij}=\pi_iK_{ij}\) restores exact aggregation.

The contribution is therefore a structured separation of informational roles.
Several ingredients are classical: copula invariance, measurement-scale
arguments, exponential choice models, additive measure extension,
quasi-arithmetic means, and Markov lumpability. The project-specific value
lies in the obstruction map that organizes them, the explicit separation of
static sufficiency from dynamic autonomy, and the exact nonclosure witness for
the chosen centered contraction.

The article proceeds as follows. Section 2 establishes the order-only
identifiability limit. Sections 3 and 4 introduce \(q\), its gauge contract,
and the status of operational kernels and their parameters. Section 5 treats
measure, multiplicity, and refinement. Sections 6 and 7 separate exact static
aggregation from dynamic closure. Section 8 develops observable-relative
coarse-graining and occupancy-weighted flow aggregation. Section 9 assembles
the provisional architecture. Section 10 states the scope, contribution, and
open bridges. Appendices record equivariance, boundary cases, restricted
closure, transform-domain conditions, and a nondecomposable median example.
