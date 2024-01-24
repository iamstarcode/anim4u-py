from typing import Any
from pydantic import BaseModel

from consumet_py.providers import BaseProvider as Provider


class Options(BaseModel):
    query: str
    quality: int
    force: bool


class BaseProvider:
    def __init__(self, options: Options, provider: Provider) -> None:
        self.options = options
        self.provider = provider

        self.searchPath = "anim4u/" + provider.name.lower()
        # print(self.searchPath)

    def run(self):
        # implent getting media.
        print("Searching media")

    """def __init__(self, options):
    super().__init__(options)"""
