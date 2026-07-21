from __future__ import annotations
import json, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class IntegrityTests(unittest.TestCase):
    def test_registry_results_pass(self):
        reg=json.loads((ROOT/'audit_registry.json').read_text())
        self.assertTrue(reg)
        for e in reg:
            d=json.loads((ROOT/'results'/e['result']).read_text())
            self.assertTrue(d['verdict'].startswith('PASS'))
            g=d.get('gates')
            if isinstance(g,dict): self.assertTrue(all(v is True for v in g.values()))
            else: self.assertEqual(d['pass_count'],d['gate_count'])
    def test_all_json_valid(self):
        for p in (ROOT/'results').glob('*.json'): json.loads(p.read_text())
    def test_notes_present(self):
        for e in json.loads((ROOT/'audit_registry.json').read_text()):
            if e.get('note'): self.assertTrue((ROOT/'docs'/'technical_notes'/e['note']).exists())
    def test_figures_present(self):
        self.assertGreater(len(list((ROOT/'figures').glob('*.png'))),0)
    def test_no_superseded_files_in_clean_package(self):
        forbidden={'a77_interval_contact_reset_certificate.py','a77_interval_contact_reset_results.json','_a75_fast_phase_test.py','_run_a75_m16_domain_roots.py'}
        present={p.name for p in ROOT.rglob('*') if p.is_file()}
        self.assertFalse(forbidden & present)
if __name__=='__main__': unittest.main()
