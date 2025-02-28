import os

from groq import Groq

api_key = "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"

client = Groq(api_key=api_key)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of fast language models",
        }
    ],
    model="llama-3.3-70b-versatile",
)

print(chat_completion.choices[0].message.content) 