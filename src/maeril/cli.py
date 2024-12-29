import typer
from rich.console import Console
from . import prompt


app = typer.Typer()
console = Console()


@app.command("prompt")
def prompt_cmd(input_path: str):
    """Process the input file using the prompt module."""
    prompt.main(input_path)

if __name__ == "__main__":
    app()
