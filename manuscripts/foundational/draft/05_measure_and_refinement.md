# 5. Measure, Multiplicity, and Refinement

## 5.1 Why relation plus marks are insufficient

Let a finite marked relational state be represented by

\[
(X,R,q),
\]

where \(X\) is a finite labeled set, \(R\) is a relation on \(X\), and
\(q:X\to\mathbb R\) is a scalar mark. A refinement replaces one macrostate
\(x\in X\) by several microstates \(x_1,\ldots,x_m\). If the new states have
the same relational profile and the same mark, the refined structure can be
interpreted in at least two ways.

In a **descriptive refinement**, the microstates are alternative descriptions
of one macrostate. Their total weight should equal the original macro weight.
In an **ontic multiplication**, they are distinct states and a counting rule
may assign \(m\) units of multiplicity. The bare refined relation and the
equal \(q\)-marks are compatible with both interpretations.

**Proposition 5.1 (semantic multiplicity obstruction).**  
No deterministic rule whose input is only the unweighted marked structure
\((R,q)\) can, in general, distinguish a descriptive refinement from an ontic
multiplication when the two interpretations yield isomorphic marked
structures.

**Proof.** The input to the rule is identical under the two interpretations,
whereas the required macro mass differs. A deterministic function of identical
input cannot return both values. \(\square\)

The proposition does not settle an ontological dispute. It identifies missing
information. A refinement map, multiplicity assignment, base measure, or
equivalent external semantics must be supplied before the two interpretations
can be distinguished.

## 5.2 Additive base mass

Introduce a positive mass

\[
\mu:X\to(0,\infty).
\]

The pair \((q,\mu)\) defines a finite marked measure

\[
\nu=\sum_{x\in X}\mu_x\,\delta_{q_x}.
\]

Suppose a contextual score \(T_\nu(q_x)\) depends only on the marked measure
and the marked point, and define normalized weights

\[
P_x
=
\frac{\mu_x f(T_\nu(q_x))}
{\sum_{y\in X}\mu_y f(T_\nu(q_y))}
\]

for a positive function \(f\).

**Proposition 5.2 (exact clone-refinement invariance).**  
Replace a state \(r\) by exact clones \(r_1,\ldots,r_m\) with

\[
q_{r_a}=q_r,
\qquad
\sum_{a=1}^{m}\mu_{r_a}=\mu_r.
\]

Then the marked measure \(\nu\), every score \(T_\nu\), and all macro
probabilities are unchanged.

**Proof.** The clone replacement preserves the atomic measure because

\[
\sum_a\mu_{r_a}\delta_{q_r}
=
\mu_r\delta_{q_r}.
\]

The combined unnormalized clone weight is

\[
\sum_a\mu_{r_a}f(T_\nu(q_r))
=
\mu_r f(T_\nu(q_r)).
\]

All other unnormalized weights are unchanged, so normalization gives the same
macro probabilities. \(\square\)

The role of \(\mu\) is therefore operationally precise: it prevents the
representation from treating the number of listed descriptions as automatic
physical multiplicity. This does not determine the origin or interpretation
of \(\mu\).

## 5.3 Finite refinement trees

Let \(\mathcal T\) be a finite rooted refinement tree. Assign each terminal leaf
\(\ell\) a positive weight \(w_\ell\).

**Lemma 5.3 (unique additive extension on a finite tree).**  
Every finitely additive extension agreeing with the leaf weights must satisfy

\[
\mu(A)
=
\sum_{\ell\in\operatorname{Desc}(A)}w_\ell
\]

for every node \(A\). This extension is unique and independent of the order in
which refinements are introduced or merged.

**Proof.** Repeated finite additivity expresses the mass of a node as the sum
of the masses of its children and, recursively, as the sum of all descendant
leaf weights. Any two additive extensions agreeing on the leaves therefore
agree on every node. \(\square\)

The same argument applies to additive sufficient statistics. For example,

\[
\sum_\ell w_\ell q_\ell,\qquad
\sum_\ell w_\ell q_\ell^2,\qquad
\sum_\ell w_\ell e^{-\lambda q_\ell}
\]

can be aggregated along any hierarchy without path dependence. Derived
quantities such as weighted means or exponential effective scores are
path-independent when the additive messages needed to reconstruct them are
carried.

