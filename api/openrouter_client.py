import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


class OpenRouterClient:

    def __init__(self):
        self.client = OpenAI(
            api_key=os.getenv("OPENROUTER_API_KEY"),
            base_url="https://openrouter.ai/api/v1"
        )

    def connect(self):
        print("[✓] Connected To OpenRouter")

    def generate(self, prompt):

        response = self.client.chat.completions.create(
            model="qwen/qwen3-coder",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            max_tokens=500
        )

        return response.choices[0].message.content