"""
Document Data Model

This module defines the Document class used throughout the
DocMind AI application.

Author: Sharon Sanjana
Project: DocMind AI
"""
from dataclasses import dataclass, field
import uuid
from datetime import datetime


@dataclass
class Document:
    """
    Represents a document uploaded by the user.

    Every supported file type (PDF, DOCX, TXT, Markdown)
    is converted into this common format.
    """
    filename: str
    extension: str
    text: str
    pages: int
    size: int
    created_at: datetime
    modified_at: datetime
    document_id: str = field(default_factory=lambda: str(uuid.uuid4()))