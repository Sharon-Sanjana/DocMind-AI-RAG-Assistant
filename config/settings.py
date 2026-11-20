"""
Application Settings

Central configuration for the entire DocMind-AI application.
All configurable values should be defined here.
"""

from pathlib import Path


class Settings:
    """
    Central application configuration.
    """

    # ==========================================================
    # PROJECT PATHS
    # ==========================================================

    BASE_DIR = Path(__file__).resolve().parent.parent

    DATA_DIR = BASE_DIR / "data"

    UPLOAD_DIR = DATA_DIR / "uploads"

    PROCESSED_DIR = DATA_DIR / "processed"

    CHUNK_DIR = DATA_DIR / "chunks"

    VECTOR_INDEX_DIR = BASE_DIR / "vector_index"

    LOG_DIR = BASE_DIR / "logs"

    ASSETS_DIR = BASE_DIR / "assets"

    # ==========================================================
    # FILE SETTINGS
    # ==========================================================

    MAX_FILE_SIZE = 20 * 1024 * 1024      # 20 MB

    SUPPORTED_EXTENSIONS = {
        ".pdf",
        ".docx",
        ".txt",
        ".md",
    }
    MIN_DOCUMENT_LENGTH = 20

    MAX_FILE_SIZE = 20 * 1024 * 1024

    # ==========================================================
    # CHUNKING SETTINGS
    # ==========================================================

    CHUNK_SIZE = 500

    CHUNK_OVERLAP = 100

    # ==========================================================
    # EMBEDDING SETTINGS
    # ==========================================================

    EMBEDDING_MODEL = "all-MiniLM-L6-v2"

    EMBEDDING_BATCH_SIZE = 32

    # ==========================================================
    # VECTOR SEARCH
    # ==========================================================

    TOP_K = 5

    SIMILARITY_THRESHOLD = 0.65

    # ==========================================================
    # LLM SETTINGS
    # ==========================================================

    OLLAMA_MODEL = "llama3.2:1b"

    TEMPERATURE = 0.3

    MAX_TOKENS = 1024

    # ==========================================================
    # LOGGING
    # ==========================================================

    LOG_LEVEL = "INFO"

    LOG_FILE = LOG_DIR / "app.log"

    # ==========================================================
    # DATABASE
    # ==========================================================

    DATABASE_NAME = "docmind.db"

    DATABASE_PATH = BASE_DIR / "database" / DATABASE_NAME

    FAISS_DIMENSION = 384
settings = Settings()