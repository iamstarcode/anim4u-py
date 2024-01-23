from typing import List
from typing import Any, Iterable
from ..providers.base_provider import SearchResult


from ..providers.anime_provider import (
    AnimeProvider,
    ISource,
    IAnimeInfo,
    IEpisodeServer,
)


class AnimepaheProvier(AnimeProvider):
    def __init__(self) -> None:
        super().__init__("Animepahe", baseURL="htpp.com")

    async def search(self, query: str) -> List[SearchResult]:
        print("searching")

    async def fetch_anime_info(self, anime_id: str, *args: Any) -> IAnimeInfo:
        """Fetches anime information, including episodes."""

    async def fetch_episode_sources(self, episode_id: str, *args: Any) -> ISource:
        """Fetches episode sources (video links)."""

    async def fetch_episode_servers(self, episode_id: str) -> Iterable[IEpisodeServer]:
        """Fetches available episode servers (video links)."""
