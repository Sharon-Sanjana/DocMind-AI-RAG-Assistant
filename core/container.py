"""
Application Container

Centralizes dependency creation
for the DocMind-AI application.
"""

from config.settings import settings

from embeddings.embedding_model import EmbeddingModel
from embeddings.embedder import Embedder

from chunking.strategies import FixedSizeChunkStrategy
from chunking.chunker import DocumentChunker

from vectorstore.faiss_store import FAISSStore
from vectorstore.search import VectorSearch

from retrieval.retriever import Retriever

from llm.ollama_client import OllamaClient
from llm.generator import ResponseGenerator
from llm.response_parser import ResponseParser

from services.document_processing_service import (
    DocumentProcessingService,
)

from services.qa_service import QAService
from services.summary_service import SummaryService
from services.keyword_service import KeywordService
from services.insight_service import InsightService
from services.compare_service import CompareService


class ApplicationContainer:
    """
    Dependency Injection Container.
    """

    def __init__(self):

    # Shared metadata
        self.metadata = []

    # Embeddings
        self.embedding_model = self._create_embedding_model()

        self.embedder = self._create_embedder()

    # Vector Store
        self.faiss_store = self._create_faiss_store()

        self.vector_search = self._create_vector_search()

    # Retrieval
        self.retriever = self._create_retriever()

    # LLM
        self.client = self._create_llm_client()

        self.generator = self._create_generator()

        self.parser = self._create_parser()

    # Chunking
        self.chunk_strategy = self._create_chunk_strategy()

        self.chunker = self._create_chunker()

    # Processing
        self.document_processing_service = (
             self._create_document_processing_service()
        )

    # Services
        self.qa_service = self._create_qa_service()

        self.summary_service = self._create_summary_service()

        self.keyword_service = self._create_keyword_service()

        self.insight_service = self._create_insight_service()

        self.compare_service = self._create_compare_service()


    # ---------------------------------------------------------
# Embeddings
# ---------------------------------------------------------

    def _create_embedding_model(self):

        return EmbeddingModel(
        model_name=settings.EMBEDDING_MODEL,
    )


    def _create_embedder(self):

        return Embedder(
        self.embedding_model,
    )

    # ---------------------------------------------------------
# Vector Store
# ---------------------------------------------------------

    def _create_faiss_store(self):

        return FAISSStore(
        dimension=settings.FAISS_DIMENSION,
    )


    def _create_vector_search(self):

        return VectorSearch(
        self.faiss_store,
        self.metadata,
    )

    # ---------------------------------------------------------
# Chunking
# ---------------------------------------------------------

    def _create_chunk_strategy(self):

        return FixedSizeChunkStrategy(
        chunk_size=settings.CHUNK_SIZE,
    )


    def _create_chunker(self):

        return DocumentChunker(
        strategy=self.chunk_strategy,
        overlap_size=settings.CHUNK_OVERLAP,
    )

    # ---------------------------------------------------------
# Document Processing
# ---------------------------------------------------------

    def _create_document_processing_service(self):

        return DocumentProcessingService(
        chunker=self.chunker,
        embedder=self.embedder,
        faiss_store=self.faiss_store,
        vector_search=self.vector_search,
    
    )

    # ---------------------------------------------------------
# LLM
# ---------------------------------------------------------

    def _create_llm_client(self):

        return OllamaClient(
        model=settings.OLLAMA_MODEL,
    )


    def _create_generator(self):

        return ResponseGenerator(
        self.client,
    )


    def _create_parser(self):

        return ResponseParser()
    
    # ---------------------------------------------------------
    # Retrieval
    # ---------------------------------------------------------
    def _create_retriever(self):

        return Retriever(
        self.embedding_model,
        self.vector_search,
    )
    

    # ---------------------------------------------------------
    # Services
    # ---------------------------------------------------------

    def _create_qa_service(self):

        return QAService(
            self.retriever,
            self.generator,
            self.parser,
        )

    def _create_summary_service(self):

        return SummaryService(
            self.retriever,
            self.generator,
            self.parser,
        )

    def _create_compare_service(self):

        return CompareService(
            self.generator,
            self.parser,
        )

    def _create_keyword_service(self):

        return KeywordService(
            self.retriever,
            self.generator,
            self.parser,
        )

    def _create_insight_service(self):

        return InsightService(
            self.retriever,
            self.generator,
            self.parser,
        )