# Appendix C. Restricted Closure and Transform Domain

## C.1 Gaussian invariant-family exception

Consider

\[
X_{t+1}=b+aX_t+\xi_t,
\]

where \(X_t\) is Gaussian and \(\xi_t\) is independent Gaussian noise. Then
\(X_{t+1}\) is Gaussian with

\[
m_{t+1}=b+am_t,
\qquad
v_{t+1}=a^2v_t+v_\xi.
\]

For a Gaussian law,

\[
Q_\lambda
=
-\lambda^{-1}\log E[e^{-\lambda X}]
=
m-\frac{\lambda}{2}v.
\]

Therefore mean and variance determine the full transform curve inside the
Gaussian invariant family.

**Proposition C.1 (conditional Gaussian closure).**  
Mean-variance closure is exact under affine dynamics when both the state and
independent innovations remain Gaussian.

This exception does not contradict the general nonclosure counterexample.
It adds an invariant-family assumption that removes the unresolved higher
cumulants. Non-Gaussian innovations regenerate higher cumulants according to

\[
\kappa_r(X_{t+1})
=
a^r\kappa_r(X_t)+\kappa_r(\xi_t),
\qquad r\ge2.
\]

Centering is a linear operation and does not by itself make a non-Gaussian
innovation law Gaussian.

## C.2 Exponential-moment domain

The existence of a finite variance does not guarantee that

\[
E[e^{-\lambda X}]
\]

is finite for nonzero \(\lambda\). Some heavy-tailed distributions have finite
variance but no moment-generating function away from the origin.

**Proposition C.2 (domain warning).**  
The score \(Q_\lambda\) is defined only on the side of the origin where the
corresponding exponential moment is finite. Finite variance alone is
insufficient.

The manuscript therefore uses finite-support distributions for the exact
nonclosure witness and states transform-domain assumptions whenever an
infinite law is discussed. Weak convergence or a central limit theorem also
does not, by itself, imply convergence of exponential moments; uniform
integrability or comparable tail control is required.
