# DocMind-AI – AI-Powered Document Assistant

DocMind-AI is an AI-powered document assistant built using Python that allows users to upload PDF documents, summarize their content, and ask questions based on the information in those documents.

The application uses Retrieval-Augmented Generation (RAG) to retrieve relevant information from uploaded documents and generate context-aware answers using a Large Language Model (LLM).

## Features

- **PDF Upload:** Upload PDF documents through an interactive Streamlit interface.
- **Text Extraction:** Extract text from uploaded PDF files.
- **Text Chunking:** Divide extracted text into smaller chunks for efficient processing.
- **Semantic Embeddings:** Convert text chunks into numerical vector representations using Sentence Transformers.
- **Vector Search:** Store and retrieve relevant document chunks using FAISS.
- **Question Answering:** Ask questions about uploaded documents and receive context-aware answers.
- **Document Summarization:** Generate concise summaries of uploaded documents.
- **Local LLM Integration:** Use Ollama to generate answers and summaries.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | User interface |
| Sentence Transformers | Text embeddings |
| FAISS | Vector storage and similarity search |
| Ollama | Local LLM integration |
| RAG | Context-aware question answering |
| PDF Processing | Document text extraction |

## Project Architecture

1. **Document Ingestion:** The user uploads a PDF document.
2. **Text Extraction:** Text is extracted from the PDF.
3. **Preprocessing:** Extracted text is divided into smaller chunks.
4. **Embedding Generation:** Sentence Transformers converts chunks into embeddings.
5. **Vector Storage:** FAISS stores the embeddings for efficient similarity search.
6. **Retrieval:** When a user asks a question, the system retrieves relevant chunks.
7. **Response Generation:** Retrieved context is passed to the Ollama LLM to generate an answer.
8. **Summarization:** The application can also generate summaries of document content.

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Sharon-Sanjana/DocMind-AI-RAG-Assistant.git
cd DocMind-AI-RAG-Assistant
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install and configure Ollama

Download Ollama from:

https://ollama.com/

Pull the model used by the project:

```bash
ollama pull llama3.2:1b
```

Make sure Ollama is running before starting the application.

### 5. Run the application

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal to access DocMind-AI.

## Project Structure

```text
DocMind-AI/
│
├── app.py
├── config/
├── data/
├── docs/
├── embeddings/
├── ingestion/
├── llm/
├── models/
├── preprocessing/
├── prompts/
├── retrieval/
├── services/
├── tests/
├── ui/
├── utils/
├── vectorstore/
│
├── requirements.txt
├── README.md
└── .gitignore
```

## Key Concepts Demonstrated

- Retrieval-Augmented Generation (RAG)
- Natural Language Processing (NLP)
- Semantic Search
- Text Embeddings
- Vector Databases
- Large Language Models (LLMs)
- Document Processing
- Python Application Development

## Future Enhancements

- Support for additional document formats.
- Conversation history for document-based questions.
- Source references for retrieved answers.
- Improved document processing and response performance.

## Author

**Sharon Sanjana S**

GitHub: https://github.com/Sharon-Sanjana

---

*DocMind-AI demonstrates the integration of document processing, semantic search, vector databases, and Large Language Models to build an intelligent document assistant.*