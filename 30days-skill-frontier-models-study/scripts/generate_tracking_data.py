#!/usr/bin/env python3
import json, csv
from pathlib import Path
root = Path(__file__).resolve().parents[1]
art = root/'artifacts'
art.mkdir(exist_ok=True)
sources = [
 {'id':'zai-hf-glm52','topic':'GLM-5.2','url':'https://huggingface.co/blog/zai-org/glm-52-blog','type':'vendor technical blog','verified':True,'claims':['1M context','Terminal-Bench 2.1 81.0','SWE-bench Pro 62.1','FrontierSWE dominance 74.4','serving bottleneck shifts to KV-cache and CPU overhead','anti-hack needed because reward hacking observed']},
 {'id':'zai-docs-glm52','topic':'GLM-5.2','url':'https://docs.z.ai/guides/llm/glm-5.2','type':'vendor docs','verified':True,'claims':['developer docs for GLM-5.2','model can be selected in coding plans']},
 {'id':'benchlm-glm52','topic':'GLM-5.2','url':'https://benchlm.ai/models/glm-5-2','type':'benchmark aggregator','verified':True,'claims':['partial third-party benchmark coverage at research time']},
 {'id':'friendli-glm52','topic':'GLM-5.2','url':'https://friendli.ai/blog/GLM-5.2','type':'inference provider blog','verified':True,'claims':['744B MoE with about 40B active parameters','1M context provider availability']},
 {'id':'anthropic-fable-mythos','topic':'Anthropic Mythos/Fable 5','url':'https://www.anthropic.com/news/fable-mythos-access','type':'first-party policy statement','verified':True,'claims':['U.S. government export-control directive suspended access to Mythos 5 and Fable 5 for any foreign national','Anthropic disabled Mythos 5 and Fable 5 for all customers to ensure compliance','other Anthropic models were stated as unaffected']},
 {'id':'gtlaw-fable-mythos','topic':'Anthropic Mythos/Fable 5','url':'https://www.gtlaw.com/en/insights/2026/6/ai-company-anthropic-suspends-access-to-claude-fable-5-claude-mythos-5-following-us-export-control-directive','type':'legal analysis','verified':True,'claims':['directive affects foreign nationals inside and outside the United States','integration customers face service interruption even where U.S. personnel might not be restricted','case signals escalation of AI export-control compliance']},
 {'id':'aljazeera-fable-mythos','topic':'Anthropic Mythos/Fable 5','url':'https://www.aljazeera.com/news/2026/6/13/us-orders-anthropic-to-disable-ai-models-for-all-foreign-nationals','type':'news report','verified':True,'claims':['public reporting corroborates model access suspension for foreign nationals','the action was framed around national security concerns']},
 {'id':'last30days-repo','topic':'Methodology','url':'https://github.com/mvanhorn/last30days-skill','type':'methodology repo','verified':True,'claims':['multi-source search across social/web/GitHub/markets','engagement-scored evidence','recency oriented last-30-days workflow','raw outputs saved to memory directory']},
]
(art/'baseline_raw.json').write_text(json.dumps({'generated':'2026-06-19','sources':sources},indent=2,ensure_ascii=False))
intervals=[]
for i in range(1,31):
    if i <= 10:
        glm_vec='multi-turn instruction drift / benchmark harness assumptions'
        restricted_vec='directive scope, affected users, first-party statement verification'
    elif i <= 20:
        glm_vec='concurrency, quota, latency, KV-cache, long-context serving bottlenecks'
        restricted_vec='customer integration interruption, employee-access controls, compliance implementation'
    else:
        glm_vec='needle-in-haystack, reward-hacking, repo-scale context stress'
        restricted_vec='sovereign-AI substitution, open-weight alternatives, policy durability and rollback signals'
    intervals.append({'interval':i,'glm_vector':glm_vec,'mythos_fable_vector':restricted_vec,'evidence_required':'source URL + claim + confidence + contradiction check','metric_slots':['latency_ms_p50','latency_ms_p95','context_tokens','source_count','affected_access_classes','compliance_confidence_1to5']})
(art/'incremental_tracking_schema.json').write_text(json.dumps({'schema_version':2,'intervals':intervals},indent=2,ensure_ascii=False))
rows=[]
for i in intervals:
    rows.append({'interval':i['interval'],'track':'GLM-5.2','vector':i['glm_vector'],'status':'designed-not-live-benchmarked','confidence':3 if i['interval']<20 else 2})
    rows.append({'interval':i['interval'],'track':'Anthropic Mythos/Fable 5','vector':i['mythos_fable_vector'],'status':'verified-policy-event-tracked','confidence':4 if i['interval']<=20 else 3})
with (art/'simulated_30_interval_log.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=rows[0].keys(), lineterminator='\n'); w.writeheader(); w.writerows(rows)
print('wrote', art)
