
"""
Uploader UI

Handles document uploads and processing.
"""

from pathlib import Path
import streamlit as st

from config.settings import settings


class Uploader:

    SUPPORTED_EXTENSIONS = {
        ".pdf", ".docx", ".txt", ".md"
    }

    @staticmethod
    def render(container):

        st.subheader("Upload Your Documents")

        uploaded_files = st.file_uploader(
            "Choose your documents",
            type=["pdf", "docx", "txt", "md"],
            accept_multiple_files=True,
        )

        if not uploaded_files:
            return

        settings.UPLOAD_DIR.mkdir(
            parents=True,
            exist_ok=True,
        )

        for uploaded_file in uploaded_files:

            if uploaded_file.name in [
                doc["name"]
                for doc in st.session_state.uploaded_documents
            ]:
                continue

            extension = Path(
                uploaded_file.name
            ).suffix.lower()

            if extension not in Uploader.SUPPORTED_EXTENSIONS:
                st.warning("Unsupported file type.")
                continue

            file_path = settings.UPLOAD_DIR / uploaded_file.name

            with open(file_path, "wb") as file:
                file.write(uploaded_file.getbuffer())

            try:
                with st.spinner(
                    f"Processing {uploaded_file.name}..."
                ):
                    result = (
                        container.document_processing_service.process(
                            str(file_path)
                        )
                    )

                st.session_state.uploaded_documents.append({
                    "name": uploaded_file.name,
                    "document_id": result["document_id"],
                    "chunks": result["chunks"],
                    "status": result["status"],
                })

                st.success(
                    f"Successfully processed {uploaded_file.name}"
                )

                st.write(f"Chunks: {result['chunks']}")
                st.write(
                    f"Processing time: {result['processing_time']} seconds"
                )

                st.write(
                     "FAISS vectors:",
                    container.faiss_store.size()
                )

                st.write(
                    "Stored metadata chunks:",
                    len(container.vector_search.metadata)
                )

            except Exception as error:
                st.error(
                    f"Processing failed: {error}"
                )

        if st.session_state.uploaded_documents:

            st.subheader("Processed Documents")

            for document in st.session_state.uploaded_documents:
                st.write(
                    f"📄 {document['name']} "
                    f"({document['chunks']} chunks)"
                )
