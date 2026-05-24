# Experiment Plan

## Research Questions
- Understand-Anything 能否成功安装并运行核心分析流水线？
- 在无 ASF 私有仓库访问时，工具是否仍可被端到端验证（以自身仓库替代）？
- 输出是否足以支持“页面/组件/内容结构”理解？

## Hypotheses
- H1: 按官方步骤可安装并运行（可能受 Node 版本影响）。
- H2: `scan-project` + `extract-import-map` + `compute-batches` 可生成可用结构数据。
- H3: 对私有仓库 asf-site-v2 的直接实验可能受权限阻塞。

## Test Environment
Ubuntu 24.04, Node v20.20.2, pnpm 10.6.2。

## Test Dataset / Input
- Tool under test: `Lum1104/Understand-Anything`
- Subject repo: `xwbcl123/asf-site-v2`（私有，尝试访问）
- Fallback corpus: Understand-Anything 仓库本体。

## Steps
1. 克隆两个仓库并记录访问结果。
2. 安装依赖并执行测试。
3. 运行核心脚本：scan/import-map/batches。
4. 与手工基线（tree/find/rg + README/package）比较可得结构信息。

## Expected Observations
- 输出 JSON 包含文件列表、导入图、批次分组。
- 可能出现文档/脚本参数不一致。

## Success Criteria
- 至少在一个可访问仓库上完成 end-to-end 结构化输出。

## Failure Criteria
- 无法安装或核心脚本无法运行。

## Comparison Baseline
- 对 subject repo 的手工侦察；若无权限则记录阻断并在 fallback corpus 上示范。

## Evidence to Collect
- clone/install/test/run 日志；生成的 JSON 工件；命令清单；失败信息。
