"""
Message Model

Represents a single chat message exchanged
between the user and the AI assistant.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, Any, List
import uuid


@dataclass
class Message:
    """
    Represents one message in a chat session.
    """

    # --------------------------------------------------
    # Identification
    # --------------------------------------------------

    message_id: str = field(
        default_factory=lambda: str(uuid.uuid4())
    )

    session_id: str = ""

    # --------------------------------------------------
    # Message Details
    # --------------------------------------------------

    role: str = "user"

    content: str = ""

    # --------------------------------------------------
    # Retrieval Information
    # --------------------------------------------------

    retrieved_chunks: List[str] = field(
        default_factory=list
    )

    # --------------------------------------------------
    # Additional Metadata
    # --------------------------------------------------

    metadata: Dict[str, Any] = field(
        default_factory=dict
    )

    # --------------------------------------------------
    # Timestamp
    # --------------------------------------------------

    created_at: datetime = field(
        default_factory=datetime.now
    )

    def __post_init__(self):
        """
        Validate the message after initialization.
        """

        self.content = self.content.strip()

        allowed_roles = {
            "user",
            "assistant",
            "system",
        }

        if self.role not in allowed_roles:
            raise ValueError(
                f"Invalid role: {self.role}"
            )

        if not self.content:
            raise ValueError(
                "Message content cannot be empty."
            )

    @property
    def word_count(self) -> int:
        """
        Returns the number of words
        in the message.
        """
        return len(self.content.split())

    def to_dict(self) -> dict:
        """
        Convert the message into a dictionary.
        """

        return {
            "message_id": self.message_id,
            "session_id": self.session_id,
            "role": self.role,
            "content": self.content,
            "retrieved_chunks": self.retrieved_chunks,
            "metadata": self.metadata,
            "created_at": self.created_at.isoformat(),
        }

    def __str__(self):
        return (
            f"Message("
            f"role={self.role}, "
            f"words={self.word_count})"
        )