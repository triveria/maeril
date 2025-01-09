import logging
import shutil
from pathlib import Path


logger = logging.getLogger(__name__)


def list_dump_files():
    dump_files_dir = Path(__file__).parent / 'dump_files'
    items = [str(p.relative_to(dump_files_dir)) for p in dump_files_dir.rglob('*')]
    return items


def main(file_name: str = None):
    dump_files_dir = Path(__file__).parent / "dump_files"

    if file_name is None:
        logger.info("No file specified. Available files and directories:")
        logger.info("---------------------------------------------------")
        available_files = list_dump_files()
        for available_file in available_files:
            logger.info(available_file)
        return

    source = dump_files_dir / file_name
    destination = Path.cwd() / file_name

    if destination.exists():
        raise FileExistsError(f"Destination '{destination}' already exists.")

    if source.is_dir():
        shutil.copytree(source, destination)
    else:
        shutil.copy(source, destination)

    logger.info(f"Copied '{file_name}' to '{destination}'")
