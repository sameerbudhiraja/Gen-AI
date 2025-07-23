# Multi model chat bot for leetcode named as leetforce
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
from openai import OpenAI
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# load api keys 
GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")
OPEN_ROUTER_API_KEY = os.getenv("OPEN_ROUTER_API_KEY")

# Create Clients
google_client = genai.configure(api_key=GOOGLE_API_KEY)
open_client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPEN_ROUTER_API_KEY
)

# SYSTEM_PROMPT
from sys_prompt._open_router_sys_prompt import SYSTEM_PROMPT_OPEN
from sys_prompt._gemini_sys_prompt import SYSTEM_PROMPT_GOOGLE


# fastApi app for api (like express)
app = FastAPI()

# cors 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # your React frontend's origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# pyDantic BaseModel Define message 
class ChatRequest(BaseModel):
    message: str  # message should be in string

# static page welcome page 
@app.get("/")
def read_root():
    return {"message": "Multi-model chatbot API is running!"}

# chat apis
@app.post("/chat")
def chat(request: ChatRequest):
    # google model and chat
    google_model = genai.GenerativeModel(model_name='gemini-2.5-flash', system_instruction=SYSTEM_PROMPT_GOOGLE)
    google_chat = google_model.start_chat()
    
    # Open_Router model and chat
    messages= [{"role": "developer", "content": SYSTEM_PROMPT_OPEN}]
    completion = open_client.chat.completions.create(
        model="mistralai/mistral-nemo:free",
        messages=messages
    )

    # get message from the request
    msg = request.message

    # get initial res from google chat 
    google_response = google_chat.send_message(msg)

    print("<----------------Response Started---------------->")
    # while True:
    while True: 

        print("Processing---------------->")

        raw = google_response.text.strip()

        # Remove outer double braces {{ ... }}
        if raw.startswith("{{") and raw.endswith("}}"):
            raw = raw[1:-1].strip()

        try:
            parsed = json.loads(raw)
            # print(f"🧠 Gemini Step ➜ {parsed['step']}")
            # print(f"✍️ Content ➜ {parsed['content']}")
        except Exception as e:
            return{"error" : "Failed to parse GEMINI response"}

        # __validation__handler__ from open router
        if parsed['step'] == "validate":
                # open router handle this step
                messages.append({"role": "user", "content": json.dumps(parsed)})
                completion = open_client.chat.completions.create(
                model="mistralai/mistral-nemo:free",
                messages=messages
                )
                open_response = completion.choices[0].message.content
                print("Open_Router Validating--------->")
                print(open_response)
                print("Validation Done--------->")
                google_response = google_chat.send_message(open_response)
                continue

        # display response to end user 
        if parsed['step'] == "display":
            print("response Print" , parsed['content'])
            return {"response": parsed['content']}

        # repeat till final result (if not display)
        google_response = google_chat.send_message(parsed['content'])

        print("<----------------Response Complete---------------->")