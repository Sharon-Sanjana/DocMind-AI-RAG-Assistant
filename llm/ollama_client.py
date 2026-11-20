
import ollama
import time

class OllamaClient:

    def __init__(self, model: str = "llama3"):
        self.model = model

    def generate(self, prompt: str) -> str:

        print("DEBUG: Prompt characters:", len(prompt))
        print("DEBUG: Sending request to Ollama...")

        start_time = time.time()

        response = ollama.chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            options={
                "num_ctx": 2048,
                "num_predict": 120,
                "temperature": 0.2,
            },
        )

        print(
            "DEBUG: Ollama generation time:",
            round(time.time() - start_time, 2),
            "seconds"
        )

        return response["message"]["content"]