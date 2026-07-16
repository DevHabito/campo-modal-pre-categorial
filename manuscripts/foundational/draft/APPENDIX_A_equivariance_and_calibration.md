# Appendix A. Equivariance and External Calibration

## A.1 Endogenous equivariance

Let a group \(G\) act on a state space \(\mathcal X\) and observation space
\(\mathcal Y\). Let \(P(x,\cdot)\) be a Markov transition kernel on
\(\mathcal X\), and let \(O:\mathcal X\to\mathcal Y\) be an observation map.
Assume

\[
P(gx,gA)=P(x,A)
\]

for every measurable \(A\subseteq\mathcal X\) and every \(g\in G\), and

\[
O(gx)=gO(x).
\]

If two initial states differ only by the group action, their evolved laws
remain related by that action at every finite time.

**Proposition A.1 (equivariant evolution preserves equivalence).**  
Purely endogenous evolution whose initial law, transition kernel, and
observation map are equivariant cannot select a preferred representative from
one group orbit.

**Proof.** The one-step statement follows directly from kernel equivariance.
Induction gives the same relation for every finite-time law. Applying the
equivariant observation map preserves the orbit relation in observation space.
\(\square\)

The result is conditional. Non-equivariant boundary conditions, calibrated
inputs, asymmetric noise laws, or new observables can break the equivalence.

## A.2 A calibrated witness

Let \(x\) and \(gx\) be observationally equivalent under the original
relational observation. Introduce an additional mark \(c:\mathcal X\to
\mathbb R\) satisfying

\[
c(gx)\ne c(x)
\]

for at least one pair in the orbit, and suppose \(c\) is externally calibrated
rather than computed equivariantly from the original relation. Then the
enriched observation

\[
\widetilde O(x)=(O(x),c(x))
\]

distinguishes that pair.

**Proposition A.2 (calibration can break degeneracy).**  
An additional non-invariant calibrated observable can separate states that are
indistinguishable under an equivariant order-only observation.

This is a constructive possibility, not a derivation of the required
calibration. The main text therefore treats calibrated marks as possible
bridges rather than as consequences of relational dynamics.
