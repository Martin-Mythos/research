import re, json
from pathlib import Path
base=Path('agent-projects-empirical-study/artifacts/upstream')
files=list(base.glob('*.py'))+list(base.glob('*.md'))
report={}
for f in files:
    t=f.read_text(errors='ignore')
    report[f.name]={
      'oauth_mentions':len(re.findall(r'OAuth|Bearer|auth',t,re.I)),
      'mcp_mentions':len(re.findall(r'\bMCP\b|model context protocol',t,re.I)),
      'rerank_mentions':len(re.findall(r'rerank',t,re.I)),
      'sandbox_mentions':len(re.findall(r'sandbox|docker|e2b',t,re.I)),
    }
Path('agent-projects-empirical-study/artifacts/static_signal_scan.json').write_text(json.dumps(report,indent=2,ensure_ascii=False))
print('written',len(report))
