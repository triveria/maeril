import logging
import typer
from rich.console import Console
from rich.logging import RichHandler
from . import prompt


app = typer.Typer()
console = Console()


def init_logging(verbose: bool):
    """
    Initialize logging with RichHandler for enhanced output.
    
    Args:
        verbose (bool): If True, set log level to DEBUG, else INFO.
    """
    log_level = logging.DEBUG if verbose else logging.INFO

    # Remove all handlers associated with the root logger.
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)
    
    # Configure logging with RichHandler
    logging.basicConfig(
        level=log_level,
        format="%(message)s",
        datefmt="[%X]",
        handlers=[RichHandler(rich_tracebacks=True)]
    )

logger = logging.getLogger("rich")

@app.callback()
def callback(
        verbose: bool = typer.Option(False, "-v", "--verbose", help="Enable verbose (DEBUG) logging")
    ):
    """Initialize logging based on verbosity."""
    init_logging(verbose)
    logger.debug("Logging initialized. Verbose mode is enabled.")

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
