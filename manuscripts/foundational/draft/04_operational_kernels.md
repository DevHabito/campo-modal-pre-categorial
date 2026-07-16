# 4. Operational Kernels and Parameter Status

## 4.1 A local exponential witness

Let \(A_{ij}\in\{0,1\}\) indicate which transitions from state \(i\) to state
\(j\) are admissible, and let \(q_{ij}\) be a mark on those transitions. A
simple local observation model is

\[
K_\beta(i,j)
=
\frac{A_{ij}e^{-\beta q_{ij}}}
{\sum_k A_{ik}e^{-\beta q_{ik}}},
\]

whenever the denominator is positive. This is a multinomial-logit or softmax
kernel [@Luce1959; @McFadden1974].

For two admissible destinations \(j\) and \(k\) from the same source,

\[
\log\frac{K_\beta(i,j)}{K_\beta(i,k)}
=
-\beta(q_{ij}-q_{ik}).
\]

Thus observable log-odds recover local \(q\)-contrasts when \(\beta\) is known
and sufficient transition data are available. The identity provides a
mathematical witness that \(q\)-contrasts can be operationalized without
assigning meaning to the common row offset.

The kernel is not derived from the relational primitives. It is one declared
coupling. Its value is to make the inferential contract explicit.

Throughout this article, \(\beta\) denotes the strength of a declared
transition kernel, while \(\lambda\) denotes the parameter of the exponential
aggregation transform. They may be set equal in a model that intentionally
uses one exponential law for both purposes, but no such identification is
assumed by notation alone.

## 4.2 Gauge and raw-scale degeneracy

For any source-dependent shift \(c_i\),

\[
q_{ij}\mapsto q_{ij}+c_i
\]

multiplies every unnormalized weight in row \(i\) by the same factor
\(e^{-\beta c_i}\), which cancels under normalization. Therefore the local
kernel identifies only within-row contrasts.

There is also a raw-scale degeneracy. For \(a>0\),

\[
K_\beta(i,j;q)
=
K_{\beta/a}(i,j;aq+c_i).
\]

Without a calibrated unit for \(q\), the data identify the products
\(\beta(q_{ij}-q_{ik})\), not \(\beta\) and the raw \(q\)-scale separately.

**Lemma 4.1 (raw-score reparameterization).**  
In the local exponential kernel, positive rescaling of the raw score can be
exactly compensated by inverse rescaling of the coupling strength.

This is a standard parameterization degeneracy. It should not be described as
evidence that every version of \(\beta\) or \(\lambda\) is pure gauge. Once a
standardization convention fixes the admissible score representation, the
remaining parameter can become identifiable within that model.

## 4.3 Scale-free local kernels remain underdetermined

For each source \(i\), suppose the outgoing marks are nonconstant and define

\[
z_{ij}
=
\frac{q_{ij}-\bar q_i}{s_i}.
\]

For any strictly positive function \(f:\mathbb R\to(0,\infty)\), define

\[
K_f(i,j)
=
\frac{A_{ij}f(z_{ij})}
{\sum_k A_{ik}f(z_{ik})}.
\]

This family is local, relabeling-equivariant, and invariant under every
row-wise positive affine recalibration

\[
q_{ij}\mapsto a_iq_{ij}+b_i,
\qquad a_i>0.
\]

Yet different positive functions \(f\) generally produce different transition
probabilities on the same marked graph.

**Proposition 4.2 (kernel underdetermination).**  
Relational locality, relabeling equivariance, and positive-affine invariance of
standardized local scores do not select a unique transition law. They admit an
infinite family \(K_f\).

The proposition blocks a common shortcut. Removing units and enforcing
symmetry can restrict the admissible representation, but those requirements
alone do not derive an exponential kernel or any other unique physical law.

## 4.4 What IIA does and does not select

For a finite choice set \(S\), every normalized pointwise-weight model

\[
P(j\mid S)
=
\frac{f(z_j)}
{\sum_{k\in S}f(z_k)}
\]

satisfies

\[
\frac{P(j\mid S)}{P(k\mid S)}
=
\frac{f(z_j)}{f(z_k)}.
\]

The pairwise odds do not depend on alternatives outside the pair. Thus the
normalized pointwise representation has the independence-of-irrelevant-
alternatives property associated with Luce's choice framework
[@Luce1959]. IIA by itself does not force \(f\) to be exponential.

A stronger condition does. Suppose the odds ratio depends only on score
difference:

\[
\frac{f(x)}{f(y)}=g(x-y),
\]

where \(f\) and \(g\) are positive and continuous. Setting \(y=0\) expresses
\(f\) through \(g\), and comparison of three scores gives

\[
g(a+b)=g(a)g(b).
\]

The positive continuous solutions are

\[
g(t)=e^{-\lambda t},
\]

so

\[
f(z)=Ce^{-\lambda z}.
\]

**Proposition 4.3 (difference-based exponential selection).**  
A positive continuous pointwise choice representation whose odds depend only
on score difference belongs to the exponential family.

