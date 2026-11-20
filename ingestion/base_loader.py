"""
Abstract Base Loader

Defines the interface that all document loaders
must implement.
"""

from abc import ABC, abstractmethod
from models.document import Document


class BaseLoader(ABC):
    """
    Abstract base class for all document loaders.
    """

    @abstractmethod
    def load(self, file_path: str) -> Document:
        """
        Load a document and return a Document object.

        Args:
            file_path (str):
                Path to the input document.

        Returns:
            Document:
                Parsed document object.
        """
        pass