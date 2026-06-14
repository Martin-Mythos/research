#!/usr/bin/env python3
from pathlib import Path
root = Path(__file__).resolve().parents[1] / 'artifacts' / 'talking-breads-v1'
text = '\n'.join(p.read_text(errors='ignore') for p in (root/'src').glob('**/*') if p.is_file())
required = ['Talking Breads Tervuren','Student lunch offer','Allergy information','Opening hours','Google Maps','Instagram','no online ordering']
for item in required:
    if item not in text:
        raise SystemExit(f'MISSING: {item}')
for forbidden in ['Order now','Pay online','Checkout','Delivery scheduling']:
    if forbidden.lower() in text.lower():
        raise SystemExit(f'FORBIDDEN: {forbidden}')
print('manual validation passed')