Uniform leaf weights recover descendant counting measure, but only
conditionally on a specified terminal-leaf interpretation. Additivity does not
decide how many terminal states exist or whether a new branch represents a
new physical alternative.

## 5.4 Infinite refinement without terminal leaves

Terminal leaves are not mathematically necessary. Consider a finitely
branching rooted tree in which every node \(A\) assigns positive fractions

\[
p(B\mid A)>0
\]

to its children \(B\), with

\[
\sum_{B\prec A}p(B\mid A)=1.
\]

The mass of a cylinder determined by a finite path is the product of its branch
fractions. These finite-dimensional cylinder probabilities are consistent:
the mass of a parent cylinder equals the sum of the masses of its child
cylinders. Under the standard extension theorem, the consistent family
determines a probability measure on the infinite path space
[@Daniell1918; @Kolmogorov1933].

This construction separates two concepts that are easily conflated:
terminality and atomicity.

**Example 5.4 (nonterminal atom).**  
Along one infinite path, let the retained branch fraction at depth \(n\ge2\)
be

\[
p_n=1-\frac1{n^2}.
\]

Then the depth-\(N\) cylinder mass is

\[
\prod_{n=2}^{N}\left(1-\frac1{n^2}\right)
=
\frac{N+1}{2N}
\longrightarrow\frac12.
\]

The infinite path is nonterminal but is an atom of mass \(1/2\).

**Example 5.5 (terminal-free non-atomic measure).**  
If every child fraction is bounded above by a fixed \(r<1\), then every
depth-\(d\) cylinder has mass at most \(r^d\), which tends to zero. No
individual infinite path is an atom.

Thus an atom need not be terminal, and the absence of terminal leaves does not
imply non-atomicity.

## 5.5 Projective branch fractions

Let a refinement hierarchy carry a positive finitely additive weight \(W\).
For a node \(A\) partitioned into children \(B_1,\ldots,B_k\), define

\[
p(B_a\mid A)
=
\frac{W(B_a)}{W(A)}.
\]

These fractions are normalized and telescope along paths. If \(\ell\) is a
leaf or a cylinder endpoint,

\[
\prod_{A\to B\text{ on path to }\ell}
p(B\mid A)
=
\frac{W(\ell)}{W(\mathrm{root})}.
\]

The result is independent of intermediate grouping. Conversely, a
path-independent branching law compatible with disjoint regrouping defines an
additive weight up to one common multiplicative constant.

This ratio architecture is ordinary conditional-measure structure. Its
significance here is restrictive rather than generative: projective
consistency determines how supplied weights must combine, but it does not
select the weights.

An important example is

\[
W_\lambda(A)
=
\sum_{\ell\in A}
\mu_\ell e^{-\lambda q_\ell}.
\]

The weight is additive, and the fractions
\(W_\lambda(B)/W_\lambda(A)\) are exactly projective. The sufficient subtree
message is the partition sum \(W_\lambda\), or equivalently the pair consisting
of total mass and the associated exponential effective score. Replacing the
subtree partition sum by the exponential of a subtree mean is generally not
additive.

## 5.6 What measure consistency does not determine

The preceding constructions establish several positive results:

1. additive mass removes naive clone-count dependence;
2. finite refinement is path-independent once terminal weights are supplied;
3. consistent infinite refinement supports a probability measure without
   terminal leaves;
4. branch probabilities have an exact ratio form once an additive weight is
   supplied.

They do not answer the prior selection problem. The same tree supports many
consistent mass assignments, including uniform, biased, atomic, and non-atomic
measures. Likewise, many terminal-weight assignments obey the same
projectivity and regrouping laws while generating different branch
probabilities.

Accordingly, the manuscript treats \(\mu\) as a separate informational
component. It is not reconstructed from \(R\) merely by choosing a convenient
order statistic, and it is not derived from \(q\) merely by exponentiating the
marks. A function \(\mu=F(R)\) may be a useful order-based summary, but it
cannot break an identifiability limit already present within each
order-equivalence class.

The conclusion is:

\[
\boxed{
\text{refinement consistency constrains the algebra of mass, not the origin of
mass.}
\]

A physical interpretation of \(\mu\), if one exists, requires an operational
mapping beyond the formal results established here.
