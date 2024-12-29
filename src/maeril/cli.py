import logging
import typer
from rich.console import Console
from . import prompt


app = typer.Typer()
console = Console()


def init_logging(verbose: bool):
    log_level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(level=log_level, format='%(message)s')


@app.callback()
def callback(
        verbose: bool = typer.Option(False, "-v", "--verbose", help="Enable verbose logging")
    ):
    """Initialize logging based on verbosity."""
    init_logging(verbose)


@app.command()
def main():
    """Main command for maeril."""
    console.print("Replace this message by putting your code into maeril.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")


@app.command("prompt")
def prompt_cmd(input_path: str):
    """Process the input file using the prompt module."""
    prompt.main(input_path)


if __name__ == "__main__":
    app()
