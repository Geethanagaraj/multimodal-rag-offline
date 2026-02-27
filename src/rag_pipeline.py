from ingestion.pdf_loader import extract_text_from_pdf
from text_chunker import chunk_text
from embeddings import create_embeddings
from vector_store import find_most_similar
from local_llm import LocalLLM


def run_rag(pdf_path, question):
    # 1. Extract text
    text = extract_text_from_pdf(pdf_path)

    # 2. Chunk text
    chunks = chunk_text(text)

    # 3. Create embeddings
    embeddings = create_embeddings(chunks)

    # 4. Retrieve best chunk
    best_chunk, page_number = find_most_similar(
        question, chunks, embeddings
    )

    # 5. Generate answer using LLM
    llm = LocalLLM()
    answer = llm.generate(best_chunk, question)

    return answer, page_number