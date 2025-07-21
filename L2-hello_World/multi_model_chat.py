# In this we are going to create an multi model chat application where one model can think and analyse the input and then result came then other model validate that then after that this cycle continue till result is not get 
 
# using the gemini and open router (mistralai)

from dotenv import load_dotenv
import os
import json
from openai import OpenAI
import google.generativeai as genai

load_dotenv()

# SYSTEM_PROMPT
SYSTEM_PROMPT_OPEN = ("""
You are OPEN, an intelligent validation and decision-making agent.

Your role is to critically evaluate the previous reasoning steps provided by the GOOGLE agent.

[OPEN VALIDATE]
- Carefully review each step of the analysis and thought process.
- Determine if the logic, reasoning, and computations are accurate.
- If everything is correct, confirm and mark the reasoning as valid.
- If there are any flaws, identify them and provide a clear correction with an explanation.

Then proceed to:

[RESULT]
- If the reasoning is valid, generate and return the final answer.
- If corrections were needed, provide the revised and accurate answer along with an explanation.

Ensure that your output remains structured, precise, and easy to follow.
""")

SYSTEM_PROMPT_GOOGLE = ("""
You are a helpful AI assistant specialized in resolving user queries.

For each user input, follow a strict step-by-step reasoning process before providing the final answer.

Steps to follow in exact sequence:
1. "analyse" — Understand what the user is asking.
2. "think" — Begin logical reasoning to break down the problem.
3. "think" — Think again, refining or extending your reasoning.
4. Repeat "think" steps multiple times if necessary for multi-step logic.
5. "output" — Derive the initial result or answer.
6. "validate" — Confirm the correctness and logic of the derived result.
7. "result" — Summarize how the answer was calculated or decided.
8. "display" — Present the final formatted result to the user.

Rules:
1. Always perform only **one step at a time** and wait for the next input.
2. Strictly use the JSON output format:
   { "step": "string", "content": "string" }
3. Think carefully and analytically at every stage before moving forward.
                        
Important:
- Never wrap your JSON in markdown (like ```json).
- Never return multiple JSON blocks at once.
- Always return ONLY a single JSON object in this format:
  { "step": "string", "content": "string" }


Example 1:
Input: What is 2 + 2  
Output:  
{ "step": "analyse", "content": "Alright! The user is asking a basic arithmetic question involving addition." }  
{ "step": "think", "content": "To solve this, I should add the operands from left to right." }  
{ "step": "output", "content": "4" }  
{ "step": "validate", "content": "Yes, 4 is the correct result for 2 + 2." }  
{ "step": "result", "content": "2 + 2 equals 4, obtained by adding both numbers." }  
{ "step": "display", "content": "2 + 2 = 4" }

Example 2:
Input: What is 2 + 2 * 5 / 3  
Output:  
{ "step": "analyse", "content": "Alright! The user is asking a math question involving multiple arithmetic operations." }  
{ "step": "think", "content": "I need to follow the BODMAS rule: Brackets, Orders, Division, Multiplication, Addition, Subtraction." }  
{ "step": "validate", "content": "Correct. Applying BODMAS is the right approach." }  
{ "step": "think", "content": "First, perform 5 / 3 = 1.6666666667." }  
{ "step": "validate", "content": "Yes, division is performed first as per BODMAS." }  
{ "step": "think", "content": "Now compute 2 + 2 * 1.6666666667." }  
{ "step": "validate", "content": "That's accurate. Multiplication next." }  
{ "step": "think", "content": "2 * 1.6666666667 = 3.3333333334. Then, 2 + 3.3333333334 = 5.3333333334." }  
{ "step": "output", "content": "5.3333333334" }  
{ "step": "validate", "content": "All operations were correctly ordered and computed." }  
{ "step": "result", "content": "Final result is 5.3333333334, using correct operator precedence." }  
{ "step": "display", "content": "2 + 2 * 5 / 3 = 5.3333333334" }
"""
)


# load api keys 
GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")
OPEN_ROUTER_API_KEY = os.getenv("OPEN_ROUTER_API_KEY")

# Create Clients
google_client = genai.configure(api_key=GOOGLE_API_KEY)
open_client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPEN_ROUTER_API_KEY
)

# models
google_model = genai.GenerativeModel(model_name='gemini-2.5-flash', system_instruction=SYSTEM_PROMPT_GOOGLE)

# chat 
google_chat = google_model.start_chat()
messages= [{"role": "developer", "content": SYSTEM_PROMPT_OPEN}]
completion = open_client.chat.completions.create(
    model="mistralai/mistral-nemo:free",
    messages=messages
)


# while True chattttt

while True:
    msg = input("> ")
    
    if msg.lower() == "break":
        print("🤖 Chat ended. Thank you!")
        break
    
    google_response = google_chat.send_message(msg)
    print("---------Response Started---------")
    while True:

        print("---------Processing---------")

        raw = google_response.text.strip()

        # Remove outer double braces {{ ... }}
        if raw.startswith("{{") and raw.endswith("}}"):
            raw = raw[1:-1].strip()

        try:
            parsed = json.loads(raw)
            print(f"🧠 Gemini Step ➜ {parsed['step']}")
            print(f"✍️ Content ➜ {parsed['content']}")
        except Exception as e:
            print("❌ Error parsing JSON:", e)

        if parsed['step'] == "validate":
            # open router handle this step
            messages.append({"role": "user", "content": json.dumps(parsed)})
            completion = open_client.chat.completions.create(
            model="mistralai/mistral-nemo:free",
            messages=messages
            )
            open_response = completion.choices[0].message.content
            print("---------✅ Open_Router Validating---------")
            print(open_response)
            print("---------Validation Done---------")
            google_response = google_chat.send_message(open_response)

        if parsed['step'] == "display":
            break 

        google_response = google_chat.send_message(parsed['content'])
    
    print("---------Response Complete---------")