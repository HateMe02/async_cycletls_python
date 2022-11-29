import json

import pydantic


class Response(pydantic.BaseModel):
    request_id: str
    status_code: int
    headers: dict
    body: str

    def jsonable_body(self) -> dict:
        return json.loads(self.body)

    class Config:
        fields = {
            "request_id": "RequestID",
            "status_code": "Status",
            "headers": "Headers",
            "body": "Body",
        }
