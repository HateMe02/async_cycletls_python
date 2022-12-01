import pydantic

from aiocycletls.enums.platform_type import PlatformType


class PlatformInformation(pydantic.BaseModel):
    type: PlatformType
    version: str

    def to_browser_string(self) -> str:
        return f"{self.type.value}/{self.version}"