This is a classical functional-equation result within the Luce/logit
tradition. The project uses it as an attributed selection principle. It is not
a new derivation of multinomial logit, and it does not determine the numerical
value of \(\lambda\).

## 4.5 Maximum entropy selects a family conditional on a constraint

A second route begins with an optimization problem. Let \(z_j\) be supplied
scores and maximize Shannon entropy

\[
H(p)=-\sum_jp_j\log p_j
\]

subject to

\[
\sum_jp_j=1,
\qquad
\sum_jp_jz_j=m.
\]

The Lagrange stationary condition gives

\[
p_j
\propto
e^{-\lambda z_j}.
\]

Strict concavity yields a unique interior maximizer for a feasible constraint.
With a reference mass \(\mu_j\), maximizing relative entropy gives

\[
p_j
\propto
\mu_je^{-\lambda z_j}
\]

[@Jaynes1957; @Csiszar1975].

This construction selects the exponential family only after the score,
reference measure, and expected-score constraint have been declared. The
multiplier \(\lambda\) is fixed by the supplied numerical constraint \(m\).
Without a principle or observation that determines \(m\), maximum entropy does
not predict a unique strength.

## 4.6 The status of \(\lambda\)

The parameter has three distinct statuses that should not be conflated.

### Raw-score model

For uncalibrated raw scores, only the product of score scale and coupling
strength is identifiable. Numerical \(\lambda\) is representation-dependent.

### Standardized-score model

For a fixed nonconstant standardized score vector \(z\), suppose

\[
P_\lambda(j)=P_\eta(j)
\]

for all \(j\). Taking the ratio of two entries with \(z_j\ne z_k\) gives

\[
e^{-\lambda(z_j-z_k)}
=
e^{-\eta(z_j-z_k)},
\]

and hence

\[
\lambda=\eta.
\]

Thus \(\lambda\) is identifiable within the standardized model. Given
multinomial transition counts and nonconstant score rows, it can be estimated
statistically.

### Physical theory

Statistical identifiability is not physical derivation. A fitted parameter can
be unique in a declared model while its value remains unexplained by the
underlying theory. Neither the variance of a chosen noise law nor the existence
of exact coarse-graining fixes \(\lambda\). Exact exponential aggregation
holds for every admissible \(\lambda\), and a numerical expected-score
constraint determines \(\lambda\) only after that constraint is independently
supplied.

The safe conclusion is:

\[
\boxed{
\lambda\text{ may be identifiable and estimable after standardization, while
remaining underived.}
}
\]

## 4.7 Context–scale incompatibility

The tension between contextual normalization and cardinal stability can be
stated directly. Let \(D_S(x,y)\) be the numerical difference between scores
assigned to \(x\) and \(y\) in a finite context \(S\). Assume:

1. adding arbitrary alternatives leaves \(D_S(x,y)\) unchanged;
2. \(D(ax+b,ay+b)=D(x,y)\) for every \(a>0\);
3. \(D\) is continuous and \(D(x,x)=0\).

Extension stability removes dependence on the surrounding context.
Translation invariance gives

\[
D(x,y)=h(x-y).
\]

Scale invariance gives

\[
h(ad)=h(d)
\qquad
\text{for every }a>0.
\]

Hence \(h\) is constant on positive separations and constant on negative
separations. Continuity at zero and \(h(0)=0\) force both constants to vanish.

**Lemma 4.4 (context–scale lemma).**  
Under the assumptions above, the only continuous cardinal score difference is
the trivial one.

The lemma is an elementary consequence of standard interval-scale and
meaningfulness arguments [@LuceEtAl1990]. It does not say that interval-scale differences
are meaningless. Ordinary differences transform covariantly with the unit.
The incompatibility arises only when one simultaneously demands a nontrivial
cardinal difference, complete context-extension stability, and numerical
invariance under every positive change of unit.

Raw differences preserve extension stability but need a scale convention.
Local standardized scores remove positive-affine scale but depend on context.
Ranks are more invariant but ordinal. The framework therefore treats score
choice as an explicit modelling contract rather than as a consequence of
symmetry alone.

## 4.8 Kernel-selection boundary

The results of this section establish a hierarchy:

1. \(q\)-contrasts can be made operational by a declared kernel;
2. raw exponential kernels have a score-scale/coupling degeneracy;
3. scale-free local principles leave infinitely many kernels;
4. difference-based odds or a maximum-entropy constraint select an
   exponential family under additional assumptions;
5. neither route determines a unique physical \(\lambda\).

A coherent operational kernel is therefore possible without circularity, but
it is not automatically fundamental. The score representation, admissible
choice axioms, reference measure, constraint, and calibration remain part of
the model specification.

## 4.9 Transition to refinement and measure

Every normalized choice or transition model presupposes a rule for how
alternatives are weighted when a representation is refined. If one listed
alternative is replaced by several exact descriptions, assigning unit
coefficient to every listed item changes the normalized law. Kernel selection
therefore does not solve multiplicity.

The next section introduces an additive base mass \(\mu\) to separate
transition preference from representational counting. This additional
structure is required even when the functional form of the kernel has already
been fixed.
