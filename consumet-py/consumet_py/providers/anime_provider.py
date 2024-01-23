from typing import Any, Iterable
from .base_provider import BaseProvider
from abc import ABC, abstractmethod


class IAnimeInfo:
    pass


class ISource:
    pass


class IEpisodeServer:
    pass


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
