from .base_provider import BaseProvider
from abc import ABC, abstractmethod

""" class IAnimeInfo:
    # Define the structure of anime information here

class ISource:
    # Define the structure of episode sources here

class IEpisodeServer:
    # Define the structure of episode servers here """


class AnimeProvider(BaseProvider):
    def __init__(self, name, baseURL) -> None:
        super().__init__(name, baseURL)

    """Abstract class for parsing anime information from various providers."""

    is_dub_available_separately: bool = False

    @abstractmethod
    async def fetch_anime_info(self, anime_id: str, *args: Any) -> IAnimeInfo:
        """Fetches anime information, including episodes."""

    @abstractmethod
    async def fetch_episode_sources(self, episode_id: str, *args: Any) -> ISource:
        """Fetches episode sources (video links)."""

    @abstractmethod
    async def fetch_episode_servers(self, episode_id: str) -> Iterable[IEpisodeServer]:
        """Fetches available episode servers (video links)."""
