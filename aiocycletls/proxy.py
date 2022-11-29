import json

import websockets

from aiocycletls.models.request import Request
from aiocycletls.models.response import Response


class WSProxyClient:

    def __init__(
            self,
            port: int = 8080,
            timeout: int = 30
    ) -> None:
        self._base_url = f"ws://localhost:{port}"
        self._timeout = timeout

    async def request(
            self,
            url: str,
            method: str,
            ja3: str,
            user_agent: str,
            body: str | None = None,
            headers: dict | None = None,
            proxy: str | None = None,
            cookies: list | None = None,
            timeout: int | None = None,
            disable_redirect: bool = False,
            header_order: list | None = None,
            order_headers_as_provided: bool | None = None
    ) -> Response:
        request = Request(
            url=url,
            method=method,
            ja3=ja3,
            userAgent=user_agent,
            body=body or "",
            headers=headers or {},
            proxy=proxy or "",
            cookies=cookies,
            timeout=timeout or self._timeout,
            disableRedirect=disable_redirect,
            header_order=header_order,
            order_headers_as_provided=order_headers_as_provided
        )

        async with websockets.connect(self._base_url, close_timeout=0.1, max_size=1_000_000_000) as websocket:
            await websocket.send(json.dumps({
                'requestId': 'requestId',
                'options': request.dict(by_alias=True, exclude_none=True)
            }))
            response = json.loads(await websocket.recv())
        return Response.parse_obj(response)
