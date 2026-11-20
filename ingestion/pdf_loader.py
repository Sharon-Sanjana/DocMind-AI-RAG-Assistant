"""
PDF Loader

Loads PDF documents and converts them into
Document objects.
"""

import os
from datetime import datetime

import fitz  # PyMuPDF

from ingestion.base_loader import BaseLoader
from models.document import Document
from utils.logger import get_logger
from utils.exceptions import (
    UnsupportedFileTypeError,
    EmptyDocumentError,
    DocumentLoadError,
)

# Create a logger for this module
logger = get_logger(__name__)


class PDFLoader(BaseLoader):
    """
    Loader responsible for reading PDF files.
    """

    def load(self, file_path: str) -> Document:
        """
        Load a PDF document and return it as a Document object.

        Args:
            file_path (str):
                Path to the PDF file.

        Returns:
            Document:
                Parsed document containing extracted text and metadata.

        Raises:
            UnsupportedFileTypeError:
                If the uploaded file is not a PDF.

            FileNotFoundError:
                If the file does not exist.

            EmptyDocumentError:
                If the PDF contains no readable text.

            DocumentLoadError:
                If the PDF cannot be processed.
        """

        # ----------------------------
        # Validate file extension
        # ----------------------------
        if not file_path.lower().endswith(".pdf"):
            logger.error("Unsupported file type: %s", file_path)
            raise UnsupportedFileTypeError(
                "Only PDF files are supported."
            )

        # ----------------------------
        # Validate file existence
        # ----------------------------
        if not os.path.exists(file_path):
            logger.error("File not found: %s", file_path)
            raise FileNotFoundError(
                f"File not found: {file_path}"
            )

        # ----------------------------
        # Validate empty file
        # ----------------------------
        if os.path.getsize(file_path) == 0:
            logger.error("Empty file: %s", file_path)
            raise EmptyDocumentError(
                "Uploaded PDF is empty."
            )

        logger.info("Opening PDF: %s", file_path)

        try:

            with fitz.open(file_path) as pdf:

                # ----------------------------
                # Extract text
                # ----------------------------
                text_parts = []

                for page in pdf:
                    text_parts.append(page.get_text())

                text = "\n".join(text_parts)

                # ----------------------------
                # Metadata
                # ----------------------------
                filename = os.path.basename(file_path)

                extension = os.path.splitext(filename)[1]

                pages = len(pdf)

                size = os.path.getsize(file_path)

                created_at = datetime.fromtimestamp(
                    os.path.getctime(file_path)
                )

                modified_at = datetime.fromtimestamp(
                    os.path.getmtime(file_path)
                )

                # ----------------------------
                # Validate extracted text
                # ----------------------------
                if not text.strip():
                    logger.warning(
                        "No readable text found in '%s'",
                        filename
                    )

                    raise EmptyDocumentError(
                        "No readable text found in the PDF."
                    )

                # ----------------------------
                # Create Document
                # ----------------------------
                document = Document(
                    filename=filename,
                    extension=extension,
                    text=text,
                    pages=pages,
                    size=size,
                    created_at=created_at,
                    modified_at=modified_at,
                )

                logger.info(
                    "Successfully loaded '%s' (%d pages)",
                    filename,
                    pages,
                )

                return document

        except (UnsupportedFileTypeError, EmptyDocumentError):
            raise

        except Exception as e:

            logger.exception(
                "Failed to load PDF: %s",
                file_path,
            )

            raise DocumentLoadError(
                f"Unable to load PDF: {str(e)}"
            ) from e