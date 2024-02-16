from typing import Any, Iterable
from .base_provider import BaseProvider
from abc import ABC, abstractmethod

from ..models.anime import AnimeInfo, EpisodeServer
from ..models import Source


class AnimeProvider(BaseProvider):
    def __init__(self, name, base_url) -> None:
        super().__init__(name, base_url)

    """Abstract class for parsing anime information from various providers."""

    is_dub_available_separately: bool = False

    @abstractmethod
    async def fetch_anime_info(self, anime_id: str, *args: Any) -> AnimeInfo:
        """Fetches anime information, including episodes."""

    @abstractmethod
    async def fetch_episode_sources(self, episode_id: str, *args: Any) -> Source:
        """Fetches episode sources (video links)."""

    @abstractmethod
    async def fetch_episode_servers(self, episode_id: str) -> Iterable[EpisodeServer]:
        """Fetches available episode servers (video links)."""
