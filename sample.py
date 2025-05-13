import google.generativeai as genai
import time

# Your Gemini API key
genai.configure(api_key="AIzaSyBG-6uKuo3njRKiDdyp-MKUBNuFQqoIFpg")

# Initialize Gemini model
model = genai.GenerativeModel('gemini-1.5-flash-latest')

# Simple agent loop
def agent_loop(goal, max_steps=5):
    context = f"You are an autonomous AI agent. Your goal is: {goal}.\nThink step by step and take actions until the goal is met."
    history = []

    for step in range(max_steps):

        prompt = context + "\n\n" + "\n".join(history) + "\nWhat should be done next?"
        response = model.generate_content(prompt)
        output = response.text.strip()
        print("Agent Response:", output)

        history.append(f"Step {step+1}: {output}")

        if "DONE" in output.upper():
            print("Goal achieved.")
            break

        time.sleep(1)

if __name__ == "__main__":
    user_goal = input("What do you want the agent to do? ")
    agent_loop(user_goal)












































from phi.agent import Agent
from phi.model.google import GoogleGeminiChat
from phi.embedder.openai import OpenAIEmbedder
from phi.vectordb.lancedb import LanceDb, SearchType
from phi.knowledge.knowledge_base import KnowledgeBase
from phi.knowledge.document import Document

import pandas as pd
import os

# === CONFIG ===
EXCEL_PATH = "Final_personal_data.xls"
TEXT_COLUMN = "YourTextColumn"  # <- CHANGE THIS
LANCE_URI = "tmp/lancedb"
TABLE_NAME = "excel_kb"

# === STEP 1: Load Excel Sheet ===
df = pd.read_excel(EXCEL_PATH)

# Replace NaNs with empty string and cast all to string
docs = []
for i, row in df.iterrows():
    content = str(row[TEXT_COLUMN])
    if content.strip():
        docs.append(Document(content=content, metadata={"row": i}))

# === STEP 2: Create Knowledge Base ===
knowledge_base = KnowledgeBase(
    documents=docs,
    vector_db=LanceDb(
        table_name=TABLE_NAME,
        uri=LANCE_URI,
        search_type=SearchType.vector,
        embedder=OpenAIEmbedder(model="text-embedding-3-small"),
    ),
)

# Load embeddings and save to LanceDB (do once)
knowledge_base.load()

# === STEP 3: Create Gemini Agent with Knowledge ===
agent = Agent(
    model=GoogleGeminiChat(id="gemini-pro"),  # Use your Gemini setup here
    knowledge=knowledge_base,
    show_tool_calls=True,
    markdown=True,
)

# === STEP 4: Ask a Question ===
query = "How to solve issues related to bacterial leaf blight?"
agent.print_response(query, stream=True)
