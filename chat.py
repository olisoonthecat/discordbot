from dotenv import load_dotenv
import openai
import os

load_dotenv("C_TOKEN")
key = os.getenv("C_TOKEN")

openai.api_key = key

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Can you help me with science hw?"},
        {"role": "assistant", "content": "Ok. :( "},
        {"role": "user", "content": "How do you crochet a cat"}
    ]
)

print(response.choices[0].message.content)