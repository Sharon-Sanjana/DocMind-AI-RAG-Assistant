"""
TXT Loader

Loads plain text files and converts them into
Document objects.
"""

from pathlib import Path
from datetime import datetime

from ingestion.base_loader import BaseLoader
from models.document import Document
from utils.logger import get_logger
from utils.exceptions import (
    DocumentLoadError,
    UnsupportedFileTypeError,
)

logger = get_logger(__name__)


class TXTLoader(BaseLoader):
    """
    Loader responsible for reading TXT files.
    """

    def load(self, file_path: str) -> Document:
        """
        Load a TXT document.

        Args:
            file_path: Path to the text file.

        Returns:
            Document object.
        """

        path = Path(file_path)

        if path.suffix.lower() != ".txt":
            logger.error(
                "Unsupported file type: %s",
                file_path,
            )
            raise UnsupportedFileTypeError(
                "Only TXT files are supported."
            )

        if not path.exists():
            logger.error(
                "File not found: %s",
                file_path,
            )
            raise FileNotFoundError(
                f"File not found: {file_path}"
            )

        logger.info(
            "Loading TXT: %s",
            file_path,
        )

        try:
            text = path.read_text(
                encoding="utf-8"
            )

            document = Document(
                filename=path.name,
                extension=path.suffix,
                text=text,
                pages=1,
                size=path.stat().st_size,
                created_at=datetime.fromtimestamp(
                    path.stat().st_ctime
                ),
                modified_at=datetime.fromtimestamp(
                    path.stat().st_mtime
                ),
            )

            logger.info(
                "Successfully loaded TXT: %s",
                path.name,
            )

            return document

        except Exception as e:

            logger.exception(
                "Failed to load TXT: %s",
                file_path,
            )

            raise DocumentLoadError(
                str(e)
            ) from e