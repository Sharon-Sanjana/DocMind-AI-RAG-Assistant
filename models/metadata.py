"""
Metadata Model

Stores metadata associated with a document.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import List


@dataclass
class Metadata:
    """
    Represents metadata for a document.
    """

    filename: str

    extension: str

    size: int

    pages: int

    author: str = "Unknown"

    language: str = "English"

    encoding: str = "utf-8"

    tags: List[str] = field(default_factory=list)

    created_at: datetime = field(default_factory=datetime.now)

    modified_at: datetime = field(default_factory=datetime.now)

    def add_tag(self, tag: str):
        """
        Add a tag if it does not already exist.
        """
        tag = tag.strip()

        if tag and tag not in self.tags:
            self.tags.append(tag)

    def remove_tag(self, tag: str):
        """
        Remove a tag.
        """
        if tag in self.tags:
            self.tags.remove(tag)

    def to_dict(self):
        """
        Convert metadata into dictionary.
        """
        return {
            "filename": self.filename,
            "extension": self.extension,
            "size": self.size,
            "pages": self.pages,
            "author": self.author,
            "language": self.language,
            "encoding": self.encoding,
            "tags": self.tags,
            "created_at": self.created_at.isoformat(),
            "modified_at": self.modified_at.isoformat(),
        }

    def __str__(self):
        return (
            f"Metadata("
            f"filename={self.filename}, "
            f"pages={self.pages}, "
            f"language={self.language})"
        )