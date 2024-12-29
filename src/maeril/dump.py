import logging
import shutil
from pathlib import Path

logger = logging.getLogger(__name__)

def main(file_name: str = None, list: bool = False):
    dump_dir = Path(__file__).parent / "dump_files"

    if list:
        files = [f.name for f in dump_dir.iterdir() if f.is_file()]
        logger.info("Available files:")
        for f in files:
            logger.info(f)
    else:
        source = dump_dir / file_name
        destination = Path.cwd() / file_name
        shutil.copy(source, destination)
        logger.info(f"Copied {file_name} to {Path.cwd()}")
