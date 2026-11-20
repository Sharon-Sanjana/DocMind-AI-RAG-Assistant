"""
FAISS Index Manager

Handles saving and loading the
FAISS index and metadata.
"""

import os
import pickle
from typing import Any

import faiss


class IndexManager:
    """
    Saves and loads FAISS indexes.
    """

    def __init__(
        self,
        index_directory: str = "vector_index",
    ):
        self.index_directory = index_directory

        os.makedirs(
            self.index_directory,
            exist_ok=True,
        )

        self.index_file = os.path.join(
            self.index_directory,
            "faiss.index",
        )

        self.metadata_file = os.path.join(
            self.index_directory,
            "metadata.pkl",
        )

    def save_index(
        self,
        index: faiss.Index,
    ) -> None:
        """
        Save FAISS index.
        """

        faiss.write_index(
            index,
            self.index_file,
        )

    def load_index(
        self,
    ):
        """
        Load FAISS index.
        """

        if not os.path.exists(
            self.index_file
        ):
            return None

        return faiss.read_index(
            self.index_file
        )

    def save_metadata(
        self,
        metadata: Any,
    ) -> None:
        """
        Save metadata mapping.
        """

        with open(
            self.metadata_file,
            "wb",
        ) as file:

            pickle.dump(
                metadata,
                file,
            )

    def load_metadata(
        self,
    ):
        """
        Load metadata mapping.
        """

        if not os.path.exists(
            self.metadata_file
        ):
            return None

        with open(
            self.metadata_file,
            "rb",
        ) as file:

            return pickle.load(file)