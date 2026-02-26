from src.ingestion.pdf_loader import extract_text_from_pdf
from src.text_chunker import chunk_text
from src.embeddings import generate_embeddings
from src.vector_store import create_faiss_index
import numpy as np

file_path = "sample.pdf"

# Extract page-wise data
pages = extract_text_from_pdf(file_path)

all_chunks = []
chunk_metadata = []

# Chunk each page
for page in pages:
    chunks = chunk_text(page["text"], chunk_size=1500)  # bigger chunk

    for chunk in chunks:
        all_chunks.append(chunk)
        chunk_metadata.append({
            "page": page["page"],
            "text": chunk
        })

# Generate embeddings
embeddings = generate_embeddings(all_chunks)

# Create FAISS index
index = create_faiss_index(embeddings)

# Ask user question
query = input("Ask your question: ")

query_embedding = generate_embeddings([query])

# Top-K retrieval
k = 3  # retrieve top 3 chunks
distances, indices = index.search(np.array(query_embedding), k)

print("\nAnswer found (Top {} chunks):\n".format(k))

for idx in indices[0]:
    print("📄 Page:", chunk_metadata[idx]["page"])
    print(chunk_metadata[idx]["text"])
    print("\n---\n")