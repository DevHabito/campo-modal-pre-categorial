#!/usr/bin/env python3
from pathlib import Path
import csv
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
errors: list[str] = []

for path in ROOT.rglob('*summary.json'):
    try:
        json.loads(path.read_text(encoding='utf-8'))
    except Exception as exc:
        errors.append(f'Invalid JSON: {path.relative_to(ROOT)}: {exc}')

manifest = ROOT / 'MANIFEST.csv'
if not manifest.exists():
    errors.append('MANIFEST.csv missing')
else:
    with manifest.open(newline='', encoding='utf-8') as handle:
        for row in csv.DictReader(handle):
            path = ROOT / row['path']
            if not path.exists():
                errors.append(f'Missing: {row["path"]}')
                continue
            if path.stat().st_size != int(row['bytes']):
                errors.append(f'Size mismatch: {row["path"]}')
                continue
            digest = hashlib.sha256(path.read_bytes()).hexdigest()
            if digest != row['sha256']:
                errors.append(f'Hash mismatch: {row["path"]}')

if errors:
    print('\n'.join(errors))
    sys.exit(1)

print('Repository validation passed.')
