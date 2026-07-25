# 实验计划

## 目标与可证伪假设

1. HTML-Anything 的语义 DOM 比 Bento JSON/绝对定位更便于代码层二次编辑。
2. Bento 的原生 slide state 与内联 runtime 比自由 HTML 更适合演示和单对象分发。
3. 把硬事实放入独立、可机检的 constraint block，比散落在叙述中的提示更可靠。

## 三场景遍历

- A：CSA 2.0 / CRA EU tracker；fixture 强制“红=支持、绿=反对、波兰=红、主席国=塞浦路斯”。这里把“塞浦路斯”当作题设约束，不把它升级为对现实政治状态的独立核验。
- B：ASF 最佳实践长文分析简报。
- C：DNA 电信监管三页演示。

每一场景生成两类 artifact：HTML-Anything 风格的语义单页，以及注入真实 Bento built shell 的 `.bento.html`。

## Prompt 策略

| 策略 | 结构 | 预期 |
|---|---|---|
| System/User 分离 | role、任务与材料分别承载 | 权限清晰，适合 API |
| XML mega-prompt | `<constraints>`、`<content>`、`<output_contract>` | 单消息中边界明确，易抽取 |
| 分阶段布局指令 | 先事实表，再结构，再输出与 validator | 可降低遗漏，但增加 token 与执行步骤 |

推荐模板：先声明不可覆盖的事实；要求输出只引用 canonical facts；把 style contract 与事实 contract 分开；最后运行外部 validator，而不是依赖模型“silent audit”。不要求输出隐式 Chain-of-Thought，只要求短的可审计检查表。

## 执行方法

1. shallow clone 到 `/tmp` 并固定 commit。
2. `npm ci`、build/test；Bento 执行 `build:single`。
3. 无任何 LLM API key：用 `generate_benchmark.py` 生成确定性 fixtures，并明确标为 mock，避免伪造 Opus 5/GPT-5.6-Sol 成绩。
4. `validate_artifacts.py` 检查 doctype、相对链接、硬约束、DOM 统计和 Bento JSON 页数。
5. `publish_r2_mock.sh` 复制 HTML 并产生 SHA-256 manifest，模拟 R2 上传前 staging；不调用 Cloudflare API。

## 评分

1=不可用，2=明显不足，3=可用但需补强，4=良好，5=强且已验证。模型响应性无法在无 key 时直接评分；矩阵中的该项是“workflow/prompt 可验证性代理分”，不能当作模型 head-to-head。
