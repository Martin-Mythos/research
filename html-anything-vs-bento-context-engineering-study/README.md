# HTML-Anything vs Bento：Context Engineering 实证研究

本目录是可独立复核的研究项目。**最终结论**：HTML-Anything 的自由语义 DOM 更适合 dashboard/长文和源码二次编辑；Bento 的单文件 runtime 与强 slide schema 更适合演示、GUI 编辑和对象化分发。两者均可形成 R2-friendly 单文件，但 HTML-Anything 的某些 style assets 仍需额外检查。

重要边界：本次没有 Opus 5 / GPT-5.6-Sol API key，模型比较未被实测；产物使用本地 deterministic mock，模型维度只给出实验设计与 workflow proxy，不伪造模型成绩。

完整方法、证据、结论层级、限制与复现命令请阅读 [`research_report.md`](research_report.md)。入口还包括：

- [`experiment_plan.md`](experiment_plan.md)：假设、三场景与 prompt 策略；
- [`notes/repo_recon.md`](notes/repo_recon.md)：上游架构侦察；
- [`evaluation_matrix.md`](evaluation_matrix.md)：1–5 分矩阵；
- [`run_log.md`](run_log.md)：实际命令与关键输出；
- [`artifacts/research_report_artifact.html`](artifacts/research_report_artifact.html)：stand-alone 交互报告；
- [`scripts/`](scripts/)：生成、验证与 Mock R2 staging。
