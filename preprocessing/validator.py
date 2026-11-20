"""
Document Validator

Validates documents before preprocessing
and embedding.
"""

from models.document import Document
from config.settings import settings
from utils.exceptions import ValidationError


class DocumentValidator:
    """
    Validates uploaded documents.
    """

    @staticmethod
    def validate(document: Document) -> None:
        """
        Validate a document.

        Raises:
            ValidationError
        """

        if document is None:
            raise ValidationError(
                "Document cannot be None."
            )

        if not document.text:
            raise ValidationError(
                "Document contains no text."
            )

        if len(document.text.strip()) == 0:
            raise ValidationError(
                "Document is empty."
            )

        if len(document.text) < settings.MIN_DOCUMENT_LENGTH:
            raise ValidationError(
                "Document is too short."
            )

        if document.extension.lower() not in settings.SUPPORTED_EXTENSIONS:
            raise ValidationError(
                f"Unsupported extension: {document.extension}"
            )

        if document.size > settings.MAX_FILE_SIZE:
            raise ValidationError(
                "Document exceeds maximum file size."
            )