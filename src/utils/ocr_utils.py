import pytesseract
from PIL import Image

def ocr_image_to_text(path: str):
    img = Image.open(path).convert('RGB')
    text = pytesseract.image_to_string(img)
    return text
