# Data Indexing -> Chunking -> Embedding -> V db -> query embedding -> Pick top relevent chunk acc to query 
# Top chunks + query -> LLM -> Result

from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader # For pdf loader method/function in lang chain
from langchain_text_splitters import RecursiveCharacterTextSplitter # For Chunking method from langChain
from langchain_openai import OpenAIEmbeddings # for creating embeddings for OpenAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_qdrant import Qdrant
import pprint
import os

load_dotenv()

google_api = os.getenv("GOOGLE_API_KEY")

file_path = "./L4-RAG/JS_File_For_RAG_Practice.pdf"
loader = PyPDFLoader(file_path= file_path)
docs = loader.load() # Read File
# docs[0] Read File Page By Page
# print( "Docs[0] :- " ,docs[0])
# pprint.pp(docs[0].metadata)

# Chunking
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
)

split_docs = text_splitter.split_documents(documents=docs)

# Embeddings
# embedding_model = OpenAIEmbeddings(
#     model="text-embedding-3-large",
#     api_key="google_api", # if not specify then automatically fetch from env file
# )

embedding_model = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
    google_api_key=google_api
)

# with embedding_model create embeddings of split_docs and store in V db (Qdrant DB)

vector_store = Qdrant.from_documents(
    documents=split_docs,
    embedding=embedding_model,
    url="http://localhost:6333",
    collection_name="Learning_Vector_DB_Qdrant"
)

print("indexing of split_docs done")