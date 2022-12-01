import pydantic

from aiocycletls.enums.extension_type import ExtensionType


class Extension(pydantic.BaseModel):
    type: ExtensionType
    version: str

    def to_browser_string(self) -> str:
        return f"{self.type.value}/{self.version}"
