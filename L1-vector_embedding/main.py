""" 
This shows the vector embeddings as shown in the comment in the last 
This vectore embedding shows the relation and the actual meaning and connection of word in real life thorugh numbers
vector embedding preserve the meaning, realtion and connection b/w the words
"""
# printing the vectore embeddings 
import google.generativeai as genai
from google import genai
# print("genai module package : " , genai)
GOOGLE_API_KEY = "AIzaSyAHWbsWXv1_S3w6P8j10SCcnLHSUeAkGyk"

client = genai.Client(api_key=GOOGLE_API_KEY)
result = client.models.embed_content(
        model="gemini-embedding-001",
        contents="What is the meaning of life?")

print(result.embeddings)

"""
#[ContentEmbedding(
  values=[
    -0.022374554,
    -0.004560777,
    0.013309286,
    -0.0545072,
    -0.02090443,
    <... 3067 more items ...>,
  ]
)]
"""