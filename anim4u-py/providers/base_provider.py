from typing import Any
from pydantic import BaseModel

from consumet_py.providers.base_provider import BaseProvider


class Options(BaseModel):
    query: str
    quality: int
    force: bool


class BaseProvider:
    def __init__(self, options: Options, provider: BaseProvider) -> None:
        self.options = options
        self.provider = provider

        # self.searchPath = search_path

    def run(self):
        # implent getting media.
        print("Searching media")

    """def __init__(self, options):
    super().__init__(options)"""
