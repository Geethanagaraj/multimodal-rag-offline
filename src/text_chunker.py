def chunk_text(text, chunk_size=1500):
    """
    Split text into chunks of approximately chunk_size characters.
    """
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i + chunk_size])
    return chunks