import json
from pathlib import Path
from utils.pdf_utils import extract_pages_text, extract_images_from_pdf, ocr_images_to_text
from processors.chunker import make_chunks_from_pages

def run_ingest(pdf_path, out_file="data/chunks.json"):
    pages = extract_pages_text(pdf_path)
    images = extract_images_from_pdf(pdf_path, "data/images")
    ocrs = ocr_images_to_text(images)

    chunks = make_chunks_from_pages(pages)

    # Append OCR text as separate chunks
    for i, item in enumerate(ocrs):
        chunks.append({
            "page": f"OCR-{i+1}",
            "chunk_id": f"ocr_{i+1}",
            "content": f"[OCR IMAGE]\n{item['ocr']}"
        })

    Path("data").mkdir(exist_ok=True)
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(chunks, f, indent=2)

    print("Ingestion completed:", len(chunks))
