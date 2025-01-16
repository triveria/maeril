"""Console script for foobar."""
import logging
import typer
from rich.console import Console
from rich.logging import RichHandler
from .foobar import main as foobar_main


logger = logging.getLogger(__name__)


app = typer.Typer()
console = Console()


def init_logging(verbose: bool):
    """
    Initialize logging with RichHandler for enhanced output.

    Args:
        verbose (bool): If True, set log level to DEBUG, else INFO.
    """
    # Remove all handlers associated with the root logger to prevent duplicate logs
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    # Configure RichHandler with conditional formatting based on the log level
    if verbose:
        log_level = logging.DEBUG
        # In DEBUG mode, show time, level, and path
        handler = RichHandler(rich_tracebacks=True, show_time=True, show_level=True, show_path=True)
    else:
        log_level = logging.INFO
        # In INFO mode, show only the message
        handler = RichHandler(rich_tracebacks=False, show_time=False, show_level=False, show_path=False)

    logging.basicConfig(level=log_level, format="%(message)s", handlers=[handler])


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
    foobar_main()


if __name__ == "__main__":
    app()
