# MF-R011 — Edge-Toggle Sensitivity of the Reachability-Preorder Map

**Novelty audit:** C1  
**Search date:** 2026-07-15  
**Final classification:** `APPARENTLY_UNREPORTED_EXACT_FINITE_STATISTIC_NOVELTY_NOT_CERTIFIED`

## Exact definition

Let

\[
m=n(n-1)
\]

and let \(\mathcal D_n\) be the \(2^m\) loopless labeled digraphs on
\([n]\). Let \(C(G)\) be the full reflexive reachability preorder of \(G\).
Define

\[
P_n
=
\frac{1}{m2^m}
\sum_{G\in\mathcal D_n}
\sum_{e}
\mathbf 1\!\left[C(G)\neq C(G\triangle e)\right],
\]

where \(G\triangle e\) toggles one directed non-loop edge.

This is the normalized edge-boundary density, or average Boolean influence,
of the vector-valued map

\[
C:\{0,1\}^{m}\longrightarrow\{\text{preorders on }[n]\}
\]

under the discrete metric on its codomain.

## Exact finite results

The auxiliary C1 enumeration gives

\[
P_2=1,\qquad
P_3=\frac34,\qquad
P_4=\frac12,\qquad
P_5=\frac{75}{256}.
\]

For \(n=5\),

\[
m2^m=20\cdot 2^{20}=20\,971\,520
\]

ordered graph-edge pairs, of which

\[
6\,144\,000
\]

change the full reachability preorder. Therefore

\[
P_5
=
\frac{6\,144\,000}{20\,971\,520}
=
\frac{75}{256}.
\]

## Closest literature found

### Dynamic SCC and reachability algorithms

Georgiadis et al. study sensitivity queries and data structures for SCCs under
edge deletions. Bernstein, Probst, and Wulff-Nilsen study decremental SCC and
single-source reachability algorithms. These works address algorithmic update
complexity and query support, not the uniform exact probability \(P_n\).

### Directed-network susceptibility

Goltsev, Timár, and Mendes define susceptibilities for changes in large
directed-network components under edge or vertex addition/pruning, especially
near directed-percolation transitions. Their observable and asymptotic regime
differ from the complete finite reachability-preorder map.

### Average sensitivity

Varma and Yoshida define average sensitivity for graph algorithms through
distances between algorithmic output distributions after edge deletion. This
is the closest abstract language, but their paper studies optimization
algorithms such as cuts, matching, coloring, and spanning forests—not the
exact edge-boundary density of the reachability-preorder map.

Primary sources:

- Georgiadis et al. (2017), DOI: 10.4230/LIPIcs.ICALP.2017.42
- Bernstein, Probst, and Wulff-Nilsen (2019), arXiv:1901.03615
- Goltsev, Timár, and Mendes (2017), DOI: 10.1103/PhysRevE.96.022317
- Varma and Yoshida (2020), arXiv:1904.03248

## Search result

No inspected source states:

- the definition of \(P_n\) above;
- the exact value \(P_5=75/256\);
- the sequence \(1,3/4,1/2,75/256\);
- a general formula for the probability that one edge toggle changes the
  entire reflexive reachability preorder of a uniform labeled digraph.

This supports the cautious description “apparently unreported in the searched
literature.” It does not certify worldwide novelty.

## Mathematical significance

The statistic is more than SCC sensitivity: \(C(G)\) changes whenever either

1. the SCC partition changes, or
2. the quotient reachability order changes while the SCC partition remains
   fixed.

Thus a general analysis must distinguish internal SCC-critical edges from
edges that alter intercomponent reachability.

The exact \(n=5\) fraction is publishable as a finite enumeration only if it is
embedded in a broader development, such as:

- a structural decomposition of pivotal edge toggles;
- exact values for further \(n\);
- bounds or asymptotics for \(P_n\);
- conditioning on edge density or SCC type;
- a theorem relating \(P_n\) to transitive reductions, dominators, or strong
  bridges.

## Safe manuscript wording

> We define the edge-toggle sensitivity \(P_n\) of the full reachability-preorder
> map. Exhaustive enumeration gives
> \(P_2=1\), \(P_3=3/4\), \(P_4=1/2\), and \(P_5=75/256\).
> We found related literatures on dynamic SCC maintenance, directed-network
> susceptibility, and average sensitivity of graph algorithms, but no source
> reporting this exact statistic or its \(n=5\) value.

## Wording to avoid

- “We have proved the general law \(P_n\).”
- “\(75/256\) is a universal constant.”
- “No one has ever studied graph sensitivity under edge changes.”
- “The result has physical significance without a model linking this ensemble
  to a physical system.”

## Editorial decision

Keep \(75/256\) as an exact finite result and open-problem generator. The next
mathematical target is a decomposition or recurrence for \(P_n\), not another
isolated decimal at a larger \(n\).
