# 评估矩阵

## 1–5 分结果

| 维度 | HTML-Anything | Bento | 可验证依据 |
|---|---:|---:|---|
| Setup & Installation | 4 | 4 | 两者安装/build 均通过；前者测试 81/81，另有 Node engine warning；后者 single build 通过 |
| Dashboard 生成适配 | 4 | 3 | fixture 均过硬约束；语义 grid 更自然，Bento 是绝对坐标 slide |
| Long-form 生成适配 | 4 | 2 | 流式文章 DOM 更适合长文；Bento 固定画布需要分页 |
| PPT 生成适配 | 3 | 5 | HTML 可模拟切换；Bento 原生 slides/presenter/editor/state schema |
| R2 就绪度 | 4 | 5 | 两类 fixture 均无相对依赖；Bento build 结构性保证单文件，HTML-Anything 某些 style 仍可能复制 assets |
| DOM 可读与二次编辑 | 5 | 3 | 前者直接暴露 headings/articles；后者内容是可读 JSON、runtime DOM 非存储真相 |
| LLM/Context adherence 代理 | 3 | 3 | fixture validator 通过，但没有真实 Opus 5/GPT-5.6-Sol 调用，不能给模型实测高分 |

## 量化观察

`artifacts/metrics.json` 保存逐文件字节数、解析标签数、最大静态 DOM 深度、相对依赖、硬约束与 Bento 页数。HTML-Anything fixture 约 2.5 KB；Bento 每件约 603.7 KB。这个大小差异反映 Bento 自带完整编辑 runtime，不等价于“低效率”。静态 parser 看不到 Bento 解压后 runtime DOM，因此 DOM 深度只可用于载体结构观察，不是渲染复杂度公平比较。

## Prompt 策略判断

在本次可验证范围内，最有效的不是让模型输出 Chain-of-Thought，而是：canonical facts 单列、色彩语义显式逆转、输出 contract 独立、外部确定性 validator。真实模型间 token efficiency 与成功率仍需有 API key 的重复采样实验。
