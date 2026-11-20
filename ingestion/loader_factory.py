"""
Loader Factory

Creates the appropriate document loader
based on the uploaded file type.
"""

from pathlib import Path

from ingestion.pdf_loader import PDFLoader
from ingestion.docx_loader import DOCXLoader
from ingestion.txt_loader import TXTLoader
from ingestion.markdown_loader import MarkdownLoader

from utils.exceptions import UnsupportedFileTypeError


class LoaderFactory:
    """
    Factory responsible for creating
    document loaders.
    """

    _loaders = {
        ".pdf": PDFLoader,
        ".docx": DOCXLoader,
        ".txt": TXTLoader,
        ".md": MarkdownLoader,
    }

    @classmethod
    def get_loader(cls, file_path: str):
        """
        Return the appropriate loader for
        the given file.
        """

        extension = Path(file_path).suffix.lower()

        loader_class = cls._loaders.get(extension)

        if loader_class is None:
            raise UnsupportedFileTypeError(
                f"No loader available for '{extension}' files."
            )

        return loader_class()