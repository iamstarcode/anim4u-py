from ..anime_provider import AnimeProvider


class AnimepaheProvier(AnimeProvider):
    def __init__(self, name, baseURL) -> None:
        super().__init__(name, baseURL)
