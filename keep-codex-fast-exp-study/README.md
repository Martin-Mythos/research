# keep-codex-fast 实验研究报告（Experimental-based）

<!-- AI-GENERATED-NOTE -->
> [!NOTE]
> This is an AI-assisted research report. Treat it as a working artifact: review sources, code, and verification evidence before relying on it.
<!-- /AI-GENERATED-NOTE -->

## 研究问题
该项目声称可以让 Codex “更快”。本研究要验证：
1. 它是否真的执行了文档宣称的各类维护场景；
2. “变快”的机制是什么（直接提速算法，还是通过清理本地状态降低后续负担）；
3. 在可复现实验下，各模式的行为、安全性、开销如何。

## 实验对象与范围
- 上游仓库：`vibeforge1111/keep-codex-fast`
- 主要被测件：
  - `scripts/keep_codex_fast.py`
  - `tests/smoke_test.py`
  - `README.md`
- 测试方式：
  - 官方 smoke test（回归）
  - CLI 参数/模式覆盖
  - 构造 fake Codex home 的对照实验与小型性能基准

## 场景覆盖（“所有场景”）
### A. 文档/命令场景
- report-only（默认）
- details（明细输出）
- backup-only
- apply（执行归档维护）
- wait-for-codex-exit（等待 Codex 退出再 apply）

### B. 维护动作场景
- 旧会话归档（非删除）
- worktree 归档
- 大日志轮转
- config 死路径清理
- Windows 扩展路径归一化
- 备份与恢复清单生成

## 实验设计与结果

### 实验1：官方 smoke tests（功能正确性）
- 命令：`python external_repo/tests/smoke_test.py`
- 结果：通过（`smoke tests passed`）。
- 验证点：
  - report-only 不改动数据、不写备份；
  - backup-only 只备份，不迁移；
  - apply 会更新 sqlite 归档标记、迁移 session/worktree、清理 config、产出 restore/manifest；
  - alias 路径识别可用。

### 实验2：参数与模式覆盖
- 命令：`python external_repo/scripts/keep_codex_fast.py --help`
- 结果：确认参数族完整，包含 `--details`、`--wait-for-codex-exit`、阈值参数与路径覆盖参数。

### 实验3：details + wait-for-codex-exit 组合
- 方法：使用 fake home，执行 `apply + details + wait`。
- 结果：返回码 0；输出包含 thread_id/title/path 明细（details 生效）；在无 Codex 进程时可直接继续 apply（wait 分支可走通）。

### 实验4：性能微基准（1500 旧会话）
- 命令：`python benchmark_keep_codex_fast.py --threads 1500`
- 结果（单次）：
  - report: 0.285s
  - backup-only: 0.299s
  - apply: 0.412s
- 解读：脚本执行成本本身较低，apply 因文件移动/写 manifest 略慢，符合预期。

## 为什么“会更快”（基于证据）

## 已验证结论（Verified Findings）
1. **该项目并非“优化 Codex 模型推理速度”**，而是通过维护本地状态（sessions/worktrees/logs/config）来减少环境负担。  
2. **默认 report-only 是只读安全模式**，不会误删或误改。  
3. **apply 采用 backup-first + archive-not-delete 策略**，在可恢复前提下把陈旧状态移出热路径。  
4. **能处理几类典型拖慢来源**：旧会话索引、陈旧 worktree、日志体积、死项目引用、路径不一致。  
5. 因此其“加速”更准确地说是：**降低本地 I/O/扫描/索引压力，改善长期使用后的交互迟滞风险**。

## 推测（Speculation）
- 实际体感增益幅度将与个人 `.codex` 规模、会话习惯、并发进程数量高度相关；轻量用户可能不明显，重度用户更明显。
- 对“首 token 延迟”或“网络/API 推理时延”影响有限，因为该工具不改远端推理链路。

## 威胁与局限
- 本研究在 fake home 上复现实验，保证可控但不等价于每位用户真实机器负载。
- 未构造超大 GB 级日志/会话数据做长时压测；结论偏机制验证与功能验证。

## 复现实验步骤
1. `git clone https://github.com/vibeforge1111/keep-codex-fast.git external_repo`
2. `python external_repo/tests/smoke_test.py`
3. `python external_repo/scripts/keep_codex_fast.py --help`
4. `python benchmark_keep_codex_fast.py --threads 1500`

## 最终判断
这个项目“能让 Codex 更快”的说法在**工程机制层面成立**，但应理解为**本地状态治理带来的间接提速**，而不是模型推理本身变快。对于“历史包袱很重”的 Codex 使用环境，价值较高。
