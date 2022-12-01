import pydantic

from aiocycletls.enums.system_platform import SystemPlatform


class SystemInformation(pydantic.BaseModel):
    type: SystemPlatform
    details: list[str]

    def to_browser_string(self) -> str:
        return '; '.join([self.type.value, *self.details])
