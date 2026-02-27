from gpt4all import GPT4All

model = GPT4All(
    model_name="Llama-3.2-3B-Instruct-Q4_0.gguf",
    model_path=r"C:/Users/shant/AppData/Local/nomic.ai/GPT4All/"
)

with model.chat_session():
    response = model.generate("What is Artificial Intelligence?")
    print(response)