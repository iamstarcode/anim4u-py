import typer
from typing_extensions import Annotated
from foru_lib_py import cli
from typing_extensions import Annotated


app = typer.Typer()


@app.command()
def download(query: str):
    print(f"Creating user: {query}", cli.provider_seperated(query))


if __name__ == "__main__":
    app()
