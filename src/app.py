import streamlit as st
import json
from pathlib import Path
from utils.pdf_utils import extract_pages_text
from processors.chunker import make_chunks_from_pages
from embed_index import embed_texts, build_faiss_index, save_metadata
from retrieve import load_index, search
from generate import generate_answer
import tempfile

st.title("Multi-Modal RAG MVP (Local)")

uploaded = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded:
    temp = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    temp.write(uploaded.read())
    pdf_path = temp.name
    st.success("PDF Loaded")

    if st.button("Ingest & Build Index"):
        pages = extract_pages_text(pdf_path)
        chunks = make_chunks_from_pages(pages)

        Path("data").mkdir(exist_ok=True)
        with open("data/chunks.json", "w", encoding="utf-8") as f:
            json.dump(chunks, f, indent=2)

        st.info("Computing embeddings...")
        texts = chunks
        embeddings = embed_texts(texts)

        Path("models").mkdir(exist_ok=True)
        build_faiss_index(embeddings, "models/faiss_index.bin")
        save_metadata(chunks, "data/index_metadata.json")

        st.success("Index ready!")

query = st.text_input("Ask something about the document:")

if st.button("Get Answer") and query:
    index, meta = load_index("models/faiss_index.bin", "data/index_metadata.json")
    results = search(index, meta, query)

    answer = generate_answer(query, results)
    st.subheader("Answer")
    st.write(answer)