# Repo Recon

- 项目定位：面向代码库“理解”的插件/技能体系，包含扫描、导入关系抽取、批处理分群、dashboard 可视化组件。
- 运行栈：Node.js + pnpm monorepo；TypeScript/Vitest；部分 Python 脚本用于图合并。
- 入口：`understand-anything-plugin/skills/understand/*.mjs|.py` 与 dashboard 包。
- 声明能力：多语言解析、结构图谱、分域理解、差异理解、可视化。
- 风险/不确定性：文档与脚本参数存在隐式约束；私有仓库访问依赖认证上下文。
