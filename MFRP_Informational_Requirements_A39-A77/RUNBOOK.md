# Reproduction Runbook

## 1. Supported environment

The archive was assembled and verified with:

- Python 3.13.5
- NumPy 2.3.5
- SciPy 1.17.0
- SymPy 1.14.0
- mpmath 1.3.0
- Matplotlib 3.10.8

The code should also work on nearby modern versions, but exact solver behavior and runtime may differ. For archival replication, use the pinned versions in `requirements-lock.txt` when wheels are available for your platform.

## 2. Install

```bash
python -m venv .venv
source .venv/bin/activate        # Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## 3. Verify committed outputs

```bash
python tools/verify_results.py
python -m unittest discover -s tests -v
```

This checks JSON parsing, PASS verdicts, Boolean gates, source compilation, the expected audit range, figures, and manifest consistency.

## 4. Regenerate figures

```bash
python tools/generate_english_figures.py
```

The figures are generated from committed JSON outputs. No OCR, web access, or external data download is used.

## 5. Materialize the historical flat runtime

Many audits were written as a sequential research notebook in script form. They expect helper scripts and previous JSON results in the same directory.

```bash
python tools/materialize_runtime.py
```

This creates `build/runtime/` and copies:

- all Python audit files;
- all result JSON files;
- all configuration templates.

## 6. Run selected audits

```bash
python tools/run_all_audits.py --from-audit 39 --to-audit 45
```

Run a single audit:

```bash
python tools/run_all_audits.py --from-audit 71 --to-audit 71
```

Run the complete sequence:

```bash
python tools/run_all_audits.py --from-audit 39 --to-audit 71
```

### Runtime warning

A complete replay is expensive. A62 contains bootstrap calibration/validation simulations. A63–A71 contain large LP catalogues and exact symbolic calculations; A71 ranks 84 designs exactly and uses multiprocessing. Do not interpret a long runtime as a failed proof. Each runner log is stored under `logs/replay/`.

## 7. Exact versus numerical layers

- **Exact rational/symbolic:** SymPy rational LPs, determinant identities, Cramer certificates, root isolation, primal–dual equality, phase boundary divisibility, and sign proofs.
- **Numerical optimization:** SciPy HiGHS LP catalogues and cross-solver checks.
- **Monte Carlo/model-conditional:** A62 bootstrap calibration and validation.

The technical note for each audit distinguishes these layers.

## 8. Common platform issue

Some hosted Python environments inject unrelated spreadsheet-runtime startup hooks and print a warning to `stderr`. Such a warning appeared during A61/A71 packaging but did not originate in the research scripts. The repository verifier ignores no audit failure: a nonzero process exit remains a failure.

## 9. Publication workflow

Before a public GitHub release:

1. choose and add a license;
2. update repository URL in `CITATION.cff`;
3. create a tagged release;
4. archive the release on Zenodo if a DOI is desired;
5. preserve `MANIFEST.sha256` with the release asset.
