# Evaluation Matrix

| Dimension | Score (1-5) | Evidence |
|---|---:|---|
| Installability | 4 | 安装成功，但 Node 版本警告 |
| Documentation Quality | 3 | 主要流程可推断；脚本输入细节需读源码 |
| Core Functionality | 4 | scan/import-map/batches 在替代语料可跑通 |
| Scenario Fit | 2 | ASF 私有仓库无法访问，目标场景仅部分验证 |
| Experiment Reproducibility | 4 | 命令与日志完整可复现 |
| Engineering Quality | 4 | 测试覆盖多语言解析；但测试总命令存在 unhandled error |
| Practical Value | 3 | 可快速给出代码结构图基础数据 |
| Integration Potential | 4 | JSON 输出适配下游 dashboard/agent 流水线 |
| Risk & Safety | 3 | 依赖较多；私有仓库权限与环境配置是主要风险 |
