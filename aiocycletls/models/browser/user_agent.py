import pydantic

from aiocycletls.enums.browser_type import BrowserType
from aiocycletls.models.browser.extension import Extension
from aiocycletls.models.browser.platform_information import PlatformInformation
from aiocycletls.models.browser.system_information import SystemInformation

DEFAULT_FORMAT = "Mozilla/5.0 ({system_information}) {platform} ({platform_details}) {extensions}"


class UserAgent(pydantic.BaseModel):
    browser_type: BrowserType
    system_information: SystemInformation
    platform_details: str = "KHTML, like Gecko"
    extensions: list[Extension]
    platform: PlatformInformation
    string_format: str = DEFAULT_FORMAT

    def to_browser_string(self) -> str:
        return self.string_format.format(
            system_information=self.system_information.to_browser_string(),
            platform_details=self.platform_details,
            platform=self.platform.to_browser_string(),
            extensions=" ".join([
                extension.to_browser_string()
                for extension in self.extensions
            ])
        )
