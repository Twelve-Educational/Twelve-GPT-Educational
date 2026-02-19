import openai
from settings import GPT_BASE, GPT_VERSION, GPT_KEY, GPT_CHAT_MODEL
# Use OpenAI API
openai.api_type = "azure"
openai.api_base = GPT_BASE
openai.api_version = GPT_VERSION
openai.api_key = GPT_KEY

response = openai.ChatCompletion.create(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        },
        {
            "role": "user",
            "content": "Who are you?",
        }
    ],
    max_tokens=4096,
    temperature=1.0,
    top_p=1.0,
    engine=GPT_CHAT_MODEL
)

print(response.choices[0].message.content)