#!/usr/bin/env python3
"""以确定性本地 fixture 生成三场景、两种载体的可复现基准产物。"""
from __future__ import annotations
import argparse, html, json, re
from pathlib import Path

SCENARIOS = {
 "dashboard": {"title":"CSA 2.0 / CRA 欧盟监管追踪器","kind":"仪表盘","facts":["波兰：支持（红色）","反对方：绿色","欧盟理事会轮值主席国：塞浦路斯"],"sections":[("硬约束状态","红色代表监管支持；绿色代表反对。"),("成员国快照","波兰被明确标为支持，不能按常见交通灯语义改写。"),("主席国","当前轮值主席国为塞浦路斯。")],"bg":"#fff7f2"},
 "brief": {"title":"AI Security Forum（ASF）最佳实践分析简报","kind":"长文","facts":["威胁建模","分层防御","事件演练"],"sections":[("摘要","安全治理应把模型、数据、工具调用与人员流程放入同一威胁模型。"),("最佳实践","采用最小权限、输入输出验证、可审计日志与人工升级路径。"),("实施路线","先建立资产清单和基线，再通过红队与桌面演练验证控制措施。")],"bg":"#f5f2e9"},
 "slides": {"title":"Digital Network Act（DNA）电信监管演示","kind":"演示文稿","facts":["竞争与投资","网络韧性","实施路线"],"sections":[("01 背景","统一规则需要兼顾跨境规模与成员国执行。"),("02 权衡","监管确定性可促进投资，但过度集中可能压缩竞争。"),("03 路线图","以公开咨询、影响评估、试点和复盘分阶段推进。")],"bg":"#eef3ff"},
}

def ha_page(s):
 cards=''.join(f'<article class="card"><h2>{html.escape(h)}</h2><p>{html.escape(p)}</p></article>' for h,p in s['sections'])
 facts=''.join(f'<li>{html.escape(x)}</li>' for x in s['facts'])
 return f'''<!doctype html><html lang="zh-CN" data-ha-style="{'dashboard' if s['kind']=='仪表盘' else 'architectural-spread'}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{s['title']}</title><style>:root{{--ink:#172033;--accent:#5b5ce2}}*{{box-sizing:border-box}}body{{margin:0;background:{s['bg']};color:var(--ink);font:16px/1.65 system-ui,sans-serif}}header,main{{max-width:1080px;margin:auto;padding:32px}}header{{border-bottom:3px solid var(--ink)}}.eyebrow{{text-transform:uppercase;letter-spacing:.18em}}.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:18px}}.card{{background:#fff;border:1px solid #ccd2dc;border-radius:16px;padding:22px;box-shadow:4px 4px 0 #172033}}li{{margin:.5rem 0}}.support{{color:#b42318}}.oppose{{color:#137333}}button{{padding:.6rem 1rem}}@media(max-width:600px){{header,main{{padding:20px}}}}@media(prefers-reduced-motion:reduce){{*{{scroll-behavior:auto!important}}}}</style></head><body><header><p class="eyebrow">HTML-Anything · 本地 Mock</p><h1>{s['title']}</h1><p>{s['kind']}场景；语义化流式 DOM，适合二次编辑。</p></header><main><section aria-labelledby="facts"><h2 id="facts">关键事实</h2><ul>{facts}</ul></section><section class="grid">{cards}</section><p><button id="toggle">切换证据说明</button> <span id="evidence" hidden>本页由无 API key 的确定性 fixture 生成，不代表真实模型输出。</span></p></main><script>const DATA={json.dumps(s,ensure_ascii=False)};document.querySelector('#toggle').onclick=()=>document.querySelector('#evidence').toggleAttribute('hidden');</script></body></html>'''

def bento_doc(s):
 slides=[]
 colors=['#18253f','#334e8c','#654a86']
 for i,(h,p) in enumerate(s['sections']):
  els=[{"id":f"title{i}","type":"text","x":80,"y":70,"w":1120,"h":100,"html":h,"fontSize":42,"fontWeight":700,"color":"#ffffff","align":"left","valign":"middle","lineHeight":1.1}, {"id":f"body{i}","type":"text","x":100,"y":230,"w":980,"h":220,"html":p,"fontSize":26,"fontWeight":400,"color":"#ffffff","align":"left","valign":"top","lineHeight":1.5}]
  if i==0:
   els.append({"id":"facts","type":"text","x":100,"y":500,"w":1050,"h":120,"html":" · ".join(s['facts']),"fontSize":20,"fontWeight":600,"color":"#ffd36a","align":"left","valign":"middle","lineHeight":1.3})
  slides.append({"id":f"slide-{i+1}","name":h,"background":colors[i],"transition":"fade","elements":els})
 return {"format":"bento/slides","title":s['title'],"size":{"width":1280,"height":720},"theme":{"fontFamily":"system-ui"},"present":{"slideNumber":True,"controls":True,"progress":True},"slides":slides}

def splice(shell, doc):
 block='<script type="application/bento+json" id="bento-doc">\n'+json.dumps(doc,ensure_ascii=False).replace('<','\\u003c')+'\n</script>'
 out,n=re.subn(r'<script type="application/bento\+json" id="bento-doc">[\s\S]*?</script>',block,shell,count=1)
 if n!=1: raise RuntimeError('Bento shell 中未找到唯一 #bento-doc')
 return out

def main():
 p=argparse.ArgumentParser(); p.add_argument('--project',type=Path,required=True); p.add_argument('--bento-shell',type=Path,required=True); a=p.parse_args()
 shell=a.bento_shell.read_text(); outputs=[]
 for key,s in SCENARIOS.items():
  hp=a.project/'artifacts/html_anything'/f'{key}.html'; bp=a.project/'artifacts/bento'/f'{key}.bento.html'
  hp.write_text(ha_page(s)); bp.write_text(splice(shell,bento_doc(s))); outputs += [hp,bp]
 for x in outputs: print(f'已生成：{x}（{x.stat().st_size} 字节）')
if __name__=='__main__': main()
