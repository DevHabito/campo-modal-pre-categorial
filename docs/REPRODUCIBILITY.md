# Reproducibility guide

## Environment

Python 3.11 or newer is recommended. Create the environment with either:

```bash
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

or:

```bash
conda env create -f environment.yml
conda activate campo-modal-research
```

## Running an audit

The scripts were written to run from the `audits/` directory because several stages import earlier sibling scripts and write result directories relative to the working directory.

```bash
cd audits
python a8_1_condensation_code_resolution.py
```

Many later audits are Monte Carlo or large exact enumerations and may require substantial memory or compute. Seeds and protocol constants are embedded in the scripts and recorded in summary JSON files.

## Evidence classes

Do not treat every CSV as the same kind of evidence:

1. **proof/theorem note** — mathematical derivation, usually `*_theorem.md`;
2. **exact enumeration** — exhaustive finite computation;
3. **synthetic witness** — constructed example or counterexample;
4. **Monte Carlo audit** — finite seeded experiment;
5. **software regression check** — confirms that implementation matches an identity;
6. **failed protocol** — retained rather than hidden;
7. **corrective protocol** — fixes a diagnostic or specification without erasing the original.

## A8.1 correction

The phrase “5,234 distinct labeled condensation-poset codes” was ambiguous. A8.1 proves that:

- 6,942 is the number of full labeled reachability preorders on five vertices arising as condensation structures;
- 5,234 is the number of minimum-representative quotient-poset codes used by the original A8 implementation;
- 139 is the fully unlabeled count;
- the one-edge-flip fraction `75/256` remains unchanged for `n=5` under both encodings.

## Integrity

`MANIFEST.csv` and `SHA256SUMS.txt` allow verification of every packaged file. Run:

```bash
python tools/validate_repository.py
```
