# 9. Provisional Informational Architecture

## 9.1 Obstruction-driven construction

The previous sections do not derive a complete ontology. They identify
distinct information deficits that appear when a relational model is asked to
support particular operations. The resulting architecture is

\[
\mathcal M=(R,q,\mu,K,\pi).
\]

Each component is introduced for a separate reason:

\[
\begin{array}{lll}
R &:& \text{relational or ordinal structure},\\
q &:& \text{relative cardinal marks},\\
\mu &:& \text{additive refinement mass},\\
K &:& \text{conditional transition law},\\
\pi &:& \text{source occupancy for dynamic aggregation}.
\end{array}
\]

The word “provisional” is essential. The tuple is minimal only relative to the
operations and representation classes considered here. It is not proved to be
the unique smallest description among all possible mathematical formalisms.

## 9.2 The role of \(R\)

The relation \(R\) records the primitive relational content admitted by the
model. Depending on the application, it may encode reachability,
comparability, adjacency, precedence, or another binary structure. From \(R\)
one may derive invariant ordinal observables such as chains, intervals,
quotients, and automorphism classes.

Order-only identifiability shows what \(R\) does not determine. Strictly
monotone recalibration can leave \(R\) unchanged while altering latent
marginal scales and densities. Therefore a preferred cardinal coordinate,
sampling measure, or numerical spacing cannot be introduced merely by
relabeling an order statistic as a metric quantity.

The architecture does not claim that every relation must be primitive. In a
more complete theory, \(R\) might be generated dynamically or derived from
another object. The present point is informational: once \(R\) is the observed
input, its equivalence classes limit what can be recovered from it.

## 9.3 The role of \(q\)

The mark \(q\) supplies cardinal contrasts not measurable from \(R\) alone.
It is introduced as additional information, not as a theorem that every
relational system possesses such a scalar field.

Only relative \(q\)-structure is used without calibration. If the operational
constructions depend on differences or centered values, then the global shift

\[
q_i\mapsto q_i+c
\]

is redundant. This is a gauge contract arising from the definitions.
It does not establish a physical gauge symmetry.

The scale of \(q\) is a separate issue. In exponential kernels, a rescaling of
\(q\) can be absorbed into the coupling parameter before a standardization
convention is fixed. After standardization, the remaining dimensionless
parameter may become statistically identifiable, but it remains underived.
Thus \(q\) adds cardinal information while leaving calibration as an open
problem.

## 9.4 The role of \(\mu\)

The mass \(\mu\) supplies additive multiplicity and refinement semantics.
Without it, exact clones can change normalized weights merely by changing the
number of listed alternatives. Relation plus equal marks cannot decide whether
a repeated representation is descriptive or ontically multiplicative.

Once \(\mu\) is supplied, exact conservative refinements preserve the marked
measure

\[
\nu=\sum_i\mu_i\delta_{q_i},
\]

and additive statistics become path-independent. Consistent branch fractions
take the ratio form \(W(B)/W(A)\), but consistency does not select the
underlying terminal weights or split fractions.

The architecture therefore distinguishes the existence of an additive measure
from the origin of that measure. A later empirical or physical theory would
need to say what operational procedure assigns \(\mu\).

## 9.5 The role of \(K\)

The kernel \(K\) specifies conditional transitions. It is not determined by
the existence of \(R\), \(q\), and \(\mu\) alone. Locality and invariance
principles can restrict a family of kernels without selecting a unique member.
Additional axioms, calibration, data, or a dynamical law are required.

The exponential form is useful because \(q\)-contrasts appear directly in
log-odds and because the corresponding partition sums admit exact static
messages. These properties make it a mathematically coherent candidate. They
do not prove that the kernel is fundamental or physical.

The dynamic nonclosure result further separates the microscopic kernel from a
putative scalar macrostate. Exact static aggregation of an exponential score
does not guarantee that the same score evolves autonomously.

## 9.6 The role of \(\pi\)

The occupancy \(\pi\) records how probability mass is distributed over source
states at the time of aggregation. A microscopic kernel and a partition do not
generally determine a unique macro transition, because averaging a row of
\(K\) requires source weights. Strong lumpability can remove this dependence,
but it is a restrictive structural condition rather than a generic fact.

