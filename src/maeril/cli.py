import logging
import typer
from rich.console import Console
from rich.logging import RichHandler
from . import prompt
from . import dump


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


@app.command("prompt")
def prompt_cmd(input_path: str = typer.Argument("./prompt.md", help="Path to the input file. Defaults to './prompt.md' if not provided.")):
    """Process the input file using the prompt module."""
    prompt.main(input_path)


@app.command("dump")
def dump_cmd(
    file_name: str = typer.Argument(
        None, help="Name of the file or folder to dump", autocompletion=dump.list_dump_files
    )
):
    """Dump files from dump_files directory."""
    dump.main(file_name)


if __name__ == "__main__":
    app()
