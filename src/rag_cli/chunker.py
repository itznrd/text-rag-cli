def chunk_text(text: str, chunk_size: int = 500, overlap: int = 100) -> list[str]:
    """
    Splits input text into overlapping chunks using a sliding window algorithm.
    
    :param text: The raw text string to be sliced.
    :param chunk_size: Maximum character count per chunk.
    :param overlap: Character overlap between adjacent chunks.
    :return: A list of text chunk strings.
    """

    if not text or not text.strip():
        return []

    if overlap >= chunk_size:
        raise ValueError("Overlap must be less than chunk size.")

    chunks = []
    start = 0
    text_length = len(text)

    step = chunk_size - overlap

    while start < text_length:
        end = min(start + chunk_size, text_length)
        chunk = text[start:end]
        chunks.append(chunk)
        start += step
        
    return chunks