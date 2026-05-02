import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

class Summarizer:
    def __init__(self):
        self.models_to_try = [
            "openchat/openchat-7b:free",
            "nvidia/llama-nemotron-embed-vl-1b-v2:free",
            "nvidia/nemotron-3-super-120b-a12b:free"
        ]

    def summarize_text(self, text):
        for model in self.models_to_try:
            try:
                response = client.chat.completions.create(
                    model=model,
                    messages=[
                        {"role": "system", "content": "Create PowerPoint bullet points."},
                        {"role": "user", "content": f"Summarize into 5 concise bullet points:\n{text}"}
                    ]
                )
                print(f"Using model: {model}")
                return response.choices[0].message.content

            except Exception as e:
                print(f"Model failed: {model} | Error: {e}")
                continue

        raise Exception("All models failed. No free model available.")


if __name__ == "__main__":
    sample_text = """Artificial Intelligence (AI) is transforming industries across the
world. It enables machines to learn from data, make decisions, and
automate tasks.

Applications of AI include: - Healthcare (disease prediction) - Finance
(fraud detection) - Marketing (customer targeting) - Transportation
(self-driving cars)

The future of AI is expected to bring more automation, efficiency, and
innovation."""

    summarizer = Summarizer()
    summary = summarizer.summarize_text(sample_text)

    print("\n* **Summarized Text: **\n")
    print(summary)
   