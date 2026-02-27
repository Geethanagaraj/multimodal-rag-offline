from src.ingestion.pdf_loader import extract_text_from_pdf
from src.text_chunker import chunk_text
from src.embeddings import generate_embeddings
from src.vector_store import create_faiss_index
from src.local_llm import LocalLLM

import numpy as np

file_path = "sample.pdf"

# 1️⃣ Extract page-wise data
pages = extract_text_from_pdf(file_path)

all_chunks = []
chunk_metadata = []

# 2️⃣ Chunk each page
for page in pages:
    chunks = chunk_text(page["text"], chunk_size=1500)

    for chunk in chunks:
        all_chunks.append(chunk)
        chunk_metadata.append({
            "page": page["page"],
            "text": chunk
        })

# 3️⃣ Generate embeddings
embeddings = generate_embeddings(all_chunks)

# 4️⃣ Create FAISS index
index = create_faiss_index(embeddings)

# 5️⃣ Ask question
query = input("Ask your question: ")

query_embedding = generate_embeddings([query])

# 6️⃣ Retrieve Top-K chunks
k = 3
distances, indices = index.search(np.array(query_embedding), k)

retrieved_context = ""
retrieved_pages = set()

for idx in indices[0]:
    retrieved_context += chunk_metadata[idx]["text"] + "\n\n"
    retrieved_pages.add(chunk_metadata[idx]["page"])

# 7️⃣ Send to Local LLM
llm = LocalLLM()
final_answer = llm.generate(retrieved_context, query)

# 8️⃣ Display Answer with Citations
print("\n📄 Source Pages:", sorted(retrieved_pages))
print("\n🧠 Final Answer:\n")
print(final_answer)