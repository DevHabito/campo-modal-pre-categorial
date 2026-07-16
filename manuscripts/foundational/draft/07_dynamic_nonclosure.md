# 7. Dynamic Transport and Nonclosure

## 7.1 Exponential effective score

Let \(q_1,\ldots,q_m\in\mathbb R\) carry positive normalized masses
\(\mu_1,\ldots,\mu_m\), with \(\sum_i\mu_i=1\). For
\(\lambda\ne0\), define

\[
Q_\lambda(q,\mu)
=
-\frac1\lambda
\log\left(
\sum_{i=1}^{m}\mu_i e^{-\lambda q_i}
\right).
\]

Up to sign conventions, this is the exponential certainty equivalent or
entropic transform familiar from exponential utility and convex risk
functionals [@FollmerSchied2002]. The present use is formal: no identification
with physical free energy is made.

The score is translation covariant:

\[
Q_\lambda(q+c,\mu)
=
Q_\lambda(q,\mu)+c.
\]

More generally, for \(a>0\),

\[
Q_\lambda(aq+c,\mu)
=
c+aQ_{a\lambda}(q,\mu).
\]

This identity is a direct algebraic property of the log-Laplace transform. Its
importance here is that changing the scale of \(q\) transports the parameter
at which the transform must be evaluated.

## 7.2 Centered affine contraction

Consider the deterministic update

\[
q_i'
=
\bar q+a(q_i-\bar q),
\qquad
0<a<1,
\]

where

\[
\bar q=\sum_i\mu_i q_i.
\]

Equivalently,

\[
q_i'=(1-a)\bar q+aq_i.
\]

**Proposition 7.1 (transport identity).**  
Under this update,

