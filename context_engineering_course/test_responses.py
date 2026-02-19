"""
Course starter: Responses API smoke test.

Purpose:
- Makes one simple chat-style request and prints the model response text.

Usage:
- Ensure `.streamlit/secrets.toml` is configured.
- Run: `python context_engineering_course/test_responses.py`
"""

from openai import OpenAI

from settings import GPT_BASE, GPT_KEY, GPT_CHAT_MODEL

client = OpenAI(
    api_key=GPT_KEY,
    base_url=GPT_BASE,
)

response = client.responses.create(
    model=GPT_CHAT_MODEL,
    input="What is context engineering?",
)

print(response.output_text)
