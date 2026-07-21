# Reproducibility and Claim Boundaries

## Reproducibility layers

### Layer 1 — Stored-result integrity

`tools/verify_results.py` checks that all 33 result files parse, all top-level gates are true, all verdicts begin with `PASS`, all expected figures exist, and all Python files compile.

### Layer 2 — Figure reconstruction

`tools/generate_english_figures.py` reconstructs 58 English figures from the JSON result records.

### Layer 3 — Audit replay

`tools/materialize_runtime.py` reconstructs the original flat working directory. `tools/run_all_audits.py` executes a chosen audit interval and stores logs.

### Layer 4 — Independent mathematical inspection

Every result JSON includes the audit contract, gates, verdict, and boundaries. Exact audits record rational values, polynomial identities, roots or isolating intervals, phase structures, or primal–dual certificates as applicable.

## Interpretation of a PASS verdict

A PASS verdict means that all encoded gates passed for the declared audit contract. It is not a peer-review decision and is not evidence outside that contract.

## Known non-universal results

The repository deliberately preserves the following negative or limiting results:

- finite observations do not generally identify an omitted transform when the hidden distribution has enough degrees of freedom;
- the far/compactified third anchor is contract-dependent outside the original six-state example;
- the boundary pair need not be unique because exact ties exist;
- order-only total positivity does not determine the coupled Cramer numerator sign;
- individual q-Schur positivity does not remove cancellation in the full numerator;
- a fixed active signature changes orientation between M=9 and M=10;
- the M=10 optimizer changes active set rather than continuing the invalid signature.

## Statistical limitation

A62's inflation factors are empirical and model-conditional. They are not universal finite-sample confidence constants. Heavy-tailed data reduce contract availability even after calibrated coverage improves.

## Physical limitation

The programme is informational/mathematical. It does not assign a physical metric, spacetime interpretation, measurement kernel, or physical unit to the transform parameters.
