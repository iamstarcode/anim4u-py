from abc import ABC, abstractmethod
from typing import List


class SearchResult:
    id: str
    """The unique identifier of the search result."""

    title: str
    """The title of the anime or movie."""

    type: str  # "anime" or "movie"
    """The type of the search result."""

    def __init__(self, id: str, title: str, type: str):
        self.id = id
        self.title = title
        self.type = type


class BaseProvider(ABC):
    name: str
    baseURL: str
    # is_nfsw

    def __init__(self, name, baseURL) -> None:
        self.name = name
        self.baseURL = baseURL

    @abstractmethod
    async def search(self, query: str) -> List[SearchResult]:
        """
        Searches for anime or movies based on the given query.

        Args:
            query: The search query.

        Returns:
            A list of SearchResult objects.
        """
