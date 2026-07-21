#!/usr/bin/env python3
from __future__ import annotations
import compileall, hashlib, json, re, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def main():
    failures=[]
    main_results=[]
    for p in sorted((ROOT/'results').glob('a[0-9][0-9]*_results.json')):
        m=re.match(r'a(\d+)_',p.name)
        if not m or not 39<=int(m.group(1))<=71: continue
        try: d=json.loads(p.read_text(encoding='utf-8'))
        except Exception as e: failures.append(f'{p}: invalid JSON: {e}'); continue
        main_results.append((int(m.group(1)),p,d))
        if not str(d.get('verdict','')).startswith('PASS_'): failures.append(f'{p}: non-PASS verdict {d.get("verdict")}')
        gates=d.get('gates')
        if not isinstance(gates,dict) or not gates: failures.append(f'{p}: missing gates')
        elif not all(v is True for v in gates.values()): failures.append(f'{p}: failing/non-Boolean gates')
    nums=sorted(n for n,_,_ in main_results)
    if nums!=list(range(39,72)): failures.append(f'Expected A39-A71, found {nums}')
    if len(list((ROOT/'figures').glob('*.png')))!=58: failures.append('Expected 58 English PNG figures')
    if not compileall.compile_dir(ROOT/'audits',quiet=1,force=True): failures.append('Audit source compilation failed')
    if not compileall.compile_dir(ROOT/'tools',quiet=1,force=True): failures.append('Tool source compilation failed')
    manifest=ROOT/'MANIFEST.sha256'
    if manifest.exists():
        for line in manifest.read_text(encoding='utf-8').splitlines():
            if not line.strip(): continue
            digest,rel=line.split('  ',1); path=ROOT/rel
            if not path.exists(): failures.append(f'Manifest missing file: {rel}'); continue
            actual=hashlib.sha256(path.read_bytes()).hexdigest()
            if actual!=digest: failures.append(f'Manifest mismatch: {rel}')
    print(json.dumps({'audit_results':len(main_results),'figures':len(list((ROOT/'figures').glob('*.png'))),'failures':failures,'status':'PASS' if not failures else 'FAIL'},indent=2))
    if failures: raise SystemExit(1)
if __name__=='__main__': main()
