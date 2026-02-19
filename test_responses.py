from openai import OpenAI

from settings import GPT_BASE, GPT_KEY, GPT_CHAT_MODEL

client = OpenAI(
    api_key=GPT_KEY,
    base_url=GPT_BASE,
)

response = client.responses.create(
    model=GPT_CHAT_MODEL,
    input="Say hello in one sentence.",
)

print(response.output_text)
