import random

from aiocycletls.browsers.browser_base import BrowserBase
from aiocycletls.enums.browser_type import BrowserType
from aiocycletls.enums.extension_type import ExtensionType
from aiocycletls.enums.platform_type import PlatformType
from aiocycletls.enums.system_platform import SystemPlatform, SYSTEM_PLATFORM_DETAILS
from aiocycletls.models.browser.extension import Extension
from aiocycletls.models.browser.platform_information import PlatformInformation
from aiocycletls.models.browser.system_information import SystemInformation
from aiocycletls.models.browser.user_agent import UserAgent

SAFARI_EXTENSION = Extension(type=ExtensionType.SAFARI, version="537.36")
EXTENSIONS = [
    [Extension(type=ExtensionType.CHROME, version="107.0.0.0"), SAFARI_EXTENSION],
    [Extension(type=ExtensionType.CHROME, version="104.0.0.0"), SAFARI_EXTENSION],
    [Extension(type=ExtensionType.CHROME, version="103.0.0.0"), SAFARI_EXTENSION],
    [Extension(type=ExtensionType.CHROME, version="99.0.4844.84"), SAFARI_EXTENSION],
    [Extension(type=ExtensionType.CHROME, version="96.0.4664.110"), SAFARI_EXTENSION]
]


class Chrome(BrowserBase):
    def generate_user_agent(self) -> UserAgent:
        if not self.randomize_user_agents and self.cached_user_agent:
            return self.cached_user_agent

        extensions = random.choice(EXTENSIONS)
        platform_information = PlatformInformation(
            type=PlatformType.WEBKIT,
            version=extensions[1].version
        )  # webkit version == safari version
        os = random.choice(list(SystemPlatform))

        user_agent = UserAgent(
            browser_type=BrowserType.CHROME,
            system_information=SystemInformation(
                type=os,
                details=random.choice(SYSTEM_PLATFORM_DETAILS[os])
            ),
            extensions=extensions,
            platform=platform_information
        )

        if not self.randomize_user_agents:
            self.cached_user_agent = user_agent

        return user_agent

    def define_ja3_for_version(self, user_agent: UserAgent) -> str:
        match user_agent.extensions[0].version:
            case "107.0.0.0":
                return "772,4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53,0-23-65281-10-11-35-16-5-13-18-51-45-43-27-17513-41,2570-29-23-24,0"
            case "104.0.0.0":
                return "772,4867-4865-4866-52393-52392-49195-49199-49196-49200-49171-49172-156-157-47-53,0-23-65281-10-11-35-16-5-13-18-51-45-43-27-17513-41,29-23-24,0"
            case "103.0.0.0":
                return "772,4867-4865-4866-52393-52392-49195-49199-49196-49200-49171-49172-156-157-47-53,0-23-65281-10-11-35-16-5-13-18-51-45-43-27-17513-41,29-23-24,0"
            case "99.0.4844.84":
                return "772,4867-4865-4866-52393-52392-49195-49199-49196-49200-49171-49172-156-157-47-53,0-23-65281-10-11-35-16-5-13-18-51-45-43-27-17513,29-23-24,0"
            case "96.0.4664.110":
                return "772,4867-4865-4866-52393-52392-49195-49199-49196-49200-49171-49172-156-157-47-53,0-23-65281-10-11-35-16-5-13-18-51-45-43-27-17513,2570-29-23-24,0"
