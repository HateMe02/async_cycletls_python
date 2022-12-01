import pydantic

from aiocycletls.models.browser.user_agent import UserAgent


class BrowserData(pydantic.BaseModel):
    user_agent: UserAgent
    ja3: str
