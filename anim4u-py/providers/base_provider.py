import time
from typing import Any
from pydantic import BaseModel

from consumet_py.providers import BaseProvider as Provider

from rich.progress import Progress, SpinnerColumn, TextColumn

from rich import print


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
        anime = self.get_anime()
        # print("Searching media from base")

    def get_anime(self):
        if self.options["force"] is True:
            return self.fetch_anime()
            pass
        pass

    def fetch_anime(self):
        provider_color = ""
        if self.provider.name == "Animepahe":
            provider_color = f"[deep_pink1]Animepahe[/deep_pink1]"

        # print(f'Searching {self.options["query"]} from {provider_color}')
        description = (
            f'Searching [yellow]{self.options["query"]}[/yellow] from {provider_color}'
        )

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}", markup=True),
            transient=True,
        ) as progress:
            progress.add_task(description, total=None)
            # todo implement search with consumet
            time.sleep(5)
        pass
