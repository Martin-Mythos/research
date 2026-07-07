from pathlib import Path
import re, json
root = Path('/tmp/loopkit-src/skills')
changed = ['PROMPT.md','IMPLEMENTATION_PLAN.md','src/routes/api.py','src/services/auth.py','src/services/tasks.py','src/data/store.py','tests/test_api.py']
keywords = 'auth authorization bearer token endpoint input test pytest sqlite sql commit PR'.lower()
rows=[]
for f in sorted(root.glob('*/SKILL.md')):
    text=f.read_text()
    name=f.parent.name
    m=re.search(r'when_to_use:\s*(.*)', text)
    trigger=m.group(1) if m else ''
    hits=[w for w in re.split(r'[,/ ]+', trigger.lower()) if w and w in keywords]
    likely=bool(hits) or name in {'spec-first','adversarial-verify','context-budget','authz-check','input-validation','owasp-review','write-failing-test-first','contract-test','secret-scan','clean-commits'}
    rows.append({'skill':name,'trigger':trigger,'likely_for_mvp_auth':likely,'evidence_terms':hits})
Path('loopkit-mvp-practicality-study/artifacts/skill_trigger_scan.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2))
print(json.dumps(rows,ensure_ascii=False,indent=2))
