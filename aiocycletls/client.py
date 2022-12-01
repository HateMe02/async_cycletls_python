import json
import random
import urllib.parse

from aiocycletls import WSProxyClient, Response
from aiocycletls.browsers.browser_base import BrowserBase


class CycleTLSClient:

    def __init__(
            self,
            browsers: BrowserBase | list[BrowserBase],
            proxy_client: WSProxyClient | None = None
    ) -> None:
        self._browsers = [browsers] if not isinstance(browsers, list) else browsers
        self._proxy_client = WSProxyClient() if proxy_client is None else proxy_client

    async def get(
            self,
            url: str,
            params: dict | None = None,
            json_body: dict | None = None,
            body: str | None = None,
            headers: dict | None = None,
            proxy: str | None = None,
            cookies: dict | None = None,
            timeout: int | None = None,
            disable_redirect: bool = False,
            header_order: list | None = None,
            order_headers_as_provided: bool | None = None
    ) -> Response:
        return await self.request(
            url=url,
            method="GET",
            params=params,
            body=body,
            json_body=json_body,
            headers=headers,
            cookies=cookies,
            header_order=header_order,
            proxy=proxy,
            timeout=timeout,
            disable_redirect=disable_redirect,
            order_headers_as_provided=order_headers_as_provided
        )

    async def post(
            self,
            url: str,
            params: dict | None = None,
            json_body: dict | None = None,
            body: str | None = None,
            headers: dict | None = None,
            proxy: str | None = None,
            cookies: dict | None = None,
            timeout: int | None = None,
            disable_redirect: bool = False,
            header_order: list | None = None,
            order_headers_as_provided: bool | None = None
    ) -> Response:
        return await self.request(
            url=url,
            method="POST",
            params=params,
            body=body,
            json_body=json_body,
            headers=headers,
            cookies=cookies,
            header_order=header_order,
            proxy=proxy,
            timeout=timeout,
            disable_redirect=disable_redirect,
            order_headers_as_provided=order_headers_as_provided
        )

    async def put(
            self,
            url: str,
            params: dict | None = None,
            json_body: dict | None = None,
            body: str | None = None,
            headers: dict | None = None,
            proxy: str | None = None,
            cookies: dict | None = None,
            timeout: int | None = None,
            disable_redirect: bool = False,
            header_order: list | None = None,
            order_headers_as_provided: bool | None = None
    ) -> Response:
        return await self.request(
            url=url,
            method="PUT",
            params=params,
            body=body,
            json_body=json_body,
            headers=headers,
            cookies=cookies,
            header_order=header_order,
            proxy=proxy,
            timeout=timeout,
            disable_redirect=disable_redirect,
            order_headers_as_provided=order_headers_as_provided
        )

    async def delete(
            self,
            url: str,
            params: dict | None = None,
            json_body: dict | None = None,
            body: str | None = None,
            headers: dict | None = None,
            proxy: str | None = None,
            cookies: dict | None = None,
            timeout: int | None = None,
            disable_redirect: bool = False,
            header_order: list | None = None,
            order_headers_as_provided: bool | None = None
    ) -> Response:
        return await self.request(
            url=url,
            method="DELETE",
            params=params,
            body=body,
            json_body=json_body,
            headers=headers,
            cookies=cookies,
            header_order=header_order,
            proxy=proxy,
            timeout=timeout,
            disable_redirect=disable_redirect,
            order_headers_as_provided=order_headers_as_provided
        )

    async def options(
            self,
            url: str,
            params: dict | None = None,
            json_body: dict | None = None,
            body: str | None = None,
            headers: dict | None = None,
            proxy: str | None = None,
            cookies: dict | None = None,
            timeout: int | None = None,
            disable_redirect: bool = False,
            header_order: list | None = None,
            order_headers_as_provided: bool | None = None
    ) -> Response:
        return await self.request(
            url=url,
            method="OPTIONS",
            params=params,
            body=body,
            json_body=json_body,
            headers=headers,
            cookies=cookies,
            header_order=header_order,
            proxy=proxy,
            timeout=timeout,
            disable_redirect=disable_redirect,
            order_headers_as_provided=order_headers_as_provided
        )

    async def patch(
            self,
            url: str,
            params: dict | None = None,
            json_body: dict | None = None,
            body: str | None = None,
            headers: dict | None = None,
            proxy: str | None = None,
            cookies: dict | None = None,
            timeout: int | None = None,
            disable_redirect: bool = False,
            header_order: list | None = None,
            order_headers_as_provided: bool | None = None
    ) -> Response:
        return await self.request(
            url=url,
            method="PATCH",
            params=params,
            body=body,
            json_body=json_body,
            headers=headers,
            cookies=cookies,
            header_order=header_order,
            proxy=proxy,
            timeout=timeout,
            disable_redirect=disable_redirect,
            order_headers_as_provided=order_headers_as_provided
        )

    async def request(
            self,
            url: str,
            method: str,
            params: dict | None = None,
            json_body: dict | None = None,
            body: str | None = None,
            headers: dict | None = None,
            proxy: str | None = None,
            cookies: dict | None = None,
            timeout: int | None = None,
            disable_redirect: bool = False,
            header_order: list | None = None,
            order_headers_as_provided: bool | None = None
    ) -> Response:
        """
        TODO: Add form-data
        """

        if body and json_body:
            raise ValueError('You need a choice, what do you need: body or json_body')

        if cookies is not None:
            cookies = [
                {
                    'key': cookie_key,
                    'value': cookie_value
                }
                for cookie_key, cookie_value in cookies.items()
            ]
        url = self._add_parameters_to_request(url, params or {})
        browser = random.choice(self._browsers)
        browser_data = browser.get_parameters()
        print(browser)
        print(browser_data.ja3)
        print(browser_data.user_agent.to_browser_string())
        request_body = None

        if body is not None:
            request_body = body
        elif json_body is not None:
            request_body = json.dumps(json_body)

        return await self._proxy_client.request(
            url=url,
            method=method,
            ja3=browser_data.ja3,
            user_agent=browser_data.user_agent.to_browser_string(),
            body=request_body,
            headers=headers,
            cookies=cookies,
            header_order=header_order,
            proxy=proxy,
            timeout=timeout,
            disable_redirect=disable_redirect,
            order_headers_as_provided=order_headers_as_provided
        )

    def _add_parameters_to_request(self, url: str, params: dict) -> str:
        url = urllib.parse.unquote(url)
        parsed_url = urllib.parse.urlparse(url)
        get_args = parsed_url.query
        parsed_get_args = dict(urllib.parse.parse_qsl(get_args))
        parsed_get_args.update(params)
        parsed_get_args.update(
            {k: json.dumps(v) for k, v in parsed_get_args.items()
             if isinstance(v, (bool, dict))}
        )
        encoded_get_args = urllib.parse.urlencode(parsed_get_args, doseq=True)
        new_url = urllib.parse.ParseResult(
            parsed_url.scheme, parsed_url.netloc, parsed_url.path,
            parsed_url.params, encoded_get_args, parsed_url.fragment
        ).geturl()
        return new_url
