"""
Document Processing Service

Coordinates the complete
document processing pipeline.
"""
import time
from models.document import Document

from ingestion.loader_factory import LoaderFactory
from preprocessing.cleaner import DocumentCleaner
from chunking.chunker import DocumentChunker
from embeddings.embedder import Embedder
from vectorstore.faiss_store import FAISSStore
from vectorstore.search import VectorSearch


class DocumentProcessingService:
    """
    Processes uploaded documents
    from ingestion to indexing.
    """

    def __init__(
        self,
        chunker: DocumentChunker,
        embedder: Embedder,
        faiss_store: FAISSStore,
        vector_search: VectorSearch,
    ):  
        
        self.chunker = chunker
        self.embedder = embedder
        self.faiss_store = faiss_store
        self.vector_search = vector_search

    def process(
        self,
        file_path: str,
    ) -> dict:
        """
        Process a document and
        index it for retrieval.
        """
        start_time = time.perf_counter()
        # -----------------------------------------
        # Load document
        # -----------------------------------------

        loader = LoaderFactory.get_loader(
            file_path
        )

        document = loader.load(
            file_path
        )

        # -----------------------------------------
        # Clean document
        # -----------------------------------------

        document = DocumentCleaner.clean(
            document
        )

        # -----------------------------------------
        # Chunk document
        # -----------------------------------------

        chunks = self.chunker.chunk(
            document
        )

        # -----------------------------------------
        # Generate embeddings
        # -----------------------------------------

        chunks = self.embedder.embed_chunks(
            chunks
        )

        # -----------------------------------------
        # Extract embeddings
        # -----------------------------------------

        embeddings = [
            chunk.embedding
            for chunk in chunks
        ]

        # -----------------------------------------
        # Store vectors
        # -----------------------------------------

        self.faiss_store.add(
            embeddings
        )

        # -----------------------------------------
        # Store chunk mapping
        # -----------------------------------------

        self.vector_search.metadata.extend(
            chunks
        )
        print("DEBUG - Indexed chunks:", len(chunks))
        print("DEBUG - FAISS total vectors:", self.faiss_store.size())
        print("DEBUG - Metadata total:", len(self.vector_search.metadata))
        processing_time = round(
    time.perf_counter() - start_time,
    2,
)
        # -----------------------------------------
        # Return processing statistics
        # -----------------------------------------
        return {
    "document_name": document.filename,
    "document_id": document.document_id,
    "file_size": document.size,
    "pages": document.pages,
    "chunks": len(chunks),
    "vector_count": len(embeddings),
    "embedding_model": self.embedder.embedding_model.model_name,
    "processing_time": processing_time,
    "status": "success",
}


        