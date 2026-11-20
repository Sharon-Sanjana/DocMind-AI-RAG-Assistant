"""
Document Cleaner

Provides utilities for cleaning document text
before chunking and embedding.
"""

import re

from models.document import Document


class DocumentCleaner:
    """
    Cleans document text.
    """

    @staticmethod
    def clean(document: Document) -> Document:
        """
        Clean document text.

        Args:
            document: Input document.

        Returns:
            Cleaned document.
        """

        text = document.text

        # Remove Windows line endings
        text = text.replace("\r", "")

        # Replace tabs with spaces
        text = text.replace("\t", " ")

        # Remove multiple spaces
        text = re.sub(r"[ ]{2,}", " ", text)

        # Remove multiple blank lines
        text = re.sub(r"\n{2,}", "\n\n", text)

        # Remove non-printable characters
        text = re.sub(
            r"[^\x20-\x7E\n]",
            "",
            text,
        )

        # Remove leading/trailing spaces
        text = text.strip()

        document.text = text

        return document