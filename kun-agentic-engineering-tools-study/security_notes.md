# security_notes.md

- Lavish: 默认 loopback 本地服务较安全；README 明确警告绑定到通配地址会暴露未认证本地文件服务，不能在不可信网络中使用。
- Treehouse: repo-level hooks 被忽略是正向安全设计；user-level hooks 可以执行 shell 命令，需要纳入个人 dotfiles 审计。
- No Mistakes: 作为 git proxy/gate，会处理分支、远程推送、PR 创建与 AI agent 调用；完整使用前应在低风险仓库验证权限边界、日志留存、secret 暴露和自动修复策略。
