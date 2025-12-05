
def chunk_text(text, chunk_size=500, overlap=50):
    """Chunk long text safely without storing huge chunks in memory."""
    
    if not text:
        return []
    
    chunks = []
    start = 0
    text_length = len(text)

    while start < text_length:
        end = min(start + chunk_size, text_length)
        chunk = text[start:end]
        chunks.append(chunk)
        start = end - overlap if end - overlap > start else end

    return chunks


def make_chunks_from_pages(pages, chunk_size=500, overlap=50):
    """Process pages one-by-one instead of merging everything."""
    all_chunks = []

    for page in pages:
        text = page.get("text", "")
        if not text:
            continue

        page_chunks = chunk_text(text, chunk_size, overlap)
        all_chunks.extend(page_chunks)

    return all_chunks