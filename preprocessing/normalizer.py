"""
Document Normalizer

Normalizes document text before chunking
and embedding.
"""

import re
import unicodedata

from models.document import Document


class DocumentNormalizer:
    """
    Normalizes document text.
    """

    @staticmethod
    def normalize(document: Document) -> Document:
        """
        Normalize document text.

        Args:
            document: Input document.

        Returns:
            Normalized document.
        """

        text = document.text

        # Unicode normalization
        text = unicodedata.normalize(
            "NFKC",
            text,
        )

        # Normalize quotation marks
        text = # Normalize quotation marks
        text = (
            text.replace("“", '"')
                .replace("”", '"')
                .replace("‘", "'")
                .replace("’", "'")
        )

        # Normalize dashes
        text = (
            text.replace("–", "-")
                .replace("—", "-")
        )

        # Collapse multiple spaces
        text = re.sub(
            r"\s+",
            " ",
            text,
        )

        # Remove surrounding whitespace
        text = text.strip()

        document.text = text

        return document