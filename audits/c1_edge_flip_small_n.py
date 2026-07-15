#!/usr/bin/env python3
"""
C1 auxiliary exact enumeration:
edge-toggle sensitivity of the full reflexive reachability preorder.

For n in {2,3,4,5}, enumerate every loopless labeled digraph G and every
ordered non-loop edge e. Compute whether toggling e changes the full reflexive
reachability matrix C(G).

Definition:
    P_n = (1 / (2^(n(n-1)) n(n-1))) *
          sum_{G,e} 1[C(G) != C(G triangle e)].

This script is an auxiliary result for Novelty Audit C1. It does not prove a
general formula or asymptotic law.
"""

from __future__ import annotations

import csv
import json
import math
from pathlib import Path

import numpy as np


def exact_probability(n: int) -> dict[str, object]:
    edges = [(i, j) for i in range(n) for j in range(n) if i != j]
    m = len(edges)
    graph_count = 1 << m
    dtype = np.uint32 if m <= 32 else np.uint64
    masks = np.arange(graph_count, dtype=dtype)

    adjacency = np.zeros((graph_count, n, n), dtype=np.bool_)
    for bit, (i, j) in enumerate(edges):
        adjacency[:, i, j] = ((masks >> bit) & 1).astype(np.bool_)

    reachability = adjacency.copy()
    for i in range(n):
        reachability[:, i, i] = True

    for k in range(n):
        reachability |= (
            reachability[:, :, k][:, :, None]
            & reachability[:, k, :][:, None, :]
        )

    codes = np.zeros(graph_count, dtype=np.uint64)
    bit = 0
    for i in range(n):
        for j in range(n):
            codes |= reachability[:, i, j].astype(np.uint64) << bit
            bit += 1

    changed = 0
    for edge_bit in range(m):
        neighbor = masks ^ (1 << edge_bit)
        changed += int(np.count_nonzero(codes != codes[neighbor]))

    total = graph_count * m
    divisor = math.gcd(changed, total)
    numerator = changed // divisor
    denominator = total // divisor

    return {
        "n": n,
        "directed_nonloop_edges": m,
        "labeled_digraphs": graph_count,
        "graph_edge_pairs": total,
        "changed_pairs": changed,
        "reduced_numerator": numerator,
        "reduced_denominator": denominator,
        "exact_fraction": f"{numerator}/{denominator}",
        "decimal": changed / total,
    }


def main() -> None:
    output = Path(__file__).resolve().parent / "c1_exact_results"
    output.mkdir(exist_ok=True)

    rows = [exact_probability(n) for n in range(2, 6)]

    with (output / "c1_edge_flip_small_n.csv").open(
        "w", newline="", encoding="utf-8"
    ) as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    expected = {
        2: "1/1",
        3: "3/4",
        4: "1/2",
        5: "75/256",
    }
    gates = {
        f"G{index + 1}_P_{row['n']}_matches_expected":
        row["exact_fraction"] == expected[row["n"]]
        for index, row in enumerate(rows)
    }

    summary = {
        "audit_id": "C1_EDGE_FLIP_SMALL_N",
        "definition": (
            "P_n is the fraction of ordered graph-edge pairs (G,e) for which "
            "toggling e changes the full reflexive reachability preorder."
        ),
        "ensemble": (
            "Uniform loopless labeled digraphs on n vertices and uniform "
            "directed non-loop edge toggle."
        ),
        "rows": rows,
        "gates": gates,
        "verdict": (
            "PASS_EXACT_SMALL_N_EDGE_FLIP_SEQUENCE"
            if all(gates.values())
            else "FAIL_SMALL_N_EDGE_FLIP_SEQUENCE"
        ),
        "limitations": [
            "No general formula is proved.",
            "No asymptotic claim is made.",
            "The enumeration stops at n=5 because the graph space has size "
            "2^(n(n-1)).",
        ],
    }

    (output / "c1_summary.json").write_text(
        json.dumps(summary, indent=2), encoding="utf-8"
    )
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
