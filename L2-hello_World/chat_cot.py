# simple chat with the bot with system prompt and setting the chat session

# printing the vectore embeddings 
from dotenv import load_dotenv
import os
import json
import google.generativeai as genai

load_dotenv()

GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")

# client = genai.Client(api_key=GOOGLE_API_KEY)
genai.configure(api_key=GOOGLE_API_KEY)

# chain of through (cot) prompting == "the model is encourage to break down the step and resoning before giving an out put"

# this is the type of the cot prompt
SYS_PROMPT = (
"""
    You are an helpfull AI assistant who is specialized in resolving user query.
    For the given user input, analyse the input and break down the problem step by step.

    The steps are you get a user input, you analyse, you think, you think again, and think for several times and then return the output with an explanation. 

    Follow the steps in sequence that is "analyse", "think", "output", "validate" and finally "result".

    Rules:
    1. Follow the strict JSON output as per schema.
    2. Always perform one step at a time and wait for the next input.
    3. Carefully analyse the user query,

    Output Format:
    {{ "step": "string", "content": "string" }}

    Example:
    Input: What is 2 + 2
    Output: {{ "step": "analyse", "content": "Alight! The user is interest in maths query and he is asking a basic arthematic operation" }}
    Output: {{ "step": "think", "content": "To perform this addition, I must go from left to right and add all the operands." }}
    Output: {{ "step": "output", "content": "4" }}
    Output: {{ "step": "validate", "content": "Seems like 4 is correct ans for 2 + 2" }}
    Output: {{ "step": "result", "content": "2 + 2 = 4 and this is calculated by adding all numbers" }}

    Example:
    Input: What is 2 + 2 * 5 / 3
    Output: {{ "step": "analyse", "content": "Alight! The user is interest in maths query and he is asking a basic arthematic operations" }}
    Output: {{ "step": "think", "content": "To perform this addition, I must use BODMAS rule" }}
    Output: {{ "step": "validate", "content": "Correct, using BODMAS is the right approach here" }}
    Output: {{ "step": "think", "content": "First I need to solve division that is 5 / 3 which gives 1.66666666667" }}
    Output: {{ "step": "validate", "content": "Correct, using BODMAS the division must be performed" }}
    Output: {{ "step": "think", "content": "Now as I have already solved 5 / 3 now the equation looks lik 2 + 2 * 1.6666666666667" }}
    Output: {{ "step": "validate", "content": "Yes, The new equation is absolutely correct" }}
    Output: {{ "step": "validate", "think": "The equation now is 2 + 3.33333333333" }}
    Output: {{ "step": "result", "think": "end result" }}
   

"""
)

# chat = client.chats.create(model="gemini-2.5-flash")
model = genai.GenerativeModel(model_name="gemini-2.5-flash" , system_instruction=SYS_PROMPT)

# create chat 
chat = model.start_chat()

# response1 = chat.send_message("tell me a joke")
# print(response1.text)

while True:
    msg = input("Type Message (or 'break' to exit): ")
    if msg.lower() == "break":
        print("Chat ended. Thank you!")
        break

    print("---------Response started---------")
    while True:
        print("---------Next Step---------")
        response = chat.send_message(msg)

        raw = response.text.strip()

        # Remove outer double braces {{ ... }}
        if raw.startswith("{{") and raw.endswith("}}"):
            raw = raw[1:-1].strip()

        # try except block for string to json
        try:
            parsed = json.loads(raw)
            print(f"Step ➜ {parsed['step']}")
            print(f"Content ➜ {parsed['content']}")
        except Exception as e:
            print("❌ Error parsing JSON:", e)

        # if parsed['step'] == "validate":
        #     # claude wil handle this validation step

        # print response of the 
        # print("parsed",parsed)
        print(response.text)
        if parsed['step'] == "result":
            break 

        chat.send_message(parsed['content'])

    print("---------Response Complete---------")


"""
MULTI MODEL

We can make multi model system by using the two different LLM model to work on single input under different steps 

example:
    In, above prompt we have some steps like THINK, ANALYSE, VALIDATE and RESULT
    if we give work of THINKING and ANALYSING to the GPT model but the VALIDATION is done by the CLAUDE then 
    there is two models which works on one single imput 
"""

