
from typing import List, Optional

from embeddings.embedding_model import EmbeddingModel
from models.chunk import Chunk
from vectorstore.search import VectorSearch


class Retriever:

    def __init__(
        self,
        embedding_model: EmbeddingModel,
        vector_search: VectorSearch,
    ):
        self.embedding_model = embedding_model
        self.vector_search = vector_search

    def retrieve(
        self,
        question: Optional[str] = None,
        top_k: int = 5,
        query: Optional[str] = None,
    ) -> List[Chunk]:

        search_text = query if query is not None else question

        if not search_text or not search_text.strip():
            return []

        query_embedding = self.embedding_model.encode(search_text)

        chunks = self.vector_search.search(
            query_embedding,
            top_k,
        )

        return chunks
