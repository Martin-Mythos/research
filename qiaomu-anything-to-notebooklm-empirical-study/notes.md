# Notes

## Original Prompt
- Evaluate https://github.com/joeseesun/qiaomu-anything-to-notebooklm empirically.

## Commands Used
- `find .. -name AGENTS.md -print`
- `git clone https://github.com/joeseesun/qiaomu-anything-to-notebooklm qiaomu-anything-to-notebooklm-src`
- `python3 -m pip install -r requirements.txt`
- `python3 check_env.py`
- `python3 main.py <input> "<prompt>"`
- `curl -L https://example.com -o ...` (failed: 403 tunnel)

## Experiments & Outcomes
- 安装依赖：成功。
- 环境检查：发现缺少 notebooklm CLI、MCP 路径异常。
- 本地 Markdown 输入：进入上传步骤后因 notebooklm 缺失失败。
- URL 输入：进入 URL 分支后同样在 notebooklm 调用失败。
- 不存在路径：被识别为 `search`，返回不支持类型。
- 手工基线：改用本地样例清洗，成功生成 notebooklm-ready txt/md。

## Failed Paths
- 公共网页抓取 `https://example.com`：`CONNECT tunnel failed, response 403`，放弃网络网页基线，改用本地样例。

## Verification Evidence
- 详见 `setup_log.md` 与 `run_log.md`。
