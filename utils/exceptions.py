"""
Custom Exceptions

Defines application-specific exceptions.
"""


class DocMindError(Exception):
    """
    Base exception for the application.
    """
    pass


class InvalidDocumentError(DocMindError):
    """
    Raised when a document is invalid.
    """
    pass


class EmptyDocumentError(DocMindError):
    """
    Raised when extracted text is empty.
    """
    pass


class UnsupportedFileTypeError(DocMindError):
    """
    Raised when an unsupported file is uploaded.
    """
    pass


class DocumentLoadError(DocMindError):
    """
    Raised when a document cannot be loaded.
    """
    pass
class ValidationError(Exception):
    """
    Raised when document validation fails.
    """

    pass