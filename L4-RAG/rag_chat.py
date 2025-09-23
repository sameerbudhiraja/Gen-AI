from dotenv import load_dotenv
from langchain_qdrant import Qdrant
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from openai import OpenAI
import os

load_dotenv()

google_api = os.getenv("GOOGLE_API_KEY")

# get user Input
query = input("> ")

# Embedding Model
embedding_model = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
    google_api_key=google_api
)

# SetUp Connection with the Vector DataBase
vector_DB = Qdrant.from_existing_collection(
    embedding=embedding_model,
    url="http://localhost:6333",
    collection_name="Learning_Vector_DB_Qdrant"
)

# search in Vector DataBase
search_result = vector_DB.similarity_search(
    query=query
)

# get similarity 
# print("search Result (Similarity with user query) : ", search_result)

# context
context = "\n\n\n-----\n\n\n".join([f"page content : {result.page_content}\n Page Number: {result.metadata['page_label']}\n file location: {result.metadata['source']}" for result in search_result])

# SYS_PROMPT
SYSTEM_PROMPT = f"""
You are a helpful AI assistant that provides accurate answers based on the given context and the user query.

You should:
- Respond directly to the user's query using the context.
- Mention the **page number** and **file location** where the information was found to help the user refer back.

Context:
{context}
"""

# print("SYSTEM_PROMPT with context", SYSTEM_PROMPT )

# chat 
client = OpenAI(
    api_key=google_api,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    response_format={"type": "json_object"},
    messages=[
        { "role": "system", "content": SYSTEM_PROMPT },
        { "role": "user", "content": query },
    ]
)

print(" 🤖 response = ", response.choices[0].message.content)