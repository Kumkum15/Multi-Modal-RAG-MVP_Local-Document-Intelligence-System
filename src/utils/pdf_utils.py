import pdfplumber
from pdf2image import convert_from_path
from pathlib import Path
from .ocr_utils import ocr_image_to_text

def extract_pages_text(pdf_path: str):
    pages = []
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            text = page.extract_text() or ""
            pages.append({"page": i+1, "text": text})
    return pages

def extract_images_from_pdf(pdf_path: str, out_dir: str):
    Path(out_dir).mkdir(parents=True, exist_ok=True)
    pil_images = convert_from_path(pdf_path)
    saved = []
    for i, img in enumerate(pil_images):
        p = Path(out_dir) / f"page_{i+1}.png"
        img.save(p, "PNG")
        saved.append(str(p))
    return saved

def ocr_images_to_text(image_paths):
    results = []
    for p in image_paths:
        txt = ocr_image_to_text(p)
        results.append({"image_path": p, "ocr": txt})
    return results
