- 依赖管理工具使用 uv
- 代码格式化工具使用 ruff
  ```sh
  uv run ruff format .
  ```
- API 框架使用 socketify
  - 安装
  ```sh
  uv add socketify
  ```
  - 示例
  ```python
  from socketify import App

  app = App()
  app.get("/", lambda res, req: res.end("Hello World!"))
  app.listen(
      3000,
      lambda config: print("Listening on port http://localhost:%d now\n" % config.port),
  )
  app.run()
  ```
- 结构体必须使用 pydantic
  ```python
  from pydantic import BaseModel


  class State(BaseModel): ...
  ```
- 异步工具包使用 anyio
  - 安装
  ```sh
  uv add anyio
  ```
  - 示例
  ```python
  from anyio import run


  async def main(): ...


  run(main)
  ```