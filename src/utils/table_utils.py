import pdfplumber

def extract_tables(pdf_path: str):
    tables_all = []
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            tables = page.extract_tables()
            for t in tables:
                tables_all.append({"page": i+1, "table": t})
    return tables_all
