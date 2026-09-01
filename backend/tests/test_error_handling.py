import asyncio
from starlette.requests import Request

from app.main import unhandled_exception_handler


def test_unhandled_exception_handler_returns_sanitized_500():
    scope = {"type": "http", "method": "GET", "path": "/some/path", "headers": []}
    request = Request(scope)

    exc = RuntimeError("some internal database detail that must not leak")
    response = asyncio.run(unhandled_exception_handler(request, exc))

    assert response.status_code == 500
    body = response.body.decode()
    assert "Internal server error" in body
    assert "database detail" not in body
