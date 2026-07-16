# 3. Additional Quantitative Structure \(q\)

## 3.1 Why an additional mark is introduced

Section 2 established an identifiability limit: quantities that vary under
strict order-preserving recalibrations are not recoverable from the relation
\(R\) alone. A natural response is to enrich the relational state with a
quantitative mark. Let \(\mathcal A\) denote the relevant relational carriers,
such as states, edges, or admissible transitions, and introduce

\[
q:\mathcal A\to\mathbb R.
\]

The mark \(q\) is not defined here as a function of the order. It is supplied
as additional information. This distinction is essential. If \(q\) were
constructed deterministically from \(R\), then it could not distinguish two
latent representatives that produce the same relation.

The same conclusion holds if the construction uses model-independent
randomness. Suppose

\[
q=F(R,U),
\]

where \(U\) has the same conditional law in every latent model sharing the
same observed relation. Then the conditional law of \(q\) is also the same
throughout that order-equivalence class. Such a mark may be useful as a
randomized relational statistic, but it does not add information about which
latent representative generated the relation.

**Proposition 3.1 (information criterion for an additional mark).**  
A mark \(q\) can break an order-only identifiability class only if its
conditional marked law is not determined by \(R\) and differs between at least
some latent models that induce the same relation.

**Proof.** If the conditional law of \(q\) given \(R\) is identical in two
latent models, then the joint observable law of \((R,q)\) is identical in
those models. No estimator based only on \((R,q)\) can distinguish them.
Therefore distinguishability requires a conditional marked law that varies
inside the order-equivalence class. \(\square\)

The proposition is an information statement, not a physical-origin theorem.
It says what an informative \(q\) must do; it does not explain how nature, an
experiment, or a deeper theory would supply it.

## 3.2 Operational meaning requires a coupling

A numerical label is not operational merely because it is stored in the
state. Relative to an observation class \(\mathcal O\), an operational mark
requires a specified conditional law

\[
K(O\mid R,q),
\qquad O\in\mathcal O,
\]

that is sensitive to at least some physically or statistically admissible
changes in \(q\).

If

\[
K(O\mid R,q)=K(O\mid R,q')
\]

for every allowed pair \(q,q'\), then \(q\) is empirically silent for that
observation class. Conversely, sensitivity alone is not enough: the coupling
should respect the symmetries assigned to the representation. In the current
framework, the minimum operational contract is:

1. relabeling equivariance;
2. invariance under declared gauge transformations;
3. a stated relational locality condition;
4. nontrivial dependence on gauge-invariant \(q\)-contrasts;
5. inferability of at least some \(q\)-information from observable
   frequencies under a calibrated model.

This contract separates two questions that are often merged. The first is
whether \(q\) contains information not already encoded by \(R\). The second is
whether a declared observable law makes any of that information measurable.
A mark can satisfy the first condition and fail the second.

## 3.3 Global-shift redundancy

Many candidate constructions use only differences, centered values, or
normalized functions of \(q\). In such cases the transformation

\[
q_\alpha\mapsto q_\alpha+c
\]

for one constant \(c\) changes no observable contrast.

Define the centered mark

\[
\widetilde q_\alpha
=
q_\alpha-\bar q,
\qquad
\bar q
=
\frac{1}{|\mathcal A|}
\sum_{\alpha\in\mathcal A}q_\alpha
\]

for a finite carrier set. Then

\[
\widetilde{(q+c)}_\alpha=\widetilde q_\alpha.
\]

Likewise, every difference satisfies

\[
(q_\alpha+c)-(q_\beta+c)
=
q_\alpha-q_\beta.
\]

**Proposition 3.2 (global-shift quotient).**  
Any construction that factors through the set of \(q\)-differences or through
the centered mark is a function of the equivalence class

\[
[q]
=
\{q+c\mathbf 1:c\in\mathbb R\}.
\]

It cannot identify an absolute additive zero for \(q\).

The proposition is definitional. Calling the redundancy a gauge contract is
useful because it prevents later formulas from depending accidentally on an
unobservable offset. It does not establish a fundamental gauge symmetry of
nature.

For a local normalized transition law, the redundancy can be larger. If each
source row is normalized separately, adding a source-dependent constant

\[
q_{ij}\mapsto q_{ij}+c_i
\]

may leave the entire row unchanged. The exact gauge group therefore belongs to
the declared observable kernel, not to the symbol \(q\) in isolation.

## 3.4 Offset and scale are different problems

Removing an additive zero does not fix a multiplicative unit. Under

\[
q\mapsto aq+c,
\qquad a>0,
\]

differences transform as

\[
q_\alpha-q_\beta
\mapsto
a(q_\alpha-q_\beta).
\]

Thus a contrast can be shift-invariant while remaining scale-covariant. A
dimensionless observable can be formed by combining \(q\) with a coupling
parameter or by standardizing the local values, but those choices have
different informational meanings.

A raw exponential factor,

\[
e^{-\beta q_\alpha},
\]

depends only on the product \(\beta q_\alpha\). Rescaling \(q\) while inversely
rescaling \(\beta\) leaves the factor unchanged. Before a \(q\)-unit is fixed,
the numerical magnitude of \(\beta\) is therefore inseparable from the scale
of \(q\).

Local standardization instead defines, when the local variance is positive,

\[
z_\alpha
=
\frac{q_\alpha-\bar q_{\mathrm{local}}}
{s_{\mathrm{local}}}.
\]

The standardized values are invariant under positive affine
recalibrations of the local raw marks. This removes raw scale from the input,
but it does not select which function of \(z\) should govern an observable.
That underdetermination is the subject of Section 4.

## 3.5 Relative information versus calibrated quantity

The current role of \(q\) is therefore limited but precise. It can provide
relative cardinal information that is absent from \(R\), provided its marked
law is not itself determined by \(R\). Gauge-invariant contrasts can become
operational through a specified observation kernel. None of these statements
supplies:

- an absolute additive zero;
- a physical unit;
- a calibration procedure;
- an empirical measurement map;
- a derivation of the mark from a deeper dynamics.

A model may consistently work on the quotient space of marks modulo global
shift while leaving the scale to be estimated. Alternatively, an external
standard may fix both offset and unit. These are different modelling
contracts and should not be blended.

The section's conclusion is:

\[
\boxed{
q\text{ is an additional informational primitive only to the extent that its
marked law and observable coupling add information beyond }R.
}
\]

The introduction of \(q\) resolves an order-only insufficiency. It does not
resolve measure, kernel selection, dynamic closure, or physical calibration.
