# 6. Static Exponential Aggregation

## 6.1 Additive exponential weight

Let a finite marked system carry positive masses \(\mu_i\) and marks \(q_i\).
For a fixed nonzero parameter \(\lambda\), define the additive exponential
weight of a block \(B\) by

\[
W_\lambda(B)
=
\sum_{i\in B}\mu_i e^{-\lambda q_i}.
\]

For disjoint blocks \(B_1,\ldots,B_r\),

\[
W_\lambda\left(\bigsqcup_{a=1}^{r}B_a\right)
=
\sum_{a=1}^{r}W_\lambda(B_a).
\]

Consequently, the ratio

\[
p(B_a\mid A)
=
\frac{W_\lambda(B_a)}{W_\lambda(A)}
\]

is normalized for every partition of \(A\), and nested branch probabilities
are independent of regrouping. This is the ordinary ratio architecture of an
additive positive measure applied to the exponential weight.

The construction is conditional. It assumes that \(\mu\), \(q\), and
\(\lambda\) have already been supplied. Projectivity constrains how their
weights combine; it does not derive them.

## 6.2 Effective score and block message

Let

\[
\mu_B=\sum_{i\in B}\mu_i.
\]

When \(\mu_B>0\), define

\[
Q_\lambda(B)
=
-\frac1\lambda
\log\left(
\frac{W_\lambda(B)}{\mu_B}
\right).
\]

Then

\[
W_\lambda(B)
=
\mu_Be^{-\lambda Q_\lambda(B)}.
\]

The pair

\[
(\mu_B,Q_\lambda(B))
\]

is therefore an exact block message for the exponential observable. It
contains precisely the information needed to reconstruct the block's total
exponential weight.

When the total mass is normalized to one, the global score is

\[
Q_\lambda(q,\mu)
=
-\frac1\lambda
\log\sum_i\mu_i e^{-\lambda q_i}.
\]

Up to sign conventions, this is the exponential certainty equivalent or
entropic transform [@FollmerSchied2002]. The identification is mathematical.
No thermodynamic energy, temperature, or physical free energy is inferred.

## 6.3 Exact hierarchical associativity

Partition the microscopic indices into blocks \(G\). Let

\[
\mu_G=\sum_{i\in G}\mu_i
\]

and define the normalized within-block score

\[
Q_G
=
-\frac1\lambda
\log\left(
\frac{1}{\mu_G}
\sum_{i\in G}\mu_i e^{-\lambda q_i}
\right).
\]

Then

\[
\mu_Ge^{-\lambda Q_G}
=
\sum_{i\in G}\mu_i e^{-\lambda q_i}.
\]

Summing over blocks gives

\[
\sum_G\mu_Ge^{-\lambda Q_G}
=
\sum_i\mu_i e^{-\lambda q_i},
\]

and hence

\[
Q_\lambda(q,\mu)
=
-\frac1\lambda
\log\sum_G\mu_Ge^{-\lambda Q_G}.
\]

**Proposition 6.1 (exact static aggregation).**  
Passing each block's total mass and exponential effective score reproduces the
global score exactly, independently of the order of grouping.

The proposition is the log-sum-exp or exponential quasi-arithmetic
associativity property. Its role in the framework is to identify a sufficient
static message for one declared observable. It is not a uniqueness theorem for
all coarse-graining problems.

## 6.4 Gauge and affine covariance

A common shift of all marks gives

\[
Q_\lambda(q+c,\mu)
=
Q_\lambda(q,\mu)+c.
\]

For \(a>0\),

\[
Q_\lambda(aq+c,\mu)
=
c+aQ_{a\lambda}(q,\mu).
\]

**Lemma 6.2 (affine covariance).**  
The exponential effective score is translation covariant, while positive
rescaling of \(q\) transports the transform parameter from \(\lambda\) to
\(a\lambda\).

**Proof.**

\[
\begin{aligned}
Q_\lambda(aq+c,\mu)
&=
-\frac1\lambda
\log\sum_i\mu_i e^{-\lambda(aq_i+c)}\\
&=
c-\frac1\lambda
\log\sum_i\mu_i e^{-a\lambda q_i}\\
&=
c+aQ_{a\lambda}(q,\mu).
\end{aligned}
\qquad\square
\]

This is classical log-Laplace algebra. It shows that the numerical scale of
\(q\) and the parameter labeling the transform curve are coupled. It does not
establish a physical renormalization flow.

## 6.5 Relative-entropy representation

Let \(\mu\) be a normalized positive reference measure. Maximizing relative
entropy

\[
-\sum_i p_i\log\frac{p_i}{\mu_i}
\]

subject to normalization and a fixed expected mark yields

\[
p_i
=
\frac{\mu_i e^{-\lambda q_i}}
{\sum_j\mu_j e^{-\lambda q_j}}
\]

for a Lagrange multiplier \(\lambda\) [@Jaynes1957; @Csiszar1975]. The
normalizing denominator is exactly \(W_\lambda\) when \(\mu\) is normalized.

This variational representation explains why the base measure cannot be
silently discarded. Different \(\mu\) define different relative-entropy
problems and different normalized laws even when the \(q\)-values are
unchanged.

The representation is conditional on the chosen constraint and reference
measure. It does not select a unique physical expected value, a unique
\(\lambda\), or a unique microscopic interpretation.

## 6.6 Observable-relative sufficiency

The score \(Q_\lambda\) is sufficient for the exponential observable because

\[
\mu_Be^{-\lambda Q_B}
=
\sum_{i\in B}\mu_i e^{-\lambda q_i}.
\]

It is not generally sufficient for another observable. For example, a block
mean preserves the first weighted moment, while a minimum preserves an
extremal mark. Two blocks can have the same \(Q_\lambda\) and different means,
variances, quantiles, or transform values at another parameter.

Even within the exponential family, the score is parameter-specific. Exact
aggregation holds for every fixed \(\lambda\), but the block value
\(Q_\lambda(B)\) changes with \(\lambda\). Static closure therefore does not
select the transform parameter.

The correct claim is:

\[
\boxed{
(\mu_B,Q_\lambda(B))
\text{ is an exact static message for the declared exponential observable at
the declared }\lambda.
}
\]

It is not “the” unique macrostate of the system.

## 6.7 From static aggregation to the dynamic question

Static associativity answers a regrouping question: can the same present
observable be computed after microscopic states are replaced by block
messages? For \(W_\lambda\), the answer is yes.

A dynamic closure question is stronger: do the block messages contain enough
information to determine their own future values under a microscopic update?
Nothing in Proposition 6.1 guarantees this. The affine covariance identity
already warns that an update involving a scale change can require
\(Q_{a\lambda}\) even when the present macrostate carries only
\(Q_\lambda\).

This distinction motivates Section 7:

\[
\boxed{
\text{exact static aggregation does not imply autonomous dynamic closure.}
}
\]
