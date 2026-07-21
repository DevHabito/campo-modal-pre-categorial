from __future__ import annotations
import json, re, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

class RepositoryIntegrityTests(unittest.TestCase):
    def setUp(self):
        self.results=[]
        for p in sorted((ROOT/'results').glob('a[0-9][0-9]*_results.json')):
            m=re.match(r'a(\d+)_',p.name)
            if m and 39<=int(m.group(1))<=71:
                self.results.append((int(m.group(1)),p,json.loads(p.read_text(encoding='utf-8'))))
    def test_complete_audit_range(self):
        self.assertEqual([n for n,_,_ in self.results],list(range(39,72)))
    def test_all_verdicts_pass(self):
        for _,p,d in self.results:
            self.assertTrue(d['verdict'].startswith('PASS_'),p.name)
    def test_all_top_level_gates_pass(self):
        for _,p,d in self.results:
            self.assertTrue(d['gates'],p.name)
            self.assertTrue(all(v is True for v in d['gates'].values()),p.name)
    def test_english_figure_count(self):
        self.assertEqual(len(list((ROOT/'figures').glob('*.png'))),58)
    def test_original_paper_present(self):
        self.assertTrue((ROOT/'paper'/'MFRP-TR-2026-01_Informational_Requirements_v1.1.pdf').exists())
if __name__=='__main__': unittest.main()
