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

    # Remove all handlers associated with the root logger to prevent duplicate logs
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)
    
    # Configure RichHandler with conditional formatting based on the log level
    if verbose:
        # In DEBUG mode, show time, level, and path
        handler = RichHandler(
            rich_tracebacks=True,
            show_time=True,
            show_level=True,
            show_path=True
        )
    else:
        # In INFO mode, show only the message
        handler = RichHandler(
            rich_tracebacks=False,
            show_time=False,
            show_level=False,
            show_path=False
        )
    
    logging.basicConfig(
        level=log_level,
        format="%(message)s",  # Simplified format; RichHandler will handle the rest
        handlers=[handler]
    )

logger = logging.getLogger(__name__)

@app.callback()
def callback(
        verbose: bool = typer.Option(
            False, "-v", "--verbose", help="Enable verbose (DEBUG) logging"
        )
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
