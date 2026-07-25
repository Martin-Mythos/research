# Goal
为任务管理 API 增加基于 HMAC JWT-like bearer token 的认证与授权，不新增第三方依赖。

# Done when
- 未授权请求返回 401。
- 用户只能访问和修改自己的任务；跨用户任务访问返回 404。
- 注册、登录、任务 CRUD 的测试全部通过：`python -m pytest -q`。
- 不修改无关的公开响应结构。
