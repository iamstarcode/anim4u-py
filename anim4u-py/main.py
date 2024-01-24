import typer
from typing_extensions import Annotated
from foru_lib_py import cli
from typing_extensions import Annotated

from consumet_py import Anime

app = typer.Typer()


@app.command()
def download(
    query: str,
    q: Annotated[int, typer.Option()] = None,
    d: Annotated[bool, typer.Option()] = False,
    f: Annotated[bool, typer.Option()] = False,
):
    [provider, que] = cli.provider_seperated(query)
    ### animepahe_provider = Anime.AnimeProvider()
    print(Anime.AnimepaheProvier())
    options = {"provider": provider, "query": que, "quality": q, "force": f}
    if d:
        print(f"Options: {options}")

    if provider == "animepahe":
        print("Animepahe", options["quality"])


@app.command()
def clear(username: str):
    print(f"Deleting user: {username}")


if __name__ == "__main__":
    app()
