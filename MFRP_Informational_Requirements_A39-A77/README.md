# Informational Requirements for Pre-Categorical Relational Models

**Computational audit repository, A39–A77**  
**Author:** Felipe Gianini Romero  
**Programme:** Modal Field Research Programme (MFRP)  
**Repository language:** English

This repository contains the complete computational audit sequence developed from the technical report **“Informational Requirements for Pre-Categorical Relational Models: Identifiability, Measure, Dynamic Closure, and Coarse-Graining”** (MFRP-TR-2026-01, v1.1, July 2026).

The central mathematical object is the Laplace-type transform

\[
L_P(\lambda)=\int e^{-\lambda x}\,dP(x),
\qquad
Q_P(\lambda)=-\frac{1}{\lambda}\log L_P(\lambda),
\]

under finite or controlled observation contracts. The audit sequence studies identifiability, sharp prediction intervals, finite-budget minimax design, continuous anchor optimization, covariance uncertainty, bootstrap calibration, finite-support generalization, exact active-basis phase theorems, dual envelopes, Cramer orientation, signed \(q\)-Schur decompositions, and active-set bifurcation.

## Repository status

- **39 main audits:** A39 through A77.
- **All stored audit verdicts:** `PASS` under their declared contracts.
- **English technical notes:** 33 audit notes plus one base non-closure note.
- **English figures:** 82 regenerated publication figures.
- **Exact and numerical outputs:** JSON records with gates, values, boundaries, and verdicts.
- **Original report:** included under `paper/`.

A passing audit means that the code satisfied the gates encoded for its declared mathematical and computational contract. It does **not** convert a finite-domain result into a universal physical theorem. Each technical note states its own scope and boundary conditions.

## Directory layout

```text
.
├── audits/                 # Audit programs and exact helper modules
├── results/                # Full JSON results and compact summaries
├── docs/technical_notes/   # English audit notes
├── figures/                # English-language regenerated figures
├── paper/                  # Original English technical report PDF
├── templates/              # Input/configuration templates for A60–A62
├── tools/                  # Figure generation, verification, and runners
├── tests/                  # Repository integrity tests
├── provenance/             # File mapping and provenance metadata
├── AUDIT_INDEX.md          # One-row index for A39–A77
├── RUNBOOK.md              # Reproduction commands and practical notes
├── REPRODUCIBILITY.md      # Scope, exactness, numerical layers, limitations
└── MANIFEST.sha256         # SHA-256 inventory
```

## Quick verification

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python tools/verify_results.py
python -m unittest discover -s tests -v
```

## Regenerate all English figures

```bash
python tools/generate_english_figures.py
```

The generator reads the committed JSON results and overwrites the 82 PNG files in `figures/`.

## Re-running audits

The historical audit programs use a flat working-directory convention because later audits read earlier result files by filename. The structured repository therefore includes a runtime materializer:

```bash
python tools/materialize_runtime.py
python tools/run_all_audits.py --from-audit 39 --to-audit 77
```

Several audits are computationally expensive, especially A62, A67, A70, A71, and the A72-A77 extensions. See `RUNBOOK.md` before starting a full replay.

## Main result sequence

The sequence progresses from exact finite-grid non-identifiability to increasingly strong design and structural results:

1. **A39–A43:** sharp intervals, monotone refinement, robust interval data, finite-budget and direct-\(Q\) minimax design.
2. **A44–A54:** continuous anchor optimization, noise phase diagrams, target exclusion, continuum witnesses, and a global anchor optimum under the declared contract.
3. **A55–A62:** finite implementability, cost regularization, channel calibration, covariance uncertainty, and model-conditional bootstrap validation.
4. **A63–A65:** general finite-support non-identifiability, scale-normalized noise, and continuous first-anchor stress with exact local sensitivity.
5. **A66–A68:** exact global phase theorems, a five-support family theorem, and an exact dual value-of-information theorem for the first channel.
6. **A69–A71:** Cramer reduction, the obstruction to order-only total positivity, signed \(q\)-Schur dominance, and active-set protection after an orientation bifurcation at \(M=10\).
7. **A72–A77:** local pivot diamonds, complete one-pivot neighborhoods, interval-stable gamma bifurcations, parity-reduced support-size theorems, candidate-versus-actual active-set separation, and an exact contact-family reset.

See `AUDIT_INDEX.md` for direct links and stored gate counts.

## Scientific boundaries

This repository does not claim:

- a physical spacetime metric or physical calibration of \(\lambda\);
- a universal theorem for all support sizes, means, targets, noise models, or anchor budgets;
- that bootstrap inflation factors are distribution-free constants;
- that finite catalogue or finite-family results automatically extend to continuous or arbitrary domains.

The strongest global continuous theorems are explicitly tied to declared finite-support contracts and fixed anchor completions. The notes preserve negative results and counterexamples, including the failure of order-only total positivity and fixed-signature induction.

## Citation

Use the metadata in `CITATION.cff`. Until a DOI or archival release is assigned, cite the repository version and commit hash.

## License

This package follows the parent repository split licensing model. Software is
licensed under Apache-2.0, and scientific content, documentation, figures,
tables, JSON result files, reports, and other research outputs are licensed
under CC BY 4.0. See `LICENSE_NOTICE.md` and the parent repository `LICENSE.md`.


## A72–A77 update

- **A72:** Exact local pivot diamond at M=10–12; orientation selects between two terminal pivot routes.
- **A73:** Complete declared one-pivot neighborhood at a rational probe and exact M=13 global extension.
- **A74:** Interval-stable gamma-sign bifurcation from M=12 to M=13 and independent exact M=14 extension.
- **A75:** Parity-reduced all-M candidate-orientation theorem on a fixed interval; exact M=15–16 extensions.
- **A76:** Candidate orientation separated from actual active-set selection; no active re-entry at M=22.
- **A77:** Fixed-family double bifurcation and exact active contact reset from {5,6} to {6,7}.

The current package contains 39 main audits, 82 English figures, and preserves the new failed/superseded exploratory files in a separate raw-provenance archive rather than presenting them as final certificates.
