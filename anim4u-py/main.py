import typer
from typing_extensions import Annotated
from foru_lib_py import cli
from typing_extensions import Annotated

from asyncio import run as aiorun

from providers.animepahe_provider import AnimepaheProvider
from providers.base_provider import Options

from functools import wraps
import anyio

from consumet_py import Anime

app = typer.Typer()


def run_async(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        async def coro_wrapper():
            return await func(*args, **kwargs)

        return anyio.run(coro_wrapper)

    return wrapper


@app.command()
@run_async
async def download(
    query: str,
    q: Annotated[int, typer.Option()] = None,
    d: Annotated[bool, typer.Option()] = False,
    f: Annotated[bool, typer.Option()] = False,
):
    [provider, que] = cli.provider_seperated(query)

    options = {"provider": provider, "query": que, "quality": q, "force": f}
    if d:
        print(f"Options: {options}")

    if provider == "animepahe":
        provider = AnimepaheProvider(options=options, provider=Anime.AnimepaheProvier())
        await provider.run()

    elif provider == "gogoanime":
        # provider = AnimepaheProvider(options=options, provider=Anime.AnimepaheProvier())
        pass


@app.command()
def clear(username: str):
    print(f"Deleting user: {username}")


if __name__ == "__main__":
    app()
