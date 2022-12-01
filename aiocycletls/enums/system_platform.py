import enum


class SystemPlatform(enum.Enum):
    WINDOWS_10 = "Windows NT 10.0"


SYSTEM_PLATFORM_DETAILS = {
    SystemPlatform.WINDOWS_10: [
        ["Win64", "x64"],
        ["WOW64"],
        []
    ]
}
