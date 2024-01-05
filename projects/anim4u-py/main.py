import typer
from typing_extensions import Annotated


# from commands import download

app = typer.Typer()

## app.add_typer(download.app, name="download")


@app.command()
def download(query: str):
    print(f"Creating user: {query}")


if __name__ == "__main__":
    app()
