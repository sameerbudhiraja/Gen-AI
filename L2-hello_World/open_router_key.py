from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

KEY = os.getenv("OPEN_ROUTER_API_KEY")

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key= KEY,
)

completion = client.chat.completions.create(
#   extra_headers={
#     "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
#     "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
#   },
#   extra_body={},
  model="mistralai/mistral-nemo:free",
  messages=[
    {
      "role": "user",
      "content": "what is 2 + 2"
    }
  ]
)

print(completion.choices[0].message.content)