"""
Application Constants

Contains fixed values used throughout the application.
These values should not change during runtime.
"""


class AppConstants:
    """
    General application constants.
    """

    APP_NAME = "DocMind-AI"

    VERSION = "1.0.0"

    AUTHOR = "Sharon Sanjana S"

    LICENSE = "MIT"

    DEFAULT_ENCODING = "utf-8"


class FileConstants:
    """
    File related constants.
    """

    PDF = ".pdf"

    DOCX = ".docx"

    TXT = ".txt"

    MARKDOWN = ".md"

    SUPPORTED_FILE_TYPES = (
        PDF,
        DOCX,
        TXT,
        MARKDOWN,
    )


class StatusConstants:
    """
    Application status constants.
    """

    SUCCESS = "SUCCESS"

    FAILED = "FAILED"

    PROCESSING = "PROCESSING"

    COMPLETED = "COMPLETED"


class LogMessages:
    """
    Frequently used log messages.
    """

    FILE_LOADED = "File loaded successfully."

    FILE_SAVED = "File saved successfully."

    DOCUMENT_CHUNKED = "Document chunked successfully."

    EMBEDDINGS_CREATED = "Embeddings generated successfully."

    VECTOR_INDEX_CREATED = "Vector index created successfully."

    RETRIEVAL_COMPLETED = "Document retrieval completed."

    RESPONSE_GENERATED = "AI response generated successfully."


class DatabaseConstants:
    """
    Database table names.
    """

    DOCUMENTS = "documents"

    CHUNKS = "chunks"

    CHAT_HISTORY = "chat_history"


class MetadataKeys:
    """
    Metadata dictionary keys.
    """

    DOCUMENT_ID = "document_id"

    FILENAME = "filename"

    FILE_SIZE = "file_size"

    FILE_TYPE = "file_type"

    CREATED_AT = "created_at"

    MODIFIED_AT = "modified_at"

    PAGE = "page"

    CHUNK_ID = "chunk_id"

    SOURCE = "source"


class PromptTypes:
    """
    Prompt identifiers.
    """

    QA = "qa"

    SUMMARY = "summary"

    COMPARE = "compare"

    EXTRACT = "extract"