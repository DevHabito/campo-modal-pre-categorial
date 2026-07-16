# Data and Code Availability

The mathematical protocols, exact witnesses, classification matrices,
manuscript claim maps, and validation scripts are archived in the public
repository:

`DevHabito/precategorical-modal-field-framework`

The manuscript body is organized independently of the audit chronology.
Repository provenance is recorded in `PROVENANCE_NOTES.md` and
`CLAIM_TRACEABILITY.csv`.

The exact four-point dynamic nonclosure witness is implemented in:

```text
audits/c2_exact_identities_and_nonclosure.py
```

The integrated manuscript is validated by:

```text
tools/validate_foundational_manuscript.py
tools/validate_foundational_core.py
tools/validate_manuscript_split.py
tools/validate_protocols.py
tools/validate_repository.py
```

All generated repository artifacts are covered by `MANIFEST.csv` and
`SHA256SUMS.txt`. Computational scripts are supporting checks and
reproducibility records; the principal proofs in the manuscript are analytic.
