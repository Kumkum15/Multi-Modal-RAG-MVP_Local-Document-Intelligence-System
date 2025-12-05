import faiss
import json

from sentence_transformers import SentenceTransformer
EMBEDDER = SentenceTransformer("all-MiniLM-L6-v2")

def load_index(index_path, meta_path):
    index = faiss.read_index(index_path)
    with open(meta_path, "r", encoding="utf-8") as f:
        meta = json.load(f)
    return index, meta

def search(index, meta, query, top_k=5):
    q_emb = EMBEDDER.encode([query], convert_to_numpy=True)
    D, I = index.search(q_emb, top_k)
    results = []
    for score, idx in zip(D[0], I[0]):
        item = meta[idx]
        
        # If old string chunk sneaks in, convert to dict
        if isinstance(item, str):
            item = {"content": item}
            results.append({
                "score": float(score),
                "meta": item
            })
        
    return results
