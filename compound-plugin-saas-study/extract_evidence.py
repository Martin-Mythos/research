import json
import re
from pathlib import Path

SRC_ROOT = Path('/tmp/compound-engineering-plugin')
OUT = Path('/workspace/research/compound-plugin-saas-study/artifact-source-evidence.json')

checks = [
    {
        'id': 'parser-load-plugin',
        'file': 'src/parsers/claude.ts',
        'patterns': [r'export async function loadClaudePlugin', r'const PLUGIN_MANIFEST = path\.join\("\.claude-plugin", "plugin\.json"\)']
    },
    {
        'id': 'skill-arg-injection',
        'file': 'plugins/compound-engineering/skills/ce-plan/SKILL.md',
        'patterns': [r'<feature_description> #\$ARGUMENTS </feature_description>', r'Phase 0: Resume, Source, and Scope', r'Phase 1: Gather Context']
    },
    {
        'id': 'issue-tracker-routing',
        'file': 'plugins/compound-engineering/skills/ce-plan/references/plan-handoff.md',
        'patterns': [r'project_tracker: github', r'project_tracker: linear', r'gh issue create', r'linear issue create']
    }
]

report = []
for c in checks:
    p = SRC_ROOT / c['file']
    text = p.read_text(encoding='utf-8')
    hit = {}
    for pat in c['patterns']:
        m = re.search(pat, text)
        hit[pat] = bool(m)
    report.append({'id': c['id'], 'file': c['file'], 'hits': hit, 'all_pass': all(hit.values())})

OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
print('wrote', OUT)
