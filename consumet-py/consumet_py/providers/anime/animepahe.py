from typing import List
from typing import Any, Iterable

from ...models.anime import EpisodeServer, AnimeResult, AnimeInfo

from ...models import Search, Source

from ...providers.anime_provider import AnimeProvider


class AnimepaheProvier(AnimeProvider):
    def __init__(self) -> None:
        super().__init__("Animepahe", baseURL="htpp.com")

    async def search(self, query: str) -> Search[AnimeResult]:
        print("searching")

    async def fetch_anime_info(self, anime_id: str, *args: Any) -> AnimeInfo:
        """Fetches anime information, including episodes."""

    async def fetch_episode_sources(self, episode_id: str, *args: Any) -> Source:
        """Fetches episode sources (video links)."""

    async def fetch_episode_servers(self, episode_id: str) -> Iterable[EpisodeServer]:
        """Fetches available episode servers (video links)."""
