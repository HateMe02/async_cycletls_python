"""
TODO: add table-sizes and headers-order, maybe with filling
"""
import abc

from aiocycletls.models.browser.browser_data import BrowserData
from aiocycletls.models.browser.user_agent import UserAgent


class BrowserBase(abc.ABC):

    """
    Some base for impl for custom
    """

    def __init__(self, randomize_user_agents: bool = True) -> None:
        self.randomize_user_agents = randomize_user_agents
        self.cached_user_agent = None

    @abc.abstractmethod
    def generate_user_agent(self) -> UserAgent:
        """
        :return: random user agent or cache user_agent and repeat it
        """

    @abc.abstractmethod
    def define_ja3_for_version(self, user_agent: UserAgent) -> str:
        ...

    def get_parameters(self) -> BrowserData:
        user_agent = self.generate_user_agent()

        return BrowserData(
            user_agent=user_agent,
            ja3=self.define_ja3_for_version(user_agent)
        )
