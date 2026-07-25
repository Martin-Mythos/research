#!/usr/bin/env python3
"""检查产物完整性、硬约束、自包含性并输出机器可读指标。"""
import argparse, json, re
from html.parser import HTMLParser
from pathlib import Path
class P(HTMLParser):
 def __init__(self): super().__init__(); self.tags=0; self.depth=0; self.maxdepth=0; self.external=[]
 def handle_starttag(self,t,a):
  self.tags+=1; self.depth+=1; self.maxdepth=max(self.maxdepth,self.depth)
  for k,v in a:
   if k in ('src','href') and v and not (v.startswith(('data:','#','http://','https://','mailto:'))): self.external.append(v)
 def handle_endtag(self,t): self.depth=max(0,self.depth-1)
def main():
 a=argparse.ArgumentParser(); a.add_argument('project',type=Path); ns=a.parse_args(); rows=[]; ok=True
 for f in sorted((ns.project/'artifacts').glob('**/*.html')):
  if f.name=='research_report_artifact.html': continue
  text=f.read_text(); p=P(); p.feed(text); hard=True
  if f.stem.startswith('dashboard'): hard=all(x in text for x in ('波兰','红色','绿色','塞浦路斯'))
  bento='bento-doc' in text; doc_slides=None
  if bento:
   m=re.search(r'id="bento-doc">\s*([\s\S]*?)\s*</script>',text); doc_slides=len(json.loads(m.group(1))['slides']) if m else 0
  row={'文件':str(f.relative_to(ns.project)),'字节':f.stat().st_size,'标签数':p.tags,'最大DOM深度':p.maxdepth,'相对依赖':p.external,'硬约束通过':hard,'Bento页数':doc_slides}; rows.append(row); ok &= hard and not p.external and text.lower().startswith('<!doctype html>')
 out=ns.project/'artifacts/metrics.json'; out.write_text(json.dumps(rows,ensure_ascii=False,indent=2)); print(json.dumps(rows,ensure_ascii=False,indent=2)); raise SystemExit(0 if ok else 1)
if __name__=='__main__': main()
