import requests

url = "http://localhost:11434/api/generate"

system_prompt = """
You are Kenjong, a local AI assistant.

Your role:
- Help me learn Python
- Help me build an offline AI system
- Explain things step-by-step
- Prioritize practical learning
- Be concise but thorough
"""

print("Kenjong initialized.")
print("Type 'exit' to quit.\n")

conversation_history = ""

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Kenjong shutting down.")
        break

    full_prompt = f"""
{system_prompt}

Conversation so far:
{conversation_history}

User: {user_input}
Kenjong:
"""

    payload = {
        "model": "qwen3:8b",
        "prompt": full_prompt,
        "stream": False
    }

    response = requests.post(url, json=payload)
    reply = response.json()["response"]

    print("\nKenjong:", reply, "\n")

    conversation_history += f"\nUser: {user_input}\nKenjong: {reply}"