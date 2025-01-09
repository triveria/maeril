import logging
import shutil
from pathlib import Path

logger = logging.getLogger(__name__)

def main(file_name: str = None):
    dump_dir = Path(__file__).parent / "dump_files"

    if file_name is None:
        items = [str(p.relative_to(dump_dir)) for p in dump_dir.rglob('*')]
        logger.info("No file specified. Available files and directories:")
        logger.info("---------------------------------------------------")
        for item in items:
            logger.info(item)
        return

    source = dump_dir / file_name
    destination = Path.cwd() / file_name

    if destination.exists():
        raise FileExistsError(f"Destination '{destination}' already exists.")

    if source.is_dir():
        shutil.copytree(source, destination)
    else:
        shutil.copy(source, destination)

    logger.info(f"Copied '{file_name}' to '{destination}'")
