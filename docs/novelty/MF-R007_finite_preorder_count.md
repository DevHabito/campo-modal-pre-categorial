# MF-R007 — Count of Full Labeled Reachability Preorders

**Novelty audit:** C1  
**Search date:** 2026-07-15  
**Final classification:** `CLASSICAL_ENUMERATION_FORMULA`

## Exact claim

Let \(p(k)\) denote the number of partial orders on a labeled \(k\)-element
set and \(S(n,k)\) the Stirling number of the second kind. The number of
preorders on a labeled \(n\)-element set is

\[
Q(n)=\sum_{k=1}^{n}S(n,k)p(k).
\]

Every preorder is realizable as the reflexive reachability relation of a
digraph. Therefore the same formula counts full labeled condensation or
reachability preorders.

For \(n=5\),

\[
Q(5)=1+45+475+2190+4231=6942.
\]

## Prior literature

This formula is not new. Fischer and Makowsky explicitly state

\[
Q(n)=\sum_{k=0}^{n}S(n,k)P(k)
\]

as a known result and attribute it to *Enumeration of finite topologies*
(1973). They also identify labeled finite topologies with labeled preorders
and \(T_0\) topologies with partial orders. Their discussion records the
historical value \(T(5)=6942\).

Kim, Kwon, and Lee likewise describe the one-to-one correspondence among
finite topologies, preorders, and transitive digraph representations and
place computer enumeration in a literature beginning with Evans, Harary, and
Lynn.

Primary sources:

- Fischer, E.; Makowsky, J. A. *Counting Finite Topologies*.
  https://arxiv.org/abs/2303.11903
- Kim, D.; Kwon, Y. S.; Lee, J. *Enumerations of Finite Topologies Associated
  with a Finite Graph*. https://arxiv.org/abs/1206.0550

## Mathematical comparison

The A8.1 proof uses the same classical decomposition:

1. choose the equivalence classes of mutual reachability;
2. choose a partial order on the quotient classes.

This is exactly the partition-plus-poset decomposition underlying the
classical preorder formula. The A8.1 proof is a correct independent
rederivation, not a new enumeration theorem.

## Project contribution that remains

A8.1 still contributes:

- an independent exhaustive reproduction for all \(2^{20}\) loopless
  labeled digraphs on five vertices;
- a formal reconciliation of \(6942\) with the earlier \(5234\) code count;
- a proof that the old implementation stored a coarser representative code;
- a public corrective audit with code, hashes, and explicit terminology.

## Safe manuscript wording

> The classical partition–quotient decomposition gives
> \(Q(n)=\sum_k S(n,k)p(k)\) for labeled preorders. We independently reproduce
> \(Q(5)=6942\) by exhaustive digraph enumeration and use the formula to
> diagnose an ambiguity in an earlier minimum-representative encoding.

## Wording to avoid

- “We derive a new formula for the number of labeled preorders.”
- “The value \(6942\) is a new enumeration.”
- “The SCC-condensation construction creates a previously unknown class of
  finite orders.”

## Editorial decision

Keep the formula as attributed background. The publishable project-specific
content is the coding correction, the independent reproduction, and the
comparison between the complete and incomplete encodings.
