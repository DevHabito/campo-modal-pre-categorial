# Erratum for preprint v1: condensation-code count

Where the manuscript states or implies that there are **5,234 distinct full labeled condensation-poset codes** for loopless labeled digraphs on five vertices, replace that claim with:

> Exhaustive enumeration yields 6,942 distinct full labeled reflexive reachability preorders. The earlier minimum-representative encoding yields 5,234 quotient-poset codes because it records SCC minima and their quotient order but not the full assignment of nonrepresentative vertices to SCCs. The fully unlabeled count is 139.

The exact one-edge-flip sensitivity `75/256` remains unchanged at `n=5` under both encodings.

See `audits/a8_1_exact_results/a8_1_theorem.md` and `audits/a8_1_exact_results/a8_1_summary.json`.
