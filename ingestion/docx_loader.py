"""
DOCX Loader

Loads Microsoft Word documents and converts them
into Document objects.
"""

import os
from datetime import datetime

from docx import Document as DOCXDocument

from ingestion.base_loader import BaseLoader
from models.document import Document
from utils.logger import get_logger
from utils.exceptions import (
    UnsupportedFileTypeError,
    EmptyDocumentError,
    DocumentLoadError,
)


logger = get_logger(__name__)


class DOCXLoader(BaseLoader):
    """
    Loader responsible for reading DOCX files.
    """

    def load(
        self,
        file_path: str,
    ) -> Document:
        """
        Load a DOCX document and return a Document object.
        """

        # ----------------------------
        # Validate file extension
        # ----------------------------

        if not file_path.lower().endswith(".docx"):

            logger.error(
                "Unsupported file type: %s",
                file_path,
            )

            raise UnsupportedFileTypeError(
                "Only DOCX files are supported."
            )

        # ----------------------------
        # Validate file existence
        # ----------------------------

        if not os.path.exists(file_path):

            logger.error(
                "File not found: %s",
                file_path,
            )

            raise FileNotFoundError(
                f"File not found: {file_path}"
            )

        # ----------------------------
        # Validate empty file
        # ----------------------------

        if os.path.getsize(file_path) == 0:

            logger.error(
                "Empty file: %s",
                file_path,
            )

            raise EmptyDocumentError(
                "Uploaded DOCX file is empty."
            )

        logger.info(
            "Opening DOCX: %s",
            file_path,
        )

        try:

            docx = DOCXDocument(
                file_path
            )

            # ----------------------------
            # Extract paragraphs
            # ----------------------------

            text_parts = []

            for paragraph in docx.paragraphs:

                text = paragraph.text.strip()

                if text:

                    text_parts.append(
                        text
                    )

            text = "\n\n".join(
                text_parts
            )

            # ----------------------------
            # Metadata
            # ----------------------------

            filename = os.path.basename(
                file_path
            )

            extension = os.path.splitext(
                filename
            )[1].lower()

            size = os.path.getsize(
                file_path
            )

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
                    filename,
                )

                raise EmptyDocumentError(
                    "No readable text found in the DOCX."
                )

            # ----------------------------
            # Create Document
            # ----------------------------

            document = Document(
                filename=filename,
                extension=extension,
                text=text,
                pages=0,
                size=size,
                created_at=created_at,
                modified_at=modified_at,
            )

            logger.info(
                "Successfully loaded '%s'",
                filename,
            )

            return document

        except (
            UnsupportedFileTypeError,
            EmptyDocumentError,
        ):

            raise

        except Exception as error:

            logger.exception(
                "Failed to load DOCX: %s",
                file_path,
            )

            raise DocumentLoadError(
                f"Unable to load DOCX: {str(error)}"
            ) from error