"""
Metadata Extractor

Extracts metadata from files and creates
Metadata objects.
"""

from pathlib import Path
from datetime import datetime

from models.metadata import Metadata


class MetadataExtractor:
    """
    Extract metadata from files.
    """

    @staticmethod
    def extract(
        file_path: str,
        pages: int = 1,
        author: str = "Unknown",
        language: str = "English",
    ) -> Metadata:
        """
        Extract metadata from a file.

        Args:
            file_path: Path to the document.
            pages: Number of pages.
            author: Document author.
            language: Document language.

        Returns:
            Metadata object.
        """

        path = Path(file_path)

        stat = path.stat()

        return Metadata(
            filename=path.name,
            extension=path.suffix.lower(),
            size=stat.st_size,
            pages=pages,
            author=author,
            language=language,
            created_at=datetime.fromtimestamp(
                stat.st_ctime
            ),
            modified_at=datetime.fromtimestamp(
                stat.st_mtime
            ),
        )