import json
from datetime import date

user_story = "作为写作者，我希望在 Markdown 编辑时获得 AI 幽灵补全（监听光标+防抖+流式返回），以更快完成草稿。"

artifact1 = {
  "experiment": "需求摄取",
  "entry_skill": "ce-plan",
  "inferred_pipeline": [
    "Phase0.2 检索 docs/brainstorms/*-requirements.md",
    "无匹配时进入 Phase0.4 bootstrap",
    "将用户输入注入 <feature_description> #$ARGUMENTS",
    "Phase1 并行触发 repo/learnings/web research 子代理"
  ],
  "normalized_input": {
    "raw": user_story,
    "domain": "software",
    "requires_clarification": False,
    "assumptions": [
      "前端为 Web 编辑器，具备光标事件",
      "后端有可用 LLM 流式 API",
      "允许新增 debounce 与取消机制"
    ]
  },
  "tracker_integration_mode": "optional",
}

artifact2 = {
  "experiment": "工程卡片拆解",
  "feature": "多人实时协同编辑",
  "tickets": [
    {
      "id": "ENG-RT-01",
      "title": "协同核心算法选型 Spike（CRDT vs OT）",
      "type": "spike",
      "acceptance": ["给出 CRDT/OT 冲突模型对比", "给出文档长度 10k 行下复杂度估计", "输出推荐方案与放弃理由"]
    },
    {
      "id": "ENG-RT-02",
      "title": "WebSocket 会话与房间路由层",
      "type": "implementation",
      "acceptance": ["支持 docId 级房间", "支持断线重连与会话恢复 token", "服务端广播延迟 P95 < 120ms"]
    },
    {
      "id": "ENG-RT-03",
      "title": "增量操作协议与冲突合并",
      "type": "implementation",
      "acceptance": ["定义 op schema（insert/delete/format）", "可重放日志恢复文档", "并发写入一致性回归测试通过"]
    },
    {
      "id": "ENG-RT-04",
      "title": "协同光标与选区 Presence 同步",
      "type": "implementation",
      "acceptance": ["显示他人光标颜色与名称", "presence 心跳超时剔除", "弱网抖动下不出现幽灵光标"]
    },
    {
      "id": "ENG-RT-05",
      "title": "离线缓存与重连后增量补偿",
      "type": "implementation",
      "acceptance": ["本地 op 队列持久化", "重连后按版本向量补偿", "冲突回放可观测日志"]
    }
  ],
  "score": {"architecture_depth": 8.5, "reason": "覆盖算法、传输、协议、presence 与离线恢复五层关键面"}
}

artifact3 = {
  "experiment": "模糊需求抗压",
  "input": "让编辑器的响应速度变得很快",
  "expected_by_skill_design": [
    "先做澄清提问或 planning bootstrap",
    "若缺指标则生成调研/基线测量任务，而非直接臆造方案",
    "将未验证项放入 Assumptions（headless 模式）"
  ],
  "simulated_output": [
    "SPIKE: 建立前端输入延迟与首屏渲染基线（P50/P95）",
    "SPIKE: flamegraph 分析主线程阻塞来源",
    "TASK: 定义性能预算与验收门槛后再进入实现"
  ]
}

root = "/workspace/research/compound-plugin-saas-study"
with open(f"{root}/artifact-exp1-input-schema.json", "w", encoding="utf-8") as f:
    json.dump(artifact1, f, ensure_ascii=False, indent=2)
with open(f"{root}/artifact-exp2-engineering-tickets.json", "w", encoding="utf-8") as f:
    json.dump(artifact2, f, ensure_ascii=False, indent=2)
with open(f"{root}/artifact-exp3-edgecase-log.json", "w", encoding="utf-8") as f:
    json.dump(artifact3, f, ensure_ascii=False, indent=2)

print("generated", date.today().isoformat())
