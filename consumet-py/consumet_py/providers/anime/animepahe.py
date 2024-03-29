from typing import List
from typing import Any, Iterable
import requests


from ...models.anime import EpisodeServer, AnimeResult, AnimeInfo

from ...models import Search, Source

from ...providers.anime_provider import AnimeProvider

import httpx


class AnimepaheProvier(AnimeProvider):
    def __init__(self) -> None:
        super().__init__("Animepahe", base_url="https://animepahe.ru")

    async def search(self, query: str) -> Search[AnimeResult]:
        try:
            HEADERS = {
                "User-Agent": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"
            }

            async with httpx.AsyncClient() as client:
                response = await client.get(
                    f"{self.base_url}/api?m=search&q={query}",
                    follow_redirects=True,
                    headers=HEADERS,
                )
                # response.raise_for_status()  # Raise an error for bad responses (non-2xx)
                print(response.json())
                data = await response.json()

                """ results = {
                    "results": [
                        {
                            "id": f"{item['id']}/{item['session']}",
                            "title": item["title"],
                            "image": item["poster"],
                            "rating": item["score"],
                            "releaseDate": item["year"],
                            "type": item["type"],
                        }
                        for item in data["data"]
                    ]
                }

                return results """

        except httpx.RequestError as err:
            raise ValueError(str(err))

    async def fetch_anime_info(self, anime_id: str, *args: Any) -> AnimeInfo:
        """Fetches anime information, including episodes."""

    async def fetch_episode_sources(self, episode_id: str, *args: Any) -> Source:
        """Fetches episode sources (video links)."""

    async def fetch_episode_servers(self, episode_id: str) -> Iterable[EpisodeServer]:
        """Fetches available episode servers (video links)."""
