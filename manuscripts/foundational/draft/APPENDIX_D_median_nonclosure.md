# Appendix D. A Nondecomposable Median Message

Robustness of a statistic does not imply hierarchical decomposability. Consider
weighted medians under the convention that the median is the smallest value
whose cumulative mass reaches at least one half of total mass.

Define two blocks of total mass one:

\[
A:
\quad
0\text{ with mass }\frac35,
\qquad
100\text{ with mass }\frac25,
\]

and

\[
A':
\quad
0\text{ with mass }\frac35,
\qquad
1\text{ with mass }\frac25.
\]

Both blocks have total mass \(1\) and weighted median \(0\). Let a third block
be

\[
B:
\quad
50\text{ with mass }\frac12.
\]

For \(A\cup B\), the ordered masses are

\[
0:\frac35,
\qquad
50:\frac12,
\qquad
100:\frac25.
\]

The total mass is \(3/2\), so the half-mass threshold is \(3/4\). The
cumulative mass at \(0\) is \(3/5<3/4\), while at \(50\) it exceeds the
threshold. Hence the combined median is \(50\).

For \(A'\cup B\), the ordered masses are

\[
0:\frac35,
\qquad
1:\frac25,
\qquad
50:\frac12.
\]

The cumulative mass first reaches \(3/4\) at \(1\). Hence the combined median
is \(1\).

**Proposition D.1 (mass plus median is not closed).**  
Two blocks can have the same total mass and weighted median yet yield different
global medians when combined with the same third block. Therefore the pair
“mass plus weighted median” is not an exact hierarchical message.

The result does not rule out mergeable quantile sketches, interval-valued
summaries, or richer order-statistic messages. It rules out exact closure of
this particular scalar summary.
