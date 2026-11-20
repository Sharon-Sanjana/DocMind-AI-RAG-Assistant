"""
Chunk Model

Represents a chunk generated from a document.
Each chunk is stored independently in the vector database.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, Dict, Any, List
import uuid


@dataclass
class Chunk:
    """
    Represents a document chunk used for retrieval.
    """

    # -----------------------------------------------------
    # Identification
    # -----------------------------------------------------

    chunk_id: str = field(
        default_factory=lambda: str(uuid.uuid4())
    )

    document_id: str = ""

    chunk_index: int = 0

    # -----------------------------------------------------
    # Content
    # -----------------------------------------------------

    text: str = ""

    # -----------------------------------------------------
    # Embedding Vector
    # -----------------------------------------------------

    embedding: Optional[List[float]] = None

    # -----------------------------------------------------
    # Metadata
    # -----------------------------------------------------

    metadata: Dict[str, Any] = field(default_factory=dict)

    # -----------------------------------------------------
    # Timestamp
    # -----------------------------------------------------

    created_at: datetime = field(
        default_factory=datetime.now
    )

    def __post_init__(self):
        """
        Validate chunk after initialization.
        """

        self.text = self.text.strip()

        if not self.text:
            raise ValueError(
                "Chunk text cannot be empty."
            )

    @property
    def length(self) -> int:
        """
        Returns the number of characters
        in the chunk.
        """
        return len(self.text)

    def to_dict(self) -> dict:
        """
        Convert Chunk object to dictionary.
        """

        return {
            "chunk_id": self.chunk_id,
            "document_id": self.document_id,
            "chunk_index": self.chunk_index,
            "text": self.text,
            "embedding": self.embedding,
            "metadata": self.metadata,
            "created_at": self.created_at.isoformat(),
        }

    def __str__(self) -> str:
        """
        Human-readable representation.
        """

        return (
            f"Chunk("
            f"chunk_id={self.chunk_id}, "
            f"document_id={self.document_id}, "
            f"chunk_index={self.chunk_index}, "
            f"length={self.length})"
        )