By carrying

\[
F_{ij}=\pi_iK_{ij},
\]

one obtains an additive flow that aggregates exactly. This explains why
\(\pi\) is not redundant with \(K\): \(K\) is conditional, whereas \(\pi\)
specifies the condition under which transitions are sampled. Nor is \(\pi\)
automatically identical to \(\mu\). A refinement mass and a dynamical
occupancy can coincide in a special model, but the formal roles are different.

## 9.7 Non-reduction statements

Within the representation classes studied, the following reductions are not
available without extra assumptions.

### \(R\not\Rightarrow q\)

Order-preserving transformations can alter latent cardinal quantities while
leaving \(R\) unchanged.

### \((R,q)\not\Rightarrow\mu\)

Marked relational clones admit incompatible multiplicity interpretations.

### \((R,q,\mu)\not\Rightarrow K\)

Symmetry, locality, and standardized scores leave multiple admissible
transition laws unless stronger choice principles or empirical calibration are
added.

### \((K,\mathcal P)\not\Rightarrow K^{\mathrm{macro}}\)

A partitioned microscopic kernel does not determine a unique macro kernel
without occupancy or lumpability.

These are conditional non-reduction statements. They do not prove logical
independence in every conceivable formalism, and they do not forbid a future
theory from deriving several components from a common deeper object.

## 9.8 Obstruction map

The architecture can be summarized as a dependency map:

\[
\begin{array}{lll}
\text{monotone-order ambiguity}
&\Longrightarrow&
\text{additional cardinal structure }q,\\[2mm]
\text{clone/multiplicity ambiguity}
&\Longrightarrow&
\text{additive mass }\mu,\\[2mm]
\text{kernel underdetermination}
&\Longrightarrow&
\text{explicit transition law }K,\\[2mm]
\text{scalar dynamic nonclosure}
&\Longrightarrow&
\text{richer macrostate or invariant-family assumption},\\[2mm]
\text{macro-transition ambiguity}
&\Longrightarrow&
\text{occupancy }\pi\text{ or lumpability}.
\end{array}
\]

Some arrows summarize classical mathematics; others summarize
project-specific exact identities and counterexamples. The contribution of
the map is organizational: it keeps these logical roles separate and prevents
a successful construction in one layer from being promoted into a conclusion
about another.

## 9.9 Relative minimality

A precise minimality claim must name its comparison class. The tuple
\((R,q,\mu,K,\pi)\) is sufficient to formulate the operations emphasized here:

- ordinal relational observables from \(R\);
- relative cardinal comparisons from \(q\);
- conservative refinement and projective weighting from \(\mu\);
- microscopic conditional evolution from \(K\);
- occupancy-weighted dynamic aggregation from \(\pi\).

Removing a component reintroduces at least one documented obstruction within
the present construction. This is a useful relative-minimality statement.
It is not a uniqueness theorem for mathematical ontology.

Alternative representations may package the same information differently.
For example, one could carry the joint flow \(F\) instead of the pair
\((K,\pi)\) when only one-step aggregation is required. A measure-valued state
may combine \(q\) and \(\mu\). A richer stochastic process may derive
occupancy from its history. Such reformulations should be compared by
information content and operational sufficiency, not by symbol count.

## 9.10 Boundary and open bridges

The architecture remains formal. The current results do not derive:

- a physical spacetime;
- calibrated temporal or spatial distances;
- curvature or gravitational dynamics;
- the physical origin of \(q\);
- a unique or empirically measured \(\mu\);
- a fundamental value of \(\lambda\);
- a preferred microscopic kernel \(K\);
- an empirical occupancy law \(\pi\).

The absence of these bridges is not hidden in terminology such as “effective
geometry” or “free energy.” Any future physical interpretation must specify a
measurement map from empirical data to the formal components and must survive
prospective tests against alternatives and null models.

The current achievement is more limited but more secure:

\[
\boxed{
\text{the model's informational requirements are stated explicitly, and the
known closures and nonclosures are separated by operation.}
}
\]

This architecture provides a controlled starting point for further theory. It
does not complete that theory.
