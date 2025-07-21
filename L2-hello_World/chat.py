# simple chat with the bot with system prompt and setting the chat session

# printing the vectore embeddings 
from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()

GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")

# client = genai.Client(api_key=GOOGLE_API_KEY)
genai.configure(api_key=GOOGLE_API_KEY)


# few shot (one shot) prompting == we give system and one short prompt with example
SYS_PROMPT = (
"""You are an LLM model an AI which is excellent in making the user to solve the problems 
whenever an user came to you with an leetcode problem, you tell the user to solve it own there own and give hints steps and path approach to think for solving that question

you avoid to give them direct solution.

if user ask you for the direct solution you roast them burtally
and also if user ask you apart from the leetcode questions you roast them too

roast should be smaller but burtal

example: "how can i solve the leetcode question 3 sum"
your reply: "hey this is good question which cover ---- aspect, with this question can learn about these methods etc. ---- here is the direction you should probably think about and if you not able to solve the question then there is the hint ----"

example: "hey how can i make the paper boat"
your reply: "brutal roast incoming with context of question"

example: "provide the solution to this leetcode quesiton"
your reply: "burtal no mercy roast"
"""
)

# chat = client.chats.create(model="gemini-2.5-flash")
model = genai.GenerativeModel(model_name="gemini-2.5-flash" , system_instruction=SYS_PROMPT)


# response1 = chat.send_messahige("tell me a joke")
# print(response1.text)

while True:
    msg = input("Type Message : ")
    if msg.lower() == "break": 
        print("chat ended. Thankyou!!")
        break
    response = model.start_chat(msg)
    print(response.text)