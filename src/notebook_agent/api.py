"""Minimal socketify API server with Swagger UI."""

from __future__ import annotations

import json
from typing import Any

from pydantic import BaseModel

DEFAULT_HOST = "0.0.0.0"
DEFAULT_PORT = 3000
OPENAPI_PATH = "/openapi.json"
DOCS_PATH = "/docs"


class HealthResponse(BaseModel):
    status: str = "ok"


def build_openapi_spec(
    *, host: str = "localhost", port: int = DEFAULT_PORT
) -> dict[str, Any]:
    return {
        "openapi": "3.0.3",
        "info": {
            "title": "Notebook Agent API",
            "version": "0.1.0",
        },
        "servers": [{"url": f"http://{host}:{port}"}],
        "paths": {
            "/health": {
                "get": {
                    "summary": "Health check",
                    "responses": {
                        "200": {
                            "description": "Service is healthy.",
                            "content": {
                                "application/json": {
                                    "schema": HealthResponse.model_json_schema(),
                                }
                            },
                        }
                    },
                }
            },
        },
    }


def render_swagger_ui(*, openapi_path: str = OPENAPI_PATH) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>API Docs</title>
  <link rel="stylesheet" href="https://unpkg.com/swagger-ui-dist@5/swagger-ui.css" />
</head>
<body>
  <div id="swagger-ui"></div>
  <script src="https://unpkg.com/swagger-ui-dist@5/swagger-ui-bundle.js"></script>
  <script>
    SwaggerUIBundle({{
      url: "{openapi_path}",
      dom_id: "#swagger-ui",
    }});
  </script>
</body>
</html>"""


def _public_host(host: str) -> str:
    if host in {"0.0.0.0", "::"}:
        return "localhost"
    return host


def create_app(*, host: str = DEFAULT_HOST, port: int = DEFAULT_PORT) -> Any:
    from socketify import App

    app = App()
    spec = build_openapi_spec(host=_public_host(host), port=port)
    spec_bytes = json.dumps(spec).encode()

    app.get("/health", lambda res, req: res.end(HealthResponse().model_dump()))
    app.get(
        OPENAPI_PATH,
        lambda res, req: res.write_header("Content-Type", "application/json").end(
            spec_bytes
        ),
    )
    app.get(
        DOCS_PATH,
        lambda res, req: res.write_header(
            "Content-Type", "text/html; charset=utf-8"
        ).end(render_swagger_ui()),
    )

    return app


def run(port: int = DEFAULT_PORT, host: str = DEFAULT_HOST) -> None:
    app = create_app(host=host, port=port)
    public_host = _public_host(host)

    def on_listen(config: Any) -> None:
        print(f"Listening on http://{public_host}:{config.port}")
        print(f"Swagger UI: http://{public_host}:{config.port}{DOCS_PATH}")

    app.listen(port, on_listen)
    app.run()


if __name__ == "__main__":
    import fire

    fire.Fire(run)
