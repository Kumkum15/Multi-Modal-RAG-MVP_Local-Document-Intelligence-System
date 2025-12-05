Multi-Modal RAG MVP – Local Document Intelligence System
A lightweight, end-to-end multi-modal Retrieval-Augmented Generation pipeline capable of processing text, tables, and images from real-world PDFs — powered locally using Ollama (no API cost).

Project Overview

This project implements a Multi-Modal RAG (Retrieval-Augmented Generation) system designed to handle complex documents containing:

Text

Tables

Figures & charts

Scanned images

OCR-extracted content

It answers user questions by extracting and retrieving relevant sections from the document and generating context-grounded answers using an LLM.

The entire pipeline runs locally and does not require OpenAI API or paid keys.

Key Features

Feature	Description
Multi-modal ingestion	Extracts text, tables, images, OCR, metadata from PDFs
OCR Support	Uses Tesseract for scanned pages
Chunking	Smart semantic + structural chunking
Vector Embeddings	Uses Ollama embeddings (nomic-embed-text or similar)
Vector Store	FAISS-based retrieval
Query Engine	Retrieves top-k chunks from vector store
Local LLM	Uses Llama 3.1 / Mistral in Ollama for grounded QA
Streamlit UI	Clean interface for upload → question → answer
Source Citations	Each answer includes page-level references

System Architecture
PDF -> Multi-modal Extractor -> Chunker -> Embeddings -> Vector DB (FAISS) -> Query -> Retriever -> LLM -> Answer

📂 Project Structure
multi_modal_rag_mvp/
│── data/
│── embeddings/
│── src/
│   │── app.py              # Streamlit frontend
│   │── ingest.py           # PDF ingestion & OCR
│   │── chunk.py            # Chunk generation
│   │── embed_index.py      # Embedding + FAISS indexer
│   │── retrieve.py         # Retriever
│   │── answer.py           # Local LLM generation
│── requirements.txt
│── README.md

Tech Stack

Python 3.10+

Streamlit

PyMuPDF

Pytesseract (OCR)

FAISS

Ollama (Llama 3 / Mistral)

LangChain components (optional)

⚙️ Installation
1️ Install Python dependencies
pip install -r requirements.txt

2️ Install and run Ollama
winget install Ollama.Ollama
ollama run llama3

3️ Install Tesseract (if OCR required)

Windows installer:
https://github.com/UB-Mannheim/tesseract/wiki

▶️ Run the App
streamlit run src/app.py

Evaluation

This system has been tested for:

Text-only PDFs

PDFs with tables

Scanned-image PDFs

Mixed multi-modal documents

Accuracy is significantly improved due to chunk-aware retrieval and multimodal embeddings.

Author

Kumkum Hirani
Email: kumkumhirani.co@gmail.com