\[
Q_\lambda(q',\mu)
=
(1-a)\bar q+aQ_{a\lambda}(q,\mu).
\]

**Proof.** Apply affine covariance with scale \(a\) and shift
\(c=(1-a)\bar q\). \(\square\)

The proposition is exact, but it is not an independent new transform theorem.
It is a model-specific dynamical corollary of classical affine covariance.
Its substantive consequence is that a fixed observational value
\(Q_\lambda\) at the next step depends on the previous score at
\(a\lambda\), not only at \(\lambda\).

## 7.3 An exact scalar nonclosure witness

We now show that the mean and one fixed-\(\lambda\) score do not generally form
an autonomous macrostate.

Take support

\[
q\in\{0,1,2,3\},
\]

parameter

\[
\lambda=\log 2,
\]

and contraction factor

\[
a=\frac12.
\]

Define two probability vectors

\[
p^+
=
\left(
\frac9{40},
\frac7{20},
\frac18,
\frac3{10}
\right)
\]

and

\[
p^-
=
\left(
\frac{11}{40},
\frac3{20},
\frac38,
\frac15
\right).
\]

Both are positive and normalized. Their means are equal:

\[
\sum_{k=0}^{3}k\,p_k^+
=
\sum_{k=0}^{3}k\,p_k^-
=
\frac32.
\]

At \(\lambda=\log2\), we have \(e^{-\lambda k}=2^{-k}\), and direct
calculation gives

\[
\sum_{k=0}^{3}p_k^+2^{-k}
=
\sum_{k=0}^{3}p_k^-2^{-k}
=
\frac{15}{32}.
\]

Therefore

\[
Q_{\log2}(p^+)=Q_{\log2}(p^-).
\]

The centered contraction with \(a=\frac12\) requires the prior transform at

\[
a\lambda=\frac12\log2.
\]

At this parameter,

\[
\sum_{k=0}^{3}p_k^+2^{-k/2}
=
\frac{23}{80}+\frac{\sqrt2}{4},
\]

whereas

\[
\sum_{k=0}^{3}p_k^-2^{-k/2}
=
\frac{37}{80}+\frac{\sqrt2}{8}.
\]

The difference is

\[
\frac{5\sqrt2-7}{40}>0.
\]

Hence

\[
Q_{\frac12\log2}(p^+)
\ne
Q_{\frac12\log2}(p^-).
\]

Applying Proposition 7.1 yields

\[
Q_{\log2}'(p^+)
\ne
Q_{\log2}'(p^-).
\]

**Proposition 7.2 (failure of fixed-score closure).**  
On the unrestricted class of finite marked distributions, the macrostate

\[
(\bar q,Q_\lambda)
\]

does not generally determine the next \(Q_\lambda\) under the centered affine
contraction.

The witness is exact. It does not rely on numerical optimization, random
search, or a finite tolerance. It is also deliberately narrow: it proves
nonclosure on the unrestricted finite-distribution class, not on every
parametric subfamily.

## 7.4 Why one transform value is insufficient

The score \(Q_\lambda\) is a single evaluation of the log-Laplace transform.
One value imposes one nonlinear constraint on the distribution. Even after
the mean is fixed, many finite distributions can satisfy that same constraint
while differing at another transform parameter. By contrast, a complete
Laplace-transform curve, under its standard domain conditions, can determine a
distribution; uniqueness results make clear that a sufficiently rich set of
transform values contains qualitatively more information than one evaluation
[@LinDou2021].

The cumulant expansion illustrates the same hierarchy. When the expansion is
valid,

\[
Q_\lambda
=
\kappa_1
-\frac{\lambda}{2}\kappa_2
+\frac{\lambda^2}{6}\kappa_3
-\frac{\lambda^3}{24}\kappa_4
+\cdots.
\]

A fixed value at one \(\lambda\) does not separately determine the cumulants.
Mean-variance closure is therefore not exact in general. Higher cumulants
contribute at finite \(\lambda\), and a finite truncation is an approximation
unless an invariant family independently forces the higher terms to be
functions of finitely many parameters. This is the familiar closure problem:
a reduced set of observables can evolve through unresolved information
[@Kuehn2016].

## 7.5 Closure hierarchy

The update admits a precise hierarchy of closure statements.

### One fixed score

A single \(Q_\lambda\), even together with \(\bar q\), is not generally closed,
as Proposition 7.2 shows.

### The full transform curve

If the macrostate carries the mean and the entire function

\[
\lambda\mapsto Q_\lambda,
\]

then the deterministic contraction is closed:

\[
Q_\lambda'
=
(1-a)\bar q+aQ_{a\lambda}.
\]

The update acts by a shift of value and a rescaling of the curve's argument.

### Restricted invariant families

A finite-dimensional closure may exist when the microscopic distribution is
known to remain in an invariant parametric family. For example, affine
transformations preserve Gaussianity, and for a Gaussian distribution

\[
Q_\lambda
=
\bar q-\frac{\lambda}{2}\sigma^2.
\]

In that restricted family, mean and variance determine the whole curve.
This conditional exception does not restore general closure; it identifies the
extra assumption that makes finite closure possible.

### Approximate moment closure

A finite cumulant truncation can be useful for small \(\lambda\) or in regimes
where higher cumulants are controlled. It must be labeled as an approximation,
not as the exact state of the unrestricted dynamics.

## 7.6 Static sufficiency is not dynamic autonomy

The same score can be an exact static message and an incomplete dynamic state.
For a fixed partition sum,

\[
W_\lambda
=
\sum_i\mu_i e^{-\lambda q_i},
\]

the pair \((\sum_i\mu_i,Q_\lambda)\) aggregates exactly across a hierarchy.
That static property says that the message preserves one declared observable
under regrouping. It does not say that the message contains all information
needed by a future update.

This distinction is central:

\[
\boxed{
\text{exact static coarse-graining}
\not\Rightarrow
\text{autonomous macrodynamics}.
}
\]

The result is mathematical and model-conditional. It does not identify
\(Q_\lambda\) as a thermodynamic state variable, derive the contraction as a
law of nature, or establish a closed physical dynamics.
