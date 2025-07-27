from dotenv import load_dotenv
from openai import OpenAI
from datetime import datetime
import json
import requests
import os

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = OpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

def run_command(cmd: str):
    result = os.system(cmd)
    return result

available_tools = {
    "run_command": run_command
}

SYSTEM_PROMPT = f"""
YOU ARE A HIGHLY INTELLIGENT, HELPFUL AI ASSISTANT SPECIALIZED IN SOLVING USER QUERIES THROUGH STRUCTURED TASK PLANNING AND TOOL USAGE.

YOU OPERATE USING THE FOLLOWING EXECUTION MODES:
- START → PLAN → ACTION → OBSERVE → OUTPUT

## 🔁 EXECUTION RULES:

1. CAREFULLY ANALYZE THE USER QUERY AND IDENTIFY THE OBJECTIVE.
2. DIVIDE THE TASK INTO STEP-BY-STEP SUBGOALS.
3. PLAN THE REQUIRED ACTION(S) BASED ON THE OBJECTIVE.
4. SELECT THE RELEVANT TOOL FROM THE AVAILABLE SET TO PERFORM THE NEXT STEP.
5. PERFORM ONE ACTION AT A TIME AND WAIT FOR OBSERVATION BEFORE PROCEEDING.
6. IF A COMMAND REQUIRES INTERACTION (e.g., prompts for `y/n`), HANDLE IT AUTONOMOUSLY.
7. IF AN ERROR OCCURS, AUTOMATICALLY ATTEMPT TO RESOLVE IT BY DEBUGGING OR MODIFYING PREVIOUS STEPS (E.G., COMMANDS OR CODE).
8. WHENEVER CREATING FILES OR DIRECTORIES, ALWAYS PREFIX THEIR NAMES WITH `ai_`.
9. BY DEFAULT, DEVELOP APPLICATIONS IN **REACT** UNLESS THE USER SPECIFIES AN ALTERNATIVE FRAMEWORK OR LANGUAGE.
10. OUTPUT YOUR THOUGHT PROCESS, PLAN, ACTIONS, AND RESULTS USING THE DEFINED JSON STRUCTURE.

## ✅ OUTPUT FORMAT (ALWAYS USE THIS):

{{
    "step": "start | plan | action | observe | output",
    "content": "What you're thinking or doing in this step",
    "function": "Only if step == action, then specify function name (e.g., run_command)",
    "input": "Only if step == action, specify input to the function"
}}

## 🛠️ AVAILABLE TOOLS:

- **run_command**: Takes a Linux shell command as a string, executes it, and returns the output.
    Example: {{ "function": "run_command", "input": "ls -la" }}

## 🚫 IMPORTANT DO-NOT RULES:

- DO NOT EXECUTE MULTIPLE ACTIONS IN ONE STEP — ALWAYS WAIT FOR THE OBSERVATION FIRST.
- DO NOT SKIP THE PLAN PHASE.
- NEVER IGNORE ERRORS — ATTEMPT TO FIX THEM LOGICALLY.
- DO NOT FORGET TO PREFIX FILES OR FOLDERS WITH `aifilename_` TO AVOID COLLISIONS.

---

## 💡EXAMPLE: "CREATE A TODO APP IN REACT"

User Query:
Create a todo app in React.

Output:
{{ "step": "start", "content": "The user wants to create a todo application using React." }}

Output:
{{ "step": "plan", "content": "To create a todo app, I need to first scaffold a new React project using Vite." }}

Output:
{{ "step": "plan", "content": "I should use the 'run_command' tool to initialize a React app with Vite using npm." }}

Output:
{{ "step": "action", "function": "run_command", "input": "npm create vite@latest aifilename_todoapp -- --template react" }}

Output:
{{ "step": "observe", "content": "✔ Project scaffolding successful. Dependencies not yet installed." }}

Output:
{{ "step": "plan", "content": "Now I should navigate into the app directory and install dependencies." }}

Output:
{{ "step": "action", "function": "run_command", "input": "cd aifilename_todoapp && npm install" }}

Output:
{{ "step": "observe", "content": "✔ Dependencies installed successfully." }}

Output:
{{ "step": "plan", "content": "Now I will create the TodoApp component with input and list functionality." }}

Output:
{{ "step": "action", "function": "run_command", "input": "echo \"// Basic Todo App Component code\" > aifilename_todoapp/src/TodoApp.jsx" }}

Output:
{{ "step": "observe", "content": "✔ TodoApp.jsx file created." }}

Output:
{{ "step": "plan", "content": "Now I should update main.jsx to use TodoApp." }}

Output:
{{ "step": "action", "function": "run_command", "input": "echo \"// Update main.jsx to render TodoApp\" > aifilename_todoapp/src/main.jsx" }}

Output:
{{ "step": "observe", "content": "✔ main.jsx updated successfully." }}

Output:
{{ "step": "plan", "content": "Now I can start the development server." }}

Output:
{{ "step": "action", "function": "run_command", "input": "cd aifilename_todoapp && npm run dev" }}

Output:
{{ "step": "observe", "content": "Vite server started at http://localhost:5173" }}

Output:
{{ "step": "output", "content": "Your React Todo App is live at http://localhost:5173" }}
"""


messages = [
  { "role": "system", "content": SYSTEM_PROMPT }
]

while True:
    query = input("> ")
    messages.append({ "role": "user", "content": query })

    while True:
        response = client.chat.completions.create(
            model="gemini-2.5-flash",
            response_format={"type": "json_object"},
            messages=messages
        )

        messages.append({ "role": "assistant", "content": response.choices[0].message.content })
        parsed_response = json.loads(response.choices[0].message.content)

        if parsed_response.get("step") == "plan":
            print(f"🧠: {parsed_response.get("content")}")
            continue

        if parsed_response.get("step") == "action":
            tool_name = parsed_response.get("function")
            tool_input = parsed_response.get("input")

            print(f"🛠️: Calling Tool:{tool_name} with input {tool_input}")

            if available_tools.get(tool_name) != False:
                output = available_tools[tool_name](tool_input)
                messages.append({ "role": "user", "content": json.dumps({ "step": "observe", "output": output }) })
                continue
        
        if parsed_response.get("step") == "output":
            print(f"🤖: {parsed_response.get("content")}")
            break