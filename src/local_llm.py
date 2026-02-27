from gpt4all import GPT4All

class LocalLLM:
    def __init__(self):
        self.model = GPT4All(
            model_name="Llama-3.2-3B-Instruct-Q4_0",
            model_path=r"C:\Users\shant\AppData\Local\nomic.ai\GPT4All",
            verbose=True
        )

    # This method must be indented at the same level as __init__
    def generate(self, context, question):
        prompt = f"""
Read the following context carefully and answer the question in a clear and detailed way.
Use only the information provided in the context. If the context does not provide enough information, respond that the answer is not available.

Context:
{context}

Question:
{question}

Answer:
"""
        with self.model.chat_session():
            response = self.model.generate(prompt, max_tokens=300)
        return response