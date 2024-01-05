import typer

from rich.progress import Progress, SpinnerColumn, TextColumn

from typing_extensions import Annotated


app = typer.Typer()


@app.command()
def main(query: Annotated[str, typer.Argument()]):
    print(f"Hello {query}")


if __name__ == "__main__":
    app()
