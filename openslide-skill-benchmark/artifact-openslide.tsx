import type { Page } from '@open-slide/core'

const Cover: Page = () => (
  <div style={{padding: 96, background:'#0B1020', color:'#F8FAFC', width:'100%', height:'100%'}}>
    <h1 style={{fontSize:64, marginBottom:24}}>2026 AI Agent 企业级落地实践与安全挑战</h1>
    <p style={{fontSize:30, opacity:0.9}}>从 PoC 到规模化：价值闭环、治理框架与风险控制</p>
  </div>
)

const P2: Page = () => (
  <div style={{padding: 80}}>
    <h2 style={{fontSize:48}}>1. 企业落地现状：从“工具试点”到“流程重构”</h2>
    <ul style={{fontSize:30, lineHeight:1.6}}>
      <li>高频场景：客服、知识检索、销售助理、研发 Copilot</li>
      <li>瓶颈转移：从模型能力不足转向数据与流程割裂</li>
      <li>关键问题：ROI 不可量化、责任边界不清晰</li>
    </ul>
  </div>
)

const P3: Page = () => (
  <div style={{padding: 80}}>
    <h2 style={{fontSize:48}}>2. 参考架构：AgentOps 四层模型</h2>
    <ol style={{fontSize:30, lineHeight:1.6}}>
      <li>交互层：多模态入口、权限分级</li>
      <li>编排层：任务分解、工具调用、记忆管理</li>
      <li>治理层：审计、评测、红队与合规策略</li>
      <li>基础层：模型路由、向量库、观测与成本控制</li>
    </ol>
  </div>
)

const P4: Page = () => (
  <div style={{padding: 80}}>
    <h2 style={{fontSize:48}}>3. 安全挑战：四类高风险面</h2>
    <table style={{fontSize:24, width:'100%', borderCollapse:'collapse'}}>
      <tbody>
        <tr><td>提示词注入</td><td>越权调用工具、数据外泄</td><td>上下文隔离 + 策略引擎</td></tr>
        <tr><td>数据污染</td><td>检索召回被投毒</td><td>数据签名 + 来源评级</td></tr>
        <tr><td>行动失控</td><td>自动执行误操作</td><td>人机协同闸门 + 回滚</td></tr>
        <tr><td>合规缺失</td><td>隐私与行业监管违规</td><td>分级脱敏 + 留痕审计</td></tr>
      </tbody>
    </table>
  </div>
)

const P5: Page = () => (
  <div style={{padding: 80}}>
    <h2 style={{fontSize:48}}>4. 落地路径：90 天分阶段推进</h2>
    <ul style={{fontSize:30, lineHeight:1.6}}>
      <li>0-30 天：场景盘点、基线评估、最小可行治理</li>
      <li>31-60 天：双轨试点（效率场景 + 决策场景）</li>
      <li>61-90 天：指标复盘、模板化复制、组织赋能</li>
    </ul>
  </div>
)

const P6: Page = () => (
  <div style={{padding: 80}}>
    <h2 style={{fontSize:48}}>5. KPI 与董事会沟通口径</h2>
    <ul style={{fontSize:30, lineHeight:1.6}}>
      <li>效率：工时节省率、处理时延、自动化覆盖率</li>
      <li>质量：首轮命中率、人工返工率、客户满意度</li>
      <li>风险：高危告警数、越权拦截率、审计闭环时长</li>
    </ul>
  </div>
)

export default [Cover, P2, P3, P4, P5, P6] satisfies Page[]
