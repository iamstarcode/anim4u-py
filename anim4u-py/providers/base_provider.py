from typing import Any
from pydantic import BaseModel

from consumet_py.providers import BaseProvider as Provider

from rich.progress import Progress, SpinnerColumn, TextColumn


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
        print("Searching media from base")

    def get_anime(self):
        if self.options.force is True:
            return self.fetch_anime()
            pass
        pass

    def fetch_anime(self):
        pass
