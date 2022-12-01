import json
from http.cookies import SimpleCookie

import pydantic


class Response(pydantic.BaseModel):
    request_id: str
    status_code: int
    headers: dict
    body: str

    def jsonable_body(self) -> dict:
        return json.loads(self.body)

    @property
    def cookies(self) -> list[SimpleCookie]:
        return [
            SimpleCookie(f'{header_key}: {header_value}')
            for header_key, header_value in self.headers.items()
            if header_key.lower() == 'set-cookie'
        ]

    class Config:
        fields = {
            "request_id": "RequestID",
            "status_code": "Status",
            "headers": "Headers",
            "body": "Body",
        }
