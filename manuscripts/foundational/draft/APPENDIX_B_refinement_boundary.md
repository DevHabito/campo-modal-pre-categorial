# Appendix B. Nondegeneracy Boundary of Weighted Standardization

Let positive masses \(\mu_i\) have total mass

\[
M=\sum_i\mu_i.
\]

Define

\[
\bar q_\mu
=
\frac1M\sum_i\mu_iq_i
\]

and

\[
s_\mu^2
=
\frac1M\sum_i\mu_i(q_i-\bar q_\mu)^2.
\]

When \(s_\mu>0\), the standardized values are

\[
z_i=\frac{q_i-\bar q_\mu}{s_\mu}.
\]

## B.1 Continuity inside the nondegenerate domain

For a fixed context with \(s_\mu>0\), adding a bounded-score alternative of
mass \(\varepsilon\) changes \(M\), \(\bar q_\mu\), \(s_\mu\), the
standardized scores, and any continuous normalized positive kernel
continuously as \(\varepsilon\to0\).

Thus conservative small-mass refinements are stable away from the singular
boundary.

## B.2 Failure of uniform stability

The convergence is not uniform as the original variance tends to zero. At

\[
s_\mu=0,
\]

all marks coincide and the standardized representation is undefined.
Moreover, an arbitrarily small mass at a separated score can generate
order-one standardized contrasts.

For example, begin with unit mass at \(q=0\), and add mass
\(\varepsilon>0\) at \(q=1\). Then

\[
\bar q_\mu=\frac{\varepsilon}{1+\varepsilon},
\qquad
s_\mu^2=\frac{\varepsilon}{(1+\varepsilon)^2}.
\]

The standardized values are

\[
z_0=-\sqrt{\varepsilon},
\qquad
z_1=\frac{1}{\sqrt{\varepsilon}}.
\]

Although the added mass tends to zero, its standardized score diverges.
A nonlinear kernel of \(z\) can therefore change by order one or more near the
zero-variance boundary.

**Proposition B.1 (standardization boundary).**  
Weighted standardization is continuous under vanishing bounded mass on every
domain bounded away from zero variance, but it is undefined at zero variance
and is not uniformly stable as variance approaches zero.

The consequence is local: standardized contextual kernels require an explicit
nondegeneracy domain, a regularization rule, or a separate boundary
definition. It does not imply that all weighted coarse-graining is unstable.
