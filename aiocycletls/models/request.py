import pydantic


def to_camel(string: str) -> str:
    words = string.split("_")
    return f'{words[0]}{"".join(map(str.capitalize, words[1:]))}'


class Request(pydantic.BaseModel):
    url: str
    method: str
    ja3: str
    user_agent: str
    body: str
    headers: dict
    proxy: str
    cookies: list | None
    timeout: int
    disable_redirect: bool
    header_order: list | None
    order_headers_as_provided: bool | None

    class Config:
        alias_generator = to_camel
