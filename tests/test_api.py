from notebook_agent.api import (
    HealthResponse,
    _public_host,
    build_openapi_spec,
    render_swagger_ui,
)


def test_build_openapi_spec_documents_health_only():
    spec = build_openapi_spec(host="localhost", port=3000)

    assert spec["openapi"] == "3.0.3"
    assert list(spec["paths"]) == ["/health"]
    assert spec["servers"] == [{"url": "http://localhost:3000"}]


def test_public_host_maps_bind_all_to_localhost():
    assert _public_host("0.0.0.0") == "localhost"
    assert _public_host("127.0.0.1") == "127.0.0.1"


def test_render_swagger_ui_loads_openapi_document():
    html = render_swagger_ui()

    assert "swagger-ui" in html
    assert 'url: "/openapi.json"' in html


def test_health_response_defaults_to_ok():
    assert HealthResponse().status == "ok"
