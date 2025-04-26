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
